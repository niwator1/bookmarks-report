# 当前可做候选（2026-10-28，UTC+8）

> 筛词结论一页纸。只看这一页就知道接下来做什么。证据细节见同目录其他文档。

## 一句话

**接下来可以做的只有 1 个主选 + 1 个备选。其他词全部淘汰。选定建站词仍由你决定。**

---

## 主选：救护车费用（ambulance cost）→ 状态「优先」

| 项 | 内容 |
|---|---|
| 通用需求词 | `ambulance cost`（>1,000，KD Medium 14）、`how much does an ambulance cost`（>1,000，KD Easy）、`how much does an ambulance ride cost`（>1,000，KD Easy 6）、`ambulance cost by state`（>100，KD Easy 0） |
| 页面类型 | 州页 × 服务类型（BLS / ALS / 空中 / 每英里）；城市页取决于能抓多少公开费率表 |
| 为什么能做 | 上层词有量；按州词 KD 0；前排有 DR3～DR39 的弱站；近一年 4 条不同的人在 Reddit 问救护车账单 |
| 数据 | CMS 救护车费率表，免费可批量下载，每年更新（Medicare 基准价，不是患者实际账单） |
| 竞品 | [ambulancecost.com](https://ambulancecost.com) 已存在（约 51 州页、自称覆盖 1/3 城市），但**不写数据来源、不写更新日期、没有邮编查询** |
| 差异化 | 带来源与口径说明的州页；按邮编查 CMS 费率；各州平衡账单法对照；“账单太高怎么办” |
| 风险 | 医疗费用相关（YMYL），必须写明 Medicare 基准价 ≠ 实际账单 |
| 失败条件 | ① 2026-12-15：抽 50 州/城市，用公开来源做出来源齐全的页面不到 30 个 → 放弃 ② 2027-01-28：竞品补上来源+日期+邮编查询，且前 10 有 3 个以上专门站 → 降为观察 ③ 上线后 8 周相关查询每月展示不到 1,000 → 停扩页 |
| 证据文件 | `idea-card-ambulance-cost.md`、`browser-batch-3.md`、`browser-batch-4.md`、`keyword-round-2-evidence.md` |

---

## 备选：医疗检查价格（MRI / CT / 结肠镜 / 超声等）→ 状态「观察」

| 项 | 内容 |
|---|---|
| 通用需求词 | `how much does an mri cost`、`mri cost without insurance`、`how much does a ct scan cost`、`how much does a colonoscopy cost`、`how much does an ultrasound cost`（量级均 >1,000，KD 0～12） |
| 页面类型 | 检查类型 × 州 / 城市；Medicare 基准价 vs 医院现金价 vs 影像中心现金价对比 |
| 为什么还留着 | 需求比救护车更大；近一年 4 条真人账单求助；前排有弱点（缺来源、缺日期、缺三类价格对比） |
| 为什么不是主选 | 前排有 goodrx（DR85）、carecredit（DR91）、mdsave、newchoicehealth；真实医院价格文件约 6000 家、格式乱、合规率低；YMYL 风险更高 |
| 数据 | CMS 医生付费表 + 医院门诊付费表（免费可下载）；医院公开价格文件处理很重 |
| 失败条件 | 2027-01-26：做不出至少 5 种检查 × 50 州、来源和日期齐全的价格表；或 `mri cost in [state]` 前 10 被大站占满 → 放弃 |
| 证据文件 | `medical-price-direction.md`、`browser-batch-7.md` |

---

## 已淘汰（不要再做）

| 词 / 方向 | 淘汰原因 |
|---|---|
| revenue per employee | C 证据弱；员工数要从 10-K 正文抽取 |
| land bordering public land / wordart generator | 量小或前排强 |
| 唱歌跑调检测 / 失联自动触发 / Google TV 去广告 / 雅思词表 | 前排无缺口或量 <100 |
| midi to chords / square a building / food truck permit / car wrap / domain hack | 量级全部 <100 |
| car registration / llc / roof pitch / lottery tax | 量小或前排大站 |
| cost to replace roof/windows/windshield、建房、生活成本 | >1,000 但前排 DR80+ 大站 |
| boat registration / hunting·fishing license / ev fee / cdl / marriage license / small claims / notary fees / hybrid battery | Ahrefs 无数据或 <100，或前排官方/协会站 |

---

## 你现在要决定的事

1. **要不要选定「救护车费用」作为建站词？**（选定后我再出项目卡和数据管线验证方案；选定前我只做研究，不建站、不注册、不花钱）
2. 备选医疗价格先挂着，等救护车验证过了再碰。
