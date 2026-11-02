# 愿你走的每一步，都更靠近喜欢的生活。

[近期漏报补刊：完整 13 条动态，含全部原始链接](https://linkx-capital.github.io/ai-daily-news/daily-ai-news-2026-11-03-supplement.html)

**日期**：2026-11-03 · AI 动态
**更新**：2026-11-03 00:32 北京时间

1. **Hydrogen-1.0 开放权重科研模型发布**
   以 GLM-5.3 为底座，用科研数据、实验记录和发现过程进行后训练。
   [@chenru_duan](https://x.com/chenru_duan/status/2117249292469665838)

2. **DeepSeek Harness 推出 Creator Mode**
   把创意转成可用插件，可用于设计工作区、沙盒游戏和 3D 大模型可视化。
   [@DeepSeekHarness](https://x.com/DeepSeekHarness/status/2117256196227019194)

3. **NVIDIA AgentX 提交高吞吐推理结果**
   据 SemiAnalysis 转述，NVIDIA 新提交称 700B 以上模型可实现单用户每秒超 1000 token。
   [@semianalysis_](https://x.com/SemiAnalysis_/status/2116950855718998288)

4. **SemiAnalysis 发布 GDPx 智能体基准**
   评测高价值领域的智能体能力；SemiAnalysis 称其测试中最佳模型得分仅 12%。
   [@semianalysis_](https://x.com/SemiAnalysis_/status/2117075900575477855) · [原文](https://gdpx.semianalysis.com/) · [原文](https://semianalysis.substack.com/p/gdpx-measuring-frontier-model-capabilities)

<details>
<summary>还有精力？再看 3 条</summary>

1. **MiniMax M3.1 Flash 本地部署扩展**
   官方汇总社区量化与本地部署进展，其中 2-bit GGUF 权重约 143.9GB。
   [@minimax_ai](https://x.com/MiniMax_AI/status/2116996123164569606)

2. **AA-AgentPerf 加入 GPU 性价比指标**
   将 GPU 市场租价引入 AA-AgentPerf，以每小时成本衡量智能体任务吞吐量。
   [@artificialanlys](https://x.com/ArtificialAnlys/status/2117255658613735918)

3. **Karpathy 用 Claude 做出 HackerTube**
   从 HN 二十年 4300 万条评论筛出 6454 个视频，他称约两小时做成了这个网站。
   [@karpathy](https://x.com/karpathy/status/2116957135661945283) · [原文](https://hackertube.org/)

</details>

---

## 完整推文 · 34 条

抓取范围：最近 24 小时；来源按账号分组。

## 🏢 公司发布（17条）

### @artificialanlys | Model

- We are collaborating with Silicon Data to bring market-based GPU pricing into AA-AgentPerf, our datacenter system performance benchmark  Our users and partners want to know how much agent work they can support per dollar of compute. @silicondata's rental price indices allow us to report a reliable value-for-money metric, updated daily as prices change. We currently display Silicon Data indices for...
  [查看](https://x.com/ArtificialAnlys/status/2117255658613735918)

### @deepseek_ai | Model

- RT @DeepSeekHarness: Your Harness. You Define It.  Meet Creator Mode in DeepSeek Harness.   Turn ideas into plugins that you can use, from…
  [查看](https://x.com/deepseek_ai/status/2117261337877455247)

### @langchain | Infra

- RT @hwchase17: want to learn how to use decision models with langgraph/deepagents?  we're doing a meetup with Typesafe (Jev creators) next…
  [查看](https://x.com/LangChain/status/2117046808425967794)
- RT @hwchase17: A lot of content engineering challenges have pretty standard solutions, which has lead to some engineers saying agent engine…
  [查看](https://x.com/LangChain/status/2117046850801037647)
- How do agents remember?  And what does preventing context rot have to do with it?  Join our live workshop on context engineering for agent memory and learn: ✅ Context management techniques by building w/ Deep Agents ✅ How to keep the context window lean from the first tool call to final report  https://t.co/MjLlxjG5Xh
  [查看](https://x.com/LangChain/status/2117256038000841160)

### @minimax_ai | Model

- MiniMax M3.1 Flash, on more of your hardware.  Quantizing a 428B model opens up more ways to run it locally. Lower-bit weights reduce the memory needed to load the model and the weight data moved during decoding. Making those savings useful takes careful calibration, efficient low-bit kernels, and hardware-aware placement of experts across GPU and system RAM.  Thank you to the builders doing that ...
  [查看](https://x.com/MiniMax_AI/status/2116996123164569606)

### @mistralai | Model

- We asked Mistral Large 4 to show what happens when you break a molecule. ⚛️  With a short prompt, it wrote a quantum chemistry SCF solver from scratch, validated its output, and built a 3D view around it.   Le Chonk also understand chemistry enough to independently choose how to break the molecule and what orbitals to show, without further input. 🧵
  [查看](https://x.com/MistralAI/status/2117229259425038344)
- RT @philipVinc: @AgentikHQ @MistralAI Hi @AgentikHQ, Filippo from @MistralAI here.  The model picked STO-3G autonomously, reasoning that it…
  [查看](https://x.com/MistralAI/status/2117268857471856984)

### @openrouter | Infra

- RT @PeterJ_Walker: New from OpenRouter: 7-day average token volume for Anthropic models is up 3.6x since the launch of Opus 5.5  Sonnet 5.5…
  [查看](https://x.com/OpenRouter/status/2116965726389239849)

### @semianalysis_ | Infra

- Today we’re releasing GDPx, a benchmark for measuring agentic capabilities across the most valuable domains.  GDPx is a true frontier-level benchmark: even the best model scores just 12% (1/7)🧵 https://t.co/RNnkcuUkih
  [查看](https://x.com/SemiAnalysis_/status/2117075900575477855)
- RT @SemiAnalysis_: @ARCVEREX @ariadata_ @nratliff9 @arithmeticlabs1 @uri_rolls @btfl_machines @akarshaurora @chakra_ai @27upon2 @datacurve…
  [查看](https://x.com/SemiAnalysis_/status/2117076817098215825)
- BREAKING NEWS🚨: HBM CHIPS CAN REACH OVER 1000 tok/s/user on giant 700B+ models via agent swarm-written software, according to a new NVIDIA AgentX submission.  Furthermore, on Rubin NVL72, it can achieve 20.9x better perf per TCO than GB300 NVL72 at even "ultrafast" speeds of 325 tok/s/user and up to 9.11x better perf per TCO at 200 tok/s/user. (1/2)🧵
  [查看](https://x.com/SemiAnalysis_/status/2116950855718998288)
- The Datacenter Backlash Goes Bipartisan:  Next Week's Midterms and the 2028 Buildout 2027 is largely locked in. 2028 is less secure: a prolonged Texas permit freeze is now the biggest single risk to the US buildout, and both parties are running on tighter rules  https://t.co/VtvwQsX6vx
  [查看](https://x.com/SemiAnalysis_/status/2116966274060165561)

### @thehumanoidai | App

- Last week, we talked about how we’re using agentic AI across the company (check out the original post).  Here’s a more detailed example of our work accelerating policy development lifecycles: real world → simulation → robot deployment, fully agentically.  We believe this is the path forward for rapidly teaching robots new skills.
  [查看](https://x.com/TheHumanoidAI/status/2117278058990502078)

### @theturingpost | Research

- RT @TheTuringPost: 10 best sources to explore harness (studies and videos)  ▪️ Harness Engineering: Anatomy, Architecture, and Evolution of…
  [查看](https://x.com/TheTuringPost/status/2117162364957307060)
- 10 best sources to explore harness (studies and videos)  ▪️ Harness Engineering: Anatomy, Architecture, and Evolution of Coding Agents ▪️ AI Models Are Eating Their Harnesses. Now What? ▪️ Why DeepSeek Harness Is The End Of Coding Agents as We Know Them ▪️ Rethinking Verification in Agent Harnesses ▪️ HarnessMM ▪️ Self-Evolving Agent Harness ▪️ Harness² ▪️ Object-Oriented Harness ▪️ Harness Scalin...
  [查看](https://x.com/TheTuringPost/status/2117025133110153618)

### @zai_org | Model

- RT @chenru_duan: We’re introducing Hydrogen-1.0, our first open-weight model for scientific research. We post-trained GLM-5.3 (@Zai_org) on…
  [查看](https://x.com/Zai_org/status/2117277068232634716)

## 👤 研究者动态（17条）

### @gklambauer | Research

- Self-normalizing neural networks rediscovered: https://t.co/uvaaiSev8G  Here, both the activation function is shifted/adjusted such that both MEAN is zero and VAR is one.
  [查看](https://x.com/gklambauer/status/2117154807085441124)
- RT @ProfvLilienfeld: Die Professoren muessen einfach nur in persona pruefen, d.h. muendlich oder handschriftlich. Beides geht und gibt es s…
  [查看](https://x.com/gklambauer/status/2117281411203752018)

### @hyhieu226 | Research

- Someone must solve the cost of serving coworking agents.
  [查看](https://x.com/hyhieu226/status/2117064729931989036)
- This opinion may not age well, but I believe there is NO better architecture than the Transformer. All the crazy attention and MoE variations we are seeing are simply for efficiency, while the hardware still lags behind.
  [查看](https://x.com/hyhieu226/status/2117145985067741684)

### @jeffdean [Google] | Infra

- Election Tuesday is just two days away.  For those eligible to vote in the U.S., please make time to go to the polls to vote (or mail in your ballot if you haven't already).  Voting is a great privilege of living in a democracy and how we all make our collective voices heard. 🗳️ https://t.co/HaPeX9ueIl
  [查看](https://x.com/JeffDean/status/2117024473992056955)

### @karpathy [independent] | Research

- Weekend hack: HackerTube. I was annoyed with YouTube's recommendations so I had Claude filter down 43M comments over 20 years of HN to 6,454 videos that keep being recommended. *Significantly* better viewing experience, ~2 hours with Opus 5.5: https://t.co/JIhXN7OSh1  - Excellent recs without any logins (state is kept in local browser session) - Thumbnail is a representative frame from middle of t...
  [查看](https://x.com/karpathy/status/2116957135661945283)

### @steipete [OpenClaw] | Application

- RT @scaling01: another brutal reality check for the open-sauce china shills  GPT-5.5 released on April 23 outscores all tested chinese mode…
  [查看](https://x.com/steipete/status/2117179634047386060)
- RT @yusuf_budunoglu: @8teAPi https://t.co/iWXJa4YLH7
  [查看](https://x.com/steipete/status/2117181019535122545)
- RT @yawaramin: In a sane language this is a type error
  [查看](https://x.com/steipete/status/2117185852392849479)
- RT @naomibrockwell: You really think you can combat the onslaught of ai-enabled offensive cyber attacks with your artisanal, hand-crafted c…
  [查看](https://x.com/steipete/status/2117214012996014198)

### @swyx [AI社区] | App

- RT @borjaperfra: Estos días han empezado a subir a YouTube las charlas de @aiDotEngineer AI Engineer, la conferencia de IA más importante a…
  [查看](https://x.com/swyx/status/2117221547366903933)

### @thesephist [Anthropic] | Research

- RT @jungofthewon: Tinkertreat: A weekend with principled, creative souls riffing on calm technology, decision-making, ambient discovery, ha…
  [查看](https://x.com/thesephist/status/2117085894876475645)
- RT @Mappletons: The carnage of giving a bunch of nerds a thermal printer to play with https://t.co/xQrTmwM9Ru
  [查看](https://x.com/thesephist/status/2116936822249214267)

### @ylecun [NYU] | Research

- RT @haider1: Yann LeCun says:  People in AI have made the same mistake for 70 years: if a machine can do a task humans see as intellectuall…
  [查看](https://x.com/ylecun/status/2117048104998392270)
- RT @KenRoth: The Trump administration is openly meddling in European democracies to promote far-right political parties that support Putin…
  [查看](https://x.com/ylecun/status/2117207246358659500)
- RT @ylecun: @iamsupersocks Tout cela est correct. Merci.  Sauf une chose : j'ai bien créé FAIR en 2013, y compris la branche parisienne en…
  [查看](https://x.com/ylecun/status/2116957881622819109)
- RT @heyshrutimishra: Yann LeCun was right &amp; nobody in this industry wants to say it out loud.  109 million parameters beat 72 billion.  He…
  [查看](https://x.com/ylecun/status/2116977874913648878)
