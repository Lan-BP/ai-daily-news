## 11月22日 AI 前沿动态

> 自动汇总 | 时间窗口: 24h | 全局精选 15 条

---

## 要点汇总

- 模型前沿：GPT-6.2 Astra 具身任务成功率较 GPT-6 Astra 翻倍; Inkling-2-Mini 以 5.4 GB 内存运行
- 产业动态：TML 开源循环 Transformer 模型，可在笔记本运行; Google 介绍 Gemini 对 Duplex 的扩展：可代用户致电商家
- 算力追踪：Oracle 宣布已落实履行 OpenAI 合同所需全部资金; 新智元报道超算相关成果重回中国队
- 初创&融资：报道称 Amazon 接近以 75 亿美元收购视频模型公司 Decart; 报道称 SoftBank 创始人孙正义曾探索万亿美元收购 SK Hynix
- 研究关注：Posterior Matching Distillation：以完整后验提升扩散模型蒸馏效果; Depth Pro 2：统一单目度量深度估计，兼顾边界锐度与时序一致性; ROSE：面向持续事实更新的多模态终身知识编辑新范式; WAM-Policy：四足机器人语言操控迁移至 85.0%，OPSD 学生采样提速 14 倍; Mind2Act World：拆解推理与执行短板，最强智能体复合任务成功率仅 12.0%
- X讨论：Anthropic 数学家 Levent Alpöge 称与 Claude 合作找到黎曼猜想证明; 报道称 Anthropic 数学家称借助 AI 模型证明黎曼猜想

---

## 📖 详细参考

### 模型前沿
**GPT-6.2 Astra 具身任务成功率较 GPT-6 Astra 翻倍**
- 量子位称，GPT-6.2 Astra 在 16 项具身任务中的成功率较 GPT-6 Astra 翻倍。该模型还实现可变形物体操控任务全球首通。
  > 💡 从任务成功率和复杂物体操控看，GPT-6.2 Astra 的升级重点已从通用语言能力延伸至具身执行，但现有证据不足以判断其实际部署成本与泛化稳定性。
   - 来源: [量子位](https://www.qbitai.com/2026/11/511779.html)

**Inkling-2-Mini 以 5.4 GB 内存运行**
- Hacker News 链接指向 GitHub 项目 lookatmyquant，页面标题显示 Inkling-2-Mini 可在 5.4 GB 内存中运行。现有证据未提供模型架构、任务表现或发布主体等进一步信息。
  > 💡 低内存运行可能有助于本地部署，但缺少模型规模、推理框架和性能数据，暂不足以判断其实际可用性。
   - 来源: [Hacker News](https://github.com/ShinMegamiBoson/lookatmyquant)

### 产业动态
**TML 开源循环 Transformer 模型，可在笔记本运行**
- 机器之心报道称，TML 开源了采用循环 Transformer 架构的新模型，可在笔记本上运行。报道还提到 Anthropic 数学家 Levent Alpöge 宣称自己与 Claude 找到了黎曼猜想的证明，并公布了相关声明。
  > 💡 循环架构与笔记本端运行构成模型轻量化方向，但现有证据未给出具体模型规模、性能指标及证明声明的核验结果。
   - 来源: [机器之心](http://mp.weixin.qq.com/s?__biz=MzA3MzI4MjgzMw%3D%3D&mid=2651075624&idx=2&sn=b6e7e23d631dba7a952cbe5da8e77769&chksm=859bdb5c2e044ab97595714f7e37c4143902997f9c5b9d068bab6099a9a2234b87ec44052b85&scene=0&xtrack=1)

**Google 介绍 Gemini 对 Duplex 的扩展：可代用户致电商家**
- Google 发布研究文章，介绍 Duplex 如何演进为可在 Gemini 中代用户联系商家的能力。现有证据将相关内容归为生成式 AI，未提供更具体的技术机制或评测数据。
  > 💡 这项更新显示 Google 正将 Duplex 的预约式交互能力延伸到主动代用户联系商家，但当前材料不足以评估其覆盖范围和实际可靠性。
   - 来源: [The latest research from Google](https://research.google/blog/how-google-duplex-evolved-to-also-call-businesses-for-you-in-gemini)

### 算力追踪
**Oracle 宣布已落实履行 OpenAI 合同所需全部资金**
- Oracle 周五宣布，已经获得履行与 OpenAI 合同所需的全部资金。该表态意味着公司已完成上月宣布最快于今年筹集的 200 亿美元新增股权与债务融资。Oracle 同时表示，任何声称相反情况的媒体报道都是错误的。
  > 💡 Oracle 公开确认资金到位，降低了履行 OpenAI 合同过程中的融资不确定性。不过，现有证据未披露具体资金结构和合同执行安排，后续仍需关注资金部署及相关算力交付。
   - 来源: [The Information](https://www.theinformation.com/briefings/oracle-says-completed-funding-fulfil-openai-deal)

**新智元报道超算相关成果重回中国队**
- 新智元发布的标题为“全国产！超算‘诺奖’5年再回中国队”。现有来源仅提供标题，没有可核验的成果主体、评选名称、技术指标或时间信息。
  > 💡 标题暗示国产超算相关成果获得重要认可，但缺少正文证据，现阶段无法判断成果的具体内容与行业影响。
   - 来源: [新智元](https://mp.weixin.qq.com/s?__biz=MzI3MTA0MTk1MA%3D%3D&mid=2652744315&idx=1&sn=d46f87fe5c3d67fafd150d6db59c8bad)

### 初创&融资
**报道称 Amazon 接近以 75 亿美元收购视频模型公司 Decart**
- 据《金融时报》报道，Amazon 正接近以 75 亿美元收购以色列 AI 初创公司 Decart。报道还称，《华尔街日报》在上个月早些时候已首次披露 Amazon 考虑收购 Decart。Decart 成立约三年，主要研发运行速度高于现有产品的视频模型。
  > 💡 如果交易完成，Amazon 将以较高价格获得以高速视频模型为核心的技术资产，但目前证据仍来自媒体报道，尚非双方正式宣布。交易进展及最终条款值得继续跟踪。
   - 来源: [The Information](https://www.theinformation.com/briefings/amazon-nearing-7-5-billion-purchase-decart)

**报道称 SoftBank 创始人孙正义曾探索万亿美元收购 SK Hynix**
- 报道称，SoftBank CEO 孙正义近期曾向华尔街机构接触，探讨为可能进行的万亿美元级收购 SK Hynix 提供融资。SoftBank 发言人表示，公司会探索多种机会，但这一交易已不再处于积极考虑之中。
  > 💡 相关意向已不再积极推进，事件当前更接近一次被放弃的融资与收购探索。其影响主要是显示资本对全球存储芯片资产整合的关注上升，而不是一项已确定的交易。
   - 来源: [The Information](https://www.theinformation.com/articles/softbanks-masayoshi-son-explored-1-trillion-moonshot-buyout-sk-hynix)

### 研究关注
**Posterior Matching Distillation：以完整后验提升扩散模型蒸馏效果**
- 论文提出 Posterior Matching Distillation（PMD），将覆盖模式的后验采样与任意步数生成结合起来。PMD 通过匹配固定噪声状态下学生样本的指数重加权均值与教师后验均值来学习完整后验，不依赖辅助的学生评分网络。论文证明，在开邻域内匹配倾斜均值能够唯一确定完整后验；基于 SDXL 和 FLUX.2 [klein] 4B 的实验显示，PMD 在两个模型上均取得四步方法中最佳的 FID，并在提示词对齐和感知质量指标上保持竞争力或领先表现。
  > 💡 PMD 直接监督完整条件分布，试图缓解反向 KL 的模式覆盖偏置，同时支持训练时间步网格内的任意步数采样。其价值在于兼顾生成多样性与推理效率，但实验结果目前集中于两个生成模型。
   - 来源: [HuggingFace Daily Papers](https://huggingface.co/papers/2611.26629)

**Depth Pro 2：统一单目度量深度估计，兼顾边界锐度与时序一致性**
- 论文提出 Depth Pro 2，以单一可扩展网络同时处理图像和视频，并在原生分辨率下预测稠密度量深度图。该方法针对既有方法在时序一致性与边界锐度之间的取舍，在度量精度、锐度、时序一致性和运行效率上均超过此前工作。作者同时发布了一组构成新帕累托前沿的模型，以及代码和权重。
  > 💡 Depth Pro 2 的价值在于用统一网络同时覆盖单帧锐度和多帧一致性，降低了视频深度估计系统在这两项指标之间选型的约束。
   - 来源: [HuggingFace Daily Papers](https://huggingface.co/papers/2611.26603)

**ROSE：面向持续事实更新的多模态终身知识编辑新范式**
- 西北工业大学团队提出 ROSE，聚焦多模态大模型在事实持续变化时的终身知识编辑。论文指出，现实知识会随企业高管更替、产品迭代和赛事结果更新而变化，模型需要持续吸收这些新事实，以保持知识时效性。
  > 💡 现有证据仅明确 ROSE 的研究目标与问题背景，尚不足以判断其具体机制和性能优势。
   - 来源: [机器之心](http://mp.weixin.qq.com/s?__biz=MzA3MzI4MjgzMw%3D%3D&mid=2651075624&idx=3&sn=d08693456bc97db18084229852b76739&chksm=858480058a0d06ff0034d52dcefa53fbb9e8906dd65e3a9eb77396c8e6d029cf74412b0265fd&scene=0&xtrack=1)

**WAM-Policy：四足机器人语言操控迁移至 85.0%，OPSD 学生采样提速 14 倍**
- 论文提出 WAM-Policy，通过跨形态策略适配与加速、任务专项改进与合并两个阶段，将面向机械臂预训练的 WAM 转为四足机器人移动操控策略。在 QLM-Bench 的十项模拟任务中，迁移策略达到 77.0%，OPSD 学生保持 76.7% 并将采样速度提高 14 倍，任务专项强化学习与多教师在线策略蒸馏进一步将成绩提升至 85.0%。作者还将 OPSD 学生部署到真实的 Unitree Go2 Air 机器人上。
  > 💡 该工作展示了从机械臂世界动作模型迁移到四足机器人的可行路径，在维持任务表现的同时显著降低推理采样成本。
   - 来源: [HuggingFace Daily Papers](https://huggingface.co/papers/2611.24011)

**Mind2Act World：拆解推理与执行短板，最强智能体复合任务成功率仅 12.0%**
- 论文提出诊断基准 Mind2Act World，覆盖五个真实应用领域的 30 项模拟操控任务，并通过三个难度等级及 Clean、Random 两种场景形成 180 种配置。基准分别设置 Mind、Act 和 Mind2Act 三类视图，用于判断失败源于历史认知推理、精确执行，还是二者无法通过环境反馈形成闭环组合。评测显示，最强智能体在 Mind 和 Act 任务中的成功率分别为 52.7% 和 39.0%，但复合任务成功率仅为 12.0%。
  > 💡 该基准揭示了具身系统中单项能力与组合能力之间的显著落差，环境反馈驱动的推理—执行闭环仍是关键难题。
   - 来源: [HuggingFace Daily Papers](https://huggingface.co/papers/2611.26444)

### X讨论
**Anthropic 数学家 Levent Alpöge 称与 Claude 合作找到黎曼猜想证明**
- 机器之心报道，Anthropic 数学家 Levent Alpöge 宣布，他与 Claude 合作找到了黎曼猜想的证明。相关结果在短时间内出现两份黎曼猜想证明声明，引发数学界关注。
  > 💡 目前可核验信息仅确认相关证明主张已经公开，尚不足以判断证明是否成立或已经通过同行审查。该事件更适合作为 AI 参与数学研究的重要案例观察，而不是直接视作黎曼猜想已被解决。
   - 来源: [机器之心](http://mp.weixin.qq.com/s?__biz=MzA3MzI4MjgzMw%3D%3D&mid=2651075624&idx=1&sn=03d16a0fc5490ccdb4b2d3151ef8b228&chksm=85778ab92fa1a89dbf35faf38ce6b529f94815af9d32885b208071cf6ade59854c05bf5709ed&scene=0&xtrack=1)

**报道称 Anthropic 数学家称借助 AI 模型证明黎曼猜想**
- 报道称，Anthropic 数学家 Levent Alpöge 宣称已在 Anthropic AI 模型帮助下解决黎曼猜想。该主张来自其个人网站上的一份文件，该文件于周五流出。黎曼猜想自 1859 年以来一直是数学界持续研究的著名未解问题，涉及黎曼 ζ 函数何时等于零。
  > 💡 个人网站上的证明文件只能说明研究主张已经公开，尚不能证明相关论证已被数学界接受。当前应关注独立核验和同行评议结果，避免把 AI 辅助形成的研究成果直接等同于既定数学结论。
   - 来源: [The Information](https://www.theinformation.com/briefings/anthropic-mathematician-says-proved-riemann-hypothesis)


---
*更新时间: 2026-11-22 08:26*