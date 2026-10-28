# ambulancecost.com 竞品逐页 SEO 分析（模板 + 逐页 + 缺口打法）

取数：2026-10-28（UTC+8），curl（桌面 UA）抓公开 HTML，BeautifulSoup 解析。原始解析输出：`/workspace/outputs/competitor-seo-raw/parsed-2026-10-28.txt`；脚本 `parse.py`；`robots.txt`、`sitemap.xml` 同目录。历史记录：`/workspace/outputs/competitor-pages-raw.md`、`ambulance-competitor-analysis.md`、`competitor-screenshots/`。
**DR、流量、排名、搜索量、外链数、CWV：全部未取得**（需 Ahrefs/Semrush/CrUX 等，本次不登录不付费）。「词数」为去掉 script/style 后的可见文本词数，含导航页脚。

## 结论先行
1. **它的护城河是 3 万个程序化城市页 + 少量「核实」页**：sitemap 30,303 URL，其中 30,208 是 `/ambulance-cost/{州}/{城市}`，51 个州页，41 个 resources。所有 lastmod 同为 2026-07-22（批量生成，不是真更新时间）。
2. **小城市页是近 100% 重复的薄页**：Adamant, VT 与 Ascutney, VT 去掉城市名后文本相似度 1.000；都是「Data Unavailable / modeled estimate」。
3. **数据与结构有硬伤**：VT 有 287 个城市页但州页 `/ambulance-cost/vt` 返回 404 且不在 sitemap；sitemap 里有不存在的「州」EM，被排「#48 of 51 states」；军邮 APO 页标题写「Apo, FL」；**纽约市页的费率来源写的是「Volunteer Ambulance Corps Of Livingston Manor Inc」**，同时还存在 `/ny/new-york` 另一页，数字不同（自我蚕食）。
4. **YMYL 信任信号弱**：全站无作者、无审核人；resources 文章（除 1 篇）零出站引用；Article schema 的 dateModified 写成「March 12, 2026」非 ISO；About / Resources / No Surprises 三页共用默认 title+description 且无 canonical。
5. **它做得好的要学**：城市页 FAQPage+BreadcrumbList、TNT 费、Medicare 基准对比、SF 这种带条例号/生效日/更新日的核实页、首页 Dataset schema（CC BY 4.0）、「Submit Local Rate」众包入口。

---

## 第一部分：逐页分析模板（字段固定）

每页一节，按下列字段填写；「取数方法」列说明能否用 curl/WebFetch 实际取到。

| # | 字段 | 看什么 | 取数方法 |
|---|---|---|---|
| 1 | URL / 页面类型 / HTTP 状态 | 首页、州、城市、ZIP/计算器、resources、About/方法论、政策页 | curl -w http_code |
| 2 | 目标词与意图 | 由 title/H1 推断主词；信息/工具/交易意图 | 人工判断（搜索量未取得） |
| 3 | Title（长度） / Meta description | 是否独有、含词、含年份/数字 | `<title>`、meta[name=description] |
| 4 | Canonical / robots meta / 在不在 sitemap | 可索引性、重复 | link[rel=canonical]、meta robots、sitemap |
| 5 | H1 / H2 / H3 | 层级、是否模板化、是否覆盖子意图 | h1-h3 |
| 6 | URL 结构 | 层级、连字符、带词 | URL |
| 7 | 页面模块与信息密度 | 模块列表、可见词数、独有数据点 | 可见文本 |
| 8 | 内链 | 上级/同级/下级/资源入口，唯一内链数 | a[href] 同域 |
| 9 | 出站/权威引用 | 出站域名、是否 .gov/研究 | a[href] 外域 |
| 10 | 结构化数据 | JSON-LD 类型、合规（日期格式、字段） | script[type=ld+json] |
| 11 | E-E-A-T / YMYL | 作者、审核、来源、更新日期、免责声明 | 文本 + schema |
| 12 | CTA / 变现 | 广告、联盟、表单、电话 | 文本、外链 |
| 13 | 重复度/模板化 | 与同类页相似度 | difflib 比对 |
| 14 | 数据准确度 | 数字自洽、来源匹配 | 文本对照来源 |
| 15 | 移动端/速度可见问题 | HTML 体积、响应时间（仅 curl 可见） | curl size/time；CWV 未取得 |
| 16 | 可被超越的缺口 | | 分析 |
| 17 | 可复制 / 不要复制 | | 分析 |

全站通用事实（每页不再重复）：Next.js（HTML 含 `_next`）；SSR 输出完整正文；每页底部共用模块「End Surprise Ambulance Bills. / GAP The Billing Loophole / GOAL Our Policy Goal / Disclaimer」；页脚 Privacy、Terms；robots.txt 仅 `Allow: /` + sitemap；全站无广告脚本（未检出 adsbygoogle/gtag），**未见变现**。

---

## 第二部分：ambulancecost.com 逐页

### 0. robots.txt / sitemap.xml
- robots：`User-Agent: * / Allow: / / Sitemap: https://www.ambulancecost.com/sitemap.xml`。
- sitemap：单文件 30,303 URL（无 sitemap index）。priority：首页 1；州 0.8（51）；大城市 0.9（316）；普通城市 0.6（29,892）；resources 0.7（41）；/about 0.4；/no-surprises 0.5。**所有 lastmod = 2026-07-22T22:35:05.540Z**。
- 州级 URL 51 个，含「em」，**缺 vt**；有城市页但无州页的州/属地：aa, ae, ap, as, fm, gu, mh, mp, pr, pw, vi, vt（VT 287 城、PR 99 城、GU 18 城）。
- 缺口：sitemap 不分片、lastmod 失真；州层级缺失 → 城市页面包屑上级 404。

### 1. 首页 https://www.ambulancecost.com/
| 字段 | 事实 |
|---|---|
| 状态/类型 | 200，首页+计算器（ZIP/城市搜索框 `ambulanceZipSearch`，客户端搜索，无 ZIP 独立 URL） |
| 目标词 | how much does an ambulance cost / ambulance cost（工具+信息） |
| Title | How Much Does an Ambulance Cost? 2026 Rates by City \| AmbulanceCost（67） |
| Meta | Look up ground ambulance costs by ZIP or city. Compare … 2026 Medicare benchmark, TNT fees, and your state’s surprise-billing protections. |
| Canonical | https://www.ambulancecost.com（无尾斜杠） |
| H1/H2 | H1「Ambulance Cost」；H2：End Surprise Ambulance Bills. / How much does an ambulance cost? / Ambulance costs by city / Browse by state / Learn more about ambulance bills |
| 模块 | 搜索框、三卖点、政策倡导（Find Representatives）、FAQ 段、城市价格卡（SF $2,555、LA $1,862、New York $1,385…）、州索引、资源入口；692 词 |
| 内链 | 82 个唯一内链（州页 + 大城市 + resources） |
| 出站 | cms.gov、kff.org |
| Schema | Organization, WebSite, WebPage, **Dataset**（license CC BY 4.0）, FAQPage（1 问，datePublished 2026-03-10） |
| E-E-A-T | 自称「largest open database of verified US ambulance prices, covering 1 in 3 cities」；无作者/团队名；有免责声明 |
| 速度 | HTML 245,675 字节（全站最大），curl 0.07s |
| 缺口 | H1 只有 2 个词；FAQ 只有 1 问；「1 in 3 cities」无出处 |
| 可复制 | Dataset schema；首页直接给城市价格卡；FAQ 首段直接回答 |
| 不要复制 | 首页 H2 第一个是政策倡导，与搜索意图无关 |

### 2. /about
| 字段 | 事实 |
|---|---|
| 状态 | 200 |
| Title/Meta | **默认** AmbulanceCost \| Ground Ambulance Rate Database（46）/ Transparency for ground ambulance rates and Medicare benchmarks. |
| Canonical | **无** |
| H1/H2 | About Us；The Policy Gap / End Surprise Ambulance Bills. |
| 模块 | 使命叙述 603 词；**无团队、无创始人、无联系方式、无方法论链接以外的资质** |
| 内链 | 6（只有导航） ；出站 0 |
| Schema | Organization, WebSite |
| E-E-A-T | 弱：谁做的、谁审核、怎么联系都没有（YMYL 关键缺口） |
| 可复制/不要复制 | 不复制；我们要有具名作者/审核、数据更新流程、联系邮箱（文档里不写具体地址） |

### 3. 州页（共用结构：Title「Ambulance Cost in {State} (2026) — How It Compares」；H2 = How X compares / What drives the cost / Surprise Billing Protection / Verified provider rates / Browse cities / Compare other states / Understand your bill；Schema = Organization, WebSite, BreadcrumbList；**无 FAQPage**；**og:image 缺失**）

| 页 | Title 长度 | Meta 关键句 | H2 数 | 词数 | 内链 | 出站域名 |
|---|---|---|---|---|---|---|
| [CA](https://www.ambulancecost.com/ambulance-cost/ca) | 53 | $2,822–$3,406，高于全国中位 147%，#1 of 51 | 7 | 807 | 61 | data.cms.gov + 7 个县市政府站（berkeleyca.gov、sandiegocounty.gov、longbeach.gov…） |
| [TX](https://www.ambulancecost.com/ambulance-cost/tx) | 48 | $1,052–$1,105，低 20%，#33 | 7 | 743 | 45 | data.cms.gov、data.texas.gov |
| [NY](https://www.ambulancecost.com/ambulance-cost/ny) | 51 | $1,385–$1,679，高 22%，#17 | 7 | 583 | 26 | data.cms.gov |
| [TN](https://www.ambulancecost.com/ambulance-cost/tn) | 52 | $1,022–$1,415，高 3%，#25 | 6（无 What drives） | 486 | 24 | data.cms.gov |
| [WY](https://www.ambulancecost.com/ambulance-cost/wy)（小州） | 50 | $1,469–$1,521，高 10%，#21 | 6 | 426 | 21 | data.cms.gov |
| [VT](https://www.ambulancecost.com/ambulance-cost/vt) | — | **404，robots noindex** | — | — | — | — |
| [EM](https://www.ambulancecost.com/ambulance-cost/em) | 45 | 「EM」$621–$744，**#48 of 51 states** | | | | |

- 目标词：ambulance cost in {state} / {state} ambulance cost（信息+比价）。
- 信息密度：大州（CA）有「Verified provider rates」引地方政府费率表，小州只剩 CMS；内容随数据量递减（807→426 词）。
- 内链：上级（首页）、同级（全部州）、下级（只列部分城市，TN 仅 5 个大城市；该州数百个小城市页无州页入口 → 依赖 sitemap 发现）。
- 数据准确度：「51 states」排名里包含 EM（非州）而 VT 缺失——排名本身失真。
- 缺口：无 FAQ schema、无州法条文链接（「Surprise Billing Protection」段未链接州法/州保险局，CA 出站也只链县市费率）、无更新日期、无作者。
- 可复制：Meta 里直接给区间+百分比+排名；州间对比；县市官方费率出站引用（CA）。
- 不要复制：用 2 字母代码直接生成「州」（EM/AA）；州页缺失却生成城市页。

### 4. 城市页（共用：Title「Ambulance Cost in {City}, {ST} (2026) — BLS, ALS & Mileage Rates」；H1「Ambulance Cost in {City} , {ST}」**逗号前多一个空格**；Schema = Organization, WebSite, BreadcrumbList, FAQPage（3–4 问）；模块：TNT 费 → 交通费区间(BLS–ALS)+每英里 → Medicare 基准+每英里 → Surprise Billing Protection → Will insurance pay → FAQ → More cities → Understand your bill（5 篇资源文）→ 倡导块）

| 页 | Title/Meta 关键数字 | 数据来源（页内） | 更新日期 | 词数 | 内链 | 出站 |
|---|---|---|---|---|---|---|
| [San Francisco](https://www.ambulancecost.com/ambulance-cost/ca/san-francisco)（priority 0.9） | $2,555–$2,555 + $49/mi，TNT $568，Medicare $597–$709 | SFFD/Controller FY2025-26 EMS fee schedule（Health Code Art.3 Sec 128.1，eff 2025-09-01） | Last updated 2026-06-11 | 761 | 20 | sf-fire.org |
| [New York City](https://www.ambulancecost.com/ambulance-cost/ny/new-york-city) | $1,200–$1,400 + $24/mi，Medicare $464–$551 | **「Volunteer Ambulance Corps Of Livingston Manor Inc」** 的费率表 | 2026-06-14，Effective 2024-01-01 | 800 | 18 | data.cms.gov |
| [New York（另一页）](https://www.ambulancecost.com/ambulance-cost/ny/new-york) | $1,385–$1,679 + $20/mi，Medicare $525–$624 | — | — | | | |
| [Nashville](https://www.ambulancecost.com/ambulance-cost/tn/nashville) | $650–$650 + $13/mi，Medicare $434–$516 | Metropolitan Government…费率表 | 2026-06-14 | 753 | 16 | data.cms.gov |
| [Ascutney, VT](https://www.ambulancecost.com/ambulance-cost/vt/ascutney)（小城，0.6） | $1,094–$1,515 + $24/mi，Medicare $465–$552；TNT「Data Unavailable」 | 「modeled estimate: Medicare × regional markup」 | 无 | 692 | 12 | 无 |
| [Adamant, VT](https://www.ambulancecost.com/ambulance-cost/vt/adamant) | **与 Ascutney 数字完全相同** | 同上 | 无 | 692 | 12 | 无 |
| [APO (aa)](https://www.ambulancecost.com/ambulance-cost/aa/apo) | Title「Apo, FL」，Meta「check AA surprise-billing protections」 | 估算 | 无 | 745 | 20 | 无 |

- 目标词：ambulance cost {city} / how much is an ambulance in {city}（工具+信息）。
- 重复度：Adamant vs Ascutney 去掉城市名后 difflib 相似度 **1.000**；SF vs Nashville 0.619（核实页有差异）。估算页约 3 万中占比未取得（需全量爬），但抽样的 3 个小城均为估算。
- 内链：上级=州页（VT/AA 的上级 404/不存在）；同级「More cities」小城市页无同级（Ascutney 只有 12 个内链）；下级无；资源入口 5 篇固定。
- 数据准确度问题：① SF「$2,555–$2,555」区间写成同值；② NYC 页引用 Livingston Manor 志愿救护队费率代表纽约市（该地在 NY 州 Sullivan 县，属通用地理常识，建议人工复核）；③ `/ny/new-york` 与 `/ny/new-york-city` 两页数字不同、互相竞争同一意图；④ 小州 Meta 用「VT」「AA」代码而非州名。
- E-E-A-T：核实页有来源+生效日+「Report Inaccurate Data」，是全站最强信任信号；估算页明说「modeled estimate」。
- 可复制：FAQPage（问答里有城市名+数字）、TNT/Medicare/每英里三段式、来源+生效日+更新日、纠错/众包按钮。
- 不要复制：数据缺失的城市也生成可索引页；H1 空格；同城两 URL。

### 5. /resources（目录页）
- 200；**默认 title/meta、无 canonical**；H1 Resources；H3 18 个文章卡；944 词；21 内链；出站 cms.gov；Schema 仅 Organization/WebSite（无 CollectionPage/ItemList）。
- 缺口：目录页只链 18 篇，sitemap 有 40 篇 → 约 22 篇只能靠 sitemap 或文内链发现（按页面观察，未全量核对）。

### 6. resources 文章（共用：Title 后缀「| AmbulanceCost Nationwide Data」；H2 只有固定的「Check ambulance costs in your city / End Surprise…」，正文小标题全是 H3；Schema = Article + BreadcrumbList，**Article 无 author、无 datePublished、dateModified 为「March 12, 2026」字符串**；每篇 18 个内链（同一组）；文末「This article was last updated on March 12, 2026」）

| 页 | Title 长度 | 词数 | 出站 | 主题/意图 | 关键发现 |
|---|---|---|---|---|---|
| [where-we-get-data](https://www.ambulancecost.com/resources/where-we-get-data)（方法论） | 57 | 1,314 | **0** | 方法论 | 讲 CMS 基准、地区系数、Medicare 理赔数据、markup 模型、众包；**方法论页不链 CMS 数据源**；schema dateModified「June 14…」 |
| [state-by-state-ambulance-protections](https://www.ambulancecost.com/resources/state-by-state-ambulance-protections) | **114** | 522 | **0** | 州法目录 | 标题称「directory」，正文只点名 CA/CO/NY/OH/MD 5 州，说「roughly 14 states」综合保护；**无州列表、无法条链接**；与 /no-surprises 和 NSA 文「22 states」口径并存未解释 |
| [how-to-dispute-ambulance-bill](https://www.ambulancecost.com/resources/how-to-dispute-ambulance-bill) | 75 | 627 | 0 | 求助/操作 | 4 步（要明细→走保险→查州法→议价）；无模板信、无电话/表单链接 |
| [hcpcs-code-a0429-bls-emergency](https://www.ambulancecost.com/resources/hcpcs-code-a0429-bls-emergency) | 102 | 525 | 0 | 术语/代码 | 只覆盖 A0429 vs A0428；无 CMS 代码表链接 |
| [highest-ambulance-cost-states](https://www.ambulancecost.com/resources/highest-ambulance-cost-states) | 105 | 393 | 0 | 排行 | 无 H3 小标题（仅固定块）；与州页「#1 of 51」排名未互链核对 |
| [does-insurance-cover-ambulance](https://www.ambulancecost.com/resources/does-insurance-cover-ambulance) | 98 | 725 | masaaccess.com（无 nofollow，带 #:~:text 片段） | 保险覆盖 | 唯一出站是空中救护会员公司 MASA 的文章，不是 CMS/Medicare.gov |
| [cost-trends-2024-2026](https://www.ambulancecost.com/resources/cost-trends-2024-2026) | 101 | 464 | 0 | 趋势 | Meta 称「rose by approximately 18% nationwide」「25% increase…」，**正文无出处** |
| [no-surprises-act-ambulances](https://www.ambulancecost.com/resources/no-surprises-act-ambulances) | 80 | 532 | 0 | 政策 | 「22 states have passed…」无出处；与 /no-surprises 主题重叠 |

- 共性缺口：YMYL 文章零引用、无作者、统一同一更新日（2026-03-12，像批量生成）；Title 普遍 >60 字符（4 篇 >100），SERP 会截断；H2 层级缺失。
- 可复制：选题覆盖面（HCPCS 代码、TNT、loaded mile、paramedic intercept、VA、NEMT、债务催收等 40 个长尾）——这就是它的 Topic Map，可直接作为我们的选题底表。
- 不要复制：无出处统计数字。

### 7. /no-surprises（政策页）
- 200；**默认 title/meta、无 canonical**（核心政策词页标题竟是站名）；H1 The No Surprises Act；338 词（全站最薄之一）；出站 cms.gov；有 CMS 帮助热线电话（公开政府号码）；Schema 仅 Organization/WebSite。
- 内容：Air 受联邦保护 / Ground 拼图；3 步行使权利（含「72-Hour Rule」表述，需对照 CMS 原文核实）；「22 states」。
- 与 resources/no-surprises-act-ambulances、why-ground-ambulances-excluded-nsa 三页主题重叠（蚕食）。
- 缺口：政策页应有法条/CMS 原文链接、州清单、更新日期、FAQ schema。

---

## 第三部分：SERP 其他对手（简版同模板）

| 字段 | World Population Review 州页 | GoodRx 文章 | CareCredit 文章 |
|---|---|---|---|
| URL | https://worldpopulationreview.com/state-rankings/ambulance-cost-by-state | https://www.goodrx.com/insurance/health-insurance/how-much-does-an-ambulance-cost | https://www.carecredit.com/well-u/health-wellness/ambulance-ride-cost/ |
| 状态 | 200 | **403（PerimeterX「Access to this page has been denied」/px-captcha）→ 正文未取得**，不猜 | 200（上轮记录为 Akamai 拦截，本次 curl 取到） |
| Title | Ambulance Cost by State 2026（28） | 未取得 | How Much Does an Ambulance Ride Cost?（37） |
| Meta | **站点通用描述**「Discover population, economy, health…」 | 未取得 | ALS $1,277、BLS $940 |
| H1/H2 | H1 同 title；H2 仅「Other Categories」 | 未取得 | 14 个 H2（BLS vs ALS、平均费用、影响因素、保险、为何贵、怎么付、议价、替代方案、CareCredit 卡…） |
| 模块/密度 | 一张 51 行表（52 tr），715 词 | 未取得 | 2,555 词，州表 55 tr，作者简介 |
| Schema | Article（author=Organization，datePublished 2026-10-22，description null） | 未取得 | Article（datePublished 2023-03-01，mainEntity MedicalWebPage）、BreadcrumbList（@id 拼接错：`carecredit.comwell-u`） |
| 出站 | 只有 carecredit.com（唯一 Sources） | 未取得；上轮记录称其参考文献点名 AmbulanceCost（见 ambulance-competitor-analysis.md 第 25 行） | FAIR Health、JAMA、ACEP、medicareinteractive、goldcross、县政府等 |
| E-E-A-T | 无作者 | 未取得 | 具名作者（健康写作者），无医学审核 |
| 数据准确度 | 数据源于 CareCredit | 未取得 | **Meta 写 BLS $940/ALS $1,277，schema description 写 BLS $1,481/ALS $1,613，自相矛盾** |
| CTA/变现 | 站内广告/分类导航（未细查） | 未取得 | CareCredit 信用卡 |
| 缺口 | 无城市粒度、无方法论 | — | 无城市/ZIP 粒度、2023 发布、变现偏向分期 |

---

## 第四部分：最大 SEO 缺口 → 我们的打法 → 失败判断标准

| # | 逐页发现的缺口（证据） | 我们的打法 | 失败判断标准 |
|---|---|---|---|
| 1 | 小城市估算页近 100% 重复（Adamant=Ascutney，相似度 1.000）；约 3 万页靠模板 | **只为有独有数据的地点建可索引页**（官方费率表/CMS 地区系数不同/县级数据），其余合并到县或州页，或 noindex；每页至少 3 个独有数据点 | 上线 8 周后 GSC「已抓取-未编入索引」占城市页 >40%，或抽 20 页互相似度 >0.9 |
| 2 | 数据错位：NYC 页用 Livingston Manor 志愿队费率；`/ny/new-york` 与 `/new-york-city` 两页不同数字；SF 区间同值 | 大城市（前 50）逐个人工核实到**市/县官方费率表**，一城一 URL，写明来源条例号+生效日+核实日 | 前 50 城中任一城无官方来源却标「verified」，或同城出现 2 个可索引 URL |
| 3 | 州层级缺口：VT 州页 404 而 287 城市页指向它；EM/AA 当州；排名「of 51」失真；州页无 FAQ schema | 50 州+DC 完整州页，州页 = 州法条文链接 + 州保险局投诉入口 + 州内县市费率表 + FAQPage；属地（PR/GU 等）单独处理 | 任一州页 404 / 不在 sitemap；或州页 Rich Results Test 不通过 |
| 4 | YMYL 信任弱：无作者/审核/联系方式；资源文 0 出站引用；Article 日期非 ISO、同一天批量 | 具名作者+审核者（医疗账单/保险从业背景），每篇 ≥3 个 .gov/研究出处，Article schema 带 author、datePublished、dateModified（ISO），About 写数据流程 | 抽查任一 YMYL 文章出处 <3 或无作者；schema 校验有日期报错 |
| 5 | 政策词承接弱：/no-surprises 默认 title、无 canonical、338 词；州法 directory 实际只点名 5 州；「14 州 vs 22 州」口径不一 | 做真正的**「州地面救护车 surprise billing 法律表」**（每州：是否有法、法条号、生效日、适用计划类型、ERISA 例外、来源链接），配 Commonwealth Fund/州法原文 | 表中任一州无原文链接；或口径与引用来源不一致 |
| 6 | 页面级技术 SEO 小错：About/Resources/No Surprises 共用默认 title+meta 且无 canonical；州/城/文 og:image 缺失；资源文 title 100+ 字符；H2 缺失、H1 空格；sitemap 单文件 lastmod 全同 | 每页独有 title(≤60)/meta、全站 canonical、og:image、正确 H2 层级；sitemap 按类型分片，lastmod=真实数据更新时间 | Screaming Frog/SiteOne 爬全站：重复 title >1%、缺 canonical >0、title>60 字符 >10% |
| 7 | 「事后求助」意图浅：dispute 文 627 词、无模板信/无工具；全站无可下载物 | 争议账单工具：输入账单行项目（HCPCS 代码、里程）→ 对比 Medicare 基准 → 生成申诉信/明细请求信 | 工具页 3 个月内无任何外部引用/自然链接（用免费外链工具查），或用户完成率无法统计 |
| 8 | 无变现、无外链布局（未见广告/联盟）；SERP 大站（GoodRx，依上轮记录）引用其数据 | 以「可引用数据集」为外链抓手：开放 CSV/许可、给媒体与 GoodRx 类站点可引用的州/城数据；按收藏里的外链反查法（@aiRobertDaily #48）找它的引用来源 | 6 个月内无任何 DR 未知但真实的媒体/机构引用我们数据（以可见链接为准） |

## 没取到的东西
- DR、流量、关键词排名、搜索量、外链数量：未取得（需付费工具，按要求不猜）。
- CWV/移动端实测：未取得（只有 curl 体积与响应时间；首页 HTML 245,675 字节）。
- GoodRx 正文：403 PerimeterX 拦截。
- 全量 3 万城市页中「核实 vs 估算」比例：未全量爬取，只抽样 7 个城市页。
- resources 目录页是否链到全部 40 篇：只核对了目录页 18 个卡片 vs sitemap 40 篇。
