#!/bin/bash
# Benchmark runner: spawn 15 independent code review sessions
# Usage: bash run_benchmark.sh

WORKSPACE="$HOME/.openclaw-autoclaw/workspace"
BENCHMARK_DIR="$WORKSPACE/memory/code-review-benchmark"

SKILL_PATH="$HOME/Desktop/project/skills/code-review-promax/SKILL.md"

# Read skill content
SKILL_CONTENT=$(cat "$SKILL_PATH")

run_review() {
    local commit_hash="$1"
    local run_num="$2"
    local commit_msg="$3"
    local diff_path="$BENCHMARK_DIR/${commit_hash}.diff"
    local diff_content=$(cat "$diff_path")
    
    local label="benchmark-${commit_hash}-run${run_num}"
    
    echo "[$(date +%H:%M:%S)] Starting $label ..."
    
    # Build the task - include SKILL.md content as system instructions
    TASK="你是一个代码审查专家。请严格按照以下 SKILL.md 中的指令执行代码审查。

\`\`\`markdown
${SKILL_CONTENT}
\`\`\`

---

现在请审查以下 commit（用中文输出报告）：

**Commit**: ${commit_hash}
**Message**: ${commit_msg}

\`\`\`diff
${diff_content}
\`\`\`

请输出完整的 Code Review 报告。"

    # Use sessions_spawn with mode=run for clean context each time
    # The report will be captured by the parent session
    echo "TASK_LENGTH: $(echo "$TASK" | wc -c) chars"
    echo "$TASK" > "$BENCHMARK_DIR/${commit_hash}/run_${run_num}_task.md"
    echo "Saved task to $BENCHMARK_DIR/${commit_hash}/run_${run_num}_task.md"
}

# Commits to test
COMMITS=(
    "435dcf6d|feat(开票): 联调企业搜索/开票/记录接口 + 关联证明上传与预览"
    "59214844|feat: 修改缺失AI标识bug&添加 该内容由AI生成"
    "d93e768e|feat(下载): 取消md2pdf和ppt下载"
)

# Generate all 15 tasks
for entry in "${COMMITS[@]}"; do
    IFS='|' read -r hash msg <<< "$entry"
    for run in 1 2 3 4 5; do
        run_review "$hash" "$run" "$msg"
    done
done

echo ""
echo "All 15 tasks prepared."
