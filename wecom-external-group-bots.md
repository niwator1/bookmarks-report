# 企业微信外部群（客户群）机器人接入方法调研
调研时间：2026-10-28（UTC+8）。只读调研，没有注册、付费或联系任何人。
标注说明：【官方】=企业微信或微信官方页面；【第三方】=服务商或博客；【未核验】=没有在官方页面逐条确认。

## 一句话结论
截至 2026-10，**企业微信没有任何官方机器人能直接加入外部群并与客户双向 AI 对话**。合规的做法有三类：
- 官方关键词自动回复
- SCRM 服务商（基于会话存档读消息，再由成员账号或服务商通道回复）
- 用微信客服做 1 对 1 承接，群只用来通知

能在外部群里双向收发消息的只有 iPad 协议和 PC Hook，这两种都有封号风险，不推荐。

## 方法清单（13 种）

### 1. 群机器人 Webhook（新版已改名「消息推送」）
- 只能加入内部群，外部群暂不支持。不支持回调，也就是只能发、不能收。每个机器人每分钟最多发 20 条。不支持 @ 成员。
  来源：【官方】https://open.work.weixin.qq.com/help2/pc/14931
- 包含外部联系人的群不能添加机器人。
  来源：【第三方】https://help.gitee.com/enterprise/management/functions/webhooks/webhook-for-wecom-robot ；https://docs.guandata.com/product/bi/7.1.0/423374913496154112
- 2023 年就有开发者提问外部群什么时候能加机器人，官方没有给出时间表。
  来源：https://developers.weixin.qq.com/community/minihome/doc/000e2ab22c0bd8584170f81c369c00

### 2. 智能机器人（AI 机器人，分 API 模式和长连接模式）
- 可以自定义模型、知识库、API/MCP 插件和工作流，在群里被 @ 后能回复。但**只能加入内部群**，互联群、上下游群、外部群暂不支持。和智能机器人的聊天记录不会进入会话存档。
  来源：【官方】https://open.work.weixin.qq.com/help2/pc/21663
- 长连接地址是 wss://openws.work.weixin.qq.com，订阅命令为 aibot_subscribe，接收 aibot_msg_callback 回调。
  来源：【官方】https://developer.work.weixin.qq.com/document/path/101463 ；https://developer.work.weixin.qq.com/document/path/101468
- 结论：适合做内部员工助手，不能直接服务外部群客户。

### 3. 客户联系 API：客户群列表、详情和变更事件
- groupchat/list 和 groupchat/get 能读取群信息和成员列表。change_external_chat 只推送建群、成员变化、群名或公告变更、解散等事件，**不推送群聊消息**。
  来源：【官方】https://developer.work.weixin.qq.com/document/path/96361 ；https://developer.work.weixin.qq.com/document/path/92707

### 4. 客户群群发（add_msg_template，chat_type=group）
- 调用接口只会创建任务，**必须由群主确认后才发出**。一次最多指定 2000 个群。每个客户群每月最多接收「当月天数」条群发，可以调整为每周 7 条或每天 1 条。
  来源：【官方】https://developer.work.weixin.qq.com/document/path/92698
- 每个客户群每天能接收成员群发 1 条；企业统一群发每月 1 条（官方帮助页，版本可能较旧）。
  来源：https://work.weixin.qq.com/nl/act/p/a255f5904bba4954
- 结论：只能做通知或 SOP，没法用来实时回复。

### 5. 官方客户群「自动回复」（关键词）
- 管理员在「客户联系-效率工具-自动回复」里配置关键词和默认回复，每个群要由群主单独开启。客户在群里 @小助理或服务人员时触发。
  来源：【官方】https://work.weixin.qq.com/nl/act/p/bfbc0708645f4551
- 这是唯一由官方提供、在外部群里「收到客户消息后自动回复」的能力。缺点是只能按关键词匹配，不是 AI，也不能调用外部系统。
- 免费与否：【未核验】。

### 6. 会话内容存档（msgaudit）或数据与智能专区
- 可以读取员工与客户的单聊和群聊内容（包括外部群），但需要员工知情、外部联系人同意，而且**只能读，不能发**。
  来源：【第三方】https://www.xiaoduoai.com/blog/docs/vsg1upc5tzfho9zy
- 价格（按账号每年计）：服务版 450 元，企业版 900 元；201–500 个账号分别为 288 元和 576 元。
  来源：【第三方】https://www.beikunscrm.com/cms/huihuacundang/6.html
- 需要企业认证才能开通。
  来源：【第三方】https://www.wescrm.com/siyuzhishiku/siyugongju/40722.html
- 数据专区是服务商购买的增值接口，免费试用 30 天，可选存储 90 天到 2 年。
  来源：【官方】https://developer.work.weixin.qq.com/document/path/100246
- 「存档读消息 + 成员账号回复」中的回复环节，官方 API 只有群发接口（需群主确认，每天 1 条）。所以要实现实时回复，实际上要靠服务商的托管或 RPA 通道。这一条是【未核验】的推论。
- 是否有「产生会话」实时回调：【未核验】。

### 7. 微信客服（kf）
- 微信用户主动发消息后，48 小时内企业最多可以发 5 条；用户继续发消息，额度会刷新。可以由「智能助手」接待。
  来源：【官方】https://developer.work.weixin.qq.com/document/path/94677
- 只支持 1 对 1，**不能拉进群**（官方文档里没有群能力，本条是根据文档推断）。微信对话开放平台的外部服务就是通过微信客服接入的。
  来源：【官方】https://developers.weixin.qq.com/doc/aispeech/platform/application/wecom.html
- 结论：AI 直接对接客户最合规、成本最低的通道。

### 8. 自建应用或第三方应用的消息回调
- 只能收发内部成员与应用之间的消息，不能收外部群消息。
  来源：https://developer.work.weixin.qq.com/document/path/94670 （需要结合第 3 条理解）

### 9. SCRM / 私域 SaaS
- **句子互动**：客户群支持关键词回复和 AI 知识库回复，可转人工，还有 RPA 产品线。
  来源：https://www.yun88.com/qa/3760.html ；https://juzibot.com/products/miaohui.html
- **微盛·企微管家**：有客户群自动回复教程。
  来源：https://college.wshoto.com/a/3851.html
- **微伴、探马**：已知存在，但它们在群内的 AI 能力和价格【未核验】。
- 官方应用市场：https://open.work.weixin.qq.com/appStore/store/home/category?id=1
- 风险提示：部分 SCRM 的群内 AI 回复靠托管账号或 RPA 实现，签约前要问清是走官方接口还是协议。

### 10. 官方 OpenClaw 插件、企业微信 CLI、MCP（2026 年新能力）
- 2026 年 3 月起陆续上线：长连接机器人可关联 OpenClaw；10 人及以下的小团队可用消息、日程等 MCP；CLI 已开源（npm 包 @wecom/cli）；2026 年 4–5 月增加了文档读取 MCP。
  来源：【官方】https://work.weixin.qq.com/nl/index/openclaw ；https://work.weixin.qq.com/nl/index/aicli
- 这些能力都基于智能机器人，因此**同样不支持外部群**（依据第 2 条推断）。

### 11. 开源 Agent 框架（Dify、FastGPT、Coze 等）
- 这类框架通常通过自建应用或智能机器人接入企业微信，只覆盖内部用户和单聊。各框架是否支持外部群【未逐个核验】。
- chatgpt-on-wechat（CowAgent）的 wework 通道依赖 ntwork（PC Hook，需要指定企微 4.0.8.6027 版本），主项目已不再维护个人号通道。
  来源：https://github.com/zhayujie/chatgpt-on-wechat/pull/1385 ；https://github.com/zhayujie/chatgpt-on-wechat/issues/2477

## 不推荐（灰色手段，有封号风险，仅供了解）

### 12. iPad 协议
- 原理是逆向企微的私有协议，能接收外部群消息并自动回复。
  来源：https://cloud.tencent.com/developer/article/2684021 ；https://github.com/wechat-ipad-api/wecomapi ；https://github.com/lichaohuai/wecom-protocol-gateway
- Wechaty 的 wxwork / WorkPro puppet 也是付费 token 加协议的模式。
  来源：https://wechaty.js.org/docs/puppet-services/compatibility
- 风险：非官方能力，账号和企业主体都可能被限制；第三方文章也承认要做防风控措施（来源同上）。

### 13. PC Hook 或 UI 自动化
- 例如 ntwork 或 DLL 注入，需要在 Windows 上固定使用旧版本客户端（来源：https://github.com/cheungchazz/ntwork）。
- 风险：客户端版本被锁定，一旦强制升级就失效，并有封号风险。

## 对比表
| 方法 | 能进外部群 | 能收客户消息 | 能回复 | 需要企业认证 | 成本 | 封号风险 | 开发量 | 结论 |
|---|---|---|---|---|---|---|---|---|
| 1 Webhook | 否 | 否 | 否 | 否 | 免费 | 无 | 极低 | 仅内部通知 |
| 2 智能机器人 / OpenClaw | 否 | 仅内部 | 仅内部 | 否【未核验】 | 免费 | 无 | 低 | 内部助手 |
| 4 客户群群发 | 是 | 否 | 群主确认，每天 1 条 | 客户联系需要（见下方） | 免费 | 无 | 低 | 通知 / SOP |
| 5 官方自动回复 | 是 | 是（需 @） | 关键词 | 同上 | 免费【未核验】 | 无 | 零代码 | 可做兜底 |
| 6 会话存档 | 是（只读） | 是 | 否 | 是 | 450 元/人/年起 | 无 | 高 | 配合服务商使用 |
| 7 微信客服 | 否（1 对 1） | 是 | 48 小时内 5 条 | 【未核验】 | 免费【未核验】 | 无 | 中 | **首选 AI 通道** |
| 9 SCRM | 是 | 是 | 关键词 / AI | 通常需要 | 付费，需询价 | 取决于实现方式 | 低 | 预算够可选 |
| 11 开源框架 | 通常否 | 内部 | 内部 | 否 | 免费 | 低 | 中 | 内部用 |
| 12 iPad 协议 | 是 | 是 | 是 | 否 | 协议费 | **高** | 中 | 不推荐 |
| 13 PC Hook | 是 | 是 | 是 | 否 | 免费 | **高** | 中 | 不推荐 |

## 企业认证与客户数量上限
- 未认证企业，全企业共享的客户上限是 **100 人**；认证后可获得免费额度，超出需要购买。
  来源：【官方】https://open.work.weixin.qq.com/help2/pc/20172 ；https://open.work.weixin.qq.com/help2/pc/21326
- 认证后免费额度为 2000 人。这个数字来自第三方：https://www.wescrm.com/siyuzhishiku/siyugongju/40722.html
- 认证费：1000 人以下每年 300 元（第三方来源，同上）。

## 给禽姐的建议（成本最低的合规路径）
1. **完成企业认证**（每年约 300 元），否则只能加 100 个客户，也开不了会话存档。需要你本人在管理后台提交认证资料，并在微信里扫码确认。
2. **AI 对话放在微信客服**：客户扫客服码后，由 AI 处理 PPT 需求的收集和交付，在 48 小时窗口内回复。
3. **外部群当服务群用**：真人员工当群主；开启官方关键词自动回复作为兜底；通知和 SOP 用客户群群发 API；需要 AI 回答时，在群里引导客户去微信客服。
4. 如果确实需要 AI 直接在群里回复：选 SCRM（比如句子互动），并书面确认对方走的是官方接口还是协议，同时评估会话存档的费用。
5. 不要把主力账号接到 iPad 协议或 PC Hook 上。
