# 每日 AI 论文

生成时间：2026-10-08 06:05 UTC  ·  共 120 篇（已按 arXiv ID 去重）

来源：Hugging Face Daily Papers + arXiv（cs.AI / cs.LG / cs.CL / cs.CV）。
排序：HF 上榜、点赞、多源命中、兴趣词。兴趣词可在 `config.json` 改。

## 1. Long-WAM: Scaling the Context of World-Action Models

- 分数：40.0  ·  HF 赞：63  ·  来源：huggingface + arxiv
- 兴趣命中：memory, coding, spec, planning
- 作者：Wei Huang, Bohan Zhang, Chenzhi Liu, Isabella Liu, Shuai Yang, Weian Mao, Luozhou Wang, Yicheng Xiao, Weifeng Lin, Qixin Hu, Bryan Chu, Sifei Liu, Linxi Fan, Xiaojuan Qi, Song Han, Yukang Chen
- 链接：[arXiv](https://arxiv.org/abs/2610.10528) · [PDF](https://arxiv.org/pdf/2610.10528) · [HF](https://huggingface.co/papers/2610.10528)

Real-time robot control demands enough visual history to infer motion and task progress, but processing that history can delay action. We present Long-WAM, a model-system framework for scaling the context of causal world-action models under real-time control constraints. Our central finding is that access to history is not the same as using it: longer histories pay off far more when the video foundation is…

## 2. TRACE: Rollout-Guided Quantization-Aware Training for FP4 Reinforcement Learning of MoE Language Models

- 分数：36.0  ·  HF 赞：84  ·  来源：huggingface
- 兴趣命中：memory, reasoning, reinforcement learning, language model, large language, coding
- 作者：Xin Wang, Hao Yu, Zhengyang Zhuge, Bochao Mao, Zheng Li, Junda Feng, Yuyan Luo, Yi Zhang, Yizhong Cao, Mi Zhang, Dayiheng Liu, Jianwei Zhang
- 链接：[arXiv](https://arxiv.org/abs/2610.07767) · [PDF](https://arxiv.org/pdf/2610.07767) · [HF](https://huggingface.co/papers/2610.07767)

Reinforcement learning (RL) for post-training large language models (LLMs) incurs substantial computation and memory overhead during rollout generation, which motivates low-precision rollout for efficient RL training. However, existing FP4 RL methods suffer from a key limitation: they primarily optimize quantization accuracy on the training and rollout paths independently rather than directly reducing the…

## 3. Recursive Game Creator: An Agentic Product-Level Experience-Oriented Game Harness

- 分数：36.0  ·  HF 赞：51  ·  来源：huggingface
- 兴趣命中：agent, evaluation, coding, spec
- 作者：Jiajun Chen, Haoyu Wu, Mingda Jia, Xihui Liu
- 链接：[arXiv](https://arxiv.org/abs/2610.08621) · [PDF](https://arxiv.org/pdf/2610.08621) · [HF](https://huggingface.co/papers/2610.08621)

Recent game design agents have made substantial progress in generating playable games. However, program correctness does not ensure an enjoyable experience for players. We present Recursive Game Creator, an experience-oriented harness to advance agentic game development from rough game prototypes into entertaining games. Recursive Game Creator organizes recursive development around four components: Designer,…

## 4. STEPQuant: When and Where Errors Matter in Delta-Rule Recurrent State Quantization

- 分数：34.0  ·  HF 赞：61  ·  来源：huggingface
- 兴趣命中：memory, benchmark, coding
- 作者：Bingchen Yao, Haobo Xu, Haokun Lin, Yichen Wu, Ziyu Guo, Renrui Zhang, Zhichao Lu, Zhenan Sun, Ying Wei
- 链接：[arXiv](https://arxiv.org/abs/2609.38169) · [PDF](https://arxiv.org/pdf/2609.38169) · [HF](https://huggingface.co/papers/2609.38169)

Linear attention replaces growing KV caches with fixed-size recurrent states, yet these persistent states can become a substantial memory bottleneck under concurrent serving. Directly quantizing recurrent states to low precision often leads to severe accuracy degradation, as quantization errors propagate through successive state updates. We discover that the impact of these errors depends on two complementary…

## 5. GRACE: Generation-aware latent compression for efficient video generation

- 分数：34.0  ·  HF 赞：52  ·  来源：huggingface + arxiv
- 兴趣命中：spec
- 作者：Jiyoung Kim, Paul Hyunbin Cho, Jisu Nam, Donghoon Lee, Hyunsung Go, Yeonkyeong Lee, Hansaem Kim, Seungryong Kim
- 链接：[arXiv](https://arxiv.org/abs/2610.10524) · [PDF](https://arxiv.org/pdf/2610.10524) · [HF](https://huggingface.co/papers/2610.10524)

Highly compressed video autoencoders offer an effective way to accelerate video diffusion models, as the Diffusion Transformer (DiT) operates on far fewer tokens. However, such autoencoders are challenging to train, since a higher compression ratio degrades reconstruction quality and recovering it requires more channels, which is known to slow the convergence of the DiT. The compressed latent also differs from the…

## 6. nanoMuse: An Open-Source Personal Agent for Every Device You Own

- 分数：34.0  ·  HF 赞：51  ·  来源：huggingface
- 兴趣命中：agent, memory, evaluation
- 作者：Guangyi Liu, Yong Liu, Jiangning Zhang
- 链接：[arXiv](https://arxiv.org/abs/2610.08699) · [PDF](https://arxiv.org/pdf/2610.08699) · [HF](https://huggingface.co/papers/2610.08699)

Assistants from 2011 answered and waited, and agents from 2023 did a task and stopped. In September 2026 Meta's Muse showed an agent for one person, with accounts, devices, memory and a conversation that lasts, closed, in a vendor's cloud, in one country. Such an agent is expected to act on a person's accounts and devices, remember them across weeks, speak first when it is worth it, and answer for what it did. It is…

## 7. SGF+: Decoupling Gradient Flows for Autoregressive Video Generation

- 分数：34.0  ·  HF 赞：40  ·  来源：huggingface + arxiv
- 兴趣命中：spec
- 作者：Zihan Su, Junhao Zhuang, Yaowei Li, Siwen Lu, Haoran Li, Lingen Li, Haoyu Wu, Weiyang Jin, Songchun Zhang, Haoyang Huang, Chun Yuan, Zeyue Xue, Nan Duan
- 链接：[arXiv](https://arxiv.org/abs/2610.10429) · [PDF](https://arxiv.org/pdf/2610.10429) · [HF](https://huggingface.co/papers/2610.10429)

Autoregressive video generation requires denoising the current frames while writing their key-value representations as context for future predictions. However, these two roles typically share parameters, and we find that their gradients exhibit distinct patterns and systematic negative alignment, hindering the joint optimization of visual quality and temporal consistency. We introduce Self Gradient Forcing Plus…

## 8. RunningTab: Direct Workspace Interaction with Environment-Side Tabs

- 分数：32.5  ·  HF 赞：25  ·  来源：huggingface + arxiv
- 兴趣命中：agent, context window, benchmark, spec
- 作者：Jinheon Baek, Soyeong Jeong, Yumin Choi, Dongsu Han, Sung Ju Hwang
- 链接：[arXiv](https://arxiv.org/abs/2610.10444) · [PDF](https://arxiv.org/pdf/2610.10444) · [HF](https://huggingface.co/papers/2610.10444)

Much knowledge work produces new deliverables from files a workspace already holds, and LLM agents are beginning to take such work over. Through direct corpus interaction, an agent can search and read any of those files from a terminal with no indexing, and producing a deliverable from many of them in this way is what we call direct workspace interaction (DWI). Reaching the files, however, is only half the task:…

## 9. Questioning the Questions: Sustaining Self-Evolution in Reasoning Models

- 分数：32.0  ·  HF 赞：54  ·  来源：huggingface
- 兴趣命中：reasoning, benchmark
- 作者：Jinyuan Li, Chengsong Huang, Langlin Huang, Donghong Cai, Shiping Gao, Yuyi Yang, Jiaxin Huang
- 链接：[arXiv](https://arxiv.org/abs/2610.04299) · [PDF](https://arxiv.org/pdf/2610.04299) · [HF](https://huggingface.co/papers/2610.04299)

Self-evolving reasoning models learn from their own generated questions, yet repeated self-training can lead to performance collapse. In this paper, we investigate why performance deteriorates over successive rounds and how to sustain self-evolution. Our analysis identifies two recurring quality problems in self-generated questions: invalid questions and repeated variants of the same mathematical questions. First,…

## 10. Semifactual Credit-Augmented Policy Optimization

- 分数：32.0  ·  HF 赞：32  ·  来源：huggingface
- 兴趣命中：reasoning, reinforcement learning, benchmark, language model, large language, coding, spec
- 作者：Junshu Pan, Zhizhang Fu, Shulin Huang, Yiran Ding, Zifan Cheng, Wenqi Shao, Qiaosheng Zhang, Yue Zhang
- 链接：[arXiv](https://arxiv.org/abs/2609.40360) · [PDF](https://arxiv.org/pdf/2609.40360) · [HF](https://huggingface.co/papers/2609.40360)

Reinforcement learning with verifiable rewards (RLVR) has improved the reasoning capabilities of large language models (LLMs), yet their predictions remain sensitive to task-irrelevant prompt features. We investigate this sensitivity through semifactual prompt interventions that preserve the underlying problem and its answer. Our analysis reveals substantial variation in token-level sensitivity and shows that…

## 11. EVISKILL: Grounding Skill Evolution in Replayable Evidence

- 分数：31.0  ·  HF 赞：38  ·  来源：huggingface
- 兴趣命中：agent, benchmark
- 作者：Yan Zhou, Yili Wang, Yiwei Dai, Qinggang Zhang, Xin Wang
- 链接：[arXiv](https://arxiv.org/abs/2610.05030) · [PDF](https://arxiv.org/pdf/2610.05030) · [HF](https://huggingface.co/papers/2610.05030)

Continual skill evolution enables LLM agents to accumulate and refine reusable procedural knowledge from interaction experience without updating model parameters. Its effectiveness depends on determining not only what to change, but also why a change is justified and when it should become persistent guidance. However, existing experience-driven methods can lose the behavioral evidence and task contexts supporting…

## 12. Rethinking Cross-Tokenizer On-Policy Distillation: From Alignment Coverage to Supervision Reliability

- 分数：30.0  ·  HF 赞：159  ·  来源：huggingface
- 兴趣命中：reasoning
- 作者：Bingxi Hou, Guochao Jiang, Guofeng Quan, Weiqing Li, Wenfeng Feng, Guohua Liu, Yuewei Zhang
- 链接：[arXiv](https://arxiv.org/abs/2610.08448) · [PDF](https://arxiv.org/pdf/2610.08448) · [HF](https://huggingface.co/papers/2610.08448)

On-Policy Distillation (OPD) trains a student on its own generations using teacher feedback. With different tokenizers, comparing teacher and student predictions requires alignment at both sequence and vocabulary levels. In this paper, we examine whether expanding this alignment coverage improves learning. Across three heterogeneous teacher--student pairs on mathematical reasoning and code generation, strict 1:1…

## 13. DuoMatching: Joint-Marginal Distribution Matching for Few-Step Video Generation

- 分数：30.0  ·  HF 赞：73  ·  来源：huggingface
- 兴趣命中：evaluation
- 作者：Jiahao Zhan, Yan Wang, Yongrui Ma, Qunliang Xing, Ruchang Yao, Runtao Liu, Shijie Zhao, Tianfan Xue
- 链接：[arXiv](https://arxiv.org/abs/2610.03543) · [PDF](https://arxiv.org/pdf/2610.03543) · [HF](https://huggingface.co/papers/2610.03543)

Streaming video generation has benefited from distribution matching distillation (DMD), which matches the joint distribution of video frames to a video teacher's approximation of the real video distribution. Although this joint matching mitigates drift during autoregressive rollouts, limitations remain in visual quality and semantic alignment. To address these limitations, we propose DuoMatching, a distribution…

## 14. AutoSciBench: Autonomous Benchmark Generation for Evaluating Scientific Agents

- 分数：30.0  ·  HF 赞：28  ·  来源：huggingface
- 兴趣命中：agent, reasoning, evaluation, benchmark, spec
- 作者：Dongki Kim, Namkyeong Lee, Surag Nair, Carl Edwards, Xiner Li, Edward De Brouwer, Jenna Lynn Collier, Sung Ju Hwang, Gabriele Scalia, Ehsan Hajiramezanali
- 链接：[arXiv](https://arxiv.org/abs/2610.05140) · [PDF](https://arxiv.org/pdf/2610.05140) · [HF](https://huggingface.co/papers/2610.05140)

As agents rapidly evolve, existing benchmarks can become saturated, limiting their ability to distinguish capabilities and reveal remaining failure modes. Particularly in scientific domains, constructing and updating benchmarks requires substantial time, labor, and domain expertise, making it difficult to keep evaluation aligned with advances in agent capabilities. We address this challenge by investigating whether…

## 15. DecepEval: A Benchmark for Evaluating Deception in LLM Agents

- 分数：29.5  ·  HF 赞：27  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark, language model, large language
- 作者：Yiming Xu, Hongyue Yu, Beihua Yang, Zihan Chen, Yixin Liu, Zhen Peng, Bin Shi, Bo Dong, Chao Shen, Irwin King, Qinghua Zheng
- 链接：[arXiv](https://arxiv.org/abs/2610.07967) · [PDF](https://arxiv.org/pdf/2610.07967) · [HF](https://huggingface.co/papers/2610.07967)

As large language model (LLM) agents become increasingly autonomous, they may pursue task performance through deception, raising concerns about their reliable deployment. Existing evaluations show that LLM agents can deceive, but often examine isolated scenarios or narrowly defined conditions, limiting systematic understanding of when deception becomes more likely. To address this gap, we introduce DecepEval, a…

## 16. From Evidence to Action: How Tool-Using Agents Fail

- 分数：27.5  ·  HF 赞：35  ·  来源：huggingface
- 兴趣命中：agent
- 作者：Hongzhan Lin, Shidong Cao, Ziyang Luo, Wenhao Chai, Mong-Li Lee, Wynne Hsu
- 链接：[arXiv](https://arxiv.org/abs/2610.07753) · [PDF](https://arxiv.org/pdf/2610.07753) · [HF](https://huggingface.co/papers/2610.07753)

Tool-using agents make consequential changes to external state, yet correct outcomes do not guarantee that their actions were supported by evidence established beforehand. We study where this evidence-to-action chain breaks as agents move from deciding whether to act to executing single actions and dependent workflows. Across ten model-harness configurations, strong static action assessment can coexist with much…

## 17. HuatuoGPT-3: RL-Only Domain Adaptation from Base Models

- 分数：27.0  ·  HF 赞：26  ·  来源：huggingface
- 兴趣命中：language model, large language, spec
- 作者：Junying Chen, Xinyuan Xie, Ziniu Li, Wenyuan Gu, Jianquan Li, Xiang Wan, Guangjun Yu, Ruoyu Sun, Haizhou Li, Benyou Wang
- 链接：[arXiv](https://arxiv.org/abs/2610.05966) · [PDF](https://arxiv.org/pdf/2610.05966) · [HF](https://huggingface.co/papers/2610.05966)

Domain adaptation aims to turn a general-purpose large language model (LLM) into an expert for a target domain. While the dominant SFT+RL pipeline offers a convenient cold start, it may reduce exploration diversity and introduces additional complexity through multi-stage optimization. These limitations motivate RL-only adaptation. However, pure on-policy RL suffers from a cold-start problem, while mixed-policy RL…

## 18. TRIAGE: Direction-Aware Mismatch Stabilization of Native NVFP4 Reinforcement Learning

- 分数：26.5  ·  HF 赞：21  ·  来源：huggingface
- 兴趣命中：reasoning, reinforcement learning, benchmark, language model, large language
- 作者：Zhen Li, Shuai Zhang, Yanggan Gu, Yiming Zhang, Yang Yu, Mingfa Feng, Congkai Xie, Shuang Yu, Junjie Lai, Hongxia Yang
- 链接：[arXiv](https://arxiv.org/abs/2610.07043) · [PDF](https://arxiv.org/pdf/2610.07043) · [HF](https://huggingface.co/papers/2610.07043)

Low-precision execution can substantially accelerate reinforcement learning (RL) for large language models, but discrepancies between learner and sampler execution can destabilize policy optimization. In this paper, we characterize the interaction between mismatch and the policy-gradient direction, distinguishing locally amplifying from contracting update contributions that mismatch magnitude alone cannot identify.…

## 19. Mechanics of Long-Context Hybrid Models Part 1.1: From Hybrid Attention to Hybrid Position

- 分数：25.5  ·  HF 赞：19  ·  来源：huggingface + arxiv
- 兴趣命中：language model, large language
- 作者：Xiaoran Liu, Ziwei He, Xipeng Qiu
- 链接：[arXiv](https://arxiv.org/abs/2610.10114) · [PDF](https://arxiv.org/pdf/2610.10114) · [HF](https://huggingface.co/papers/2610.10114)

The architectural design of Large Language Models (LLMs) is shifting from traditional full-attention-only models to hybrid models, which combine different attention modules to improve long-context efficiency and performance in length extrapolation and context extension. To explain why hybrid models work and how to design them better, we propose Mechanics of Long-Context Hybrid Models. As Part 1.1 of this series, we…

## 20. Tetris3D: 3D Scene Generation With Objects That Fit Together

- 分数：25.0  ·  HF 赞：26  ·  来源：huggingface + arxiv
- 兴趣命中：-
- 作者：Jaeyeong Kim, Jinhyuk Jang, Jongmin Lee, Kyehong Park, Seungryong Kim
- 链接：[arXiv](https://arxiv.org/abs/2610.10539) · [PDF](https://arxiv.org/pdf/2610.10539) · [HF](https://huggingface.co/papers/2610.10539)

We propose Tetris3D, a generative framework for single-image 3D scene reconstruction that recovers objects which are physically and geometrically coherent as a scene. Existing methods often generate objects independently or couple them implicitly, providing limited guidance for ensuring fine-grained spatial compatibility between neighboring objects that interact with one another. To address this, we explicitly…

## 21. RobotWorld: Benchmarking Multimodal Agents for Robot Use Across Diverse Tasks and Embodiments

- 分数：25.0  ·  HF 赞：18  ·  来源：huggingface + arxiv
- 兴趣命中：agent, benchmark
- 作者：Zhiqin Yang, Chenxin Li, Xiaomeng Hu, Yibin Liu, Weidong Huang, Jiankai Sun, Haitao Li, Zijian Wu, Yuzhi Huang, Fanding Huang, Hanwen Sun, Jiashun Liu, Jingqi Tong, Mingxin Huang, Shaoli Hu, Shijue Huang, Tianyi Bai, Xinyuan Wang, Yunlong Lin, Zhengyang Tang, Zhexin Zhang, Zhuo Chen, Xierui Song, Juntao Dai, Boyuan Chen, Jiaming Ji, Fangneng Zhan, Mengkang Hu, Wei Xue, Yonggang Zhang, Han Hu, Tsung-Yi Ho, Yike Guo
- 链接：[arXiv](https://arxiv.org/abs/2610.10409) · [PDF](https://arxiv.org/pdf/2610.10409) · [HF](https://huggingface.co/papers/2610.10409)

General-purpose agents increasingly write code, use tools, and complete complex digital tasks, raising the question of how far these capabilities carry into the physical world. To investigate this, we introduce RobotWorld, a challenging simulation testbed for robot use: turning instructions and observations into physical task execution through robot interfaces. Its 84 tasks span manipulation, mobile manipulation,…

## 22. On KL-Regularized Policy Optimization

- 分数：24.5  ·  HF 赞：17  ·  来源：huggingface
- 兴趣命中：agent, reinforcement learning, language model, large language, spec
- 作者：Yifan Zhang
- 链接：[arXiv](https://arxiv.org/abs/2610.08963) · [PDF](https://arxiv.org/pdf/2610.08963) · [HF](https://huggingface.co/papers/2610.08963)

Asynchronous reinforcement learning (RL) for large language model (LLM) agents trains one policy on trajectories generated by another: rollouts come from stale checkpoints, and the inference engine's probabilities differ from the trainer's even at identical parameters. Standard remedies either clip importance ratios, which biases the update, or, as in GRPO, sample a group of responses per prompt, which is costly…

## 23. SWE-Game: Can Coding Agents Build the Games We Want?

- 分数：24.5  ·  HF 赞：17  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark, coding, spec
- 作者：Xiaoyu Chen, Lai Wei, Jin Wang, Xiangyu Zou, Ruochen Fan, Enze Luo, Mingzhe Yao, Jiahui Zhu, Yuhua Wen, Linghe Kong, Weiran Huang
- 链接：[arXiv](https://arxiv.org/abs/2609.33678) · [PDF](https://arxiv.org/pdf/2609.33678) · [HF](https://huggingface.co/papers/2609.33678)

We introduce SWE-Game, a benchmark of 247 tasks grounded in 41 executable reference Godot games spanning 13 gameplay categories in 2D and 3D. Five task types cover development from a brief, implementation from a game design document, skeleton completion, repair of 83 injected-fault cases, and Godot-to-Unity porting. Reference materials specify the intended gameplay, while a shared instrumentation interface lets…

## 24. AdSpark: A Large-Scale Dataset and Benchmark for Product-Centric Advertisement Video Generation

- 分数：24.5  ·  HF 赞：13  ·  来源：huggingface + arxiv
- 兴趣命中：evaluation, benchmark, spec
- 作者：Zhifei Yang, Zhao Jiang, Keyang Lu, Honghe Zhu, Zheng Zhang, Jingjing Lv, Changping Peng, Ching Law, Zhen Xiao
- 链接：[arXiv](https://arxiv.org/abs/2610.10047) · [PDF](https://arxiv.org/pdf/2610.10047) · [HF](https://huggingface.co/papers/2610.10047)

Product-centric advertisement video generation aims to create promotional videos that preserve fine-grained product identity while presenting selling points through coherent multi-shot narratives. However, this emerging task remains underexplored due to the lack of large-scale advertisement-specific datasets and comprehensive evaluation frameworks. To address this gap, we introduce \textbf{AdSpark}, a large-scale…

## 25. Taming VLAs under Robot Execution Errors: Self-Compensation and Stress Testing

- 分数：24.0  ·  HF 赞：28  ·  来源：huggingface
- 兴趣命中：benchmark
- 作者：Sohyun Lee, Yoonjae Baek, Jaesang Won, Jinnyeong Kim, Kang Hyunwoo, Seung-Hwan Baek, Ivan Laptev, Suha Kwak
- 链接：[arXiv](https://arxiv.org/abs/2609.37334) · [PDF](https://arxiv.org/pdf/2609.37334) · [HF](https://huggingface.co/papers/2609.37334)

Vision-language-action (VLA) policies often fail when a robot's executed motion deviates from their commanded action. Such execution errors arise from the robot's mechanics and operating conditions, such as wear and payload changes. We propose self-compensating VLA, a deployment-time adaptation method that enables a VLA policy to pre-compensate for the robot's execution errors when generating commands. Without task…

## 26. Agentic RAG Evaluation: Budget Allocation Across Questions, Trajectories, and Reads

- 分数：23.5  ·  HF 赞：15  ·  来源：huggingface
- 兴趣命中：agent, evaluation, spec, retrieval
- 作者：Jingjie Ning, Xueqi Li, Yibo Kong
- 链接：[arXiv](https://arxiv.org/abs/2610.05034) · [PDF](https://arxiv.org/pdf/2610.05034) · [HF](https://huggingface.co/papers/2610.05034)

Evaluation budgets in agentic retrieval-augmented generation span questions, search trajectories, and repeated answers. We measure allocation precision, reading efficiency, and cost boundaries using a retrieval-feedback comparison on HotpotQA and MuSiQue. At 34.14--34.39M model tokens, broader question coverage lowers standard error by 33\% versus five reads and 12.6\% versus three trajectories. Archived nested and…

## 27. ReSAIL: Mitigating Collapse in Iterative Agent Self-Distillation

- 分数：23.0  ·  HF 赞：26  ·  来源：huggingface
- 兴趣命中：agent
- 作者：Shengjie Jin, Hengbo Xu, Zelong Sun, YuJie Guo, Zhiwu Lu
- 链接：[arXiv](https://arxiv.org/abs/2609.39306) · [PDF](https://arxiv.org/pdf/2609.39306) · [HF](https://huggingface.co/papers/2609.39306)

Iterative self-distillation enables LLM agents to learn from successive deployments, offering a path toward recursive self-improvement (RSI). Yet our experiments with existing methods reveal a collapse in deployment performance across cycles, while task performance with privileged information (PI) also declines. We address this collapse by prioritizing informative interaction steps for distillation and preserving…

## 28. WorldSonus: Bringing Sound to Worlds

- 分数：23.0  ·  HF 赞：26  ·  来源：huggingface
- 兴趣命中：benchmark
- 作者：Pengjun Fang, Jingyi Fa, Kam Man Wu, Jiaming Wang, Haoyuan Huang, Yaguang Wu, Xiangjun Huang, Ziyang Ma, Weijia Chen, Hongyu Liu, Zeyue Tian, Qifeng Chen
- 链接：[arXiv](https://arxiv.org/abs/2610.08760) · [PDF](https://arxiv.org/pdf/2610.08760) · [HF](https://huggingface.co/papers/2610.08760)

Recent advances in world models have enabled increasingly realistic visual synthesis. However, these generated environments remain largely silent. Bringing sound to world models poses three core challenges: real-time generation to keep pace with interactive video streams, interactive control to respond to mid-stream sound instructions, and spatially aligned stereo to reflect scene geometry and camera motion. To…

## 29. Gains and Collapse in On-Policy Distillation:A Reinforcement Learning Perspective

- 分数：23.0  ·  HF 赞：18  ·  来源：huggingface
- 兴趣命中：reinforcement learning, language model, spec
- 作者：Han Cui, Jianhao Yan, Yun Luo, Hongbo Zhang, Zhizhang Fu, Yue Zhang
- 链接：[arXiv](https://arxiv.org/abs/2610.03185) · [PDF](https://arxiv.org/pdf/2610.03185) · [HF](https://huggingface.co/papers/2610.03185)

On-policy distillation (OPD) has become an important approach to language model post-training. However, despite its performance gains, OPD can also collapse into excessively long and repetitive generation, and the mechanism underlying these divergent outcomes remains poorly understood. We explain these outcomes through a reinforcement learning perspective: the teacher implicitly rewards student behaviors, even those…

## 30. Selection-Based Structured Reasoning: Toward Efficient Multimodal Search Agents

- 分数：23.0  ·  HF 赞：14  ·  来源：huggingface
- 兴趣命中：agent, reasoning, reinforcement learning, benchmark, spec
- 作者：Feiyu Gavin Zhu, Xiaoyu Zhu, Jiqi Yang, Rui Yang, Arnab Kumar Mondal, Yancheng Wang, Xinke Deng, Jean Oh, Reid Simmons, Joerg Liebelt, Xiang Kong, Zhongyu Jiang
- 链接：[arXiv](https://arxiv.org/abs/2610.01892) · [PDF](https://arxiv.org/pdf/2610.01892) · [HF](https://huggingface.co/papers/2610.01892)

Multimodal agents commonly generate free-form reasoning before each action. For small models, limited model capacity can result in lengthy reasoning that provides little useful guidance for action generation while incurring substantial inference cost. To address this challenge, we introduce Selection-based Structured Reasoning (SSR), a framework that reformulates reasoning as selection instead of open-ended…

## 31. Inverting Multi-Vector Visual Document Indices

- 分数：23.0  ·  HF 赞：14  ·  来源：huggingface + arxiv
- 兴趣命中：benchmark, language model
- 作者：Zhuchenyang Liu, Yao Zhang, Yu Xiao
- 链接：[arXiv](https://arxiv.org/abs/2610.09920) · [PDF](https://arxiv.org/pdf/2610.09920) · [HF](https://huggingface.co/papers/2610.09920)

Prevailing multi-vector visual document retrievers store each page as about a thousand patch vectors, often in vector databases run by a third party. Since no one can read a page from its vectors, this index is easily treated as less sensitive than the page. However, because the index keeps one vector per patch in raster order, and each vector is computed by a vision-language model pre-trained to read documents, we…

## 32. MiniCorp: The Last Mile of the AI Agent Firm

- 分数：22.5  ·  HF 赞：21  ·  来源：huggingface
- 兴趣命中：agent, evaluation
- 作者：Jingying Zeng, Zhenwei Dai, Jinning Li, Changho Shin, Dylan Zhang, Yuxuan Lu, Qi He, Dakuo Wang, Kai-Wei Chang
- 链接：[arXiv](https://arxiv.org/abs/2610.05912) · [PDF](https://arxiv.org/pdf/2610.05912) · [HF](https://huggingface.co/papers/2610.05912)

The last mile toward enterprise AGI is a company that runs itself. Training and adapting such agents require longitudinal enterprise data, which remain scarce, costly to acquire, and often restricted by privacy constraints. Historical archives are also frequently incomplete and record only what actually happened. They cannot show the outcomes of alternative decisions. We introduce MiniCorp, an office simulator for…

## 33. VIEScore2: Unified Image Evaluation with Spatially Grounded Explanations

- 分数：22.5  ·  HF 赞：17  ·  来源：huggingface
- 兴趣命中：evaluation, benchmark, spec
- 作者：Xianda Du, Max Ku, Weiming Ren, Zhi Rui Tam, Chunlin Ren, Ping Nie, Min-Hung Chen, Wenhu Chen
- 链接：[arXiv](https://arxiv.org/abs/2610.00994) · [PDF](https://arxiv.org/pdf/2610.00994) · [HF](https://huggingface.co/papers/2610.00994)

Existing synthetic image evaluators typically provide only a scalar quality score and do not identify the image regions that support it. We introduce VIEScore2, a unified evaluator for image generation and editing tasks with optional conditioning images. VIEScore2 represents an image as an N x N grid and jointly predicts quality scores and defect locations in a single model pass. Its text-native grid representation…

## 34. WebFovea: When the Model Is Right but the Click Is Wrong -- Reliable Round Trips for Vision-Based Web Agents on Live Websites

- 分数：22.5  ·  HF 赞：13  ·  来源：huggingface
- 兴趣命中：agent, reasoning, benchmark, language model, large language
- 作者：Jiangang Han
- 链接：[arXiv](https://arxiv.org/abs/2610.03036) · [PDF](https://arxiv.org/pdf/2610.03036) · [HF](https://huggingface.co/papers/2610.03036)

We present WebFovea, a vision-based web agent that placed 2nd in the WebRetriever Challenge 2026 with a final score of 57.0 out of 100. The challenge evaluates agents end to end on Protocol III of the WebRetriever benchmark (arXiv:2607.06118): starting from an entry URL on a live website, the agent must operate the site's own interface and return a verifiable answer. A capable multimodal large language model (LLM)…

## 35. DiffGate: Difficulty-Gated Teacher Guidance for On-Policy Distillation

- 分数：22.0  ·  HF 赞：12  ·  来源：huggingface
- 兴趣命中：reasoning, reinforcement learning, evaluation, language model, large language, spec
- 作者：Karn Tiwari, Varnith Chordia, Prathosh A P
- 链接：[arXiv](https://arxiv.org/abs/2610.04596) · [PDF](https://arxiv.org/pdf/2610.04596) · [HF](https://huggingface.co/papers/2610.04596)

On-policy distillation (OPD) has emerged as a widely used paradigm for post-training large language models, reducing the train--test mismatch of conventional distillation by supervising the student on its own generated trajectories. However, existing OPD objectives remain largely token-local and outcome-agnostic, optimizing teacher--student agreement at each prefix despite reasoning quality being determined at the…

## 36. Rationale-Guided Policy Optimization: Learning to Reason with Adaptive Rationale Scaffolding

- 分数：21.5  ·  HF 赞：11  ·  来源：huggingface
- 兴趣命中：reasoning, reinforcement learning, language model, large language
- 作者：Hoang Phan, Minh Pham, Chau Pham, Chinmay Hegde, Trung Le, Qi Lei
- 链接：[arXiv](https://arxiv.org/abs/2610.07342) · [PDF](https://arxiv.org/pdf/2610.07342) · [HF](https://huggingface.co/papers/2610.07342)

On-policy reinforcement learning has become a central paradigm for improving the reasoning abilities of large language models. However, its effectiveness is often limited by reward sparsity: when a model fails to discover correct trajectories for difficult problems, the optimization process receives little useful signal and may stagnate. Existing approaches mitigate this issue by incorporating off-policy…

## 37. AGO AI Quality Gate: Evidence-First Release Decisions for Retrieval-Augmented Generation

- 分数：20.5  ·  HF 赞：13  ·  来源：huggingface
- 兴趣命中：evaluation, benchmark, retrieval
- 作者：Giulio Zeloni, Enrico Lo Conte, Salvatore Rionero, Giuseppe Santoro, Alessandro Rastelli, Fabio Sorrentino
- 链接：[arXiv](https://arxiv.org/abs/2610.01218) · [PDF](https://arxiv.org/pdf/2610.01218) · [HF](https://huggingface.co/papers/2610.01218)

Enterprises adopting retrieval-augmented generation (RAG) face a recurring operational decision: promote, revise, or block a system version. The evidence is incomplete and the metrics come from fallible LLM judges. We report on AGO AI Quality Gate (AGO), an evidence-first quality-gate framework deployed in industrial RAG assessment engagements. AGO integrates four key components: a four-state decision model that…

## 38. Minimal Witness Reinforcement Learning

- 分数：20.5  ·  HF 赞：13  ·  来源：huggingface
- 兴趣命中：reinforcement learning, language model, large language
- 作者：T. Y. Tsui, Zihao Ye, Pengxiang Cai, Yanchao Li, Yuqiang Li, Zhehong Ai
- 链接：[arXiv](https://arxiv.org/abs/2610.07226) · [PDF](https://arxiv.org/pdf/2610.07226) · [HF](https://huggingface.co/papers/2610.07226)

``What are the irreducible conditions that are sufficient to produce an outcome?'' is one of the most common questions that recur across computation and science. Its answers, the minimal sufficient witnesses, are what we mean by explanations, mechanisms and reasons. These problems usually ask for multiple minimal witnesses, yet standard RL methods may reveal only one solution or redundant ones. We formalize this…

## 39. UltraText Bench: A Comprehensive Bilingual Benchmark for Evaluating Visual Text Rendering in Image Generation

- 分数：20.0  ·  HF 赞：12  ·  来源：huggingface
- 兴趣命中：evaluation, benchmark, language model
- 作者：Deyuan Liu, Yihao Hu, Jingxuan Zhang, Xingying Li, Jun Xie, Jiacheng Liu, Jungang Li, Yu Huang, Xuanyi Liu, Yue Ding, Zecheng Wang, Lei Zhao, Mingda Wang, Zhenglin Cheng, Peng Sun, Tao Lin
- 链接：[arXiv](https://arxiv.org/abs/2610.09823) · [PDF](https://arxiv.org/pdf/2610.09823) · [HF](https://huggingface.co/papers/2610.09823)

Dense visual text requires image generators to reproduce long strings across multiple regions with correct placement and legibility. As short-string rendering improves, evaluation must test sustained performance across more demanding scenes. We introduce UltraText Bench, a bilingual benchmark for prompt-only generation of dense visual text. It contains 432 prompts spanning 24 real-world scene categories and three…

## 40. Sherpa: Teaching LLMs to Teach Adaptively

- 分数：20.0  ·  HF 赞：8  ·  来源：huggingface
- 兴趣命中：reinforcement learning, evaluation, language model, large language, spec
- 作者：Weixian Xu, Yanzhe Zhang, Zora Zhiruo Wang, Changyu Chen, Diyi Yang
- 链接：[arXiv](https://arxiv.org/abs/2610.08778) · [PDF](https://arxiv.org/pdf/2610.08778) · [HF](https://huggingface.co/papers/2610.08778)

Large language models (LLMs) have become increasingly capable problem solvers, but being able to solve a problem is not the same as being able to teach it. Existing approaches to training LLMs as teachers rely on demonstrations, preference data, or predefined pedagogical criteria that specify what good teaching looks like. However, these signals are often not grounded in individual student learning outcomes, where…

## 41. Making LLMs Say What They Think: Measuring and Improving CoT-Interpretability Alignment

- 分数：19.5  ·  HF 赞：11  ·  来源：huggingface
- 兴趣命中：reasoning, language model, large language
- 作者：Yihuai Hong, Shauli Ravfogel, Chen Zhao, Eunsol Choi
- 链接：[arXiv](https://arxiv.org/abs/2609.38972) · [PDF](https://arxiv.org/pdf/2609.38972) · [HF](https://huggingface.co/papers/2609.38972)

Chain-of-thought (CoT) traces often serve as a proxy for how Large Language Models (LLMs) arrive at their answers. However, growing evidence shows that models' CoT often fails to reflect their internal computations and can be changed without affecting their final answers. In this work, we measure and improve the alignment between the reasoning described in an LLM's CoT and what it computes internally. We propose…

## 42. GUI-HARVEST: Self-Improving GUI Agents through Evidence-Driven Harness Evolution

- 分数：19.5  ·  HF 赞：11  ·  来源：huggingface
- 兴趣命中：agent, evaluation, spec
- 作者：Geyi Yang, Zikun Qu, Xiang Li, Zhiyong Wang, Min Zhang, Shipei Zeng, Zhongxiang Dai
- 链接：[arXiv](https://arxiv.org/abs/2610.00948) · [PDF](https://arxiv.org/pdf/2610.00948) · [HF](https://huggingface.co/papers/2610.00948)

The executable harness surrounding a GUI model determines how observations are assembled, actions are executed, and verification, recovery, and termination are controlled. Compared with harness optimization for non-GUI agents, automatically optimizing this harness poses three coupled challenges: reconciling model intent with observed visual effects, diagnosing failures under variable execution outcomes, and…

## 43. World Action Learning via Interaction-Centric Spectral Latent Guidance

- 分数：19.0  ·  HF 赞：18  ·  来源：huggingface
- 兴趣命中：spec
- 作者：Zhiming Liu, Yikun Miao, Ying Chen, Hongrui Yin, Fangqi Zhu, Xiaoyi Pang, Quanxin Shou, Zhengyang Yan, Haodong Wang, Song Guo
- 链接：[arXiv](https://arxiv.org/abs/2610.03607) · [PDF](https://arxiv.org/pdf/2610.03607) · [HF](https://huggingface.co/papers/2610.03607)

Learning general-purpose robot policies requires large-scale real-world interaction data, yet collecting robot demonstrations remains expensive and difficult to scale. Egocentric videos offer abundant human interaction experience with task-relevant semantics for robotic manipulation, but direct transfer is challenging for two reasons: latent actions inferred from frame reconstruction can be dominated by nuisance…

## 44. Mobile-4DGS: Unified Static-Dynamic Real-time Mobile Gaussian Splatting

- 分数：19.0  ·  HF 赞：14  ·  来源：huggingface
- 兴趣命中：agent, spec
- 作者：Xiaobiao Du, Beixi Hao, Zhen Fang, Tianqing Zhu, Richard Hartley, Xin Yu
- 链接：[arXiv](https://arxiv.org/abs/2610.05289) · [PDF](https://arxiv.org/pdf/2610.05289) · [HF](https://huggingface.co/papers/2610.05289)

Recent advances in 3D Gaussian Splatting (3DGS) have achieved remarkable performance in novel view synthesis, yet deploying both static and dynamic Gaussian representations on resource-constrained mobile devices remains challenging due to heavy storage, redundant primitives, and costly per-frame computation. We present Mobile-4DGS, a unified lightweight framework for high-fidelity real-time static and dynamic…

## 45. UniWAM: Unified World-Action Model

- 分数：19.0  ·  HF 赞：10  ·  来源：huggingface
- 兴趣命中：reasoning, evaluation, language model
- 作者：Jiayi Chen, Wenxuan Song, Jingbo Wang, Shuai Zhou, Xicheng Gong, Zehua Fan, Ziyang Zhou, Junwu E, Haodong Yan, Fuhao Li, Qize Yu, Xu Huang, Pengwei Wang, Wen Chen, Shunbo Zhou, Haoang Li
- 链接：[arXiv](https://arxiv.org/abs/2610.02054) · [PDF](https://arxiv.org/pdf/2610.02054) · [HF](https://huggingface.co/papers/2610.02054)

Vision-language-action models benefit from the understanding and reasoning capabilities of pretrained vision-language models, but action-only supervision provides limited grounding in world dynamics. Conversely, world-action models inherit spatiotemporal priors from video generation models, yet remain limited in semantic understanding and reasoning under distribution shifts. We introduce UniWAM, a unified…

## 46. TimeBraid: Unifying Time Series and Language for Understanding and Forecasting

- 分数：19.0  ·  HF 赞：6  ·  来源：huggingface
- 兴趣命中：reasoning, benchmark, language model, spec
- 作者：Xinyue Wang, Jiacheng Pang, Kun Zhou, Kexin Zhang, Defu Cao, Fan Feng, Faisal, Songyao Jin, Yan Liu, Biwei Huang
- 链接：[arXiv](https://arxiv.org/abs/2609.29792) · [PDF](https://arxiv.org/pdf/2609.29792) · [HF](https://huggingface.co/papers/2609.29792)

We present TimeBraid, a series of unified time-series and language models that align pretrained language models and pretrained time-series foundation models through interleaved global residual attention layers. Each model inherits knowledge, instruction following, and reasoning from one side, continuous-signal perception and zero-shot forecasting from the other, and fuses the two in a shared representation space…

## 47. Learning Multimodal Embeddings with Evidence-Aligned Readout

- 分数：19.0  ·  HF 赞：6  ·  来源：huggingface
- 兴趣命中：language model, large language, spec, retrieval
- 作者：Zirong Chen, Fuda Ye, Enjun Du, Junfu Pu, Xinlei Wang, Xinyu Zuo, Lisheng Duan, Haijin Liang, Jin Ma, Jiachuan Wang, Yongqi Zhang
- 链接：[arXiv](https://arxiv.org/abs/2609.33659) · [PDF](https://arxiv.org/pdf/2609.33659) · [HF](https://huggingface.co/papers/2609.33659)

Multimodal large language models can expose task-relevant evidence through generation, but producing useful evidence does not by itself determine how it enters a retrieval embedding. We study whether the semantic organization of that evidence can also specify where representations are read. To address this question, we introduce EviAlign, which couples Semantic Evidence Generation with Boundary Readout in a shared…

## 48. Harness-Aware Distillation for Small Language Model Agents

- 分数：19.0  ·  HF 赞：6  ·  来源：huggingface
- 兴趣命中：agent, reasoning, benchmark, language model, spec
- 作者：Moonseok Choi, Taehong Moon, Giung Nam, Juho Lee
- 链接：[arXiv](https://arxiv.org/abs/2610.02858) · [PDF](https://arxiv.org/pdf/2610.02858) · [HF](https://huggingface.co/papers/2610.02858)

Language model agents are deployed with a harness, the software around the model that manages its context, tools, and feedback. When such an agent is distilled into a smaller one, the harness stays in place, so the student mainly needs the teacher-specific abilities that the harness cannot provide, such as acting correctly on harness information. Standard distillation, however, imitates the teacher's full outputs…

## 49. Hiding Tool Latency in On-Device Cascaded Voice Agent through Speculative Execution

- 分数：19.0  ·  HF 赞：6  ·  来源：huggingface
- 兴趣命中：agent, language model, large language, spec
- 作者：Kyudan Jung, Hyunsin Park, Yoonhyung Lee, Jinhwan Park, Jinhyeok Yang, KiHyun Nam, Jaegul Choo, Jinkyu Lee
- 链接：[arXiv](https://arxiv.org/abs/2610.07641) · [PDF](https://arxiv.org/pdf/2610.07641) · [HF](https://huggingface.co/papers/2610.07641)

Tool-augmented speech assistants typically serialize automatic speech recognition, large language model inference, and external tool execution. As a result, tool latency is incurred only after the user has finished speaking and the LLM has identified the required tool calls. We present speculative tool execution for on-device cascaded voice agents, which predicts tool requests from partial ASR hypotheses and…

## 50. DAEDALUS: Bootstrapping Agent Memory from Self-Generated Tasks

- 分数：18.5  ·  HF 赞：5  ·  来源：huggingface
- 兴趣命中：agent, memory, benchmark, spec
- 作者：Antoine Edy, Max Conti, Victor Xing, Marc-Antoine Allard, Nawfal Benhamdane, Gautier Viaud
- 链接：[arXiv](https://arxiv.org/abs/2610.08048) · [PDF](https://arxiv.org/pdf/2610.08048) · [HF](https://huggingface.co/papers/2610.08048)

LLM agents often lack the operational knowledge to act reliably in new environments, as they must discover specific tool behaviors or environment conventions on their own. Without memory of past attempts, they repeat the same mistakes across tasks, leading to more task failures and longer trajectories. To address this, agentic systems typically rely on human-written guidelines or on procedural memory built from…

## 51. Towards In-Parameter Memory Augmentation for Large Language Models

- 分数：18.5  ·  HF 赞：5  ·  来源：huggingface
- 兴趣命中：agent, memory, language model, large language, coding
- 作者：Haoyu Huang, Zhongwei Xie, Jiaxin Bai, Yisen Gao, Hong Ting Tsang, Wuganjing Song, Huihao Jing, Yufei Li, Yangqiu Song
- 链接：[arXiv](https://arxiv.org/abs/2610.08630) · [PDF](https://arxiv.org/pdf/2610.08630) · [HF](https://huggingface.co/papers/2610.08630)

Recently Large Language Models (LLMs) and LLM-based agents increasingly need to incorporate knowledge acquired after pretraining, e.g., domain facts, user preferences, documents, and interaction experience. In-context learning (ICL) and ICL-based agent harness remain flexible, but they consume context capacity and incur repeated discretized encoding cost that grows with context length. In-parameter memory offers a…

## 52. RoboQuest: Generalist Physical Agents that Search, Inspect and Test

- 分数：18.5  ·  HF 赞：1  ·  来源：huggingface + arxiv
- 兴趣命中：agent, benchmark, spec
- 作者：Liu Renhang, Navonil Majumder, Tej Deep Pala, Soujanya Poria
- 链接：[arXiv](https://arxiv.org/abs/2610.10388) · [PDF](https://arxiv.org/pdf/2610.10388) · [HF](https://huggingface.co/papers/2610.10388)

Recent advances in multimodal foundation models have made them capable generalist physical agents for a range of manipulation tasks. However, successful operation in an unfamiliar environment may require an agent to seek task-relevant information through interaction when it is absent from the observations: it may need to determine where a relevant object is, inspect an unobserved property, or discover the effect of…

## 53. UNREAL: Unifying Retrieval and Long-Context with a Single Model

- 分数：18.0  ·  HF 赞：16  ·  来源：huggingface
- 兴趣命中：retrieval
- 作者：Edan Kinderman, Elad Hoffer, Yochai Blau, Brian Chmiel, Ron Banner, Daniel Soudry, Boris Ginsburg
- 链接：[arXiv](https://arxiv.org/abs/2610.08463) · [PDF](https://arxiv.org/pdf/2610.08463) · [HF](https://huggingface.co/papers/2610.08463)

Long-context inference and Retrieval-Augmented Generation (RAG) handle evidence selection at vastly different scales, from a single long prompt to an entire corpus. We ask whether a single model-internal mechanism can select evidence across this range. We introduce UNifying REtrieval And Long-Context with a Single Model (UNREAL), a model-native evidence selection framework to span corpus retrieval and long-context…

## 54. SlimWise: Decoupling Expert Pruning Across Prefill and Decode for Efficient MoE Serving

- 分数：18.0  ·  HF 赞：12  ·  来源：huggingface
- 兴趣命中：benchmark, coding
- 作者：Gunho Park, Kyoungho Jeun, Juntaek Oh, Byeongjun Shin, Baeseong Park, Minsoo Rhu
- 链接：[arXiv](https://arxiv.org/abs/2609.34117) · [PDF](https://arxiv.org/pdf/2609.34117) · [HF](https://huggingface.co/papers/2609.34117)

Mixture-of-experts (MoE) models activate few experts per token, yet batched decoding can access nearly the entire expert pool, making expert-weight traffic a major bottleneck. Expert pruning reduces this traffic, but conventional approaches also prune compute-bound prefill, sacrificing model quality for little throughput benefit. We present SlimWise, a serving framework that tailors the expert pool to each inference…

## 55. QuadTok: Quadtree Visual Tokenizer for Autoregressive Image Generation

- 分数：18.0  ·  HF 赞：8  ·  来源：huggingface + arxiv
- 兴趣命中：benchmark
- 作者：Yucheng Mao, Zeyuan Chen, Xiaojun Shan, Xiang Zhang, Divyansh Srivastava, Bingnan Li, Zhuowen Tu
- 链接：[arXiv](https://arxiv.org/abs/2610.10497) · [PDF](https://arxiv.org/pdf/2610.10497) · [HF](https://huggingface.co/papers/2610.10497)

We introduce QuadTok, a novel framework for visual tokenization and autoregressive image generation. Compared to traditional approaches using 2D grids or 1D token sequences, we propose a hierarchical quadtree structure, bridging the gap between 2D spatial binding and 1D sequence-level flexibility. The QuadTok tokenizer dynamically allocates representational capacity to visually intricate areas while leaving…

## 56. DLoop: Looped Speculative Decoding

- 分数：18.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：language model, large language, coding, spec
- 作者：Geonmo Gu, Byeongho Heo, HeeJae Jun, Yoohoon Kang, Sangmin Lee, Sangdoo Yun, Dongyoon Han
- 链接：[arXiv](https://arxiv.org/abs/2610.07659) · [PDF](https://arxiv.org/pdf/2610.07659) · [HF](https://huggingface.co/papers/2610.07659)

Speculative decoding accelerates autoregressive generation in large language models. In each drafting stage, a lightweight draft model proposes tokens that the target model subsequently verifies. With increasingly capable draft models, we find that the target model frequently accepts all tokens produced in a drafting stage. A verification nevertheless follows each drafting stage, resulting in unnecessary…

## 57. World Models' Last Exam in Physics

- 分数：18.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：evaluation, benchmark, language model, spec, planning
- 作者：Mingju Gao, Qingle Liu, Yuzhao Peng, Xinjie Lin, Ziming Qin, Zheng Jiang, Wenyi Li, Calvin Xiao, Youjie Zheng, Kaisen Yang, Qinhuai Na
- 链接：[arXiv](https://arxiv.org/abs/2610.08791) · [PDF](https://arxiv.org/pdf/2610.08791) · [HF](https://huggingface.co/papers/2610.08791)

Video world models can produce visually convincing yet physically inconsistent sequences, raising concerns about their reliability for prediction and planning in embodied AI systems. Existing evaluations often rely on model-based judgments or reference videos, while direct physical tests largely focus on mechanics. We introduce World Models' Last Exam in Physics, a measurement-based benchmark for evaluating physical…

## 58. Harness Engineering for Software Engineering via Modular Executable Dev-Primitives

- 分数：18.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：agent, reasoning, benchmark, language model, large language
- 作者：Haibo Jin, Xinjie Li, Peng Kuang, Haohan Wang
- 链接：[arXiv](https://arxiv.org/abs/2610.07832) · [PDF](https://arxiv.org/pdf/2610.07832) · [HF](https://huggingface.co/papers/2610.07832)

Large language models (LLMs) equipped with terminal access have demonstrated strong capabilities in automating software engineering tasks. However, existing agents remain brittle on long-horizon workflows, where they must repeatedly reconstruct program state scattered across source files, configurations, tests, dependencies, and runtime behavior, leading to increasingly long interaction histories, context explosion,…

## 59. From Pareto to Preference: Personalized Test-Time Scaling via Amortized Agentic Policy Discovery

- 分数：18.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：agent, reasoning, evaluation, language model, large language, spec
- 作者：Xinglin Wang, Zishen Liu, Tong Zheng, Shaoxiong Feng, Peiwen Yuan, Yiwei Li, Jiayi Shi, Yueqi Zhang, Chuyi Tan, Ji Zhang, Boyuan Pan, Kan Li
- 链接：[arXiv](https://arxiv.org/abs/2610.09684) · [PDF](https://arxiv.org/pdf/2610.09684) · [HF](https://huggingface.co/papers/2610.09684)

Test-time scaling (TTS) improves the reasoning capabilities of large language models by allocating additional inference computation. Existing approaches to improving TTS efficiency largely optimize accuracy against one resource dimension at a time, advancing either the accuracy--cost or accuracy--latency Pareto frontier. Yet user requirements are multidimensional: users may specify accuracy, latency, and…

## 60. Adaptive Latent Capacity for World Models

- 分数：17.5  ·  HF 赞：11  ·  来源：huggingface
- 兴趣命中：spec, planning
- 作者：Idan Achituve, Lior Dikstein, Idit Diamant, Arnon Netzer, Hai Victor Habi
- 链接：[arXiv](https://arxiv.org/abs/2609.32921) · [PDF](https://arxiv.org/pdf/2609.32921) · [HF](https://huggingface.co/papers/2609.32921)

We introduce Adaptive LeWorldModel (ALeWM), a world model based on a joint-embedding predictive architecture (JEPA) that learns to concentrate predictive information in compact prefixes of a wide latent representation. To encourage this ordering, ALeWM learns a sequence-conditioned distribution over prefix lengths and trains the predictor to estimate the full next embedding from a sampled input prefix. As standard…

## 61. EmbodiedSmith: Scaling Embodied Data through Recursive Self-Improvement Flywheel in Simulation

- 分数：17.5  ·  HF 赞：11  ·  来源：huggingface
- 兴趣命中：agent, evaluation
- 作者：Yikai Qin, Yifei Deng, Mingjian Liang, Wenxuan Song, Zepeng Lin, Zhiyi Jiang, Jiajun Fu, Qiao Sun, Huashuo Lei, Xicheng Gong, Jiayi Chen, Han Zhao, Shuanghao Bai, Pengxiang Ding, Pengwei Wang, Haoang Li
- 链接：[arXiv](https://arxiv.org/abs/2610.07969) · [PDF](https://arxiv.org/pdf/2610.07969) · [HF](https://huggingface.co/papers/2610.07969)

Scaling robotic foundation models requires diverse training data and reliable evaluation environments. Simulation offers a scalable solution, yet existing generation pipelines remain constrained by predefined assets and skills, a disconnect between scene generation and task generation, and limited support for complex embodiments and physics. We introduce EmbodiedSmith, a framework for scalable embodied data…

## 62. Do Language Models Need a Trainable Input Embedding Table? Fixed Minimal Token Codes at 1.7B-Class Scale

- 分数：17.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：evaluation, language model, coding, spec
- 作者：A. Bochkov
- 链接：[arXiv](https://arxiv.org/abs/2610.04002) · [PDF](https://arxiv.org/pdf/2610.04002) · [HF](https://huggingface.co/papers/2610.04002)

A trainable input embedding table assigns each vocabulary item an independently adjustable vector. We investigate whether this token-specific parameterization is required for substantial language-modeling capability, or whether a shared Transformer can learn from fixed token identities. We compare three decoder-only language models trained from scratch with the same tokenizer, contextual backbone, untied output-head…

## 63. VepAgent: Bridging Causal-Transition via Tool-Augmented Reinforcement Learning for Video Event Prediction

- 分数：17.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：agent, reasoning, reinforcement learning, evaluation, language model, large language, spec, retrieval
- 作者：Qiutong Chen, Yuchan Guo, Zhenlong Yuan, Haobo Yang, Fangfang Lin, Xinyi Long, Yin Wang, Zijian Song, Rui Lan, Shi Qiu, Boyuan Pan, Yang Luo, Yuyin Zhou
- 链接：[arXiv](https://arxiv.org/abs/2610.06293) · [PDF](https://arxiv.org/pdf/2610.06293) · [HF](https://huggingface.co/papers/2610.06293)

Multimodal Large Language Models (MLLMs) have demonstrated remarkable potential in video understanding, yet their reliance on retrospective summarization and text-centric priors often limits their ability to bridge unobserved causal transitions when applied to Video Event Prediction (VEP). To address this, we propose VepAgent, an agentic framework that integrates causal-transition reasoning with tool-augmented…

## 64. Stepped MoE: Segment-Level Routing with Configurable Inference Complexity

- 分数：17.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：memory, benchmark, language model, large language, spec
- 作者：Arnav Kundu, Zhaoyang Xu, Bairu Hou, Chang Gao, Reed Li, Tao Lei
- 链接：[arXiv](https://arxiv.org/abs/2610.07348) · [PDF](https://arxiv.org/pdf/2610.07348) · [HF](https://huggingface.co/papers/2610.07348)

Training large language models (LLMs) is resource-intensive, and adapting them for diverse deployment scenarios with varying computational constraints remains challenging. While elastic architectures enable flexible model deployment and sparsely activated models allow input-adaptive computation, existing approaches treat these dimensions independently. Moreover, models catered towards on-device edge inference need…

## 65. Judged Useless, Queried Anyway: Tool-Using Agents Rarely Turn Their Own Evidence Judgments into Stopping Decisions

- 分数：17.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：agent, memory, reasoning, retrieval
- 作者：Chubin Zhang, Zhenglin Wan, Xingrui Yu, Jingxuan Wu, Yaxin Zhou, Ivor Tsang, Bo An
- 链接：[arXiv](https://arxiv.org/abs/2610.06191) · [PDF](https://arxiv.org/pdf/2610.06191) · [HF](https://huggingface.co/papers/2610.06191)

An agent whose tool keeps returning nothing useful should stop relying on it. In a retrieval environment with controlled source failures, we separate how agents judge results from what they do. We compare stopping at the same step after longer and shorter runs of results the agent judged useless; this contrast is zero for clock- or deadline-driven stopping. Where we record their judgments, the seven agents we test…

## 66. Recurrent Looped Transformer

- 分数：17.0  ·  HF 赞：18  ·  来源：huggingface
- 兴趣命中：-
- 作者：Yifan Zhang, Jichen Feng, Shihan Qin
- 链接：[arXiv](https://arxiv.org/abs/2610.07591) · [PDF](https://arxiv.org/pdf/2610.07591) · [HF](https://huggingface.co/papers/2610.07591)

State tracking requires an update at every input, but the depth a Transformer applies to each token is fixed regardless of sequence length. We introduce the Recurrent Looped Transformer (RLT), which splits its layers between a parallel causal encoder and a recurrent decoder. At each token, the decoder merges the encoder output with the previous token's final decoder state, so the computation path grows with sequence…

## 67. NeMo-DCR: Bit-Exact Delta-Compressed Refit for Scalable Agentic RL at Trillion-Parameter Scale

- 分数：17.0  ·  HF 赞：10  ·  来源：huggingface
- 兴趣命中：agent, reinforcement learning
- 作者：Songlin Jiang, Zhiyu Li, Terry Kong, Yu Yao, Youngeun Kwon, Bernard Nguyen, Ashwath Aithal, Mario Di Francesco
- 链接：[arXiv](https://arxiv.org/abs/2610.08430) · [PDF](https://arxiv.org/pdf/2610.08430) · [HF](https://huggingface.co/papers/2610.08430)

Agentic reinforcement learning (RL) disaggregates training from rollout, so each policy update must reach the rollout clusters before the next batch. Transferring a full 1T checkpoint for such weight synchronization (refit) takes 87.5 min between two AWS regions. Measurements of BF16 training show that about 1% of weights change their stored values per step. Recent systems exploit this sparsity but fall short on…

## 68. Learning to Read the Contextual Tokens in Diffusion Transformers

- 分数：17.0  ·  HF 赞：6  ·  来源：huggingface
- 兴趣命中：language model, large language, spec
- 作者：Omer Dahary, Etai Sella, Hadar Averbuch-Elor, Daniel Cohen-Or, Or Patashnik
- 链接：[arXiv](https://arxiv.org/abs/2610.06844) · [PDF](https://arxiv.org/pdf/2610.06844) · [HF](https://huggingface.co/papers/2610.06844)

Multimodal Diffusion Transformers (MM-DiTs) jointly process visual and textual representations throughout generation. These models repeatedly update the text tokens through multimodal attention, forming dynamic contextual tokens whose function is not well understood. In this work, we introduce a framework for reading this contextual space through natural-language interrogation. We train a lightweight bottleneck…

## 69. HLA: Expressive Hybrid Linear Attention via Chunk-Wise Dynamic Mixing

- 分数：17.0  ·  HF 赞：6  ·  来源：huggingface
- 兴趣命中：memory, coding, spec
- 作者：Zhuokun Chen, Xi Lin, Xiyu Wu, Jiahao He, Jianfei Cai, Bohan Zhuang
- 链接：[arXiv](https://arxiv.org/abs/2610.05842) · [PDF](https://arxiv.org/pdf/2610.05842) · [HF](https://huggingface.co/papers/2610.05842)

Linear attention enables efficient long-context autoregressive decoding by compressing history into recurrent states, but this compression can make selective access to sparse and distant information difficult. Existing chunk-based extensions increase memory capacity, yet learned chunk-mixing coefficients may remain fixed with respect to input content and therefore cannot adapt historical access to each query. We…

## 70. DistScene: Object-to-Scene Distillation for 3D Scene Generation

- 分数：16.5  ·  HF 赞：5  ·  来源：huggingface
- 兴趣命中：evaluation, benchmark, spec
- 作者：Kunming Luo, Hongyu Yan, Ken Deng, Chengcheng Zhou, Tianyu Liu, Haipeng Li, Haibin Huang, Xuelong Li, Ping Tan
- 链接：[arXiv](https://arxiv.org/abs/2610.06960) · [PDF](https://arxiv.org/pdf/2610.06960) · [HF](https://huggingface.co/papers/2610.06960)

We present DistScene, a framework for single-image compositional 3D scene generation by jointly modeling the environment and individual objects. Unlike existing methods that represent scenes primarily as collections of objects, we model the environment as an explicit scene component to provide geometric context for object placement. Specifically, we introduce Scene-Frame Generation, which jointly generates separate…

## 71. PhysEvo: Astra Can Act, Let It

- 分数：16.5  ·  HF 赞：5  ·  来源：huggingface
- 兴趣命中：agent, evaluation, spec
- 作者：Wenqing Tian, Zeyu Zhang, Zhaocheng Liu, Fengwei Liu, Qiang Liu, Liang Wang
- 链接：[arXiv](https://arxiv.org/abs/2610.08995) · [PDF](https://arxiv.org/pdf/2610.08995) · [HF](https://huggingface.co/papers/2610.08995)

Astra can act, yet reliable manipulation depends on the system through which it observes and controls the world. We introduce PhysEvo, a framework for physical recursive self-improvement (RSI) around a single frozen model. A task agent executes robot tasks; a meta-agent uses the resulting trajectories to diagnose failures, revise tools and skills, and test corrections. The meta-agent can also improve its own…

## 72. Structuring MoE Expert Selection for Agentic Reinforcement Learning

- 分数：16.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：agent, reinforcement learning, benchmark, spec
- 作者：Bolian Li, Ting-Yao Hu, Cheng-Yu Hsieh, Sanjoy Chowdhury, Oncel Tuzel, Raviteja Vemulapalli
- 链接：[arXiv](https://arxiv.org/abs/2610.07332) · [PDF](https://arxiv.org/pdf/2610.07332) · [HF](https://huggingface.co/papers/2610.07332)

Long-horizon LLM agents are frequently implemented using sparse mixture-of-experts (MoE) models, yet the co-design of agentic behavior and MoE structures remains underexplored. In this work, we comprehensively study the connections between agentic post-training and MoE expert selection. In off-the-shelf MoE models, we observe expert selection exhibits a specialized structure that naturally aligns with agentic…

## 73. CheckerBench: Can Long-Horizon Agents Synthesize Static-Analysis Checkers?

- 分数：16.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：agent, tool use, evaluation, benchmark, coding, spec
- 作者：Hang He, Li Wang, Hao Chen, Yuchen Shao, Yuling Shi, Lisheng Wang, Peiyang Liu, Goose Lin, Zaiyuan Wang, Haiying Sun, Ting Su, Chengcheng Wan
- 链接：[arXiv](https://arxiv.org/abs/2610.07557) · [PDF](https://arxiv.org/pdf/2610.07557) · [HF](https://huggingface.co/papers/2610.07557)

Static-analysis checker synthesis requires agents to interpret a defect specification, inspect a repository, implement analyzer-specific logic, and refine the checker through repeated compilation and analysis feedback. Existing coding-agent benchmarks focus on tasks such as patch generation or vulnerability detection and rarely assess whether an agent can develop a working checker in a repository from start to…

## 74. SkillForge: Co-Evolving Skills and Agents via Dynamic Skill Lifecycles

- 分数：16.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：agent, memory, reinforcement learning, evaluation, benchmark
- 作者：Yuyao Ge, Yiwei Wang, Yuchen He, Baolong Bi, Lingrui Mei, Jiayu Yao, Lizhe Chen, Shenghua Liu
- 链接：[arXiv](https://arxiv.org/abs/2610.09832) · [PDF](https://arxiv.org/pdf/2610.09832) · [HF](https://huggingface.co/papers/2610.09832)

Memory-augmented reinforcement learning strengthens LLM agents' ability to solve complex long-horizon tasks. Skills are one such form of memory, pairing instructions with an applicability condition over task types. However, retaining every skill indiscriminately as the policy improves lets obsolete or harmful entries accumulate and mislead the agent. We propose SkillForge, an agentic RL method that compiles and…

## 75. VeriFine: Scaling Verification for Self-Improvement in Embodied Reasoning

- 分数：16.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：agent, reasoning, evaluation
- 作者：Zewei Zhou, Rachel Luo, Yulong Cao, Chaowei Xiao, Chensheng Peng, Boyi Li, Thomas Tian, Zheng Lian, Yan Wang, Jiaqi Ma, Boris Ivanovic, Marco Pavone, Wenhao Ding
- 链接：[arXiv](https://arxiv.org/abs/2610.08761) · [PDF](https://arxiv.org/pdf/2610.08761) · [HF](https://huggingface.co/papers/2610.08761)

Self-improving policies continually expose new failure patterns, changing what their judges must be able to verify. However, current fixed judges constrain both optimization feedback and the discovery of useful training examples, limiting further self-improvement. This challenge is even more acute in embodied reasoning, where reliable evaluation must account for spatial grounding, causal reasoning, and safety-aware…

## 76. ALIVE: Interaction-Aligned Object Insertion for First-Frame-Guided Video Editing

- 分数：16.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：benchmark, language model, spec
- 作者：Zhenghong Zhou, Zhe Lin, Jiebo Luo, Yuqian Zhou
- 链接：[arXiv](https://arxiv.org/abs/2610.08779) · [PDF](https://arxiv.org/pdf/2610.08779) · [HF](https://huggingface.co/papers/2610.08779)

Current video editors can insert objects but often struggle to make them participate in interactions such as being picked up or manipulated. We introduce ALIVE, a framework that makes inserted objects "alive" through coherent interactions with the source video's contents, using an edited first frame and an instruction naming only the added object. We curate 35,800 editing pairs combining 3D-rendered,…

## 77. Rethinking World-Action Model for Compositional and In-Context Robotic Manipulation

- 分数：16.0  ·  HF 赞：0  ·  来源：huggingface
- 兴趣命中：reasoning, benchmark, spec, planning
- 作者：Shukai Gong, Xuanran Zhai, Yintianrun Zhang, Ruopeng Cui, Ye Huang, Yiyang Fu, Dexuan Lyu, Chaojie Li, Xinyi Song, Peiwen Lin, Chuang Wang, Mingyuan Jia, Yufan Deng, Jiaxin Fang, Bo Liang, Jiaxin Li, Yuxiang Gao, Hao Liu, Daquan Zhou
- 链接：[arXiv](https://arxiv.org/abs/2610.02368) · [PDF](https://arxiv.org/pdf/2610.02368) · [HF](https://huggingface.co/papers/2610.02368)

Long-horizon compositional manipulation has become increasingly important for real-world robot deployment, where a single task involves multiple coordinated subtasks. Existing world-action models (WAMs) jointly predict short-horizon visual futures and actions, but typically lack explicit subtask-level reasoning. We propose Visual Goal-conditioned Action Reasoning (ViGAR), a hierarchical framework that factorizes…

## 78. On-Policy Distillation with Negative-Policy Rollouts

- 分数：15.5  ·  HF 赞：11  ·  来源：huggingface
- 兴趣命中：reasoning
- 作者：Jaehui Hwang, Dongyoon Han, Sangdoo Yun, Byeongho Heo
- 链接：[arXiv](https://arxiv.org/abs/2610.07874) · [PDF](https://arxiv.org/pdf/2610.07874) · [HF](https://huggingface.co/papers/2610.07874)

On-policy distillation (OPD) has been widely studied as a post-training method in which a student model obtains token-level supervision from a stronger teacher on its own rollouts. Recent studies have improved OPD through alternative distillation reward formulations and teacher configurations, while the objective of distillation remains centered on mimicking the teacher. However, when a stronger teacher has limited…

## 79. RLHND: Video Foundation Models as Physically Grounded Hand Trackers for Robot Learning

- 分数：15.5  ·  HF 赞：11  ·  来源：huggingface
- 兴趣命中：benchmark
- 作者：Seungjun Moon, Subin Jeon, Sangwoo Kim, Hanbyul Joo, Jinwoo Shin
- 链接：[arXiv](https://arxiv.org/abs/2610.09455) · [PDF](https://arxiv.org/pdf/2610.09455) · [HF](https://huggingface.co/papers/2610.09455)

Recently, approaches that leverage human video datasets for robot policy training have become increasingly prevalent. However, most existing hand trackers regress pose from cropped frames with limited priors on hand motion and object interaction, resulting in inaccurate and physically inconsistent estimates. Moreover, the lack of physical cues, e.g., contact and force, limits the use of human videos for robot policy…

## 80. Understanding and Enhancing Backdoor Persistency in LLM Agent Post-Training

- 分数：15.0  ·  HF 赞：6  ·  来源：huggingface
- 兴趣命中：agent, reinforcement learning
- 作者：Qiusi Zhan, Nian Lyu, Stephanie Ding, Arnav Mehta, Xander Davies, Daniel Kang
- 链接：[arXiv](https://arxiv.org/abs/2610.07510) · [PDF](https://arxiv.org/pdf/2610.07510) · [HF](https://huggingface.co/papers/2610.07510)

Developers can build LLM agents by adapting third-party models through benign post-training. We study a supply-chain threat in which an attacker supplies a model with a backdoor: hidden behavior that produces malicious outputs when a particular input pattern appears. Focusing on software-engineering agents, we ask whether such backdoors survive the developer's supervised fine-tuning (SFT) and subsequent task-level…

## 81. We Query, Therefore We Compute: On Oracle Computation beyond the Machine, with an Application to Agents

- 分数：15.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：agent, language model, large language
- 作者：Kefan Liu, Fengning Ou, Yelin Luo, Jingdi Lei
- 链接：[arXiv](https://arxiv.org/abs/2610.09243) · [PDF](https://arxiv.org/pdf/2610.09243) · [HF](https://huggingface.co/papers/2610.09243)

Agentic systems use large language models (LLMs) to carry out concrete tasks. Prior work often borrows abstractions such as scheduling, caching or isolation piecemeal from operating systems, so the mechanisms it builds share little common ground, and the shared view of the two forms of agentic system, Workflows and Agents, is limited. We construct an abstract machine that provides both.   We treat the LLM as an…

## 82. ConEx: Human-Interpretable Saliency Maps via Concept-Aware Attribution

- 分数：14.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：reasoning, benchmark, spec
- 作者：Yehonatan Elisha, Oren Barkan, Ziv Weiss Haddad, Noam Koenigstein
- 链接：[arXiv](https://arxiv.org/abs/2610.04605) · [PDF](https://arxiv.org/pdf/2610.04605) · [HF](https://huggingface.co/papers/2610.04605)

Many visual explanation methods in computer vision highlight pixel importance but struggle to link these low-level cues to semantically meaningful concepts, limiting their interpretability and trustworthiness. We introduce Concept-based Explanations (ConEx), a novel framework that bridges saliency visualization with concept-based reasoning to provide both faithfulness and interpretability. ConEx automatically…

## 83. Technical Report on the Turba Fertilizer Machine Learning Stack in Morocco

- 分数：14.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：benchmark, spec, retrieval
- 作者：Abdelghani Belgaid, Zakaria Mahmoud, Fahd Chibani, Oumnia Ennaji, Younes Boudoul, Dounia Rachid
- 链接：[arXiv](https://arxiv.org/abs/2610.05949) · [PDF](https://arxiv.org/pdf/2610.05949) · [HF](https://huggingface.co/papers/2610.05949)

Site-specific fertilizer recommendation systems adapt nutrient advice to location, soil properties, crop type, and production targets, but scientific reuse is constrained when recommendation functions remain accessible mainly through interactive interfaces, outputs are not versioned, and trained approximations cannot be independently loaded or benchmarked. This technical report presents the Turba fertilizer machine…

## 84. Multilinguality in Hybrid Attention LLMs

- 分数：14.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：agent, reasoning
- 作者：Lucas Bandarkar, Junlin Hu, Chenyuan Yang, Mohsen Fayyaz, Nanyun Peng
- 链接：[arXiv](https://arxiv.org/abs/2609.35378) · [PDF](https://arxiv.org/pdf/2609.35378) · [HF](https://huggingface.co/papers/2609.35378)

In response to the growing demand for long sequences in agentic and reasoning use cases, many state-of-the-art LLMs combine multiple variants of attention to mitigate the quadratic complexity of traditional softmax attention. These hybrid attention LLMs aim to balance the strengths and limitations of full attention and alternatives based on recurrence. This work presents a first study of how hybrid attention impacts…

## 85. Personal-Agent Mediated Recommendation with Cross-Platform User History

- 分数：14.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：agent, benchmark
- 作者：Yu Xia, Jiangfan Zhang, Jun Xiao, Julian McAuley, Xiangjun Fan
- 链接：[arXiv](https://arxiv.org/abs/2610.07588) · [PDF](https://arxiv.org/pdf/2610.07588) · [HF](https://huggingface.co/papers/2610.07588)

Modern recommendation is shifting from platform-centric personalization toward user-governed personalization, where a personal LLM agent can act on the user's behalf across services. We formalize this emerging paradigm as Personal-Agent Mediated Recommendation: a platform recommender ranks a candidate set using platform-local information, and a personal agent uses user-authorized cross-platform history to mediate…

## 86. HiPLEX: Hierarchical Policy Factorization for Full Duplex Speech Language Models

- 分数：14.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：reinforcement learning, language model
- 作者：Kyudan Jung, Hyunsin Park, Yoonhyung Lee, Jinhwan Park, Jinhyeok Yang, KiHyun Nam, Jaegul Choo, Jinkyu Lee
- 链接：[arXiv](https://arxiv.org/abs/2610.07727) · [PDF](https://arxiv.org/pdf/2610.07727) · [HF](https://huggingface.co/papers/2610.07727)

As human--AI interactions become more conversational, full-duplex speech language models capable of natural real-time dialogue are growing in importance. Beyond generating appropriate responses, these models must coordinate turn-taking, backchanneling, and floor management in real time. Reinforcement learning (RL) provides a way to refine these behaviors through direct feedback on interaction outcomes. However,…

## 87. JumpStart Your Policy Learning with Lessons from 160,000 Training Runs

- 分数：14.0  ·  HF 赞：0  ·  来源：huggingface
- 兴趣命中：evaluation, benchmark, spec
- 作者：Nabil Omi, Eric Bae, Chung Yik Edward Yeung, Siddhartha Sen, Ali Farhadi
- 链接：[arXiv](https://arxiv.org/abs/2609.13730) · [PDF](https://arxiv.org/pdf/2609.13730) · [HF](https://huggingface.co/papers/2609.13730)

Reliable progress in offline policy learning depends on careful reporting, well-tuned baselines, and evaluation across diverse conditions. Prior work has shown that results can be sensitive to reporting choices, hyperparameter tuning, and dataset properties, but these sources of variability have not been systematically investigated together at the scale needed to understand how they shape conclusions. To address…

## 88. Internalizing Agent Experience into Diffusion Model Weights via On-Policy Context Distillation

- 分数：14.0  ·  HF 赞：0  ·  来源：huggingface
- 兴趣命中：agent, memory, benchmark
- 作者：Wenxuan Wang, Zekai Liu, Weinan Zhang, Yu Cheng, Yang Yang
- 链接：[arXiv](https://arxiv.org/abs/2610.07250) · [PDF](https://arxiv.org/pdf/2610.07250) · [HF](https://huggingface.co/papers/2610.07250)

Wrapping an image generation model in an agentic harness can effectively boost Text-to-Image task performance: the harness can leverage memory, skills, workflow orchestration, result verification, and iterative refinement to continually construct and revise prompts, thereby eliciting better images. These gains, however, remain external to the diffusion model and are realized only while the full harness runs. We…

## 89. DiVeR: Decision-Critical Verifier Learning for VLA Test-Time Scaling

- 分数：13.0  ·  HF 赞：10  ·  来源：huggingface
- 兴趣命中：-
- 作者：Seongheon Park, Heecheol Kim, Shulin Tian, Lilika Makabe, Namiko Saito, Katsushi Ikeuchi, Sharon Li, Yasuyuki Matsushita
- 链接：[arXiv](https://arxiv.org/abs/2610.04933) · [PDF](https://arxiv.org/pdf/2610.04933) · [HF](https://huggingface.co/papers/2610.04933)

Scaling robot data and model capacity has improved Vision-Language-Action (VLA) policies, but further progress is constrained by the high cost of robotic data. Verifier-guided test-time scaling offers an efficient alternative by sampling multiple action candidates and selecting the one most likely to lead to task success at inference time. Existing classification-based verifiers learn from trajectory-level outcomes…

## 90. AdvSim2Real : Training Web Agents Against Adaptive Prompt Injection in a Web World Model

- 分数：13.0  ·  HF 赞：6  ·  来源：huggingface
- 兴趣命中：agent
- 作者：Sarim Hashmi, Mukul Ranjan, Kshitij Mishra, Mikhail Kuznetsov, Praneeth Vepakomma, Nils Lukas
- 链接：[arXiv](https://arxiv.org/abs/2610.08773) · [PDF](https://arxiv.org/pdf/2610.08773) · [HF](https://huggingface.co/papers/2610.08773)

Web agents complete user requests by reading and acting on pages that third parties write, so an instruction planted on a page can redirect the agent away from the user's goal. The agent cannot simply ignore the page, because the page also holds the values and controls the task requires. Current defenses fine-tune the agent on injections fixed before training, and attackers that adapt to the trained model bypass…

## 91. MEND: RL For Flow Models via Proximal Velocity Matching

- 分数：13.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：reinforcement learning, spec
- 作者：Shreshth Saini, Neil Birkbeck, Yilin Wang, Balu Adsumilli, Alan C. Bovik
- 链接：[arXiv](https://arxiv.org/abs/2610.05954) · [PDF](https://arxiv.org/pdf/2610.05954) · [HF](https://huggingface.co/papers/2610.05954)

Reward post-training of flow models either reweights the model's own samples under a KL penalty or a frozen reference, often for thousands of updates, or backpropagates the reward and moves every sample without checking that the move is worth its size. We introduce MEND, a reinforcement learning method built on proximal velocity matching. MEND caps rewards within each prompt group, so samples that already score well…

## 92. A Safe Action Is Not Enough: Feasible-Future Decoding for Vision-Language-Action Policies

- 分数：13.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：evaluation, coding
- 作者：Tu Nguyen, Matthieu Zimmer, Vu Anh Vu, Ziyi Wang, Jannik Hammel Nielsen, Xuebing Zhou, Haitham Bou Ammar
- 链接：[arXiv](https://arxiv.org/abs/2610.05166) · [PDF](https://arxiv.org/pdf/2610.05166) · [HF](https://huggingface.co/papers/2610.05166)

A safe action is not necessarily a viable one. A frozen vision-language-action (VLA) policy can favor a locally admissible move that leaves no policy-supported route to safe task completion. We call this the feasibility-likelihood gap: likelihood ranks the next move, while feasibility depends on the futures it leaves open.   To bring those futures into the decision, we derive the exact next-block marginal of the…

## 93. OPD Before RL: Warm-Starting Rubric-Based RL with On-Policy Distillation

- 分数：12.5  ·  HF 赞：5  ·  来源：huggingface
- 兴趣命中：reinforcement learning
- 作者：Xinpeng Wang, Wei Shi, Yu-Chia Chen, Maria Zontak, Yun He, Richard Yuanzhe Pang
- 链接：[arXiv](https://arxiv.org/abs/2610.02781) · [PDF](https://arxiv.org/pdf/2610.02781) · [HF](https://huggingface.co/papers/2610.02781)

Many useful language-model tasks cannot be evaluated by exact outcome verification. Rubric-based reinforcement learning (RL) addresses this issue by scoring open-ended responses against explicit criteria. However, because the reward is assigned after the complete response, the training signal does not directly identify which individual decisions contributed to the final score. We propose a two-stage training…

## 94. Improving Proactive AI Assistance with Hierarchical Procedural Understanding

- 分数：12.5  ·  HF 赞：5  ·  来源：huggingface
- 兴趣命中：evaluation
- 作者：Jin-Seop Lee, TaeYeon Won, SeongJun Jung, JungHoon Kim, Boyang Albert Li, JinYeong Bak, Jaehong Yoon, Jee-Hyong Lee
- 链接：[arXiv](https://arxiv.org/abs/2610.06505) · [PDF](https://arxiv.org/pdf/2610.06505) · [HF](https://huggingface.co/papers/2610.06505)

Proactive AI assistants continuously observe a user's activity and decide whether to provide new guidance or remain silent. They should provide appropriate guidance for the task, determine when to provide the next guidance based on task progress, and adjust the guidance level to the user's expertise and needs. Supporting these capabilities requires training and evaluation data that reflect procedural structure and…

## 95. DeCoPrune: Efficient KV-Cache Pruning for Autoregressive Video Diffusion via Denoising Consistency

- 分数：12.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：benchmark, spec
- 作者：Zeqi Xiao, Qingle Liu, Kaiwen Zhang, Yifan Zhou, Zihan Ding, Xingang Pan
- 链接：[arXiv](https://arxiv.org/abs/2609.39096) · [PDF](https://arxiv.org/pdf/2609.39096) · [HF](https://huggingface.co/papers/2609.39096)

Autoregressive video diffusion supports streaming generation and interactive control, but its KV cache grows continuously with the generated history. Existing compression strategies either discard history using fixed windows or select tokens through local attention and similarity signals, which do not directly measure whether the current chunk contributes information beyond the retained context. We introduce…

## 96. Conditional Trajectory Peaks: Single-Pass Multimodal Policies over Action Chunks

- 分数：12.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：spec, planning
- 作者：Di Wu, Rongtian Shen, Ping Liu, Xuhua Chen, He Zheng, Lingfeng Zhang, Tao Zhang
- 链接：[arXiv](https://arxiv.org/abs/2610.06104) · [PDF](https://arxiv.org/pdf/2610.06104) · [HF](https://huggingface.co/papers/2610.06104)

Multimodal imitation learning requires diverse executable futures under the same observation and consistent behavior across replanning cycles. We present Conditional Trajectory Peaks (CTP), a single-pass policy framework that jointly predicts complete action-chunk candidates, probability masses, and trajectory scales. Distribution-Aware Peak Specialization (DAPS) specializes trajectory peaks using trajectory-level…

## 97. WildMatch: Weakly Supervised Image Matcher Adaptation for Wildlife Re-Identification

- 分数：12.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：spec, retrieval
- 作者：Turhan Can Kargin, Piotr Kubaty, Ekaterina Rostovskaya, Izabela Wierzbowska, Bartosz Zieliński, Marcin Przewięźlikowski
- 链接：[arXiv](https://arxiv.org/abs/2610.07384) · [PDF](https://arxiv.org/pdf/2610.07384) · [HF](https://huggingface.co/papers/2610.07384)

Individual animal re-identification from camera-trap imagery is an instance retrieval problem central to non-invasive wildlife monitoring: a query image must retrieve the correct individual from a reference set of known animals. This requires computer vision models to recognize distinctive local patterns in fur, skin, or other visual markings. Current approaches either learn global embeddings as a classification…

## 98. Sensor-Language-Action Models

- 分数：12.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：benchmark, spec
- 作者：Yuekai Xu, Zitao Shuai, Yuzhe Yang
- 链接：[arXiv](https://arxiv.org/abs/2610.08244) · [PDF](https://arxiv.org/pdf/2610.08244) · [HF](https://huggingface.co/papers/2610.08244)

Sensors are useful not only for understanding the world but also for deciding what to do next. Existing sensor models however largely stop at perception: they recognize states or predict outcomes, leaving actions modeled separately through task-specific and often closed label spaces. We introduce Sensor-Language-Action (SLA) modeling, a framework that connects multimodal sensor observations, natural language, and…

## 99. Learning Functional Subspaces for Neural Network Compression

- 分数：12.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：memory
- 作者：Massimo Bini, Anders Christensen, Stephan Alaniz, Judah Goldfeder, Ole Winther, Yann LeCun, Ravid Shwartz-Ziv, Zeynep Akata
- 链接：[arXiv](https://arxiv.org/abs/2609.40127) · [PDF](https://arxiv.org/pdf/2609.40127) · [HF](https://huggingface.co/papers/2609.40127)

Modern transformers pair impressive capabilities with substantial memory and compute demands. Low-rank weight factorization reduces both while keeping the matrices dense, and thus efficient on standard hardware. Existing methods, however, choose the subspace to remove from each weight matrix with local closed-form criteria: activation energy, layer-wise reconstruction error, or a quadratic approximation of the loss.…

## 100. Attacca: Goal-Directed Control under State Continuity for Long-Horizon Embodied Agents

- 分数：12.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：agent
- 作者：Gyusik Seo, Jaehong Yoon
- 链接：[arXiv](https://arxiv.org/abs/2610.07785) · [PDF](https://arxiv.org/pdf/2610.07785) · [HF](https://huggingface.co/papers/2610.07785)

A central capability of embodied agents is to accomplish complex objectives through sequences of interdependent tasks. Yet existing visual goal-conditioned policies underlying these agents are typically evaluated on isolated interactions where the target is already visible, and thus do not capture the conditions that arise during continuous long-horizon task execution. In such settings, each task begins from the…

## 101. Co-Evolving Robot Orchestrators and Policies through Deployment

- 分数：12.0  ·  HF 赞：0  ·  来源：huggingface
- 兴趣命中：agent, language model
- 作者：Xilun Zhang, Maggie Wang, Erik Bauer, Hong-Xing Yu, Huang Huang, Jiajun Wu, Marco Pavone
- 链接：[arXiv](https://arxiv.org/abs/2610.09228) · [PDF](https://arxiv.org/pdf/2610.09228) · [HF](https://huggingface.co/papers/2610.09228)

Vision-language-action (VLA) policies trained on large datasets are capable within their training domains, yet they still fail to generalize to the variety of situations a robot meets in real-world deployment. Agentic robot systems complement the policy with a vision-language model (VLM) orchestrator that learns when to call the policy, how to instruct it, and when to use scripted skills instead. However, because…

## 102. JLD: Perceptual Distance Through A Jacobian Lens

- 分数：11.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：spec
- 作者：Shreshth Saini, Balu Adsumilli, Alan C. Bovik
- 链接：[arXiv](https://arxiv.org/abs/2610.05967) · [PDF](https://arxiv.org/pdf/2610.05967) · [HF](https://huggingface.co/papers/2610.05967)

Image compression, restoration, and generation all require a way to measure how different two images look to a person. Pixel error ignores how people see, while the most accurate perceptual distances are typically fitted to human judgments, tying them to a fixed data and resolution. For example, when image resolution is doubled, the correlation of DISTS with human scores on TID2013 drops from 0.815 to 0.717. We…

## 103. Kinematic MeanFlow: One-Step Action Generation Policy for Robotic Foundation Models

- 分数：11.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：spec
- 作者：Jiawei Fan, Sifeng Wang, Yuqing Hou, Anbang Yao
- 链接：[arXiv](https://arxiv.org/abs/2610.00864) · [PDF](https://arxiv.org/pdf/2610.00864) · [HF](https://huggingface.co/papers/2610.00864)

In this paper, we study how to achieve one-step action generation in Robotic Foundation Models (RFMs), aiming to overcome the high inference latency of multi-step flow matching. MeanFlow provides a promising framework for this goal, yet its direct application leads to performance collapse. We discover that this stems from two distinctive dynamics exhibited in the RFM velocity field: (1) the ``local acceleration"…

## 104. DMAD: Distribution Matching as Adversarial Distillation for Fast Visual Generation

- 分数：10.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：memory
- 作者：Zhengming Yu, Junkun Yuan, Haotian Yang, Gordon Guocheng Qian, Yizhi Wang, Angtian Wang, Yiding Yang, Bo Liu, Xin Li, Wenping Wang, Chongyang Ma
- 链接：[arXiv](https://arxiv.org/abs/2610.02188) · [PDF](https://arxiv.org/pdf/2610.02188) · [HF](https://huggingface.co/papers/2610.02188)

Distribution Matching Distillation (DMD) trains a few-step student from the difference between separately estimated target and student scores, so it must keep an auxiliary diffusion model fitted to the student's evolving distribution at extra memory and computation cost. We introduce DMAD, Distribution Matching as Adversarial Distillation, which recasts distribution matching as classification and learns the required…

## 105. Cross-Lingual Alignment for Decoder-Only Models using MoE Routers

- 分数：10.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：evaluation
- 作者：Lucas Bandarkar, Clark Peng, Ahmed Haj Ahmed, Aditi Khandelwal, Nanyun Peng
- 链接：[arXiv](https://arxiv.org/abs/2610.01921) · [PDF](https://arxiv.org/pdf/2610.01921) · [HF](https://huggingface.co/papers/2610.01921)

Cross-lingual contrastive learning has been a core component of multilingual encoder training, but the ability to explicitly align representations is not possible in decoder-only LLMs because of varying multilingual tokenization. However, a growing amount of research suggests that even in LLMs, higher cross-lingual representational alignment leads to improved cross-lingual transfer. In this paper, we propose a novel…

## 106. Toward Real-Time VLAs: Stage-Aware Two-Step Flow Denoising and System-Level Evaluation

- 分数：10.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：evaluation
- 作者：Di Wu, Rongtian Shen, Ping Liu, Yan Shen, Zhenhan Yin, Shun Zuo, Xuhua Chen, He Zheng, Lingfeng Zhang, Jianglin Zhang, Tao Zhang
- 链接：[arXiv](https://arxiv.org/abs/2609.39822) · [PDF](https://arxiv.org/pdf/2609.39822) · [HF](https://huggingface.co/papers/2609.39822)

Vision-language-action (VLA) models face a timing gap between low-rate inference and high-rate robot execution. We characterize this gap through end-to-end latency measurements of model inference and the robot execution chain. Repeated Flow Matching denoising contributes substantially to inference cost, while robot-side delays mainly arise from perception acquisition, communication scheduling, and physical response.…

## 107. Execution-Aligned Progressive Noise for Consistent Asynchronous Replanning in Generative Robot Policies

- 分数：10.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：planning
- 作者：Di Wu, Ping Liu, Xuhua Chen, He Zheng, Lingfeng Zhang, Tao Zhang
- 链接：[arXiv](https://arxiv.org/abs/2610.06090) · [PDF](https://arxiv.org/pdf/2610.06090) · [HF](https://huggingface.co/papers/2610.06090)

Continuous asynchronous replanning is essential for real-time generative robot policies, but independent stochastic initialization can cause mode switching and inconsistent continuation across action chunks. We propose Execution-Aligned Progressive Noise (EAPN), which introduces structured stochasticity at both inter-chunk and intra-chunk levels. Across replanning steps, EAPN propagates a shared noise trajectory and…

## 108. CtrlCache: Accelerating Interactive Video World Models with Control-Aware Caching

- 分数：10.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：spec
- 作者：Shangye Song, Dong Gong, Hong Jia, Yun Sing Koh, Xinyu Zhang
- 链接：[arXiv](https://arxiv.org/abs/2610.08777) · [PDF](https://arxiv.org/pdf/2610.08777) · [HF](https://huggingface.co/papers/2610.08777)

Interactive video world models need to generate each video chunk efficiently while responding faithfully to user controls. Many systems use chunk-wise autoregressive generation with few-step denoising, but each chunk still requires several costly denoising iterations. Training-free caching can reduce this cost, yet existing policies make reuse decisions primarily from model-internal denoising dynamics and do not…

## 109. Accent Analogy Guidance: More Speaker Similarity at Equal Accent in Cross-Lingual Voice Cloning

- 分数：10.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：-
- 作者：Yoomee Cho, Jisun Lee
- 链接：[arXiv](https://arxiv.org/abs/2609.29123) · [PDF](https://arxiv.org/pdf/2609.29123) · [HF](https://huggingface.co/papers/2609.29123)

In cross-lingual zero-shot text-to-speech, the accent of the reference leaks into the target speech. We propose accent analogy guidance (AAG), a training-free sampler term that subtracts an accent direction estimated from the model's own predictions for one synthetic voice rendered in both languages, so the voice cancels and only the accent remains. By a blind LLM accent judge on real dubbing data, reweighting…

## 110. Building Rome from a Single Image

- 分数：10.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：-
- 作者：Jiraphon Yenphraphai, Fang Li, Tianshuo Xu, Depu Meng, Quentin Herau, Yihan Hu, Raymond A. Yeh, Wei Zhan
- 链接：[arXiv](https://arxiv.org/abs/2610.08790) · [PDF](https://arxiv.org/pdf/2610.08790) · [HF](https://huggingface.co/papers/2610.08790)

Single-image scene generation aims to produce a complete 3D scene mesh from a single image, including surfaces the camera did not observe. While pretrained 3D object generators encode a strong shape prior, they are mainly designed for isolated objects in a fixed canonical volume and focus mostly on indoor scenes, since diverse 3D data for outdoor scenes are quite limited. In this work, we present a method that…

## 111. Learning Discriminative Geometry for Drifting Models

- 分数：9.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：-
- 作者：Doudou Zhang, Wenwen Hou, Yilin Chen, Qi Chen
- 链接：[arXiv](https://arxiv.org/abs/2610.04703) · [PDF](https://arxiv.org/pdf/2610.04703) · [HF](https://huggingface.co/papers/2610.04703)

Recently proposed Drifting Models shift iterative distribution refinement from inference to training, enabling effective one-step generation. However, their performance on complex image datasets depends strongly on the representation used to construct the drifting field: pixel-space drifting performs poorly, whereas pretrained feature spaces substantially improve sample quality for reasons that remain unclear. We…

## 112. Constrained-Action AI Remediation for SIEM/XDR via a NeMo-Guardrails Proxy

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reasoning, language model, large language, spec
- 作者：Georgios Koutidis, Nikolaos Kekatos, Tom Nianios, Alexios Lekidis
- 链接：[arXiv](https://arxiv.org/abs/2610.09906) · [PDF](https://arxiv.org/pdf/2610.09906) · [HF](https://huggingface.co/papers/2610.09906)

Security Operations Centers (SOCs) for information technology and operational technology share one incident-response problem: a flood of correlated alerts and too few analysts. Large Language Models (LLMs) are increasingly proposed as reasoning engines that triage alerts and, in autonomous deployments, issue commands that block IPs, kill processes, or quarantine files on production hosts. This coupling introduces a…

## 113. RollVerify: Bridging Efficiency and Accuracy in Long-Tail Rollout Reinforcement Learning

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：context window, reasoning, reinforcement learning, language model, large language, spec
- 作者：Yongqiang Yao, Jinru Tan, Kaihuan Liang, Zixin Yin, Yazhe Niu, Ruihao Gong, Dahua Lin, Ningyi Xu
- 链接：[arXiv](https://arxiv.org/abs/2610.09914) · [PDF](https://arxiv.org/pdf/2610.09914) · [HF](https://huggingface.co/papers/2610.09914)

Reinforcement learning is crucial for improving large language models' reasoning and generalization. It relies on massive rollouts whose lengths become increasingly long-tailed as context windows grow. In on-policy training, these long-tail rollouts can result in GPU bubbles, reducing system utilization and limiting RL scalability. Asynchronous or partial-rollout methods improve throughput by relaxing…

## 114. Purifying Backdoored Large Vision-Language Models by Removing Hijacked Directions

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, language model, coding, spec
- 作者：Bojun Yang, Haochen Zhou, Zhifang Zhang, Haobo Wang, Songze Li, Lei Feng
- 链接：[arXiv](https://arxiv.org/abs/2610.09941) · [PDF](https://arxiv.org/pdf/2610.09941) · [HF](https://huggingface.co/papers/2610.09941)

Large vision-language models (LVLMs) are increasingly deployed in safety-critical applications, yet they remain vulnerable to backdoor attacks. Defending against such attacks remains costly, as existing methods require either extensive retraining on clean data or per-query intervention at inference time. To address this limitation, we propose OrthoPurify, a more efficient method to purify backdoored model weights…

## 115. AgentTime: Can Agents Estimate and Control Their Own Runtime?

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, evaluation, benchmark, coding, spec
- 作者：Michael Ofengenden, Maksym Andriushchenko
- 链接：[arXiv](https://arxiv.org/abs/2610.09944) · [PDF](https://arxiv.org/pdf/2610.09944) · [HF](https://huggingface.co/papers/2610.09944)

An essential control of AI agents is their ability to manage runtime. This ability requires a sense of time-awareness, to predict and estimate wall-clock time and to control their own actions. Prior work has focused on time-awareness, but duration-following and control in native agent harnesses remain unexplored. We present AgentTime, a benchmark for testing whether agents can work for a requested duration, predict…

## 116. Marrying Pricing and Advertising with LLMs

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, language model, large language
- 作者：Alessandro Barro, Francesco Bacchiocchi, Francesco Emanuele Stradi, Alberto Marchesi
- 链接：[arXiv](https://arxiv.org/abs/2610.09985) · [PDF](https://arxiv.org/pdf/2610.09985) · [HF](https://huggingface.co/papers/2610.09985)

We study a sequential pricing problem in which a seller jointly posts a price and an advertisement generated by a large language model (LLM). The seller aims to maximize revenue under an unknown product demand that depends on both decisions, while observing only whether each offer leads to a purchase. We propose an online actor-critic algorithm that combines low-rank adaptation (LoRA) of a pretrained LLM with a…

## 117. Efficient Patch-Based Anomaly Detection Fused with Diffusion Driven Generative Modeling for Semiconductor Wafer Bin Map Open Set Anomaly Detection

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, evaluation, benchmark, spec
- 作者：Limon Bin Hossain, Md Sadib Rahman Ananta
- 链接：[arXiv](https://arxiv.org/abs/2610.09993) · [PDF](https://arxiv.org/pdf/2610.09993) · [HF](https://huggingface.co/papers/2610.09993)

Spatial defect signatures on wafer bin maps (WBMs) trace yield loss to specific process faults, yet supervised classifiers recognize only the defect types seen during training, and one-class detectors built on a single mechanism tend to capture either local structural deviations or global distributional violations, but rarely both. This work proposes a hybrid one-class framework that couples a patch-based…

## 118. Learning to Accumulate Knowledge with Mutual Information

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reinforcement learning, language model, large language, spec
- 作者：Yuyang Zhao, Lizi Liao, Leyang Shen, Xiaoyan Zhao, Yang Zhang, Fuli Feng, Xiangnan He
- 链接：[arXiv](https://arxiv.org/abs/2610.10042) · [PDF](https://arxiv.org/pdf/2610.10042) · [HF](https://huggingface.co/papers/2610.10042)

Large language model (LLM) agents can improve their performance by reusing knowledge distilled from past interactions. However, curating new experiences into a knowledge bank that becomes more useful as it grows remains challenging. Effective knowledge accumulation should limit redundant overlap among entries and ensure that new knowledge contributes beyond what the bank already provides. Yet training a curator with…

## 119. The Long Road to the Same Answer: Cognitive Bias Under Escalating Reasoning Budgets in Large Language Models

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, benchmark, language model, large language
- 作者：Obada Kraishan
- 链接：[arXiv](https://arxiv.org/abs/2610.10049) · [PDF](https://arxiv.org/pdf/2610.10049) · [HF](https://huggingface.co/papers/2610.10049)

Reasoning models allocate extra computation at inference time and present their answers as the product of deliberate thought. If this deliberation works the way dual-process accounts of human cognition suggest, longer thinking should weaken the classic decision biases that fast, intuitive judgment produces. Using 30 vignettes covering six biases (anchoring, framing, loss aversion, escalation of commitment,…

## 120. Cache the Encoder Within:Compact, Reusable Memory across LLM Queries

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, benchmark, coding, spec
- 作者：Hanzuo Liu, Chunyu Liu, Chaofan Lin, Alex Lamb, Mingyu Gao
- 链接：[arXiv](https://arxiv.org/abs/2610.10058) · [PDF](https://arxiv.org/pdf/2610.10058) · [HF](https://huggingface.co/papers/2610.10058)

Repeated queries over shared documents incur redundant encoding, while caching model states introduces persistent storage costs. Building on CoMem's intermediate-state interface, EncBank treats a pretrained LLM's lower layers as a reusable document encoder and compactly stores their outputs for an adapted upper-layer reader. A self-distilled suffix adapter is shared across storage precisions within each backbone,…
