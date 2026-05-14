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
openclaw skills install code-review-ProMax
openclaw skills install fe-cli
openclaw skills install screenshot-to-prompt
openclaw skills install project-doc-analyst
openclaw skills install project-onboarding
openclaw skills install skill-prompt-generatoropenclaw skills update --all
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

#### 📋 project-doc-analyst — 项目文档生成

深度阅读代码仓库，输出面向人类和 AI 的工程语义资产文档套件。按优先级分阶段生成：P0（项目总览 + 技术架构）→ P1（设计原因 + 产品分析 + 代码示例），支持可选文档和复杂专题深挖。

**触发词**：分析项目 / 生成文档 / 项目文档 / 代码分析 / 项目架构分析 / 架构图 / 调用链图 / 数据流图

#### 🚀 project-onboarding — 项目接手指南

帮助有经验的开发者快速接手陌生项目。分三阶段输出：快速总览（10 分钟建地图）→ 深入专项 → 定向开发辅助。覆盖开发流程、工程规范、API 集成、组件体系、环境部署、团队协作等。

**触发词**：接手项目 / 项目上手 / 快速上手 / 新人接手 / onboarding / 如何开发 / 项目怎么跑

#### 🎯 skill-prompt-generator — Skill Prompt 架构师

根据用户想法、流程或需求，自动生成结构完整、工程化、可直接使用的 Skill Prompt。支持中英双语输出，根据 Skill 类型自动增强（开发/UI/文档/架构/测试等）。

**触发词**：生成 skill / 创建 skill / 写个 prompt / 设计 skill / prompt 设计 / skill 架构

#### 🧭 dev-mentor — 跨领域学习伴侣

帮助有经验的开发者学习不熟悉的领域，通过连续对话从零完成项目的完整生命周期。首批支持：后端开发（TypeScript/Go/Python）、数据库、服务器部署（Docker/Nginx/HTTPS/CI-CD）、Rust 系统编程。自动识别用户已有经验，不重复教，用类比教学。专业名词自带解释，代码使用最新技术栈和最佳实践。

**触发词**：学后端 / 学 Rust / 从零做项目 / 前端学后端 / 教我做项目 / 带我开发

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
openclaw skills install code-review-ProMax
openclaw skills install fe-cli
openclaw skills install project-doc-analyst
openclaw skills install project-onboarding
openclaw skills install skill-prompt-generatoropenclaw skills install screenshot-to-prompt
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

#### 📋 project-doc-analyst — Project Documentation Generator

Deep-read the entire codebase and generate engineering semantic asset documentation for both humans and AI. Staged by priority: P0 (project overview + technical architecture) → P1 (design rationale + product analysis + code examples), with optional docs and deep dives.

**Triggers**: analyze project / generate docs / project documentation / code analysis / architecture analysis / architecture diagram

#### 🚀 project-onboarding — Project Onboarding Guide

Help experienced developers quickly onboard onto unfamiliar projects. Three-stage output: quick overview (10-min project map) → deep dive → targeted dev assistance. Covers dev workflow, engineering standards, API integration, component system, environment/deployment, team collaboration.

**Triggers**: onboard / project handover / quick start / how to develop / how to run

#### 🎯 skill-prompt-generator — Skill Prompt Architect

Transforms vague ideas into structured, engineering-grade, ready-to-use Skill Prompts. Supports bilingual Chinese/English output with type-specific enhancements (dev, UI, docs, architecture, testing, etc.).

**Triggers**: create skill / write a prompt / design skill / prompt design / skill architecture

#### 🧭 dev-mentor — Cross-Domain Learning Companion

Helps experienced developers learn unfamiliar domains by building a full project from zero to production via continuous conversation. First batch: backend (TypeScript/Go/Python), databases, server deployment (Docker/Nginx/HTTPS/CI-CD), Rust systems programming. Auto-detects existing skills, uses analogies from known domains, explains technical terms on first use.

**Triggers**: learn backend / learn Rust / build project from scratch / teach me to code

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
├── project-doc-analyst/SKILL.md
├── project-onboarding/SKILL.md
├── dev-mentor/SKILL.md
└── skill-prompt-generator/SKILL.md
```
