# 每日 AI 论文

生成时间：2026-10-15 04:40 UTC  ·  共 120 篇（已按 arXiv ID 去重）

来源：Hugging Face Daily Papers + arXiv（cs.AI / cs.LG / cs.CL / cs.CV）。
排序：HF 上榜、点赞、多源命中、兴趣词。兴趣词可在 `config.json` 改。

## 1. Player-1: Learning to Play from Synthetic Experience

- 分数：40.0  ·  HF 赞：54  ·  来源：huggingface + arxiv
- 兴趣命中：agent, reasoning, reinforcement learning, spec
- 作者：Mingyu Ouyang, Yiran Wang, Siyuan Hu, Xingyilang Yin, Huiqiang Sun, Guangzhi Wang, Junfu Pu, Cheng Cheng, Honghao Chen, Ying Shan, Mike Zheng Shou, Hwee Tou Ng
- 链接：[arXiv](https://arxiv.org/abs/2610.20584) · [PDF](https://arxiv.org/pdf/2610.20584) · [HF](https://huggingface.co/papers/2610.20584)

Computer-use agents have demonstrated strong capabilities in interpreting screens and executing keyboard and mouse actions. However, games, with their visually rich worlds and diverse mechanics, remain challenging and offer a demanding next step toward general digital control. Current game-agent learning pipelines often rely on large-scale demonstrations with limited coverage of dynamic game states, while scalable…

## 2. Any Time, Any Space: A World-State-Centric Framework for Agentic Video Generation

- 分数：38.0  ·  HF 赞：84  ·  来源：huggingface + arxiv
- 兴趣命中：agent, memory, benchmark
- 作者：Weijie Wang, Haomin Zhang, Ye Li, Akide Liu, Zeyu Zhang, Haoyu Zhao, Yefei He, Donny Y. Chen, Feng Chen, Bohan Zhuang
- 链接：[arXiv](https://arxiv.org/abs/2610.20571) · [PDF](https://arxiv.org/pdf/2610.20571) · [HF](https://huggingface.co/papers/2610.20571)

Long-form agentic video generation must turn a screenplay into shots that remain spatially and temporally consistent across nonconsecutive requests. Passing prompts or recent frames between shots does not provide a shared spatial frame for revisiting a scene or a time-indexed record for replaying an earlier event. We present Any Time, Any Space (ATAS), which compiles a screenplay into shot requests with explicit…

## 3. VideoJev: System One Model for Video Understanding and Interaction

- 分数：36.0  ·  HF 赞：198  ·  来源：huggingface
- 兴趣命中：agent, benchmark, language model, large language, coding, spec
- 作者：Yuhan Zhu, Xiangyu Zeng, Qingyi Si, Chenxu Yang, Yifei Li, Luozheng Qin, Junhao Zhou, Dingyu Yao, Jun Zhang, Chuanyu Qin, Zhiqiu Zhang, Yuandong Yang, Yuqi Xu, Tianyu Zhang, Hongcheng Guo, Jiaqi Wang, Nan Duan, Limin Wang
- 链接：[arXiv](https://arxiv.org/abs/2610.18615) · [PDF](https://arxiv.org/pdf/2610.18615) · [HF](https://huggingface.co/papers/2610.18615)

Visual agents must turn video observations into timely decisions to track progress and choose what to do next. Building on the emerging System One paradigm, we introduce VideoJev, a family of models that cast video understanding and interaction as structured decision tasks. We adapt pretrained multimodal large language models (MLLMs) by replacing autoregressive answer decoding with a shared head that scores temporal…

## 4. Agent-Reflex: Teaching Language Agents to Act Reflectively

- 分数：36.0  ·  HF 赞：195  ·  来源：huggingface
- 兴趣命中：agent, tool-use, reasoning, reinforcement learning, benchmark, language model, large language, spec
- 作者：Guanting Dong, Xinyu Yang, Jiajie Jin, Yuyang Hu, Xiaoshuai Song, Yifei Chen, Xiaoxi Li, Jiejun Tan, Yutao Zhu, Tat-Seng Chua, Ji-Rong Wen, Zhicheng Dou
- 链接：[arXiv](https://arxiv.org/abs/2610.17953) · [PDF](https://arxiv.org/pdf/2610.17953) · [HF](https://huggingface.co/papers/2610.17953)

Large language models have evolved from single-turn chatbots into interactive agents capable of long-horizon reasoning. In real deployments, MCP tool services can return noisy feedback and users may intervene to correct the agent, but existing methods provide limited supervision for reflection learning and failure recovery. To bridge this gap, we propose Agent-Reflex, a general training framework for incentivizing…

## 5. AesCode: Aesthetic Code Generation with Decoupled Cross-Modal Rewards

- 分数：36.0  ·  HF 赞：80  ·  来源：huggingface
- 兴趣命中：reinforcement learning, benchmark, spec, planning
- 作者：Xin Gao, Yifan Yang, Xin Li, Pan Wang, Yan Li, Muzhao Tian, Mingxi Cheng, Bei Liu, Kai Qiu, Qi Dai, Dong Chen, Yue Dong, Leandros Tassiulas, Rex Ying, Ji Li, Chong Luo
- 链接：[arXiv](https://arxiv.org/abs/2610.18860) · [PDF](https://arxiv.org/pdf/2610.18860) · [HF](https://huggingface.co/papers/2610.18860)

Generating information-rich visual artifacts such as slides, posters, and dashboards as code is appealing because the outputs are structured, editable, and verifiable. Yet code models cannot see how their choices of layout and color come together on the canvas, often limiting spatial planning and aesthetic quality. Image generators excel at visual design but can misrender requested content, making their outputs…

## 6. TPPO: Tracking-Value PPO For Language Model Reasoning

- 分数：36.0  ·  HF 赞：75  ·  来源：huggingface
- 兴趣命中：reasoning, reinforcement learning, language model, coding, spec
- 作者：Futing Wang, Chenxi Li, Jianhao Yan, Yun Luo, Zhi Wang, Yizhuo Li, Runzhe Zhan, Yu Cheng, Tao Lin
- 链接：[arXiv](https://arxiv.org/abs/2610.16794) · [PDF](https://arxiv.org/pdf/2610.16794) · [HF](https://huggingface.co/papers/2610.16794)

Proximal Policy Optimization (PPO) is widely used in reinforcement learning with verifiable rewards for language-model reasoning. While value evolution along trajectory characterizes relative token-level credit, yet standard critics often fail to track it under sparse terminal rewards. To model this evolution, we analyze the relation between successive prefix values and show that they admit a Bayesian decomposition…

## 7. WorkRover: Scaling Long-Horizon Cowork Agent Training Via Recursive Environment Evolution

- 分数：36.0  ·  HF 赞：74  ·  来源：huggingface
- 兴趣命中：agent, reinforcement learning, evaluation, benchmark
- 作者：Hang He, Linting Wang, Guanming Liu, Bo Mao, Jinxiu Liu, Yiran Suo, Maosen Zhou, Zhiheng Xi, Guanting Dong, Zhou Shao, Rui Zheng, Jie Zhou, Chengcheng Wan, Tao Gui, Qi Zhang, Xipeng Qiu, Xuanjing Huang
- 链接：[arXiv](https://arxiv.org/abs/2610.18067) · [PDF](https://arxiv.org/pdf/2610.18067) · [HF](https://huggingface.co/papers/2610.18067)

Scaling interactive environments is important for training long-horizon agents through reinforcement learning. These environments often require further testing and refinement after initial generation, and correcting defects in a task may also require updating its work context and verifier. However, existing construction pipelines offer limited support for such iterative refinement while keeping these components…

## 8. Vela: User Behavior as Supervision Sparks LLM Intelligence

- 分数：36.0  ·  HF 赞：69  ·  来源：huggingface
- 兴趣命中：agent, reinforcement learning, benchmark, language model, large language
- 作者：Yang Xiao, Yusong Sun, Haoyi Wu, Wenyang Hui, Weiqiang Hang, Luqing Wang, Zejian Wang, Zirui Tu, Jingsheng Mao, Shaobo Hu, Yang Luo, Jiale Guo, Jin Zhang, Yudan Liu, Zhaokai Luo, Ren Huan, Yao Hu, Chengyue Jiang, Wenjie Li, Chuan Mu
- 链接：[arXiv](https://arxiv.org/abs/2610.14709) · [PDF](https://arxiv.org/pdf/2610.14709) · [HF](https://huggingface.co/papers/2610.14709)

Large language models are increasingly deployed in applications that act on users' long-term behavior histories, from personal assistants to recommendation and advertising systems. These applications demand the user dimension of LLM intelligence: inferring a person's preferences, intent, and likely future actions from weeks to years of behavior data. Yet current models are trained on static text or synthetic data,…

## 9. X-Ragent: Tool-Augmented Reinforcement Learning for Evidence-Grounded Chest X-Ray Reasoning

- 分数：36.0  ·  HF 赞：66  ·  来源：huggingface
- 兴趣命中：agent, reasoning, reinforcement learning, benchmark, spec
- 作者：Yi Wang, Zhenlong Yuan, Yuchan Guo, Maolei Huang, Zijian Song, Dapeng Zhang, Rongbin Tan, Jiyuan Wang, Zhiyuan Wang, Fangfang Lin, Shuhan Song, Huawei Cao
- 链接：[arXiv](https://arxiv.org/abs/2610.16811) · [PDF](https://arxiv.org/pdf/2610.16811) · [HF](https://huggingface.co/papers/2610.16811)

Chest X-ray (CXR) interpretation often requires integrating visual findings with task-specific evidence rather than relying on direct visual recognition alone. While tool-augmented medical agents can supply such evidence via external modules, they often lack explicit mechanisms for learning when auxiliary evidence is needed and for preventing inapplicable quantitative evidence from entering diagnostic reasoning. To…

## 10. ExeWorldBench: Benchmarking Code-Based Executable 3D World Modeling

- 分数：36.0  ·  HF 赞：63  ·  来源：huggingface
- 兴趣命中：agent, reasoning, evaluation, benchmark, coding
- 作者：Xinge Peng, Zhen Fang, Ruibing Wang, Yongxuan Lv, Haodong Li, Guohui Zhang, Xiaoxiao Ma, Yiting Lu, Lin Chen, Zehui Che, Feng Zhao
- 链接：[arXiv](https://arxiv.org/abs/2610.15166) · [PDF](https://arxiv.org/pdf/2610.15166) · [HF](https://huggingface.co/papers/2610.15166)

Coding agents are increasingly evolving beyond reproducing what a world looks like toward constructing executable worlds that capture how a world works. This shift calls for executable world modeling, which integrates two core capabilities: world understanding, reasoning about the underlying structural, mechanical, and causal principles of a world, and executable realization, translating that understanding into a…

## 11. Last Secure Code Benchmark: Is the Code You Vibe Secure?

- 分数：36.0  ·  HF 赞：61  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark, coding, spec
- 作者：Tianyi Wu, Chao Ge, Peng Chen, Fengji Zhang, Yongxing Wu, Yuchong Xie, Jian Li, Chaoyuan Peng, Kaikai Zhang, Dong Huang, Mingzhe Du, Yukai Huang, Jiaheng Zhang, Terry Yue Zhuo, See-Kiong Ng
- 链接：[arXiv](https://arxiv.org/abs/2610.14766) · [PDF](https://arxiv.org/pdf/2610.14766) · [HF](https://huggingface.co/papers/2610.14766)

AI coding agents now write much of the code that ships, yet whether that code is secure remains unclear. We introduce the Last Secure Code Benchmark, a comprehensive evaluation of secure code generation by coding agents. Built from 150 real vulnerabilities, its 450 tasks span seven widely used languages (Java, C, C++, JavaScript, Python, PHP, and Go), 24 CWEs including 21 of the 2025 CWE Top 25 and 8 of the Top 10…

## 12. EviScene: Beyond "Is It AI?" for Agentic Image Factuality Assessment

- 分数：36.0  ·  HF 赞：47  ·  来源：huggingface
- 兴趣命中：agent, benchmark, spec, retrieval
- 作者：ZiAn Wang, Ruiqi Liu, Zhengbo Zhang, Yi Han, Jialiang Shen, Ruoxin Chen, Manni Cui, Ximo Zhu, Jin Jiang, Mingzhe Liu, Linhao Wang, Wenhao Wang, Shu Wu
- 链接：[arXiv](https://arxiv.org/abs/2610.14609) · [PDF](https://arxiv.org/pdf/2610.14609) · [HF](https://huggingface.co/papers/2610.14609)

Determining whether an image is AI-generated does not establish whether the situation it depicts is factually supported. We formulate Image Factuality Assessment: given an image and a generic verification instruction, a system returns a supported or refuted verdict with an evidence-grounded explanation. Without a supplied textual claim, the system must progressively refine factual questions during investigation and…

## 13. Learning How to Remember: Memory Modality Selection for GUI Agents

- 分数：36.0  ·  HF 赞：41  ·  来源：huggingface
- 兴趣命中：agent, memory, benchmark, language model
- 作者：Taeyun Roh, Suhyeong Park, Gijin Kim, Wonjune Jang, Jaewoo Kang
- 链接：[arXiv](https://arxiv.org/abs/2610.17928) · [PDF](https://arxiv.org/pdf/2610.17928) · [HF](https://huggingface.co/papers/2610.17928)

Recent advances in vision-language models (VLMs) have substantially improved the capabilities of GUI agents, while memory augmentation has emerged as a promising approach for reusing knowledge from past interactions. However, existing memory augmented GUI agents typically adopt a fixed representation strategy, providing retrieved experience as a static modality. It remains unclear whether a single memory modality is…

## 14. Jeva: System One Models from First Principles

- 分数：34.0  ·  HF 赞：270  ·  来源：huggingface
- 兴趣命中：memory, evaluation, spec
- 作者：Qi Li, Xinchao Wang
- 链接：[arXiv](https://arxiv.org/abs/2610.18773) · [PDF](https://arxiv.org/pdf/2610.18773) · [HF](https://huggingface.co/papers/2610.18773)

System one models enable direct, low-latency decision-making. Yet recent practice of predicting an answer from serialized text does not, by itself, respect the structure of a decision problem. We argue that current designs underemphasize four important structural requirements. (i) null-aware: Models should distinguish answer absence from uncertainty among candidates; (ii) permutation-invariant: Reordering…

## 15. Urbex: Agentic Spatial Grounding for City-Scale 3D Scenes

- 分数：34.0  ·  HF 赞：111  ·  来源：huggingface
- 兴趣命中：agent, tool-use, reinforcement learning
- 作者：Yu Wang, Rui Dai, Wei Chen, Yi Wang, Bo Dang, Kaikui Liu, Xiangxiang Chu, Yansheng Li
- 链接：[arXiv](https://arxiv.org/abs/2610.18356) · [PDF](https://arxiv.org/pdf/2610.18356) · [HF](https://huggingface.co/papers/2610.18356)

City-scale 3D grounding is commonly formulated as candidate ranking, which requires precomputed instance proposals and becomes inefficient in large outdoor scenes. We propose Urbex, an agentic vision-language framework that instead casts grounding as active spatial search. Urbex represents a city-scale 3D scene as an interactive multi-view environment, allowing a VLM agent to query landmarks, zoom into local…

## 16. Harness^2: Recursive Agent Harnessing for an Open World

- 分数：34.0  ·  HF 赞：87  ·  来源：huggingface
- 兴趣命中：agent, benchmark, spec
- 作者：Ruiyao Xu, Yanfei Chen, Zhongying CuiZhu, Bhavana Dalvi Mishra, Yifei Ming, Han Yu, Rujun Han, Chen-Yu Lee, Tomas Pfister
- 链接：[arXiv](https://arxiv.org/abs/2610.14224) · [PDF](https://arxiv.org/pdf/2610.14224) · [HF](https://huggingface.co/papers/2610.14224)

LLM agents' capabilities depend not only on their underlying models but also on their execution harnesses. Recursive self-improvement (RSI) offers a promising approach to automatically evolve these harnesses. However, deploying RSI in open-world settings still faces two critical challenges. First, open-world tasks are typically unseen during the harness design phase and novel at test time, leaving no ground-truth…

## 17. Scoring Higher, Answering Worse: Mitigating Reward Hacking in Rubric-Based RL via Protocol-Level Rubrics

- 分数：34.0  ·  HF 赞：60  ·  来源：huggingface
- 兴趣命中：reinforcement learning, benchmark, language model
- 作者：Maoqi Liu, Junwei He, Bowen Zhang, Feiran Li, Wentao Ma, Rongyi Lin, Shuhan Zhong, Quan Fang
- 链接：[arXiv](https://arxiv.org/abs/2609.38847) · [PDF](https://arxiv.org/pdf/2609.38847) · [HF](https://huggingface.co/papers/2609.38847)

Rubric-based reinforcement learning (Rubric-RL) trains language models where no verifier exists. A judge checks each criterion of a rubric, and the verdicts are aggregated into a reward, most often by a weighted sum. We show that this additive aggregation is the weak point. Under a sum, criteria compensate for one another: a policy that misses the one decision that matters can buy the points back with advice nobody…

## 18. UltraBERT: Beyond the Limit of BERT Pre-Training

- 分数：34.0  ·  HF 赞：52  ·  来源：huggingface
- 兴趣命中：language model, large language, retrieval
- 作者：Jungwoo Park, Taewhoo Lee, Jaewoo Kang
- 链接：[arXiv](https://arxiv.org/abs/2610.15028) · [PDF](https://arxiv.org/pdf/2610.15028) · [HF](https://huggingface.co/papers/2610.15028)

Recent bidirectional encoders have been modernized with innovations from causal large language models (LLMs). However, the pretraining recipe itself remains inherited from small-scale conventions, leaving encoders underoptimized, with no single model performing competitively across both classification and retrieval tasks. In this work, we investigate how far encoder performance can be pushed by revisiting core…

## 19. Tev: Scaling Long-Horizon Agentic Environments with Dense Progress Rewards

- 分数：32.0  ·  HF 赞：96  ·  来源：huggingface
- 兴趣命中：agent, spec
- 作者：Wenbo Hu, Shraman Pramanick, Krishna Kumar Singh, Nanyun Peng, Kai-Wei Chang, Yong Jae Lee
- 链接：[arXiv](https://arxiv.org/abs/2610.18868) · [PDF](https://arxiv.org/pdf/2610.18868) · [HF](https://huggingface.co/papers/2610.18868)

Long-horizon agents have drawn growing attention for their ability to work autonomously -- from hours to days -- on economically valuable tasks, a capability essential to automated discovery and recursive self-improvement (RSI). Yet open-source models still struggle on long-horizon tasks, largely for lack of both training data and a working recipe, and scaling both is hard: long, complex tasks are difficult to…

## 20. DoSA: Dots Sparse Attention

- 分数：32.0  ·  HF 赞：67  ·  来源：huggingface
- 兴趣命中：evaluation, spec
- 作者：Fanxu Meng, Taosong Fang
- 链接：[arXiv](https://arxiv.org/abs/2610.13990) · [PDF](https://arxiv.org/pdf/2610.13990) · [HF](https://huggingface.co/papers/2610.13990)

Sparse attention visits few keys, yet finding them can still require scoring every key with every indexer head. We introduce DoSA (Dots Sparse Attention), a lossless method for making this computation conditional while preserving exact token selection. Its central observation is that Top-K selection requires sufficient evidence to reject a candidate, not necessarily its full score. A seed set supplies a lower bound…

## 21. SALD: Self-Referenced Advantage Learning for Diffusion Models

- 分数：32.0  ·  HF 赞：47  ·  来源：huggingface
- 兴趣命中：memory, spec
- 作者：Aryan Das, Surjo Dey, Koushik Biswas, Swalpa Kumar Roy, Moloud Abdar, Arnab Bhattacharya, Vinay Kumar Verma
- 链接：[arXiv](https://arxiv.org/abs/2610.01496) · [PDF](https://arxiv.org/pdf/2610.01496) · [HF](https://huggingface.co/papers/2610.01496)

Recent work on language-model adaptation has shown that single models can obtain informative training signals by evaluating their behavior in demonstrationor feedback-augmented contexts, with the help of a teacher network, which is driven by the student's learned parameters. Inspired by this internal-reference principle, we investigate how diffusion models can identify self-referenced training signals without…

## 22. LatentLoop: Scaling Looped MoE Models with Asymmetric Compute Allocation

- 分数：31.0  ·  HF 赞：34  ·  来源：huggingface + arxiv
- 兴趣命中：benchmark
- 作者：Zefeng He, Yunkai Chai, Xiaoyang Chen, Tong Zhu, Zongliang Wu, Yun Luo, Yafu Li, Yu Cheng
- 链接：[arXiv](https://arxiv.org/abs/2610.19975) · [PDF](https://arxiv.org/pdf/2610.19975) · [HF](https://huggingface.co/papers/2610.19975)

Looped Mixture-of-Experts (MoE) models combine parameter reuse with sparse computation to improve performance under matched budgets. Prior work demonstrates that different loop visits can play different roles even when they share parameters. To probe the contributions of different loop visits, we learn separate residual coefficients in a model that applies a shared block twice, observing a smaller scale in the first…

## 23. GreenWAM: A World Foundation Model for Robotics

- 分数：30.0  ·  HF 赞：82  ·  来源：huggingface
- 兴趣命中：spec
- 作者：Gennady Sidorov, Valerii Kornilov, Denis Grankin, Polina Fedotova, Aleksey Postnikov
- 链接：[arXiv](https://arxiv.org/abs/2610.18774) · [PDF](https://arxiv.org/pdf/2610.18774) · [HF](https://huggingface.co/papers/2610.18774)

A robot needs a world model that predicts how its actions will change the scene and a policy that chooses those actions. Models are usually built and evaluated for only one of these roles, and every robot records its actions in its own format. We ask whether one robot world model can serve both roles across different bodies, and what makes this work. We present GreenWAM, a world foundation model for robotics,…

## 24. LeWAM: End-to-End World and Action Modeling with JEPAs

- 分数：30.0  ·  HF 赞：63  ·  来源：huggingface
- 兴趣命中：planning
- 作者：Minghao Fu, Tavis Siebert, Eryk Halicki, Randall Balestriero
- 链接：[arXiv](https://arxiv.org/abs/2610.12818) · [PDF](https://arxiv.org/pdf/2610.12818) · [HF](https://huggingface.co/papers/2610.12818)

Joint-embedding predictive architectures (JEPAs) learn compact latent world models without pixel reconstruction. Existing JEPA pipelines typically train visual representations and action-conditioned dynamics before adding a control policy or solver. We introduce LeWAM, an end-to-end JEPA for control with: (1) a joint training objective over next latent state prediction and action flow matching, and (2) an isotropic…

## 25. Multics: Generative Multi-Player World Model with Hierarchical Communication

- 分数：30.0  ·  HF 赞：56  ·  来源：huggingface
- 兴趣命中：spec
- 作者：Kaiyi Huang, Wangbo Yu, Yukun Huang, Jiwen Yu, Kunhao Liu, Donglin Yang, Wenbo Hu, Ying Shan, Xihui Liu
- 链接：[arXiv](https://arxiv.org/abs/2610.17201) · [PDF](https://arxiv.org/pdf/2610.17201) · [HF](https://huggingface.co/papers/2610.17201)

Multi-player interactive world models aim to simulate shared environments from multiple players' perspectives, but achieving robust generation while scaling to more players remains challenging. Existing approaches that rely on fully-connected communication (e.g., Solaris) incur quadratic attention costs as the number of players grows, while centralized approaches (e.g., γ-World) suffer from interference between…

## 26. LensErase: A Foundation Model for Erase Anything

- 分数：29.0  ·  HF 赞：26  ·  来源：huggingface
- 兴趣命中：reinforcement learning, evaluation, benchmark, coding, spec
- 作者：Yunuo Chen, Xiuyu Wu, Qinhong Yang, Jinjing Zhao, Yanchen Dong, Sirui Zhang, Dong Chen, Fangyun Wei, Lei Shi, Ji Li, Dongdong Chen, Guo Lu, Yan Lu, Baining Guo
- 链接：[arXiv](https://arxiv.org/abs/2610.18072) · [PDF](https://arxiv.org/pdf/2610.18072) · [HF](https://huggingface.co/papers/2610.18072)

We introduce LensErase, a general-purpose mask-based Erase Anything foundation model designed to cover a broad spectrum of real-world erase scenarios. LensErase supports diverse objects, visual text, watermarks, associated visual effects, multiple-object removal, and a wide range of object scales, aspect ratios, and image resolutions. First, to enable such broad coverage, we construct LensErase-100M, a large-scale…

## 27. Seeing, Maintaining, and Learning: The Evolution of Multimodal Agent Memory

- 分数：29.0  ·  HF 赞：26  ·  来源：huggingface
- 兴趣命中：agent, memory, reasoning, spec
- 作者：Minghao Guo, Qingyue Jiao, Xiujin Liu, Jianhong Pang, Ruimeng Yang, Naihao Xu, Liwei Che, Haochen Xue, Ziqi Wang, Xinying Cai, Jiaxuan Luo, Jiaxin Deng, Xuesong Ye, Jintao Qu, Wenyao Gao, Jingwen Gu, Chenyang Zhao, Shichun Liu, Guibin Zhang, Zefang Liu, Siyin Wang, Wujiang Xu, Danrui Li, Zeru Shi, Woongyeong Yeo, Shuang Liu, Wei-Chieh Huang, Weizhi Zhang, Tianyu Yang, Kangsan Kim, Yebowen Hu, Bowen Wen, Bowen Jiang, Haohao Su, Ming Yin, Sheldon Yu, Mian Zhang, Yuyan Chen, Hanrong Zhang, Kai Mei, Zihao Zhang, Mingyu Jin, Xi Zhu, Hengyi Wang, Tianxin Wei, Linyong Nan, Zhenwen Liang, Zhendong Chu, Ziqi Huang, Yongye Su, Sixun Dong, Shujian Liu, Kaiqu Liang, Jiaojiao Han, Zhaoye Fei, Kun Wang, Shihan Dou, Zhichun Guo, Xingjian Diao, Zeqi Gu, Heng Wang, Tao Feng, Cheng Qian, Hamid Palangi, Silei Xu, Xi Yun, Yi Zhu, Shilong Liu, Qingsong Wen, Sung Ju Hwang, Zuxuan Wu, Yu-Gang Jiang, Yiyu Shi, Dimitris N. Metaxas, Jiaxuan You, Julian McAuley, Mengdi Wang, Jiawei Han, Philip S. Yu, Ziyi Ye
- 链接：[arXiv](https://arxiv.org/abs/2610.19366) · [PDF](https://arxiv.org/pdf/2610.19366) · [HF](https://huggingface.co/papers/2610.19366)

Multimodal models and agents have emerged to enable AI systems to learn from and interact with the real world more like humans by integrating information across multiple modalities. However, enabling multimodal agents to continually acquire useful information from complex, heterogeneous multimodal data remains a significant challenge as they move toward long-horizon tasks and lifelong settings. Addressing this…

## 28. VEDJE: Video-Efficient Discriminative Joint Encoder for Scalable Video-Text Retrieval

- 分数：28.5  ·  HF 赞：37  ·  来源：huggingface
- 兴趣命中：retrieval
- 作者：Shahaf Wagner, Gabriele Serussi, Dan Ben Ami, Tomer Galanti, Chaim Baskin
- 链接：[arXiv](https://arxiv.org/abs/2610.11850) · [PDF](https://arxiv.org/pdf/2610.11850) · [HF](https://huggingface.co/papers/2610.11850)

Finding the right video often requires distinguishing similar scenes in which different events occur. Joint matching improves retrieval, but processing rich video representations for each query is costly. VEDJE compresses features within sampled frames while keeping their representations separate in a reusable cache. Feature-change prediction supplies an auxiliary training signal that improves retrieval from the…

## 29. A Decade in a Day: Synthesizing Agent-Native Interfaces from Human-Oriented Software Evolution

- 分数：28.5  ·  HF 赞：25  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark, language model, large language, spec
- 作者：Alan Wu, Wei Tao, Yiwen Guo
- 链接：[arXiv](https://arxiv.org/abs/2610.15765) · [PDF](https://arxiv.org/pdf/2610.15765) · [HF](https://huggingface.co/papers/2610.15765)

Large language model agents are emerging as an important new class of users of desktop applications. However, existing desktop interfaces were designed for human end users or application developers, leaving agents to interpret visual controls or discover and compose low-level software operations. This mismatch can hinder even capable agents, yet it remains unclear what interface properties make desktop software…

## 30. AReA: Adaptive Receptive-Field Attention for Efficient High-Resolution Diffusion Transformers

- 分数：28.0  ·  HF 赞：46  ·  来源：huggingface
- 兴趣命中：-
- 作者：Javad Rajabi, Koorosh Roohi, David B. Lindell, Babak Taati
- 链接：[arXiv](https://arxiv.org/abs/2610.17227) · [PDF](https://arxiv.org/pdf/2610.17227) · [HF](https://huggingface.co/papers/2610.17227)

Generating images beyond the training resolution of Diffusion Transformers (DiTs) remains challenging, as the number of tokens grows rapidly with resolution, full attention becomes expensive, and outputs often suffer from structural distortions and degraded detail. We identify uniform full attention as the common source of both problems. Attending to all tokens at every step causes quadratic cost and exposes the…

## 31. APEX: Asynchronous Prefix Denoising for Extreme Compression

- 分数：28.0  ·  HF 赞：43  ·  来源：huggingface
- 兴趣命中：-
- 作者：David Dinkevich, Nisan Chiprut, Yoav HaCohen, Dani Lischinski
- 链接：[arXiv](https://arxiv.org/abs/2610.12843) · [PDF](https://arxiv.org/pdf/2610.12843) · [HF](https://huggingface.co/papers/2610.12843)

Fewer latent tokens promise cheaper diffusion. Yet aggressive latent compression creates a reconstruction-generation dilemma: adding channels improves reconstruction but makes generation harder. We introduce APEX, short for Asynchronous Prefix denoising for EXtreme compression, which pairs a hierarchical latent space with asynchronous denoising over channel groups. Our autoencoder orders channel prefixes from…

## 32. Self-Distillation with Verbal Regularization

- 分数：27.5  ·  HF 赞：27  ·  来源：huggingface
- 兴趣命中：reasoning, language model, large language
- 作者：Jiazheng Li, Yawei Li, Junru Lu, Zhenyi Shen, Di Yin, Lin Gui, Xing Sun, David Rügamer, Xinpeng Wang, Yulan He
- 链接：[arXiv](https://arxiv.org/abs/2610.16354) · [PDF](https://arxiv.org/pdf/2610.16354) · [HF](https://huggingface.co/papers/2610.16354)

On-policy self-distillation (OPSD) trains a large language model using supervision from a teacher instantiated from the same model as the student. The teacher is conditioned on privileged information (PI), such as verified solutions. The student, which does not observe PI, learns from the teacher's next-token distributions along its own sampled responses. However, PI can bias supervision toward shortcut reasoning…

## 33. DeltaTTG: Training Multi-Turn Agents with a Token-to-Go Progress Meter

- 分数：27.5  ·  HF 赞：27  ·  来源：huggingface
- 兴趣命中：agent, reinforcement learning, spec
- 作者：Xuyan Ye, Xiyan Fu, Shengda Fan, Jiawei Cui, Yankai Lin, Wei Lu
- 链接：[arXiv](https://arxiv.org/abs/2610.17666) · [PDF](https://arxiv.org/pdf/2610.17666) · [HF](https://huggingface.co/papers/2610.17666)

Reinforcement learning with verifiable rewards (RLVR) for multi-turn agents relies on sparse terminal rewards that say little about individual steps. Within-group step comparisons depend on reliable state matching and sufficiently diverse sampled outcomes, while direct step scoring may require costly external evaluators, human annotations, or task-specific heuristics. We introduce DeltaTTG to learn a reusable…

## 34. Data-Centric Recursive Self-Improvement for Navigation via Policy-Synchronized Language-Action Dual Bootstrapping

- 分数：26.5  ·  HF 赞：25  ·  来源：huggingface
- 兴趣命中：agent, reasoning, spec
- 作者：Songze Li, Haoming Gu, Ziyang Gong, Zhitong Wang, Gengze Zhou, Zun Wang, Yuhan Zhu, Tianxiang Jiang, Juanzi Li, Qi Wu, Weinan Zhang, Yu Qiao, Wenwei Zhang, Yi Wang
- 链接：[arXiv](https://arxiv.org/abs/2610.15782) · [PDF](https://arxiv.org/pdf/2610.15782) · [HF](https://huggingface.co/papers/2610.15782)

Vision-language navigation requires agents to follow natural-language instructions to reach target locations, making high-quality language supervision essential. Since human annotation is costly, prior work has explored scalable data synthesis methods. However, existing methods typically either use separate models for navigation and instruction generation or couple the two tasks through task-specific components;…

## 35. ClawLoop: Self-Improving Agents via Harness-Native Training Loop

- 分数：26.5  ·  HF 赞：21  ·  来源：huggingface
- 兴趣命中：agent, tool-use, evaluation, benchmark, language model, large language
- 作者：Hansi Yang, Linji Hao, Hongyan Hao, An Wang, Han Wu, Qi Gu, Xunliang Cai
- 链接：[arXiv](https://arxiv.org/abs/2610.14118) · [PDF](https://arxiv.org/pdf/2610.14118) · [HF](https://huggingface.co/papers/2610.14118)

The rapid advancement of Large Language Models (LLMs) has driven their deployment toward general-purpose harness environments, where LLM-based agents operate in sandbox workspaces and interact directly with file systems and shells. While numerous post-training pipelines exist for tool-use agents, their counterparts for harness-based agents remain scarce and are predominantly one-shot and teacher-dependent: a…

## 36. CineRecon: Benchmarking Frontier Models for Agentic Cinematic Reconstruction

- 分数：26.5  ·  HF 赞：21  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark, spec
- 作者：Jialei Wang, Zehan Wang, XiaoYang Wu, Ziang Zhang, Siyu Chen, Jiaer Huang, Yujia Zhang, Tianyu Pang, Hengshuang Zhao
- 链接：[arXiv](https://arxiv.org/abs/2610.16577) · [PDF](https://arxiv.org/pdf/2610.16577) · [HF](https://huggingface.co/papers/2610.16577)

Reconstructing reference videos as editable dynamic 3D scenes is an important path toward controllable video generation for filmmaking: these scenes provide modifiable, renderable visual proxies that enable explicit control over scene layout, subject actions, and camera behavior. To evaluate agents' ability to reconstruct editable dynamic 3D scenes from dynamic reference videos, we introduce CineRecon, a benchmark…

## 37. Recovering Reliable Supervision via Critique-Guided On-Policy Distillation

- 分数：26.5  ·  HF 赞：21  ·  来源：huggingface + arxiv
- 兴趣命中：reasoning, benchmark
- 作者：Kaixiang Zhao, Tianrun Yu, Shangzhe Li, Yuxiao Yang, Amanda Hughes, Weitong Zhang, Taylor W. Killian
- 链接：[arXiv](https://arxiv.org/abs/2610.20572) · [PDF](https://arxiv.org/pdf/2610.20572) · [HF](https://huggingface.co/papers/2610.20572)

On-policy distillation (OPD) trains a student model on its own rollouts with token-level supervision from a teacher, assuming that the teacher can reach a correct answer from any prefix the student writes. We call this property the recoverability of the teacher and show it fails on incorrect rollouts: the teacher follows student errors, although it recognizes them. We propose CriticOPD, using error recognition to…

## 38. JevGPT: Thinking Fast and Slow in Autonomous Research

- 分数：26.0  ·  HF 赞：20  ·  来源：huggingface
- 兴趣命中：agent, spec, planning, retrieval
- 作者：Yasheng Sun, Yanning Dai, Yimeng Chen, Nanbo Li, Firas Laakom, Yifan Xu, Piotr Piękos, Mateusz Ostaszewski, Wenyi Wang, Cheng Luo, Yuhui Wang, Jürgen Schmidhuber
- 链接：[arXiv](https://arxiv.org/abs/2610.18272) · [PDF](https://arxiv.org/pdf/2610.18272) · [HF](https://huggingface.co/papers/2610.18272)

Autonomous research agents must acquire and reason over evidence within a limited budget. Yet relevant sources can remain uninspected or unused, leaving a gap between retrieval coverage and the evidence that informs research. The challenge is to align fast local judgments with changing evidence needs and feed their findings back into research decisions. We introduce JevGPT, a dual-system architecture for autonomous…

## 39. VIEWCRAFT: Evolving What Multimodal Agents See and How They Read It

- 分数：25.5  ·  HF 赞：23  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark
- 作者：Binxiao Xu, Ruichuan An, Bocheng Zou, Weihua Du, Xinyu Wei, Hangyu Guo, YiFan Zhang, Renye Yan, Chengqi Duan, Hang Hua
- 链接：[arXiv](https://arxiv.org/abs/2610.15915) · [PDF](https://arxiv.org/pdf/2610.15915) · [HF](https://huggingface.co/papers/2610.15915)

Reusable skills improve multimodal agents without updating model weights, but their effectiveness depends on both the evidence presented and the procedure used to read it. We introduce ViewCraft, which jointly evolves an executable evidence interface and its reading procedure. The interface selects, transforms, and organizes observations; the reader interprets the resulting views. Failure traces guide revisions,…

## 40. Open-o3-Video-v2: Seek, Ground, and Reason with Verifiable Spatio-Temporal Evidence

- 分数：25.5  ·  HF 赞：19  ·  来源：huggingface
- 兴趣命中：agent, reasoning, reinforcement learning, benchmark, spec, retrieval
- 作者：Jiahao Meng, Zhongyuan Bao, Yue Tan, Haiquan Wen, Renrui Zhang, Anna Wang, Jason Li, Yanwei Fu, Yunhai Tong, Ming-Hsuan Yang
- 链接：[arXiv](https://arxiv.org/abs/2610.17656) · [PDF](https://arxiv.org/pdf/2610.17656) · [HF](https://huggingface.co/papers/2610.17656)

Reliable video reasoning requires models to produce correct answers and expose supporting visual evidence. Open-o3-Video enables verifiable reasoning by embedding timestamps and object-level bounding boxes into reasoning traces, but is restricted to frames from an initial sparse sampler. We introduce Open-o3-Video-v2, which formulates video reasoning as a unified agentic evidencegrounded process. The model…

## 41. FlashVSR+: Efficient Video Super-Resolution via Hybrid Attention and Reward-Yield Distribution Matching

- 分数：25.0  ·  HF 赞：30  ·  来源：huggingface
- 兴趣命中：memory
- 作者：Ruchang Yao, Shi Guo, Junhao Zhuang, Mingde Yao, Xin Cai, Jiahao Zhan, Bin Fu, Xinyuan Chen, Yu Qiao, Tianfan Xue
- 链接：[arXiv](https://arxiv.org/abs/2610.17552) · [PDF](https://arxiv.org/pdf/2610.17552) · [HF](https://huggingface.co/papers/2610.17552)

Recent video super-resolution (VSR) models achieve efficient one-step generation through diffusion distillation. However, high-resolution inference remains costly, and distilled models are difficult to align with human preferences. These challenges call for improvements in both model architecture and training strategy. We present FlashVSR+ to address both limitations. On the architecture side, we introduce hybrid…

## 42. WAVE-0: Bridging VLA Policies and WAMs with Lightweight Latent Future Prediction

- 分数：24.0  ·  HF 赞：24  ·  来源：huggingface
- 兴趣命中：spec, planning
- 作者：Haomin Wang, Anqiong Ji, Ke Wang, Zhongshan Liu, Ru Ying, Ran Zheng, Zhipeng Zhang
- 链接：[arXiv](https://arxiv.org/abs/2610.18568) · [PDF](https://arxiv.org/pdf/2610.18568) · [HF](https://huggingface.co/papers/2610.18568)

Vision-language-action (VLA) policies excel at generalist robotic manipulation but generate actions without explicitly modeling their environmental consequences. World action models (WAMs) incorporate future prediction, yet most rely on costly video generation, while latent alternatives either use predicted futures only as auxiliary targets or infer latent actions from suboptimal visual transitions through costly…

## 43. LifeSearch: Benchmarking Deep Research Agents for Real-World Life and Productivity

- 分数：23.5  ·  HF 赞：15  ·  来源：huggingface
- 兴趣命中：agent, reasoning, evaluation, benchmark, spec
- 作者：Yibo Wang, Senjie Jin, Yansong Ning, Xinbing Liang, Haotian Luo, Jiazheng Zhang, Yuxuan He, Will Wu, Clarenceai
- 链接：[arXiv](https://arxiv.org/abs/2610.18092) · [PDF](https://arxiv.org/pdf/2610.18092) · [HF](https://huggingface.co/papers/2610.18092)

Deep research (DR) agents address open-ended information needs through multi-step reasoning, long-horizon web search, and evidence synthesis. However, existing benchmarks primarily focus on academic research or synthetic tasks, leaving DR agents' capabilities in real-world life and professional productivity settings insufficiently evaluated. To bridge this gap, we introduce LifeSearch, a challenging benchmark…

## 44. Doc2Harness: Benchmarking LLMs on Long-Horizon Harness Engineering of Coding Agents

- 分数：23.5  ·  HF 赞：7  ·  来源：huggingface + arxiv
- 兴趣命中：agent, benchmark, language model, large language, coding
- 作者：Yuyao Ge, Shenghua Liu, Peizhong Gao, Chendi Ge, Chenxu Liu, Yiwei Wang, Lingrui Mei, Baolong Bi, Jiayu Yao, Jiafeng Guo, Xueqi Cheng
- 链接：[arXiv](https://arxiv.org/abs/2610.20344) · [PDF](https://arxiv.org/pdf/2610.20344) · [HF](https://huggingface.co/papers/2610.20344)

Agents driven by large language models are increasingly deployed on long-horizon tasks, where they use tools and modify real workspaces. How well they perform depends as much on the harness around the model as on the model itself. Existing benchmarks measure downstream task success under a fixed harness, leaving harness engineering itself unexplored. We propose Doc2Harness, a two-stage benchmark that evaluates…

## 45. PhyProbe: Rethinking Physical Consistency Evaluation in Generated Videos

- 分数：23.0  ·  HF 赞：14  ·  来源：huggingface
- 兴趣命中：evaluation, benchmark, language model, spec
- 作者：Max Ku, Jiaojiao Fan, Zekun Hao, Francesco Ferroni, Heng Wang, Wenhu Chen, Ming-Yu Liu, Prithvijit Chattopadhyay
- 链接：[arXiv](https://arxiv.org/abs/2609.38377) · [PDF](https://arxiv.org/pdf/2609.38377) · [HF](https://huggingface.co/papers/2609.38377)

Evaluating the physical consistency of generated videos remains a fundamental challenge. Existing approaches rely on off-the-shelf vision-language models, which can often be myopic to physical dynamics, or fine-tuned evaluators trained on human annotations, which overfit to dataset-specific cues and fail to generalize. A key challenge is that existing supervision sources provide either relative ordering or absolute…

## 46. Elephant in the Fridge: Constant-Memory Frame Packing for Long Video Understanding

- 分数：22.5  ·  HF 赞：13  ·  来源：huggingface
- 兴趣命中：memory, context window, benchmark, language model, coding, spec
- 作者：Shuo Gao, Chenhao Zheng, Zhongzheng Ren
- 链接：[arXiv](https://arxiv.org/abs/2610.16118) · [PDF](https://arxiv.org/pdf/2610.16118) · [HF](https://huggingface.co/papers/2610.16118)

Hour-long videos, streaming feeds, and movie-length content are pushing vision-language models (VLMs) past their breaking point -- the standard recipe of encoding each frame into visual tokens yields sequences that grow linearly with video length, causing prohibitive memory consumption and inference latency. Existing approaches, such as token reduction and keyframe selection, shorten the token sequence but leave the…

## 47. Hybrid Reasoning Agents

- 分数：22.5  ·  HF 赞：13  ·  来源：huggingface
- 兴趣命中：agent, memory, reasoning, benchmark, spec
- 作者：Jiaru Zou, Yunzhe Qi, Sirui Chen, Federico Bianchi, Shang Zhu, Pan Lu, Jingrui He, James Zou
- 链接：[arXiv](https://arxiv.org/abs/2610.18861) · [PDF](https://arxiv.org/pdf/2610.18861) · [HF](https://huggingface.co/papers/2610.18861)

How can we build an agent that thinks beyond human language, yet still acts through it in the external environment? Modern LLM agents still reason and interact through text, while latent reasoning offers an efficient internal medium but lacks native tool access and reasoning transparency. We bridge these two directions with Hybrid Reasoning Agents (HybridAgents), which dynamically navigate between latent reasoning…

## 48. ReTerm: Recovery Training for Self-Improving Terminal Agents

- 分数：22.0  ·  HF 赞：20  ·  来源：huggingface
- 兴趣命中：agent, coding
- 作者：Wei Xie, Kaituo Feng, Shiming Fu, Yong Liu, Xiangyu Yue, Shuangjia Zheng
- 链接：[arXiv](https://arxiv.org/abs/2610.18484) · [PDF](https://arxiv.org/pdf/2610.18484) · [HF](https://huggingface.co/papers/2610.18484)

Terminal agents have shown strong abilities in complex coding tasks. However, they often struggle to recover from errors during long-running execution (e.g., command errors, faulty implementations), eventually leading to task failures. To this end, we present ReTerm, a self-improving terminal agent trained by learning how to recover from its own failed terminal tasks. To support its training, we construct a…

## 49. APT: Feedback-Driven Agentic Post-Training for Text-to-Image Generation

- 分数：22.0  ·  HF 赞：12  ·  来源：huggingface
- 兴趣命中：agent, reinforcement learning, evaluation, benchmark, spec
- 作者：Sirui Zhang, Fangyun Wei, Dong Chen, Jinjing Zhao, Yitong Wang, Yunuo Chen, Baining Guo, Zheng-Jun Zha
- 链接：[arXiv](https://arxiv.org/abs/2610.18097) · [PDF](https://arxiv.org/pdf/2610.18097) · [HF](https://huggingface.co/papers/2610.18097)

Post-training is crucial for improving text-to-image models, yet existing pipelines typically rely on manually curated training data and fixed training distributions. We introduce APT (Agentic Post-Training), a fully automated framework that adaptively post-trains a base model according to its evolving capability profile. APT coordinates three agents to construct evaluation sets from user requirements, diagnose…

## 50. Spectral-Driven Adaptive-Rank Optimizer for Large Language Model Reinforcement Learning with Verifiable Rewards

- 分数：21.0  ·  HF 赞：10  ·  来源：huggingface
- 兴趣命中：reasoning, reinforcement learning, language model, large language, spec
- 作者：Zhipeng Chen, Wayne Xin Zhao, Ji-Rong Wen
- 链接：[arXiv](https://arxiv.org/abs/2610.16533) · [PDF](https://arxiv.org/pdf/2610.16533) · [HF](https://huggingface.co/papers/2610.16533)

Reinforcement learning with verifiable rewards (RLVR) is reshaping how large language models (LLMs) acquire reasoning capabilities, yet the optimizers used remain largely inherited from teacher-forcing training. This raises a fundamental question: does RLVR induce a distinct optimization geometry that calls for a different optimizer? We investigate this question through the spectral structure of LLM gradients and…

## 51. SWE-MISBEHAVIOR: Benchmarking and Mitigating Boundary Violations in Software Coding Agents

- 分数：21.0  ·  HF 赞：10  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark, coding
- 作者：Do Xuan Trong, Duc Anh Nguyen, Do Xuan Long, Ngoc-Hai Nguyen, Tongyao Zhu, Duy Dinh, Cayden Chik, Cuong Dang, Jiaying Wu, Xuan-Phi Nguyen, Vinh Van Nguyen, Kenji Kawaguchi, Shafiq Joty, Nancy F. Chen, Min-Yen Kan
- 链接：[arXiv](https://arxiv.org/abs/2610.18206) · [PDF](https://arxiv.org/pdf/2610.18206) · [HF](https://huggingface.co/papers/2610.18206)

We present SWE-MISBEHAVIOR, the first taxonomy and evaluation framework for diagnosing boundary-violating misbehaviors in coding agents. It contains 7.4K human-in-the-loop synthesized samples spanning three layers of agent action space: (i) Code Generation, (ii) File Management, and (iii) System Interaction. Across these categories, SWE-MISBEHAVIOR covers 11 distinct misbehaviors with a fully automated evaluation…

## 52. What Makes a Social Agent's Interactions Effective? Learning from Verifiable Outcomes in Paired Worlds

- 分数：21.0  ·  HF 赞：2  ·  来源：huggingface + arxiv
- 兴趣命中：agent, evaluation, benchmark, spec
- 作者：Caixin Kang, Ke Wang, Yuchuan Wu, Xiaoqiang Wang, Ling Li, Bingxue Qiu, Yongbin Li, Yoichi Sato
- 链接：[arXiv](https://arxiv.org/abs/2610.20195) · [PDF](https://arxiv.org/pdf/2610.20195) · [HF](https://huggingface.co/papers/2610.20195)

Effective social interaction requires more than fluent responses: agents must reach plans that fit the participants' needs and circumstances. Existing evaluations of social agents mainly rely on LLM judges that rate the conversation, without checking the resulting plan. We introduce HICO-Bench, a benchmark of 180 everyday coordination scenarios, such as resource allocation, scheduling, and authorization, in which…

## 53. Cepheid: Decoupling Scale from Structure for Cross-Family Motion Completion

- 分数：20.0  ·  HF 赞：24  ·  来源：huggingface
- 兴趣命中：-
- 作者：Chih-Hai Su, Tsung-Wei Ke, Yu-Lun Liu
- 链接：[arXiv](https://arxiv.org/abs/2610.18871) · [PDF](https://arxiv.org/pdf/2610.18871) · [HF](https://huggingface.co/papers/2610.18871)

Sparse-to-dense motion completion recovers dense mesh motion from sparse vertex displacements. Residual priors trained on one geometry family frequently fail to beat parameter-free harmonic extension off-family. Moreover, cross-family training meets a scaling barrier: residual amplitude varies by more than an order of magnitude across geometry families and collapses as observations become denser. Since this scale…

## 54. EgoExplorer: A Vision-Motion-Touch Observatory for Human Loco-Manipulation In Situ

- 分数：20.0  ·  HF 赞：20  ·  来源：huggingface
- 兴趣命中：evaluation
- 作者：Yunsong Zhou, Xuekun Jiang, Haiqi Shen, Hangxu Liu, Chaojian Shi, Yujie Liu, Jingyuan Li, Haoran Yang, Jiafei Cao, Dongzhan Zhou, Dong Wang, Yao Mu, Chunhua Shen, Weinan Zhang
- 链接：[arXiv](https://arxiv.org/abs/2610.18872) · [PDF](https://arxiv.org/pdf/2610.18872) · [HF](https://huggingface.co/papers/2610.18872)

Learning humanoid loco-manipulation from human demonstrations rests on observing how locomotion, posture, and object interaction evolve together as tasks unfold. Scaling collection across diverse environments, in turn, favors lightweight, portable capture systems. Yet, existing datasets provide only partial views of this coordination. Thus, we introduce EgoExplorer, a 100-hour vision-motion-touch observatory of…

## 55. PANINI-DR: Controlled Deep Research through Generative Semantic Workspaces

- 分数：20.0  ·  HF 赞：8  ·  来源：huggingface
- 兴趣命中：agent, memory, reasoning, benchmark, planning
- 作者：M. Yigit Turali, Shreyas Rajesh, M. Efe Lorasdagi, Chenda Duan, Kartik Sharma, Vwani Roychowdhury
- 链接：[arXiv](https://arxiv.org/abs/2610.15208) · [PDF](https://arxiv.org/pdf/2610.15208) · [HF](https://huggingface.co/papers/2610.15208)

Deep research requires connecting multiple steps of search, reasoning, and computation, with intermediate findings guiding what to investigate next. As investigations grow, agents must maintain research state across model calls and check findings before errors propagate into subsequent work. We introduce PANINI-DR, a multi-agent harness that separates coordination of the overall investigation from the research and…

## 56. Beyond Domain-Routed Supervision: Cross-Teacher Guarding for Multi-Teacher On-Policy Distillation

- 分数：19.5  ·  HF 赞：19  ·  来源：huggingface
- 兴趣命中：spec
- 作者：Shi-Yu Tian, Yong Liu, Ximan Liu, Tianrui Zhu, Sule Bai, Xinwei Yang, Ruiqi Liu, Kun-Yang Yu, Ming Yang, Zhi Zhou, Yu-Feng Li, Yipeng Sun, Gu Simiu
- 链接：[arXiv](https://arxiv.org/abs/2610.13521) · [PDF](https://arxiv.org/pdf/2610.13521) · [HF](https://huggingface.co/papers/2610.13521)

Multi-teacher on-policy distillation (MOPD) extends on-policy distillation (OPD) by routing domain-specific data to specialized teachers, integrating their capabilities through dense token-level supervision on student-generated trajectories. However, domain routing only distinguishes the supervision sources for different domains; updates from all domains still act on shared parameters. When teachers differ…

## 57. Agent Sociodrama: Social-Dynamics-Guided Persona Recasting for LLM Agent Teams

- 分数：19.5  ·  HF 赞：7  ·  来源：huggingface
- 兴趣命中：agent, benchmark, language model, large language, spec
- 作者：Yirui Qi, Xiaoming Zhang, Jaehong Yoon
- 链接：[arXiv](https://arxiv.org/abs/2610.15788) · [PDF](https://arxiv.org/pdf/2610.15788) · [HF](https://huggingface.co/papers/2610.15788)

Large language model (LLM) agents are increasingly deployed as teams, yet they fail in characteristically social ways: information holders stay silent, dominant speakers anchor groups on wrong answers, and norm violations go unsanctioned. We present Agent Sociodrama, a framework for modeling and validating evolving social dynamics in LLM agent teams. Under fixed personas, agents' emotional states and directed,…

## 58. Long-Horizon RL Needs Muon

- 分数：19.5  ·  HF 赞：3  ·  来源：huggingface + arxiv
- 兴趣命中：agent, tool use, reasoning
- 作者：Kai Ruan, Jinghao Lin, Tao Chen, Ziqi Zhou, Qianshan Wei, Zihe Huang
- 链接：[arXiv](https://arxiv.org/abs/2610.20256) · [PDF](https://arxiv.org/pdf/2610.20256) · [HF](https://huggingface.co/papers/2610.20256)

Long-horizon agents must coordinate reasoning, tool use, and environment feedback over extended interactions. Learning from sparse outcome rewards requires weighting trajectories of different lengths and updating the policy while rollouts are still being collected. We examine a single-rollout asynchronous recipe combining Muon, token-averaged loss, truncated importance sampling, and auxiliary length and tool-error…

## 59. Fish Audio Drama 3 Technical Report

- 分数：19.0  ·  HF 赞：18  ·  来源：huggingface
- 兴趣命中：reinforcement learning
- 作者：Dawei Han, Shidong Li, Shijia Liao, Jiahua Liu, Songting Liu, Qingzheng Wang, Yuxuan Wang, Xin Chen, Yifan Cheng, Tianyu Li, Gangin Park, Xuehao Yang, Chang Zeng, Haoyang Zhang, Ruoyi Zhang, Xiangyu Zhang
- 链接：[arXiv](https://arxiv.org/abs/2610.18010) · [PDF](https://arxiv.org/pdf/2610.18010) · [HF](https://huggingface.co/papers/2610.18010)

We introduce Fish Audio Drama 3, an open-source speech generation model that turns text into directed performances, built on a 35B-parameter mixture-of-experts backbone that activates 3B parameters per token. It clones voices from multiple references, follows natural-language direction, revises a take when the next turn gives a note, voices multi-character scenes, edits existing speech by infilling, and synthesizes…

## 60. HumanoidToolBench: Benchmarking Humanoid Tool Use from Selection to Mobile Execution

- 分数：19.0  ·  HF 赞：10  ·  来源：huggingface
- 兴趣命中：tool use, evaluation, benchmark
- 作者：Kyochul Jang, Seohyeon Park, Ohchul Kwon, Sangjun Park, Junhyeok Choi, Seungyeop Yi, Chaeyun Kim, Sangkyu Lee, Idan Szpektor, Avi Caciularu, Jongmin Park, Youngjae Yu
- 链接：[arXiv](https://arxiv.org/abs/2610.02089) · [PDF](https://arxiv.org/pdf/2610.02089) · [HF](https://huggingface.co/papers/2610.02089)

As robotic hardware and learning methods advance, humanoids need tools to perform tasks beyond their inherent physical limits. Successful tool use requires selecting a suitable tool and coordinating manipulation and, when needed, locomotion to complete the task. Existing benchmarks do not jointly evaluate these capabilities on a humanoid. We introduce HumanoidToolBench, an 18-task benchmark spanning three scenarios,…

## 61. EMHO: EMbodied Agent Harness Optimization via Experience Traces

- 分数：19.0  ·  HF 赞：10  ·  来源：huggingface
- 兴趣命中：agent, tool use, planning
- 作者：Hyun Jung Lee, Jungtaek Kim, Jongwon Jeong, Tae-Eui Kam, Donghyun Kim, Yong Jae Lee
- 链接：[arXiv](https://arxiv.org/abs/2610.08432) · [PDF](https://arxiv.org/pdf/2610.08432) · [HF](https://huggingface.co/papers/2610.08432)

Improving embodied agents often focuses on optimizing the underlying model through training, while the surrounding agent harness that controls planning, context, and tool use is typically engineered. We ask whether this harness can instead improve itself directly from experience traces under sparse environmental feedback. We propose EMbodied Agent Harness Optimization (EMHO), a self-evolving framework that keeps the…

## 62. Reading Right, Acting Wrong: Diagnosing Decision Failures of System One Models in Agent Loops

- 分数：19.0  ·  HF 赞：6  ·  来源：huggingface
- 兴趣命中：agent, tool use, reasoning, benchmark, coding, spec
- 作者：Yubo Li, Ramayya Krishnan, Rema Padman
- 链接：[arXiv](https://arxiv.org/abs/2610.18579) · [PDF](https://arxiv.org/pdf/2610.18579) · [HF](https://huggingface.co/papers/2610.18579)

System One models choose an agent's next action by scoring a supplied set of options in a single pass. This makes them fast and cheap, but when they choose wrongly there is nothing to inspect: did the model misread what the agent has seen, or read it correctly and still act wrongly? We answer behaviorally. On a frozen benchmark of agent decision states from simulated environments, customer-service policies, tool…

## 63. More Methods, Better Agents? A Reality Check on Self-Distillation in Agentic Reinforcement Learning

- 分数：19.0  ·  HF 赞：6  ·  来源：huggingface
- 兴趣命中：agent, reinforcement learning, evaluation, benchmark
- 作者：Linhao Zhong, Bozhen Fang, Xuehao Wang, Duochao Shi, Zekai Luo, Guangming Yao, Yi Yuan, Hao Chen, Jingdong Chen, Chunhua Shen
- 链接：[arXiv](https://arxiv.org/abs/2610.19789) · [PDF](https://arxiv.org/pdf/2610.19789) · [HF](https://huggingface.co/papers/2610.19789)

Self-distillation in agentic reinforcement learning has produced a growing number of methods. However, existing evaluations often reuse published baseline scores under differing experimental conditions, provide few direct comparisons among contemporaneous methods, and give limited attention to training stability and computational cost. These limitations obscure the source of reported gains and the practical…

## 64. Simplifying and Improving On-Policy Distillation for Few-Step Diffusion

- 分数：18.5  ·  HF 赞：13  ·  来源：huggingface
- 兴趣命中：benchmark, spec
- 作者：Jiawei Zhang, Ziyu Wan, Nanye Ma, Long Zhao, Dong Chen, Hongyu Liu, Qifeng Chen, Dongdong Chen
- 链接：[arXiv](https://arxiv.org/abs/2610.18472) · [PDF](https://arxiv.org/pdf/2610.18472) · [HF](https://huggingface.co/papers/2610.18472)

Few-step distillation reduces the sampling cost of diffusion and flow models, but existing approaches often require auxiliary score models or specialized architectures. We show that simple on-policy velocity regression already provides a strong foundation for 4-NFE generation. To represent teacher velocity variation within each coarse transition, we introduce Pivot, a training-only residual proxy that separates…

## 65. What Really Works for Universal Multimodal Embeddings? A Controlled Study of Contrastive Training Strategies

- 分数：18.5  ·  HF 赞：9  ·  来源：huggingface
- 兴趣命中：evaluation, benchmark, retrieval
- 作者：Duo Li, Haojun Pan, Zuhao Yang, Xintong Wang, Chengfu Huo, Shijian Lu, Liang Ding
- 链接：[arXiv](https://arxiv.org/abs/2610.15035) · [PDF](https://arxiv.org/pdf/2610.15035) · [HF](https://huggingface.co/papers/2610.15035)

Contrastive learning has become the standard paradigm for multimodal representation learning, aligning semantically matched pairs while separating mismatched ones in a shared embedding space. Although various contrastive training strategies have been proposed across negative selection, batch construction, and gradient modulation, their actual effectiveness under controlled, reproducible conditions remains poorly…

## 66. Towards Agentic Robots: Model, Data, Environment, and Harness

- 分数：18.5  ·  HF 赞：9  ·  来源：huggingface
- 兴趣命中：agent, evaluation, planning
- 作者：Chonghan Qin, Dongming Wu, Kaituo Feng, Jiaxu Wang, Xinlei Yu, Peiwen Sun, Yijia Fan, Xilin He, Bingao Chen, Weitong Lian, Ryan Ji, Wenqi Ren, Xiaobin Hu, Dahua Lin, Yu-Gang Jiang, Xiangyu Yue
- 链接：[arXiv](https://arxiv.org/abs/2610.20442) · [PDF](https://arxiv.org/pdf/2610.20442) · [HF](https://huggingface.co/papers/2610.20442)

Foundation models are driving a paradigm shift in robotic intelligence, moving beyond low-level action prediction to goal-directed orchestration of data collection, model training, task planning, and real-world execution. We characterize this emerging paradigm as an agentic robots, in which agents reason over human instructions, interact with robotic environments, rectify execution errors autonomously, and…

## 67. Web$hell: A Unified Interface for Agentic Web Access

- 分数：18.5  ·  HF 赞：5  ·  来源：huggingface
- 兴趣命中：agent, benchmark, language model, large language
- 作者：Sunghwan Kim, Deogyong Kim, Sangam Lee, Donguk Kwon, Dongha Lee
- 链接：[arXiv](https://arxiv.org/abs/2610.13416) · [PDF](https://arxiv.org/pdf/2610.13416) · [HF](https://huggingface.co/papers/2610.13416)

Large language model (LLM) agents are becoming direct users of the open web. As they take on increasingly complex and information-intensive tasks, effective web access is becoming a core capability for agentic problem solving. Existing approaches have advanced agentic web access through different access models, including search-augmented agents, browser-based agents, and, more recently, filesystem-based agents.…

## 68. The COUNT: Counting N-grams Unlocks Scaling on Host Memory and Training-Free Adaptation

- 分数：18.5  ·  HF 赞：1  ·  来源：huggingface + arxiv
- 兴趣命中：memory, language model, spec
- 作者：Ian Magnusson, Noah A. Smith, Pang Wei Koh
- 链接：[arXiv](https://arxiv.org/abs/2610.20456) · [PDF](https://arxiv.org/pdf/2610.20456) · [HF](https://huggingface.co/papers/2610.20456)

The scaling relationship of compute and performance for language models (LMs) has been extensively studied; more recently, models are being designed to scale memory use, as well. In particular, adding embeddings for n-grams scales memory separately from compute use, because each pass only processes individual embedding rows, which are much smaller than the storage used for the whole embedding table. However,…

## 69. KV4-RL: Unlocking Faster Asynchronous Rollouts for RLVR with INT4 KV Cache Quantization

- 分数：18.0  ·  HF 赞：12  ·  来源：huggingface
- 兴趣命中：reinforcement learning, benchmark
- 作者：Sihwan Park, Sung-Yub Kim, Doohyuk Jang, Eunho Yang
- 链接：[arXiv](https://arxiv.org/abs/2610.14448) · [PDF](https://arxiv.org/pdf/2610.14448) · [HF](https://huggingface.co/papers/2610.14448)

Asynchronous rollout improves the efficiency of reinforcement learning with verifiable rewards (RLVR) by reducing under-utilization during long-tail generation. Sustained concurrency also concentrates context processing into fewer decode steps, increasing the KV workload per step. We characterize this KV concentration and find that KV cache quantization delivers substantially greater acceleration than weight-only…

## 70. LongR: Unleashing Long-Context Reasoning via Reinforcement Learning with Dense Utility Rewards

- 分数：18.0  ·  HF 赞：12  ·  来源：huggingface
- 兴趣命中：reasoning, reinforcement learning
- 作者：Qize Yu, Zijun Chen, Chen Wu, Yue Chen, Yiyao Yu, Tingfeng Hui, Bowen Ping, Junchi Yan, Baobao Chang
- 链接：[arXiv](https://arxiv.org/abs/2602.05758) · [PDF](https://arxiv.org/pdf/2602.05758) · [HF](https://huggingface.co/papers/2602.05758)

Reinforcement Learning (RL) has emerged as a key driver for LLM reasoning. This capability is equally pivotal in long-context scenarios---such as long-dialogue understanding and structured data analysis---where the challenge extends beyond consuming tokens to performing rigorous deduction. While existing efforts focus on data synthesis or architectural changes, recent work points out that relying solely on sparse,…

## 71. Beyond the Verdict: Agentic Code Judging with Verifiable Feedback

- 分数：18.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：agent, reinforcement learning, language model, large language
- 作者：Zheye Deng, Sha Li, Changlong Yu, Xin Liu, Qin Lu, Priyanka Nigam, Yangqiu Song
- 链接：[arXiv](https://arxiv.org/abs/2610.18760) · [PDF](https://arxiv.org/pdf/2610.18760) · [HF](https://huggingface.co/papers/2610.18760)

Test-time scaling for large language models (LLMs) can involve generating multiple candidate solutions for selection or revising an earlier attempt. To guide selection and revision, we need a verifier that can estimate candidate correctness and provide evidence of failure. In competitive programming, however, official judging systems provide authoritative verdicts under finite submission budgets, without revealing…

## 72. DoubtLess: Training-Free Contrastive Decoding for Efficient Reasoning

- 分数：18.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：agent, reasoning, benchmark, coding
- 作者：Minghao Luo, Liang Chen
- 链接：[arXiv](https://arxiv.org/abs/2610.18862) · [PDF](https://arxiv.org/pdf/2610.18862) · [HF](https://huggingface.co/papers/2610.18862)

Reasoning models achieve strong performance through long chains of thought (CoT), but often spend more tokens than needed to solve a problem. Existing ways to shorten the CoT require additional training for each model, add a fixed steering vector to the model's hidden states, or use decoding heuristics such as stopping early or banning words like "wait", which can reduce accuracy. We propose DoubtLess, a…

## 73. Latent World Action Model for GUI Agents

- 分数：17.5  ·  HF 赞：11  ·  来源：huggingface
- 兴趣命中：agent, spec
- 作者：Seungjun Yu, Hojun Choi, Seojeong Park, Jaeyo Shin, Hyunjung Shim
- 链接：[arXiv](https://arxiv.org/abs/2610.14228) · [PDF](https://arxiv.org/pdf/2610.14228) · [HF](https://huggingface.co/papers/2610.14228)

Pixel-space world models have recently emerged as a promising approach for GUI agents, predicting future screens prior to execution and subsequently re-perceiving them for action selection. However, this two-stage paradigm faces two key challenges in GUI environments: (L1) the high computational cost of pixel reconstruction and (L2) the need to reconstruct large and diverse appearance-level details beyond what is…

## 74. RSIPO: Recursive Self-Improving Policy Optimization for Agentic Reinforcement Learning via Skill-Policy Co-Evolution

- 分数：17.5  ·  HF 赞：7  ·  来源：huggingface
- 兴趣命中：agent, reinforcement learning, spec
- 作者：Fan Zhang, Hao Wu, Jinyang Wu, Hongyu Qu, Zheng Lian, Xiao Luo, Yefeng Zheng, Bo Zhang, Haoxuan Li, Pheng-Ann Heng
- 链接：[arXiv](https://arxiv.org/abs/2610.15772) · [PDF](https://arxiv.org/pdf/2610.15772) · [HF](https://huggingface.co/papers/2610.15772)

Recent focus in agentic reinforcement learning (RL) seeks to improve credit assignment in long-horizon tasks. One promising direction combines reinforcement learning with verifiable rewards (RLVR) and on-policy self-distillation (OPSD), integrating trajectory-level advantages with dense token-level supervision. This line of work often conditions a teacher model on privileged context, such as agentic skills, to score…

## 75. Are We Testing Too Much? A Survey of Benchmark Compression for Efficient Evaluation of Large Language Models

- 分数：17.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：evaluation, benchmark, language model, large language
- 作者：Guoming Ling, Yupei Lin, Zhongzhan Huang, Junxin Li, Junjie Liu, Shanshan Zhong, Hefeng Wu, Liang Lin
- 链接：[arXiv](https://arxiv.org/abs/2610.18248) · [PDF](https://arxiv.org/pdf/2610.18248) · [HF](https://huggingface.co/papers/2610.18248)

Benchmarks are essential for evaluating and improving large language models (LLMs). Yet many widely used benchmarks are redundant, making evaluation unnecessarily expensive. Benchmark compression lowers this cost by estimating full-benchmark scores and rankings from a partial evaluation. Research in this area has grown rapidly since 2024, but to our knowledge no survey has systematically organized its methods and…

## 76. GeoFix: Geometry Fixing for 4D Consistent Generation

- 分数：17.0  ·  HF 赞：18  ·  来源：huggingface
- 兴趣命中：-
- 作者：Yeobin Hong, Hyojun Go, Dohun Lee, Jeongjae Lee, Sunghwan Hong, Federico Tombari, Zhaochong An, Jong Chul Ye, Konrad Schindler, Dominik Narnhofer
- 链接：[arXiv](https://arxiv.org/abs/2610.14293) · [PDF](https://arxiv.org/pdf/2610.14293) · [HF](https://huggingface.co/papers/2610.14293)

Video diffusion models increasingly serve as priors for 4D generation, but the generated videos often lack geometric consistency. Recent approaches address this through post-training by designing geometric rewards, yet this can degrade texture and fine detail, requiring auxiliary appearance rewards and careful reward balancing. To address this challenge, we propose GeoFix, a unified framework that improves geometric…

## 77. AutoEnvScaling: Automating the Data Flywheel with Terminal Agents

- 分数：17.0  ·  HF 赞：10  ·  来源：huggingface
- 兴趣命中：agent, reinforcement learning
- 作者：Simon Yu, Baolin Peng, Bo Liu, Zhengyan Shi, Zhaoyang Wang, Hao Cheng, Qianhui Wu, Wenlin Yao, Natasha Jaques, Weiyan Shi, Jianfeng Gao
- 链接：[arXiv](https://arxiv.org/abs/2610.14163) · [PDF](https://arxiv.org/pdf/2610.14163) · [HF](https://huggingface.co/papers/2610.14163)

Terminal agents solve tasks in software engineering and scientific research by executing commands in a terminal. Training them via reinforcement learning (RL) requires diverse and verifiable environments, but these environments are still mostly designed by human researchers, so their supply grows only as fast as researchers can work. We introduce AutoEnvScaling, which treats environment design as a terminal task and…

## 78. ActionOPD: Distilling Decisions, Not Tokens

- 分数：17.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：agent, tool-use, reasoning, benchmark, spec
- 作者：Huining Yuan, Xiangmin Yi, Zelai Xu, Zixu Wang, Xinlei Chen, Xiao-Ping Zhang, Yu Wang, Chao Yu
- 链接：[arXiv](https://arxiv.org/abs/2610.19820) · [PDF](https://arxiv.org/pdf/2610.19820) · [HF](https://huggingface.co/papers/2610.19820)

Distilling capable language-model agents into smaller models requires aligning the student's behavior with the teacher's. This raises a fundamental question: at which states and at what granularity should this alignment be performed? Offline imitation provides dense but token-specific supervision and can suffer from state-distribution mismatch. Token-level on-policy distillation (OPD) addresses this mismatch but…

## 79. Diagnosing and Correcting Reward Hacking in Verifiable Instruction Following

- 分数：17.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：reasoning, reinforcement learning, evaluation, benchmark
- 作者：Sangyeon Yoon, Wooseok Seo, Hamish Ivison, Hyesoo Hong, Donghoon Kim, Wonjun Kang, Albert No, Jaehyung Kim
- 链接：[arXiv](https://arxiv.org/abs/2610.19525) · [PDF](https://arxiv.org/pdf/2610.19525) · [HF](https://huggingface.co/papers/2610.19525)

Verifiable instruction-following benchmarks emphasize output-constraint satisfaction but can overlook whether responses meaningfully answer the underlying request, creating an evaluation blind spot. We show that frontier models can receive full credit for responses with little substantive answer content. Using the same verifier-based criterion as a training reward can induce reward hacking, as publicly released…

## 80. Pristine Models

- 分数：16.5  ·  HF 赞：13  ·  来源：huggingface
- 兴趣命中：spec
- 作者：Anirudh Sundara Rajan, Krishna Kumar Singh, Richard Zhang, Yong Jae Lee
- 链接：[arXiv](https://arxiv.org/abs/2610.14091) · [PDF](https://arxiv.org/pdf/2610.14091) · [HF](https://huggingface.co/papers/2610.14091)

Training on broad, unfiltered data enables high-quality image generation, but can also teach models concepts that should not be generated; restricting the training data ensures safety, but reduces quality because examples containing unsafe concepts also provide useful knowledge that is not itself unsafe. Existing approaches largely address this trade-off post hoc through concept unlearning, which can lead to…

## 81. GroundGUI: GUI Grounding by High-Quality Data and Distillation-to-Reinforcement Learning

- 分数：16.5  ·  HF 赞：5  ·  来源：huggingface
- 兴趣命中：agent, reinforcement learning, benchmark
- 作者：Qingsong Xie, Jiahao Tian, Jiacheng Tang, Zhifeng Li, Madalina Ciobanu, Navan Preet Singh, Qingqing Mao, Ritankar Das
- 链接：[arXiv](https://arxiv.org/abs/2610.19100) · [PDF](https://arxiv.org/pdf/2610.19100) · [HF](https://huggingface.co/papers/2610.19100)

Constructing robust GUI agents relies on multimodal visual grounding: the ability to precisely map natural language intents to actionable on-screen components. Despite abundant desktop, web, and mobile benchmarks, high-fidelity resources tailored for diverse environments are surprisingly scarce. To bridge this gap, we introduce the Screen Referring Grounding Dataset (ScreenRef), a comprehensive GUI grounding dataset…

## 82. Video-Arena: A Scalable Agentic Video Benchmark for Spatiotemporal Capability

- 分数：16.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark, spec
- 作者：Kuan Zhang, Yukun Chen, Zhihao Yang, Yue Su, Xiangnan Wu, Zirong Chen, Run Luo, Tao Tan, Yinhe Zheng, Yiming Li
- 链接：[arXiv](https://arxiv.org/abs/2610.14158) · [PDF](https://arxiv.org/pdf/2610.14158) · [HF](https://huggingface.co/papers/2610.14158)

Understanding and tracking a dynamic world are fundamental to visual intelligence. Existing video benchmarks provide limited insight into whether models can maintain a coherent understanding of evolving world state. Building such a benchmark from real-world videos is challenging because the underlying world state is partially observable, making annotations hard to obtain. To close this gap, we introduce Video-Arena,…

## 83. EventLens: Event-Structure Reinforcement Learning for Video Understanding

- 分数：16.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：reasoning, reinforcement learning, benchmark, language model, large language, spec
- 作者：Guowen Zhang, Boshen Xu, Zihao Yue, Ziheng Wang, Xiaokun Liu, Xin Tao, Wenyu Qin, Pengfei Wan, Qin Jin
- 链接：[arXiv](https://arxiv.org/abs/2610.16172) · [PDF](https://arxiv.org/pdf/2610.16172) · [HF](https://huggingface.co/papers/2610.16172)

Recent multimodal large language models (MLLMs) achieve strong results on video question answering, yet often fail to recover the temporal structure that makes a video coherent. They may merge neighboring events, miss single-event progression, or infer implausible relations across events. We study structured temporal understanding as the ability to recover event structure from visual evidence, including event…

## 84. Beyond Perfect Teammates: Multi-Agent Collaboration with Unreliable Colleagues

- 分数：16.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：agent, reasoning, evaluation, benchmark, spec
- 作者：Chen Huang, Yiyang Zhang, Yuhao Wu, Yang Deng, Wenxuan Zhang
- 链接：[arXiv](https://arxiv.org/abs/2610.16117) · [PDF](https://arxiv.org/pdf/2610.16117) · [HF](https://huggingface.co/papers/2610.16117)

LLM-based multi-agent collaboration is increasingly used to solve complex tasks by dividing work among specialized agents and integrating complementary expertise. Yet existing systems and evaluations largely rest on an implicit perfect-colleague assumption: collaborators provide correct and complete information and respond promptly to requests. In realistic teamwork, however, collaborators may return information…

## 85. Diff Diffusion: Predicting Edit Paths with Diffusion Models for Efficient Code Editing

- 分数：16.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：evaluation, benchmark, language model, large language, coding, spec
- 作者：Xiaolong Xu, Hao Jiang, Bo Jiang, Zhiwen Deng, Ningyuan Sun, Bingzhou Chen, Jin Chen, Chenxing Wei
- 链接：[arXiv](https://arxiv.org/abs/2610.17831) · [PDF](https://arxiv.org/pdf/2610.17831) · [HF](https://huggingface.co/papers/2610.17831)

Diffusion large language models (dLLMs) are appealing for code generation because they can update many tokens in parallel, yet many are optimized for sequence synthesis rather than edit prediction. This setting is poorly matched to modern AI-assisted IDEs, where edit prediction must infer the next code change from recent edits, the current file, and cursor-local context. Such changes are usually sparse and preserve…

## 86. TacitVLA: Reasoning Vision-Language-Action Models Without Reasoning Latency

- 分数：16.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：memory, reasoning, benchmark, coding
- 作者：Jack Lu, Yurong You, Boyi Li, Yulong Cao, Thomas Tian, Chaowei Xiao, Xiangyu Chen, Wenjie Luo, Boris Ivanovic, Marco Pavone, Yan Wang
- 链接：[arXiv](https://arxiv.org/abs/2610.17540) · [PDF](https://arxiv.org/pdf/2610.17540) · [HF](https://huggingface.co/papers/2610.17540)

Textual reasoning before acting has improved vision-language-action (VLA) models, but at the cost of latency: every action conditioned on the reasoning text must wait for autoregressive decoding. We show that actions do not need to wait for or condition on the generated reasoning to benefit from it, because the reasoning supervision already improves the backbone representation. We introduce TacitVLA, a reasoning VLA…

## 87. Words to World: Benchmarking LLMs in Interactive Physical Environments

- 分数：16.0  ·  HF 赞：0  ·  来源：huggingface
- 兴趣命中：agent, reasoning, benchmark, language model, large language, planning
- 作者：Xinnan Dai, Kaiqi Yang, Yaxin Li, Cheng Luo, Wanli Li, Mingqing Xiao, Xinyang Jiang, Daoan Zhang, Kaitao Song, Fengze Liu, Zefan Cai, Caihua Shan
- 链接：[arXiv](https://arxiv.org/abs/2610.15228) · [PDF](https://arxiv.org/pdf/2610.15228) · [HF](https://huggingface.co/papers/2610.15228)

Words are increasingly becoming an interface for action: large language models (LLMs) can now invoke tools, operate devices, and make decisions that affect the physical world. However, current benchmarks largely evaluate LLMs through static text responses, offline tool calls, or simulated tasks, leaving open the question of how well they can act in real physical environments. We present a benchmark for measuring…

## 88. Let the Mind Conceive, Let the Hand Achieve: Following Multimodal Instructions for Long-Horizon Robotic Manipulation

- 分数：16.0  ·  HF 赞：0  ·  来源：huggingface
- 兴趣命中：agent, benchmark, spec, planning
- 作者：Youpeng Wen, Gang Wang, Tianyu Huang, Weiwei Zhang, Zhijian Huang, Wei Chen, Xieyuanli Chen, Yunhui Liu
- 链接：[arXiv](https://arxiv.org/abs/2610.18352) · [PDF](https://arxiv.org/pdf/2610.18352) · [HF](https://huggingface.co/papers/2610.18352)

A robot following a multi-step instruction needs to act on the right objects in the right order, even as the scene changes. It must also maintain awareness of task progress and determine when to advance. To address these challenges, we introduce Orchestra, an agent harness that separates task planning and execution management from action generation. Orchestra decomposes a complete multimodal instruction into ordered…

## 89. Continuum Attention

- 分数：16.0  ·  HF 赞：0  ·  来源：huggingface + arxiv
- 兴趣命中：memory, spec
- 作者：Afshin Khadangi
- 链接：[arXiv](https://arxiv.org/abs/2610.20586) · [PDF](https://arxiv.org/pdf/2610.20586) · [HF](https://huggingface.co/papers/2610.20586)

We introduce Continuum Attention (CA), a causal Transformer attention operator that replaces discrete key and value lookup with integration over a continuous, piecewise linear memory curve. Each query induces an exponential relevance density along the curve. Integrating the density and interpolated values yields exact normalized attention from closed form exponential moments, including half token boundary…

## 90. ACCRUE: Continual Off-Policy Reinforcement Learning for Robot Foundation Models

- 分数：15.5  ·  HF 赞：11  ·  来源：huggingface
- 兴趣命中：reinforcement learning
- 作者：Changyeon Kim, Kimin Lee, Yashraj Narang, Yijie Guo
- 链接：[arXiv](https://arxiv.org/abs/2610.18596) · [PDF](https://arxiv.org/pdf/2610.18596) · [HF](https://huggingface.co/papers/2610.18596)

Reinforcement learning (RL) post-training improves robot foundation models (RFMs) beyond their demonstrations, but real-world deployment demands more: learning new tasks efficiently while retaining previously acquired behaviors. Existing continual RL methods on top of VLAs mitigate forgetting but rely on on-policy updates with limited forward transfer, whereas off-policy methods improve single-task sample efficiency…

## 91. PsyBer-Agent: A Psychology-Driven User Agent for Recommender Systems

- 分数：15.5  ·  HF 赞：7  ·  来源：huggingface
- 兴趣命中：agent, benchmark
- 作者：Chong Zhang, Qijie Shen, Haichao Zhang, Can Wang, Xiaobo Jin, Jia Wang
- 链接：[arXiv](https://arxiv.org/abs/2610.13989) · [PDF](https://arxiv.org/pdf/2610.13989) · [HF](https://huggingface.co/papers/2610.13989)

Evaluating recommender systems before deployment requires simulators that remain realistic over long, closed-loop interaction cycles. Current LLM-based agents generally function as surface imitators that generate realistic short-term responses but fail to capture the underlying user dynamics such as fatigue, affect, and shifting preferences. We propose PsyBer-Agent, a psychology-inspired simulator that models these…

## 92. Controlled Acquisition and Abstention in Three-Channel Score Conflicts

- 分数：15.5  ·  HF 赞：7  ·  来源：huggingface
- 兴趣命中：benchmark, spec
- 作者：Mengzhe Geng
- 链接：[arXiv](https://arxiv.org/abs/2610.10808) · [PDF](https://arxiv.org/pdf/2610.10808) · [HF](https://huggingface.co/papers/2610.10808)

When audio, video, and text disagree, accuracy alone does not show whether to acquire another source or abstain. We study these choices in a controlled three-score benchmark: a policy observes two signed scores, may request the third at a cost, and can abstain. The primary reward is mechanism-specific: abstention is correct only for one designated ambiguity mechanism and is penalized under mixed corruption. Matched…

## 93. LightVAE: Towards Compact and Efficient Video Autoencoders

- 分数：15.5  ·  HF 赞：7  ·  来源：huggingface
- 兴趣命中：coding, spec
- 作者：Shiqiao Gu, Yang Yong, Fengjun Zhong, Ruihao Gong, Chengtao Lv, Xiangyu Fan, Lei Yang, Xianglong Liu
- 链接：[arXiv](https://arxiv.org/abs/2610.14726) · [PDF](https://arxiv.org/pdf/2610.14726) · [HF](https://huggingface.co/papers/2610.14726)

Latent diffusion models enable high-quality video generation, but video VAE encoding and decoding remain computationally expensive. Existing methods use stage-specific lightweight operators, yet either constrain spatial and temporal computation jointly or remove temporal computation altogether, without distinguishing their compression sensitivities in pretrained Conv3D. To address these limitations, we present…

## 94. WorldRecon: Generative Multi-View Mesh Reconstruction for Large-Scale 3D World

- 分数：15.0  ·  HF 赞：10  ·  来源：huggingface
- 兴趣命中：spec
- 作者：Mengchen Zhang, Yang Li, Chunshi Wang, Tong Wu, Chunchao Guo
- 链接：[arXiv](https://arxiv.org/abs/2610.18846) · [PDF](https://arxiv.org/pdf/2610.18846) · [HF](https://huggingface.co/papers/2610.18846)

Reconstructing complete, high-quality meshes of large-scale scenes from unposed multi-view images requires faithful geometric grounding while plausibly completing surfaces that are unobserved or only sparsely captured. We present WorldRecon, a generative multi-view reconstruction framework for recovering complete, large-scale 3D scene meshes from unposed RGB images. WorldRecon uses a coarse, noisy global point cloud…

## 95. RAR: Rate-Adaptive Rollout for Time-Consistent Interactive World Models

- 分数：15.0  ·  HF 赞：6  ·  来源：huggingface
- 兴趣命中：context window, spec
- 作者：Yaoyang Liu, Dongyu Yan, Yihua Du, Shengju Qian, Zeke Xie, Xin Wang, Ying-Cong Chen, Long Chen
- 链接：[arXiv](https://arxiv.org/abs/2610.16302) · [PDF](https://arxiv.org/pdf/2610.16302) · [HF](https://huggingface.co/papers/2610.16302)

Video-based interactive world models aim to enable real-time, user-controllable environments. Yet most existing systems are trained and rolled out at a fixed temporal rate, limiting both runtime-rate adaptation and physical-horizon coverage -- a limitation we term temporal-rate coupling. Specifically, when runtime generation throughput differs from the learned temporal rate, the generated world evolves…

## 96. Rubrics from the Task, Verdicts from Evidence: Pointwise Rubric Rewards with Tool-Augmented Judges

- 分数：14.5  ·  HF 赞：9  ·  来源：huggingface
- 兴趣命中：reasoning
- 作者：Tianci Liu, Haoyu Wang
- 链接：[arXiv](https://arxiv.org/abs/2610.18766) · [PDF](https://arxiv.org/pdf/2610.18766) · [HF](https://huggingface.co/papers/2610.18766)

Rubric-based reward models (RMs) evaluate responses against explicit criteria. However, existing methods often derive criteria from observed response candidates, introducing response-induced bias that may limit rubric generalizability. Their judges also struggle with mechanical constraints when relying on reading alone, and commonly used pairwise judges provide only relative preferences, complicating their direct…

## 97. Diffusion Editing with Soft Mask: Pixel Level Redo of Image and Video with Adjustable Strength

- 分数：14.5  ·  HF 赞：5  ·  来源：huggingface
- 兴趣命中：memory, spec
- 作者：Candi Zheng, Yuan Lan
- 链接：[arXiv](https://arxiv.org/abs/2610.00359) · [PDF](https://arxiv.org/pdf/2610.00359) · [HF](https://huggingface.co/papers/2610.00359)

Diffusion models with prompt and reference image-guided editing have seen rapid progress, yet they remain too coarse for pixel-level control. One promising direction is to incorporate a soft mask that specifies spatially varying edit strengths but training such fine-grained control demands expensive pixel-wise annotations, while existing zero-shot methods often yield unsatisfactory results. We introduce SoftPaint, a…

## 98. CURIO: Curiosity-Driven Test-Time Learning for Open-Ended Discovery

- 分数：14.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：reinforcement learning, language model, large language
- 作者：Tao Feng, Fangxu Yu, Zijie Lei, Jiaru Zou, Changjiang Jiang, Yi Yan, Jiaxuan You, Pan Lu
- 链接：[arXiv](https://arxiv.org/abs/2610.04851) · [PDF](https://arxiv.org/pdf/2610.04851) · [HF](https://huggingface.co/papers/2610.04851)

Open-ended discovery requires learning from repeated attempts while continuing to explore directions whose value is not yet apparent. Search with a frozen large language model (LLM) can reuse previous solutions in context, but cannot update the model from its successes and failures on the test problem. Reinforcement learning (RL) enables such adaptation; however, strongly favoring high-reward trajectories may…

## 99. Who to Trust in Multi-Robot Systems: Joint Robot and Object Hypothesis Trust Inference via Neural-Symbolic Cross-Validation

- 分数：14.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：reasoning, evaluation, benchmark
- 作者：Ruiyang Wang, Hao-Lun Hsu, Haocheng Meng, Songqiao Xie, Miroslav Pajic
- 链接：[arXiv](https://arxiv.org/abs/2610.14530) · [PDF](https://arxiv.org/pdf/2610.14530) · [HF](https://huggingface.co/papers/2610.14530)

Multi-robot systems (MRS) offer significant advantages over single-robot platforms by enabling information sharing and coordination for different tasks in complex environments. However, reliable cooperation critically depends on inferring trust over both information sources and their reported hypotheses, particularly under partial observability and potential adversarial interference. Existing approaches frequently…

## 100. Model-Based Online Decision Making via Generative Trajectory Planning

- 分数：14.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：reasoning, spec, planning
- 作者：Haldun Balim, Yilun Du, Na Li
- 链接：[arXiv](https://arxiv.org/abs/2610.18677) · [PDF](https://arxiv.org/pdf/2610.18677) · [HF](https://huggingface.co/papers/2610.18677)

Online decision-making faces a tension between efficient inference and long-horizon reasoning. Value-based methods rely on short-horizon bootstrapping that limits the propagation of long-term information, while trajectory optimization methods plan explicitly but must solve a high-dimensional optimization problem at every decision step. We propose Generative Trajectory Planning (GTP), a model-based framework that…

## 101. Can an Agent Learn to Predict Its Own Failure? Outcome-Grounded Confidence Calibration in LLM Agents

- 分数：14.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：agent, reinforcement learning, evaluation
- 作者：Ashutosh Hathidara
- 链接：[arXiv](https://arxiv.org/abs/2610.18614) · [PDF](https://arxiv.org/pdf/2610.18614) · [HF](https://huggingface.co/papers/2610.18614)

Controlling an acting LLM agent means deciding, at each step of a long-horizon task, whether to trust its next action, abstain, or hand off to a human. That decision needs a per-step confidence signal predicting whether the current rollout will eventually succeed. The agent's own self-reported verbalized confidence is the natural candidate, but existing reinforcement learning methods calibrate it against the…

## 102. Training LLMs for Multi-Agent Collaboration with Verifiable Information Rewards

- 分数：14.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：agent, language model, large language
- 作者：Keru Chen, Sen Lin, Yingbin Liang, Nathaniel D. Bastian, Shaofeng Zou
- 链接：[arXiv](https://arxiv.org/abs/2610.17893) · [PDF](https://arxiv.org/pdf/2610.17893) · [HF](https://huggingface.co/papers/2610.17893)

Effective collaboration among large language model (LLM) agents in multi-agent systems requires sharing relevant evidence, requesting missing information, and incorporating teammates' contributions into decisions. Training these behaviors is challenging because final task outcomes provide limited feedback on the value of individual messages. We introduce CoSIR (Collaboration via Surprisal-based Information Rewards),…

## 103. DecisionRobust: Benchmarking Robustness for JEV Style Decision Models Across Text and Vision

- 分数：14.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：evaluation, benchmark, spec
- 作者：Yifan Lan, Zhongye Liu, Yurui Chang, Hanyu Wang, Yongkang Du, Lu Lin, Jinghui Chen
- 链接：[arXiv](https://arxiv.org/abs/2610.19118) · [PDF](https://arxiv.org/pdf/2610.19118) · [HF](https://huggingface.co/papers/2610.19118)

Emerging decision models such as JEV provide typed interfaces that map task instructions and observations directly to choices, judgments, and scores. As these models are increasingly used for automated decision-making, understanding their reliability under adversarial manipulation becomes critical. We introduce DecisionRobust, a benchmark for systematically evaluating the robustness of decision models across textual…

## 104. HexaBee-4B: Six-Language Translation with Multilingual Answering and Bidirectional Supervision

- 分数：14.0  ·  HF 赞：8  ·  来源：huggingface
- 兴趣命中：spec
- 作者：Iman Barati, Mohammadmostafa Rostamkhani, Mohammad Badzohreh
- 链接：[arXiv](https://arxiv.org/abs/2610.16361) · [PDF](https://arxiv.org/pdf/2610.16361) · [HF](https://huggingface.co/papers/2610.16361)

Multilingual translation requires a model to preserve meaning while producing text in a requested language. We present HexaBee-4B, a translator adapted from Gemma 3 4B IT through three stages: Wikipedia continued pretraining, joint multilingual answering and answer-text translation, and bidirectional translation specialization. The intermediate stage connects two tasks through shared multilingual answers: answering…

## 105. MA-Bench: Measuring Operational Planning in Language Models

- 分数：14.0  ·  HF 赞：0  ·  来源：huggingface
- 兴趣命中：reasoning, language model, planning
- 作者：Rodney Lafuente-Mercado, Robert Sincero, Phil Sage, Yuan Xue
- 链接：[arXiv](https://arxiv.org/abs/2610.19138) · [PDF](https://arxiv.org/pdf/2610.19138) · [HF](https://huggingface.co/papers/2610.19138)

How well can a language model turn a large, incomplete and partly contradictory body of documents into a plan when no single correct answer exists? We introduce Mission Analysis (MA)-Bench, built on mission analysis, the first step of military operational planning, in which a staff reads the full situation and states the problem before anyone proposes a solution. Its 10 expert-built scenarios pair synthetic packets…

## 106. G^3VLA: Geometric Inductive Bias for Vision-Language-Action Models

- 分数：14.0  ·  HF 赞：0  ·  来源：huggingface
- 兴趣命中：reasoning, coding, spec
- 作者：Yue Peng, Yongzhe Zhao, Artur Habuda, Khuyen Pham, Yanheng Zhu, Tran Nguyen Le, Fares Abu-Dakka, Li Guo
- 链接：[arXiv](https://arxiv.org/abs/2606.24472) · [PDF](https://arxiv.org/pdf/2606.24472) · [HF](https://huggingface.co/papers/2606.24472)

Vision-language-action (VLA) models have rapidly advanced generalist robot manipulation by harnessing the semantic knowledge of pretrained vision-language backbones. However, their visual representations are typically grounded in 2D image coordinates rather than calibrated camera geometry. This limitation is especially pronounced in multi-camera systems, where views are coupled by known intrinsics and extrinsics but…

## 107. CIViC: Evidence Gates for Audio-Conditioned Visual Prediction on Proxy Tasks

- 分数：13.0  ·  HF 赞：10  ·  来源：huggingface
- 兴趣命中：-
- 作者：Mengzhe Geng, Max W. Y. Lam, Yuewen Cao, Shoukang Hu, Jing Xu, Marc Tessier, Xu Li
- 链接：[arXiv](https://arxiv.org/abs/2610.15327) · [PDF](https://arxiv.org/pdf/2610.15327) · [HF](https://huggingface.co/papers/2610.15327)

Removing audio can shift a visual predictor's output without showing whether the task uses the intended audio information. We introduce Conditional Input and Visual Interpretation Checks (CIViC), a four-gate protocol that links an interpretation to an intervention, held-out task comparison, or endpoint control. We demonstrate CIViC on actor-disjoint face-raster tests, a synthetic audio-feature mixture, and…

## 108. TextVerifier: Seeing Beyond Recognition to Verify Chinese Text Rendering

- 分数：13.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：benchmark, language model
- 作者：Yiyang Chen, Guo-Hua Wang, Yaoli Liu, Qing-Guo Chen, Zhao Xu, Weihua Luo, Xiujun Ma
- 链接：[arXiv](https://arxiv.org/abs/2610.19551) · [PDF](https://arxiv.org/pdf/2610.19551) · [HF](https://huggingface.co/papers/2610.19551)

Text-to-image models increasingly generate readable Chinese text that still contains local rendering defects, such as a character with an extra or missing stroke or a malformed component. Such errors are invisible to OCR and vision-language models, which are trained for recognition and are therefore invariant to the very structural deviations that define a rendering error. We formalize text rendering verification as…

## 109. Physical Time as a Missing Dimension of Robot Policy Memory Dynamics

- 分数：13.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：memory, evaluation
- 作者：Yushen Liang, Yue Peng, Baosheng Jin, Tianluo Zhang, Xinyu Zhang, Shuyi Zhou, Zhuoran Chen, Xinqi Liu, Shenji Wan
- 链接：[arXiv](https://arxiv.org/abs/2610.20524) · [PDF](https://arxiv.org/pdf/2610.20524) · [HF](https://huggingface.co/papers/2610.20524)

Existing robot policy memories typically evolve with observation sequences, implicitly treating each update as the same amount of physical time. Yet identical observation histories can span different durations and require different actions, exposing physical time as a missing dimension of policy memory. We introduce Temporal Flow Policy (TFP), which learns memory dynamics to retain past events and evolve the memory…

## 110. Learning Transferable World-Action Models from Task-Paired Human Videos

- 分数：12.5  ·  HF 赞：9  ·  来源：huggingface
- 兴趣命中：-
- 作者：Jeongeun Park, Taekyung Kim, Dongyoon Han, Sangdoo Yun
- 链接：[arXiv](https://arxiv.org/abs/2610.14351) · [PDF](https://arxiv.org/pdf/2610.14351) · [HF](https://huggingface.co/papers/2610.14351)

World-action models inherit broad visual and physical priors from video pre-training. However, standard within-video next-frame prediction allows them to rely on appearance shared between the context and future, rather than learning interactions that transfer across scenes and embodiments. We introduce WATCH, a cross-video pre-training that learns from task-paired human demonstrations collected across diverse…

## 111. UniForge3D: Joint 3D Reconstruction and Generation in a Shared Anchor-Guided Space

- 分数：12.5  ·  HF 赞：9  ·  来源：huggingface
- 兴趣命中：-
- 作者：Wenjue Chen, Wenyue Chen, Heliang Zheng, Rongfei Jia, Yuan Liu, Meng Li
- 链接：[arXiv](https://arxiv.org/abs/2610.15357) · [PDF](https://arxiv.org/pdf/2610.15357) · [HF](https://huggingface.co/papers/2610.15357)

Generating complete 3D assets from sparse, unposed images requires preserving observed geometry while completing unseen regions. Joint reconstruction and generation offers a way to address both goals: reconstruction recovers the geometry observed in the input images, while generation contributes learned shape priors. However, combining camera-relative reconstruction with canonical-space generation introduces a…

## 112. Efficient Scene-Text Refinement via Pixel-Space Grouped Image Generation

- 分数：12.5  ·  HF 赞：5  ·  来源：huggingface
- 兴趣命中：benchmark
- 作者：Yaoli Liu, Guo-Hua Wang, Yiyang Chen, Qing-Guo Chen, Zhao Xu, Weihua Luo, Yao-Xiang Ding
- 链接：[arXiv](https://arxiv.org/abs/2610.18284) · [PDF](https://arxiv.org/pdf/2610.18284) · [HF](https://huggingface.co/papers/2610.18284)

Generated images often have coherent layouts and visual content, yet local errors in small text and complex characters still limit their readability and practical use. Scene-text refinement requires accuracy, preservation, and efficiency. Existing methods based on variational autoencoders (VAEs) can lose fine strokes during reconstruction, while full-image editing can shift background colors. In this work, we…

## 113. Scaling Verifiable Environments for Long-horizon Work Agents

- 分数：12.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：agent, spec
- 作者：Jiazheng Zhang, Long Ma, Yunxian Yang, Zhiheng Xi, Zhikai Lei, Yajie Yang, Chenyang Liao, Enyu Zhou, Yang Nan, Yuchen Tian, Senjie Jin, Yibo Wang, Wei He, Boyang Liu, Jixuan Huang, Xin Guo, Zhezheng Hao, Xinbing Liang, Zhihao Zhang, Changzhi Zhou, Wiggin Zhou, Tao Gui, Qi Zhang, Xuanjing Huang, Clarenceai, Aiden Adams
- 链接：[arXiv](https://arxiv.org/abs/2610.04906) · [PDF](https://arxiv.org/pdf/2610.04906) · [HF](https://huggingface.co/papers/2610.04906)

Work agents operate over digital artifacts to execute professional knowledge-intensive work, requiring training environments that support long-horizon interaction and trustworthy verification. However, hand-crafted environments incur prohibitive engineering overhead that prevents environment scaling, whereas synthesis methods sacrifice workspace complexity, realism, or grounded verifiability. To bridge this gap, we…

## 114. Omni-Modal LLMs Know More Than They Say

- 分数：12.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：language model, large language
- 作者：Na Min An, Taekyung Kim, Jaemyung Yu, Hyunjung Shim, Dongyoon Han
- 链接：[arXiv](https://arxiv.org/abs/2610.16135) · [PDF](https://arxiv.org/pdf/2610.16135) · [HF](https://huggingface.co/papers/2610.16135)

Omni-modal large language models (Omni-LLMs) extend LLMs to process heterogeneous modalities (e.g., vision, audio, and IMU signals) alongside language, enabling a broader range of multimodal tasks. Yet we find that these models often fail to express information from non-textual modalities even when they perceive it correctly. We term this disconnect knows-but-cannot-say. To investigate this phenomenon, we introduce…

## 115. Enabling Token-wise Importance Sampling in Off-Policy RLVR with Proximal KL Regularization

- 分数：12.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：reinforcement learning, benchmark
- 作者：Hao Bai, Jiarui Yao, Tong Zhang
- 链接：[arXiv](https://arxiv.org/abs/2610.18738) · [PDF](https://arxiv.org/pdf/2610.18738) · [HF](https://huggingface.co/papers/2610.18738)

Off-policy data in reinforcement learning with verifiable rewards (RLVR) can arise from asynchronous generation, rollout-training mismatch, and response reuse. Token-wise importance weighting avoids multiplying likelihood ratios across a response but generally biases policy gradients. We prove that, under coverage and local expressiveness conditions, full future KL credit makes the exact proximal optimizer the…

## 116. SHELDON: Reasoning through Dual Search over Hypothesis and Observation Spaces

- 分数：12.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：reasoning, benchmark
- 作者：Harshit Joshi, Priyank Shethia, Monica S. Lam
- 链接：[arXiv](https://arxiv.org/abs/2610.18025) · [PDF](https://arxiv.org/pdf/2610.18025) · [HF](https://huggingface.co/papers/2610.18025)

Test-time scaling has enabled LLMs to solve increasingly complex reasoning, discovery, and optimization tasks. However, existing approaches often gather observations while seeking evidence for current hypotheses, then generate new hypotheses conditioned on those hypotheses and their associated evidence. This couples observation discovery to existing hypotheses, favoring local refinements over exploration of unknown…

## 117. 4LC: 4D Latent Cache for Efficient Conditioning in Dynamic World Modeling

- 分数：12.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：coding, spec
- 作者：Jianhui Zhang, Zuyao Lin, Pengxin Xu, Jingdong Wang, Xingyu Chen
- 链接：[arXiv](https://arxiv.org/abs/2610.17625) · [PDF](https://arxiv.org/pdf/2610.17625) · [HF](https://huggingface.co/papers/2610.17625)

For video generation in dynamic world modeling, observed static and dynamic content should be efficiently reused to provide conditions for repeated generation at different times and viewpoints. We introduce 4LC, a 4D latent cache with composite visual representations and a flexible spatiotemporal access interface. As a latent cache, 4LC directly reuses visual representations of static and dynamic content to provide…

## 118. Batched Speech Decisions Without Decoding: Single-Token Supervision Lets a Frozen LLM Hear Beyond the Transcript

- 分数：12.0  ·  HF 赞：0  ·  来源：huggingface
- 兴趣命中：agent, coding
- 作者：Jie Jin, Ziyin Ma, Min Yin, Jinyu Chen, Haigang Song, Zhikun Pang, Xiaowen Zhang
- 链接：[arXiv](https://arxiv.org/abs/2610.02638) · [PDF](https://arxiv.org/pdf/2610.02638) · [HF](https://huggingface.co/papers/2610.02638)

Full-duplex voice agents make many small, closed decisions, which current systems answer by slow autoregressive decoding. We propose DuplexJev, which feeds ASR-encoder hidden states through a small connector into a frozen LLM and reads each question as a single-token distribution over its options. Nothing is decoded, and an 8-GPU node answers 80 decisions about eight utterances in about 0.1 s. With a last-layer…

## 119. Privacy-Preserving Intent Fulfilment and Assurance for 6G RAN

- 分数：12.0  ·  HF 赞：0  ·  来源：huggingface
- 兴趣命中：agent, spec
- 作者：Joss Armstrong
- 链接：[arXiv](https://arxiv.org/abs/2607.08809) · [PDF](https://arxiv.org/pdf/2607.08809) · [HF](https://huggingface.co/papers/2607.08809)

Intent-based network management automates 6G service lifecycles, but existing fulfilment and assurance approaches require traffic inspection, per-flow tracking, or vendor-internal telemetry. These requirements conflict with privacy constraints in multi-tenant networks and vendor opacity in O-RAN deployments. We present an architecture that provisions resources from declared intent categories without traffic…

## 120. Judges Follow the Reference: The Derivation Gap in Verifying Tool-Call Arguments

- 分数：12.0  ·  HF 赞：0  ·  来源：huggingface
- 兴趣命中：agent, benchmark
- 作者：Linhai Ma, Yan Wang, Lingfei Qian, Yupeng Cao, Victor Gutierrez Basulto
- 链接：[arXiv](https://arxiv.org/abs/2610.18497) · [PDF](https://arxiv.org/pdf/2610.18497) · [HF](https://huggingface.co/papers/2610.18497)

Tool-call judges evaluate argument values proposed by LLM agents. We find that they accept a correct value less often when their input holds no reference for it, that is, no text that says what the value should be. This happens when the value is a default value from the function schema that the user did not mention, when it has to be inferred, or when the text it comes from was cut from the judge input. We call this…
