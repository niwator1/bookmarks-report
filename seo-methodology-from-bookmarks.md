# 禽姐收藏里的 SEO 方法论清单（用于竞品逐页分析）

整理日期：2026-10-28（UTC+8）。只读整理，未登录、未发帖。
来源文件：`/workspace/bookmarks.txt`（行号:序号 @作者）、`/workspace/bm_full.json`（全文，键为序号）、`/workspace/x-bookmarks-repo/bookmarks.md`（带推文链接）、GitHub stars（`gh api user/starred`，账号 niwator1，共 259 个，只读）。
标记说明：**【收藏】** = 她真收藏过的；**【补充】** = 我补的通用方法，不是她收藏的。

## 结论先行：最有用的 5 条
1. **竞品是可以「拆」出来的（实体 Entity 视角）**：@loki_yan_seo「老词并不难做，竞争对手做过什么事情，为什么他们做得好其实是可以拆的出来的」。直接决定我们做逐页拆解。【收藏】bm_full #155，https://x.com/loki_yan_seo/status/2110999959084634146
2. **关键词 → Topic Map（主题地图），按搜索意图归并**：@CoderJeffLee《SaaS SEO Playbook》第 5 章 + 「新站关键词优先级」图；@JokerMayCry_Jun 补充：知识库 + 关键词表 + **竞品/自己 sitemap URL 清单** 交给 AI 出 Topic Map，判断显性/隐性意图。【收藏】#152/#153/#134/#159，https://x.com/CoderJeffLee/status/2110978201849933879 、https://bysocket.com/saas-seo-playbook/ 、https://x.com/JokerMayCry_Jun/status/2110917976723701819
3. **页面类型分流 + 模板批量页（程序化 SEO）**：@codyschneider：信息/对比词写文章（先抓 SERP 前排结构、做内容缺口、每 30 天按 GSC 刷新）；「找工具」意图做落地页模板（约 5 个模块）批量生成，再给这些页建外链。【收藏】#125，https://x.com/codyschneider/status/2111517654749999271
4. **反查竞品 SERP 与引用来源（含 AI 引用）**：@illyism 开源 SEO+AEO 提示词仓库：技术 SEO 审计、逆向前 10 SERP 标题结构、写有 information gain 的对比页、查 ChatGPT/Perplexity 引用谁。她也 star 了 `Illyism/seo-skills` 和 `AgriciDaniel/claude-seo`（技术 SEO、**E-E-A-T、schema**、GEO/AEO 子技能）。【收藏】#166，https://x.com/illyism/status/2110180038637408357 ；https://github.com/Illyism/seo-skills ；https://github.com/AgriciDaniel/claude-seo
5. **技术检查清单（爬取/结构化数据/CWV/死链）**：@bloggersarvesh「33 个 SEO 网站」（Google 看站方式、CWV、结构化数据测试、schema 校验、Wayback 看竞品历史、PAA 问题…）；@sven_ai 上线前 6 工具（SiteOne Crawler、Unlighthouse、lychee 死链、Nu Html Checker…）；@loki_yan_seo：Screaming Frog（有 MCP）、CrUX 真实用户 CWV 看板、URL 用连字符。【收藏】#172 https://x.com/bloggersarvesh/status/2109707846241915222 ；#56；#121；#67；#18

## 全量清单（按方法论类别）

| 类别 | 内容要点 | 来源（作者/链接/收藏位置） | 标记 | 用到竞品分析的哪一步 |
|---|---|---|---|---|
| 竞品可拆 / 实体 | 新词实体未建立好做；老词靠拆竞品做法 | @loki_yan_seo #155 https://x.com/loki_yan_seo/status/2110999959084634146 | 收藏 | 总方法：逐页拆 |
| GEO=SEO | 排名只占 1/3，还有 Crawling、Indexing；AI Mode/Overview 从 Google 索引取 | @loki_yan_seo #141 https://x.com/loki_yan_seo/status/2110891254217400371 | 收藏 | 加「可抓取/可索引」维度（robots、sitemap、canonical、404） |
| Topic Map | 关键词研究=整理需求→主题地图；优先级图 | @CoderJeffLee #152 #153 #134；GitHub 源文件见推文 | 收藏 | 从竞品 sitemap 反推它的 Topic Map |
| sitemap→Topic Map | 知识库+关键词+sitemap URL 清单交 AI 判断意图 | @JokerMayCry_Jun #159 | 收藏 | 用 ambulancecost sitemap 3 万 URL 分页面类型 |
| 页面类型分流/程序化 | 文章 vs 落地页模板批量生成；30 天刷新；内容缺口 | @codyschneider #125 | 收藏 | 模板化程度、缺口、刷新日期维度 |
| 全站资产共振 | 国际化 + 内页架构；用 similarweb/reddit/GSC 真实数据；拿做得差的竞品当反例 | @meepodev #66 (bookmarks.txt 67 行) | 收藏 | 内链结构维度；反例（不要复制的） |
| SERP/AEO 逆向 | 审计技术 SEO、逆向前 10 SERP、info gain 对比页、AI 引用 | @illyism #166；star `Illyism/seo-skills` | 收藏 | SERP 对手简版分析 |
| E-E-A-T / Schema / 技术 | 26 子技能：技术 SEO、E-E-A-T、schema、GEO/AEO | star `AgriciDaniel/claude-seo` | 收藏(star) | E-E-A-T、Schema 维度 |
| 工具清单 | 33 个：Google 视角、CWV、结构化数据测试、schema 校验、Wayback、技术栈识别、PAA | @bloggersarvesh #172 | 收藏 | 维度取数工具 |
| 上线前检查 | SiteOne Crawler、Unlighthouse、lychee、Nu Html Checker、Gatus | @sven_ai #56 | 收藏 | 死链/404、HTML 错误维度 |
| Screaming Frog | 必备爬虫，可自建，有 MCP | @loki_yan_seo #121 | 收藏 | 全站爬（本次用 curl 抽样代替） |
| CrUX | 真实用户 CWV 看板 | @loki_yan_seo #67 | 收藏 | 速度维度（本次未取得） |
| URL 规范 | 用 - 不用 _；URL 带词有帮助 | @loki_yan_seo #18 | 收藏 | URL 结构维度 |
| 外链反查 | 找赚钱竞品→Semrush 外链→按权威排序看文章→整理清单 | @aiRobertDaily #48 | 收藏 | 外链维度（需付费工具，本次未取得） |
| 外链渠道 | 10 平台 / 73 个 DR 渠道 / GitHub、Chrome 商店 | @aiRobertDaily #19；@liangzhu_AI #88 #124 | 收藏 | 我们的外链打法 |
| 防被抄 | 同行能像素级复刻页面结构、外链 | @qianshuixia2026 #32 | 收藏 | 反向提醒：我们上线后也会被拆 |
| 关键词流程 | 哥飞六步：学方法→挖词→判断→… | @iamjianyuwu #147；@aiRobertDaily #58 | 收藏 | 已在 keyword-screening-workflow 用过 |
| 工具 star | open-seo（Semrush/Ahrefs 开源替代）、serpbear（排名追踪）、seonaut（审计）、mcp-gsc、awesome-open-source-seo、seomachine、GEOInflow | GitHub stars（`every-app/open-seo`、`towfiqi/serpbear`、`StJudeWasHere/seonaut`、`AminForou/mcp-gsc`、`ZensInk/awesome-open-source-seo`、`TheCraigHewitt/seomachine`、`yaojingang/GEOInflow`） | 收藏(star) | 后续取 DR/排名/抓取的免费工具候选 |
| YMYL | 医疗/财务/法律类内容需更高可信度：作者、审核、引用、更新日期、免责声明 | Google Search Quality Rater Guidelines（公开文档） | **补充** | 救护车账单=健康+钱+法律，三重 YMYL |
| 结构化数据规范 | FAQPage/BreadcrumbList/Article/Dataset 合规写法；日期用 ISO 8601 | Google Search Central 结构化数据文档 | **补充** | Schema 维度判定 |
| 重复内容/thin content | 程序化页若数字和文字全相同，属近重复薄页 | 通用 SEO 实践 | **补充** | 重复度维度 |

说明：她收藏里**没有**专门讲 YMYL、Schema 写法细则、canonical/重复内容的推文；这三条在模板里使用时均标为【补充】。私有 seo-pilot 仓库本次未查（未在本机目录中找到；未额外尝试）。

## 怎么落到竞品分析（对应模板维度）
- 拆竞品（#155）→ 逐页、字段固定。
- Crawl/Index（#141）→ robots、sitemap、canonical、404、noindex 每页都查。
- Topic Map（#152/#159）→ 先用 sitemap 把 30,303 个 URL 分成页面类型，再逐类抽样。
- 页面类型分流（#125）→ 计算器/城市页=工具意图；resources=信息意图；分别看模块与刷新日期。
- E-E-A-T/Schema（claude-seo star + 补充）→ 作者、来源、更新日期、JSON-LD 类型与合规。
- 工具清单（#172/#56/#121/#67）→ 本次只用 curl+BeautifulSoup；CWV、外链、DR 需上述工具，未取得。
