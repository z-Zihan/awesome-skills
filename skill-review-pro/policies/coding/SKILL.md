# policy: coding — 开发类 Skill 评审策略

适用于：代码生成、项目搭建、代码审查、 scaffolding 等开发类 Skill。

## 评审侧重 / Focus Areas

| 一级维度 | 侧重内容 / Focus |
|---|---|
| Reliability | 生成结果是否正确、可运行、符合预期 |
| Engineering | 技术栈选择、项目结构、代码规范、配置合理性 |
| UX | 使用者是否能快速上手，指令是否直观 |
| Maintainability | Skill 是否便于扩展（如新增框架支持、新增模板） |

## 特殊观察项 / Special Observations

- **确定性 / Determinism** — 同样的输入是否产出一致结构的结果
- **执行稳定性 / Execution Stability** — 多轮调用是否稳定，是否 context 漂移
- **技术准确性 / Tech Accuracy** — 技术选型、API 用法、配置项是否正确

## 对抗测试建议 / Adversarial Test Suggestions

- 需求模糊（只说"搭个项目"，不指定技术栈）
- 技术冲突（要求 React + Vue 混用）
- 超出能力（要求不支持的框架或版本）
- 边界场景（空项目、超大项目、monorepo）

## Phase 2 权重调整

Reliability ×1.5, Engineering ×1.5, UX ×0.8, Maintainability ×0.8
