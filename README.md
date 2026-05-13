# 🧰 Awesome Skills

通用 AI Agent 技能库。一个 skill 就是一份 `SKILL.md`，按需加载，开箱即用。

适用于任何支持读取本地 Markdown 作为系统指令的 AI Agent（OpenClaw、Claude Desktop、Cursor、Cline 等）。

## 安装

### 方式一：Git Clone

```bash
git clone https://github.com/z-Zihan/awesome-skills.git
```

将 `SKILL.md` 放到你的 Agent 能扫描到的目录即可：

| Agent | 配置方式 |
|---|---|
| OpenClaw | 软链接到 `~/.openclaw-autoclaw/skills/` |
| Claude Desktop | 在 `CLAUDE.md` 中引用文件路径 |
| Cursor | 在 `.cursorrules` 或项目 `.cursor/` 中配置 |
| Cline | 在 `.clinerules` 中引用 |

### 方式二：ClawHub 安装（OpenClaw 用户）

> ⚠️ 首次需要先安装 ClawHub CLI 并登录：`npm i -g clawhub && clawhub login`

```bash
openclaw skills install code-review
openclaw skills install fe-cli
openclaw skills install screenshot-to-prompt
```

更新已安装的 skill：

```bash
openclaw skills update --all
```

---

## Skill 一览

### 🤖 code-review — 代码审查

资深代码审查专家。从正确性、回归风险、完成度、兼容性、安全性、上下游影响等多维度审查代码变更。输出结构化审查结论，含可复制给 AI agent 的修复指令。

- **能力**：需求完成度分析、Bug 修复边界检查、旧功能影响评估、自动生成修复指令
- **触发**："review 这段代码" / "帮我看看改动" / "审查代码" / "代码有没有问题"

### 🏗️ fe-cli — 前端项目脚手架

一键创建规范化前端项目，自动生成标准目录结构、共享代码层（请求封装 / 样式 / 工具函数 / 环境配置 / AI 可读文档）。

| 子 Skill | 类型 | 触发关键词 |
|---|---|---|
| `fe-cli-web` | Web SPA | 官网、网页、SPA |
| `fe-cli-admin` | 后台管理 | 后台、管理、Admin、Dashboard |
| `fe-cli-h5` | 移动端 H5 | 移动、H5、手机、微信 H5 |
| `fe-cli-electron` | 桌面应用 | 桌面、Electron、客户端 |
| `fe-cli-ssr` | 服务端渲染 | SSR、Next.js、Nuxt、SEO |
| `fe-cli-miniapp` | 小程序 | 小程序、微信小程序、MiniApp |

**技术栈规范：** pnpm / Sass / native fetch / Vite + TypeScript / `@/` 路径别名

### 📸 screenshot-to-prompt — 截图转实现 Prompt

输入页面截图，输出结构化页面识别结果 + 可直接发给 coding agent 的实现 prompt。不是代码生成器，是截图翻译器。

- **能力**：页面结构识别、组件类型识别、文案字段提取、交互状态推断、多图状态归并
- **UI 策略**：自动切换骨架模式 / 自由发挥 UI / 设计稿还原
- **触发**：发截图说"帮我分析这个页面" / "生成实现 prompt" / "截图转实现"

---

## 版本管理

- **日常更新**：push 到 `main` 分支，GitHub Actions 自动同步到 ClawHub（版本号自动递增）
- **正式发版**：打 git tag（如 `v1.0.0`），Actions 使用 tag 作为版本号发布

```bash
# 日常开发，push 即自动发布
git push origin main

# 正式发版
git tag v1.0.0
git push origin v1.0.0
```

---

## 目录结构

```
awesome-skills/
├── .github/workflows/
│   └── publish.yml         # ClawHub 自动发布
├── README.md
├── code-review/
│   └── SKILL.md
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
└── screenshot-to-prompt/
    └── SKILL.md
```

---

## 贡献新 Skill

1. 创建文件夹 + `SKILL.md`：

```
my-skill/
└── SKILL.md
```

2. 建议包含 YAML frontmatter（用于触发匹配）：

```yaml
---
name: my-skill
description: >
  一句话描述。列出触发关键词。
  NOT for: 不适用的场景。
---
```

3. 提交 push，GitHub Actions 会自动发布到 ClawHub。

---

## 设计原则

- **按需加载**：Skill 内容只在触发时读入，不占用日常上下文
- **独立触发**：每个子 Skill 独立可被发现和加载
- **通用兼容**：纯 Markdown 格式，适配任何 AI Agent 工具
- **自动发布**：push 即发布，无需手动管理版本号
