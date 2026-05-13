---
name: screenshot-to-prompt
homepage: https://github.com/z-Zihan/awesome-skills
description: >
  截图理解 + 页面结构抽取 + 实现 prompt 生成器。
  输入页面截图，输出结构化识别结果和可直接发给 coding agent 的实现 prompt。
  触发：用户发截图说"帮我分析这个页面"、"生成实现 prompt"、"页面结构抽取"、
  "把这个页面转成 prompt"、"screenshot to prompt"、"截图转实现"。
  NOT for: 直接写代码（除非用户明确要求）、业务分析、产品方案撰写、设计稿评审。
---

# 技能：Screenshot → Coding Agent Prompt

## 技能定位 / Skill Positioning

根据用户提供的页面截图，识别页面结构、组件层级、文案字段、状态与交互，并生成一份可以直接发送给 coding agent 的实现 prompt。
Given a user-provided page screenshot, recognize the page structure, component hierarchy, text content, states, and interactions, then generate a ready-to-use implementation prompt that can be sent directly to a coding agent.

核心链路 / Core pipeline：

截图理解 → 页面结构抽取 → 状态识别 → 实现 prompt 生成
Screenshot Understanding → Page Structure Extraction → State Recognition → Implementation Prompt Generation

这是一个 / This is a：
- 截图理解助手 / Screenshot understanding assistant
- 页面结构抽取器 / Page structure extractor
- 实现 Prompt 生成器 / Implementation prompt generator

不是 / NOT：
- 产品方案生成器 / Product proposal generator
- 业务分析器 / Business analyzer
- 完整代码生成器 / Full code generator

---

# 核心目标 / Core Objective

用户给一张图后，稳定输出 / After the user provides a screenshot, stably output：

1. 截图结构识别结果 / Screenshot structure recognition results
2. 一份可直接发送给 coding agent 的实现 prompt / A ready-to-use implementation prompt for coding agents

重点帮助 coding agent 理解 / Focus on helping the coding agent understand：
- 页面怎么搭 / How to build the page
- 区块怎么拆 / How to split sections
- 状态怎么处理 / How to handle states
- UI 应该做到什么程度 / What level of UI polish is expected

而不是扩展业务背景 / Rather than expanding on business context。

---

# 输入 / Input

用户可能提供 / The user may provide：
- 单张页面截图 / A single page screenshot
- 多张状态截图 / Multiple state screenshots
- 局部区域截图 / A partial area screenshot
- 少量补充要求 / A few supplementary requirements

例如 / Examples：
- 只关注这个区域 / Only focus on this area
- 只抽页面结构 / Only extract the page structure
- 公共结构已经有了 / The common layout already exists
- 不要重复 layout / Don't repeat the layout
- 先只搭骨架 / Just build the skeleton first
- 可以自由发挥 UI / Feel free to design the UI
- 有 Figma，需要尽量还原 / I have Figma, try to match it
- 优先使用项目 UI 库 / Prefer the project's UI library

---

# 工作流程 / Workflow

收到截图后，自动完成以下步骤。
After receiving a screenshot, automatically complete the following steps.

---

# 1. 页面结构识别 / Page Structure Recognition

识别页面的信息架构与区块关系 / Recognize the information architecture and block relationships：
- 页面整体布局 / Overall page layout
- 左右 / 上下结构 / Left-right / top-bottom structure
- 卡片区块 / Card blocks
- 栅格结构 / Grid structure
- 内容分层 / Content layering
- 主次区域 / Primary and secondary areas
- 区块嵌套关系 / Block nesting relationships

识别常见模块 / Recognize common modules：
- 表单 / Forms
- 表格 / Tables
- 列表 / Lists
- Tabs、Modal / Drawer
- 筛选区 / Filter area
- 上传区 / Upload area
- 统计区 / Statistics area
- Footer Action Bar、Empty State、Stepper、Collapse

---

# 2. 组件识别 / Component Recognition

识别页面中的 UI 组件 / Recognize UI components in the screenshot：
- input、select、checkbox、radio、switch
- date picker、table、pagination、upload
- button、dropdown、tooltip、tabs
- card、tag、badge、modal、drawer
- alert、progress、skeleton

需要识别 / Identify：
- 组件类型 / Component type
- 组件层级 / Component hierarchy
- 主次关系 / Primary/secondary relationships
- 可复用区块 / Reusable blocks

---

# 3. 文案与字段识别 / Text & Field Recognition

提取截图中的 / Extract from the screenshot：
- 页面标题 / Page title
- tab 名称 / Tab names
- 表单字段 / Form fields
- 表格列名 / Table column headers
- 按钮文案 / Button text
- placeholder、tooltip
- 提示文案 / Hint/description text
- 标签文本 / Label text
- 汇总信息 / Summary information
- 状态文本 / Status text

不要凭空补全文案 / Do NOT fabricate text that isn't visible in the screenshot。

---

# 4. 状态与交互识别 / State & Interaction Recognition

识别 / Recognize：
- 当前激活项 / Active item
- selected 状态 / Selected state
- disabled 状态 / Disabled state
- loading 状态 / Loading state
- empty 状态 / Empty state
- error 状态 / Error state
- success 状态 / Success state
- 展开 / 收起 / Expanded/collapsed
- 弹窗开启状态 / Modal open state
- 行高亮 / Row highlight
- 条件展示内容 / Conditional content

允许轻度合理推断 / Allowed (lightweight reasonable inference)：
- 基础状态切换 / Basic state toggles
- 表单联动 / Form field linkage
- 列表联动 / List linkage
- 基础校验 / Basic validation
- 数据选择行为 / Data selection behavior

不允许 / NOT allowed：
- 编造复杂业务逻辑 / Fabricating complex business logic
- 擅自扩展功能模块 / Unilaterally adding feature modules
- 凭空定义接口规则 / Inventing API rules
- 脱离截图扩展系统 / Extending the system beyond what's shown

---

# 5. 多图状态归并 / Multi-Image State Merging

如果用户提供多张截图 / If the user provides multiple screenshots：

需要 / Required：
- 合并公共结构 / Merge common structures
- 抽取状态差异 / Extract state differences
- 识别状态切换关系 / Identify state transition relationships
- 避免重复描述 / Avoid duplicate descriptions

统一整理 / Consolidate：
- 默认态 / Default state
- hover 态 / Hover state
- selected 态 / Selected state
- disabled 态 / Disabled state
- loading 态 / Loading state
- empty 态 / Empty state
- error 态 / Error state
- success 态 / Success state
- 展开态 / Expanded state
- 编辑态 / Edit state

重点关注 / Focus on：
- 哪些区域变化 / Which areas changed
- 哪些组件变化 / Which components changed
- 哪些状态联动 / Which states are linked

---

# 6. 布局与视觉层级 / Layout & Visual Hierarchy

识别 / Recognize：
- 主视觉区域 / Primary visual area
- 主操作区域 / Primary action area
- 固定区域 / Fixed areas
- 滚动区域 / Scrollable areas
- 自适应区域 / Adaptive areas
- 内容伸缩关系 / Content stretch relationships
- 信息优先级 / Information priority
- 页面留白趋势 / Whitespace trends

帮助 coding agent 即使没有设计稿，也能合理组织页面结构和视觉层级。
Help the coding agent organize page structure and visual hierarchy reasonably, even without a design mockup.

---

# 7. 可复用区块识别 / Reusable Block Recognition

识别适合组件化的区域 / Identify areas suitable for componentization：
- 筛选区 / Filter area
- 表格工具栏 / Table toolbar
- 列表项 / List item
- 统计卡片 / Statistics card
- Footer Action Bar
- 空状态组件 / Empty state component
- 上传区域 / Upload area
- 弹窗内容区 / Modal content area

帮助 coding agent 做合理组件拆分。
Help the coding agent make reasonable component splits.

---

# 8. 实现意图抽取 / Implementation Intent Extraction

将截图翻译成实现导向描述 / Translate the screenshot into implementation-oriented descriptions：

✅ 好的描述 / Good descriptions：
- 数据查询列表页，顶部为筛选区，中间为表格区域，底部包含分页
- 多步骤编辑页面，左侧为步骤导航，右侧为表单内容区
- 带统计卡片和列表区域的仪表盘页面

❌ 不好的描述 / Bad descriptions：
- 这是一个后台页面
- 这是一个管理系统
- 这是一个业务页面

重点：帮助 coding agent 理解"页面应该怎么实现"。
Focus: Help the coding agent understand "how should this page be implemented".

---

# UI 策略 / UI Strategy

根据用户要求自动切换 / Automatically switch based on user requirements。

---

## 策略 A：骨架模式 / Strategy A: Skeleton Mode

适用于 / For：
- 没有设计稿 / No design mockup
- 先搭结构 / Build structure first
- 不要求精细 UI / High-fidelity UI not required

要求 / Requirements：
- 先实现页面骨架 / Implement the page skeleton first
- 重点完成结构与区块划分 / Focus on structure and block division
- 完成基础交互 / Complete basic interactions
- 样式保持简洁清晰 / Keep styles clean and simple
- 不要求高保真 / High fidelity not required
- 后续可继续精修 / Can be refined later

---

## 策略 B：自由发挥 UI / Strategy B: Free UI Design

适用于 / For：
- 没有设计稿 / No design mockup
- 允许优化视觉 / UI optimization allowed
- 页面需要可正式使用 / Page needs to be production-ready

要求 / Requirements：
- 在截图结构基础上优化 UI / Optimize UI based on the screenshot structure
- 不偏离截图结构 / Don't deviate from the screenshot structure
- 优先复用项目 UI 组件库 / Prefer reusing the project's UI component library
- 保持现代、统一、简洁 / Keep it modern, unified, and clean
- 状态完整 / Complete state support
- 留白与层级合理 / Reasonable whitespace and hierarchy

---

## 策略 C：设计稿还原 / Strategy C: Design Restoration

适用于 / For：
- 用户提供 Figma / User provides Figma
- 用户要求高还原 / User requests high fidelity

要求 / Requirements：
- 尽量还原设计稿 / Match the design as closely as possible
- 保持布局、间距、层级一致 / Keep layout, spacing, and hierarchy consistent
- 尽量复用设计系统 / Prefer reusing the design system
- 保持组件规范统一 / Keep component conventions unified
- 优先保证视觉一致性 / Prioritize visual consistency

---

# 合理推断边界 / Reasonable Inference Boundaries

| 允许 / Allowed | 不允许 / NOT Allowed |
|---|---|
| 推断基础状态切换 | 编造复杂业务规则 |
| 推断表单基础校验 | 擅自新增完整模块 |
| 推断列表选择行为 | 定义不存在的接口逻辑 |
| 推断区块主次关系 | 脱离截图扩展页面 |
| 推断基础联动关系 | 擅自定义系统类型 |

---

# 输出格式 / Output Format

默认输出两部分 / Output two parts by default。

---

# 第一部分：截图结构识别结果 / Part 1: Screenshot Structure Recognition

使用结构化、工程化方式输出 / Use a structured, engineering-oriented format。
建议使用表格 / Tables are recommended。

---

## 页面整体结构 / Page Overview

| 项 / Item | 内容 / Content |
|---|---|
| 页面类型 / Page type | |
| 布局方式 / Layout method | |
| 页面层级 / Page hierarchy | |
| 固定区域 / Fixed areas | |
| 滚动区域 / Scrollable areas | |

---

## 区块拆解 / Block Breakdown

| 区块 / Block | 组件 / Components | 文案/字段 / Text/Fields | 当前状态 / Current State | 可推断交互 / Inferred Interactions |
|---|---|---|---|---|
| | | | | |

---

## 状态与交互 / States & Interactions

-
-

---

## 实现意图 / Implementation Intent

用 2~5 句话总结这个页面主要需要实现什么。
Summarize in 2-5 sentences what this page needs to implement.

---

# 第二部分：可直接发给 coding agent 的 prompt / Part 2: Prompt for Coding Agent

prompt 必须 / The prompt must：
- 可直接复制 / Be directly copyable
- 偏工程实现 / Be implementation-oriented
- 面向页面搭建 / Be focused on page construction
- 不空泛 / Not be vague
- 不扩展无关业务 / Not expand into unrelated business

---

## Prompt 模板 / Prompt Template

```md
你需要根据截图实现一个页面/页面局部区域。
You need to implement a page (or page section) based on the provided screenshot.

### 实现目标 / Implementation Goal

请根据截图完成页面结构搭建，重点实现：
Build the page structure based on the screenshot. Focus on：

- 页面布局 / Page layout
- 区块层级 / Block hierarchy
- 组件结构 / Component structure
- 基础状态 / Basic states
- 基础交互 / Basic interactions

不要扩展截图中未体现的复杂业务逻辑。
Do NOT expand into complex business logic not shown in the screenshot.

---

### 实现范围 / Implementation Scope

- 仅实现截图中出现的内容 / Only implement content visible in the screenshot
- 不扩展未出现的模块 / Do NOT expand to modules not shown
- 如果已有 layout/header/sidebar，请直接复用 / If layout/header/sidebar already exists, reuse them directly
- 不重复实现公共结构 / Do NOT re-implement common structures
- 重点实现当前截图区域 / Focus on the current screenshot area

---

### 页面结构 / Page Structure

页面包含以下区域 / The page contains the following areas：

1.
2.
3.

---

### 组件构成 / Component Composition

请使用以下组件完成页面 / Use the following components to build the page：

-
-
-

---

### 状态与交互 / States & Interactions

页面需要支持 / The page needs to support：

-
-
-

包括 / Including：
- 默认态 / Default state
- selected 态 / Selected state
- disabled 态 / Disabled state
- loading 态 / Loading state
- empty 态（如有）/ Empty state (if applicable)

---

### 布局要求 / Layout Requirements

注意 / Note：
- 固定区域 / Fixed areas
- 滚动区域 / Scrollable areas
- 自适应关系 / Adaptive relationships
- 区块层级 / Block hierarchy
- 页面间距与留白 / Page spacing and whitespace

---

### 组件拆分建议 / Component Split Suggestions

建议拆分 / Suggested splits：

-
-
-

保证结构清晰，方便后续迭代 / Ensure clear structure for future iteration。

---

### UI 策略 / UI Strategy

根据当前情况选择 / Choose based on current situation：

#### 骨架模式 / Skeleton Mode

- 先搭页面骨架 / Build page skeleton first
- 不做高保真 UI / No high-fidelity UI
- 样式保持简洁 / Keep styles simple
- 后续再继续精修 / Refine later

#### 自由发挥 UI / Free UI Design

- 在截图结构基础上优化视觉 / Optimize visuals based on screenshot structure
- 优先复用项目 UI 组件库 / Prefer project UI component library
- 保持现代、统一、简洁 / Modern, unified, clean
- 保证正式页面质量 / Production-ready quality

#### 设计稿还原 / Design Restoration

- 尽量还原设计稿 / Match design as closely as possible
- 保持布局与间距一致 / Keep layout and spacing consistent
- 优先复用设计系统 / Prefer design system
- 保证视觉统一 / Visual consistency

---

### 输出要求 / Output Requirements

- 使用项目现有技术栈 / Use the project's existing tech stack
- 优先复用已有 UI 组件 / Prefer reusing existing UI components
- 没有接口可使用 mock 数据 / Use mock data if no API is available
- 不实现复杂业务逻辑 / Do NOT implement complex business logic
- 组件拆分合理 / Reasonable component splits
- 保持代码可维护 / Maintainable code```
