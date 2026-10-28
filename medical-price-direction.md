# 医疗价格透明方向（MRI/CT/结肠镜/超声/X光/急诊费用）评估 — 2026-10-28
只读调研，WebSearch 得到的信息，没有登录。没有猜搜索量。

## 1. 数据可行性
| 来源 | 内容/格式 | 许可/条款 | 更新 | 自建处理量 |
|---|---|---|---|---|
| CMS Hospital Price Transparency MRF（45 CFR 180）https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-E/part-180/subpart-B ；规范 https://github.com/CMSgov/hospital-price-transparency | 每家医院一个 CSV/JSON：毛价、现金折扣价、按保险公司的协商价、最低/最高。2026-01-01 起用 v3.0：中位数、P10、P90 allowed amount 和计数，加 Type 2 NPI。2026-04-01 起执法 https://www.cms.gov/newsroom/fact-sheets/cy-2026-opps-ambulatory-surgical-center-final-rule-hospital-price-transparency-policy-changes | 公开的法定披露；再发布的条款要看各医院网站，**没核实** | 医院自己更新（规则要求至少每年一次，**这一条没再核实原文**） | 很重：约 6000 家医院，每家文件几十 MB 到几 GB，格式不一。PRA 2026-09 报告：2000 家医院里 49.4% 完全合规，只有 18% 给出可用的美元价（覆盖一半以上项目）https://www.patientrightsadvocate.org/eighth-report-toolkit |
| CMS Physician Fee Schedule https://www.cms.gov/medicare/physician-fee-schedule/search | 按 CPT/HCPCS 和地区（locality）给 Medicare 付费额、RVU，可下载 | 联邦公开；CPT 描述文字归 AMA 版权（**许可细节没核实**，一般不能整段转载 CPT 描述） | 每年，季度修订 | 很小 |
| OPPS Addendum B（2026 年 10 月）https://www.cms.gov/medicare/payment/prospective-payment-systems/hospital-outpatient-pps/quarterly-addenda-updates/october-2026-addendum-b | HCPCS→APC→全国付费额 | 同上 | 每季度（10 月版 2026-10-05 生效） | 很小，要自己按地区工资指数调整 |
| DoltHub transparency-in-pricing https://www.dolthub.com/blog/2023-06-28-how-not-to-hpt/ | 1000+ 家医院，3.3 亿行，SQL/Parquet | CC 4.0（博客原话，具体是 BY 还是 BY-NC **没核实**） | **已停更**：数据是 2023 年第三季度的，官方说不再收集 https://www.dolthub.com/blog/2025-01-28-state-of-hospital-price-transparency-data/ | 中等，但数据太旧 |
| Turquoise Health 研究数据集 https://turquoise.health/researchers/request_dataset?dataset_type=hospital_rates | 有限子集 | 免费，但要签 **Non-Commercial** MSA，**不能用于商业站** | 不定期 | — |
| FAIR Health Consumer https://www.fairhealthconsumer.org/ | 理赔数据，按 geozip，只能网页查询 | 消费者用免费；商业用途的链接/内容要授权付费；**不能抓取** | — | 不可用 |
| PatientRightsAdvocate 合规报告 | 报告和工具包，不是价格数据集 | 只能引用 | 每年 | — |

结论：免费又能商用的现成汇总数据集**没找到**。可行的路线是 CMS PFS + OPPS 做 Medicare 基准价（按州/地区），再从少量医院 MRF 自己抽现金价当样例。

## 2. 竞品
- **newchoicehealth.com**：MRI 等检查有全国均价页（$1,325、"target fair price $750"）、按城市页（例如 /places/california/fairfield/mri，写了"7 家机构的中位数"）、按细分部位的价格区间。是程序化生成的大站。页面能看到作者，但**数据来源和更新日期不清楚**。有些城市区间很离谱（Tampa MRI $80–190），引导用户点"Free Quote"。https://www.newchoicehealth.com/mri/cost
- **healthcarebluebook.com（Valenz）**：输入 ZIP 出 Fair Price，数据来自全国支付数据。是工具，不是可索引的静态长尾页。https://www.healthcarebluebook.com/ui/findfairprice
- **fairhealthconsumer.org**：非营利，有权威的理赔数据，按 geozip 估算有保险/无保险费用。是交互工具，不是静态页。
- **mdsave.com**：卖预付套餐的平台，有 MRI 全国均价（不打造影剂 $612、打造影剂 $768）和按城市、按机构的价格。https://www.mdsave.com/t/imaging-radiology/how-much-does-mri-cost
- **Turquoise Health**：消费者搜索工具，数据量大，没能确认它有按城市的静态 MRI 页。
- 很多保险经纪和影像中心的博客（例如 hotalinginsurance.com 2026 年的 MRI 文章）和影像中心公开的自费价目表（advancedimg.com、brightlightimaging PDF）。
- mrisearch、medicalpriceguide：**没核实**。
- 它们缺的东西：没有统一标注"Medicare 基准 vs 医院现金价 vs 独立影像中心现金价"的三层对比；数据来源和更新日期不透明；没有引用 2026 年 v3.0 的 P10/P50/P90 allowed amount；没有"怎么自己查医院 MRF"的教程。

## 3. C 证据（近 12 个月真人帖子）
1. 2026-03-25，r/povertyfinance：医院报价 $800，问没保险怎么做最便宜的肩部 MRI。https://www.reddit.com/r/povertyfinance/comments/1s3bd5i/cheapest_way_to_get_an_mri_without_insurance/
2. 2025-10-07，r/HealthInsurance：发帖人问"你们没保险做 MRI 花了多少"，多人回复 $250–$475。https://www.reddit.com/r/HealthInsurance/comments/1o072dm/how_much_did_your_mri_scan_cost_without_insurance/
3. 2026-08-12，r/HospitalBills：一次 CT 被收 $10,000，问是否正常、能否申诉。https://www.reddit.com/r/HospitalBills/comments/1vmrvbz/being_charged_10000_for_ct_scan/
4. 2026-08-01，r/MedicalBill：没保险的应届毕业生，一次急诊加一次 CT 收到 $10,355 账单，问怎么办。https://www.reddit.com/r/MedicalBill/comments/1vcb65p/one_er_visit_one_ct_scan_and_a_10355_bill_what/
（补充：r/HospitalBills 上有人拿医院 MRF 里的价格去对账，发现超声账单是文件价的 4 倍。但帖子日期大约在 2024 年，**不在 12 个月内**。https://www.reddit.com/r/HospitalBills/comments/1e45pdz/ ）
4 条来自不同版块、不同发帖人。帖子日期是网页里的回复时间推出来的，发帖日期本身没逐条打开核实。HN 没搜到。

## 4. YMYL 风险与合规
- 必须写清楚：仅供参考的估算，不是报价，也不是医疗、法律或保险建议；实际费用取决于保险计划、免赔额、机构和账单代码；就医前向机构要书面现金价，或按《No Surprises Act》要 Good Faith Estimate（CMS 页面写明急诊不适用 GFE）。每个数字标注来源、数据期和更新日期。
- 不能这样写：
  - 写成"你会付 $X"或"保证最低价"；
  - 劝人因为价格放弃或推迟急诊和医生建议的检查；
  - 把 Medicare 付费额说成现金价；
  - 整段复制 CPT 描述（AMA 版权）；
  - 未经授权使用 FAIR Health、Turquoise 的数据；
  - 拿医院排名做"贵、坑人"之类的指控性措辞。
- 作者和审核：最好有医疗账单或保险背景的人审核署名，写明方法论页。

## 5. 相对 ambulance cost 的结论
- 优劣一句：需求更大、长尾更多（几十种检查 × 50 州 × 有无保险），C 证据也更强；但竞品更多、更成熟（newchoicehealth、mdsave、FAIR Health、Bluebook），真实现金价数据处理很重，YMYL 风险也更高。ambulance cost 数据单一、对手少，更适合先做小站；这个方向更适合作为第二站，或者以后从 ambulance 站扩展出去。
- 失败条件：到 **2027-01-26（第 90 天）** 复查。如果用 CMS PFS/OPPS 加不超过 20 家医院 MRF，做不出至少 5 种检查 × 50 州、有清楚来源和日期的价格表；或者 Google 上 "mri cost in [state]" 的前 10 名里，没有任何一个 DR 低、数据薄的页面（全是 newchoicehealth、mdsave、大型医疗或保险站），就放弃这个方向。

## 没取到的
mrisearch、medicalpriceguide 的情况；医院 MRF 再发布条款的原文；DoltHub CC 4.0 的具体变体；规则要求的 MRF 更新频率原文；各竞品的页面数量和规模数字；HN 帖子；搜索量（按要求没猜）。
