---
name: fe-cli
version: "1.2.0"
homepage: https://github.com/z-Zihan/awesome-skills
description: >
  前端项目脚手架 CLI。支持 React/Vue/Next.js + Tailwind/Ant Design/MUI + Zustand/Redux + i18n，
  初始化标准化前端项目。支持 6 种项目类型：Web SPA、后台管理、移动 H5、Electron 桌面端、
  SSR (Next.js/Nuxt)、小程序 (微信/Taro)。
  触发：用户要求创建新前端项目、初始化项目、搭建脚手架，
  或提到"新建前端项目"、"初始化项目"、"脚手架"、"创建 React/Vue 项目"。
  也可用于检查/审查已有前端项目的规范性。
---

# fe-cli — 前端项目脚手架

## 语言规则

**检测用户使用的语言，全程使用同一语言输出。** 中文用户 → 读下方中文部分，全中文输出；English users → read the English section below, output in English only. 技术术语（React、Vite、pnpm 等）保留原文即可。

---

# 中文版

所有前端项目类型的统一入口。路由到类型专属子技能，并生成共享公共层（请求工具、全局样式、多环境配置等）。

## 快速开始

### 一句话启动（跳过所有问题）

```
用户: "初始化一个 React + Tailwind + Zustand 后台项目，叫 my-admin"
→ 识别类型=admin → 委派给 fe-cli-admin 快速模式
```

### 交互模式

```
用户: "新建前端项目"
→ 询问: "什么类型？" → 路由到子技能 → 子技能询问详细问题
```

## 项目类型检测

从用户请求中识别类型：

| 关键词 | 类型 | 子技能 |
|---|---|---|
| 后台/管理/Admin/Dashboard/CRUD | admin | fe-cli-admin |
| 移动/H5/手机/微信H5/Mobile | h5 | fe-cli-h5 |
| 桌面/Electron/客户端/Desktop | electron | fe-cli-electron |
| SSR/Next.js/Nuxt/服务端渲染/SEO | ssr | fe-cli-ssr |
| 小程序/微信小程序/MiniApp/WeChat | miniapp | fe-cli-miniapp |
| (默认/官网/Web/SPA/网页) | web | fe-cli-web |

如果不确定，询问："这是什么类型的项目？Web SPA / 后台管理 / 移动H5 / Electron桌面 / SSR / 小程序"

### 输入澄清

当用户请求模糊时，**必须先澄清再执行**：
- **模糊输入**（如"帮我搞一下"、"新建项目"）→ 询问项目名称 + 类型 + 技术栈偏好
- **矛盾请求**（如"用 React 和 Vue"）→ 指出矛盾，请求确认使用哪一个
- **越界请求**（如"帮我部署到服务器"）→ 拒绝并说明："fe-cli 只负责本地项目初始化，部署请使用其他工具"
- **非前端请求**（如"写一个 Python 后端"）→ 拒绝并重定向："fe-cli 仅支持前端项目脚手架"

### 降级策略

- `pnpm create vite` 失败 → 提示用户手动创建：`pnpm init vite@latest`，或检查网络/Node 版本
- 依赖安装失败 → 提示检查网络代理、npm registry 配置，提供淘宝镜像命令
- 目标目录已存在 → 询问："目录已存在，覆盖 / 合并 / 取消？"
- 模板中引用的包版本不存在 → 提示用户手动指定版本，不阻塞流程

## 路由到子技能

类型识别后，读取对应子技能的 SKILL.md：

```
Read: ./<type>/SKILL.md (relative to fe-cli/)
```

每个子技能负责：
1. 类型专属问题（框架、UI 库、状态管理、i18n、pre-commit）
2. 类型专属文件生成（布局、页面、路由）
3. 安装和后续配置

## 共享公共层

子技能生成类型专属文件后，在项目中生成以下共享文件。
Read `references/shared-base.md` and `references/shared-config.md` for code templates.

### 要生成的目录结构

```
project-name/
├── src/
│   ├── services/
│   │   ├── request.ts         # fetch 请求封装（含拦截器）
│   │   ├── logger.ts          # 结构化日志（分级、轮转、持久化）
│   │   ├── log-export.ts      # 日志导出（下载 .log/.json）+ 上报（待定）
│   │   └── api/
│   │       └── index.ts       # API 接口定义
│   ├── styles/
│   │   ├── global.scss        # CSS 变量 + 全局样式
│   │   ├── reset.scss         # CSS reset
│   │   └── variables.scss     # 设计令牌（颜色、间距、断点）
│   ├── utils/
│   │   ├── index.ts           # 通用工具函数（防抖、深拷贝等）
│   │   ├── storage.ts         # localStorage/sessionStorage 封装
│   │   ├── format.ts          # 日期/数字格式化
│   │   └── validate.ts        # 表单校验工具
│   └── types/
│       └── global.d.ts        # 全局类型声明
├── .env                       # 公共环境变量
├── .env.development           # 开发环境
├── .env.test                  # 测试环境
├── .env.production            # 生产环境
└── package.json               # Scripts 配置
```

### Package.json scripts

```json
{
  "scripts": {
    "dev": "vite --mode development",
    "dev:test": "vite --mode test",
    "build:test": "vite build --mode test",
    "build:prod": "vite build --mode production",
    "preview": "vite preview",
    "lint": "eslint src --ext .ts,.tsx",
    "lint:fix": "eslint src --ext .ts,.tsx --fix",
    "typecheck": "tsc --noEmit"
  }
}
```

### 共享代码模板

所有共享源码模板见 `references/shared-base.md`（含 logger.ts 和 log-export.ts）。
vite/tsconfig/eslint 配置模板见 `references/shared-config.md`。

## AI 可读项目文档

生成所有项目文件后，在项目根目录生成 `.ai/PROJECT.md`。
This file is for AI agents to quickly understand the project.

### .ai/PROJECT.md 目标

- **完整目录树**，每个文件列出并有一行说明
- **技术栈摘要**（框架、UI 库、状态管理、CSS 等）
- **架构约定**（路径别名、导入顺序、命名规则）
- **命令**（dev、build、test、lint、typecheck）
- **关键模式**（路由、API 调用、状态管理）

### 模板

完整模板见 `references/ai-project-md.md`，根据具体项目类型调整目录树。

### 规则

- 目录使用 `tree` 命令格式（├── 和 └──），文件用一行说明
- 每个文件必须有说明其用途的注释
- 按目录分组，与实际文件系统顺序一致
- 项目结构变化时更新
- 保持简洁——每个文件一行，不是段落

## 关键规则

- **包管理器**：始终使用 pnpm
- **CSS 预处理器**：默认 Sass（SCSS 语法）
- **路径别名**：在 tsconfig 和 vite config 中配置 `@/` → `src/`
- **响应式断点**：Mobile < 768px < Tablet < 1024px < Desktop
- **网络库**：原生 fetch 封装（不用 axios），见 references/shared-base.md
- **环境文件**：始终生成 `.env`、`.env.development`、`.env.test`、`.env.production`
- **日志**：始终生成 `services/logger.ts` + `services/log-export.ts`。使用 `Logger.child("Module")` 模式。最大存储 5MB 自动清理。仅开发模式控制台输出。上报端点为占位符（待定）。
- **Node 版本**：目标 Node 18+
- **pnpm 构建脚本**：在 package.json 中使用 `pnpm.onlyBuiltDependencies` 自动批准原生构建（如 `@parcel/watcher`）。Vite 渲染层构建命令（`build:prod`、`build:test`）不应包含 `tsc -b`——Vite 处理 TS 转译；类型检查是独立的 `typecheck` 脚本。**Electron 主进程例外**：`electron/main.ts` 和 `preload.ts` 在 Node 环境运行，需要 `tsc -p tsconfig.electron.json` 编译。

## 已有项目审查

当用户要求检查已有项目时："检查这个前端项目"、"审查项目规范性"：

### 审查步骤

1. 读取 `package.json` → 检查必要依赖和脚本
2. 检查 vite.config / tsconfig / eslint / prettier 配置
3. 对照上述标准检查 src 目录结构
4. 输出审查报告

### 审查报告格式

```markdown
## 项目审查报告

### ✅ 符合项
- [列出符合标准的条目]

### ❌ 缺失项
- [缺失项]：描述 + 建议修复方案
- ...

### ⚠️ 建议项
- [可选改进]：描述
```

### 审查检查项

| 检查项 | 标准 |
|---|---|
| 包管理器 | 使用 pnpm |
| 路径别名 | tsconfig + vite.config 中 `@/` → `src/` |
| CSS 预处理器 | 配置 Sass (SCSS) |
| 环境文件 | 存在 `.env` / `.env.development` / `.env.test` / `.env.production` |
| 请求封装 | `services/request.ts` 使用 fetch wrapper（非 axios） |
| 日志 | `services/logger.ts` 存在，使用 `Logger.child("Module")` 模式 |
| 全局样式 | `styles/global.scss` + `reset.scss` + `variables.scss` |
| 工具函数 | `utils/index.ts` + `storage.ts` + `format.ts` + `validate.ts` |
| 类型声明 | `types/global.d.ts` 含 ImportMetaEnv |
| Scripts | 含 dev / build:prod / build:test / lint / typecheck |
| .ai/PROJECT.md | 存在且与实际项目结构一致 |

---
---

# English Version

Shared entry point for all frontend project types. Routes to type-specific sub-skills and generates the shared common layer (fetch utils, global styles, multi-env config, etc.).

## Quick Start

### One-liner (skip all questions)

```
User: "Initialize a React + Tailwind + Zustand admin project called my-admin"
→ Identify type=admin → Delegate to fe-cli-admin quick mode
```

### Interactive mode

```
User: "Create a new frontend project"
→ Ask: "What type?" → Route to sub-skill → Sub-skill asks detailed questions
```

## Project Type Detection

Identify the type from the user's request:

| Keywords | Type | Sub-Skill |
|---|---|---|
| Admin/Dashboard/CRUD | admin | fe-cli-admin |
| Mobile/H5/WeChat H5 | h5 | fe-cli-h5 |
| Electron/Desktop/Client | electron | fe-cli-electron |
| SSR/Next.js/Nuxt/SEO | ssr | fe-cli-ssr |
| MiniApp/WeChat Mini Program | miniapp | fe-cli-miniapp |
| (Default/Web/SPA/Website) | web | fe-cli-web |

If unsure, ask: "What type of project? Web SPA / Admin Dashboard / Mobile H5 / Electron Desktop / SSR / Mini App"

### Input Clarification

When the user's request is ambiguous, **must clarify before executing**：
- **Vague input** (e.g., "help me set up", "new project") → Ask for project name + type + tech stack preference
- **Contradictory request** (e.g., "use React and Vue") → Point out the contradiction, ask which one to use
- **Out-of-scope request** (e.g., "deploy to server for me") → Reject and explain: "fe-cli only handles local project initialization, please use other tools for deployment"
- **Non-frontend request** (e.g., "write a Python backend") → Reject and redirect: "fe-cli only supports frontend project scaffolding"

### Degradation Strategy

- `pnpm create vite` fails → Suggest manual creation: `pnpm init vite@latest`, or check network/Node version
- Dependency install fails → Suggest checking network proxy, npm registry config, provide Taobao mirror command
- Target directory already exists → Ask: "Directory already exists. Overwrite / Merge / Cancel?"
- Referenced package version doesn't exist → Suggest user manually specify version, don't block the flow

## Routing to Sub-Skills

Once type is identified, read the corresponding sub-skill's SKILL.md：

```
Read: ./<type>/SKILL.md (relative to fe-cli/)
```

Each sub-skill handles：
1. Type-specific questions (framework, UI library, state management, i18n, pre-commit)
2. Type-specific file generation (layouts, pages, routes)
3. Installation and post-setup

## Shared Common Layer

After the sub-skill generates type-specific files, generate these shared files into the project.
Read `references/shared-base.md` and `references/shared-config.md` for code templates.

### Directory structure to generate

```
project-name/
├── src/
│   ├── services/
│   │   ├── request.ts         # Fetch request wrapper (with interceptors)
│   │   ├── logger.ts          # Structured logger (leveled, rotated, persisted)
│   │   ├── log-export.ts      # Log export (download .log/.json) + upload (TBD)
│   │   └── api/
│   │       └── index.ts       # API interface definitions
│   ├── styles/
│   │   ├── global.scss        # CSS variables + global styles
│   │   ├── reset.scss         # CSS reset
│   │   └── variables.scss     # Design tokens (colors, spacing, breakpoints)
│   ├── utils/
│   │   ├── index.ts           # Common utilities (debounce, deep copy, etc.)
│   │   ├── storage.ts         # localStorage/sessionStorage wrapper
│   │   ├── format.ts          # Date/number formatting
│   │   └── validate.ts        # Form validation utilities
│   └── types/
│       └── global.d.ts        # Global type declarations
├── .env                       # Common env variables
├── .env.development           # Development environment
├── .env.test                  # Test environment
├── .env.production            # Production environment
└── package.json               # Scripts config
```

### Package.json scripts

```json
{
  "scripts": {
    "dev": "vite --mode development",
    "dev:test": "vite --mode test",
    "build:test": "vite build --mode test",
    "build:prod": "vite build --mode production",
    "preview": "vite preview",
    "lint": "eslint src --ext .ts,.tsx",
    "lint:fix": "eslint src --ext .ts,.tsx --fix",
    "typecheck": "tsc --noEmit"
  }
}
```

### Shared code templates

All shared source code templates are in `references/shared-base.md` (including logger.ts and log-export.ts).
Vite/tsconfig/eslint config templates are in `references/shared-config.md`.

## AI-Readable Project Doc

After generating ALL project files (shared layer + type-specific), generate `.ai/PROJECT.md` in the project root.
This file is for AI agents to quickly understand the project.

### .ai/PROJECT.md Goals

- **Full directory tree** with every file listed and a one-line purpose
- **Tech stack summary** (framework, UI library, state management, CSS, etc.)
- **Architectural conventions** (path aliases, import order, naming rules)
- **Commands** (dev, build, test, lint, typecheck)
- **Key patterns** (routing, API calls, state management)

### Template

Full template is in `references/ai-project-md.md`, adjust the directory tree based on the specific project type.

### Rules

- Use `tree` command format for directories (├── and └──), files with one-line description
- Every file entry must have a comment explaining its purpose
- Group by directory; keep the same order as the actual file system
- Update whenever project structure changes
- Keep it concise — one line per file, not paragraphs

## Key Rules

- **Package manager**: Always use pnpm
- **CSS preprocessor**: Sass (SCSS syntax) by default
- **Path alias**: Configure `@/` → `src/` in tsconfig and vite config
- **Responsive breakpoints**: Mobile < 768px < Tablet < 1024px < Desktop
- **Network library**: Native fetch wrapper (not axios), see references/shared-base.md
- **Environment files**: Always generate `.env`, `.env.development`, `.env.test`, `.env.production`
- **Logging**: Always generate `services/logger.ts` + `services/log-export.ts`. Use `Logger.child("Module")` pattern. Max storage 5MB auto-cleanup. Console output only in dev mode. Upload endpoint is a placeholder (TBD).
- **Node version**: Target Node 18+
- **pnpm build scripts**: Use `pnpm.onlyBuiltDependencies` in package.json to auto-approve native builds (e.g., `@parcel/watcher`). Vite renderer build commands (`build:prod`, `build:test`) should not include `tsc -b` — Vite handles TS transpilation; type checking is a separate `typecheck` script. **Electron main process exception**: `electron/main.ts` and `preload.ts` run in Node environment and need `tsc -p tsconfig.electron.json` compilation.

## Existing Project Audit

When the user asks to check an existing project: "Check this frontend project", "Audit project standards":

### Audit Steps

1. Read `package.json` → Check required dependencies and scripts
2. Check vite.config / tsconfig / eslint / prettier config
3. Compare src directory structure against the above standards
4. Output audit report

### Audit Report Format

```markdown
## Project Audit Report

### ✅ Compliant
- [Items meeting standards]

### ❌ Missing
- [Missing item]: Description + suggested fix
- ...

### ⚠️ Suggestions
- [Optional improvement]: Description
```

### Audit Checklist

| Check | Standard |
|---|---|
| Package manager | Using pnpm |
| Path alias | `@/` → `src/` in tsconfig + vite.config |
| CSS preprocessor | Sass (SCSS) configured |
| Environment files | `.env` / `.env.development` / `.env.test` / `.env.production` exist |
| Request wrapper | `services/request.ts` using fetch wrapper (not axios) |
| Logging | `services/logger.ts` exists, using `Logger.child("Module")` pattern |
| Global styles | `styles/global.scss` + `reset.scss` + `variables.scss` |
| Utility functions | `utils/index.ts` + `storage.ts` + `format.ts` + `validate.ts` |
| Type declarations | `types/global.d.ts` contains ImportMetaEnv |
| Scripts | Contains dev / build:prod / build:test / lint / typecheck |
| .ai/PROJECT.md | Exists and matches actual project structure |
