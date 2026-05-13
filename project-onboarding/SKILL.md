---
name: project-onboarding
homepage: https://github.com/z-Zihan/awesome-skills
description: >
  帮助有经验的开发者快速接手陌生项目，分阶段输出项目概览、开发流程、
  工程规范、API 集成、组件体系、环境部署等实用开发指南，达到"可以开始安全开发"的状态。
  触发词：接手项目, 项目上手, 快速上手, 新人接手, 项目入门, onboarding,
  如何开发, 怎么启动项目, 项目怎么跑, 开发流程, onboarding guide,
  how to onboard, project handover, developer quick start.
  NOT for: generating long architecture reports, code analysis without dev context,
  beginner programming tutorials, onboarding for interns.
---

# project-onboarding — 项目接手指南 / Project Onboarding Guide

帮助有经验的开发者快速理解并接手一个陌生项目，尽快具备实际开发能力。
Help experienced developers quickly understand and onboard onto an unfamiliar project, reaching actual development capability as fast as possible.

## 这个 Skill 不是 / This Skill Is NOT

- 面向编程新手 / Not for beginners
- 面向实习生教学 / Not for intern training
- 面向基础知识解释 / Not for explaining basic programming concepts
- 面向纯代码分析 / Not for pure code analysis

## 核心目标 / Core Objective

让专业开发者在最短时间内完成 / Enable a professional developer to achieve the following in minimum time:

- 项目理解 / Project understanding
- 工程结构理解 / Engineering structure understanding
- 开发流程理解 / Development workflow understanding
- 团队规范理解 / Team standards understanding
- 环境体系理解 / Environment system understanding
- API 调用方式理解 / API integration understanding
- 组件体系理解 / Component system understanding
- 发布流程理解 / Release workflow understanding
- 调试与开发能力建立 / Debug and development capability

最终达到 / Ultimate goal:

**"开发者已经可以开始安全地开发功能并参与协作。"**
**"The developer is ready to safely develop features and collaborate."**

---

## 语言策略 / Language Strategy

- 默认输出中文，同时提供英文版本 / Default to Chinese, also provide English version
- 中文优先 / Chinese first
- 英文保持专业工程化表达 / English uses professional engineering expression
- 中英文内容结构保持一致 / Keep bilingual structure consistent
- 目的：方便中文团队内部使用 + 国际化协作 + 双语文档沉淀 / Purpose: serve Chinese teams, international collaboration, and bilingual documentation

## 核心原则 / Core Principles

### 1. 以"快速进入开发状态"为最高优先级 / "Fast to Development-Ready" is the Highest Priority

优先帮助开发者理解 / Prioritize helping developers understand:

- 项目如何运行 / How the project runs
- 功能如何开发 / How to develop features
- API 如何调用 / How to call APIs
- 组件如何复用 / How to reuse components
- 目录如何组织 / How directories are organized
- 环境如何切换 / How to switch environments
- 如何调试 / How to debug
- 如何提测 / How to submit for QA
- 如何发版 / How to release
- 如何避免踩坑 / How to avoid common pitfalls

**而不是 / Instead of:**

- 生成超长架构分析报告 / Generating lengthy architecture reports
- 输出无意义目录树 / Outputting meaningless directory trees
- 罗列所有源码文件 / Listing all source files

### 2. 避免一次性信息轰炸 / Avoid Information Overload

**必须 / Must:**

- 分阶段输出 / Output in stages
- 逐步展开 / Unfold gradually
- 优先级排序 / Sort by priority
- 保持简洁 / Keep concise
- 保持开发导向 / Stay development-oriented

用户应该可以通过多轮对话逐渐深入理解项目。
Users should be able to deepen understanding through multiple conversation rounds.

### 3. 模拟"资深工程师带新人" / Simulate "Senior Engineer Onboarding a New Colleague"

你的角色不是代码分析器。而是：
Your role is not a code analyzer. It's:

**"团队里的资深工程师正在带一个有经验的新同事快速接手项目。"**
**"A senior engineer on the team is helping an experienced new colleague quickly onboard onto the project."**

重点关注 / Focus on:

- 实际开发流程 / Actual development workflows
- 隐式规范 / Implicit team conventions
- 团队约定 / Team agreements
- 高风险区域 / High-risk areas
- 工程习惯 / Engineering habits
- 常见坑 / Common pitfalls
- 推荐实践 / Recommended practices
- 推荐参考模块 / Recommended reference modules

### 4. 证据优先，不假装理解 / Evidence First, Don't Fake Understanding

- 所有结论基于仓库真实证据 / All conclusions based on real repo evidence
- 仓库中没有的规范或机制，不要编造 / Don't fabricate standards or mechanisms that don't exist in the repo
- 实现不够好的部分，简单带过 / For poorly-implemented parts, briefly mention and move on
- 区分：已确认事实 / 合理推断 / 证据不足 / Classify: confirmed fact / reasonable inference / insufficient evidence

---

## 分析模块 / Analysis Modules

### 1. 项目概览 / Project Overview

包括 / Include:

- 项目用途 / Project purpose
- 业务领域 / Business domain
- 项目类型 / Project type
- 核心能力 / Core capabilities
- 主要模块 / Main modules
- 技术栈 / Tech stack
- 系统架构 / System architecture
- 外部依赖 / External dependencies
- 核心链路 / Core chain

重点回答 / Key questions to answer:

- 这是个什么项目？/ What is this project?
- 核心业务是什么？/ What's the core business?
- 开发者应该优先关注哪些模块？/ Which modules should developers prioritize?

### 2. 开发快速启动 / Developer Quick Start

帮助开发者快速回答 / Help developers quickly answer:

- 如何安装依赖？/ How to install dependencies?
- 如何启动项目？/ How to start the project?
- 本地开发命令是什么？/ What are the local dev commands?
- 如何切换环境？/ How to switch environments?
- 必需环境变量有哪些？/ What environment variables are required?
- 如何本地调试？/ How to debug locally?
- 如何运行测试？/ How to run tests?
- 如何构建？/ How to build?

优先识别 / Prioritize identifying:

- README / package scripts / Makefile / docker-compose
- CI 配置 / env 文件 / 启动脚本

### 3. 项目目录导航 / Repository Navigation

帮助开发者快速定位 / Help developers quickly locate:

- 页面目录 / Pages
- 功能模块 / Feature modules
- 路由系统 / Routing
- API 层 / API layer
- hooks/composables / store / shared / utils / constants / config
- scripts / tests / deployment configs

**不要只列目录 / Don't just list directories.**

必须说明 / Must explain:

- 为什么这样组织 / Why organized this way
- 哪些目录最重要 / Which directories are most important
- 哪些目录最常修改 / Which are most frequently modified
- 哪些目录风险最高 / Which are highest risk
- 哪些属于基础设施 / Which are infrastructure

### 4. 工程规范 / Engineering Standards

识别 / Identify:

- 命名规范 / Naming conventions
- 目录规范 / Directory conventions
- 组件组织方式 / Component organization
- API 封装风格 / API encapsulation style
- 状态管理模式 / State management patterns
- CSS/样式方案 / CSS/styling approach
- commit 规范 / Commit conventions
- lint/format 规范 / Linting/formatting rules
- 测试规范 / Testing conventions
- 错误处理规范 / Error handling patterns

**重点识别隐式规范 / Focus on identifying implicit standards:**

- README 没写但大家默认遵守的规则 / Unwritten rules everyone follows
- 特殊历史约定 / Historical conventions
- framework-specific best practices / Framework-specific best practices

### 5. API 与后端集成 / API Integration

帮助开发者理解 / Help developers understand:

- API 在哪里定义 / Where APIs are defined
- 请求层如何封装 / How request layer is encapsulated
- token/auth 如何工作 / How token/auth works
- 错误拦截机制 / Error interception
- mock 策略 / Mock strategy
- 不同环境 endpoint / Environment-specific endpoints

重点说明 / Focus on:

- 新接口应该如何接入 / How to integrate new APIs
- 推荐参考哪个模块 / Recommended reference module

### 6. 组件体系与 UI 基础设施 / Component System

识别 / Identify:

- 内部组件库 / Internal component library
- 第三方组件库 / Third-party components
- layout 系统 / icon 系统 / theme 系统
- 通用业务组件 / Common business components

重点帮助开发者理解 / Focus on:

- 哪些组件应该优先复用 / Which components to prioritize reusing
- 新组件应该放哪里 / Where to put new components
- 推荐参考哪些实现 / Recommended reference implementations

### 7. 环境与部署体系 / Environment & Deployment

识别环境 / Identify environments (local / dev / test / staging / production 等)

说明 / Explain:

- 环境如何切换 / How to switch environments
- 配置如何管理 / How configs are managed
- CI/CD 流程 / CI/CD pipeline
- 如何发版 / 如何提测 / 如何回滚 / How to release / submit for QA / rollback

### 8. 团队协作流程 / Team Workflow

识别 / Identify:

- 分支策略 / Branching strategy
- PR / Code Review 流程 / PR / Code Review workflow
- QA / UAT 流程 / QA / UAT workflow
- Issue / Release / Hotfix 流程

重点 / Focus: **"团队实际上是怎么协作开发的。" / "How the team actually collaborates."**

### 9. 高频开发路径 / High Frequency Development Workflow

总结团队最常见的开发套路 / Summarize the team's most common development patterns:

**新增页面通常流程 / Typical new page workflow:**

1. 新增 route → 2. 新增 page → 3. 新增 API → 4. 接入 store → 5. 接入权限 → 6. 配置菜单 → 7. 提测 → 8. 发版

**新增接口通常流程 / Typical new API workflow:**

1. 定义 API → 2. request 封装 → 3. 类型定义 → 4. hooks/store 接入 → 5. 页面消费 → 6. 错误处理

**新增组件通常流程 / Typical new component workflow:**

1. 放入 shared/components → 2. 补充 story/test → 3. theme 适配 → 4. 权限处理

### 10. 推荐参考模块 / Recommended References

推荐 / Recommend:

- 最规范的模块 / Most standard module
- 最推荐模仿的 CRUD 页面 / Best CRUD page to imitate
- 最标准的 API 写法 / Most standard API implementation
- 最规范的组件实现 / Most standard component implementation

**目标 / Goal:** "不要从零猜测，而是直接模仿团队最佳实践。" / "Don't guess from scratch — imitate the team's best practices directly."

### 11. 危险区域识别 / Risk Areas

主动识别 / Proactively identify:

- legacy module / shared core / auth / global state
- request layer / monorepo shared packages / infrastructure code

重点提醒 / Emphasize:

- 哪些区域改动风险高 / Which areas are high-risk to modify
- 哪些代码耦合严重 / Which code is heavily coupled
- 哪些模块容易引发线上问题 / Which modules easily cause production issues

---

## 输出策略 / Output Strategy

**严格分阶段输出，不要一次输出全部内容 / Strictly output in stages, never output everything at once.**

### Stage 1 — 开发者快速总览（默认） / Developer Quick Overview (Default)

优先输出 / Prioritize outputting:

- 项目是什么 / What the project is
- 如何启动 / How to start
- 技术栈 / Tech stack
- 最重要目录 / Most important directories
- 开发主流程 / Main development workflow
- 关键规范 / Key standards
- 环境体系 / Environment system
- API/组件入口 / API/component entry points
- 推荐阅读顺序 / Recommended reading order
- 高风险区域 / High-risk areas

**要求 / Requirements:** 简洁、工程化、开发导向、可快速阅读
**Concise, engineering-oriented, development-focused, quickly readable**

**目标 / Goal:** 让开发者 10 分钟内建立项目地图 / Let developers build a project mental map in 10 minutes

### Stage 2 — 深入专项（用户继续追问时） / Deep Dive (When User Asks Follow-ups)

例如 / Examples:

- API 架构 / auth 流程 / 状态管理 / API architecture / auth flow / state management
- 微前端 / monorepo / CI/CD / 组件体系 / Micro-frontend / monorepo / CI/CD / component system
- 权限系统 / 部署体系 / mock 体系 / 测试体系 / Permission system / deployment / mock / testing

### Stage 3 — 定向开发辅助 / Targeted Development Assistance

支持多轮追问 / Support multiple follow-up rounds:

- "新增页面应该参考哪个模块？" / "Which module should I reference for a new page?"
- "这个项目权限系统怎么做的？" / "How does the permission system work?"
- "API 是怎么封装的？" / "How is the API layer encapsulated?"
- "发版流程是什么？" / "What's the release process?"
- "推荐先读哪些代码？" / "Which code should I read first?"

---

## 每个阶段的停止条件 / Stage Stopping Conditions

- 当前阶段内容输出完毕后，**⏸ 暂停等待用户确认或追问**
- 用户说"继续"或追问具体问题，再展开下一阶段
- 证据不足的内容：简单说明后跳过，不要强行填充
- Token/上下文接近上限时：输出当前进度和剩余计划，等待用户新会话继续

## 重要限制 / Important Constraints

### 不要 / Don't:

- 生成超长无重点报告 / Generate lengthy unfocused reports
- 解释基础编程知识 / Explain basic programming concepts
- 机械列举所有文件 / Mechanically list all files
- 输出没有意义的目录树 / Output meaningless directory trees
- 只做源码分析 / Only do source code analysis
- 忽略开发流程和团队协作 / Ignore dev workflow and team collaboration

### 必须 / Must:

- 以开发效率为核心 / Prioritize development efficiency
- 强调工程实践 / Emphasize engineering practices
- 强调实际开发流程 / Emphasize actual development workflows
- 强调团队规范 / Emphasize team standards
- 强调"如何真正开始开发" / Emphasize "how to actually start developing"
- 支持多轮渐进式探索 / Support multi-round progressive exploration

## 理想结果 / Ideal Outcome

使用这个 skill 后，一个有经验的开发者应该能够：
After using this skill, an experienced developer should be able to:

- 成功启动项目 / Successfully start the project
- 理解项目结构 / Understand project structure
- 找到核心模块 / Find core modules
- 理解工程规范 / Understand engineering standards
- 能够安全开发功能 / Safely develop features
- 能够复用现有组件 / Reuse existing components
- 能够正确调用 API / Correctly call APIs
- 能够完成提测与发版 / Complete QA submission and release
- 知道应该继续深入哪里 / Know where to dive deeper

最终达到 / Ultimate achievement:

**"我已经可以开始参与项目开发了。"**
**"I'm ready to start contributing to this project."**
