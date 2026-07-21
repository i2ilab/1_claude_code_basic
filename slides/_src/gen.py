# -*- coding: utf-8 -*-
"""1_claude_code_basic 模块导览 deck —— Fathom 数据叙事风 (Path A, html2pptx 原生可编辑).
画布 960x540px. 与 lecture/v2.0 数据叙事风、1_DEFINE_guide slides 同源。"""
import os

BG="#FFFFFF"; INK="#2B2B2B"; NAVY="#1A365D"; ACC="#C2410C"
GREEN="#2D7D46"; RED="#B03A2E"; GREY="#8A8A8A"; LINE="#E3E1DC"
PANEL="#F6F4EF"; NAVYT="#EAF0F6"
FCJK="'PingFang SC','Helvetica Neue',sans-serif"
FNUM="'Helvetica Neue','PingFang SC',Arial,sans-serif"
W,H=960,540; MX=56; CW=W-2*MX

def rect(x,y,w,h,fill=None,border=None,bw=1.5,radius=0):
    s=f"position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{h}px;box-sizing:border-box;"
    if fill:s+=f"background:{fill};"
    if border:s+=f"border:{bw}px solid {border};"
    if radius:s+=f"border-radius:{radius}px;"
    return f'<div style="{s}"></div>'
def hline(x,y,w,color=NAVY,h=2): return f'<div style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{h}px;background:{color};"></div>'
def vline(x,y,h,color=NAVY,w=2): return f'<div style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{h}px;background:{color};"></div>'
def txt(x,y,w,s,size=17,color=INK,weight=400,align="left",lh=1.35,tag="p",font=FCJK,ls="0px"):
    st=(f"position:absolute;left:{x}px;top:{y}px;width:{w}px;margin:0;padding:0;"
        f"font-family:{font};font-size:{size}px;color:{color};font-weight:{weight};"
        f"text-align:{align};line-height:{lh};letter-spacing:{ls};")
    return f'<{tag} style="{st}">{s}</{tag}>'
def bullets(x,y,w,items,size=15,color=INK,lh=1.6,gap=4):
    lis="".join(f'<li style="margin:0 0 {gap}px 0;padding:0;">{it}</li>' for it in items)
    st=(f"position:absolute;left:{x}px;top:{y}px;width:{w}px;margin:0;padding:0 0 0 18px;"
        f"font-family:{FCJK};font-size:{size}px;color:{color};line-height:{lh};list-style:disc;")
    return f'<ul style="{st}">{lis}</ul>'
def kicker(k): return txt(MX,38,CW,k.upper(),12,NAVY,700,ls="1.5px")
def title(t,y=60,size=32,color=INK): return txt(MX,y,CW,t,size,color,700,lh=1.18)
def rule(y,x=MX,w=54): return hline(x,y,w,ACC,3)
def foot(deck,page): return [txt(MX,512,460,deck,11,GREY,500),txt(W-140,512,84,f"{page:02d}",11,GREY,600,align="right",font=FNUM)]
def source(s,y=508,x=MX): return txt(x,y,CW,s,11,GREY,400,lh=1.3)
def page(bl):
    body=("<body style='margin:0;padding:0;width:960px;height:540px;position:relative;"
          f"background:{BG};overflow:hidden;'>"+"".join(bl)+"</body>")
    return ("<!doctype html><html><head><meta charset='utf-8'>"
            "<style>*{box-sizing:border-box;}p,h1,h2,h3,h4,ul,li{margin:0;}</style></head>"+body+"</html>")

def cards(items,y,h,accents=None,gap=18,top=18,bodysize=13):
    n=len(items); cw=(CW-gap*(n-1))//n; b=[]
    for i,(lab,tt,bd) in enumerate(items):
        x=MX+i*(cw+gap); acc=accents[i] if accents else NAVY
        b.append(rect(x,y,cw,h,fill="#FFFFFF",border=LINE,bw=1.4)); b.append(vline(x,y,h,acc,4))
        if lab: b.append(txt(x+16,y+top,cw-26,lab.upper(),11,acc,700,ls="1px"))
        b.append(txt(x+16,y+top+(20 if lab else 0),cw-26,tt,16,INK,700,lh=1.22))
        b.append(txt(x+16,y+top+(48 if lab else 26),cw-26,bd,bodysize,INK,400,lh=1.5))
    return b

FMONO="'Menlo','Courier New',monospace"
DECK="1_claude_code_basic · 亲手复现 mini Claude Code"; P=[]

def stagepage(pg,kick,tt,codelines,expl,cc,pain,note,emph=False):
    """c0–c5 阶段页模板:左=关键代码+讲解, 右=对照真CC/痛点场景, 底=思考题."""
    acc=ACC if emph else NAVY
    b=[kicker(kick),title(tt),rule(112)]
    b+=[rect(MX,178,516,232,fill=("#FBF1EC" if emph else "#FFFFFF"),border=(ACC if emph else LINE),bw=(1.8 if emph else 1.4)),
        vline(MX,178,232,acc,5),
        txt(MX+22,194,470,"关键代码",12,acc,700,ls="1px")]
    for i,cl in enumerate(codelines):
        b.append(txt(MX+22,220+i*21,474,cl,12.5,NAVY,600,font=FMONO,lh=1.3))
    b.append(bullets(MX+22,224+len(codelines)*21+8,468,expl,13.5,lh=1.6))
    x2=MX+532; wr=CW-532
    b+=[rect(x2,178,wr,110,fill=NAVYT,border=LINE,bw=1.2),
        txt(x2+16,192,wr-30,"🔗 对照真 Claude Code",12,NAVY,700,ls="1px"),
        txt(x2+16,216,wr-30,cc,12.5,INK,400,lh=1.5),
        rect(x2,300,wr,110,fill="#FBF1EC",border=LINE,bw=1.2),
        txt(x2+16,314,wr-30,"🔥 痛点场景(demo_project)",12,ACC,700,ls="1px"),
        txt(x2+16,338,wr-30,pain,12.5,INK,400,lh=1.5)]
    b.append(txt(MX,432,CW,note,13,GREY,500,lh=1.4))
    b+=foot(DECK,pg); return page(b)

# ── 01 封面 ──
P.append(page([
    rect(0,0,W,6,fill=NAVY),
    txt(MX,120,CW,"1_claude_code_basic",52,NAVY,800,font=FNUM,lh=1.0),
    rule(196,MX,72),
    txt(MX,216,CW,"亲手复现 mini Claude Code",34,INK,800,lh=1.2),
    txt(MX,278,CW,"c0 → c5 · 你每天在用的工具,亲手造出雏形",18,GREY,500),
    txt(MX,340,CW,"TOOLBOX · PLAN · SUBAGENT · COMPACT · GUARD",12,NAVY,700,ls="2px"),
    txt(MX,470,CW,"《AI智能体在心理与教育的应用》· 北京师范大学心理学部",13,GREY,400),
]))
# ── 02 定位 ──
b=[kicker("定位 · FROM TOY TO HARNESS"),title("Harness 的五根支柱,就是真 Claude Code 的骨架"),rule(112)]
b+=[rect(MX,178,(CW-24)//2,232,fill=PANEL,border=LINE,bw=1.4),
    txt(MX+20,196,360,"起点 · s3:能跑的玩具",15,GREY,800),
    bullets(MX+20,230,(CW-24)//2-44,["30 行:双层循环 + 文本协议 + os.popen","会说也会做——但一碰真实项目就露怯","协议太脆、工具太少、没计划没安全"],14,lh=1.7)]
x2=MX+(CW-24)//2+24
b+=[rect(x2,178,(CW-24)//2,232,fill="#FBF1EC",border=ACC,bw=1.8),
    txt(x2+20,196,360,"终点 · c5:工业品雏形",15,ACC,800),
    bullets(x2+20,230,(CW-24)//2-44,["每步只加一个想法:协议→工具箱→计划→子 agent→压缩→权限门","~35 行,五根支柱齐备","每一步都对得上真 CC 的一个功能"],14,lh=1.7)]
b.append(txt(MX,428,CW,"上个模块你造出了「行为」;这个模块,把它长成一套框架——五步,从玩具到工业品。",13,GREY,500))
b+=foot(DECK,2); P.append(page(b))
# ── 03 出发点:引号灾难 ──
b=[kicker("出发点 · WHY UPGRADE"),title("命令里一出现引号,s3 的协议就切崩了"),rule(112)]
b+=[rect(MX,178,516,232,fill="#FBECEA",border=RED,bw=1.6),vline(MX,178,232,RED,5),
    txt(MX+22,194,470,"引号灾难现场",12,RED,700,ls="1px"),
    txt(MX+22,220,474,'你:写一个 hello.py,内容是 print("你好, world")',12.5,INK,600,font=FMONO),
    txt(MX+22,246,474,'reply.split("命令:")[1]   # 引号/冒号/换行混进来',12.5,NAVY,600,font=FMONO),
    txt(MX+22,272,474,"→ IndexError,程序当场死掉",12.5,RED,700,font=FMONO),
    bullets(MX+22,308,468,["靠切字符串猜意图,AI 一不守格式就崩","内容和指令搅在一起,没法区分「做什么」和「写什么」"],13.5,lh=1.6)]
x2=MX+532
b+=[rect(x2,178,CW-532,232,fill=NAVYT,border=LINE,bw=1.2),
    txt(x2+18,196,CW-532-36,"s3 的两个软肋",12,NAVY,700,ls="1px"),
    txt(x2+18,224,CW-532-36,"协议太脆",15,NAVY,800),
    txt(x2+18,248,CW-532-36,"split(\"命令:\") 切字符串,一不守格式就 IndexError",12,GREY,500,lh=1.4),
    txt(x2+18,300,CW-532-36,"工具太少",15,NAVY,800),
    txt(x2+18,324,CW-532-36,"只有一个 os.popen:没有分工、没有计划、没有安全约束",12,GREY,500,lh=1.4)]
b.append(txt(MX,432,CW,"真 Claude Code 强在哪?就强在把这两点做扎实了——协议健壮性是第一课。",13,GREY,500))
b+=foot(DECK,3); P.append(page(b))
# ── 04 c0 JSON 协议 ──
P.append(stagepage(4,"C0 · JSON 协议","让机器听得懂机器:从「切字符串」到「读字段」",
    ['AI 回复: {"tool":"bash","args":{"cmd":"ls"}}','action = json.loads(reply)','cmd = action["args"]["cmd"]'],
    ["「做什么」和「内容」用 {} 分得清清楚楚","再也不用数「命令:」在第几个字符;双层循环一字没变,变的只有协议"],
    "tool_use 结构化工具调用——模型直接返回结构化调用,我们手写的 JSON 就是它的极简版。",
    "写一个带引号、冒号、换行的 hello.py——s3 切歪,c0 稳稳落地。",
    "思考题:为什么结构化 JSON 能避免 s3 的切割歧义?"))
# ── 05 c1 工具箱 ──
P.append(stagepage(5,"C1 · 工具箱","不止一把锤子:专用工具更可控、可审计",
    ['TOOLS = {"read_file": read_file,','         "write_file": write_file, "bash": bash}','result = TOOLS[name](**args)   # 按名字派发'],
    ["AI 说用哪个工具,代码就调哪个——dispatch","parse() 剥掉 ```json 包裹;坏格式 try/except 请模型重发,不再崩"],
    "Read / Write / Bash 专用工具:限制路径、记录每次读写、避开 shell 转义地狱。",
    "改 TODO.md 的一行:sed 要跟转义搏斗;read → 想清楚 → write,干净可控。",
    "思考题:改用 bash 的 sed 改一行,遇到特殊符号会出什么岔子?"))
# ── 06 c2 计划是工具 ──
P.append(stagepage(6,"C2 · 计划是工具","TodoWrite:把「思考过程」变得可见",
    ['def todo_write(items):   # 也只是一个普通工具','    ...打印 ☐ / ☑ 清单','系统提示:接到多步任务,先列计划、边做边勾'],
    ["todo_write 不执行命令,只更新并打印一张清单","计划可见,人就能盯着它别跑偏——这也是「人在环」的一部分"],
    "TodoWrite——你见过的那张待办清单:让模型把计划写进一个能反复更新的工具。",
    "给 notes_app 加 export 命令:读 cli.py、改代码、再测试——没计划就容易漏掉「测试」。",
    "思考题:不让它先列计划,你猜它最容易漏掉哪一步?"))
# ── 07 c3 子智能体 ──
P.append(stagepage(7,"C3 · 子智能体","把脏活外包出去,只拿回结论",
    ['def subagent(task):','    msgs = [...]   # 全新的一份 messages','    ...跑自己的循环,最后只 return 一句结论'],
    ["长任务最大的敌人是「上下文越来越脏」","像让室友去查 100 篇论文,他只把结论发你,不把论文全塞你脑子"],
    "Task 子 agent——「探索这个代码库」时派出去翻文件,主对话不被文件内容淹没。",
    "读懂整个 demo_project 架构:几十屏代码塞爆主对话 vs 一段总结带回来。",
    "思考题:子 agent 返回全部文件内容还是一段总结?为什么后者对长任务这么关键?"))
# ── 08 c4 上下文压缩 ──
P.append(stagepage(8,"C4 · 上下文压缩","记不下,就做笔记:历史折叠成一条摘要",
    ['if len(messages) > LIMIT:','    messages = compact(messages)','# 模型给自己写摘要,[系统提示+摘要] 当新起点'],
    ["旧的一大堆细节被折叠掉,关键进展留下来","真 CC 按 token 数触发,我们简化成消息条数——原理一样"],
    "/compact 与自动压缩——长会话把历史折叠成摘要重开窗口,context rot 的解药。",
    "排查 stats 的 bug 来回二十轮:不压缩,迟早撑爆窗口、越来越慢越来越贵。",
    "思考题:压缩后它还记得任务目标吗?如果摘要漏了个关键细节会怎样?"))
# ── 09 c5 权限门 ──
P.append(stagepage(9,"C5 · 权限门","危险动作,先问人:Human-in-the-loop",
    ['DANGER = ["rm ", "sudo", "mv ", ...]  # 黑名单','if any(d in cmd for d in DANGER):','    input("允许吗?(y/n) ")   # 人说 n 就不执行'],
    ["命中危险词 → 停下来征求人的同意","拒绝后把「用户拒绝了」告诉 AI——它得学会接受 no"],
    "危险操作确认弹窗——rm、改关键文件、跑未知脚本前,先问你要不要允许。",
    "「清理临时文件」听着无害,agent 却可能生成 rm——没有门,它手一滑就删了。",
    "思考题:黑名单靠关键词匹配,rm 能不能被写成绕过检查的样子?",emph=True))
# ── 10 五支柱合影 ──
b=[kicker("合影 · FIVE PILLARS"),title("~35 行,五根支柱齐了"),rule(108)]
b+=[txt(MX+54,140,340,"你的 mini CC",12,NAVY,700,ls="1px"),
    txt(505,140,399,"真 Claude Code",12,ACC,700,ls="1px")]
rows=[("c0","JSON 协议:json.loads 读字段","tool_use 结构化工具调用"),
      ("c1","TOOLS 字典按名派发 + 坏格式重发","Read / Write / Bash 专用工具"),
      ("c2","todo_write 打印 ☐☑ 清单","TodoWrite:计划可见"),
      ("c3","subagent() 全新 messages,只回结论","Task 子 agent"),
      ("c4","compact() 把历史折叠成摘要","/compact · 自动压缩"),
      ("c5","DANGER 黑名单 + input() 问 y/n","权限确认弹窗")]
for i,(cid,mine,real) in enumerate(rows):
    y=166+i*44
    if i%2==0: b.append(rect(MX,y,CW,44,fill=PANEL))
    b.append(txt(MX+10,y+11,40,cid,15,NAVY,800,font=FNUM))
    b.append(txt(MX+54,y+13,368,mine,13,INK,500))
    b.append(txt(432,y+11,60,"←→",14,GREY,600,align="center",font=FNUM))
    b.append(txt(505,y+13,399,real,13,INK,600))
b.append(txt(MX,446,CW,"差别只有一个:真 CC 用模型原生 tool_use(更稳),我们手写 JSON(看得见每一个字节)。机制完全一样。",13,GREY,500))
b+=foot(DECK,10); P.append(page(b))
# ── 11 demo_project ──
b=[kicker("练习靶子 · DEMO_PROJECT"),title("一个麻雀虽小的真项目,和一个等你来修的 bug"),rule(112)]
b+=cards([("NOTES_APP","玩具笔记 CLI","多文件互相调用 + README + TODO——像一个真实的小项目"),
          ("预埋 BUG","stats 一跑就崩","空标签触发 IndexError——故意藏好的,等你带着 agent 来修"),
          ("同一个靶子","人人一致、可复现","c0–c5 的复杂例子和全部作业,都在它上面跑")],
         178,196,accents=[NAVY,RED,NAVY])
b.append(txt(MX,404,CW,"工具箱/计划/子 agent/压缩/权限——简单任务用不上,一到真实项目就离不开。这就是给你一个「假项目」的原因。",13,GREY,500,lh=1.4))
b+=foot(DECK,11); P.append(page(b))
# ── 12 capstone ──
b=[kicker("CAPSTONE · 端到端"),title("用你自己的 mini CC,真的修好那个 bug"),rule(112)]
steps=[("① 复现","让它跑一次 stats,亲眼看到报错"),("② 定位","让它读 analyze.py,找到出事的那行"),
       ("③ 修复","让它说出「为什么会崩」,再动手改"),("④ 验证","再跑 stats,确认通过")]
cw=(CW-3*14)//4
for i,(t,d) in enumerate(steps):
    x=MX+i*(cw+14); y=178
    b.append(rect(x,y,cw,150,fill="#FFFFFF",border=LINE,bw=1.4))
    b.append(txt(x+14,y+16,cw-24,t,16,NAVY,800))
    b.append(hline(x+14,y+48,cw-28,LINE,1))
    b.append(txt(x+14,y+62,cw-24,d,12.5,INK,400,lh=1.5))
    if i<3: b.append(txt(x+cw-2,y+64,16,"→",18,ACC,800))
b.append(txt(MX,356,CW,"「指挥 agent 调试,而不是自己调试」——全程你只把关、不代劳。这正是你以后用真 Claude Code 修 bug 的姿势。",13,GREY,500))
b.append(txt(MX,384,CW,"做了选项 B 的审查员?先让审查员子 agent 定位,再让主 agent 修——这就是多 agent 协作。",13,GREY,500))
b+=foot(DECK,12); P.append(page(b))
# ── 13 作业2 三选一 ──
b=[kicker("作业 2 · HOMEWORK"),title("三选一:给你的 mini CC 加一块骨头"),rule(112)]
b+=cards([("A · 改 C1","加一件「搜索」工具","真实开发最高频的动作:按关键词在项目里搜文件——加进 TOOLS,教 AI 什么时候用"),
          ("B · 改 C3","审查员子代理","给子 agent 装「代码审查员」人设——真 CC 的 code-review 子 agent 就是这么来的"),
          ("C · 防崩加固","堵住 c1 还没堵的洞","坏 JSON、越界路径、死循环……让它在恶意输入下也不崩")],
         178,200,accents=[NAVY,ACC,NAVY])
b.append(txt(MX,408,CW,"以 c1 / c3 / c5 为基础改,每个改动都要能单独跑通;capstone 修 bug 是加分挑战。",13,GREY,500))
b+=foot(DECK,13); P.append(page(b))
# ── 14 AI 教练 ──
b=[kicker("AI 教练 · COACH SKILLS"),title("三个教练带着走:陪跑,不代写"),rule(112)]
b+=cards([("/HARNESS-TUTOR","概念陪跑","c0–c5 一个阶段一个阶段问你「讲给我听」——讲不出=没真懂"),
          ("/HARNESS-HW2","作业陪跑","三级提示一层层翻,只指路;答案代码一行都不给"),
          ("/HARNESS-DEBUG","调试陪跑","陪你修 capstone 的 bug——绝不剧透 bug 位置,只教你怎么找")],
         178,190,accents=[NAVY,ACC,NAVY])
b.append(txt(MX,398,CW,"三条路径可混用:网页版 web/index.html 可视化 · 教程 + 逐个跑 c0–c5(先 diff 再跑)· 让教练带着走。",13,GREY,500))
b+=foot(DECK,14); P.append(page(b))
# ── 15 i2i Academy ──
b=[kicker("平台 · I2I ACADEMY"),title("浏览器里零安装,c0 → c5 可跑可判题"),rule(112)]
b.append(txt(MX,124,CW,"课程原版 .py 逐字节不改,在浏览器 Pyodide 里直接跑——本地环境没配好,也不耽误造你的 mini CC。",14,GREY,500))
b+=cards([("零安装","编辑器 + 终端直跑","input()、同步 chat.send()、停止按钮原样工作"),
          ("判题门禁","自动判题,过关解锁","mock 模式按脚本回复,零 token 判题;real 连真模型"),
          ("C5 实测","权限门真的弹 y/n","浏览器里输入 n,命令就是不执行——亲手感受人在环")],
         196,186,accents=[NAVY,ACC,NAVY])
b.append(txt(MX,400,CW,"平台内容直读课程仓库构建(hash 锁),与你手里的代码永不漂移。",13,GREY,500))
b+=foot(DECK,15); P.append(page(b))
# ── 16 与真 CC 的差距 ──
b=[kicker("课后深入 · MIND THE GAP"),title("五根支柱齐了,但真 CC 还有这些"),rule(112)]
b+=cards([("压缩","token 级触发","真 CC 按 token 精确计量并保留关键上下文;我们只数消息条数"),
          ("权限","细粒度规则","allowlist / 分级确认 / 会话记忆,远不止一个黑名单"),
          ("MCP","外部工具生态","用协议接数据库、浏览器、第三方服务——工具箱可无限扩展"),
          ("HOOKS","关键节点挂自动化","工具调用前后自动跑检查/格式化——框架长出「反射」")],
         178,208,accents=[NAVY,NAVY,ACC,NAVY],bodysize=12.5)
b.append(txt(MX,416,CW,"想读工业级实现:learn-claude-code(s01–s12)——我们的 c0–c5 正是它的「最小可理解版」。",13,GREY,500))
b+=foot(DECK,16); P.append(page(b))
# ── 17 模块地图 ──
b=[kicker("模块地图 · WHERE NEXT"),title("这套 harness,是 Build & Ship 后端的地基"),rule(112)]
mods=[("0","造行为","0_agent_basic:s0–s7,亲手造出会干活的 agent",False),
      ("1","造框架","1_claude_code_basic:c0–c5,复现 mini Claude Code",True),
      ("2","定义与评估","DEFINE 双支柱:想清楚造什么、凭什么说它行",False),
      ("3","上线","Build & Ship:你的 agent 包成后端 API,部署上公网",False)]
cw=(CW-3*14)//4
for i,(num,name,desc,em) in enumerate(mods):
    x=MX+i*(cw+14); y=178
    b.append(rect(x,y,cw,150,fill=("#FBF1EC" if em else "#FFFFFF"),border=(ACC if em else LINE),bw=(2 if em else 1.4)))
    b.append(txt(x+14,y+14,cw-24,num,26,(ACC if em else NAVY),800,font=FNUM))
    b.append(txt(x+14,y+52,cw-24,name,15,INK,700))
    b.append(txt(x+14,y+78,cw-26,desc,11.5,GREY if not em else INK,400,lh=1.45))
    if i<3: b.append(txt(x+cw-3,y+58,18,"→",18,ACC,800))
b.append(txt(MX,356,CW,"上线那天,你的后端跑的就是今天这套 harness;c3 的子 agent,会变成上线后的安全复核层。",13,GREY,500))
b+=foot(DECK,17); P.append(page(b))
# ── 18 c5 的哲学 ──
P.append(page([rect(0,0,W,H,fill=NAVY),
    txt(MX,130,CW,"C5 的哲学 · HUMAN-IN-THE-LOOP",14,"#8FB0CC",800,ls="3px",font=FNUM),rule(176,MX,72),
    txt(MX,208,CW-40,"自主性越强,",40,"#FFFFFF",800,lh=1.25),
    txt(MX,266,CW-40,"越需要人握着最后的开关。",40,"#FFFFFF",800,lh=1.25),
    txt(MX,352,CW-60,"agent 可以自己规划、自己派子 agent、自己压缩记忆——但 rm 之前,要先问你一声。",16,"#C6D6E6",500,lh=1.6),
    txt(MX,470,CW,"在心理与教育场景,这不是技术选择,是伦理责任。",13,"#8FB0CC",400)]))
# ── 19 结课 ──
P.append(page([rect(0,0,W,6,fill=NAVY),
    txt(MX,130,CW,"带走一句话",13,NAVY,700,ls="2px"),rule(166,MX,72),
    txt(MX,196,CW-40,"「你每天在用的 Claude Code,",34,INK,800,lh=1.35),
    txt(MX,252,CW-40,"你已经知道它为什么这样设计。」",34,ACC,800,lh=1.35),
    txt(MX,330,CW-40,"工具箱 · 计划 · 子 agent · 压缩 · 权限——五根支柱,~35 行,你全亲手写过。",17,GREY,600,lh=1.5),
    txt(MX,392,CW,"下一站:用 DEFINE 想清楚造什么,再让这套 harness 载着你的 agent 上线。",15,GREY,500),
    txt(MX,470,CW,"郑先隽 · 北京师范大学心理学部 · 人本 AI 设计与创新",13,GREY,400)]))

HERE=os.path.dirname(os.path.abspath(__file__))
d=os.path.join(HERE,"html"); os.makedirs(d,exist_ok=True)
for i,html in enumerate(P,1):
    open(os.path.join(d,f"{i:02d}.html"),"w",encoding="utf-8").write(html)
print(f"{len(P)} pages")
