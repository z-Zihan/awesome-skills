---
name: skill-review-fix
description: >
  skill-review-pro 的子技能。读取评审报告中的修复清单，在用户逐条确认后对目标 Skill 执行修复。
  Sub-skill of skill-review-pro. Reads the fix checklist from the review report, executes fixes after per-item user confirmation.
  注意：此技能不独立使用，由 skill-review-pro 的修复阶段调用。
---

# skill-review-fix — Skill 修复执行器 / Skill Fix Executor

基于 skill-review-pro 评审报告中的修复清单，对目标 Skill 进行针对性修复。
Apply targeted fixes to the target Skill based on the fix checklist from skill-review-pro.

## 输入 / Input

从 skill-review-pro 的最终报告中提取修复清单。修复清单位于 `<!-- SKILL-REVIEW-FIX-LIST-START -->` 和 `<!-- SKILL-REVIEW-FIX-LIST-END -->` 标记之间，包含：
- 目标 Skill 名称和文件路径
- 问题列表（每条包含：问题描述、修复方案、影响维度、预估提分）
- 详细修复方案（每条包含：原文引用、修改后内容、文件位置）

如果上下文中没有修复清单标记，说明评审阶段还没有输出修复清单，应提示用户先完成评审。

## 核心原则 / Core Principles

**不主动执行，必须询问用户。** / **Never act without asking.**

每一条修复在执行前，必须：
1. 告诉用户要改什么 / Tell the user what will change
2. 展示修改前后的对比 / Show before/after diff
3. 等待用户确认 / Wait for user confirmation

用户响应：
- "修" / "fix" / "确认" → 执行这一条
- "都修" / "fix all" / "全部" → 展示所有修改的 before/after，确认后批量执行
- "跳过" / "skip" → 跳过这一条
- "只修 1、3" → 选择性执行
- "不修了" / "stop" → 终止修复流程

## 执行流程 / Workflow

### Step 1：解析修复清单 / Parse Fix Checklist

从修复清单标记中提取：
- 目标文件路径
- 修复项列表（问题、方案、位置）
- 详细修复方案（原文 → 修改后）

如果修复清单中没有"详细修复方案"部分，需要根据问题描述和修复方案自行生成具体的 before/after 内容。

### Step 2：确认修复范围 / Confirm Scope

展示修复清单摘要：

```markdown
## 即将执行的修复

**目标文件**：`<路径>`

| # | 问题摘要 | 修改位置 |
|---|----------|----------|
| 1 | ... | ... |

确认要开始修复吗？可以：
- 逐条确认：说"修"确认每一条
- 批量执行：说"都修"一次性全部执行
- 选择性执行：说"只修 1、3"
```

**⏸ 等待用户确认。**

### Step 3a：逐条模式 / Per-item Mode（默认）

对每条待修复项：
1. 展示**当前原文**（引用具体行或段落）
2. 展示**修改后内容**
3. 询问用户："这条修吗？（修/跳过/停止）"

用户确认后：
- 执行修改
- 标记状态为 ✅ 已修复

### Step 3b：批量模式 / Batch Mode（用户说"都修"）

1. 展示所有修改项的 before/after 对比
2. 询问用户："确认全部执行？"
3. 用户确认后批量执行所有修改

### Step 4：修复验证 / Fix Verification

所有修复执行完毕后：
1. 重新读取修改后的文件
2. 检查是否引入新问题（格式错误、中英不对应、逻辑矛盾）
3. 如发现新问题，告知用户并询问是否处理

### Step 5：更新评分 / Update Score

基于实际执行的修复，更新 Phase 1 评分：

```markdown
## 评分对比

| 维度 | 修复前 | 修复后 | 变化 |
|------|--------|--------|------|
| ... | X | X | +X |
| **Phase 1** | **XX** | **XX** | **+X** |
| **总计** | **XX** | **XX** | **+X** |
```

## 约束 / Constraints

- **绝不主动修改** — 每条必须经用户确认 / Never modify without confirmation
- **只修清单里的内容** — 不擅自扩大范围 / Only fix what's in the checklist
- **中英双语同步** — 修中文必须同步修英文 / Keep bilingual in sync
- **不动 frontmatter** — 除非清单明确指出 / Don't touch frontmatter unless specified
- **每条可回退** — 用户说"不对"则撤销上一条 / Every change is revertible

## 反模式 / Anti-patterns

- ❌ 不问就改 / Modifying without asking
- ❌ 改着改着扩大范围 / Scope creeping during fixes
- ❌ 只改中文不改英文 / Fixing Chinese but not English
- ❌ 改完后不验证 / Not verifying after fixes
- ❌ 忽略文件路径直接乱改 / Ignoring the target file path
