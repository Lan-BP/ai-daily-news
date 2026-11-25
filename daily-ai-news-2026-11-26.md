## 11月26日 AI 前沿动态

> 自动汇总 | 时间窗口: 24h | 全局精选 15 条

---

## 要点汇总

- 产业动态：S&P Global 将 Nvidia 列入“负面观察”：治理风险上升，未来 90 天或下调评级; 智元推出 AIMA 具身智能生态技术体系，并称灵心平台一年孵化超3万个机器人智能体
- 算力追踪：SemiAnalysis：MI355X 在 K3.1 Pro 上 TokenSpeed 具竞争力，高并发端接近 B300; Unconv AI 探索“由权重编程”的存算一体架构，目标是降低每 token 能耗; Dell 上调年度预期：第三季度收入翻倍，AI 数据中心需求继续增长
- 初创&融资：Micro-LED 互连开发商 Avicena 获超 1 亿美元 C 轮融资; 中性原子量子计算企业原子芯光完成超亿元天使轮融资; 具身智能开发商 Nidus 获 3000 万美元战略投资
- 研究关注：RLVB：按可验证信念奖励智能体等待证据，九项设置平均提升 17.1%; Mega-MMDF 与 DeepfakeBench-MM：用百万级伪造片段统一多模态深伪检测评测; Antom 3-in-1 Transformer：约 7B 参数支付基础模型统一序列、表格与图风险检测; iTDM：以瞬时轨迹分布匹配稳定扩散模型强化学习，GenEval2 收敛近 3 倍提速
- X讨论：Amazon 提交首批 Trainium3 UltraServer 测试结果：每美元性能称为对竞品 2.28 倍; 报道称美国收紧先进芯片与模型训练手段访问，中国 AI 企业面临压力; Artificial Analysis 发布 AA-Robotics-Sim v0.1：让语言模型直接控制 Unitree G1 仿真人形机器人

---

## 📖 详细参考

### 产业动态
**S&P Global 将 Nvidia 列入“负面观察”：治理风险上升，未来 90 天或下调评级**
- S&P Global 周三将 Nvidia 的信用评级列入“CreditWatch Negative”，理由是管理层与治理风险上升。该行动意味着评级机构将重新审查 Nvidia 的信用评级，并可能在未来 90 天下调评级。S&P Global 表示，Nvidia CEO 黄仁勋的辞职与复职尚不足以消除相关疑问。
  > 💡 此次观察直接触及 Nvidia 的治理连续性，而非单一业务或财务指标；未来 90 天的审查结果将影响市场对其信用风险的判断。
   - 来源: [The Information](https://www.theinformation.com/briefings/s-p-global-puts-nvidia-creditwatch-negative-due-governance-risks)

**智元推出 AIMA 具身智能生态技术体系，并称灵心平台一年孵化超3万个机器人智能体**
- 量子位报道称，智元灵心平台一年已孵化超过3万个机器人智能体，并面向零基础开发者提供开发能力。智元同时推出 AIMA，定位为行业首个开放且完整的具身智能生态技术体系。现有证据未披露该平台与生态体系的具体功能边界、部署规模或商业化指标。
  > 💡 智元正在同时推进开发平台和生态体系，智能体数量的快速增长有助于扩大开发者触达，但该指标尚不能直接等同于任务效果、活跃使用或商业收入。
   - 来源: [量子位](https://www.qbitai.com/2026/11/512715.html)

### 算力追踪
**SemiAnalysis：MI355X 在 K3.1 Pro 上 TokenSpeed 具竞争力，高并发端接近 B300**
- SemiAnalysis 测试称，TokenSpeed 在 K3.1 Pro 场景中采用 MI355X 已具备竞争力。其每美元总拥有成本对应的 token 数超过 B200 和 GB200，并在高并发端接近 B300。该结果由面向大型 MoE 的 ROCm 推理服务支持。
  > 💡 结果表明 AMD 大型 MoE 推理栈正在缩小与 NVIDIA 同代平台的成本差距，但高并发端仍以接近 B300 描述，尚不能视为全面领先。
   - 来源: [@semianalysis_](https://x.com/SemiAnalysis_/status/2125477398896693373)

**Unconv AI 探索“由权重编程”的存算一体架构，目标是降低每 token 能耗**
- NaveenG Rao 此前将 Nervana 出售给 Intel、将 MosaicML 出售给 Databricks，其创办的第三家公司 Unconv AI 正探索不同于 GPU 的计算架构。Unconv AI 认为 AI 当前受能源限制，因此关键指标是每个 token 消耗的焦耳数。公司提出打破内存与计算分离的冯·诺依曼结构，并建设“由权重编程”的机器。
  > 💡 Unconv AI 把竞争焦点从通用 GPU 性能转向每 token 能耗与存算一体，但现有证据仅覆盖技术主张和方向，尚未提供性能、能耗或商业化数据。
   - 来源: [@semianalysis_](https://x.com/SemiAnalysis_/status/2125371388743565562)

**Dell 上调年度预期：第三季度收入翻倍，AI 数据中心需求继续增长**
- Dell 公布第三季度业绩后股价上涨 5%，此前常规交易时段已下跌超过 10%。这家 PC 与数据中心硬件厂商当季收入超过翻倍，并由此前的收入预测超出近 60 亿美元。推动业务增长的主要因素之一，是企业升级服务器以训练 AI 模型和运行 AI 应用。
  > 💡 收入超预期近 60 亿美元并上调年度预期，显示 AI 服务器升级正在直接拉动 Dell 的数据中心硬件业务，但股价先跌后涨也反映市场波动较高。
   - 来源: [The Information](https://www.theinformation.com/briefings/dell-raises-annual-forecast-ai-data-center-boom-continues)

### 初创&融资
**Micro-LED 互连开发商 Avicena 获超 1 亿美元 C 轮融资**
- Avicena 是 Micro-LED 互连技术开发商，首创基于 Micro-LED 的 LightBundle™超低功耗高速互连方案。该方案用于 AI 与高性能算力集群内芯片、内存之间的数据传输，以替代传统铜互连，并具备高带宽密度、低能耗和远距离传输特点。Avicena 近日获得超 1 亿美元 C 轮融资，由 Intervest 领投，Hitachi Ventures、Diamond Edge Ventures、Prosperity7 Ventures、AMD、Samsung Catalyst Fund、Cerberus Capital Management、Tiger Global老虎海外和 SK 海力士参投。
  > 💡 超 1 亿美元 C 轮融资及多家芯片与算力产业资本参投，显示资本市场正关注面向 AI 集群的芯片、内存互连技术。Avicena 的差异化定位是将 Micro-LED 方案用于替代集群内部铜互连，但商业化规模仍需后续验证。
   - 来源: [IT桔子](https://www.itjuzi.com/investevent/14705552)

**中性原子量子计算企业原子芯光完成超亿元天使轮融资**
- 原子芯光是一家中性原子量子计算全栈企业，采用中性原子 QPU 与光量子互联 QLink 一体化技术路线，研发可规模化扩展的容错量子计算集群。公司近日完成超亿元天使轮融资，由联想之星和上海未来产业基金联合领投，北京中关村资本、徐汇资本、嘉铭浩春、硅港资本、金雨茂物和添宥资本等机构共同投资。资金将用于中性原子量子处理器与光量子互联技术迭代、量子计算一体机产品化以及核心团队建设。
  > 💡 本轮资金同时覆盖芯片、互联和产品化，反映投资方对中性原子路线从技术研发走向工程落地的支持。量子计算一体机的产品化进展与容错集群扩展能力将是后续关键验证点。
   - 来源: [IT桔子](https://www.itjuzi.com/investevent/14708640)

**具身智能开发商 Nidus 获 3000 万美元战略投资**
- Nidus 是具身智能科技研发商，主要研发机器人基础模型，为传统工业机器人提供泛化操作能力。其主打场景包括国防工厂线束精密装配自动化，并采用本地化主权 AI 框架，以保障涉密生产环境中的数据可控。公司商业化上线 4 个月即实现七位数营收，近日获得 3000 万美元战略投资，投资方包括 KPCB 全球、Costanoa Ventures、Ludlow Ventures、Tau、SF1、Absolute Partners及个人投资者。
  > 💡 Nidus 将具身智能基础模型聚焦于工业精密装配，并以涉密环境的数据可控能力作为差异化方向。融资规模与上线 4 个月实现七位数营收的进展显示其已进入早期商业验证阶段，但工业部署规模与持续盈利能力仍需观察。
   - 来源: [IT桔子](https://www.itjuzi.com/investevent/14708679)

### 研究关注
**RLVB：按可验证信念奖励智能体等待证据，九项设置平均提升 17.1%**
- 论文提出 Reinforcement Learning with Verifiable Beliefs（RLVB），根据模拟器计算的答案后验概率，在证据不足时奖励智能体继续行动，并在证据充分时奖励其作答。该方法不需要评审器、评论模型或奖励模型，也不读取智能体每次行动前写出的信念文本。论文同时发布视觉谜题基准 Pro Worlds，并在三个基准上评测三种视觉语言模型，其中两个基准未出现在训练数据中。RLVB 在全部九种设置中均优于基础模型，平均提升 17.1%，较使用 LLM 评审器过程奖励的 PPO 平均高 9.3%，同时少用 1.6 倍 GPU 小时。
  > 💡 RLVB 将长任务中的“过早作答”转化为可由模拟器验证的训练信号，结果同时改善准确率与 GPU 效率；但其依赖精确后验概率，证据目前尚未说明真实任务中的适用边界。
   - 来源: [HuggingFace Daily Papers](https://huggingface.co/papers/2611.32884)

**Mega-MMDF 与 DeepfakeBench-MM：用百万级伪造片段统一多模态深伪检测评测**
- 论文提出 Mega-MMDF，包含10万个真实片段和120万个伪造片段，覆盖22条伪造流程，包括单模态操纵、叠加伪造以及音视频联合生成。论文同时提出 DeepfakeBench-MM，在8个数据集和10种检测器上统一训练与评测流程；基于训练的检测器在使用 Mega-MMDF 训练时取得各自最高平均 AUC，相比各检测器的最佳替代训练数据集最多提升0.0784。跨流程实验表明，在复合伪造上训练并不必然提升对其中单项伪造操作的独立检测能力，而模态遮蔽可能增加误报和漏检。
  > 💡 大规模、多流程训练数据能够改善检测器，但复合伪造与组成操作之间存在泛化断层，部署评测需要覆盖不同伪造链路及输入异常。
   - 来源: [HuggingFace Daily Papers](https://huggingface.co/papers/2510.22622)

**Antom 3-in-1 Transformer：约 7B 参数支付基础模型统一序列、表格与图风险检测**
- 论文提出 Antom 3-in-1 Transformer，将序列、表格和图表示整合到同一支付基础模型中，总参数量约70亿，每条任务路由激活约17亿参数。模型主要使用 Ant International 内部支付数据进行预训练；在跨业务迁移实验中，预训练使目标业务指标较同架构从零训练提升34.5%。在使用25%训练标签时，预训练模型在不同商户域上的平均精确率和 Recall@0.5% 均超过使用完整标签的从零训练基线；在十亿级支付平台为期四个月的在线实验中，整体损失率较 XGB-Online 降低37.88%。
  > 💡 该模型展示了支付风控中统一建模多类数据结构与跨业务迁移的收益，但核心训练证据来自蚂蚁国际内部数据，外部场景中的适用性仍需进一步验证。
   - 来源: [HuggingFace Daily Papers](https://huggingface.co/papers/2611.25403)

**iTDM：以瞬时轨迹分布匹配稳定扩散模型强化学习，GenEval2 收敛近 3 倍提速**
- 论文指出，现有前向扩散强化学习方法本质上依赖带符号奖励加权回归，在分类器无引导采样、离线更新和在线自洽性不完美等情况下会出现行为策略与目标策略不匹配，并引发基线漂移。论文提出瞬时轨迹分布匹配方法 iTDM，通过后验分数恒等式构造样本级梯度，并用在线辅助去噪器跟踪行为速度，在辅助最优解处保证基线不变性。实验覆盖组合生成、文字渲染和偏好对齐；在 GenEval2 上，iTDM 的收敛速度接近竞争方法的3倍并扩展至0.87而不崩溃，同时已扩展至56亿参数的 FLUX.3。
  > 💡 iTDM 针对的是扩散模型强化学习中的基线漂移问题，并通过更大规模模型实验显示扩展潜力；公开代码为复现和后续验证提供了基础。
   - 来源: [HuggingFace Daily Papers](https://huggingface.co/papers/2611.30986)

### X讨论
**Amazon 提交首批 Trainium3 UltraServer 测试结果：每美元性能称为对竞品 2.28 倍**
- Amazon 已向 SemiAnalysis 的 Agentic Inference Benchmark 提交首批 Trainium3 UltraServer 测试结果。SemiAnalysis 称，Trainium3 UltraServer 每美元性能达到 GB300 NVL72、B300 和 MI355 的 2.28 倍，并将结果归因于面向外部客户采用的广泛 EP 方案。
  > 💡 该结果来自 Amazon 提交并由 SemiAnalysis 公布的特定基准，当前信息尚不足以说明其覆盖的任务、配置与复现范围，因此更适合作为 Trainium3 推理性价比的新增信号，而非对现有 GPU 集群的全面性能定论。
   - 来源: [@semianalysis_](https://x.com/SemiAnalysis_/status/2125658708357128703)

**报道称美国收紧先进芯片与模型训练手段访问，中国 AI 企业面临压力**
- 据 The Information 报道，美国商务部本月出台一项规则，旨在限制中国企业在境外数据中心获取先进 Nvidia 芯片。该规则填补了美国对华芯片出口管制中的长期漏洞；黄仁勋恢复职务后，这项规则目前仍继续生效。报道还称，中国 AI 模型开发商长期依赖的开发手段正受到美国政府及美国 AI 竞争者的进一步限制。
  > 💡 境外数据中心使用先进 Nvidia 芯片的渠道收窄，意味着中国模型开发者的算力采购与训练安排可能受到更直接影响。报道未披露具体受影响企业及限制边界，实际影响仍需结合规则细则和企业供应链调整评估。
   - 来源: [The Information](https://www.theinformation.com/articles/chinese-ai-firms-confront-dire-future-u-s-tightens-access-chips-tokens)

**Artificial Analysis 发布 AA-Robotics-Sim v0.1：让语言模型直接控制 Unitree G1 仿真人形机器人**
- Artificial Analysis 发布 AA-Robotics-Sim v0.1，这是其机器人评测研究预览的最新阶段。此前，AA-Robotics v0.1 让模型控制机械臂；新版将语言模型置于原生测试框架中，直接控制仿真的 Unitree G1 人形机器人，并为每项任务设置简单目标。团队计划继续扩展该研究预览。
  > 💡 该预览把语言模型从机械臂控制推进到人形机器人全身任务，但目前公开信息聚焦仿真研究与研究预览，尚不能据此判断真实机器人上的实际表现。
   - 来源: [@artificialanlys](https://x.com/ArtificialAnlys/status/2125683694103064979)


---
*更新时间: 2026-11-26 06:49*