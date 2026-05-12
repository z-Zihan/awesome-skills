---
name: fe-cli
description: >
  Frontend project scaffolding CLI. Initialize standardized frontend projects with React/Vue/Next.js,
  with Tailwind/Ant Design/MUI, Zustand/Redux, i18n, and more. Supports 6 project types: web SPA,
  admin dashboard, mobile H5, Electron desktop, SSR (Next.js/Nuxt), and mini-program (WeChat/Taro).
  Use when user asks to create a new frontend project, scaffold a project, init a frontend app,
  or mentions "新建前端项目", "初始化项目", "脚手架", "创建 React/Vue 项目".
  Also use when user asks to check/audit an existing project for frontend best practices.
---

# fe-cli — Frontend Project Scaffolding

Shared entry point for all frontend project types. Routes to type-specific sub-skills and generates
the shared common layer (fetch utils, global styles, multi-env config, etc.).

## Quick Start

### One-liner (skip all questions)

```
User: "初始化一个 React + Tailwind + Zustand 后台项目，叫 my-admin"
→ Detect type=admin → delegate to fe-cli-admin in fast mode
```

### Interactive mode

```
User: "新建前端项目"
→ Ask: "什么类型？" → Route to sub-skill → Sub-skill asks detailed questions
```

## Project Type Detection

Identify the type from user's request. Keywords mapping:

| Keywords | Type | Sub-Skill |
|---|---|---|
| 后台/管理/Admin/Dashboard/CRUD | admin | fe-cli-admin |
| 移动/H5/手机/微信H5/Mobile | h5 | fe-cli-h5 |
| 桌面/Electron/客户端/Desktop | electron | fe-cli-electron |
| SSR/Next.js/Nuxt/服务端渲染/SEO | ssr | fe-cli-ssr |
| 小程序/微信小程序/MiniApp/WeChat | miniapp | fe-cli-miniapp |
| (default / 官网/Web/SPA/网页) | web | fe-cli-web |

If ambiguous, ask: "这是什么类型的项目？Web SPA / 后台管理 / 移动H5 / Electron桌面 / SSR / 小程序"

## Routing to Sub-Skills

Once type is identified, read the corresponding sub-skill's SKILL.md:

```
Read: ./<type>/SKILL.md (relative to fe-cli/)
```

Each sub-skill handles:
1. Type-specific questions (framework, UI library, state management, i18n, pre-commit)
2. Type-specific file generation (layout, pages, routing)
3. Installation and post-setup

## Shared Common Layer

After the sub-skill generates type-specific files, generate these shared files into the project.
Read `references/shared-base.md` and `references/shared-config.md` for code templates.

### Directory structure to generate

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
├── .env                       # Common env
├── .env.development           # Dev env (API_BASE_URL=http://localhost:3000)
├── .env.test                  # Test env
├── .env.production            # Prod env
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

### Shared code templates

See `references/shared-base.md` for all shared source code templates (including logger.ts and log-export.ts).
See `references/shared-config.md` for vite/tsconfig/eslint config templates.

## AI-Readable Project Doc

After generating ALL project files (shared layer + type-specific), generate `.ai/PROJECT.md` in the project root. This file is for AI agents to quickly understand the project.

### .ai/PROJECT.md Goals

- **Full directory tree** with every file listed and a one-line purpose
- **Tech stack summary** (framework, UI lib, state management, CSS, etc.)
- **Architectural conventions** (path aliases, import order, naming rules)
- **Commands** (dev, build, test, lint, typecheck)
- **Key patterns** (how routing works, how API calls are made, how state is managed)

### Template

Read `references/ai-project-md.md` for the full template. Adapt the directory tree to match the actual files generated for the specific project type.

### Rules

- Always use `tree` command format (├── and └──) for directories; a flat list with one-liners for files
- Every file entry must have a comment explaining its purpose
- Group by directory; keep the same order as the actual file system
- Update `.ai/PROJECT.md` whenever project structure changes
- Keep it concise — one line per file, not paragraphs

## Key Rules

- **Package manager**: Always use pnpm
- **CSS preprocessor**: Sass (SCSS syntax) by default
- **Path alias**: Configure `@/` → `src/` in both tsconfig and vite config
- **Responsive breakpoints**: Mobile < 768px < Tablet < 1024px < Desktop
- **Network library**: Native fetch with wrapper (no axios), see references/shared-base.md
- **Env files**: Always generate `.env`, `.env.development`, `.env.test`, `.env.production`
- **Logging**: Always generate `services/logger.ts` + `services/log-export.ts`. Logger uses `Logger.child("Module")` pattern. Max storage 5MB with auto-trim. Console output only in dev mode. Submit endpoint is placeholder (TBD).
- **Node version**: Target Node 18+
- **pnpm build scripts**: Use `pnpm.onlyBuiltDependencies` in package.json to auto-approve native builds (e.g., `@parcel/watcher`). Build commands (`build:prod`, `build:test`) should NOT include `tsc -b` — Vite handles TS transpilation; type checking is a separate `typecheck` script.

## Existing Project Audit

When user asks to check an existing project: "检查这个前端项目", "审查项目规范性":

1. Read `package.json` → check required dependencies and scripts
2. Check for vite.config / tsconfig / eslint / prettier config
3. Check src directory structure against the standard above
4. Report what's missing and suggest improvements
