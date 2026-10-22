#!/usr/bin/env python3
"""analyze_usage.py — 从 Claude Code 会话 JSONL 的 usage 字段还原真实上下文轨迹

Claude Code 每条 assistant 记录的 message.usage 携带官方计量数据：
  input_tokens + cache_creation_input_tokens + cache_read_input_tokens ≈ 本轮请求的上下文总输入
本脚本沿会话顺序提取这条轨迹，输出：
  - 上下文增长曲线（首/末/峰值/均值）
  - Compaction 检测：上下文骤降点（疑似自动压缩）与队列续接检测
  - 无效/异常 usage 统计（usage 覆盖率低时明确降级为估算建议）

与其他脚本不同，这里读的是**真实计量值**，输出不再加 "≈"。
它回答"上下文实际涨到多大了、什么位置发生了压缩"，七类归组仍请用 analyze_session.py。

用法:
  python3 analyze_usage.py <session.jsonl> [--json]
  python3 analyze_usage.py <session.jsonl> --window 200000   # 显示窗口占用百分比
适用格式:
  - Claude Code: ~/.claude/projects/<项目路径编码>/<sessionId>.jsonl
  - 其他平台: 若 assistant 行含 message.usage(input_tokens 等字段)亦可解析,
    否则报错并提示改用 analyze_session.py
输出: Markdown 轨迹报告(或 --json)
"""
import argparse
import json
import sys
from pathlib import Path


def _extract_usage(obj: dict):
    """从一行 JSON 提取 (usage_total_in, output_tokens)；非 assistant/无 usage 返回 None"""
    if obj.get("type") != "assistant":
        return None
    msg = obj.get("message")
    if not isinstance(msg, dict):
        return None
    u = msg.get("usage")
    if not isinstance(u, dict) or "input_tokens" not in u:
        return None
    total_in = (
        u.get("input_tokens", 0)
        + u.get("cache_read_input_tokens", 0)
        + u.get("cache_creation_input_tokens", 0)
    )
    return total_in, u.get("output_tokens", 0)


def analyze(path: Path, window: int):
    trace = []          # (lineno, context_in, output)
    usage_lines = 0
    assistant_lines = 0
    unparsed = 0

    with open(path, encoding="utf-8", errors="replace") as f:
        for lineno, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
            except json.JSONDecodeError:
                unparsed += 1
                continue
            if obj.get("type") == "assistant":
                assistant_lines += 1
            u = _extract_usage(obj)
            if u is None:
                continue
            usage_lines += 1
            # 去重:同一请求的流式分段会重复相同 usage,只保留变化点
            if trace and trace[-1][1] == u[0] and trace[-1][2] == u[1]:
                continue
            trace.append((lineno, u[0], u[1]))

    if not trace:
        return {
            "file": str(path),
            "format": "unknown",
            "error": "未找到任何 message.usage 数据点。该文件可能不是 Claude Code 会话记录,"
                     "或平台未记录 usage。请改用 analyze_session.py 走估算路线。",
            "assistant_lines": assistant_lines,
            "unparsed_lines": unparsed,
        }

    values = [v for _, v, _ in trace]
    peak = max(values)
    # Compaction 检测:较前值下降 ≥20% 视为骤降候选
    drops = []
    for k in range(1, len(trace)):
        prev_v, cur_v = trace[k - 1][1], trace[k][1]
        if prev_v > 0 and cur_v < prev_v * 0.8:
            drops.append({
                "line": trace[k][0],
                "from_tokens": prev_v,
                "to_tokens": cur_v,
                "drop_pct": round((prev_v - cur_v) / prev_v * 100, 1),
            })
    last_in = values[-1]
    return {
        "file": str(path),
        "format": "claude-code-usage",
        "window": window,
        "data_points": len(trace),
        "assistant_lines": assistant_lines,
        "usage_coverage_pct": round(len(trace) / assistant_lines * 100, 1) if assistant_lines else None,
        "context_first_tokens": values[0],
        "context_last_tokens": last_in,
        "context_peak_tokens": peak,
        "context_mean_tokens": round(sum(values) / len(values)),
        "window_peak_pct": round(peak / window * 100, 1) if window else None,
        "window_last_pct": round(last_in / window * 100, 1) if window else None,
        "compaction_drops": drops,
        "growth_last_minus_first": last_in - values[0],
        "unparsed_lines": unparsed,
    }


def to_markdown(r: dict) -> str:
    if r.get("format") == "unknown":
        lines = [f"# usage 轨迹分析(失败)", "",
                 f"- 文件:`{r['file']}`",
                 f"- {r['error']}",
                 f"- assistant 行数:{r.get('assistant_lines', 0)};未解析行:{r.get('unparsed_lines', 0)}"]
        return "\n".join(lines)

    lines = [f"# Claude Code usage 轨迹分析(真实计量)", "",
             f"- 文件:`{r['file']}`",
             f"- 数据点:{r['data_points']}(assistant {r['assistant_lines']} 行,覆盖率 {r['usage_coverage_pct']}%)",
             f"- 上下文输入:首 {r['context_first_tokens']:,} → 末 {r['context_last_tokens']:,} tokens(增长 {r['growth_last_minus_first']:+,})",
             f"- 峰值 {r['context_peak_tokens']:,}(窗口占用 {r['window_peak_pct']}%),均值 ≈{r['context_mean_tokens']:,}"]
    if r["compaction_drops"]:
        lines.append("")
        lines.append("**疑似 Compaction 骤降点**(较前值下降 ≥20%):")
        for d in r["compaction_drops"]:
            lines.append(f"- 第 {d['line']} 行:{d['from_tokens']:,} → {d['to_tokens']:,} tokens(降 {d['drop_pct']}%)")
    else:
        lines.append("")
        lines.append("未检测到上下文骤降点;若会话确实经历过压缩,该文件可能不含压缩边界,请结合 SKILL.md 人工核对。")
    lines.append("")
    lines.append("> 数据来自 message.usage 官方计量字段(input + cache_read + cache_creation),为真实值而非估算;"
                 "重复 usage 已按变化点去重。七类内容归组请配合 analyze_session.py 使用。")
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser(description="Claude Code 会话 usage 真实上下文轨迹分析")
    ap.add_argument("file", help="Claude Code 会话 JSONL(~/.claude/projects/<proj>/<sessionId>.jsonl)")
    ap.add_argument("--window", type=int, default=200000, help="上下文窗口大小(默认 200000)")
    ap.add_argument("--json", action="store_true", help="输出 JSON 而非 Markdown")
    args = ap.parse_args()
    path = Path(args.file)
    if not path.exists():
        print(f"错误:文件不存在:{path}", file=sys.stderr)
        sys.exit(1)
    result = analyze(path, args.window)
    print(json.dumps(result, ensure_ascii=False, indent=2) if args.json else to_markdown(result))


if __name__ == "__main__":
    main()
