# policy: workflow — 工作流类 Skill 评审策略

适用于：自动化流程、审批链、多步骤操作、CI/CD 等工作流类 Skill。

## 评审侧重 / Focus Areas

| 一级维度 | 侧重内容 / Focus |
|---|---|
| Reliability | 流程是否完整、步骤是否有遗漏、异常处理是否到位 |
| Engineering | 流程定义是否清晰、条件分支是否覆盖 |
| UX | 用户在流程中是否清楚当前状态和下一步 |
| Maintainability | 流程步骤增删是否方便、新流程模板是否易添加 |

## 特殊观察项 / Special Observations

- **流程完整性 / Process Completeness** — 是否覆盖正常路径和异常路径
- **状态管理 / State Management** — 流程中的状态是否清晰、可追溯
- **错误恢复 / Error Recovery** — 中断后是否能恢复或回退

## 对抗测试建议 / Adversarial Test Suggestions

- 流程中途失败（第 3 步出错了怎么办）
- 用户跳步（直接跳到第 5 步）
- 重复执行（连续触发两次）
- 并发冲突（两个流程同时运行）

## 评分权重调整 / Scoring Weight Adjustment

Maintainability ×1.5, Reliability ×1.5, Engineering ×0.8, UX ×0.8
