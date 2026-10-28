# 美国救护车费用数据站：需求规模有多大（只用公开来源）

查询日期：2026-10-29（新加坡时间，UTC+8）。原则：每个数字都附来源，取不到的写「未取得」，不做估算。

## 1. 使用量（出车/转运）
| 指标 | 数值 | 来源 |
|---|---|---|
| NEMSIS 2023 年全国 EMS 出车（activations），注意这是出车次数，不是患者人数 | 54,190,579 次（14,369 家机构） | https://nemsis.org/wp-content/uploads/2025/05/NEMSIS-Annual-Public-Data-Report-2023__.pdf |
| 每年被救护车送到急诊的商业保险患者人数 | 约 300 万人；约占商业保险急诊就诊的 1/10 | https://www.kff.org/health-costs/analysis-half-of-emergency-ambulance-rides-lead-to-out-of-network-bills-for-privately-insured-patients/ |
| 应急地面救护车按运营方分（2020，NEMSIS） | 消防 37%、其他政府 25%、私营 30%、医院 8% | https://www.healthsystemtracker.org/brief/ground-ambulance-rides-and-potential-for-surprise-billing/ |
| Medicare FFS 地面救护车（2023） | 1,140 万次转运；支付 53 亿美元；10,500 家机构 | https://www.medpac.gov/wp-content/uploads/2025/03/Ambulance-MedPAC-03.25_SEC.pdf |
| Traditional Medicare 转运量趋势 | 2017 年超过 1,460 万次，2022 年低于 1,080 万次（约 2/3 的降幅可由 MA 参保增加解释） | https://www.cms.gov/files/document/ground-ambulance-industry-trends-2017-2022-report-analysis-medicare-fee-service-claims.pdf |
| GAO-13-6（2010 年数据） | 约 1,660 万次转运；约 510 万 Medicare FFS 受益人；约 52 亿美元 | https://www.gao.gov/products/gao-13-6 |
| 全美地面救护车年转运总数（所有付款方） | 未取得（没找到权威的单一合计数） | — |
| Medicare 近年使用救护车的受益人人数 | 未取得（只有上面 2010 年的数字） | — |

## 2. 账单端痛点
| 指标 | 数值 | 来源 |
|---|---|---|
| 有网络外收费的应急地面救护车比例（2018 年大雇主保险） | 应急 51%；非应急 39% | https://www.healthsystemtracker.org/brief/ground-ambulance-rides-and-potential-for-surprise-billing/ |
| 网络外应急救护车比例超过 2/3 的州 | WA、CA、FL、CO、TX、IL、WI | 同上 |
| 潜在意外账单比例（HCCI 数据，2014–17） | 应急 28%；非应急 26%（应急网络外比例 85%） | https://www.healthaffairs.org/doi/10.1377/hlthaff.2022.00738 |
| 潜在意外账单比例（单一大型保险，2013–17） | 全部救护车 71%；应急地面 79% | https://www.healthaffairs.org/doi/full/10.1377/hlthaff.2019.01484 |
| 地面救护车潜在意外账单的中位数 | 450 美元；中位总收费约 1,005 美元（应急）和 992 美元（非应急） | 同上 |
| 地面救护车潜在意外账单的年度总额 | 约 1.29 亿美元/年（2013–17，单一保险样本） | 同上 |
| 网络外应急地面救护车比例（Elevance，2012–2025） | 44%–51% | https://www.elevancehealth.com/content/dam/elevance-health/articles/ppi_assets/reports/PPI_Emerg_Ground_Ambulance_Costs.pdf |
| 平均意外账单金额 | 未取得 | — |
| GAO-22-104632 原文 | 未取得（搜索没有找到这份报告的内容，无法引用） | — |
| 《No Surprises Act》是否覆盖地面救护车 | 不覆盖（覆盖空中救护车）；法案要求成立 GAPB 咨询委员会，该委员会已于 2023 年提出建议 | https://www.healthsystemtracker.org/brief/ground-ambulance-rides-and-potential-for-surprise-billing/ ；https://www.cms.gov/files/document/report-advisory-committee-ground-ambulance-and-patient-billing.pdf |
| 有州级地面救护车保护的州数 | 24 个州（Commonwealth Fund，限完全保险计划）；KFF Health News 的口径是 2025 年 Utah、North Dakota 加入另外 18 个州（共 20 个）。两家口径不同 | https://www.commonwealthfund.org/publications/maps-and-interactives/expanding-no-surprises-act-protect-consumers-surprise-ambulance ；https://kffhealthnews.org/health-care-costs/ground-ambulance-surprise-billing-colorado-montana-insurer-pushback-premiums/ |

## 3. 搜索需求
- 项目已有的 Ahrefs 免费量级（美国，只是区间，不是精确值）：`ambulance cost` >1,000/月，KD14；`how much does an ambulance ride cost` >1,000/月，KD6；`ambulance cost by state` >100/月，KD0。
- Google Trends 相对热度：未取得（本次没有可直接读取的公开数据，没有登录，也没有抓取）。
- 其他精确搜索量：未取得，本文不给出。

## 4. 需求规模判断
**结论：这是一个「小而精的数据站」，不是大流量站。**

依据：
- 现实需求大：每年 5,400 万次出车，Medicare 一年 1,140 万次转运。痛点也真实：约一半应急转运有网络外收费，潜在意外账单的中位数为 450 美元。此外，联邦法律不保护地面救护车，州级保护只覆盖约 20–24 个州，各州规则不同，正好适合「按州查」的数据页。
- 但能看到的头部搜索词只有「>1,000/月」量级，长尾词「by state」只有「>100/月」。从现有公开证据看不出单个词有数万级月搜索量。
- KD 低（0–14），说明有机会排进前列，但总流量的天花板有限。价值更可能来自高意图的长尾（州、城市、保险、账单申诉）和引用/外链，而不是大流量。

不确定点：
- Ahrefs 的数字是下限区间，真实量可能明显更高。
- 没有取得 Trends 数据和长尾词合计。
- 账单研究的数据大多是 2013–2018 年的，在州法普及后比例可能已经下降。
- 没有取得 GAO-22-104632 原文，也没有全付款方的转运总数。
