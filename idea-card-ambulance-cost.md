# 思路卡：救护车费用（ambulance cost）数据站

> 日期：2026-10-28（UTC+8）｜状态：优先候选（待用户决定是否建站）｜证据来源见同目录 browser-batch-3.md、browser-batch-4.md、keyword-round-2-evidence.md

## 通用需求词（不是名字）
- ambulance cost：Ahrefs 美国量级 >1,000，KD Medium（14），想法词总数 822
- how much does an ambulance cost：>1,000，KD Easy
- how much does an ambulance ride cost：>1,000，KD Easy（6）
- ambulance cost by state：>100，KD Easy（0）
- air ambulance cost by state：Ahrefs 无数据（淘汰这条）

## 证据（A/B/C/D）
- A：同上。Ahrefs 免费档只给量级带，没有具体数字。
- B：前排有 uhc.com、carecredit.com、goodrx.com 等大站，也有弱站（wcambulance.com DR3 反链 0；wagnerreese.com DR39；eliteamb.com DR25）。但**专门竞品 ambulancecost.com 已存在**：自称 "covering 1 in 3 cities"，州页约 51 个，全站链接约 192 个，没有数据来源列表也没有更新日期，在 "ambulance cost by state" 排第 1。
- C：近 12 个月 4 条不同的人的 Reddit 帖子（NoStupidQuestions 2026-07-09 直接问各州救护车价格；HospitalBills 2026-09-10、2026-09-15；MedicalBill 2025-11-26）。
- D：供给热度中等，有专门站，说明已有人在做。
- 数据：CMS 救护车费率表，免费、可整包下载、每年更新；但那是 Medicare 费率，不是患者实际账单。实际价格要抓各地 EMS 费率表，自建工作量中到高。

## 差异化（缺口）
- 竞品缺：数据来源和口径说明、更新日期、按邮编查的 CMS 费率工具、各州平衡账单法对照、"账单太高怎么办"的处理流程页。
- 页面类型：州页 × 服务类型（BLS/ALS/空中/每英里）；城市页取决于能抓到多少公开费率表。

## 风险
- YMYL（医疗费用）：页面必须写明 Medicare 基准价与实际账单的区别，不能当医疗或法律建议。
- 竞品 ambulancecost.com 有精确匹配域名和先发优势。
- 几乎所有前排都有 AI Overview（部分词没有）。
- Google 结果带洛杉矶位置偏向，只是前排的粗判断，不是真实排名。

## 怎么判断它失败了
1. 2026-12-15：抽 50 个州和城市，只用公开来源（CMS 文件加各地 EMS 费率表）能做出带来源的页面不到 30 个，就说明数据做不出差异化，放弃。
2. 2027-01-28：ambulancecost.com 若补上数据来源、更新日期和邮编查询，且前 10 名里已有 3 个以上带州页的专门站，降为观察。
3. 上线后 4 周（索引和展示）和 8 周（点击）：Search Console 里相关查询每月展示不到 1,000，或没有一页进前 20，停止扩页。

## 还缺什么
- 搜索量只有量级带，没有具体数字；前排判断来自一次浏览器结果页。
- ambulancecost.com 的数据来源、DR 和流量未核实。
- CMS 文件的使用条款原文未打开。
