# 愿灵感在路上，也在你放松的那一刻。
**日期**：2026-11-08 · AI 动态
**更新**：2026-11-08 17:12 北京时间

1. **NaceAI 发布 Drex 决策模型家族**
   Drex 含 4 个开源决策模型，直接为选项分配概率；Drex Max 耗时 183ms，并支持最多 255 个选项。
   [@theturingpost](https://x.com/TheTuringPost/status/2119245755731124487)

2. **内蒙古 Stargate 园区建设进展披露**
   SemiAnalysis 实地探访称该风电驱动的 800MW 园区一年内建成 120MW，并采用 5MW 直流与无中央冷水机冷却设计。
   [@semianalysis_](https://x.com/SemiAnalysis_/status/2119162511203131591) · [原文](https://newsletter.semianalysis.com/p/we-visited-chinas-stargate-in-inner)

3. **Xiaomi MiMo 转向稀疏因果编码器**
   MiMo 下一代模型拟让提示仅经过 49 层中的 25 层，厂商称 100 万上下文下预填充计算量和 KV 缓存分别降至 1/5、约 1/4.5。
   [@semianalysis_](https://x.com/SemiAnalysis_/status/2119142144749293863)

4. **Inkling 2 Small 限时免费开放**
   Inkling 2 Small 可在 OpenCode 上限时免费使用，厂商表示此举用于收集反馈并改进模型。
   [@soumithchintala](https://x.com/soumithchintala/status/2119086689201316272) · [原文](https://opencode.ai/data/thinkingmachines/inkling-2-small)

<details>
<summary>还有精力？再看 3 条</summary>

1. **LeHami 用 Hamiltonian 机制改进 JEPA**
   LeHami 将 Hamiltonian 力学引入 JEPA，通过学习能量函数和辛 leapfrog 积分器维持长期预测中的相空间体积。
   [@theturingpost](https://x.com/TheTuringPost/status/2119063055107784753) · [原文](https://www.turingpost.com/p/lehami-explained-can-physics-help-world-models-predict-motion)

2. **GitHub 为智能体时代重构平台**
   GitHub 正面向智能体工作流进行全栈重构，平台拥有 2.25 亿开发者和一年 343 亿次提交。
   [@swyx](https://x.com/swyx/status/2119244488925446620) · [演示](https://youtu.be/rSWiNE92xqM) · [原文](https://ai.engineer/code)

3. **开源模型转向精简代码检查**
   PatronusAI 称，多款开放模型如今会直接用“Need inspect repo. Grep.”表达检查意图，较少再输出冗长的仓库探索过程。
   [@thesephist](https://x.com/thesephist/status/2119194290358464911)

</details>

---

## 完整推文 · 42 条

抓取范围：最近 24 小时；来源按账号分组。

## 🏢 公司发布（8条）

### @semianalysis_ | Infra

- We Visited China’s Stargate in Inner Mongolia  A wind-powered 800MW campus,  120MW built within a year,  a 5MW SST-native 800V DC pilot and a cooling design without central chillers   https://t.co/t1CnGzAVgG
  [查看](https://x.com/SemiAnalysis_/status/2119162511203131591)
- After DeepSeek V4.1 Flash, Xiaomi MiMo is moving to a causal encoder-decoder for its next-gen models.  HySparse2: prompts run through only 25 of 49 layers. Decoder KV is projected from encoder states.  At 1M context vs MiMo-V2: 5x less prefill compute, 4.5x smaller KV cache. https://t.co/ZVxZ4FDCDx
  [查看](https://x.com/SemiAnalysis_/status/2119142144749293863)

### @theturingpost | Research

- RT @TheTuringPost: Speaking of decision models, one interesting family just came out - Drex by @NaceAI.  This family includes 4 open-source…
  [查看](https://x.com/TheTuringPost/status/2119291492871413795)
- Speaking of decision models, one interesting family just came out - Drex by @NaceAI.  This family includes 4 open-source decision models, each of which skips text generation altogether and directly assigns probabilities to the available options.  Drex explores 4 different ways to do this:  1. Three smaller models use a pointer architecture:  It consists of a pretrained LM + a small head that compa...
  [查看](https://x.com/TheTuringPost/status/2119245755731124487)
- RT @TheTuringPost: There's one great example that shows how physics can help upgrade AI world models, and it's LeHami.  @ylecun, @randall_b…
  [查看](https://x.com/TheTuringPost/status/2119200794071503269)
- There's one great example that shows how physics can help upgrade AI world models, and it's LeHami.  @ylecun, @randall_balestr and @RominaYalov brought Hamiltonian mechanics into JEPA to preserve phase-space volume and prevent latent collapse during long-term predictions.  Why exactly Hamiltonian mechanics?  • Variables are coordinates q and momenta p (not velocities like in Lagrangian mechanics),...
  [查看](https://x.com/TheTuringPost/status/2119063055107784753)
- RT @TheTuringPost: A free, 24-hour online conference – "Engineering better intelligence" by @neo4j  It's a great opportunity to learn the m…
  [查看](https://x.com/TheTuringPost/status/2119020616074535081)
- RT @TheTuringPost: Open-source AI stack from DeepSeek for building your own agent:  ▪️ DeepSeek Harness (dsh): Connects a model to tools an…
  [查看](https://x.com/TheTuringPost/status/2119020574743666980)

## 👤 研究者动态（34条）

### @alexolegimas [Google DeepMind] | Research

- RT @PeterStone_TX: The School of Computing at UT Austin will be hiring aggressively, aiming for 50 new tenure-track faculty over the next 5…
  [查看](https://x.com/alexolegimas/status/2119259061065531679)
- RT @Jason: Wake up babe, new @bobdylan dropped https://t.co/490VWpM0xY
  [查看](https://x.com/alexolegimas/status/2119228131076919377)
- RT @sebkrier: Updated version! https://t.co/st0ZYOiRS9
  [查看](https://x.com/alexolegimas/status/2119223786666865029)
- RT @skominers: Where else can you work on "AI and machine learning, agentic commerce, cryptography, security, distributed computing, hardwa…
  [查看](https://x.com/alexolegimas/status/2119158290689241568)
- RT @RuxandraTeslo: Bryan Caplan is, after all, a spiritual slave.   But this is not such an uncommon view. Born out of excessive scientism…
  [查看](https://x.com/alexolegimas/status/2119116837401104621)
- RT @MarkusEconomist: Chris Sims Alumni Conference at @PrincetonEcon with Tom Sargent as keynote. https://t.co/TULwtdMTom
  [查看](https://x.com/alexolegimas/status/2119102794351235283)
- RT @AchimWar: @alexolegimas Amusing to me that the extreme point of libertarianism is you believe in a central planner
  [查看](https://x.com/alexolegimas/status/2119102077376827475)
- Literally this https://t.co/mzv612GjHT
  [查看](https://x.com/alexolegimas/status/2119097196423647541)
- This is really worth emphasizing: you can get incredible increases in welfare but the GDP growth numbers would barely move. Economics of how automation translates into aggregate statistics can be non obvious and counterintuitive.
  [查看](https://x.com/alexolegimas/status/2119093019727085720)
- RT @danielrock: Hell yeah @alexolegimas on MTS
  [查看](https://x.com/alexolegimas/status/2119092052151431349)

### @denny_zhou [Google DeepMind] | Model

- RT @unclebobmartin: I used to be a language lawyer.  In the late 80s I _studied_ the ARM (Annotated Reference Manual for C++).  I knew the…
  [查看](https://x.com/denny_zhou/status/2119088602856759795)

### @karpathy [independent] | Research

- Earlier this week Tristan published his top YouTube channels: https://t.co/NZ3UCNo6cT Which looked excellent so clearly I had to turn it into TristanTube: https://t.co/l0KyW1WdNH 47K super nerdy videos +TV mode for laid back watching. (One-shotted with Claude Code in 3 minutes)
  [查看](https://x.com/karpathy/status/2119114537442189652)

### @neelnanda5 [Google DeepMind] | Research

- I gave a talk for the Oxford AI Safety Society, and they got me by far the best gift I've received for giving a talk: a custom made jigsaw puzzle of Oxford + a cute shoggoth! 10/10 I'm very impressed, good market research https://t.co/yEpNyIlsT8
  [查看](https://x.com/NeelNanda5/status/2119249576842706953)

### @soumithchintala [Meta] | Research

- RT @tinkerapi: It’s encouraging to see how much tinker accelerated @msuiche- he’d previously burned 4600$ in gpu rental without finishing a…
  [查看](https://x.com/soumithchintala/status/2119243022520996314)
- Inkling 2 Small on OpenCode for free for a limited time, to help us improve our models further: https://t.co/x5ihVRYBn1
  [查看](https://x.com/soumithchintala/status/2119086689201316272)

### @steipete [OpenClaw] | Application

- The Asahi project was all about taking something closed and restricted and opening it up.  Adding new restrictions that make it harder for other projects to build on that is not the way. And that AI rejection is just silly. https://t.co/fT4O4wieQm
  [查看](https://x.com/steipete/status/2119264334627090514)
- RT @awesomekling: “we were made aware of multiple attempts to exploit our permissive licensing to hijack our work”  what did y’all think pe…
  [查看](https://x.com/steipete/status/2119222845243109400)
- RT @i0n1c: People keep asking me how GPT-6 cyber is better. Well let’s say previous models would take project zero postings and then try to…
  [查看](https://x.com/steipete/status/2119185811929530408)
- RT @owenthcarey: Me explaining how my app works after vibe coding the entire thing. https://t.co/JOGVuUGmdC
  [查看](https://x.com/steipete/status/2119183196155945203)
- RT @PrakashM14: I'm increasingly bearish on Reflection.  This is what happens when you import Google's engineering bureaucracy into an earl…
  [查看](https://x.com/steipete/status/2119177578410123513)
- RT @thomasmc: Life hack if your flight doesn't have Starlink: ask your agent to bypass the 443 split-TCP proxy via a $0.03/h BBR multiplexe…
  [查看](https://x.com/steipete/status/2119163785680445921)
- RT @codycollier: 88x31.gif https://t.co/comAGCsAz6
  [查看](https://x.com/steipete/status/2119156572597502238)
- RT @signulll: i grew up playing simcity (one of my favorite games of all time), &amp; if you told me i could zone land for data centers which r…
  [查看](https://x.com/steipete/status/2119147572447297622)

### @swyx [AI社区] | App

- RT @latentspacepod: How GitHub is rebuilding for Agents  225M developers. 34.3B commits in a year. @github’s agent era is a full-stack rebu…
  [查看](https://x.com/swyx/status/2119244488925446620)
- sticker game inspired by @dexhorthy @CompleteSkeptic et al https://t.co/NWvVRZ71uW
  [查看](https://x.com/swyx/status/2119242830707311005)
- just arrived… best swag game in the business. u guys are in for a treat next week https://t.co/4tppCNnBWf
  [查看](https://x.com/swyx/status/2119210582654210255)
- RT @jose_goncalves_: Da Vinci’s to-do list btw https://t.co/wh1GurRHss
  [查看](https://x.com/swyx/status/2119164911121314270)
- RT @JenniferHli: I can watch this show ALL DAY.
  [查看](https://x.com/swyx/status/2119162248610644207)
- Local AI is back on the menu!  incredibly hyped for @TheAhmadOsman's return to AIE CODE next week. follow him for some exclusive discount code drops
  [查看](https://x.com/swyx/status/2119140818690974203)
- just got my test order and was delightfully surprised to find that this client is open source!!!! (v impt for sticking anything in a physical port)  very delighted to have a use for this useless SD Card slot and the api is so nice and agent friendly. watch for surprises at @aiDotEngineer ...
  [查看](https://x.com/swyx/status/2118996445936361933)

### @thesephist [Anthropic] | Research

- RT @rough__sea: talking to a coding agent is more like email than irc - because the interactions are few and far between, I often finding m…
  [查看](https://x.com/thesephist/status/2119335073975791842)
- RT @PatronusAI: “Need inspect repo. Grep.”  Last year open models said “Let me start by exploring the repository.” Now several write exclus…
  [查看](https://x.com/thesephist/status/2119194290358464911)
- RT @nbhdlady: I like text but I don’t think I like text *that* much
  [查看](https://x.com/thesephist/status/2119194224507924781)

### @ylecun [NYU] | Research

- RT @ylecun: @gabriberton Several comments: 1. image/video SSL methods differ by whether they use reconstruction or not. Joint embedding arc…
  [查看](https://x.com/ylecun/status/2119143975739142269)
