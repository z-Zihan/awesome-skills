# execution — 执行模式 / Execution Mode

skill-review-pro 的执行能力抽象层。定义测试执行的方式、环境和约束。
本模块同时被**主控**和 **testing** 模块引用。

## 执行模式 / Execution Modes

根据当前运行环境自动选择，或在 Phase 2 开始前手动指定：

| 模式 / Mode | 条件 / Condition | 说明 / Description |
|---|---|---|
| **Real / 真实执行** | 支持 `sessions_spawn` 或可加载 Skill prompt 并独立调用模型 | 在隔离环境中真实执行被测 Skill，记录完整输出 |
| **Simulated / 模拟执行** | 无法隔离执行（如当前环境是单轮对话、无 sub-agent） | 严格按 Skill 指令推演执行过程和预期输出，禁止自行补全逻辑 |
| **Restricted / 受限执行** | 部分工具可用但无法完整隔离 | 能执行但需标注哪些步骤是真实的、哪些是模拟的 |

### 模式切换规则

- 默认尝试真实执行，失败时自动降级为模拟执行
- 模拟执行时**必须明确标注"⚡ 模拟执行"**，不能假装真实执行过
- 模拟执行的要求：严格按被测 Skill 的指令逐步推演，**关键判断点**必须引用对应指令原文

### 测试设计联动 / Testing Integration

testing 模块根据当前执行模式设计不同类型的测试：

| 执行模式 | 可设计的测试类型 |
|---|---|
| Real | 真实运行测试、端到端验证、性能测试 |
| Simulated | 可推演的确定性测试、逻辑验证、路径覆盖 |
| Restricted | 静态验证测试、部分执行测试 |

---

## 失败归因 / Failure Attribution

测试失败 ≠ Skill 差。每次测试失败必须归因，避免错误扣分：

| 归因类型 / Type | 是否扣分 / Deduct | 说明 / Description |
|---|---|---|
| **Skill Design Issue** | ✅ 扣分 | 指令不清、缺少约束、流程漏洞等 Skill 本身的问题 |
| **Runtime Limitation** | ❌ 不扣 | 环境不支持、权限不足、网络问题等 |
| **Tool Unavailable** | ❌ 不扣 | 被测 Skill 依赖的工具在测试环境中不存在 |
| **Model Capability Limitation** | ⚠️ 部分扣 | 模型无法理解复杂指令、超长 context 丢失信息等（扣分不超过该维度 30%） |
| **User Input Issue** | ❌ 不扣 | 测试用例设计不合理或输入有歧义 |

### 归因规则

- 每个测试用例的结果必须标注归因类型
- 归因为"模型能力不足"时，需说明是 Skill 对模型能力假设过高，还是模型本身的限制
- 最终报告中汇总归因分布，帮助用户区分 Skill 问题 vs 环境问题

---

## Context 优化 / Context Optimization

长 Skill（超过 8000 字符）评审时，避免全量重复加载导致 context 膨胀：

1. **首次全量读取** — Phase 1 时完整读取，建立结构索引
2. **后续引用索引** — Phase 2 和修复阶段只引用需要的章节，不重复加载全文
3. **子 skill 抽样** — 多文件 Skill 优先读取主 SKILL.md，子 skill 只读取测试用例涉及的
4. **超长 Skill 抽样评审** — 超过 15000 字符的 Skill，Phase 1 后标注"建议拆分为多个子 skill"
