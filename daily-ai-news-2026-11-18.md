## 11月18日 AI 前沿动态

> 自动汇总 | 时间窗口: 24h | 全局精选 15 条

---

## 要点汇总

- 模型前沿：OpenAI 发布 GPT-6.2 Astra 与 Sol：覆盖专业输出、编程和计算机操作
- 产业动态：vLLM-Omni 首日支持 AURA 2.0：9B 流式视频模型支持主动对话与场景感知工具调用; Google DeepMind 推出 Gemini 4 Hydrogen 机器人插件：自然语言连接仿真与真机任务; Nvidia 机器人主管称 OpenAI Astra 将部分机器人训练数据生成提速 100 倍
- 算力追踪：Nvidia 将截至 2028 年 1 月财年的收入增速预期上调至 75%; 报道称美国自 2024 年起调查 Megaspeed 潜在出口管制违规; JPMorgan 与 Citi 的数据中心贷款暴露 Megaspeed 间接关联风险; SemiAnalysis 称中国境内逾 1.5GW 芯片可能违反美国法律，相关供应链网络或将收缩
- 初创&融资：AI 药物设计公司 Isomorphic Labs 获 50 亿美元融资; Alphabet 旗下 AI 制药商 Isomorphic Labs 完成 50 亿美元 C 轮融资
- 研究关注：K2-Horizon 发布六款全开放语言模型：36B-A4B 以七分之一活跃参数逼近 32B 稠密模型; Sage S1.5 Flash 面向科学推理与交互式智能体：320B MoE 在 33 项基准中取得多项首位; SALA：以语义对齐连接人类与机器人潜在动作，支持双轴扩展具身基础模型; 低地球轨道核爆研究：100 万吨爆炸一周内或使约 98% 模型卫星失效
- X讨论：Microsoft AI 发布 MAI-Image-2.7：登顶 AA-Image-Editing v2.1，每千张图像定价 34.82 美元

---

## 📖 详细参考

### 模型前沿
**OpenAI 发布 GPT-6.2 Astra 与 Sol：覆盖专业输出、编程和计算机操作**
- OpenAI 发布 GPT-6.2 Astra 和 Sol，改进专业场景输出、编程、计算机操作与效率。新模型将面向 ChatGPT Work、Codex 和 API 提供服务，并以更低成本运行。
  > 💡 此次更新同时覆盖通用工作、编程代理和 API，反映 OpenAI 正将同一代模型向多个高频入口铺开；官方尚需通过实际使用效果验证成本下降与能力提升的组合价值。
   - 来源: [OpenAI News](https://openai.com/index/introducing-gpt-6-2-astra-sol)

### 产业动态
**vLLM-Omni 首日支持 AURA 2.0：9B 流式视频模型支持主动对话与场景感知工具调用**
- vLLM-Omni 宣布首日支持 AURA 2.0，这是一款 90 亿参数的流式视频模型，可观察场景、发起相关对话并根据所见内容采取行动。该模型支持模型主动对话，可自行决定何时发言以及发言内容，无需等待用户提问；其流式感知工具调用功能可依据实时场景和对话调用工具，并将结果带回对话。
  > 💡 AURA 2.0 把视频输入从等待提问的视觉问答推进到主动交互与工具执行，90 亿参数规模也有利于降低流式部署门槛；实际应用仍需验证工具调用时延、场景持续跟踪和错误动作控制。
   - 来源: [@vllm_project](https://x.com/vllm_project/status/2122729021888954599)

**Google DeepMind 推出 Gemini 4 Hydrogen 机器人插件：自然语言连接仿真与真机任务**
- Google DeepMind 宣布 Gemini 4 Hydrogen 与 Google Antigravity 新增的机器人插件可用于机器人任务。用户可以连接受支持的机械臂，在 MuJoCo 仿真环境中练习，并通过日常对话将任务运行到真实世界。
  > 💡 该方案把模型对话、仿真练习和真机执行串联起来，降低了机器人新任务训练与部署的工具链门槛。
   - 来源: [@googledeepmind](https://x.com/GoogleDeepMind/status/2122767521925230896)

**Nvidia 机器人主管称 OpenAI Astra 将部分机器人训练数据生成提速 100 倍**
- 报道称，OpenAI 于 9 月发布 Astra 后，Nvidia 机器人主管 Deepu Talla 认为该模型在理解物理世界方面取得突破。Talla 表示，Astra 已使某些机器人 AI 模型训练数据的生成速度提高 100 倍，并可能帮助自动化机器人进入工厂工作的流程。该访谈录制于 Jensen Huang 卸任 Nvidia CEO 之前。
  > 💡 如果相关提速和工厂部署效果得到进一步验证，物理世界数据生成可能成为机器人规模化落地的关键瓶颈环节。
   - 来源: [The Information](https://www.theinformation.com/articles/openais-astra-boon-robotics-says-nvidia-robotics-chief-deepu-talla)

### 算力追踪
**Nvidia 将截至 2028 年 1 月财年的收入增速预期上调至 75%**
- Nvidia 临时首席执行官 Colette Kress 表示，截至 2028 年 1 月 31 日的 12 个月内，公司收入预计同比增长 75%。这一增速较三个月前给出的预测高 5 个百分点，但低于公司当前增长水平。报道指出，Nvidia 10 月季度收入增长至 116 亿美元的两倍以上。
  > 💡 75% 的预期显示 Nvidia 仍押注算力需求保持强劲，但预测增速低于当前水平，意味着管理层对高基数下的增长回落已有明确预期。
   - 来源: [The Information](https://www.theinformation.com/briefings/nvidia-says-revenue-rose-103-first-earnings-report-since-huang-departure)

**报道称美国自 2024 年起调查 Megaspeed 潜在出口管制违规**
- 据报道，美国司法部和商务部表示，自 2024 年起已调查总部位于新加坡的 Megaspeed，调查重点是该公司是否违反向中国出售先进芯片的限制。商务部此前在发现可疑活动后启动了调查，Megaspeed 是一家 Nvidia 云服务合作伙伴。
  > 💡 调查触及先进芯片对华销售、东南亚转售渠道和云合作伙伴关系，显示美国出口管制审查正在延伸至更复杂的跨境交易链条。
   - 来源: [The Information](https://www.theinformation.com/briefings/u-s-probing-megaspeed-since-2024-export-control-violations)

**JPMorgan 与 Citi 的数据中心贷款暴露 Megaspeed 间接关联风险**
- 报道称，JPMorgan 和 Citigroup 于 2025 年向一家与 Megaspeed 有业务往来的数据中心运营商提供贷款，金额规模达到数十亿美元。随着东南亚数据中心融资接受更严格的国家安全审查，银行通过借款人形成的间接敞口开始受到关注。报道指出，数据中心运营商通常需要审查主要客户，而相关融资安排也引出了银行是否充分核查复杂所有权结构及其他风险信号的问题。
  > 💡 银行对数据中心运营商的授信风险不只取决于借款人自身，还取决于其客户、所有权和供应链关系；随着先进芯片交易审查加强，供应商审查可能成为贷款风控的必需环节。
   - 来源: [The Information](https://www.theinformation.com/articles/jpmorgan-citi-missed-megaspeed-risks-2-8-billion-data-center-loan)

**SemiAnalysis 称中国境内逾 1.5GW 芯片可能违反美国法律，相关供应链网络或将收缩**
- 据报道，SemiAnalysis 认为，中国境内有超过 1.5GW、按美国法律不应存在的芯片，并称这些芯片如何流入及其背后的网络将被拆解。该分析还提出，如果 Nvidia 因 Jensen Huang 离任而不再支持开源生态，其角色变化可能影响这一进程对开源 AI 的影响，但现有证据仅包含相关引述。
  > 💡 这一说法提供了芯片供给合规风险与开源生态政策依赖之间的观察角度，但 1.5GW 的统计口径、涉及芯片的具体来源和处置范围均未在现有证据中展开，宜等待可核验的进一步材料。
   - 来源: [@semianalysis_](https://x.com/SemiAnalysis_/status/2122519830381346945)

### 初创&融资
**AI 药物设计公司 Isomorphic Labs 获 50 亿美元融资**
- Demis Hassabis 宣布 Isomorphic Labs 获得 50 亿美元融资，用于推进其以人工智能重新设计药物、寻找新药的使命。Isomorphic Labs 表示，将继续从第一性原理出发，利用 AI 缩短寻找新药所需的时间并降低成本。
  > 💡 50 亿美元融资为 AI 药物设计的大规模投入提供了充足资金，但该笔资金能否转化为更短的药物发现周期，仍取决于后续临床和研发成果。
   - 来源: [@demishassabis](https://x.com/demishassabis/status/2122662616367853670)

**Alphabet 旗下 AI 制药商 Isomorphic Labs 完成 50 亿美元 C 轮融资**
- Alphabet 旗下 AI 制药商 Isomorphic Labs 完成 50 亿美元 C 轮融资，将人工智能和计算方法应用于药物发现。该轮由 Greenoaks 与红杉资本共同领投，Alphabet 再次参与投资，Andreessen Horowitz、Thrive Capital、GV 和淡马锡等投资者也参与其中。
  > 💡 这笔融资显示，资本正继续押注将 AI 与计算方法用于药物发现的高投入方向。
   - 来源: [IT桔子](https://www.itjuzi.com/investevent/14708098)

### 研究关注
**K2-Horizon 发布六款全开放语言模型：36B-A4B 以七分之一活跃参数逼近 32B 稠密模型**
- 论文提出 K2-Horizon，一组六款完全开放的语言模型，覆盖 0.9B 稠密模型至 375B-A23B MoE，面向数学、科学、软件工程、深度研究、办公自动化及智能体任务。其 36B-A4B 模型采用 Mixture-of-Value Attention 和 softplus attention gating，活跃参数量约为同数据训练的 32B 稠密模型七分之一；论文同时提出 Uno 无损扩散适配器，在无需单独草稿模型的情况下将解码速度最高提升 2.2 倍。K2-Horizon 按 LLM360 的开源定义发布完整开发历史、各训练阶段中间检查点、预训练数据、训练日志以及训练、评测和基础设施代码，其中相关流水线生成了约 10 万亿 Token 合成预训练数据，四款模型共用一套 22 万亿 Token 预训练语料与配方。
  > 💡 K2-Horizon 的关键价值不只在模型规模和成绩，还在训练历史、合成数据流水线与基础设施代码的完整披露；36B-A4B 的参数效率与 Uno 解码加速为生产部署提供了明确工程指标，但完整开放仍需用户承担模型、数据和代码复现的存储与算力成本。
   - 来源: [HuggingFace Daily Papers](https://huggingface.co/papers/2611.21003)

**Sage S1.5 Flash 面向科学推理与交互式智能体：320B MoE 在 33 项基准中取得多项首位**
- 论文提出 Sage S1.5 Flash，这是一款 3200 亿参数的通用 MoE 模型，用于基于科学证据进行推理并在交互式环境中执行任务。其配套的 Sage Sci-Perception 使用分子图、生物序列和光谱测量编码器，通过模态专用投影器与文本、图像共同输入共享骨干；团队还构建了涵盖工具调用、搜索、编程、机器学习实验和科学软件的可验证环境，并依据执行结果、环境状态变化或提交产物检查任务完成情况。在七个领域的 33 项基准评测中，Sage S1.5 Flash 在与五个基线模型的主要比较中位列 OfficeQA Pro、MLE-bench Lite、Harvey LAB 和 SpreadsheetBench~2 第一，在 OSWorld-Verified、WebArena-Verified 和 DeepResearch Bench~II 排名第二。
  > 💡 Sage S1.5 Flash 已从科学感知模型推进到可验证执行的通用智能体架构，其相对优势集中在文档证据处理、可验证工作簿和机器学习实验；若要在实际办公与浏览器流程中落地，视觉反馈下的执行稳定性仍比单项榜单排名更值得验证。
   - 来源: [HuggingFace Daily Papers](https://huggingface.co/papers/2611.21072)

**SALA：以语义对齐连接人类与机器人潜在动作，支持双轴扩展具身基础模型**
- 论文提出 SALA，通过未配对人类与机器人片段的语言描述估计语义相似度，并以软邻域结构引导人类潜在动作对齐到语义相关的机器人潜在动作。机器人动作重建则将共享潜在空间落到控制层面，为具身基础模型提供人类与机器人视频的统一监督信号。实验显示，增加通用人类视频预训练数据可持续降低下游机器人动作预测误差，增加特定任务的人类视频后训练数据则显著提升真实世界机器人任务成功率。
  > 💡 SALA 尝试用语言语义监督替代配对数据，缓解纯视频重建按外观聚类的问题，并同时改善预训练与后训练阶段的数据扩展效果。
   - 来源: [HuggingFace Daily Papers](https://huggingface.co/papers/2611.17110)

**低地球轨道核爆研究：100 万吨爆炸一周内或使约 98% 模型卫星失效**
- 论文研究了低地球轨道核爆的初始 X 射线、放射性裂变产物电子俘获及人工辐射带演化，并将其与卫星失效、碰撞和大气阻力相耦合。中心情景显示，在南大西洋上空 500 公里处发生 100 万吨当量爆炸后，约一周内约 98% 的模型卫星因反复辐射带暴露而失效。若将假定辐射耐受度提高至三倍，两周内仍约有 97% 卫星失效，广泛失效只会推迟数日；机动能力丧失还会使两年内预计发生约 20 次碰撞。
  > 💡 研究显示，卫星失效并不局限于爆炸后的瞬时辐射冲击，后续人工辐射带、失控碰撞和长期碎片暴露可能形成持续性基础设施损失。
   - 来源: [Hacker News](https://arxiv.org/abs/2611.09827)

### X讨论
**Microsoft AI 发布 MAI-Image-2.7：登顶 AA-Image-Editing v2.1，每千张图像定价 34.82 美元**
- Artificial Analysis 宣布 Microsoft AI 发布 MAI-Image-2.7，该模型在 AA-Image-Editing v2.1 排名第一，并称其价格约为榜单后四款模型的六分之一。MAI-Image-2.7 与 MAI-Image-2.7-Flash 进入图像编辑和文生图的质量与价格前沿，每千张图像价格分别为 34.82 美元和 10.24 美元。Artificial Analysis 表示，两款模型均在图像编辑任务中表现最佳，其中 MAI-Image-2.7 在文字或符号、场景与风格以及增强类项目上排名第一。
  > 💡 MAI-Image-2.7 同时以榜首质量和较低价格进入图像编辑前沿，可能提高该能力的商业可用性；不过现有证据只覆盖 Artificial Analysis 的单项评测，跨模型泛化、复杂局部编辑一致性和批量生成稳定性仍需独立验证。
   - 来源: [@artificialanlys](https://x.com/ArtificialAnlys/status/2122754535206846610)


---
*更新时间: 2026-11-18 06:46*