# policy: review — 评审类 Skill 评审策略

适用于：代码审查、文档评审、Skill 评审、质量检查等评审类 Skill。

## 评审侧重 / Focus Areas

| 一级维度 | 侧重内容 / Focus |
|---|---|
| Reliability | 评审结论是否准确、是否有遗漏 |
| Engineering | 评分体系是否严谨、规则是否可量化 |
| UX | 评审报告是否清晰易懂、建议是否可执行 |
| Maintainability | 评审标准是否便于扩展和调整 |

## 特殊观察项 / Special Observations

- **判断稳定性 / Judgment Stability** — 同类问题在不同目标上评分是否一致
- **归因准确性 / Attribution Accuracy** — 能否区分目标本身问题 vs 环境问题
- **建议可执行性 / Actionability** — 改进建议是否具体到可直接操作
- **偏见检测 / Bias Detection** — 评审是否存在系统性偏好（如偏爱某种风格）

## 对抗测试建议 / Adversarial Test Suggestions

- 评审一个故意写得很好看但内容空洞的 Skill
- 评审一个风格与评审者截然不同的 Skill
- 评审一个功能正确但格式混乱的 Skill
- 评审一个超长 Skill（测试 context 处理）

## Phase 2 权重调整

Reliability ×1.5, UX ×1.5, Engineering ×0.8, Maintainability ×0.8
