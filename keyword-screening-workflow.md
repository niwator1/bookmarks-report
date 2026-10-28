# 免费档位下的高质量筛词流程（草案 v0.1）

> 整理时间：2026-10-28（UTC+8）。只读调研：X 书签（工作号）、GitHub 星标（niwator1，共 259 个）、私人项目 seo-pilot 的文档。
> 原则（沿用 seo-pilot 手册）：**查不到的数据写"未知"，不估；不猜搜索量。** 帖子里的流量、收入均为作者自述，未核实。
> 标记：【已有】= 资料里已有的做法；【新增】= 本次新增建议。

---

## 0. 资料盘点

### 0.1 X 书签里最相关的帖子（工作号，共约 199 条，读完全部 2 页；两个账号都没有书签文件夹）

| # | 要点 | 链接 |
|---|---|---|
| 1 | 新词在 Semrush 查不到量时，拿一个已知量的长年平稳老词（如 pdf merge）当"尺子"，在 Google Trends 同屏比 12 个月：一直压在尺子下面就先别碰，越过尺子能估量级，刚起来且很陡的最值得盯 | https://x.com/victor_UWer/status/2113209003958243645 |
| 2 | 完整实操：Trends 的 Rising 上升词 → 拉 5 年看季节性（例 secret santa generator 每年圣诞爆）→ Google 搜结果页看前排是不是工具页、AI 概览推荐谁 → 看竞品数据 | https://x.com/aiRobertDaily/status/2113211389221417334 |
| 3 | 去 Reddit 搜带引号的 "I would pay for"，找用户亲口说愿意付钱的需求，再把需求翻译成通用搜索词（例 app store screenshot generator）去查量 | https://x.com/aiRobertDaily/status/2114925454486577427 |
| 4 | 导航站的"最新提交"页就是别人刚抢的新需求：只看 48 小时内新收录的 → 查域名注册时间 → 看官网在做什么 | https://x.com/aiRobertDaily/status/2113946292099612995 |
| 5 | 看别人新注册的域名在上什么内容，就知道什么在爆（例：一天出现两个 crazy frog） | https://x.com/forever7943/status/2112598940583633035 |
| 6 | 哥飞社群六步：学概念 → 挖 20 个"刚出现、有人搜、没好站承接"的候选 → 按标准打分筛到 3 → 定 1 → 单页站 → 每周看 Search Console | https://x.com/i/status/2110983676993683761 |
| 7 | 关键词研究不是导一堆词按量排序，而是整理需求、合并同需求词、变成 Topic Map | https://x.com/i/status/2110787857195647226 · https://x.com/i/status/2110978201849933879 |
| 8 | openseo 找词，配图中 indie survival horror games 月均 4,400、最近一个月 390 → seo-pilot 里"趋势陷阱"的来源 | https://x.com/i/status/2111649719592374484 |
| 9 | 自建抓词系统，能在词火之前监控到；但即使进场早，有些类别该不火还是不火（rap 风格出单率远高于其他）→ 早不等于成 | https://x.com/Wuc436/status/2115050386285375702 |
| 10 | 新词好做是因为实体（Entity）还没建立；老词难是因为别的站和实体关联更强 | https://x.com/i/status/2110999959084634146 |
| 11 | SaaS 博客选"漏斗底部"词：X vs Y、X alternative、X review、best X for Y、how to X；先看第一页现在是谁 | https://x.com/i/status/2111517654749999271 |
| 12 | 新词雷达开源（对应星标里的 new-term-radar） | https://x.com/i/status/2109543158761808243 |
| 补 | 长期在投的广告（Meta 广告库/Google 广告透明中心）= 别人花真钱验证过的卖点 | https://x.com/aiRobertDaily/status/2112844869240868884 |
| 补 | Gumroad 销量榜看已被付费验证的数字产品需求 | https://x.com/aiRobertDaily/status/2112188370353086852 |
| 补 | 新站关键词优先级图 | https://x.com/i/status/2110789661908246677 |

### 0.2 GitHub 星标里最相关的项目（niwator1，259 个星标中筛出）

| 项目 | 作用 | 免费可用？ |
|---|---|---|
| [zhuyansen/new-term-radar](https://github.com/zhuyansen/new-term-radar)（1.9k★） | 新词雷达：X、HF 热门、GitHub 爆发仓库、导航站 sitemap、Reddit 求助、新卖家等，名字→通用词→搜索量/首页竞争，14 天复盘 | **部分**。HF、GitHub 爆发、sitemap、Product Hunt/Show HN 等免费；X、新站、Reddit 求助、新卖家需 AIsa 付费 key（README 列每周几美分到几毛） |
| [every-app/open-seo](https://github.com/every-app/open-seo)（25k★） | 开源版 Semrush/Ahrefs | **软件免费，数据付费**：必须自带 DataForSEO API key 按量付费（README） |
| [AminForou/mcp-gsc](https://github.com/AminForou/mcp-gsc)（2k★） | Search Console 封装成 MCP：查询、页面、对比时段、URL 检查 | 免费（需自己站点的 GSC 授权） |
| [towfiqi/serpbear](https://github.com/towfiqi/serpbear)（2.1k★） | 关键词排名追踪 | 软件免费；抓 SERP 需第三方 SERP API 或代理（多为付费，本次未核实其免费额度） |
| [StJudeWasHere/seonaut](https://github.com/StJudeWasHere/seonaut)（845★） | 站点 SEO 体检 | 免费自建 |
| [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo)（23k★） | Claude Code SEO 技能集，每条建议附"怎么知道它失败了" | 免费 |
| [Illyism/seo-skills](https://github.com/Illyism/seo-skills)（614★） | seo-autopilot：仓库内 keyword-map.csv + 日/周/月节奏 | 免费（无许可证声明） |
| [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar)（63k★） | 多平台热点聚合 + 关键词筛选提醒 | 免费自建（主要中文平台，对海外 SEO 是辅助线索） |
| [garycaogan/intel-radar](https://github.com/garycaogan/intel-radar)（63★） | 每天扫 B站/YouTube/抖音/TikTok/小红书/X/GitHub 找 AI 圈新题材 | 免费（各平台抓取能力未核实） |
| [ZensInk/awesome-open-source-seo](https://github.com/ZensInk/awesome-open-source-seo) | 只收开源 SEO 工具的清单（爬虫、SERP、GEO） | 免费 |
| [TheCraigHewitt/seomachine](https://github.com/TheCraigHewitt/seomachine)（7.5k★） | 长文 SEO 内容工作区（偏写作，不是选词） | 免费 |
| [qianshuixia/shrimpreel](https://github.com/qianshuixia/shrimpreel) | "一个热词一个站"的 AI 视频站模板（建站用，不是选词） | 免费 |

---

## 1. seo-pilot 里已有的选词积累（摘要，来源：私人项目 docs/）

- **流程**【已有】：资讯雷达/收件箱 → 候选词池 → 关键词判断 + 结果页快照 + 交付检查 + 打分 → 短名单 ≤3 → 选定 1 → 项目卡（含失败标准、复盘日）。（docs/manual.md §2）
- **名字 ≠ 需求**【已有】：每个候选背后写 1–5 个**通用需求词**，分别记月均量、最近一个月量、趋势、首页竞争、结论、数据来源。star 增长、模型上榜、域名里有词，都只是线索，不证明有搜索量。（manual §4.4；research/seo-system-from-x-bookmarks.md §2）
- **趋势陷阱**【已有】：最近一个月 < 月均 × 0.3 标红（例 4,400 vs 390）。（manual §4.4）
- **结果页快照**【已有】：前 10 每条记页面类型（工具/文章/比较/列表/论坛/视频/官方/仓库/商店）和强弱；整体结论"有空位/一般/挤满"+"现有结果缺什么"。前排都是工具页→做工具；都是比较文→做内容页。（manual §4.5）
- **交付能力检查**【已有】：模型、API、数据、支付、版权、服务器逐项"可行/有风险/卡住/未知"，一项卡住整体卡住。（manual §4.6）
- **8 项打分**【已有】（1–5 分，权重）：真实问题 2、意图清晰 2、需求量 2、趋势 1、结果页空位 2、交付能力 2、变现路径 1、需求寿命 1；没打的项不计入并显示覆盖率；作者注明"研究资料没给通用阈值，这套是起点"。（manual §4.7）
- **失败判定**【已有】：思路卡必须写"怎么判断它失败了"；项目卡写成功/失败标准 + 复盘日，验证阶梯：有人搜 → 被收录 → 有自然访问 → 有人使用 → 有线索 → 有付费。（manual §4.8–4.9、§4.15）
- **雷达参数**【已有】（config/radar.json）：GitHub 爆发 14 天窗口、≥300 star、日增 ≥200 或日增量 ≥400；监控 12 个 AI/MCP 导航站 sitemap；14 天复盘；首页竞争"弱站"阈值 DR<30、地区 US；用例词最低量 50。
- **已知的坑**【已有】：低 KD ≠ 没竞争（best roguelike games 难度 0 但前排有大游戏媒体）；访问者 ≠ 付款人；Trends 是相对热度不是搜索量；同模板批量建站会造成名字"假聚集"；本站 GSC 首次曝光 ≠ 全网新词诞生；作者流量/收入为自述。（research 两篇）

---

## 2. 流程草案（7 步）

> 每个候选词建一张卡，字段固定：线索来源+日期、通用需求词、每个来源的观察值（带截图/链接和查询日期）、结论、**失败判定**。缺数据一律写"未知（原因）"。

### 第 1 步：发现线索（只进池，不下结论）
| 免费来源 | 看什么信号 | 进池标准 | 登录？ |
|---|---|---|---|
| Hugging Face 热门榜前 50【已有】 | 新进榜的模型/Spaces 名 | 新出现即进池 | 否 |
| GitHub 爆发仓库【已有】 | 14 天内新仓库、日均 +200★ | 满足 radar.json 阈值 | 否（无 token 每小时 60 次，[GitHub 文档](https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api)） |
| 导航站 sitemap / "最新提交"页【已有】 | 多个新 URL 共有、旧 URL 少见的词 | 48h 内 ≥2 个**不同主体**的站围绕同一名字【新增：排除同模板批量站】 | 否 |
| Product Hunt / Show HN RSS【已有】 | 新品名、解决的任务 | 有明确任务描述 | 否（RSS）；HN 搜索 API 免登录（[HN Algolia API](https://hn.algolia.com/api)） |
| Google Trends 上升查询【已有】 | Rising / Breakout | 直接进池 | 网页本次未登录使用，额度未核实；官方 API 仍是 alpha 需申请（[Google 文档](https://developers.google.com/search/apis/trends)） |
| Reddit 求助帖【已有】 | "I would pay for" "is there a tool that" | 有具体任务 + 有人附和 | 网页搜索不用登录；API 要 OAuth（见第 7 节） |
| 新注册域名 / 广告库 / Gumroad 榜【已有，来自书签】 | 新域名含同一词；长期在投广告；销量榜 | 作为"付费证据"线索 | 广告库、Gumroad 浏览未核实是否需登录 |

**淘汰**：无。此步只记录。**缺数据**：来源跑不通写"来源不可用（原因）"。

### 第 2 步：还原成通用需求词【已有，补充规则为新增】
- 把名字翻译成 1–5 个"用户会怎么搜"的词：`<名字> + 任务`（如 `xxx video generator`）和**不含名字**的通用任务词（如 `ai rap video generator`）。【已有】
- 【新增】加商业修饰：`free / online / alternative / vs / pricing / how to`（对应书签 #11）。
- **淘汰**：写不出"谁、为什么、要完成什么任务"的 → 跳过（对应打分"真实问题"1 分）。

### 第 3 步：需求量与趋势（v0.2，按 2026-10-28 实测修订）
> 实测依据：对 3 个候选词，Google Trends 和 Ahrefs 免费关键词生成器、KD 检查器均免登录可打开；但 Trends 对大词尺子会把小词压成 0，Ahrefs 免费档只给量级档（小于 100、大于 100、大于 1000、大于 10000）和 KD，不给精确量。

1. **拆词**：每个候选同时查"整句词"和 1–2 个"上位词"（更短、更通用的说法）。整句词查不到、上位词有量，记"长尾待验证"，不直接淘汰。
2. **A 类证据 = Ahrefs 免费量级档 + KD**（keyword-generator、keyword-difficulty，美国）。原样抄录档位和 KD，注明日期，不换算成精确量。底线：量级档至少"大于 100"，且 KD 不是 Hard 以上；"小于 100"或"无数据"的整句词，必须靠上位词补证。
3. **Trends 只当辅助**：看近 4 周方向和季节性，不再作为必须通过的门槛。**尺子词必须与候选同量级**（Ahrefs 档位相近）；用大词做尺子，小词会读成 0，读不出趋势。页面显示"数据不足"时写"Trends：数据不足"，并截图确认后才算数。
4. **趋势陷阱规则保留**：最近一个月 < 月均 × 0.3 标红（需要有月均数据时才适用）。
5. **缺数据**：Ahrefs"无数据"写"Ahrefs：无数据（日期）"，不估数。

### 第 4 步：搜索结果页（SERP）与相关搜索
- Google 搜通用需求词（无痕、固定地区 US），记前 10 页面类型和强弱 → 结论"有空位/一般/挤满"+"缺什么"【已有】。
- 【新增，v0.2】"其他人还问了"、"相关搜索"、自动补全用浏览器手动取（脚本取不到），并记录；同时记"其他人还搜了"、"相关搜索"、自动补全（Ahrefs 免费 Keyword Generator 不用登录实测只显示前 20 个想法，[Ahrefs FAQ](https://ahrefs.com/faq)），用来确认词义、合并同需求词。
- **通过**：前排有 ≥1–2 个位置是弱站/论坛/不直接完成任务的页面；意图集中（前排大多同一页面类型）。
- **淘汰**：前排全是强站且已直接完成任务；或意图分散（工具、新闻、百科混杂）；或词义歧义（同名其他事物占满）。
- **缺数据**：地区搜不到/被验证码挡 → 写"SERP：未取得（原因）"，该项不打分。

- 【新增，来自站点类型指南】**适合做成站的四个判断**：① 有明确搜索词（单词月搜只有几百也行，聚成一族就够）；② 前排弱（泛聚合页、旧页面、Pinterest）；③ 能参数化（一套模板批量生成变体）；④ 有付费空间（职业类、场景类易卖打包版，纯装饰类很难）。①②对应第 5 步的 A、B，③④放在第 6 步交付与变现里检查。

### 第 5 步：多平台互证（核心）
把证据分成 4 类，每类取 1 个最强来源：

| 类别 | 免费来源 | 算一票的信号 |
|---|---|---|
| A 搜索需求 | Ahrefs 免费量级档+KD（主）、Google Trends 方向（辅）、Bing Webmaster 量、Keyword Planner 区间、Semrush 免费额度 | 第 3 步"通过" |
| B 结果页空位 | Google SERP + 相关搜索 | 第 4 步"通过" |
| C 真人求助/付费意愿 | Reddit、HN 评论、论坛、Stack Exchange | 近 30 天 ≥2 个不同人提出同一任务，或有人说愿意付钱 |
| D 供给/热度 | GitHub star、HF 热度、Product Hunt/Show HN、导航站新提交、新注册域名、长期广告 | 近 14 天有独立主体在做（=需求被别人押注），但**不能单独作为需求证据** |

- **过关标准【新增】**：A 必须有 + B 必须有 + C、D 中至少 1 个 = **至少 3 个来源、3 类**才进"优先"。只有 D 类（热度）没有 A 类（搜索）→ 最多"观察"。A 是"数据不足"时可以先上"观察"，14 天后再查（沿用雷达 14 天复盘【已有】）。
- 同一来源不同页面不算两票；同一作者/同模板站不算两票。

### 第 6 步：交付 + 打分 + 20→3→1【已有】
- 交付检查一项"卡住"即淘汰。
- 8 项打分，覆盖率 < 75% 的不进短名单【新增阈值，可调】。
- 【新增，来自站点类型指南】**数据变化频率检查**：慢变数据（执照要求、法规、品种资料、历史数据，一年核一次）适合低运维；快变数据（趋势、新闻、优惠、榜单）需持续更新，运维高，直接降级或淘汰。另外要确认数据能否合法、稳定获取，以及数据有没有人搜；纯公开汇总的数据护城河薄，要有自己的加工层（分类、评分、实测、场景标注），否则容易被 AI 回答替代。
- 短名单 ≤3，选 1 个。

### 第 7 步：写失败判定并复盘
每个候选词卡必须有"怎么判断它失败了"，建议默认模板【新增，数字是起点、需要你定】：

| 阶段 | 失败信号（满足任一即判失败或降级） |
|---|---|
| 选词期（第 3–5 步复查，14 天后） | Trends 跌破尺子线 / 触发趋势陷阱；SERP 前排被 ≥3 个新强站占满；Reddit 求助帖不再出现 |
| 上线后 2–4 周 | GSC 无收录或目标词 0 曝光（先排查技术问题再判） |
| 上线后 8 周（项目卡复盘日） | 目标词曝光有、点击为 0（标题/意图不匹配）；有点击无人使用；未达到项目卡 target_value |

GSC 首次曝光查询可反哺第 1 步（本站新词线索）【已有】。

---

## 3. 需要登录 / 注册的平台（免费额度，本次查到的来源）

| 平台 | 免费档能做什么 | 来源 / 状态 |
|---|---|---|
| Google Search Console | 自己站点的曝光、点击、查询词、收录；需验证站点 | 免费（常识，本次未单独打开官方页核实额度） |
| Bing Webmaster Tools | 免费关键词研究：Bing 精确搜索量、趋势、相关词；需验证站点 | [Bing 帮助](https://www2.bing.com/webmasters/help/keyword-research-628070b6) |
| Google Ads（Keyword Planner） | 不投广告也能用，但只给量区间（如 1K–10K） | [Rank Math 教程](https://rankmath.com/kb/use-keyword-planner-without-running-ads/)（官方帮助页本次未直接打开） |
| Semrush Free | 每天 10 次 关键词/域名/竞品/外链查询，每次显示 10 行，不能导出；1 个项目、10 个排名词、审计 100 页 | [Semrush 知识库](https://www.semrush.com/kb/1011-subscriptions)、[官方博客](https://www.semrush.com/blog/what-can-i-do-with-a-free-account-from-semrush/)（有 Reddit 用户反映额度可能改为总共 10 次，未核实） |
| Ahrefs Free | 免登录工具：Keyword Generator 前 100 个、KD 检查、SERP 检查、外链前 20；注册后只能看已验证站点（1000 词/外链，每月 5000 抓取额度）；**不含 Keywords Explorer** | [Ahrefs FAQ](https://ahrefs.com/faq)、[帮助中心](https://help.ahrefs.com/en/articles/13002606-what-can-i-use-for-free-in-ahrefs) |
| Reddit Data API | 需 OAuth 注册应用，免费每个 client id 100 次/分钟；不用 OAuth 会被封 | [Reddit 帮助](https://support.reddithelp.com/hc/en-us/articles/16160319875092-Reddit-Data-API-Wiki) |
| Product Hunt API | 需开发者 token；每 15 分钟 6,250 复杂度点 / 450 次请求 | [PH API 文档](https://api.producthunt.com/v2/docs/rate_limits/headers)（RSS 不需要） |
| GitHub API（token） | 带 token 每小时 5,000 次（不带 60 次） | [GitHub 文档](https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api) |
| Google Trends API | alpha，需申请审批 | [Google 文档](https://developers.google.com/search/apis/trends) |
| Similarweb、Reddit Pro、Toolify、Meta 广告库 | 书签/研究里提到的用法 | 免费额度**未核实** |
| 付费（不在免费流程里） | AIsa（new-term-radar 付费来源）、DataForSEO（open-seo 必须）、SERP API | 仅列出，不建议在免费档使用 |

---

## 3.5 补充来源：《出海 SEO 网站矩阵：站点类型与落地路径说明》（2026-10）
已读取全文。主要结论：优先低运维的工具站和数据站，其次模板站、小游戏站，目录站靠后，内容站和评测站先放一边；先单站验证再复制；一个站只解决一类需求。已把其中“适合做成站的四个判断”和“数据变化频率检查”并入第 4、6 步。文中的收入和流量数字是经验性估计，需以工具数据验证。

## 4. 读不到 / 缺失的资料
- 站群指南 PDF 最初读取损坏，后由用户重新提供，已读完（见 3.5）。
- 默认 X 账号书签 0 条；两个账号都没有书签文件夹。X 书签接口不给"加入书签的时间"，只能看帖子发布时间。
- cursor-github 连接器没有"星标列表"工具，星标是用 GitHub 公开 API（不登录）读的，共 259 个。
- Trends、Similarweb 等需要浏览器交互的平台本次没有实际操作，只核实了公开说明。


---

## 附：v0.2 修订记录（2026-10-28）
- 第 1 轮筛词（20 词）：全部因为没取到 A 类数据，最多进"观察"。
- 浏览器实测（美国，免登录）：wordart generator，Ahrefs 量级大于 100、KD 50；revenue per employee，量级大于 100、KD 12；land bordering public land，Ahrefs 无数据。Trends 上三者对大词尺子均读为 0 或接近 0。
- 据此修订第 3 步：拆词、改用 Ahrefs 量级档为主、尺子同量级、Trends 降为辅助。
