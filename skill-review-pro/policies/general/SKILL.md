# policy: general — 通用 Skill 评审策略

默认策略，当无法识别 Skill 类型时使用。也适用于通用助手、工具封装、混合功能等 Skill。

## 评审侧重 / Focus Areas

| 一级维度 | 侧重内容 / Focus |
|---|---|
| Reliability | 核心功能是否正确、是否能稳定完成任务 |
| Engineering | 结构是否清晰、指令是否明确 |
| UX | 使用是否直观、交互是否顺畅 |
| Maintainability | 是否便于迭代和扩展 |

## 特殊观察项 / Special Observations

- 使用默认的二级观察项，不额外添加类型特有项
- 评分使用默认权重，不调整

## 对抗测试建议 / Adversarial Test Suggestions

- 模糊输入（不明确的需求）
- 职责外请求（超出 Skill 范围的请求）
- 不完整输入（缺少必要参数）
