#!/usr/bin/env python3
"""
足球泊松分布概率计算器 / Football Poisson Distribution Probability Calculator

用法 / Usage:
  python3 poisson-calculator.py <lambda_home> <lambda_away> [<handicap>]

示例 / Examples:
  # 不让球
  python3 poisson-calculator.py 2.5 0.4

  # 让球 -2（主队让2球）
  python3 poisson-calculator.py 2.5 0.4 -2

  # 让球 +1（主队受让1球）
  python3 poisson-calculator.py 2.5 0.4 1

输出：
  - 每个比分概率（Top 10）
  - 胜/平/负概率
  - 让球胜/平/负概率（如指定让球数）
  - 总进球概率
  - 期望值计算（需配合赔率手动输入）
"""

import sys
import math
from typing import Dict, Tuple, List


def poisson(k: int, lam: float) -> float:
    """泊松分布概率 P(X=k) = (λ^k × e^(-λ)) / k!"""
    return (lam ** k) * math.exp(-lam) / math.factorial(k)


def calc_score_matrix(lam_home: float, lam_away: float, max_goals: int = 10) -> Dict[Tuple[int, int], float]:
    """计算所有比分概率矩阵"""
    matrix = {}
    for i in range(max_goals + 1):
        for j in range(max_goals + 1):
            matrix[(i, j)] = poisson(i, lam_home) * poisson(j, lam_away)
    return matrix


def calc_outcomes(matrix: Dict[Tuple[int, int], float]) -> Tuple[float, float, float]:
    """计算胜/平/负概率"""
    win = draw = loss = 0.0
    for (i, j), prob in matrix.items():
        if i > j:
            win += prob
        elif i == j:
            draw += prob
        else:
            loss += prob
    return win, draw, loss


def calc_handicap_outcomes(matrix: Dict[Tuple[int, int], float], handicap: int) -> Tuple[float, float, float]:
    """计算让球胜/平/负概率

    handicap > 0: 主队受让（如 +1 = 主队让1球，即客队让1球）
    handicap < 0: 主队让球（如 -2 = 主队让2球）
    handicap = 0: 不让球
    """
    win = draw = loss = 0.0
    for (i, j), prob in matrix.items():
        adjusted_diff = (i - j) + handicap
        if adjusted_diff > 0:
            win += prob
        elif adjusted_diff == 0:
            draw += prob
        else:
            loss += prob
    return win, draw, loss


def calc_total_goals(matrix: Dict[Tuple[int, int], float]) -> Dict[int, float]:
    """计算总进球概率"""
    goals = {}
    for (i, j), prob in matrix.items():
        total = i + j
        if total not in goals:
            goals[total] = 0.0
        goals[total] += prob
    return goals


def top_scores(matrix: Dict[Tuple[int, int], float], n: int = 10) -> List[Tuple[Tuple[int, int], float]]:
    """返回概率最高的 n 个比分"""
    return sorted(matrix.items(), key=lambda x: -x[1])[:n]


def expected_value(prob: float, odds: float) -> float:
    """期望值 = (概率 × 赔率) - 1"""
    return prob * odds - 1


def ev_label(ev: float) -> str:
    """期望值标签"""
    if ev < 0:
        return "❌"
    elif ev < 0.05:
        return "⚠️观望"
    elif ev < 0.15:
        return "🟡轻仓"
    else:
        return "🟢正常投入"


def format_pct(p: float) -> str:
    return f"{p * 100:.1f}%"


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)

    lam_home = float(sys.argv[1])
    lam_away = float(sys.argv[2])
    handicap = int(sys.argv[3]) if len(sys.argv) > 3 else 0

    print(f"\n{'='*60}")
    print(f"⚽ 泊松分布概率计算 / Poisson Distribution Calculator")
    print(f"{'='*60}")
    print(f"📊 主队预期进球 λ₁ = {lam_home}")
    print(f"📊 客队预期进球 λ₂ = {lam_away}")
    if handicap != 0:
        print(f"📊 让球数 = {handicap}（{'主队让' + str(abs(handicap)) + '球' if handicap < 0 else '主队受让' + str(handicap) + '球'}）")
    print(f"{'='*60}\n")

    # 计算比分矩阵
    matrix = calc_score_matrix(lam_home, lam_away)

    # Top 10 比分
    print(f"🎯 比分概率 Top 10 / Top 10 Score Probabilities:")
    print(f"{'-'*40}")
    for (i, j), prob in top_scores(matrix, 10):
        bar = "█" * int(prob * 100)
        print(f"  {i}-{j:>2}  {format_pct(prob):>7}  {bar}")
    print()

    # 胜平负
    win, draw, loss = calc_outcomes(matrix)
    print(f"📈 胜平负概率 / Win-Draw-Loss:")
    print(f"{'-'*40}")
    print(f"  主队胜: {format_pct(win):>7}")
    print(f"  平局:   {format_pct(draw):>7}")
    print(f"  客队胜: {format_pct(loss):>7}")
    print(f"  合计:   {format_pct(win + draw + loss):>7}")
    print()

    # 让球胜平负
    if handicap != 0:
        h_win, h_draw, h_loss = calc_handicap_outcomes(matrix, handicap)
        print(f"📈 让球胜平负概率 / Handicap Outcomes ({handicap}):")
        print(f"{'-'*40}")
        print(f"  让胜: {format_pct(h_win):>7}")
        print(f"  让平: {format_pct(h_draw):>7}")
        print(f"  让负: {format_pct(h_loss):>7}")
        print(f"  合计: {format_pct(h_win + h_draw + h_loss):>7}")
        print()

    # 总进球
    goals = calc_total_goals(matrix)
    print(f"📈 总进球概率 / Total Goals:")
    print(f"{'-'*40}")
    for g in sorted(goals.keys()):
        if g <= 7:
            label = f"{g}球" if g < 7 else "7+球"
        else:
            continue
        print(f"  {label:>4}: {format_pct(goals[g]):>7}")
    if any(k > 7 for k in goals):
        over7 = sum(v for k, v in goals.items() if k > 7)
        print(f"  7+球: {format_pct(over7):>7}")
    print()

    # 期望值计算提示
    print(f"💡 期望值计算 / Expected Value:")
    print(f"{'-'*40}")
    print(f"  公式: E = (概率 × 赔率) - 1")
    print(f"  E < 0 → ❌不买 | E > 5% → 🟡轻仓 | E > 15% → 🟢正常投入")
    print()

    if handicap == 0:
        print(f"  请输入赔率计算期望值（留空跳过）:")
        try:
            win_odds = input(f"  主队胜赔率 [{format_pct(win)}]: ").strip()
            if win_odds:
                ev = expected_value(win, float(win_odds))
                print(f"    → E = {format_pct(ev)} {ev_label(ev)}")
            draw_odds = input(f"  平局赔率 [{format_pct(draw)}]: ").strip()
            if draw_odds:
                ev = expected_value(draw, float(draw_odds))
                print(f"    → E = {format_pct(ev)} {ev_label(ev)}")
            loss_odds = input(f"  客队胜赔率 [{format_pct(loss)}]: ").strip()
            if loss_odds:
                ev = expected_value(loss, float(loss_odds))
                print(f"    → E = {format_pct(ev)} {ev_label(ev)}")
        except (EOFError, ValueError):
            print()
    else:
        print(f"  请输入让球赔率计算期望值（留空跳过）:")
        try:
            h_win_odds = input(f"  让胜赔率 [{format_pct(h_win)}]: ").strip()
            if h_win_odds:
                ev = expected_value(h_win, float(h_win_odds))
                print(f"    → E = {format_pct(ev)} {ev_label(ev)}")
            h_draw_odds = input(f"  让平赔率 [{format_pct(h_draw)}]: ").strip()
            if h_draw_odds:
                ev = expected_value(h_draw, float(h_draw_odds))
                print(f"    → E = {format_pct(ev)} {ev_label(ev)}")
            h_loss_odds = input(f"  让负赔率 [{format_pct(h_loss)}]: ").strip()
            if h_loss_odds:
                ev = expected_value(h_loss, float(h_loss_odds))
                print(f"    → E = {format_pct(ev)} {ev_label(ev)}")
        except (EOFError, ValueError):
            print()

    print(f"\n{'='*60}")
    print(f"⚠️ 注意: 泊松分布是数学模型，基于预期进球估算概率。")
    print(f"   实际比赛受红牌、伤病、战术、天气等因素影响。")
    print(f"   概率仅供参考，不构成投注建议。")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
