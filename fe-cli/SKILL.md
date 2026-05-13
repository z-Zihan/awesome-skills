---
name: fe-cli
homepage: https://github.com/z-Zihan/awesome-skills
description: >
  Frontend project scaffolding CLI. Initialize standardized frontend projects with React/Vue/Next.js,
  with Tailwind/Ant Design/MUI, Zustand/Redux, i18n, and more. Supports 6 project types: web SPA,
  admin dashboard, mobile H5, Electron desktop, SSR (Next.js/Nuxt), and mini-program (WeChat/Taro).
  Use when user asks to create a new frontend project, scaffold a project, init a frontend app,
  or mentions "新建前端项目", "初始化项目", "脚手架", "创建 React/Vue 项目".
  Also use when user asks to check/audit an existing project for frontend best practices.
---

# fe-cli — Frontend Project Scaffolding / 前端项目脚手架

Shared entry point for all frontend project types. Routes to type-specific sub-skills and generates
the shared common layer (fetch utils, global styles, multi-env config, etc.).
所有前端项目类型的统一入口。路由到类型专属子技能，并生成共享公共层（请求工具、全局样式、多环境配置等）。

## Quick Start / 快速开始

### One-liner (skip all questions / 跳过所有问题)

```
User: "初始化一个 React + Tailwind + Zustand 后台项目，叫 my-admin"
→ Detect type=admin → delegate to fe-cli-admin in fast mode
```

### Interactive mode / 交互模式

```
User: "新建前端项目"
→ Ask: "什么类型？" → Route to sub-skill → Sub-skill asks detailed questions
→ 询问: "什么类型？" → 路由到子技能 → 子技能询问详细问题
```

## Project Type Detection / 项目类型检测

Identify the type from user's request. Keywords mapping:
从用户请求中识别类型。关键词映射：

| Keywords / 关键词 | Type / 类型 | Sub-Skill / 子技能 |
|---|---|---|
| 后台/管理/Admin/Dashboard/CRUD | admin | fe-cli-admin |
| 移动/H5/手机/微信H5/Mobile | h5 | fe-cli-h5 |
| 桌面/Electron/客户端/Desktop | electron | fe-cli-electron |
| SSR/Next.js/Nuxt/服务端渲染/SEO | ssr | fe-cli-ssr |
| 小程序/微信小程序/MiniApp/WeChat | miniapp | fe-cli-miniapp |
| (default / 官网/Web/SPA/网页) | web | fe-cli-web |

If ambiguous, ask: "这是什么类型的项目？Web SPA / 后台管理 / 移动H5 / Electron桌面 / SSR / 小程序"

## Routing to Sub-Skills / 路由到子技能

Once type is identified, read the corresponding sub-skill's SKILL.md:
类型识别后，读取对应子技能的 SKILL.md：

```
Read: ./<type>/SKILL.md (relative to fe-cli/)
```

Each sub-skill handles:
每个子技能负责：
1. Type-specific questions (framework, UI library, state management, i18n, pre-commit) / 类型专属问题（框架、UI 库、状态管理、i18n、pre-commit）
2. Type-specific file generation (layout, pages, routing) / 类型专属文件生成（布局、页面、路由）
3. Installation and post-setup / 安装和后续配置

## Shared Common Layer / 共享公共层

After the sub-skill generates type-specific files, generate these shared files into the project.
子技能生成类型专属文件后，在项目中生成以下共享文件。
Read `references/shared-base.md` and `references/shared-config.md` for code templates.

### Directory structure to generate / 要生成的目录结构

```
project-name/
├── src/
│   ├── services/
│   │   ├── request.ts         # fetch wrapper with interceptors
│   │   ├── logger.ts          # Structured logger (levels, rotation, persistent storage)
│   │   ├── log-export.ts      # Log export (download .log/.json) + submit (endpoint TBD)
│   │   └── api/
│   │       └── index.ts       # API endpoint definitions
│   ├── styles/
│   │   ├── global.scss        # CSS variables + global styles
│   │   ├── reset.scss         # CSS reset
│   │   └── variables.scss     # Design tokens (colors, spacing, breakpoints)
│   ├── utils/
│   │   ├── index.ts           # General utilities (debounce, clone, etc.)
│   │   ├── storage.ts         # localStorage/sessionStorage wrapper
│   │   ├── format.ts          # Date/number formatters
│   │   └── validate.ts        # Form validation helpers
│   └── types/
│       └── global.d.ts        # Global type declarations
├── .env                       # Common env / 公共环境变量
├── .env.development           # Dev env / 开发环境
├── .env.test                  # Test env / 测试环境
├── .env.production            # Prod env / 生产环境
└── package.json               # Scripts section
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

### Shared code templates / 共享代码模板

See `references/shared-base.md` for all shared source code templates (including logger.ts and log-export.ts).
See `references/shared-config.md` for vite/tsconfig/eslint config templates.

## AI-Readable Project Doc / AI 可读项目文档

After generating ALL project files (shared layer + type-specific), generate `.ai/PROJECT.md` in the project root.
生成所有项目文件（共享层 + 类型专属）后，在项目根目录生成 `.ai/PROJECT.md`。
This file is for AI agents to quickly understand the project. This file helps AI agents quickly understand the project.

### .ai/PROJECT.md Goals / 目标

- **Full directory tree** with every file listed and a one-line purpose / 完整目录树，每个文件列出并有一行说明
- **Tech stack summary** (framework, UI lib, state management, CSS, etc.) / 技术栈摘要
- **Architectural conventions** (path aliases, import order, naming rules) / 架构约定（路径别名、导入顺序、命名规则）
- **Commands** (dev, build, test, lint, typecheck) / 命令（开发、构建、测试、lint、类型检查）
- **Key patterns** (how routing works, how API calls are made, how state is managed) / 关键模式（路由、API 调用、状态管理）

### Template / 模板

Read `references/ai-project-md.md` for the full template. Adapt the directory tree to match the actual files generated for the specific project type.

### Rules / 规则

- Always use `tree` command format (├── and └──) for directories; a flat list with one-liners for files
- Every file entry must have a comment explaining its purpose / 每个文件必须有说明其用途的注释
- Group by directory; keep the same order as the actual file system / 按目录分组，与实际文件系统顺序一致
- Update `.ai/PROJECT.md` whenever project structure changes / 项目结构变化时更新
- Keep it concise — one line per file, not paragraphs / 保持简洁 — 每个文件一行，不是段落

## Key Rules / 关键规则

- **Package manager**: Always use pnpm
- **CSS preprocessor**: Sass (SCSS syntax) by default
- **Path alias**: Configure `@/` → `src/` in both tsconfig and vite config
- **Responsive breakpoints**: Mobile < 768px < Tablet < 1024px < Desktop
- **Network library**: Native fetch with wrapper (no axios), see references/shared-base.md
- **Env files**: Always generate `.env`, `.env.development`, `.env.test`, `.env.production`
- **Logging**: Always generate `services/logger.ts` + `services/log-export.ts`. Logger uses `Logger.child("Module")` pattern. Max storage 5MB with auto-trim. Console output only in dev mode. Submit endpoint is placeholder (TBD).
- **Node version**: Target Node 18+
- **pnpm build scripts**: Use `pnpm.onlyBuiltDependencies` in package.json to auto-approve native builds (e.g., `@parcel/watcher`). Build commands (`build:prod`, `build:test`) should NOT include `tsc -b` — Vite handles TS transpilation; type checking is a separate `typecheck` script.

## Existing Project Audit / 已有项目审查

When user asks to check an existing project: "检查这个前端项目", "审查项目规范性":
当用户要求检查已有项目时：

1. Read `package.json` → check required dependencies and scripts / 读取 → 检查必要依赖和脚本
2. Check for vite.config / tsconfig / eslint / prettier config / 检查配置文件
3. Check src directory structure against the standard above / 对照上述标准检查 src 目录结构
4. Report what's missing and suggest improvements / 报告缺失项并给出改进建议
