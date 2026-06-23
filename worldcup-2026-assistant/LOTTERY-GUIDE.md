# 体彩选购指南 / Sports Lottery Guide

> 本文件从 worldcup-2026-assistant SKILL.md 拆分而来。当用户询问体彩相关问题时，读取本文件获取详细指南。
> This file is split from the main SKILL.md. Read this file when user asks about sports lottery.

## 功能四：体彩选购指南 / Feature 4: Sports Lottery Guide

### 触发场景 / Trigger Scenarios

- "今天的体彩" / "Today's sports lottery"
- "能买什么比赛" / "What matches can I bet on"
- "体彩赔率" / "Lottery odds"
- "单关串关推荐" / "Single and parlay recommendations"
- "体彩购买时间" / "Lottery purchase hours"

### 体彩基础知识 / Sports Lottery Basics

- **体彩 / Tǐcǎi** = 中国体育彩票（唯一合法足球竞猜渠道）/ China Sports Lottery (only legal channel for football betting)
- **竞彩足球 / Jìngcǎi** = 体彩中的足球竞猜产品，共5种玩法 / Football pools product within Tǐcǎi, 5 play types
- **胜平负 / Shèngpíngfù** = 猜主队胜/平/负，最基础玩法 / Predict home win/draw/loss, most basic play
- **让球胜平负 / Ràngqiú Shèngpíngfù** = 加上让球数的胜平负 / Handicap-adjusted win/draw/loss
- **比分 / Bǐfēn** = 猜具体比分（仅90分钟+补时），31种选项，赔率最高 / Correct score bet, 31 options, highest odds
- **总进球 / Zǒng Jìnqiú** = 猜比赛总进球数（0/1/2/3/4/5/6/7+球，共8个选项）/ Total goals (0-7+, 8 options)
- **半全场胜平负 / Bànquánchǎng** = 猜上半场结果+全场结果的组合（9种：胜胜/胜平/胜负/平胜/平平/平负/负胜/负平/负负）/ Half-time + full-time result combination (9 options)
- **单关 / Dānguān** = 单独买1场比赛 / Bet on a single match
- **串关/过关 / Chuànguān** = 猜多场比赛，全对才赢，赔率累乘 / Parlay: all must win, odds multiply
- **混合过关 / Hùnhé Guòguān** = 一注里面混不同玩法串起来 / Mixed parlay: combine different play types in one bet

### 半全场详解 / Half/Full Details

猜上半场结果 + 全场结果，共9种组合：

| 简称 | 上半场 | 全场 | 典型场景 |
|------|--------|------|---------|
| **胜胜** | 主队领先 | 主队赢 | 强队从头压到尾 |
| **胜平** | 主队领先 | 平局 | 主队先进球后被逼平 |
| **胜负** | 主队领先 | 客队赢 | 大逆转，赔率最高 |
| **平胜** | 平局 | 主队赢 | 下半场发力 |
| **平平** | 平局 | 平局 | 全场闷平 |
| **平负** | 平局 | 客队赢 | 僵持后客队破门 |
| **负胜** | 客队领先 | 主队赢 | 逆转 |
| **负平** | 客队领先 | 平局 | 主队追平 |
| **负负** | 客队领先 | 客队赢 | 客队从头赢到尾 |

- 强队打弱队最常见的两个结果：**胜胜**（全程碾压）、**平胜**（上半场僵持下半场破局）
- **支持单场投注**，赔率比胜平负高
- ⚠️ 跟比分/总进球一样只算90分钟+补时

### 混合过关详解 / Mixed Parlay Details

把不同玩法串在一注里。例如：
> 荷兰「胜平负-胜」+ 德国「半全场-胜胜」+ 厄瓜多尔「让球-让胜」

| 规则 |
|------|
| 最多 8串1（含比分/半全场时降至 4串1） |
| 同一场比赛的**不同玩法可以混串** |
| 同一场比赛的**互斥结果不能串**（如同场「胜」和「平」） |
| 不同比赛的任意玩法可自由组合 |

- ⚠️ 不做主动推荐，除非用户明确问

### ⚠️ 玩法规则速查 / Quick Rules Reference

| 问题 | 答案 |
|------|------|
| 几块钱一注？ | **2元**，最低投注单位 |
| 最多串几场？ | 胜平负/让球 **8串1**；比分/半全场 **4串1**；总进球 **6串1** |
| 混合过关含比分/半全场？ | 最多 **4串1** |
| 比分/半全场能单关吗？ | ✅ 天然支持单场，不用 dg |
| 胜平负/让球能单关吗？ | 只有 dg=1 的场次才能单关，dg=0 必须串 |
| 同一场能同时买比分和让球吗？ | ❌ 每场一注只能选一种玩法 |
| 同一场「胜」和「平」能串吗？ | ❌ 互斥结果不能串 |
| 4串1双选（每场2个）多少注？ | 2⁴ = **16注 × 2元 = 32元** |
| 8串1单挑每场1个多少注？ | 1⁸ = **1注 × 2元 = 2元** |
| 8串247是什么意思？ | 8场全组合容错：2串1~8串1共247注，**494元** |
| 容错过关是什么意思？ | 如 8串9 = 允许错1场（买8个7串1），比8串1贵但容错 |
| 所有玩法算加时赛吗？ | ❌ **只算90分钟+伤停补时**，加时/点球不计 |
| 强弱悬殊场怎么买？ | 胜平负可能不开售，只能买让球或比分/半全场 |
| 赔率哪里查最准？ | 官方 sporttery.cn → zgzcw → autoglm-websearch |

**⏰ 关键规则 / Critical Rule**
所有竞彩足球玩法（胜平负、让球、比分、总进球、半全场）一律**只算90分钟+伤停补时**，淘汰赛也一样！加时赛和点球均不计入。如需猜冠军/晋级方，需专门的"冠军竞猜"玩法
ALL jingcai plays only count 90 min + stoppage time, including knockouts. Extra time and penalties excluded for ALL play types

### 单关与串关详解 / Single Match vs Parlay Details

**什么是单关 / What is Dānguān**
单关 = 只猜1场比赛，买了就走。简单直接，风险可控
单关 = Bet on one match only. Simple, lower risk

**什么是串关 / What is Chuànguān**
串关 = 同时猜2场以上，全对才赢，赔率相乘。如2串1 = 猜2场全对，赔率=场1赔率×场2赔率
串关 = Bet on 2+ matches, all must win, odds multiply. E.g. 2-match parlay: odds = match1 × match2

**⚠️ 单关规则（重要） / Single Bet Rules (Important)**
**比分、总进球、半全场**：天然支持单场投注，可以单独买1场
**胜平负、让球胜平负**：默认至少2串1，只有体彩中心指定的"单关场次"才能单独买
- Correct score, total goals, half/full: single match bet always supported
- Win/draw/loss, handicap: need at least 2-match parlay unless match is designated as "单关"

体彩中心决定哪些场开胜平负单关，不是自动全开
- **强弱悬殊场通常不开单关**：赔率太低（如1.10-1.22），买100才赚十几块
- **豪门焦点战容易开单关**：关注度高、竞猜热度大
- 有些场连胜平负玩法都不开售，只能买让球玩法

**串关上限 / Parlay Limits**
- 胜平负 / 让球胜平负：最多 8串1
- 总进球：最多 6串1
- 比分 / 半全场：传统过关 2串1、3串1；自由过关最多 4串1
- 混合过关：最多 8串1（含比分/半全场时降至4串1）

### 🎯 比分4串1双选战术 / Score 4×1 Dual-Pick Strategy

> 实战验证的高赔率比分玩法策略。投入 16注×2元=32元，全中回报可达百倍以上。
> Battle-tested high-odds strategy. 32 yuan input, 100x+ return if all hit.

**核心思路 / Core Idea：**
1. 每场选 **2 个比分**，覆盖最可能的两个结果
2. 4 串 1 = 2×2×2×2 = **16 注**，每注 2 元 = 总投入 32 元
3. 比分赔率 5-12 倍，4 场相乘 → 数千倍赔率

**选比分原则 / Score Selection Rules：**
- **强队零封**：如德国 vs 弱旅 → 选 2:0 + 3:0
- **实力接近**：两边各押一个小比分 → 1:0 + 0:1（不猜输赢，两边覆盖）
- **可能平局**：1:1 + 0:0 或 1:1 + 0:1
- **原则**：2 个选项必须覆盖不同的比赛走向，不能两个都是主队赢

**实战案例 / Real Case（2026-06-20 实际中奖票）：**

| 场次 | 比分选项 | 策略 |
|------|---------|------|
| 美国 vs 澳大利亚 | 2:0 @7.00 + 2:1 @5.50 | 美国赢2球 |
| 苏格兰 vs 摩洛哥 | 1:1 @5.85 + 0:1 @6.05 | 平 or 摩洛哥小胜 |
| 巴西 vs 海地 | 2:0 @7.20 + 3:0 @5.50 | 巴西零封大胜 |
| 土耳其 vs 巴拉圭 | 1:0 @6.60 + 0:1 @11.50 | 两边覆盖，无论谁1-0都中 |

**结果**：2:0 × 0:1 × 3:0 × 0:1 全中 → 7.00×6.05×5.50×11.50 = **2678 倍** → 32元变 **5357 元**

**何时推荐 / When to Recommend：**
- ✅ 当天有 4 场以上比赛可买
- ✅ 多场强弱对决，强队零封概率高
- ✅ 有 1-2 场实力接近的比赛，需双选覆盖
- ❌ 强弱过分悬殊（如德国 vs 库拉索，胜平负不开售，比分也可能不开）。**输出前必须核实该场赔率是否开售**
- ❌ 当天比赛不足 4 场
- ❌ 用户只想少量投入（32元门槛）

**输出模板 / Output Template：**

```
🎯 比分4串1双选 · 32元
 ・🇦🇷 阿根廷 vs 奥地利：2:0 / 2:1
 ・🇫🇷 法国 vs 伊拉克：3:0 / 4:0
 ・🇳🇴 挪威 vs 塞内加尔：2:1 / 2:0
 ・🇯🇴 约旦 vs 阿尔及利亚：0:2 / 1:2
```

**格式规则 / Format Rules：**
- 标题行固定：`🎯 比分4串1双选 · 32元`
- 每行一场：` ・🇺🇸 主队 vs 🇨🇳 客队：比分1 / 比分2`
- 主队国旗 + 主队 vs 客队国旗 + 客队 + 冒号 + 两个比分用 `/` 分隔
- 不再使用表格、赔率标注、策略说明（简洁为主）
- 可在方案后附上理论奖金计算

**单关查询方式 / How to Check Single Bet Availability**
1. **autoglm-websearch** 搜索（首选）
   - 搜索词：`竞彩足球 X月X日 单关场次` 或 `竞彩足球 X月X日 赔率`
2. **zgzcw.com** web_fetch（如可用，zgzcw 有时被 CloudWAF 拦截）
   - URL: `https://cp.zgzcw.com/lottery/jchtplayvsForJsp.action?lotteryId=47&type=jcmini`
3. **中国体彩APP**（最权威，手机端）

**让球玩法说明 / Handicap Betting Explained**
让球 = 假设强队开场就落后N球，再判胜负
E.g. 法国-1：如果实际2-0 → 让球后1-0 → 法国让球胜；如果2-1 → 让球后1-1 → 让球平
赔率格式：让球胜 / 让球平 / 让球负
强弱差距越大，让球数越多（如伊拉克+2 vs 挪威）

### 📊 期望值分析 / Expected Value Analysis

> 基于价值投注（Value Betting）理论，用数学期望值过滤下注决策。核心思想：只有当 AI 估计的真实概率 × 赔率 > 1 时，长期才有正收益。
> Based on Value Betting theory: only bet when AI-estimated true probability × odds > 1 for long-term positive returns.

**核心公式 / Core Formula：**

1️⃣ **虚拟胜率（庄家隐含概率）= 1 / 赔率**
   - 如阿根廷胜赔率 1.32 → 虚拟胜率 = 1/1.32 = 75.75%
   - 三项虚拟胜率之和 > 100%，超出部分为庄家抽水（通常 8-15%）

2️⃣ **期望值 = (真实概率 × 赔率) - 1**
   - 「真实概率」= 本 skill 的 AI 分析给出的胜率估计
   - 期望值 > 0 = 有长期价值，期望值 < 0 = 长期亏钱

**决策标准 / Decision Criteria：**
- 期望 < 0 → ❌ **不买**
- 期望 0% ~ 5% → ⚠️ **观望**（价值不够）
- 期望 > 5% → 🟡 **轻仓**
- 期望 > 15% → 🟢 **正常投入**

**真实概率估计方法 / How to Estimate True Probability：**
- 根据预测分析的综合维度（实力差、近期状态、交锋记录、核心球员状态）给出百分比
- 高置信度预测 → 胜率 70%+；中高 → 55-70%；中 → 40-55%；中低 → 30-40%；低 → <30%
- 每个赔率选项都要给出对应概率，三项概率之和应接近 100%（不是赔率反推的 112%，而是去抽水后的真实估计）

**串关期望值 / Parlay EV：**
- 串关期望 = (真实概率1 × 真实概率2 × ... × 赔率1 × 赔率2 × ...) - 1
- ⚠️ 串关抽水是指数叠加的，2串1实际抽水约 24%，3串1约 36%，串越多抽水越重
- 因此串关的期望值门槛更高，建议 > 10% 才考虑

**让平高赔率检测规则 / Draw High-Odds Detection Rule：**
- 当让球盘中让平赔率 ≥ 3.40 时，触发检测
- 如果 AI 概率三选项接近均分（各约 30-36%），让平期望值天然为正（因为 0.33 × 3.40 = 1.122 > 1）
- 此时让平是一个 Value Bet，即使 AI 对胜负判断模糊，高赔率本身提供了价值
- ⚠️ 但风险在于：让平需要强队恰好赢让球数，一场没中就全废，串关风险极高
- 建议：让平高赔率可作为单关或 2 串 1 轻仓尝试，不建议多场串关

**使用场景 / When to Use：**
- ✅ 每场推荐都附带期望值计算，作为「买不买」的最终过滤层
- ✅ 串关方案也要算总期望值
- ✅ 用户自行决策时，建议参考期望值而非单纯看赔率高低
- ✅ 让平赔率 ≥ 3.40 时自动触发高赔率检测
- ❌ 不要唯期望值论——AI 概率估计本身有误差，期望值只是辅助工具

**示例 / Example：**
```
📊 期望值分析 · 阿根廷 vs 奥地利

不让球 [0]：
• 阿根廷胜：赔率 1.32 | AI概率 80% | 期望 = 0.80×1.32-1 = +5.6% 🟡轻仓
• 平局：赔率 4.17 | AI概率 15% | 期望 = 0.15×4.17-1 = -37.4% ❌
• 奥地利胜：赔率 7.60 | AI概率 5% | 期望 = 0.05×7.60-1 = -62.0% ❌
庄家抽水：12.89%

💡 结论：仅阿根廷胜有正期望（+5.6%），可轻仓单关
```

### 执行流程 / Workflow

1. 从本地 `schedule.json` 获取当日/次日赛程
2. **必须实时抓取 zgzcw.com 确认单关/赔率/让球数**（见下方强制验证规则）
3. 实时查询体彩销售时间信息
4. **对每场推荐计算期望值**（见上方期望值分析规则）
5. 综合分析输出指南

### ⚠️ 强制验证规则 / Mandatory Verification Rule

**每次输出体彩选购指南或预测时，必须先抓取官方数据验证，禁止凭记忆或搜索片段编造赔率/单关信息！**

MUST fetch live data from zgzcw.com before outputting any lottery guide or prediction. NEVER fabricate odds/single-bet info from memory or search snippets!

**验证步骤 / Verification Steps：**
1. 优先用 autoglm-websearch 搜索 `竞彩足球 X月X日 单关 赔率`，搜索返回的赔率通常可靠
2. 如 web_fetch zgzcw 可用：`curl -s "https://cp.zgzcw.com/lottery/jchtplayvsForJsp.action?lotteryId=47&type=jcmini" -o /tmp/zgzcw_jc.html`，解析 HTML 提取：`dg="1"`=单关可购 / `dg="0"`=只能串关 / `rq`=让球数 / 赔率数值
   - ⚠️ zgzcw 可能被 CloudWAF 拦截，被拦截时跳过此步
3. **检查「未开售」→ 从抓取结果中搜索「未开售」或「停售」文本**
4. 如果以上全失败 → 告知用户「当前无法获取体彩数据，请打开中国体彩APP查看」，不准编造
5. **赔率、单关、让球数、玩法开售状态必须与抓取结果一致，不得自行编造**

### 🔴 解析防错规则 / Parsing Anti-Error Rule

**zgzcw.com 的 HTML 中，每场比赛行内包含多个玩法的赔率数据（胜平负、让球、比分、总进球、半全场），必须严格区分，禁止混用！**
The HTML row for each match contains odds for MULTIPLE play types. Must separate them strictly, NEVER mix values from different play types!

**常见错误 / Common Mistake：**
- ❌ 把比分玩法（22.76 等高赔值）当作让球赔率 → 导致预测回报虚高
- ❌ 把半全场数值混入胜平负

**正确做法 / Correct Approach：**
1. 每场比赛的前 3 个数值（A/B/C）是**胜平负**（主胜/平/客胜）
2. 接着 3 个数值（D/E/F）是**让球胜平负**（让胜/让平/让负）
3. 后续数值是比分/半全场/总进球，只在用户明确问这些玩法时才使用
4. **数值校验**：让球赔率应合理（-2 让球胜通常 1.5~2.5，不可能出现 20+）。如发现异常高值，一定是取错了玩法列！
5. **用户出票后以票面为准**：如果用户发了实际彩票照片，票面上的赔率 > 一切抓取数据。**立即以票面数据覆盖账本！**

### 输出格式 / Output Format

```
🎰 体彩选购指南 · 6月17日

⏰ 购买时间 / Purchase Hours
• 周一至周五：11:00-22:00
• 周六周日：11:00-23:00
• ⚠️ 比赛开赛前约5分钟停止销售

📋 今日可购场次 / Available Matches

1️⃣ 🇫🇷 法国 vs 🇸🇳 塞内加尔 03:00
   胜平负：1.50 / 4.35 / 6.85
   让球（法国-1）：2.10 / 3.40 / 3.20
   单关：✅ 可购
   📊 期望值：法国胜 +12.5% 🟢 | 平 -8.7% ❌ | 负 -52.0% ❌

2️⃣ 🇧🇷 巴西 vs 🇨🇴 哥伦比亚 06:00
   胜平负：1.65 / 3.80 / 5.20
   让球（巴西-1）：2.25 / 3.30 / 2.90
   单关：✅ 可购
   📊 期望值：巴西胜 +3.0% ⚠️观望 | 平 -16.4% ❌ | 负 -40.4% ❌

🎯 串关建议 / Parlay Suggestions
• 2串1稳健：法国胜+德国胜 → 赔率约 2.33
  📊 串关期望：+8.2% 🟡（两场正期望叠加，可轻仓）
• 比分4串1双选：32元以小博大
  📊 串关期望：需4场全中，概率低但赔率高，娱乐性质

📌 今日看点 / Today's Highlights
• 法国vs塞内加尔：期望值最高（+12.5%），首选
• 巴西vs哥伦比亚：期望仅+3%，观望或极轻仓
```

**期望值标注规则 / EV Annotation Rules：**
- 每场推荐必须附带期望值，格式：`📊 期望值：选项 +X.X% 🟢/🟡/⚠️/❌`
- 串关方案也要算总期望值
- 期望值 > 15% 标 🟢，> 5% 标 🟡，0-5% 标 ⚠️，< 0 标 ❌

### 体彩查询要点 / Key Points for Lottery Queries

- **最权威来源 / Most Authoritative**：`https://m.sporttery.cn/mjc/jsq/zqspf/`（中国体彩官方胜平负计算器），需用 autoglm-browser-agent 打开（JS 渲染），curl 不可用
- **备用来源 / Backup**：`https://cp.zgzcw.com/lottery/jchtplayvsForJsp.action?lotteryId=47&type=jcmini`（足彩网），curl + 浏览器 UA 可抓 HTML，解析 dg/让球/赔率
- ⚠️ 体彩官方页面一次只显示 2-3 场，需滚动查看全部比赛

- **赔率 / Odds**：实时查询，体彩赔率会变化，以购买时为准
- **单关信息 / Single Match Availability**：并非所有比赛都开单关，必须查询确认。查询优先级：autoglm-websearch > zgzcw.com(web_fetch，如可用) > 中国体彩APP
- **胜平负未开售 / Win/Draw/Loss Not Available**：强弱悬殊场可能连胜平负都不开售，只能买让球玩法
- **销售时间 / Sales Hours**：工作日和周末不同，注意截止时间
- **让球数 / Handicap Lines**：根据双方实力差距设定，注意让球后赔率变化
- **比分玩法 / Correct Score**：31种比分选项（主队胜13种、平5种、主队负13种，含"胜其他""平其他""负其他"）。**支持单场投注**。赔率最高但命中率低，属于"以小博大"娱乐型，推荐时占比要小，点到为止
- **半全场胜平负 / Half-Full**：9种组合（上半场胜平负 × 全场胜平负），赔率仅次于比分，同样支持单场投注
- **总进球 / Total Goals**：8个选项（0-7+球），支持单场投注
- **⏰ 重要规则 / Important Rule**：所有竞彩足球标准玩法（胜平负、让球、比分、总进球）一律**只算90分钟+伤停补时**，淘汰赛也一样！加时赛和点球均不计入。如需预测冠军/晋级方，需专门的"冠军竞猜"玩法，不是普通胜平负
- **赔率来源 / Odds Source**：必须从中国体彩渠道获取（zgzcw.com等），不用国际盘口作为体彩赔率
- **只推荐中国体彩合法渠道 / Legal Channel Only**：不提及任何境外博彩平台

### ⚠️ 投注方案校验规则 / Bet Plan Validation Rules

**输出体彩选购指南或用户告知投注方案后，必须校验方案是否合法可购！**
After outputting lottery guide or when user mentions their bet plan, MUST validate the plan is legal/purchasable!

**校验步骤 / Validation Steps：**
1. 从 zgzcw.com 抓取的 `dg` 字段判断每场比赛是否开单关
2. **检查每场比赛的玩法是否开售**：抓取时必须检查 HTML 中是否有「未开售」或「停售」标记。强弱悬殊场（如巴西vs海地）可能**胜平负不开售**，只能买让球！输出前必须确认推荐的玩法真实可购
3. 检查用户方案中每注是否满足单关/串关要求：
   - 胜平负/让球胜平负：`dg=0` 的场次**不能单独买（单关）**，必须至少 2 串 1
   - 比分/总进球/半全场：天然支持单场投注，不受 `dg` 限制
4. 如果胜平负未开售（如巴西vs海地仅让球可购）→ **立即警告**：「⚠️ XX 这场胜平负未开售，只能买让球！方案需要调整」
5. 如果用户方案中有不可单买的场次被当作单关 → **立即警告**：「⚠️ XX 这场不能单关，只能串关！请至少再选一场搭配」
6. **互斥检查**：同一场比赛的多注之间不能买互斥结果（如同场平 vs 同场胜，必有一个死）。新增方案时必须检查是否与已有方案在同一场上有互斥投注
7. 输出推荐方案时，同样校验：确保推荐的每注都能实际出票，玩法真实可购，无互斥冲突

### 📡 实时比分查询 / Live Score Query

**用户问比赛结果时，不能只依赖 autoglm-websearch 搜索（搜索索引有延迟，刚结束的比赛可能搜不到）。必须直接抓取实时比分页面！**
When user asks for match results, do NOT rely solely on web search (search index has delay). MUST fetch live score pages directly!

**查询策略 / Query Strategy（按优先级）：**
1. **ESPN API（首选）**：`curl -s "https://site.api.espn.com/apis/site/v2/sports/soccer/fifa.world/scoreboard"`
   - 返回 JSON 格式，含 `name`（队名）、`score`（比分）、`status`（比赛状态/时钟）、`clock`（已过秒数）
   - **已验证可用**，数据准确无需怀疑
2. **autoglm-websearch**：搜索「X vs Y 比分 全场比赛结果」，但必须标注「搜索结果可能有延迟」
3. **81tiyu 比分直播**：`curl -s "https://www.81tiyu.com/TV/bf.aspx?id={id}"`
4. **如果以上全部失败 → 告知用户「当前无法获取实时比分，请稍后再试」，不准空手返回！**

**比分展示规则 / Score Display Rule：**
- **比赛进行中（未完场）**：必须明确标注「🔴 进行中」+ 当前实时比分 + 大致时间（如"下半场 65分钟"）
- **比赛已结束（完场）**：标注「✅ 完场」+ 最终比分
- **抓到比分就是对的**：ESPN API 返回的比分就是实时数据。不要因为后续搜索没找到而怀疑、推翻、否定之前已经抓到的正确比分！第一次抓到就认，不用反复验证

