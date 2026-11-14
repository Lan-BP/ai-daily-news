## 11月15日 AI 前沿动态

> 自动汇总 | 时间窗口: 24h | 全局精选 15 条

---

## 要点汇总

- 模型前沿：HiPhys-RSI 登顶 BEHAVIOR-1K Challenge 2026：具身智能开启 Scaling 路径; Perplexity 发布 Decider v1.3 与 Flash v1.3：Decision Index v2.1 分别得分 70 和 64
- 产业动态：报道梳理 Jensen Huang 离开 Nvidia 的事件时间线; Tesla 向部分客户开放 Cybercab 购买资格：预计售价 29990 美元
- 算力追踪：联想提出“绿电进 Token 出”词元工厂：年产能 2000 万亿 Token
- 研究关注：MolRSI 引入递归自我改进筛选分子：湿实验命中率升至 15.9%; Meta 与 École Nationale des Ponts et Chaussées 提出 e-means：训练轮数降至十分之一; FAME-QP：GPU 加速实时控制二次规划，在保持精度的同时降低延迟; TurtLES：14 TB 三维湍流数据集评测神经 PDE 代理模型，揭示长时间滚动失稳与能量损失; BirdDreams：联合生成透视视频与 BEV 视频，提升驾驶世界模型的轨迹跟随与周围车辆行为
- X讨论：报道分析 Jensen Huang 离开 Nvidia 后的公司内外影响; Patrick McGee 认为 Johny Srouji 不会接任 Nvidia CEO; 湿实验预测基准发布：十余家顶尖团队参与; 11 月 14 日新闻汇总：美国停飞全国航班、微软服务宕机及 OpenAI 撤销独立机器人团队

---

## 📖 详细参考

### 模型前沿
**HiPhys-RSI 登顶 BEHAVIOR-1K Challenge 2026：具身智能开启 Scaling 路径**
- 华为诺亚具身智能团队 The North Star 以 HiPhys-RSI 方案参加 BEHAVIOR-1K Challenge 2026。The North Star 在来自全球 57 支参赛团队的挑战赛中取得领先成绩。
  > 💡 HiPhys-RSI 的竞赛成绩显示递归自我改进与具身任务扩展可能形成新的能力提升路径，但当前证据未披露完整排名及具体任务成绩。
   - 来源: [机器之心](http://mp.weixin.qq.com/s?__biz=MzA3MzI4MjgzMw%3D%3D&mid=2651074456&idx=1&sn=fd945abf7738045bba3669031d5ef7a2&chksm=853efd430d630f7666bc14113f8aadb3f928e15f7f510ff850a971ecca4857ea9ef78a18ec00&scene=0&xtrack=1)

**Perplexity 发布 Decider v1.3 与 Flash v1.3：Decision Index v2.1 分别得分 70 和 64**
- Perplexity 发布 Decider v1.3 与 Decider Flash v1.3，作为对 v1.2 旗舰决策模型的更新。两款模型在 Artificial Analysis Decision Index v2.1 上分别获得 70 分和 64 分。相较 v1.2，Decider v1.3 保持第六位，Decider Flash v1.3 升至第十位。
  > 💡 此次更新显示 Flash 版本在榜单排名上有所提升，但官方发布与第三方评测同日出现，榜单分数更适合作为版本表现的佐证。现有证据不足以判断提升来自模型能力、评测波动还是两者共同作用。
   - 来源: [@artificialanlys](https://x.com/ArtificialAnlys/status/2121595922090230033)

### 产业动态
**报道梳理 Jensen Huang 离开 Nvidia 的事件时间线**
- 报道称，Jensen Huang 已离开他共同创办于 33 年前的芯片公司 Nvidia。报道将相关事件追溯至 2010 年代，并称其与多名女性的关系、一次住宅冲突及董事会会议构成了后续风波的一部分。
  > 💡 现有证据以媒体梳理和未经证实的指控为主，董事会决策过程及其具体原因仍缺少完整官方说明。
   - 来源: [The Information](https://www.theinformation.com/articles/everything-led-nvidia-ceo-jensen-huangs-fall)

**Tesla 向部分客户开放 Cybercab 购买资格：预计售价 29990 美元**
- Tesla 宣布向“部分客户”提供购买 Cybercab 的机会，该车型为无方向盘和踏板的两座自动驾驶电动车。Tesla 在 X 上公布的预计购买价格为 29990 美元，客户还需每月支付 299 美元使用自动驾驶功能。
  > 💡 Cybercab 由此进入面向部分客户的购买阶段，但现有证据不足以确认全面上市时间、交付规模及自动驾驶功能在不同运行环境中的实际表现。
   - 来源: [The Information](https://www.theinformation.com/briefings/tesla-announces-cybercab-personal-use)

### 算力追踪
**联想提出“绿电进 Token 出”词元工厂：年产能 2000 万亿 Token**
- 量子位报道称，联想重新定义“词元工厂”，提出以绿色电力生产 Token 的模式。其披露的年产能为 2000 万亿 Token，相关成本下降 70%。
  > 💡 现有证据仅给出产能和成本降幅，尚不足以验证 Token 的具体类型、算力配置、能源来源及成本核算口径。
   - 来源: [量子位](https://www.qbitai.com/2026/11/510094.html)

### 研究关注
**MolRSI 引入递归自我改进筛选分子：湿实验命中率升至 15.9%**
- MolRSI 自主优化抗菌分子筛选流程，同时权衡抑菌活性、细胞毒性和结构新颖性。其湿实验命中率达到 15.9%，此前人类专家设计的非智能体工作流为 8.7%，相对提高约 82%。
  > 💡 该结果表明递归自我改进方案在湿实验分子发现中优于所述非智能体工作流，但现有证据不足以证明其在更广泛分子任务中的泛化能力。
   - 来源: [机器之心](http://mp.weixin.qq.com/s?__biz=MzA3MzI4MjgzMw%3D%3D&mid=2651074456&idx=3&sn=3ce02b6ba0021829c919847dffc37e64&chksm=85df8293d329cd21dc2d215f1f949b6eee8d2bdb647a3cd5c8a2feb267f1ece4b436548fa5f5&scene=0&xtrack=1)

**Meta 与 École Nationale des Ponts et Chaussées 提出 e-means：训练轮数降至十分之一**
- AIatMeta 与 École Nationale des Ponts et Chaussées 的研究人员开发了名为 e-means 的小批量聚类算法。该算法使用指数移动平均，可作为标准 k-means 的高效替代方案。研究团队称，e-means 在十分之一训练轮数下超过 k-means 的准确率，并获得 10 倍至 45 倍的 GPU 墙钟时间加速，同时无需针对特定缩放规律进行超参数调优。
  > 💡 e-means 将训练轮数、GPU 实际运行时间与无需额外调参结合在同一方案中，若结果可复现，可能降低聚类训练和部署的计算成本。
   - 来源: [@theturingpost](https://x.com/TheTuringPost/status/2121725370135450083)

**FAME-QP：GPU 加速实时控制二次规划，在保持精度的同时降低延迟**
- 论文提出 FAME-QP，一种用于线性模型预测控制中稠密二次规划问题的 GPU 加速求解器。该方案结合约束相关算子表示、通过 CUDA graphs 重放的融合单内核与双内核迭代，并利用设备校准和问题专项计时自动选择执行配置。论文指出，缓存算子库用于选择初始惩罚值，问题矩阵变化时则延迟更新算子。数值基准以及仿真人形机器人和四旋翼控制实验显示，FAME-QP 相比其他 GPU 求解器降低了延迟，同时保持解的精度与控制性能。
  > 💡 FAME-QP 的价值集中在实时模型预测控制的延迟优化，其自动配置与算子缓存机制有望减少部署时的手工调优，但现有证据未给出各控制实验的具体时延幅度。
   - 来源: [HuggingFace Daily Papers](https://huggingface.co/papers/2611.13766)

**TurtLES：14 TB 三维湍流数据集评测神经 PDE 代理模型，揭示长时间滚动失稳与能量损失**
- 论文提出 TurtLES，这是一个总规模 14 TB 的三维湍流圆柱尾迹数据集，覆盖剪切层转捩流态。数据集包含 400 条轨迹，每条轨迹有 400 个时间步，每帧包含 300 万至 1100 万个点，并改变几何形状、雷诺数与迎角。论文基于高保真隐式大涡模拟计算数据，使用密集非规则网格和长时间动态评测神经算子，识别出时间失稳、小尺度能量损失及大尺度非规则域学习困难等失效模式。
  > 💡 TurtLES 将真实湍流、非规则网格和长时滚动结合起来，补足了现有神经 PDE 代理模型评测对工业级网格分辨率与长期动态覆盖不足的问题。其披露的失效模式可作为代理模型研发与验收时的重点检查项，但论文结果不能直接证明某一类模型已适合实际工业部署。
   - 来源: [HuggingFace Daily Papers](https://huggingface.co/papers/2611.09567)

**BirdDreams：联合生成透视视频与 BEV 视频，提升驾驶世界模型的轨迹跟随与周围车辆行为**
- 论文提出 BirdDreams，一种自回归驾驶世界模型，可同时生成透视视角视频与示意性鸟瞰视角视频。该方法通过两个视频扩散 Transformer 的联合注意力，让两种视角在生成时相互提供信息，并以预测的 BEV 视频作为自车轨迹控制的几何接口。推理时，模型仅需单张摄像机图像，无需高精地图或车辆状态输入，即可生成两类视频。论文称，在 PhysicalAI-AV 和 nuScenes 上，BirdDreams 比既有驾驶世界模型更忠实遵循输入自车轨迹，并在无自车动作条件下生成更合理的自车运动；人工评测显示，其周围车辆行为也比仅使用透视视角的基线更逼真。
  > 💡 BirdDreams 的主要价值是把未来场景布局纳入预测，同时保留 BEV 对轨迹控制的便利与透视视频的场景细节。其结果说明联合表征可能比依赖未来周围车辆轨迹的既有方案更适合闭环应用，但证据仍集中于所列数据集和评测设置。
   - 来源: [HuggingFace Daily Papers](https://huggingface.co/papers/2611.14815)

**SO-Arena：覆盖 11 个领域评测 System One 模型，发现综合最高者可靠性仅列第七**
- 论文提出 SO-Arena，用于刻画 System One 模型的能力谱系与决策可靠性。该基准覆盖 11 个领域和五类能力，采用可靠来源与人工核验的参考答案、领域特定难度标准，以及让模型在沙箱中迭代执行动作的交互式评测。基准还通过受控选项集变化下的决策稳定性和无可用选项时的缺答识别，评估模型的决策可靠性。对 21 个模型的评测显示，扩展规模和增加推理带来的收益会随领域显著变化；综合表现最佳的 System One 模型在可靠性排名中仅列第七。
  > 💡 SO-Arena 表明，模型在综合基准上的强表现不能直接等同于稳定、可依赖的决策可靠性。对 System One 模型的选型应同时考察领域能力、推理成本和受扰动稳定性，避免仅凭聚合分数判断部署价值。
   - 来源: [HuggingFace Daily Papers](https://huggingface.co/papers/2611.15777)

### X讨论
**报道分析 Jensen Huang 离开 Nvidia 后的公司内外影响**
- 报道称，Jensen Huang 曾向 Nvidia 高管隐瞒其与 Alice Huang 之外另外两人的关系，其中一人是其直接下属。报道还称，公司总法律顾问 Tim Teter 坚持推动董事会采取行动，Nvidia 员工随后曾在线上流传要求 Huang 复职的联名请愿。
  > 💡 报道同时援引对 Huang 的个人批评、公司治理争议和华盛顿政治因素，显示其离任影响并不限于单一丑闻，但部分关键说法仍属媒体转述。
   - 来源: [The Information](https://www.theinformation.com/articles/fallout-jensens-downfall)

**Patrick McGee 认为 Johny Srouji 不会接任 Nvidia CEO**
- Patrick McGee 在 X 上表示，Apple 硬件负责人 Johny Srouji 能力突出且有强烈野心，但他认为 Srouji 很可能不会把 Nvidia CEO 职位视为 Apple 硬件负责人的升级。McGee 还称，Nvidia 董事会考虑 Srouji 的消息与 Srouji 对 Apple 及其芯片架构的忠诚并不相称。
  > 💡 这属于个人判断而非 Nvidia 官方人事安排；Srouji 是否获邀、是否有意愿以及最终人选均未得到确认。
   - 来源: [Daring Fireball](https://x.com/patrickmcgee_/status/2120799867140550999)

**湿实验预测基准发布：十余家顶尖团队参与**
- 斯坦福、哈佛、康奈尔等十余家团队参与发布一项湿实验预测基准。该基准用于考察模型对湿实验结果的预测能力。
  > 💡 现有证据仅能确认参与团队与发布动作，尚不足以判断基准的任务设计、评测结果及模型间的具体差异。
   - 来源: [量子位](https://www.qbitai.com/2026/11/510232.html)

**11 月 14 日新闻汇总：美国停飞全国航班、微软服务宕机及 OpenAI 撤销独立机器人团队**
- 报道称，美国停飞全国航班、微软服务大面积宕机，以及 OpenAI 撤销独立机器人团队，被列为当天值得关注的其他新闻。页面同时标明当天为 11 月 14 日，农历十月初六。现有证据未提供上述三项事件的具体时间、影响范围和官方说明。
  > 💡 该条目只能作为当日事件索引，现有证据不足以支撑对停飞范围、服务影响或组织调整细节的深入判断。后续发布或引用时，需要补充对应事件的原始报道或官方材料。
   - 来源: [差评X.PIN](https://mp.weixin.qq.com/s?__biz=MzA5NDc1NzQ4MA%3D%3D&mid=2654708671&idx=1&sn=927e8811b286eda0aa22ce080aba4ecb)


---
*更新时间: 2026-11-15 06:46*