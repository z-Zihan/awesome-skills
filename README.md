# 🧰 Awesome Skills

[English](#english) | [中文](#中文)

---

<a id="中文"></a>

## 中文

通用 AI Agent 技能库。一个 skill 就是一份 `SKILL.md`，按需加载，开箱即用。

适用于任何支持读取本地 Markdown 作为系统指令的 AI Agent（OpenClaw、Claude Desktop、Cursor、Cline 等）。

### 安装

**Git Clone：**

```bash
git clone https://github.com/z-Zihan/awesome-skills.git
```

将 `SKILL.md` 放到你的 Agent 能扫描到的目录：

| Agent | 配置方式 |
|---|---|
| OpenClaw | 软链接到 `~/.openclaw-autoclaw/skills/` |
| Claude Desktop | 在 `CLAUDE.md` 中引用文件路径 |
| Cursor | 在 `.cursorrules` 或项目 `.cursor/` 中配置 |
| Cline | 在 `.clinerules` 中引用 |

**ClawHub（OpenClaw 用户）：**

```bash
openclaw skills install deep-code-review
openclaw skills install fe-cli
openclaw skills install screenshot-to-prompt
openclaw skills update --all
```

### Skill 一览

#### 🤖 code-review — 代码审查

多维度代码审查：需求完成度、回归风险、边界情况、上下游影响。输出结构化结论，含可发给 AI agent 的修复指令。

**触发词**：review 代码 / 帮我看看改动 / 代码有没有问题 / 改动有没有风险

#### 🏗️ fe-cli — 前端项目脚手架

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

#### 📸 screenshot-to-prompt — 截图转实现 Prompt

输入页面截图，输出页面结构识别 + 可发给 coding agent 的实现 prompt。不是代码生成器，是截图翻译器。

**触发词**：帮我分析这个页面 / 生成实现 prompt / 截图转实现

### 版本管理

**日常开发（自动发布）：**

push 到 `main` 分支，GitHub Actions 自动检测 `SKILL.md` 变更并发布到 ClawHub，版本号自动递增，无需手动管理。

**正式发版（手动）：**

```bash
# 1. 更新 CHANGELOG.md（记录本次变更）
# 2. 打 tag 并推送
git tag v1.0.0
git push origin v1.0.0
# 3. GitHub Actions 自动用 tag 作为版本号发布到 ClawHub
```

Tag 命名规范：`v<major>.<minor>.<patch>`，例如 `v1.0.0`、`v1.1.0`、`v1.1.1`

### 贡献

1. 创建文件夹 + `SKILL.md`，包含 YAML frontmatter
2. Push 到 `main`，自动发布

---

<a id="english"></a>

## English

A universal AI Agent skill library. Each skill is a single `SKILL.md` file — load on demand, zero config.

Compatible with any AI Agent that reads local Markdown as system instructions (OpenClaw, Claude Desktop, Cursor, Cline, etc.).

### Installation

**Git Clone:**

```bash
git clone https://github.com/z-Zihan/awesome-skills.git
```

Place `SKILL.md` in your Agent's skill directory:

| Agent | Setup |
|---|---|
| OpenClaw | Symlink to `~/.openclaw-autoclaw/skills/` |
| Claude Desktop | Reference path in `CLAUDE.md` |
| Cursor | Add to `.cursorrules` or `.cursor/` |
| Cline | Reference in `.clinerules` |

**ClawHub (OpenClaw users):**

```bash
openclaw skills install deep-code-review
openclaw skills install fe-cli
openclaw skills install screenshot-to-prompt
openclaw skills update --all
```

### Skills

#### 🤖 code-review — Code Review

Multi-dimensional code review: requirement completion, regression risk, edge cases, upstream/downstream impact. Outputs structured report with AI-agent-ready fix instructions.

**Triggers**: review this code / check my changes / any issues / is this safe to merge

#### 🏗️ fe-cli — Frontend Scaffolding

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

#### 📸 screenshot-to-prompt — Screenshot to Implementation Prompt

Input: page screenshot. Output: structured page analysis + an implementation prompt ready for any coding agent. Not a code generator — a screenshot translator.

**Triggers**: analyze this page / generate implementation prompt / screenshot to prompt

### Versioning

**Daily development (auto-publish):**

Push to `main` — GitHub Actions detects `SKILL.md` changes and auto-publishes to ClawHub with an auto-incrementing version. No manual version management needed.

**Official release (manual):**

```bash
# 1. Update CHANGELOG.md
# 2. Tag and push
git tag v1.0.0
git push origin v1.0.0
# 3. GitHub Actions uses the tag as the version for ClawHub
```

Tag format: `v<major>.<minor>.<patch>` (e.g. `v1.0.0`)

### Contributing

1. Create a folder + `SKILL.md` with YAML frontmatter
2. Push to `main` — auto-published via GitHub Actions

---

## Project Structure

```
awesome-skills/
├── .github/workflows/
│   └── publish.yml         # ClawHub auto-publish
├── code-review/SKILL.md
├── fe-cli/
│   ├── SKILL.md
│   ├── references/
│   │   ├── shared-base.md
│   │   ├── shared-config.md
│   │   └── ai-project-md.md
│   ├── web/SKILL.md
│   ├── admin/SKILL.md
│   ├── h5/SKILL.md
│   ├── electron/SKILL.md
│   ├── ssr/SKILL.md
│   └── miniapp/SKILL.md
└── screenshot-to-prompt/SKILL.md
```
