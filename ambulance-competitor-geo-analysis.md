# 救护车费用站：竞品 GEO 分析与打法

> 取数日期：2026-10-28（Asia/Singapore, UTC+8）。只读：curl / WebSearch，未登录、未注册、未发帖、未联系、未花钱。
> 原始文件：`/workspace/outputs/geo-raw/`（各站 robots/llms.txt、页面 HTML、`sig.py` 解析脚本、`urls.txt`）。早期材料：`ambulance-competitor-analysis.md`、`competitor-pages-raw.md`、`competitor-seo-raw/`。
> 不猜引用率、流量、排名；取不到写「未取得」。

---

## 结论先行

1. **竞品 GEO 最强的是 ambulancecost.com**：唯一有 `/llms.txt`（含权威外链清单与方法论页）、首页 `FAQPage + Dataset` JSON-LD、首页首段就是「$500–$3,000+」一句话直答，且在本轮 WebSearch 合成答案中被列为第 1 来源（「how much does an ambulance cost」「ambulance cost by state」两问均出现）。另据旧材料，GoodRx 参考文献点名引用它（见 `ambulance-competitor-analysis.md`「浏览器核验补记」）。
2. **大站靠「表格 + 品牌权威」被引**：WPR 和 CareCredit 那张 51 行州表是 AI 回答「by state」的直接数据来源（合成答案的 Alabama $1,266 / Hawaii $2,473 就是这张表）；UHC 靠「Key takeaways」直答块 + 脚注被引（$450 / $940 / 空中 $12k–25k 在合成答案中逐字出现）。
3. **没人做好的地方**：作者/审核人（除 CareCredit 的一位撰稿人外，没有医疗/计费审核人）、`sameAs`/Wikidata 实体信号（全部为空）、州法事实一致性（UHC 写 10 州，healthinsurance.org 写 23 州，Commonwealth Fund 写 24 州）、城市问法（Chicago 问法时 AI 合成答案直接引市政府 PDF 与市法典，**没有任何竞品被引**）。
4. **答案形态固定**：全国区间 → 州平均（BLS/ALS）→ Medicare 基准（基础费 + $9.15/英里）→ 有/无保险自付 → 空中救护 → No Surprises Act 不管地面、州法补位。机会在「城市官方费率」「州法可行动矩阵」两块：AI 现在拿的是政府原文件或保险科普，不是专门站。
5. **她最该做的 5 件事**：①每页首段 40–60 字直答 + 来源；②城市页以市政费率原文件为锚（带生效日、PDF 链接、减免规则）；③州法矩阵做成「唯一正确且带日期」的版本；④公开方法论/数据下载页 + 实名审核人；⑤robots 全放行 AI 检索爬虫 + `llms.txt`，每周用免费方式（WebSearch 合成、Bing/Google 手动、GSC）自检。

---

## 一、逐站 GEO 信号（字段固定）

字段说明：AI 爬虫规则 = robots.txt 是否单独点名 GPTBot / ChatGPT-User / OAI-SearchBot / PerplexityBot / ClaudeBot / Google-Extended / CCBot / Applebot-Extended。**6 个站全部未点名任何 AI 爬虫（`grep` 计数均为 0），即全部按 `User-agent: *` 规则对 AI 爬虫放行**（文件：`geo-raw/*.robots.txt`）。

### 1. ambulancecost.com

| 字段 | 结果 | 来源 |
| --- | --- | --- |
| robots / AI 爬虫 | `User-Agent: * Allow: /`，未点名 AI 爬虫 → 全放行 | https://www.ambulancecost.com/robots.txt |
| llms.txt / llms-full.txt | **有 llms.txt（200，2,987 字节）**：一句话定位、核心页、解释文、方法论页、CMS/Medicare/KFF 外链、免责声明；llms-full.txt 404 | https://www.ambulancecost.com/llms.txt；`geo-raw/www.ambulancecost.com.llms.txt` |
| sitemap / lastmod | 30,303 个 URL，**全部同一 lastmod `2026-07-22T22:35:05Z`**（模板式统一时间，非真实逐页更新） | https://www.ambulancecost.com/sitemap.xml |
| JSON-LD 首页 | WebSite+SearchAction、Organization、WebPage、**Dataset**、**FAQPage**（Question/Answer）、Place；datePublished 2026-03-10，dateModified 2026-07-22 | `geo-raw/ac-home.html` |
| JSON-LD 州页 (CA) | BreadcrumbList、Organization、WebSite；**无 FAQ/Dataset/日期** | `geo-raw/ac-state.html` |
| JSON-LD 城市页 (San Francisco) | BreadcrumbList、**FAQPage**；无 Dataset、无日期字段 | `geo-raw/ac-city.html` |
| JSON-LD resources | `where-we-get-data`、`does-insurance-cover-ambulance`：Article + Breadcrumb，dateModified 写成 "June 14, 2026" / "March 12, 2026"（**非 ISO 格式**），**无 author** | `geo-raw/ac-r-data.html`、`ac-r-ins.html` |
| 一句话直答 | 首页（WebSearch 抽取）：「a ground ambulance ride typically costs between $500 and $3,000+ … plus a per-mile charge」；州页首句：「A typical ground-ambulance bill here runs $2,822 – $3,406 — 147% above the national median」 | WebSearch 结果；`ac-state.html` |
| 表格 | 州/城页 `<table>` 数 0（数据用卡片 div 呈现）；保险文 1 张表 | `sig.py` 输出 |
| 可引用数据块 | 城市页：TNT $568、生效日 2025-09-01、updated 2026-06-11、「Report Inaccurate Data」 | `ac-city.html` |
| 方法论/来源页 | 有 `/resources/where-we-get-data`（CMS CY2026 AFS、PUF、市政费率） | https://www.ambulancecost.com/resources/where-we-get-data |
| 作者/审核人 | **无**（About 页无人名，JSON-LD 无 author/reviewedBy） | `ac-about.html` |
| 出站权威引用 | 首页 cms.gov、kff.org；CA 州页链到 sandiegocounty.gov、longbeach.gov、berkeleyca.gov、data.cms.gov 等市郡原文件 | `sig.py` 输出 |
| 实体信号 | Organization 无 `sameAs`；Wikipedia/Wikidata 条目：未取得（未查到） | `ac-home.html` |
| 被引情况 | WebSearch 合成答案第 1 来源（两问）；GoodRx 参考文献引用（旧材料，浏览器核验） | 本文第二节；`ambulance-competitor-analysis.md` |

### 2. worldpopulationreview.com（州排名页）

| 字段 | 结果 | 来源 |
| --- | --- | --- |
| robots / AI 爬虫 | `User-agent: * Disallow:`（空）→ 全放行 | https://worldpopulationreview.com/robots.txt |
| llms.txt | 404 / 404 | `geo-raw/` |
| sitemap | 有 sitemap-index；本页 lastmod 未逐条核对（未取得） | robots.txt |
| JSON-LD | Article、Organization；datePublished 2026-10-22（标题写「2026」，**每年刷新年份**）；author = 「World Population Review」（机构，无人名） | `geo-raw/wpr.html` |
| 直答 | 无文字直答，H1 后直接是图表 + 51 行表 | `wpr.html` |
| 表格 | 1 张 51 行 BLS/ALS 表 | 同上 |
| 方法论/来源 | Sources 只有 1 条：CareCredit（数字与 CareCredit 完全一致） | WebSearch 抽取 |
| 作者/审核 | 无 | — |
| 实体信号 | sameAs 空 | `wpr.html` |
| 被引情况 | 「how much / by state」两问 WebSearch 合成答案均引用（州最高/最低数字） | 第二节 |

### 3. carecredit.com（Well U 文章）

| 字段 | 结果 | 来源 |
| --- | --- | --- |
| robots / AI 爬虫 | 只禁 /training/ 等内部路径，未点名 AI → 放行 | https://www.carecredit.com/robots.txt |
| llms.txt | 404 | `geo-raw/` |
| 访问 | 本轮 curl 200（早期材料曾 Akamai Access Denied，时有时无） | `geo-raw/carecredit.html` |
| JSON-LD | Article、**MedicalWebPage**、BreadcrumbList、Person（作者 Adrienne Santos-Longhurst，sameAs 指向其 contently 作品集）、Organization；datePublished 2023-03-01，dateModified 2025-04-11 | `carecredit.html` |
| 直答 | 页首摘要：「national average … $1,481 for BLS and $1,613 for ALS」 | 同上 |
| 表格 | 2 张（全国 BLS/ALS 区间表 + 50 州表） | 同上 |
| 来源 | 有编号脚注（FAIR Health 私保理赔研究等），出站 medicareinteractive.org、montgomerycountymd.gov | 同上 |
| 作者/审核 | 有撰稿人，**无医学/计费审核人** | 同上 |
| 弱点 | 数据 2025-04 后未更新；文末导向 CareCredit 信用卡（商业动机） | 同上 |
| 被引情况 | 「by state」问法 WebSearch 合成答案引用 | 第二节 |

### 4. goodrx.com

| 字段 | 结果 | 来源 |
| --- | --- | --- |
| 页面 / llms.txt | **403**（PerimeterX「Access to this page has been denied」）→ 正文、JSON-LD、llms.txt **未取得** | `geo-raw/goodrx.html` |
| robots / AI 爬虫 | robots.txt 可取：未点名 AI 爬虫，只禁 /coupon、/my-rx 等 → 文本上放行；但 **机器人防护层会挡非浏览器请求**，实际 AI 爬虫能否抓取：未取得 | https://www.goodrx.com/robots.txt |
| 已知 | 旧材料浏览器核验：州表数字与 AmbulanceCost 重合，参考文献点名 AmbulanceCost | `ambulance-competitor-analysis.md` |
| 被引情况 | 本轮 4 个问法的 WebSearch 合成答案中**未出现** GoodRx | 第二节 |

### 5. uhc.com（文章）

| 字段 | 结果 | 来源 |
| --- | --- | --- |
| robots / AI 爬虫 | 未点名 AI → 放行 | https://www.uhc.com/robots.txt |
| llms.txt | **有（200）**，全站导航型（门户、计划、找医生），未单独列救护车文章；llms-full.txt 404 | https://www.uhc.com/llms.txt |
| 访问 | 本轮 curl 200（早期材料曾 403） | `geo-raw/uhc.html` |
| JSON-LD | NewsArticle/Article、WebPage、Person、Organization；datePublished 2026-05-19，dateModified 2026-10-23；author = UnitedHealthcare（机构） | `uhc.html` |
| 直答 | **「Key takeaways」块**：有保险约 $450+、无保险约 $940+、空中 $12,000–25,000、联邦法不管地面、Medicare 可能支付 | 同上 |
| 来源 | 编号脚注带「Updated … Accessed Apr. 2026」，出站 kffhealthnews.org、healthaffairs.org、medicare.gov | 同上 |
| 弱点 | 州法写「Ten states」，与 healthinsurance.org（23 州）、Commonwealth Fund（24 州）不一致 → 过时事实 | WebSearch 结果 |
| 被引情况 | 「how much」问法 WebSearch 合成答案中 $450 / $940 / 空中区间均标注引用 UHC | 第二节 |

### 6. masaaccess.com

| 字段 | 结果 | 来源 |
| --- | --- | --- |
| robots / AI 爬虫 | 只禁 HubSpot 预览路径 → 放行 | https://masaaccess.com/robots.txt |
| llms.txt | 404 | `geo-raw/` |
| JSON-LD | BlogPosting、WebPage、Person、Organization；2025-12-08 发布；author = MASA | `geo-raw/masa.html` |
| 直答 | 无；开头为情绪铺垫，第二段才有「average invoice … $2,086」 | 同上 |
| 表格 / 来源 | 表格 0；权威出站链接 0 | `sig.py` 输出 |
| 弱点 | 会员产品导购、无来源数字 | 同上 |
| 被引情况 | 本轮问法中**未出现** | 第二节 |

---

## 二、被引用情况（公开、免登录可得部分）

方法：WebSearch 工具返回的「Synthesis」合成答案及其来源编号（这是一个 AI 合成的答案，作为「AI 回答引擎会引什么」的近似样本；**不等于** Google AI Overview / ChatGPT / Perplexity 的真实结果）。日期 2026-10-28。

| 问法 | 合成答案引用的来源 | 页面类型 |
| --- | --- | --- |
| how much does an ambulance cost 2026 | ambulancecost.com 首页、WPR 州表、MedPAC PDF（Medicare $9.15/英里）、UHC 文章、Sacramento Metro Fire 费率页 | 数据库首页 / 州表 / 政府 PDF / 保险科普 / 市政费率 |
| ambulance cost by state 2026 | WPR、CareCredit、s2reason.com（Medicare AFS 按州查询工具）、ambulancecost.com、UHC | 州表 ×2 / 工具页 / 数据库 / 保险科普 |
| ambulance cost in Chicago without insurance | chicago.gov 费率规则 PDF、市法典 amlegal、chicago.gov 账单页、parkingday.org、shunauto.com（后两者为内容农场且数字过时/错误） | **政府原文件为主，无专门竞品** |
| does No Surprises Act cover ground ambulance state laws 2026 | Commonwealth Fund 地图、healthinsurance.org、CMS PDF ×2 | 智库 / 非营利科普 / 政府 |

计数（4 问，每问 4–5 来源）：ambulancecost.com 2、WPR 2、UHC 2、CareCredit 1、GoodRx 0、MASA 0；政府/智库原始文件合计 8。

**未取得**：Google AI Overview（curl 返回 JS 页面，无结果内容）、Perplexity（403 Cloudflare「Just a moment」）、Bing Copilot / DuckDuckGo（返回页面无来源内容）、ChatGPT（需登录，未尝试）。各引擎真实引用率、点击量、排名：未取得。

新发现竞品：**s2reason.com/ambulance-fee-schedule-lookup**——Medicare AFS 按州/locality 查询，写明「every figure read from the CMS file… verified against all 10,536 rate cells」，在「by state」问法被引。这是「方法论透明 → 被引」的样板。

---

## 三、分析

### 每个竞品做得好 / 做得不好

| 站 | 做得好 | 做得不好 |
| --- | --- | --- |
| ambulancecost.com | llms.txt；首页 Dataset+FAQPage；首段直答；方法论页；城市页链市政原文件 + 生效日 + 纠错入口；被 GoodRx 引用（第三方背书） | 3 万页同一 lastmod（更新信号失真）；无作者/审核人；无 sameAs；州页无 FAQ/日期 schema；数据放 div 不放 table；州页自相矛盾（旧材料：NY「1 verified」列 6 家）；城市问法（Chicago）没被引 |
| WPR | 年份标题 + 一张干净 51 行表，极易被抽取 | 数字全部转抄 CareCredit、唯一来源；无方法说明；无作者 |
| CareCredit | MedicalWebPage + Person schema；全国区间表 + 州表；脚注来源 | 2025-04 后未更新；无审核人；商业导流 |
| GoodRx | 品牌权威；参考文献规范（旧材料） | 机器人防护把非浏览器请求挡在外（403），本轮问法未被引 |
| UHC | Key takeaways 直答块；脚注带访问日期；dateModified 新 | 州法「10 州」过时；数字粗；机构署名无人名 |
| MASA | 有日期、Person schema | 无直答、无表、无出站来源，导购为主；未被引 |

### ambulancecost.com 的 GEO 强弱

- 强：数据库型站 + llms.txt + 方法论页 + 首页直答，本轮两大泛问法都被引；被 GoodRx 当参考文献，等于大站替它做了实体背书。
- 弱：被引的几乎都是**首页**，州/城长尾页在本轮样本里没被引用（样本小，不能下结论，只能说「未观察到」）。城市问法 AI 直接去拿市政府 PDF——说明它的城市页没有比原文件更「可引」。

### 这个话题的 AI 答案形态（本轮合成答案归纳）

1. 全国区间（$500–$3,000+）→ 2. 州平均 BLS/ALS（CareCredit/WPR 表）→ 3. Medicare 基准（基础费 + $9.15/英里，MedPAC/CMS）→ 4. 有/无保险（UHC $450/$940）→ 5. 空中 $12k–25k → 6. No Surprises Act 不覆盖地面，州法补位（州数各家说法不一）。

**还没人被稳定引用的意图块**（对照 `ambulance-competitor-analysis.md` 机会点）：
- **城市官方费率**：AI 用政府 PDF，内容农场混入错误数字（shunauto 引 2,969 旧价）→ 需要「核实+生效日+原件链接+减免规则」的城市页。
- **州法可行动矩阵**：州数 10 / 23 / 24 冲突；没有「我的计划类型（ERISA 自保）是否适用」的可查表。
- **事后账单行动流**：本轮样本没有任何竞品因「怎么处理账单」被引（未专门测问法，列为待测）。

---

## 四、给她的打法（按优先级）

| # | 打法 | 怎么做 | 怎么判断它失败了 |
| --- | --- | --- | --- |
| 1 | 直答块 | 每页 H1 下 40–60 字一句话答案（数字 + 范围 + 适用条件 + 日期），紧跟「来源：xx 文件，生效日 xx」 | 4–8 周后同问法的 WebSearch/Bing 合成答案仍不出现本站；或被引但抽到的是别段文字 |
| 2 | 真 `<table>` + 事实卡 | 州/城费率用 HTML table（BLS/ALS/里程/TNT/Medicare 基准/生效日/来源链接列）；每页一张「事实卡」（5 行内可被整段引用） | 合成答案引用的数字与本站表格不同（说明抽取失败或被别站覆盖） |
| 3 | 城市页以官方原件为锚 | 先做前 50–100 个大城市：市/郡费率 PDF 链接、生效日、减免/分期规则（如 Chicago FPL 阶梯）、balance billing 规则 | 「ambulance cost in [city]」问法仍只引 .gov PDF 和内容农场 |
| 4 | 州法矩阵（唯一正确版） | 50 州 × {是否有地面救护保护、生效日、适用计划类型、公立/私立、法条链接、投诉入口}，每行带核对日期；文首解释 10/23/24 州差异来源 | 合成答案仍引用 UHC「10 州」或其他站；或你自己发现超 90 天未复核 |
| 5 | 数据与方法论页 | `/methodology`（来源、计算、更新频率、已知局限）+ 可下载 CSV + 变更日志；学 s2reason 写「每个数字可回溯到哪个文件哪一行」 | 无外部站引用/链接该页；GoodRx 类大站引用的仍是竞品 |
| 6 | YMYL 信任信号 | 实名编辑 + 一位有资质的审核人（医疗计费/保险背景，真实可查）；About 写清谁在做、利益关系、无广告导流；免责声明 | 找不到愿意实名的审核人 → 宁可不写审核人，不要虚构 |
| 7 | 结构化数据 | 首页 Organization（含 sameAs 指向真实社媒/GitHub 数据仓库）+ WebSite；数据页 Dataset（含 distribution、temporalCoverage、license）；城市/州页 BreadcrumbList + FAQPage（只放页面上真实可见的问答）+ dateModified（ISO 格式、真实变动才改） | Rich Results Test / Schema validator 报错；schema 内容与页面可见内容不一致 |
| 8 | robots / llms.txt | robots 对 OAI-SearchBot、ChatGPT-User、PerplexityBot、ClaudeBot、Googlebot、Bingbot 放行（训练类 GPTBot/Google-Extended/CCBot 是否放行是取舍，建议放行以扩大曝光）；不要套强 WAF 挡爬虫（GoodRx 反例）；`/llms.txt` 列方法论、州法矩阵、数据下载、核心城市 | 服务器日志里看不到上述 UA 的抓取；或 WAF 日志显示拦截 |
| 9 | 更新节奏 | 每年 1 月 CMS AFS 更新当周发 2027 版；州法每季度复核；城市费率按原件生效日更新；sitemap lastmod 只在内容真实变化时改 | lastmod 全站同一时间（ambulancecost 的问题）；AI 答案里出现你页面的旧年份数字 |
| 10 | 避免模板化稀释 | 无核实数据的城市不生成独立页（或 noindex），先合并到州页；每个城市页必须至少有 1 个独有事实（原件费率/提供方/减免规则） | GSC「已抓取-未编入索引」比例高；长尾页零展示 |
| 11 | 免费自检 | 每周固定 15 个问法（泛问 / by state / 10 个城市 / Medicare / NSA / 争议账单）：①WebSearch 合成答案来源记录；②Bing 搜索手动看 Copilot 引用；③Google 手动看 AI Overview；④GSC 效果报告（含 AI 相关报告若可用，见收藏 [126]）；⑤服务器日志按 AI 爬虫 UA 统计；⑥Bing Webmaster Tools（免费）。结果记表，不猜比例 | 连续 8 周 15 问法中本站被引 0 次 → 回到 #1–#4 查原因 |

### 值得学

- ambulancecost：`/llms.txt` 结构（定位 + 核心页 + 方法论 + 权威外链 + 免责）；首页 Dataset + FAQPage；城市页「生效日 + Report Inaccurate Data」。
- UHC：「Key takeaways」开头直答 + 脚注写「Updated / Accessed」日期。
- CareCredit：MedicalWebPage + Person schema；全国区间表放在州表之前。
- WPR：标题带年份 + 一张极干净的表（最易被抽取）。
- s2reason：方法论写到「可逐格核对」的程度。
- 政府原件被直接引用 → 你的价值是「把原件整理、核实、标日期、链接」，而不是改写。

### 应该避免

| 避免项 | 风险 |
| --- | --- |
| 刷引用（在 Reddit/Quora/论坛批量自问自答、水军评论、买 AI 推荐「信源」投放） | 平台封号；Google 垃圾政策中的站点声誉/链接操纵；被识别后整站信任下降；YMYL 话题尤其严重 |
| 伪造或插值数据冒充「verified」（没有原件却写核实价、编造审核人） | 用户据此付账产生实害；被纠错或媒体曝光；Google 质量评估 YMYL 最低分；可能涉及消费者保护问题 |
| 批量低质城市页（3 万页同模板、只换城市名） | 规模化内容滥用政策；索引膨胀而不被引；稀释站点整体质量（ambulancecost 已显露自相矛盾问题） |
| 隐藏文本 / 只给爬虫看的内容（cloaking、给 AI UA 不同内容、白字关键词、schema 写页面没有的 FAQ） | 违反 Google 垃圾政策；结构化数据手动处罚；AI 引用到与页面不一致的话导致信任崩塌 |
| 假 lastmod / 每天改日期 | 更新信号失效，搜索引擎忽略 lastmod |
| 照抄竞品数字不注来源（WPR 模式） | 数字一旦被上游改，全错；无独特信息不会被优先引用 |
| 律师/贷款导流嵌入正文 | YMYL 利益冲突，降低被当作中立来源的概率 |

---

## 五、没取到的东西

- GoodRx 页面正文、JSON-LD、llms.txt（PerimeterX 403）。
- Google AI Overview、Perplexity（Cloudflare 403）、Bing Copilot、ChatGPT 的真实回答与引用；各站真实引用率、流量、排名。
- 各站 Wikipedia/Wikidata 实体条目（未查）。
- WPR/CareCredit/UHC/MASA sitemap 中本页的 lastmod（未逐条核对）。
- 「怎么处理/争议救护车账单」类问法的引用来源（本轮未测）。

---

## 六、她收藏的 GEO 方法论

来源文件：`/workspace/bookmarks.txt`、`/workspace/bookmarks-analysis.md`、`/workspace/x-bookmarks-repo/bookmarks.md`、`/workspace/outputs/seo-methodology-from-bookmarks.md`。编号为 `bookmarks-analysis.md` 中的序号。

| 方法 | 要点（只写收藏里有的） | 来源 | 本项目用法 |
| --- | --- | --- | --- |
| GEO 就是 SEO | Google 称 AI Mode/Overview 从索引取内容；排名只占 1/3，还有抓取、索引 | [141] @loki_yan_seo https://x.com/loki_yan_seo/status/2110891254217400371 | 先保证可抓取/可索引（打法 #8、#10） |
| SEO+AEO 提示词仓库 | 技术 SEO 审计、逆向前 10 SERP、写有 information gain 的对比页、查 ChatGPT/Perplexity 引用 | [166] @illyism https://x.com/illyism/status/2110180038637408357 ；star `Illyism/seo-skills` | 用于审计与 info-gain 页（打法 #3–#5） |
| claude-seo 子技能 | 技术 SEO、E-E-A-T、schema、GEO/AEO 等 26 子技能 | star `AgriciDaniel/claude-seo`（`seo-methodology-from-bookmarks.md` 第 25 行） | E-E-A-T 与 schema 检查（打法 #6、#7） |
| ChatGPT Fan-out Queries | 开源 Skill 输出 ChatGPT 拆分子查询报告 | [175] @CoderJeffLee https://x.com/CoderJeffLee/status/2110215759075164502 | 用来扩展自检问法表（打法 #11） |
| GSC 生成式 AI 报告 | GSC 新增 Generative AI 表现报告 | [126] @alexgroberman https://x.com/alexgroberman/status/2111484443726852385 | 免费观察 AI 流量（打法 #11）；功能是否对她的站可用：未核实 |
| ChatGPT 推荐 → 外链 | 问 ChatGPT 最佳 X → Ahrefs 查被推荐者外链 → 联系 best-of 列表 | [71] @yanhua1010 https://x.com/yanhua1010/status/2112704120641765471 | 只读借鉴思路；Ahrefs 付费，联系对方需她本人批准 |
| GEO 布局平台 | 除 Reddit 外 12 个值得布局平台（YouTube 等） | [64] @houzhongji89090 https://x.com/houzhongji89090/status/2112867613546258882 | 真实内容分发，不刷（见避免项） |
| Reddit 高质量评论 | 五点方法 | [119] @heizolshao https://x.com/heizolshao/status/2111970717218816316 | 只做真实有用回答 |
| URL 用连字符 | Google 把 - 当分词，_ 不是 | bookmarks.txt #18 @loki_yan_seo | URL 规范 |
| 官网做 GEO/SEO | 用官网承接 GEO | [9] @vista8 https://x.com/vista8/status/2115081949958316244 | — |
| Supabase SEO/GEO 值得学 | 案例 | [161] @loki_yan_seo https://x.com/loki_yan_seo/status/2110708811128594793 | 可后续拆解 |
| 风险提醒 | AI Overview 冲击 SEO（[131]）；GEO 效果难量化、过度承诺会客诉（bookmarks-analysis.md 第 82 行） | [131] https://x.com/LeMutantX/status/2111047881977139307 | 自检只记事实，不报比例 |
| 无细节 | 「跑通 GEO 才发现有多爽」 | [168] https://x.com/Jiaxi_Cui/status/2110286729534173577 | 无可用方法 |

**补充（非她收藏，为通用做法）**：`llms.txt` 约定（llmstxt.org）；OpenAI 区分 OAI-SearchBot（检索）与 GPTBot（训练）、Google-Extended 控制 Gemini 训练而不影响搜索；Google 垃圾内容政策（规模化内容滥用、cloaking、隐藏文本）；Bing Webmaster Tools 免费；结构化数据只标记页面可见内容。以上为通用知识，本轮未逐条抓取官方页面核对。

---

## 更正（2026-10-28，据 [web-geo-requirements.md](./web-geo-requirements.md) 官方核对）

- Claude 的搜索爬虫是 **Claude-SearchBot**，不是 ClaudeBot（ClaudeBot 属训练类）。放行搜索类：OAI-SearchBot、PerplexityBot、Claude-SearchBot。
- 本文推荐的 **FAQPage、Dataset 标记不再算有效的 AI 引用手段**：Google 的 FAQ 富结果自 2026-05-07 起不再显示，Dataset 只用于 Dataset Search；`llms.txt` Google 明确表示忽略，仅作可选。
- 其余结论（直答块、核实费率、审核人署名、州法表、避免模板薄页）不变。
