# scoring — 评分模型 / Scoring Model

skill-review-pro 的评分体系。总分 100 分，分两阶段。

## Phase 1 — 静态审查评分（50 分）/ Static Review Score

### 一级维度 / Primary Dimensions

| 维度 / Dimension | 分值 / Points | 核心问题 / Core Question |
|---|---|---|
| Reliability / 可靠性 | 16 | Skill 能不能稳定、正确地完成任务？ |
| Engineering / 工程化 | 14 | 写得像工程规范还是 AI 套话？ |
| UX / 用户体验 | 12 | 使用者（人和 AI）用起来顺畅吗？ |
| Maintainability / 可维护性 | 8 | 后续迭代和扩展容易吗？ |

### 二级观察项 / Secondary Observation Signals

二级观察项**不直接参与打分**，作为证据归入对应一级维度：

| 二级观察项 / Signal | 归属维度 / Primary Dimension | 说明 / Description |
|---|---|---|
| Positioning Clarity / 定位清晰度 | Reliability | 能否快速理解 Skill 干什么、不做什么 |
| Instruction Clarity / 指令明确性 | Reliability | 指令有无歧义、矛盾、缺失 |
| Boundary Rationality / 边界合理性 | Reliability | 职责是否聚焦，有无膨胀 |
| Engineering Quality / 工程质量 | Engineering | 结构组织、命名规范、格式一致性 |
| Practicability / 实用性 | Engineering | 真实场景下 AI 能否稳定执行 |
| Information Density / 信息密度 | UX | 信息量是否合理，不轰炸也不贫乏 |
| Interaction Pacing / 交互节奏 | UX | 暂停点是否合理，用户是否疲劳 |
| Modularity / 模块化程度 | Maintainability | 是否便于拆分、扩展、复用 |
| Structure Completeness / 结构完整性 | Maintainability | 核心模块是否齐全 |

### 维度去重 / Deduplication

**同一问题只在一个一级维度扣分。** 归属规则：

- "不知道它干啥" → Reliability
- "写得像 AI 套话" → Engineering
- "用起来太累" → UX
- "改起来很麻烦" → Maintainability

如果一个证据信号同时影响多个维度，在主维度扣分，其他维度用备注标注但不额外扣分。

### 动态权重 / Dynamic Weights

根据 Skill 类型（由主控的路由模块识别），对应一级维度权重 ×1.5，其他 ×0.8。加权后需重新归一化，确保 Phase 1 总分仍为 50 分。

| Skill 类型 | +权重维度 |
|---|---|
| Coding | Reliability, Engineering |
| Teaching | UX, Reliability |
| Workflow | Maintainability, Reliability |
| Analysis | Reliability, Engineering |
| Planning | Maintainability, Engineering |
| Review | Reliability, UX |

如果主控未识别到类型，使用默认权重。

### 评分锚点 / Scoring Anchors

**Reliability（16分）**
- 16分 = 定位清晰、指令无歧义、边界明确、真实场景稳定执行
- 10分 = 能理解但有模糊处，大部分场景可执行
- 5分 = 经常跑偏或指令矛盾

**Engineering（14分）**
- 14分 = 读起来像团队内部工程规范，结构清晰无 AI 套话
- 9分 = 有结构但夹杂套话或格式不统一
- 4分 = 大量空泛描述和口号

**UX（12分）**
- 12分 = 信息密度合理，暂停点恰当，重点突出
- 7分 = 信息略多但可接受，交互基本顺畅
- 3分 = 信息轰炸或过度简略

**Maintainability（8分）**
- 8分 = 模块化清晰，核心模块齐全，便于扩展
- 5分 = 有基本结构但扩展需重写
- 2分 = 巨石结构，改一处影响全局

---

## Phase 2 — 测试执行评分（50 分）/ Test Execution Score

| 维度 / Dimension | 分值 / Points | 评分标准 / Criteria |
|---|---|---|
| Task Completion / 任务完成度 | 20 | 测试用例的完成比例和质量 |
| Output Quality / 输出质量 | 15 | 输出是否专业、结构化、可直接使用 |
| Stability / 稳定性 | 10 | 多个测试间表现是否一致 |
| User Experience / 用户体验 | 5 | 交互节奏、信息密度、是否让用户疲劳 |

### Phase 2 评分锚点

- **任务完成度** 20分=所有测试完整执行且结果正确；12分=大部分完成但有 1-2 个不达标；5分=半数以上失败
- **输出质量** 15分=专业、结构化、可直接使用；9分=有结构但细节不足或偶有空话；3分=输出混乱或大量废话
- **稳定性** 10分=所有测试表现一致，同类问题处理方式相同；6分=大部分一致但有个别波动；2分=表现差异大
- **用户体验** 5分=信息密度合理，重点突出；3分=信息略多但可接受；1分=信息轰炸或过度简略

---

## 评分等级 / Grade Scale

| 分数 / Score | 等级 / Grade | 结论 / Conclusion |
|---|---|---|
| 90-100 | ⭐ 优秀 / Excellent | 可直接发布 / Ready to publish |
| 75-89 | ✅ 良好 / Good | 小幅改进后可发布 / Minor improvements needed |
| 60-74 | ⚠️ 及格 / Pass | 需要较多修改 / Significant improvements needed |
| <60 | ❌ 不及格 / Fail | 建议重新设计 / Recommend redesign |
