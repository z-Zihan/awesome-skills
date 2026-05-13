# Changelog

## [Unreleased]

### code-review
- 新增需求完成度 / Bug 修复完成度分析
- 新增"确认变更背景"步骤，主动询问用户变更意图
- 输出改为：无影响变更 → 建议关注 → 需要修复 → 修复指令
- 日志和注释不再作为问题提出

### fe-cli
- 6 种前端项目类型（web / admin / h5 / electron / ssr / miniapp）
- 共享代码层（请求封装 / 样式 / 工具函数 / 环境配置）
- AI 可读项目文档（.ai/PROJECT.md）

### screenshot-to-prompt
- 截图结构识别 + 实现 prompt 生成
- 3 种 UI 策略（骨架 / 自由发挥 / 设计稿还原）
- 多图状态归并
