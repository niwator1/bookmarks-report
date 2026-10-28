# 救护车费用站竞品与生态位分析

> 调研日期：2026-10-28（Asia/Singapore, UTC+8）  
> 范围：只读 WebSearch / WebFetch / curl 公开页；不登录、不注册、不发帖、不联系、不花钱  
> 用途：供禽姐决策「ambulance cost」建站主选的差异化方向  
> 不猜 DR / 流量数字；取不到写「未取得」

---

## 结论先行

1. **生态位一句话**：美国「救护车费用」搜索意图被切成六块——事前估价、事后账单震惊、州/城比价、Medicare/保险规则、空中救护、律师/债务协商；**唯一真正做「全国地面救护车价格数据库」的专门站是 ambulancecost.com**，其余多为保险公司/金融科普单页、律师线索博客、本地 EMS 费率 PDF、或空中救护会员销售。
2. **最强专门竞品**：`ambulancecost.com`（精确匹配域名 + 约 3 万城/州页 + ZIP 查询 + CMS 方法论 + resources 科普）。**弱点不是「没有来源」**（它已有详细数据页与更新日期），而是：**核实市政费率覆盖不均、城市页存在明显错绑供应商、TNT（到场不送医）大量缺数据、州保护法页是叙述而非可行动的法条/投诉目录、CMS 官方事后指南仍滞后**。
3. **我们最该抓的 3 个机会**（均可只用公开数据验证）：  
   - **市政/郡 EMS 核实费率库**（带来源 PDF、生效日、NPI 对照）  
   - **州级 surprise-billing 可行动矩阵**（法条链接、适用范围、ERISA 自保缺口、投诉入口）  
   - **事后账单行动流**（按州 checklist：明细单 → 保险 → 州法 → 现金锚点 → charity care）  
4. **不建议做**：纯州平均表（CareCredit/WPR 已占）、空中救护会员对打 MASA/AirMedCare、律师线索站（资质与 YMYL 风险）。
5. **相对早期内部笔记的更正**：此前「无数据来源列表、无更新日期」的判断**已过时**——该站现有 `/resources/where-we-get-data`（文内写 last updated 2026-06-14）及城市页 `Last updated` 字段。差异化必须建立在**更深、更可核验、更可行动**，而不是「补一篇来源说明」。

---

## 浏览器核验补记（2026-10-28）

- **GoodRx 州表数字与 AmbulanceCost 重合，且参考文献点名 AmbulanceCost**（可见两条：Florida 州费用页；里程文）。大站在转载/引用专门站数据，不是另建独立费率库。来源页：[GoodRx 文章](https://www.goodrx.com/insurance/health-insurance/how-much-does-an-ambulance-cost)。
- **旧金山城页是「核实做得好」的样板**：市政费率 + TNT $568 + 2026 Medicare 基准 + 生效日 2025-09-01 + Resource last updated 2026-06-11。差异化应做「更多像旧金山这样的核实页」，不是否认对方完全无核实。页：[SF](https://www.ambulancecost.com/ambulance-cost/ca/san-francisco)。
- **州页自相矛盾仍在**：NY 写 “1 verified” 却下列 6 家；TN 先写尚无核实又列出多家（多为 CMS PUF）。首页地图仍有脏码 `EM`。
- **WPR** 只有一张 51 行 BLS/ALS 表，Sources 只链 CareCredit；加州数字与 AmbulanceCost/GoodRx 那套不同。
- **打不开正文**：CareCredit（Akamai Access Denied）、usasymbol 州排名（Cloudflare）、Google/部分 DuckDuckGo（流量验证）。
- **误判排除**：ercost.com 是急诊室现金价（46 都会区），不是救护车价。
- 原始页记与截图：本机 `/workspace/outputs/competitor-pages-raw.md`、`competitor-screenshots/`（未推仓库）。

---


## 1. 相关站分类清单

### A. 专门数据 / 比价站

| 站 | URL | 备注 |
| --- | --- | --- |
| AmbulanceCost | https://www.ambulancecost.com/ | 全国地面救护车费率库；自称覆盖 1/3 美国城市；sitemap 约 3 万 URL |
| MedicAnalyze（救护车程序页） | https://www.medicanalyze.com/procedure/ambulance-transport | 按城市展示 **Medicaid 赔付**均值，非患者账单；约 6,157 城 |
| World Population Review | https://worldpopulationreview.com/state-rankings/ambulance-cost-by-state | 州级 BLS/ALS 表；来源指向 CareCredit |

### B. 保险公司 / 金融科普（大站单页，非数据库）

| 站 | URL | 备注 |
| --- | --- | --- |
| CareCredit（Synchrony） | https://www.carecredit.com/well-u/health-wellness/ambulance-ride-cost/ | 50 州 BLS/ALS 平均表 + 支付/协商科普；文末推 CareCredit 卡 |
| GoodRx | https://www.goodrx.com/insurance/health-insurance/how-much-does-an-ambulance-cost | SERP 常见；本轮 WebFetch/curl 被 PerimeterX **403 拦截 → 正文未取得**（仅有搜索摘要） |
| UnitedHealthcare | https://www.uhc.com/news-articles/benefits-and-coverage/ambulance-cost-coverage | SERP 常见；本轮 **403 → 正文未取得**（仅有搜索摘要） |
| MASA | https://masaaccess.com/learning-center/understanding-ambulance-costs | 科普费用构成，导向 **空中/地面救护会员产品** |

### C. 律师 / 人身伤害线索站

| 站 | URL | 备注 |
| --- | --- | --- |
| Wagner Reese, LLP | https://www.wagnerreese.com/blog/ambulance-cost-no-insurance/ | 印第安纳无保险费用区间 + 转伤残索赔咨询 |

### D. 账单援助 / 官方行动指南

| 站 | URL | 备注 |
| --- | --- | --- |
| CMS 地面救护账单行动计划 | https://www.cms.gov/initiatives/your-patient-rights/medical-bill-rights/get-help/find-action-plan/ground-ambulance-bill | 事后怎么办；州保护法列表标「截至 2021-11-15 共 10 州」——**已明显过时** |
| Medicare.gov 覆盖说明 | https://www.medicare.gov/coverage/ambulance-services | Part B：免赔后付 Medicare 批准额的 20% |
| Dollar For | https://dollarfor.org/ | 医院 charity care 申请协助；用户证言提到 EMS 账单也可被处理，但主产品是医院账单 |
| Undue Medical Debt（原 RIP Medical Debt） | https://unduemedicaldebt.org/ | 批量购买并注销医疗债；用户无法主动申请；是否含救护车取决于合作方 |
| 本地 EMS hardship（样例） | 如 https://www.rescueinc.org/assistance 、EmergyCare hardship 页 | 单机构慈善护理，非全国站 |

### E. 地方政府 EMS 费率页 / 条例（数据源，非竞品站）

公开可找到大量市政条例 PDF，例如：

- Frankfort, KY EMS 账单费率条例：https://frankfort.ky.gov/DocumentCenter/View/4819/Ordinance-No-22-2025-Series---EMS-BIlling-Rates-Update  
- Chambersburg, PA 2026 Master Fee Schedule：https://chambersburgpa.gov/pdf/Resolution%20-%20Master%20Fee%20Scheduale%2003-23-2026.pdf  
- Manatee / Corpus Christi 等郡市亦有更新费率的决议（搜索结果可定位）

这类页是**可抓取的一手核实源**，不是流量竞品。

### F. 本地救护车运营商（区域获客页）

| 站 | URL | 备注 |
| --- | --- | --- |
| Elite Ambulance（IL/IN） | https://www.eliteamb.com/how-much-does-an-ambulance-ride-cost/ | 2021 博客式全国平均 + 推销自家 NEMT |
| West Coast Ambulance（CA） | https://wcambulance.com/pricing-guide | LA/OC 私人付费区间表（轮椅/担架/BLS），非 911 比价库 |

### G. 空中救护 / 计算器 / 会员网络

| 站 | URL | 备注 |
| --- | --- | --- |
| WellCare 空中费用计算器 | https://wellcareambulance.com/air-ambulance-cost-calculator/ | 空中估价工具 |
| Flying Assist | https://flyingassist.com/air-ambulance-finder/ | 空中报价撮合 |
| AirMedCare Network | https://www.airmedcarenetwork.com/air-ambulance-service | 会员网络 |
| Angel MedFlight 等 | 运营商 FAQ / 报价页 | 个案报价，非地面数据库 |

### H. 研究 / 政策（塑造叙事，占权威 SERP）

| 站 | URL | 备注 |
| --- | --- | --- |
| KFF | https://www.kff.org/private-insurance/ground-ambulance-rides-and-potential-for-surprise-billing/ | 约一半紧急地面救护可能产生网络外收费（2021 分析） |
| Commonwealth Fund | https://www.commonwealthfund.org/blog/2026/consumers-still-face-surprise-bills-ground-ambulances-states-are-trying-protect-them | **截至文中：22 州有某种地面救护 surprise-billing 保护**；强调 ERISA 自保计划州管不了 |
| FAIR Health | https://www.fairhealth.org/article/fair-health-releases-study-on-ground-ambulance-services | 私营赔付研究；常被 CareCredit/GoodRx 引用 |
| CMS Ambulance Fee Schedule | https://www.cms.gov/medicare/payment/fee-schedules/ambulance | 公开可下载的 Medicare 费率表（建站核心数据源） |

---

## 2. 重要竞品深挖

### 2.1 ambulancecost.com（专门站，优先对手）

**生态位一句话**：服务「想按 ZIP/城市查大概花多少、以及本州有没有 surprise-billing 保护」的美国患者与家属；靠精确域名 + 海量程序化州/城页 + CMS 基准与模型估价赢流量。

**做得好的点**

1. **产品完整**：首页 ZIP/城市搜索；州页排名与保护状态；城页同时给「报告收费区间 + Medicare 基准 + 每英里 + 州保护徽章」。样例：  
   - 州：https://www.ambulancecost.com/ambulance-cost/ny  
   - 城：https://www.ambulancecost.com/ambulance-cost/ny/new-york-city  
   - CA 州页显示「39 verified provider rates」并列出市政来源链接：https://www.ambulancecost.com/ambulance-cost/ca  
2. **方法论公开且分层**：核实市政表 → CMS Provider billed charges PUF → 区域 markup 模型；见 https://www.ambulancecost.com/resources/where-we-get-data （文内写 last updated 2026-06-14）。  
3. **内容护城河**：`/resources` 下约 40 篇（sitemap 计），覆盖 NSA 缺口、纠纷步骤、BLS/ALS、TNT、里程码、州保护法概述等；另有 `/about`、`/no-surprises`。robots.txt：`Allow: /`，Sitemap 指向 `/sitemap.xml`。

**明显缺口**

1. **数据质量/错绑**：纽约市页把 Primary 911 provider 写成「Volunteer Ambulance Corps Of Livingston Manor Inc」（卡茨基尔山区志愿队），与 NYC 现实不符——程序化绑定不可靠。来源：https://www.ambulancecost.com/ambulance-cost/ny/new-york-city  
2. **核实覆盖不均**：NY 州页自称仅「1 verified provider rate」；大量条目实为 CMS billed charges。TNT 在 NYC 显示「Data Unavailable」。  
3. **州保护法不够可行动**：https://www.ambulancecost.com/resources/state-by-state-ambulance-protections 是叙述分级（comprehensive / partial / none），**不是**带法条、生效日、适用险种、投诉链接的州×州矩阵；与 Commonwealth Fund「22 州有保护、且 ERISA 自保常不在州管辖」的精细度有差距。  
4. **Sitemap 异常**：存在伪州码 `/ambulance-cost/em`（页面标题「Ambulance Cost in EM」），说明程序化生成有脏数据。  
5. **外链/权威页**：resources 多为站内科普；**未见到**系统的「市政费率原文外链目录」独立枢纽页（州页有部分核实链接，但全国索引未取得）。传统「博客」= `/resources`，无独立 blog 子域。DR/流量：**未取得**（本轮不做 Ahrefs 登录）。

**结构快照（本轮实测）**

| 项 | 观测 |
| --- | --- |
| sitemap URL 数 | 约 **30,303**（curl 解析） |
| 州级路径 | **51** 个（含异常 `em`；缺 `vt`？列表未见 vt——需标注：标准 50+DC 中 sitemap 列出含 `em`，**未在列表中看到 `vt`**） |
| 城级路径 | 约 **30,208**（如 NY 城页约 1,639；CA 约 1,255；TX 约 1,491） |
| resources | 约 **40–41** |
| robots | `User-Agent: *` / `Allow: /` |
| FAQ | 无单独 `/faq`；FAQ 嵌在城页底部 + resources 文章 |
| 纠纷指南 | https://www.ambulancecost.com/resources/how-to-dispute-ambulance-bill （有步骤，但未按州分支） |

> 注：WebFetch 对 sitemap.xml 返回 500，curl 可正常下载——站点地图对部分抓取端不稳定。

---

### 2.2 World Population Review

**生态位**：服务「要一张州排名表」的轻量查询用户；靠大站域名与表格模板赢「ambulance cost by state」类词。

**好**：完整 50+DC 表、可读排名、地图视觉。  
**缺口**：数据源写明来自 CareCredit 二次转载（非一手）；无城市/ZIP；无保险规则；无账单行动。  
来源：https://worldpopulationreview.com/state-rankings/ambulance-cost-by-state

---

### 2.3 CareCredit

**生态位**：服务「先看全国/州平均、再找融资方式」的用户；靠金融品牌权威 + 州表 + 协商/会员制科普，最终导向 CareCredit 卡。

**好**：州表完整；引用 FAIR Health / Synchrony ASQ360 研究；覆盖保险、里程、协商折扣、会员制。  
**缺口**：无 ZIP/城市工具；无市政核实库；无按州保护法矩阵；商业转化目标与「中立数据站」不同。  
来源：https://www.carecredit.com/well-u/health-wellness/ambulance-ride-cost/

---

### 2.4 GoodRx / UHC

**生态位**：大站信任背书下的「how much does an ambulance ride cost」科普入口。

**好（据搜索摘要）**：解释 NSA 不含地面救护、有/无保险大致区间、协商建议。  
**缺口**：单页；无数据库。  
**本轮正文**：**未取得**（403 / bot 墙）。摘要来源见 WebSearch 结果页。

---

### 2.5 MASA

**生态位**：恐吓高账单 → 销售空中/地面救护会员保障。

**好**：讲清 BLS/ALS、里程、耗材、空中运营成本；有内部均值（地面约 $2,086、空中约 $72,469，文内标注内部数据）。  
**缺口**：不是公开费率库；利益冲突明显（卖会员）。  
来源：https://masaaccess.com/learning-center/understanding-ambulance-costs

---

### 2.6 MedicAnalyze

**生态位**：服务「看 Medicaid 实际赔付」的分析/支付方视角用户。

**好**：城市级、按 HCPCS 拆分、声称海量 claims。  
**缺口**：明确声明是 Medicaid paid，**远低于**患者账单；易误导若被当成「救护车费用」。  
来源：https://www.medicanalyze.com/procedure/ambulance-transport

---

### 2.7 Wagner Reese / Elite / West Coast Ambulance

| 站 | 生态位 | 好 | 缺口 |
| --- | --- | --- | --- |
| Wagner Reese | 印第安纳车祸伤者 → 律师线索 | 本地区间、纠纷 FAQ、立法提及 | 非全国；CTA 全是咨询律师 |
| Elite Amb | IL/IN 运营商获客 | 解释为何贵、保险网络外 | 数据旧（2021）、无结构化库 |
| WC Ambulance | CA NEMT 预订转化 | 私人付费透明区间 | 非 911 全国比价 |

---

### 2.8 官方与研究（「吃权威意图」而非抢城页）

- **Medicare.gov**：覆盖规则权威源，不做比价。  
- **CMS 行动计划**：事后流程入口，但州列表滞后。  
- **KFF / Commonwealth Fund**：政策叙事与州法进展；不提供 ZIP 估价工具。

---

## 3. 生态位地图（查询意图 × 谁在吃）

| 意图块 | 用户问题形态 | 谁在吃 | 谁没吃透 |
| --- | --- | --- | --- |
| ① 事前估价（要不要叫 / 大概多少钱） | how much does an ambulance ride cost；ZIP 估价 | CareCredit/GoodRx/UHC 全国平均数；**ambulancecost ZIP/城页** | 真正「本地核实市政费率 + 预期自付」仍稀缺；TNT 事前几乎空白 |
| ② 事后账单震惊 | dispute ambulance bill；can't afford | CMS 行动计划；ambulancecost 纠纷文；律师站；Dollar For（偏医院） | **按州分支的可执行 checklist**弱；CMS 州名单过时；charity care 与 EMS 账单衔接分散 |
| ③ 按州/城市比价 | ambulance cost by state；city rates | WPR 州表；ambulancecost 州/城海量页；CareCredit 州表 | **核实市政源密度**除 CA 等少数州外偏低；脏数据/错绑损害信任 |
| ④ Medicare/保险覆盖规则 | Medicare ambulance；medical necessity；NSA | Medicare.gov；保险公司科普；ambulancecost resources | 「Medicare 批准额 vs 贴纸价 vs 你可能付多少」三联对照工具少；ERISA 自保例外解释弱 |
| ⑤ 空中救护 | air ambulance cost | NSA 已覆盖空中；MASA/AirMedCare 卖会员；独立计算器 | 地面站不必硬刚；空中是另一产品线 |
| ⑥ 律师/债务协商 | personal injury ambulance；medical debt | 律师博客；Undue Medical Debt；本地 hardship | 全国「非律师」的债务协商工具+模板几乎空白；法律风险高 |

---

## 4. 机会点（3～5 个可验证差异化）

> 原则：必须是竞品**现在缺或做得浅**的，且我们用 **CMS 公开文件 + 市政/郡公开费率条例 + 州法公开文本** 能做。

### 机会 1：市政/郡「核实费率」优先库（带来源 PDF、生效日、NPI）

- **做什么**：先做人口大、公开费率多的州/郡（如 CA 各 EMS agency、大城市 fire/EMS），每条记录：BLS/ALS/里程/TNT、来源 URL、抓取日、生效日、是否与 CMS billed charge 一致。城页默认展示核实价，模型价降级显示。  
- **为什么竞品没做透**：ambulancecost 自称 CA 有 39 条核实、NY 仅 1 条；NYC 仍出现明显错绑；大量城页靠模型/Medicare billed。市政 PDF 分散、格式不一，工程脏活重。  
- **需要什么数据**：CMS Ambulance Fee Schedule + ZIP locality 文件；CMS Physician & Other Practitioners by Provider and Service PUF；各地 ordinance/fee schedule PDF。  
- **做成了 / 失败条件**：  
  - 做成：目标州抽检 50 城，≥70% 有可点击一手来源且供应商名称与本地 911/特许运营商一致。  
  - 失败：到约定日（可沿用内部卡 2026-12-15）用公开源做带来源页 <30 州/城核心样本，或错绑率抽检 >10%。

### 机会 2：州级 surprise-billing「可行动矩阵」

- **做什么**：50+DC 表：有无保护法、紧急/非紧急/TNT/院间转运是否覆盖、是否允许 ERISA opt-in、患者自付上限逻辑一句话、DOI/AG/消费者援助投诉链接、法条或官方解释页链接、最后核验日。对标 Commonwealth Fund 的 22 州进展，但产品化为查询工具。  
- **为什么竞品没做透**：ambulancecost 只有叙述文 + 州页徽章；CMS 官方仍列 10 州（2021）；政策站不做消费者工具。  
- **需要什么数据**：各州立法/DOI 页、Commonwealth Fund/KFF 综述作交叉核验（引用政策文，以法条为准）。  
- **做成了 / 失败条件**：  
  - 做成：用户按州 2 次点击到达「该不该拒付余额账单 + 去哪投诉」；每州至少 1 个官方外链。  
  - 失败：矩阵与两家权威综述冲突且 30 日内无法核验修正；或半数以上州只有「Protected」布尔而无投诉路径。

### 机会 3：事后账单「按州行动流」+ Medicare 现金锚点

- **做什么**：交互/静态 checklist：① 要明细（HCPCS）② 确认已交保险 ③ 查本州矩阵 ④ 用本 ZIP 的 Medicare AFS 作谈判锚点 ⑤ 查该供应商 charity care / hardship ⑥ 链到 CMS Help Desk。纠纷文要**按州分支**，不是全国一篇。  
- **为什么竞品没做透**：ambulancecost 有全国四步文（https://www.ambulancecost.com/resources/how-to-dispute-ambulance-bill），未按州；CMS 指南州名单旧；Dollar For 主攻医院。  
- **需要什么数据**：同上矩阵 + AFS + 可选供应商 hardship 政策链接（能链则链）。  
- **做成了 / 失败条件**：  
  - 做成：「dispute ambulance bill」类意图页能给出州特异步骤且每步有出处。  
  - 失败：只能复制全国通用建议、无法区分有保护法/无保护法州；或被认定为提供法律服务（需强免责声明，不做个案代理）。

### 机会 4：TNT / Treat-No-Transport 专项库

- **做什么**：单独意图页 + 有公开费率的城市收录 A0998/assessment fee；无数据明确「未公布」而非编造。  
- **为什么竞品没做透**：联邦表常不含；ambulancecost 依赖众包，NYC 等显示 Unavailable。  
- **需要什么数据**：市政 fee schedule 中的 TNT/assessment/first responder 条目。  
- **做成了 / 失败条件**：  
  - 做成：在公布该类费的样本城市中覆盖率可核验，并解释「保险常拒付」机制。  
  - 失败：3 个月内找不到足够公开 TNT 源形成差异（则降级为解释文，不做库）。

### 机会 5（可选增强）：ZIP 级「三联价」计算器

- **做什么**：同一 ZIP 并排：Medicare 批准基准｜供应商贴纸（核实或 PUF billed）｜「有保险时可能仍欠」说明（指向州矩阵与 medical necessity）。  
- **为什么竞品相关但可差异化**：ambulancecost 已有双列，但错绑与核实不足；大站只有全国平均。  
- **需要什么数据**：CMS AFS + PUF + 核实表。  
- **做成了 / 失败条件**：抽 100 ZIP，Medicare 列与官方 AFS 文件一致率 ≥95%；贴纸列来源标签正确（核实/PUF/模型三分清）。失败：模型价被用户当成报价导致投诉且免责不足。

---

## 5. 不建议做的事

1. **再做一个「州平均 BLS/ALS 表」当主产品**  
   CareCredit 一手研究表 + WPR 转载已占「by state」表格式意图；无 ZIP/来源深度则无法差异化，还会与大站权威撞车。

2. **空中救护会员 / 对打 MASA、AirMedCare**  
   空中已被联邦 NSA 覆盖；商业模式是会员销售与运营网络，需要理赔能力与合规，不是公开数据内容站能赢的。

3. **律师线索 / 伤残索赔站形态**  
   Wagner Reese 等已吃「事故后谁付钱」；无律师牌照做线索有合规与 YMYL 风险，且与「中立费用数据」品牌冲突。

（附加警示）**堆 3 万城页但不先解决错绑与来源**：ambulancecost 已证明规模可以很大，但 NYC 类错误说明「只扩页」会被信任与质量信号反噬。

---

## 6. 决策含义（给禽姐）

- **可以建站**，但定位应是：**「可核验的地面救护车价格 + 州保护法行动工具」**，不是第二个只有模型价的 ambulancecost 克隆。  
- **先做深、后做广**：优先核实源州（CA 等公开费率多）+ 全州保护法矩阵 + 事后行动流；城页规模跟随核实进度，而不是先生成 3 万再补来源。  
- **文案必须区分**：Medicare 基准 ≠ 患者账单 ≠ Medicaid 赔付（MedicAnalyze）≠ 空中费用。  
- **YMYL**：每页紧急免责（Call 911）、非法律/医疗建议；州法页以官方链接为准并显示核验日。

---

## 7. 本轮未取得 / 限制

| 项 | 状态 |
| --- | --- |
| GoodRx 正文 | 403 / PerimeterX，未取得 |
| UHC 正文 | CloudFront 403，未取得 |
| ambulancecost DR / 流量 / 反链 | 未取得（不猜） |
| ambulancecost 全站核实费率占比精确统计 | 未取得（仅抽样州页文案：CA=39，NY=1） |
| sitemap 中是否缺 `vt` 等州 | 列表未见 `vt`、见异常 `em`；未逐一 HTTP 核验全部 51 码 |
| 用户站浏览器登录态下的 Ahrefs 复测 | 本任务未做 |
| 联系任何运营商或发邮件 | 按任务禁止，未做 |

---

## 8. 关键来源（抽样）

- https://www.ambulancecost.com/  
- https://www.ambulancecost.com/about  
- https://www.ambulancecost.com/resources  
- https://www.ambulancecost.com/resources/where-we-get-data  
- https://www.ambulancecost.com/resources/how-to-dispute-ambulance-bill  
- https://www.ambulancecost.com/resources/state-by-state-ambulance-protections  
- https://www.ambulancecost.com/no-surprises  
- https://www.ambulancecost.com/robots.txt  
- https://www.ambulancecost.com/sitemap.xml （curl 取得）  
- https://www.ambulancecost.com/ambulance-cost/ny  
- https://www.ambulancecost.com/ambulance-cost/ny/new-york-city  
- https://www.ambulancecost.com/ambulance-cost/ca  
- https://worldpopulationreview.com/state-rankings/ambulance-cost-by-state  
- https://www.carecredit.com/well-u/health-wellness/ambulance-ride-cost/  
- https://masaaccess.com/learning-center/understanding-ambulance-costs  
- https://www.medicanalyze.com/procedure/ambulance-transport  
- https://www.wagnerreese.com/blog/ambulance-cost-no-insurance/  
- https://www.eliteamb.com/how-much-does-an-ambulance-ride-cost/  
- https://wcambulance.com/pricing-guide  
- https://www.medicare.gov/coverage/ambulance-services  
- https://www.cms.gov/initiatives/your-patient-rights/medical-bill-rights/get-help/find-action-plan/ground-ambulance-bill  
- https://www.cms.gov/medicare/payment/fee-schedules/ambulance  
- https://www.commonwealthfund.org/blog/2026/consumers-still-face-surprise-bills-ground-ambulances-states-are-trying-protect-them  
- https://www.kff.org/private-insurance/ground-ambulance-rides-and-potential-for-surprise-billing/  
- https://dollarfor.org/  

---

*文档路径：`/workspace/outputs/ambulance-competitor-analysis.md`*
