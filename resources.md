# 资源库 —— 按「学到哪一步查什么」组织

> 不用一次读完。**卡在哪个 c,就翻对应那节。** 每条给一句「什么时候用得上」+ 一句白话 + 可查证来源。
> 课程代码本身零依赖这些资料——它们是给"想再往下挖一层"的你准备的。

---

## 🧭 贯穿全程

- **Anthropic《Building Effective Agents》** —— *什么时候查*:想知道我们这套"双层循环 + 工具"在业界叫什么(agent loop / augmented LLM)、什么时候该用 agent 什么时候不该。https://www.anthropic.com/engineering/building-effective-agents
- **learn-claude-code(工业级对照教程)** —— *什么时候查*:c0–c5 走完想看"同样思路做到工业级长什么样"(s01–s12)。https://learn.shareai.run/zh/ (本地:`../agent_projects/learn-claude-code/`)

## 📦 c0 时查:JSON 与结构化协议

- **JSON 基础** —— *什么时候查*:分不清 `{}`/`[]`/`""`、不知道"键值对"是什么时。五分钟能读完的官方语法图。https://www.json.org/json-zh.html
- **为什么结构化协议更可靠(白话)** —— 文本协议靠"猜格式切字符串",AI 一不守格式就悄悄切歪;JSON 有严格语法,解析器要么整段读懂、要么当场报错——错误从"悄悄发生"变成"立刻被抓住"。这就是 c0 的全部意义。
- **Anthropic tool_use(白话对照)** —— *什么时候查*:想知道真 CC 的协议长什么样。真 CC 不让模型"嘴上说 JSON",而是模型**原生返回**一个结构化的 tool_use 块,连"解析"这步都省了——我们手写 JSON,正是为了把这层看得见。https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview

## 🔧 c1 时查:工具设计原则

- **单一职责** —— 一个工具只干一件事(read_file 只读、write_file 只写):出错好定位、SYSTEM 里好描述、模型好选择。工具越"万能",模型越容易用错。
- **可审计** —— 每次调用都能打印"用了哪个工具、参数是什么、返回了什么"——bash 一把梭是黑盒,专用工具是留痕的。这是"能力 vs 安全"的平衡,你写自己的 agent 会反复遇到。
- **Anthropic《Writing Tools for Agents》** —— *什么时候查*:作业 A 设计 search 的参数和返回格式时。工具名、参数、返回怎么设计,模型才不会用错。https://www.anthropic.com/engineering/writing-tools-for-agents

## 📋 c2 时查:为什么计划要显式化

- **白话** —— 计划写进对话历史 = 模型每一轮都能"看见自己答应过什么",不靠转瞬即逝的"心里想";同时人也能盯着清单把关——计划可见,是"人在环"的第一步。
- **真 CC 的对应物** —— TodoWrite 之外还有 Plan Mode(先出完整方案、经你批准才动手)。*什么时候查*:想知道"计划显式化"做到头是什么样。https://docs.anthropic.com/en/docs/claude-code

## 🤝 c3 时查:上下文隔离与子代理

- **白话** —— 上下文是稀缺资源;探索的"过程"最占地方,但主线只需要"结论"。子 agent = 用一份**一次性**的上下文,换主线永远干净。
- **Anthropic《How we built our multi-agent research system》** —— *什么时候查*:作业 B 做审查员、或好奇"真·多 agent 系统怎么分工与汇报"时。https://www.anthropic.com/engineering/multi-agent-research-system

## 🗜 c4 时查:上下文窗口与压缩策略

- **上下文窗口(白话)** —— 模型一次能"看见"的最大文本量。超了装不下;而且越接近上限,模型越容易"糊"——这就是 Day1 讲的 context rot。
- **压缩的取舍** —— 摘要必然丢细节:丢掉"啰嗦"是收益,丢掉"关键约束"是事故。所以真 CC 的 compact 提示词精心设计了"必须保留什么"(任务目标、已做决定、未完成项)。想一想 c4 思考题,就是这个取舍。
- **Anthropic《Effective Context Engineering for AI Agents》** —— *什么时候查*:想系统了解"上下文该放什么、怎么省"时。https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents

## 🚦 c5 时查:Human-in-the-loop 安全思想

- **白话** —— 自动化程度越高,越需要在**不可逆动作**前留一个"人的检查点"。权限门不是不信任 AI,是承认任何执行者(包括人自己)都会犯错。
- **黑名单的局限** —— 关键词匹配挡得住 `rm `,挡不住变着花样写的 rm(c5 思考题!)。真 CC 用的是 allow/ask/deny 规则 + 沙箱的组合拳,不是黑名单。
- **Shneiderman 人本 AI 二维框架** —— *什么时候查*:想给"高自动化和高人类控制可以并存"找理论背书时。arXiv:2002.04087

---

## 🚀 课后深入:真 Claude Code 还有什么(每条一句白话)

- **token 级压缩** —— 我们按"消息条数"触发压缩,真 CC 按 token 精确计量,接近窗口上限自动 compact,且摘要提示词专门调过"保留什么"。→ https://docs.anthropic.com/en/docs/claude-code/costs
- **细粒度权限** —— 不止黑名单:allow / ask / deny 三档规则,能精确到"哪个工具 + 哪种参数模式"(比如允许 `git status` 但拦 `git push`)。→ https://docs.anthropic.com/en/docs/claude-code/iam
- **MCP(Model Context Protocol)** —— 让工具箱"即插即用":agent 按统一协议接上外部服务(数据库/浏览器/日历),工具不用每个都自己写。→ https://modelcontextprotocol.io/
- **hooks** —— 在 agent 动作前后挂你自己的脚本(比如"每次写完文件自动跑测试")——相当于把 c5 的权限门思想,推广成**可编程的关卡**。→ https://docs.anthropic.com/en/docs/claude-code/hooks
- **自定义子代理** —— 真 CC 里可以在 `.claude/agents/` 给子 agent 写人设文件——你作业 B 的"审查员",正是它的手写版。→ https://docs.anthropic.com/en/docs/claude-code/sub-agents

> 收尾一句:真 CC 的每个"高级功能",拆开都是你已经亲手造过的五根支柱之一——**造得出来,才算真懂**。

---
*MIT License｜郑先隽，北京师范大学心理学部教授，人本AI设计与创新*
