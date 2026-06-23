# 🧰 Awesome Skills

[中文](#中文) | [English](#english)

---

<a id="中文"></a>

## 中文

通用 AI Agent 技能库。一个 skill 就是一份 `SKILL.md`，按需加载，开箱即用。

适用于任何支持读取本地 Markdown 作为系统指令的 AI Agent（OpenClaw、Claude Code、Codex、Cursor、Cline 等）。

### Skill 一览

### 🤖 code-review-ProMax — 高级代码审查 + 直接修复

多维度代码审查：需求完成度、回归风险、边界情况、上下游影响。输出结构化结论，含修复指令。支持变更意图识别、风险推导链、审查置信度。用户说"直接修复"时自动切换到修复模式（`fix/` 子 skill），逐条 apply 修复。

**触发词**：review 代码 / 帮我看看改动 / 代码有没有问题 / 直接修复 / fix

### 🏗️ fe-cli — 前端项目脚手架

一键创建规范化前端项目。支持 6 种类型：

| 子 Skill | 类型 | 触发词 |
|---|---|---|
| `web` | Web SPA | 官网、SPA |
| `admin` | 后台管理 | 后台、Admin |
| `h5` | 移动端 H5 | H5、移动端 |
| `electron` | 桌面应用 | Electron、桌面 |
| `ssr` | 服务端渲染 | SSR、Next.js |
| `miniapp` | 小程序 | 微信小程序 |

**技术栈**：pnpm / Sass / native fetch / Vite + TypeScript

### 📸 screenshot-to-prompt — 截图转实现 Prompt

输入页面截图，输出页面结构识别 + 可发给 coding agent 的实现 prompt。不是代码生成器，是截图翻译器。

**触发词**：帮我分析这个页面 / 生成实现 prompt / 截图转实现

### 📋 project-doc-analyst — 项目文档生成

深度阅读代码仓库，输出面向人类和 AI 的工程语义资产文档套件。按优先级分阶段生成：P0（项目总览 + 技术架构）→ P1（设计原因 + 产品分析 + 代码示例），支持可选文档和复杂专题深挖。

**触发词**：分析项目 / 生成文档 / 项目文档 / 代码分析 / 项目架构分析 / 架构图 / 调用链图 / 数据流图

### 🚀 project-onboarding — 项目接手指南

帮助有经验的开发者快速接手陌生项目。分三阶段输出：快速总览（10 分钟建地图）→ 深入专项 → 定向开发辅助。覆盖开发流程、工程规范、API 集成、组件体系、环境部署、团队协作等。支持前端 Web、后端服务、客户端（Electron/Tauri）、小程序、移动端。

**触发词**：接手项目 / 项目上手 / 快速上手 / 新人接手 / onboarding / 如何开发 / 项目怎么跑

### 🎯 skill-creator-ProMax — Skill 全流程创建器

从想法到 Skill 文件的全流程创建器。通过多轮对话帮助用户设计、打磨并生成高质量的 Agent Prompt，最终输出可直接使用的多平台 Skill 文件（OpenClaw、Claude Code、Cursor、Cline 等）。四阶段：定位 → 完整 Prompt → 迭代优化 → 文件生成。

**触发词**：生成 skill / 创建 skill / 设计 skill / 新建 skill / skill prompt / agent prompt

### 🔍 skill-review-pro — Skill 质量评审专家

模块化 Skill 评审 QA 系统。通过静态审查 + 行为测试 + 评分，对 Skill 进行专业评审。支持 5 种模式：完整评审、直接修复（轻量审查→修复报告）、意见验证（验证用户修复意见有效性）、修复执行、稳定性 Benchmark。基于 Policy Inheritance 架构，按 Skill 类型（engineering/cognition/workflow）匹配评审策略。

**触发词**：评审 skill / 测评 skill / 改进 skill / 验证修复意见 / skill 评分 / skill 质量检查

### 📕 rednote-creator — 小红书内容创作全流程

选题策划、文案写作、标题生成、多图封面生成、发布策略和一键发布。覆盖6大热门赛道（美妆护肤、穿搭时尚、减脂健身、美食探店、旅行攻略、家居收纳），内置赛道爆款规律、标题公式、封面策略和发布节奏。AI味黑名单确保文案说人话。支持 autoglm-generate-image 生图 + autoglm-browser-agent 一键发布。

**触发词**：发小红书 / 写小红书 / 小红书笔记 / rednote / 小红书文案 / 发笔记 / 发种草 / 发攻略

### 🧭 dev-mentor — 跨领域学习伴侣

帮助有经验的开发者学习不熟悉的领域，通过连续对话从零完成项目的完整生命周期。首批支持：后端开发（TypeScript/Go/Python）、数据库、服务器部署（Docker/Nginx/HTTPS/CI-CD）、Rust 系统编程。自动识别用户已有经验，不重复教，用类比教学。专业名词自带解释，代码使用最新技术栈和最佳实践。

**触发词**：学后端 / 学 Rust / 从零做项目 / 前端学后端 / 教我做项目 / 带我开发

### 📝 english-assessment — 交互式英语水平测评

大学英语水平（CEFR B1-C1）交互式快速测评。支持三种模式：默认测评（20-40题）、快速测评（约18题）、错题重测（10题）。12种题型覆盖词汇翻译、语法填空、选择题、句子改错、阅读理解、中译英翻译等。内容覆盖各专业领域。全程静默判分，完成后输出得分与弱项分析。支持错题集（本地持久化、自动清理）、错题重测、查看错题讲解。

**触发词**：开始英语测评 / 英语测试 / 测一下英语 / 快速测评 / 错题重测 / 看错题

### 🏆 worldcup-2026-assistant — 2026美加墨世界杯助手

2026 FIFA World Cup专属助手。四大核心功能：赛程查询（本地缓存+验证）、球队硬实力分析（历史数据+实时状态）、比赛预测（多维数据+置信度）、体彩选购指南（赔率+单关串关建议）。所有输出适配飞书消息格式，静态数据缓存至 `worldcup-data/`，动态数据实时查询。

**触发词**：世界杯 / 世界杯赛程 / 世界杯预测 / 世界杯分析 / 世界杯赔率 / 世界杯体彩 / worldcup / 美加墨 / 体彩指南 / 球队排名 / 竞彩 / 足彩

### 🏠 renovation-143m — 143㎡专属装修助手

基于固定户型（三室两厅两卫一厨一阳台改善型住宅）的长期装修决策助手。覆盖验房、风格研究、空间设计、收纳规划、水电灯光、家电材料、预算规划、避坑、AI生图模拟全流程。内置完整户型数据（13个空间尺寸估算+朝向分析）、25条避坑检查清单、小众实用设计库。所有分析绑定本户型，不提供泛通用建议。风格研究强制联网搜索，AI生图提示词必须包含户型约束。

**触发词**：143装修 / 专属装修助手 / 装修规划 / 验房 / 装修风格 / 收纳设计 / 水电规划 / 灯光规划 / 家电规划 / 材料选择 / 预算规划 / 装修避坑 / AI效果图

永久不丢失的待办事项管理。自动从聊天中捕获待办（文字/图片/附件），智能解析时间与优先级，每日晚上 9 点主动推送未完成提醒。支持四级优先级（P0-P3）、多种自然语言触发、完成/删除/修改操作。

**触发词**：TODO: / 帮我记录一下 / 记一下 / 别忘了 / 提醒我 / TODOLIST / 今天还有哪些 / 还有什么没做 / 待办列表

### 安装

**Git Clone：**

```bash
git clone https://github.com/z-Zihan/awesome-skills.git
```

**SKILL.md 格式规范：**

```yaml
---
name: skill-name          # 唯一标识，kebab-case
version: "1.0.0"         # 语义化版本号，每次修改 skill 时手动递增
homepage: https://...     # 仓库地址（可选）
description: >            # 触发词 + 功能描述 + NOT for 边界
  ...
---

# Skill 标题

prompt 正文...
```

- `name` — 唯一标识，也是 ClawHub 的 slug
- `version` — 语义化版本号（SemVer），每次修改 skill 内容时手动递增（patch → minor → major），方便对比本地和 ClawHub 版本
- `description` — 包含触发词和 NOT for 边界，是 skill 匹配的关键字段

将 `SKILL.md` 放到你的 Agent 能扫描到的目录：

| Agent | 安装路径 | 格式兼容 |
|---|---|---|
| OpenClaw | `~/.openclaw-autoclaw/skills/<name>/` | ✅ 原生 |
| Claude Code | `~/.claude/skills/<name>/` | ✅ 原生 |
| Codex | `~/.codex/skills/<name>/` | ✅ 原生 |
| Cursor | `.cursor/rules/<name>.md` | ✅ 原生 |
| Cline | `.clinerules` | ✅ 原生 |

> 💡 五大平台均使用相同的 SKILL.md 格式（YAML frontmatter + markdown prompt），无需任何转换，直接安装即可。

**一键安装（OpenClaw 用户）：**

```bash
openclaw skills install code-review-ProMax
openclaw skills install fe-cli
openclaw skills install screenshot-to-prompt
openclaw skills install project-doc-analyst
openclaw skills install project-onboarding
openclaw skills install skill-creator-ProMax
openclaw skills install skill-review-pro
openclaw skills install dev-mentor
openclaw skills install rednote-creator
openclaw skills install english-assessment
openclaw skills install worldcup-2026-assistant
openclaw skills install todo-list-promax
openclaw skills install renovation-143m
openclaw skills update --all
```

**手动安装（Claude Code / Codex 用户）：**

```bash
# Claude Code
ln -s ~/path/to/awesome-skills/todo-list-promax ~/.claude/skills/todo-list-promax

# Codex
ln -s ~/path/to/awesome-skills/todo-list-promax ~/.codex/skills/todo-list-promax
```

安装后重启 Agent 即可生效。

### 体系职责边界 / Skill Pipeline Architecture

本项目不是零散 Skill 的集合，而是一个有职责分层的设计体系。各 Skill 严格遵循单一职责，通过协作流程串联：

```
skill-creator-ProMax（生成）
        ↓
  skill-review-pro（测评验证）
        ↓ （不合格）
  修复循环（review-pro 内置）
        ↓ （合格）
  发布就绪
```

| Skill | 职责 | NOT for |
|-------|------|---------|
| **skill-creator-ProMax** | 结构设计 + 多平台文件生成 + 测评引导 | 测试 / 评分 / 修复 |
| **skill-review-pro** | 静态审查 + 行为测试（对抗/边界/歧义）+ 评分 + 修复 | 生成 / 设计 |
| **code-review-ProMax** | 代码变更风险审查 + 直接修复模式 | Skill 质量评审 |

**架构原则**：
- **各 Skill 不越界** — creator 不内置测试，reviewer 不生成 prompt
- **模块化按需加载** — 每个 Skill 只在需要时加载相关子模块
- **Stage 流程驱动** — 显式阶段 + 暂停确认 + 回退机制，避免一次性输出
- **修复闭环** — 评审发现问题 → 用户确认 → 执行修复 → 回归验证

### 版本管理

**版本号来源**：SKILL.md frontmatter 的 `version` 字段是唯一版本来源，CI 不生成版本号。

**更新流程**：
1. 修改 SKILL.md 内容
2. 手动 bump `version` 字段
3. push main → CI 自动校验版本号（必须大于 ClawHub 最新版）→ 发布

**版本号规则**：

| 改动类型 | 版本变化 | 示例 |
|---------|---------|------|
| 小修（修 bug、补细节） | patch +1 | 2.0.0 → 2.0.1 |
| 加功能、改流程 | minor +1 | 2.0.1 → 2.1.0 |
| 大重构、不兼容变更 | major +1 | 2.1.0 → 3.0.0 |

**忘了 bump 怎么办？** CI 会拦截并报错，提示版本号未增长，补上再推即可。

**全量发布**（所有 skill 重发一遍）：推 tag 触发，如 `git tag v2.0.0 && git push origin v2.0.0`

### 贡献

1. 创建文件夹 + `SKILL.md`，包含 YAML frontmatter
2. Push 到 `main`，自动发布

**SKILL.md 编写规范**：

- **必须中英双语**：所有内容同时包含中文和英文
- **Frontmatter description**：纯中文（ClawHub 卡片展示优先中文）
- **标题**：中文在前，英文在后，用 `/` 分隔，如 `## 标题 / English Title`
- **正文**：中文在先，英文跟在后面
- **每次修改后自查**：所有标题和段落都有双语、新增章节补了英文、description 保持纯中文

---

<a id="english"></a>

## English

A universal AI Agent skill library. Each skill is a single `SKILL.md` file — load on demand, zero config.

Compatible with any AI Agent that reads local Markdown as system instructions (OpenClaw, Claude Code, Codex, Cursor, Cline, etc.).

### Skills

### 🤖 code-review-ProMax — Advanced Code Review + Direct Fix

Multi-dimensional code review: requirement completion, regression risk, edge cases, upstream/downstream impact. Outputs structured report with fix instructions. When user says "直接修复"/"fix", auto-switches to fix mode (`fix/` sub-skill) to apply fixes one by one.

**Triggers**: review this code / check my changes / any issues / 直接修复 / fix

### 🏗️ fe-cli — Frontend Scaffolding

One-command project scaffolding with 6 templates:

| Sub-skill | Type | Triggers |
|---|---|---|
| `web` | Web SPA | website, SPA |
| `admin` | Dashboard | admin, dashboard |
| `h5` | Mobile H5 | mobile, H5 |
| `electron` | Desktop | Electron, desktop app |
| `ssr` | Server-side | SSR, Next.js |
| `miniapp` | Mini Program | WeChat miniapp |

**Stack**: pnpm / Sass / native fetch / Vite + TypeScript

### 📸 screenshot-to-prompt — Screenshot to Implementation Prompt

Input: page screenshot. Output: structured page analysis + an implementation prompt ready for any coding agent. Not a code generator — a screenshot translator.

**Triggers**: analyze this page / generate implementation prompt / screenshot to prompt

### 📋 project-doc-analyst — Project Documentation Generator

Deep-read the entire codebase and generate engineering semantic asset documentation for both humans and AI. Staged by priority: P0 (project overview + technical architecture) → P1 (design rationale + product analysis + code examples), with optional docs and deep dives.

**Triggers**: analyze project / generate docs / project documentation / code analysis / architecture analysis / architecture diagram

### 🚀 project-onboarding — Project Onboarding Guide

Help experienced developers quickly onboard onto unfamiliar projects. Three-stage output: quick overview (10-min project map) → deep dive → targeted dev assistance. Covers dev workflow, engineering standards, API integration, component system, environment/deployment, team collaboration. Supports frontend web, backend services, desktop apps (Electron/Tauri), mini programs, and mobile apps.

**Triggers**: onboard / project handover / quick start / how to develop / how to run

### 🎯 skill-creator-ProMax — Full-cycle Skill Creator

Full-cycle Skill creator from idea to file. Helps users design, iterate, and generate production-ready Agent Prompts through multi-turn conversation, then outputs multi-platform Skill files (OpenClaw, Claude Code, Cursor, Cline, etc.). Four stages: positioning → complete Prompt → iteration → file generation.

**Triggers**: create skill / design skill / new skill / skill prompt / agent prompt / system prompt

### 🔍 skill-review-pro — Expert Skill Reviewer

Modular Skill QA system. Evaluates Skills through static analysis + behavioral testing + scoring. Supports 5 modes: full review, direct fix (lightweight review → fix report), opinion validation (verify user-provided fix suggestions), fix execution, and stability benchmark. Uses Policy Inheritance architecture to match review strategies by Skill type (engineering/cognition/workflow).

**Triggers**: review skill / evaluate skill / improve skill / validate fix suggestions / skill score / skill quality check

### 📕 rednote-creator — Xiaohongshu Content Creation Pipeline

Topic planning, copywriting, title generation, multi-image cover generation, publishing strategy, and one-click publish. Covers 6 hot niches (beauty & skincare, fashion & OOTD, fitness & weight loss, food & restaurants, travel guides, home & organization) with built-in viral patterns, title formulas, cover strategies, and posting rhythms. AI-speak blacklist ensures human-like writing. Supports autoglm-generate-image for covers + autoglm-browser-agent for one-click publishing.

**Triggers**: 发小红书 / 写小红书 / rednote / 小红书笔记 / 小红书文案 / post to xiaohongshu / xiaohongshu post / rednote post

### 🧭 dev-mentor — Cross-Domain Learning Companion

Helps experienced developers learn unfamiliar domains by building a full project from zero to production via continuous conversation. First batch: backend (TypeScript/Go/Python), databases, server deployment (Docker/Nginx/HTTPS/CI-CD), Rust systems programming. Auto-detects existing skills, uses analogies from known domains, explains technical terms on first use.

**Triggers**: learn backend / learn Rust / build project from scratch / teach me to code

### 🏆 worldcup-2026-assistant — 2026 FIFA World Cup Assistant

Dedicated assistant for the 2026 FIFA World Cup. Four core features: schedule query (local cache + verification), team strength analysis (historical data + live player status), match prediction (multi-dimensional data + confidence levels), sports lottery guide (odds + single/parlay suggestions). All output formatted for Feishu messages. Static data cached in `worldcup-data/`, dynamic data queried live.

**Triggers**: 世界杯 / World Cup / worldcup / 美加墨 / 世界杯赛程 / 世界杯预测 / 世界杯分析 / 世界杯赔率 / 世界杯体彩 / 体彩指南 / 竞彩 / 足彩

### ✅ todo-list-promax — 个人待办事项系统

Permanent, loss-proof todo management. Auto-captures todos from chat (text/image/attachment), parses time & priority, pushes unfinished reminders daily at 9 PM. Supports 4 priority levels (P0-P3), natural language triggers, and complete/delete/modify operations.

**Triggers**: TODO: / 帮我记录一下 / remind me / 别忘了 / TODOLIST / what's left today / anything pending / show todos

### Installation

**Git Clone:**

```bash
git clone https://github.com/z-Zihan/awesome-skills.git
```

**SKILL.md Format:**

```yaml
---
name: skill-name          # Unique identifier, kebab-case
version: "1.0.0"         # SemVer, increment manually when modifying
homepage: https://...     # Repo URL (optional)
description: >            # Triggers + description + NOT for boundary
  ...
---

# Skill Title

Prompt body...
```

- `name` — Unique identifier, also used as ClawHub slug
- `version` — Semantic version (SemVer), increment manually when modifying skill content, to compare local vs ClawHub versions
- `description` — Contains trigger words and NOT for boundary, key field for skill matching

Place `SKILL.md` in your Agent's skill directory:

| Agent | Install Path | Format |
|---|---|---|
| OpenClaw | `~/.openclaw-autoclaw/skills/<name>/` | ✅ Native |
| Claude Code | `~/.claude/skills/<name>/` | ✅ Native |
| Codex | `~/.codex/skills/<name>/` | ✅ Native |
| Cursor | `.cursor/rules/<name>.md` | ✅ Native |
| Cline | `.clinerules` | ✅ Native |

> 💡 All five platforms share the same SKILL.md format (YAML frontmatter + markdown prompt) — zero conversion needed.

**ClawHub (OpenClaw users):**

```bash
openclaw skills install code-review-ProMax
openclaw skills install fe-cli
openclaw skills install screenshot-to-prompt
openclaw skills install project-doc-analyst
openclaw skills install project-onboarding
openclaw skills install skill-creator-ProMax
openclaw skills install skill-review-pro
openclaw skills install dev-mentor
openclaw skills install rednote-creator
openclaw skills install english-assessment
openclaw skills install worldcup-2026-assistant
openclaw skills install todo-list-promax
openclaw skills install renovation-143m
openclaw skills update --all
```

**Manual install (Claude Code / Codex):**

```bash
# Claude Code
ln -s ~/path/to/awesome-skills/todo-list-promax ~/.claude/skills/todo-list-promax

# Codex
ln -s ~/path/to/awesome-skills/todo-list-promax ~/.codex/skills/todo-list-promax
```

Restart your Agent after installing.

### Architecture

This is not a loose collection of Skills — it's a layered design system with clear responsibility boundaries:

```
skill-creator-ProMax (generate)
        ↓
  skill-review-pro (evaluate & verify)
        ↓ (fails)
  fix loop (built into review-pro)
        ↓ (passes)
  ready to publish
```

| Skill | Responsibility | NOT for |
|-------|---------------|---------|
| **skill-creator-ProMax** | Architecture design + multi-platform file generation + review guidance | Testing / Scoring / Fixing |
| **skill-review-pro** | Static review + behavioral testing (adversarial/boundary/ambiguity) + scoring + fixing | Generation / Design |
| **code-review-ProMax** | Code change risk review + direct fix mode | Skill quality evaluation |

**Principles**: No boundary crossing between Skills. Modular on-demand loading. Stage-driven workflow with explicit pause/rollback. Fix loop with regression verification.

### Versioning

**版本号来源**：SKILL.md frontmatter 的 `version` 字段是唯一版本来源，CI 不生成版本号。

**更新流程**：
1. 修改 SKILL.md 内容
2. 手动 bump `version` 字段
3. push main → CI 自动校验版本号（必须大于 ClawHub 最新版）→ 发布

**版本号规则**：

| 改动类型 | 版本变化 | 示例 |
|---------|---------|------|
| 小修（修 bug、补细节） | patch +1 | 2.0.0 → 2.0.1 |
| 加功能、改流程 | minor +1 | 2.0.1 → 2.1.0 |
| 大重构、不兼容变更 | major +1 | 2.1.0 → 3.0.0 |

**忘了 bump 怎么办？** CI 会拦截并报错，提示版本号未增长，补上再推即可。

**全量发布**（所有 skill 重发一遍）：推 tag 触发，如 `git tag v2.0.0 && git push origin v2.0.0`

### Contributing

1. Create a folder + `SKILL.md` with YAML frontmatter
2. Push to `main` — auto-published via GitHub Actions

**SKILL.md Writing Standards**：

- **Bilingual required**: All content must include both Chinese and English
- **Frontmatter description**: Chinese only (ClawHub card displays Chinese first)
- **Headings**: Chinese first, English after, separated by `/`, e.g. `## 标题 / English Title`
- **Body content**: Chinese first, English follows
- **Self-check after edits**: All headings and paragraphs are bilingual, new sections have English translations, description remains Chinese only
