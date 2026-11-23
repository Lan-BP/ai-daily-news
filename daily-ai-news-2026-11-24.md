## 11月24日 AI 前沿动态

> 自动汇总 | 时间窗口: 24h | 全局精选 15 条

---

## 要点汇总

- 模型前沿：Z.ai 发布 GLM-5.4：首次采用 Loop Transformer，扩展至视频、游戏与 CAD; Google DeepMind 用 Gemini 4 智能体构建量子电路：未来模拟成本最高降 10 倍
- 产业动态：报道称 Nvidia 恢复黄仁勋 CEO 职务，股价盘初上涨 32%; Amazon 收购 AI 芯片软件公司 Decart 核心技术与团队; Claude 面向符合条件企业公测 ZDR 与 EFS 组合方案
- 算力追踪：vLLM 披露 AMD KV Cache 卸载测试：NVMe 吞吐达到 1TB DRAM 的 5.1 倍
- 初创&融资：具身智能公司至简动力完成 1 亿美元融资，估值达 16 亿美元; 具身智能公司章鱼动力获数亿元 A 轮融资：美的集团投资; 脑机接口与具身智能企业傲意科技获数亿元 D 轮融资; AI 建筑审批服务商 Pulley Studios 获 4100 万美元 B 轮融资
- 研究关注：RoboTrack 面向真实世界机器人操作研究点跟踪; Clover-35B-A3B-Preview：扩散语言模型支持思考模式，智能体七项指标领先; NoPeWorld：用冻结 DiT 隐状态阻止物体穿透，违规率由 74% 降至 16%; Accord：单相机与 IMU 在线构建稠密度量地图，统一配置下 F-score 达最佳或次佳
- X讨论：RoboChallenge 发布首期 RoboChallenge Zero 大模型机器人评测

---

## 📖 详细参考

### 模型前沿
**Z.ai 发布 GLM-5.4：首次采用 Loop Transformer，扩展至视频、游戏与 CAD**
- Z.ai 发布 GLM-5.4，并称这是其首个 Loop Transformer 模型。该模型在 GLM-5 基座中循环现有层以深化推理，应用范围从传统编程扩展至视频、游戏、3D 着色器和 CAD 建模，同时加入视觉能力以增强视觉编程。官方表示，API 将在安全评估后开放，模型权重也将以负责任的方式发布。
  > 💡 GLM-5.4 的重点不只是代码生成，而是将循环 Transformer、视觉能力和多类视觉内容生产纳入同一模型。API 与权重开放的具体时间尚未明确，现阶段可确认的是模型发布及后续开放计划。
   - 来源: [@zai_org](https://x.com/Zai_org/status/2124811995912286352)

**Google DeepMind 用 Gemini 4 智能体构建量子电路：未来模拟成本最高降 10 倍**
- Google DeepMind 使用 Gemini 4 智能体团队构建了新的量子电路，可将未来量子模拟成本最多降低 10 倍。相关成果面向聚变能源、化学和药物发现等模拟场景，但实际应用仍取决于算法能否高效运行于早期量子硬件。
  > 💡 多智能体方法已把量子电路设计推进到可量化的成本优化阶段，不过现阶段效果仍受早期量子硬件与算法效率约束。
   - 来源: [@googledeepmind](https://x.com/GoogleDeepMind/status/2124911073266413634)

### 产业动态
**报道称 Nvidia 恢复黄仁勋 CEO 职务，股价盘初上涨 32%**
- 据 The Information 报道，Nvidia 于周一上午恢复黄仁勋的 CEO 职务，此前美国政府高级官员向 Nvidia 董事会保证其复职不构成国家安全风险。Nvidia 董事会主席 Harvey Jones 六天前曾排除让黄仁勋回归的可能，此举是在总统 Donald Trump、员工、部分投资者及包括 Elon Musk 在内的其他人士施压后作出的逆转。Nvidia 股价自 10 月初高点至上周五一度下跌 48%，市值蒸发 2.4 万亿美元，周一盘初上涨 32%。
  > 💡 公司治理在短时间内出现方向性逆转，说明此次复职不仅是常规人事安排，也受到政府、员工和资本市场多重因素影响。股价剧烈反应显示市场仍在重新评估 Nvidia 的领导层连续性与经营预期。
   - 来源: [The Information](https://www.theinformation.com/articles/nvidia-reinstates-jensen-huang)

**Amazon 收购 AI 芯片软件公司 Decart 核心技术与团队**
- Amazon 宣布收购以色列 AI 初创公司 Decart 的关键技术和部分核心员工。Decart 的软件用于提升芯片运行效率，并支持包括 Nvidia、Google 等厂商设计的多种 AI 芯片。Amazon 表示，此举将帮助其提高 AI 计算资源的运行效率，其中也包括自研 Trainium AI 芯片。
  > 💡 此次交易显示 Amazon 正通过吸收软件与人才补强自研 AI 芯片栈，目标是降低 AI 计算成本并提升 Trainium 的实际使用效率。相关技术对多类芯片的兼容范围，也可能强化 Decart 技术在 Amazon 算力体系中的应用价值。
   - 来源: [The Information](https://www.theinformation.com/briefings/amazon-acquires-chip-software-business-ai-startup-decart)

**Claude 面向符合条件企业公测 ZDR 与 EFS 组合方案**
- Anthropic 宣布，面向符合条件的企业，零数据保留（ZDR）与 Enterprise Frontier Safeguards（EFS）的组合方案已进入公开测试。该方案在保持 ZDR 兼容性的同时，对多次请求中的滥用行为进行检测，并已与超过 100 家客户共同开发。
  > 💡 这一组合方案试图在严格数据保留限制下提供跨请求滥用检测，为受监管或数据敏感型企业采用 Claude 提供了更完整的安全选项。
   - 来源: [@claudeai](https://x.com/claudeai/status/2124929944530587712)

### 算力追踪
**vLLM 披露 AMD KV Cache 卸载测试：NVMe 吞吐达到 1TB DRAM 的 5.1 倍**
- vLLM 项目披露了在 AMD 平台上的 KV Cache 卸载测试，测试环境采用 Kimi-K3、16 块 AMD MI355X 和 UMBP MoRI，并使用 NVMe 替代 DRAM。测试结果显示，1.8 TB NVMe 与 1.8 TB DRAM 的表现差距在 1% 以内；在 70 个会话下，4.6 TB NVMe 的吞吐量达到 1 TB DRAM 的 5.1 倍。该测试由 vLLM 项目与 AMD、EmbeddedLLM 协作完成，完整拆解发布在 vLLM 博客。
  > 💡 测试表明，在特定 AMD 与 vLLM 配置下，NVMe 不再只是 KV Cache 卸载的容量补充方案，也可能承担更高吞吐需求。不过，结果对应特定模型、硬件和会话规模，不能直接外推到所有部署环境。
   - 来源: [@vllm_project](https://x.com/vllm_project/status/2124783254683132414)

### 初创&融资
**具身智能公司至简动力完成 1 亿美元融资，估值达 16 亿美元**
- 至简动力近日完成由蚂蚁集团领投的 1 亿美元融资，公司估值达到 16 亿美元，约合人民币 107 亿元。阿里巴巴、腾讯、红杉资本和蓝驰创投等现有投资者也参与了本轮投资。至简动力打造了世界模型与 VLA 一体化模型，以统一 Transformer 联合建模和理解语言逻辑、视觉语义、3D 空间结构及机器人状态。
  > 💡 本轮融资规模与蚂蚁集团领投、既有股东跟投，表明资本正在加大对具身智能模型与机器人软硬件协同路线的支持。资金规模较大，但统一架构能否转化为稳定产品和用户价值仍需后续业务表现验证。
   - 来源: [IT桔子](https://www.itjuzi.com/investevent/14708475)

**具身智能公司章鱼动力获数亿元 A 轮融资：美的集团投资**
- 章鱼动力（SynapX）近日获得数亿元人民币 A 轮融资，美的集团参与投资。公司以 SYNTH 深思架构为技术底座，构建任务与数据闭环，推动机器人在实际工作中规模化部署，并通过数据飞轮推进具身智能迭代。
  > 💡 本轮融资引入了产业资本方，章鱼动力将具身智能模型与机器人规模化部署相结合的业务路径获得进一步资金支持。
   - 来源: [IT桔子](https://www.itjuzi.com/investevent/14708438)

**脑机接口与具身智能企业傲意科技获数亿元 D 轮融资**
- 傲意科技近日宣布完成数亿元人民币 D 轮融资，本轮由中兵顺景、长江资本、光谷产投等机构联合投资。公司专注于脑机接口与具身智能机器人的核心算法和整机研发。
  > 💡 多类产业与投资机构共同参与此次 D 轮融资，傲意科技同时布局脑机接口算法和具身智能整机，业务协同空间值得关注。
   - 来源: [IT桔子](https://www.itjuzi.com/investevent/14708119)

**AI 建筑审批服务商 Pulley Studios 获 4100 万美元 B 轮融资**
- Pulley Studios 是一家 AI 建筑审批服务商，将 AI 智能体与持证建筑专业人员结合，为商业地产、数据中心、新能源和多户住宅项目提供一站式建筑审批服务。其服务覆盖前期合规尽调、施工图 AI 预审、许可申报和市政对接，支持美国 2000 多个市县的私人图纸预审，并服务 Meta、Amazon、JLL 等客户。近日，Pulley Studios 获得 4100 万美元 B 轮融资，由 Jump Capital 领投，Catalyst Investors 参投。
  > 💡 该轮融资反映资本对垂直行业审批自动化的关注，其差异化能力来自 AI 智能体与持证专业人员的结合，以及覆盖多地市政流程的业务基础。
   - 来源: [IT桔子](https://www.itjuzi.com/investevent/14708468)

### 研究关注
**RoboTrack 面向真实世界机器人操作研究点跟踪**
- RoboTrack 聚焦真实世界机器人操作中的点跟踪问题。现有来源仅提供标题，未披露具体方法、实验结果或应用范围。
  > 💡 由于缺少方法、数据与评测信息，当前无法判断该方案的实际效果及落地价值，后续需等待更完整的技术说明。
   - 来源: [HuggingFace Blog](https://huggingface.co/blog/allenai/robotrack)

**Clover-35B-A3B-Preview：扩散语言模型支持思考模式，智能体七项指标领先**
- 论文提出 Clover-35B-A3B-Preview，一款总参数量为 350 亿、激活参数量为 30 亿的混合专家扩散语言模型，支持思考模式生成。该模型将 Gated Delta Networks 改造为分块扩散机制，在当前块内结合双向 softmax 注意力，并利用历史记忆读取、可学习的块大小校准和独立的零初始化右侧上下文卷积分支处理生成上下文。Clover 在七项智能体指标中领先，其中包括 SWE-bench Verified 的 73.6 分和 Terminal-Bench 2.1 的 51.7 分；在内部智能体工作负载中，使用一块 NVIDIA GB300 GPU、BF16 精度和批大小 1，报告生成速度为每秒 680 个 token。其评估还覆盖模型质量、起草与验证成本以及内存受限部署；另一决策模型变体可通过一次去噪过程联合回答相关问题，在内部 500 组数据上将问题准确率从 90.37% 提升至 93.88%，并将全对组准确率从 65.4% 提升至 77.0%。
  > 💡 Clover 的核心价值是以较低激活参数量兼顾扩散式生成、思考模式和智能体任务，但其部署优势仍需结合独立复现及真实负载成本验证。
   - 来源: [HuggingFace Daily Papers](https://huggingface.co/papers/2611.24636)

**NoPeWorld：用冻结 DiT 隐状态阻止物体穿透，违规率由 74% 降至 16%**
- 论文针对交互式视频世界模型中的物体穿透问题，提出用于评估模型应对物理障碍能力的 NoPeBench 基准。评测显示，被测开源模型均无法可靠避免穿透，但这些模型的隐藏状态已包含预测动作是否穿透障碍所需的信息。论文进一步提出轻量框架 NoPeWorld，在冻结的扩散 Transformer 隐状态上训练小型预测头，判定候选动作是否安全，并将不安全动作替换为尽可能保留原始意图的安全动作。NoPeWorld 在六个视频世界模型上的平均物理违规率由 74% 降至 16%，并对开放域图像、第三人称视角和移动障碍表现出零样本泛化能力。论文公开了代码、NoPeBench 基准和模型权重。
  > 💡 该工作显示，无需改造世界模型主体，也可利用其已有隐状态增加一层安全约束，为具身与视频世界模型落地提供了低成本干预路径。
   - 来源: [HuggingFace Daily Papers](https://huggingface.co/papers/2611.27963)

**Accord：单相机与 IMU 在线构建稠密度量地图，统一配置下 F-score 达最佳或次佳**
- 论文提出 Accord，可使用任意配有 IMU 的相机在线构建稠密度量地图。其流程由 VIO 滤波器发布度量位姿，以位姿为条件调用深度基础模型预测短关键帧窗口的深度，再通过因子图融合所得子地图。Accord 利用多视图一致性，将每个关键帧窗口锚定到由滤波器位姿三角化得到的度量三维点，并通过共同可见图像间的双向稠密深度一致性估计和修正单图尺度误差，同时保留锚点建立的度量尺度。论文在五个公开的相机—IMU 配置以及一个新采集的 Phone-rig/GoPro 数据集上使用同一映射配置评测，未针对各数据集调参，且每张地图仅按 Accord 自身轨迹对齐；Accord 在每个平台上均取得 5 厘米阈值下最佳或次佳的平均 F-score。Accord 与手机拍摄装置数据集均已开源。
  > 💡 Accord 将稀疏但具度量尺度的 VIO 与稠密深度预测结合，并以统一配置跨设备验证，展示了单相机在线度量建图的实用潜力。
   - 来源: [HuggingFace Daily Papers](https://huggingface.co/papers/2611.25279)

### X讨论
**RoboChallenge 发布首期 RoboChallenge Zero 大模型机器人评测**
- RoboChallenge 正式发布面向大模型与真实机器人交互的新评测基准 RoboChallenge Zero。现有证据仅确认该基准及其首期评测已经发布，未提供参赛模型、具体任务或成绩数据。
  > 💡 RoboChallenge Zero 将评测触点从模型能力延伸到真实机器人场景，但缺少首期结果，暂时无法判断现有模型的实际操作水平。
   - 来源: [量子位](https://www.qbitai.com/2026/11/511978.html)


---
*更新时间: 2026-11-24 07:04*