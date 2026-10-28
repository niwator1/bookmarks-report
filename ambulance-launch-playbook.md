# 救护车费用（ambulance cost）站 · 落地流程全面指南

> 编写：2026-10-28（UTC+8）｜给禽姐｜只读研究，未登录、未注册、未发帖、未花钱、未建站。
> 标记：**【收藏】**=她收藏过的推文/仓库（编号为 `本机:bm_full.json` 的键）；**【补充】**=我补充的（多为官方文档）；**【本地】**=本机已有分析文件。
> 价格与门槛取数日期：2026-10-28（UTC+8），来源见各行链接；取不到的写「未取得」。
> 内部失败判断日：**2026-12-15**（沿用 `./idea-card-ambulance-cost.md`）。

---

## A. 一页纸摘要

| 项 | 结论 |
|---|---|
| 目标 | 做「美国救护车费用」里**唯一能把每个数字追到官方原件**的站：市/郡核实费率库 + 州级 surprise-billing 行动矩阵 + 收到账单后按州的处理流程 + Medicare 现金锚点（按 ZIP）。 |
| 第一个 14 天 | ①第 1–3 天：域名/站名、合规页草稿、robots 策略；②第 2–7 天：下载 CMS AFS 2026 PUF 与 ZIP-locality 文件，做成按 ZIP 的 Medicare 基准表；同时找 **50 个大城市的官方费率原件**；③第 8–12 天：Astro 静态站 + Cloudflare Pages 上线首页、50 州页、方法论、变更日志、已核实城市页；④第 13–14 天：GSC/Bing 验证、提交 sitemap、跑上线检查表、记录 15 个固定问法基线。 |
| 总预算 | **零成本档 ≈ 仅域名 $10.46–11.17/年**（.com 在 Cloudflare 的成本价，2026-11-01 起 $11.17）；**约 100 美元档**：+ 少量付费 OCR/工具月费；**约 500 美元档**：+ 一次性条款模板/律师审阅（价格未取得）或外部校对。详见 D。 |
| 最先变现 | **不急着挂广告**。最先验证的是 **数据产品（核实费率 CSV / 州法矩阵的付费版或授权）**，对象是账单倡导者、律师事务所研究员、记者；其次是**展示广告**（流量够后）。账单协商类联盟有合规顾虑，只在审过条款后小规模试。 |
| 最大风险 | ①**2026-12-15 前做不出 30 个带官方原件的城市页** → 数据差异化不成立；②YMYL：数字出错或被理解为医疗/法律建议；③竞品 ambulancecost.com 补齐来源/日期；④AI 概述吃掉点击。 |

---

## B. 核心落地流程（按阶段）

> 每阶段格式：目标｜步骤｜产出物｜验收标准｜怎么判断失败｜预计耗时。命令只写不执行。

### 阶段 0 · 准备与合规
- **目标**：拿到一个可信、不越界的站点外壳。
- **步骤**
  1. 域名：优先 `.com`，描述性非 EMD（ambulancecost.com 已被占）。候选方向如「ambulance-bill / ambulance-rates / ems-fee」+ 中性词（例如 *AmbulanceRates*、*EMS Fee Index*）。用 Cloudflare Registrar 查可用性（只查不买，购买需她批准）。【收藏 #0 @Wuc436：EMD 被抢光就加前缀变体】https://x.com/Wuc436/status/2115035797393207683 ；【收藏 #104 @ChainEpic：不要公开问/公开自己域名，防被抄】、【收藏 #32 @qianshuixia2026：公开域名被像素级复刻】。
  2. 站名：中性、机构感，不带「Official」「Gov」等误导词。
  3. 合规页：`/disclaimer`（非医疗/法律建议；Medicare 基准≠实际账单；数据截至日期）、`/privacy`、`/terms`、`/about`（谁做的、怎么赚钱）、`/methodology`、`/corrections`（纠错流程）。
  4. 每页固定标注：**「数据来自官方原件 + 自动比对；未经医疗专业人员审核」**（已批准决策，不编造审核人）。
  5. 边界：不推荐具体医疗处置；不说「你不必付」；法律信息只给「法条原文链接 + 官方投诉入口」，不做个案判断；不做律师导流。
- **产出物**：域名短名单（3–5 个）、合规页草稿 6 篇、全站页脚免责模块。
- **验收**：每个合规页都有生效日期；免责模块出现在全部模板；About 写明收入来源。
- **失败判断**：任何页面出现「审核人：某某」但无法查证；或页面用祈使句给个案法律/医疗建议 → 立即下线该页修正。
- **耗时**：1–2 天。

### 阶段 1 · 数据获取与清洗
- **目标**：建一个可追溯、带版本的数据仓：每个数字 → 原件文件 + 页码/行 + 生效日。
- **数据源**
  | 数据 | 来源 | 说明 |
  |---|---|---|
  | CMS AFS PUF（CY2018–2026） | https://www.cms.gov/medicare/payment/fee-schedules/ambulance/ambulance-fee-schedule-public-use-files | 字段：Contractor、Locality、HCPCS（A0425–A0436 等）、RVU、GPCI 等；CMS 自注「仅供参考，MAC 的官方金额可能略有差异」——页面必须照写。 |
  | ZIP→Carrier Locality（2026-08-13 更新）+ 需 ZIP+4 的清单 | https://www.cms.gov/medicare/payment/fee-schedules/ambulance | 含 urban/rural/super-rural 标记。CY2027 拟改用 RUCA 划分城乡（CMS 公告）→ **2027-01 必须重算**。 |
  | 地面救护临时加成（延至 2027-12-31） | https://www.cms.gov/ambulance-news-announcements | 写进方法论与变更日志。 |
  | 市/郡/消防局 EMS 费率原件 | 市政条例、费率决议 PDF、消防局 fee schedule 页 | 发现方法见下。 |
  | NPI（机构识别） | NPPES NPI Registry 公共 API【补充】https://npiregistry.cms.hhs.gov/api-page | 用于把费率原件对应到收费机构。 |
  | 州 surprise-billing 法条 | 州议会官网法条原文、州保险监管机构投诉页 | 联邦 No Surprises Act **不覆盖地面救护**（仅空中救护），这正是州法矩阵的价值；表述以 CMS 官方页为准【补充】https://www.cms.gov/nosurprises |
- **市政原件发现（只用公开搜索，不抓违反 ToS 的站）**：搜索式 `site:.gov "ambulance" "fee schedule" filetype:pdf "{City}"`、`"{City}" "ambulance transport fee" ordinance`、`"{County}" EMS "rates" resolution`；优先 `.gov`/市议会议程/Municode 等条例库（只人工浏览，遵守 robots）。
- **工具取舍**
  | 工具 | 用于 | 取舍 |
  |---|---|---|
  | Python + pandas | CMS 表、ZIP 映射、计算 | 免费，主力 |
  | pdfplumber / camelot | 文字型 PDF 表格 | 免费；先试它 |
  | Tesseract / ocrmypdf | 扫描件 | 免费，精度一般，**OCR 出来的数字必须人工逐项对照原件** |
  | 付费云 OCR | 大量扫描件 | 现价未取得（查证：各云厂商官网 pricing 页）；首批 50–100 城不需要 |
  | Git + CSV/Parquet | 版本管理 | 原件 PDF 存 R2/仓库 LFS，记 sha256 |
- **示例命令（不执行）**
  ```bash
  python -m venv .venv && . .venv/bin/activate
  pip install pandas pdfplumber openpyxl
  curl -LO "<CMS CY2026 AFS ZIP 链接>"   # 从上面官方页取实际链接
  sha256sum *.zip >> data/raw/CHECKSUMS.txt
  python scripts/build_medicare_by_zip.py --afs data/raw/afs2026.xlsx --zip data/raw/zip_locality.txt --out data/derived/medicare_by_zip_2026.csv
  ocrmypdf in.pdf out.pdf && python scripts/extract_rates.py out.pdf
  ```
- **字段表（核实城市费率 `city_rates.csv`）**：`city, state, county, provider_name, npi, service_level(BLS/ALS1/ALS2/SCT/mileage/TNT/other), resident_rate, nonresident_rate, unit, effective_date, source_title, source_url, source_file_sha256, page_ref, retrieved_at, extracted_by(script/manual), checked_at, notes`。州法矩阵：`state, ground_ambulance_protection(Y/N/partial), statute_cite, statute_url, effective_date, plan_types_covered, erisa_gap_note, complaint_url, checked_at`。
- **质量抽检**：每批随机抽 10%（至少 5 条）由第二遍人工/脚本对照原件；Medicare 计算与 CMS 官方示例对一遍；字段完整率 100%（source_url、effective_date 不能空）；数字范围检查（ALS < BLS 等异常报警）。
- **产出物**：`data/raw`（原件+校验和）、`data/derived/*.csv`、`DATA_SOURCES.md`、抽检记录。
- **验收**：≥50 城有完整原件记录；抽检错误率 0（发现错误即全批重查）；50 州矩阵每行有法条链接与核对日期。
- **失败判断**：**2026-12-15 时可出页的有原件城市 < 30 个** → 按 idea-card 放弃/降级；单城平均找原件耗时 > 45 分钟且无改善 → 调整为「州页+Medicare 锚点」为主。
- **耗时**：Medicare 部分 1–2 天；城市原件 50 个约 5–8 天（估计，未实测）；州法矩阵 3–5 天。

### 阶段 2 · 站点架构与技术栈
- **目标**：纯静态、零运维、免费托管、每页可追溯。
- **栈对比**
  | 选项 | 优点 | 缺点 | 建议 |
  |---|---|---|---|
  | **Astro（静态输出）** | 默认零 JS，内容站快；Markdown/CSV 直接生成页 | 交互组件需岛屿 | **首选** |
  | Next.js 静态导出 | 生态大；竞品同栈 | 偏重；静态导出有限制 | 备选 |
  | TanStack Start + Workers【收藏 #165 @York_981、#0 @Wuc436】 | 她圈子常用 | 为 SaaS 设计，本站用不上数据库/登录 | 二期做付费数据/API 时再考虑 |
  | Hugo/11ty | 极快 | 计算器需另写 JS | 可选 |
- **免费托管**
  | 托管 | 免费额度（取数 2026-10-28） | 商用 | 来源 |
  |---|---|---|---|
  | **Cloudflare Pages** | 500 次构建/月、单站 20,000 文件、单文件 25 MiB、静态带宽不限 | 未写明限制 | https://developers.cloudflare.com/pages/platform/limits/ |
  | Cloudflare Workers Free | 10 万请求/天；D1 5GB | — | https://developers.cloudflare.com/workers/platform/limits/ |
  | Vercel Hobby | 100 GB 传输/月 | **条款限非商业用途** → 有广告/联盟就不合适 | https://vercel.com/legal/terms（汇总见 https://zeroraised.com/data/free-tiers） |
  | Netlify Free | 300 credits/月，超额暂停全部项目 | 未写明 | https://www.netlify.com/pricing/ |
  【收藏 #110 @Michaelzsguo：Cloudflare 免费策略「As long as I'm CEO」】https://x.com/Michaelzsguo/status/2111908769034543149 ；**反面**【收藏 #171 @madawei2699：D1/Email/RealtimeKit 被坑，billing 与 support 弱】https://x.com/madawei2699/status/2110194480922140890 → 本站只用 Pages 静态，不依赖 D1；保留 GitHub 仓库可一键迁 Netlify。
- **URL 结构**（小写、连字符【收藏 #18 @loki_yan_seo】）
  - `/` 首页（直答 + ZIP 计算器 + 州地图）
  - `/states/{state}/`（50 州 + DC）
  - `/states/{state}/{city}/`（**仅限有原件的核实城市**）
  - `/medicare-ambulance-rates/`（ZIP 计算器，ZIP 不单独出页，避免 4 万薄页）
  - `/ambulance-bill/`（收到账单怎么办总流程）+ `/ambulance-bill/{state}/`（按州行动流，可合并到州页的一个区块，二期再拆）
  - `/surprise-billing-laws/`（州法矩阵）
  - `/methodology/`、`/changelog/`、`/data/`（CSV 下载）、合规页
- **内链**：首页→州→城市；城市↔同州城市；每页→方法论、账单行动流、州法行；面包屑。【收藏 #66 @meepodev 全站资产共振】
- **sitemap/lastmod**：分 `sitemap-states.xml`、`sitemap-cities.xml`、`sitemap-pages.xml`；lastmod = 该页**数据或正文真实变化**的日期（从 `checked_at`/git 变更取），不批量刷新（竞品全站同一 lastmod 是反例）。【收藏 #128 @CoderJeffLee：sitemap lastmod、canonical、schema 一致】
- **Schema**（参考 `./web-geo-requirements.md` ④）：Organization（sameAs 只填真实账号）+ WebSite（全站）；Article（方法论、行动流，dateModified 用 ISO 8601）；BreadcrumbList（州/城市）；Dataset（`/data/` 页，仅帮助 Google Dataset Search，**证据强度：对普通排名/AI 引用无官方证据**）；FAQPage 不当成手段（FAQ 富结果 2026-05-07 起已停显示，见 web-geo-requirements 附录 2）。
- **产出物**：仓库骨架、5 种页面模板、sitemap 生成脚本、schema 组件。
- **验收**：Lighthouse 移动端性能 ≥90（目标值，自定）；Rich Results Test/Schema validator 零错误；所有城市页能点到原件链接。
- **失败判断**：构建 > 20 分钟或文件 > 20,000（触 Pages 免费上限）→ 说明页面数失控，回到「不批量生成」原则；任一页 schema 与可见内容不一致。
- **耗时**：3–4 天。

### 阶段 3 · 内容生产
- **目标**：每页有信息增量、可被直接引用。
- **页面固定结构**：①直答块（首段 1–2 句：「{城市} 地面救护 BLS/ALS 官方费率 $X–$Y，生效日 YYYY-MM-DD，来源：[原件]」）②事实卡（5 行：服务等级、居民/非居民、每英里、生效日、Medicare 同地基准）③HTML `<table>` ④「这不等于你的账单」说明 ⑤收到账单怎么办（链到州行动流）⑥来源与核对日期 ⑦免责。
- **模板 vs 人工**：数字与表格 100% 来自数据；文字模板 ≤ 60%，每个城市页至少 1 段**基于原件的独有说明**（如非居民加价、TNT 费、免收居民费）。【收藏 #123 @NicholasDulait：城市页过时、规模化内容滥用会被排除；新站每周 3–4 页】→ 首批 50–100 城分批上，不一次倒。
- **AI 辅助边界**：AI 只做①草拟说明文字 ②从原件抽字段的初稿 ③改写可读性；**AI 不得产生任何数字、法条结论、生效日**。
- **自检清单（每页发布前）**：数字都能在原件找到（页码）｜日期 ISO｜无「审核人」虚构｜无个案建议句式｜Medicare≠账单说明在｜原件链接 200｜和州法矩阵一致｜title/description 唯一｜相似度对同州其他城市页 < 0.8（difflib，竞品反例是 1.000）。
- **产出物**：内容风格指南 1 页、页面模板、自检脚本。
- **验收/失败判断**：自检脚本任一项红灯不得发布；上线后被用户/纠错入口指出数字错误 → 24 小时内修正并写进变更日志，同类错误 ≥2 次则暂停发新页先全量复核。
- **耗时**：每城 20–40 分钟（估计）。

### 阶段 4 · 上线与收录
- **步骤**：GSC 域名资源验证（DNS TXT）→ 提交 sitemap index；Bing Webmaster（可从 GSC 导入）→ 提交 sitemap、开启 IndexNow【收藏 #147 @iamjianyuwu：上线后向 Google、Bing 提交，每周看 GSC】；Cloudflare Web Analytics（免费）。
- **robots.txt（按已批准决策）**
  ```
  User-agent: Googlebot
  Allow: /
  User-agent: Bingbot
  Allow: /
  User-agent: OAI-SearchBot
  Allow: /
  User-agent: PerplexityBot
  Allow: /
  User-agent: Claude-SearchBot
  Allow: /
  User-agent: GPTBot
  Disallow: /
  User-agent: ClaudeBot
  Disallow: /
  User-agent: CCBot
  Disallow: /
  User-agent: Google-Extended
  Disallow: /
  User-agent: *
  Allow: /
  Sitemap: https://<域名>/sitemap-index.xml
  ```
  注意：Cloudflare 有「AI 爬虫一键拦截/托管 robots」开关，**要确认没有把搜索类爬虫也挡了**。Google-Extended 不影响 Google 搜索/AI 概述收录（Google 官方说明）。
- **上线检查表**【收藏 #56 @sven_ai：SiteOne Crawler、Unlighthouse、lychee、Nu Html Checker、Gatus】https://x.com/sven_ai/status/2113060195777827302 ：死链 0；HTML 校验无错；canonical 自指；noindex 只在 /search 等；404 页正常；移动端可用；CrUX 数据（新站通常不足）【收藏 #67 @loki_yan_seo】。
- **产出物**：检查表打勾记录、提交截图。
- **验收**：sitemap 被 GSC 读取成功；2 周内首页与州页被索引。
- **失败判断**：4 周后有效索引率 < 50%（GSC 页面报告）→ 查质量/重复；**上线 4 周展示 < 1,000/月或 8 周无一页进前 20 → 停止扩页**（idea-card 第 3 条）。
- **耗时**：1 天 + 等待。

### 阶段 5 · 冷启动与外部信号（只白帽）
| 动作 | 做法 | 风险 | 需她逐次批准？ |
|---|---|---|---|
| 公开数据集 | GitHub 仓库发布 CSV + 方法论（CC BY 4.0），README 链回站【收藏 #124 @liangzhu_AI：GitHub 建仓 DR96】https://x.com/liangzhu_AI/status/2111666130142253327 ；也可上 Kaggle/data.world（免费账号） | 数据被直接抄走（接受，署名要求） | 是（注册+发布属对外） |
| 给记者/账单援助机构的资源页 | 「各州救护车账单法 + 投诉入口」一页式，可引用；把引用格式写好 | 低 | 页面本身不用；**主动邮件联系**需逐次批准 |
| Reddit/社区真实回答 | 在 r/HospitalBills、r/MedicalBill 里**先答问题本身**，只在确有帮助时给原件或州法页链接【收藏 #118 @momo_peggy：活人感，要有观点或利他】https://x.com/momo_peggy/status/2111986350270615770 ；【收藏 #119 @heizolshao：高质量评论五点】https://x.com/heizolshao/status/2111970717218816316 | 自推被删/封号；子版规则 | **是，每条** |
| 记者请求平台（HARO 后继如 Qwoted、Featured、Help a B2B Writer 等，免费档情况未取得） | 只回答与救护车账单数据相关的请求 | 低价值请求多；不能夸大身份 | 是（注册+每次回复） |
| 「最佳资源」列表 | 问 AI「best resources for ambulance bill」，找被推荐页面，礼貌建议补充【收藏 #71 @yanhua1010】 | 被当垃圾邮件 | 是 |
| 外链平台清单 | Medium/DEV/Hashnode/Notion 公开页等【收藏 #19 @aiRobertDaily、#88 @liangzhu_AI 73 渠道】只发**有内容**的方法论文章 | 薄内容被当垃圾；医疗主题在 Product Hunt 类平台不合适 | 是 |
| **不做** | 买外链、adsy 类付费投放【收藏 #156】、过期域名截胡【收藏 #96 @ChainEpic】、友链互换网、自动发外链 | 违反 Google 垃圾政策 | — |
- **失败判断**：8 周后 GSC「链接」报告外部引用域 < 5 且 Reddit 回答零正向反馈 → 换渠道（转向记者/机构资源页），不要加大发帖量。

### 阶段 6 · 监测与迭代
- **周节奏（免费，每周一 30–60 分钟）**：GSC 效果（查询/页面/有效索引）＋**生成式 AI 报告**（只有展示）https://support.google.com/webmasters/answer/16984139 ；Bing WMT **AI Performance**（引用次数与 grounding 查询样本）https://blogs.bing.com/webmaster/2026/2/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview/ ；Cloudflare 日志/分析按 UA 统计搜索类 AI 爬虫（用官方 IP 段核验）；纠错收件处理。【收藏 #115 @vikingmute：GSC MCP 每周自动观察】、GitHub star `AminForou/mcp-gsc`、`towfiqi/serpbear`（自托管排名追踪）。
- **每月 15 个固定问法**（4 个引擎：Google AI 概述、Bing/Copilot、ChatGPT 搜索、Perplexity；记录是否提到本站、引用了谁、有无错误；**只当样本**，不买付费扇出接口）：
  1. how much does an ambulance ride cost
  2. ambulance cost by state
  3. how much does an ambulance cost without insurance
  4. ambulance cost in New York City
  5. ambulance cost in Los Angeles
  6. ambulance cost in Chicago
  7. ambulance cost in Houston
  8. ambulance cost in Phoenix
  9. ambulance cost in Philadelphia
  10. ambulance cost in San Francisco
  11. ambulance cost in Seattle
  12. Medicare ambulance rate for my ZIP code
  13. does the No Surprises Act cover ground ambulance
  14. which states ban surprise ground ambulance bills
  15. how to dispute an ambulance bill
  （城市可换成首批实际核实的 8 个城市，问法本身固定不变，方便对比。）
- **扩城/扩州条件**：已上城市页中 ≥50% 在 GSC 有展示，且纠错率为 0 → 每周加 10–20 个有原件的城市；州法矩阵被外部引用 ≥1 次 → 拆出按州行动流独立页。
- **止损**：见阶段 4 失败判断与 2026-12-15 / 2027-01-28 条件。
- **月度**：CMS 新年度 PUF（每年 1 月）当周更新；州法每季复核；原件链接死链检查（lychee）。

### 阶段 7 · 时间线
| 时间（UTC+8） | 里程碑 | 与 2026-12-15 的关系 |
|---|---|---|
| 第 1–2 周（10-29 → 11-11） | 合规页、Medicare-by-ZIP 数据、**30 个城市原件**、站点上线（首页/州页/方法论/变更日志/计算器）、GSC+Bing 提交、问法基线 | 提前 1 个月看到原件命中率 |
| 第 3–6 周（11-12 → 12-09） | 城市累计 50–70；州法矩阵 51 行完成；GitHub 数据集；首批 Reddit 回答（逐条批准） | **12-15 判断：有原件可出页城市 < 30 → 放弃/降级** |
| 第 7–12 周（12-10 → 2027-01-20） | 城市 80–100；2027 年 CMS PUF 与城乡新划分更新；首个数据产品验证（见 E）；AI 引用/展示第二轮记录 | 通过 12-15 后进入；**2027-01-28** 竞品补齐判断；上线后 4/8 周 GSC 门槛 |

---

## C. 小技巧清单（30 条）

**数据**
1. 每个数字存 `source_file_sha256 + page_ref` —— 原件被改或下线时能自证。【补充】
2. 原件 PDF 自己留存（R2/仓库）并在页上给「存档副本」链接 —— 市政网站常改版死链。【补充】
3. 先用 pdfplumber，扫描件才 OCR，OCR 数字必须人工复核 —— 省时间又保证准确。【补充】
4. Medicare 计算按 ZIP→locality→GPCI 走，并区分 urban/rural/super-rural —— 竞品只给笼统基准。【本地 ambulance-competitor-seo-page-by-page.md】
5. 把「居民/非居民」「TNT（不运送）费」单列字段 —— 这是竞品少数做得好的点，要学。【本地 同上】
6. 用老词当尺子在 Google Trends 比新词热度 —— Ahrefs 免费档只有量级带时可交叉验证。【收藏 #53 @victor_UWer】
7. 2027 年 CMS 拟改 RUCA 城乡划分，提前把 ZIP 分类做成可替换列 —— 1 月可一键重算。【补充 CMS 公告】

**SEO**
8. 只为有原件的城市出页，其余合并进州页 —— 避开竞品 3 万重复薄页的坑。【本地；收藏 #123 @NicholasDulait】
9. lastmod 只随真实变化 —— 竞品全站同一 lastmod 是反例。【收藏 #128 @CoderJeffLee】
10. 用竞品 sitemap 反推 Topic Map 再找缺口。【收藏 #159 @JokerMayCry_Jun、#152 @CoderJeffLee】
11. URL 用连字符、带词。【收藏 #18 @loki_yan_seo】
12. 信息词写文章、工具词做模板页，30 天按 GSC 刷新。【收藏 #125 @codyschneider】
13. 拆竞品逐页（字段固定）而不是凭感觉。【收藏 #155 @loki_yan_seo】

**GEO**
14. 首段直答 + 生效日 + 来源 —— AI 最常截取页面前部。【收藏 star AgriciDaniel/claude-seo（第三方研究，未复核）】
15. GEO 本质是被抓取、被索引 —— 先把 Crawl/Index 做好。【收藏 #141 @loki_yan_seo】
16. 放行 Claude-SearchBot 而不是 ClaudeBot（后者是训练）。【补充 Anthropic 官方，见 web-geo-requirements.md】
17. 州法数量各家说法冲突（10/23/24 州），文首解释差异来源 —— 成为「纠错型」可引用源。【本地 ambulance-competitor-geo-analysis.md】
18. 每月固定问法记录「引用了谁、哪里说错」。【收藏 Illyism/seo-skills seo-autopilot、#166 @illyism】

**内容**
19. 每页一句「Medicare 基准不是你的账单」 —— YMYL 必备也是信息增量。【补充】
20. 对比页公平并写「截至日期」。【收藏 Illyism seo-autopilot】
21. 围绕用户真实问题写（Reddit 原帖里的措辞）。【收藏 #190 @0xEcho99；#13 @aiRobertDaily「I would pay for」搜索法】
22. 新站每周 3–4 页稳步加，不一次倒库。【收藏 #123 @NicholasDulait】

**技术**
23. 静态站上 Cloudflare Pages，注意 20,000 文件上限。【收藏 #110；补充 Cloudflare 文档】
24. 不把核心数据放 D1，保持可迁移。【收藏 #171 @madawei2699】
25. 上线前跑 SiteOne Crawler / Unlighthouse / lychee / Nu Html Checker。【收藏 #56 @sven_ai】
26. 看真实 CWV 用 CrUX Vis。【收藏 #67 @loki_yan_seo】

**效率/自动化**
27. 用 GSC MCP 让 bot 每周出观察。【收藏 #115 @vikingmute；star AminForou/mcp-gsc】
28. 「注册域名→写代码→部署→提交 GSC→接分析」流水线化，做成可复用模板。【收藏 #97 @AI_Jasonyu】

**风险规避**
29. 不公开域名/不问别人域名，防同行像素级复刻。【收藏 #32 @qianshuixia2026、#104 @ChainEpic】
30. 过期域名截胡、付费外链一律不做。【收藏 #96 @ChainEpic、#156 @houzhongji89090（反例）】

---

## D. 花费表

> 取数日期 2026-10-28（UTC+8）。「未取得」= 本次没查到官方现价，附查证方法。

| 项 | 必须/可选/可省 | 免费方案 | 付费档位 | 来源 |
|---|---|---|---|---|
| 域名 .com | **必须** | 无 | Cloudflare 成本价 **$10.46/年**，**2026-11-01 起 $11.17**（Verisign 批发价 $10.97 + ICANN $0.20）；首年促销更低但续费贵 | https://pikkly.dev/domains/registrar/cloudflare/ ；ICANN 费率 https://itp.cdn.icann.org/en/files/registry-agreements/com/com-fees-01-11-2026-en.pdf 【收藏 #20 @HarriesSteele Spaceship 优惠码，首年价，续费另计】 |
| 托管 | 可省 | Cloudflare Pages 免费（见 B2） | Pages Pro 价未取得（查 https://www.cloudflare.com/plans/） | Cloudflare 文档 |
| 数据存储 | 可省 | GitHub 仓库 + Pages；R2 有免费额度（额度未在本次核实，查 https://developers.cloudflare.com/r2/pricing/） | 未取得 | — |
| 邮箱（纠错收件） | 可选 | Cloudflare Email Routing 转发（免费，本次未核实条款） | 未取得 | 查 https://developers.cloudflare.com/email-routing/ |
| 监测 | 可省 | GSC、Bing WMT、Cloudflare Web Analytics、serpbear 自托管 | Ahrefs/Semrush 等：不采购 | 官方 |
| 写作辅助 | 可省 | 现有 bot | — | — |
| OCR | 可省 | Tesseract/ocrmypdf | 云 OCR 价格未取得（查各厂商 pricing 页） | — |
| 抓取/代理 | **不需要** | 人工浏览 + curl 下载公开 PDF，遵守 robots 与 ToS | 不买代理（绕封属灰色） | — |
| 法律/条款模板 | 可选 | 自写 + 参考公开模板，标注非律师审阅 | 律师审阅价未取得（查证：本地律所报价或 LegalZoom 类官网） | — |
| 审核人（真人，将来） | 可选 | 不写审核人 | 价格未取得；只用真实可查的人 | — |
| 数据集托管 | 可省 | GitHub / Kaggle 免费 | — | — |

**三档方案**
- **零成本档（≈$11/年）**：只买域名；其余全免费栈。**最低可行方案 = 这一档**。
- **约 100 美元档**：域名 + 少量按量付费 OCR 或一个月单项 SEO 工具试用（具体价格未取得，购买前现查）+ 备用域名一个。
- **约 500 美元档**：上面 + 一次性律师审阅免责/条款（价格未取得）或外部兼职数据校对（价格未取得）。**建议在有收入信号前不进这一档。**

---

## E. 变现路径

**推荐顺序与理由**（YMYL 费用站：信任 > 流量；首批页数少 → 不能靠广告量）
| 序 | 路径 | 理由 |
|---|---|---|
| 1 | **数据产品：核实费率 CSV/州法矩阵 付费完整版或授权**（面向账单倡导者、律所研究员、记者、医院收入周期团队） | 唯一与差异化直接挂钩；不依赖流量量级；验证成本低 |
| 2 | **展示广告**（AdSense → Journey by Mediavine → Raptive） | 流量起来后的地板收入；对 YMYL 也可接受，但医疗类广告受限 |
| 3 | **赞助/资源页**（账单援助非营利、软件） | 需明确标注；与中立性冲突要控制 |
| 4 | **工具型小产品**（账单核对清单 PDF、申诉信模板生成器） | 她收藏里「数字产品先到第一笔钱」【本地 seo-出海方向调研.md】；但申诉信涉及法律边界 |
| 5 | **账单协商/医疗账单援助联盟** | 用户意图最匹配，但条款与按成功收费模式需审，FTC 披露必做 |
| 6 | 保险比价/医疗融资（CareCredit 等） | 金融+医疗双 YMYL；CareCredit 公开页只见**服务商融资协议**，未找到联盟条款 |
| 7 | 空中救护会员联盟 | **不建议**：会员常与保险/网络覆盖重叠、销售纠纷多（未在本次核实具体投诉数据），推荐会被视为不中立 |

**逐项**
1. **数据产品**
   - 怎么赚：免费公开基础 CSV（外链引擎）；付费版 = 全字段+原件存档+变更提醒+商用授权。收款需主体（见 G；【本地 week1-plans.md：Stripe 需境外主体，或 Lemon Squeezy/Paddle 类 MoR】）。
   - 指标量级：未取得（无同类公开数据）。
   - 合规：公共记录本身可自由使用，卖的是整理与核对；写清「不保证完整」；不承诺用于诉讼。
   - 启动成本：≈0（Gumroad/MoR 抽成比例未取得）。
   - **第一个验证动作**：在 `/data/` 放「需要完整版/API？留下用途」表单（只收集意向，不收款），统计 4 周意向数。
   - 失败判断：上线 8 周意向 < 3 条，或意向方都只要免费版 → 降为纯外链资产。
2. **展示广告**
   - 门槛（官方，2026-10-28）：**Journey by Mediavine ≥1,000 premium sessions/30 天**，GA4 连接，过度用 AI 会被拒 https://journeymv.zendesk.com/hc/en-us/articles/24633185741723-Journey-Minimum-Requirements ；**Mediavine Official 需上年广告收入 ≥$5,000** https://help.mediavine.com/what-does-it-take-to-get-approved-by-mediavine ；**Raptive ≥25,000 PV/月**，25k–99k 需 50% 来自美英加澳新，域名 ≥6 个月 https://help.raptive.com/hc/en-us/articles/360032840891-Who-is-eligible-for-Raptive ；AdSense 无公开流量门槛但需内容审核（以官方为准）；Ezoic 门槛未取得（查 https://www.ezoic.com/ 官方 FAQ）。
   - RPM：未取得。
   - 合规：AdSense 发布商政策；YMYL 页面广告不得遮挡数据/免责；Google Ads 医疗政策限制部分广告主出现【补充】https://support.google.com/adspolicy/answer/176031 。
   - 失败判断：达到 Journey 门槛后申请被拒（「excessive use of AI」）→ 提高人工内容比例再申请；广告上线后跳出率显著上升或纠错反馈说「像广告站」→ 减量。
3. **赞助/资源页**：标注「Sponsored」，FTC 披露【补充】https://www.ftc.gov/business-guidance/resources/ftcs-endorsement-guides ；赞助方不得影响数据。失败：3 个月无询价。
4. **工具小产品**：清单/模板只给流程与官方链接，不给个案法律意见；不做「代写申诉」服务。失败：免费版下载数 4 周无增长。
5. **账单协商联盟**：先查各家联盟条款原文（本次未取得具体项目条款）；要求 FTC 披露；**不得做律师导流**（各州律师广告/转介规则，不做付费转介）。失败：条款禁止 YMYL/医疗费用站或要求夸大省钱比例 → 不接。
6. **医疗融资**：CareCredit 公开资料只见服务商协议与广告披露指南 https://www.carecredit.com/sites/pc/pdf/CareCredit_Advertising_Disclosure.pdf ，联盟条款未取得；推荐信贷有消费金融披露义务 → 暂不做。
7. **空中救护会员**：不做；若将来做，只作为中立说明页不挂链接。

---

## F. 风险清单与「不要做」

**风险**
| 风险 | 概率/影响 | 缓解 |
|---|---|---|
| 原件不足（< 30 城） | 中/致命 | 第 1–2 周先测命中率；12-15 止损 |
| 数字错误（YMYL） | 中/高 | 原件页码、抽检、纠错 24h、变更日志 |
| 被当成法律/医疗建议 | 中/高 | 边界句式、免责、只链官方 |
| 竞品补齐 | 中/中 | 2027-01-28 复评；我们的护城河是原件存档与州法矩阵 |
| AI 概述截流 | 高/中 | 做被引用的源；变现不依赖纯点击（数据产品） |
| Cloudflare 免费策略/账单问题 | 低/中 | 静态+Git，随时迁移 |
| 被同行抄 | 中/低 | 不公开域名于社群；数据 CC BY 署名 |
| CMS 年度更新/城乡改划 | 确定/中 | 1 月更新流程写进日历 |
| 收款主体缺失 | 高/中 | 先只收意向（见 G） |

**不要做**：刷单/刷点击；买外链/付费链接投放/PBN/过期域名截胡；绕过封号或多账号；隐藏文本/伪装；伪造数据或「估算」冒充官方；虚构审核人/作者资质；批量生成无原件城市页或 ZIP 页；放行训练类爬虫（当前决策）；买付费 ChatGPT 扇出接口；律师/医疗导流抽成；空中救护会员推广；Reddit 批量自推；在页面上承诺「能省 X%」。

---

## G. 需要她决定的事项（6 项）

1. **域名与站名**：建议买一个描述性 .com（Cloudflare 成本价约 $11/年），不用 EMD 变体；理由：可信度与长期续费成本低。需她批准购买。
2. **首批城市数**：建议先 50（不是 100），2026-12-15 前跑完；理由：先验证原件命中率再扩。
3. **技术栈与托管**：建议 Astro 静态 + Cloudflare Pages；理由：免费、商用无限制条款问题（Vercel Hobby 禁商用）、可迁移。
4. **数据授权方式**：建议基础 CSV 用 CC BY 4.0 免费公开，完整版付费；理由：公开版换外链与引用，付费版验证 B2B。
5. **收款主体**：建议暂不开收款，只收意向表；有 ≥3 条真实付费意向再决定 MoR 平台或境外主体。理由：避免先投入合规成本。
6. **对外动作的审批粒度**：建议 Reddit/记者平台/邮件联系**逐条批准**，GitHub 数据集发布**一次性批准**；理由：社区封号与信任风险高，数据集风险低。

---

## H. 附录：她收藏的资源索引

> 编号=`本机:bm_full.json` 键；链接来自 `本机:x-bookmarks-repo/bookmarks.md`、`本机:bookmarks-analysis.md`。链接写「未在本地索引取得」的未另行打开（X 需登录）。

| # | 作者 | 链接 | 主张 | 采纳到 |
|---|---|---|---|---|
| 0 | @Wuc436 | https://x.com/Wuc436/status/2115035797393207683 | EMD 被抢就加 free 等变体；栈 TanStack Start + Workers/D1/R2 | B0、B2 |
| 13 | @aiRobertDaily | 未在本地索引取得 | Reddit 搜 "I would pay for" 找付费需求 | C21 |
| 19 | @aiRobertDaily | 未在本地索引取得 | 10 个外链平台（Medium、GitHub、DEV…） | B5 |
| 20 | @HarriesSteele | https://x.com/HarriesSteele/status/2114311845633024037 | Spaceship 域名首年优惠码 | D（首年价，续费另计） |
| 32 | @qianshuixia2026 | 未在本地索引取得 | 公开域名被像素级复刻 | C29、F |
| 48 | @aiRobertDaily | 未在本地索引取得 | 反查赚钱竞品外链四步法（Semrush） | 未采纳（付费工具）；思路用于找资源页 |
| 53 | @victor_UWer | https://x.com/victor_UWer/status/2113209003958243645（按 bookmarks-analysis 推断，未逐条核对） | 老词当尺子比 Trends | C6 |
| 56 | @sven_ai | https://x.com/sven_ai/status/2113060195777827302 | 上线前 6 个免费检查工具 | B4、C25 |
| 66 | @meepodev | https://x.com/meepodev/status/2096566469584900534 | 全站资产共振/内页架构 | B2 |
| 67 | @loki_yan_seo | https://x.com/loki_yan_seo/status/2109262732763783400 | CrUX Vis 看真实 CWV | B4、C26 |
| 70 | @aiRobertDaily | 未在本地索引取得 | 扒竞品广告库看卖点 | 未采纳（竞品无广告） |
| 71 | @yanhua1010 | https://x.com/yanhua1010/status/2112704120641765471 | 问 AI「最佳」→ 联系 best-of 列表 | B5 |
| 88 | @liangzhu_AI | https://x.com/liangzhu_AI/status/2112516933858021826 | 73 个 DR 外链渠道 | B5（只取正当渠道） |
| 96 | @ChainEpic | 未在本地索引取得 | 过期域名截胡 | **反例** F |
| 97 | @AI_Jasonyu | 未在本地索引取得 | 域名→代码→部署→GSC→分析→外链流水线 | C28 |
| 104 | @ChainEpic | 未在本地索引取得 | 不要问别人域名 | C29 |
| 110 | @Michaelzsguo | https://x.com/Michaelzsguo/status/2111908769034543149 | Cloudflare 免费策略长期提供 | B2、C23 |
| 115 | @vikingmute | https://x.com/vikingmute/status/2111814559942197535 | GSC MCP 每周自动观察 | B6、C27 |
| 118 | @momo_peggy | https://x.com/momo_peggy/status/2111986350270615770 | Reddit 要活人感、利他 | B5 |
| 119 | @heizolshao | https://x.com/heizolshao/status/2111970717218816316 | Reddit 高质量评论五点 | B5 |
| 123 | @NicholasDulait | https://x.com/NicholasDulait/status/2109909279452868684 | 城市页过时、规模化滥用、每周 3–4 页 | B3、C8、C22 |
| 124 | @liangzhu_AI | https://x.com/liangzhu_AI/status/2111666130142253327 | GitHub/Chrome/NPM/Notion 高 DR 外链 | B5 |
| 125 | @codyschneider | https://x.com/codyschneider/status/2111517654749999271 | 文章 vs 模板页、30 天刷新 | C12 |
| 128 | @CoderJeffLee | https://x.com/CoderJeffLee/status/2111317432577274260 | SEO 四层；lastmod/canonical/schema 一致 | B2、C9 |
| 132 | @yaojingang | https://x.com/yaojingang/status/2110979737774379129 | GEO 12 种盈利模式（含卖信源） | F（风险提示） |
| 137 | @ChainEpic | https://x.com/ChainEpic/status/2110922611031167050（按 bookmarks.md 匹配） | 工具站/目录站「躺赚」 | 未采纳（YMYL 需持续维护） |
| 141 | @loki_yan_seo | https://x.com/loki_yan_seo/status/2110891254217400371 | GEO=SEO，抓取索引占大头 | C15 |
| 147 | @iamjianyuwu | https://x.com/iamjianyuwu/status/2110983676993683761 | 上线提交 Google/Bing，每周看 GSC | B4 |
| 152/159 | @CoderJeffLee / @JokerMayCry_Jun | https://x.com/CoderJeffLee/status/2110978201849933879 ；https://x.com/JokerMayCry_Jun/status/2110917976723701819 | Topic Map；sitemap 交 AI 分意图 | C10 |
| 155 | @loki_yan_seo | https://x.com/loki_yan_seo/status/2110999959084634146 | 老词可拆竞品 | C13 |
| 156 | @houzhongji89090 | https://x.com/houzhongji89090/status/2110658202014716409 | 看好 adsy 外链投放 | **反例** F |
| 165 | @York_981 | https://x.com/York_981/status/2109637258890600775 | TanStack Start + Drizzle + Cloudflare 栈 | B2（二期） |
| 166 | @illyism | https://x.com/illyism/status/2110180038637408357 | SEO+AEO 提示词：逆向 SERP、查 AI 引用 | C18 |
| 171 | @madawei2699 | https://x.com/madawei2699/status/2110194480922140890 | Cloudflare D1 等被坑 | B2、C24 |
| 176 | @gefei55 | 未在本地索引取得 | ShipAny 模板（Stripe/Creem/PayPal 收款） | 未采纳（本站一期无需 SaaS 模板） |
| 190 | @0xEcho99 | https://x.com/0xEcho99/status/2108927962305511520 | 按客户会问 AI 的问题写内容 | C21 |
| star | AgriciDaniel/claude-seo | https://github.com/AgriciDaniel/claude-seo | GEO 五维评分、AI 爬虫表 | C14 |
| star | Illyism/seo-skills | https://github.com/Illyism/seo-skills | seo-autopilot 固定问法 | B6、C18、C20 |
| star | AminForou/mcp-gsc、towfiqi/serpbear | GitHub | GSC MCP、自托管排名追踪 | B6 |

**本地依据文件**：`./idea-card-ambulance-cost.md`、`ambulance-competitor-seo-page-by-page.md`、`ambulance-competitor-geo-analysis.md`、`web-geo-requirements.md`、`seo-methodology-from-bookmarks.md`、`本机:seo-出海方向调研.md`、`本机:week1-plans.md`、`本机:site-reference-analysis.md`。

**没取到**：Ezoic 门槛、AdSense RPM/各网盟 RPM、云 OCR 现价、律师审阅价、R2/Email Routing 免费额度本次未复核、账单协商类联盟具体条款、CareCredit 联盟条款（公开页只见服务商协议）、记者请求平台免费档现状、城市原件单城平均耗时（未实测）、部分收藏推文链接（标「未在本地索引取得」）。
