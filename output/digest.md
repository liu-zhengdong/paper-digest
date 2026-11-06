# 每日 AI 论文

生成时间：2026-11-06 06:46 UTC  ·  共 120 篇（已按 arXiv ID 去重）

来源：Hugging Face Daily Papers + arXiv（cs.AI / cs.LG / cs.CL / cs.CV）。
排序：HF 上榜、点赞、多源命中、兴趣词。兴趣词可在 `config.json` 改。

## 1. FrontierPhysics: Evaluating Agents for End-to-End Physics Research

- 分数：34.0  ·  HF 赞：48  ·  来源：huggingface
- 兴趣命中：agent, reasoning, benchmark
- 作者：Bingran You, Wenjun Ke, Ria Rosenauer, Bo Liu, Wenbo Chen, Min Chen, Shuqi Xu, Yue Ma, Jiechao Feng, Bo Chen, Xiangkai Sun, Jiarui Liu, Jinen Guo, Zeyu Zhou, Xu Huang, Zhuohan Li, Haoyu Li, Heguang Lin, Lijie Ding, Yadong Zeng, Kangqi Zhang, Xinge Liu, Hanwen Liu, Zhenghong Li, Alexander von Recum, Yuchen Zhu, Felix Schwarzfischer, Yizhou Zhao, Jicheng Wang, Binxu Li, Qian Yu, Chan Li, Cheng Dai, Di Wang, Haoyu Zhang, Jiankai Sun, Kaituo Feng, Mian Qin, Ruihong Yin, Yiqun Luo, Weiwei Wu, Shihong Pan, Tsung Yeh Hsieh, Xiao Huang, Yan Zhang, Sihan Li, Zirui Ren, Zengji Tu, Kyoung Whan Choe, Ke Sun, Vincenzo Galia, Vaisakhi Mishra, Jiashu He, Hongyang Wang, Zhiheng Yang, Shubham Gaur, Yifan Gu, Shuyi Wang, Zihao Zuo, Steven Dillmann, Yiyou Sun, Xinyang Han, Hanchung Lee, Molei Tao, Yue Zhao, Shilong Liu, Yuchen Wu, Xuandong Zhao, Xiangyi Li, Florian Brand, Gerbrand Ceder, Hartmut Haeffner
- 链接：[arXiv](https://arxiv.org/abs/2611.06910) · [PDF](https://arxiv.org/pdf/2611.06910) · [HF](https://huggingface.co/papers/2611.06910)

AI agents are playing an increasingly important role in physics research. However, existing physics benchmarks only evaluate fixed questions, isolated sub-tasks, or paper reproduction with given solutions, and rarely check research quality alongside correctness. We introduce FrontierPhysics, an end-to-end benchmark with 56 tasks made by 42 physicists based on their own research, covering nine domains across…

## 2. VFlash: Fast, Accurate Visual Planning via Flash Primitive Decoding

- 分数：30.5  ·  HF 赞：25  ·  来源：huggingface + arxiv
- 兴趣命中：language model, coding, planning
- 作者：Yu-Cheng Chou, Shihao Wang, Jin Huang, Chi-Pin Huang, Chiao-An Yang, Xianzhe Fan, Jing Wang, Zhiqi Li, Yuanguo Kuang, Ruijie Zheng, Johan Bjorck, Sifei Liu, Hang Su, Abhishek Badki, Lei Zhang, Alan Yuille, Linxi &#34;Jim&#39;&#39; Fan, Jan Kautz, Zhiding Yu
- 链接：[arXiv](https://arxiv.org/abs/2611.08449) · [PDF](https://arxiv.org/pdf/2611.08449) · [HF](https://huggingface.co/papers/2611.08449)

Models for physical AI tasks, such as robotics and autonomous driving, need not reason solely in language. They can use visual plans--points, bounding boxes, and trajectories--to represent spatial goals and anticipate motion. However, autoregressive vision-language models generate these plans one coordinate token at a time, making richer predictions increasingly costly. We introduce VFlash, a method for fast,…

## 3. Turns Matter: Advancing Streaming Video RL via Turn-Level Credit

- 分数：30.0  ·  HF 赞：85  ·  来源：huggingface
- 兴趣命中：spec
- 作者：Shuai Dong, Kanghui Tian, Linghan Chen, Wenqi Shao, Hongrui Wu, Haowen Hou, Yongfu Zhu, Xuehui Wang, Ziyue Wang, Wenpu Liu, Weichu Xie, Yuqi Xu, Congcong Wang, Kaiwen Tuo, Caoyuan Ma, Taiqiang Wu, Ji Zhao, Wenzheng Chang, Dianyi Wang, Siyuan Wang, Zhongyu Wei, Yu Qiao, Jiaqi Wang
- 链接：[arXiv](https://arxiv.org/abs/2611.06728) · [PDF](https://arxiv.org/pdf/2611.06728) · [HF](https://huggingface.co/papers/2611.06728)

Streaming video understanding requires models to repeatedly decide whether to respond or continue observing. Recently, Group Relative Policy Optimization (GRPO) has been applied to this setting, with existing approaches emphasizing reward design while retaining a single trajectory-level advantage across turns. Such shared credit can reinforce redundant replies after earlier successes and discourage useful follow-ups…

## 4. From Pixels to Actions - Towards Native Vision-Language-Action Policies

- 分数：30.0  ·  HF 赞：57  ·  来源：huggingface
- 兴趣命中：reasoning
- 作者：Weichen Fan, Haiwen Diao, Penghao Wu, Siyuan Hu, Ziqi Huang, Tianqi Liu, Mingze Sun, Ziyi Wang, Zhongang Cai, Hanming Deng, Quan Wang, Lei Yang, Lewei Lu, Fangzhou Hong, Zhaoxi Chen, Dahua Lin, Ziwei Liu
- 链接：[arXiv](https://arxiv.org/abs/2611.06918) · [PDF](https://arxiv.org/pdf/2611.06918) · [HF](https://huggingface.co/papers/2611.06918)

Vision-language-action models are typically built on a simple premise: perception is first compressed by visual encoders, and action reasoning begins only afterwards. Yet manipulation often hinges on precisely the visual signals most vulnerable to this abstraction, e.g., local geometry, boundaries, depth, and subtle state changes. This raises a fundamental question: should action policies inherit a fixed visual…

## 5. What Does Multi-Turn Reinforcement Learning Really Improve in LLM Agents?

- 分数：29.5  ·  HF 赞：35  ·  来源：huggingface
- 兴趣命中：agent, reinforcement learning
- 作者：Kejian Zhu, Zhuoran Jin, Shangqing Tu, Tianyi Men, Yupu Hao, Jiachun Li, Kang Liu, Jun Zhao
- 链接：[arXiv](https://arxiv.org/abs/2611.06483) · [PDF](https://arxiv.org/pdf/2611.06483) · [HF](https://huggingface.co/papers/2611.06483)

While multi-turn agentic reinforcement learning (RL) excels on long-horizon tasks, its performance gains remain highly sensitive to interaction constraints. Evaluating across sampling breadth K and interaction depth T via Pass@(K,T), we show that trajectory-level RL advantages depend on sufficient turn budgets, diminishing significantly when budgets tighten. Besides, agentic RL does not uniformly elevate single-step…

## 6. Harness-S: Learning from Sibling Harnesses for Generalizable Agent Training

- 分数：28.0  ·  HF 赞：28  ·  来源：huggingface
- 兴趣命中：agent, reinforcement learning, spec
- 作者：Kangning Zhang, Wenxiang Jiao, Bowen Fang, Shuai Shao, Jiachen Zhu, Rong Shan, Shijian Wang, Hao Wang, Yuan Lu, Weiwen Liu, Weinan Zhang
- 链接：[arXiv](https://arxiv.org/abs/2611.04277) · [PDF](https://arxiv.org/pdf/2611.04277) · [HF](https://huggingface.co/papers/2611.04277)

Harness evolution from a common base exhibits Locality, Complementarity, and Nonstationarity: variants repair different failures, and their utility changes as the policy learns. Rather than seeking a universally superior harness, we introduce Harness-S to selectively rescue failures of a base execution system through sibling harnesses and transfer the resulting capabilities into a single policy that remains…

## 7. EmoReward: Self-Evolving Reward Calibration for Emotional Video Generation RL

- 分数：27.5  ·  HF 赞：23  ·  来源：huggingface
- 兴趣命中：agent, memory, evaluation, spec
- 作者：Mingzhe Zheng, Yue Wu, Jing Tan, Chang Zou, Dengyang Jiang, Zeyue Tian, Xuanhua He, Ryan Xu, Yunyang Ge, Sihui Ji, Yunlong Lin, Kaihang Pan, Hongru Yan, Sixiang Chen, Dianyi Wang, Julian Zhang, Weijie Kong, Changlin Li, Lanqing Guo, Zhao Zhong, Qifeng Chen, Harry Yang
- 链接：[arXiv](https://arxiv.org/abs/2611.06518) · [PDF](https://arxiv.org/pdf/2611.06518) · [HF](https://huggingface.co/papers/2611.06518)

Group Relative Policy Optimization (GRPO) has advanced generative model post-training in verifiable domains such as code and mathematics, but evaluating video quality, especially emotional expression, often depends on subjective aesthetics and has no uniquely correct target. Existing approaches typically rely on fixed rewards for visual quality, motion quality, and text alignment that poorly capture emotional intent…

## 8. MUON-RT Reusing the Teacher's Trajectory for Momentum-Free Muon for LLM Self-Distillation

- 分数：25.5  ·  HF 赞：19  ·  来源：huggingface
- 兴趣命中：memory, language model, large language, spec
- 作者：Aryan Das, Vinay Kumar Verma, Aakansha Mishra
- 链接：[arXiv](https://arxiv.org/abs/2610.41104) · [PDF](https://arxiv.org/pdf/2610.41104) · [HF](https://huggingface.co/papers/2610.41104)

Self-distillation methods for large language models with an exponential moving average (EMA) teacher already retain a history of student updates. Muon nevertheless stores a separate momentum buffer, increasing persistent training memory. We propose Muon with Reused Teacher (Muon-RT), which reuses the teacher-student displacement to eliminate momentum buffers for hidden weight matrices. We show that this displacement…

## 9. On the Generalization Limitation of On-Policy Distillation for Post-RL Consolidation

- 分数：25.5  ·  HF 赞：19  ·  来源：huggingface
- 兴趣命中：agent, reasoning, reinforcement learning, coding, spec
- 作者：Yichen Wang, Yufa Zhou, Siqi Zhu, Haozheng Luo, Jingzhi Bao, Zhichao Liu, Zijun Wei
- 链接：[arXiv](https://arxiv.org/abs/2611.05609) · [PDF](https://arxiv.org/pdf/2611.05609) · [HF](https://huggingface.co/papers/2611.05609)

Multi-teacher on-policy distillation (MOPD) extends on-policy distillation (OPD) to consolidate capabilities from multiple teachers. Although prior work reports near-perfect in-distribution (IND) distillation performance, we find that this can mask incomplete capability consolidation beyond the supervised distribution. A preliminary study on synthetic reasoning shows that OPD does not fully transfer teachers'…

## 10. Towards Foundation Decision Models: Drex

- 分数：25.5  ·  HF 赞：11  ·  来源：huggingface + arxiv
- 兴趣命中：agent, reasoning, reinforcement learning, language model, large language, coding
- 作者：Nischay Dhankhar, Alisher Amantay, Zhanibek Datbayev, Darkhan Akhmetov, Yash Shah, Nurmukhamed Ubaidullayev, Raman Saparkhan, Dos Baha, Abulhair Saparov
- 链接：[arXiv](https://arxiv.org/abs/2611.07854) · [PDF](https://arxiv.org/pdf/2611.07854) · [HF](https://huggingface.co/papers/2611.07854)

Autoregressive approaches with large language models, such as long chain-of-thought reasoning, have become the default for new AI applications because they reach higher accuracy on a wide range of tasks. In production, however, they give inconsistent answers, require parsing of outputs, and add cost and latency. Decision models address this: given a question and a set of options supplied by the user, they return a…

## 11. Halley: A Predictive Control Plane for Optical AI Data Center Networks

- 分数：25.0  ·  HF 赞：34  ·  来源：huggingface
- 兴趣命中：-
- 作者：Manav Mishra, Krishna M. Sivalingam
- 链接：[arXiv](https://arxiv.org/abs/2611.04408) · [PDF](https://arxiv.org/pdf/2611.04408) · [HF](https://huggingface.co/papers/2611.04408)

A frontier AI model is trained in an AI data center, on tens of thousands of accelerators joined by a dedicated network, and every training step ends with all of them exchanging data at once. Between racks, that network is optical, and each of its four layers, from lasers to switches, runs a fixed or after-the-fact policy. Lasers sharing an enclosure, cooling, and power can fail together. At a fixed spare ratio,…

## 12. VideoMemBench: How Well Do MLLMs Remember in Video Conversations?

- 分数：25.0  ·  HF 赞：18  ·  来源：huggingface
- 兴趣命中：memory, evaluation, benchmark, language model, large language
- 作者：Zhengdong Hu, Chao Wang, Kaituo Feng, Huanjin Yao, Mingfei Lu, Hehe Fan, Yi Yang
- 链接：[arXiv](https://arxiv.org/abs/2610.40131) · [PDF](https://arxiv.org/pdf/2610.40131) · [HF](https://huggingface.co/papers/2610.40131)

Multimodal large language models (MLLMs) can now process hour-long videos, making extended multi-turn dialogue over a single video a natural mode of use. Sustaining such a dialogue requires more than answering each question in isolation: the model must retrieve and reuse information established earlier in the conversation, both what it has seen and what it has said, an ability we term in-context video memory.…

## 13. GameVerse: A Minute-Scale Gameplay Dataset for Long-Horizon Interactive World Modeling

- 分数：24.5  ·  HF 赞：33  ·  来源：huggingface
- 兴趣命中：-
- 作者：Kang He, Wenshuo Peng, Chuanhao Li, Zihui Gao, Xiaojie Xu, Zhengyuan Lin, Yuzhe Ding, Donghong Ji, Kaipeng Zhang, Yongtao Ge
- 链接：[arXiv](https://arxiv.org/abs/2610.37257) · [PDF](https://arxiv.org/pdf/2610.37257) · [HF](https://huggingface.co/papers/2610.37257)

Recent advances in interactive world models have made it possible to generate controllable, dynamic environments from action inputs. Yet current models struggle to maintain coherence beyond roughly one minute of rollout, a limitation rooted not in model capacity but in the scarcity of long-horizon training data. Existing gameplay video datasets typically consist of clips under ten seconds, with captions that…

## 14. PyRUA-DataFarm: LLM Agent as a Cost-Efficient Teleoperator for Real-Ready Robot Data

- 分数：24.0  ·  HF 赞：24  ·  来源：huggingface
- 兴趣命中：agent, coding
- 作者：Kewei Zhang, Juncheng Ma, Guodong Lv, Duomin Wang, Feixiang Ruan, Ruiyang Si, Chuanrui Zhang, Yuxuan Chen, Hao Chen, Yichen Liu, Yintianrun Zhang, Yufan Deng, Enze Xie, Daquan Zhou
- 链接：[arXiv](https://arxiv.org/abs/2611.05320) · [PDF](https://arxiv.org/pdf/2611.05320) · [HF](https://huggingface.co/papers/2611.05320)

Teleoperation remains the default way to collect robot demonstrations, but every episode costs robot and operator time, and every new task starts from scratch. We ask whether a coding agent can take over the teleoperator's job. In our DataFarm, the agent receives a data request and one calibration episode of the robot in the target scene and rebuilds the task in simulation: it writes the scene, an expert controller,…

## 15. TAC-CoT: Tool-Empowered Implicit Chain-of-Thought via Interleaving Explicit Tokens

- 分数：23.0  ·  HF 赞：14  ·  来源：huggingface
- 兴趣命中：agent, tool-use, reasoning, benchmark
- 作者：Juseon Do, Sangmin Bae, Jeesu Jung, Hwanjun Song
- 链接：[arXiv](https://arxiv.org/abs/2611.01926) · [PDF](https://arxiv.org/pdf/2611.01926) · [HF](https://huggingface.co/papers/2611.01926)

LLM-based agentic systems are increasingly combined with CoT reasoning to solve tasks that require accurate reasoning, external knowledge, and multi-step deliberation. Yet, explicit CoT incurs substantial generation overhead, while implicit CoT, which replaces textual rationales with compact continuous tokens, does not naturally support the explicit communication interface required for agentic tool-use. We propose…

## 16. SpecOPD: Branch-Parallel On-Policy Distillation for Speculative Decoding

- 分数：22.5  ·  HF 赞：13  ·  来源：huggingface
- 兴趣命中：agent, language model, large language, coding, spec
- 作者：Tianyu Liu, Jun Zhang, Wenjie Huang, Yuhao Shen, Tianqi Xu, Xinyue Hao, Hongyaoxing Gu, Xuyang Liu, Baolin Zhang, Yating Zhu, Shuang Ge, Jun Dai, Lei Chen, Yue Li, Mingchen Wan
- 链接：[arXiv](https://arxiv.org/abs/2611.02846) · [PDF](https://arxiv.org/pdf/2611.02846) · [HF](https://huggingface.co/papers/2611.02846)

Speculative decoding (SD) accelerates large language model inference by reducing the sequential cost of token-by-token generation. Advanced SD methods reduce proposal cost with parallel drafters that predict entire blocks in one forward pass, but overall speedup still depends on acceptance length. On-policy distillation (OPD) can push well-trained drafters beyond acceptance-length plateaus, yet conventional…

## 17. Random Is Almost Enough? Stable and Low-Cost Benchmark Compression via BestRand

- 分数：22.0  ·  HF 赞：16  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark
- 作者：George Ling, Shanshan Zhong, Lijin Yang, Hao Yang, Nanxiang Li, Zhongzhan Huang
- 链接：[arXiv](https://arxiv.org/abs/2611.00883) · [PDF](https://arxiv.org/pdf/2611.00883) · [HF](https://huggingface.co/papers/2611.00883)

Benchmark compression reduces the often prohibitive time and cost of model evaluation by evaluating models on a small benchmark subset that closely matches full-benchmark results. To quantify estimation error, we derive an accurate analytical approximation to the error distribution when estimating full-benchmark scores from a subset, showing that most subsets yield small errors, while a few produce much larger…

## 18. PyRUA-REAL: Robot Exploration and Adaptive Learning through RSI in the Real World

- 分数：21.0  ·  HF 赞：10  ·  来源：huggingface
- 兴趣命中：agent, memory, reasoning, evaluation, benchmark, coding, spec
- 作者：Qiang Wang, Jianxin Bi, Shulong Jiang, Ruiyang Si, Wenbo Huang, Kaiqi Chen, Jiaxin Li, Liyun Li, Xuanyi Li, Daquan Zhou
- 链接：[arXiv](https://arxiv.org/abs/2611.06768) · [PDF](https://arxiv.org/pdf/2611.06768) · [HF](https://huggingface.co/papers/2611.06768)

Coding agents powered by models such as GPT-6-Astra connect spatial reasoning with executable robot behavior, raising the question of how such agents can produce lasting improvements in robot capabilities from physical interaction. In this work, we study embodied recursive self-improvement (RSI) through real-world exploration, code refinement, and deployment using PyRUA-REAL, a framework in which coding agents…

## 19. NPCBench: A Clinical Apprenticeship Benchmark for Multimodal Care-Pathway Reasoning in Nasopharyngeal Carcinoma

- 分数：20.5  ·  HF 赞：1  ·  来源：huggingface + arxiv
- 兴趣命中：reasoning, evaluation, benchmark, spec, planning
- 作者：Pengkai Wang, Wei-Wei Zhang, Yan Li, Min Tang, Zhitian Hou, Zeyu Liu, Guanghao Zhu, Yuanyi Wang, Yanggan Gu, Wenjun Wang, Minheng Ni, Congkai Xie, Zhijie Sang, Jianmin Wu, Ying Sun, Hongxia Yang
- 链接：[arXiv](https://arxiv.org/abs/2611.08369) · [PDF](https://arxiv.org/pdf/2611.08369) · [HF](https://huggingface.co/papers/2611.08369)

Current medical benchmarks typically break down clinical competence into isolated factual questions, single-image tasks, or static case vignettes. These tests score individual answers, but reveal less about whether a model can integrate subspecialty knowledge with multimodal evidence and track a patient's condition throughout a course of care. To close this gap, we introduce NPCBench, a clinical apprenticeship…

## 20. LoopVQ: Sub 1-bit KV Cache Quantization for Looped Transformers

- 分数：20.0  ·  HF 赞：8  ·  来源：huggingface
- 兴趣命中：memory, reasoning, language model, retrieval
- 作者：Minsoo Cheong, Sungjoo Yoo
- 链接：[arXiv](https://arxiv.org/abs/2611.05304) · [PDF](https://arxiv.org/pdf/2611.05304) · [HF](https://huggingface.co/papers/2611.05304)

Looped transformers are a parameter-efficient alternative to standard transformers for language modeling. By reapplying the same layers across multiple loop steps, recent looped language models match the performance of non-looped models several times their size. While this architecture effectively reduces parameter memory, each loop step still stores its own keys and values, so the key-value (KV) cache grows…

## 21. StreamDuo: A Live Commentator and a Research Agent for Unseen Games

- 分数：19.5  ·  HF 赞：19  ·  来源：huggingface
- 兴趣命中：agent
- 作者：Zixian Gao, Penghao Luo, Xiangcheng Cao, Lixin Xiu, Ziqi Cai, Zhen Li, Erwin Wu, Kaipeng Zhang
- 链接：[arXiv](https://arxiv.org/abs/2611.01120) · [PDF](https://arxiv.org/pdf/2611.01120) · [HF](https://huggingface.co/papers/2611.01120)

Streaming video LLMs can now commentate live gameplay, but they are trained and tested on the same games. We study cross-game streaming commentary, in which a model trained on one game commentates games it has never seen, and find that current commentators transfer their timing but not their knowledge of the game world. We propose StreamDuo, which pairs a trainable commentator with a frozen research agent that reads…

## 22. How I Aligned Your Model: Scaling Up Multilingual Safety Training with Templates

- 分数：19.5  ·  HF 赞：7  ·  来源：huggingface
- 兴趣命中：evaluation, language model, large language, spec
- 作者：Max Neuwinger, Hanna Yukhymenko, Imanol Schlag
- 链接：[arXiv](https://arxiv.org/abs/2610.40516) · [PDF](https://arxiv.org/pdf/2610.40516) · [HF](https://huggingface.co/papers/2610.40516)

Safety alignment for Large Language Models is heavily focused on English with limited multilingual representation, particularly damaging low-resource language performance. Related open training datasets are often limited in size or do not follow region-localized harmful topics to broaden the scope of alignment beyond cultures. We propose a scalable template-based augmentation pipeline to produce massive multilingual…

## 23. D3D: Decoupled Diffusion Drafting for Asynchronous Speculative Decoding

- 分数：18.5  ·  HF 赞：9  ·  来源：huggingface
- 兴趣命中：benchmark, coding, spec
- 作者：Baoyou Chen, Ruiqiao Mei, Guancong Lin, Tao Song, Weihao Yuan, Qun Liu, Siyu Zhu
- 链接：[arXiv](https://arxiv.org/abs/2611.06425) · [PDF](https://arxiv.org/pdf/2611.06425) · [HF](https://huggingface.co/papers/2611.06425)

Target-conditioned diffusion drafters predict candidate tokens in parallel, yet each new block must wait for updated target-model hidden states. This forces drafting and verification to run sequentially, limiting speedup even though each block is generated in one pass. We introduce D3D, a standalone diffusion drafter that removes this inter-round dependency. D3D combines blockwise denoising with auxiliary…

## 24. Solv3R: 3D Looped Transformer as a Multi-view Solver

- 分数：18.0  ·  HF 赞：16  ·  来源：huggingface
- 兴趣命中：spec
- 作者：Jeong-gi Kwak, Andrea Tagliasacchi, Sho Kagami, Yuki Ono, Kwang Moo Yi
- 链接：[arXiv](https://arxiv.org/abs/2611.02857) · [PDF](https://arxiv.org/pdf/2611.02857) · [HF](https://huggingface.co/papers/2611.02857)

Classical structure-from-motion reconstruction proceeds iteratively, refining camera poses and scene geometry from a current estimate. This allows maps to easily expand without recomputing already computed views, or geometry estimates to improve as more observations are provided. Most geometric foundation models, however, predict entire geometry in a single forward pass or update a recurrent state as frames arrive…

## 25. The SIMPLE Law for Energy Cost of LLM Inference

- 分数：17.5  ·  HF 赞：7  ·  来源：huggingface
- 兴趣命中：agent, memory, reasoning
- 作者：Hiari Pizzini Cavagna, Andrea Proia, Daniele Cesarini, Zeynep Kiziltan, Andrea Bartolini
- 链接：[arXiv](https://arxiv.org/abs/2611.03330) · [PDF](https://arxiv.org/pdf/2611.03330) · [HF](https://huggingface.co/papers/2611.03330)

Generative AI is billed per token, yet tokens are not equally expensive. Each token enters the KV-cache and raises the cost of those that follow, so energy grows non-linearly along a sequence whose tokens look identical. No analytical model states what a token costs, and the most accurate SOTA model is a fit, not a law: it absorbs architecture into fitted coefficients, requiring per-LLM fitting. We derive…

## 26. EDGAR: Efficient Diffusion-Driven Gaussian Avatar Refinement via Synthetic Failure

- 分数：17.5  ·  HF 赞：7  ·  来源：huggingface + arxiv
- 兴趣命中：evaluation
- 作者：Kwan Yun, Minhyeok Bang, Colette Suhjung Koo, Junyong Noh
- 链接：[arXiv](https://arxiv.org/abs/2611.07909) · [PDF](https://arxiv.org/pdf/2611.07909) · [HF](https://huggingface.co/papers/2611.07909)

Recent advances in Gaussian splatting have enabled efficient and photorealistic head avatar reconstruction, yet monocular video-based or image-based methods still suffer from under-constrained geometry and texture, leading to artifacts such as blurring, stretching, and temporal instability. We present EDGAR (Efficient Diffusion-Driven Gaussian Avatar Refinement), a conditional diffusion framework designed to enhance…

## 27. EvoMemState: Evolving Memory State for Personal Agents

- 分数：17.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：agent, memory, reasoning, reinforcement learning, benchmark, language model, large language, spec, retrieval
- 作者：Zhishang Xiang, Yunbo Tang, Zhongqiao Liu, Junkai Chen, Zerui Chen, Qingguo Hu, Yuxuan Zhang, William Grant, Qinggang Zhang, Jinsong Su
- 链接：[arXiv](https://arxiv.org/abs/2611.03743) · [PDF](https://arxiv.org/pdf/2611.03743) · [HF](https://huggingface.co/papers/2611.03743)

Long-term memory enables large language model (LLM) agents to provide continuous personalized assistance by retaining user information across interactions. Existing systems support this process through fact extraction, organization, updating, and retrieval, but largely maintain memories as independent facts. This fact-centric paradigm may overlook how new facts update, constrain, or conflict with earlier ones, while…

## 28. Ask, Don't Equip: Question-Driven Coding Agents for Deep Kernel Optimization

- 分数：17.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：agent, evaluation, coding, spec, retrieval
- 作者：Gabriele Oliaro, Jaeseong Lee, Zhaoyuan Su, Sreeram Vennam, Zhihao Jia, Samyam Rajbhandari
- 链接：[arXiv](https://arxiv.org/abs/2611.03517) · [PDF](https://arxiv.org/pdf/2611.03517) · [HF](https://huggingface.co/papers/2611.03517)

LLM agents for GPU kernel optimization sit at two ends of a structure-freedom tradeoff. Scripted agents fix what the model does at each step, via a learned policy, an optimization menu, or fixed roles, and are sample-efficient where the recipe applies and stall where it does not. Open-ended agents let a self-directed model mutate a population of kernels and pay for the freedom in trials: thousands of evaluations,…

## 29. Why Pay for Long Reasoning When Rewrite Do Trick? Causal Effects of Reasoning History Compaction on Future Generation and Agent Cost

- 分数：17.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：agent, reasoning, language model, coding, spec
- 作者：Anton Hristov
- 链接：[arXiv](https://arxiv.org/abs/2611.03852) · [PDF](https://arxiv.org/pdf/2611.03852) · [HF](https://huggingface.co/papers/2611.03852)

Reasoning substantially improves language models' ability to solve difficult problems, but long reasoning traces make these gains expensive. Efficient reasoning should express useful analysis in fewer tokens by reducing repetition and text that adds little value to solving the problem. Progress in proprietary models motivates this goal, yet their hidden scratchpads limit direct study of how it is achieved. We…

## 30. Hybrid Computer Use: A Unified Programmatic, Semantic, and Visual Interface for General Agents

- 分数：16.5  ·  HF 赞：13  ·  来源：huggingface
- 兴趣命中：agent
- 作者：Haoqing Wang, Xiaoyi Zhang, Sicheng Fan, Zhexin Zhang, Xinjie Zhang, Jiahao Li, Bin Li, Yan Lu
- 链接：[arXiv](https://arxiv.org/abs/2610.41432) · [PDF](https://arxiv.org/pdf/2610.41432) · [HF](https://huggingface.co/papers/2610.41432)

Computer-use agents increasingly tackle tasks ranging from everyday desktop activities to long-horizon professional workflows. Yet interfaces centered on screenshots and mouse-and-keyboard actions can impose a human-interaction prior, requiring repeated screen interpretation while leaving the computer's semantic and programmatic capabilities underexposed. We argue for exposing these capabilities and letting models…

## 31. Human-to-Robot Transfer via Bridging Representation and Action Space in VLAs

- 分数：16.5  ·  HF 赞：13  ·  来源：huggingface
- 兴趣命中：spec
- 作者：Junhyeong Park, Wook Jung, Taeyoung Kim, Huiwon Jang, Jinwoo Shin
- 链接：[arXiv](https://arxiv.org/abs/2611.04391) · [PDF](https://arxiv.org/pdf/2611.04391) · [HF](https://huggingface.co/papers/2611.04391)

Pretrained Vision-Language-Action (VLA) policies provide a strong starting point for deployment, but adapting them to a target robot and environment still requires costly embodiment-specific demonstrations. Human demonstrations are far easier to collect, yet directly leveraging them is challenging due to the substantial human-robot embodiment gap, particularly when the underlying VLA has been pretrained primarily on…

## 32. VisSearch-Bench: Evaluating Long Horizon Visual Search in Multimodal Agents

- 分数：16.5  ·  HF 赞：9  ·  来源：huggingface
- 兴趣命中：agent, retrieval
- 作者：ZhengXian Wu, Qianhao Nie, Zhuohong Chen, Junjie Gao, Yuyao Zhang, Yunyao Yu, Hangrui Xu, Cheng Cheng, Guiyu Ma, Jin Zhang, Xingzhong Xu, Kai Yang, Haoqian Wang
- 链接：[arXiv](https://arxiv.org/abs/2611.04894) · [PDF](https://arxiv.org/pdf/2611.04894) · [HF](https://huggingface.co/papers/2611.04894)

Multimodal agents use web and image tools to answer questions beyond their internal knowledge. Some search tasks use images mainly to identify an initial entity, then rely on text retrieval. These tasks offer limited insight into how agents connect information across images, objects, and search steps. We therefore focus on visual context management. This involves organizing and using visual information and linking…

## 33. Decode Before You Hear: Speculative Listening for Chunk-Interleaved Full-Duplex Speech Language Models

- 分数：16.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：benchmark, language model, coding, spec
- 作者：Yutong Bian, Yanglin Zhang, Yuxiang Wang, Luoyuan Zhang, Rongshen He, Zihao Wang, Junwen Qiu, Jiaqi Li, Zhizheng Wu
- 链接：[arXiv](https://arxiv.org/abs/2611.06982) · [PDF](https://arxiv.org/pdf/2611.06982) · [HF](https://huggingface.co/papers/2611.06982)

Chunk-interleaved full-duplex speech language models listen and speak in fixed time chunks, and each chunk must be processed before the next one arrives. Their workload is asymmetric across chunks: listen chunks leave compute idle while awaiting audio, and speak and tool-call chunks require serial generation, which delays responses and tool calls. Using the idle compute for the next chunk requires decoding it before…

## 34. VA-TDM: A Unified View for Improving Few-Step Diffusion Models by Velocity Adversarial Distillation

- 分数：16.0  ·  HF 赞：12  ·  来源：huggingface
- 兴趣命中：spec
- 作者：Yihong Luo, Tianyu Pang, Tianyang Hu
- 链接：[arXiv](https://arxiv.org/abs/2611.06796) · [PDF](https://arxiv.org/pdf/2611.06796) · [HF](https://huggingface.co/papers/2611.06796)

Few-step distillation offers efficient generation with diffusion and flow models, but preserving quality with only a few sampling steps remains challenging. Distribution-matching methods via score distillation provide a strong foundation, yet they rely on accurately tracking the student's changing distribution. At intermediate generation steps in few-step sampling, student-score estimation can be difficult, and…

## 35. VidDub: Replacement-Aware Distillation for Two-Step Video Dubbing

- 分数：16.0  ·  HF 赞：8  ·  来源：huggingface
- 兴趣命中：evaluation, benchmark
- 作者：Yexin Liu, Yunlong Lin, Zehan Wang, Guangxin He, Xinli Xu, Jiajun Zha, Yaofu Liu, Yueze Wang, Bowen Ping, Yuanming Li, Amie Wang, Bernard Ghanem, Bing Li, Harry Yang
- 链接：[arXiv](https://arxiv.org/abs/2611.03404) · [PDF](https://arxiv.org/pdf/2611.03404) · [HF](https://huggingface.co/papers/2611.03404)

Video dubbing aims to synthesize lip movements that match target speech while preserving the speaker identity, head pose, and background of a source video. Existing editors are predominantly trained via self-reconstruction under original paired audio, even though the source mouth becomes a conflicting target when driving speech is replaced. We introduce replacement-aware cross-audio supervision: paired-audio samples…

## 36. NitroFusion2: Bringing Adversarial Loss to the Text Stream of Multimodal Diffusion Transformers

- 分数：15.5  ·  HF 赞：7  ·  来源：huggingface
- 兴趣命中：benchmark, spec
- 作者：Dar-Yen Chen, Yi-Zhe Song
- 链接：[arXiv](https://arxiv.org/abs/2611.05648) · [PDF](https://arxiv.org/pdf/2611.05648) · [HF](https://huggingface.co/papers/2611.05648)

Adversarial diffusion distillation has conventionally relied on image features for discrimination. We revisit this choice for multimodal diffusion transformers (MMDiTs), whose text stream becomes image-dependent through joint attention. We introduce Text-Stream Adversarial Distillation (TSAD), which exploits intermediate text-token states as a new adversarial representation. Because the text stream has already read…

## 37. WeLM-Image: A Unified Image Generation Model towards Visual Intelligence

- 分数：15.5  ·  HF 赞：7  ·  来源：huggingface
- 兴趣命中：evaluation, spec
- 作者：Canmiao Fu, Chen Li, Guohui Zhang, Hao Lu, Hongyang Wei, Huadong Wu, Huaisong Zhang, Hubery Yin, Liyuan Cui, Qixin Yan, Tong Shao, Xiaoqiang Zhou, Xinhang Leng, Ying Zhang, Zhenhai Liu, Zhipeng Huang
- 链接：[arXiv](https://arxiv.org/abs/2611.07392) · [PDF](https://arxiv.org/pdf/2611.07392) · [HF](https://huggingface.co/papers/2611.07392)

We present WeLM-Image, a unified image foundation model that integrates multimodal understanding into text-to-image generation, instruction-guided editing, and multi-reference synthesis. Designed for single-GPU deployment in WeChat's large-scale consumer applications, the model processes text, reference images, and target latents as one interleaved sequence. A Mixture-of-Transformers (MoT) backbone combines shared…

## 38. SleuthVLM: Do We Really Need Audio-in-Video for Omni Video Understanding?

- 分数：15.0  ·  HF 赞：6  ·  来源：huggingface
- 兴趣命中：agent, benchmark
- 作者：Peiran Wu, Fangfei Gou, Zhaoxi Mu, Changhao Zhang, Jian Liu, Weiqiang Wang, Yuntao Wang, Yuanchun Shi, Junxiao Shen
- 链接：[arXiv](https://arxiv.org/abs/2611.06083) · [PDF](https://arxiv.org/pdf/2611.06083) · [HF](https://huggingface.co/papers/2611.06083)

Omni models answer questions about videos by jointly processing sampled frames and audio in one turn, with progress driven largely by scaling model size and omni training data. We ask whether a model needs to hear the audio directly at all, and present SleuthVLM, an agent harness built on a VLM that never hears the audio directly: speech will be transcribed into text, and the VLM will sleuth the video on its own…

## 39. VeriSpoof: Beyond Real or Fake with One Audio LLM

- 分数：14.5  ·  HF 赞：5  ·  来源：huggingface
- 兴趣命中：evaluation, language model
- 作者：Yang Xiao, Ting Dang
- 链接：[arXiv](https://arxiv.org/abs/2611.04634) · [PDF](https://arxiv.org/pdf/2611.04634) · [HF](https://huggingface.co/papers/2611.04634)

A speech deepfake detector estimates whether a recording is synthetic, but a forensic analyst also asks which system produced it, whether recordings share a source, and what evidence supports each conclusion. We present VeriSpoof, an audio language model that unifies five tasks with shared weights: deepfake detection, generator attribution (generator, acoustic model and vocoder), recording-condition analysis,…

## 40. Monitor Accuracy Isn't the Answer: A Decision-Value Framework for Evaluating AI Agent Restart Monitors

- 分数：13.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：agent, spec
- 作者：Siddharth Jain, Venkat N. Vedam
- 链接：[arXiv](https://arxiv.org/abs/2610.36544) · [PDF](https://arxiv.org/pdf/2610.36544) · [HF](https://huggingface.co/papers/2610.36544)

Classification accuracy and true-positive and false-positive rates alone do not determine whether restarting an AI agent improves success. Using an exact alarm-to-action identity for an independent clean restart with zero monitoring overhead, we show analytically that a monitor with fixed 90% accuracy can swing from a five-percentage-point loss to a 35-point gain in success rate, depending solely on the replacement…

## 41. Open-HumanScale: An Open Recipe for Scaling Human and Robot Experience for Embodied Foundation Models

- 分数：13.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：evaluation, benchmark
- 作者：Juncheng Ma, Jiaxin Li, Jiankai Tu, Bo Liang, Guodong Lv, Yufan Deng, Junzhe Tang, Liangzhu Yang, Chen Bian, Zicong Cao, Baohao Zhu, Jianxin Bi, Tengfei Yan, Yinyuan Zhang, Kewei Zhang, Xinglong Chen, Kaiqi Chen, Duomin Wang, Xiaotian Tang, Liang Tan, Li Li, Yuan Xu, Haosen Yang, Yuqi Wang, Jingfei Xia, Songyan Huang, Zhiyang Dou, Zhen Dong, Enze Xie, Tat-Seng Chua, Daquan Zhou
- 链接：[arXiv](https://arxiv.org/abs/2611.06817) · [PDF](https://arxiv.org/pdf/2611.06817) · [HF](https://huggingface.co/papers/2611.06817)

Egocentric human video offers a scalable source of manipulation priors for robot learning, yet translating raw data scale into generalizable robot policies demands rigorous data curation and training recipes. We introduce Open-HumanScale, the first fully open recipe for scaling egocentric pretraining to 50,000 hours, anchored by Open-HumanScale-50K---a curated egocentric video corpus densely annotated with hand…

## 42. UniRestorer++: Scalable Universal Image Restoration with Multi-Granularity Degradation Modeling

- 分数：13.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：benchmark, spec
- 作者：Jingbo Lin, Zhilu Zhang, Fan Li, Renjing Pei, Wenbo Li, Hang Xu, Hongzhi Zhang, Wangmeng Zuo
- 链接：[arXiv](https://arxiv.org/abs/2611.06042) · [PDF](https://arxiv.org/pdf/2611.06042) · [HF](https://huggingface.co/papers/2611.06042)

Universal image restoration aims to handle diverse degradations within a single model, but a reliable scaling strategy remains underexplored. Increasing backbone depth and width can lead to performance saturation, while degradation-aware specialization depends on accurate degradation estimation and is vulnerable to errors on out-of-distribution and real-world inputs. We propose UniRestorer++, a scalable framework…

## 43. AnchorComplete: Recovering Complete Scene Meshes from Partial Point Clouds

- 分数：12.5  ·  HF 赞：9  ·  来源：huggingface
- 兴趣命中：-
- 作者：Weirong Chen, Ismail El-Yamany, Ganlin Zhang, Chuanxia Zheng, Andrea Vedaldi, Daniel Cremers
- 链接：[arXiv](https://arxiv.org/abs/2611.03228) · [PDF](https://arxiv.org/pdf/2611.03228) · [HF](https://huggingface.co/papers/2611.03228)

Most image-based 3D reconstructors primarily recover visible surfaces, producing partial point clouds with large holes and leaving unobserved geometry unresolved. To address this limitation, we introduce AnchorComplete, a framework that reconstructs complete scene meshes from partial point clouds while preserving observed geometry and supporting scenes of varying scales. Building on TRELLIS.2, our method combines…

## 44. Identically Trained Language Models Break on Different Jailbreaks

- 分数：12.0  ·  HF 赞：0  ·  来源：huggingface
- 兴趣命中：benchmark, language model
- 作者：Chi-Wei Chang, Mu-Tien Kuo, Kuan-Wei Lee, Meng-Hsun Tsai
- 链接：[arXiv](https://arxiv.org/abs/2610.34074) · [PDF](https://arxiv.org/pdf/2610.34074) · [HF](https://huggingface.co/papers/2610.34074)

Jailbreak benchmarks test one checkpoint and treat which jailbreaks break it as a property of its pretraining data and safety training. We ask whether another pretraining run of the same data, given the same safety training, would break on the same jailbreaks. For each of 25 pretraining data recipes, we take 1B base models from 3 pretraining seeds and give each the same safety post-training with 2 post-training…

## 45. HERIT: Enabling Global Access to Hanja-to-English Historical Translation by Mitigating Temporal Bias

- 分数：12.0  ·  HF 赞：0  ·  来源：huggingface
- 兴趣命中：evaluation, retrieval
- 作者：Dayeon Jeong, Kyeongpil Kang
- 链接：[arXiv](https://arxiv.org/abs/2611.04949) · [PDF](https://arxiv.org/pdf/2611.04949) · [HF](https://huggingface.co/papers/2611.04949)

Historical archives are invaluable for multidisciplinary research but remain inaccessible globally due to severe language barriers. While manual translation is prohibitively expensive and time-consuming, simply applying existing machine translation models is inadequate due to unique linguistic nuances and the temporal bias inherent in scarce human-labeled corpora. To address these challenges, we propose HERIT, a…

## 46. DRAP: Dynamics-Risk Adaptive Plasticity for Continual Learning in Physical AI

- 分数：12.0  ·  HF 赞：0  ·  来源：huggingface
- 兴趣命中：agent, memory
- 作者：Oswaldo Ludwig
- 链接：[arXiv](https://arxiv.org/abs/2611.05029) · [PDF](https://arxiv.org/pdf/2611.05029) · [HF](https://huggingface.co/papers/2611.05029)

Continual learning in physical AI differs from conventional continual learning because small per-step policy errors can accumulate over a trajectory. Each deviation may move the agent outside the training distribution, increase subsequent prediction errors, and ultimately cause closed-loop task failure. This work introduces Dynamics-Risk Adaptive Plasticity (DRAP), a replay-free method that estimates the historical…

## 47. Multi-layer Indexer: Overlapping Selection and Attention in DeepSeek Sparse Attention

- 分数：11.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：long context
- 作者：Serdarcan Dilbaz, Arjun Krishna, Kiran Kamble, Daniel M. Bikel
- 链接：[arXiv](https://arxiv.org/abs/2611.03768) · [PDF](https://arxiv.org/pdf/2611.03768) · [HF](https://huggingface.co/papers/2611.03768)

Sparse attention cuts the cost of long-context inference by making the attention matrix sparse: each query attends only a subset of the sequence, chosen by a fixed pattern or, in recent production LLMs, learned per query. In DeepSeek Sparse Attention (DSA), the attention of DeepSeek-V3.2 and the GLM-5 family, every layer is preceded by a lightning indexer that scores the whole cache and keeps the k=2048…

## 48. Koopman Generative Operators for Efficient Probabilistic Time-Series Forecasting

- 分数：11.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：benchmark
- 作者：Raz Marshanski, Liran Nochumsohn, Mayank Jauhari, Boris N. Oreshkin, Omri Azencot
- 链接：[arXiv](https://arxiv.org/abs/2611.04760) · [PDF](https://arxiv.org/pdf/2611.04760) · [HF](https://huggingface.co/papers/2611.04760)

Probabilistic time-series forecasting requires models that simultaneously capture structured temporal dynamics, expressive uncertainty, and efficient inference, yet existing approaches fall short of this goal: latent dynamical models impose structure but rely on restrictive generation mechanisms, while modern generative methods such as diffusion and flow matching achieve flexibility at the cost of iterative and…

## 49. SLA: Scaling Spatial-Language-Action Model via Continual Pre-training

- 分数：10.0  ·  HF 赞：0  ·  来源：huggingface
- 兴趣命中：spec
- 作者：Fuhao Li, Wenxuan Song, Qizhou Huang, Ziyang Zhou, Jingbo Wang, Junwu E, Pengwei Wang, Yan Wang, Shunbo Zhou, Haoang Li
- 链接：[arXiv](https://arxiv.org/abs/2611.08373) · [PDF](https://arxiv.org/pdf/2611.08373) · [HF](https://huggingface.co/papers/2611.08373)

Reliable robotic manipulation requires both semantic understanding and precise control in three-dimensional space. However, vision-language-action (VLA) foundations largely inherit visual representations from 2D vision-language pre-training, while spatial supervision is often introduced only during task-specific adaptation. Developing spatial understanding as a transferable foundation-model capability therefore…

## 50. GaussianRenderFormer: Transformer-based Rendering of 3D Gaussian Splats

- 分数：9.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：-
- 作者：Shahaf Valencia Levy, Sagie Benaim
- 链接：[arXiv](https://arxiv.org/abs/2611.05593) · [PDF](https://arxiv.org/pdf/2611.05593) · [HF](https://huggingface.co/papers/2611.05593)

Can a neural network learn to render 3D Gaussian splats on its own, with no rasterizer in the renderer? We present GaussianRenderFormer, a transformer that takes a set of Gaussians and a camera and outputs the image directly. Each Gaussian becomes one token in a view-independent encoder, and a view-dependent decoder turns small patches of camera rays into pixels by attending to those tokens. Trained on 26,820…

## 51. LiveFoley: Dynamic Real-Time Video-to-Audio Generation for Immersive Interactive Worlds

- 分数：9.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：-
- 作者：Yusheng Dai, Vladimir Iashin, Kangdi Wang, Yuxuan Jiang, Ilpo Viertola, Weiqiang Wang, Qiuhong Ke, Min Zhao, Jianfei Cai
- 链接：[arXiv](https://arxiv.org/abs/2611.05988) · [PDF](https://arxiv.org/pdf/2611.05988) · [HF](https://huggingface.co/papers/2611.05988)

Streaming video-to-audio (V2A) generation is essential for immersive interactive applications. However, real-time constraints leave existing streaming V2A methods far behind offline models: (1) visual frontends shrink their receptive fields to cut look-ahead latency, severely degrading audio-visual alignment; (2) causal autoregressive diffusion backends denoise each audio patch in isolation, impairing audio quality.…

## 52. TaoMate-HD: Progressive-Resolution Autoregressive Audio-Video Generation

- 分数：9.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：-
- 作者：Qijun Gan, Chenwei Zhang, Xinyang Li, Meiguang Jin, Junfeng Ma, Shen Qiu
- 链接：[arXiv](https://arxiv.org/abs/2611.03394) · [PDF](https://arxiv.org/pdf/2611.03394) · [HF](https://huggingface.co/papers/2611.03394)

Streaming digital humans produce detailed video while continuing speech as new text arrives. High-resolution denoising is costly, and text updates can cause repeated or interrupted speech. We present TaoMate-HD, an autoregressive model for high-resolution audio-video streaming. For each short segment, or chunk, two denoising steps establish coarse video structure at low resolution. A final step refines the video to…

## 53. Future Representation Distillation for Imagination-free World Action Models

- 分数：9.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：-
- 作者：Jaehyeong Jo, Sangwon Jang, Sihyun Yu, Seonghyeon Ye, Yekyung Nah, Hojung Jung, Kimin Lee, Sung Ju Hwang
- 链接：[arXiv](https://arxiv.org/abs/2611.04527) · [PDF](https://arxiv.org/pdf/2611.04527) · [HF](https://huggingface.co/papers/2611.04527)

World Action Models (WAMs) use the predictive knowledge of pretrained video diffusion models for robot control through future video prediction. However, iterative video denoising is costly, and inaccurate visual predictions can compromise action prediction. Our key idea is to make this predictive knowledge available through visual representations computed from the current observation, enabling action prediction…

## 54. ReferClaw: Disambiguating User Intent for Egocentric Assistance

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, evaluation, benchmark, spec
- 作者：Hangyu Qin, Junbin Xiao, Angela Yao
- 链接：[arXiv](https://arxiv.org/abs/2611.07683) · [PDF](https://arxiv.org/pdf/2611.07683) · [HF](https://huggingface.co/papers/2611.07683)

Users of egocentric AI assistants often ask short, ambiguous questions whose intended referents cannot be uniquely resolved from video and dialogue history. For example, "Where did I leave it?" may refer to several previously handled objects. Existing VideoQA systems typically commit to a single interpretation, risking plausible but intention-misaligned answers. We introduce ReferClaw, an agentic framework that…

## 55. MCPHallu: Benchmarking Reasoning, Execution, and Memory Hallucinations in MCP Agents

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, memory, reasoning, benchmark, language model, large language, spec
- 作者：Yizhen Jiang, Haowei Guo, Tianyi Bai, Zengjie Hu, Lu Ma, Zhengyang Zhao, Haoze Sun, Peng Pei, Wentao Zhang
- 链接：[arXiv](https://arxiv.org/abs/2611.07689) · [PDF](https://arxiv.org/pdf/2611.07689) · [HF](https://huggingface.co/papers/2611.07689)

Large language model agents are increasingly deployed through the Model Context Protocol (MCP), which allows them to discover and invoke tools across multiple servers at runtime. Existing MCP benchmarks primarily measure task completion; where they diagnose failures, they do so after execution rather than building specific reasoning, execution, and memory failure risks into task construction. We introduce MCPHallu,…

## 56. CAMP: Context-Aware Mapping and Placement for LLMs on 3D-IMC Arrays

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, language model, large language, spec
- 作者：Orhun Görkem, Athanasios Vasilopoulos, Georgios Pagonis, Victoria Clerico, Hadjer Benmeziane, Irem Boybat, Hsinyu Tsai, Abu Sebastian, William Andrew Simon
- 链接：[arXiv](https://arxiv.org/abs/2611.07707) · [PDF](https://arxiv.org/pdf/2611.07707) · [HF](https://huggingface.co/papers/2611.07707)

Large Language Models (LLMs) incur severe memory-access overheads due to the cost of loading large weight matrices and key-value (KV) caches. Analog In-Memory Computing (AIMC) is an emerging solution that enables computation directly on static weights stored in memory, substantially reducing energy and latency. 3D-IMC further stacks memory arrays into vertical tiers, increasing capacity but revealing a new…

## 57. Evaluating Token Probabilities as Confidence Estimators in Human Behavior Simulations: A Case Study in Luxembourgish Next Like Prediction

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, language model, large language, spec
- 作者：Nils Schwager, Simon Münker, Alistair Plum, Achim Rettinger
- 链接：[arXiv](https://arxiv.org/abs/2611.07735) · [PDF](https://arxiv.org/pdf/2611.07735) · [HF](https://huggingface.co/papers/2611.07735)

As large language models (LLMs) are increasingly used to simulate human behavior, their operational validity is typically assessed through accuracy alone, implicitly treating human behavior as deterministic. We argue that on noisy digital trace data, a model's performance depends not only on predicting the correct outcome but on its calibration. We present a case study testing whether the token probabilities of…

## 58. Automated Video-to-QA Pipeline: End-to-End Question Generation and Verification Using Large Language Models

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：language model, large language, spec, retrieval
- 作者：Jaival Chauhan, Vikram Singh, Pruthwik Mishra
- 链接：[arXiv](https://arxiv.org/abs/2611.07755) · [PDF](https://arxiv.org/pdf/2611.07755) · [HF](https://huggingface.co/papers/2611.07755)

The exponential growth of educational and informational video content on platforms like YouTube presents a challenge for efficient knowledge retrieval and assessment. This paper proposes an end-to-end automated pipeline for extracting structured summaries and generating high-fidelity Question-Answer (QA) pairs from video streams. The framework integrates a cascade of state-of-the-art models: audio extraction is…

## 59. BiGrounder: Bidirectional Training Unlocks the Potential of GUI Grounding

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reinforcement learning, evaluation, benchmark
- 作者：Dengyao Shi, Tianyu Fu, Fei Hu, Anyang Su, Hanning Wang, Shuo Wang, Minghui Wu, Chenxu Zhao, Zhen Lei
- 链接：[arXiv](https://arxiv.org/abs/2611.07765) · [PDF](https://arxiv.org/pdf/2611.07765) · [HF](https://huggingface.co/papers/2611.07765)

Graphical User Interface (GUI) grounding aims to map natural language instructions to precise operational coordinates, serving as a critical task for autonomous agent interaction. Current approaches formalize GUI grounding as predicting action-coordinate pairs from instructions, with end-to-end training supervised solely by final coordinates. Training datasets typically provide only a small number of descriptions…

## 60. PBPO: Prefix-Block Policy Optimization for Diffusion Language Models

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, language model, large language
- 作者：Katherine Tieu, Dongqi Fu, Si Zhang, Hanqing Zeng, Tianxin Wei, Chenglin Wei, Yinglong Xia, Hong Li, Jingrui He
- 链接：[arXiv](https://arxiv.org/abs/2611.07783) · [PDF](https://arxiv.org/pdf/2611.07783) · [HF](https://huggingface.co/papers/2611.07783)

Diffusion Large Language Models (dLLMs) commonly decode responses by proceeding autoregressively across blocks while iteratively denoising multiple tokens within each block. This structure makes block-level policy optimization a natural adaptation of autoregressive policy optimization. However, the exact likelihood of a completed block is intractable because it marginalizes over the intermediate states and reveal…

## 61. Generate-then-Rank: Learning Symbolic Goal Interpretation for Embodied Agents

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, benchmark, language model, large language, planning
- 作者：Jisen Lei, Huizhi Liang
- 链接：[arXiv](https://arxiv.org/abs/2611.07825) · [PDF](https://arxiv.org/pdf/2611.07825) · [HF](https://huggingface.co/papers/2611.07825)

Goal interpretation is to translate a natural language instruction into a formal symbolic goal that a planner can execute. It is critical for embodied agents because any error here propagates to every downstream planning and action step. Doing it well requires both generating suitable candidates and reliably selecting among them. We present a two-stage generate-then-rank approach to Goal Interpretation in the…

## 62. Instantiating the Knowledge Plane

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reasoning, language model, large language
- 作者：Francisco Pereira, Justine Sherry, Pratiksha Thaker
- 链接：[arXiv](https://arxiv.org/abs/2611.07827) · [PDF](https://arxiv.org/pdf/2611.07827) · [HF](https://huggingface.co/papers/2611.07827)

In 2003, Clark et al. proposed the "Knowledge Plane", a layer of intelligent agents that share rich information about network state in order to collaboratively manage the Internet across administrative boundaries. The technology of the day lacked the two capabilities it demanded most: reasoning and unstructured communication. Thus, automated network management has remained largely confined to single domains, while…

## 63. Which Signals of Code Correctness Survive Distribution Shift? Hidden-State and Causal Predictors of Program and Verdict Correctness

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, benchmark, language model, large language
- 作者：Viola Campos, Thomas Klassert, Adrian Ulges
- 链接：[arXiv](https://arxiv.org/abs/2611.07876) · [PDF](https://arxiv.org/pdf/2611.07876) · [HF](https://huggingface.co/papers/2611.07876)

Large language models increasingly judge code, yet without external feedback such judgments are unreliable, and verifying them by executing tests or by extended reasoning is costly. Instead, execution-free correctness predictors use signals from the model's output probabilities, sampled solutions, or hidden states to identify judgments that warrant further verification. However, these predictors may degrade under…

## 64. WAM-Sim0.1: World Anchored Memory Meets Online RL for Consistent and Realistic Driving Simulation

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, benchmark, language model, coding
- 作者：Jiahao Cui, Jiaye Li, Wenhao Zhang, Yaoyi Li, Shan Luan, Quanhui Tang, Jianhua Han, Lin Cheng, Hang Xu, Siyu Zhu
- 链接：[arXiv](https://arxiv.org/abs/2611.07939) · [PDF](https://arxiv.org/pdf/2611.07939) · [HF](https://huggingface.co/papers/2611.07939)

Autoregressive driving world models systematically suffer from structural drift, identity drift, and quality decay over long rollout horizons due to transient conditioning signals that lack persistent state. We present WAM-Sim, a driving world model anchored by a persistent hierarchical memory and optimized via online flow-matching RL. WAM-Sim structures persistent context across three temporal and semantic scales:…

## 65. Circe: Training-Free LLM Self-Evaluation via Component Interaction Consistency

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, language model, large language
- 作者：Shuyi Miao, Zheng Li, Xu Xie, Linrui Xu, Fei Shen, Xiaoyu Du, Tat-Seng Chua
- 链接：[arXiv](https://arxiv.org/abs/2611.07948) · [PDF](https://arxiv.org/pdf/2611.07948) · [HF](https://huggingface.co/papers/2611.07948)

As large language models (LLMs) are increasingly deployed in real-world applications, evaluating the correctness of their responses is crucial for reliable use. However, such evaluation is challenging because reference answers are rarely available in practice. Existing reference-free methods mainly rely on output signals, which may assign high scores to incorrect responses and thus do not necessarily reflect…

## 66. TCSExam: Evaluating Frontier LLMs on the Full Range of TCS Research

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, evaluation, benchmark, language model, large language, spec
- 作者：Yifan Luo, Zhengying Liu, Yang Yuan, Zhilin Yang, Andrew Chi-Chih Yao
- 链接：[arXiv](https://arxiv.org/abs/2611.07962) · [PDF](https://arxiv.org/pdf/2611.07962) · [HF](https://huggingface.co/papers/2611.07962)

Can large language models (LLMs) advance theoretical computer science and resolve its long-standing open conjectures? To study progress toward this goal, we introduce TCSExam, a unified framework and benchmark covering the full range of TCS research. It evaluates theorem proving, solver engineering, and constructions alongside direct attempts to resolve open conjectures, capturing both concrete research…

## 67. QRAE: Query-Relevant Attention Entropy for Context Compression in DeepSearch Agents

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reasoning, evaluation, benchmark, spec
- 作者：Yingjie Tan, Haiquan Qiu, Quanming Yao, Manyi Zhong, Xianzhi Yu, Yaqing Wang
- 链接：[arXiv](https://arxiv.org/abs/2611.07976) · [PDF](https://arxiv.org/pdf/2611.07976) · [HF](https://huggingface.co/papers/2611.07976)

DeepSearch LLM agents repeatedly search and carry retrieved sources into subsequent reasoning steps. This expanding context increases token consumption and latency, although many results do not contribute to later reasoning. We propose Query-Relevant Attention Entropy (QRAE), an online context compression method that uses sparse evidence-assessment heads to decide which intact retrieved chunks should persist across…

## 68. How Far Can Lightweight LLMs Go in Intent-to-SLO Translation?

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, evaluation, language model, large language
- 作者：Sabbir Ahmed, Hazem Abbas, Salimur Choudhury
- 链接：[arXiv](https://arxiv.org/abs/2611.07982) · [PDF](https://arxiv.org/pdf/2611.07982) · [HF](https://huggingface.co/papers/2611.07982)

Intent-based networking (IBN) promises QoS provisioning in which the network derives the configuration from operator-stated goals. Its first step, translating a natural-language intent into enforceable service-level objectives (SLOs) grounded in a live snapshot of the network state, increasingly relies on large language models (LLMs). These large models add cost and energy to the management loop and typically…

## 69. Compression Through a Context Lens: Evaluating Adaptation, Quantization, and Distillation in Arabic Legal LLMs

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, evaluation, benchmark, language model, large language, spec
- 作者：Md. Rafiul Biswas, George Mikros, Wajdi Zaghouani
- 链接：[arXiv](https://arxiv.org/abs/2611.07988) · [PDF](https://arxiv.org/pdf/2611.07988) · [HF](https://huggingface.co/papers/2611.07988)

Model compression can facilitate the deployment of large language models in resource-constrained legal settings, but its effects on domain-specific performance may depend on the evaluation protocol. We investigate this issue using ArabLegalEval, a Saudi Arabic legal benchmark, under both with-context and no-context evaluation. The former provides supporting legal passages, while the latter assesses performance…

## 70. Automatic keyphrase extraction and annotation: modern theoretical approaches and practical solutions for text and speech

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, language model, large language, spec
- 作者：Daria Guseva, Olga Mitrofanova
- 链接：[arXiv](https://arxiv.org/abs/2611.08006) · [PDF](https://arxiv.org/pdf/2611.08006) · [HF](https://huggingface.co/papers/2611.08006)

The exponential growth of textual and audiovisual information has made the task of automatic keyphrase extraction (KE) increasingly significant. This article provides a comprehensive analysis of contemporary theoretical approaches and practical solutions for KE across both text and speech modalities. The primary contribution of this work is its systematic synthesis of these often-disparate research strands into a…

## 71. DictLLM: Post-training Compression of Large Language Model with Dictionary Kernels

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, reasoning, benchmark, language model, large language, spec
- 作者：Jinho Park, Se Young Chun, Mingoo Seok
- 链接：[arXiv](https://arxiv.org/abs/2611.08082) · [PDF](https://arxiv.org/pdf/2611.08082) · [HF](https://huggingface.co/papers/2611.08082)

Efficient deployment of large language models (LLMs) on mobile devices requires balancing performance with compute and memory constraints. Post-training compression is an effective approach to managing this trade-off, while requiring much less computation than in-training counterparts. We propose DictLLM, a dictionary-based compression scheme in which weight matrices within grouped layers are decomposed into a…

## 72. PersonaAgent: Retrieval-Augmented Transaction Anomaly Scoring with Refreshable Multi-Entity Persona Memory

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, memory, benchmark, retrieval
- 作者：Zhengyu Fang, Liang Wang, Yingtong Dou, Yuzhong Chen, Shubham Jain, Junpeng Wang, Xiran Fan, Menghai Pan, Jiarui Sun, Yan Zheng, Yiwei Cai
- 链接：[arXiv](https://arxiv.org/abs/2611.08094) · [PDF](https://arxiv.org/pdf/2611.08094) · [HF](https://huggingface.co/papers/2611.08094)

In large-scale payment networks, entities (card, merchant, etc.) and their interactions play a key role in transaction anomaly detection. However, transaction patterns between different entities usually change more frequently than the production model refresh schedule. Meanwhile, entity embedding tables suffer from high-cardinality and sparse interaction issues. To resolve the above challenges, we present…

## 73. ProQuant: Progressive Quantization-aware Training for Edge MLLMs

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, benchmark, language model, large language, spec
- 作者：Yufei Xue, Yushi Huang, Jiawei Shao, Pingcheng Dong, Yonghao Tan, Shiyao Li, Kwang-Ting Cheng, Jun Zhang
- 链接：[arXiv](https://arxiv.org/abs/2611.08216) · [PDF](https://arxiv.org/pdf/2611.08216) · [HF](https://huggingface.co/papers/2611.08216)

Multi-modal large language models (MLLMs) with impressive perception and understanding capabilities will enable a range of downstream applications. However, their substantial computational and memory requirements hinder the real-world implementation, particularly for resource-constrained edge devices. Quantization has emerged as an effective solution for deploying large models. While post-training quantization (PTQ)…

## 74. Agent-R$^2$: Scaling Agents for Realistic Productivity Work via Real-Source Data Synthesis

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, tool use, reasoning, reinforcement learning, evaluation, language model, large language, spec
- 作者：Teng Pan, Zixuan Wang, Yuchen Yan, Qifei Wu, Yao Chen, Yingqi Qu, Ruiqing Zhang, Yongliang Shen
- 链接：[arXiv](https://arxiv.org/abs/2611.08219) · [PDF](https://arxiv.org/pdf/2611.08219) · [HF](https://huggingface.co/papers/2611.08219)

Large language models have made rapid progress in agentic reasoning and tool use, raising expectations for agents that can take over realistic productivity work from humans. However, current agents still struggle to finish such tasks, where success requires following long-horizon professional workflows, understanding heterogeneous file contexts, and producing usable deliverables under fine-grained requirements. A…

## 75. From Twisted Facts to Rogue Agents: Can LLMs Reliably Detect Multi-Dimensional Hallucinations?

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, benchmark, language model, large language
- 作者：Hanyu Qiu, Ze Liu, Zhe Zhao, Kuang Xiong, Blaze Chen, Zhenxiang Yan, Renfen Hu
- 链接：[arXiv](https://arxiv.org/abs/2611.08231) · [PDF](https://arxiv.org/pdf/2611.08231) · [HF](https://huggingface.co/papers/2611.08231)

Large language models (LLMs) are widely used for information access, content production, and agent-based task execution, but their outputs remain vulnerable to subtle, high-risk hallucinations. To systematically evaluate and advance post-generation hallucination detection, we introduce HaluCheck, a large-scale, bilingual benchmark comprising over 42k instances spanning both factual hallucinations in text and…

## 76. Signals, Evidence, and Context: User Scrutiny in Real-World LLM Conversations

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, language model, large language, spec
- 作者：Ahana Biswas, Yu-Ru Lin
- 链接：[arXiv](https://arxiv.org/abs/2611.08232) · [PDF](https://arxiv.org/pdf/2611.08232) · [HF](https://huggingface.co/papers/2611.08232)

Large language models (LLMs) often present synthesized answers without making their supporting evidence easy to inspect. We study how features of these answers relate to users' subsequent accepting, checking, and challenging in 489,283 assistant-user response pairs from ShareChat and WildChat. Broad attribution language appears in 31.9% of qualifying responses, compared with explicit URLs in 1.33%, revealing a gap…

## 77. Multimodal-SEA: Benchmarking AI Agent Security under Multimodal Social Engineering Attacks

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, evaluation, benchmark, spec
- 作者：Zhitao He, Chi Him Zhang, Chengru Han, Yi R Fung
- 链接：[arXiv](https://arxiv.org/abs/2611.08281) · [PDF](https://arxiv.org/pdf/2611.08281) · [HF](https://huggingface.co/papers/2611.08281)

Personal AI agents face social engineering attacks supported by forged multimodal content, but existing evaluations mainly focus on text-based dialogue, leaving their intrinsic security under such attacks insufficiently studied. We introduce Multimodal-SEA, an interactive benchmark comprising 608 expert-designed tasks grounded in real-world fraud cases, covering 14 domains and 152 attack scenarios with prepared…

## 78. AutoCompress: Automated Hardware-Guided Model Compression

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, benchmark, coding, spec
- 作者：Sheldon Liang, Ali Taghibakhshi, Saurav Muralidharan, Sharath Turuvekere Sreenivas, Ashwath Aithal, Pavlo Molchanov, Nima Tajbakhsh
- 链接：[arXiv](https://arxiv.org/abs/2611.08290) · [PDF](https://arxiv.org/pdf/2611.08290) · [HF](https://huggingface.co/papers/2611.08290)

LLM pruning must preserve quality while meeting hardware- and workload-specific constraints on latency, throughput, and memory. Existing pruning workflows often target parameter counts, requiring practitioners to manually select model sizes that meet latency, throughput, and GPU memory limits. However, parameter count alone does not predict these metrics, which depend on the model architecture, workload, hardware,…

## 79. RM-VLM: From Natural-Language Task Descriptions to Vision-Grounded Reward Machines

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reinforcement learning, language model, large language
- 作者：Roko Parac, Christos Ziakas, Leo Ardon, Alessandra Russo
- 链接：[arXiv](https://arxiv.org/abs/2611.08308) · [PDF](https://arxiv.org/pdf/2611.08308) · [HF](https://huggingface.co/papers/2611.08308)

Reward machines (RMs) have been proposed as a reward formulation in reinforcement learning (RL) to capture non-Markovian tasks where credit assignment depends on history. By representing reward functions as automata, RMs expose the task's temporal structure and allow such rewards to be handled within a Markovian framework. However, they assume a labelling function, a proposition-grounding oracle for observations,…

## 80. Benchmarking Large Language Models on Heterogeneous Cognitive and Biomedical Knowledge Graphs: The Role of Graph Grounding in Multi-Hop Reasoning and Hallucination Mitigation

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, benchmark, language model, large language, spec
- 作者：Ali Sarabadani, Kheirolah Rahsepar Fard, Tahereh Jeirani
- 链接：[arXiv](https://arxiv.org/abs/2611.08315) · [PDF](https://arxiv.org/pdf/2611.08315) · [HF](https://huggingface.co/papers/2611.08315)

Large language models (LLMs) are increasingly used in biomedical and cognitive neuroscience, but their ability to reason reliably over heterogeneous knowledge graphs (KGs) remains unclear. We benchmark five LLMs (GPT-5.1, Gemini 2.0 Pro, Llama 3, Qwen, and BioGPT) across five KGs: DrugBank, NeuroSynth, Cognitive Atlas, Brain Map, and GDPKG. We introduce a multitier query dataset to evaluate reasoning depth and…

## 81. Learning the Task or Learning the Verifier? Rethinking Criteria Exposure in Embodied Self-Improvement

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, benchmark, coding, spec
- 作者：Wenbo Huang, Jianxin Bi, Shunyu Yang, Ruiyang Si, Rui Ni, Qiang Wang, Shulong Jiang, Yintianrun Zhang, Feixiang Ruan, Kewei Zhang, Ye Huang, Shukai Gong, Daquan Zhou
- 链接：[arXiv](https://arxiv.org/abs/2611.08318) · [PDF](https://arxiv.org/pdf/2611.08318) · [HF](https://huggingface.co/papers/2611.08318)

Self-improving embodied agents are increasingly being developed and compared on robot simulation benchmarks. Several recent works expose the benchmark's success criteria to the learning agent, a practice we call Criteria Exposure (CE). These criteria, originally written to verify policies trained by imitation learning, often demand more than the corresponding language instructions, so a score from such a verifier…

## 82. SpecCTMC: Exact Speculative Simulation of Diffusion Language Model Continuous-Time Markov Chains

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, language model, coding, spec
- 作者：Siva Rajesh Kasa, Yasong Dai, Sumit Negi, Hongdong Li
- 链接：[arXiv](https://arxiv.org/abs/2611.08362) · [PDF](https://arxiv.org/pdf/2611.08362) · [HF](https://huggingface.co/papers/2611.08362)

Masked diffusion language models offer parallel text generation, but independently sampling multiple tokens can disrupt their dependencies and change the output distribution. Exact continuous-time sampling avoids this approximation, yet typically requires one sequential model evaluation per token. We introduce SpecCTMC, a training-free speculative sampler that reduces this sequential bottleneck without a separate…

## 83. StrataFlux: Memory-Hierarchy-Native Low-Bit LLM Inference

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, language model, large language, coding
- 作者：Jake Hyun, Ziyu Zhao, Jae-sun Seo, Mohamed S. Abdelfattah
- 链接：[arXiv](https://arxiv.org/abs/2611.08363) · [PDF](https://arxiv.org/pdf/2611.08363) · [HF](https://huggingface.co/papers/2611.08363)

Quantization reduces the memory and bandwidth demands of large language model (LLM) inference but can degrade accuracy; offloading higher-precision data can instead stall generation. We introduce StrataFlux, a framework that challenges this tradeoff by recovering accuracy lost to low-bit weight and key-value (KV) cache quantization while retaining quantization's memory and speed advantages. StrataFlux co-designs…

## 84. Benchmarks as Software: Terminal-Bench and the Case for Continuous Benchmarks

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, evaluation, benchmark, coding, spec
- 作者：E. Kelly Buchanan, Crystal Zhou, Scott W. Linderman, Christopher Ré
- 链接：[arXiv](https://arxiv.org/abs/2611.08417) · [PDF](https://arxiv.org/pdf/2611.08417) · [HF](https://huggingface.co/papers/2611.08417)

Coding agents are among the most economically consequential deployments of LLMs to date, making reliable evaluation increasingly important. Yet even benchmarks that are carefully validated at release can become stale. As models improve, they can discover valid solutions that existing verifiers reject, while changes to evaluation infrastructure can invalidate assumptions embedded in tasks and tests. We call the…

## 85. The Power of Meta Access in the Software of the Future --- Demonstrated on LLM Chat UIs and Chat AI

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, language model, large language, coding, retrieval
- 作者：Julian Kunkel, Ali Doosthosseini
- 链接：[arXiv](https://arxiv.org/abs/2611.08428) · [PDF](https://arxiv.org/pdf/2611.08428) · [HF](https://huggingface.co/papers/2611.08428)

Chat remains the default surface for many large language model (LLM) tasks, even as agentic tools such as OpenCode excel at coding and automation. Yet the model sees the current dialogue but not the workspace around it. We explore meta access---giving the assistant a structured, permissioned view of the interface itself and propose a ladder of levels: feature tutoring; metadata, settings, and preference access;…

## 86. Multimodal Information Interactions Bottleneck for Multimodal Self-Supervised Learning

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, coding, spec
- 作者：Liangjian Wen, Jiangtao Zheng, Jiang Duan, Qun Dai, Yong Dai, Jianzhuang Liu, Jun Wang, Shu-Dong Huang, Xinwang Liu, Zenglin Xu, Zhao Kang
- 链接：[arXiv](https://arxiv.org/abs/2611.07718) · [PDF](https://arxiv.org/pdf/2611.07718) · [HF](https://huggingface.co/papers/2611.07718)

Multimodal self-supervised learning is challenged by heterogeneity, unequal informativeness, and complex information interactions across multimodal data sources such as images, text, audio, and tabular data. While contrastive methods effectively align shared semantics, they typically rely on strong multi-view redundancy assumptions, overlooking modality-specific and synergistic information, thus leading to…

## 87. Evaluating Language Model Features for Zero-Shot Time-Series Anomaly Detection Under Isolation Assumption

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, language model, large language
- 作者：Romain Hermary, Nesryne Mejri, Djamila Aouada
- 链接：[arXiv](https://arxiv.org/abs/2611.07720) · [PDF](https://arxiv.org/pdf/2611.07720) · [HF](https://huggingface.co/papers/2611.07720)

Time-Series Anomaly Detection (TSAD) is a fundamentally challenging task: it is unsupervised, requires high local precision capabilities, and suffers from limited labelled data. Recent work has explored adapting Large Language Models (LLMs) to time-series via cross-modal transfer. However, existing approaches are poorly suited to Multivariate TSAD (MTSAD), as tokenisation often obscures fine-grained temporal and…

## 88. Seeing Beyond the Next Step: World-Model-Guided Human-Like Navigation in Multi-Agent Scenes

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reasoning, evaluation
- 作者：Seong-Eun Hong, JuYeong Hwang, Jinhyun Kim, Hanyoung Jang, HyeongYeop Kang
- 链接：[arXiv](https://arxiv.org/abs/2611.07730) · [PDF](https://arxiv.org/pdf/2611.07730) · [HF](https://huggingface.co/papers/2611.07730)

Selecting a next motion in a populated scene is not just a matter of avoiding what is currently in the way: an action can be locally feasible yet drift onto the road instead of the crosswalk, cut into a stream of crossing pedestrians, or bottleneck a narrow passage. These failure modes are invisible from the current state alone, and acting on them requires reasoning about what each candidate action will cause. World…

## 89. MV-Sign: Multi-View 3D Motion Integration and Enhanced Text-to-Motion Conditioning for Sign Language Production

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, spec, retrieval
- 作者：Singyu Muk, Kaustubh Kundu, Kunyuan Xie, Weijie Wang, Kalin Stefanov
- 链接：[arXiv](https://arxiv.org/abs/2611.07811) · [PDF](https://arxiv.org/pdf/2611.07811) · [HF](https://huggingface.co/papers/2611.07811)

Sign language production (SLP) aims to generate appropriate sign language motion from spoken language text. However, current 3D SLP methods suffer from noisy supervision and weak text conditioning. Specifically, these methods typically rely on pseudo-3D motion data fitted from single-view frontal videos, which introduces severe self-occlusion and loses fine-grained hand details, ultimately degrading downstream…

## 90. Different Corpora, Different Skills? A Paired Study of Small Language Models

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, language model
- 作者：Edoardo Vaira, Georgios Chavales, Pierre Nugues
- 链接：[arXiv](https://arxiv.org/abs/2611.07812) · [PDF](https://arxiv.org/pdf/2611.07812) · [HF](https://huggingface.co/papers/2611.07812)

Small language models are often trained under tight data budgets, where the choice of pretraining corpus may matter as much as model size or training recipe. We compare two contrasting corpora at matched 10-million- and 37-million-word budgets: the 1911 Encyclopaedia Britannica and the BabyLM 2026 strict pretraining corpus. For each corpus, we train teacher models, distilled 58-million-parameter Baby-Llama students,…

## 91. Axis-LoRA: Probing and Adapting Embedding Models for Personal-Memory Retrieval

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, benchmark, retrieval
- 作者：Dohoon Kim, Junho Park, Hyunwoong Bae, Seyoon Kim, Taesup Moon
- 链接：[arXiv](https://arxiv.org/abs/2611.07820) · [PDF](https://arxiv.org/pdf/2611.07820) · [HF](https://huggingface.co/papers/2611.07820)

As LLMs are increasingly asked questions about a user's personal experiences, retrieval must distinguish memories by time, place, person, and event. Current personal-memory pipelines rely on frozen dense embedding models to embed memories for retrieval, but we find that these models do not capture the four axes well. Swapping a memory's date or place barely shifts its embedding, and a trained projection on top of…

## 92. Estimating Spectrum-Free Information Bounds for Generative Surrogates Beyond Conditional Collapse

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, spec
- 作者：Chaitanya Dumbre, Sourabh Dube
- 链接：[arXiv](https://arxiv.org/abs/2611.07826) · [PDF](https://arxiv.org/pdf/2611.07826) · [HF](https://huggingface.co/papers/2611.07826)

Conditional generative surrogates in high-energy physics, such as models that predict reconstructed jets from partons, are often evaluated on $1\text{D}$ marginal divergences among other metrics. Taken alone these metrics can reward conditional collapse. On a CMS simulation benchmark, a sampler that ignores the conditioner beats a trained Mixture Density Network (MDN) on all four target marginals under both KL and…

## 93. Computation, not weight access: large language models as auditors of clinical prediction networks

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：language model, large language, spec
- 作者：Zhiyu Liu, Xinyu Yang
- 链接：[arXiv](https://arxiv.org/abs/2611.07847) · [PDF](https://arxiv.org/pdf/2611.07847) · [HF](https://huggingface.co/papers/2611.07847)

Frontier large language models (LLMs) have been reported to read, edit and write the weights of small neural networks, raising the prospect of auditing clinical prediction models from their files alone. Public demonstrations, however, mixed reading raw weights with running code. We separated these conditions in internally pre-specified simulation experiments. Tanh networks of 105 to 38,401 weights were trained on…

## 94. Learning Robotic World Models with Semantic and Visual Feedback

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, spec, planning
- 作者：Hao Wu, Yuqi Li, Yizhou Zhao, Kun Wang, Xiao Luo, Yu Cheng, Bo An, Yingli Tian, Laszlo A. Jeni, Ming-Hsuan Yang
- 链接：[arXiv](https://arxiv.org/abs/2611.07850) · [PDF](https://arxiv.org/pdf/2611.07850) · [HF](https://huggingface.co/papers/2611.07850)

Robot world models predict action-conditioned future visual states to support robotic planning and decision making. However, visual reconstruction does not fully capture task progress, semantic evaluation alone provides limited constraints on fine-grained visual errors, and homogeneous predictions limit comparative feedback. We present RoboImagine, a framework for post-training autoregressive robotic world models…

## 95. FARR: Forecast-Aware Residual Refinement with Matched Endpoint Evidence for Long-Horizon Time-Series Forecasting

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, language model, large language
- 作者：Yiyang Zhang, Yuli Zheng, Bin Li, Meimei Zhang, Qiang Sun
- 链接：[arXiv](https://arxiv.org/abs/2611.07870) · [PDF](https://arxiv.org/pdf/2611.07870) · [HF](https://huggingface.co/papers/2611.07870)

Large language models use auxiliary conditioning to incorporate additional information into time-series forecasts. However, auxiliary conditioning does not consistently improve accuracy and can increase forecasting error when its influence is poorly matched to the observed temporal context. We propose Forecast-Aware Residual Refinement (FARR), which learns to correct forecasts using endpoint evidence. FARR obtains a…

## 96. When Bigger Becomes Brittle: Why Compression Hurts More as Language Models Scale

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, language model, retrieval
- 作者：Gautam Gupta, Dikshant Kukreja, Unique Kumar, Avni Mittal, Deepanshu Dabas, Kshitij Sah, Erik Cambria, Rajiv Ratn Shah, Zhengkui Wang, Avinash Anand
- 链接：[arXiv](https://arxiv.org/abs/2611.07891) · [PDF](https://arxiv.org/pdf/2611.07891) · [HF](https://huggingface.co/papers/2611.07891)

Quantization and pruning reduce the cost of deploying language models, but their effects are usually reported as benchmark scores. Such scores record only the loss that remains at the output. Inside the model, compression damages some components more than others, and the rest of the network can partly compensate. The observed loss therefore reflects both the damage and this compensation, which benchmark scores…

## 97. Structure from Collision via Hypothesis-Space Reasoning

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, benchmark, spec
- 作者：Takuhiro Kaneko
- 链接：[arXiv](https://arxiv.org/abs/2611.07900) · [PDF](https://arxiv.org/pdf/2611.07900) · [HF](https://huggingface.co/papers/2611.07900)

Knowledge of the hidden interior structure of an object, including the presence and location of cavities, is essential for predictive simulation, robotic manipulation, and nondestructive inspection. However, such cavities leave no direct signature on the static visible surface, making collision-induced deformation one of the few cues used to infer their presence. Structure from Collision (SfC) addresses this problem…

## 98. Adaptive Semantic Branching: Disagreement-Localized Cross-Trajectory Regeneration for Reasoning Candidate Expansion

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, evaluation, spec
- 作者：Jeong-Yoon Kim, Tae-Yoon Lee
- 链接：[arXiv](https://arxiv.org/abs/2611.07918) · [PDF](https://arxiv.org/pdf/2611.07918) · [HF](https://huggingface.co/papers/2611.07918)

Reasoning trajectories generated for the same problem often arrive at conflicting answers. These disagreements reveal alternative intermediate decisions that can be reused to explore new solutions. We introduce Adaptive Semantic Branching (ASB), a training-free inference procedure that turns cross-trajectory disagreement into targeted candidate generation. ASB first groups independently sampled trajectories by…

## 99. ZeroRAG: Adaptive Semantic Peer Routing for Decentralized Retrieval-Augmented Generation

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：language model, large language, retrieval
- 作者：Petru Neague, Quinten Stokkink, Martijn de Vos, Rafael Pires, Mathis Randl, Anne-Marie Kermarrec, Johan Pouwelse
- 链接：[arXiv](https://arxiv.org/abs/2611.07928) · [PDF](https://arxiv.org/pdf/2611.07928) · [HF](https://huggingface.co/papers/2611.07928)

Retrieval-augmented generation (RAG) is a standard approach to enhance the reliability of large language model (LLM) outputs by retrieving documents relevant to a query and supplying them in the LLM prompt. Today's RAG systems collect, index, and serve these documents from centralized stores. In practice, however, documents are owned by organizations, devices, and individuals who cannot or will not surrender custody…

## 100. Towards Scalable Diagnostic-Driven Whole-Slide Image Retrieval for Pathology Archives

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, benchmark, retrieval
- 作者：Jingsong Liu, Youssef Wally Han Li, Weiwei Zhou, Jing Dai, Elisabeth Wetzer, Peter J. Schüffler
- 链接：[arXiv](https://arxiv.org/abs/2611.07935) · [PDF](https://arxiv.org/pdf/2611.07935) · [HF](https://huggingface.co/papers/2611.07935)

The growing adoption of digital pathology has rapidly expanded collections of hematoxylin-and-eosin whole-slide images, yet efficient navigation through these archives remains challenging, as metadata is often inconsistent or unavailable. Content-based image retrieval addresses this challenge by identifying similar cases directly from visual representations instead of manual annotations or metadata. Existing…

## 101. CardioLM: A multilingual suite of small language models for the cardiology domain

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, language model, spec
- 作者：Manuela-Daniela Danu, Miguel Rodríguez-Ortega, Alberto Becerra-Tome, Pablo Arancibia, Fernando Gallego-Donoso, Lorenzo Pratesi, Xi Bai, Andrei-Damian Dinescu, Salvador Lima-López, Andrea Guala, Saskia Haitjema, Jonas Mack, Michele Miranda, Wesam Al Nabki, Jan Rodríguez-Miret, Vasile George Marica, Vladimír Kincl, Kateřina Dostálová, Michael Andrej, Alicia Ujil, Corinne Allaart, Machteld Boonstra, Malin Overmars, Anoop Shah, Giovanna Ceroni, Jonathan Kossoff, Domenico D'Amario, Renzo Laborante, Antonio Iaconelli, Isabella Fumarulo, Jacopo Lenkowicz, Livia Lilli, Emma Weiss, Alex Scafa, Felix Lindberg, Milou Gamage, Eulàlia Farré-Maduell, Sébastien Bratières, Martin Krallinger, Bram van Es
- 链接：[arXiv](https://arxiv.org/abs/2611.07940) · [PDF](https://arxiv.org/pdf/2611.07940) · [HF](https://huggingface.co/papers/2611.07940)

Background: Cardiovascular care generates large volumes of clinical free-text documentation in local languages. However, clinical natural language processing (NLP) resources remain concentrated in English, and no existing benchmark is cardiology-specific, multilingual, and broad in entity coverage. Methods: We present two contributions. The first is CardioCCC, a corpus of 508 cardiology case reports originally…

## 102. ChemE-as-Code: An Open-Source Platform for Agentic AI in Chemical Engineering

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, language model, large language
- 作者：Artur M. Schweidtmann
- 链接：[arXiv](https://arxiv.org/abs/2611.07947) · [PDF](https://arxiv.org/pdf/2611.07947) · [HF](https://huggingface.co/papers/2611.07947)

ChemE-as-Code provides an open-source environment in which AI agents built on large language models (LLMs) can carry out chemical engineering work and engineers can check it. Its calculation tools range from catalysis through process simulation to plant layout, HAZOP and life cycle assessment, and skills tell a general-purpose agent how to use them. Engineering files are linked, machine-readable and versioned in…

## 103. Beyond the Keyword: A Human-Annotated Benchmark for Arabic Anxiety-Related Discourse

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, retrieval
- 作者：Shimaa Ibrahim, Mabrouka Bessghaier, Md. Rafiul Biswas, Insaf Elouard, Wajdi Zaghouani
- 链接：[arXiv](https://arxiv.org/abs/2611.07949) · [PDF](https://arxiv.org/pdf/2611.07949) · [HF](https://huggingface.co/papers/2611.07949)

Keyword retrieval returns expressions of personal anxiety together with many other uses of anxiety-related language. We present a benchmark of 1,000 Arabic Twitter/X posts retrieved with the keyword qalaq ("anxiety/worry") and annotated for six discourse functions. Two native Arabic-speaking annotators labeled every post independently, reaching 51.1% raw agreement (Cohen's $κ= 0.378$). We then reviewed all 489…

## 104. Rotation Is Token-Blind: A Structural Criterion for Post-Training Quantization of Feed-Forward Geometry Transformers

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, benchmark, spec
- 作者：Huanfei He, Bohao Zhang, Jiaxin Zhang, Wei Sui, John See, Zeyd Boukhers, Cong Yang
- 链接：[arXiv](https://arxiv.org/abs/2611.07955) · [PDF](https://arxiv.org/pdf/2611.07955) · [HF](https://huggingface.co/papers/2611.07955)

Feed-forward 3D models use Transformers to predict camera poses, depth, and structure in one pass, avoiding iterative multi-view optimization. Long sequences and deep attention incur high compute and memory costs, motivating Post-Training Quantization (PTQ) for deployment. Existing PTQ methods mainly suppress channel-wise outliers by smoothing or orthogonal rotation. Geometry Transformers introduce a different…

## 105. CoRD: Coupled Rollouts Fill the Blind Spot of On-Policy Distillation

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, coding, spec
- 作者：Guhan Chen, Bohan Li, Jun Rao, Hejin Wang, Songtao Tian, Yexin Xie, Xiaojun Meng, Peng Yuan, Jiansheng Wei, Xuebo Liu, Zixiong Yu
- 链接：[arXiv](https://arxiv.org/abs/2611.07959) · [PDF](https://arxiv.org/pdf/2611.07959) · [HF](https://huggingface.co/papers/2611.07959)

On-policy distillation trains a student on its own rollouts, so states the teacher would reach but the student does not are seldom supervised. We introduce CoRD (coupled-rollout distillation), which keeps the on-policy loss and moves only the distribution of training states toward the teacher, drawing rollouts from a geometric interpolation of student and teacher through the maximal coupling of speculative decoding.…

## 106. NutriVisRAG: Multimodal Exemplar Grounding for Nutrient Estimation with Vision-Language Models

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：language model, spec, retrieval
- 作者：Lubnaa Abdur Rahman, Ioannis Papathanail, Maria Panagiotou, Nefeli Dimitropoulou, Margret Harðardóttir, Elisabeth J. den Brok, Bastiaan E. de Galan, Stavroula Georgia Mougiakakou
- 链接：[arXiv](https://arxiv.org/abs/2611.08054) · [PDF](https://arxiv.org/pdf/2611.08054) · [HF](https://huggingface.co/papers/2611.08054)

Diet is a major determinant of health, yet accurate dietary assessment from free-living meal images remains challenging. Existing retrieval-based Vision-Language Model (VLM) approaches to nutrient estimation typically rely on textual food representations, while, to our knowledge, direct grounding on visually similar annotated meals has not been investigated. We present NutriVisRAG, a retrieval-augmented generation…

## 107. Can an LLM Actually Reason and Program about Neural Network's Weights or is it just memorization on steroids? Exploring "Weight-Space Programming"

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, language model, large language
- 作者：Nazmus Sakib Ahmed
- 链接：[arXiv](https://arxiv.org/abs/2611.08070) · [PDF](https://arxiv.org/pdf/2611.08070) · [HF](https://huggingface.co/papers/2611.08070)

Large language models (LLMs) have recently been reported to read and write the raw weights of neural networks directly, a capability termed weight-space programming. We ask whether the reading side of this capability reflects reasoning about weight flows or a combination of local arithmetic at the network's edges and memorized priors over public datasets. We test Claude Opus 5.5 on small convolutional networks of…

## 108. Spatiotemporal Dynamics-Aware Industrial Anomaly Detection and Reasoning

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, language model, large language
- 作者：S-Wei Chen, Siangyu Yang, Yi-Chen Jan, Chun-Yi Lee, Shao-Yuan Lo
- 链接：[arXiv](https://arxiv.org/abs/2611.08080) · [PDF](https://arxiv.org/pdf/2611.08080) · [HF](https://huggingface.co/papers/2611.08080)

Industrial Anomaly Detection (IAD) is a long-established problem that aims to detect defects in industrial products during manufacturing for quality control. Most existing studies focus on static visual patterns as the basis for detection. However, in real manufacturing environments, many anomalies are dynamics-based, such as irregular movements that cannot be perceived from static cues alone. We observe that even…

## 109. TerraMesh-Masks: Open-Vocabulary Segmentation for Earth Observation

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, spec
- 作者：Benedikt Blumenstiel, Hugues Devimeux, Johannes Jakubik, Konrad Schindler
- 链接：[arXiv](https://arxiv.org/abs/2611.08081) · [PDF](https://arxiv.org/pdf/2611.08081) · [HF](https://huggingface.co/papers/2611.08081)

Open-vocabulary segmentation (OVS) enables models to segment a variety of concepts specified in natural language, removing the need for fixed label sets and fine-tuning. While recent OVS approaches have shown strong performance on natural images, they transfer poorly to Earth observation (EO) data due to differing semantics, scales, sensing modality, and geographic context. To date, large-scale EO-specific datasets…

## 110. Linguistic boundaries emerge from pressure-constrained processing dynamics

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, language model, large language
- 作者：Rui He, Philipp Homan, Wolfram Hinzen
- 链接：[arXiv](https://arxiv.org/abs/2611.08085) · [PDF](https://arxiv.org/pdf/2611.08085) · [HF](https://huggingface.co/papers/2611.08085)

Human cognition organizes continuous experience into bounded units while maintaining continuity across them. Linguistic elements are also organized into bounded structural units such as words and phrases, with sentence marking the final bound of a grammatical construction process. How do such boundaries emerge? We propose boundaries emerge from interacting demands to maintain unresolved dependencies, integrate…

## 111. MUSS: A Multi-scale and Sequence-based Model for Single-cell Gene Regulation

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：language model, coding, spec
- 作者：Kangjie Zheng, Amirhossein Vahidi, Liying Jin, Joseph Clarke, Vijaya Baskar MS, Connor Rogerson, Mengji Zhang, Muzlifah Haniffa, Anshul Kundaje, Mo Lotfollahi
- 链接：[arXiv](https://arxiv.org/abs/2611.08086) · [PDF](https://arxiv.org/pdf/2611.08086) · [HF](https://huggingface.co/papers/2611.08086)

Modeling gene regulation in single cells requires jointly representing DNA sequence, chromatin accessibility, and gene expression across regulatory scales. Sequence-based models capture DNA-level regulatory grammar but often lack cell-level resolution, whereas many single-cell omics models represent genes and peaks as fixed-vocabulary tokens without their underlying sequence. Here, we present MUSS, a sequence-based…

## 112. Gabor Gabor: E-Gaborformer, a Strictly Causal Speech Recognizer with Gabor-Dictionary Convolutions and Delta-Rule Memory

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, memory, coding
- 作者：Nir Krakowski, Tamir Cohen, Ohad Zohar, Chen Zarfati
- 链接：[arXiv](https://arxiv.org/abs/2611.08092) · [PDF](https://arxiv.org/pdf/2611.08092) · [HF](https://huggingface.co/papers/2611.08092)

Real-time voice agents need a speech recognizer that never waits for future audio and whose memory per call does not grow with the length of the call. We present E-Gaborformer, a strictly causal encoder that combines Gated DeltaNet-2 recurrent layers with sliding-window attention in a 3:1 ratio, and builds every temporal convolution from a fixed dictionary of causal Gabor atoms. Its streaming state is constant,…

## 113. Gradient Boosting for Efficient Rank Discovery in Tensor Network Kernel Machines

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, benchmark, spec
- 作者：Albert Saiapin, Kim Batselier
- 链接：[arXiv](https://arxiv.org/abs/2611.08093) · [PDF](https://arxiv.org/pdf/2611.08093) · [HF](https://huggingface.co/papers/2611.08093)

Tensor network kernel machines (TNKMs) combine nonlinear features with low-rank tensor representations to model complex relationships efficiently. However, selecting an appropriate tensor rank remains challenging, as conventional rank-search methods require training multiple candidate models, increasing computational costs. In this work, we focus on a canonical polyadic (CP) tensor network parameterization and…

## 114. Reinforcing End-to-End Autonomous Driving Safety via Negative-Aware Planning in a Unified World-Action Model

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, planning
- 作者：Zihao Zhang, Xinyu Zhang, Bing Zeng, Xingyu Chen, Zhenning Li, Bin Yu, Ziyuan Pu
- 链接：[arXiv](https://arxiv.org/abs/2611.08111) · [PDF](https://arxiv.org/pdf/2611.08111) · [HF](https://huggingface.co/papers/2611.08111)

World-action models (WAMs) jointly model future traffic states and driving actions for end-to-end autonomous driving in intelligent transportation systems. However, their action learning remains dominated by expert-trajectory imitation, leaving unsafe alternatives close to expert trajectories insufficiently constrained. To improve WAM robustness in safety-critical scenarios, we propose NegWAM, a safety post-training…

## 115. Create Your Own Work Stack: Deploying Self-hosted AI and Tooling in a Tech Startup

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, coding, retrieval
- 作者：Saad Ahmed Bazaz, Talha Amjad, Abdurrehman Subhani, Sohaib Ahmed Bazaz, Abdullah Aamir
- 链接：[arXiv](https://arxiv.org/abs/2611.08116) · [PDF](https://arxiv.org/pdf/2611.08116) · [HF](https://huggingface.co/papers/2611.08116)

Self-hosting AI is often presented as a way to reduce inference costs and increase control, but deployment introduces its own costs. We report our experience deploying a hybrid AI stack at Grayhat Developers, a small software company with an AI-intensive development workflow. Our initial motivation was to counter the growing cost of commercial AI usage: Claude/Codex incurred approximately \$325 per month, with more…

## 116. Detecting Silent Faults at the Environment-Trainer Boundary in Reinforcement Learning

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reinforcement learning, evaluation
- 作者：Zuo Gou, Chenhao Lu
- 链接：[arXiv](https://arxiv.org/abs/2611.08144) · [PDF](https://arxiv.org/pdf/2611.08144) · [HF](https://huggingface.co/papers/2611.08144)

Robot reinforcement learning increasingly runs environments outside the trainer: in another process, on another machine, in another language. Many faults at this boundary raise no error. We make the boundary a wire protocol and ask what notices a fault in it. On Pendulum, HalfCheetah, Hopper and a 7-joint arm (Pusher), we injected up to 23 faults into what crosses the wire and 2 into the trainer's log, from one…

## 117. A Generative Foundation Model for Multimodal Tokamak Tasks

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, spec
- 作者：Yingshuai Ji, Haodong Feng, Guohong Deng, Gelin Bian, Yue Wang
- 链接：[arXiv](https://arxiv.org/abs/2611.08153) · [PDF](https://arxiv.org/pdf/2611.08153) · [HF](https://huggingface.co/papers/2611.08153)

Tokamak experiments record diverse measurements, including waveforms, profiles, fields, and scalars, which are used to reconstruct the plasma, forecast its evolution, recover associated control signals, and estimate disruption risk. Most models are built separately for one task and a fixed set of inputs and outputs, and each relies on a prescribed subset of diagnostics rather than structuring the full multimodal…

## 118. BabyTheorist: A Benchmark for Learning to Theorize the World from Observation Alone

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, evaluation, benchmark
- 作者：Doojin Baek, Junyeob Baek, Mingyu Jo, Hosung Lee, Taegu Kang, Gyubin Lee, Sungjin Ahn
- 链接：[arXiv](https://arxiv.org/abs/2611.08177) · [PDF](https://arxiv.org/pdf/2611.08177) · [HF](https://huggingface.co/papers/2611.08177)

How would we know whether a machine truly understands the world? We argue that one key capability is \textit{observational theory learning}: acquiring reusable theories from pure observations and applying them to new situations. Current visual reasoning benchmarks focus primarily on the latter, presenting each task as a few-shot puzzle grouped by a common rule. We introduce BabyTheorist, a benchmark for controlled…

## 119. LeanContext: Disentangling Mathematical Resources from Local Formal Context in Lean Whole-Proof Generation

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, spec
- 作者：Hang Zhang, Qihao Ye, Litong Liu, Yunbei Zhang, Yugyung Lee, Yue Zhou, Bowen Liu, Emily First, Cheng Han, Qiao Zhuang
- 链接：[arXiv](https://arxiv.org/abs/2611.08277) · [PDF](https://arxiv.org/pdf/2611.08277) · [HF](https://huggingface.co/papers/2611.08277)

Neural theorem proving increasingly uses retrieved premises and project context to support proof generation. Evaluating these resources requires measuring the advantage of target-selected declarations over comparable alternatives and how this advantage depends on training. We introduce LeanContext, a benchmark of 129,826 Lean whole-proof generation problems, to investigate these questions. We group selected complete…

## 120. A Generative Model of Contextual Integrity: Appropriate vs. Inappropriate Information Sharing

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：language model, large language, spec
- 作者：Omer Ebead, Claude Formanek, Joel Z. Leibo
- 链接：[arXiv](https://arxiv.org/abs/2611.08284) · [PDF](https://arxiv.org/pdf/2611.08284) · [HF](https://huggingface.co/papers/2611.08284)

Contextual integrity (CI) holds that appropriate information flow depends on context-specific norms. The same disclosure may be appropriate in one context and inappropriate in another. We build a generative model of contextual integrity to study information sharing through simulated conversations. Two actors played by large language models exchange messages, with one holding private information and the other seeking…
