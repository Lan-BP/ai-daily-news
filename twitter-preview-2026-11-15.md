# 愿你带着轻松的心情，遇见今天的新鲜事。
**日期**：2026-11-15 · AI 动态
**更新**：2026-11-15 06:51 北京时间

1. **Perplexity 更新 Decider 决策模型**
   Perplexity 发布 Decider v1.3 与 Flash v1.3，支持256K上下文、文本和图像输入，并已进入决策能力与成本前沿。
   [@artificialanlys](https://x.com/ArtificialAnlys/status/2121595922090230033)

2. **SubQ Snap 1.2 提升决策稳定性**
   Subquadratic 发布 SubQ Snap 1.2，决策指数升至73，支持384K上下文，并以更少弃答提高非幻觉率。
   [@artificialanlys](https://x.com/ArtificialAnlys/status/2121396191024071088)

3. **NVIDIA 大客户的自研芯片冲击**
   SemiAnalysis 称 NVIDIA 七大自然客户中有六家自研芯片，Google 的 TPU 被其评测认为已可与 NVIDIA 相比。
   [@semianalysis_](https://x.com/SemiAnalysis_/status/2121725048402681946)

4. **Meta 发布 e-means 聚类算法**
   Meta 与 École Nationale des Ponts et Chaussées 提出 e-means，以十分之一训练轮数提升聚类精度，并带来10至45倍GPU加速。
   [@theturingpost](https://x.com/TheTuringPost/status/2121725370135450083)

<details>
<summary>还有精力？再看 3 条</summary>

1. **编码智能体指数升级后 Claude 并列领先**
   Artificial Analysis 升级编码智能体指数后，Claude Fable 5.2 与 Claude Opus 5.5 均以58分并列领先。
   [@artificialanlys](https://x.com/ArtificialAnlys/status/2121393821955334328)

2. **vLLM 优化 DeepSeek-V4.1-Flash**
   vLLM 团队称其在 Vera Rubin NVL72 上优化 DeepSeek-V4.1-Flash，吞吐量达到 GB300 NVL72 的58倍。
   [@vllm_project](https://x.com/vllm_project/status/2121387736338944475)

3. **研究衡量工作非金钱价值**
   Google DeepMind 研究显示，多数人从工作获得显著非金钱价值，各收入群体均如此，但国家间差异明显。
   [@alexolegimas](https://x.com/alexolegimas/status/2121605533295595546)

</details>

---

## 完整推文 · 42 条

抓取范围：最近 24 小时；来源按账号分组。

## 🏢 公司发布（13条）

### @artificialanlys | Model

- Decider v1.3 and Decider Flash v1.3 from Perplexity score 70 and 64, respectively, on the Artificial Analysis Decision Index v2.1  @perplexity_ai has released Decider v1.3 and Decider Flash v1.3, updating their v1.2 flagship decision models. Compared to v1.2, Decider v1.3 maintains its #6 position while Decider Flash v1.3 moves up into the #10 position.  Key results:  ➤ Decider v1.3 has strong dec...
  [查看](https://x.com/ArtificialAnlys/status/2121595922090230033)
- Subquadratic’s SubQ Snap 1.2 gains 5 points over SubQ Snap 1.1 on the Artificial Analysis Decision Index v2.1, and is tied with Drex Max v1.1 and GLiDE v1.2 as the leading decision model  SubQ Snap 1.2 is the latest decision model from @subquadratic. Pricing is unchanged at $0.04 per 1M input tokens, and it supports a 384K token context window.  Decision Index v2.1 updates AA-Symmetry to v1.1. AA-...
  [查看](https://x.com/ArtificialAnlys/status/2121396191024071088)
- Announcing Artificial Analysis Coding Agent Index v2.1, upgrading FrontierCode and Terminal-Bench. Claude Fable 5.2 and Claude Opus 5.5 share the lead at 58  The Coding Agent Index measures models in agent harnesses; v2.1 of the Index upgrades FrontierCode from 1.1 to 2.0 and Terminal-Bench from 4.0 to 4.1.  Upgraded:  ➤ FrontierCode-AA 2.0 (replacing FrontierCode v1.1): our implementation of Cogn...
  [查看](https://x.com/ArtificialAnlys/status/2121393821955334328)

### @semianalysis_ | Infra

- Six of Nvidia’s seven biggest customers are building their own chips.  “NVIDIA’s seven biggest customers account for the vast majority of GPUs being deployed: Google, Microsoft, Meta, Amazon, SpaceX, Anthropic and OpenAI. All of them, except SpaceX, are making their own chips.”  “If NVIDIA didn’t prop up CoreWeave and the other neoclouds, those industries just would not exist, and the hyperscalers...
  [查看](https://x.com/SemiAnalysis_/status/2121725048402681946)
- https://t.co/FDfRFeDh9G https://t.co/rP4BwFTuqN
  [查看](https://x.com/SemiAnalysis_/status/2121636060715192685)
- “Jensen has been incredibly good at retaining talent. There are very few high-profile departures from the NVIDIA executive team.” “This is probably when the sharks are in the water. The VCs are going to come in and offer people billions of dollars to start their own chip companies, their own neolabs.”  “If a year from now we’ve seen a bunch of departures from NVIDIA, I’m going to be really concern...
  [查看](https://x.com/SemiAnalysis_/status/2121462524281282700)
- Stargate Abilene is impressive. Colossus 2 is adding nearly two of them in under a year. SpaceX's campus on the Memphis/Mississippi line goes from 0.4GW of IT in January to 2.4GW by YE2026, across Macrohard, MiniHard, Macroharder, Project SPAM and Gun Range. (1/5)🧵 https://t.co/yG7k6DQ5vH
  [查看](https://x.com/SemiAnalysis_/status/2121401747734208740)

### @theturingpost | Research

- RT @TheTuringPost: AI routing is like an art of its own ↓  Which model, tool, or policy should handle your request is a job of a router.  A…
  [查看](https://x.com/TheTuringPost/status/2121732066517909727)
- .@AIatMeta and École Nationale des Ponts et Chaussées researchers developed e-means - a new mini-batch clustering algorithm.  It's a much more efficient drop-in replacement for standard k-means. It relies on exponential moving averages (EMA) and:  • Beats k-means accuracy in 1/10th the epochs • Gives 10×–45× GPU wall-clock speedups • Zero hyperparameter tuning with specific scaling laws  Let's see...
  [查看](https://x.com/TheTuringPost/status/2121725370135450083)
- RT @TheTuringPost: Lauren is like Occam's razor:  if your coding loop produces slop, automating it produces more slop, faster, with a large…
  [查看](https://x.com/TheTuringPost/status/2121680195811750088)
- AI routing is like an art of its own ↓  Which model, tool, or policy should handle your request is a job of a router.  AI router can be a set of rules, a classifier, a small neural network, or another language model.  Its decision can work in a few ways:  - Route by task type: e.g., send coding requests to a coding model. But simple, a one-line edit and a difficult bug don’t need the same resource...
  [查看](https://x.com/TheTuringPost/status/2121648446411014432)
- When there is no Jensen at NVIDIA, America doesn’t fly.   Just saying
  [查看](https://x.com/TheTuringPost/status/2121382429264888126)

### @vllm_project | Infra

- RT @vllm_project: We optimized DeepSeek-V4.1-Flash on vLLM for Vera Rubin NVL72 and reached 58× the throughput of GB300 NVL72 at 1.7 millio…
  [查看](https://x.com/vllm_project/status/2121387736338944475)

## 👤 研究者动态（29条）

### @alexolegimas [Google DeepMind] | Research

- RT @kevinweil: Absolute goosebumps. @SpaceX caught the starship! I will never get tired of watching rockets. https://t.co/SznFQ8ptO0
  [查看](https://x.com/alexolegimas/status/2121719543730954370)
- FWIW Ive been in the “sparks” camp for a few months now (excellent term, @dwarkesh_sp). I don’t think we will have a “general” intelligence explosion across all domains. Within 12 months I expect an IE in at least one domain (with substantial uncertainty). This IE will make IEs and other domains easier, and these speed ups will depend on the cross domain elasticities.   This of course assumes no s...
  [查看](https://x.com/alexolegimas/status/2121674665374388605)
- RT @eliebakouch: this is a very important essay if you want to understand AI progress and how to measure it. i've been working on this for…
  [查看](https://x.com/alexolegimas/status/2121672599046668678)
- RT @RDMetcalfe: @JulianDJacobs @Moreincommon_ @benwansell @alexolegimas I think what would help motivate but also help model is the large s…
  [查看](https://x.com/alexolegimas/status/2121636139698155679)
- RT @eliebakouch: this is just harmful to repost such plot without a labelled y axis, no values, no definition of how they computed this com…
  [查看](https://x.com/alexolegimas/status/2121635767009104254)
- RT @Thom_Wolf: According to Andon Labs’ new reports, Fable 5.2 knows it is being tested when we run it on the latest Vending-Bench.  But it…
  [查看](https://x.com/alexolegimas/status/2121624433504948726)
- RT @dioscuri: Some personal news: after several happy years as Education Director of @LeverhulmeCFI, I'm passing the torch to my brilliant…
  [查看](https://x.com/alexolegimas/status/2121624148518551726)
- RT @JesusFerna7026: METR spent almost three months inside Anthropic and concluded that Anthropic is now improving its new models about twic…
  [查看](https://x.com/alexolegimas/status/2121610491357536710)
- There is a lot of heated discourse around the meaning of work and how much people value the non money elements of it. But very little data.   My @GoogleDeepMind colleague Julian’s paper sheds light on these questions, 1) showing that the majority of people do derive substantial value from work besides the money, 2) people across the whole income distribution value work beyond the money, and 3) the...
  [查看](https://x.com/alexolegimas/status/2121605533295595546)
- RT @GregoryConti19: Great paper.  Work is one of the greatest sources of meaning and satisfaction for most people. To me, this shows that h…
  [查看](https://x.com/alexolegimas/status/2121594056484565250)

### @demishassabis [Isomorphic Labs / Google DeepMind] | Research

- RT @mirrokni: Check out our recent results solving open challenges across math/science and engineering with /teamwork and Gemini 4 models :…
  [查看](https://x.com/demishassabis/status/2121713883911950656)

### @neelnanda5 [Google DeepMind] | Research

- I respect Buck's judgement, and he's often been more right than me on what needs to happen in AI Safety. Seeing him conclude things like this is very concerning...
  [查看](https://x.com/NeelNanda5/status/2121668751875838307)

### @steipete [OpenClaw] | Application

- RT @petergostev: I nominate this typical Londoner for the Nvidia CEO job - impossible to honeypot https://t.co/pmY3pC5ebH
  [查看](https://x.com/steipete/status/2121718064337326470)
- RT @NateBef: I revisited OpenClaw this week after months off it. The web UI is far more polished than I expected, and the app holds up on m…
  [查看](https://x.com/steipete/status/2121667194471977193)

### @svlevine [UCB] | Research

- RT @Stone_Tao: our bottom line is robotics and we are incredibly driven to deliver useful robots everywhere  apply here to push the frontie…
  [查看](https://x.com/svlevine/status/2121442024486547546)

### @swyx [AI社区] | App

- if you're in SF, i have 3 spare tix for our matinee show, just show up to odc theater now and drop my name  2.30pm doors open 3pm starts
  [查看](https://x.com/swyx/status/2121730527174787181)
- RT @poteto: my AIE talk is up! come hear how the grok @bot team ships so quickly without compromise on quality  https://t.co/Fel7tlxqSL
  [查看](https://x.com/swyx/status/2121695596054794273)
- RT @drewjs: Unforgettable week at @aiDotEngineer! So many insightful talks and it was great meeting so many talented folks. Shoutout to the…
  [查看](https://x.com/swyx/status/2121690896731451800)
- openai dot now has a setting to just solve all captchas for the rest of time https://t.co/rIqg7nVP8K
  [查看](https://x.com/swyx/status/2121681368224797014)
- RT @Swizec: The No Slop [in software] Manifesto is fantastic.   https://t.co/5K3ELhdcJR https://t.co/YCKAs7NrZO
  [查看](https://x.com/swyx/status/2121667902856441877)
- RT @aiDotEngineer: taking day 1 view count predictions for the @poteto talk launching in 30 mins  https://t.co/UbXuS2cTXj  hit the bell etc…
  [查看](https://x.com/swyx/status/2121667604809224555)
- RT @dexhorthy: a few days ago we published the "No AI Slop Manifesto" at @aiDotEngineer Code Summit in SF, written in collaboration with ma…
  [查看](https://x.com/swyx/status/2121660851212161303)
- RT @aiDotEngineer: AI can do more of the work. So why does the job feel harder?  @simonw on what happens when the easy tasks disappear and…
  [查看](https://x.com/swyx/status/2121650197751378210)
- RT @0xmaz_: Pretty cool in San Francisco you can watch @swyx perform musical theater for a cool 34 bucks !!! Link to tickets below https://…
  [查看](https://x.com/swyx/status/2121472881708380478)
- RT @vadiamit: what a week at @aiDotEngineer. thanks to @swyx, @Beccalytics and team for putting so many world class builders in one room an…
  [查看](https://x.com/swyx/status/2121468902437974225)

### @ylecun [NYU] | Research

- RT @sainingxie: before hopping on the ‘encoder-free’ hype train, think twice.
  [查看](https://x.com/ylecun/status/2121702381125546472)
- RT @ClementDelangue: This whole thing sucks, and I wish none of it had happened. It’s a really sad day!  But I want to make one thing clear…
  [查看](https://x.com/ylecun/status/2121698920355024983)
- RT @joanbruna: Mathematics and AI now define an interface full of fascinating questions that extend beyond a single discipline, and that re…
  [查看](https://x.com/ylecun/status/2121698166613635165)
- RT @Dragonhau66: 终于实锤了❗️❗️  干掉黄仁勋的，不是婚外情，而是一场由美国政客、媒体、CIA和Anthropic 联合做局的“完美猎杀”。  黄仁勋辞职后，《纽约时报》两名记者在播客里亲口承认： 他们是收到了一位“科技界联系人”的爆料，才去查Megaspe…
  [查看](https://x.com/ylecun/status/2121388007626359219)
