# 每日 AI 论文

生成时间：2026-11-03 06:48 UTC  ·  共 120 篇（已按 arXiv ID 去重）

来源：Hugging Face Daily Papers + arXiv（cs.AI / cs.LG / cs.CL / cs.CV）。
排序：HF 上榜、点赞、多源命中、兴趣词。兴趣词可在 `config.json` 改。

## 1. REA: A Routed Embodied Agent Runtime for Asynchronous Brain-Cerebellum Control

- 分数：34.0  ·  HF 赞：136  ·  来源：huggingface
- 兴趣命中：agent, memory, reasoning
- 作者：Pengfei Zhou, Yixing Ma, Zhengfeiyang Zhang, Haoyuan Chen, Zhenglin Wan, Hexin Wang, Wangbo Zhao, Yang You
- 链接：[arXiv](https://arxiv.org/abs/2610.42053) · [PDF](https://arxiv.org/pdf/2610.42053) · [HF](https://huggingface.co/papers/2610.42053)

Foundation models are becoming remarkably reliable at high-level reasoning, yet they remain too slow and costly to serve as fine-grained controllers. Conversely, fast policies like VLAs and whole-body controllers offer more efficient reflexes, but struggle to generalize. While pairing a deliberative brain (foundation models) with a reactive cerebellum (fast policies) seems natural for embodied systems, two obstacles…

## 2. FrameForge: Harnessing Priors of Video Foundation Models for Unified Image Generation

- 分数：34.0  ·  HF 赞：112  ·  来源：huggingface
- 兴趣命中：reasoning, coding, spec
- 作者：Yijing Lin, Zhendong Mao, Mengqi Huang, Yuxin Wang, Yongdong Zhang
- 链接：[arXiv](https://arxiv.org/abs/2610.36545) · [PDF](https://arxiv.org/pdf/2610.36545) · [HF](https://huggingface.co/papers/2610.36545)

Unified conditional image generation requires a single model to preserve different aspects of a visual input while producing a target image that follows textual guidance. Pretrained video models provide a promising foundation by encoding visual transformations across time, yet existing approaches typically assign the condition and target to fixed temporal positions. We observe that condition-target relationships…

## 3. Does Scaling Toward AGI Depend on What System-1 Lets System-2 Execute?

- 分数：34.0  ·  HF 赞：59  ·  来源：huggingface
- 兴趣命中：agent, tool use, reasoning
- 作者：Qi Wang, Yun Qu, Lizhou Cai, Heming Zou, Haoang Chi, Yiqin Lv, Xiang Li, Haiyan Feng, Mengyu Ge, Yize Geng, Yuhang Jiang, Yixiu Mao, Xiangyang Ji
- 链接：[arXiv](https://arxiv.org/abs/2610.39497) · [PDF](https://arxiv.org/pdf/2610.39497) · [HF](https://huggingface.co/papers/2610.39497)

Progress toward artificial general intelligence (AGI) has largely relied on scaling a resource-intensive executive, System-2, through larger models, more data and compute, longer reasoning, and more agents. We ask whether the next stage may come instead from co-designing it with System-1, a lightweight, semantically aware predictor that evaluates candidate interactions before execution, so that System-2 acts only on…

## 4. HiFOR: Hierarchical Foresight with Action-Guided World Grounding for Vision-Language-Action Model

- 分数：33.5  ·  HF 赞：39  ·  来源：huggingface
- 兴趣命中：benchmark, spec, retrieval
- 作者：Rongxing Ding, Hongyu Qu, Kehong Wu, Xudong Wang, Fan Zhang, Xinguang Xiang, Xiangbo Shu
- 链接：[arXiv](https://arxiv.org/abs/2610.40373) · [PDF](https://arxiv.org/pdf/2610.40373) · [HF](https://huggingface.co/papers/2610.40373)

Vision-Language-Action (VLA) models have demonstrated promising capabilities in robotic manipulation by integrating visual perception, language understanding, and action generation. Recent advances have further incorporated future prediction to enhance the understanding of environmental dynamics and task progression. However, existing methods often model short-term dynamics and long-term task objectives separately,…

## 5. Video Generation Meets Agent Harness: Agentic Video Generation, Agentic World Modeling and Recursive Self-Improvement

- 分数：32.5  ·  HF 赞：33  ·  来源：huggingface
- 兴趣命中：agent, tool use, memory, evaluation, planning
- 作者：Liaoyuan Fan, Yuhao Zheng, Dongxing Mao, Hangyu Ran, Siyuan Hu, Weijia Mao, Rui Zhao, Weijia Wu, Guian Fang, Yanzhe Chen, Zeyu Zhu, Yuxin Jiang, Yiren Song, Yuchao Gu, Junchao Yi, Qi Hu, Dan Kong, Alex Jinpeng Wang, Kevin Qinghong Lin, Mike Zheng Shou, Wei Liu
- 链接：[arXiv](https://arxiv.org/abs/2610.40191) · [PDF](https://arxiv.org/pdf/2610.40191) · [HF](https://huggingface.co/papers/2610.40191)

Video generation is shifting from end-to-end synthesis toward agentic generation, where planning, tool use, and feedback enable coherent, controllable multi-shot videos. In parallel, video world models provide action-conditioned observations and predicted futures, serving as interactive environments for agents. We study their intersection through the agent harness: an executable runtime that constructs context,…

## 6. R^2Orch: Recursive Self-Improvement for Agent Orchestration via Self-Play within a Skill-Internalization Loop

- 分数：32.0  ·  HF 赞：93  ·  来源：huggingface
- 兴趣命中：agent, evaluation
- 作者：Mingda Zhang, Yun Huang, Qiang Huang, Yanjin Li, Rui Qian, Qichao Zhao, Tiesunlong Shen, Na Zhao, Jian Wang, Xiaoying Tang
- 链接：[arXiv](https://arxiv.org/abs/2610.22740) · [PDF](https://arxiv.org/pdf/2610.22740) · [HF](https://huggingface.co/papers/2610.22740)

In recent years, agentic orchestration has been widely applied to solve complex human tasks. However, existing orchestration learning still faces key challenges, including hand-designed curricula, advantage collapse when a task's rollouts all reach the same outcome, and unreliable evaluation signals that judge each skill by one noisy score. To address these challenges, we propose R^2Orch, a new paradigm of Recursive…

## 7. Apriel Voice 27B Preview: An Open Model for Speech, Reasoning, and Tool Use

- 分数：30.5  ·  HF 赞：33  ·  来源：huggingface
- 兴趣命中：tool use, reasoning, language model
- 作者：Aman Tiwari, Akshay Kalkunte, Akintunde Oladipo, Jash Shah, Tara Bogavelli, Hoang Nguyen, Nishanth Madhusudhan, Vishal Juneja, Sridhar Nemala, Srinivas Sunkara, Sathwik Tejaswi Madhusudhan, Shruthan Radhakrishna, Masoud Hashemi, Kelechi Ogueji, Khalil Slimi, Saloni Mittal, Pulkit Pattnaik, Shashank Maiya, Dhruv Jhamb, Esakkivel Esakkiraja, Katrina Stankiewicz, Gabrielle Gauthier Melançon, Fanny Riols, Amit Saha, Lakshmi Sirisha Chodisetty, Nitin Aggarwal, Anil Madamala, Sagar Davasam, Segan Subramanian, Vikas Yadav, Sai Rajeswar Mudumba
- 链接：[arXiv](https://arxiv.org/abs/2610.40738) · [PDF](https://arxiv.org/pdf/2610.40738) · [HF](https://huggingface.co/papers/2610.40738)

A capable voice assistant must do more than recognize words; it must understand requests, reason over context, sustain conversations, and act through tools. We present Apriel Voice 27B Preview, an open speech-language model that unifies these capabilities within a shared reasoning backbone while retaining text and image input modalities. Built on the post-trained Gemma 4 26B-A4B checkpoint, Apriel Voice directly…

## 8. Wave Forcing: Towards Speed-of-Light Streaming Video Generation

- 分数：30.0  ·  HF 赞：40  ·  来源：huggingface
- 兴趣命中：coding
- 作者：Yijie Jin, Yuxuan Liu, Jiajun Xu, Ye Huang, Chuzhi Wang, Jiayang Li, Ruiyang Chen, Chenling Hong, Xu Wang, Zhijie Deng
- 链接：[arXiv](https://arxiv.org/abs/2611.00859) · [PDF](https://arxiv.org/pdf/2611.00859) · [HF](https://huggingface.co/papers/2611.00859)

Real-time long-video generation requires continuous output with consistent appearance and natural motion. Existing chunk-wise autoregressive methods face challenges in both generation efficiency and long-video quality: serialized denoising and history-cache refresh require two forward passes even with one-step denoising, and longer rollouts can degrade quality and cause camera drift. We propose Wave Forcing (WF),…

## 9. Latent Reasoning in Continuous Space for Unified Multimodal Models

- 分数：30.0  ·  HF 赞：28  ·  来源：huggingface
- 兴趣命中：reasoning, reinforcement learning, benchmark, language model, large language, spec
- 作者：Byungwoo Jeon, Yoonwoo Jeong, Hyunseok Lee, Minsu Cho, Jinwoo Shin
- 链接：[arXiv](https://arxiv.org/abs/2610.42149) · [PDF](https://arxiv.org/pdf/2610.42149) · [HF](https://huggingface.co/papers/2610.42149)

Unified Multimodal Models (UMMs) achieve remarkable success on diverse multimodal understanding and generation tasks, yet they still struggle to effectively leverage language-based chain-of-thought reasoning for image generation. As a result, existing reasoning-augmented UMMs often fail to inherit the test-time scaling and fine-grained controllability observed in large language models. We attribute this failure to a…

## 10. Follow the Gradient: Tracing Safety Degradation Back to Training Data

- 分数：26.5  ·  HF 赞：29  ·  来源：huggingface
- 兴趣命中：language model, large language
- 作者：Saket Reddy, Amro Abbas, Anshuman Suri, Ari Morcos, David Schwab, Pratyush Maini
- 链接：[arXiv](https://arxiv.org/abs/2610.37481) · [PDF](https://arxiv.org/pdf/2610.37481) · [HF](https://huggingface.co/papers/2610.37481)

Fine-tuning Large Language Models (LLMs) on instruction data can quietly erode their safety, even when no training example looks harmful. Because this safety-degrading data looks benign, standard content filters struggle to catch it. We tackle this problem by developing SimpleLoRIF, a scalable gradient embedding method that identifies fine-tuning examples whose gradients align with unsafe behavior. By simplifying a…

## 11. CaPtain: A Pipeline for Post-Training Code-as-Policy Robot Agents

- 分数：25.5  ·  HF 赞：19  ·  来源：huggingface
- 兴趣命中：agent, tool-use, reinforcement learning, language model, coding
- 作者：Yijia Fan, Xilin He, Yilei Jiang, Dongming Wu, Jiaxu Wang, Xiangyu Yue
- 链接：[arXiv](https://arxiv.org/abs/2610.40799) · [PDF](https://arxiv.org/pdf/2610.40799) · [HF](https://huggingface.co/papers/2610.40799)

Across coding, web, and tool-use tasks, language-model agents are now routinely trained with the same recipe: supervised fine-tuning (SFT) to learn the interface, then multi-turn reinforcement learning (RL) to master it. Code-as-policy (CaP) casts robot manipulation in the same form, as the policy writes code against robot APIs and reads back the results, so the same recipe should apply. Yet existing CaP agents…

## 12. CUA-Master: Scaling Computer-use Agents through Open-World Recursive Improvements

- 分数：25.5  ·  HF 赞：19  ·  来源：huggingface + arxiv
- 兴趣命中：agent, benchmark
- 作者：Xinlei Yu, Gen Li, Ji Zhao, Zhangquan Chen, Congcong Wang, Shuai Dong, Zelin Peng, Yuqi Xu, Hongrui Wu, Kaiwen Tuo, Cheng Yang, Kaituo Feng, Yifan Wu, Jiayi Zhang, Dongming Wu, Wenqi Shao, Jiaqi Wang, Xiangyu Yue
- 链接：[arXiv](https://arxiv.org/abs/2611.03126) · [PDF](https://arxiv.org/pdf/2611.03126) · [HF](https://huggingface.co/papers/2611.03126)

Despite recent advances in CUAs, their development remains constrained by the limited diversity, controllability, and reliability of interaction data. Moreover, conventional optimization pipelines lack iterative feedback, while existing recursive improvement approaches often rely on self-generated experiences, limiting ability expansion and yielding diminishing returns. To address these challenges, we introduce…

## 13. CEPO: A General Framework for Improving Prompt Optimization in Multi-Agent Systems

- 分数：24.0  ·  HF 赞：20  ·  来源：huggingface
- 兴趣命中：agent, benchmark, spec
- 作者：Jongha Kim, Seohyun Lee, Jonathan Minho Chung, Jinsung Yoon, Hyunwoo J. Kim
- 链接：[arXiv](https://arxiv.org/abs/2610.34722) · [PDF](https://arxiv.org/pdf/2610.34722) · [HF](https://huggingface.co/papers/2610.34722)

Multi-agent systems (MAS) require both effective coordination and specialized task execution. Existing prompt optimization approaches typically couple these functions within agent-specific prompts. We introduce Coordinator-Executor Prompt Optimization (CEPO), a general framework for improving prompt optimization in MAS. CEPO separates system-level coordination from agent-level execution through a shared coordinator…

## 14. WorldBridge: Bridging Video and Action for Task Generalization in World Action Models

- 分数：23.5  ·  HF 赞：19  ·  来源：huggingface
- 兴趣命中：memory, benchmark, spec
- 作者：Jun Cen, Yubo Guo, Hao Li, Liangkai Li, Yaoxu Lyu, Meng Wei, Zeqi Xiao, Sizhe Yang, Yuqiang Yang, Yifan Ye, Shanghang Zhang, Duo Zheng
- 链接：[arXiv](https://arxiv.org/abs/2610.40748) · [PDF](https://arxiv.org/pdf/2610.40748) · [HF](https://huggingface.co/papers/2610.40748)

Achieving the broad task generalization of embodied models in physical environments remains a central challenge in robot learning. We study this challenge in World Action Models (WAMs) through two complementary capabilities: video generalization, which predicts the visual evolution of new tasks, and action generalization, which translates these predictions into executable behavior through a video-to-action bridge.…

## 15. WeFair: Fidelity-Aware Alignment from Human Feedback for Personalized Query Rewriting in Short-Video Search

- 分数：23.0  ·  HF 赞：26  ·  来源：huggingface
- 兴趣命中：reasoning
- 作者：Yingtao Ren, Aolin Li, Cheng Cheng, Huiyun Hu, Huasheng Liang, Baoxing Xie, Jun Yuan, Haijun Wu, Yiwei Fu, Chenxing Wang
- 链接：[arXiv](https://arxiv.org/abs/2610.16927) · [PDF](https://arxiv.org/pdf/2610.16927) · [HF](https://huggingface.co/papers/2610.16927)

Short-video search needs compact query rewriters that recover users' personalized intent from ambiguous queries under strict latency constraints. Existing LLM-based methods have improved rewriting by using synthetic reasoning and subsequent consumption-behavioral feedback. However, overemphasizing subsequent consumption can favor engaging content over the user's immediate need, causing intent drift even when…

## 16. NorthCUA Technical Report: Turbocharging Computer-Use Agents through Experience at Scale

- 分数：22.5  ·  HF 赞：17  ·  来源：huggingface
- 兴趣命中：agent, reinforcement learning, evaluation
- 作者：Chaoyun Zhang, Bingxuan Li, Pinxue Guo, Yangfan Gao, Zikun Cai, Tianci Xie, Hui Li, Yuqi Huang, Yifei Cao, Bo Mao, Tian Tang, Qichang Zheng, Tongtong Liu, Xiaoxing Wang, Jinxiu Liu, Lizhi Lin, Zhou Shao, Maosen Zhou, Miao Zheng, Shuo Zhang, Yangji He, Kepeng Lei, Ning Zhao, Wei Shen, Zhenjiang Jin, Xinyue Zhang, Peng Sun, Zhenhua Han, Rui Zheng, Hang Yan
- 链接：[arXiv](https://arxiv.org/abs/2611.02102) · [PDF](https://arxiv.org/pdf/2611.02102) · [HF](https://huggingface.co/papers/2611.02102)

Scaling computer-use agents from individual actions to complex software work requires experience that connects decisions to complete outcomes. We present NorthCUA, an integrated system for turbocharging computer-use agents through experience at scale. Its Experience Flywheel supplies diverse executable tasks to the NorthCUA Harness, which sustains long interactions, records decisions, and checks task outcomes. The…

## 17. Diagnosing the Reference Gap: What Visual Scaffolds Can and Cannot Fix in Multimodal Reasoning

- 分数：22.5  ·  HF 赞：13  ·  来源：huggingface
- 兴趣命中：reasoning, benchmark, language model, large language
- 作者：Guizhen Chen, Weiwen Xu, Wotao Yin, Anh Tuan Luu, Hou Pong Chan
- 链接：[arXiv](https://arxiv.org/abs/2610.39419) · [PDF](https://arxiv.org/pdf/2610.39419) · [HF](https://huggingface.co/papers/2610.39419)

Multimodal large language models can recognize visual content yet struggle to reason reliably over it across multiple steps. In counting, a model may see all objects but lose track of which ones it has counted. We argue that such failures, commonly attributed to perception, reveal a reference gap: the failure to bind language to the relevant visual entities, regions, or locations. Motivated by the theory of visual…

## 18. Wizard: Manipulate Any World in Real Time via Agentic Control

- 分数：22.0  ·  HF 赞：24  ·  来源：huggingface
- 兴趣命中：agent
- 作者：Yuzhe Wu, Zijun Lin, Yeying Jin
- 链接：[arXiv](https://arxiv.org/abs/2610.40339) · [PDF](https://arxiv.org/pdf/2610.40339) · [HF](https://huggingface.co/papers/2610.40339)

Recent advances in video world models have enabled the generation of increasingly realistic and interactive virtual environments, opening new possibilities for player-customizable gameplay. Agentic frameworks further advance this direction by decoupling explicit game logic and controllable world representations from visual generation. However, existing approaches support only simple game settings and predefined…

## 19. Venus-DefakerOne2: A Vision-Forensics Foundation Model with Broader Coverage

- 分数：21.5  ·  HF 赞：19  ·  来源：huggingface
- 兴趣命中：benchmark, spec
- 作者：Chenfan Qu, Yachao Liang, Mingqi Fang, Jiangwei Xie, Zhenming Wang, Baoyue Zhang, Changjiang Jiang, Zheng Chang, Fanli Jin, Xuekang Zhu, Kaiwen Feng, Junchi Li, Weihong Zhang, Haoyue Wang, Chenfeng Zhang, Yinan Xia, Fangming Cui, Dong Fan, Jingjing Liu, Tianyi Zhang, Luobin Chen, Ji-Zhe Zhou, Sheng Li, Wei Wang, Bin Li, Ran He, Xinpeng Zhang, Linna Zhou, Jian Liu, Weiqiang Wang
- 链接：[arXiv](https://arxiv.org/abs/2610.37918) · [PDF](https://arxiv.org/pdf/2610.37918) · [HF](https://huggingface.co/papers/2610.37918)

Real-world forgery is inherently heterogeneous: it manifests not only as digital manipulation but also as physical spoofing, and is carried not only by images but also by videos. Despite substantial progress, a unified anti-forgery foundation model covering such a broad threat spectrum remains absent. In this paper, we present Venus-DefakerOne2, which substantially extends the forensic capability boundary along both…

## 20. ReLift: Dense 3D Tracking as Lifted Trajectory Repair

- 分数：21.0  ·  HF 赞：22  ·  来源：huggingface
- 兴趣命中：spec
- 作者：Assaf Singer, Maroun Khriesh, Noam Rotstein, Yoni Kasten, Or Litany
- 链接：[arXiv](https://arxiv.org/abs/2610.42136) · [PDF](https://arxiv.org/pdf/2610.42136) · [HF](https://huggingface.co/papers/2610.42136)

Dense 3D tracking from monocular video requires establishing point correspondences over time, estimating their depth, and inferring their trajectories during occlusion. Existing methods typically learn these tasks jointly, a demanding objective given the scarcity of 4D supervision. We show that strong pretrained 2D trackers and 3D geometry models provide an effective foundation: lifted trajectories, with occluded…

## 21. Democratizing Robot-Use Agents: A Unified Harness with Open Models

- 分数：21.0  ·  HF 赞：22  ·  来源：huggingface
- 兴趣命中：agent
- 作者：Jiarui Yuan, Yuxin Zuo, Xiaoyu Huang, Wenbo Zhang, Kwanyoung Park, Junlin Yang, Tianxiang Zhang, Ruoqu Chen, Yutao Ouyang, Bingxiang He, Xingtai Lv, Hongjin Wu, Jiajun Liu, Jiahao Zhao, Tianwei Luo, Haozhan Li, Cheng Qian, Jiaxin Ge, Huan-ang Gao, Kaisen Yang, Jiaqi Deng, Qixin Xu, Siqiao Huang, Bowen Zhou, Mengdi Xu, Zhiyuan Liu, Pieter Abbeel, Ning Ding
- 链接：[arXiv](https://arxiv.org/abs/2611.01560) · [PDF](https://arxiv.org/pdf/2611.01560) · [HF](https://huggingface.co/papers/2611.01560)

Robot-use Agents (RUAs) have shown promising zero-shot manipulation capabilities, but reliance on frontier, proprietary models limits research into further training. To democratize RUA research, we introduce uni-robot-agent, a unified harness for competitive open-weight robot use that supports further training. Without privileged inputs, an out-of-the-box Qwen3.8-Flash-Next achieves a RoboDojo Score of 31.39,…

## 22. When Requirements Interact: Scaling Long-Horizon Coding via Interdependent Specifications

- 分数：20.5  ·  HF 赞：9  ·  来源：huggingface
- 兴趣命中：agent, reasoning, reinforcement learning, benchmark, coding, spec
- 作者：Yishuo Cai, Minzheng Wang, Liang Zhao, Linghao Zhang, Lei Li, Shicheng Li, Xu Sun, Fuli Luo
- 链接：[arXiv](https://arxiv.org/abs/2610.40256) · [PDF](https://arxiv.org/pdf/2610.40256) · [HF](https://huggingface.co/papers/2610.40256)

To succeed in real-world long-horizon software development, coding agents must satisfy multi-dimensional task specifications, such as interface compatibility and error handling, and do so without breaking existing dependencies. However, current works lack specification in both quantity and diversity, often emphasizing primary goals while ignoring complex constraints. Synthesizing tasks to bridge this gap presents…

## 23. OSWAM: An Effective World Action Model with One-Step Action Generation

- 分数：20.0  ·  HF 赞：24  ·  来源：huggingface
- 兴趣命中：-
- 作者：Guowen Zhang, Liyi Chen, Xu Hu, Pengfei Wang, Jingfan Chen, Chenhang He, Lei Zhang
- 链接：[arXiv](https://arxiv.org/abs/2610.35850) · [PDF](https://arxiv.org/pdf/2610.35850) · [HF](https://huggingface.co/papers/2610.35850)

Direct-policy World Action Models (WAM) have demonstrated the benefits of decoupling action generation from explicit future visual prediction for efficient inference in autonomous driving and embodied control. However, they still require tens of denoising steps to achieve competitive action quality, incurring substantial latency and hindering real-time deployment. Simply reducing the number of denoising steps will…

## 24. Avatar Intelligence: Amplifying Human Agency Through Persistent Personal Agents

- 分数：20.0  ·  HF 赞：8  ·  来源：huggingface + arxiv
- 兴趣命中：agent, spec
- 作者：Zheng Wu, Xinbei Ma, Yao Yao, Zhaoyuan Huang, Haowen Hu, Yijie Lu, Taolei Wang, Yifei Yang, Wuyue Xiong, Pengzhou Cheng, Zhuosheng Zhang
- 链接：[arXiv](https://arxiv.org/abs/2611.03092) · [PDF](https://arxiv.org/pdf/2611.03092) · [HF](https://huggingface.co/papers/2611.03092)

Personal AI agents are increasingly capable of handling long-horizon tasks across applications, yet users often need to invest substantial effort in specifying goals, resolving ambiguity, and verifying outcomes. We argue that progress should be measured by how effectively agents amplify human agency: enabling people to pursue their goals with less routine supervision while retaining control over consequential…

## 25. HALO: Human-Grounded Granular Evaluation of Proactive Agents

- 分数：19.5  ·  HF 赞：7  ·  来源：huggingface
- 兴趣命中：agent, reasoning, evaluation, spec, retrieval
- 作者：Wenqi Pei, Xinyu Wang, Jinrui Liu, Cynthia Zhuge, Jie Sheng, Zihan Wang, Tenghao Huang, Muhao Chen
- 链接：[arXiv](https://arxiv.org/abs/2610.39086) · [PDF](https://arxiv.org/pdf/2610.39086) · [HF](https://huggingface.co/papers/2610.39086)

Proactive agents must decide whether, when, and how far to assist without an explicit request. Existing evaluations often rely on automated scores or binary verdicts, offering limited human diagnosis of evidence use and intervention quality. To address these gaps, we introduce HALO, Human-Grounded GrAnular EvaLuation of PrOactive Agents. HALO-Arena covers 4 proactive need types, Dependency, Blockage, Risk, and…

## 26. DecisionRank: On-Policy Distillation for Decision-Model Rerankers

- 分数：19.5  ·  HF 赞：7  ·  来源：huggingface
- 兴趣命中：reasoning, benchmark, coding, retrieval
- 作者：Yanran Wu, Dian Yu, Chongyang Bai, Jieyi Zhang, Rui Liu, Tianyi Chen, Shike Mei, Hang Cui, Frank Shyu, Sandeep Pandey, Luke Simon, Chunwei Liu, Xi Liu
- 链接：[arXiv](https://arxiv.org/abs/2610.42128) · [PDF](https://arxiv.org/pdf/2610.42128) · [HF](https://huggingface.co/papers/2610.42128)

Decision models target structured tasks by directly predicting choices or scores, avoiding autoregressive decoding latency. However, transferring a generative LLM's ranking knowledge to a decision model remains challenging: the teacher expresses preferences through a ranked list of document ID sequences, while the student determines the ranking using scores from the first-token position. To bridge this gap, we…

## 27. DeFT-RAG: Decomposing Multi-Hop Questions into Self-Contained Sub-Questions with Reusable Answers

- 分数：19.5  ·  HF 赞：7  ·  来源：huggingface
- 兴趣命中：language model, large language, planning, retrieval
- 作者：Dingyi Kang, Bingzhe Li
- 链接：[arXiv](https://arxiv.org/abs/2610.37826) · [PDF](https://arxiv.org/pdf/2610.37826) · [HF](https://huggingface.co/papers/2610.37826)

Retrieval-augmented generation (RAG) lets a large language model (LLM) answer questions by retrieving relevant passages from a large corpus. However, RAG struggles with multi-hop questions, which require chaining facts spread across several documents through intermediate entities that the question never mentions. Graph-based RAG methods retrieve once from the entities a question names and so rarely recover the full…

## 28. From Fragmentation to Fusion: A Survey and Roadmap for Omnimodal Embeddings

- 分数：19.0  ·  HF 赞：18  ·  来源：huggingface
- 兴趣命中：spec
- 作者：Ziyin Zhang, Yuyu Guo, Ying Zhang, Siqiao Xue, Zihan Liao, Jin Qin, Wenjie Yang, Siyuan Yang, Shijie Li, Cheng Chen, Hao Wu, Zhaoyang Zhu, Ruipeng Li, Zhaokun Jiang, Lei Lei, Rui Wang, Hang Yu, Rui Wang
- 链接：[arXiv](https://arxiv.org/abs/2611.00172) · [PDF](https://arxiv.org/pdf/2611.00172) · [HF](https://huggingface.co/papers/2611.00172)

Embedding models underpin virtually every modern AI system, from search engines to recommendation systems. Despite shared mathematical foundations, research on embedding models remains fragmented by modality: the communities develop largely in isolation, seldom exchanging insights. We argue that this fragmentation obscures a deeper convergence. Driven by contrastive learning, Transformer architectures, and a…

## 29. GLOW-FM: Efficient Generative Low-Light Image Enhancement with One-Step Latent Flow Matching

- 分数：19.0  ·  HF 赞：10  ·  来源：huggingface
- 兴趣命中：evaluation, benchmark, spec
- 作者：Ariel Lapid, Yuval Haitman, Reuven Peretz, Arnon Netzer, Idit Diamant
- 链接：[arXiv](https://arxiv.org/abs/2610.31222) · [PDF](https://arxiv.org/pdf/2610.31222) · [HF](https://huggingface.co/papers/2610.31222)

Low-light image enhancement (LLIE) aims to recover well-exposed and perceptually faithful images from severely degraded observations. Recent diffusion-based generative methods achieve strong perceptual quality by leveraging powerful image priors, but their iterative sampling incurs substantial computational cost, limiting practical deployment. Despite recent efficiency gains in generative LLIE, high-quality…

## 30. MemSteer: Turning User Histories into Supervision for Agent Memory Optimization

- 分数：19.0  ·  HF 赞：6  ·  来源：huggingface
- 兴趣命中：agent, memory, evaluation, spec, retrieval
- 作者：Jie Huang, Cuiling Lan, Qize Yu, Xiulian Peng, Yan Lu
- 链接：[arXiv](https://arxiv.org/abs/2610.39276) · [PDF](https://arxiv.org/pdf/2610.39276) · [HF](https://huggingface.co/papers/2610.39276)

An effective agent memory system should adapt to a user's history and task requirements. Human-annotated supervision can guide this adaptation by providing feedback for evaluating and improving memory designs. Yet suitable labels are rarely available for new user histories, and manually constructing QA pairs and supporting evidence is costly. We introduce MemSteer, which turns unlabeled user histories into…

## 31. RoboArchitect: Automating the Design of Robotic Agents with Persistent Memory

- 分数：19.0  ·  HF 赞：6  ·  来源：huggingface
- 兴趣命中：agent, memory, benchmark, coding, spec
- 作者：Shengguang Wu, Suning Huang, Cherie Ho, Ria Doshi, Hao Zhu, Serena Yeung-Levy
- 链接：[arXiv](https://arxiv.org/abs/2610.42141) · [PDF](https://arxiv.org/pdf/2610.42141) · [HF](https://huggingface.co/papers/2610.42141)

Recent work shows that a frozen robot policy performs far better inside an agent harness, where control code decides when to query the policy, consult vision tools, or command the arm directly. Yet today these harnesses are built by hand and redesigned for each new robot or benchmark. We show that harness design can be automated, offering a strong alternative to finetuning on a novel setup. In RoboArchitect, a…

## 32. GEPA-Curator: Curated Learning for Self Improving Agents

- 分数：18.5  ·  HF 赞：5  ·  来源：huggingface
- 兴趣命中：agent, language model, large language, retrieval
- 作者：Zack Yu, Nicholas Lee, Minjae Lee, Lakshya Agarwal, Luca Manolache, Wonjun Kang, Matei Zaharia, Michael W. Mahoney, Kurt Keutzer, Sehoon Kim, Amir Gholami
- 链接：[arXiv](https://arxiv.org/abs/2610.37651) · [PDF](https://arxiv.org/pdf/2610.37651) · [HF](https://huggingface.co/papers/2610.37651)

Large Language Models (LLMs) are increasingly used in multi-turn agentic workloads that require sustained interaction with complex environments. Existing reflective prompt optimizers such as GEPA learn from failed rollouts, but agentic failures can also come from prompt weaknesses, harness limitations, stochastic execution, or noisy judges. We argue that such failures may not provide useful learning signal, and may…

## 33. On the Origin and Evolution of Training-Inference Mismatch in LLM Reinforcement Learning

- 分数：18.0  ·  HF 赞：8  ·  来源：huggingface
- 兴趣命中：reinforcement learning, language model, large language
- 作者：Yu Li, Yufa Zhou, Tian Lan
- 链接：[arXiv](https://arxiv.org/abs/2610.40945) · [PDF](https://arxiv.org/pdf/2610.40945) · [HF](https://huggingface.co/papers/2610.40945)

On-policy reinforcement learning for large language models assumes that training responses are sampled from the current policy. In practice, an inference engine samples the responses and a separate trainer computes the gradients, and the training-inference mismatch between the two makes the training data off-policy. The mismatch has two sources, the numerics of the engine and the stale weights of asynchronous…

## 34. SOMA: A Benchmark for Fine-Grained Egocentric Behavior and Body-Motion Understanding

- 分数：18.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：reasoning, evaluation, benchmark, language model, large language, spec
- 作者：Matea Tashkovska, Naël Ouerghemi, Haozhe Qi, Alexander Mathis
- 链接：[arXiv](https://arxiv.org/abs/2610.36384) · [PDF](https://arxiv.org/pdf/2610.36384) · [HF](https://huggingface.co/papers/2610.36384)

Perceiving human body motion is critical for multimodal systems that understand and assist people. Yet current evaluations of Multimodal Large Language Models (MLLMs) largely focus on objects, scenes, and coarse actions, leaving their ability to reason about the body itself poorly assessed. This is especially challenging from the egocentric perspective, in which the body is only partially visible and motion must be…

## 35. Think Twice: The Metis-1.6 Technical Report

- 分数：18.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：memory, long context, benchmark, language model
- 作者：Giulianno Vollmer
- 链接：[arXiv](https://arxiv.org/abs/2610.37903) · [PDF](https://arxiv.org/pdf/2610.37903) · [HF](https://huggingface.co/papers/2610.37903)

Metis is a bet that better data, better training methods and new architectures can buy what a bigger parameter count cannot, at a fraction of the cost. Metis-1.6 is its latest step: two language models built from scratch by a single researcher, Praxis (2.94B parameters, 0.46B active per pass) and Logos (10.23B parameters, 1.18B active per pass). Both run a hybrid Mamba-2 and attention mixture-of-experts stack twice…

## 36. Probing Spatial State Representations in Visual Foundation Models

- 分数：17.5  ·  HF 赞：15  ·  来源：huggingface
- 兴趣命中：retrieval
- 作者：Baiqiao Yin, Zhongang Cai, Ruisi Wang, Qiwei Liang, Lei Yang, Ziwei Liu
- 链接：[arXiv](https://arxiv.org/abs/2610.40636) · [PDF](https://arxiv.org/pdf/2610.40636) · [HF](https://huggingface.co/papers/2610.40636)

An observer sees only part of the surrounding world, yet must keep track of what lies beyond the current view. Spatial perception therefore involves more than recognizing individual images: it calls for a persistent spatial state that is updated under self-motion and used to guide action. Do visual foundation models provide representations that support such a state? We study this question through four levels of…

## 37. SciGame: Let Agents Play the Scientific Discovery Games in the Real and Counterfactual World

- 分数：17.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：agent, benchmark, language model, large language
- 作者：Yusheng Zhao, Bowei He, Xue Liu, Mingxiao Li
- 链接：[arXiv](https://arxiv.org/abs/2610.37919) · [PDF](https://arxiv.org/pdf/2610.37919) · [HF](https://huggingface.co/papers/2610.37919)

Large language model agents are increasingly used for scientific discovery. However, existing benchmarks mix law inference with programming, score data fitting instead of prediction on unseen inputs, and do not separate empirical evidence from pretrained priors. We introduce SciGame, a controlled benchmark that converts scientific literature into structured scientific cards. Each card yields a pair of Original and…

## 38. MAServeBench: Benchmarking Multi-Agent LLM Serving Systems with Hierarchical Collaboration Workloads

- 分数：17.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：agent, memory, evaluation, benchmark, language model, large language, spec
- 作者：Shengxuan Qiu, Haochen Huang, Shuzhang Zhong, Zizhuo Fu, Zebin Yang, Jianming Tong, Meng Li
- 链接：[arXiv](https://arxiv.org/abs/2610.40293) · [PDF](https://arxiv.org/pdf/2610.40293) · [HF](https://huggingface.co/papers/2610.40293)

Large language model (LLM)-based multi-agent systems (MAS) coordinate specialized agents to solve complex tasks, turning each user request into interdependent model and tool operations. Unlike independent requests, these operations become ready at different times and consume evolving context as agents coordinate and exchange results. This creates changing patterns of concurrency, computation, and memory demand that…

## 39. ProVe: Proposer-Verifier Decoding

- 分数：17.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：benchmark, language model, coding, spec
- 作者：Ziqi Jin, Weiwen Xu, Jiaxi Li, Yujie Zhong, Qi She, Aixin Sun
- 链接：[arXiv](https://arxiv.org/abs/2610.27815) · [PDF](https://arxiv.org/pdf/2610.27815) · [HF](https://huggingface.co/papers/2610.27815)

Speculative decoding accelerates autoregressive (AR) language models by letting a small model draft tokens serially and a large model verify them in parallel. We reverse these roles. Starting from a standard AR checkpoint, we fine-tune the large model into a proposer that predicts a block of future tokens in a single forward pass, then use one additional forward pass to verify the proposed block. This gives ProVe,…

## 40. TinyAstral: Transferring Self-Evolving Harnesses to Tiny Generalist Manipulation Agents

- 分数：17.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：agent, memory, reasoning, benchmark, language model
- 作者：Kehong Gong, Xiaoxu Zheng, Guanli Hou, Seunghun Lee, Mengqi Guo, Runjia Tan, Zhengyu Wen, Qi Wang, Xiaoyu He, Mingyuan Zhang, Michael Bi Mi
- 链接：[arXiv](https://arxiv.org/abs/2610.41216) · [PDF](https://arxiv.org/pdf/2610.41216) · [HF](https://huggingface.co/papers/2610.41216)

Robot agents built on vision-language models depend on both the planner and its harness: the tools, feedback, memory, and recovery logic around it. Can improvements to a large teacher's harness be carried into a compact agent with lower inference compute cost? We present TinyAstral, a two-stage approach. We first freeze an open-weight teacher and improve its harness through recursive self-improvement (RSI): frontier…

## 41. SketchDirector: Complex Scene Sketching via Agentic Layout Reasoning and Detail Refinement

- 分数：16.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：agent, memory, reasoning, language model, large language
- 作者：Yiqi Liang, Xiaodong Cun
- 链接：[arXiv](https://arxiv.org/abs/2610.41260) · [PDF](https://arxiv.org/pdf/2610.41260) · [HF](https://huggingface.co/papers/2610.41260)

Existing sketch generation methods often rely on image guidance and are largely limited to individual objects or simplified scenes, leaving text-guided complex scene sketching underexplored. We present SketchDirector, an agentic framework that mimics the human sketching workflow for automatic multi-concept scene sketching. Given a scene-level text prompt, SketchDirector first employs a large language model~(LLM) to…

## 42. Lost in Recovery: Demystifying Recovery Behavior of Computer-Use Agents via Goal-Oriented Action Replay

- 分数：16.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：agent, evaluation, language model
- 作者：Byeonghun Bang, Sangwoo Park, Jinheon Baek, Kangsan Kim, Youngwan Lee, Sung Ju Hwang
- 链接：[arXiv](https://arxiv.org/abs/2610.27954) · [PDF](https://arxiv.org/pdf/2610.27954) · [HF](https://huggingface.co/papers/2610.27954)

Recent advances in large (vision) language models have enabled computer-use agents that automate digital workflows via fine-grained keyboard and mouse operations. However, such agents remain fragile in long-horizon settings, where errors accumulate and executed actions leave unintended side effects, making the ability to recover from failures critical. Yet, existing remedies remain inadequate: environment resets are…

## 43. Self-Improvement with Auxiliary Rewards: Learning from Verified Traces and Evaluating Transfer

- 分数：15.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：reasoning, evaluation, benchmark
- 作者：Minju Gwak, Alan Ritter
- 链接：[arXiv](https://arxiv.org/abs/2610.41296) · [PDF](https://arxiv.org/pdf/2610.41296) · [HF](https://huggingface.co/papers/2610.41296)

Answer-level rewards cannot distinguish reasoning traces with equally correct outcomes. We study whether auxiliary trajectory preferences improve small-language-model self-improvement and transfer under limited supervision. We compare confidence-based (SC) and entropy-based metrics (UID-Conj.), which combines global entropy variation and local smoothness, through online reward augmentation and offline training on…

## 44. Supervising the Visible State: Separating Representation from View Selection in Streaming Video

- 分数：14.5  ·  HF 赞：5  ·  来源：huggingface
- 兴趣命中：reasoning, spec
- 作者：Yihao Hu, Pan Wang, Yitong Lin, Zhihao Wen, Deyuan Liu, Hang Wang, Mingda Wan, Yiwen Zhao, Yutong Li, Yuchen Mao, Tao Lin
- 链接：[arXiv](https://arxiv.org/abs/2610.34926) · [PDF](https://arxiv.org/pdf/2610.34926) · [HF](https://huggingface.co/papers/2610.34926)

An action seen once and the same action seen three times receive the same action-recognition label, so that supervision does not require a model to count. Answers shared across histories that differ in event order, accumulation, or relations leave those distinctions unconstrained; we call this state under-specification. Visible-State Supervision (ViSS) addresses it by training on source-grounded probes of event…

## 45. TSFLab: A Self-Improving Agent-Agnostic Workbench for Time Series Forecasting Research

- 分数：14.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：agent, benchmark, coding
- 作者：ChengAo Shen, Yanjun Zhao, Haoxin Liu, Bonnie Chen, Miles Ma, Dongjin Song, Hanghang Tong, Qingsong Wen, Jingrui He, Jingchao Ni
- 链接：[arXiv](https://arxiv.org/abs/2610.40901) · [PDF](https://arxiv.org/pdf/2610.40901) · [HF](https://huggingface.co/papers/2610.40901)

As publications and products on time series forecasting (TSF) proliferate, researchers face a growing burden of analyzing existing work. First, not all publications release code. For instance, only about 20% of arXiv TSF papers have a code link in the surveyed period. Second, released code also requires manual maintenance. Thus, TSF researchers must constantly adapt or implement existing works. However, independent…

## 46. VoxLock: Target-Speaker Extraction for Voice Agents Without an Enrollment Step

- 分数：13.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：agent, benchmark
- 作者：Arbaz Siddiqui
- 链接：[arXiv](https://arxiv.org/abs/2610.40727) · [PDF](https://arxiv.org/pdf/2610.40727) · [HF](https://huggingface.co/papers/2610.40727)

A voice agent's speech recognizer transcribes everyone near the microphone, including people other than the caller. I fine-tuned a public causal target-speaker extraction model (REAL-TSE, 27M parameters) on one GPU to work from a voice sample cut from the call itself, and released it as VoxLock. I score it by what a recognizer writes on real recordings. On Krisp's 265-recording benchmark it reaches 4.95% WER against…

## 47. rTaste: Do Research Agents Have Taste? Evaluating Early Stage Research Judgment

- 分数：13.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：agent, evaluation
- 作者：Art Kanke
- 链接：[arXiv](https://arxiv.org/abs/2610.40488) · [PDF](https://arxiv.org/pdf/2610.40488) · [HF](https://huggingface.co/papers/2610.40488)

Do research agents have taste, the judgment of which experiments are worth running before their outcomes are known? We give six frontier models seven recent NLP papers. Each model, working as a research agent alone or as a team, proposes minimum viable experiments (MVEs), forecasts whether each will pass a threshold it sets and ranks them. A separate executor then attempts every MVE, including those ranked last, and…

## 48. TurnTurk-GPT: Text-Based Turn-Taking Prediction for Turkish

- 分数：13.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：evaluation, language model
- 作者：Ahmet Tuğrul Bayrak, Fatma Nur Korkmaz, Nur Yağmur Tuncer, Mustafa Sertaç Türkel
- 链接：[arXiv](https://arxiv.org/abs/2610.42010) · [PDF](https://arxiv.org/pdf/2610.42010) · [HF](https://huggingface.co/papers/2610.42010)

This paper presents TurnTurk-GPT, a text-based turn-taking predictor for Turkish obtained by fine-tuning a Turkish GPT-2 model with the TurnGPT objective on synthetic and real dialogue, and evaluates it on real Turkish conversation against rule baselines, a zero-shot Turkish language model and a widely used multilingual end-of-turn detector. Evaluation uses word-level decision points on unpunctuated, lower-cased…

## 49. Learning Quality-Controllable Robot Policies with Iterative Hindsight Relabeling

- 分数：11.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：evaluation
- 作者：Sinjae Kang, Dong Kyu Shin, Jaehong Kim, Kamin Lee, Hyoeun Kim, Kaixin Wang, Li Zhao, Seonghyeon Ye, Kimin Lee
- 链接：[arXiv](https://arxiv.org/abs/2610.37393) · [PDF](https://arxiv.org/pdf/2610.37393) · [HF](https://huggingface.co/papers/2610.37393)

Robot policy evaluation often relies on a binary success signal for task completion. In real-world deployment, however, desired execution behaviors are also defined by quality attributes such as execution speed and motion smoothness, which need to be dynamically controlled according to task requirements. To address this, we introduce Quality-Controllable Policy (QCP), a robot policy that enables inference-time…

## 50. No Channels Left Behind: Understanding Diffusion Acceleration through Residual Gates

- 分数：10.5  ·  HF 赞：5  ·  来源：huggingface
- 兴趣命中：-
- 作者：Junha Park, Jaemyung Yu, Jaehui Hwang, Jong-Seok Lee, Dongyoon Han
- 链接：[arXiv](https://arxiv.org/abs/2610.40914) · [PDF](https://arxiv.org/pdf/2610.40914) · [HF](https://huggingface.co/papers/2610.40914)

Training acceleration methods for diffusion transformers, such as REPA and dispersive regularization, are commonly explained by additional supervision, spatial-structure priors, or improved feature geometry. We revisit this view and uncover a striking internal change: the AdaLN-Zero residual gate α, which directly controls how conditioned updates enter the residual stream, is substantially reorganized by these…

## 51. TernScope: Model-Hardware Co-Design for Efficient Ternary Endoscopic Segmentation

- 分数：9.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：-
- 作者：Zhuoyu Wu, Wenhui Ou, Qiawei Zheng, Xuhong Qiu, Wenqi Fang, Raphaël C. -W. Phan
- 链接：[arXiv](https://arxiv.org/abs/2610.29617) · [PDF](https://arxiv.org/pdf/2610.29617) · [HF](https://huggingface.co/papers/2610.29617)

Edge medical segmentation must reconcile small model size, high accuracy, and fast inference. TernScope addresses this tradeoff through model--hardware co-design, learning a compact segmentation network whose low-bit operators also simplify hardware execution. Split-channel large-kernel blocks preserve spatial context with limited computation, while branch fusion removes redundant inference paths. Ternary…

## 52. CausalWAM: Learning the Causes of Actions in World Action Models

- 分数：9.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：-
- 作者：Juntao Cheng, Jinzhou Tang, Fan Feng, Henrik I. Christensen, Yujia Zheng
- 链接：[arXiv](https://arxiv.org/abs/2610.42096) · [PDF](https://arxiv.org/pdf/2610.42096) · [HF](https://huggingface.co/papers/2610.42096)

World action models (WAMs) learn latent variables from observations and use these to both predict the evolution of the scene and to generate actions. The prediction has to be of the whole scene, whereas only a portion of the scene causes actions. WAMs fitted to demonstrations do not, in general, guarantee that they will generate actions solely from the latent causes of the demonstrated actions (the action-relevant…

## 53. On-Policy Self-Distillation with Teacher Evolution

- 分数：9.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：-
- 作者：Shufan Shen, Zhongni Hou, Chao Bi, Yufei Zhang, Guojun Yin, Shuhui Wang
- 链接：[arXiv](https://arxiv.org/abs/2610.38637) · [PDF](https://arxiv.org/pdf/2610.38637) · [HF](https://huggingface.co/papers/2610.38637)

On-Policy Self-Distillation (OPSD), which aligns a student model's token-level distribution with that of its self-teacher prompted by privileged context, has emerged as a promising direction to mitigate reward sparsity in sequence-level post-training paradigms. However, OPSD often fails to achieve continuous performance gains during training. In this paper, we find that the model's limited self-teaching capability…

## 54. SpecPilot: Autonomous Algorithm Discovery and Systems Optimization for Speculative Decoding

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, memory, benchmark, coding, spec
- 作者：Kunjun Li, Wenhao Chai, Yihao Liang, Yuezhou Hu, Shuyao Xu, Yi Pan, William X. Zheng, Kannan Ramchandran, Kurt Keutzer, Jiantao Jiao
- 链接：[arXiv](https://arxiv.org/abs/2611.02501) · [PDF](https://arxiv.org/pdf/2611.02501) · [HF](https://huggingface.co/papers/2611.02501)

Speculative decoding accelerates memory-bound LLM decoding with a lightweight drafter, and parallel drafters extend this speedup by drafting a whole block in one forward pass. However, it remains unclear whether their released systems (stock) attain the full speedup that parallel drafting permits. We identify three challenges. First, with one request, each step accepts few tokens but reads every target weight.…

## 55. Towards Multi-Value Alignment via Value Localization in LLMs

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, language model, large language, spec
- 作者：Xueqi Ma, Yanbei Jiang, Xingjun Ma, James Bailey, Sarah M. Erfani
- 链接：[arXiv](https://arxiv.org/abs/2611.02503) · [PDF](https://arxiv.org/pdf/2611.02503) · [HF](https://huggingface.co/papers/2611.02503)

Aligning large language models (LLMs) with multiple, potentially conflicting human values remains challenging, as existing multi-objective alignment methods often require costly fine-tuning and provide limited insight into the internal mechanisms underlying value-related behaviors. In this work, we investigate multi-value alignment from a mechanistic interpretability perspective by identifying value-sensitive…

## 56. Cumulative and Audited Guardrail Tool Evolution for LLM Agent Safety

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, benchmark, language model, large language
- 作者：Xiao Yang, Aishan Liu, Siyuan Liang, Zonghao Ying, Le Wang, Jiakai Wang, Xianglong Liu, Dacheng Tao
- 链接：[arXiv](https://arxiv.org/abs/2611.02516) · [PDF](https://arxiv.org/pdf/2611.02516) · [HF](https://huggingface.co/papers/2611.02516)

Large language model (LLM) agents increasingly operate in open-world environments where safety risks cannot be fully predefined. However, most existing guardrail mechanisms remain static, relying on fixed rules, prompts, or classifiers that generalize poorly to emerging risks. Here we present EVOLVE, a tool-level self-evolving defense framework that formulates agent security as a process of cumulative security…

## 57. FORGE: Fault-Oriented Rework Code Generation for Executable Interlocking Assembly

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, benchmark, language model, large language
- 作者：Fuqiang Wang, Jiahao Fu, Ren Hefeng, Yining Qian, Chuanting Zhang, Cheng Tan, Yuwen Liu, Jingxuan Wei
- 链接：[arXiv](https://arxiv.org/abs/2611.02536) · [PDF](https://arxiv.org/pdf/2611.02536) · [HF](https://huggingface.co/papers/2611.02536)

Large language models have demonstrated strong capabilities in structured reasoning and code generation, yet identifying an assembly fault does not guarantee the ability to generate executable rework programs. In interlocking assemblies, a locally plausible repair program may violate blocking dependencies, omit required recovery operations, or terminate in an incorrect configuration. We identify this challenge as…

## 58. PixelBench: Can LLMs Understand and Generate Images Pixel by Pixel?

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, language model, large language, spec
- 作者：Haoquan Zhang, Feiyang Liu, Juanxi Tian, Wanhua Li, Haodong Duan, Weiyang Liu
- 链接：[arXiv](https://arxiv.org/abs/2611.02540) · [PDF](https://arxiv.org/pdf/2611.02540) · [HF](https://huggingface.co/papers/2611.02540)

Large language models (LLMs) can generate visual assets through text-based formats such as SVG and CAD, but these symbolic representations describe images using high-level primitives rather than explicit raster values. We ask whether LLMs can instead generate pixel images directly through their existing vocabulary, without a learned image tokenizer or decoder. We introduce PixelBench, a benchmark for text-to-pixel…

## 59. EEFA: A Framework for the Ethical Evaluation of AI Agents

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, evaluation, benchmark, spec
- 作者：Swathi Pallikala, Yashas Hariprasad
- 链接：[arXiv](https://arxiv.org/abs/2611.02561) · [PDF](https://arxiv.org/pdf/2611.02561) · [HF](https://huggingface.co/papers/2611.02561)

The rapid deployment of autonomous AI agents across consequential domains including healthcare, legal services, nancial management, and enterprise workows has created an urgent governance challenge. While the eld of AI evaluation has produced sophisticated benchmarks for measuring agent capability, these frameworks measure exclusively what agents can do rather than how they do it. The ethical dimensions most…

## 60. SMILE: A Structured Multi-Agent Clinical Reasoning for Liver Ultrasound Understanding

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reasoning, language model, spec
- 作者：Haris Ghafoor, Minjee Seo, Seonaeng cho, Keungmo Yang, Jaejun Lee, Kyungho Yoon
- 链接：[arXiv](https://arxiv.org/abs/2611.02581) · [PDF](https://arxiv.org/pdf/2611.02581) · [HF](https://huggingface.co/papers/2611.02581)

Automated liver ultrasound report generation improves the diagnosis of liver diseases by producing clinically structured descriptions of anatomical and disease-related findings. However, current generative vision-language models (VLMs) often rely on a single reasoning pathway that maps ultrasound appearance directly to textual descriptions. In addition to the inherent vision-language modality gap, this design is…

## 61. From Language to Country to Valence: A Multilingual Audit of Stereotype Bias Across LLMs

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, language model, large language, spec
- 作者：Zihao Sun
- 链接：[arXiv](https://arxiv.org/abs/2611.02585) · [PDF](https://arxiv.org/pdf/2611.02585) · [HF](https://huggingface.co/papers/2611.02585)

Large language models (LLMs) are increasingly considered for education, recruitment, workplace decision support, and other consequential applications, making pre-deployment social-bias detection essential. Yet major benchmarks are English-centred or translated, focus mainly on negative stereotypes, and may miss linguistic and cultural variation. We investigate gender, racial, and religious bias using 12,000 locally…

## 62. They Know Where It Is, But Not What It Says: A Bilingual Hallucination Benchmark of Hadith Recall in Open LLMs

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, evaluation, benchmark, language model, large language, spec, retrieval
- 作者：Dayam Nadeem, Safdar Mustafa, Ameen Ur Rehman, Shahab Saquib Sohail, Mohammad Nadeem, Usman Naseem
- 链接：[arXiv](https://arxiv.org/abs/2611.02587) · [PDF](https://arxiv.org/pdf/2611.02587) · [HF](https://huggingface.co/papers/2611.02587)

Large language models are increasingly consulted for religious knowledge, including the recall of specific Hadith (recorded sayings and actions of the Prophet Muhammad, peace be upon him). Unlike open-ended generation, Hadith recall is a high-stakes, verifiable task: a reference (collection, chapter, and Hadith number) has exactly one correct text, and any deviation from it constitutes a fabrication that can be…

## 63. AVID: A 5T fMRI Dataset for Benchmarking Auditory-induced Visual Mental Imagery Decoding

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, evaluation, benchmark, coding, spec
- 作者：Shiqi Shen, Shurui Li, Xilin Zhang, Yuanning Li
- 链接：[arXiv](https://arxiv.org/abs/2611.02593) · [PDF](https://arxiv.org/pdf/2611.02593) · [HF](https://huggingface.co/papers/2611.02593)

Visual mental imagery (VMI) decoding uses brain activity to reconstruct internally generated visual scenes, providing a potential pathway for externalizing internal experiences and developing neuroprosthetic communication interfaces. However, progress is limited by the lack of dedicated, training-scale VMI datasets. Current VMI paradigms often rely on visual prompts or short-term memory images, introducing visual…

## 64. StateFence: Task-State Protection Against Evidence-Chain Contamination in Blue-Team LLM Agents

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, memory, evaluation, language model, large language, retrieval
- 作者：Haowen Dai, Alejandro Guerra-Manzanares
- 链接：[arXiv](https://arxiv.org/abs/2611.02605) · [PDF](https://arxiv.org/pdf/2611.02605) · [HF](https://huggingface.co/papers/2611.02605)

Indirect prompt injection creates a distinctive risk for blue-team Large Language Model (LLM) agents in Security Operations Centers (SOCs). Malicious instructions can be embedded in telemetry, tickets, retrieval results, or memory and then propagate through alert triage, incident summarization, response recommendation, and Indicator of Compromise (IOC) extraction as locally plausible intermediate decisions. We…

## 65. Scalaris: A Scalable Enterprise Memory Architecture for Conversational AI Assistants

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, benchmark, spec, retrieval
- 作者：Devarsh Gandhi, Sarthak Pawar, Hemprasad Badgujar, Vaibhav Rathore, Siddharth Sureka, Neha Bhargava
- 链接：[arXiv](https://arxiv.org/abs/2611.02612) · [PDF](https://arxiv.org/pdf/2611.02612) · [HF](https://huggingface.co/papers/2611.02612)

Enterprise conversational systems require memory to personalize interactions, retain information across sessions, and maintain conversational coherence. At enterprise scale, however, memory must not only retrieve relevant information accurately but also provide it efficiently to the answer-generation model. Existing memory systems face a trade-off between retrieval accuracy and context efficiency. Retrieving more…

## 66. Widening Harm Evaluation Coverage with a Judge that Reads the World

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, evaluation, coding, spec
- 作者：Prabhpreet Singh Setia, Bhavesh Neekhra, Debayan Gupta
- 链接：[arXiv](https://arxiv.org/abs/2611.02624) · [PDF](https://arxiv.org/pdf/2611.02624) · [HF](https://huggingface.co/papers/2611.02624)

An agent acting in a stateful environment can leave evidence of harm in two places: the record of what it did and said, or the world it changed. Safety evaluations for discovering harm examine one or the other in limited ways, using either an LLM judge over the trajectory or deterministic checks over the final state. Although LLM-based verifiers that inspect the environment exist, they have been used to verify task…

## 67. Measuring AI Agents as Teammates with Collaborative Intelligence

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, evaluation, benchmark, coding
- 作者：Sean Wu, Aneesh Pappu, Jiaru Zou, Yubin Kim, Yuncong Mao, Hongjian Zhou, Junchi Yu, Jieneng Chen, James Zou
- 链接：[arXiv](https://arxiv.org/abs/2611.02633) · [PDF](https://arxiv.org/pdf/2611.02633) · [HF](https://huggingface.co/papers/2611.02633)

Progress in AI is often measured by what a single model can do on its own. Yet teams of AI agents are starting to make breakthroughs and discoveries in science, medicine, mathematics and software engineering. As AI begins to work in teams of agents and people, the ability to collaborate becomes a core part of their intelligence. Research on human teams has measured this ability for decades. Inspired by this, we…

## 68. Variable names provide priors: semantic grounding enables data-efficient numerical prediction by large language models

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, language model, large language, spec
- 作者：Xin-Rui Ma, Shi-Zhi Chen, Hai-Yan Jiang, De-Cheng Feng, Michael Beer
- 链接：[arXiv](https://arxiv.org/abs/2611.02637) · [PDF](https://arxiv.org/pdf/2611.02637) · [HF](https://huggingface.co/papers/2611.02637)

Large language models (LLMs) have achieved strong performance across diverse tasks, from question answering to code generation. Recent studies have found that LLMs can perform numerical prediction on tabular datasets via in-context learning. However, it remains unclear under what conditions and how LLMs use variable names and in-context examples for numerical prediction. Here we show that semantic grounding, the…

## 69. SearchInject: Retrieval Exposure Control for Indirect Prompt Injection in Language-Model Search

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, language model, large language, retrieval
- 作者：Kainan Zhou, Gangzhen Qian, Janet Sung, Zhi Jing, Rong Bao, Qianru Lao
- 链接：[arXiv](https://arxiv.org/abs/2611.02643) · [PDF](https://arxiv.org/pdf/2611.02643) · [HF](https://huggingface.co/papers/2611.02643)

An indirect prompt injection can affect a search-augmented large language model only after its carrier page reaches model context. SearchInject controls this admission decision with a joint score combining retrieval relevance, search-abuse cues, instruction likelihood, and two relevance interactions. A quarantine threshold is selected under an empirical 0.5% clean-candidate false-quarantine constraint on a…

## 70. ReinSeg: Retrieval-Guided Bounded Multimodal Refinement for 3-D Road Anomaly Segmentation

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, benchmark, spec, retrieval
- 作者：Haifa Zhang, Yijing Wang, Zhiqiang Zuo
- 链接：[arXiv](https://arxiv.org/abs/2611.02648) · [PDF](https://arxiv.org/pdf/2611.02648) · [HF](https://huggingface.co/papers/2611.02648)

3-D road anomaly segmentation is essential for risk-aware perception in autonomous driving. Its central challenge is to rank sparsely observed hazards ahead of abundant normal road structures while preserving point-wise metric localization. LiDAR provides accurate 3-D point support, whereas surround-view imagery offers complementary semantic context for separating unexpected hazards from challenging normal…

## 71. Parametric CAD Bench v3: Evaluating Agentic Parametric CAD Authoring from Text and Engineering Drawings

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, evaluation, benchmark, spec
- 作者：Mei Chen, Yu Xia, Haipeng Mao
- 链接：[arXiv](https://arxiv.org/abs/2611.02659) · [PDF](https://arxiv.org/pdf/2611.02659) · [HF](https://huggingface.co/papers/2611.02659)

Producing an executable CAD script is not sufficient to establish that an agent has satisfied an engineering design request. Evaluation must also consider the resulting geometry, specified dimensions, and native CAD modeling history. We present Parametric CAD Bench v3, a 100-task benchmark comprising 30 text-to-CAD creation tasks, 30 text-to-CAD create-and-edit tasks, and 40 tasks that reconstruct mechanical parts…

## 72. UPSHIFT: User Preference Steering from Human-AI Interaction Feedback Traces

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, evaluation, language model, large language, spec
- 作者：Jingping Wang, Zhanhao Li, Shao Zhang, Shuyue Hu
- 链接：[arXiv](https://arxiv.org/abs/2611.02667) · [PDF](https://arxiv.org/pdf/2611.02667) · [HF](https://huggingface.co/papers/2611.02667)

Personalizing large language model assistants requires adapting their responses to individual users, including the selection of content, reasoning approach, level of detail, and form of presentation. Such preferences are often latent, becoming visible only when users respond to an initial answer and request revisions. We investigate whether these feedback trajectories can be converted into a reusable personalization…

## 73. LLMs Cannot Be Neutral: Gender Sensitivity Across Candidates, Evaluators, and Models

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, language model, large language, spec
- 作者：Danial Amin, Joni Salminen, Bernard J. Jansen
- 链接：[arXiv](https://arxiv.org/abs/2611.02692) · [PDF](https://arxiv.org/pdf/2611.02692) · [HF](https://huggingface.co/papers/2611.02692)

Large language models (LLMs) are increasingly used to evaluate candidates for professional roles, raising concerns about their sensitivity to demographic identities. We examine how candidate and evaluator gender assignments affect decisions by LLM-as-a-Judge (LaJ) models and decision language models (DLMs). In a hypothetical city council voting task, eight models evaluated 240 synthetic professional narratives from…

## 74. GeoGuesser Bench: Benchmarking Vision-Language Agents on Interactive Geolocation

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, tool-use, benchmark, language model
- 作者：Huanzhi Mao, Yichuan Wang, Michael Koo, Wenyuan Huang, Huy Doan, Jinghan Xia, Ziyao Wang, Joseph E. Gonzalez
- 链接：[arXiv](https://arxiv.org/abs/2611.02698) · [PDF](https://arxiv.org/pdf/2611.02698) · [HF](https://huggingface.co/papers/2611.02698)

Vision-language model (VLM) agents that act in the open world need two abilities: world knowledge to interpret what they see, and exploration to find what they cannot yet see. We study how agents combine the two through interactive visual geolocation. GeoGuesser Bench contains 282 tasks in an offline Street View environment where agents rotate, zoom, and move between real panoramas. Its three task types shift the…

## 75. Beyond Answers, Traces, and Efficiency: Evidence for Adaptive Reasoning

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, evaluation, benchmark, spec
- 作者：Sejin Kim, Sundong Kim
- 链接：[arXiv](https://arxiv.org/abs/2611.02704) · [PDF](https://arxiv.org/pdf/2611.02704) · [HF](https://huggingface.co/papers/2611.02704)

Current AI systems are evaluated as reasoners through final-answer accuracy, reasoning traces, process supervision, and computational or human-relative efficiency. Yet these measures do not establish whether reasoning adapts when tasks or evidence change. We distinguish across-task adaptivity, where acquired abstractions transfer or recombine across novel problems, fromwithin-task adaptivity, where hypotheses and…

## 76. AffToM: Benchmarking Recursive Affective Theory of Mind in Dynamic Multi-Party Interactions

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reasoning, reinforcement learning, benchmark, spec
- 作者：Jinpeng Hu, Yiduo Jin, Erqiang Wang, Jia Li, Jingjing Wu, Peipei Song
- 链接：[arXiv](https://arxiv.org/abs/2611.02725) · [PDF](https://arxiv.org/pdf/2611.02725) · [HF](https://huggingface.co/papers/2611.02725)

Understanding emotion in realistic social interactions requires more than recognizing facial expressions or assigning affective labels. The same event can elicit different emotions depending on what each participant knows, what they believe others know or feel, and how these nested mental states evolve over time. Existing benchmarks largely study higher-order epistemic Theory of Mind (ToM) and multimodal emotion…

## 77. Lookahead Prediction-Guided Adaptive Visual Refocusing for Interleaved Multimodal Reasoning

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, benchmark, language model, large language, coding, spec
- 作者：Mengzhao Wang, Yanli Ji, Peng Ye
- 链接：[arXiv](https://arxiv.org/abs/2611.02780) · [PDF](https://arxiv.org/pdf/2611.02780) · [HF](https://huggingface.co/papers/2611.02780)

Interleaved multimodal chain-of-thought reasoning improves the visual reasoning capabilities of multimodal large language models by dynamically incorporating visual evidence during reasoning. However, existing methods primarily select evidence from historical context. When the reasoning focus shifts, history-guided evidence may remain focused on prior regions and fail to cover the visual information required by the…

## 78. HLSClaw: Bringing Vibe Coding to High-Level Synthesis through Skill-Based Agentic Harness

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, benchmark, coding, spec
- 作者：Jinming Ge, Shang Liu, Jiawei Liang, Shangkun Li, Afzal Ahmad, Jiang Xu, Linfeng Du, Wei Zhang
- 链接：[arXiv](https://arxiv.org/abs/2611.02784) · [PDF](https://arxiv.org/pdf/2611.02784) · [HF](https://huggingface.co/papers/2611.02784)

LLM agents are rapidly shifting software development toward intent-driven \emph{vibe coding}, yet their effectiveness drops sharply in high-level synthesis (HLS), where code optimization must jointly consider design structure, directive search, and downstream hardware constraints. Existing HLS optimization approaches, including both heuristic-based methods and recent LLM-assisted pipelines, typically operate at…

## 79. PGuard: A Native, Streaming, and Plug-in Guardrail for Multimodal Large Language Models

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, language model, large language, coding, spec
- 作者：Junyu Lin, Mengjie Wu, Yonghao Dong, Yuchuan Fu, Jinfeng Li, Xiaodan Li, Xiaohan Yuan, Yicheng Liu, Yuefeng Chen, Hui Xue, Jingyi Wang, Yitong Yang, Jiyuan Fu, Qinga He
- 链接：[arXiv](https://arxiv.org/abs/2611.02791) · [PDF](https://arxiv.org/pdf/2611.02791) · [HF](https://huggingface.co/papers/2611.02791)

As streaming generation becomes the dominant serving paradigm for both text-only and multimodal large language models, ensuring safety throughout the generation process has become a critical challenge. We introduce PGuard, a native, streaming, and plug-in guardrail that transforms safety monitoring from an external serving dependency into an integrated capability of the backbone model. PGuard directly leverages the…

## 80. SelfImprove-Bench: Evaluating Generalization in Self-Improving Agents

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reasoning, evaluation, planning
- 作者：Bangrui Xu, Jie Yang, Sidi Chen, Xuanhe Zhou, Jiantao Qiu, Qianyu Yang, Zijie Wang, Fan Wu, Zhoufutu Wen
- 链接：[arXiv](https://arxiv.org/abs/2611.02797) · [PDF](https://arxiv.org/pdf/2611.02797) · [HF](https://huggingface.co/papers/2611.02797)

Recursively self-improving (RSI) systems are increasingly viewed as a promising means of accelerating progress toward artificial general intelligence. They aim to autonomously improve their capabilities by refining their working pipelines and recursively improving the strategies that guide subsequent refinements, with gains generalizing to unseen scenarios.However, existing evaluations lack reliable metrics to…

## 81. Creating Hybrid Interactive Narrative Systems with LLM: From Formal Description to Evaluation

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, language model, large language, spec
- 作者：Jules Clerc, Domitile Lourdeaux, Mohamed Sallak, Marc Ravaine
- 链接：[arXiv](https://arxiv.org/abs/2611.02807) · [PDF](https://arxiv.org/pdf/2611.02807) · [HF](https://huggingface.co/papers/2611.02807)

Interactive narratives let users shape a story while an Experience Manager (EM) keeps it coherent, balancing player freedom against authorial control. Large Language Models now enable a new generation of hybrid EMs, which combine run-time generation from free-text input with symbolic narrative control. However, their heterogeneity makes them hard to compare: A manager's behaviour is generally tied to the unique and…

## 82. TRIO: Task Refinement with Individual Optimization for Retrieval-Augmented Generation

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, benchmark, language model, spec, retrieval
- 作者：Yingtao Ren, Xiao Luo, Yiwei Fu, Jinzhao Zhou, Yu-Cheng Chang, Chin-Teng Lin
- 链接：[arXiv](https://arxiv.org/abs/2611.02810) · [PDF](https://arxiv.org/pdf/2611.02810) · [HF](https://huggingface.co/papers/2611.02810)

This paper studies retrieval-augmented generation (RAG), which leverages external knowledge to improve the performance of language models. Despite the remarkable progress, current RAG approaches are still far from satisfactory due to inadequate retrieval and potential hallucinations. Towards this end, we propose a novel approach named Task Refinement with Individual Optimization (TRIO) for RAG. The core idea of our…

## 83. Discovering hierarchical governing equations for community-structured complex network dynamics with LLM agents

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, language model, large language, spec
- 作者：Jinlei Zhang, Zixuan Zhang, Hao Qiu, Feng Chen, Jiateng Yin, Xiaoyong Yan, Xiaolei Ma, Hao Sun, Jianxi Gao, Lixing Yang, Ziyou Gao
- 链接：[arXiv](https://arxiv.org/abs/2611.02816) · [PDF](https://arxiv.org/pdf/2611.02816) · [HF](https://huggingface.co/papers/2611.02816)

Governing equations provide an interpretable description of the mechanisms underlying complex network dynamics, yet their discovery from observational data remains challenging when shared community-level dynamics coexist with individual-level variations and the relevant functional structures may be absent from the initial candidate library or not explicitly specified in advance. Here we formulate this task as a…

## 84. Predictive Safety Guardrails Do Not Always Make LLM Agents Safer

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, evaluation, language model, large language, spec
- 作者：Weixiang Zhao, Zhihao Liu, Guancheng Li, Yanyan Zhao, Bing Qin, Ting Liu
- 链接：[arXiv](https://arxiv.org/abs/2611.02815) · [PDF](https://arxiv.org/pdf/2611.02815) · [HF](https://huggingface.co/papers/2611.02815)

Large language model agents increasingly take consequential actions in digital and physical environments, where safety risks may emerge only after multiple interaction steps. This has motivated world-model-driven predictive safety guardrails, which anticipate future consequences before execution. However, existing evaluations largely focus on end-to-end safety outcomes, leaving unclear whether safety gains arise…

## 85. RxnMiner: A Multimodal Agent for Structured Reaction Data Extraction from Chemistry Figures

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, benchmark, spec, planning
- 作者：Jinbo Hu, Songren Zhang, Chuanxun Fu, Jinrui Huang, Zhen Hao Wong, Dongxu Cui, Haoran Fan, Muhao Ge, Zhen Jian, Jian Zhou, Chengxiang Luo, Han Lyu, Haoyi Tao, Chaozheng Huang, Hanzheng Li, ZiChen Wang, Hengtian Ma, Jinyang Dai, Nan Wang, Yanhui Hong, Xi Fang, Guolin Ke
- 链接：[arXiv](https://arxiv.org/abs/2611.02826) · [PDF](https://arxiv.org/pdf/2611.02826) · [HF](https://huggingface.co/papers/2611.02826)

Reaction data underpin machine learning for reaction prediction, condition recommendation, and retrosynthetic planning, yet extracting these data from literature figures still requires substantial manual effort. Many figures encode multiple experiments through shared templates, substituent tables, and product grids. Recovering concrete reaction records therefore requires molecular recognition, association of…

## 86. Think with Skills: Pseudocode Planning Before Execution for Advanced Reasoners

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reasoning, language model, spec, planning
- 作者：Boshen Zhou, Boxuan Yue, Xiang Li, Shanchao Yang
- 链接：[arXiv](https://arxiv.org/abs/2611.02830) · [PDF](https://arxiv.org/pdf/2611.02830) · [HF](https://huggingface.co/papers/2611.02830)

Language model agents often struggle with complex tasks even when equipped with expert-written skills. Such skills encode declarative knowledge, whereas successful execution requires procedural knowledge tailored to the task at hand. Natural language skills may leave conditions and dependencies implicit, and tasks involving multiple skills further require agents to coordinate intermediate results and execution…

## 87. Math Foundation Formalization Agent: A General-Purpose Approach to Formalizing Mathematical Foundations

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reasoning, language model, large language
- 作者：Jiaxin Xie, Guowei Dou, Xiang Ji, Wensheng Yu
- 链接：[arXiv](https://arxiv.org/abs/2611.02843) · [PDF](https://arxiv.org/pdf/2611.02843) · [HF](https://huggingface.co/papers/2611.02843)

Mathematical formalization plays an important role in establishing rigorous and machine-verifiable foundations for mathematical reasoning. With the development of large language models (LLMs) and interactive theorem provers, intelligent agents offer a promising approach to automating the formalization of mathematical theories. This paper presents the Math Foundation Formalization Agent (MFF-Agent), a general-purpose…

## 88. SpecOPD: Branch-Parallel On-Policy Distillation for Speculative Decoding

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, language model, large language, coding, spec
- 作者：Tianyu Liu, Jun Zhang, Wenjie Huang, Yuhao Shen, Tianqi Xu, Xinyue Hao, Hongyaoxing Gu, Xuyang Liu, Baolin Zhang, Yating Zhu, Shuang Ge, Jun Dai, Lei Chen, Yue Li, Mingchen Wan
- 链接：[arXiv](https://arxiv.org/abs/2611.02846) · [PDF](https://arxiv.org/pdf/2611.02846) · [HF](https://huggingface.co/papers/2611.02846)

Speculative decoding (SD) accelerates large language model inference by reducing the sequential cost of token-by-token generation. Advanced SD methods reduce proposal cost with parallel drafters that predict entire blocks in one forward pass, but overall speedup still depends on acceptance length. On-policy distillation (OPD) can push well-trained drafters beyond acceptance-length plateaus, yet conventional…

## 89. TLAPS-Bench: Formally Proving Correctness of Real-World System Specifications with TLA+ Proof System

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reasoning, benchmark, spec
- 作者：Qian Cheng, Ruize Tang, Saad Mohammad Rafid Pial, Zhizhen Cathy Cai, Yiming Su, Jackson Clark, Munim Thahmid, Mahdiya Rahman Sukanya, Chris Newcombe, Igor Konnov, Stephan Merz, Xudong Sun, Murat Demirbas, Yu Huang, Markus Alexander Kuppe, Tianyin Xu
- 链接：[arXiv](https://arxiv.org/abs/2611.02849) · [PDF](https://arxiv.org/pdf/2611.02849) · [HF](https://huggingface.co/papers/2611.02849)

TLAPS-Bench is a benchmark and execution harness for constructing machine-checked proofs for real-world system specifications in TLA+ with agentic AI. Proving correctness of complex system specifications requires discovering inductive invariants, reasoning about intricate state transitions, and decomposing proofs into tractable obligations. TLAPS-Bench provides a proof harness that supports iterative proof…

## 90. Scaling Action-Free Video Latent Prediction for Transferable Representations in End-to-End Autonomous Driving

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, spec, planning
- 作者：Xingtai Gui, Xubin Zhou, Yucheng Zhou, Dongqian Guo, Jiahao Gong, Feiyang Tan, Jianbing Shen
- 链接：[arXiv](https://arxiv.org/abs/2611.02853) · [PDF](https://arxiv.org/pdf/2611.02853) · [HF](https://huggingface.co/papers/2611.02853)

End-to-end autonomous driving policies require effective visual representations that capture both spatial scene structure and temporal dynamics. Video latent prediction has emerged as an effective paradigm for learning spatiotemporal visual representations, yet it remains unclear whether scaling this objective with action-free driving videos can yield representations that benefit end-to-end planning. We study…

## 91. What makes a theorem interesting? Operationalizing interestingness for open-ended exploration

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, memory, language model, large language
- 作者：Silvère Gangloff
- 链接：[arXiv](https://arxiv.org/abs/2611.02905) · [PDF](https://arxiv.org/pdf/2611.02905) · [HF](https://huggingface.co/papers/2611.02905)

An agent that explores, whether it generates conjectures or research ideas, must decide which of them are worth keeping. This judgment of interestingness is usually delegated to a hand-picked proxy or to a language model, neither of which is known to correspond to what humans actually value. I study it for mathematical theorems, by observing which results mathematicians single out in formal libraries and in papers.…

## 92. BLPO: Beyond-Local Policy Optimization for Long-Horizon LLM Agents

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, memory, reinforcement learning, language model, large language
- 作者：Xuanren Chen, Chongyang Tao, Wenpeng Hu, Yong Wang, Bo Deng, Xinlei Zheng, Shuai Ma
- 链接：[arXiv](https://arxiv.org/abs/2611.03005) · [PDF](https://arxiv.org/pdf/2611.03005) · [HF](https://huggingface.co/papers/2611.03005)

Long-horizon tasks require large language model (LLM) agents to coordinate interdependent actions, a capability central to automating complex workflows. Stepwise group-based reinforcement learning provides finer credit than trajectory-level supervision, but reliable comparisons must account for differences in interaction history. Enforcing this consistency within the limited rollouts of each task can leave…

## 93. VizDAGuide: Misleading Chart Question Answering in Compact Vision Language Models via DAG-Structured Supervision

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, evaluation, benchmark, language model
- 作者：Haiyang Zhang, Sicheng Song, Zixin Chen, Jie Gu, Huiya Ou, Chenhui Li, Changbo Wang
- 链接：[arXiv](https://arxiv.org/abs/2611.03023) · [PDF](https://arxiv.org/pdf/2611.03023) · [HF](https://huggingface.co/papers/2611.03023)

Misleading charts can lead vision-language models to conclusions that conflict with underlying data. Existing work focuses on inference-time strategies, while training-time supervision remains less explored. We present VizDAGuide, a DAG-structured supervision method for misleading-chart question answering. The method represents intermediate reasoning states and their dependencies as a directed acyclic graph, assigns…

## 94. Towards a Trustworthy and Governable Internet of Agentics: An Architectural Perspective on Protocols, Systems, and Services

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, language model, large language, spec
- 作者：Haoyi Xiong, Yi Liu, Jiang Bian, Peng Diao, Bin Zhu, Tingting Hu, Yi Wang, Sumi Helal
- 链接：[arXiv](https://arxiv.org/abs/2611.03066) · [PDF](https://arxiv.org/pdf/2611.03066) · [HF](https://huggingface.co/papers/2611.03066)

Large language model applications are increasingly being organized as tool-using and multi-agent workflows rather than as isolated chat interfaces. This perspective paper examines the architectural problem that follows from that shift: agents may reason, invoke tools, and delegate work, but dependable deployment still requires interoperability across frameworks, runtimes, data boundaries, and organizational control…

## 95. An Experimental Study of Hybrid Retrieval, NLI and Open-source LLMs for Scientific Claim Verification

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, language model, large language, spec, retrieval
- 作者：Lakshmi Narayanan P, Narenkarthik K, Naren Kumar C
- 链接：[arXiv](https://arxiv.org/abs/2611.03093) · [PDF](https://arxiv.org/pdf/2611.03093) · [HF](https://huggingface.co/papers/2611.03093)

Claim verification is the task of deciding whether a source text supports a claim, contradicts it, or lacks sufficient evidence. Natural Language Inference (NLI) models can judge whether a single sentence supports or contradicts a claim, but they struggle when the evidence is spread across several sentences. Conversely, Large Language Models (LLMs) can reason across sentences, but may draw conclusions the text does…

## 96. A Fine-Grained Hierarchy and Benchmark for State Tracking in Language Models

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：long context, evaluation, benchmark, language model
- 作者：Jackson Petty, William Merrill, Ashish Sabharwal
- 链接：[arXiv](https://arxiv.org/abs/2611.03094) · [PDF](https://arxiv.org/pdf/2611.03094) · [HF](https://huggingface.co/papers/2611.03094)

Theoretical limitations of transformers on state tracking---the ability to track information about entities or variables over long contexts---have motivated new recurrent language modeling (LM) architectures such as Gated DeltaNet (GDN). These architectures have, in particular, been benchmarked against the $S_5$ word problem, a theoretically hard state-tracking task that captures abilities such as code evaluation…

## 97. DR Pixel: Page-Native Deep Research with Vision-Language Models

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reasoning, benchmark, language model, retrieval
- 作者：Tiansheng Hu, Yichuan Wang, James V. Talwar, Nicholas Tomlin, Chen Zhao, Sewon Min
- 链接：[arXiv](https://arxiv.org/abs/2611.03097) · [PDF](https://arxiv.org/pdf/2611.03097) · [HF](https://huggingface.co/papers/2611.03097)

Complex documents such as scientific papers contain rich information in tables, figures, and equations; however, existing deep research (DR) agents typically reduce papers to OCR-extracted text. We instead ask whether vision-language models (VLMs) can enable page-native deep research: directly retrieving and reasoning over rendered document page images. We introduce DR Pixel, the first open-source end-to-end…

## 98. Diagonal Equivalence in State Space Models: Characterization, Retrieval Rank, and Selective Extensions

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, language model, spec, retrieval
- 作者：Dennis Rochau
- 链接：[arXiv](https://arxiv.org/abs/2611.03101) · [PDF](https://arxiv.org/pdf/2611.03101) · [HF](https://huggingface.co/papers/2611.03101)

We classify real and complex state-space models (SSMs) with linear transitions, distinguishing fixed-basis diagonal equivalence from input-output equivalence and tracking coefficient-conditioning windows under coordinate changes. We characterize diagonal equivalence through commuting transition families whose members are diagonalizable over the chosen field. With time-shared token-local matrix maps, we identify this…

## 99. From Local Skills to Long-Horizon Web Tasks: Progressive Skill Exploration for LLM Web Agents

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, language model, large language, spec
- 作者：Xueyang Feng, Xiaohe Bo, Xu Chen, Quanyu Dai, Feng Wen
- 链接：[arXiv](https://arxiv.org/abs/2611.03116) · [PDF](https://arxiv.org/pdf/2611.03116) · [HF](https://huggingface.co/papers/2611.03116)

Large language models (LLMs) are driving autonomous agents toward real-world environments, with the Web emerging as one of the most representative interaction scenarios. However, training Web agents with naive exploration remains challenging: successful trajectories are rare, and the sparse terminal rewards make it difficult for agents to obtain useful feedback from failed trajectories. Inspired by skill acquisition…

## 100. ComplianceAtlas: A Taxonomy-Driven Agentic AI Framework for Automated AI Act Gap Analysis and Remediation

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, evaluation, spec, planning, retrieval
- 作者：Ilias Driouich, Hongliu Cao, Eoin Thomas, Yannick Devaux, Agnes Brodelle
- 链接：[arXiv](https://arxiv.org/abs/2611.03121) · [PDF](https://arxiv.org/pdf/2611.03121) · [HF](https://huggingface.co/papers/2611.03121)

Assessing regulatory compliance for high-risk AI systems requires systematic identification of technical gaps such as missing controls, in- adequate processes, or shallow evaluation of practices. Compliance officers typically admin- ister structured questionnaires collecting evi- dence of current practices, where organizations respond with descriptions of their existing pro- cesses, technical capabilities, and…

## 101. SurgPace: Complexity-Aware Progressive Distillation for Surgical Multimodal Large Language Models

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, benchmark, language model, large language, coding
- 作者：Zhicheng He, Xiaohan Xing, Hongqiu Wang, Kun Yuan, Guankun Wang, Yanheng Li, Haoxuan Che, Nassir Navab, Hongliang Ren, Long Bai
- 链接：[arXiv](https://arxiv.org/abs/2611.03125) · [PDF](https://arxiv.org/pdf/2611.03125) · [HF](https://huggingface.co/papers/2611.03125)

Multimodal large language models (MLLMs) have shown strong potential in robotic surgery for question answering, scene understanding, and grounded assistance, but their high computational cost limits real clinical deployment. Knowledge distillation provides a practical way to build compact surgical MLLMs, yet direct distillation is not well suited to surgical data because surgical samples vary greatly in difficulty,…

## 102. Meet Students Where They Are: Student-Prefix Teacher Adaptation for On-Policy Distillation

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, reinforcement learning, benchmark, spec
- 作者：Xue Zhang, Songming Zhang, Yunlong Liang, Fandong Meng, Yufeng Chen, Jinan Xu
- 链接：[arXiv](https://arxiv.org/abs/2611.03133) · [PDF](https://arxiv.org/pdf/2611.03133) · [HF](https://huggingface.co/papers/2611.03133)

On-policy distillation (OPD) mitigates the student's exposure bias by optimizing on student-generated trajectories. However, student-generated prefixes may contain reasoning errors or follow patterns unfamiliar to the teacher, undermining the reliability of its token-level supervision. This degradation becomes more pronounced as prefixes grow longer. To address this teacher-side distribution mismatch, we propose…

## 103. DepthGraft: Structural Regularization through Hierarchical Cross-Layer KV Reconstruction

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, language model, large language, retrieval
- 作者：Xiaohan Qin, Xiangdong Zhang, Yu Wang, Huaijin Wu, Zhuo Xia, Yebin Yang, Junchi Yan
- 链接：[arXiv](https://arxiv.org/abs/2611.03142) · [PDF](https://arxiv.org/pdf/2611.03142) · [HF](https://huggingface.co/papers/2611.03142)

Scaling depth is a key route to stronger large language models, but Pre-LN architectures often suffer from depth-wise information dilution, limiting the effective use of deep layers. While cross-layer connectivity has proven effective at mitigating this problem, existing designs usually introduce additional computation or memory access. We revisit cross-layer KV sharing as an efficient form of such connectivity.…

## 104. AuditFL: A Contract-Backed Clearing Layer for Open Federated Learning

- 分数：8.0  ·  HF 赞：0  ·  来源：huggingface
- 兴趣命中：-
- 作者：Alexandros Balla, Spyros Lalis
- 链接：[arXiv](https://arxiv.org/abs/2610.41278) · [PDF](https://arxiv.org/pdf/2610.41278) · [HF](https://huggingface.co/papers/2610.41278)

Federated learning (FL) keeps raw data local, but most deployments still rely on a trusted coordinator for client admission, checkpoint distribution, update collection, aggregation, and rewards. This paper presents AuditFL, a contract-backed clearing layer for auditable FL in open settings. AuditFL keeps training and aggregation off chain, stores model artifacts in an assumed reliable off-chain artifact store, and…

## 105. When Prediction Shapes the Future: A BlueSky Agenda for Reflexive Time Series Analysis

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, memory, evaluation
- 作者：Tao Xie, Yiqun Zhang, Yiu-ming Cheung
- 链接：[arXiv](https://arxiv.org/abs/2611.02511) · [PDF](https://arxiv.org/pdf/2611.02511) · [HF](https://huggingface.co/papers/2611.02511)

Time-series models are increasingly deployed in operational systems (e.g., inventory management and clinical care) where predictions trigger interventions that alter future observations, producing records we term AI-shaped trajectories. This sequence-prediction coupling deepens as such systems evolve into agents that autonomously predict, act, and remember across long horizons. Such AI-shaped trajectories support…

## 106. MedHEB: Benchmarking Medical Embeddings Across Heterogeneous Clinical Evidence

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, retrieval
- 作者：Yingshu Li, Shaoyang Zhou, Zhanyu Wang, Yunyi Liu, Xinyu Liang, Xi Zhang, Lingqiao Liu, Lei Wang, Luping Zhou
- 链接：[arXiv](https://arxiv.org/abs/2611.02519) · [PDF](https://arxiv.org/pdf/2611.02519) · [HF](https://huggingface.co/papers/2611.02519)

Clinical evidence is inherently relational: medical images are interpreted with prior studies, cross-modal examinations, reports, and localized findings, and retrieving relevant evidence is therefore central to clinical interpretation. Recent foundation models increasingly encode these heterogeneous sources into shared embedding spaces, yet existing embedding evaluation often focuses on isolated matches, leaving…

## 107. FindLink: Learning to Assess Scientific Connections from Source-Grounded Premises

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, evaluation, benchmark
- 作者：Jingxuan Wei, Song Tan, Xiaohan Liu, Chao Sang, Changwei Wang, Linzhuang Sun, Bihui Yu, Fuqiang Wang, Junnan Zhu
- 链接：[arXiv](https://arxiv.org/abs/2611.02545) · [PDF](https://arxiv.org/pdf/2611.02545) · [HF](https://huggingface.co/papers/2611.02545)

Scientific discovery from the literature requires assessing connections among findings obtained under different study conditions. Source attribution makes individual findings traceable, but does not determine what they jointly support. We introduce GI-TraceBench, a benchmark of 10,282 questions in gastrointestinal oncology that unifies provenance question answering, knowledge discovery, and hypothesis evaluation…

## 108. Re$^3$Rank: Listwise Reranking with Reasoning-Conditioned Retrieval Heads

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, benchmark, retrieval
- 作者：Ruiyi Yan, Zhuoyuan Mao, Yugo Murawaki, Yiwen Guo
- 链接：[arXiv](https://arxiv.org/abs/2611.02550) · [PDF](https://arxiv.org/pdf/2611.02550) · [HF](https://huggingface.co/papers/2611.02550)

Attention-based rerankers score each candidate by the attention mass that retrieval heads route to it from the question, but the question, serving as a fixed query, carries limited information for locating relevant evidence. We propose Re$^3$Rank, a listwise reranker built on reasoning-conditioned retrieval heads (RRHeads). A generator first writes a reasoning trace over the question and the candidates, and a scorer…

## 109. CR-Bench-v2: Evaluating the Real-World Utility of AI Code Review Agents

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, evaluation, benchmark
- 作者：Kristen Pereira, Neelabh Sinha, Rajat Ghosh, Debojyoti Dutta
- 链接：[arXiv](https://arxiv.org/abs/2611.02566) · [PDF](https://arxiv.org/pdf/2611.02566) · [HF](https://huggingface.co/papers/2611.02566)

The rapid growth of automated code generation has created a pressing need for automated code review. Yet code review resists full automation: it depends on context beyond the \textit{diff}, on the author's intent, and on judgments about design and maintainability on which even expert reviewers disagree. Existing code review benchmarks lack standardization and rely largely on noisy human review comments scored with…

## 110. SeMo3D: Unifying 3D Generation, Editing, and Completion via Selective Modeling

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, benchmark, spec
- 作者：Xiaokun Sun, Jian Yang, Zhenyu Zhang
- 链接：[arXiv](https://arxiv.org/abs/2611.02568) · [PDF](https://arxiv.org/pdf/2611.02568) · [HF](https://huggingface.co/papers/2611.02568)

3D generation, editing, and completion are typically treated as regenerating the complete 3D asset under task-specific constraints, even when only a local region needs modification. This leads to task isolation, inconsistency in content that should remain unchanged, and dependence on task-specific paired data. We address these issues with a key observation: the three tasks all synthesize a designated region while…

## 111. Beyond $L_\infty$-Norm Sets: Synthesizing Interpretable Non-Uniform Uncertainty Sets for Evaluation-Time State-Adversarial Robustness

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reinforcement learning, evaluation
- 作者：Xulin Chen, Ruipeng Liu, Garrett E. Katz
- 链接：[arXiv](https://arxiv.org/abs/2611.02576) · [PDF](https://arxiv.org/pdf/2611.02576) · [HF](https://huggingface.co/papers/2611.02576)

Deep reinforcement learning (DRL) agents are vulnerable to perturbations of their observed state inputs. Prior works often constrain state adversaries with $L_p$-norm uncertainty sets and evaluate policy performance under the resulting perturbations. However, in continuous control tasks like robotics control, different state dimensions have distinct physical meanings and influence policy behavior to different…

## 112. BasisKV: Value Latents for Communication and Key Routing

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：language model, large language, spec
- 作者：Lixun Zhang, Zishan Shao, Kangning Cui, Yu Liang, Fan Yang, Yiran Chen
- 链接：[arXiv](https://arxiv.org/abs/2611.02583) · [PDF](https://arxiv.org/pdf/2611.02583) · [HF](https://huggingface.co/papers/2611.02583)

Long-context large language model (LLM) inference is increasingly constrained by the cost of maintaining an ever-growing KV-cache. Low-rank K/V projections provide a promising way to compress the KV-cache with minimal quality loss, but prior work has largely optimized KV-cache compression in isolation, leaving distributed inference, especially with tensor parallelism where attention computation is partitioned across…

## 113. Parallelism-Aligned Pruning and Round-Aware Context Reuse for On-Device Multimodal Agents

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, memory, coding
- 作者：Peipei Jiao, Mingkang Liu, Weiming Meng, Lichen Pang, Tianyuan Liu, Junyan Li
- 链接：[arXiv](https://arxiv.org/abs/2611.02601) · [PDF](https://arxiv.org/pdf/2611.02601) · [HF](https://huggingface.co/papers/2611.02601)

On-device multimodal agents are limited by two deployment mismatches: pretrained attention structures may not divide evenly across the compute cores of an edge accelerator, causing irregular partitions; and standard prefix caching keeps historical visual tokens in the persistent KV cache, whose capacity grows with the number of rounds. We present PARC, which combines parallelism-aligned structured pruning with…

## 114. Train the Sampler You Run: Few-Step Masked Diffusion Language Models via Mixture-Likelihood Fine-Tuning

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, language model, coding
- 作者：Amin Najafgholizadeh
- 链接：[arXiv](https://arxiv.org/abs/2611.02666) · [PDF](https://arxiv.org/pdf/2611.02666) · [HF](https://huggingface.co/papers/2611.02666)

When a masked diffusion language model is sampled in a few parallel steps in a random order, the model actually run is a mixture over reveal plans, while cross-entropy training fits token conditionals rather than this mixture. We introduce mixture-likelihood fine-tuning (Mix-FT), which fine-tunes a pretrained model on an importance-weighted bound of its own sampler's likelihood, with no teacher and no change to the…

## 115. MicroMouse: Masking Harmful Supervision in Long CoT via Relative Potential

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, benchmark, spec
- 作者：Xiaowei Zhu, Hengzhu Tang, Zhenyu Zhang, Shuohuan Wang, Yubing Ren, Yanan Cao
- 链接：[arXiv](https://arxiv.org/abs/2611.02710) · [PDF](https://arxiv.org/pdf/2611.02710) · [HF](https://huggingface.co/papers/2611.02710)

Even successful long CoTs may contain harmful supervision, motivating the need for methods that can automatically identify and mask such signals during SFT. Inspired by the MicroMouse maze-solving process, we view a long CoT as a search trajectory from the input problem toward the target answer. This perspective motivates maintaining a goal-relative measure, analogous to a MicroMouse's spatial coordinates, to…

## 116. Human-Supervised Artificial Intelligence Researchers in Electric Power Systems: Knowledge, Physics, Simulation, and Governance for Large Language Models

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, language model, large language
- 作者：Xiangrui Meng, Jingcheng Liu, Ke Wang, Miaopeng Yu, Zhengping Lin
- 链接：[arXiv](https://arxiv.org/abs/2611.02711) · [PDF](https://arxiv.org/pdf/2611.02711) · [HF](https://huggingface.co/papers/2611.02711)

Conclusions in power-system research require a clear evidential basis. Researchers need to understand the data sources, modelling assumptions, and solution procedures to assess the conditions under which a conclusion holds. Large language models (LLMs) can help researchers extract information from documents and translate research requests into code and tool calls, but their outputs still require physical validation.…

## 117. Risk-Constrained Evaluation of Financial Document Recognition: A Formal Framework for Evidence, Critical Errors, and Selective Automation

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, spec
- 作者：Subodh Lonkar
- 链接：[arXiv](https://arxiv.org/abs/2611.02775) · [PDF](https://arxiv.org/pdf/2611.02775) · [HF](https://huggingface.co/papers/2611.02775)

Financial document recognition is commonly evaluated using character and word error rates, which do not adequately represent the consequences of errors in financial workflows. This paper formalizes financial document recognition as a risk-constrained evidence-recovery problem. It defines typed, evidence-linked financial facts and a multi-layer quality model spanning text, layout, tables, fields, semantic relations,…

## 118. Rethinking Neural Decompilation: Candidate Selection as the Hidden Bottleneck

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：language model, large language, coding
- 作者：Felix Mächtle, Gautham Sriram, Manjil Neupane, Nils Loose, Thomas Eisenbarth
- 链接：[arXiv](https://arxiv.org/abs/2611.02788) · [PDF](https://arxiv.org/pdf/2611.02788) · [HF](https://huggingface.co/papers/2611.02788)

Reverse engineering obfuscated binaries is a core task in malware analysis and software security auditing. While neural decompilers based on Large Language Models (LLMs) have improved the readability and functional fidelity of recovered code over heuristic tools such as Ghidra and IDA Pro, a substantial gap remains between best-sample performance and practical single-output accuracy, particularly under code…

## 119. Efficient Detailed Scheduling of Multiproduct Pipelines using Action-Decoupled Deep Reinforcement Learning

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reinforcement learning, benchmark, spec
- 作者：Kai Shao, Ling Jian, Liming Liu, Serguey V. Bogomolov, Xinmin Wang
- 链接：[arXiv](https://arxiv.org/abs/2611.02823) · [PDF](https://arxiv.org/pdf/2611.02823) · [HF](https://huggingface.co/papers/2611.02823)

Multiproduct pipelines transport refined products to delivery stations in sequential batches, and their detailed scheduling must meet market demand while respecting nonlinear hydraulic constraints. Retaining the full hydraulic nonlinearity yields a mixed-integer nonlinear program that is computationally intractable, while the linearization commonly adopted for solver-based optimization degrades hydraulic accuracy…

## 120. Reimagining computational quantum research with AI scientists

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, language model, large language
- 作者：Yuxuan Du, Hanqing Zhao, Xinbiao Wang, Yiming Lu, Kaining Zhang, Dacheng Tao
- 链接：[arXiv](https://arxiv.org/abs/2611.02833) · [PDF](https://arxiv.org/pdf/2611.02833) · [HF](https://huggingface.co/papers/2611.02833)

AI scientists are expanding automated research across scientific domains, yet their ability to turn the scientific record into a foundation for autonomous discovery remains elusive. Here we uncover a fundamental barrier to this transition and demonstrate a route to overcome it in computational quantum science, where advances shape both what we can learn from complex quantum systems and what quantum computing can…
