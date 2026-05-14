---
name: project-onboarding
homepage: https://github.com/z-Zihan/awesome-skills
description: >
  帮助有经验的开发者快速接手陌生项目，支持前端 Web、后端服务、
  客户端（Electron/Tauri）、小程序、移动端等多种项目类型。自动识别项目类型，分阶段输出
  项目概览、开发流程、工程规范、类型专项指南等，达到"可以开始安全开发"的状态。
  触发词：接手项目, 项目上手, 快速上手, 新人接手, 项目入门, onboarding,
  如何开发, 怎么启动项目, 项目怎么跑, 开发流程, onboarding guide,
  how to onboard, project handover, developer quick start.
  NOT for: generating long architecture reports, code analysis without dev context,
  beginner programming tutorials, onboarding for interns.
---

# project-onboarding — 项目接手指南 / Project Onboarding Guide

帮助有经验的开发者快速理解并接手一个陌生项目，尽快具备实际开发能力。

## 支持的项目类型 / Supported Project Types

按优先级排序 / Priority order:

| 类型 | 识别信号 | 专项模块 |
|---|---|---|
| **前端 Web** | React/Vue/Svelte/Angular, webpack/vite/nextjs | 组件体系、路由、状态管理、CSS 方案、API 集成、浏览器兼容 |
| **后端服务** | Express/Nest/Django/Spring/Gin, ORM/migration | 数据库 Schema、ORM、中间件链、API 设计、认证鉴权、缓存与队列 |
| **客户端** | Electron/Tauri/Capacitor, 主进程/渲染进程 | 主进程架构、渲染进程、IPC 通信、原生能力、签名与分发、自动更新 |
| **小程序** | 微信/支付宝/抖音小程序, app.json/pages.json | 平台适配、分包策略、审核流程、原生能力调用、用户体系 |
| **移动端** | React Native/Flutter/SwiftUI/Kotlin, podfile/gradle | 原生模块 Bridge、热更新、应用签名、应用商店发布、权限管理 |

**多类型混合项目**（如 Electron + Vue、Tauri + React）：同时加载对应专项模块，按优先级排序。

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
- 项目类型特有的核心能力理解 / Type-specific core capabilities
- 发布流程理解 / Release workflow understanding
- 调试与开发能力建立 / Debug and development capability

最终达到 / Ultimate goal:

**"开发者已经可以开始安全地开发功能并参与协作。"**

## 语言策略 / Language Strategy

- 默认输出中文，同时提供英文版本 / Default to Chinese, also provide English version
- 中文优先 / Chinese first

## 核心原则 / Core Principles

### 1. 以"快速进入开发状态"为最高优先级 / "Fast to Development-Ready" is the Highest Priority

优先帮助开发者理解 / Prioritize helping developers understand:

- 项目如何运行 / How the project runs
- 功能如何开发 / How to develop features
- 项目类型特有的核心机制 / Type-specific core mechanisms
- 目录如何组织 / How directories are organized
- 环境如何切换 / How to switch environments
- 如何调试 / How to debug
- 如何发版 / How to release
- 如何避免踩坑 / How to avoid common pitfalls

**而不是 / Instead of:**

- 生成超长架构分析报告 / Generating lengthy architecture reports
- 输出无意义目录树 / Outputting meaningless directory trees
- 罗列所有源码文件 / Listing all source files

### 2. 避免一次性信息轰炸 / Avoid Information Overload

- 分阶段输出 / Output in stages
- 优先级排序 / Sort by priority
- 保持简洁 / Keep concise
- 支持多轮渐进式探索 / Support multi-round progressive exploration

### 3. 模拟"资深工程师带新人" / Simulate "Senior Engineer Onboarding a New Colleague"

你的角色不是代码分析器，而是团队里的资深工程师在带一个有经验的新同事。
Your role is not a code analyzer — it's a senior engineer helping an experienced new colleague onboard.

重点关注 / Focus on:

- 实际开发流程 / Actual development workflows
- 隐式规范 / Implicit team conventions
- 高风险区域 / High-risk areas
- 常见坑 / Common pitfalls
- 推荐参考模块 / Recommended reference modules

### 4. 证据优先，不假装理解 / Evidence First, Don't Fake Understanding

- 所有结论基于仓库真实证据 / All conclusions based on real repo evidence
- 仓库中没有的规范或机制，不要编造 / Don't fabricate standards or mechanisms not in the repo
- 区分：已确认事实 / 合理推断 / 证据不足

### 5. 按项目类型裁剪内容 / Tailor Content by Project Type

- 只分析与当前项目类型相关的模块 / Only analyze modules relevant to the project type
- 不要给后端项目讲组件体系，不要给前端项目讲 ORM
- 混合项目按优先级排序专项模块

---

## 分析模块 / Analysis Modules

### 一、通用模块（所有项目类型）

以下模块适用于任何项目类型，按分析顺序排列：

#### 1. 项目概览 / Project Overview

- 项目用途与业务领域 / Project purpose and business domain
- 项目类型（自动识别）/ Project type (auto-detected)
- 核心能力与主要模块 / Core capabilities and main modules
- 技术栈 / Tech stack
- 系统架构 / System architecture
- 外部依赖 / External dependencies
- 核心链路 / Core chain

#### 2. 开发快速启动 / Developer Quick Start

- 如何安装依赖 / How to install dependencies
- 如何启动项目 / How to start the project
- 本地开发命令 / Local dev commands
- 如何切换环境 / How to switch environments
- 必需环境变量 / Required environment variables
- 如何本地调试 / How to debug locally
- 如何运行测试 / How to run tests
- 如何构建 / How to build

#### 3. 项目目录导航 / Repository Navigation

必须说明 / Must explain:

- 为什么这样组织 / Why organized this way
- 哪些目录最重要 / Which directories are most important
- 哪些目录最常修改 / Which are most frequently modified
- 哪些目录风险最高 / Which are highest risk
- 哪些属于基础设施 / Which are infrastructure

#### 4. 工程规范 / Engineering Standards

- 命名规范 / Naming conventions
- 目录规范 / Directory conventions
- 代码组织方式 / Code organization style
- commit 规范 / Commit conventions
- lint/format 规范 / Linting/formatting rules
- 测试规范 / Testing conventions
- 错误处理规范 / Error handling patterns
- 隐式规范（README 没写但团队默认遵守的规则）/ Implicit standards

#### 5. 环境与部署体系 / Environment & Deployment

- 环境列表（local/dev/test/staging/production 等）/ Environment list
- 环境如何切换 / How to switch environments
- 配置如何管理 / How configs are managed
- CI/CD 流程 / CI/CD pipeline
- 如何发版 / 如何提测 / 如何回滚

#### 6. 团队协作流程 / Team Workflow

- 分支策略 / Branching strategy
- PR / Code Review 流程 / PR / Code Review workflow
- QA / UAT 流程 / QA / UAT workflow

#### 7. 高频开发路径 / High Frequency Development Workflow

总结团队最常见的开发套路（按项目类型定制示例）/ Summarize most common development patterns (examples tailored by project type)

#### 8. 推荐参考模块 / Recommended References

- 最规范的模块 / Most standard module
- 最推荐模仿的实现 / Best implementation to imitate
- 入口文件 / Entry files

#### 9. 危险区域识别 / Risk Areas

- 哪些区域改动风险高 / Which areas are high-risk
- 哪些代码耦合严重 / Which code is heavily coupled
- 哪些模块容易引发线上问题 / Which modules easily cause production issues

---

### 二、前端 Web 专项 / Frontend Web Specific

当识别到前端 Web 项目时加载 / Load when Frontend Web project is detected:

#### A. 组件体系与 UI 基础设施 / Component System & UI Infrastructure

- 内部组件库 / Internal component library
- 第三方组件库 / Third-party components
- layout 系统 / icon 系统 / theme 系统
- 通用业务组件 / Common business components
- 哪些组件应优先复用 / Which components to reuse
- 新组件放哪里 / Where to put new components

#### B. 路由系统 / Routing System

- 路由如何组织 / How routes are organized
- 路由守卫与权限 / Route guards and permissions
- 动态路由 / 懒加载 / Dynamic routes / lazy loading
- 新增页面的路由配置方式 / How to add route for a new page

#### C. 状态管理 / State Management

- 使用的方案（Redux/Pinia/Zustand/Jotai 等）/ Solution used
- 全局状态 vs 局部状态的划分策略 / Global vs local state strategy
- store 如何组织 / How stores are organized
- 新功能应该用全局还是局部状态 / When to use global vs local

#### D. CSS 与样式方案 / Styling Approach

- CSS Modules / Tailwind / CSS-in-JS / styled-components / SCSS
- 设计系统 / token 体系 / Design system / token system
- 样式约定 / Styling conventions

#### E. API 集成 / API Integration

- 请求层如何封装 / How request layer is encapsulated
- token/auth 如何工作 / How token/auth works
- 错误拦截机制 / Error interception
- mock 策略 / Mock strategy
- 新接口应该如何接入 / How to integrate new APIs

**高频开发路径示例（前端 Web）/ High Frequency Workflow Example:**

```
新增页面: 新增 route → 新增 page → 新增 API → 接入 store → 接入权限 → 配置菜单 → 提测 → 发版
新增接口: 定义 API → request 封装 → 类型定义 → hooks/store 接入 → 页面消费 → 错误处理
新增组件: 放入 shared/components → 补充 story/test → theme 适配 → 权限处理
```

---

### 三、后端服务专项 / Backend Service Specific

当识别到 Electron / Tauri / Capacitor 等客户端项目时加载 / Load when Desktop Client project is detected:

#### A. 进程架构 / Process Architecture

**Electron 项目：**
- 主进程（Main Process）职责与入口 / Main process responsibilities and entry
- 渲染进程（Renderer Process）架构 / Renderer process architecture
- 预加载脚本（Preload）与 contextBridge / Preload scripts and contextBridge
- 多窗口管理 / Multi-window management
- 进程间通信（IPC）设计 / IPC design pattern

**Tauri 项目：**
- 前端层（WebView）/ Frontend layer
- Rust 后端层（Tauri Commands）/ Rust backend layer
- IPC 通信方式（invoke/listen） / IPC communication
- 插件系统 / Plugin system
- 安全策略（allowlist/CSP）/ Security policies

#### B. 原生能力集成 / Native Capability Integration

- 文件系统操作（读写、对话框）/ File system operations
- 系统托盘与通知 / System tray and notifications
- 剪贴板 / 屏幕截图 / 全局快捷键 / Clipboard / screenshot / global shortcuts
- 网络状态监听 / Network status monitoring
- 系统信息获取 / System info access
- 原生模块（Node Addons / Rust FFI）/ Native modules

#### C. 签名与分发 / Signing & Distribution

- 开发者证书与签名配置 / Developer certificates and signing config
- macOS: codesign + notary / Windows: 签名证书
- 自动更新机制（autoUpdater）/ Auto-update mechanism
- 更新服务器配置 / Update server config
- 各平台分发渠道（App Store / Microsoft Store / 自建）/ Distribution channels

#### D. 构建与打包 / Build & Packaging

- 构建命令与配置 / Build commands and config
- 多平台构建（macOS arm64/x64 / Windows x64）/ Multi-platform builds
- 安装包格式（DMG/EXE/MSI/AppImage）/ Package formats
- 构建时间优化 / Build time optimization
- CI/CD 中的构建流程 / Build flow in CI/CD

#### E. 客户端特有调试 / Client-Specific Debugging

- 主进程调试 / Main process debugging
- 渲染进程调试（DevTools）/ Renderer process debugging
- IPC 通信调试 / IPC debugging
- 原生能力调试 / Native capability debugging
- 性能分析（CPU/内存/启动速度）/ Performance profiling

**高频开发路径示例（客户端）/ High Frequency Workflow Example:**

```
新增功能: 前端开发 → IPC 通信定义 → 主进程/Rust 命令实现 → 联调 → 测试 → 构建
新增原生能力: 调研 API → 实现 IPC 命令 → 前端调用封装 → 错误处理 → 多平台测试
发版流程: 构建多平台 → 签名 → 公证 → 上传更新服务器 → 灰度 → 全量
```

---

### 四、客户端专项 / Desktop Client Specific

当识别到后端服务项目时加载 / Load when Backend Service project is detected:

#### A. 数据库与存储 / Database & Storage

- 使用的数据库（MySQL/PostgreSQL/MongoDB/Redis 等）/ Database used
- ORM/Query Builder（Prisma/TypeORM/Sequelize/GORM 等）/ ORM used
- Migration 策略 / Migration strategy
- 数据库 Schema 设计思路 / Schema design approach
- 缓存策略（Redis/Memcached）/ Caching strategy
- 文件存储（OSS/S3/本地）/ File storage

#### B. 中间件与请求处理 / Middleware & Request Handling

- 中间件链与执行顺序 / Middleware chain and execution order
- 认证与鉴权（JWT/Session/OAuth）/ Authentication and authorization
- 请求验证与参数校验 / Request validation
- 日志策略 / Logging strategy
- 限流与熔断 / Rate limiting and circuit breaking

#### C. API 设计 / API Design

- RESTful / GraphQL / gRPC / tRPC
- API 版本管理 / API versioning
- 错误码体系 / Error code system
- 文档生成（Swagger/OpenAPI）/ API documentation
- 请求/响应格式约定 / Request/response format conventions

#### D. 异步与任务处理 / Async & Task Processing

- 消息队列（RabbitMQ/Kafka/Redis）/ Message queues
- 定时任务（Cron）/ Scheduled tasks
- 后台任务/Worker / Background jobs/workers
- WebSocket / SSE 长连接 / Long connections

**高频开发路径示例（后端）/ High Frequency Workflow Example:**

```
新增接口: 定义路由 → 参数校验 → 业务逻辑 → 数据库操作 → 返回响应 → 补充测试
新增数据表: 设计 Schema → 创建 Migration → 编写 Model → 实现业务逻辑 → API 接入
新增定时任务: 注册 Cron → 实现任务逻辑 → 日志与监控 → 测试验证
```

---

### 五、小程序专项 / Mini Program Specific

当识别到微信/支付宝/抖音小程序项目时加载 / Load when Mini Program project is detected:

#### A. 平台与框架 / Platform & Framework

- 目标平台（微信/支付宝/抖音/多端）/ Target platform(s)
- 使用原生还是跨端框架（Taro/uni-app） / Native vs cross-platform framework
- 平台 API 差异处理 / Platform API difference handling

#### B. 小程序架构 / Mini Program Architecture

- 页面与组件结构 / Page and component structure
- 全局配置（app.json/pages.json）/ Global config
- 自定义组件封装 / Custom component encapsulation
- 分包策略 / Subpackage strategy
- 插件使用 / Plugin usage

#### C. 用户体系与登录 / User System & Auth

- 登录流程（wx.login 等）/ Login flow
- 用户信息获取与存储 / User info retrieval and storage
- Session 管理 / Session management
- 与后端用户系统的对接 / Integration with backend user system

#### D. 发布与审核 / Publishing & Review

- 审核流程与注意事项 / Review process and notes
- 体验版 / 正式版 发布 / Trial vs production release
- 版本管理与回滚 / Version management and rollback
- 小程序码 / 分享配置 / Mini program code / share config

#### E. 性能优化 / Performance Optimization

- 分包加载 / Subpackage loading
- 图片懒加载 / Image lazy loading
- setData 优化 / setData optimization
- 长列表优化 / Long list optimization
- 自定义组件懒加载 / Component lazy loading

**高频开发路径示例（小程序）/ High Frequency Workflow Example:**

```
新增页面: pages.json 注册 → 创建页面目录 → 实现页面逻辑 → 配置路由 → 提交体验版 → 审核
新增组件: 创建组件目录 → 实现 component → 引入使用 → 样式隔离
新增接口: 封装请求方法 → 页面调用 → 错误处理 → 加载态
```

---

### 六、移动端专项 / Mobile App Specific

当识别到 React Native / Flutter / SwiftUI / Kotlin 等移动端项目时加载 / Load when Mobile App project is detected:

#### A. 应用架构 / App Architecture

- 使用的框架（React Native/Flutter/SwiftUI/Compose）/ Framework used
- 架构模式（MVI/MVVM/Clean Architecture）/ Architecture pattern
- 模块化方案 / Modularization approach
- 导航系统 / Navigation system

#### B. 原生模块与 Bridge / Native Modules & Bridge

- 原生模块列表与用途 / Native module list and purposes
- Bridge 通信机制 / Bridge communication mechanism
- 如何新增原生模块 / How to add new native modules
- 第三方原生 SDK 集成方式 / Third-party native SDK integration

#### C. 状态管理与数据持久化 / State Management & Data Persistence

- 状态管理方案 / State management solution
- 本地存储（AsyncStorage/MMKV/SQLite/CoreData）/ Local storage
- 离线策略 / Offline strategy

#### D. 发布与应用商店 / Release & App Store

- Android: 签名配置（keystore）/ Android signing config
- iOS: 证书与 Profile 管理 / iOS certificate and profile management
- 应用商店提交流程（App Store / Google Play）/ Store submission process
- 热更新方案（CodePush/EAS Update）/ Hot update solution
- TestFlight / 内测分发 / TestFlight / beta distribution

#### E. 移动端特有调试 / Mobile-Specific Debugging

- 真机调试流程 / Physical device debugging
- 性能分析工具 / Performance profiling tools
- 崩溃日志收集 / Crash log collection
- 网络抓包 / Network packet capture

**高频开发路径示例（移动端）/ High Frequency Workflow Example:**

```
新增页面: 创建页面/Screen → 注册路由 → 接入状态 → 接入导航 → 联调接口
新增原生模块: 定义 Bridge 接口 → 实现 Android/iOS 原生代码 → JS 调用封装 → 测试
发版流程: 构建 Android/iOS → 签名 → 上传商店 → 提交审核 → 发布
```

---

## 项目类型自动识别 / Project Type Auto-Detection

分析项目前，先通过以下信号识别项目类型（可多选）:

**前端 Web 信号:**
- `package.json` 中有 react/vue/svelte/angular/next/nuxt
- 存在 webpack.config/vite.config/tsconfig.json
- 存在 public/index.html 或 index.html
- src 下有 pages/views/components/hooks/store 目录

**客户端信号:**
- `package.json` 中有 electron/tauri
- 存在 electron/ 目录或 src-tauri/ 目录
- Capacitor 配置文件
- main process 入口文件

**后端服务信号:**
- `package.json` 中有 express/nest/fastify/koa（Node）
- go.mod / requirements.txt / pom.xml / Cargo.toml
- 存在 migration/ 目录
- Dockerfile / docker-compose.yml

**小程序信号:**
- app.json / pages.json / project.config.json
- Taro/uni-app 配置
- 微信开发者工具配置文件

**移动端信号:**
- android/ 或 ios/ 目录
- Podfile / build.gradle / pubspec.yaml
- App.tsx/AppDelegate.swift（RN/Flutter 入口）
- .xcodeproj / .xcworkspace

识别结果在 Stage 1 开头明确告知用户，如果识别不准确，用户可以手动指定。

---

## 输出策略 / Output Strategy

**严格分阶段输出，不要一次输出全部内容。**

### Stage 1 — 开发者快速总览（默认）/ Developer Quick Overview (Default)

- 项目类型（自动识别结果）/ Project type (auto-detected)
- 项目是什么 / What the project is
- 如何启动 / How to start
- 技术栈 / Tech stack
- 最重要目录 / Most important directories
- 关键规范 / Key standards
- 环境体系 / Environment system
- 推荐阅读顺序 / Recommended reading order
- 高风险区域 / High-risk areas

**目标：让开发者 10 分钟内建立项目地图。**

### Stage 2 — 通用模块深入 / Universal Modules Deep Dive

用户追问时展开目录导航、工程规范、团队协作、环境部署等通用模块。

### Stage 3 — 项目类型专项深入 / Type-Specific Deep Dive

用户追问时展开对应项目类型的专项模块（前端 Web / 后端 / 客户端 / 小程序 / 移动端）。

### Stage 4 — 定向开发辅助 / Targeted Development Assistance

支持多轮追问：

- "新增页面应该参考哪个模块？"
- "权限系统怎么做的？"
- "IPC 通信怎么调的？"
- "发版流程是什么？"

## 每个阶段的停止条件 / Stage Stopping Conditions

- 当前阶段内容输出完毕后，**⏸ 暂停等待用户确认或追问**
- 证据不足的内容：简单说明后跳过，不要强行填充
- Token/上下文接近上限时：输出当前进度和剩余计划

## 重要限制 / Important Constraints

### 不要 / Don't:

- 生成超长无重点报告
- 解释基础编程知识
- 机械列举所有文件
- 输出没有意义的目录树
- 给后端项目讲组件体系，给前端项目讲 ORM
- 忽略开发流程和团队协作

### 必须 / Must:

- 以开发效率为核心
- 按项目类型裁剪内容，只加载相关模块
- 强调工程实践和实际开发流程
- 强调"如何真正开始开发"
- 支持多轮渐进式探索

## 理想结果 / Ideal Outcome

使用这个 skill 后，一个有经验的开发者应该能够：

- 成功启动项目 / Successfully start the project
- 理解项目结构与项目类型特有架构 / Understand project structure and type-specific architecture
- 找到核心模块 / Find core modules
- 理解工程规范 / Understand engineering standards
- 能够安全开发功能 / Safely develop features
- 能够正确使用项目类型特有能力（组件/API/IPC/原生模块等）
- 能够完成提测与发版 / Complete QA submission and release
- 知道应该继续深入哪里 / Know where to dive deeper

最终达到：**"我已经可以开始参与项目开发了。"**
