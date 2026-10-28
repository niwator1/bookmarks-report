# 候选卡：burning bridges ai（2026-10-29，UTC+8）

## 结论（先看这里）
**不建独立站，状态「淘汰/仅观察」。救护车费用仍为主线。** 证据等级：C（SERP 与竞品页为公开实测；搜索量、KD、Trends 均未取得）。
理由：① 已有 ≥9 个同类 AI 工具站/大平台专题页抢同一个词，含精确匹配域名多个；② 需求完全绑定 Drake 一首歌的一段视频，找不到脱离名字的稳定需求词（通用词 character swap / ai 换人视频 已被大平台占据）；③ 歌曲与肖像版权风险高，同类站自己在条款里承认音乐不授权。

## ① 搜索趋势
- Google Trends（美国，近 12 个月 / 5 年，对比 ambulance cost）：**未取得**。试过：curl 调 Trends explore 接口，返回 HTTP 429（限流）；Trends 页面需浏览器渲染。缺：0-100 指数曲线、起涨时间点、相关查询。需要浏览器的清单：trends.google.com 打开 `burning bridges ai` vs `ambulance cost`，geo=US，分别选 past 12 months / past 5 years，截相关查询。
- 公开时间线索（非量）：同类站条款「Last updated October 8, 2026」（https://drakeburningbridgesai.com/terms ），说明 2026 年 10 月初已有站上线；线索帖 https://x.com/kristoff_wu/status/2112216903150436383 。
- 搜索量 / KD（Ahrefs 美国）：**未取得**。试过：curl https://ahrefs.com/keyword-generator 返回 200 但为前端应用壳，结果需浏览器内执行并可能有人机验证；按要求未硬绕。需要浏览器：keyword-generator 与 keyword-difficulty 输入 `burning bridges ai`、`drake burning bridges ai`、`character swap video`，国家 US。

## ② SERP 前 10（WebSearch 实测，非 Google 原生排序）
| 位次 | 站点 | 类型 | 精确匹配域名 |
|---|---|---|---|
| 1 | https://klingmotion.ai/burning-bridges-ai | AI 工具站内页 | 否 |
| 2 | https://imageat.com/trends/drake-burning-bridges-ai-video-generator | AI 工具站趋势页 | 否 |
| 3 | https://burning-bridgesai.com/agents/product.md | 专门 AI 站 | 是 |
| 4 | https://drakeburningbridgesai.com/terms | 专门 AI 站 | 是 |
| 5 | https://www.media.io/ai/explore/zone/drake-burning-bridges-ai-video-generator | 大平台（Wondershare 系）专题页 | 否 |
- 本次搜索只返回 5 条，6-10 位**未取得**（DuckDuckGo HTML 接口返回空，Google 未直连）。
- 已有同类 AI 站：是，且全部为“上传一张照片换主角”的同质玩法。
- DR / 估算流量：**未取得**（Ahrefs traffic-checker 需浏览器）。需要浏览器：traffic-checker 查 klingmotion.ai、imageat.com、media.io、getburningbridges.com。

## ③ 已有同类站清单
| 站 | 玩法（来源页面原文） | 流量线索 |
|---|---|---|
| https://getburningbridges.com/ | 线索给出的活站，换主角视频 | 未取得 |
| https://burningbridgesvideo.io/ | 同上 | 未取得 |
| https://aiburningbridges.io/ | 同上 | 未取得 |
| https://burningbridges.video/ | 同上 | 未取得 |
| https://burning-bridgesai.com | 1 张主角照+最多 3 个朋友照；15 秒 100 积分 / 28 秒 300 积分；**不带音乐**；一次性积分 | 未取得 |
| https://drakeburningbridgesai.com | 积分包+月/年订阅，Stripe 支付；条款说明配乐属权利人、不授予许可 | 未取得 |
| https://klingmotion.ai/burning-bridges-ai | 1 张照片，15 秒 16:9 带原曲，失败退积分 | 未取得 |
| https://imageat.com/trends/drake-burning-bridges-ai-video-generator | 205 积分/次，15 或 29 秒，480p/720p | 未取得 |
| https://www.media.io/ai/explore/zone/drake-burning-bridges-ai-video-generator | 提示词 + Motion Control 参考视频 | 未取得 |

## ④ 变现可行性
- 可行方式：**按次积分/订阅**（同类站均如此，见 burning-bridgesai.com、drakeburningbridgesai.com/terms）。广告：工具页停留短、词寿命短，不支撑；联盟：可挂 AI 视频平台联盟，但前提是有流量，未取得量数据。
- 成本：每次生成调用视频模型有真实成本（drakeburningbridgesai.com/terms 原文“Every render costs us real money”），我们不建站不付费即无法核实毛利。
- 风险：**歌曲版权**——同类站条款明确配乐为商业音乐、不授予许可，平台可能静音/下架（https://drakeburningbridgesai.com/terms ）；部分站为此直接去掉音乐（burning-bridgesai.com）。**名人肖像/商标**——词本身含艺人名，原片人物形象与 MV 画面属权利人；均自称“非官方、与 Drake 及唱片公司无关”。**换脸政策**——需限制仅本人/同意的成年人、禁止儿童与色情，支付与广告平台对 deepfake 类审核严。

## ⑤ 怎么判断值得做 / 何时放弃（判定线 vs 实测）
| 判定线 | 实测 | 结果 |
|---|---|---|
| ① 美国月搜索量 <1,000 且 Trends 近 3 个月下降 → 不建 | 量与 Trends 未取得 | 待补；但本线不是唯一否决 |
| ② SERP 前 5 有 ≥3 个 DR50+ 工具站且无差异化 → 不建 | 前 5 全是工具站（DR 未取得）；玩法全同质，无差异化切口 | 竞争侧已倾向否决 |
| ③ 找不到脱离名字的通用需求词 → 只做内页 | 通用词 `character swap video`/`ai 换人视频` 已有 Revid、Mitte 等大平台工具页（https://www.revid.ai/tools/character-swap ） | 最多做内页，不独立建站 |
- 值得重开的条件（需浏览器补数后）：美国月量 ≥1,000 **且** Trends 近 3 个月仍在涨 **且** 前 5 至少 2 个 DR<30 的站。任一不满足即放弃。
- 放弃时点：2026-11-30 前若补不到上述三项数据或 Trends 已回落到峰值 30% 以下 → 彻底淘汰。
