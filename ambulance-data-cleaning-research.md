# 救护车费用数据站：费率原件清洗调研 & 是否新开 bot
日期：2026-10-29（新加坡时间）。只用公开资料与项目已有文件；数字均来自原件，未取得的写「未取得」。

## 0. 先看样本（本次搜索命中的 5 个官方原件，用来说明格式有多杂）
| 形态 | 例子 | 难点 |
|---|---|---|
| 主管部门规章 PDF（文字层） | 芝加哥财政局 Ambulance Rules 2026：BLS $3,234、ALS $3,384、$19/英里、氧气 $28，2026-01-03 生效，依据市政法典 4-68-130 https://www.chicago.gov/content/dam/city/depts/dol/rulesandregs/Ambulance_Rules_2026.pdf | 费率藏在规章正文里，没有表格 |
| “最高限价”PDF（特许经营） | 拉斯维加斯 2026 Maximum Allowable Rates（依据 LVMC 6.08.190，2026-02-01 生效）https://files.lasvegasnevada.gov/finance/Franchise/2026_Maximum_Allowable_Ambulance_Service_Rates-Effective-Feb-1-2026.pdf | 这是“上限”，不是实收价 → 要单独设 rate_kind 字段 |
| 消防局费率表（居民/非居民） | Noblesville FD 2026（BLS 居民 $661 / 非居民 $761）https://www.noblesville.in.gov/DocumentCenter/View/4900/2026NFDAmbulanceFeeSchedule | 一档服务有两个价 |
| 混在全市杂费表里 | Harmony MN 2026 费用表 https://harmonymn.gov/wp-content/uploads/2026/01/Harmony-2026-Fees-schedule.pdf | 要从无关行里挑出救护车的行（小城市，只用来示范格式） |
| 法典条文（按年分级上限） | DC Code §5-416：2026 年起每次转运不超过 $2,000、每英里不超过 $30 https://code.dccouncil.gov/us/dc/council/code/sections/5-416 | 同一条文里有多个生效日期 → 要存版本历史 |
结论：一份原件里可能同时出现“上限价 / 实收价”、“居民价 / 非居民价”、“多个生效日期”。数据模型必须把这几种情况分开存。

## 1. 原件获取
**常见来源**：①市/县法典（Municode、American Legal、eCode360 等法典库，或自建网站，如 DC）；②年度杂费表 / 收费决议 PDF；③市议会或县委员会的议程附件（Legistar、Granicus 等）；④消防局或 EMS 局页面；⑤财政或特许经营监管页面（如拉斯维加斯）。
**系统化搜索**（沿用 launch-playbook 里的搜索式，并做扩展）：
- `site:{city}.gov ambulance "fee schedule" filetype:pdf`
- `"{City}" "ambulance" (rates OR fees) (ordinance OR resolution) 2026`
- `"{City}" fire department "ambulance billing"`（账单页通常会链接到费率）
- `"{County}" EMS "rate" "board of supervisors"`
- 法典库站内搜 "ambulance"
- 找不到时，按州公开记录法（FOIA/Public Records）申请是正规途径，但这需要对外联系，**本阶段不做**，只记为“可申请”。
**留证据（免费）**：
- 下载原文件，算 `sha256sum` 存进 CHECKSUMS（与 playbook 做法一致）。
- 用 Wayback Machine 的 Save Page Now 存档：https://web.archive.org/save （说明：https://help.archive.org/help/using-the-wayback-machine/ ）。`.gov` 原件可公开存档；注意这一步会向第三方发请求，属于“存档”而不是发帖，可以接受。如果严格按“完全不对外”执行，先只做本地存档 + 哈希。
- 每条记录保存：原件 URL、抓取时间（UTC）、HTTP Last-Modified、哈希、Wayback URL。
- 网页表格：额外存一份 HTML 快照和一张截图。

## 2. 抽取
| 工具 | 适用 | 局限 | 来源 |
|---|---|---|---|
| pdftotext -layout（poppler） | 有文字层的 PDF，最快 | 列容易错位 | https://poppler.freedesktop.org/ |
| pdfplumber | 有文字层的表格，能按坐标切 | 扫描件不行 | https://github.com/jsvine/pdfplumber |
| camelot（lattice/stream） | 有线框的表格 | 扫描件不行；无线框表要调参 | https://camelot-py.readthedocs.io/ |
| ocrmypdf + Tesseract | 扫描件：先加文字层，再接上面的工具 | 数字可能认错（$1,136 → $1,1З6），必须核对 | https://ocrmypdf.readthedocs.io/ , https://github.com/tesseract-ocr/tesseract |
| AI 读 PDF 或截图 | 规章正文、无结构的条文（如芝加哥、DC） | 可能“编”数字 → 只能作为其中一种方式，不能单独定稿 | — |
**交叉核对流程（建议）**：
1. A 路：规则抽取（pdfplumber/camelot；扫描件先过 ocrmypdf）。
2. B 路：AI 独立读原件，输出同样的 JSON schema，并要求附上原文引用（逐字截取的那一句）。
3. 脚本逐字段比对，比金额、单位、服务类型、生效日期。全一致 → `auto_verified`；有不一致 → `needs_review`，由人工看原件。
4. 校验 AI 的引用：引用的原文必须能在 pdftotext 输出里字符串匹配到，匹配不到就当作疑似编造。
**能否做成可重复脚本**：可以。下载 → 哈希 → 判断有无文字层（pdffonts 或 pdftotext 输出为空则判为扫描件）→ A/B 两路抽取 → 比对 → 输出 CSV 和差异报告。真正要人工做的是**找原件**和**看差异**。
**每城市所需时间**：未取得公开基准。建议用前 10 个城市实测计时后再估。

## 3. 数据模型
**rates 表**（一行 = 一个运营方 × 一个服务项 × 一个适用对象 × 一个生效区间）：
`rate_id`、`jurisdiction`（州/县/市 + FIPS）、`operator_name`、`operator_npi`（查 NPPES：https://npiregistry.cms.hhs.gov/api-page ）、`service_code`（BLS_E / BLS_NE / ALS1 / ALS2 / SCT/CCT / MILEAGE / NO_TRANSPORT / OXYGEN / OTHER；可对应 HCPCS A0429/A0428/A0427/A0433/A0434/A0425）、`amount`、`currency`、`unit`（per_transport / per_loaded_mile / per_item）、`rate_kind`（charged / maximum_allowed / resident_discounted）、`applies_to`（resident / non_resident / all）、`effective_from`、`effective_to`、`legal_ref`（条例号或法典条）、`evidence_tier`（official_source / cms_benchmark / model_estimate，三层不混用，只有 official_source 能上城市页）、`source_url`、`source_page`、`source_quote`、`retrieved_at`、`sha256`、`archive_url`、`check_status`（auto_verified / needs_review / human_verified / rejected）、`checked_at`、`notes`。
**主键**：用自然键 `(jurisdiction_fips, operator_npi 或 operator_slug, service_code, applies_to, rate_kind, effective_from)`，另外加一个代理键 `rate_id`。
- 多运营方：每个运营方各占若干行。城市页按运营方分组展示，不合并成一个“城市价”（竞品就是把纽约市绑到 Livingston Manor 志愿队上）。
- 居民/非居民：用 `applies_to` 拆成两行。
- 版本历史：不覆盖旧行。新原件到了，就给旧行写 `effective_to`，再插新行；`sources` 表按哈希留存每个版本的原件。
**来源描述规范**：
- Frictionless Data Package / Table Schema：一个 datapackage.json 写字段类型、主键、取值约束，有现成的 `frictionless validate` 可以直接做校验。**最简单，也够用，推荐。** https://specs.frictionlessdata.io/ , https://framework.frictionlessdata.io/
- W3C CSVW：表达力和 Table Schema 差不多，但工具生态偏弱。https://www.w3.org/TR/tabular-data-primer/
- W3C PROV：适合描述复杂的溯源图，对本项目太重；把逐行的 source_url / sha256 / retrieved_at 字段当作“简化版 PROV”即可。https://www.w3.org/TR/prov-overview/

## 4. 质量门
- 抽样复核：auto_verified 的记录每批随机抽 10%，至少 5 条，人工对照原件（与 playbook 一致）。needs_review 100% 人工看。首批 10 个城市建议 100% 人工复核，用来校准流程（这是建议）。
- 异常规则：ALS 低于 BLS；ALS2 低于 ALS1；里程费超出 $5–$100/英里，或单次转运超出 $200–$10,000（这些阈值是建议，实测后再调）；生效日期早于 2018 年或晚于今天 +1 年；同一个键出现两个金额；单位缺失；`source_quote` 匹配不到原文；哈希变了但金额没变（说明原件改版，需要复核）；与 CMS 基准的比值超过 20 倍或低于 0.5 倍时标记一下（只作提醒，不作结论）。
- **不出页的条件**：没有官方原件；原件只有“上限价”却没有标注清楚；运营方对应不上；生效日期缺失，或原件已经过期且没有新版；needs_review 还没清零；只有 CMS 或模型数据（这类只能放到州/ZIP 计算器里，不出城市页）。页面统一标注“官方原件 + 自动比对，未经医疗专业人员审核”。

## 5. 是否需要新开 bot
**判断标准**：①量：50 城市 × 约 5–15 行，属于一次性批量；②是否长期例行：每年 1 月 CMS 更新、每季度死链检查、原件变更监测，都是长期的；③是否需要独立权限或上下文：只需要读公开网页、在本机跑脚本，不需要新账号；④上下文污染：数据清洗的细节会挤占选题助理的记忆。
- (a) 选题助理 + executor 子任务：成本最低；子任务结束后上下文就丢了，只能靠文件和脚本衔接。适合前 10 城市的试点。
- (b) 专门的数据 bot：有自己的记忆，能长期盯原件变化和年度更新；代价是多一个要管理的 bot，交接也有成本。
**推荐**：**先用 (a) 跑前 10 个城市**，把脚本和 schema 固化下来；满足下面任一条件就开 (b)：命中率过了第 6 节的阈值，准备扩到 50 城以上；或者需要每月、每季度例行监测。不确定点：每城市的实际工时（未取得）；扫描件的占比（未取得）。
**如果新开，它的职责**：找原件、存档哈希、A/B 双路抽取、比对、维护 rates.csv / sources.csv / datapackage.json / 变更日志，按季度巡检死链和哈希变化。
**边界**：只读公开资料；不对外联系（不发 FOIA，需要的话由它起草、交人决定）；不花钱；不注册；不发帖；不改网站代码；不写页面文案。
**产出格式**：Frictionless Data Package（CSV + datapackage.json）、每批一份差异报告（markdown）、证据文件夹（原件 + 哈希）。
**交接方式**：共享电脑上固定的数据目录 + 每批一份 handoff.md（新增/变更/待复核/不出页清单）。选题助理只读取 check_status 为 auto_verified/human_verified、且 evidence_tier = official_source 的行来出页。

## 6. 失败判断（以下都是建议阈值，不是数据）
- 前 10 个大城市里能找到官方原件的不到 5 个（<50%） → 重新评估“只做有官方原件的城市”这个定位（例如改成以州/县为单位，或者先做州法矩阵）。
- 能找到原件的城市里，有效原件（未过期、能对应到运营方）不到 70% → 重新评估。
- A/B 两路不一致率超过 30%，或者人工复核发现 auto_verified 里有错 → 停下来修流程，暂不扩量。
- 每城市平均工时超过 2 小时（实测）→ 50 城市的计划要重排，或者改为开 (b) 并降低目标。
