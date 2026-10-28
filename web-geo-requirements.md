# 网站做 GEO 的要求说明（让 ChatGPT / Perplexity / Google AI 概述等引用与推荐你的网站）

> 版本：v1，2026-10-28（UTC+8）。只读研究：未登录、未注册、未发帖、未联系任何人、未花钱。
> 素材：禽姐 X 收藏全量（`bm_full.json` 199 条，关键词全量检索）+ 她 star 的 GitHub 仓库（`AgriciDaniel/claude-seo`、`Illyism/seo-skills`，本轮 clone 只读）+ 官方一手文档（本轮打开核对）。
> 标记：**【收藏】** = 来自她的 X 收藏 / star 仓库；**【补充（官方）】** = 我用官方文档补的；**【补充（实践）】** = 我补的通用做法，没有官方背书。
> 原则：不猜数据，取不到写「未取得」。GEO 领域很多说法没有官方证实，下面每条都写了证据强度。

---

## A. 一页纸摘要

### 目标
让网站成为 AI 回答引擎（Google AI Overviews / AI Mode、ChatGPT 搜索、Perplexity、Bing Copilot、Claude）**愿意抓取、能检索到、敢引用**的来源。
官方给的底层逻辑一致：**AI 搜索 = 传统搜索索引 + 检索增强生成（RAG）+ 查询扇出（query fan-out）**。Google 原话：“从 Google 搜索的角度看，针对生成式 AI 搜索做优化就是针对搜索体验做优化，因此仍然是 SEO。”（[Google AI 优化指南](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)）她收藏里 @loki_yan_seo 说的也是这个意思：「GEO 就是 SEO……AI Mode 和 AI Overview 是从 Google 的 Index 里面去掏东西」（[推文](https://x.com/loki_yan_seo/status/2110891254217400371)）。

### 最重要的 5 条要求
1. **先能被收录**：robots 放行搜索类爬虫（Googlebot、Bingbot、OAI-SearchBot、PerplexityBot、Claude-SearchBot），WAF/CDN 不拦；页面能被索引、能显示摘要。不在索引里，就没有被引用的可能。（官方明确）
2. **写非同质化的一手内容**：自有数据、实测、原件整理、方法论；不要把前 10 名的内容重新拼一遍。（Google 指南里排第一的建议，官方明确）
3. **关键事实写在页面顶部、能单独成立**：每页一个主题，开头直接给答案，事实明确写出，实体名称前后一致。（Bing 官方指南第 15–18 条明确写了；Google 说「不需要专门切块」——这条两家说法有差别，见 B②）
4. **信任信号真实可查**：作者/审核人、来源引用、更新日期、About/联系方式、方法论页；YMYL（钱、健康、法律）话题要求更高。（官方明确：Google 有用内容的「谁/怎么/为什么」；E-E-A-T）
5. **用免费的第一方工具监测**：GSC「生成式 AI 效果报告」（2026-08-31 起全球开放，只有展示次数）、Bing Webmaster Tools「AI Performance」（引用次数、被引页面、grounding 查询）、服务器日志里的 AI 爬虫，加上固定问法的手动抽查。（官方明确）

### 不要做的事
刷引用/买推荐/批量自问自答；cloaking（给 AI 爬虫和用户看不同内容）；隐藏文本；结构化数据与页面可见内容不一致；伪造数据、日期、审核人；批量换城市名的薄页；为每个扇出查询各做一页（Google 明确说这属于「规模化内容滥用」）；向页面注入针对大模型的指令（Bing 列为「Prompt Injection and AI Manipulation」）。

### 一句话提醒
**llms.txt、FAQPage schema、「切块」「答案块写 X 个字」这些 GEO 热门做法，Google 都明确说过不需要或已经不给展示**。可以做，但只能当低成本的附加项，不能当成核心。

---

## B. 要求清单（按层）

字段固定：要求｜为什么（机制/证据）｜怎么做｜怎么验证｜怎么判断它失败了｜证据强度｜来源。
证据强度定义：**官方明确**（引擎方文档写了）／**多源实践**（她收藏或社区 ≥2 个独立来源，没有官方背书）／**单源**／**未证实**（有人说，没有数据，或与官方说法矛盾）。

### ① 可抓取与可索引

| # | 要求 | 为什么 | 怎么做 | 怎么验证 | 失败信号 | 证据强度 | 来源 |
|---|---|---|---|---|---|---|---|
| 1.1 | robots.txt 放行**搜索/检索类**AI 爬虫：Googlebot、Bingbot、OAI-SearchBot、PerplexityBot、Claude-SearchBot | 各家官方：OAI-SearchBot 被禁的站不会出现在 ChatGPT 搜索答案里；PerplexityBot 管 Perplexity 搜索结果；Claude-SearchBot 被禁会降低 Claude 搜索可见度；Google AI 功能用 Googlebot 抓的内容 | `User-agent: *` 默认放行即可；如需点名，单独写这几个 UA 的 `Allow: /`。改完 OpenAI/Perplexity 约 24 小时生效 | `curl https://站点/robots.txt`；GSC 网址检查；Bing WMT robots 测试 | 日志里没有这些 UA 的访问；ChatGPT/Perplexity 从来不引用你，但引用同类站 | 官方明确 | 【补充（官方）】[OpenAI bots](https://platform.openai.com/docs/bots)、[Perplexity bots](https://docs.perplexity.ai/guides/bots)、[Anthropic 爬虫说明](https://support.anthropic.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler)、[Google AI features](https://developers.google.com/search/docs/appearance/ai-features) |
| 1.2 | **训练类**爬虫（GPTBot、ClaudeBot、Google-Extended、CCBot、Applebot-Extended）按授权意愿决定，**不要把它们和搜索可见度混为一谈** | OpenAI：GPTBot 只管训练，禁掉它不影响 ChatGPT 搜索；Anthropic：ClaudeBot 只管训练；Google-Extended 不影响 Google 搜索收录和排名 | 想被模型「记住」品牌就放行；有版权顾虑就禁。在文档里写清楚选了哪种、为什么 | 同上 | 误把 GPTBot 当成 ChatGPT 搜索开关（常见误区） | 官方明确 | 【补充（官方）】同上；她 star 的 claude-seo `skills/seo-geo/SKILL.md`「Check the right bot for the claim」表【收藏】 |
| 1.3 | 用户触发类抓取（ChatGPT-User、Perplexity-User、Claude-User）不要被 WAF/机器人防护拦掉 | 用户在对话里让 AI 读你的页面时用这些 UA；OpenAI/Perplexity 说这类请求可能不遵守 robots；Anthropic 说 Claude-User 遵守 robots | WAF 按官方公布的 IP 段（`openai.com/chatgpt-user.json`、`perplexity.com/perplexity-user.json` 等）加白名单，UA 和 IP 同时校验 | 用官方 IP 段比对日志；看 WAF 拦截日志 | 竞品案例：GoodRx 用 PerimeterX 拦非浏览器请求（本地 `ambulance-competitor-geo-analysis.md`），本轮问法里没被引用（样本小，只能算旁证） | 官方明确（机制）／单源（效果） | 【补充（官方）】Perplexity WAF 配置一节；OpenAI bots |
| 1.4 | 页面已被索引，**并且允许显示摘要** | Google：要在 AI Overviews/AI Mode 里作为支撑链接出现，页面必须已编入索引、能带摘要显示；`nosnippet`/`max-snippet`/`noindex` 会限制 AI 功能 | 重要页面不要加 `nosnippet`、`data-nosnippet`；Bing 方面，`NOCACHE` 会让 Copilot 只用 URL/标题/摘要，`NOARCHIVE` 会让内容不进 Copilot 回答 | GSC 网址检查「已编入索引」；Bing WMT URL 检查 | GSC「已抓取-尚未编入索引」比例高 | 官方明确 | 【补充（官方）】[Google AI features](https://developers.google.com/search/docs/appearance/ai-features)、[Bing Webmaster Guidelines §10](https://www2.bing.com/webmasters/help/webmaster-guidelines-30fba23a) |
| 1.5 | GSC 的「Search generative AI」控制项保持「包含」 | Google：站点必须在 Search Console 里被纳入 Search generative AI 功能才有资格展示；默认是包含 | GSC → 设置 → Search generative AI，确认没被改成 Exclude | 看设置页面 | 被误设为排除后，生成式 AI 报告不出数据 | 官方明确 | 【补充（官方）】[GSC 帮助 16908024](https://support.google.com/webmasters/answer/16908024)、[AI 优化指南](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide) |
| 1.6 | sitemap 只列规范 URL，**lastmod 只在内容真的变了才更新** | Bing：sitemap 只列 canonical，准确的 lastmod 加上 ETag 有助于发现变更；全站同一个 lastmod 等于没有更新信号 | 由构建脚本按内容哈希生成 lastmod（ISO 8601）；删除或重定向的 URL 及时移出 | 抽 20 个 URL，对比 lastmod 和页面「更新于」日期 | 全站 lastmod 相同（竞品 ambulancecost 3 万页同一个时间） | 官方明确（Bing）／多源实践 | 【补充（官方）】Bing §3；【收藏】@CoderJeffLee「sitemap.xml 是否完整并正确更新 lastmod」[推文](https://x.com/CoderJeffLee/status/2111317432577274260) |
| 1.7 | 新增、更新、删除 URL 时推送 IndexNow | Bing：IndexNow 能减少 Copilot 回答里过时或错误的 URL；建议逐条实时推送，不要攒批 | 部署钩子里调用 IndexNow API（免费） | Bing WMT IndexNow 报告 | Copilot 引用你已删除或改过的旧内容 | 官方明确（只针对 Bing/Copilot） | 【补充（官方）】Bing §4 |
| 1.8 | 核心内容放在服务端输出的 HTML 里（SSR/SSG） | Google 能渲染 JS；Bing 要求不要把关键内容藏在客户端渲染后面；claude-seo 说公开测试中 GPTBot、PerplexityBot 等很多 AI 爬虫不执行 JS | 正文、表格、价格、FAQ 直接出现在初始 HTML 里；canonical 写在原始 HTML 里 | `curl -A "OAI-SearchBot" URL \| grep 关键数字` | curl 拿到的是空壳 | 官方明确（Bing、Google）／多源实践（AI 爬虫不跑 JS，没有 OpenAI/Perplexity 官方说明） | 【补充（官方）】Bing §8；【收藏】claude-seo `seo-geo` §5 |
| 1.9 | 状态码、重定向、canonical、重复 URL 规范 | Bing：重复 URL 会降低被选作 grounding 来源的信心；永久迁移用 301；删除返回 404。Google：减少重复内容 | 每个内容只有一个 URL；参数页加 canonical；软 404 修成真 404 | Screaming Frog / SiteOne Crawler 全站爬一遍 | 爬虫报告里重复标题、链式跳转、软 404 很多 | 官方明确 | 【补充（官方）】Bing §6–9；【收藏】@sven_ai 上线前 6 个免费检查工具 [推文](https://x.com/sven_ai/status/2113060195777827302)、@loki_yan_seo Screaming Frog [推文](https://x.com/loki_yan_seo/status/2112015156201087419) |
| 1.10 | 页面体验和速度（CWV），移动端可用 | Google 指南列为最佳实践；用户点进来后的体验 | 用 CrUX 看真实用户数据，Unlighthouse 批量跑 | CrUX Vis / PageSpeed | LCP、INP 长期标红 | 官方明确（是最佳实践，没说是 AI 引用因素） | 【收藏】@loki_yan_seo CrUX [推文](https://x.com/loki_yan_seo/status/2109262732763783400)；【补充（官方）】AI 优化指南 |
| 1.11 | URL 用连字符分词，不用下划线 | Google 2026-10-23 更新 URL 结构文档：连字符算分词符，下划线不算 | 新站统一 `kebab-case`；老站有下划线 URL 就 301 | 爬虫导出 URL 列表，grep `_` | — | 官方明确（排名作用小） | 【收藏】@loki_yan_seo [推文](https://x.com/loki_yan_seo/status/2114767197180751881)、@rustybrick [推文](https://x.com/rustybrick/status/2112864300184309773)；【补充（官方）】[Search Central 更新日志 2026-10-23](https://developers.google.com/search/updates) |

### ② 内容结构

| # | 要求 | 为什么 | 怎么做 | 怎么验证 | 失败信号 | 证据强度 | 来源 |
|---|---|---|---|---|---|---|---|
| 2.1 | **非同质化内容**：每页至少有一项别人没有的东西（自有数据、实测、原件整理、截图、失败案例、计算器） | Google：非同质化内容对 AI 搜索可见度的长期影响「可能超过本指南的其他所有建议」；只复述已有信息不行 | 写作前列出「本页独有事实」清单，一项都没有就不发 | 自问：和 SERP 前 10 比，多了什么？ | 被引用的总是竞品或政府原件，不是你 | 官方明确 | 【补充（官方）】AI 优化指南；【收藏】@CoderJeffLee「真正稀缺的是信息增量」[推文](https://x.com/CoderJeffLee/status/2111317432577274260)、@illyism「comparison pages with real information gain」[推文](https://x.com/illyism/status/2110180038637408357)、@NicholasDulait「Is it more useful than the 9 pages next to it?」[推文](https://x.com/NicholasDulait/status/2109909279452868684) |
| 2.2 | **开头直接回答**：H1 下第一段给出结论（数字/范围/条件/日期），不写长铺垫 | Bing：关键信息靠前、避免长引言，被选作 grounding 的概率更高 | 「一句话答案 + 适用条件 + 来源 + 日期」 | 只读首段能不能回答标题问题 | AI 合成答案抽的是你页面别处的文字，或者干脆不引 | 官方明确（Bing §18）／多源实践 | 【补充（官方）】Bing §18；【收藏】claude-seo「Direct answer in first 40-60 words」（第三方启发式） |
| 2.3 | 事实**明确写出、能单独成立**，不依赖上下文和图片 | Bing：内容能独立验证时更容易被引用；事实和定义要写明；图片视频不能是唯一的信息载体 | 不用「如上所述」「见下图」；关键数字用文字写一遍；图片配 alt 和说明 | 把一段单独复制出来，看还能不能读懂 | — | 官方明确（Bing §12、§15） | 【补充（官方）】Bing |
| 2.4 | **一个 URL 一个主题**，标题、H 标签、正文意图一致 | Bing：单主题页面更容易被选作 grounding 来源 | 拆开混杂的页面；标题和 H1 一致 | 人工抽查 | — | 官方明确（Bing §17） | 【补充（官方）】Bing |
| 2.5 | 用清晰的标题层级、段落、列表、**真正的 `<table>`** 组织内容；问题式小标题可以用 | Google：按段落、小节和标题组织对读者有帮助；Bing：用语义 HTML 和合理的标题层级 | 对比/数据用 HTML table，不要用 div 卡片模拟；步骤用 `<ol>` | Nu Html Checker；看源码里有没有 `<table>` | — | 官方明确（结构）／多源实践（「表格更容易被引」，本地竞品观察：WPR、CareCredit 的州表数字被合成答案直接引用） | 【补充（官方）】AI 优化指南、Bing §13；【收藏】claude-seo「Tables for comparative data」；本地 `ambulance-competitor-geo-analysis.md` |
| 2.6 | **不要为 AI 专门「切块」或改写成特定句式；不追求固定字数** | Google 原文：不需要切块，没有理想页面长度，不用为 AI 专门写；Bing 的「靠前、单独成立」是可读性要求，不是字数要求 | 写给人看；直答块长短看问题本身 | — | 把整站改成 40–60 字的碎片，读起来很差 | 官方明确（Google 明确说不需要） | 【补充（官方）】AI 优化指南 Mythbusting；注意：claude-seo 里「130–170 词答案块」「首段 40–60 词」是第三方研究的启发式，**和 Google 立场不一致**，只能当写作习惯 |
| 2.7 | 标出**发布和更新日期**，内容变了才改日期 | Bing：事实变化时及时更新，移除过时信息；Google 有用内容指南把「伪造新鲜度」列为警示信号 | 页面显示「更新于 YYYY-MM-DD」，并写清改了什么；与 `dateModified`、sitemap lastmod 保持一致 | 三处日期对得上 | 每天自动改日期（等于造假） | 官方明确（Bing §19）／「新内容更容易被引用」：多源实践（SE Ranking 研究，claude-seo 转述，未复核） | 【补充（官方）】Bing；【收藏】@codyschneider「每 30 天按 GSC 刷新」[推文](https://x.com/codyschneider/status/2111517654749999271) |
| 2.8 | 覆盖**扇出子问题**，但写在同一主题页或专题集群里，**不要每个变体各做一页** | Google：AI 功能会做 query fan-out；但为每个扇出查询单独做页属于规模化内容滥用 | 用扇出工具拿到子查询 → 归入现有页的小节或支柱页 | 子问题覆盖清单 | 出现大量只差几个词的页面 | 官方明确（机制和红线都写了） | 【收藏】@CoderJeffLee chatgpt-fanout-queries [推文](https://x.com/CoderJeffLee/status/2110215759075164502)、[仓库](https://github.com/JeffLi1993/open-growth-skills/tree/main/chatgpt-fanout-queries)；@alexgroberman「Google can break that question into several related searches」[推文](https://x.com/alexgroberman/status/2111484443726852385)；【补充（官方）】AI 优化指南 |
| 2.9 | 按搜索意图选页面类型：信息型 → 教程/指南，商业型 → 对比/替代/榜单，交易型 → 工具/定价 | 用户能在页面上把事情办完 | 先建「关键词 → 用户任务 → 页面类型」映射表 | — | 工具意图的词配了一篇长文 | 多源实践 | 【收藏】@CoderJeffLee [推文](https://x.com/CoderJeffLee/status/2111317432577274260)、@codyschneider [推文](https://x.com/codyschneider/status/2111517654749999271) |
| 2.10 | 对比页**中立**：竞品比你强的地方要写，每条对比附来源和「截至日期」 | 自己把自己排第一的榜单，LLM 读完会引用其他每个工具，唯独不引你（单源经验）；Illyism 的 seo-autopilot 也要求「Be fair……every claim about a competitor gets a source and an 'as of' date」 | 中立评分方法写在页面上 | — | AI 回答引用了你的榜单，却不提你自己 | 单源（@NicholasDulait 转述的从业者经验）＋ 她 star 仓库的规则 | 【收藏】@NicholasDulait [推文](https://x.com/NicholasDulait/status/2109909279452868684)；`Illyism/seo-skills/seo/seo-autopilot/SKILL.md` |
| 2.11 | 配高质量图片和视频（辅助文字，不替代文字） | Google：AI 功能可能带出图片和视频；Bing：多模态内容要配 alt、字幕、文字稿 | 原创截图、示意图，视频配字幕 | — | — | 官方明确 | 【补充（官方）】AI 优化指南、Bing §12 |

### ③ 实体与信任（E-E-A-T）

| # | 要求 | 为什么 | 怎么做 | 怎么验证 | 失败信号 | 证据强度 | 来源 |
|---|---|---|---|---|---|---|---|
| 3.1 | 署名真实作者；YMYL 页面加**真实、可查**的审核人 | Google 有用内容指南的「谁/怎么/为什么」：读者期待署名的地方要有署名，YMYL 话题权重更高 | 作者页写资历和外部链接；审核人写资质，并链接到可核验的执照或机构页 | 外人能不能在站外查到这个人 | 找不到审核人 → **宁可不写，也不能编** | 官方明确 | 【补充（官方）】[有用内容指南](https://developers.google.com/search/docs/fundamentals/creating-helpful-content)；【收藏】claude-seo「Author byline with credentials」 |
| 3.2 | About 页：谁在做、怎么赚钱（广告/联盟/导流）、利益关系、联系方式 | 信任和透明；Google 站点声誉政策看「署名与编辑责任是否清楚」 | About + Contact + 编辑政策三页，从页脚可达 | — | — | 官方明确（原则）／没有「AI 引用因素」的官方说法 | 【补充（官方）】[Spam policies 站点声誉](https://developers.google.com/search/docs/essentials/spam-policies) |
| 3.3 | **方法论页 + 数据来源页 + 变更日志** | 让「每个数字能回溯到哪个文件」可以验证；Bing：内容能独立验证更容易被引 | `/methodology`：来源、计算方法、更新频率、已知局限；`/changelog`：按日期记录改了什么 | — | 方法论页没有任何外部链接或引用 | 官方明确（原则）／单源（本地竞品观察：s2reason 写「verified against all 10,536 rate cells」后在州级问法被引用） | 本地 `ambulance-competitor-geo-analysis.md`；【补充（官方）】Bing §15 |
| 3.4 | 正文引用一手来源（政府、标准、论文、官方文档），带链接和访问日期 | 可核验；本地观察：UHC 的脚注写了「Updated/Accessed」日期，被合成答案引用 | 脚注编号 + 原件链接 + 访问日期 | 链接死链检查（lychee） | 引用的是二手转述站 | 多源实践 | 【收藏】claude-seo「Citations to primary sources」；@sven_ai lychee |
| 3.5 | 实体名称前后一致（品牌、人名、地名、产品名） | Bing：实体命名清晰一致，可以提高 grounding 可见度和引用准确性 | 一个品牌只用一种写法；首次出现写全称 | 全站 grep 品牌的各种变体 | AI 把你和同名实体混在一起 | 官方明确（Bing §16） | 【补充（官方）】Bing；【收藏】@loki_yan_seo「新词好做是因为实体 Entity 还没有建立好」[推文](https://x.com/loki_yan_seo/status/2110999959084634146) |
| 3.6 | Organization 的 `sameAs` 指向**真实存在的**官方账号（X、GitHub 数据仓库、LinkedIn） | 帮助消歧；Google Organization 文档说部分属性用于知识面板，部分在后台使用 | 只填真实账号；有独立关注度时才考虑 Wikidata/Wikipedia（不能自己写软文） | Rich Results Test | sameAs 指向空号或买来的号 | 官方明确（有 Organization 标记）／「sameAs 提升 AI 引用」：未证实 | 【补充（官方）】[Organization 结构化数据](https://developers.google.com/search/docs/appearance/structured-data/organization)；【收藏】@houzhongji89090 关于 Wikipedia 的说明（「不是一个可以随意购买文章的营销渠道」）[推文](https://x.com/houzhongji89090/status/2112867613546258882) |
| 3.7 | YMYL 免责声明 + 纠错入口 | 用户实际风险；纠错通道本身就是信任信号 | 页面底部写「仅供参考、以原件为准」+「报告数据错误」按钮 | — | — | 多源实践 | 本地竞品观察（ambulancecost「Report Inaccurate Data」） |
| 3.8 | 如果用 AI 辅助写作，要有人工编辑和事实核查，并在合适的位置说明流程 | Google：AI 生成内容可以，但要符合 Search Essentials；用来批量生产低价值页面就是垃圾内容 | 每页记录核查人和日期（内部） | — | — | 官方明确 | 【补充（官方）】[使用生成式 AI 内容](https://developers.google.com/search/docs/fundamentals/using-gen-ai-content) |

### ④ 结构化数据

**先说结论**：结构化数据**不是** AI 功能的必要条件。Google 原文：“Structured data isn't required for generative AI search, and there's no special schema.org markup you need to add.” Bing：“may support clearer grounding but does not guarantee visibility……Markup must accurately reflect visible content.” 做它主要是为了富结果、帮助理解实体，以及不出错。

| 类型 | Google 富结果现状（2026-10） | 对 AI 的作用 | 建议 | 证据强度 / 来源 |
|---|---|---|---|---|
| Organization | 支持（logo、知识面板等） | 实体消歧，作用未量化 | **做**：首页一份，含 name、url、logo、sameAs（只填真实账号）、contactPoint | 官方明确 [Organization](https://developers.google.com/search/docs/appearance/structured-data/organization) |
| WebSite | 用于站点名称；sitelinks 搜索框 2024-11 已下线 | — | 做（站点名称） | 官方明确 [更新日志 2024-11-29](https://developers.google.com/search/updates) |
| Article / BlogPosting | 支持；建议写 author.url，日期要带时区 | 作者、日期信号 | 文章页做；`datePublished`/`dateModified` 用 ISO 8601，和页面显示一致 | 官方明确 |
| BreadcrumbList | 支持，2025-01 起只在桌面端显示 | 层级理解 | 做 | 官方明确 [更新日志 2025-01-22] |
| FAQPage | **2026-05-07 起 Google 不再显示 FAQ 富结果**（2023 年起只给权威政府、医疗站显示），文档已删除；留着无害 | Google 没有说对 AI 有用；Bing 只要求和可见内容一致 | 页面上有真实 FAQ 可以保留标记，**别指望它带来展示**；严禁写页面上没有的问答 | 官方明确（废弃）[更新日志 2026-05-08、06-15](https://developers.google.com/search/updates)；「FAQ schema 帮助 AI 引用」：**未证实** |
| HowTo | 2023-09 起全面废弃 | 未证实 | 不必新做 | 官方明确 [博客 2023-08](https://developers.google.com/search/blog/2023/08/howto-faq-changes) |
| Dataset | **只用于 Google Dataset Search，不用于 Google 搜索**（2025-11 澄清） | 数据型站可以被 Dataset Search 收录 | 有可下载数据（CSV）时做，含 distribution、temporalCoverage、license | 官方明确 [更新日志 2025-11-05] |
| QAPage / DiscussionForum | 支持（适用于用户问答和论坛） | — | 只有真正的问答社区才用 | 官方明确 |
| Product / Review / LocalBusiness | 支持；有自我评价和虚假评价的限制 | Google 说 AI 回答会带商品和本地商家信息，**主渠道是 Merchant Center 和商家资料** | 电商或本地业务才做；评价要真实 | 官方明确 [AI 优化指南](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide) |
| MedicalWebPage、Person 等 | 不产生富结果 | 未证实 | 可选，不作为重点 | 未证实 |
| ClaimReview 等 | 2025 年已退役 | — | 不做 | 官方明确 [博客 2025-06](https://developers.google.com/search/blog/2025/06/simplifying-search-results) |

通用要求（官方明确）：标记必须和页面可见内容一致（Google AI features 页、Bing §14 和「Misleading Structured Data」条）；用 JSON-LD；用 Rich Results Test 加 Schema Markup Validator 验证。她收藏的 @bloggersarvesh 工具清单里有结构化数据测试工具（[推文](https://x.com/bloggersarvesh/status/2109707846241915222)）。

### ⑤ 站点架构

| # | 要求 | 为什么 | 怎么做 | 怎么验证 | 失败信号 | 证据强度 | 来源 |
|---|---|---|---|---|---|---|---|
| 5.1 | 主题地图（Topic Map）/ 主题集群：支柱页 + 子页 + 互相内链 | 把搜索意图组织成专题，而不是零散追关键词；fan-out 子主题要有地方承接 | 知识库 + 关键词表 + 现有 sitemap URL 交给 AI，生成 Topic Map，判断显性和隐性意图 | Topic Map 覆盖率表 | 孤立页多，子主题没有归属 | 多源实践 | 【收藏】@CoderJeffLee 第 5 章 [推文](https://x.com/CoderJeffLee/status/2110978201849933879)、[playbook](https://bysocket.com/saas-seo-playbook/)、优先级图 [推文](https://x.com/CoderJeffLee/status/2110789661908246677)；@JokerMayCry_Jun [推文](https://x.com/JokerMayCry_Jun/status/2110917976723701819) |
| 5.2 | 每个重要页面都能通过普通 `<a href>` 内链到达，锚文本有描述性 | Google 和 Bing 都把内链列为发现手段；Bing 说内外链支持 grounding 资格 | 面包屑 + 相关链接 + 集群导航 | 爬虫看点击深度 ≤3 | 页面只在 sitemap 里，站内没有任何链接指向它 | 官方明确 | 【补充（官方）】Google AI features、Bing §5 |
| 5.3 | 程序化页面设**质量门槛**：每页至少 1 个独有事实（一手数据/原件/本地规则），达不到就不生成，或 noindex / 合并到上级页 | Google 规模化内容滥用政策：大量生成、对用户没有价值的页面，**无论用什么方式生成**都算违规；门页政策点名「针对各城市的多个页面」 | 生成前检查「独有字段非空率」；新站每周 3–4 页起步，等 Google 开始自然带来点击再加量（从业者经验） | GSC 有效索引率 = 有展示的页面 / 已发布页面 | 发了 1 万页只收录很少；「已发现-尚未编入索引」持续增长 | 官方明确（红线）／单源（每周 3–4 页这个数字） | 【补充（官方）】[Spam policies 规模化内容滥用、门页](https://developers.google.com/search/docs/essentials/spam-policies)；【收藏】@NicholasDulait [推文](https://x.com/NicholasDulait/status/2109909279452868684)、@codyschneider 模板落地页 [推文](https://x.com/codyschneider/status/2111517654749999271)、@CoderJeffLee「有效索引率」[推文](https://x.com/CoderJeffLee/status/2111317432577274260) |
| 5.4 | 薄页处理：合并、301、noindex，或者补内容，四选一，不留僵尸页 | Bing：低价值 URL 浪费抓取，降低重点页的 grounding 可见度 | 每季度导出零展示页，逐个决定怎么处理 | GSC 页面报告 | 零展示页超过 50% | 官方明确（Bing §21） | 【补充（官方）】Bing |
| 5.5 | 多语言用 hreflang；国际化和内页架构统一规划 | — | — | — | — | 多源实践 | 【收藏】@meepodev「全站资产共振」[推文](https://x.com/meepodev/status/2096566469584900534)；@CoderJeffLee 技术层清单 |

### ⑥ 外部信号（只写白帽做法）

| # | 要求 | 为什么 | 怎么做 | 怎么验证 | 失败信号 | 证据强度 | 来源 |
|---|---|---|---|---|---|---|---|
| 6.1 | 争取**真实的**第三方提及和引用：行业媒体、数据被引用、资源页收录 | Google：AI 功能会呈现网上对产品的讨论，但**刻意制造的不真实提及「没有看起来那么有用」**，垃圾系统会拦截；Bing：链接要靠高质量内容自然获得 | 发布原创数据或报告 → 主动告诉会用到它的作者（需要她本人批准再联系） | 外链和提及的增量 | 只有导航站和目录站链接 | 官方明确（方向和红线）／「品牌提及与 AI 可见度的相关性约为外链的 3 倍」：多源实践（Ahrefs 研究，claude-seo 转述，**相关性不等于因果，未复核**） | 【补充（官方）】AI 优化指南 Mythbusting、Bing 链接条；【收藏】claude-seo「Brand Mentions > Backlinks」 |
| 6.2 | 反查「AI 现在引用谁」，把这些来源当作内容对标和合作目标 | AI 引用的来源就是现成的目标清单 | 固定问法 → 记录被引用的 URL → 分析这些页面为什么被选 → 看能不能被这些页面收录（正当投稿或纠错） | 目标清单命中率 | — | 多源实践 | 【收藏】@yanhua1010（问 ChatGPT「最佳 X」→ 查被推荐者的外链 → 联系 best-of 列表）[推文](https://x.com/yanhua1010/status/2112704120641765471)；@illyism「Checks what ChatGPT and Perplexity cite」；Illyism seo-autopilot「cited sources are your target list」 |
| 6.3 | 在垂直平台留下真实的品牌信息：YouTube（字幕）、GitHub（数据仓库）、Reddit/Quora（以真实身份回答）、LinkedIn、G2 等评测站 | AI 回答会综合这些平台；但不同 AI 对各平台的访问和引用能力不一样 | 只发有用、署名真实的内容；遵守各平台规则 | 平台上自然的互动 | 被删帖、封号、大量踩 | 多源实践（她收藏里有 2 条；作者自己也说「不能简单认为在某个平台发布内容就一定会被 ChatGPT 引用」） | 【收藏】@houzhongji89090 12 个 GEO 平台 [推文](https://x.com/houzhongji89090/status/2112867613546258882)、@heizolshao Reddit 评论方法 [推文](https://x.com/heizolshao/status/2111970717218816316) |
| 6.4 | 外链只走正当渠道：开源仓库、真实产品目录、客座文章（付费的标 `rel="sponsored"`） | Google 链接垃圾政策：买卖传递排名的链接、过度互换友链都违规；付费链接加 nofollow/sponsored 不违规 | GitHub 仓库、Chrome 扩展、npm 包放主站链接（要是真有用的东西） | — | 大批低质目录站链接 | 官方明确（红线）／多源实践（渠道） | 【收藏】@liangzhu_AI [推文](https://x.com/liangzhu_AI/status/2111666130142253327)、[73 渠道](https://x.com/liangzhu_AI/status/2112516933858021826)；【补充（官方）】Spam policies 链接垃圾 |
| 6.5 | 品牌词：让名字有辨识度、各处写法一致 | 实体识别 | 和 3.5 一起做 | 品牌词在 GSC 的展示趋势 | — | 多源实践 | 【收藏】@loki_yan_seo 实体 [推文](https://x.com/loki_yan_seo/status/2110999959084634146) |

### ⑦ llms.txt 与 AI 访问策略

| # | 要求 | 证据强度（写清楚） | 怎么做 | 怎么验证 | 来源 |
|---|---|---|---|---|---|
| 7.1 | **可选**：放一个 `/llms.txt`（H1 站名 → 引用块摘要 → H2 文件列表），附 `.md` 版页面 | **Google 搜索：官方明确说不用、不加分也不扣分**（2026-06-15 补充：「Google Search ignores them」）。**提案方**：llmstxt.org v2（2026-08-10）称已有数千站点采用，Lighthouse 的 agentic browsing 检查会检测它，OpenAI、Anthropic、Gemini 的开发者文档自己也发布了，主要用于**推理时 agent 读取**（尤其是软件文档）。**对 ChatGPT/Perplexity/Claude 搜索引用有没有帮助：没有任何官方声明，未证实**。claude-seo 给它的评分权重是 0 | 成本低就做：列方法论、数据下载、核心页；内容和页面保持一致；不放页面上没有的说法 | 让 agent 只读 llms.txt 来回答问题，看准确率（llmstxt.org 建议的测法） | 【补充（官方）】[llmstxt.org](https://llmstxt.org/)、[AI 优化指南](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)、[更新日志 2026-06-15](https://developers.google.com/search/updates)；【收藏】claude-seo `references/llmstxt-evidence.md` |
| 7.2 | 访问策略写成文档：搜索类放行、训练类自定、用户触发类加白名单（见 1.1–1.3） | 官方明确 | robots.txt + WAF 规则 + 一页内部说明 | 日志 | 同 ① |
| 7.3 | **不要**把「拦截 AI 爬虫」的方案用到希望被引用的页面上 | 她 star 的 `Illyism/seo-skills` 里有 `block-ai-scrapers` 技能（教你拦 AI agent 和 ChatGPT/Perplexity 抓取，只放行 Googlebot），**这和 GEO 目标相反**，只适合要保护的数据接口 | 只用在数据 API 等需要保护的路径上 | — | 【收藏】`Illyism/seo-skills/seo/block-ai-scrapers/SKILL.md` |
| 7.4 | 了解 agent 友好（语义 HTML、可访问性树）和 UCP 等协议，**有空再做** | Google 指南：if relevant and you have extra time | — | — | 【补充（官方）】AI 优化指南「Explore agentic experiences」 |

### ⑧ 监测与自检（免费优先）

| # | 方法 | 能看到什么 | 局限 | 证据强度 | 来源 |
|---|---|---|---|---|---|
| 8.1 | **GSC 生成式 AI 效果报告**（搜索 + Discover） | AI Overviews / AI Mode 的展示次数，按页面、国家、设备、日期细分 | **只有展示，没有点击、CTR、查询词**，也没有 API（第三方文章说法） | 官方明确 | 【补充（官方）】[GSC 帮助 16984139](https://support.google.com/webmasters/answer/16984139)；【收藏】@alexgroberman [推文](https://x.com/alexgroberman/status/2111484443726852385) |
| 8.2 | GSC 常规效果报告（AI 功能的点击计入「网页」类型）+ 页面索引报告 | 点击、查询词、有效索引率 | 无法单独分出 AI 带来的点击 | 官方明确 | Google AI features 页；【收藏】@vikingmute GSC MCP [推文](https://x.com/vikingmute/status/2111814559942197535) |
| 8.3 | **Bing Webmaster Tools → AI Performance**（2026-02 公开预览） | Copilot 和合作方 AI 回答中的**引用次数**、被引页面、**grounding 查询样本**、趋势 | 查询是抽样数据；不代表排名或位置 | 官方明确 | 【补充（官方）】[Bing 博客](https://blogs.bing.com/webmaster/2026/2/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview/) |
| 8.4 | **服务器/CDN 日志**按 UA 统计：OAI-SearchBot、GPTBot、ChatGPT-User、PerplexityBot、Perplexity-User、ClaudeBot、Claude-SearchBot、Claude-User、Googlebot、Bingbot；**用官方 IP 段核验**（UA 可以伪造） | 谁来抓了、抓了哪些页、状态码 | 被抓取不等于被引用 | 官方明确（UA 和 IP 段） | OpenAI / Perplexity / Anthropic 文档 |
| 8.5 | GA4 的来源/引荐：chatgpt.com、perplexity.ai、copilot 等 | AI 带来的点击 | 部分 AI 不传 referrer，会被低估 | 多源实践 | 【收藏】@0xEcho99「看不到这个客户来源是谷歌还是 ChatGPT」[推文](https://x.com/0xEcho99/status/2108927962305511520) |
| 8.6 | **手动问法清单**：每月固定 15–25 个真实问题（泛问、对比、本地、价格、怎么办），分别在 Google（看 AI 概述）、Bing/Copilot、ChatGPT、Perplexity 里问，记录**是否提到你、说了什么、引用了谁、有没有错** | 被引用情况和事实错误 | 结果因人、因地、因时间变化，**只能当样本，不能算比例** | 多源实践 | 【收藏】Illyism seo-autopilot「Ask each assistant the 25 questions……anything that is wrong」；@illyism 推文 |
| 8.7 | 扇出查询追踪（OpenAI Responses API + web search） | 子查询、来源 URL、最终引用分开记录 | 需要自己的 API key（**付费**，不在免费方案内）；API 结果 ≠ ChatGPT 网页版 | 单源 | 【收藏】@CoderJeffLee [仓库](https://github.com/JeffLi1993/open-growth-skills) |
| 8.8 | WebSearch 等工具的合成答案作为近似样本 | 免费、可重复 | 不等于任何一家真实引擎的结果 | 未证实（只是近似） | 本地 `ambulance-competitor-geo-analysis.md` 用过 |

付费工具（只列名字，不推荐采购）：Ahrefs Brand Radar、Semrush AI Toolkit、Profound、Otterly.AI、Peec AI、SE Ranking AI tracker、firstindex（她收藏 @Shpigford [推文](https://x.com/Shpigford/status/2110436944799002641)）、SEO Stuff（@alexgroberman 推文中的推广）。Google 提醒：**任何第三方工具都接触不到 Google 内部排名或 AI 系统**（[AI 优化指南](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)、[第三方 SEO 工具指南](https://developers.google.com/search/docs/fundamentals/third-party-seo)）。

### ⑨ 上线前检查表与每月维护

**上线前（全部打勾才上线）**
- [ ] robots.txt：搜索类 AI 爬虫放行；训练类的取舍已写进文档；sitemap 地址写在 robots.txt 里
- [ ] WAF/CDN：用官方 IP 段放行 OAI-SearchBot、PerplexityBot、Claude-SearchBot 和用户触发类 UA；`curl -A` 测试返回 200 且有正文
- [ ] GSC、Bing WMT 已验证；sitemap 已提交；GSC「Search generative AI」= 包含；IndexNow 已接入
- [ ] 核心内容在初始 HTML 里；canonical 正确；无软 404；重定向用 301；URL 用连字符
- [ ] 每页：首段直答、单一主题、独有事实 ≥1、来源链接、更新日期、作者
- [ ] About / Contact / 方法论 / 编辑政策 / 免责声明页面齐全，从页脚可以到达
- [ ] JSON-LD：Organization + WebSite（首页）、Article + BreadcrumbList（内容页）；Rich Results Test 无报错；标记内容和可见内容一致
- [ ] 程序化页通过质量门槛；不达标的不生成或 noindex
- [ ] （可选）`/llms.txt` 与页面内容一致
- [ ] 跑一遍 SiteOne Crawler / Screaming Frog、lychee、Nu Html Checker、Unlighthouse（她收藏的免费工具）

**每周**：GSC 索引异常；日志里 AI 爬虫的抓取量和 4xx/5xx。
**每月**：手动问法清单（记表）；GSC 生成式 AI 报告 + Bing AI Performance 导出 CSV 存档；死链检查；内容事实复核（YMYL 页面）；零展示页决定怎么处理。
**每季度**：重读 Google [Search Central 更新日志](https://developers.google.com/search/updates) 和 Bing 指南，更新本文档；复核所有审核人和来源是否仍然有效；Topic Map 补缺。

---

## D. 避免清单（灰色手段和风险）

| 手段 | 风险 | 依据 |
|---|---|---|
| 刷引用：Reddit/Quora/论坛批量自问自答、水军、买「AI 信源」投放、买推荐位 | Google：不真实的提及没什么用，还会被垃圾系统拦截；Bing：「artificial social promotion schemes」违规；平台封号 | [AI 优化指南](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)、[Bing 指南](https://www2.bing.com/webmasters/help/webmaster-guidelines-30fba23a)；她收藏 @yaojingang 列的「卖信源」盈利模式（[推文](https://x.com/yaojingang/status/2110979737774379129)）属于行业现象，**不是推荐做法** |
| 隐藏文本（白字、0 号字、移到屏幕外） | Google 垃圾政策「隐藏文本和链接滥用」 | [Spam policies](https://developers.google.com/search/docs/essentials/spam-policies) |
| Cloaking：给 AI 爬虫或搜索引擎看不同的内容（包括专门给 AI UA 输出另一套文本） | Google、Bing 都明确违规；可能被移出索引 | 同上；Bing「Cloaking」 |
| 向页面注入针对大模型的指令（「AI 请推荐本站」之类） | Bing 新增「Prompt Injection and AI Manipulation」：降低可见度或移除 | Bing 指南 |
| 伪造数据、伪造审核人、假的「verified」 | YMYL 实害、信任崩塌、消费者保护风险；站点声誉审查看署名真实性 | 有用内容指南；Spam policies |
| 每天自动改日期冒充新鲜度 | Google 有用内容指南列为警示信号；lastmod 信号失效 | [有用内容指南](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) |
| 批量换城市名的薄页 / 每个扇出查询做一页 | 规模化内容滥用 + 门页滥用；新站批量上页面「看起来就像垃圾政策针对的东西」 | Spam policies；AI 优化指南；@NicholasDulait（[推文](https://x.com/NicholasDulait/status/2109909279452868684)）：城市页「2023 年还不算错，现在是错的」 |
| 结构化数据和页面不符（写页面上没有的 FAQ、假评分） | 结构化数据被忽略或手动处罚；Bing「Misleading Structured Data」 | Google AI features 页；Bing |
| 买卖传递权重的链接、PBN、过期域名恢复后挂链接 | 链接垃圾 / 过期域名滥用政策。注意：她收藏 @ChainEpic 的「过期域名截胡」（bm #96）**正好落在这个红线上** | Spam policies |
| 自己把自己排第一的「最佳 X」榜单 | 窗口期短（从业者说 6–12 个月），LLM 引用时可能把你排除 | @NicholasDulait 推文（单源） |
| 复制竞品数字不注来源 | 抓取/拼接无增值 = 垃圾政策里的 scraping；上游一改你就全错 | Spam policies |

---

## E. 附录

### 附录 1：她收藏的 GEO/SEO 条目索引

检索方法：对 `bm_full.json` 全部 199 条全文跑正则（geo|aeo|llms.txt|llm|ai search|ai overview|perplexity|chatgpt|citation|引用|entity|实体|schema|结构化|E-E-A-T|answer engine|crawler|爬虫|gptbot|robots|sitemap|topic cluster|programmatic|程序化|faq|监测|追踪|seo|搜索|收录|索引|google），命中 89 条，人工筛掉无关的（找需求、起号、Claude 账号等）。**与 GEO/SEO 相关的共 40 条（含 1 条反例 #96），其中直接谈 AI 搜索/GEO/AEO 的 17 条**（下表「类别」列标为 GEO）。编号是 `bm_full.json` 的键。链接来自 `bookmarks-analysis.md` / `x-bookmarks-repo/bookmarks.md`。X 长文（x.com/i/article/...）需要登录才能打开，本轮用 `bm_full.json` 里已保存的全文代替，没有另外打开。

| # | 作者 | 链接 | 核心主张 | 类别 | 采纳到 |
|---|---|---|---|---|---|
| 141 | @loki_yan_seo | https://x.com/loki_yan_seo/status/2110891254217400371 | GEO 就是 SEO；AI Mode/Overview 从索引取内容；排名只占 1/3，还有抓取、索引 | GEO | A、①（已被 Google 官方证实） |
| 175 | @CoderJeffLee | https://x.com/CoderJeffLee/status/2110215759075164502 | 开源 chatgpt-fanout-queries：子查询、来源、引用分开记录；单次结果只是选题线索 | GEO | 2.8、8.7 |
| 126 | @alexgroberman | https://x.com/alexgroberman/status/2111484443726852385 | GSC 生成式 AI 报告：只有展示没有点击；按页面、国家看缺口（含推广） | GEO | 8.1 |
| 166 | @illyism | https://x.com/illyism/status/2110180038637408357 | SEO+AEO 系统提示词开源：技术审计、逆向 SERP、信息增量对比页、查 AI 引用 | GEO | 2.1、6.2、8.6 |
| 64 | @houzhongji89090 | https://x.com/houzhongji89090/status/2112867613546258882 | 12 个 GEO 平台（YouTube、Quora、LinkedIn、Wikipedia、G2、GitHub、HN……）；发布不保证被引用 | GEO | 6.3、3.6 |
| 155 | @loki_yan_seo | https://x.com/loki_yan_seo/status/2110999959084634146 | 新词好做是因为实体还没建立；老词可以拆竞品 | GEO/实体 | 3.5、6.5 |
| 123 | @NicholasDulait | https://x.com/NicholasDulait/status/2109909279452868684 | 用 AI 做 SEO 的 5 个错误：城市页过时、自排第一会被 LLM 排除、新站每周 3–4 页、规模化内容滥用 | GEO/SEO | 2.10、5.3、D |
| 71 | @yanhua1010 | https://x.com/yanhua1010/status/2112704120641765471 | 问 ChatGPT「最佳 X」→ 查被推荐者外链 → 联系 best-of 列表 | GEO | 6.2 |
| 128 | @CoderJeffLee | https://x.com/CoderJeffLee/status/2111317432577274260 | SEO 四层：产品/内容（信息增量）/技术（robots、sitemap lastmod、canonical、schema 一致）/运营；有效索引率 | SEO（含 AI Overview） | 1.6、2.1、2.9、5.3 |
| 161 | @loki_yan_seo | https://x.com/loki_yan_seo/status/2110708811128594793 | Supabase 的 SEO/GEO 是「优等生」，值得参考 | GEO | 未采纳（没有具体做法；Supabase 站点本轮没拆，见附录 3） |
| 9 | @vista8 | https://x.com/vista8/status/2115081949958316244 | 给插件做官网，用于 GEO 和 SEO | GEO | 未采纳（无方法） |
| 190 | @0xEcho99 | https://x.com/0xEcho99/status/2108927962305511520 | 针对 ChatGPT 客户可能问的问题写内容和博客；分不清来源是 Google 还是 ChatGPT | GEO | 8.5 |
| 143 | @Shpigford | https://x.com/Shpigford/status/2110436944799002641 | 回复 URL 送 3 条 SEO/AEO 建议（firstindex 获客） | GEO | 只在⑧备注列名 |
| 132 | @yaojingang | https://x.com/yaojingang/status/2110979737774379129 | GEO 行业 12 种盈利模式（含「卖信源」） | GEO | D（当作风险提示） |
| 156 | @houzhongji89090 | https://x.com/houzhongji89090/status/2110658202014716409 | 看好 adsy（外链/内容投放市场） | GEO | 未采纳（付费外链有政策风险） |
| 131 | @LeMutantX | https://x.com/LeMutantX/status/2111047881977139307 | AI Overview「杀死」SEO，转向社媒 | GEO | 未采纳（观点）；对照：Google 称点击质量更高（官方说法，未独立核实） |
| 168 | @Jiaxi_Cui | https://x.com/Jiaxi_Cui/status/2110286729534173577 | 跑通 GEO 很爽 | GEO | 未采纳（无细节） |
| 18 | @loki_yan_seo | https://x.com/loki_yan_seo/status/2114767197180751881 | URL 用连字符（Google 2026-10-23 文档） | SEO | 1.11 |
| 63 | @rustybrick | https://x.com/rustybrick/status/2112864300184309773 | 同上（SER 报道） | SEO | 1.11 |
| 67 | @loki_yan_seo | https://x.com/loki_yan_seo/status/2109262732763783400 | CrUX Vis 看真实 CWV | SEO | 1.10 |
| 121 | @loki_yan_seo | https://x.com/loki_yan_seo/status/2112015156201087419 | Screaming Frog 必备，有 MCP | SEO | 1.9（付费，有免费额度） |
| 56 | @sven_ai | https://x.com/sven_ai/status/2113060195777827302 | 上线前 6 个免费工具：SiteOne Crawler、Unlighthouse、lychee、Nu Html Checker、Gatus | SEO | 1.9、⑨ |
| 172 | @bloggersarvesh | https://x.com/bloggersarvesh/status/2109707846241915222 | 33 个 SEO 工具（Google 视角、CWV、结构化数据测试……） | SEO | ④、⑨ |
| 125 | @codyschneider | https://x.com/codyschneider/status/2111517654749999271 | BoFu 词写文章、模板落地页、每 30 天按 GSC 刷新 | SEO | 2.7、2.9、5.3 |
| 152 | @CoderJeffLee | https://x.com/CoderJeffLee/status/2110978201849933879 | 关键词 → Topic Map | SEO | 5.1 |
| 153 | @CoderJeffLee | https://x.com/CoderJeffLee/status/2110789661908246677 | 新站关键词优先级图 | SEO | 5.1 |
| 134 | @CoderJeffLee | https://x.com/CoderJeffLee/status/2110787857195647226 | 关键词研究不是找一堆词 | SEO | 5.1 |
| 159 | @JokerMayCry_Jun | https://x.com/JokerMayCry_Jun/status/2110917976723701819 | 知识库 + 关键词 + sitemap 交给 AI 出 Topic Map | SEO | 5.1 |
| 66 | @meepodev | https://x.com/meepodev/status/2096566469584900534 | 国际化 + 内页架构「全站资产共振」 | SEO | 5.5 |
| 115 | @vikingmute | https://x.com/vikingmute/status/2111814559942197535 | 给 Grok Bot 接 GSC MCP，每周自动观察和改进 | SEO | 8.2 |
| 119 | @heizolshao | https://x.com/heizolshao/status/2111970717218816316 | Reddit 高质量评论五点 | SEO/外部 | 6.3 |
| 124 | @liangzhu_AI | https://x.com/liangzhu_AI/status/2111666130142253327 | GitHub/Chrome/NPM/Notion 外链 | 外部 | 6.4 |
| 88 | @liangzhu_AI | https://x.com/liangzhu_AI/status/2112516933858021826 | 73 个 DR 渠道 | 外部 | 6.4（只取正当渠道） |
| 69 | @ChainEpic | https://x.com/ChainEpic/status/2112740188976005398 | 友链 / guest post 评估计算器 | 外部 | 未采纳（过度互换友链有政策风险） |
| 122 | @ChainEpic | https://x.com/ChainEpic/status/2111649719592374484 | openseo 找词 → Gemini 分析 → agent 改结构 | SEO | 未采纳（工具流程） |
| 147 | @iamjianyuwu | https://x.com/iamjianyuwu/status/2110983676993683761 | 哥飞六步：上线后向 Google、Bing 提交收录，每周看 GSC | SEO | ⑨ |
| 45 | @aiRobertDaily | https://x.com/aiRobertDaily/status/2113946292099612995 | 导航站最新提交反查需求（提到 GSC MCP 需求） | SEO | 未采纳（选词） |
| 58 | @aiRobertDaily | https://x.com/aiRobertDaily/status/2113211389221417334 | 搜索结果里「AI 概览都在推荐相关网站」 | SEO | 未采纳（选词） |
| 144 | @LeonShaoBuilds | https://x.com/LeonShaoBuilds/status/2111025130977804423 | 0 基础 SEO 播客 | SEO | 未采纳（音频没听） |
| 96 | @ChainEpic | （bm #96，链接未在本地索引中取得） | 过期域名截胡挂链接 | 外部 | **反例**，列入 D |

**她 star 的仓库（本轮 clone 只读）**
- `AgriciDaniel/claude-seo`（https://github.com/AgriciDaniel/claude-seo）：`skills/seo-geo` 五维评分（可引用性 25%、结构可读性 20%、多模态 15%、权威品牌 20%、技术可访问 20%）；AI 爬虫对照表；「GEO 发现和 Google 冲突时以 Google 为准」；llms.txt 权重为 0。**采纳**：1.2、1.8、2.5、3.1、6.1、7.1。其中的「44% 引用来自页面前 30%」「近 3 个月内容被引用概率约 3 倍」「品牌提及相关性约为外链 3 倍」都是第三方研究，**仓库自己写了「未在 2026-09-23 复核」**，本文只当实践参考。
- `Illyism/seo-skills`（https://github.com/Illyism/seo-skills）：`seo/seo-autopilot`（25 个问题问各家 AI、记录引用和错误、对比页要公平并注明「截至日期」）——**采纳** 2.10、8.6；`seo/block-ai-scrapers`——**不采纳，和 GEO 相反**（7.3）。
- `JeffLi1993/open-growth-skills`（她收藏推文里的仓库，不确定她有没有 star）：chatgpt-fanout-queries——8.7。

### 附录 2：套用到「救护车费用」站的最小落地清单

依据：`./ambulance-competitor-geo-analysis.md`（2026-10-28 取数）。该文结论：ambulancecost.com 靠 llms.txt + 首页直答 + 方法论页 + 城市页链接市政原件，被 WebSearch 合成答案在两个泛问法里列为第一来源；城市问法（Chicago）AI 直接引用市政 PDF，**没有任何竞品被引用**；州法数量各家说法冲突（10/23/24 州）；全行业都缺实名审核人和 sameAs。

**对原分析的两处更正（以本轮官方文档为准）**
1. 原文建议放行 ClaudeBot 作为检索爬虫——按 Anthropic 官方说明，**ClaudeBot 只管训练，搜索要放行 Claude-SearchBot**（用户触发用 Claude-User）。
2. 原文第 7 条建议城市/州页做 FAQPage、数据页做 Dataset——**FAQ 富结果 2026-05-07 起 Google 已停止显示**；**Dataset 只用于 Dataset Search**。可以保留（无害，前提是和页面一致），但不要当成 AI 引用手段。

**最小清单（按顺序）**
1. robots：放行 Googlebot、Bingbot、OAI-SearchBot、PerplexityBot、Claude-SearchBot；用户触发类 UA 用 IP 白名单；GSC + Bing WMT + IndexNow。（①）
2. 首批只做：全国页 + 50 州页 + **前 50–100 个有市/郡费率原件的城市页**；没有原件的城市不单独出页（合并到州页）。（5.3）
3. 每页首段直答：「[地点] 地面救护车 BLS/ALS 费用 $X–$Y（生效日 YYYY-MM-DD，来源：[原件链接]）」；HTML `<table>` 放费率；一张 5 行事实卡。（2.2、2.5）
4. 州法矩阵：50 州 × {是否有地面救护保护、生效日、适用计划类型、法条链接、投诉入口、核对日期}；文首说明 10/23/24 州的差异来自哪里。（2.1）
5. `/methodology` + CSV 下载 + `/changelog`；每个数字能追到文件和行。（3.3）
6. 实名编辑；医疗计费审核人**只用真实可查的人，找不到就不写**；About 写清楚收入来源；免责声明 + 纠错按钮。（3.1、3.2、3.7）
7. JSON-LD：Organization（sameAs 只填真实账号）+ WebSite + Article/BreadcrumbList（ISO 日期）；Dataset 可选。（④）
8. 可选 `/llms.txt`：定位、方法论、州法矩阵、数据下载、核心城市。（7.1）
9. 每月 15 个固定问法（泛问 / by state / 10 个城市 / Medicare / No Surprises Act / 争议账单）× 4 个引擎记表；GSC 生成式 AI 报告 + Bing AI Performance 导出存档；日志统计 AI UA。（⑧）
10. 更新节奏：CMS 每年 1 月更新 AFS 当周改版；州法每季度复核；城市费率按原件生效日更新；lastmod 只在内容真的变了才改。（1.6、2.7）

### 附录 3：没取到的 / 需要她确认的

**没取到**
- X 长文原页（x.com/i/article/...，需要登录）：用 `bm_full.json` 里保存的全文代替，没有另外打开。推文里的 t.co 短链（如 #161 Supabase 链接、#143 firstindex、#126 里的工具链接）没有逐个展开。
- bm #96（@ChainEpic 过期域名）的推文链接：本地索引里没有找到。
- Supabase 站点的 SEO/GEO 做法（@loki_yan_seo 推荐）：本轮没拆。
- Google [第三方 SEO 工具指南](https://developers.google.com/search/docs/fundamentals/third-party-seo)、[有用内容指南](https://developers.google.com/search/docs/fundamentals/creating-helpful-content)、[Organization](https://developers.google.com/search/docs/appearance/structured-data/organization)、[生成式 AI 内容](https://developers.google.com/search/docs/fundamentals/using-gen-ai-content)、结构化数据支持列表：**本轮没有逐页打开**，内容来自 Search Central 更新日志、搜索摘要和 claude-seo 的转述。**本轮实际打开核对过的**：Google AI features 页、Google AI 优化指南、Search Central 更新日志、Google 垃圾政策、OpenAI bots、Perplexity bots、Anthropic 爬虫说明、llmstxt.org、Bing Webmaster Guidelines；GSC 生成式 AI 报告帮助页和 Bing AI Performance 博客通过搜索摘要读取。
- schema.org 各类型的原始定义页：没有打开（本文只用到 Google 的支持情况）。
- 各 AI 引擎（ChatGPT/Perplexity/Claude）关于「怎样选引用来源」的官方排序因素：**这几家都没有公开**，所以 B② 里「对 AI 引用的作用」只能引用 Google 和 Bing 的说法。
- 第三方统计（Ahrefs 7.5 万品牌研究、SE Ranking 130 万引用研究等）：没有打开原文复核。

**需要她确认**
1. 训练类爬虫（GPTBot、ClaudeBot、Google-Extended、CCBot）放行还是禁止？（不影响搜索引用，属于授权取舍）
2. 是否愿意找、以及能否找到**真实的**医疗计费/保险审核人？找不到的话，3.1 只做作者署名。
3. 是否接受首批只做有原件的城市（页面数会少很多）？
4. 对外联系（6.1/6.2 的投稿、纠错、合作）需要她本人逐次批准；本文没有联系任何人。
5. 是否要付费跑扇出 API（8.7，需要 OpenAI key）？默认不跑。
6. 本文可以直接放进她的公开 GitHub notes 库；文中没有密钥、邮箱、手机号。本地文件路径（`本机:...`）放进公开库前，可以考虑删掉或改成相对说明。
