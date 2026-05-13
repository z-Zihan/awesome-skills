---
name: screenshot-to-prompt
homepage: https://github.com/z-Zihan/awesome-skills
description: >
  Screenshot understanding + page structure extraction + implementation prompt generator.
  Input a page screenshot, output structured recognition results and a ready-to-use implementation
  prompt for coding agents.
  Triggers: user sends a screenshot and says "帮我分析这个页面", "生成实现 prompt", "页面结构抽取",
  "把这个页面转成 prompt", "screenshot to prompt", "截图转实现".
  NOT for: directly writing code (unless explicitly requested), business analysis, product proposal
  writing, design review.
---

# Skill: Screenshot → Coding Agent Prompt

## Skill Positioning / 技能定位

Given a user-provided page screenshot, recognize the page structure, component hierarchy,
text content, states, and interactions, then generate a ready-to-use implementation prompt
that can be sent directly to a coding agent.

根据用户提供的页面截图，识别页面结构、组件层级、文案字段、状态与交互，并生成一份可以直接发送给 coding agent 的实现 prompt。

Core pipeline / 核心链路：

Screenshot Understanding → Page Structure Extraction → State Recognition → Implementation Prompt Generation

截图理解 → 页面结构抽取 → 状态识别 → 实现 prompt 生成

This is a / 这是一个：
- Screenshot understanding assistant / 截图理解助手
- Page structure extractor / 页面结构抽取器
- Implementation prompt generator / 实现 Prompt 生成器

NOT / 不是：
- Product proposal generator / 产品方案生成器
- Business analyzer / 业务分析器
- Full code generator / 完整代码生成器

---

# Core Objective / 核心目标

After the user provides a screenshot, stably output:

1. Screenshot structure recognition results / 截图结构识别结果
2. A ready-to-use implementation prompt for coding agents / 可直接发送给 coding agent 的实现 prompt

Focus on helping the coding agent understand:
重点帮助 coding agent 理解：
- How to build the page / 页面怎么搭
- How to split sections / 区块怎么拆
- How to handle states / 状态怎么处理
- What level of UI polish is expected / UI 应该做到什么程度

Rather than expanding on business context.
而不是扩展业务背景。

---

# Input / 输入

The user may provide:
用户可能提供：
- A single page screenshot / 单张页面截图
- Multiple state screenshots / 多张状态截图
- A partial area screenshot / 局部区域截图
- A few supplementary requirements / 少量补充要求

Examples / 例如：
- Only focus on this area / 只关注这个区域
- Only extract the page structure / 只抽页面结构
- The common layout already exists / 公共结构已经有了
- Don't repeat the layout / 不要重复 layout
- Just build the skeleton first / 先只搭骨架
- Feel free to design the UI / 可以自由发挥 UI
- I have Figma, try to match it / 有 Figma，需要尽量还原
- Prefer the project's UI library / 优先使用项目 UI 库

---

# Workflow / 工作流程

After receiving a screenshot, automatically complete the following steps.
收到截图后，自动完成以下步骤。

---

# 1. Page Structure Recognition / 页面结构识别

Recognize the information architecture and block relationships:
识别页面的信息架构与区块关系，包括：
- Overall page layout / 页面整体布局
- Left-right / top-bottom structure / 左右 / 上下结构
- Card blocks / 卡片区块
- Grid structure / 栅格结构
- Content layering / 内容分层
- Primary and secondary areas / 主次区域
- Block nesting relationships / 区块嵌套关系

Recognize common modules:
识别常见模块：
- Forms / 表单
- Tables / 表格
- Lists / 列表
- Tabs
- Modal / Drawer
- Filter area / 筛选区
- Upload area / 上传区
- Statistics area / 统计区
- Footer Action Bar
- Empty State
- Stepper
- Collapse

---

# 2. Component Recognition / 组件识别

Recognize UI components in the screenshot:
识别页面中的 UI 组件，例如：
- input, select, checkbox, radio, switch
- date picker, table, pagination, upload
- button, dropdown, tooltip, tabs
- card, tag, badge, modal, drawer
- alert, progress, skeleton

Identify:
需要识别：
- Component type / 组件类型
- Component hierarchy / 组件层级
- Primary/secondary relationships / 主次关系
- Reusable blocks / 可复用区块

---

# 3. Text & Field Recognition / 文案与字段识别

Extract from the screenshot:
提取截图中的：
- Page title / 页面标题
- Tab names / tab 名称
- Form fields / 表单字段
- Table column headers / 表格列名
- Button text / 按钮文案
- Placeholder text
- Tooltip text
- Hint/description text / 提示文案
- Label text / 标签文本
- Summary information / 汇总信息
- Status text / 状态文本

Do NOT fabricate text that isn't visible in the screenshot.
不要凭空补全文案。

---

# 4. State & Interaction Recognition / 状态与交互识别

Recognize:
识别：
- Active item / 当前激活项
- Selected state / selected 状态
- Disabled state / disabled 状态
- Loading state / loading 状态
- Empty state / empty 状态
- Error state / error 状态
- Success state / success 状态
- Expanded/collapsed / 展开 / 收起
- Modal open state / 弹窗开启状态
- Row highlight / 行高亮
- Conditional content / 条件展示内容

Allowed (lightweight reasonable inference):
允许轻度合理推断：
- Basic state toggles / 基础状态切换
- Form field linkage / 表单联动
- List linkage / 列表联动
- Basic validation / 基础校验
- Data selection behavior / 数据选择行为

NOT allowed / 不允许：
- Fabricating complex business logic / 编造复杂业务逻辑
- Unilaterally adding feature modules / 擅自扩展功能模块
- Inventing API rules / 凭空定义接口规则
- Extending the system beyond what's shown in the screenshot / 脱离截图扩展系统

---

# 5. Multi-Image State Merging / 多图状态归并

If the user provides multiple screenshots:
如果用户提供多张截图：

Required / 需要：
- Merge common structures / 合并公共结构
- Extract state differences / 抽取状态差异
- Identify state transition relationships / 识别状态切换关系
- Avoid duplicate descriptions / 避免重复描述

Consolidate:
统一整理：
- Default state / 默认态
- Hover state / hover 态
- Selected state / selected 态
- Disabled state / disabled 态
- Loading state / loading 态
- Empty state / empty 态
- Error state / error 态
- Success state / success 态
- Expanded state / 展开态
- Edit state / 编辑态

Focus on / 重点关注：
- Which areas changed / 哪些区域变化
- Which components changed / 哪些组件变化
- Which states are linked / 哪些状态联动

---

# 6. Layout & Visual Hierarchy / 布局与视觉层级

Recognize:
识别：
- Primary visual area / 主视觉区域
- Primary action area / 主操作区域
- Fixed areas / 固定区域
- Scrollable areas / 滚动区域
- Adaptive areas / 自适应区域
- Content stretch relationships / 内容伸缩关系
- Information priority / 信息优先级
- Whitespace trends / 页面留白趋势

Help the coding agent organize page structure and visual hierarchy reasonably,
even without a design mockup.
帮助 coding agent 即使没有设计稿，也能合理组织页面结构和视觉层级。

---

# 7. Reusable Block Recognition / 可复用区块识别

Identify areas suitable for componentization:
识别适合组件化的区域，例如：
- Filter area / 筛选区
- Table toolbar / 表格工具栏
- List item / 列表项
- Statistics card / 统计卡片
- Footer Action Bar
- Empty state component / 空状态组件
- Upload area / 上传区域
- Modal content area / 弹窗内容区

Help the coding agent make reasonable component splits.
帮助 coding agent 做合理组件拆分。

---

# 8. Implementation Intent Extraction / 实现意图抽取

Translate the screenshot into implementation-oriented descriptions:
将截图翻译成实现导向描述，例如：

✅ Good descriptions / 好的描述：
- A data query list page with a filter area at the top, a table in the middle, and pagination at the bottom / 数据查询列表页，顶部为筛选区，中间为表格区域，底部包含分页
- A multi-step edit page with step navigation on the left and form content on the right / 多步骤编辑页面，左侧为步骤导航，右侧为表单内容区
- A dashboard page with statistics cards and a list area / 带统计卡片和列表区域的仪表盘页面

❌ Bad descriptions / 不好的描述：
- This is a backend page / 这是一个后台页面
- This is a management system / 这是一个管理系统
- This is a business page / 这是一个业务页面

Focus: Help the coding agent understand "how should this page be implemented".
重点：帮助 coding agent 理解"页面应该怎么实现"。

---

# UI Strategy / UI 策略

Automatically switch based on user requirements.
根据用户要求自动切换。

---

## Strategy A: Skeleton Mode / 策略 A：骨架模式

For / 适用于：
- No design mockup / 没有设计稿
- Build structure first / 先搭结构
- High-fidelity UI not required / 不要求精细 UI

Requirements / 要求：
- Implement the page skeleton first / 先实现页面骨架
- Focus on structure and block division / 重点完成结构与区块划分
- Complete basic interactions / 完成基础交互
- Keep styles clean and simple / 样式保持简洁清晰
- High fidelity not required / 不要求高保真
- Can be refined later / 后续可继续精修

---

## Strategy B: Free UI Design / 策略 B：自由发挥 UI

For / 适用于：
- No design mockup / 没有设计稿
- UI optimization allowed / 允许优化视觉
- Page needs to be production-ready / 页面需要可正式使用

Requirements / 要求：
- Optimize UI based on the screenshot structure / 在截图结构基础上优化 UI
- Don't deviate from the screenshot structure / 不偏离截图结构
- Prefer reusing the project's UI component library / 优先复用项目 UI 组件库
- Keep it modern, unified, and clean / 保持现代、统一、简洁
- Complete state support / 状态完整
- Reasonable whitespace and hierarchy / 留白与层级合理

---

## Strategy C: Design Restoration / 策略 C：设计稿还原

For / 适用于：
- User provides Figma / 用户提供 Figma
- User requests high fidelity / 用户要求高还原

Requirements / 要求：
- Match the design as closely as possible / 尽量还原设计稿
- Keep layout, spacing, and hierarchy consistent / 保持布局、间距、层级一致
- Prefer reusing the design system / 尽量复用设计系统
- Keep component conventions unified / 保持组件规范统一
- Prioritize visual consistency / 优先保证视觉一致性

---

# Reasonable Inference Boundaries / 合理推断边界

| Allowed / 允许 | NOT Allowed / 不允许 |
|---|---|
| Infer basic state toggles / 推断基础状态切换 | Fabricate complex business rules / 编造复杂业务规则 |
| Infer basic form validation / 推断表单基础校验 | Unilaterally add complete modules / 擅自新增完整模块 |
| Infer list selection behavior / 推断列表选择行为 | Define non-existent API logic / 定义不存在的接口逻辑 |
| Infer block priority / 推断区块主次关系 | Extend the page beyond the screenshot / 脱离截图扩展页面 |
| Infer basic linkages / 推断基础联动关系 | Arbitrarily define system types / 擅自定义系统类型 |

---

# Output Format / 输出格式

Output two parts by default.
默认输出两部分。

---

# Part 1: Screenshot Structure Recognition / 第一部分：截图结构识别结果

Use a structured, engineering-oriented format.
使用结构化、工程化方式输出。

Tables are recommended / 建议使用表格。

---

## Page Overview / 页面整体结构

| Item / 项 | Content / 内容 |
|---|---|
| Page type / 页面类型 | |
| Layout method / 布局方式 | |
| Page hierarchy / 页面层级 | |
| Fixed areas / 固定区域 | |
| Scrollable areas / 滚动区域 | |

---

## Block Breakdown / 区块拆解

| Block / 区块 | Components / 组件 | Text/Fields / 文案/字段 | Current State / 当前状态 | Inferred Interactions / 可推断交互 |
|---|---|---|---|---|
| | | | | |

---

## States & Interactions / 状态与交互

- 
- 
- 

---

## Implementation Intent / 实现意图

Summarize in 2-5 sentences what this page needs to implement.
用 2~5 句话总结这个页面主要需要实现什么。

---

# Part 2: Prompt for Coding Agent / 第二部分：可直接发给 coding agent 的 prompt

The prompt must / prompt 必须：
- Be directly copyable / 可直接复制
- Be implementation-oriented / 偏工程实现
- Be focused on page construction / 面向页面搭建
- Not be vague / 不空泛
- Not expand into unrelated business / 不扩展无关业务

---

## Prompt Template / Prompt 模板

```md
You need to implement a page (or page section) based on the provided screenshot.
你需要根据截图实现一个页面/页面局部区域。

### Implementation Goal / 实现目标

Build the page structure based on the screenshot. Focus on:
请根据截图完成页面结构搭建，重点实现：

- Page layout / 页面布局
- Block hierarchy / 区块层级
- Component structure / 组件结构
- Basic states / 基础状态
- Basic interactions / 基础交互

Do NOT expand into complex business logic not shown in the screenshot.
不要扩展截图中未体现的复杂业务逻辑。

---

### Implementation Scope / 实现范围

- Only implement content visible in the screenshot / 仅实现截图中出现的内容
- Do NOT expand to modules not shown / 不扩展未出现的模块
- If layout/header/sidebar already exists, reuse them directly / 如果已有 layout/header/sidebar，请直接复用
- Do NOT re-implement common structures / 不重复实现公共结构
- Focus on the current screenshot area / 重点实现当前截图区域

---

### Page Structure / 页面结构

The page contains the following areas:
页面包含以下区域：

1.
2.
3.

---

### Component Composition / 组件构成

Use the following components to build the page:
请使用以下组件完成页面：

-
-
-

---

### States & Interactions / 状态与交互

The page needs to support:
页面需要支持：

-
-
-

Including / 包括：
- Default state / 默认态
- Selected state / selected 态
- Disabled state / disabled 态
- Loading state / loading 态
- Empty state (if applicable) / empty 态（如有）

---

### Layout Requirements / 布局要求

Note / 注意：
- Fixed areas / 固定区域
- Scrollable areas / 滚动区域
- Adaptive relationships / 自适应关系
- Block hierarchy / 区块层级
- Page spacing and whitespace / 页面间距与留白

---

### Component Split Suggestions / 组件拆分建议

Suggested splits:
建议拆分：

-
-
-

Ensure clear structure for future iteration.
保证结构清晰，方便后续迭代。

---

### UI Strategy / UI 策略

Choose based on current situation:
根据当前情况选择：

#### Skeleton Mode / 骨架模式

- Build page skeleton first / 先搭页面骨架
- No high-fidelity UI / 不做高保真 UI
- Keep styles simple / 样式保持简洁
- Refine later / 后续再继续精修

#### Free UI Design / 自由发挥 UI

- Optimize visuals based on screenshot structure / 在截图结构基础上优化视觉
- Prefer project UI component library / 优先复用项目 UI 组件库
- Modern, unified, clean / 保持现代、统一、简洁
- Production-ready quality / 保证正式页面质量

#### Design Restoration / 设计稿还原

- Match design as closely as possible / 尽量还原设计稿
- Keep layout and spacing consistent / 保持布局与间距一致
- Prefer design system / 优先复用设计系统
- Visual consistency / 保证视觉统一

---

### Output Requirements / 输出要求

- Use the project's existing tech stack / 使用项目现有技术栈
- Prefer reusing existing UI components / 优先复用已有 UI 组件
- Use mock data if no API is available / 没有接口可使用 mock 数据
- Do NOT implement complex business logic / 不实现复杂业务逻辑
- Reasonable component splits / 组件拆分合理
- Maintainable code / 保持代码可维护```
