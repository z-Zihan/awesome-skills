---
name: todo-list-promax
description: >
  个人待办事项永久存储、智能分类与定时提醒系统。
  自动从聊天消息中捕获待办（文字/图片/附件），解析时间与优先级，每日晚上9点推送未完成提醒。
  当用户消息包含以下触发词时激活：
  【录入】"TODO:"、"帮我记录一下"、"记录："、"待办："、"加个待办"、"记一下"、"别忘了"、"记得提醒我"、"回头要做"、"备忘"、"提醒我"
  【查询】"TODOLIST"、"待办列表"、"查看待办"、"看看待办"、"我有哪些待办"、"今天还有哪些未完成"、"还有什么没做"、"今天还要干嘛"、"今天的事做完了没"、"我的清单"
  NOT for: 项目管理、日历集成、多人协作、自动执行任务。
---

# todo-list — 个人待办事项系统 / Personal Todo System

## 目标 / Goal

为用户提供一个永久不丢失的待办事项管理系统。自动从聊天消息中捕获待办，智能解析时间和优先级，每日主动提醒未完成任务。
Provide a permanent, loss-proof todo management system. Auto-capture todos from chat, parse time & priority, proactively remind daily.

## 核心原则 / Core Principles

1. **零摩擦录入** / Zero-friction input — 用户随意发一句话或一张图，系统自动识别并存储
2. **永久不丢** / Permanent storage — 完成 = 标记 done，不等于删除。已删除 = 真正移除
3. **智能解析** / Smart parsing — 从自然语言自动提取时间、优先级、任务内容
4. **主动提醒** / Proactive reminders — 有截止时间的未完成任务，每天 21:00 主动推送
5. **按需响应** / On-demand response — 用户不问不回复，避免打扰

## 主要职责 / Responsibilities

### 1. 待办录入 / Todo Capture

**触发词 / Triggers:** `TODO:`、`帮我记录一下`、`记录：`、`待办：`、`加个待办`、`记一下`、`别忘了`、`记得提醒我`、`回头要做`、`备忘`、`提醒我`。消息中必须包含具体可执行的待办事项内容才能触发录入，纯日常陈述（如"我打算吃饭"）不触发。
**操作优先级**：如果同一条消息同时匹配录入和操作指令（如"删除这个 TODO: xxx"），优先执行操作指令（完成 > 删除 > 修改 > 录入），不创建重复待办。

**流程 / Flow:**
1. 从用户消息中提取任务内容
2. 如果消息包含图片/附件，下载并保存到 `workspace/todo-list/attachments/`
3. 解析时间要求（如有）
4. 解析优先级（如有）
5. 生成唯一 ID，写入 `workspace/todo-list/todos.json`
6. 回复用户确认（简洁一行：ID + 摘要 + 优先级 + 截止时间）

**时间解析 / Time Parsing:**
- 相对时间：今天、明天、后天、下周一、本周五、今晚、月底 等
- 绝对时间：5月20日、5-20、2026/5/20 等
- 模糊时间：尽快、ASAP、有空时 → 不设截止时间
- 精确到"天"，不支持具体小时
- 无法解析时 → 不设截止时间，不追问

**优先级解析 / Priority Parsing:**

| 级别 | 标记方式 | 自然语言线索 / Natural Language Cues |
|------|---------|--------------------------------------|
| P0 | `[P0]`、`⚠️` | "很紧急"、"立刻"、"马上"、"必须今天" / "urgent", "immediately", "must do today" |
| P1 | `[P1]` 或不标 | "重要"、"要做" / "important", default |
| P2 | `[P2]`、`⚡` | "急但不重要"、"顺手做" / "urgent but not important" |
| P3 | `[P3]`、`📌` | "有空再说"、"随手记一下"、"不急" / "no rush", "note to self" |

无法判断时默认 P1。/ Default to P1 when unclear.

**附件处理 / Attachment Handling:**
- 图片/文件：下载到 `workspace/todo-list/attachments/{todoId}_{原文件名}`
- json 中记录 `attachments: [{path, type}]`，type 枚举：`image`（图片）、`file`（其他文件）
- 同时有文字和图片时，两者都存储

### 2. 待办查询 / Todo Query

**触发词 / Triggers:** `TODOLIST`、`待办列表`、`查看待办`、`看看待办`、`我有哪些待办`、`今天还有哪些未完成`、`还有什么没做`、`今天还要干嘛`、`今天的事做完了没`、`我的清单`。

**查询模式 / Query Modes:**
- 无条件 → 所有未完成待办，按优先级排序
- 按时间 → 今天/本周/本月到期的未完成待办
- 按优先级 → 某个级别的待办（如"有哪些紧急的"）

**输出格式 / Output Format:**
```
📋 未完成待办（共 X 条）

🔴 P0 重要紧急
  #1 今天下班前提交周报  📅 今天

🟡 P1 重要不紧急
  #3 看完那篇论文  📅 下周一
  #5 整理桌面  （无截止时间）

🟢 P3 不急
  #7 买个充电线  📅 有空再说
```

### 3. 待办操作 / Todo Operations

**完成 / Complete:** "完成了 #1" 或 "TODO 完成 1" → 标记 `status: done`，记录 `completed_at`
**删除 / Delete:** "删除 #1" 或 "TODO 删除 1" → 回复待删除的 todo 内容摘要（ID + 内容 + 优先级），等用户确认后再移除。用户说"确认"或"删"时才执行
**修改 / Modify:** "#1 改成明天" → 更新对应字段，回复确认

### 4. 每日提醒 / Daily Reminder

- **时间 / Time:** 每天 21:00
- **配置方式 / Setup:** 使用 OpenClaw cron 功能创建每日提醒任务，或参考 `feishu-cron-reminder` skill 的配置方式。示例：每天 21:00 触发一个 session 读取 todos.json 并筛选未完成项推送。
- **筛选 / Filter:** 有 `due_time` 且 `status != done` 的待办
- **排序 / Sort:** 按优先级 P0 > P1 > P2 > P3
- **输出 / Output:** 紧凑列表，只推未完成的。末尾附操作指引：`回复"完成 #N"标记完成 · 回复"TODOLIST"查看全部 · 回复"#N 改成X"修改`
- **跳过 / Skip:** 如果没有需要提醒的待办，不推送

## 数据结构 / Data Schema

存储文件 / Storage: `workspace/todo-list/todos.json`

```json
{
  "version": 1,
  "todos": [
    {
      "id": 1,
      "content": "提交周报",
      "status": "pending",
      "priority": "P0",
      "due_time": "2026-05-16",
      "created_at": "2026-05-16T09:30:00+08:00",
      "completed_at": null,
      "attachments": [],
      "source_message": "TODO:今天下班前提交周报"
    }
  ]
}
```

字段说明 / Field Reference:
- `id`: 自增整数，不重复使用 / Auto-increment, never reuse
- `content`: 任务内容（纯文本摘要）/ Task content (text summary)
- `status`: `pending` | `done`
- `priority`: `P0` | `P1` | `P2` | `P3`
- `due_time`: 截止日期 YYYY-MM-DD，可为 null / Deadline date, nullable
- `created_at`: 创建时间 ISO 8601 / Creation time
- `completed_at`: 完成时间 ISO 8601，完成时填入 / Completion time, set when done
- `attachments`: `[{path, type}]` 附件列表 / Attachment list
- `source_message`: 原始消息内容 / Original message text

## 约束 / Constraints

- 存储路径：`workspace/todo-list/todos.json`
- 附件路径：`workspace/todo-list/attachments/`
- ID 自增，已删除的 ID 不重复使用
- 不修改用户消息原文
- 删除操作必须二次确认
- 时间解析精确到天
- `todos.json` 或目录不存在时自动创建
- 写入 json 前自动备份上一版本到 `todos.json.bak`
- 读取 json 解析失败时，尝试使用 `todos.json.bak` 恢复
