# 每日 AI 论文

生成时间：2026-10-14 04:54 UTC  ·  共 120 篇（已按 arXiv ID 去重）

来源：Hugging Face Daily Papers + arXiv（cs.AI / cs.LG / cs.CL / cs.CV）。
排序：HF 上榜、点赞、多源命中、兴趣词。兴趣词可在 `config.json` 改。

## 1. Thinking Inertia: LLMs Keep Thinking When Told Not To

- 分数：36.0  ·  HF 赞：217  ·  来源：huggingface
- 兴趣命中：reasoning, evaluation, language model, large language
- 作者：Dianqiao Lei, Kevin Qinghong Lin, Pan Lu, Philip Torr, James Zou
- 链接：[arXiv](https://arxiv.org/abs/2610.11765) · [PDF](https://arxiv.org/pdf/2610.11765) · [HF](https://huggingface.co/papers/2610.11765)

Large Language Models (LLMs) increasingly ship with explicit "thinking modes", yet their counterpart, "no-thinking", has received far less attention. We study LLMs' no-thinking behavior along two axes. a. How to measure no-thinking? Prior work typically defines no-thinking through proxies such as a disabled thinking mode or the absence of long traces. These proxies are unreliable: disabled thinking modes may still…

## 2. Scaling Agentic Data for Long-Horizon Terminal Intelligence

- 分数：36.0  ·  HF 赞：136  ·  来源：huggingface
- 兴趣命中：agent, reasoning, benchmark, coding
- 作者：Shun Zou, Ziyu Ma, Yi Zou, Yong Wang, Lin Chen, Zehui Chen, Guanhua Chen, Xiangxiang Chu, Feng Zhao
- 链接：[arXiv](https://arxiv.org/abs/2610.13166) · [PDF](https://arxiv.org/pdf/2610.13166) · [HF](https://huggingface.co/papers/2610.13166)

Terminal agents are moving beyond local operations toward completing real-world professional tasks. Short trajectories can demonstrate commands and tool calls, but they do not fully show how agents accumulate evidence through exploration, use it to inform judgments, continually adjust strategies based on feedback, and turn intermediate results into final deliverables. High-quality long-horizon trajectories capture…

## 3. GroundingPI: A Grounding Foundation Model towards Physical Intelligence with Visual Primitives

- 分数：34.0  ·  HF 赞：249  ·  来源：huggingface
- 兴趣命中：reinforcement learning, benchmark, spec
- 作者：Qize Yu, Lianrui Fan, Boyu Chen, Jiaqi Liang, Xini Ding, Yue Chen, Zetian Song, Yuran Wang, Yi Zou, Kaixuan Wang, Tianxing Chen, Wenxuan Song, Bohan Zhou, Mingleyang Li, Siqiao Huang, Yuqi Ye, Caigao Jiang, Wei Wei, Ruihai Wu, Hang Zhang, Yixiao Ge, Shuchang Zhou, Shilong Liu, Xianming Liu, Ping Luo, Shiyu Huang
- 链接：[arXiv](https://arxiv.org/abs/2609.39601) · [PDF](https://arxiv.org/pdf/2609.39601) · [HF](https://huggingface.co/papers/2609.39601)

Precise grounding matters. It specifies which object is the target and where that object is, even in clutter and for tiny objects, and it has to be fast enough for closed-loop control. Yet vision-language-action (VLA) and world-action models (WAMs) take perception from general-purpose vision-language and video-generation backbones, which still fail in these settings. We introduce GroundingPI, a 4B grounding…

## 4. AgentSWE: Can Coding Agents Build the Agent You Actually Want?

- 分数：34.0  ·  HF 赞：202  ·  来源：huggingface
- 兴趣命中：agent, benchmark, coding
- 作者：Jiahao Wang, Hongjin Qian, Yuyang Hu, Jiajun Zhang, Zheng Liu
- 链接：[arXiv](https://arxiv.org/abs/2610.13361) · [PDF](https://arxiv.org/pdf/2610.13361) · [HF](https://huggingface.co/papers/2610.13361)

As the production of software passes into the hands of software itself, coding agents are increasingly commissioned to build agents fitted to their users' own workflows. This delegation carries a quiet assumption, that the delivered agent will faithfully serve the requirement it was built for, rather than merely appear to. No existing benchmark tests that assumption. We introduce AgentSWE, a benchmark for agent…

## 5. GroundAnything: Reconciling Parallel Decoding with Precise Visual Grounding at Flash Speed

- 分数：34.0  ·  HF 赞：71  ·  来源：huggingface
- 兴趣命中：benchmark, coding, spec
- 作者：Qize Yu, Lianrui Fan, Bowen Ping, Xini Ding, Zetian Song, Junbo Niu, Kaixuan Wang, Tianxing Chen, Yue Chen, Minghua He, Yuran Wang, Jie Huang, Haojun Zhang, Min Chen, Hao Li, Wenxuan Song, Ruihai Wu, Xianming Liu, Shilong Liu, Shuchang Zhou, Ping Luo, Shiyu Huang
- 链接：[arXiv](https://arxiv.org/abs/2609.39600) · [PDF](https://arxiv.org/pdf/2609.39600) · [HF](https://huggingface.co/papers/2609.39600)

Autoregressive (AR) grounding models serialize spatial predictions, introducing sequential latency and imposing a causal order on output tokens. We view grounding as visual evidence extraction: objects, locations, and spatial relations are jointly constrained by the image and query, yet their dependencies do not imply an intrinsic left-to-right generation order. This distinction makes bidirectional diffusion a…

## 6. Vela: User Behavior as Supervision Sparks LLM Intelligence

- 分数：33.5  ·  HF 赞：35  ·  来源：huggingface
- 兴趣命中：agent, reinforcement learning, benchmark, language model, large language
- 作者：Yang Xiao, Yusong Sun, Haoyi Wu, Wenyang Hui, Weiqiang Hang, Luqing Wang, Zejian Wang, Zirui Tu, Jingsheng Mao, Shaobo Hu, Yang Luo, Jiale Guo, Jin Zhang, Yudan Liu, Zhaokai Luo, Ren Huan, Yao Hu, Chengyue Jiang, Wenjie Li, Chuan Mu
- 链接：[arXiv](https://arxiv.org/abs/2610.14709) · [PDF](https://arxiv.org/pdf/2610.14709) · [HF](https://huggingface.co/papers/2610.14709)

Large language models are increasingly deployed in applications that act on users' long-term behavior histories, from personal assistants to recommendation and advertising systems. These applications demand the user dimension of LLM intelligence: inferring a person's preferences, intent, and likely future actions from weeks to years of behavior data. Yet current models are trained on static text or synthetic data,…

## 7. VIS-Ground: Video Interactive Storytelling with Contextual Grounding

- 分数：32.0  ·  HF 赞：79  ·  来源：huggingface
- 兴趣命中：spec, planning
- 作者：Bingxuan Li, Yiwen Song, Xueqing Wu, Yanzhou Pan, Yang Li, Kuang Su, Jingyun Liu, Sebastian Ko, Huan Zhang, Tong Zhang, Nanyun Peng, Tomas Pfister, Yale Song
- 链接：[arXiv](https://arxiv.org/abs/2610.09326) · [PDF](https://arxiv.org/pdf/2610.09326) · [HF](https://huggingface.co/papers/2610.09326)

Video interactive storytelling enables viewers to actively steer how a video unfolds. However, once we allow viewers to intervene during generation, a new challenge arises: The viewer's request can have latent dependencies on both the grounding source and the current rendered video state. These dependencies may not be explicitly stated in any individual input, but emerge only when the source, rendered history, and…

## 8. Multi-Stream Attention Residuals

- 分数：29.0  ·  HF 赞：34  ·  来源：huggingface
- 兴趣命中：benchmark, retrieval
- 作者：Xiaohan Qin, Xiangdong Zhang, Tuo Dai, Sunan Zou, Huaijin Wu, Yebin Yang, Zhuo Xia, Lin Yao, Yuliang Liu, Junchi Yan
- 链接：[arXiv](https://arxiv.org/abs/2610.13630) · [PDF](https://arxiv.org/pdf/2610.13630) · [HF](https://huggingface.co/papers/2610.13630)

Attention Residuals (AttnRes) enables content-dependent retrieval over network depth, which can be viewed as single-stream softmax attention along the depth axis. Inspired by the success of multi-head attention along the sequence axis, we introduce Multi-Stream Attention Residuals (MSAR), an extension of AttnRes that generalizes this mechanism to multi-head depth attention, yielding substantial performance gains…

## 9. PR-OPD: Privileged Representation On-policy Self-Distillation for Agentic Reinforcement Learning

- 分数：28.0  ·  HF 赞：28  ·  来源：huggingface
- 兴趣命中：agent, reinforcement learning, spec
- 作者：Muyang Li, Jie Yang, Zhengyu Fang, Junchao Zhu, Zhengkun Xiao, Ruining Deng, Zhe Jiang, Shigang Chen
- 链接：[arXiv](https://arxiv.org/abs/2609.36642) · [PDF](https://arxiv.org/pdf/2609.36642) · [HF](https://huggingface.co/papers/2609.36642)

Language-model agents are usually trained by reinforcement learning from one reward per episode, and privileged self-distillation enriches it by letting the same policy, given a skill, teach its skill-free self through token probabilities. However, we identify two phenomena that question this channel. Invisible Advantage: a skill in context lifts WebShop success from 42.2% to 56.2%, yet changes the probabilities of…

## 10. DoSA: Dots Sparse Attention

- 分数：27.5  ·  HF 赞：31  ·  来源：huggingface
- 兴趣命中：evaluation, spec
- 作者：Fanxu Meng, Taosong Fang
- 链接：[arXiv](https://arxiv.org/abs/2610.13990) · [PDF](https://arxiv.org/pdf/2610.13990) · [HF](https://huggingface.co/papers/2610.13990)

Sparse attention visits few keys, yet finding them can still require scoring every key with every indexer head. We introduce DoSA (Dots Sparse Attention), a lossless method for making this computation conditional while preserving exact token selection. Its central observation is that Top-K selection requires sufficient evidence to reject a candidate, not necessarily its full score. A seed set supplies a lower bound…

## 11. UltraBERT: Beyond the Limit of BERT Pre-Training

- 分数：26.5  ·  HF 赞：25  ·  来源：huggingface
- 兴趣命中：language model, large language, retrieval
- 作者：Jungwoo Park, Taewhoo Lee, Jaewoo Kang
- 链接：[arXiv](https://arxiv.org/abs/2610.15028) · [PDF](https://arxiv.org/pdf/2610.15028) · [HF](https://huggingface.co/papers/2610.15028)

Recent bidirectional encoders have been modernized with innovations from causal large language models (LLMs). However, the pretraining recipe itself remains inherited from small-scale conventions, leaving encoders underoptimized, with no single model performing competitively across both classification and retrieval tasks. In this work, we investigate how far encoder performance can be pushed by revisiting core…

## 12. Relevance Does Not Imply Applicability: Experience Activation for Personal GUI Agents

- 分数：24.5  ·  HF 赞：29  ·  来源：huggingface
- 兴趣命中：agent
- 作者：Fuyao Zhang, Xuan Wang, Zherui Li, Jiaming Zhang, Longtao Huang, Wei Yang Bryan Lim
- 链接：[arXiv](https://arxiv.org/abs/2609.33304) · [PDF](https://arxiv.org/pdf/2609.33304) · [HF](https://huggingface.co/papers/2609.33304)

Personal Graphical User Interface (GUI) agents rely on interaction history to infer what a user wants from ambiguous instructions and to anticipate recurring routines. Existing approaches retrieve task-relevant history and append it to the policy's context, implicitly assuming that experience relevant to a task remains useful for each decision within it. We find that this help is largely spent at the first decision:…

## 13. SpatialASM: Internalizing Active Mentalization for Spatial Reasoning

- 分数：24.0  ·  HF 赞：16  ·  来源：huggingface
- 兴趣命中：reasoning, benchmark, language model, spec, planning
- 作者：Yuhong Liu, Shenxi Wu, Junyi Chi, Beichen Zhang, Xuanlang Dai, Jiaqi Wang, Yuhang Zang, Dahua Lin
- 链接：[arXiv](https://arxiv.org/abs/2610.13832) · [PDF](https://arxiv.org/pdf/2610.13832) · [HF](https://huggingface.co/papers/2610.13832)

When solving complex spatial reasoning tasks, ordinary humans naturally revisit the scenes from task-relevant viewpoints and mentally reconstruct the spatial layouts from those viewpoints. But can Large Vision-Language Models (LVLMs) proactively think in the same way? We term this ability Active Spatial Mentalization (ASM), an intrinsic component of visual intelligence that remains substantially underdeveloped in…

## 14. CrossTimeEdit: A Decade-Spanning Cross-View Dataset and Reward-Guided Editing for Historical Street-View Generation

- 分数：22.5  ·  HF 赞：21  ·  来源：huggingface
- 兴趣命中：reinforcement learning, evaluation
- 作者：Hanwen Lu, Jun He, Mingjia Yang, Hao Wei, Jinhao Huang, Yi Lin, Xiang Zhang
- 链接：[arXiv](https://arxiv.org/abs/2609.36616) · [PDF](https://arxiv.org/pdf/2609.36616) · [HF](https://huggingface.co/papers/2609.36616)

Historical street-view imagery records urban evolution, but uneven coverage leaves substantial gaps in historical records. Generating plausible past appearances requires restoring changed structures while preserving persistent scene content. We construct VIGOR-his, a decade-spanning cross-view dataset containing 43,653 location-level quadruplets across 11 cities on three continents. Its automated pipeline performs…

## 15. Scoring Higher, Answering Worse: Mitigating Reward Hacking in Rubric-Based RL via Protocol-Level Rubrics

- 分数：22.0  ·  HF 赞：16  ·  来源：huggingface
- 兴趣命中：reinforcement learning, benchmark, language model
- 作者：Maoqi Liu, Junwei He, Bowen Zhang, Feiran Li, Wentao Ma, Rongyi Lin, Shuhan Zhong, Quan Fang
- 链接：[arXiv](https://arxiv.org/abs/2609.38847) · [PDF](https://arxiv.org/pdf/2609.38847) · [HF](https://huggingface.co/papers/2609.38847)

Rubric-based reinforcement learning (Rubric-RL) trains language models where no verifier exists. A judge checks each criterion of a rubric, and the verdicts are aggregated into a reward, most often by a weighted sum. We show that this additive aggregation is the weak point. Under a sum, criteria compensate for one another: a policy that misses the one decision that matters can buy the points back with advice nobody…

## 16. Harness^2: Recursive Agent Harnessing for an Open World

- 分数：22.0  ·  HF 赞：16  ·  来源：huggingface
- 兴趣命中：agent, benchmark, spec
- 作者：Ruiyao Xu, Yanfei Chen, Zhongying CuiZhu, Bhavana Dalvi Mishra, Yifei Ming, Han Yu, Rujun Han, Chen-Yu Lee, Tomas Pfister
- 链接：[arXiv](https://arxiv.org/abs/2610.14224) · [PDF](https://arxiv.org/pdf/2610.14224) · [HF](https://huggingface.co/papers/2610.14224)

LLM agents' capabilities depend not only on their underlying models but also on their execution harnesses. Recursive self-improvement (RSI) offers a promising approach to automatically evolve these harnesses. However, deploying RSI in open-world settings still faces two critical challenges. First, open-world tasks are typically unseen during the harness design phase and novel at test time, leaving no ground-truth…

## 17. LeWAM: End-to-End World and Action Modeling with JEPAs

- 分数：21.5  ·  HF 赞：23  ·  来源：huggingface
- 兴趣命中：planning
- 作者：Minghao Fu, Tavis Siebert, Eryk Halicki, Randall Balestriero
- 链接：[arXiv](https://arxiv.org/abs/2610.12818) · [PDF](https://arxiv.org/pdf/2610.12818) · [HF](https://huggingface.co/papers/2610.12818)

Joint-embedding predictive architectures (JEPAs) learn compact latent world models without pixel reconstruction. Existing JEPA pipelines typically train visual representations and action-conditioned dynamics before adding a control policy or solver. We introduce LeWAM, an end-to-end JEPA for control with: (1) a joint training objective over next latent state prediction and action flow matching, and (2) an isotropic…

## 18. Systematic Multi-Agent Vision-and-Language Navigation: Formulation, Benchmark, and Method

- 分数：21.0  ·  HF 赞：10  ·  来源：huggingface
- 兴趣命中：agent, memory, benchmark, planning
- 作者：Yunzhe Xu, Zhe Liu
- 链接：[arXiv](https://arxiv.org/abs/2609.35965) · [PDF](https://arxiv.org/pdf/2609.35965) · [HF](https://huggingface.co/papers/2609.35965)

Vision-and-Language Navigation (VLN) has largely focused on a single agent following a single instruction, yet many real-world applications require teams of robots to tackle tasks beyond the capabilities of any individual agent. We present Systematic Multi-Agent Vision-and-Language Navigation, providing, to our knowledge, the first systematic formalization of multi-agent VLN as a constrained coordination problem:…

## 19. CineRecon: Benchmarking Frontier Models for Agentic Cinematic Reconstruction

- 分数：20.5  ·  HF 赞：9  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark, spec
- 作者：Jialei Wang, Zehan Wang, XiaoYang Wu, Ziang Zhang, Siyu Chen, Jiaer Huang, Yujia Zhang, Tianyu Pang, Hengshuang Zhao
- 链接：[arXiv](https://arxiv.org/abs/2610.16577) · [PDF](https://arxiv.org/pdf/2610.16577) · [HF](https://huggingface.co/papers/2610.16577)

Reconstructing reference videos as editable dynamic 3D scenes is an important path toward controllable video generation for filmmaking: these scenes provide modifiable, renderable visual proxies that enable explicit control over scene layout, subject actions, and camera behavior. To evaluate agents' ability to reconstruct editable dynamic 3D scenes from dynamic reference videos, we introduce CineRecon, a benchmark…

## 20. WorkRover: Scaling Long-Horizon Cowork Agent Training Via Recursive Environment Evolution

- 分数：20.5  ·  HF 赞：1  ·  来源：huggingface + arxiv
- 兴趣命中：agent, reinforcement learning, evaluation, benchmark
- 作者：Hang He, Linting Wang, Guanming Liu, Bo Mao, Jinxiu Liu, Yiran Suo, Maosen Zhou, Zhiheng Xi, Guanting Dong, Zhou Shao, Rui Zheng, Jie Zhou, Chengcheng Wan, Tao Gui, Qi Zhang, Xipeng Qiu, Xuanjing Huang
- 链接：[arXiv](https://arxiv.org/abs/2610.18067) · [PDF](https://arxiv.org/pdf/2610.18067) · [HF](https://huggingface.co/papers/2610.18067)

Scaling interactive environments is important for training long-horizon agents through reinforcement learning. These environments often require further testing and refinement after initial generation, and correcting defects in a task may also require updating its work context and verifier. However, existing construction pipelines offer limited support for such iterative refinement while keeping these components…

## 21. PhyProbe: Rethinking Physical Consistency Evaluation in Generated Videos

- 分数：20.0  ·  HF 赞：8  ·  来源：huggingface
- 兴趣命中：evaluation, benchmark, language model, spec
- 作者：Max Ku, Jiaojiao Fan, Zekun Hao, Francesco Ferroni, Heng Wang, Wenhu Chen, Ming-Yu Liu, Prithvijit Chattopadhyay
- 链接：[arXiv](https://arxiv.org/abs/2609.38377) · [PDF](https://arxiv.org/pdf/2609.38377) · [HF](https://huggingface.co/papers/2609.38377)

Evaluating the physical consistency of generated videos remains a fundamental challenge. Existing approaches rely on off-the-shelf vision-language models, which can often be myopic to physical dynamics, or fine-tuned evaluators trained on human annotations, which overfit to dataset-specific cues and fail to generalize. A key challenge is that existing supervision sources provide either relative ordering or absolute…

## 22. ClawLoop: Self-Improving Agents via Harness-Native Training Loop

- 分数：20.0  ·  HF 赞：8  ·  来源：huggingface
- 兴趣命中：agent, tool-use, evaluation, benchmark, language model, large language
- 作者：Hansi Yang, Linji Hao, Hongyan Hao, An Wang, Han Wu, Qi Gu, Xunliang Cai
- 链接：[arXiv](https://arxiv.org/abs/2610.14118) · [PDF](https://arxiv.org/pdf/2610.14118) · [HF](https://huggingface.co/papers/2610.14118)

The rapid advancement of Large Language Models (LLMs) has driven their deployment toward general-purpose harness environments, where LLM-based agents operate in sandbox workspaces and interact directly with file systems and shells. While numerous post-training pipelines exist for tool-use agents, their counterparts for harness-based agents remain scarce and are predominantly one-shot and teacher-dependent: a…

## 23. JevGPT: Thinking Fast and Slow in Autonomous Research

- 分数：20.0  ·  HF 赞：0  ·  来源：huggingface + arxiv
- 兴趣命中：agent, spec, planning, retrieval
- 作者：Yasheng Sun, Yanning Dai, Yimeng Chen, Nanbo Li, Firas Laakom, Yifan Xu, Piotr Piękos, Mateusz Ostaszewski, Wenyi Wang, Cheng Luo, Yuhui Wang, Jürgen Schmidhuber
- 链接：[arXiv](https://arxiv.org/abs/2610.18272) · [PDF](https://arxiv.org/pdf/2610.18272) · [HF](https://huggingface.co/papers/2610.18272)

Autonomous research agents must acquire and reason over evidence within a limited budget. Yet relevant sources can remain uninspected or unused, leaving a gap between retrieval coverage and the evidence that informs research. The challenge is to align fast local judgments with changing evidence needs and feed their findings back into research decisions. We introduce JevGPT, a dual-system architecture for autonomous…

## 24. Learning More by Training Less: Uncertainty-Guided Progressive Contraction for Efficient Reasoning Post-Training

- 分数：19.5  ·  HF 赞：7  ·  来源：huggingface
- 兴趣命中：reasoning, benchmark, language model, large language, spec
- 作者：Suorong Yang, Jiaxin Wang, Jiaming Su, Chentao Yue, Furao Shen, Peng Ye, Soujanya Poria
- 链接：[arXiv](https://arxiv.org/abs/2610.12933) · [PDF](https://arxiv.org/pdf/2610.12933) · [HF](https://huggingface.co/papers/2610.12933)

Large language models have achieved remarkable advances in complex reasoning. However, scaling reasoning post-training with ever-larger corpora can substantially increase training cost without proportional performance gains. In this study, we therefore ask: how far can reasoning supervision be compressed without sacrificing capability? To this end, we propose an uncertainty-guided progressive contraction framework…

## 25. ExeWorldBench: Benchmarking Code-Based Executable 3D World Modeling

- 分数：19.0  ·  HF 赞：6  ·  来源：huggingface
- 兴趣命中：agent, reasoning, evaluation, benchmark, coding
- 作者：Xinge Peng, Zhen Fang, Ruibing Wang, Yongxuan Lv, Haodong Li, Guohui Zhang, Xiaoxiao Ma, Yiting Lu, Lin Chen, Zehui Che, Feng Zhao
- 链接：[arXiv](https://arxiv.org/abs/2610.15166) · [PDF](https://arxiv.org/pdf/2610.15166) · [HF](https://huggingface.co/papers/2610.15166)

Coding agents are increasingly evolving beyond reproducing what a world looks like toward constructing executable worlds that capture how a world works. This shift calls for executable world modeling, which integrates two core capabilities: world understanding, reasoning about the underlying structural, mechanical, and causal principles of a world, and executable realization, translating that understanding into a…

## 26. PANINI-DR: Controlled Deep Research through Generative Semantic Workspaces

- 分数：19.0  ·  HF 赞：6  ·  来源：huggingface
- 兴趣命中：agent, memory, reasoning, benchmark, planning
- 作者：M. Yigit Turali, Shreyas Rajesh, M. Efe Lorasdagi, Chenda Duan, Kartik Sharma, Vwani Roychowdhury
- 链接：[arXiv](https://arxiv.org/abs/2610.15208) · [PDF](https://arxiv.org/pdf/2610.15208) · [HF](https://huggingface.co/papers/2610.15208)

Deep research requires connecting multiple steps of search, reasoning, and computation, with intermediate findings guiding what to investigate next. As investigations grow, agents must maintain research state across model calls and check findings before errors propagate into subsequent work. We introduce PANINI-DR, a multi-agent harness that separates coordination of the overall investigation from the research and…

## 27. DeltaTTG: Training Multi-Turn Agents with a Token-to-Go Progress Meter

- 分数：18.5  ·  HF 赞：9  ·  来源：huggingface
- 兴趣命中：agent, reinforcement learning, spec
- 作者：Xuyan Ye, Xiyan Fu, Shengda Fan, Jiawei Cui, Yankai Lin, Wei Lu
- 链接：[arXiv](https://arxiv.org/abs/2610.17666) · [PDF](https://arxiv.org/pdf/2610.17666) · [HF](https://huggingface.co/papers/2610.17666)

Reinforcement learning with verifiable rewards (RLVR) for multi-turn agents relies on sparse terminal rewards that say little about individual steps. Within-group step comparisons depend on reliable state matching and sufficiently diverse sampled outcomes, while direct step scoring may require costly external evaluators, human annotations, or task-specific heuristics. We introduce DeltaTTG to learn a reusable…

## 28. TPPO: Tracking-Value PPO For Language Model Reasoning

- 分数：18.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：reasoning, reinforcement learning, language model, coding, spec
- 作者：Futing Wang, Chenxi Li, Jianhao Yan, Yun Luo, Zhi Wang, Yizhuo Li, Runzhe Zhan, Yu Cheng, Tao Lin
- 链接：[arXiv](https://arxiv.org/abs/2610.16794) · [PDF](https://arxiv.org/pdf/2610.16794) · [HF](https://huggingface.co/papers/2610.16794)

Proximal Policy Optimization (PPO) is widely used in reinforcement learning with verifiable rewards for language-model reasoning. While value evolution along trajectory characterizes relative token-level credit, yet standard critics often fail to track it under sparse terminal rewards. To model this evolution, we analyze the relation between successive prefix values and show that they admit a Bayesian decomposition…

## 29. Spectral-Driven Adaptive-Rank Optimizer for Large Language Model Reinforcement Learning with Verifiable Rewards

- 分数：18.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：reasoning, reinforcement learning, language model, large language, spec
- 作者：Zhipeng Chen, Wayne Xin Zhao, Ji-Rong Wen
- 链接：[arXiv](https://arxiv.org/abs/2610.16533) · [PDF](https://arxiv.org/pdf/2610.16533) · [HF](https://huggingface.co/papers/2610.16533)

Reinforcement learning with verifiable rewards (RLVR) is reshaping how large language models (LLMs) acquire reasoning capabilities, yet the optimizers used remain largely inherited from teacher-forcing training. This raises a fundamental question: does RLVR induce a distinct optimization geometry that calls for a different optimizer? We investigate this question through the spectral structure of LLM gradients and…

## 30. WOVEN: Weaving Visual World Modeling into Multimodal LLMs

- 分数：17.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：reasoning, benchmark, language model, large language, spec
- 作者：Zheyu Fan, Yue Zhang, Mingkai Deng, Kangrui Wang, Qineng Wang, Canyu Chen, Jie Hao, Xing Fan, Chenlei Guo, Eric P. Xing, Mohit Bansal, Manling Li
- 链接：[arXiv](https://arxiv.org/abs/2610.12417) · [PDF](https://arxiv.org/pdf/2610.12417) · [HF](https://huggingface.co/papers/2610.12417)

Multimodal large language models (MLLMs) struggle with spatial, embodied, physical, and temporal reasoning. We hypothesize that these failures reflect a shared deficit in visual transition reasoning, and test whether this capability can serve as a shared training primitive, one that different models can learn from different supervision sources and reuse across different tasks, with a systematic training recipe.…

## 31. Evaluating LLM Creativity through Long-Tail Performance

- 分数：17.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：benchmark, language model, large language, spec
- 作者：Yichen Wang, Tenghao Huang, Vishakh Padmakumar, Mina Lee
- 链接：[arXiv](https://arxiv.org/abs/2610.12998) · [PDF](https://arxiv.org/pdf/2610.12998) · [HF](https://huggingface.co/papers/2610.12998)

Creativity benchmarks for large language models (LLMs) vary widely in task and metric design. This raises the question of whether they capture a common notion of creativity. We propose that this shared target can be formalized as task-specific performance in the long tail of a reference input-output distribution, which describes how common input-output pairs are relative to a chosen source of text. We ground this…

## 32. Agent Sociodrama: Social-Dynamics-Guided Persona Recasting for LLM Agent Teams

- 分数：17.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：agent, benchmark, language model, large language, spec
- 作者：Yirui Qi, Xiaoming Zhang, Jaehong Yoon
- 链接：[arXiv](https://arxiv.org/abs/2610.15788) · [PDF](https://arxiv.org/pdf/2610.15788) · [HF](https://huggingface.co/papers/2610.15788)

Large language model (LLM) agents are increasingly deployed as teams, yet they fail in characteristically social ways: information holders stay silent, dominant speakers anchor groups on wrong answers, and norm violations go unsanctioned. We present Agent Sociodrama, a framework for modeling and validating evolving social dynamics in LLM agent teams. Under fixed personas, agents' emotional states and directed,…

## 33. Narrow Multimodal Fine-Tuning Can Induce Emergent Misalignment

- 分数：17.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：agent, reasoning, evaluation, language model
- 作者：Shunchang Liu, Lukas Fluri, Xin Chen, Francesco Croce
- 链接：[arXiv](https://arxiv.org/abs/2609.35291) · [PDF](https://arxiv.org/pdf/2609.35291) · [HF](https://huggingface.co/papers/2609.35291)

Modern AI models are aligned through post-training to adapt them to downstream tasks. Recent work shows that fine-tuning language models on narrow tasks can induce emergent misalignment (EM), causing broadly harmful behaviors beyond the training task. However, EM has been studied almost entirely in text-only tasks, leaving its manifestation in multimodal models unclear. In this paper, we define and analyze EM in the…

## 34. Prospective Hindsight: Self-Calibrating Reinforcement Learning via Prediction-Reality Gaps

- 分数：17.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：agent, reinforcement learning, evaluation, spec
- 作者：Jiaxin Zhang, Xiangyu Peng, Qinglin Chen, Yu Li, Hiroaki Hayashi, Chien-Sheng Wu
- 链接：[arXiv](https://arxiv.org/abs/2610.02740) · [PDF](https://arxiv.org/pdf/2610.02740) · [HF](https://huggingface.co/papers/2610.02740)

Reinforcement learning for long-horizon agents relies on purely retrospective training signals: credit is assigned only after observing environmental consequences, leaving the agent's belief at action time invisible to the gradient. We introduce Prospective Hindsight (PH), a self-calibrating training principle that augments any retrospective base method with a signal derived from the gap between the agent's…

## 35. A Decade in a Day: Synthesizing Agent-Native Interfaces from Human-Oriented Software Evolution

- 分数：17.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark, language model, large language, spec
- 作者：Alan Wu, Wei Tao, Yiwen Guo
- 链接：[arXiv](https://arxiv.org/abs/2610.15765) · [PDF](https://arxiv.org/pdf/2610.15765) · [HF](https://huggingface.co/papers/2610.15765)

Large language model agents are emerging as an important new class of users of desktop applications. However, existing desktop interfaces were designed for human end users or application developers, leaving agents to interpret visual controls or discover and compose low-level software operations. This mismatch can hinder even capable agents, yet it remains unclear what interface properties make desktop software…

## 36. X-Ragent: Tool-Augmented Reinforcement Learning for Evidence-Grounded Chest X-Ray Reasoning

- 分数：17.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：agent, reasoning, reinforcement learning, benchmark, spec
- 作者：Yi Wang, Zhenlong Yuan, Yuchan Guo, Maolei Huang, Zijian Song, Dapeng Zhang, Rongbin Tan, Jiyuan Wang, Zhiyuan Wang, Fangfang Lin, Shuhan Song, Huawei Cao
- 链接：[arXiv](https://arxiv.org/abs/2610.16811) · [PDF](https://arxiv.org/pdf/2610.16811) · [HF](https://huggingface.co/papers/2610.16811)

Chest X-ray (CXR) interpretation often requires integrating visual findings with task-specific evidence rather than relying on direct visual recognition alone. While tool-augmented medical agents can supply such evidence via external modules, they often lack explicit mechanisms for learning when auxiliary evidence is needed and for preventing inapplicable quantitative evidence from entering diagnostic reasoning. To…

## 37. Elephant in the Fridge: Constant-Memory Frame Packing for Long Video Understanding

- 分数：16.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：memory, context window, benchmark, language model, coding, spec
- 作者：Shuo Gao, Chenhao Zheng, Zhongzheng Ren
- 链接：[arXiv](https://arxiv.org/abs/2610.16118) · [PDF](https://arxiv.org/pdf/2610.16118) · [HF](https://huggingface.co/papers/2610.16118)

Hour-long videos, streaming feeds, and movie-length content are pushing vision-language models (VLMs) past their breaking point -- the standard recipe of encoding each frame into visual tokens yields sequences that grow linearly with video length, causing prohibitive memory consumption and inference latency. Existing approaches, such as token reduction and keyframe selection, shorten the token sequence but leave the…

## 38. ARCS: Towards Precise Text-to-SQL via Structured Disambiguation

- 分数：16.0  ·  HF 赞：8  ·  来源：huggingface
- 兴趣命中：benchmark, spec
- 作者：Yihao Hu, Yanlin Feng, Naoki Otani, Nikita Bhutani
- 链接：[arXiv](https://arxiv.org/abs/2610.09396) · [PDF](https://arxiv.org/pdf/2610.09396) · [HF](https://huggingface.co/papers/2610.09396)

As text-to-SQL systems move beyond demonstrations toward real-world deployment, ambiguity in user questions becomes a primary source of errors. Such ambiguities are often subtle, domain- or data-specific, and can silently cause system outputs to deviate from the user's true intent. Ambiguity is traditionally addressed through conversational clarification, which is often inefficient, cognitively demanding, and poorly…

## 39. RSIPO: Recursive Self-Improving Policy Optimization for Agentic Reinforcement Learning via Skill-Policy Co-Evolution

- 分数：16.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：agent, reinforcement learning, spec
- 作者：Fan Zhang, Hao Wu, Jinyang Wu, Hongyu Qu, Zheng Lian, Xiao Luo, Yefeng Zheng, Bo Zhang, Haoxuan Li, Pheng-Ann Heng
- 链接：[arXiv](https://arxiv.org/abs/2610.15772) · [PDF](https://arxiv.org/pdf/2610.15772) · [HF](https://huggingface.co/papers/2610.15772)

Recent focus in agentic reinforcement learning (RL) seeks to improve credit assignment in long-horizon tasks. One promising direction combines reinforcement learning with verifiable rewards (RLVR) and on-policy self-distillation (OPSD), integrating trajectory-level advantages with dense token-level supervision. This line of work often conditions a teacher model on privileged context, such as agentic skills, to score…

## 40. HyperThink: Text-to-Parameter Hypernetworks for Efficient Reasoning

- 分数：16.0  ·  HF 赞：0  ·  来源：huggingface
- 兴趣命中：reasoning, language model, large language, coding
- 作者：Donggyun Kim, Jack Lu, Chanwoo Kim, Mengye Ren, Seunghoon Hong
- 链接：[arXiv](https://arxiv.org/abs/2610.03039) · [PDF](https://arxiv.org/pdf/2610.03039) · [HF](https://huggingface.co/papers/2610.03039)

Long-form thinking traces can substantially improve the multi-step reasoning performance of large language models (LLMs), but they introduce high inference-time overhead, with latency dominated by sequential decoding. We propose HyperThink, a text-to-parameter approach that amortizes this reasoning computation into a single query-conditioned parameter update: a lightweight hypernetwork reads the question and…

## 41. Web$hell: A Unified Interface for Agentic Web Access

- 分数：16.0  ·  HF 赞：0  ·  来源：huggingface
- 兴趣命中：agent, benchmark, language model, large language
- 作者：Sunghwan Kim, Deogyong Kim, Sangam Lee, Donguk Kwon, Dongha Lee
- 链接：[arXiv](https://arxiv.org/abs/2610.13416) · [PDF](https://arxiv.org/pdf/2610.13416) · [HF](https://huggingface.co/papers/2610.13416)

Large language model (LLM) agents are becoming direct users of the open web. As they take on increasingly complex and information-intensive tasks, effective web access is becoming a core capability for agentic problem solving. Existing approaches have advanced agentic web access through different access models, including search-augmented agents, browser-based agents, and, more recently, filesystem-based agents.…

## 42. TacitVLA: Reasoning Vision-Language-Action Models Without Reasoning Latency

- 分数：16.0  ·  HF 赞：0  ·  来源：huggingface
- 兴趣命中：memory, reasoning, benchmark, coding
- 作者：Jack Lu, Yurong You, Boyi Li, Yulong Cao, Thomas Tian, Chaowei Xiao, Xiangyu Chen, Wenjie Luo, Boris Ivanovic, Marco Pavone, Yan Wang
- 链接：[arXiv](https://arxiv.org/abs/2610.17540) · [PDF](https://arxiv.org/pdf/2610.17540) · [HF](https://huggingface.co/papers/2610.17540)

Textual reasoning before acting has improved vision-language-action (VLA) models, but at the cost of latency: every action conditioned on the reasoning text must wait for autoregressive decoding. We show that actions do not need to wait for or condition on the generated reasoning to benefit from it, because the reasoning supervision already improves the backbone representation. We introduce TacitVLA, a reasoning VLA…

## 43. Visual Grounding Safety in Vision-Language Models

- 分数：15.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：agent, benchmark, language model
- 作者：Erfan Shayegani, Kundan Krishna, Yue Dong, Nael Abu-Ghazaleh, Leon Gatys, Shruti Palaskar
- 链接：[arXiv](https://arxiv.org/abs/2610.05637) · [PDF](https://arxiv.org/pdf/2610.05637) · [HF](https://huggingface.co/papers/2610.05637)

Vision-language models (VLMs) are increasingly trained to generate structured outputs like points and bounding boxes that downstream interfaces, agents, and robots can act on, yet safety alignment of this output channel has not been systematically analyzed. We study visual grounding safety by repurposing three safety benchmarks spanning direct harm (VLSU), social bias (BBQ-V), and situational safety (Asimov-2.0)…

## 44. VIEWCRAFT: Evolving What Multimodal Agents See and How They Read It

- 分数：15.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark
- 作者：Binxiao Xu, Ruichuan An, Bocheng Zou, Weihua Du, Xinyu Wei, Hangyu Guo, YiFan Zhang, Renye Yan, Chengqi Duan, Hang Hua
- 链接：[arXiv](https://arxiv.org/abs/2610.15915) · [PDF](https://arxiv.org/pdf/2610.15915) · [HF](https://huggingface.co/papers/2610.15915)

Reusable skills improve multimodal agents without updating model weights, but their effectiveness depends on both the evidence presented and the procedure used to read it. We introduce ViewCraft, which jointly evolves an executable evidence interface and its reading procedure. The interface selects, transforms, and organizes observations; the reader interprets the resulting views. Failure traces guide revisions,…

## 45. Initialization Improves LLM-Driven Discovery

- 分数：14.5  ·  HF 赞：5  ·  来源：huggingface
- 兴趣命中：language model, large language
- 作者：Mansi Sakarvadia, Marco Ciccone, Colin Raffel
- 链接：[arXiv](https://arxiv.org/abs/2610.00707) · [PDF](https://arxiv.org/pdf/2610.00707) · [HF](https://huggingface.co/papers/2610.00707)

Large Language Models (LLMs) have been used for novel discovery of algorithms, theorems, drugs, and other tasks through the use of harnesses that prompt an LLM to iteratively optimize an objective. In this work, we study the relationship between the population of previous iterates and eventual discovery success. We generalize past work on harness design to develop a suite of 12 harnesses called 'Modular' and…

## 46. CURIO: Curiosity-Driven Test-Time Learning for Open-Ended Discovery

- 分数：14.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：reinforcement learning, language model, large language
- 作者：Tao Feng, Fangxu Yu, Zijie Lei, Jiaru Zou, Changjiang Jiang, Yi Yan, Jiaxuan You, Pan Lu
- 链接：[arXiv](https://arxiv.org/abs/2610.04851) · [PDF](https://arxiv.org/pdf/2610.04851) · [HF](https://huggingface.co/papers/2610.04851)

Open-ended discovery requires learning from repeated attempts while continuing to explore directions whose value is not yet apparent. Search with a frozen large language model (LLM) can reuse previous solutions in context, but cannot update the model from its successes and failures on the test problem. Reinforcement learning (RL) enables such adaptation; however, strongly favoring high-reward trajectories may…

## 47. SALD: Self-Referenced Advantage Learning for Diffusion Models

- 分数：14.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：memory, spec
- 作者：Aryan Das, Surjo Dey, Koushik Biswas, Swalpa Kumar Roy, Moloud Abdar, Arnab Bhattacharya, Vinay Kumar Verma
- 链接：[arXiv](https://arxiv.org/abs/2610.01496) · [PDF](https://arxiv.org/pdf/2610.01496) · [HF](https://huggingface.co/papers/2610.01496)

Recent work on language-model adaptation has shown that single models can obtain informative training signals by evaluating their behavior in demonstrationor feedback-augmented contexts, with the help of a teacher network, which is driven by the student's learned parameters. Inspired by this internal-reference principle, we investigate how diffusion models can identify self-referenced training signals without…

## 48. Branching On-Policy Distillation

- 分数：14.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：agent, benchmark
- 作者：Dongyang Chen, Shudong Liu, Shubo Li, Duoxun Tang, Jinwei Liang, Zehuan Wu, Lewei Lu
- 链接：[arXiv](https://arxiv.org/abs/2610.13481) · [PDF](https://arxiv.org/pdf/2610.13481) · [HF](https://huggingface.co/papers/2610.13481)

On-policy distillation (OPD) provides teacher supervision on student-generated trajectories, but a single trajectory realizes only one continuation at each decision, limiting supervision coverage under a finite sampling budget. We propose BranchOPD (Branching On-Policy Distillation), which selects informative decision points using student uncertainty and teacher-student disagreement, resamples student-policy…

## 49. Fish Audio Drama 3 Technical Report

- 分数：14.0  ·  HF 赞：0  ·  来源：huggingface + arxiv
- 兴趣命中：reinforcement learning
- 作者：Dawei Han, Shidong Li, Shijia Liao, Jiahua Liu, Songting Liu, Qingzheng Wang, Yuxuan Wang, Xin Chen, Yifan Cheng, Tianyu Li, Gangin Park, Xuehao Yang, Chang Zeng, Haoyang Zhang, Ruoyi Zhang, Xiangyu Zhang
- 链接：[arXiv](https://arxiv.org/abs/2610.18010) · [PDF](https://arxiv.org/pdf/2610.18010) · [HF](https://huggingface.co/papers/2610.18010)

We introduce Fish Audio Drama 3, an open-source speech generation model that turns text into directed performances, built on a 35B-parameter mixture-of-experts backbone that activates 3B parameters per token. It clones voices from multiple references, follows natural-language direction, revises a take when the next turn gives a note, voices multi-character scenes, edits existing speech by infilling, and synthesizes…

## 50. T3lescope: Arbitrary-Resolution High-Fidelity Generative Surface Reconstruction from Images

- 分数：13.5  ·  HF 赞：11  ·  来源：huggingface
- 兴趣命中：-
- 作者：Atsuhiro Noguchi, Tianhan Xu, Yiming Liang, Yuta Kikuchi, Masahiro Ishiyama, Shintaro Takagi, Hitoshi Murai, Eiichi Matsumoto
- 链接：[arXiv](https://arxiv.org/abs/2610.03308) · [PDF](https://arxiv.org/pdf/2610.03308) · [HF](https://huggingface.co/papers/2610.03308)

We reconstruct high-fidelity 3D scene meshes from posed multi-view images without per-scene optimization, across scales ranging from single objects to large outdoor scenes. Per-scene optimization methods lack the learned 3D prior needed when observations are sparse or surfaces are glossy or transparent. Existing generative methods leverage such priors to complete geometry in sparsely observed regions, but typically…

## 51. Diffusion Editing with Soft Mask: Pixel Level Redo of Image and Video with Adjustable Strength

- 分数：13.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：memory, spec
- 作者：Candi Zheng, Yuan Lan
- 链接：[arXiv](https://arxiv.org/abs/2610.00359) · [PDF](https://arxiv.org/pdf/2610.00359) · [HF](https://huggingface.co/papers/2610.00359)

Diffusion models with prompt and reference image-guided editing have seen rapid progress, yet they remain too coarse for pixel-level control. One promising direction is to incorporate a soft mask that specifies spatially varying edit strengths but training such fine-grained control demands expensive pixel-wise annotations, while existing zero-shot methods often yield unsatisfactory results. We introduce SoftPaint, a…

## 52. Controlled Acquisition and Abstention in Three-Channel Score Conflicts

- 分数：13.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：benchmark, spec
- 作者：Mengzhe Geng
- 链接：[arXiv](https://arxiv.org/abs/2610.10808) · [PDF](https://arxiv.org/pdf/2610.10808) · [HF](https://huggingface.co/papers/2610.10808)

When audio, video, and text disagree, accuracy alone does not show whether to acquire another source or abstain. We study these choices in a controlled three-score benchmark: a policy observes two signed scores, may request the third at a cost, and can abstain. The primary reward is mechanism-specific: abstention is correct only for one designated ambiguity mechanism and is penalized under mixed corruption. Matched…

## 53. SPLATIFY: Reproduce, Discover, Innovate! From Papers and Ideas to Trainable 3DGS Code

- 分数：12.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：agent, evaluation
- 作者：Seemandhar Jain, Keshav Gupta, Manmohan Chandraker
- 链接：[arXiv](https://arxiv.org/abs/2610.09116) · [PDF](https://arxiv.org/pdf/2610.09116) · [HF](https://huggingface.co/papers/2610.09116)

The rapid growth of 3D Gaussian Splatting (3DGS) research demands significant effort to reimplement papers before building on them. We introduce SPLATIFY, a multi-agent framework that converts 3DGS papers into trainable gsplat-based implementations, where generic paper-to-code methods and frontier models fail. SPLATIFY achieves this through five innovations: (1) A context-free grammar for gsplat over a modular…

## 54. AutoEnvScaling: Automating the Data Flywheel with Terminal Agents

- 分数：12.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：agent, reinforcement learning
- 作者：Simon Yu, Baolin Peng, Bo Liu, Zhengyan Shi, Zhaoyang Wang, Hao Cheng, Qianhui Wu, Wenlin Yao, Natasha Jaques, Weiyan Shi, Jianfeng Gao
- 链接：[arXiv](https://arxiv.org/abs/2610.14163) · [PDF](https://arxiv.org/pdf/2610.14163) · [HF](https://huggingface.co/papers/2610.14163)

Terminal agents solve tasks in software engineering and scientific research by executing commands in a terminal. Training them via reinforcement learning (RL) requires diverse and verifiable environments, but these environments are still mostly designed by human researchers, so their supply grows only as fast as researchers can work. We introduce AutoEnvScaling, which treats environment design as a terminal task and…

## 55. Rubrics from the Task, Verdicts from Evidence: Pointwise Rubric Rewards with Tool-Augmented Judges

- 分数：12.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：reasoning
- 作者：Tianci Liu, Haoyu Wang
- 链接：[arXiv](https://arxiv.org/abs/2610.18766) · [PDF](https://arxiv.org/pdf/2610.18766) · [HF](https://huggingface.co/papers/2610.18766)

Rubric-based reward models (RMs) evaluate responses against explicit criteria. However, existing methods often derive criteria from observed response candidates, introducing response-induced bias that may limit rubric generalizability. Their judges also struggle with mechanical constraints when relying on reading alone, and commonly used pairwise judges provide only relative preferences, complicating their direct…

## 56. EgoExplorer: A Vision-Motion-Touch Observatory for Human Loco-Manipulation In Situ

- 分数：12.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：evaluation
- 作者：Yunsong Zhou, Xuekun Jiang, Haiqi Shen, Hangxu Liu, Chaojian Shi, Yujie Liu, Jingyuan Li, Haoran Yang, Jiafei Cao, Dongzhan Zhou, Dong Wang, Yao Mu, Chunhua Shen, Weinan Zhang
- 链接：[arXiv](https://arxiv.org/abs/2610.18872) · [PDF](https://arxiv.org/pdf/2610.18872) · [HF](https://huggingface.co/papers/2610.18872)

Learning humanoid loco-manipulation from human demonstrations rests on observing how locomotion, posture, and object interaction evolve together as tasks unfold. Scaling collection across diverse environments, in turn, favors lightweight, portable capture systems. Yet, existing datasets provide only partial views of this coordination. Thus, we introduce EgoExplorer, a 100-hour vision-motion-touch observatory of…

## 57. Same Output, Different Gold: Measuring How Reference Choice Moves a Multilingual Benchmark Score

- 分数：11.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：benchmark
- 作者：Parth Kulshreshtha, Shivali Dalmia, Abhishek Mukherji
- 链接：[arXiv](https://arxiv.org/abs/2610.03825) · [PDF](https://arxiv.org/pdf/2610.03825) · [HF](https://huggingface.co/papers/2610.03825)

A benchmark score compares a system output against a reference, and methodological attention falls almost entirely on the first term. We measure the second. The retained annotation record of a six-language benchmark for personally identifiable information contains two independent annotator labellings, the aggregate shipped as gold, and a reviewer gold from independent expert re-annotation of a sample. Using it, we…

## 58. GeoFix: Geometry Fixing for 4D Consistent Generation

- 分数：10.5  ·  HF 赞：5  ·  来源：huggingface
- 兴趣命中：-
- 作者：Yeobin Hong, Hyojun Go, Dohun Lee, Jeongjae Lee, Sunghwan Hong, Federico Tombari, Zhaochong An, Jong Chul Ye, Konrad Schindler, Dominik Narnhofer
- 链接：[arXiv](https://arxiv.org/abs/2610.14293) · [PDF](https://arxiv.org/pdf/2610.14293) · [HF](https://huggingface.co/papers/2610.14293)

Video diffusion models increasingly serve as priors for 4D generation, but the generated videos often lack geometric consistency. Recent approaches address this through post-training by designing geometric rewards, yet this can degrade texture and fine detail, requiring auxiliary appearance rewards and careful reward balancing. To address this challenge, we propose GeoFix, a unified framework that improves geometric…

## 59. Probable but Not Valid: A Psychometric Audit of Decision Models as Synthetic Survey Respondents

- 分数：10.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：language model
- 作者：Mantas Lukauskas, Viktorija Šarkauskaitė
- 链接：[arXiv](https://arxiv.org/abs/2610.14912) · [PDF](https://arxiv.org/pdf/2610.14912) · [HF](https://huggingface.co/papers/2610.14912)

Language models are increasingly used to create synthetic survey samples, also called silicon samples. Decision models are a new class of language models that return a probability for each point of a rating scale instead of text. We ask whether these models, or the newest generative LLMs, can stand in for human respondents on a psychometric survey. We test fourteen decision models from eleven providers and 47…

## 60. UniForge3D: Joint 3D Reconstruction and Generation in a Shared Anchor-Guided Space

- 分数：9.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：-
- 作者：Wenjue Chen, Wenyue Chen, Heliang Zheng, Rongfei Jia, Yuan Liu, Meng Li
- 链接：[arXiv](https://arxiv.org/abs/2610.15357) · [PDF](https://arxiv.org/pdf/2610.15357) · [HF](https://huggingface.co/papers/2610.15357)

Generating complete 3D assets from sparse, unposed images requires preserving observed geometry while completing unseen regions. Joint reconstruction and generation offers a way to address both goals: reconstruction recovers the geometry observed in the input images, while generation contributes learned shape priors. However, combining camera-relative reconstruction with canonical-space generation introduces a…

## 61. AReA: Adaptive Receptive-Field Attention for Efficient High-Resolution Diffusion Transformers

- 分数：9.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：-
- 作者：Javad Rajabi, Koorosh Roohi, David B. Lindell, Babak Taati
- 链接：[arXiv](https://arxiv.org/abs/2610.17227) · [PDF](https://arxiv.org/pdf/2610.17227) · [HF](https://huggingface.co/papers/2610.17227)

Generating images beyond the training resolution of Diffusion Transformers (DiTs) remains challenging, as the number of tokens grows rapidly with resolution, full attention becomes expensive, and outputs often suffer from structural distortions and degraded detail. We identify uniform full attention as the common source of both problems. Attending to all tokens at every step causes quadratic cost and exposes the…

## 62. DriveWLA: Unifying Future Dynamics and Scene Semantics through World-Language-Action Modeling for Autonomous Driving

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reinforcement learning, evaluation, language model, spec
- 作者：Shuzheng Wang, Haoxuan Li, Shengzhen Li, Chenxi Wu, Yajing Sun, Lu Hou, Wenyu Liu, Xinggang Wang
- 链接：[arXiv](https://arxiv.org/abs/2610.17903) · [PDF](https://arxiv.org/pdf/2610.17903) · [HF](https://huggingface.co/papers/2610.17903)

Vision-Language Models (VLMs) and world models have demonstrated strong capabilities in semantic understanding and future scene evolution for autonomous driving. However, effectively integrating both capabilities for trajectory generation remains challenging. In this work, we propose DriveWLA, a unified World-Language-Action model based on Mixture-of-Transformers (MoT) that jointly models semantic understanding,…

## 63. SpecCloak: Probing Harmful Code Generation through Engineering Specifications

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, language model, large language, coding, spec
- 作者：Wenbin Chen, Jiexin Wang, Guanting Wu, Jiaxi Liang, Yi Cai
- 链接：[arXiv](https://arxiv.org/abs/2610.17907) · [PDF](https://arxiv.org/pdf/2610.17907) · [HF](https://huggingface.co/papers/2610.17907)

The code generation capabilities of large language models (LLMs) can equally be misused to implement harmful functionality, underscoring the need to understand their safety behavior in response to programming requests. While request phrasing is known to influence refusal, it remains unclear whether the form in which coding task requirements are stated affects the refusal process for malicious code generation. We…

## 64. CineMem: Attention-Aligned Fine-grained Memory Retrieval for Multi-Shot Long Video Generation

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, evaluation, spec, retrieval
- 作者：Xiaoxue Wu, Xinyu Gao, Fang Yu, Yu Qiao, Xinyuan Chen
- 链接：[arXiv](https://arxiv.org/abs/2610.17926) · [PDF](https://arxiv.org/pdf/2610.17926) · [HF](https://huggingface.co/papers/2610.17926)

Autoregressive video generation relies on memory retrieval to model long-range dependencies. This capability becomes particularly critical for multi-shot generation, where models must reconcile substantial visual changes across shot transitions with persistent semantic continuity. Existing methods tend to perform memory retrieval at the frame level and share the same historical context across all query tokens,…

## 65. Learning How to Remember: Memory Modality Selection for GUI Agents

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, memory, benchmark, language model
- 作者：Taeyun Roh, Suhyeong Park, Gijin Kim, Wonjune Jang, Jaewoo Kang
- 链接：[arXiv](https://arxiv.org/abs/2610.17928) · [PDF](https://arxiv.org/pdf/2610.17928) · [HF](https://huggingface.co/papers/2610.17928)

Recent advances in vision-language models (VLMs) have substantially improved the capabilities of GUI agents, while memory augmentation has emerged as a promising approach for reusing knowledge from past interactions. However, existing memory augmented GUI agents typically adopt a fixed representation strategy, providing retrieved experience as a static modality. It remains unclear whether a single memory modality is…

## 66. MERIT: Multimodal Evidence Reasoning over Image Tables

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, reinforcement learning, language model, spec, retrieval
- 作者：Haoyang Jiang, Zhuotong Fan, Mingyang Yi, Ju Fan, Lanqing Hu, Xiao Zan
- 链接：[arXiv](https://arxiv.org/abs/2610.17937) · [PDF](https://arxiv.org/pdf/2610.17937) · [HF](https://huggingface.co/papers/2610.17937)

Table reasoning with language models typically assumes access to clean textual tables. In practice, tables are often serialized into text, which can corrupt cell contents, distort structural relationships, and discard visual cues, leaving the model to reason over incomplete evidence. In contrast, table images retain this information, but using it requires both accurate perception and reasoning grounded in the…

## 67. HaloBlock: Faster and Better Decoding for Diffusion Large Language Models

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, benchmark, language model, large language, coding
- 作者：Zhaohui Zheng, Chenhang He, Jinrui Zhang, Ming-Ming Cheng, Lei Zhang
- 链接：[arXiv](https://arxiv.org/abs/2610.17948) · [PDF](https://arxiv.org/pdf/2610.17948) · [HF](https://huggingface.co/papers/2610.17948)

Diffusion large language models (dLLMs) have attracted increasing research attention due to their bidirectional attention and arbitrary order decoding. However, there are two issues in dLLMs inference: the decoding difficulty is dominated by the tokens on the right side of the block, and the block-wise decoding inherently suffers from boundary contextual discontinuity. To tackle these limitations, we propose…

## 68. Agent-Reflex: Teaching Language Agents to Act Reflectively

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, tool-use, reasoning, reinforcement learning, benchmark, language model, large language, spec
- 作者：Guanting Dong, Xinyu Yang, Jiajie Jin, Yuyang Hu, Xiaoshuai Song, Yifei Chen, Xiaoxi Li, Jiejun Tan, Yutao Zhu, Tat-Seng Chua, Ji-Rong Wen, Zhicheng Dou
- 链接：[arXiv](https://arxiv.org/abs/2610.17953) · [PDF](https://arxiv.org/pdf/2610.17953) · [HF](https://huggingface.co/papers/2610.17953)

Large language models have evolved from single-turn chatbots into interactive agents capable of long-horizon reasoning. In real deployments, MCP tool services can return noisy feedback and users may intervene to correct the agent, but existing methods provide limited supervision for reflection learning and failure recovery. To bridge this gap, we propose Agent-Reflex, a general training framework for incentivizing…

## 69. Virtual Head Attention

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, language model, large language, coding
- 作者：Xibo Ding, Guoxia Wang, Jinle Zeng, Jiabin Yang, Sirui Tao, Chao Yang, Dianhai Yu
- 链接：[arXiv](https://arxiv.org/abs/2610.17959) · [PDF](https://arxiv.org/pdf/2610.17959) · [HF](https://huggingface.co/papers/2610.17959)

The design of attention mechanisms in long-context large language models faces an ``impossible triangle'' among KV cache size, training and prefill FLOPs, and model quality. GQA achieves strong quality but incurs high KV cache overhead; alternative approaches such as MLA and MFA can compress the cache, but MLA suffers from quality loss while MFA substantially increases training and prefill compute. We propose…

## 70. BELT : BEhavior-Aligned Low-Rank KV Cache Compression with Learned Top-k Rank Allocation

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, benchmark, language model, large language, coding, spec
- 作者：Yaoyang Liu, Shuwei Shen, Jincheng Tang, Jinguang Liu, Jinbao Xue, Hailong Yang, Ke Zhang, Yinjun Wu
- 链接：[arXiv](https://arxiv.org/abs/2610.17966) · [PDF](https://arxiv.org/pdf/2610.17966) · [HF](https://huggingface.co/papers/2610.17966)

Long-context inference makes the key-value (KV) cache a major memory bottleneck for large language models. We propose BELT, a low-rank KV cache compression framework. Its key-side objective targets attention distributions rather than raw keys or pre-softmax logits, yielding a quadratic surrogate with a closed-form low-rank solution. A learned global rank allocator uses differentiable soft selection during training…

## 71. Match the Canvas, Not Just the Answer: Predictability-Aware SFT for Diffusion Language Models

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, benchmark, language model, coding
- 作者：Miao Li, Hanyang Jiang, Hengyu Fu, Baihe Huang, Yating Liu, Yuhang Cai, Changkun Guan, Zhongzhu Chen, Jiecheng Lu, Michael A. Boateng, Pascal Van Hentenryck
- 链接：[arXiv](https://arxiv.org/abs/2610.18001) · [PDF](https://arxiv.org/pdf/2610.18001) · [HF](https://huggingface.co/papers/2610.18001)

Diffusion language models (DLMs) enable flexible parallel generation by resolving tokens according to the model's evolving predictability rather than a fixed left-to-right order. This flexibility, however, introduces training choices absent from standard autoregressive teacher forcing: which reference tokens are visible when a target is supervised and how much generation space is allocated. Standard supervised…

## 72. SWEPatchTest: Evaluating Software Tests Beyond Reproduction

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, evaluation, benchmark, coding
- 作者：Hua Lu, Pengcheng Wang, Han Li, Zichen Tian, Yanyu Chen, Huang He, Bingjin Chen
- 链接：[arXiv](https://arxiv.org/abs/2610.18004) · [PDF](https://arxiv.org/pdf/2610.18004) · [HF](https://huggingface.co/papers/2610.18004)

Coding agents use generated tests to decide whether a proposed patch satisfies an issue's requirements. A suite that fails on the buggy program and passes after applying the reference patch can still accept an incorrect patch or reject a correct patch. We introduce SWEPATCHTEST, a test-generation benchmark with 619 tasks from SWE-bench Pro, SWE-bench Multilingual, and DeepSWE and 82,579 candidate patches collected…

## 73. Machine--human agreement in marking undergraduate assignments is specific to model, prompt and institution

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, language model, large language, spec
- 作者：Giulio Corsi, Maryam Abo-Tabik, Yael Benn, Georgiana Thorpe Apreutesei, Roni Tibon, Alexandru Marcoci, Deborah Talmi
- 链接：[arXiv](https://arxiv.org/abs/2610.18019) · [PDF](https://arxiv.org/pdf/2610.18019) · [HF](https://huggingface.co/papers/2610.18019)

Large language models (LLMs) promise to automate one of higher education's most resource-intensive activities: assessing student writing. Existing evaluations are typically limited to a single model, a single prompt and a single institution. Using 761 undergraduate psychology assignments from three UK universities, we evaluated three frontier LLMs, individually and in ensemble, on accuracy, prompt sensitivity, error…

## 74. FRACTION: Fraud Explanation Generation via Agentic Graph Context Navigation

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, tool-use, evaluation, language model, large language, spec
- 作者：Cecelia Soh, Jun Hu, Yuan Li, Cheng Chen, Hui Liu, Yanjia Zhu, Hao He, Bryan Hooi, Bingsheng He
- 链接：[arXiv](https://arxiv.org/abs/2610.18023) · [PDF](https://arxiv.org/pdf/2610.18023) · [HF](https://huggingface.co/papers/2610.18023)

Graph fraud explanation generation emerges as an important task, which requires jointly leveraging graph structure and content information to produce human-readable explanations for a given risk label. An intuitive approach is to adapt existing graph-enhanced large language models (LLMs), which inject graph structure into LLMs via graph-conditioned instruction tuning or structure-aware embeddings. However, existing…

## 75. inLoRA-MINT: Internal Representations for Auditing Training Data in Domain-adapted LLMs

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, language model, large language, spec
- 作者：Gonzalo Mancera, Julian Fierrez, Aythami Morales, Ruben Tolosana, Daniel DeAlcala, Francisco Jurado
- 链接：[arXiv](https://arxiv.org/abs/2610.18051) · [PDF](https://arxiv.org/pdf/2610.18051) · [HF](https://huggingface.co/papers/2610.18051)

This work investigates the application of the Membership Inference Test (MINT) to large language models (LLMs) fine-tuned with LoRA, aiming to determine whether specific samples were used during training and address concerns about data privacy, leakage, and transparency. Building on our previous LoRA-MINT framework, which relies exclusively on perplexity under a strict black-box setting, we propose an approach based…

## 76. Can Agents Forget When Asked? A Benchmark for Memory Unlearning in LLM Agents

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, memory, benchmark, language model, large language, retrieval
- 作者：Bofan Xie, Chaokun Wang, Guanchen Ge, Songyao Wang, Fang Niu, Hang Zhang, Wei Wang
- 链接：[arXiv](https://arxiv.org/abs/2610.18052) · [PDF](https://arxiv.org/pdf/2610.18052) · [HF](https://huggingface.co/papers/2610.18052)

Long-term memory has become a core component of large language model (LLM) agents. As agents accumulate personal information over long-term use, users increasingly ask them to delete sensitive or outdated facts. A memory system should honor such requests. It should remove exactly what was requested and keep the rest of its memory intact. However, existing memory benchmarks evaluate only memory writing, retrieval,…

## 77. From Agents to Edges: Paired Optimization for Multi-Agent Collaboration

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, benchmark, language model, spec
- 作者：Feng Lin, Xiaotian Yu, Yifan Yang, Aijun Li
- 链接：[arXiv](https://arxiv.org/abs/2610.18069) · [PDF](https://arxiv.org/pdf/2610.18069) · [HF](https://huggingface.co/papers/2610.18069)

Strong individual agents do not guarantee effective collaboration. Communication must align what one agent conveys with how another interprets and uses it. This dependency makes the communication edge a natural unit of optimization. We introduce Paired Automated Communication Optimization (PACO), which jointly optimizes the instructions at both ends of each edge and their shared communication convention in systems…

## 78. LensErase: A Foundation Model for Erase Anything

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reinforcement learning, evaluation, benchmark, coding, spec
- 作者：Yunuo Chen, Xiuyu Wu, Qinhong Yang, Jinjing Zhao, Yanchen Dong, Sirui Zhang, Dong Chen, Fangyun Wei, Lei Shi, Ji Li, Dongdong Chen, Guo Lu, Yan Lu, Baining Guo
- 链接：[arXiv](https://arxiv.org/abs/2610.18072) · [PDF](https://arxiv.org/pdf/2610.18072) · [HF](https://huggingface.co/papers/2610.18072)

We introduce LensErase, a general-purpose mask-based Erase Anything foundation model designed to cover a broad spectrum of real-world erase scenarios. LensErase supports diverse objects, visual text, watermarks, associated visual effects, multiple-object removal, and a wide range of object scales, aspect ratios, and image resolutions. First, to enable such broad coverage, we construct LensErase-100M, a large-scale…

## 79. Failure Recovery via Belief Updates and World Modeling for Long-Horizon Agents

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reasoning, benchmark, spec
- 作者：Xiyang Wu, Zhichao Liu, Shengxin zhang, Zongxia Li, Ming Li, Tianyi Zhou, Dinesh Manocha
- 链接：[arXiv](https://arxiv.org/abs/2610.18082) · [PDF](https://arxiv.org/pdf/2610.18082) · [HF](https://huggingface.co/papers/2610.18082)

Long-horizon agents often struggle to recover from failures whose causes lie several steps earlier, beyond what local reflection or backtracking can resolve. We introduce BELIEFWEAVER, a framework that combines persistent evidence across attempts with prospective reasoning over repair directions. It maintains a relational belief state over frontiers, attempts, observations, and checkpoints. Execution evidence…

## 80. AReaL-RSI: Adaptive Scaling and Coordination of Recursive Self-Improvement

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, memory, evaluation, spec
- 作者：Wenhao Zhou, Jiajun Song, Haitao Wang, Zipeng Qiu, Yingqi Peng, Ruida Xu, Jiale Li, Wenshuang Li, Shusheng Xu, Wei Dong, Hao Dai, Tongkai Yang, Yi Gao, Binhang Yuan
- 链接：[arXiv](https://arxiv.org/abs/2610.18083) · [PDF](https://arxiv.org/pdf/2610.18083) · [HF](https://huggingface.co/papers/2610.18083)

Scaling recursive self-improvement requires additional computation to produce useful research progress in reaching persistent objectives. Intuitively, more researcher agents can explore more hypotheses, but early evaluation scores might misrepresent their promise, shared findings could lose their applicability conditions, and useful procedures could remain confined to completed investigations. In this paper, we…

## 81. ResearchFlow-Eval: Tracing the Execution Gap in End-to-End Multi-Claim Autoresearch

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, evaluation, spec, planning
- 作者：Peng Jiang, Dongyang Li, Quanying Liu, Xiaoxuan Jia
- 链接：[arXiv](https://arxiv.org/abs/2610.18088) · [PDF](https://arxiv.org/pdf/2610.18088) · [HF](https://huggingface.co/papers/2610.18088)

Autoresearch systems increasingly undertake entire research projects. In practice, scientific research requires systems to pursue multiple interdependent claims through a continuous, multi-stage workflow and revise experiments as evidence accumulates. Existing evaluations of autoresearch systems, however, typically score isolated tasks or final artifacts, leaving these process-level capabilities largely unmeasured.…

## 82. AM-Bench: Understanding Agents under Task Underspecification across Models and Harnesses

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, evaluation, benchmark, spec
- 作者：Kaiyu Huang, Yiting Li, Angyang Gu, Pinjia He, Minchen Yu, Qingjiang Shi
- 链接：[arXiv](https://arxiv.org/abs/2610.18090) · [PDF](https://arxiv.org/pdf/2610.18090) · [HF](https://huggingface.co/papers/2610.18090)

Ambiguous or incomplete task specifications complicate both execution and clarification for language-model agents. Yet agents' responses to these information gaps remain poorly characterized across models and execution harnesses. We present AM-Bench, a benchmark built from 48 tasks adapted from Terminal-Bench 2.0 and Harness-Bench. Each task includes a fully specified reference and six variants spanning ambiguous or…

## 83. LifeSearch: Benchmarking Deep Research Agents for Real-World Life and Productivity

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reasoning, evaluation, benchmark, spec
- 作者：Yibo Wang, Senjie Jin, Yansong Ning, Xinbing Liang, Haotian Luo, Jiazheng Zhang, Yuxuan He, Will Wu,  Clarenceai
- 链接：[arXiv](https://arxiv.org/abs/2610.18092) · [PDF](https://arxiv.org/pdf/2610.18092) · [HF](https://huggingface.co/papers/2610.18092)

Deep research (DR) agents address open-ended information needs through multi-step reasoning, long-horizon web search, and evidence synthesis. However, existing benchmarks primarily focus on academic research or synthetic tasks, leaving DR agents' capabilities in real-world life and professional productivity settings insufficiently evaluated. To bridge this gap, we introduce LifeSearch, a challenging benchmark…

## 84. APT: Feedback-Driven Agentic Post-Training for Text-to-Image Generation

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reinforcement learning, evaluation, benchmark, spec
- 作者：Sirui Zhang, Fangyun Wei, Dong Chen, Jinjing Zhao, Yitong Wang, Yunuo Chen, Baining Guo, Zheng-Jun Zha
- 链接：[arXiv](https://arxiv.org/abs/2610.18097) · [PDF](https://arxiv.org/pdf/2610.18097) · [HF](https://huggingface.co/papers/2610.18097)

Post-training is crucial for improving text-to-image models, yet existing pipelines typically rely on manually curated training data and fixed training distributions. We introduce APT (Agentic Post-Training), a fully automated framework that adaptively post-trains a base model according to its evolving capability profile. APT coordinates three agents to construct evaluation sets from user requirements, diagnose…

## 85. A CaLLM Judge is a Better Judge: Mitigating Bias in LLM-as-a-judge

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, language model, large language, spec
- 作者：Cesare Barbera, Luca Stradiotti, Lorenzo Cascioli, Lorenzo Perini, Niek Tax, Daniel Haimovich, Jesse Davis, Andrea Passerini, Andrea Pugnana
- 链接：[arXiv](https://arxiv.org/abs/2610.18108) · [PDF](https://arxiv.org/pdf/2610.18108) · [HF](https://huggingface.co/papers/2610.18108)

Large language models (LLMs) are increasingly used as judges to predict which of two candidate answers a human evaluator would prefer, providing a scalable alternative when human evaluation is too costly. Unfortunately, LLM judgments can exhibit systematic biases. Prior work has documented position, verbosity or model family of the candidate answers influencing the judge decision rather than their quality, while…

## 86. H-DDCM: Hadamard Codebooks for Fast Generative Image and Video Compression

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, benchmark, coding, spec
- 作者：Or Ronai, Vladimir Kulikov, Tomer Michaeli
- 链接：[arXiv](https://arxiv.org/abs/2610.18125) · [PDF](https://arxiv.org/pdf/2610.18125) · [HF](https://huggingface.co/papers/2610.18125)

Training-free diffusion-based compression methods repurpose the generative priors of a diffusion or a flow model to compress data without retraining them as task-specific codecs. Recent codebook-based approaches such as Turbo-DDCM achieve strong perceptual quality at ultra-low bitrates, but their reliance on dense Gaussian codebooks remains costly in both memory and computation, and scales poorly with the large…

## 87. SparPR: Runtime KV-Cache Recovery for Resource-Constrained LLM Inference on Consumer Hardware

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, language model, large language, spec
- 作者：Jieyun Deng, Keming Hu, Yanghe Liu, Li Feng
- 链接：[arXiv](https://arxiv.org/abs/2610.18140) · [PDF](https://arxiv.org/pdf/2610.18140) · [HF](https://huggingface.co/papers/2610.18140)

Running large language models (LLMs) on consumer hardware is bottlenecked by the key-value (KV) cache, which grows with every decoded token and quickly exhausts the memory and bandwidth of a single consumer GPU. We present SparPR (Sparse Partial Recomputation), a runtime KV-cache recovery mechanism that does not modify model weights and requires no offline training. SparPR couples three online decisions: Query-Aware…

## 88. Benchmarking Multimodal Large Language Models for Zero-Shot Human-Object Interaction

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, evaluation, benchmark, language model, large language, spec
- 作者：Oriol Rabasseda, Zenjie Li, Kamal Nasrollahi, Sergio Escalera
- 链接：[arXiv](https://arxiv.org/abs/2610.18161) · [PDF](https://arxiv.org/pdf/2610.18161) · [HF](https://huggingface.co/papers/2610.18161)

Multimodal Large Language Models (MLLMs) have demonstrated strong zero-shot reasoning across diverse domains, but their potential for Human-Object Interaction (HOI) remains unexplored. Unlike traditional HOI approaches that rely on extensive labeled datasets and fixed interaction taxonomies, MLLMs offer flexible reasoning, making them well-suited for dynamic, real-world scenarios. In this work, we present the first…

## 89. TRACESTEER: Trace Driven Activation Steering for Hallucination Mitigation in Diffusion Language Models

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, language model, large language, spec
- 作者：Xin Zhang, Yili Wang, Yue Tan, Xin He, Rui Miao, Yixin Liu, Yi Chang, Xin Wang
- 链接：[arXiv](https://arxiv.org/abs/2610.18173) · [PDF](https://arxiv.org/pdf/2610.18173) · [HF](https://huggingface.co/papers/2610.18173)

Diffusion large language models (dLLMs) have emerged as a promising alternative to autoregressive LLMs, yet remain susceptible to hallucination. Activation steering offers a promising mitigation approach by guiding parallel token predictions through internal representations. However, existing steering methods largely overlook two characteristics of dLLMs: dynamic denoising states and temporal hallucination risks,…

## 90. QORH: Learning Query-Specific Ordered Rule Hypergraphs for Inductive Knowledge Graph Link Prediction

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, evaluation, benchmark, spec
- 作者：Naixing Xu
- 链接：[arXiv](https://arxiv.org/abs/2610.18198) · [PDF](https://arxiv.org/pdf/2610.18198) · [HF](https://huggingface.co/papers/2610.18198)

Knowledge graph link prediction involving unseen entities and relations requires learning transferable reasoning patterns from observed graph structure. Existing methods based on relation graphs primarily capture pairwise dependencies, limiting their ability to preserve the compositional semantics, relation ordering, and role information of complete path rules. To address this limitation, we propose QORH…

## 91. A Few More Tokens Ahead: Reinforcing Parallelism in Diffusion LLMs

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, language model, large language, spec
- 作者：Jiahao Kuang, Yangfan Gao, Tao Gui, Yuanbin Wu, Qi Zhang, Xuanjing Huang, Tao Ji
- 链接：[arXiv](https://arxiv.org/abs/2610.18200) · [PDF](https://arxiv.org/pdf/2610.18200) · [HF](https://huggingface.co/papers/2610.18200)

Parallel generation is widely regarded as an inherent advantage of diffusion large language models. Yet our fixed-quota evaluation of four representative models reveals severe degradation across mathematics and code, with all scores below 15% at 16 tokens per step. Token-level probes identify local predictive potential near the observed prefix, especially in mathematical text. We propose RePara, which reinforces…

## 92. How Reliable Are Large Language Models for Soil Organic Carbon Assessment? An Australian Benchmark

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, language model, large language, spec
- 作者：Yingxuan Cheng, Tong Li, Yayong Li, Yuchuan Fan, You-Gan Wang, Jinran Wu, Scott Chapman, Geoffrey J. McLachlan
- 链接：[arXiv](https://arxiv.org/abs/2610.18201) · [PDF](https://arxiv.org/pdf/2610.18201) · [HF](https://huggingface.co/papers/2610.18201)

Soil organic carbon (SOC) is an indicator of agricultural soil condition and carbon storage, but numerical outputs from large language models (LLMs) require validation before use in monitoring or management. We evaluated seven general-purpose LLM configurations on three direct-response tasks: estimating 0--10 cm SOC concentrations for 308 Australian paddocks under two information conditions, calculating SOC stock in…

## 93. SWE-MISBEHAVIOR: Benchmarking and Mitigating Boundary Violations in Software Coding Agents

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, evaluation, benchmark, coding
- 作者：Do Xuan Trong, Duc Anh Nguyen, Do Xuan Long, Ngoc-Hai Nguyen, Tongyao Zhu, Duy Dinh, Cayden Chik, Cuong Dang, Jiaying Wu, Xuan-Phi Nguyen, Vinh Van Nguyen, Kenji Kawaguchi, Shafiq Joty, Nancy F. Chen, Min-Yen Kan
- 链接：[arXiv](https://arxiv.org/abs/2610.18206) · [PDF](https://arxiv.org/pdf/2610.18206) · [HF](https://huggingface.co/papers/2610.18206)

We present SWE-MISBEHAVIOR, the first taxonomy and evaluation framework for diagnosing boundary-violating misbehaviors in coding agents. It contains 7.4K human-in-the-loop synthesized samples spanning three layers of agent action space: (i) Code Generation, (ii) File Management, and (iii) System Interaction. Across these categories, SWE-MISBEHAVIOR covers 11 distinct misbehaviors with a fully automated evaluation…

## 94. TextualRL: Textual Reinforcement Learning for Context Management

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reinforcement learning, benchmark, spec
- 作者：Tianyu Huai, Jie Zhou, Bo Mao, Qin Chen, Liang He, Xipeng Qiu
- 链接：[arXiv](https://arxiv.org/abs/2610.18216) · [PDF](https://arxiv.org/pdf/2610.18216) · [HF](https://huggingface.co/papers/2610.18216)

LLM agents can adapt to task feedback by revising the textual context that guides their behavior, without changing their model parameters. However, turning execution rewards into reusable context updates is challenging: individual trajectories offer limited comparative evidence about what to change, while task-specific fixes may overgeneralize when incorporated into a shared context. We introduce TextualRL, a…

## 95. Heading Hierarchy Reconstruction for Complex and Long Documents with Level-Wise Multimodal Memory

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, evaluation, benchmark, language model, retrieval
- 作者：Qian Chen, Xianyin Zhang, Lifan Guo, Chi Zhang
- 链接：[arXiv](https://arxiv.org/abs/2610.18238) · [PDF](https://arxiv.org/pdf/2610.18238) · [HF](https://huggingface.co/papers/2610.18238)

Vision-language models (VLMs) have been widely adopted for document parsing and optical character recognition (OCR), as they can accurately extract page-level elements. However, downstream applications such as retrieval-augmented generation (RAG) also require coherent document-level structure. Although these models indicate heading levels using different numbers of preceding ``\#'' symbols, page-by-page prediction…

## 96. Beyond Answer Sharing: TrueMAD for Targeted Peer Engagement in Multi-Agent Debate

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reasoning, language model, large language, spec
- 作者：Dezheng Bao, Sihang Du, Renhong Huang, Zhizhang Yuan, Yifei Sun, Yang Yang
- 链接：[arXiv](https://arxiv.org/abs/2610.18240) · [PDF](https://arxiv.org/pdf/2610.18240) · [HF](https://huggingface.co/papers/2610.18240)

Multi-agent debate (MAD) aims to improve large language model reasoning by exposing agents to alternative solutions and enabling iterative revision. However, standard broadcast-style MAD makes peer answers visible without requiring agents to engage with a particular peer claim. As a result, reliable reasoning may be suppressed by conflicting or majority responses, limiting achievable performance, while erroneous…

## 97. Are We Testing Too Much? A Survey of Benchmark Compression for Efficient Evaluation of Large Language Models

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, language model, large language
- 作者：Guoming Ling, Yupei Lin, Zhongzhan Huang, Junxin Li, Junjie Liu, Shanshan Zhong, Hefeng Wu, Liang Lin
- 链接：[arXiv](https://arxiv.org/abs/2610.18248) · [PDF](https://arxiv.org/pdf/2610.18248) · [HF](https://huggingface.co/papers/2610.18248)

Benchmarks are essential for evaluating and improving large language models (LLMs). Yet many widely used benchmarks are redundant, making evaluation unnecessarily expensive. Benchmark compression lowers this cost by estimating full-benchmark scores and rankings from a partial evaluation. Research in this area has grown rapidly since 2024, but to our knowledge no survey has systematically organized its methods and…

## 98. Output Discipline Sets the Floor: A Falsification-Guided, Model-Agnostic Agent Protocol for Auditable Hypothesis-Driven Decision Making

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reasoning, benchmark, language model, large language
- 作者：Jing Liu, Yongxing Qi, Ping Yao, Ting Wu
- 链接：[arXiv](https://arxiv.org/abs/2610.18298) · [PDF](https://arxiv.org/pdf/2610.18298) · [HF](https://huggingface.co/papers/2610.18298)

What binds large language models on auditable, hypothesis-driven decision tasks, where every candidate can be checked against the evidence? On the public TCMEval-SDT benchmark for Traditional Chinese Medicine syndrome differentiation (200 cases), the binding constraint is output discipline and reasoning structure, not model capability alone: two years of model scaling move zero-shot scores by only -0.03 to +0.08,…

## 99. Lightweight but Linguistically Fair? Quantisation Robustness across Bavarian, German, and English

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, evaluation, benchmark, language model, large language
- 作者：Jophin John, Michael Hoffmann, Piroska Lendvai, Florent Dufour
- 链接：[arXiv](https://arxiv.org/abs/2610.18343) · [PDF](https://arxiv.org/pdf/2610.18343) · [HF](https://huggingface.co/papers/2610.18343)

Post-training quantisation reduces the memory cost of large language models, but it remains unclear whether compression preserves language skills of regional varieties as reliably as their standard-language counterparts. We study this question for Bavarian, Standard German, and English using BAVGROUND, a multiple-choice benchmark, where 206 source questions are aligned across all three languages. Across 14…

## 100. Let the Mind Conceive, Let the Hand Achieve: Following Multimodal Instructions for Long-Horizon Robotic Manipulation

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, benchmark, spec, planning
- 作者：Youpeng Wen, Gang Wang, Tianyu Huang, Weiwei Zhang, Zhijian Huang, Wei Chen, Xieyuanli Chen, Yunhui Liu
- 链接：[arXiv](https://arxiv.org/abs/2610.18352) · [PDF](https://arxiv.org/pdf/2610.18352) · [HF](https://huggingface.co/papers/2610.18352)

A robot following a multi-step instruction needs to act on the right objects in the right order, even as the scene changes. It must also maintain awareness of task progress and determine when to advance. To address these challenges, we introduce Orchestra, an agent harness that separates task planning and execution management from action generation. Orchestra decomposes a complete multimodal instruction into ordered…

## 101. Choosing LLMs for Strategic Agent Interactions

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, evaluation, benchmark, language model, large language, spec
- 作者：Arastun Mammadli, Herbert Woisetschläger, Jawad Fayaz, Shiqiang Wang
- 链接：[arXiv](https://arxiv.org/abs/2610.18354) · [PDF](https://arxiv.org/pdf/2610.18354) · [HF](https://huggingface.co/papers/2610.18354)

Game-theoretic benchmarks claim that large language model (LLM) strategic decision-making varies across game types, interaction structures, and capability dimensions. However, they only evaluate strategic performance across individual fixed models. In parallel, contemporary LLM routers pick models under quality-cost trade-offs, but with no notion of a strategic structure. They do not account for an opponent that…

## 102. ABot-ER: Unified Embodied Reasoning through Agentic Data-Model Co-Evolution

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reasoning, evaluation, benchmark, spec, planning
- 作者：Qiuyu Ding, Heng-Da Xu, Changda Xia, Jiajun Shen, Zihao Guan, Zhengchen Yuan, Jianfang Zhang, Di Yang, Jiayi Tian, Yuting Xu, Fei Wang, Shiao Liu, Wei Zhang, Xiaolong Wu, Wenbin Tang, Zedong Chu, Mu Xu
- 链接：[arXiv](https://arxiv.org/abs/2610.18355) · [PDF](https://arxiv.org/pdf/2610.18355) · [HF](https://huggingface.co/papers/2610.18355)

We introduce \textbf{ABot Embodied Reasoning (ABot-ER)}, a unified embodied reasoning foundation model that breaks the tension between breadth and depth in embodied reasoning. Embodied intelligence demands the joint mastery of perception, planning, and execution, yet reconciling generality with specialization across this spectrum remains an open challenge. Within a single unified model, ABot-ER commands…

## 103. Hallucination-aware Faithful Reasoning in Remote Sensing

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, benchmark, language model, large language
- 作者：Yi Liu, Jing Zhang, Xiang Feng, Xiaoyu Tian, Haonan Guo, Di Wang, Zengmao Wang, Bo Du
- 链接：[arXiv](https://arxiv.org/abs/2610.18369) · [PDF](https://arxiv.org/pdf/2610.18369) · [HF](https://huggingface.co/papers/2610.18369)

Multimodal large language models (MLLMs) have demonstrated promising capabilities for remote sensing reasoning, yet they frequently generate visually unsupported reasoning that contradicts the visual evidence. Existing post-training methods optimize primarily for final-answer correctness, providing limited supervision for identifying and correcting hallucinations that arise during the reasoning process. To address…

## 104. ReDiS: Reasoning-Diagnosis Self-Evolution for Multimodal Reasoning in Remote Sensing

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, evaluation, language model, large language, spec
- 作者：Yi Liu, Wentao Jiang, Shuo Ni, Zhiming Luo, Di Wang, Zengmao Wang, Jing Zhang, Bo Du
- 链接：[arXiv](https://arxiv.org/abs/2610.18388) · [PDF](https://arxiv.org/pdf/2610.18388) · [HF](https://huggingface.co/papers/2610.18388)

Multimodal large language models (MLLMs) have shown strong potential for remote sensing understanding, yet reliable reasoning remains challenging when tasks require fine-grained visual grounding and multi-step inference. Existing approaches typically rely on either costly pre-constructed reasoning trajectories or self-generated signals such as response consistency, which can reinforce shared errors and provide…

## 105. Bifocal: Training-Free Mixed Granularity Visual Token Pruning for Multimodal LLMs

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, language model, large language
- 作者：Peiran Yin, Hao Wu, Zihao Yang, Fengyu Zhou, Yijuan Liang, Haozhe Hu, Xudong Wang, Wei Zhang, Xiaoyu Shen
- 链接：[arXiv](https://arxiv.org/abs/2610.18399) · [PDF](https://arxiv.org/pdf/2610.18399) · [HF](https://huggingface.co/papers/2610.18399)

Visual token pruning for multimodal large language models (MLLMs) appears highly effective, with existing methods retaining over 95% of unpruned performance on common VQA benchmarks using a quarter of the visual tokens or fewer. However, our extensive evaluation of ten methods across three MLLM families and five ability groups reveals a critical gap: strong general performance often comes at the cost of severe…

## 106. Do Factuality Methods Make LLMs More Factual? Reproducibility and Fair Comparison

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, language model, large language, spec, retrieval
- 作者：Pratuat Amatya, Vinay Setty, V Venktesh, Avishek Anand
- 链接：[arXiv](https://arxiv.org/abs/2610.18415) · [PDF](https://arxiv.org/pdf/2610.18415) · [HF](https://huggingface.co/papers/2610.18415)

Large Language Models (LLMs) are aligned to human preferences, after pre-training and supervised fine-tuning steps. However, standard RL alignment steps such as RLHF do not focus on factuality of LLMs, hence they may generate non-factual information, which could result in unintended consequences. In response, a number of factuality alignment approaches have been proposed in the literature which claim to improve…

## 107. EmoGenie: Benchmarking and Evaluating Expressed and Evoked Emotion in T2I Generation with MLLMs

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, language model, large language, spec
- 作者：Zixuan Xing, Lancheng Gao, Shengyan Li, Huiyu Duan, Zhaolin Cai, Guangtao Zhai, Xiongkuo Min
- 链接：[arXiv](https://arxiv.org/abs/2610.18455) · [PDF](https://arxiv.org/pdf/2610.18455) · [HF](https://huggingface.co/papers/2610.18455)

Rapid advances in artificial intelligence-generated content (AIGC) have significantly promoted using text-to-image (T2I) models to generate images with specific affective intentions. However, the emotional effects conveyed by generated images frequently deviate from target expectations, and it remains unclear whether multimodal large language models (MLLMs) can reliably interpret the emotion of AI-generated visual…

## 108. Kairos: Transactional Security Enforcement at the System Boundary for LLM Agents

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, benchmark, language model, large language, spec
- 作者：Kristoffer Hempel, Nils Loose, Lorenzo Cavallaro, Thomas Eisenbarth
- 链接：[arXiv](https://arxiv.org/abs/2610.18457) · [PDF](https://arxiv.org/pdf/2610.18457) · [HF](https://huggingface.co/papers/2610.18457)

Large language model (LLM) agents are becoming an integral part of the software development lifecycle, and the capabilities granted to them allow an agent to act with the user's authority on any resource it can access. The reach that gives an agent its utility is equally available to an attacker who can steer it. Anything an agent ingests can carry an injected instruction, and since the model does not reliably…

## 109. Teacher-Guided Tool Learning for Small Language Models via Bidirectional KL Constraints

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：tool use, reinforcement learning, language model, spec
- 作者：Haoxuan Gao, Qin-Wen Luo, Xiang Chen, Yu Tian, Zequn Sun, Xiaofeng Cao, Jiangchao Yao, Sheng-Jun Huang
- 链接：[arXiv](https://arxiv.org/abs/2610.18459) · [PDF](https://arxiv.org/pdf/2610.18459) · [HF](https://huggingface.co/papers/2610.18459)

External tools can extend the capabilities of small language models (SLMs), enabling their deployment in resource constrained environments. However, their limited capabilities make it difficult for SLMs to discover effective tool use behaviors through reinforcement learning alone, while direct teacher supervision suffers from teacher student behavioral distribution mismatch and may propagate erroneous preferences.…

## 110. EgoOmniWorld: Unifying Egocentric Understanding via Ego-Action-World Interactions

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, language model, large language
- 作者：Songruo Chen, Yuqian Fu, Yu Li, Mingkang Dong, Sifan Zhou, Bin Ren, Xu Zheng, Tianwen Qian, Mohamed Elhoseiny, Yanwei Fu
- 链接：[arXiv](https://arxiv.org/abs/2610.18499) · [PDF](https://arxiv.org/pdf/2610.18499) · [HF](https://huggingface.co/papers/2610.18499)

Egocentric video understanding spans diverse capabilities, modalities, and evaluation formats, yet these are often studied in isolation despite their tight coupling in real-world interaction. We propose the Ego-Action-World interaction loop as a unifying principle: the wearer perceives the world, forms goals, acts, changes the world, and uses feedback to guide subsequent behavior. Based on this view, we introduce…

## 111. How Low Can You Go: Fine-Tuning LLMs with Bayesian Optimization (LlMBO)

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, benchmark, language model, large language, coding
- 作者：Aditya Kulkarni, Davide Sartor, Carlos Soto, Nathan Wycoff
- 链接：[arXiv](https://arxiv.org/abs/2610.18504) · [PDF](https://arxiv.org/pdf/2610.18504) · [HF](https://huggingface.co/papers/2610.18504)

Recently, Morris et al. introduced TinyLoRA, a strategy for LLM fine-tuning which introduces arbitrarily few parameters, and demonstrated accuracy improvements using less than $10$ parameters rather than the ${\gtrsim 10,000}$ typically demanded by LoRA-based methods. However, that study continued to use gradient-based local search methods of the kind deployed for training multi-billion parameter LLMs in the first…

## 112. The Last Mile of Coding Agents for Long-Document Tasks: An Empirical Study on Clinical Trial Protocol Digitization

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, evaluation, benchmark, coding, spec
- 作者：Jiacheng Lin, Geoffrey Low, Nishit Agarwal, Rahul Jain, Afrah Shafquat, Mandis Beigi, Jimeng Sun
- 链接：[arXiv](https://arxiv.org/abs/2610.18507) · [PDF](https://arxiv.org/pdf/2610.18507) · [HF](https://huggingface.co/papers/2610.18507)

Clinical trial protocols serve as the source of truth for study design, but are mostly written and used as unstructured PDF documents. Digitizing protocols turns static content into structured, machine-readable data that clinical software can analyze, validate, and execute. Coding agents, which select tools, execute code, and revise their approach as they work, are increasingly applied to such long-document tasks,…

## 113. UNITAS: A 3D-Native World Action Model for Embodied Manipulation

- 分数：8.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：-
- 作者：Ruixiang Wang, Yongyi Su, Wenlve Zhou, Bo Yue, Hengyan Liu, Dekun Lu, Yuxin Tian, Yihan Fang, Zerui Wu, Xing Hu, Jietao Chen, Yong Guo, Ziyan He, Junbin Yuan, Guiliang Liu, Xiaofen Xing, Kui Jia
- 链接：[arXiv](https://arxiv.org/abs/2610.12099) · [PDF](https://arxiv.org/pdf/2610.12099) · [HF](https://huggingface.co/papers/2610.12099)

World action models (WAMs) aim to answer a coupled physical question: given a task instruction, what motion should the robot execute, and how will that motion change the surrounding world? Most existing WAMs build on pretrained video generators and represent world evolution through images or visual latents. Robotic interaction, however, takes place in metric three-dimensional space, while images are view-dependent…

## 114. ShellElastic: Scalable Elastic Pretraining with Simultaneous Maximal Updates and Hyperparameter Transfer

- 分数：8.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：-
- 作者：Can Jin, Yan Kang, Yifan Gong, Chongjian Ge, Mingze Xu, Yuanjun Xiong, Dimitris N. Metaxas, Hongwu Peng
- 链接：[arXiv](https://arxiv.org/abs/2610.15124) · [PDF](https://arxiv.org/pdf/2610.15124) · [HF](https://huggingface.co/papers/2610.15124)

Foundation models need to support diverse inference budgets, yet training a separate model for each budget duplicates pretraining effort. Elastic models train several nested sub-networks inside one weight-shared supernet, but existing recipes face three obstacles: variable per-step workloads that hinder distributed scaling, limited hyperparameter (HP) transfer across model sizes, and no guarantee that all…

## 115. CIViC: Evidence Gates for Audio-Conditioned Visual Prediction on Proxy Tasks

- 分数：8.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：-
- 作者：Mengzhe Geng, Max W. Y. Lam, Yuewen Cao, Shoukang Hu, Jing Xu, Marc Tessier, Xu Li
- 链接：[arXiv](https://arxiv.org/abs/2610.15327) · [PDF](https://arxiv.org/pdf/2610.15327) · [HF](https://huggingface.co/papers/2610.15327)

Removing audio can shift a visual predictor's output without showing whether the task uses the intended audio information. We introduce Conditional Input and Visual Interpretation Checks (CIViC), a four-gate protocol that links an interpretation to an intervention, held-out task comparison, or endpoint control. We demonstrate CIViC on actor-disjoint face-raster tests, a synthetic audio-feature mixture, and…

## 116. Searching for What Matters: Open-Ended Discovery of Multiple Hypotheses with Agentic Data Exploration

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, benchmark, spec
- 作者：Sanchit Kabra, Nurendra Choudhary, Jiangshu Du, Eddie Huang, Danai Koutra, Chandan K Reddy
- 链接：[arXiv](https://arxiv.org/abs/2610.17874) · [PDF](https://arxiv.org/pdf/2610.17874) · [HF](https://huggingface.co/papers/2610.17874)

Discovering what drives an outcome from data is central to science and often requires deciding what is worth investigating before a specific hypothesis is known. Yet most existing hypothesis generation settings substantially narrow this search by providing a research question, target relationship, or curated context. We introduce open-ended multiple hypothesis discovery, where a system receives only a large tabular…

## 117. Training LLMs for Multi-Agent Collaboration with Verifiable Information Rewards

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, language model, large language
- 作者：Keru Chen, Sen Lin, Yingbin Liang, Nathaniel D. Bastian, Shaofeng Zou
- 链接：[arXiv](https://arxiv.org/abs/2610.17893) · [PDF](https://arxiv.org/pdf/2610.17893) · [HF](https://huggingface.co/papers/2610.17893)

Effective collaboration among large language model (LLM) agents in multi-agent systems requires sharing relevant evidence, requesting missing information, and incorporating teammates' contributions into decisions. Training these behaviors is challenging because final task outcomes provide limited feedback on the value of individual messages. We introduce CoSIR (Collaboration via Surprisal-based Information Rewards),…

## 118. Interaction-as-a-Judge

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, evaluation, coding
- 作者：Wayne Chi, I-Hung Hsu, Li Chen, Wei-Lin Chiang, Ion Stoica, Anastasios Nikolas Angelopoulos, Ameet Talwalkar, Chris Donahue, Cho-Jui Hsieh
- 链接：[arXiv](https://arxiv.org/abs/2610.17895) · [PDF](https://arxiv.org/pdf/2610.17895) · [HF](https://huggingface.co/papers/2610.17895)

Coding agents are tasked with producing sophisticated interactive applications such as websites, desktop applications, and games. While humans assess these applications interactively, current automated LLM evaluations primarily focus on code analysis and unit tests. This mismatch can cause LLM judges to miss failures that are immediately apparent to human users. We study Interaction-as-a-Judge, an evaluation…

## 119. PaceReasoner: Label-Free Learning to Answer Briefly from Long Reasoning

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, reinforcement learning, benchmark
- 作者：Changguo Jia, Zhiyou Xiao, Xinbei Ma, Geng Chen, Weiming Zhang, Yiming Xu, Tianqi Zhao, Minghui Zhou
- 链接：[arXiv](https://arxiv.org/abs/2610.17900) · [PDF](https://arxiv.org/pdf/2610.17900) · [HF](https://huggingface.co/papers/2610.17900)

Extended chain-of-thought reasoning improves problem-solving performance but increases inference cost and latency, motivating more accurate answers with shorter reasoning. We introduce PaceReasoner, a label-free test-time reinforcement learning framework that uses a model's LONG responses to improve its SHORT-mode accuracy. Both modes share a trainable policy, creating a need for reliable supervision, sufficient…

## 120. Batch-Paced: Fixed-Budget Batch Decoding in Discrete Diffusion Language Models

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, language model, coding
- 作者：Shuai Zhang, Zhanchao Zhou, Huachuan Qiu, Anqi Li, Zhenzhong Lan
- 链接：[arXiv](https://arxiv.org/abs/2610.17917) · [PDF](https://arxiv.org/pdf/2610.17917) · [HF](https://huggingface.co/papers/2610.17917)

As generative language models become more capable and widely used, inference demand grows, making efficient serving increasingly important. Discrete diffusion language models (dLLMs) offer a promising path to more efficient inference through parallel token generation. Prior dLLM decoding methods, however, focus on improving inference efficiency for individual sequences. We formulate fixed-budget dLLM batch decoding…
