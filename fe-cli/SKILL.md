---
name: fe-cli
homepage: https://github.com/z-Zihan/awesome-skills
description: >
  前端项目脚手架 CLI。支持 React/Vue/Next.js + Tailwind/Ant Design/MUI + Zustand/Redux + i18n，
  初始化标准化前端项目。支持 6 种项目类型：Web SPA、后台管理、移动 H5、Electron 桌面端、
  SSR (Next.js/Nuxt)、小程序 (微信/Taro)。
  触发：用户要求创建新前端项目、初始化项目、搭建脚手架，
  或提到"新建前端项目"、"初始化项目"、"脚手架"、"创建 React/Vue 项目"。
  也可用于检查/审查已有前端项目的规范性。
---

# fe-cli — 前端项目脚手架 / Frontend Project Scaffolding

所有前端项目类型的统一入口。路由到类型专属子技能，并生成共享公共层（请求工具、全局样式、多环境配置等）。
Shared entry point for all frontend project types. Routes to type-specific sub-skills and generates the shared common layer (fetch utils, global styles, multi-env config, etc.).

## 快速开始 / Quick Start

### 一句话启动（跳过所有问题）/ One-liner (skip all questions)

```
用户: "初始化一个 React + Tailwind + Zustand 后台项目，叫 my-admin"
→ 识别类型=admin → 委派给 fe-cli-admin 快速模式
```

### 交互模式 / Interactive mode

```
用户: "新建前端项目"
→ 询问: "什么类型？" → 路由到子技能 → 子技能询问详细问题
```

## 项目类型检测 / Project Type Detection

从用户请求中识别类型 / Identify the type from user's request：

| 关键词 / Keywords | 类型 / Type | 子技能 / Sub-Skill |
|---|---|---|
| 后台/管理/Admin/Dashboard/CRUD | admin | fe-cli-admin |
| 移动/H5/手机/微信H5/Mobile | h5 | fe-cli-h5 |
| 桌面/Electron/客户端/Desktop | electron | fe-cli-electron |
| SSR/Next.js/Nuxt/服务端渲染/SEO | ssr | fe-cli-ssr |
| 小程序/微信小程序/MiniApp/WeChat | miniapp | fe-cli-miniapp |
| (默认/官网/Web/SPA/网页) | web | fe-cli-web |

如果不确定，询问："这是什么类型的项目？Web SPA / 后台管理 / 移动H5 / Electron桌面 / SSR / 小程序"

## 路由到子技能 / Routing to Sub-Skills

类型识别后，读取对应子技能的 SKILL.md：
Once type is identified, read the corresponding sub-skill's SKILL.md：

```
Read: ./<type>/SKILL.md (relative to fe-cli/)
```

每个子技能负责 / Each sub-skill handles：
1. 类型专属问题（框架、UI 库、状态管理、i18n、pre-commit） / Type-specific questions
2. 类型专属文件生成（布局、页面、路由） / Type-specific file generation
3. 安装和后续配置 / Installation and post-setup

## 共享公共层 / Shared Common Layer

子技能生成类型专属文件后，在项目中生成以下共享文件。
After the sub-skill generates type-specific files, generate these shared files into the project.
Read `references/shared-base.md` and `references/shared-config.md` for code templates.

### 要生成的目录结构 / Directory structure to generate

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

### 共享代码模板 / Shared code templates

所有共享源码模板见 `references/shared-base.md`（含 logger.ts 和 log-export.ts）。
vite/tsconfig/eslint 配置模板见 `references/shared-config.md`。

## AI 可读项目文档 / AI-Readable Project Doc

生成所有项目文件后，在项目根目录生成 `.ai/PROJECT.md`。
After generating ALL project files (shared layer + type-specific), generate `.ai/PROJECT.md` in the project root.
This file is for AI agents to quickly understand the project.

### .ai/PROJECT.md 目标 / Goals

- **完整目录树**，每个文件列出并有一行说明 / Full directory tree with every file listed and a one-line purpose
- **技术栈摘要**（框架、UI 库、状态管理、CSS 等）/ Tech stack summary
- **架构约定**（路径别名、导入顺序、命名规则）/ Architectural conventions
- **命令**（dev、build、test、lint、typecheck）/ Commands
- **关键模式**（路由、API 调用、状态管理）/ Key patterns

### 模板 / Template

完整模板见 `references/ai-project-md.md`，根据具体项目类型调整目录树。

### 规则 / Rules

- 目录使用 `tree` 命令格式（├── 和 └──），文件用一行说明 / Always use `tree` format for directories
- 每个文件必须有说明其用途的注释 / Every file entry must have a comment explaining its purpose
- 按目录分组，与实际文件系统顺序一致 / Group by directory; keep the same order as the actual file system
- 项目结构变化时更新 / Update whenever project structure changes
- 保持简洁——每个文件一行，不是段落 / Keep it concise — one line per file

## 关键规则 / Key Rules

- **包管理器**：始终使用 pnpm / Package manager: Always use pnpm
- **CSS 预处理器**：默认 Sass（SCSS 语法）/ CSS preprocessor: Sass (SCSS syntax) by default
- **路径别名**：在 tsconfig 和 vite config 中配置 `@/` → `src/` / Path alias: Configure `@/` → `src/`
- **响应式断点**：Mobile < 768px < Tablet < 1024px < Desktop
- **网络库**：原生 fetch 封装（不用 axios），见 references/shared-base.md
- **环境文件**：始终生成 `.env`、`.env.development`、`.env.test`、`.env.production`
- **日志**：始终生成 `services/logger.ts` + `services/log-export.ts`。使用 `Logger.child("Module")` 模式。最大存储 5MB 自动清理。仅开发模式控制台输出。上报端点为占位符（待定）。
- **Node 版本**：目标 Node 18+
- **pnpm 构建脚本**：在 package.json 中使用 `pnpm.onlyBuiltDependencies` 自动批准原生构建（如 `@parcel/watcher`）。构建命令（`build:prod`、`build:test`）不应包含 `tsc -b`——Vite 处理 TS 转译；类型检查是独立的 `typecheck` 脚本。

## 已有项目审查 / Existing Project Audit

当用户要求检查已有项目时："检查这个前端项目"、"审查项目规范性"：

1. 读取 `package.json` → 检查必要依赖和脚本 / Read → check required dependencies and scripts
2. 检查 vite.config / tsconfig / eslint / prettier 配置 / Check for config files
3. 对照上述标准检查 src 目录结构 / Check src directory structure against the standard above
4. 报告缺失项并给出改进建议 / Report what's missing and suggest improvements
