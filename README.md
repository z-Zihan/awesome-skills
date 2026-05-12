# 🧰 Awesome Skills

通用 AI Agent 技能库。一个 skill 就是一份 `SKILL.md`，按需加载，开箱即用。

适用于任何支持读取本地 Markdown 作为系统指令的 AI Agent（OpenClaw、Claude Desktop、Cursor、Cline 等）。

## 快速开始

```bash
git clone https://github.com/z-Zihan/awesome-skills.git
```

将 `SKILL.md` 放到你的 Agent 能扫描到的目录即可。不同工具的加载方式：

| Agent | 配置方式 |
|---|---|
| OpenClaw | 软链接到 `~/.openclaw-autoclaw/skills/` |
| Claude Desktop | 在 `CLAUDE.md` 中引用文件路径 |
| Cursor | 在 `.cursorrules` 或项目 `.cursor/` 中配置 |
| Cline | 在 `.clinerules` 中引用 |

---

## Skill 一览

### 🤖 code-review — 代码审查

资深代码审查专家。从正确性、回归风险、兼容性、稳定性、性能、安全性、上下游影响等多维度审查代码变更。输出结构化、可用于合入决策的审查结论。

```
触发："review 这段代码" / "审查这个文件" / 贴 diff
```

### 🏗️ fe-cli — 前端项目脚手架

一键创建规范化前端项目，自动生成标准目录结构、共享代码层（请求封装 / 样式 / 工具函数 / 环境配置 / AI 可读文档）、Vite + TypeScript 配置。

| 子 Skill | 类型 | 触发关键词 |
|---|---|---|
| `fe-cli-web` | Web SPA | 官网、网页、SPA |
| `fe-cli-admin` | 后台管理 | 后台、管理、Admin、Dashboard |
| `fe-cli-h5` | 移动端 H5 | 移动、H5、手机、微信 H5 |
| `fe-cli-electron` | 桌面应用 | 桌面、Electron、客户端 |
| `fe-cli-ssr` | 服务端渲染 | SSR、Next.js、Nuxt、SEO |
| `fe-cli-miniapp` | 小程序 | 小程序、微信小程序、MiniApp |

**使用：**

```
"创建一个 React + Ant Design 后台项目，叫 order-admin"
"新建一个移动端 H5 项目"
"初始化 Electron 桌面应用"
```

**技术栈规范：**

| 约束 | 值 |
|---|---|
| 包管理器 | pnpm |
| CSS 预处理器 | Sass (SCSS) |
| 网络库 | native fetch（不用 axios） |
| 路径别名 | `@/` → `src/` |
| Node 版本 | 18+ |
| 响应式断点 | 768px / 1024px |

---

## 目录结构

```
awesome-skills/
├── README.md
├── code-review/
│   └── SKILL.md            # 代码审查
└── fe-cli/
    ├── SKILL.md            # 主控：类型识别 + 共享层生成
    ├── references/         # 共享模板（按需读取）
    │   ├── shared-base.md
    │   ├── shared-config.md
    │   └── ai-project-md.md
    ├── web/SKILL.md
    ├── admin/SKILL.md
    ├── h5/SKILL.md
    ├── electron/SKILL.md
    ├── ssr/SKILL.md
    └── miniapp/SKILL.md
```

---

## 贡献新 Skill

1. 在仓库根目录创建文件夹 + `SKILL.md`：

```
my-skill/
└── SKILL.md
```

2. **SKILL.md 建议包含 YAML frontmatter**：

```yaml
---
name: my-skill
description: >
  一句话描述。支持多关键词触发。
  例如：Use when user asks for X, mentions Y, or wants to Z.
---
```

3. 提交 push 即可。

---

## 设计原则

- **按需加载**：Skill 内容只在触发时读入，不占用日常上下文
- **独立触发**：每个子 Skill 独立可被发现和加载
- **模板分离**：共享代码模板放在 `references/`，不影响 skill 发现
- **通用兼容**：纯 Markdown 格式，适配任何 AI Agent 工具
