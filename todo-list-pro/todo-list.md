# todo-list — 个人待办事项系统 / Personal Todo System

## 目标 / Goal

为用户提供一个永久不丢失的待办事项管理系统。自动从聊天消息中捕获待办，智能解析时间和优先级，每日主动提醒未完成任务。

Provide a permanent, loss-proof todo management system. Auto-capture todos from chat messages, intelligently parse time and priority, and proactively remind about unfinished tasks daily.

## 核心原则 / Core Principles

1. **零摩擦录入** — 用户随意发一句话或一张图，系统自动识别并存储
2. **永久不丢** — 完成 = 标记 done，不等于删除。已删除 = 真正移除
3. **智能解析** — 从自然语言自动提取时间、优先级、任务内容
4. **主动提醒** — 有截止时间的未完成任务，每天 21:00 主动推送
5. **按需响应** — 用户不问不回复，避免打扰

## 主要职责 / Responsibilities

### 1. 待办录入 / Todo Capture

**触发词 / Triggers:** `TODO:`、`帮我记录一下`、`记录：`、`待办：`、`加个待办`、`记一下`、`别忘了`、`记得提醒我`、`回头要做`、`我打算`、`需要做`、`我得去`、`计划`、`安排`、`备忘`、`提醒我`，或消息中明确表达了"要做某事"的意图。

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

| 级别 | 标记方式 | 自然语言线索 |
|------|---------|-------------|
| P0 | `[P0]`、`⚠️` | "很紧急"、"立刻"、"马上"、"必须今天" |
| P1 | `[P1]` 或不标 | "重要"、"要做" / 默认 |
| P2 | `[P2]`、`⚡` | "急但不重要"、"顺手做" |
| P3 | `[P3]`、`📌` | "有空再说"、"随手记一下"、"不急" |

无法判断时默认 P1。

**附件处理 / Attachment Handling:**
- 图片/文件：下载到 `workspace/todo-list/attachments/{todoId}_{原文件名}`
- json 中记录 `attachments: [{path, type}]`
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

**完成:** "完成了 #1" 或 "TODO 完成 1" → 标记 `status: done`，记录 `completed_at`
**删除:** "删除 #1" 或 "TODO 删除 1" → 二次确认后从 json 中移除
**修改:** "#1 改成明天" → 更新对应字段，回复确认

### 4. 每日提醒 / Daily Reminder

- **时间:** 每天 21:00（通过 cron job 实现）
- **筛选:** 有 `due_time` 且 `status != done` 的待办
- **排序:** 按优先级 P0 > P1 > P2 > P3
- **输出:** 紧凑列表，只推未完成的，附操作指引
- **跳过:** 没有需要提醒的待办时，不推送

## 数据结构 / Data Schema

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

- `id`: 自增整数，已删除的 ID 不重复使用
- `content`: 任务内容（纯文本摘要）
- `status`: `pending` | `done`
- `priority`: `P0` | `P1` | `P2` | `P3`
- `due_time`: 截止日期 YYYY-MM-DD，可为 null
- `created_at`: 创建时间 ISO 8601
- `completed_at`: 完成时间 ISO 8601，完成时填入
- `attachments`: `[{path, type}]` 附件列表
- `source_message`: 原始消息内容

## 约束 / Constraints

- 存储路径：`workspace/todo-list/todos.json`
- 附件路径：`workspace/todo-list/attachments/`
- ID 自增，已删除的 ID 不重复使用
- 不修改用户消息原文
- 删除操作必须二次确认
- 时间解析精确到天
- `todos.json` 或目录不存在时自动创建
