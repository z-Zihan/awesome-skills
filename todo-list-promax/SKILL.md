---
name: todo-list-promax
version: "1.1.0"
description: >
  个人待办事项永久存储、智能分类与定时提醒系统。
  自动从聊天消息中捕获待办（文字/图片/附件），解析时间与优先级，每日晚上9点推送未完成提醒。
  当用户消息包含以下触发词时激活：
  【录入】"TODO:"、"帮我记录一下"、"记录："、"待办："、"加个待办"、"记一下"、"别忘了"、"记得提醒我"、"回头要做"、"备忘"、"提醒我"
  【查询】"TODOLIST"、"待办列表"、"查看待办"、"看看待办"、"我有哪些待办"、"今天还有哪些未完成"、"还有什么没做"、"今天还要干嘛"、"今天的事做完了没"、"我的清单"
  NOT for: 项目管理、日历集成、多人协作、自动执行任务。
---

# todo-list — 个人待办事项系统

## 语言规则

**检测用户使用的语言，全程使用同一语言输出。** 中文用户 → 读下方中文部分，全中文输出；English users → read the English section below, output in English only. 技术术语（JSON、ID 等）保留原文即可。

---

# 中文版

## 目标

为用户提供一个永久不丢失的待办事项管理系统。自动从聊天消息中捕获待办，智能解析时间和优先级，每日主动提醒未完成任务。

## 核心原则

1. **零摩擦录入** — 用户随意发一句话或一张图，系统自动识别并存储
2. **永久不丢** — 完成 = 标记 done，不等于删除。已删除 = 真正移除
3. **智能解析** — 从自然语言自动提取时间、优先级、任务内容
4. **主动提醒** — 有截止时间的未完成任务，每天 21:00 主动推送
5. **按需响应** — 用户不问不回复，避免打扰

## 主要职责

### 1. 待办录入

**触发词：** `TODO:`、`帮我记录一下`、`记录：`、`待办：`、`加个待办`、`记一下`、`别忘了`、`记得提醒我`、`回头要做`、`备忘`、`提醒我`。消息中必须包含具体可执行的待办事项内容才能触发录入，纯日常陈述（如"我打算吃饭"）不触发。
**操作优先级**：如果同一条消息同时匹配录入和操作指令（如"删除这个 TODO: xxx"），优先执行操作指令（完成 > 删除 > 修改 > 录入），不创建重复待办。

**流程：**
1. 从用户消息中提取任务内容
2. 如果消息包含图片/附件，下载并保存到 `workspace/todo-list/attachments/`
3. 解析时间要求（如有）
4. 解析优先级（如有）
5. 生成唯一 ID，写入 `workspace/todo-list/todos.json`
6. 回复用户确认（简洁一行：ID + 摘要 + 优先级 + 截止时间）

**时间解析：**
- 相对时间：今天、明天、后天、下周一、本周五、今晚、月底 等
- 绝对时间：5月20日、5-20、2026/5/20 等
- 模糊时间：尽快、ASAP、有空时 → 不设截止时间
- 精确到"天"，不支持具体小时
- 无法解析时 → 不设截止时间，不追问

**优先级解析：**

| 级别 | 标记方式 | 自然语言线索 |
|------|---------|-------------|
| P0 | `[P0]`、`⚠️` | "很紧急"、"立刻"、"马上"、"必须今天" |
| P1 | `[P1]` 或不标 | "重要"、"要做"（默认） |
| P2 | `[P2]`、`⚡` | "急但不重要"、"顺手做" |
| P3 | `[P3]`、`📌` | "有空再说"、"随手记一下"、"不急" |

无法判断时默认 P1。

**附件处理：**
- 图片/文件：下载到 `workspace/todo-list/attachments/{todoId}_{原文件名}`
- json 中记录 `attachments: [{path, type}]`，type 枚举：`image`（图片）、`file`（其他文件）
- 同时有文字和图片时，两者都存储

### 2. 待办查询

**触发词：** `TODOLIST`、`待办列表`、`查看待办`、`看看待办`、`我有哪些待办`、`今天还有哪些未完成`、`还有什么没做`、`今天还要干嘛`、`今天的事做完了没`、`我的清单`。

**查询模式：**
- 无条件 → 所有未完成待办，按优先级排序
- 按时间 → 今天/本周/本月到期的未完成待办
- 按优先级 → 某个级别的待办（如"有哪些紧急的"）

**输出格式：**
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

### 3. 待办操作

**完成：** "完成了 #1" 或 "TODO 完成 1" → 标记 `status: done`，记录 `completed_at`
**删除：** "删除 #1" 或 "TODO 删除 1" → 回复待删除的 todo 内容摘要（ID + 内容 + 优先级），等用户确认后再移除。用户说"确认"或"删"时才执行
**修改：** "#1 改成明天" → 更新对应字段，回复确认

### 4. 每日提醒

- **时间：** 每天 21:00
- **配置方式：** 使用 OpenClaw cron 功能创建每日提醒任务，或参考 `feishu-cron-reminder` skill 的配置方式。示例：每天 21:00 触发一个 session 读取 todos.json 并筛选未完成项推送。
- **筛选：** 有 `due_time` 且 `status != done` 的待办
- **排序：** 按优先级 P0 > P1 > P2 > P3
- **输出：** 紧凑列表，只推未完成的。末尾附操作指引：`回复"完成 #N"标记完成 · 回复"TODOLIST"查看全部 · 回复"#N 改成X"修改`
- **跳过：** 如果没有需要提醒的待办，不推送

## 数据结构

存储文件：`workspace/todo-list/todos.json`

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

字段说明：
- `id`: 自增整数，不重复使用
- `content`: 任务内容（纯文本摘要）
- `status`: `pending` | `done`
- `priority`: `P0` | `P1` | `P2` | `P3`
- `due_time`: 截止日期 YYYY-MM-DD，可为 null
- `created_at`: 创建时间 ISO 8601
- `completed_at`: 完成时间 ISO 8601，完成时填入
- `attachments`: `[{path, type}]` 附件列表
- `source_message`: 原始消息内容

## 约束

- 存储路径：`workspace/todo-list/todos.json`
- 附件路径：`workspace/todo-list/attachments/`
- ID 自增，已删除的 ID 不重复使用
- 不修改用户消息原文
- 删除操作必须二次确认
- 时间解析精确到天
- `todos.json` 或目录不存在时自动创建
- 写入 json 前自动备份上一版本到 `todos.json.bak`
- 读取 json 解析失败时，尝试使用 `todos.json.bak` 恢复

---
---

# English Version

## Goal

Provide a permanent, loss-proof todo management system. Auto-capture todos from chat messages, parse time & priority intelligently, and proactively remind daily.

## Core Principles

1. **Zero-friction input** — User sends a casual message or image, system auto-identifies and stores
2. **Permanent storage** — Done = mark as done, not delete. Deleted = actually removed
3. **Smart parsing** — Auto-extract time, priority, and task content from natural language
4. **Proactive reminders** — Unfinished tasks with deadlines get a daily push at 21:00
5. **On-demand response** — Don't reply unless asked, avoid disturbance

## Responsibilities

### 1. Todo Capture

**Triggers:** `TODO:`, `帮我记录一下`, `记录：`, `待办：`, `加个待办`, `记一下`, `别忘了`, `记得提醒我`, `回头要做`, `备忘`, `提醒我`. The message must contain a specific, actionable todo item to trigger capture. Casual statements (e.g., "I'm going to eat") do not trigger.
**Operation priority:** If a single message matches both capture and operation triggers (e.g., "delete this TODO: xxx"), prioritize the operation (complete > delete > modify > capture), do not create a duplicate todo.

**Flow:**
1. Extract task content from user message
2. If message contains images/attachments, download and save to `workspace/todo-list/attachments/`
3. Parse time requirements (if any)
4. Parse priority (if any)
5. Generate unique ID, write to `workspace/todo-list/todos.json`
6. Reply with confirmation (concise one-liner: ID + summary + priority + deadline)

**Time Parsing:**
- Relative: today, tomorrow, day after tomorrow, next Monday, this Friday, tonight, end of month, etc.
- Absolute: May 20, 5-20, 2026/5/20, etc.
- Vague: ASAP, when free, whenever → no deadline set
- Precision: day-level only, no specific hours
- Unparseable → no deadline, no follow-up questions

**Priority Parsing:**

| Level | Markers | Natural Language Cues |
|-------|---------|-----------------------|
| P0 | `[P0]`, `⚠️` | "urgent", "immediately", "right now", "must do today" |
| P1 | `[P1]` or unmarked | "important", "need to do" (default) |
| P2 | `[P2]`, `⚡` | "urgent but not important", "quick one" |
| P3 | `[P3]`, `📌` | "no rush", "note to self", "whenever" |

Default to P1 when unclear.

**Attachment Handling:**
- Images/files: download to `workspace/todo-list/attachments/{todoId}_{original_filename}`
- Record in json: `attachments: [{path, type}]`, type enum: `image` (images), `file` (other files)
- When both text and images are present, store both

### 2. Todo Query

**Triggers:** `TODOLIST`, `待办列表`, `查看待办`, `看看待办`, `我有哪些待办`, `今天还有哪些未完成`, `还有什么没做`, `今天还要干嘛`, `今天的事做完了没`, `我的清单`.

**Query Modes:**
- No filter → all pending todos, sorted by priority
- By time → pending todos due today/this week/this month
- By priority → todos at a specific level (e.g., "what's urgent")

**Output Format:**
```
📋 Pending Todos (X total)

🔴 P0 Urgent & Important
  #1 Submit weekly report before end of day  📅 Today

🟡 P1 Important
  #3 Read that paper  📅 Next Monday
  #5 Clean up desk  (No deadline)

🟢 P3 No Rush
  #7 Buy a charging cable  📅 Whenever
```

### 3. Todo Operations

**Complete:** "完成了 #1" or "TODO 完成 1" → mark `status: done`, record `completed_at`
**Delete:** "删除 #1" or "TODO 删除 1" → reply with the todo's summary (ID + content + priority), wait for user confirmation before removing. Execute only when user says "确认" or "删"
**Modify:** "#1 改成明天" → update the corresponding field, reply with confirmation

### 4. Daily Reminder

- **Time:** Every day at 21:00
- **Setup:** Use OpenClaw cron to create a daily reminder task, or refer to the `feishu-cron-reminder` skill setup. Example: trigger a session at 21:00 daily that reads todos.json and filters pending items for push notification.
- **Filter:** Items with `due_time` and `status != done`
- **Sort:** By priority P0 > P1 > P2 > P3
- **Output:** Compact list, only pending items. Append action guide at end: `Reply "完成 #N" to mark done · Reply "TODOLIST" to view all · Reply "#N 改成X" to modify`
- **Skip:** If no reminders needed, don't push

## Data Schema

Storage file: `workspace/todo-list/todos.json`

```json
{
  "version": 1,
  "todos": [
    {
      "id": 1,
      "content": "Submit weekly report",
      "status": "pending",
      "priority": "P0",
      "due_time": "2026-05-16",
      "created_at": "2026-05-16T09:30:00+08:00",
      "completed_at": null,
      "attachments": [],
      "source_message": "TODO:Submit weekly report before end of day"
    }
  ]
}
```

Field Reference:
- `id`: Auto-increment integer, never reuse
- `content`: Task content (text summary)
- `status`: `pending` | `done`
- `priority`: `P0` | `P1` | `P2` | `P3`
- `due_time`: Deadline date YYYY-MM-DD, nullable
- `created_at`: Creation time ISO 8601
- `completed_at`: Completion time ISO 8601, set when done
- `attachments`: `[{path, type}]` attachment list
- `source_message`: Original message text

## Constraints

- Storage path: `workspace/todo-list/todos.json`
- Attachment path: `workspace/todo-list/attachments/`
- ID auto-increments, deleted IDs are never reused
- Do not modify original user messages
- Delete operations require secondary confirmation
- Time parsing precision: day-level only
- Auto-create `todos.json` and directories if they don't exist
- Auto-backup previous version to `todos.json.bak` before writing
- If json parsing fails, attempt recovery from `todos.json.bak`
