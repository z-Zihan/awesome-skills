# base: maintainability — 可维护性基础 / Maintainability Foundation

所有 Skill 类型共享的可维护性评审基础。

## 核心问题 / Core Question

后续迭代和扩展容易吗？

## 二级观察项 / Secondary Observations

- **Structure Completeness / 结构完整性** — 核心模块是否齐全
- **Modularity / 模块化程度** — 是否便于拆分、扩展、复用
- **Publishing Compatibility / 发布兼容性** — 是否符合平台发布限制

## 评审要点 / Review Points

- 是否有清晰的结构组织（章节分明、层级合理）
- 核心模块是否齐全（目标、流程、约束、输出）
- 子 skill 组织是否合理（如果有多文件结构）
- 新增功能是否需要大规模重写还是局部修改即可
- 是否有硬编码或魔法值限制扩展性
- **ClawHub embedding 限制**：整个 skill 目录（含子目录）总内容会被 `text-embedding-ada-002` embedding，最大 **8192 tokens**（约 32KB 文本）。如果总内容超限，发布到 ClawHub 会报错 `Invalid 'input': maximum context length is 8192 tokens`。评审时应：
  - 检查 skill 目录总大小，如果超过 25KB（留安全余量）应标为问题
  - 主 SKILL.md 建议控制在 14KB 以内，预留子目录空间
  - 如果因总量超限需要排除子目录，评估子目录内容是否为核心功能（非核心子 skill 排除后不影响主功能则可接受）
- **客户端功能兼容**：Skill 输出中的关键标记（标题、格式）应能被客户端正确识别。例如：
  - 修复指令块标题如使用特定文字（如 `## Code Review 修复任务`），不得随意更改，否则客户端可能无法识别对应功能按钮
  - 评审时应检查 Skill 中是否有依赖客户端解析的固定格式，如果有，确认格式是否明确标注且不易被误改

## 评分锚点 / Scoring Anchors (Maintainability 维度内)

评分锚点的完整定义见 `scoring/SKILL.md` 中的"评分锚点"章节。

综合锚点：
- 8 分=模块化清晰，核心模块齐全，发布兼容，便于扩展
- 5 分=有基本结构但扩展需重写，或发布有超限风险
- 2 分=巨石结构，改一处影响全局，或发布必定失败
