# testing — 测试设计 / Test Design

skill-review-pro 的测试设计模块。定义如何设计测试用例、对抗测试和回归测试。
本模块引用 **execution** 模块获取当前执行能力，据此设计合适的测试。

## 正常测试 / Normal Tests

### 设计原则

- 模拟真实用户场景，不能是 "hello world" 级别
- 覆盖核心能力和边界场景
- 如果 Skill 是中英双语的，测试用例也应中英覆盖
- 按难度递进：基础功能 → 常规场景 → 困难/边界场景

### 用例结构

每个测试用例包含：
- **测试场景 / Scenario** — 具体的用户输入
- **预期行为 / Expected Behavior** — Skill 应该怎么响应
- **评分标准 / Scoring Criteria** — 什么算好、什么算差
- **归因预判 / Expected Attribution** — 如果失败，最可能的归因类型

### 根据执行模式调整 / Adjust by Execution Mode

读取 execution 模块的当前执行模式，据此调整测试设计：

- **Real** → 设计真实运行测试，验证端到端行为
- **Simulated** → 设计可推演的确定性测试，验证逻辑正确性
- **Restricted** → 设计静态验证测试，验证 Skill 结构和指令完整性

---

## 对抗测试 / Adversarial Tests

**必须包含至少 1 个对抗测试用例。**

同模型设计 + 执行 = 容易"给自己出简单题"。对抗测试防止自欺欺人。

### 对抗类型 / Adversarial Types

| 类型 / Type | 示例 / Example | 期望行为 / Expected Behavior |
|---|---|---|
| 模糊输入 / Ambiguous Input | "帮我搞一下" — 没有明确目标 | 应澄清需求，不应胡乱执行 |
| 不完整需求 / Missing Context | 只给一半必要信息 | 应询问缺失信息，不应自行脑补 |
| 意外输入 / Unexpected Input | 在 Skill 职责范围外的请求 | 应拒绝或重定向，不应强行处理 |
| 低质量表达 / Low-quality Input | 语法混乱、逻辑矛盾的用户输入 | 应尽力理解并确认理解，不应崩溃 |
| 矛盾请求 / Contradictory Request | 同时要求两个互相冲突的目标 | 应指出矛盾并请求澄清 |

### 对抗测试评分

- 被测 Skill 能优雅处理（澄清/拒绝/降级）= 满分
- 部分处理但有遗漏 = 部分分
- 崩溃或胡乱执行 = 0 分

---

## 回归测试 / Regression Testing

如果被测 Skill 有历史评审记录：

### 版本对比 / Version Comparison

- 列出两次评审的维度分数变化
- 标注哪些维度分数下降（⚠️ 回归）
- 多次评审的分数走势

### 变更优先 / Change-focused

如果被测 Skill 提供了变更 diff：
- 优先评审变更部分
- 非变更部分使用历史分数
- 标注变更是否引入新问题

### 报告格式

```markdown
## 回归对比

| 维度 | v1 | v2 | 变化 |
|------|-----|-----|------|
| Reliability | X | X | ⚠️ -X |

**结论**: 稳定 / 发现 X 处回归
```
