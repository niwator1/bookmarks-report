# 10% 抽查（v3，2026-10-29）

- 抽样：rates.csv 共 56 行，抽 6 行（≥10%）。方法：Python `random.Random(42)`，先把 10 个城市名排序后 shuffle，取前 6 个城市，每城用同一随机源 `choice` 一行（为尽量覆盖不同城市）。
- 核对方式：重新打开 raw 原件（pdftotext / HTML 去标签后 grep），独立读金额、单位、生效日期；未参考 path_a 列。

| CSV 行号 | 城市 | 项目 | CSV 值 | 原件所见 | 结果 |
|---|---|---|---|---|---|
| 31 | San Antonio, TX | 非居民附加费 | $100 / per patient / 2026-10-01 | "EMS Services Effective as of October 1, 2026 Cost per patient … Transport fee surcharge for each nonresident patient $100"（sa.gov EMS Billing 页） | 一致 |
| 50 | Las Vegas, NV | 非急诊 ALS | $1,209.06 / per transport / 2026-02-01 | "Effective February 1, 2026 … Non-emergency response ALS $1,209.06"（files.lasvegasnevada.gov 2026 Maximum Allowable Rates） | 金额、日期一致；单位：原件只写 "Rate"，未写 per transport，「per transport」属解读，建议标注 |
| 18 | Houston, TX | 治疗+转运 | $2,158.16 / per transport / 2026-01-01 | "EMS/Ambulance Service Treatment and Transport 4-13(a)(1) $2,158.16 01/01/2026"（cohweb.houstontx.gov Fee Schedule） | 一致 |
| 42 | San Diego, CA | ALS2 | $3,371.91 / per incident / 2025-07-01 | FY2026 User Fee Schedule "(effective Date July 1, 2025) … ALS Emergency Transport Level 2 $3,371.91 per incident" | 与原件一致；但按 R-316243 该价自 2026-07-01 起已被 FY2027（+5%）取代，FY2027 官方金额未取得，属「可能过期」 |
| 3 | New York, NY | BLS（旧价） | $1,385 / per transport / 2023-05-01（旧版） | "Effective [May 1, 2023] July 1, 2026 … Basic Life Support Ambulance [$1,385.00] $1,793.00"（方括号为删除内容） | 一致 |
| 24 | Phoenix, AZ | BLS | $1,090.65 / per transport / 2026-04-17 | AZDHS Ground Ambulance Rate Schedule："Phoenix ETS (Emergency Transportation Services), City of … (1,224.39) (1,090.65) … 04/17/26" | 金额、日期一致；单位原件为 BLS 列基础费率，per transport 属解读 |

结论：6/6 金额与生效日期一致；0 行金额不一致。需注意 2 行单位为解读（拉斯维加斯、凤凰城），1 行（圣迭戈）因 FY2027 未取得而可能过期。
