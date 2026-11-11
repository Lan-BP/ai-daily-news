## 11月12日 AI 前沿动态

> 自动汇总 | 时间窗口: 24h | 全局精选 15 条

---

## 要点汇总

- 模型前沿：Google 发布 AlphaGenome 2：预测不同细胞类型中的 DNA 变异影响; 阿里预告 Qwen4：强化知识、编码与智能体能力，Qwen4-Max 开放预览
- 产业动态：Google 发布 TPU 8i Max（Whalefish）：单芯片配备 384GB 8 层 HBM; Anthropic 启动 IPO 路演，披露 Claude 多芯片训练与部署策略; Agility Robotics 谈协作安全：安全里程碑将拓展机器人部署环境与应用场景
- 算力追踪：Envision 乌兰察布 Galaxy 风电数据中心园区投用：首期 120MW 一年内交付; NVIDIA 联手 Radixark 优化 SGLang Rubin：不到 5 天性能最高提升 10 倍
- 初创&融资：AI 全栈硬件研发商 Sparxity 获 A 轮融资：布局动态稀疏芯片与机架级系统; AI 数据服务商 Mercor 完成 7.5 亿美元 D 轮融资; Anthropic 寻求 1.26 万亿至 1.4 万亿美元 IPO 估值; 中性原子量子计算企业原基量子完成亿元级天使轮融资; 机器人焊接单元开发商 Path Robotics 完成 3 亿美元 E 轮融资
- 研究关注：World In-Context Learning：冻结模型借仿真记忆操控任务，RoboTwin 2.0 成功率达 83.4%; DexForesight：以隐式空间预知增强灵巧策略，仿真总体成功率由 49.4% 升至 60.5%; SWAM：以跨模态对齐扩展世界动作模型，RoboTwin 困难条件成功率达 61.56%

---

## 📖 详细参考

### 模型前沿
**Google 发布 AlphaGenome 2：预测不同细胞类型中的 DNA 变异影响**
- Demis Hassabis 宣布推出新的 DNA 序列模型 AlphaGenome 2。该模型用于预测 DNA 变异在不同特定细胞类型中的影响，以帮助理解复杂疾病。AlphaGenome 2 已可通过 API 供学术研究使用。
  > 💡 AlphaGenome 2 将模型能力明确指向细胞类型特异的 DNA 变异影响预测，并以 API 开放学术研究使用，为复杂疾病相关研究提供新的模型工具。
   - 来源: [@demishassabis](https://x.com/demishassabis/status/2120565316619284734)

**阿里预告 Qwen4：强化知识、编码与智能体能力，Qwen4-Max 开放预览**
- 阿里 Qwen 预告即将发布 Qwen4，强调更深入的知识、更丰富的世界理解，以及更强的编码和智能体能力。该模型面向复杂编码、知识工作、前端构建和专业软件流程等现实任务。Qwen4-Max 已在 Alibaba Token Plan 上开放预览，用户也可通过 QwenWork、Qoder、Qwen APP 和 QwenStudio 提前体验。
  > 💡 Qwen4 的官方预告将重点放在编码、知识工作和智能体任务，而不只是通用对话能力；多平台同步开放早期体验，便于在正式发布前收集不同工作流中的反馈。
   - 来源: [@alibaba_qwen](https://x.com/Alibaba_Qwen/status/2120335993643684315)

### 产业动态
**Google 发布 TPU 8i Max（Whalefish）：单芯片配备 384GB 8 层 HBM**
- Google 发布 TPU 8i Max，代号为 Whalefish。官方信息确认，该芯片配备每芯片 384GB 的 8 层 HBM，而原版 TPU 8i 使用 12 层 HBM。
  > 💡 TPU 8i Max 将 HBM 堆叠层数由 12 层降至 8 层，但单芯片容量提升至 384GB；结合近期已发布的 TPU 8tx 与 TPU 8i Max，Google 正继续扩展面向敏感数据和重型工作负载的 TPU 产品线。
   - 来源: [@semianalysis_](https://x.com/SemiAnalysis_/status/2120578135594791297)

**Anthropic 启动 IPO 路演，披露 Claude 多芯片训练与部署策略**
- Anthropic 启动 IPO 路演，并发布此前未公开的业务信息。联合创始人 Tom Brown 在路演中表示，Anthropic 已在 AWS Trainium、Google TPU、NVIDIA GPU 和 AMD GPU 四大芯片系列上训练及部署 Claude，每种芯片均配有专门的软件与推理栈。公司称，今年首次接入 AMD GPU 时，Mythos 在三天内让 Claude 运行于该平台，Claude 移植或编写了几乎全部 kernels。Anthropic 将总有效算力定义为物理容量与已发现算力乘数的乘积，并认为算力乘数能够叠加并持续扩大其计算优势。
  > 💡 Anthropic 已把多芯片适配从高成本工程投入转化为可复用能力，四天内完成 AMD 适配尤其体现其软件栈的成熟度；多芯片策略能否转化为更低成本和更稳定的算力供给仍需后续数据验证。
   - 来源: [Simon Willison's Weblog](https://simonwillison.net/2026/Nov/11/anthropic-ipo-roadshow)

**Agility Robotics 谈协作安全：安全里程碑将拓展机器人部署环境与应用场景**
- Agility Robotics 的 Pras Velagapudi 和 Kevin Reese 表示，每项安全里程碑都会打开新的发展通道。二人称，协作安全能够解锁此前无法进入的环境和使用场景，而实际运营经验又可用于持续演进安全技术，进而支持下一层级安全概念与认证。
  > 💡 该表述将协作安全视为机器人扩大应用范围和积累部署经验的前提，但现有材料没有给出具体安全等级、认证进度或产品落地指标。
   - 来源: [@agilityrobotics](https://x.com/agilityrobotics/status/2120602274049479137)

### 算力追踪
**Envision 乌兰察布 Galaxy 风电数据中心园区投用：首期 120MW 一年内交付**
- SemiAnalysis 实地探访了 Envision 位于内蒙古乌兰察布的 Galaxy 风电数据中心园区。该园区规划规模为 800MW，一期 120MW 从空地推进至交付用时不足一年。
  > 💡 该园区将大规模风电供电与数据中心建设结合，首期 120MW 快速交付为后续 800MW 园区规划提供了已落地的工程样本。
   - 来源: [@semianalysis_](https://x.com/SemiAnalysis_/status/2120305690522599867)

**NVIDIA 联手 Radixark 优化 SGLang Rubin：不到 5 天性能最高提升 10 倍**
- NVIDIA 与 Radixark 合作继续优化 SGLang 在 Rubin 平台上的性能。SemiAnalysis 称，相关改进在不到 5 天内使性能最高提升 10 倍。
  > 💡 这一消息显示，模型推理框架与新硬件平台的协同优化仍可能快速释放性能，但现有证据未说明提升对应的具体工作负载、配置和测试方法。
   - 来源: [@semianalysis_](https://x.com/SemiAnalysis_/status/2120532776403247464)

### 初创&融资
**AI 全栈硬件研发商 Sparxity 获 A 轮融资：布局动态稀疏芯片与机架级系统**
- Sparxity 是一家 AI 全栈硬件研发商，自研面向动态稀疏 AI 的专用芯片、编译软件和机架级整机系统。其方案主打只计算必要参数，以提升稀疏模型推理能效，面向超算、科研和数据中心场景。此次融资由 ICM HPQC Fund 领投，Cloudberry Ventures、GS Futures、GlobalFoundries、Lockheed Martin Ventures、TGFS 和 EIC Fund 参投。
  > 💡 Sparxity 同时覆盖芯片、编译器和机架级系统，并以动态稀疏推理能效为核心定位；多家产业与投资机构参与本轮融资，反映其全栈方案获得一定资本支持，但现有证据未披露融资金额。
   - 来源: [IT桔子](https://www.itjuzi.com/investevent/14707658)

**AI 数据服务商 Mercor 完成 7.5 亿美元 D 轮融资**
- Mercor 是一家 AI 数据服务平台，并开发了评估体系 APEX。该体系从专业场景提取实际任务，由跨领域专家团队指导制定评估标准，以建立 AI 性能基准测试。Mercor 近日完成 7.5 亿美元 D 轮融资，Benchmark Capital、Felicis Ventures、Apollo、G Squared、General Catalyst Partners、Glade Brook Capital Partners、NVIDIA、Salesforce、Sapphire Ventures、行健资本、XTX Ventures、Zoom 和 Fundomo 参与投资。
  > 💡 大额融资显示资本仍在押注面向 AI 模型开发的数据、专家任务与评估基础设施，APEX 可能成为 Mercor 扩展企业业务的重要抓手。
   - 来源: [IT桔子](https://www.itjuzi.com/investevent/14707670)

**Anthropic 寻求 1.26 万亿至 1.4 万亿美元 IPO 估值**
- 据报道，Anthropic 披露其即将进行的 IPO 目标估值区间为 1.26 万亿至 1.4 万亿美元。此前 OpenAI 最近一轮融资的估值为 1.25 万亿美元，这意味着 Anthropic 预期公开投资者给予的估值仅比 OpenAI 高 12%。报道还称，Anthropic 第三季度收入比 OpenAI 高 70%，且今年大部分时间增速更快。部分 Anthropic 投资者预计，如果首日交易需求强劲，公司可能提高 IPO 价格或出售更多股份。
  > 💡 Anthropic 的目标估值与 OpenAI 近期融资估值差距不大，与其收入和增长表现并不完全对应；较低的发行估值可能是在为上市初期需求留出空间。
   - 来源: [The Information](https://www.theinformation.com/articles/anthropic-openai-valuation-gap)

**中性原子量子计算企业原基量子完成亿元级天使轮融资**
- 原基量子是一家专注中性原子量子计算的高科技企业，目标是建造百万量子比特、通用容错的实用量子计算机。公司致力于推动中性原子系统从实验室原型走向可流水线制造、稳定运行、高速迭代及全栈软硬协同的工程化产品。近期，原基量子完成亿元级天使轮融资，由中国互联网投资基金与清华系资本慕华科创联合领投，另有近 10 家机构跟投。资金将用于核心技术研发、工程化平台建设和核心团队扩充。
  > 💡 本轮资金用途聚焦技术工程化与团队扩充，融资重点是推动中性原子量子计算系统向规模化、工业级产品演进，而非仅停留在实验室验证。
   - 来源: [IT桔子](https://www.itjuzi.com/investevent/14707647)

**机器人焊接单元开发商 Path Robotics 完成 3 亿美元 E 轮融资**
- Path Robotics 是一家机器人焊接单元研发商，业务涵盖机器人技术、自动化以及软件和数据库解决方案。公司将解决一般问题的方法开发后应用于制造，并探索机器学习、适应与问题解决能力。近期，Path Robotics 完成 3 亿美元 E 轮融资，由 Georgian Partners 领投，Addition、Drive Capital、Tiger Global、Yamaha Motor Ventures、D. E. Shaw Ventures、IronArc Ventures 和 NAVER 参投。
  > 💡 大额 E 轮融资显示资本继续关注制造自动化中的机器人软件与执行单元，但材料未披露融资后具体业务扩张指标或商业化进度。
   - 来源: [IT桔子](https://www.itjuzi.com/investevent/14707656)

### 研究关注
**World In-Context Learning：冻结模型借仿真记忆操控任务，RoboTwin 2.0 成功率达 83.4%**
- 论文提出 World In-Context Learning（WICL），让冻结模型从演示出发，在仿真等环境中预演任务，并把反馈写入上下文而非模型权重。其模块化系统 RoboScript 将预演所得知识冻结为任务记忆，再部署到新场景；在 RoboTwin 2.0 的 50 项任务中，每项仅使用一次演示且不进行梯度更新，平均成功率达到 83.4%，较最强训练动作策略高出 20 多个百分点。该方法还支持跨视觉分布泛化、通过反思改进、随基础模型扩展，并可通过跨具身记忆适配迁移到双臂实体机器人。
  > 💡 WICL 将机器人技能习得从更新权重转为积累上下文记忆，在单演示和跨场景条件下展示了明显优势；其实际价值仍需结合实体机器人任务范围、记忆成本与部署稳定性判断。
   - 来源: [HuggingFace Daily Papers](https://huggingface.co/papers/2611.12885)

**DexForesight：以隐式空间预知增强灵巧策略，仿真总体成功率由 49.4% 升至 60.5%**
- 论文提出 DexForesight，将具备动态感知能力的世界表征注入灵巧操作策略的潜空间，以隐式学习场景和机器人手部的空间预知。训练阶段的世界模型利用离线场景深度、运动学手部几何和演示轨迹，预测三维手部点运动与视觉特征变化；部署时仅保留策略，并依靠 RGB 观测、语言和机器人状态生成动作，无需深度输入或显式未来预测。该方法在 11 项 DexJoCo 仿真任务上将基础策略总体成功率从 49.4% 提升至 60.5%，在 3 项真实机器人灵巧操作任务中达到 58.3%，高于最强基线的 50.0%。
  > 💡 DexForesight 显示，空间动力学可以作为条件信息注入策略，而不必在部署端显式执行未来预测；真实机器人上的提升幅度较为有限，尚需更多任务验证。
   - 来源: [HuggingFace Daily Papers](https://huggingface.co/papers/2611.11166)

**SWAM：以跨模态对齐扩展世界动作模型，RoboTwin 困难条件成功率达 61.56%**
- 论文提出 SWAM，围绕世界动作模型在动作学习过程中维持语言与视频对齐的问题，系统研究语言—视频监督、语言—视频—动作监督及其联合使用。研究团队整理了约 4.7 万小时通用视频、第一视角视频、UMI 演示和机器人演示，并考察语言标注质量、不同动作监督、联合训练方案和模型架构。采用选定配置扩展预训练后，再仅用 RoboTwin Clean 演示进行后训练，模型在 Easy 的 Clean-to-Clean 条件和 Hard 的 Clean-to-Random 条件下分别取得 88.10% 和 61.56% 的成功率；在 3 项真实世界任务上成功率为 40.00%，高于最强基线的 23.33%。研究团队同时发布整理后的数据、训练代码和模型权重。
  > 💡 SWAM 的数据与监督配比方案表明，世界动作模型的扩展不能只依赖动作数据规模，语言—视频预训练能力的保持与模型架构同样关键。
   - 来源: [HuggingFace Daily Papers](https://huggingface.co/papers/2611.12870)


---
*更新时间: 2026-11-12 06:46*