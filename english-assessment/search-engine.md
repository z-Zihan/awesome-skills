## 搜题引擎

独立模块：搜题策略 + 随机化 + 解析 + 黑名单，测评流程通过「按搜题引擎执行」引用。

⚠️ **静默搜题（强制）**：搜题全过程对考生完全不可见——不在聊天中叙述搜题进度，不展示搜到的原始 URL 或文件路径，搜题失败静默回退。详见核心原则第3条。

### 首题即时策略（减少等待）

- **前 1-3 题用 AI 即时出题**：用户选择模式后，**回复内容直接就是第一道题**，不插入任何工具调用（不读文件、不搜题、不规划试卷结构）。试卷结构规划在考生答第一题后的下一个 turn 里完成
- **搜题与出题并行**：在前几道 AI 题目出题的同时/之后，后台静默搜题，搜到的真题用于后续题目
- **AI 题目不影响比例**：前几题用 AI 出的题计入 AI 出题比例，后续搜题时相应调整，确保整份试卷真题/AI 比例仍在 40-70%/30-60% 范围内
- **前几题选型**：优先选**客观题**（选择题、填空题）作为前几题，因为客观题判分无争议、出题快、考生上手容易

### 搜题源按速度分级

搜题时**优先使用快速源**，慢速源仅作为补充，减少整体等待时间：

- ⚡ **快速（<1秒）**：SEARCH_GITHUB_MD（Markdown 直取）、SEARCH_GITHUB_CET_JSON（JSON 直取）、SEARCH_KOOLEARN / SEARCH_KOOLEARN_TEM4 / SEARCH_KOOLEARN_CET6（网页直抓）、SEARCH_XDF（网页直抓）、Gitee API 目录浏览
- 🟡 **中等（1-3秒）**：SEARCH_GITHUB_CAE（Markdown，含答案）、SEARCH_GITHUB_CET_PDF_REPO（GitHub API 目录浏览 + 下载 + PDF 解析）、SEARCH_GITHUB_KAOYAN（GitHub API 目录浏览 + 下载 + PDF 解析）、SEARCH_GRE_MANHATTAN（海外站，~1.4秒）
- 🐢 **慢速（>3秒）**：SEARCH_VOCABULARY（~0.8秒可用，但页面大需筛选）、SEARCH_OXFORD（~12秒，极慢，但释义权威、例句优质，3%概率出题+分析阶段举一反三优先使用）

**搜题优先级**：⚡ 快速源优先出题 → 🟡 中等源补充多样性 → 🐢 慢速源仅用于词汇查证/难度参考，不依赖其出题。每次测评的真题来源中，⚡快速源占比 ≥ 60%

### 搜题策略（autoglm-websearch 搜题 + web_fetch 抓取正文，按优先级排序）

- **autoglm-websearch 搜题** → 获取 URL → web_fetch 抓取正文。autoglm-websearch 返回 URL 和摘要，再用 web_fetch 抓取页面全文提取真题原文
  - **API 调用方式**：POST `https://autoglm-api.zhipuai.cn/agentdr/v1/assistant/skills/web-search`
  - **请求体**：`{"queries": [{"query": "<搜索词>"}]}`
  - **签名 Headers**（每次动态生成）：
    - `X-Auth-Appid`: `100003`
    - `X-Auth-TimeStamp`: 当前秒级 Unix 时间戳
    - `X-Auth-Sign`: MD5(`100003` + "&" + timestamp + "&" + `38d2391985e2369a5fb8227d8e6cd5e5`)
    - `Authorization`: Bearer token（从 `http://127.0.0.1:18432/get_token` 获取）
  - ⚠️ 注意：app_id 是 `100003` 不是 `10000`；签名必须按上述规则动态生成，不能只传 app_key
- **autoglm-websearch 已验证可搜到的内容源**：SEARCH_KOOLEARN（新东方在线四级，选词填空/翻译/语法真题全文可抓取）、SEARCH_KOOLEARN_TEM4（专四真题+答案，具体年份页面需二次跳转）、SEARCH_KOOLEARN_CET6（六级真题+答案）、SEARCH_XDF（新东方网，阅读/翻译真题原文）
- **GitHub Markdown 真题库（最友好格式，国内用 SEARCH_GH_PROXY 加速）**⭐：SEARCH_GITHUB_MD，含 CET-4/6 2023年真题，Markdown 格式直接使用，选项独立成行，无需 PDF 解析或格式校准。优先级高于 PDF 源。目录浏览：`SEARCH_GH_PROXY/https://api.github.com/repos/wamich/english-exem-md/contents/`，文件下载：`SEARCH_GH_PROXY/https://raw.githubusercontent.com/wamich/english-exem-md/main/{路径}`
- **GitHub CET-4/6 真题 PDF（国内用 SEARCH_GH_PROXY 镜像加速下载+pdf工具解析）**：SEARCH_GITHUB_CET_PDF_REPO，含 2015-2023 年 CET-4/6 真题 PDF。通过 SEARCH_GH_PROXY 代理下载后用 pdf 工具解析，可提取选词填空原文+选项、阅读理解全文+题目、翻译题中文原文。目录浏览：`SEARCH_GH_PROXY/https://api.github.com/repos/DieDiDi/CET4-6-past-exam-paper/contents/{路径}`，文件下载：`SEARCH_GH_PROXY/https://raw.githubusercontent.com/DieDiDi/CET4-6-past-exam-paper/main/{路径}`
- **Gitee CET-4 真题 PDF（国内直连+pdf工具解析）**：SEARCH_GITEE_CET_PDF，含 2013-2020 年 CET-4 真题 PDF。通过 Gitee API 获取 download_url 下载后用 pdf 工具解析。Gitee API: `gitee.com/api/v5/repos/jasonwarner/CET4/contents/{路径}`
- **GitHub CET-4 真题库（国内用 SEARCH_GH_PROXY 镜像加速）**：SEARCH_GITHUB_CET_JSON，含 2023-2025 CET-4 阅读选择题，JSON 格式直接解析（听力部分跳过）。文件下载：`SEARCH_GH_PROXY/https://raw.githubusercontent.com/ShepiTT/CET_practice_questions/main/parsed_data.json`
- **词汇/语法参考站（已验证可抓取）**：SEARCH_VOCABULARY（高频词+释义+真实语料例句）、SEARCH_OXFORD（Oxford 3000/5000+CEFR等级+搭配）
- **GRE 题源**：SEARCH_GRE_MANHATTAN（免费 GRE Verbal 练习题+详细解析，含 Sentence Equivalence 和 Text Completion）
- **考研英语 PDF（国内用 SEARCH_GH_PROXY 加速下载+pdf工具解析）**：SEARCH_GITHUB_KAOYAN，含考研英语一 2002-2021 真题 PDF、六级 2016-2021 真题 PDF。目录浏览：`SEARCH_GH_PROXY/https://api.github.com/repos/youngflysky/KaoYanZhenTi-PDF/contents/{路径}`，文件下载：`SEARCH_GH_PROXY/https://raw.githubusercontent.com/youngflysky/KaoYanZhenTi-PDF/main/{路径}`。考研翻译题可直接用，阅读理解可提取
- **CAE C1 高级英语（Markdown 格式）**⭐：SEARCH_GITHUB_CAE，含 CAE C1 Multiple Choice Cloze、Open Cloze、Word Formation 等题型，Markdown 格式含答案，难度对标 CEFR C1-C2，适合高难度测评。目录浏览：`SEARCH_GH_PROXY/https://api.github.com/repos/gunqiuwang/cae-question-bank/contents/`，文件下载：`SEARCH_GH_PROXY/https://raw.githubusercontent.com/gunqiuwang/cae-question-bank/main/{路径}`
- 搜索专业领域最新术语和表达（科技、医学、法律、金融等）
- 搜索时事热点相关英语表达，确保内容与时俱进
- 搜索外刊原文（经济学人、BBC、NYT、Guardian 等）作为阅读理解和词汇题素材
- 搜索双语对照资源（政府工作报告、UN文件、学术论文摘要）作为翻译题素材
- 搜索商务英语/职场沟通资源作为实用表达题素材
- 搜索英语学习社区高频错题（Reddit r/EnglishLearning、StackExchange 等）作为易错点出题参考

### 搜题黑名单（已验证不可用，不要作为搜题源）

- zhenti.burningvocabulary.cn（PDF查看器，web_fetch抓不到正文）
- 沪江英语/考虫/扇贝/百词斩/中国教育在线（付费墙/SPA/已下线）
- 知乎（403反爬）
- eol.cn 考研频道（正文抓不到）

### 搜题回退规则（全局唯一定义，其他位置引用本规则）

搜题失败时：静默回退AI自身知识出题，不提示用户，但必须按「知识点追踪>冷却期规则」排除已考点。AI 出题也必须保证随机性和多样性（见通用规则第5条）

极端情况：如果本次测评搜题全部失败，或搜到的真题与近期测评重复过多，可以 100% AI 出题。这是唯一允许全 AI 出题的情况

### 搜题随机化策略（防止多次测评搜到同一份题目，多层随机）

- **搜索词随机化**：每次搜题时从以下维度组合生成不同的搜索词，不使用固定搜索词：
  - 年份：从 2019-2025 中随机选（如 "2021年6月"、"2023年12月"）
  - 题型：选词填空/阅读理解/翻译/语法（中英文混用，不含听力）
  - 考试类型：CET-4/CET-6/考研英语/GRE/IELTS/TOEFL/专四专八，随机选不同考试
  - 话题：从话题库中随机选一个（环保/科技/AI/健康/教育/经济/文化/社会/职场/心理学/农业/法律/金融）
  - 示例组合："2023年12月 CET-4 翻译真题" / "GRE sentence equivalence 2024" / "考研英语 阅读理解 科技" / "CET-6 选词填空 环保"
  - **随机组合规则**：每次搜题至少随机2个维度组合（如年份+考试类型、话题+题型），不使用单维度搜索词（如只搜"CET-4"太宽泛）
- **源随机化**：每次测评随机选择搜题源组合（不每次都从同一源搜），⚡快速源占比 ≥ 60%：
  - ⚡ 25% 概率：SEARCH_KOOLEARN / SEARCH_KOOLEARN_TEM4 / SEARCH_KOOLEARN_CET6 / SEARCH_XDF（网页直抓，最快）
  - ⚡ 20% 概率：GitHub Markdown（SEARCH_GITHUB_MD，最友好格式，秒取）
  - ⚡ 15% 概率：GitHub JSON（SEARCH_GITHUB_CET_JSON，JSON 直取，跳过听力题）
  - ⚡ 10% 概率：Gitee CET-4 PDF（SEARCH_GITEE_CET_PDF，国内直连）
  - 🟡 12% 概率：CAE C1 高级英语（SEARCH_GITHUB_CAE，Markdown 格式，C1-C2 难度）
  - 🟡 10% 概率：GitHub PDF（SEARCH_GITHUB_CET_PDF_REPO，需下载+解析）
  - 🟡 5% 概率：考研英语 PDF（SEARCH_GITHUB_KAOYAN，需下载+解析）
  - 🐢 3% 概率：SEARCH_VOCABULARY / SEARCH_OXFORD / SEARCH_GRE_MANHATTAN（词汇/GRE/权威词典，慢但质量高）
  - **同一测评内源轮换**：一次测评中不同题型从不同源搜题，不要所有题都来自同一源；同一源在一次测评中最多贡献40%的搜题量
- **题内随机化**：从搜到的页面/文件中随机选取题目，不从头开始选：
  - PDF：解析全文后随机选不同位置的题目（不总是选第1题）
  - JSON：从 15 套试卷中随机选一套，再从中随机选题
  - 网页：页面内通常有多道题，随机选不同题目
  - **多页随机**：如果搜到的源有多页/多套，随机选页/选套，不总是选第一页/第一套
- **历史去重**：出题前读取 `tested_points.json`，按「知识点追踪>冷却期规则」检查，确保本次搜到的题目不与近期重复。若搜到的真题已被用过，换年份/套号重新搜
- **混合出题**：一次测评中不同题型从不同源搜题，不要所有题都来自同一份试卷
- **年份分散**：一次测评中的真题尽量来自不同年份（不全是同一年的试卷），如果一次搜到了2023年6月的整套卷，只从中选取部分题目，其余从其他年份补充

### 搜题解析策略（搜到真题后如何生成解析）

- **优先搜答案页**：搜到题目后，额外搜索对应的答案/解析页（搜索词加"答案"或"解析"），如"2024年6月四级选词填空答案"。答案页通常有参考答案，部分有解析
- **有官方答案时**：AI 解析必须以官方答案为准，AI 只负责解释"为什么这个答案对"。如果 AI 认为官方答案有误，仍以官方答案为准，但在解析末尾加注「⚠️ 此题存在争议」
- **无官方答案时**（GitHub JSON、部分 PDF）：AI 自行判断正确答案并生成解析，解析末尾标注「💡 此题为 AI 解析，仅供参考」
- **翻译题特殊处理**：SEARCH_XDF/SEARCH_KOOLEARN 上的翻译真题通常附带参考译文，直接作为评分标准。AI 评分时对照参考译文，不以 AI 自己的翻译为准
- **阅读理解特殊处理**：阅读理解需要理解全文才能做对，AI 必须先完整阅读搜到的原文，再基于原文内容解析题目。如果原文不完整（截断），标注「⚠️ 原文不完整，解析可能不准确」
- **听力题跳过**：搜到的整份试卷如果含听力部分，听力选择题跳过（听力无法在文字测评中实现）。但如果试卷附带听力原文（Tape Script / Transcript），可将原文转为阅读理解或翻译题素材——取 news report/passage 短文做阅读理解，取短句做翻译题，对话类（A: ... B: ...）跳过。只提取阅读/翻译/语法/词汇部分
