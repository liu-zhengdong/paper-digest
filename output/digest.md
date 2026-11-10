# 每日 AI 论文

生成时间：2026-11-10 07:19 UTC  ·  共 120 篇（已按 arXiv ID 去重）

来源：Hugging Face Daily Papers + arXiv（cs.AI / cs.LG / cs.CL / cs.CV）。
排序：HF 上榜、点赞、多源命中、兴趣词。兴趣词可在 `config.json` 改。

## 1. Toward the Era of Agentic Embodied Intelligence

- 分数：32.5  ·  HF 赞：37  ·  来源：huggingface
- 兴趣命中：agent, benchmark, spec
- 作者：Chao Liang, Ke Chen, Fengxiaoxiao Li, Shibo Huang, Yufeng Sun, Zhaokai Yin, Jianhuan Lai, Haozhe Feng, Chenghuan Jia, Zhipeng Zhang
- 链接：[arXiv](https://arxiv.org/abs/2611.09124) · [PDF](https://arxiv.org/pdf/2611.09124) · [HF](https://huggingface.co/papers/2611.09124)

Foundation models increasingly guide robot actions, yet sustained autonomy requires efficient control and failure recovery. We introduce A2-MEAS, an embodied multi-agent framework built around code as a scaling interface. Learned correction codes combine corrective language, spatial evidence, execution history, and action proposals. MetaBrain provides training supervision and runtime guidance. A correction encoder…

## 2. Confucius4-R2T2: A Stable-Prefix Streaming ASR Model for Real Real-Time Transcription

- 分数：32.0  ·  HF 赞：78  ·  来源：huggingface
- 兴趣命中：agent, evaluation
- 作者：Daniel Huang, Qi He, Shaoxiong Duan, Yingjie Li, Qiao Cheng, Yitao Duan
- 链接：[arXiv](https://arxiv.org/abs/2611.06043) · [PDF](https://arxiv.org/pdf/2611.06043) · [HF](https://huggingface.co/papers/2611.06043)

Streaming speech recognition is increasingly consumed by machines, such as translators and voice agents, that act on each token as it appears. A token that is later revised costs wasted work or a wrong action. In this work, we present Confucius4-R2T2 (short for Real Real-Time Transcription), a stable-prefix streaming ASR model that never modifies its earlier output while maintaining high accuracy and low latency.…

## 3. OneTrans-GSR: A Generative Slate Ranking Paradigm Unifying Reranking and Mix-Ranking with One Autoregressive Transformer

- 分数：31.0  ·  HF 赞：30  ·  来源：huggingface
- 兴趣命中：reinforcement learning, evaluation, coding, spec
- 作者：Feng Cheng, Yu-Hsuan Huang, Fengyi Wang, Chaofan Zhou, Zhennan Zhu, Huan He, Bo Zhang, Ruoqi Zhang, Zhanfeng Mo, Ziwei Liu, Lanyi Li, Yifeng Pan, Junhua Long, Ziqiu Zhou, Yue Lin, Shaowei Liu
- 链接：[arXiv](https://arxiv.org/abs/2611.04720) · [PDF](https://arxiv.org/pdf/2611.04720) · [HF](https://huggingface.co/papers/2611.04720)

Industrial recommender systems allocate substantial computation to pointwise candidate scoring, yet separate reranking and mix-ranking stages still assemble the final exposure slate using hand-crafted rules and specialized low-capacity models. Mix-ranking combines product cards, short videos, livestreams, and advertising cards supplied by distinct upstream business channels. Although these rules and models encode…

## 4. LongBanana: An Expert-Verified Benchmark for Long-Context Multi-Reference Image Synthesis

- 分数：31.0  ·  HF 赞：30  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark, spec
- 作者：Haoxiang Cao, Yuxuan Zhang, Penghui Du, Bo Li, Jiajiong Cao, Yingying Fan, Zimeng Wu, Yifu Luo, Mingzhe Zheng, Junwen Miao, Huaisong Zhang, Yang Yao, Yu Wang, Dongfu Jiang, Ping Nie, Wenhu Chen, Chaoqun Wang, Changqian Yu, Kelsey R. Allen
- 链接：[arXiv](https://arxiv.org/abs/2611.06856) · [PDF](https://arxiv.org/pdf/2611.06856) · [HF](https://huggingface.co/papers/2611.06856)

We introduce LongBanana, to our knowledge the first expert-designed and expert-verified benchmark for long-context multi-reference image synthesis in the age of agent-driven image generation. The task requires retrieving dispersed visual evidence, rejecting distractors, binding entities and relations, and composing one coherent final image from multiple references. LongBanana contains 90 carefully designed tasks…

## 5. PCBRouteAgent: How Close Are LLM Agents to Becoming PCB Routing Engineers?

- 分数：30.5  ·  HF 赞：37  ·  来源：huggingface
- 兴趣命中：agent, spec
- 作者：Yue Zhang, Jilei Sun, Liqiang Jing, Yijie Wei, Ruohan Yang
- 链接：[arXiv](https://arxiv.org/abs/2611.08175) · [PDF](https://arxiv.org/pdf/2611.08175) · [HF](https://huggingface.co/papers/2611.08175)

Automating printed circuit board (PCB) routing requires coordinating board-level connectivity decisions with geometric execution under strict design rules. Although recent agents can interact with native routing tools, reliable routing on complex boards remains challenging. We present PCBRouteAgent, a multimodal PCB routing agent inspired by how human engineers coordinate global strategy with local execution. A…

## 6. SplatAnything: Gaussian Spacing Normalization for Feed-forward 3DGS across Arbitrary Scenes

- 分数：30.0  ·  HF 赞：64  ·  来源：huggingface
- 兴趣命中：benchmark
- 作者：Hao Yu, Zhenwei Wang, Yongzhen Hu, Yuning Gong, Junta Wu, Xiaowei Zhou, Hujun Bao, Tengfei Wang, Chunchao Guo, Sida Peng
- 链接：[arXiv](https://arxiv.org/abs/2611.08264) · [PDF](https://arxiv.org/pdf/2611.08264) · [HF](https://huggingface.co/papers/2611.08264)

We identify a key limitation of existing feed-forward 3DGS methods: Gaussian attributes are typically predicted in a radial-distance-normalized space that canonicalizes a global radial statistic of the reconstructed geometry, while the spacing between neighboring Gaussian centers can still vary substantially across scene scales and camera configurations. This mismatch induces systematic shifts in Gaussian-scale…

## 7. WorldFoundry: Towards Unified Infrastructure for World Intelligence

- 分数：30.0  ·  HF 赞：32  ·  来源：huggingface
- 兴趣命中：evaluation, benchmark, spec
- 作者：Juanxi Tian, Jiadong Hou, Baiang Li, Xin Lin, Zhengbo Jiao, Weijia Zhang, Yeying Jin, Truong Nguyen, Haitian Zheng, Zhifei Zhang, Jianfei Yang, Ming-Hsuan Yang, Felix Heide, Wei Xiong, Enze Xie, Wanhua Li
- 链接：[arXiv](https://arxiv.org/abs/2611.10771) · [PDF](https://arxiv.org/pdf/2611.10771) · [HF](https://huggingface.co/papers/2611.10771)

Visual generative models increasingly blur the line between synthesizing observations and simulating environments. Yet visual plausibility alone does not constitute successful world modeling: compelling outputs may lack persistent state, physical dynamics, or causally consistent responses to interactions. We define a generative world model as a predictive dynamical system that maintains a persistent,…

## 8. P^2-MOPD: Accelerating Multi-Teacher On-Policy Distillation via Parameter Priors

- 分数：28.0  ·  HF 赞：48  ·  来源：huggingface
- 兴趣命中：-
- 作者：Sinuo Wang, Jiacheng Lu, Zeyu Zhang, Maojia Song, Rui Sun, Beidi Luan, Yutong Xie, Jing Li, Daxin Jiang, Qi Wu, Zuo Bai
- 链接：[arXiv](https://arxiv.org/abs/2611.03953) · [PDF](https://arxiv.org/pdf/2611.03953) · [HF](https://huggingface.co/papers/2611.03953)

Multi-teacher on-policy distillation consolidates expert capabilities by supervising student-generated trajectories, whereas task arithmetic offers a training-free alternative through linear parameter combinations. We view the linear combination of student and expert parameters as a single differentiable model and propose P^2-MOPD, which jointly optimizes the mixing coefficients and the student weights under the…

## 9. LLMs Don't Know What They Know: Benchmarking Temporal Self-Knowledge for Financial Backtesting

- 分数：28.0  ·  HF 赞：28  ·  来源：huggingface
- 兴趣命中：benchmark, language model, large language
- 作者：Lingfei Qian, Yan Wang, Xueqing Peng, Yupeng Cao, Yuechen Jiang, Zhuohan Xie, Anke Xu, Wenbo Cao, Jiarui Chen, Zehan Li, Jimin Huang, Alejandro Lopez-Lira, Yuehua Tang, Sophia Ananiadou, Jian-Yun Nie
- 链接：[arXiv](https://arxiv.org/abs/2611.06808) · [PDF](https://arxiv.org/pdf/2611.06808) · [HF](https://huggingface.co/papers/2611.06808)

Financial backtests of large language models (LLMs) are meaningful only if the model did not already know the outcomes it is asked to predict. Practitioners guard against this by trusting a vendor's stated knowledge cutoff, by asking the model what it knows, or by instructing it to answer as of a past date. To verify whether any of these safeguards can be trusted, we introduce FinDendro, a benchmark of 2,226 dated…

## 10. Beneath the Surface: What We Overlook When We Talk About Agent Evolution

- 分数：27.5  ·  HF 赞：23  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark, coding, spec
- 作者：Xiaobo Wang, Zimu Wang, Siyu Ye, Jiaqi Li, Min Tang, Jun Bai, Yuling Shi, Ruobing Wang, Jingjing Zhang, Chaofan Wang, Kai Wu, Mengnan Qi, Kai Cai, Xiaodong Gu, Qi Liu, Zilong Zheng
- 链接：[arXiv](https://arxiv.org/abs/2611.07624) · [PDF](https://arxiv.org/pdf/2611.07624) · [HF](https://huggingface.co/papers/2611.07624)

Agent harness evolution enables recursive self-improvement (RSI) without updating model weights. We examine whether higher benchmark scores yield reliable, efficient, and transferable improvement. We evaluate four methods across harnesses, general and coding tasks. Repeated evaluations, controlled agent expansion, component interventions, and admission replays reveal recurring patterns. All sixteen evolved agents…

## 11. EvoWorld: Towards Out-of-Sight World Evolution in Generative Video Models

- 分数：22.0  ·  HF 赞：20  ·  来源：huggingface
- 兴趣命中：reasoning, language model
- 作者：Yequan Bie, Dengyang Jiang, Zhixuan Chen, Xiaozhuan Liang, Haoxuan Che, Quande Liu, Xi Chen, Hao Chen
- 链接：[arXiv](https://arxiv.org/abs/2611.06748) · [PDF](https://arxiv.org/pdf/2611.06748) · [HF](https://huggingface.co/papers/2611.06748)

Generative video models are increasingly used as visual world simulators, yet their primary strength lies in rendering plausible pixels rather than reasoning about how a world should evolve. Coherent world evolution requires more than visual fidelity: when an event occurs, a model must infer its consequences for the entities in the world and then render the resulting state. For example, after a wild beast appears,…

## 12. Video-Coder: Reinforcing Agentic Coding for Video Generation

- 分数：22.0  ·  HF 赞：16  ·  来源：huggingface
- 兴趣命中：agent, reinforcement learning, coding
- 作者：Chaoyang Wang, Sicheng Gao, Junan Hu, Kunyang Li, Dongyang Chen, Yiyang Zhou, Huaxiu Yao, Yong Jae Lee, Radu Timofte, Yuzhang Shang
- 链接：[arXiv](https://arxiv.org/abs/2611.09894) · [PDF](https://arxiv.org/pdf/2611.09894) · [HF](https://huggingface.co/papers/2611.09894)

Recent years have witnessed remarkable progress in video generation in terms of visual quality and temporal consistency. However, generating videos with precise spatial structure, coherent motion dynamics, and controllable scene composition remains challenging. In this paper, we introduce Video-Coder, the first attempt to train a code-driven video generation agent, which autonomously writes and executes code to…

## 13. Fast and Exact Relative-Position Attention via Structure-Aware Kernels

- 分数：21.5  ·  HF 赞：19  ·  来源：huggingface
- 兴趣命中：memory, spec
- 作者：Delyan Boychev, Ivo Petrov, Dimitar I. Dimitrov
- 链接：[arXiv](https://arxiv.org/abs/2611.01182) · [PDF](https://arxiv.org/pdf/2611.01182) · [HF](https://huggingface.co/papers/2611.01182)

Relative-position attention mechanisms offer compelling alternatives to RoPE across various transformer architectures, delivering superior performance in domains such as audio. These mechanisms typically modify attention scores by adding content-position or bias-position terms. Unlike RoPE, which encodes position via per-token rotations directly on the queries and keys, relative-position terms generally require…

## 14. Exploring Weight-Space Programming: Capabilities, Generalization, and Limitations

- 分数：21.5  ·  HF 赞：11  ·  来源：huggingface
- 兴趣命中：agent, reasoning, evaluation, benchmark, spec
- 作者：Junru Hu, Cheng Tang, Wei Li, Hongze Zhu, Chun-Mei Feng, Qi Zhang, Yirong Chen, Ming Hu
- 链接：[arXiv](https://arxiv.org/abs/2611.09382) · [PDF](https://arxiv.org/pdf/2611.09382) · [HF](https://huggingface.co/papers/2611.09382)

Weight-Space Programming (WSP) enables reasoning agents to directly inspect and modify neural network parameters, offering an alternative to gradient-based model adaptation. However, its capabilities, cross-task generalization, and practical limitations remain insufficiently understood. We systematically investigate WSP through 16 editing trajectories across seven benchmarks and two model scales (Qwen3.5-0.8B and…

## 15. Frontier3DBench: Benchmarking Coding Agents for 3D Creation across Objects, Scenes, and Interactive Open Worlds

- 分数：21.0  ·  HF 赞：10  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark, coding, spec
- 作者：Xinjie Lin, Qingle Liu, Wenyi Li, John Lam, Xiaoqiu Wang, Deyao Hong, Mingju Gao, Zheng Jiang, Yizhe Chi, Youjie Zheng, Calvin Xiao, Kaisen Yang, Huan-ang Gao
- 链接：[arXiv](https://arxiv.org/abs/2611.09017) · [PDF](https://arxiv.org/pdf/2611.09017) · [HF](https://huggingface.co/papers/2611.09017)

Coding agents combine visual understanding with program execution, offering a new route to automated 3D creation. By translating images and instructions into editable programs, they bring reconstruction, generation, and editing into a shared workflow. Yet existing benchmarks fragment evaluation across task scopes and protocols, leaving their capabilities across construction levels unclear. We propose…

## 16. AutoCompress: Automated Hardware-Guided Model Compression

- 分数：20.5  ·  HF 赞：9  ·  来源：huggingface
- 兴趣命中：memory, benchmark, coding, spec
- 作者：Sheldon Liang, Ali Taghibakhshi, Saurav Muralidharan, Sharath Turuvekere Sreenivas, Ashwath Aithal, Pavlo Molchanov, Nima Tajbakhsh
- 链接：[arXiv](https://arxiv.org/abs/2611.08290) · [PDF](https://arxiv.org/pdf/2611.08290) · [HF](https://huggingface.co/papers/2611.08290)

LLM pruning must preserve quality while meeting hardware- and workload-specific constraints on latency, throughput, and memory. Existing pruning workflows often target parameter counts, requiring practitioners to manually select model sizes that meet latency, throughput, and GPU memory limits. However, parameter count alone does not predict these metrics, which depend on the model architecture, workload, hardware,…

## 17. ReproBridge: Building Reproducibility into ML Research Artifacts

- 分数：20.0  ·  HF 赞：16  ·  来源：huggingface
- 兴趣命中：agent, coding
- 作者：Yubo Wang, Rui Meng, Jaehyun Nam, Tomas Pfister, Jinsung Yoon
- 链接：[arXiv](https://arxiv.org/abs/2611.08452) · [PDF](https://arxiv.org/pdf/2611.08452) · [HF](https://huggingface.co/papers/2611.08452)

Reproducing machine learning experiments requires reconstructing procedures from information scattered across papers, released code, and supporting artifacts. For coding agents, reproduction success can therefore depend on their ability to fill in missing details, rather than on the released artifacts alone. We ask whether preserving recovered procedures and decisions improves subsequent independent reproduction. We…

## 18. AgentBaton: Efficient Model Collaboration in Agentic Tasks

- 分数：20.0  ·  HF 赞：12  ·  来源：huggingface
- 兴趣命中：agent, reasoning, benchmark
- 作者：Junlong Li, Jindong Jiang, Yonggan Fu, Jiarui Yao, Hanrong Ye, Wonmin Byeon, Peter Belcak, Hao Zhang, Pavlo Molchanov
- 链接：[arXiv](https://arxiv.org/abs/2610.35959) · [PDF](https://arxiv.org/pdf/2610.35959) · [HF](https://huggingface.co/papers/2610.35959)

Solving long-horizon agentic tasks requires language agents to interact with their environments over multiple steps, and reliable performance often comes from the expensive capable models available through cloud providers. Meanwhile, alternative efficient models with inferior performance but a much lower cost are emerging, including lower-tier cloud models and smaller open-weights models deployable on local…

## 19. Sage-Taiyi: A Metacognitive Architecture for Scientific Discovery

- 分数：20.0  ·  HF 赞：8  ·  来源：huggingface + arxiv
- 兴趣命中：reasoning, benchmark
- 作者：Weida Wang, Benteng Chen, Yigeng Jiang, Shuchen Pu, Weiping Shen, Zichao Liu, Yulin Su, Zitong Wang, Siyu Zhou, Zifu Wang, Yizhi Li, Xin Zong, Yuning Yang, Jixiang Bi, Yuan Wang, Chuyi Peng, Shiyao Geng, Qi Zhang, Kuan Lu, Mengzhu Li, Weiwang Xu, Peishan Xiang, Chengjun Liu, Chengrui Wei, Fangchen Yu, Shengji Tang, Yichen Jiang, Jingqi Ye, Cheng Yang, Tao Hu, Jianbiao Mei, Qinglong Cao, Kun Li, Yixin Chen, Shengyuan Xu, Juncheng Xiao, Yiheng Wang, Ruizhe Chen, Shiyang Feng, Runmin Ma, Xiangchao Yan, Zongsheng Cao, Haomeng Hu, Yu Ke, Taihui Wu, Meng Dai, Xu Guo, Haoyang Peng, Yinglong Ni, Pingsen Shi, Xiaosong Wang, Shuyue Hu, Haijun Li, Sherry Dongqi Bao, Yang Yang, Chao Yang, Jie Hou, Tianfan Fu, Yi Gong, Jin Zeng, Mao Su, Hongxia Hao, Fanyang Mo, Fenghua Ling, Tianshu Yu, Yunqi Cai, Baihong Chi, Jingwei Wang, Lei Wang, Chuncheng Bu, Shide Lv, Guangyu Wang, Yuqiang Li, Chunfeng Song, Lei Bai, Hui Wang, Xujun Fu, Li Cao, Lei Chen, Dahua Lin, Xing Xie, Bowen Zhou, Wenlong Zhang, Pinlong Cai, Peng Ye, Aiwen Lei, Jie Li, Shengchun Wang, Bo Zhang, Shufei Zhang
- 链接：[arXiv](https://arxiv.org/abs/2611.12762) · [PDF](https://arxiv.org/pdf/2611.12762) · [HF](https://huggingface.co/papers/2611.12762)

We introduce Sage-Taiyi, a metacognition-inspired architecture that uses accumulated scientific understanding to guide what to investigate next and how to investigate it. Through explicit monitoring and control, the system revises its understanding of evidence, assumptions, and unresolved questions, then uses these assessments to adapt research targets and select reusable reasoning methods. On Taiyi-Bench, an AI…

## 20. LowRAM: Low-Rank Keys and Amortised Values for Composable KV Cache Compression at Test-Time

- 分数：19.0  ·  HF 赞：10  ·  来源：huggingface
- 兴趣命中：memory, long context, coding
- 作者：Teresa Delgado, Hugo Hazard, Martin Benfeghoul, Jun Wang, Zafeirios Fountas
- 链接：[arXiv](https://arxiv.org/abs/2611.07025) · [PDF](https://arxiv.org/pdf/2611.07025) · [HF](https://huggingface.co/papers/2611.07025)

Autoregressive decoding relies on the KV cache, whose memory footprint grows linearly with context length and caps batch size and throughput. Existing post-training methods exploit redundancy across tokens, layers, and feature dimensions, or lower numerical precision. We identify a complementary axis: within each attention head, values are largely predictable from their corresponding keys. We exploit this with value…

## 21. CPU-ARC: Agentic Reasoning Caching for on-CPU Reasoning Reuse

- 分数：19.0  ·  HF 赞：6  ·  来源：huggingface
- 兴趣命中：agent, reasoning, language model, large language
- 作者：Peter Belcak, Greg Heinrich, Saurav Muralidharan, Shizhe Diao, Pavlo Molchanov
- 链接：[arXiv](https://arxiv.org/abs/2611.09891) · [PDF](https://arxiv.org/pdf/2611.09891) · [HF](https://huggingface.co/papers/2611.09891)

Large language models reinvent the wheel all the time. They conflate task-solving with the execution of the solutions, which forces them to solve every problem from scratch. We show that once a task has been reasoned through, the application of its solution to a new problem instance can be done very efficiently and with little involvement from language models. We introduce agentic reasoning caching, a method for…

## 22. Flide: Accelerating Decision Inference with Exact State Forking

- 分数：18.0  ·  HF 赞：8  ·  来源：huggingface
- 兴趣命中：agent, reasoning, evaluation
- 作者：Bobo Li, Jiajia Song, Hao Fei, Wynne Hsu, Mong Li Lee
- 链接：[arXiv](https://arxiv.org/abs/2610.42148) · [PDF](https://arxiv.org/pdf/2610.42148) · [HF](https://huggingface.co/papers/2610.42148)

Decision models such as Jev have emerged as a highly promising paradigm for LLM agent systems, providing lightweight and reliable categorical reasoning for rapid System One execution. However, existing generation-oriented inference engines fail to support these workloads effectively, suffering from severe prefix recomputation overheads or distorted output probabilities. To address this challenge, we propose Flide,…

## 23. Steerable Multi-Objective Group-Relative Preference Optimization with Jointly Trained Low-Rank Adapters

- 分数：17.5  ·  HF 赞：7  ·  来源：huggingface
- 兴趣命中：reinforcement learning, language model, spec
- 作者：Constantinos Karouzos, Nikolaos Aletras
- 链接：[arXiv](https://arxiv.org/abs/2611.09634) · [PDF](https://arxiv.org/pdf/2611.09634) · [HF](https://huggingface.co/papers/2611.09634)

Language model deployment often requires different trade-offs between competing objectives as user preferences change, yet standard post-training methods typically produce a single policy for a fixed objective weighting. We introduce LambdaMix, a new parameter efficient method for learning a preference conditioned family of policies with group-relative online reinforcement learning. LambdaMix jointly trains one…

## 24. TRIO: Task Refinement with Individual Optimization for Retrieval-Augmented Generation

- 分数：17.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：agent, benchmark, language model, spec, retrieval
- 作者：Yingtao Ren, Xiao Luo, Yiwei Fu, Jinzhao Zhou, Yu-Cheng Chang, Chin-Teng Lin
- 链接：[arXiv](https://arxiv.org/abs/2611.02810) · [PDF](https://arxiv.org/pdf/2611.02810) · [HF](https://huggingface.co/papers/2611.02810)

This paper studies retrieval-augmented generation (RAG), which leverages external knowledge to improve the performance of language models. Despite the remarkable progress, current RAG approaches are still far from satisfactory due to inadequate retrieval and potential hallucinations. Towards this end, we propose a novel approach named Task Refinement with Individual Optimization (TRIO) for RAG. The core idea of our…

## 25. Authorization Drift in LLM Agents: Evaluating Boundary Compliance in Multi-Step Tool Use

- 分数：17.0  ·  HF 赞：6  ·  来源：huggingface
- 兴趣命中：agent, tool use, benchmark
- 作者：Chuxue Cao, Jingru Zeng, Boqin Yin, Yujin Zhou, Yidan Huang, Sujin Chen, Jinluan Yang, Haoran Li, Yike Guo, Sirui Han
- 链接：[arXiv](https://arxiv.org/abs/2611.09113) · [PDF](https://arxiv.org/pdf/2611.09113) · [HF](https://huggingface.co/papers/2611.09113)

LLM agents can exceed their authorization boundaries while pursuing user goals without an adversary. We formalize this phenomenon as authorization drift across data, tool, scope, and time, and introduce the Authorization Drift Benchmark (ADB): 648 samples across seven domains, each pairing a sufficient compliant path with an attractive unauthorized shortcut. To ensure executable tasks, tempting shortcuts, and…

## 26. Coding or Cheating? An Investigation of Frontier Coding LLMs

- 分数：17.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：agent, reinforcement learning, benchmark, coding, spec
- 作者：Yuntao Gui
- 链接：[arXiv](https://arxiv.org/abs/2611.10404) · [PDF](https://arxiv.org/pdf/2611.10404) · [HF](https://huggingface.co/papers/2611.10404)

Frontier agentic LLMs are trained on verifiable rewards in reinforcement learning (RL) environments built from real software repositories. A passing test suite is treated as the reward for solving the task. We show that, on hard problems, frontier models often satisfy these rewards by obtaining the answer instead of deriving it, known as reward hacking. Prior reports document this behavior on public benchmarks. We…

## 27. "PRISM" Is Not All You Need: Cross-Topic Name Collisions and Scientific Paper Retrieval

- 分数：16.5  ·  HF 赞：5  ·  来源：huggingface
- 兴趣命中：evaluation, spec, retrieval
- 作者：Jingjie Ning, Xueqi Li, Yibo Kong
- 链接：[arXiv](https://arxiv.org/abs/2611.01362) · [PDF](https://arxiv.org/pdf/2611.01362) · [HF](https://huggingface.co/papers/2611.01362)

Scientific names increasingly connect papers from different research topics, leaving readers to recover a paper's identity from context. We study this convergence in 564,861 AI-related arXiv records. Cross-topic name collision grows 4.33-fold from a pooled 2020-2022 reference to 2026, compared with 1.12-fold within topics. A second sentence encoder reproduces the pattern, and name-group resampling quantifies its…

## 28. Human-Centred, Risk-Constrained Evaluation of Financial Document Recognition: Evidence, Critical Errors, and Selective Automation

- 分数：16.5  ·  HF 赞：5  ·  来源：huggingface
- 兴趣命中：evaluation, benchmark, spec
- 作者：Subodh Lonkar
- 链接：[arXiv](https://arxiv.org/abs/2611.02775) · [PDF](https://arxiv.org/pdf/2611.02775) · [HF](https://huggingface.co/papers/2611.02775)

Financial document recognition is often assessed using character and word error rates, although these metrics do not express whether a system preserves the financial facts on which people and organisations act. This paper develops a human-centred, risk-constrained framework for evaluating financial document recognition as evidence recovery and decision support. It defines typed financial facts linked to visible…

## 29. AutoVend: Benchmarking LLM Agents on Long-Horizon Autonomous Vending Operations

- 分数：16.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：agent, benchmark, language model, large language
- 作者：Qiming Shi, Yikun Li, Beidi Luan, Rui Sun, Sinuo Wang, Delin Wang, Yan Ma, Jing Li, Daxin Jiang, Zuo Bai
- 链接：[arXiv](https://arxiv.org/abs/2610.36980) · [PDF](https://arxiv.org/pdf/2610.36980) · [HF](https://huggingface.co/papers/2610.36980)

Large language model (LLM) agents are extending agent-mediated commerce on the Web from shopping for consumers to operating businesses for sellers. In online-to-offline (O2O) commerce, decisions are issued through Web-based platforms but realized through costly physical execution. Evaluating such agents requires going beyond individual transactions to ask whether decisions made online turn into sustained economic…

## 30. How Many Exposures Does a World Model Need? Learning Unseen Game Mechanics at Test Time

- 分数：16.5  ·  HF 赞：1  ·  来源：huggingface + arxiv
- 兴趣命中：agent, benchmark
- 作者：Ku Onoda, Haruto Kawano, Shota Takashiro, Kohei Hayashi
- 链接：[arXiv](https://arxiv.org/abs/2611.12324) · [PDF](https://arxiv.org/pdf/2611.12324) · [HF](https://huggingface.co/papers/2611.12324)

World models enable agents to plan and learn from imagined experience, but in an unfamiliar environment they must learn its mechanics from limited interaction. A mechanic is a rule for how an action or an interaction changes part of the environment. Each occurrence of a mechanic that the model observes is one exposure. We ask how many exposures a world model needs to predict the effects of a new environment's…

## 31. FlyHash for LLM Agent Memory: An Empirical Validation and a New Application

- 分数：16.0  ·  HF 赞：0  ·  来源：huggingface
- 兴趣命中：agent, memory, benchmark, language model, large language, spec, retrieval
- 作者：Mohan Bheemadolu, Chrisogonas O. Odhiambo
- 链接：[arXiv](https://arxiv.org/abs/2611.05791) · [PDF](https://arxiv.org/pdf/2611.05791) · [HF](https://huggingface.co/papers/2611.05791)

Large language model (LLM) agents increasingly rely on external memory stores to retain information across conversations, typically via dense vector embeddings searched with approximate nearest-neighbor methods. The fruit fly's olfactory circuit computes a locality-sensitive hash of sensory input using a strikingly different mechanism - sparse random projection followed by winner-take-all competition - and prior…

## 32. Hierarchical Residuals: A Minimalist Decoupling of Residual Width from Compute Width

- 分数：15.5  ·  HF 赞：7  ·  来源：huggingface
- 兴趣命中：memory, spec
- 作者：Ziteng Wang, Jianqiao Lu, Xinyu Ma, Jintao Zhang, Jun Zhu, Yiyuan Ma, Jianfei Chen
- 链接：[arXiv](https://arxiv.org/abs/2610.41711) · [PDF](https://arxiv.org/pdf/2610.41711) · [HF](https://huggingface.co/papers/2610.41711)

Residual connections underpin Transformers, but they implicitly tie the residual width carried through depth to the compute width used inside each layer. We introduce Hierarchical Residuals (HiRes), a minimalist architectural change that decouples these dimensions, widening the residual state while keeping per-layer compute width fixed. HiRes groups layers into blocks: standard d-dimensional PreNorm layers operate…

## 33. Sketchpad: certified exact arithmetic with a small vision-language model

- 分数：15.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：tool use, memory, language model
- 作者：Mostafa 'Neo' Mohsenvand
- 链接：[arXiv](https://arxiv.org/abs/2611.04434) · [PDF](https://arxiv.org/pdf/2611.04434) · [HF](https://huggingface.co/papers/2611.04434)

Language models are accurate on most long-arithmetic problems, but their accuracy is estimated on samples and carries no guarantee for an unseen input; tool use is exact but moves the computation outside the network. We show that exactness at all input lengths becomes a finite, checkable property of a network when each of its steps reads only a bounded view of an external working memory. In Sketchpad, Qwen3.5-0.8B…

## 34. The Last Mile to the Real World: Agent-Native Primitives as Reusable Building Blocks for Solving Real-World Tasks

- 分数：15.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：agent, benchmark, spec
- 作者：Haibo Jin, Peng Kuang, Xiaopeng Yuan, Lucheng Fu, Jerry Wang, Xucheng Yu, Yaoning Yu, Dehao Wu, Runguo Li, Colin Su, Jingxuan Sun, Xuyang Liu, Haojing Luo, Haohan Wang
- 链接：[arXiv](https://arxiv.org/abs/2611.07461) · [PDF](https://arxiv.org/pdf/2611.07461) · [HF](https://huggingface.co/papers/2611.07461)

How can an agent handle a real-world task end to end? Frontier models with their own harnesses still fall short on real-world benchmarks: on Terminal-Bench 4.0, GPT-5.6 Sol with Codex resolves 37.3% of the tasks and Claude Opus 5 with Claude Code 51.8%. These tasks fail at the step from reaching a resource to applying it, which we call the last mile to the real world. Existing approaches put the resource within…

## 35. Where to Connect? Boosting MLLMs via Dynamic Gated Pathways across ALL ViT and LLM Layers

- 分数：15.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：benchmark, language model, large language
- 作者：Yingying Yan, Jiaqi Tang, Wei Wei, Qianzhou Wang, Lei Zhang, Jianmin Chen, Yuyang Xia, Botong Geng, Jinjian Wu, Qifeng Chen
- 链接：[arXiv](https://arxiv.org/abs/2611.06844) · [PDF](https://arxiv.org/pdf/2611.06844) · [HF](https://huggingface.co/papers/2611.06844)

A central yet under-explored question in Multimodal Large Language Models (MLLMs) is where to connect---how visual information from a hierarchical vision encoder should be wired into the layer-wise semantics of a large language model. Mainstream MLLMs inject a fixed single-layer visual representation into the LLM and treat all LLM layers as a single consumer, ignoring that different layers demand different visual…

## 36. IWIBench: Evaluating Gradient-Free Model Driven Intra-weight Injection

- 分数：13.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：coding, spec
- 作者：Chris von Csefalvay, Pranav Doma, Achyuthan Unni Krishnan, Tamás Földi
- 链接：[arXiv](https://arxiv.org/abs/2611.08647) · [PDF](https://arxiv.org/pdf/2611.08647) · [HF](https://huggingface.co/papers/2611.08647)

Intra-weight injection lets one model change another model's behaviour by editing its weights directly, without gradients. Such edits can range from altering lexical associations to enforcing output formats or updating factual knowledge. Despite growing interest in these approaches, there has been no systematic way to evaluate how well models perform them. We introduce IWIBench, which measures a large editor model's…

## 37. Static Recovery Is Not Dynamic Stability: Dynamics-Aware Benchmarking of Protein Motif Scaffolding

- 分数：13.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：evaluation, benchmark
- 作者：Emile de Bruyn, Moritz Schäffler, Jannik Schneider, Sebastian R. Schmidt, Chanwoong Hwang, Aleena Siji, Utkarsh Upadhyay, Stefan Bauer, Alexander Schug, Stefan Kesselheim, Artur Yakimovich, Alina Bazarova
- 链接：[arXiv](https://arxiv.org/abs/2611.07723) · [PDF](https://arxiv.org/pdf/2611.07723) · [HF](https://huggingface.co/papers/2611.07723)

Protein motif scaffolding benchmarks assess whether generative models can build scaffolds around functionally important residues. Their conclusions depend on which motifs are tested and which criteria define success. Existing benchmarks typically use small hand-curated motif sets and static refolding criteria, but protein function often depends on conformational ensembles and transitions. Here, we address both…

## 38. PREEN: Exemplar-Based Color Style Transfer with Smartphone Editor Presets

- 分数：12.5  ·  HF 赞：5  ·  来源：huggingface
- 兴趣命中：benchmark
- 作者：Beomjin Ahn
- 链接：[arXiv](https://arxiv.org/abs/2610.36896) · [PDF](https://arxiv.org/pdf/2610.36896) · [HF](https://huggingface.co/papers/2610.36896)

We present PREEN (Preset Regression via an Exemplar-based Editor Network), which casts color style transfer as regression onto the 29 parameters of a deterministic image editor. Given a content image and a style reference, PREEN predicts a preset, a vector of editor slider values that is interpretable and editor-consumable, not a raster image. The key obstacle is supervision, since an arbitrary real reference lacks…

## 39. PhysioWave-T: Token-Efficient Wavelet Foundation Models for Biosignals

- 分数：12.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：memory, spec
- 作者：Yanlong Chen, Simone Benatti, Luca Benini, Cuntai Guan, Yawei Li
- 链接：[arXiv](https://arxiv.org/abs/2611.08969) · [PDF](https://arxiv.org/pdf/2611.08969) · [HF](https://huggingface.co/papers/2611.08969)

We present PhysioWave-T, a token-efficient wavelet foundation model family for EEG, ECG, and sEMG. Dynamic scale folding recombines J+1 wavelet subbands prior to tokenization, compressing sequence length from (J+1)CS to CS tokens for J levels, C channels, and S temporal patches. Route-specific front ends and learned channel-name embeddings allow one Transformer per modality to handle diverse montages and sampling…

## 40. SIRIS: Can LLMs Tell When Simulation Errors Matter in AI-Driven Systems Research

- 分数：12.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：agent
- 作者：Jinwoo Hwang, Sukmin Cho, Tao Zhang, Soheil Abbasloo, Jongse Park, Peng Cheng
- 链接：[arXiv](https://arxiv.org/abs/2611.10329) · [PDF](https://arxiv.org/pdf/2611.10329) · [HF](https://huggingface.co/papers/2611.10329)

LLM agents increasingly drive systems research and rely on simulators to evaluate candidate designs at scale. Simulators are imperfect by design: their modeling limitations can distort predictions yet leave the recommended design correct, or change which design should be selected. We introduce Siris to test whether LLMs can tell these cases apart, judging from their systems understanding when a limitation…

## 41. Knowing When to Teach: Learning from Teachable Prefixes in Multilingual Reasoning Distillation

- 分数：11.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：reasoning
- 作者：Jaewon Cho, Minseo Yoon, Jinyoung Park, Jinwoo Seo, Jaewon Chu, Alice Oh, Hyunwoo J. Kim
- 链接：[arXiv](https://arxiv.org/abs/2611.08179) · [PDF](https://arxiv.org/pdf/2611.08179) · [HF](https://huggingface.co/papers/2611.08179)

On-Policy Self-Distillation (OPSD) improves reasoning by training a student on its own reasoning, using the same model conditioned on reference solutions as a teacher. Applying OPSD to multilingual reasoning requires the teacher to provide useful feedback across languages, even when the student makes mistakes in intermediate steps. We observe a phenomenon we call Teacher Drift: as these mistakes accumulate, the…

## 42. Learning to evolve by matching velocities

- 分数：11.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：spec
- 作者：Nicola Farenga, Andrea Manzoni
- 链接：[arXiv](https://arxiv.org/abs/2611.00448) · [PDF](https://arxiv.org/pdf/2611.00448) · [HF](https://huggingface.co/papers/2611.00448)

Learning the continuous-time evolution of nonlinear dynamical systems relies on trajectory-based objectives, which require simulating the learned dynamics during training and backpropagating through the numerical scheme, at a cost that grows with the rollout horizon. We show that trajectory-based objectives degenerate as the rollout horizon increases, hindering gradient-based optimization, and that the numerical…

## 43. FewStepRL: Fine-tuning Few-step Diffusion Models with Reinforcement Learning

- 分数：10.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：reinforcement learning
- 作者：Haitao Lin, Minsi Ren, Yang Li, Xingtong Ge, Zheyuan Hu, Peiyan Hu, Tailin Wu
- 链接：[arXiv](https://arxiv.org/abs/2611.08240) · [PDF](https://arxiv.org/pdf/2611.08240) · [HF](https://huggingface.co/papers/2611.08240)

Reinforcement learning (RL) has become a standard post-training method for diffusion models, but most RL objectives roll out the current policy at every iteration, and with a many-step sampler these rollouts typically dominate the cost of training. Few-step models cut this cost, yet they model an average velocity over an interval, whereas existing RL objectives are built for an instantaneous velocity with a…

## 44. OmniLatent: Unified Latent for 3D Part Modeling

- 分数：10.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：-
- 作者：Yunhan Yang, Yunfei Zhao, Zeqiang Lai, Jiachen Xu, Minxiu Wang, Xintong Han, Xiangyu Yue, Xihui Liu, Chunchao Guo
- 链接：[arXiv](https://arxiv.org/abs/2611.09055) · [PDF](https://arxiv.org/pdf/2611.09055) · [HF](https://huggingface.co/papers/2611.09055)

3D part decomposition is a central capability for editable asset creation, yet existing workflows typically segment a completed mesh as a post-processing step, making the result sensitive to geometric artifacts, texture ambiguity, and limited part-level annotations. We present OmniLatent, a unified latent modeling framework for 3D part decomposition. Instead of predicting part labels in isolation, OmniLatent learns…

## 45. ODE Policy: Robot Learning via Action Dynamics, Not Actions

- 分数：10.0  ·  HF 赞：0  ·  来源：huggingface
- 兴趣命中：reinforcement learning
- 作者：Jindou Jia, Jingliang Li, Kuangji Zuo, Tuo An, Yuxuan Hu, Mengfei Zhao, Bofan Lyu, Jiaqi Bai, Daoyuan Zhu, Hengyu Dai, Junpeng Zhang, Jianfei Yang
- 链接：[arXiv](https://arxiv.org/abs/2611.01729) · [PDF](https://arxiv.org/pdf/2611.01729) · [HF](https://huggingface.co/papers/2611.01729)

Most robot policies, whether trained by imitation learning (IL) or reinforcement learning (RL), map observations to action values at discrete control steps and leave the continuity of physical motion to be learned implicitly. We propose ODE policy, which learns the dynamics of the action rather than the action itself. A neural ordinary differential equation (ODE) learns the vector field of the action by matching the…

## 46. JoVox: Joint Hierarchical Flow Matching for Lightweight Voxel Generation

- 分数：9.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：-
- 作者：Xiangjun Tang, Jianqi Chen, Peter Wonka
- 链接：[arXiv](https://arxiv.org/abs/2611.10690) · [PDF](https://arxiv.org/pdf/2611.10690) · [HF](https://huggingface.co/papers/2611.10690)

Generating high-fidelity voxels while keeping their lightweight nature remains an open problem in computer vision. Current generators are either high-fidelity but computationally heavy, or lightweight but of lower fidelity. Hierarchical methods keep the lightweight nature of voxels. However, their coarse levels, which decide where all finer cells can appear, are generated with the least information about the shape…

## 47. SMO: Compiling Natural Language Skills into Graphs of Reusable State-Move-Outcome Bricks

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, evaluation, language model, large language
- 作者：Chao Chen, Jiashuo Zhang, Yunhang Shen, Liangyu Lian, Rongrong Ji
- 链接：[arXiv](https://arxiv.org/abs/2611.12041) · [PDF](https://arxiv.org/pdf/2611.12041) · [HF](https://huggingface.co/papers/2611.12041)

Large language model agents increasingly rely on reusable natural-language skills, yet growing skill collections remain accumulations of isolated text artifacts that are difficult to compare, deduplicate, and compose. We argue that the reusable content of a skill lies not in its surface wording but in its procedural transitions: which operation to execute under a given state and which observable outcome to produce.…

## 48. Evaluating AI Agents for Industrial-Level Chip Floorplanning: A Framework and Empirical Study

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, evaluation, spec, planning
- 作者：Nova-Silicon Team
- 链接：[arXiv](https://arxiv.org/abs/2611.12048) · [PDF](https://arxiv.org/pdf/2611.12048) · [HF](https://huggingface.co/papers/2611.12048)

Floorplanning is an early step in turning a logical circuit into a physical chip: it positions large circuit modules and constrains the space available for subsequent logic placement and wiring. These decisions affect congestion and timing, but their physical consequences emerge through downstream implementation. For AI agents, the task requires translating engineering constraints into spatial decisions whose…

## 49. COMPASS: Composable Policy-Amortized Structured Search for LLM-Based Optimization Modeling

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, language model, large language, retrieval
- 作者：Nguyen Le Minh Hoang, Van Duc Cuong, Bui Trong Duc, Huynh Thi Thanh Binh
- 链接：[arXiv](https://arxiv.org/abs/2611.12060) · [PDF](https://arxiv.org/pdf/2611.12060) · [HF](https://huggingface.co/papers/2611.12060)

Large language models offer a promising technique for translating natural-language optimization problems into solver code, but their reliability remains constrained by the quality of template retrieval. While recent structured methods improve over flat prompting through hierarchical taxonomy search, their traversal rules remain fixed or LLM-driven at inference time, leaving retrieval unable to improve from past…

## 50. MIRIX-2.0: Multi-Agent Memory System

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, memory, benchmark, spec, retrieval
- 作者：Wei-Chieh Huang, Weizhi Zhang, Jiayan Nan, Peng Xia, Yu Wang
- 链接：[arXiv](https://arxiv.org/abs/2611.12068) · [PDF](https://arxiv.org/pdf/2611.12068) · [HF](https://huggingface.co/papers/2611.12068)

Long-term memory lets LLM agents personalize, stay consistent, and reuse what worked before. Parametric memories need training, consolidation can lose details for good, and keeping every record leaves a growing store to search. We present MIRIX-2.0, a multi-agent memory system designed to be practical, accurate, and efficient at once. It is the most accurate of the compared systems on four of five QA benchmarks. It…

## 51. Correct First, Fast Second: What a Local 7B Code Model Can and Cannot Do for GPU Kernel Optimization

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, memory, reasoning, evaluation, retrieval
- 作者：Jui-Chien Tsou, Po-Yi Wu
- 链接：[arXiv](https://arxiv.org/abs/2611.12079) · [PDF](https://arxiv.org/pdf/2611.12079) · [HF](https://huggingface.co/papers/2611.12079)

We study how much the interaction strategy around a fixed, locally hosted 7B-parameter code model (Qwen2.5-Coder-7B-Instruct) affects its ability to replace PyTorch operators with custom CUDA kernels. On 30 KernelBench tasks (levels 1-3, first 10 each, evaluated on a V100), we compare four regimes of increasing structure: zero-shot prompting, profiling-guided prompting, iterative refinement on execution feedback,…

## 52. Compass 1: Towards Open-World and Persistent Embodied Navigation from Monocular RGB Videos

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, memory, reasoning, evaluation, retrieval
- 作者：Hai Zhang, Siqi Liang, Yanjun Guo, Shoufeng Zhang, Yunhao Wang, Hangyu Du, Haoguang Mai, Hongchen Li, Jiazhi Yang, Jialong Zeng, Yu Hu, Chen Chen, Gangcheng Jiang, Zishun Zhuo, Lirui Zhao, Zhigang Li, Yu Qiao, Zhenjie Yang, Fu Zhang, Hongyang Li
- 链接：[arXiv](https://arxiv.org/abs/2611.12087) · [PDF](https://arxiv.org/pdf/2611.12087) · [HF](https://huggingface.co/papers/2611.12087)

Embodied navigation requires agents to achieve persistent spatial awareness and long-horizon execution stability in open-world environments. However, existing navigation architectures struggle to sustain both capabilities, remaining effective only over a handful of recent frames. We present Compass 1, the first embodied navigation foundation model to unify language understanding and video generation while enabling…

## 53. Zero-Search Reinforcement Learning for Slay the Spire 2 with Failure-Driven Restarts

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reasoning, reinforcement learning, evaluation
- 作者：Xiangqin Chen, Zhengxuan Xie
- 链接：[arXiv](https://arxiv.org/abs/2611.12088) · [PDF](https://arxiv.org/pdf/2611.12088) · [HF](https://huggingface.co/papers/2611.12088)

Slay the Spire 2 (STS2) is a deck-building roguelike in which a winning run at the highest difficulty takes several hundred decisions, and most losses happen in late boss fights that a learner seldom reaches. We train agents that choose every action with one forward pass of a 6.6M-parameter entity transformer, without lookahead. Training and evaluation run the game's own compiled assembly (v0.107.1) in a headless…

## 54. From Fluent Text to Ontology-Compatible Definitions: A Quality-Control Agentic Workflow

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, language model, large language, coding, spec
- 作者：Kun Feng, Chenchen Chu, Yan Liu, Haojie Sun, Jijun Tang, Chen Tian, Shuolin Xiao, Jianping He, Zhao Li
- 链接：[arXiv](https://arxiv.org/abs/2611.12095) · [PDF](https://arxiv.org/pdf/2611.12095) · [HF](https://huggingface.co/papers/2611.12095)

Biomedical ontologies are structured knowledge systems that must evolve continuously to represent newly emerging knowledge, but their manual maintenance remains time-consuming and laborintensive. Textual definitions are especially costly because they must be readable to humans and compatible with controlled entities, relations, and logical constraints. Large language models (LLMs) offer a promising way to assist…

## 55. OGDA: Ontology-Grounded Data Agents for Reliable Analysis over Heterogeneous Data Lakes

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, context window, reasoning, spec
- 作者：Boyi Zhang, Hong Ting Tsang, Yisen Gao, Qiao Xiao, LI Yufei, Haoyu Huang, Zhongwei Xie, Jiaxin Bai, Yangqiu Song
- 链接：[arXiv](https://arxiv.org/abs/2611.12114) · [PDF](https://arxiv.org/pdf/2611.12114) · [HF](https://huggingface.co/papers/2611.12114)

Full-pipeline data analysis over real-world data lakes requires LLM agents to locate and integrate information across large collections of tables with different schemas. Existing data agents follow task-specific exploration, which exhausts the context window in massive lakes. As the context fills, the agent's reasoning degrades, leading it to locate and process incorrect data files. These errors propagate into the…

## 56. SCALE: Small-Model-First Concept Abstraction with LLM-Guided Experience Internalization

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, memory, reasoning, language model, large language
- 作者：Hong Su
- 链接：[arXiv](https://arxiv.org/abs/2611.12120) · [PDF](https://arxiv.org/pdf/2611.12120) · [HF](https://huggingface.co/papers/2611.12120)

Autonomous agents must continually acquire reusable knowledge from experience without relying on costly large language model (LLM) reasoning for every decision. However, existing experience-based approaches often struggle to transform accumulated observations and reasoning into compact knowledge that lightweight models can independently apply. This paper proposes SCALE, a small-model-first framework that integrates…

## 57. Lost in Rounding: bf16 Recurrent State Makes Hybrid Reasoning Models Think Longer

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, reasoning, evaluation, coding
- 作者：Yuchuan Weng, Xin Chen, Chi Liu
- 链接：[arXiv](https://arxiv.org/abs/2611.12127) · [PDF](https://arxiv.org/pdf/2611.12127) · [HF](https://huggingface.co/papers/2611.12127)

Hybrid reasoning models interleave attention with recurrent mixers such as Mamba-2 and Gated DeltaNet, whose state is cached between decoding steps. Prior work showed that storing this state in FP16 or INT8 with round-to-nearest (RTN) makes Mamba-2 and GDN hybrids more verbose, and that stochastic rounding (SR) fixes it. We study the other 16-bit format that serving engines expose, bf16, on six open hybrid reasoning…

## 58. Toward Sustainable Agentic AI: Carbon Tradeoffs Across Iterative Self-Refinement and Tool-Augmented Coding

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, benchmark, language model, coding
- 作者：Boris Ruf, Adrien de Mailly Nesle, Marcin Detyniecki
- 链接：[arXiv](https://arxiv.org/abs/2611.12128) · [PDF](https://arxiv.org/pdf/2611.12128) · [HF](https://huggingface.co/papers/2611.12128)

Agentic language model systems can improve performance either by iterating on their own outputs or by using external tools in grounded environments. While these strategies can reduce error rates and substitute for larger models in some settings, their environmental cost remains relatively underexplored. We present two complementary empirical studies that estimate the energy and carbon footprint of agentic AI across…

## 59. Let the Fixer Decide: Training a Code Localizer from the Fixer's Likelihood

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reinforcement learning, evaluation, coding
- 作者：Khalil Hennara, Muhammad Hreden, Zeina Aldallal, Sara Chrouf, Safwan AlModhayan
- 链接：[arXiv](https://arxiv.org/abs/2611.12164) · [PDF](https://arxiv.org/pdf/2611.12164) · [HF](https://huggingface.co/papers/2611.12164)

Code localizers are usually trained to predict the files a reference patch edits, but the code a fixer needs to read is not the same as the code it changes. We propose Fixer-Guided Localization (FGL): the localizer proposes several localizations, a frozen fixer scores each by how likely it makes a verified patch, and the localizer is trained on these scores with weighted supervised fine-tuning, without running tests…

## 60. FraudBench: A Legal Evaluation of AI Deception

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, evaluation, language model, large language
- 作者：Kevin Wei, Sumaya Nur Adan, Stephan Llerena, Mark Gitau, Jakob Merane, Anita Srinivasan, Colette Le Brannan, Keethan Kleiner, Alessandro Tacconelli, Michael Tiu, Case Thomason, Kyle Emili, Natasza Gadowska, Alex Mark, Eric Ren, Umang Bhatt, Jatinder Singh, Jacy Reese Anthis, Doni Bloomfield, Noam Kolt
- 链接：[arXiv](https://arxiv.org/abs/2611.12167) · [PDF](https://arxiv.org/pdf/2611.12167) · [HF](https://huggingface.co/papers/2611.12167)

We introduce FraudBench, an evaluation of large language models' (LLMs) propensities to recommend, assist, or directly take actions that would constitute fraud under U.S. law. Our evaluation contains a novel dataset of 159 scenarios based on real-world U.S. court cases and validated by legal experts. We present each scenario to LLMs via three tasks at varying levels of autonomy: advising users, drafting messages for…

## 61. GeoMind: A Benchmark for Spatial Understanding in Robotic Manipulation

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, memory, reasoning, evaluation, benchmark
- 作者：Jinghe Wang, Xinrui Cao, Duo Wu, Chenghao Gu, Yong Zhong, Linjia Kang, Tianyi Xiong, Zhi Wang
- 链接：[arXiv](https://arxiv.org/abs/2611.12175) · [PDF](https://arxiv.org/pdf/2611.12175) · [HF](https://huggingface.co/papers/2611.12175)

Robotic manipulation has advanced rapidly in mapping visual observations and language instructions to actions. However, reliable manipulation in open-world environments requires robust spatial understanding: the ability to identify targets in complex layouts (spatial reasoning) and adapt to scenes that continuously evolve through interaction (spatial memory). Yet existing embodied benchmarks fall short in evaluating…

## 62. Embodied First Exam

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, evaluation, benchmark, coding
- 作者：Kangrui Wang, Qineng Wang, Changhe Chen, Pingyue Zhang, Chi Gui, Feishi Wang, Canyu Chen, Wenli Xiao, Xiaoyu Huang, Tonghe Zhang, Linjie Li, Zihan Wang, Minyeong Kim, Yiyou Sun, Mingkai Deng, Jinyu Hou, Qi Zhu, Han Liu, Eric P. Xing, Huaxiu Yao, Zhiwen Fan, Yuejiang Liu, Dawn Song, Pieter Abbeel, Li Fei-Fei, Jiajun Wu, Yuke Zhu, Guanya Shi, Ruohan Zhang, Manling Li
- 链接：[arXiv](https://arxiv.org/abs/2611.12177) · [PDF](https://arxiv.org/pdf/2611.12177) · [HF](https://huggingface.co/papers/2611.12177)

Early successes on agentic robotics point to a potential paradigm shift toward using coding agents to control robots. Existing robotics benchmarks are built around visuomotor policy learning, leaving it open whether coding agents can reliably control diverse robots under physical-world constraints. We therefore introduce the Embodied First Exam, a unified, comprehensive, and agent-native evaluation framework where…

## 63. TrajLift: Lifting Memory Recall Trajectories with Latency-Modulated Heat Diffusion

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, benchmark, spec, retrieval
- 作者：Jiawen Kang, Jinchao Li, Mingyu Cui, Junan Li, Xixin Wu, Helen Meng
- 链接：[arXiv](https://arxiv.org/abs/2611.12197) · [PDF](https://arxiv.org/pdf/2611.12197) · [HF](https://huggingface.co/papers/2611.12197)

Verbal memory retrieval carries rich diagnostic information for Alzheimer's disease through the order, hesitation, and categorical organization of recalled words, yet computational modeling of this retrieval process remains largely unexplored. A key challenge is that timing and hierarchical structure are diagnostically entangled: the diagnostic meaning of retrieval timing depends on its hierarchical context. We…

## 64. Graph-Based RL for Sequential Rendezvous Planning with Multiple Patrolling USVs

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reinforcement learning, evaluation, spec, planning
- 作者：Seung Woo Han, Hyeon Bin Yeo, Seung Heon Oh
- 链接：[arXiv](https://arxiv.org/abs/2611.12205) · [PDF](https://arxiv.org/pdf/2611.12205) · [HF](https://huggingface.co/papers/2611.12205)

In patrol missions involving multiple unmanned surface vehicles (USVs), a designated command USV can support fleet management by sequentially rendezvousing with each patrolling USV. These operations require motion-feasible route planning and priority-aware rendezvous sequencing, with the objective of minimizing mission completion time and total tardiness relative to priority-dependent due dates. We propose a…

## 65. PARIS: A multi-agent LLM framework for end-to-end, PRISMA-guided systematic literature reviews with pre-synthesis corpus quality assessment

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, language model, large language, spec, retrieval
- 作者：Christophe Cruz, Hussam Ghanem, Samir Jabbar, Ait Kbir, Hocine Cherifi
- 链接：[arXiv](https://arxiv.org/abs/2611.12222) · [PDF](https://arxiv.org/pdf/2611.12222) · [HF](https://huggingface.co/papers/2611.12222)

Systematic literature reviews (SRs) remain slow and labor-intensive, and most automation tools address single stages of the workflow. We present PARIS (PRISMA Agentic Research Intelligence System), an open-source framework in which a conductor agent running in Claude Code orchestrates 15 specialized large language model (LLM) agents, from scoping a research question to exporting a manuscript draft. Agents are…

## 66. Agent4Crypto: A Dual-Reflective and Market-Feedback-Aligned LLM-Based Multi-Agent System for Cryptocurrency Trading

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, memory, reasoning, reinforcement learning, spec, retrieval
- 作者：Guangyan Gan, Jiahao Li, Jiashun Wang, Lin William Cong
- 链接：[arXiv](https://arxiv.org/abs/2611.12269) · [PDF](https://arxiv.org/pdf/2611.12269) · [HF](https://huggingface.co/papers/2611.12269)

Cryptocurrency markets provide a natural testbed for autonomous AI agents because they are digital-native, high-frequency, and machine-speed environments, yet existing methods often struggle with non-stationary market regimes, opaque decisions, and fixed aggregation rules. In this paper, we propose Agent4Crypto, a dual-reflective and market-feedback-aligned multi-agent system. The framework coordinates specialized…

## 67. Learning Evidence-Grounded Reasoning for Context-Aware Time Series Forecasting

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, reinforcement learning, benchmark, spec
- 作者：Xingpeng Gao, Mingyue Cheng, Daoyu Wang, Huajian Zhang, Xiaoyu Tao
- 链接：[arXiv](https://arxiv.org/abs/2611.12285) · [PDF](https://arxiv.org/pdf/2611.12285) · [HF](https://huggingface.co/papers/2611.12285)

LLM-driven time series forecasting has become increasingly promising by leveraging contextual features to generate future values directly or refine forecast priors. However, incorporating contextual features alone does not ensure that models can identify which features matter for forecasting and understand what they suggest about future dynamics. We argue that the fundamental challenge is how to extract predictive…

## 68. Depth as a Candidate Source: Portfolio Allocation for Recurrent Test-Time Scaling in Large Language Models

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, language model, large language, spec
- 作者：Chaoyuan Hao, Wentao Yue, Yanyan Wu, Boyuan Gao, Tianyou Lai, Maolin Wang, Yongxin Ni, Hanwen Du, Youhua Li
- 链接：[arXiv](https://arxiv.org/abs/2611.12293) · [PDF](https://arxiv.org/pdf/2611.12293) · [HF](https://huggingface.co/papers/2611.12293)

Recurrent latent reasoning in large lanugage models (LLMs) scales test-time computation by increasing recurrent depth, naturally framing inference as a problem of deciding when to stop. We identify a previously overlooked limitation of this single-depth view through systematic preliminary analysis: deeper recurrence can lose correct solutions found at shallower depths, while depth-specific success sets remain…

## 69. HumanSightBench: A Benchmark for Human Visual Perception in MLLMs

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, evaluation, benchmark, language model, large language, spec
- 作者：Zixin Su, Yangguang Lin, Zegang Peng, Yuntong Sun, Xuanyi Wang, Jiahao Wang, Qiankai Xu, Bing Yuan, Jinze Bai, Youbin Wu, Jingjia Huang, Ruyang Liu, Yanxu Hu
- 链接：[arXiv](https://arxiv.org/abs/2611.12305) · [PDF](https://arxiv.org/pdf/2611.12305) · [HF](https://huggingface.co/papers/2611.12305)

Multimodal large language models (MLLMs) have demonstrated strong performance on knowledge-intensive and reasoning-based vision-language benchmark datasets, but still struggle to solve the visual questions that people can solve easily. Evaluating the differences between MLLMs and human-level visual perception is challenging due to end-to-end evaluation which combines various skills, or because we are uncertain if…

## 70. MNN-Pocket-0.3B Technical Report

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, reasoning, evaluation, benchmark, language model, coding, spec
- 作者： MNN Team
- 链接：[arXiv](https://arxiv.org/abs/2611.12311) · [PDF](https://arxiv.org/pdf/2611.12311) · [HF](https://huggingface.co/papers/2611.12311)

This technical report presents MNN-Pocket-0.3B, a compact 300M-parameter dense language model designed for efficient on-device deployment and supporting context lengths of up to 32K tokens. With an INT4 deployment footprint of only 173 MB and decoding throughput of up to 466 tokens/s on iPad Pro M5 (Metal), it can be seamlessly integrated into applications on edge devices such as smartphones and smart glasses.…

## 71. A Modular Perspective for Modeling MARL Systems

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reinforcement learning, evaluation, spec
- 作者：Tiziano Maisonhaute, Jean-Christophe Soulié, Fabien Michel
- 链接：[arXiv](https://arxiv.org/abs/2611.12314) · [PDF](https://arxiv.org/pdf/2611.12314) · [HF](https://huggingface.co/papers/2611.12314)

The growing complexity of Multi-Agent Reinforcement Learning (MARL) has fragmented the literature, obscuring underlying architectural choices behind diverse implementations. This fragmentation makes it difficult to evaluate critical modeling dimensions in isolation, identify how components affect the resulting system dynamics, and compare, reuse, or combine contributions across the literature. This paper proposes a…

## 72. AMSchem: Automated Schematic Visualization of AMS Circuits via Verifiable Agentic Generation

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, evaluation, benchmark, spec, planning
- 作者：Yichen Shi, Zhiyuan Wang, Jianing Cui, Yao Lai, Jinting Zhang, Zhuofu Tao, Hongyang Wang, Zhiping Yu, Ting Jung Lin, Lei He
- 链接：[arXiv](https://arxiv.org/abs/2611.12333) · [PDF](https://arxiv.org/pdf/2611.12333) · [HF](https://huggingface.co/papers/2611.12333)

For decades, the netlist-to-schematic gap has remained a persistent challenge in design automation, especially for analog and mixed-signal (AMS) circuits. Netlists encode connectivity, not visual presentation, making their manual conversion into readable schematics time-consuming and dependent on expert conventions. The same gap leaves LLM-based design tools without structured visual feedback, forcing them to…

## 73. TMT: Adapting CLIP to Infrared Imagery via Text-Derived Modality Knowledge Transfer

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, language model, spec, retrieval
- 作者：Ruofan Wang, Puzuo Wang, Xin Chen, Zibo Yu, Jungang Yang, Yi Hou
- 链接：[arXiv](https://arxiv.org/abs/2611.12345) · [PDF](https://arxiv.org/pdf/2611.12345) · [HF](https://huggingface.co/papers/2611.12345)

Vision-language models such as CLIP achieve strong performance across computer vision tasks, yet their image-text alignment is less reliable for infrared (IR) imagery because large-scale pre-training is dominated by visible-spectrum data. Due to the high cost of the infrared-text labeling, we investigate adapting CLIP to IR through only paired infrared-visible images, which requires considering modality-specific…

## 74. DForkTree: Accelerating Speculative Decoding with Fork-Aware Block Diffusion Draft Trees

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, language model, coding, spec
- 作者：Zhicheng Zheng, Cheng Zhang, Chenkai Tang
- 链接：[arXiv](https://arxiv.org/abs/2611.12356) · [PDF](https://arxiv.org/pdf/2611.12356) · [HF](https://huggingface.co/papers/2611.12356)

Speculative decoding speeds up language models by letting a lightweight drafter propose several future tokens that the target model verifies in parallel. Block diffusion drafters such as DFlash draft a whole block in one forward pass, and DDTree builds a draft tree from their per-position distributions. Each of these distributions assumes that the drafter's own most likely continuation is correct. A tree, however,…

## 75. TRIAD: Multimodal Retrieval across Abstraction, Constraints, and State

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reasoning, benchmark, spec, retrieval
- 作者：Xiangyang Wu, Chen Ju, Xu Chen, Likang Peng, Jinsong Lan, Haihong Tang, Yang Hu
- 链接：[arXiv](https://arxiv.org/abs/2611.12364) · [PDF](https://arxiv.org/pdf/2611.12364) · [HF](https://huggingface.co/papers/2611.12364)

Multimodal retrieval increasingly supports agentic systems, where user requests can involve cross-level relations, combine multiple constraints, and evolve across dialogue turns. In these settings, a highly similar result may still violate the user's requirements, while retrieved content may directly inform downstream actions without human screening. We introduce TRIAD, a multimodal retrieval benchmark for…

## 76. AutoVLA-D: Learn a Trajectory-Geometric Condition from Reasoning for Autonomous Driving VLA

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, benchmark, spec, planning
- 作者：Yuguang Yang, Zhewen Tan, Canyu Chen, Linlin Yang, Cheng Chi, Chunyang Liu, Kehua Sheng, Jinyu Yang, Baochang Zhan, Bo Zhang, Yan Wang, Xianbin Cao
- 链接：[arXiv](https://arxiv.org/abs/2611.12382) · [PDF](https://arxiv.org/pdf/2611.12382) · [HF](https://huggingface.co/papers/2611.12382)

Autoregressive VLA planning usually predicts continuous trajectories as the final output, but driving instructions often describe actions rather than ego states, which weakens direct conditioning on the final continuous trajectory. We address this gap with TrajCond, which introduces a discrete trajectory-geometric condition for VLA planning. Specifically, we represent TrajCond as a 1D-Brohan differential action…

## 77. More Than Just Style: Benchmarking Personality Influence in Large Language Models

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, language model, large language, spec
- 作者：Yuhao Liu, Mengyu Wang, Xiao Chen, Lu Liu
- 链接：[arXiv](https://arxiv.org/abs/2611.12392) · [PDF](https://arxiv.org/pdf/2611.12392) · [HF](https://huggingface.co/papers/2611.12392)

In addition to the effects of explicit input prompts and instructions, large language model outputs are influenced by underlying behavioral preferences similar to human personality tendencies. These tendencies can affect how models interpret situations and make decisions. However, their influence is difficult to disentangle from the effects of model capabilities and instructions. Therefore, we introduce SPACE, a…

## 78. BDBBQ: A Human-AI Collaborative Benchmark for Bengali Social Bias in LLMs

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, language model, large language
- 作者：Provat Saha, Ashika Habib Khan, Tahseen Tanha, Hasin Ishrak, Muhammad Iqbal Hossain
- 链接：[arXiv](https://arxiv.org/abs/2611.12407) · [PDF](https://arxiv.org/pdf/2611.12407) · [HF](https://huggingface.co/papers/2611.12407)

Despite growing attention to social bias in large language models (LLMs), existing bias benchmarks provide limited coverage of culturally grounded evaluation in Bengali, particularly within Bangladesh's sociocultural context. To address this gap, we develop a bilingual extension of BanglaBBQ comprising 61,312 question-answering instances across 12 social categories in English and Bengali. The benchmark incorporates…

## 79. Unprompted coordination through shared memory in LLM agents: a locked two-implementation replication and extension

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, memory, large language, spec
- 作者：Pekka Abrahamsson, Muhammad Waseem, Esa Karjalainen, Petrus Jussila, Henri Hansen, Jussi Rasku, Bilhanan Silverajan, Kai-Kristian Kemell
- 链接：[arXiv](https://arxiv.org/abs/2611.12412) · [PDF](https://arxiv.org/pdf/2611.12412) · [HF](https://huggingface.co/papers/2611.12412)

Coordination between large language-model agents has become a central question for AI safety and software engineering, as such agents are deployed in groups that share infrastructure. Existing research tells the agents that partners exist or asks them to coordinate. Whether coordination arises through shared state alone, with nothing disclosing that anyone else is present, is the key question for deployments that…

## 80. dNaViT: Discrete Codes are General-Purpose Visual Representations

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, language model, coding, spec
- 作者：Xiaotong Li, Zhengrong Yue, Xu Huang, Jialv Zou, Minhao Jing, Wenhao Yan, Haodong Li, Hai Huang, Bo Zhao, Yan Feng, Peng Pei, Xunliang Cai
- 链接：[arXiv](https://arxiv.org/abs/2611.12426) · [PDF](https://arxiv.org/pdf/2611.12426) · [HF](https://huggingface.co/papers/2611.12426)

Discrete autoregressive modeling, notably through next-token prediction, has become a cornerstone of modern language models. Extending this paradigm to vision allows visual and language models to converge on a unified framework, thereby fostering shared methodology and infrastructure. This work investigates a central question: how far can a finite discrete vocabulary go in representing the richness of the visual…

## 81. Beyond Sunny Skies: Using Large Language Models to Predict Urban Traffic in Adverse Weather

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, language model, large language, spec
- 作者：Zhu Xiao, Kuan Feng, Tong Li, Chenxi Liu, Gang Wang, Zhuo Tang, Kenli Li
- 链接：[arXiv](https://arxiv.org/abs/2611.12635) · [PDF](https://arxiv.org/pdf/2611.12635) · [HF](https://huggingface.co/papers/2611.12635)

Urban traffic flow prediction is a cornerstone of intelligent transportation systems, yet accurate forecasting under adverse weather conditions remains a significant challenge. Existing data-driven models, while effective for routine patterns, often struggle with the sparse data and complex non-linear shifts associated with rare meteorological events. These methods typically treat environmental contexts as shallow…

## 82. Simulation-aided Reinforcement Learning with Control Variates

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reinforcement learning, evaluation, benchmark, spec
- 作者：Omer Hemo, Ido Sefi, Mirco Mutti, Aviv Tamar, Kfir Y. Levy
- 链接：[arXiv](https://arxiv.org/abs/2611.12643) · [PDF](https://arxiv.org/pdf/2611.12643) · [HF](https://huggingface.co/papers/2611.12643)

Reinforcement Learning (RL) algorithms often rely on data collected from a target environment, which can be expensive and noisy. Although simulators can generate large amounts of additional data, standard simulation mixing approaches, which directly combine simulated and real experience, can degrade performance due to simulator inaccuracies, especially when they bias the solution away from the optimal policy. We…

## 83. A local language model layered with rule-based and neural detectors for clinical text de-identification: an open-source toolkit and evaluation

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, language model, large language, spec
- 作者：Valentin Burkin
- 链接：[arXiv](https://arxiv.org/abs/2611.12709) · [PDF](https://arxiv.org/pdf/2611.12709) · [HF](https://huggingface.co/papers/2611.12709)

Objectives: To measure whether a locally hosted large language model (LLM), stacked with deterministic and clinical named-entity recognition (NER) detectors, finds more protected health information (PHI) than open tools, and at what precision. Materials and Methods: DeidSharp, an open-source .NET toolkit, combines the findings of pluggable detectors (patterns, a clinical NER model, a local 26B mixture-of-experts…

## 84. Safe Reinforcement Learning for Multi-Turn Clinical Agents: When Dense Rewards Beat Outcome Rewards

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reasoning, reinforcement learning, evaluation, language model
- 作者：Brendan P. Murphy, Agustina Saenz
- 链接：[arXiv](https://arxiv.org/abs/2611.12728) · [PDF](https://arxiv.org/pdf/2611.12728) · [HF](https://huggingface.co/papers/2611.12728)

Reinforcement learning with verifiable rewards is increasingly used to improve language model reasoning, yet its effects on sequential decision procedures remain poorly understood. We study this problem in clinical multi-turn agents that must decide what information to request, when to stop gathering evidence, and which action to take. We introduce three controlled environments: medication refill triage, acute…

## 85. Inference Validation for Regulated AI: Building a Decision Pipeline on NVIDIA AIPerf

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：language model, large language, coding, spec
- 作者：Dev Akre, Roman Bobalo, Manoj Dobbali
- 链接：[arXiv](https://arxiv.org/abs/2611.12737) · [PDF](https://arxiv.org/pdf/2611.12737) · [HF](https://huggingface.co/papers/2611.12737)

Deploying large language models in regulated industries requires more than picking the fastest inference engine: it requires evidence that a configuration meets contractual and legal obligations before it serves a single customer request. We describe Runway, an internal validation harness built at MasterControl that builds a governed decision pipeline around NVIDIA AIPerf. The key insight is separating concerns:…

## 86. The Narrative Gap: Can LLMs Help Us Navigate Diverse Narratives Across Languages?

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, language model, large language, spec
- 作者：Nikhil Sharma, Kelly Marchisio, Kenton Murray, Ziang Xiao
- 链接：[arXiv](https://arxiv.org/abs/2611.12750) · [PDF](https://arxiv.org/pdf/2611.12750) · [HF](https://huggingface.co/papers/2611.12750)

Large language models (LLMs) increasingly mediate how people seek and consume information, including accounts that differ across languages and regions, especially on contested topics. Supporting diverse information seeking requires models to help users navigate competing narratives across languages and information streams. We define six capabilities necessary for diverse multilingual information seeking: three…

## 87. Large Language Models as a Universal Searcher for Open-World Automated Machine Learning

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, reinforcement learning, benchmark, language model, large language, coding, spec
- 作者：Yuxuan Hu, Jihao Liu, Weikang Shi, Xijie Huang, Linda Wei, Mingjie Zhan, Aojun Zhou, Rui Liu, Hongsheng Li
- 链接：[arXiv](https://arxiv.org/abs/2611.12791) · [PDF](https://arxiv.org/pdf/2611.12791) · [HF](https://huggingface.co/papers/2611.12791)

Developing effective machine learning models requires complex manual tuning, while current Automated Machine Learning (AutoML) frameworks remain domain-specific and isolate model architecture, training hyperparameter, and data ratio optimization. Here, we bridge this gap by proposing a universal, large language model (LLM)-based AutoML framework that jointly optimizes these configurations for the first time without…

## 88. Complementarity-Driven Dual-Teacher Hierarchical Alignment for Zero-Shot EEG-to-Image Retrieval

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, coding, spec, retrieval
- 作者：Lukun Wu, Jie Li, Ziqi Ren, Ruiyang Xia, Yan Gao, Xinbo Gao
- 链接：[arXiv](https://arxiv.org/abs/2611.12798) · [PDF](https://arxiv.org/pdf/2611.12798) · [HF](https://huggingface.co/papers/2611.12798)

Decoding visual information from EEG is central to brain--computer interfaces and brain-inspired intelligence, and contrastive alignment with pretrained vision foundation models (VFMs) has become the dominant paradigm. However, existing methods align EEG solely with CLIP-family VFMs, leaving hierarchical visual information in neural responses under-exploited. To address this gap, we formulate a mechanism-paradigm…

## 89. Agentic-OPD: Recovering Forgotten Agent Capabilities via On-Policy Distillation for Agentic Tasks

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reinforcement learning, benchmark, spec
- 作者：Tingcheng Bian, Kangye Gong, Jinchang Luo, MingQuan Cheng, Feiran Liu, Ni Li, Xiaoling Xia, Haiwei Wang, Hui Li
- 链接：[arXiv](https://arxiv.org/abs/2611.12799) · [PDF](https://arxiv.org/pdf/2611.12799) · [HF](https://huggingface.co/papers/2611.12799)

Reinforcement learning is now the mainstream paradigm for training LLMs on agentic tasks, yet standard practice keeps only the best-validation checkpoint and discards the rest. We show that this is lossy: in GRPO training of LLM agents, the best-validation checkpoint fails on problems that earlier checkpoints from the same run had already solved, and the union of problems solved across checkpoints far exceeds any…

## 90. MaxIM: Maximally Informative Incremental Summarization via Reinforcement Learning

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, reinforcement learning, evaluation, benchmark
- 作者：Jihwan Jeong, Guy Tennenholtz, Yinlam Chow, Chih-Wei Hsu, Craig Boutilier
- 链接：[arXiv](https://arxiv.org/abs/2611.12825) · [PDF](https://arxiv.org/pdf/2611.12825) · [HF](https://huggingface.co/papers/2611.12825)

AI systems must often maintain bounded memory of unbounded interaction histories. However, optimizing the memory representation, and its updates, for downstream task utility is difficult for standard reinforcement learning (RL) due to severe credit assignment bottlenecks induced by sparse, delayed rewards. We introduce MaxIM (Maximally Informative Incremental Memory), a framework that formulates incremental…

## 91. Mitigating Agentic Deception via Evaluation-Side Partially Observable Games

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, tool use, reasoning, evaluation, language model, large language
- 作者：Hanxiao Li, Shutong Liu, Yongjia Ma, Jiaming Ji, Juntao Dai, Shuning Zhang, Kejian Shi, Kai Chen, Pu Feng, Yuqing Ma, Qi Dou, Yaodong Yang, Xianglong Liu, Simin Li
- 链接：[arXiv](https://arxiv.org/abs/2611.12835) · [PDF](https://arxiv.org/pdf/2611.12835) · [HF](https://huggingface.co/papers/2611.12835)

As large language models become more capable agents, they can exhibit deceptive behaviors, cheating human for higher rewards while appearing helpful. We attribute this failure to evaluation-side partial observability, where models are evaluated mainly from final outcome, without checking the faithfulness of underlying reasoning, tool use, and environmental effects. Prior mitigations address this partial…

## 92. WorkflowArena: Benchmarking Executable Workflow Orchestration in LLM-Based Multi-Agent Systems

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, evaluation, benchmark, language model, large language, spec
- 作者：Zheng Jiang, Fang Niu, Bo Peng, Houde Qian, Wenyi Li, Deyao Hong, Mingju Gao, Yizhe Chi, Youjie Zheng, Kaisen Yang, Calvin Xiao, Lifeng Sun, Huan-ang Gao
- 链接：[arXiv](https://arxiv.org/abs/2611.12856) · [PDF](https://arxiv.org/pdf/2611.12856) · [HF](https://huggingface.co/papers/2611.12856)

Large language model agents are increasingly deployed as multi-agent systems rather than as a standalone model operating within a single context. Recent agent harnesses allow the model to instantiate worker agents and to author the executable workflow that coordinates them, shifting the design of system structure from developers to the model at run time. The quality of this organization therefore constitutes a…

## 93. HiVe-Mem: Interleaving Horizontal Memory Expansion and Vertical Evidence Composition for Multimodal Agents

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, memory, benchmark, retrieval
- 作者：Haozhen Zhang, Bohan Liu, Jianzhu Bao, Qingyuan Liu, Haodong Yue, Xiao Li, Zi Pong Lim, Wenya Wang
- 链接：[arXiv](https://arxiv.org/abs/2611.12872) · [PDF](https://arxiv.org/pdf/2611.12872) · [HF](https://huggingface.co/papers/2611.12872)

As multimodal agents accumulate increasingly long interaction histories, effectively retrieving and utilizing past information becomes critical for long-term interaction. Existing memory systems typically rely on semantic retrieval over compressed memories and expose predefined representations, which may miss relevant memories and overlook heterogeneous evidence needs across queries. We introduce \textbf{\hivemem},…

## 94. Adaptive Quantization Preserves Fast Rates for TD Learning over Rate-Limited Channels

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reinforcement learning, evaluation, spec
- 作者：Sreejeet Maity, Aritra Mitra
- 链接：[arXiv](https://arxiv.org/abs/2611.12878) · [PDF](https://arxiv.org/pdf/2611.12878) · [HF](https://huggingface.co/papers/2611.12878)

Motivated by reinforcement learning subject to communication constraints, we study a policy evaluation problem with linear function approximation over a rate-limited channel. In our setup, an agent interacting with an unknown environment (modeled as a Markov Decision Process) transmits quantized estimates of a temporal-difference (TD) learning update direction to a server over a finite-capacity channel. Our goal is…

## 95. Beyond Modality Preference: Controlling Multimodal Arbitration under Modality Conflict in MLLMs

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, language model, large language, spec
- 作者：Zhaoying Pan, Shenyu Lu, Jun Hui Wong, Junyi Chai, Xiaoqian Wang
- 链接：[arXiv](https://arxiv.org/abs/2611.12883) · [PDF](https://arxiv.org/pdf/2611.12883) · [HF](https://huggingface.co/papers/2611.12883)

Multimodal large language models (MLLMs) integrate information across modalities, but become unreliable when those modalities disagree. Under conflicting inputs, MLLMs may favor modalities that are not the most reliable for the task, thus motivating inference-time control of modality arbitration. We identify a small set of attention heads, termed arbitration heads, that causally influence whether predictions follow…

## 96. Reframe: Observation-Aligned Multi-Teacher On-Policy Distillation for Agentic Visual Reasoning

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, tool use, reasoning, reinforcement learning, benchmark, spec
- 作者：Haozhi Yuan, Handong Li, Yifan Zhang, Qianshan Wei
- 链接：[arXiv](https://arxiv.org/abs/2611.12886) · [PDF](https://arxiv.org/pdf/2611.12886) · [HF](https://huggingface.co/papers/2611.12886)

Agentic reinforcement learning (RL) and multi-teacher on-policy distillation (MOPD) offer complementary routes to post-training. For visual agents, however, tool use presents two related challenges. Models may overlook useful tool-returned observations, while poorly grounded actions can limit the evidence available for subsequent distillation. We introduce Reframe, a post-training framework that treats the…

## 97. Horizon-Scalable Q-Learning

- 分数：8.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：-
- 作者：Haoran Xu, Pragya Srivastava, Xinjie Liu, Siddhant Agarwal, Amy Zhang
- 链接：[arXiv](https://arxiv.org/abs/2611.10987) · [PDF](https://arxiv.org/pdf/2611.10987) · [HF](https://huggingface.co/papers/2611.10987)

Learning accurate off-policy state-action value functions (Q-functions) from offline datasets becomes harder as the task horizon grows. One-step temporal-difference (TD) learning bootstraps after every transition, so small per-step errors accumulate along the horizon, and early states can be badly misvalued even when the TD loss is small. Multi-step TD shortens this chain by following the dataset trajectory for…

## 98. BECON: Belief-Conditioned Constrained Multi-Objective Reinforcement Learning under Drifting Preferences and Budgets

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reinforcement learning, spec
- 作者：Bui Trong Duc, Huynh Thi Thanh Binh
- 链接：[arXiv](https://arxiv.org/abs/2611.12053) · [PDF](https://arxiv.org/pdf/2611.12053) · [HF](https://huggingface.co/papers/2611.12053)

Constrained preference-conditioned MORL typically assumes full task observability, treating preferences and safety budgets as stationary task signals. In real-world deployment, however, these signals are often unreliable proxies: intent may drift, safety tolerances may shift with context, and exposed descriptors may be noisy, delayed, or incomplete. We therefore formulate constrained preference-conditioned MORL as a…

## 99. SadaqahStories: A Verified English-Arabic Corpus of Charity Stories for Children, with an Audit of Errors in AI-Drafted Religious Narratives

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：language model, large language, spec
- 作者：Wajdi Zaghouani, Spencer Striker
- 链接：[arXiv](https://arxiv.org/abs/2611.12078) · [PDF](https://arxiv.org/pdf/2611.12078) · [HF](https://huggingface.co/papers/2611.12078)

We present SadaqahStories, a parallel English-Arabic corpus of 41 illustrated four-page stories about charitable giving in Islam (Sadaqah, Zakat and Waqf), written for readers aged 7 to 18. The stories were first drafted with large language model (LLM) assistance, then audited against hadith collections, Qur'an references and historical sources, and finally rewritten for children and signed off by an Islamic…

## 100. Joi-Bench-Task: Benchmarking Task Coordination in Full-duplex Voice Agents through Interactive Simulation

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, evaluation, benchmark
- 作者：Xiangheng He, Mingjun Zhao, Zhehao Fan, Zhengjia Li, Xiaopeng Sun, Qingqing Xiao, Haolan Chen, Yu Xu
- 链接：[arXiv](https://arxiv.org/abs/2611.12118) · [PDF](https://arxiv.org/pdf/2611.12118) · [HF](https://huggingface.co/papers/2611.12118)

Full-duplex voice agents enable natural, hands-free interaction, allowing users to refine requests, redirect ongoing work, and seek clarification while the agent is speaking. However, existing voice-agent benchmarks insufficiently isolate coordination between task execution and conversation. We introduce a benchmark that assesses this coordination by examining whether agents track what is being executed, what has…

## 101. CARE-PO: Controllable Tool-Call Efficiency for LLM Agents

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, tool-use, benchmark
- 作者：Xiaoyang Ye, Xiao Yao, Hairui Zhu, Yiying Yang, Bei Gan, Jinliang Lu, Tengjin Weng, Yuan Yao, Wenhao Jiang
- 链接：[arXiv](https://arxiv.org/abs/2611.12125) · [PDF](https://arxiv.org/pdf/2611.12125) · [HF](https://huggingface.co/papers/2611.12125)

External tool calls are a major running cost of an LLM agent, while its training objectives align almost exclusively with task completion. In a step-level diagnosis of Qwen3.5 trajectories at two model sizes on GAIA, a long-horizon tool-use benchmark, we find that most contain removable calls, at a similar rate at both sizes. Some methods add an efficiency reward to the objective to reduce the call count, but…

## 102. Do Time-Series Foundation Models Forecast Index-Futures Returns? A Preregistered Evaluation of Models, Metrics, and Input Representations

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, spec
- 作者：Rishabh Upadhyay
- 链接：[arXiv](https://arxiv.org/abs/2611.12141) · [PDF](https://arxiv.org/pdf/2611.12141) · [HF](https://huggingface.co/papers/2611.12141)

We ask whether the apparent forecasting skill of frozen time-series foundation models (TSFMs) on intraday index-futures returns is incremental skill. In a pre-registered evaluation on E-mini Nasdaq-100 (NQ) and E-mini S&P 500 (ES) futures, a common panel of five zero-shot models (Chronos-Bolt, Chronos-2, TimesFM 2.5, Moirai 2.0 and TiRex), plus separate experiments with Kronos, is compared with a no-change forecast…

## 103. Harnessing Vision-Language Models for Federated Unsupervised Visual Recognition

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：language model, coding, spec
- 作者：Jian Liang, Kuangpu Guo, Ran He, Tieniu Tan
- 链接：[arXiv](https://arxiv.org/abs/2611.12187) · [PDF](https://arxiv.org/pdf/2611.12187) · [HF](https://huggingface.co/papers/2611.12187)

Federated learning (FL) is a promising research paradigm that enables collaborative model training across distributed clients without data sharing. To handle unlabeled data in local clients, existing unsupervised FL research has primarily focused on tasks like clustering and self-supervised representation learning, leaving the critical problem of unsupervised visual recognition largely unexplored. To bridge this…

## 104. A Cost That Practice Accuracy Hides: Worked Solutions in Self-Generated Training Data and the Compositional Use of New Rules

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, evaluation, spec
- 作者：Jiantong Xu
- 链接：[arXiv](https://arxiv.org/abs/2611.12225) · [PDF](https://arxiv.org/pdf/2611.12225) · [HF](https://huggingface.co/papers/2611.12225)

A worked solution can make self-generated training targets shorter and cheaper, but accuracy on the practiced operation may hide how well a model can reuse newly learned rules. We study this choice in a 2B-parameter reasoning model learning two invented quantitative rules. The model generates targets from a rule sheet alone or from the sheet plus a program-written worked solution; targets are accepted for…

## 105. Prune, Don't Merge: Expert Compression of Mixture-of-Experts LLMs on Multilingual Production Tasks

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, benchmark, language model
- 作者：Tomas Rasymas, Povilas Kvedaras
- 链接：[arXiv](https://arxiv.org/abs/2611.12240) · [PDF](https://arxiv.org/pdf/2611.12240) · [HF](https://huggingface.co/papers/2611.12240)

Mixture-of-Experts language models are cheap to run per token but expensive to hold in GPU memory, which drives the cost of serving them in production. One-shot expert compression shrinks them after a single calibration pass. Its two current state-of-the-art methods are REAP for expert pruning, which deletes the least salient experts, and REAM for expert merging, which merges them into the most salient ones. Both…

## 106. VLA-MOPD: On-Policy Distillation for Multi-Task VLA Policy Consolidation

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reinforcement learning, spec
- 作者：Yongxuan Lv, Zhen Fang, Lichen Man, Hao Li, Pu Li, Hengyi Wang, Langfeng Cao, Lin Chen, Jie Huang, Xiu Su, Shan You, Fei Wang, Feng Zhao
- 链接：[arXiv](https://arxiv.org/abs/2611.12286) · [PDF](https://arxiv.org/pdf/2611.12286) · [HF](https://huggingface.co/papers/2611.12286)

Physical intelligence requires embodied agents to ground language in observations and execute actions while retaining useful skills. Vision-language-action (VLA) policies offer a shared interface, but task-specific post-training often produces separate specialists. Consolidation is difficult: mixed-task reinforcement learning provides sparse trajectory-level credit, while offline distillation may miss…

## 107. RecoGEM: A Serving System for Production-Scale Generative Recommendation

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：coding, spec, planning
- 作者：Xiangrui Yang, Yunfeng Zhao, Jiawei Yang, Fangyu Zhang, Enrui Zhao, Liang Zeng, Cheng Peng, Minhui Xie, Jiaqiang Liu, Xiao Liang, Yiming Qiu
- 链接：[arXiv](https://arxiv.org/abs/2611.12296) · [PDF](https://arxiv.org/pdf/2611.12296) · [HF](https://huggingface.co/papers/2611.12296)

Generative recommendation (GR) is moving industrial recommender systems (RecSys) from scoring candidate items to autoregressively generating item identifiers. This shift promises higher recommendation quality, but makes serving substantially harder: each request executes a short sequence of dependent decoding steps that explore a large item space and select promising candidates on the latency-critical path. GR not…

## 108. Physics-Informed Sinusoidal Representation Networks for Damage Identification in Ultrasonic Guided Wave Structural Health Monitoring

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, spec
- 作者：Lukas Jilke, Caspar Wasle, Norbert Hosters, Florian Raddatz, Marek Behr, Gerko Wende
- 链接：[arXiv](https://arxiv.org/abs/2611.12299) · [PDF](https://arxiv.org/pdf/2611.12299) · [HF](https://huggingface.co/papers/2611.12299)

Ultrasonic guided wave (UGW) inspection has become an effective method in structural health monitoring (SHM). While machine learning has enhanced damage detection capabilities, purely data-driven models remain constrained by extensive labeled datasets and limited physical interpretability. Standard multi-layer perceptrons (MLPs) further suffer from spectral bias (F-Principle) in high-frequency regimes, prioritizing…

## 109. AutoBuddy: Evaluating Proactive, Always-On Agents on Task Discovery and Execution in a Simulated Workplace

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, evaluation, benchmark
- 作者：Shiqi Chen, Daniel Madrigal Diaz, Wei-Ning Chen, Gbola Afonja, Fangkai Yang, Rujia Wang, Chetan Bansal, Victor Rühle, Saravan Rajmohan, Dongge Han
- 链接：[arXiv](https://arxiv.org/abs/2611.12393) · [PDF](https://arxiv.org/pdf/2611.12393) · [HF](https://huggingface.co/papers/2611.12393)

As LLM agents become more autonomous, they are increasingly expected to run as always-on assistants on a user's behalf, identifying work to be done and completing it without being asked. Yet existing benchmarks usually give the agent its task, whereas in knowledge work the requests sit in the user's workspace and the agent must first recognise which obligations exist. We study proactive task discovery and execution,…

## 110. Can Frontier Auto Researchers Reconstruct Human Research Decisions in AI?

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, evaluation, spec
- 作者：Shengyun Si, Junjie Chu, Ye Leng, Yang Zhang
- 链接：[arXiv](https://arxiv.org/abs/2611.12429) · [PDF](https://arxiv.org/pdf/2611.12429) · [HF](https://huggingface.co/papers/2611.12429)

Scientific research has long been driven by substantial human effort, from reviewing prior work and identifying research gaps to designing specific solutions. Recent advances in harness-based agent systems have given rise to increasingly capable Auto Researchers, which can autonomously carry out these tasks and, increasingly, entire end-to-end research workflows. Yet despite their rapidly growing capabilities, how…

## 111. Causal discovery from Bayesian symbolic regression

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, benchmark, spec
- 作者：Roger Guimerà, Kai-Hendrik Cohrs, Sergio Pedreira, Marta Sales-Pardo, Gustau Camps-Valls
- 链接：[arXiv](https://arxiv.org/abs/2611.12458) · [PDF](https://arxiv.org/pdf/2611.12458) · [HF](https://huggingface.co/papers/2611.12458)

Causal discovery from observational data is central to scientific reasoning, yet established constraint-based and score-based methods often recover only a Markov equivalence class and provide no signal in bivariate or strongly autocorrelated regimes typical in some areas of science. Here, we recast causal discovery as a Bayesian symbolic regression problem. Given a set of candidate parents for each target variable,…

## 112. AuDiR: Diagnosing Audio Reasoning with Rule and Percept Interventions

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, evaluation, benchmark
- 作者：Chengwei Wei, Yi Ma, Nancy F. Chen
- 链接：[arXiv](https://arxiv.org/abs/2611.12478) · [PDF](https://arxiv.org/pdf/2611.12478) · [HF](https://huggingface.co/papers/2611.12478)

Answer accuracy alone does not distinguish failures in acoustic perception, rule knowledge, and rule application. AuDiR (Audio Diagnostic Reasoning) examines these distinctions through controlled input interventions. Each item contains an audio clip, a multiple-choice question, a task-general rule, and a textual description of the acoustic observations needed to answer. Three conditions progressively supply the rule…

## 113. UniHam: A Large-Scale SOC-Complete Dataset and Benchmark for Hamiltonian Learning in Materials

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, spec
- 作者：Yuewen Huang, Pin Chen, Yutong Lu
- 链接：[arXiv](https://arxiv.org/abs/2611.12509) · [PDF](https://arxiv.org/pdf/2611.12509) · [HF](https://huggingface.co/papers/2611.12509)

Accurate prediction of electronic Hamiltonians would enable broad property inference while avoiding the high computational cost of Density Functional Theory (DFT). However, progress toward general-purpose materials foundation models is limited by a data bottleneck: existing Hamiltonian datasets are typically small, lack structural diversity, and often omit essential relativistic physics such as spin--orbit coupling…

## 114. EditJudge-Bench: Auditing VLM Image-Edit Judges with Synthetic Ground Truth

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, language model
- 作者：Jens Parslov, Marco Schouten, Dim P. Papadopoulos
- 链接：[arXiv](https://arxiv.org/abs/2611.12524) · [PDF](https://arxiv.org/pdf/2611.12524) · [HF](https://huggingface.co/papers/2611.12524)

Vision-language models (VLMs) are increasingly used as automated judges for image-editing benchmarks, yet their reliability is poorly understood. Auditing these judges is difficult because real edited images lack controlled ground truth and entangle the requested changes with model artefacts, unintended side effects, and ambiguous degrees of success. In this paper, we introduce EditJudge-Bench, a diagnostic…

## 115. WanderBench: Can World Models Explore Dynamic Worlds from Video?

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, evaluation, benchmark
- 作者：Yuhang Chen, Jiheng Li, Jiale Wang, Zai Wang, Guangyue Liu
- 链接：[arXiv](https://arxiv.org/abs/2611.12557) · [PDF](https://arxiv.org/pdf/2611.12557) · [HF](https://huggingface.co/papers/2611.12557)

Video world models conditioned on an input video make it possible to explore real, recorded dynamic scenes, enabling re-shooting of footage, free-viewpoint replay, and real-to-sim environments for embodied agents. Such uses require the generated rollout to stay faithful to the recorded world, yet existing benchmarks start from a single image or a text prompt, and video-conditioned generation is evaluated mainly on…

## 116. GHiML: VLM-Guided Hierarchical Multi-Label Learning with Applications to Benthic Imagery

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, language model, spec
- 作者：Isaac Xu, Devi Ayyagari, Martin Gillis, Benjamin Misiuk, Craig J. Brown, Thomas Trappenberg
- 链接：[arXiv](https://arxiv.org/abs/2611.12564) · [PDF](https://arxiv.org/pdf/2611.12564) · [HF](https://huggingface.co/papers/2611.12564)

Vision language models (VLMs) encode substantial expert knowledge within their weights, yet their direct application to specialised classification domains such as benthic imagery remains limited. Meanwhile, vision transformers trained on these tasks rely predominantly on low-level visual latents (colours, textures, and shapes) that lack the higher-level reasoning humans employ for identification. We propose Guided…

## 117. TrialDesignBench: Benchmarking Language Models for Phase-I Trial Design Against Clinical Knowledge

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, benchmark, language model
- 作者：Yihan Hank Tang, Peng Yang, Jiayi Xin, Tianqi Shang, Xuyang Chen, Ying Yuan, Yi Lian, Qi Long
- 链接：[arXiv](https://arxiv.org/abs/2611.12640) · [PDF](https://arxiv.org/pdf/2611.12640) · [HF](https://huggingface.co/papers/2611.12640)

AI is used in much of the clinical trial pipeline. However, selecting the statistical design of a trial, a crucial step that determines how drug doses are tested on humans and evaluated, has seen almost no AI progress. LLMs appear to be a natural fit given their strengths in biomedical knowledge and statistical reasoning. Nevertheless, there is currently no appropriate way to evaluate such abilities because recent…

## 118. CoilStellaration: A Dataset and Benchmark for Engineering-Aware Stellarator Coilset Generation

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, spec
- 作者：Jan-Hendrik Ewers, Santiago A. Cadena, Nicolò Foppiani, Andrea Merlo
- 链接：[arXiv](https://arxiv.org/abs/2611.12689) · [PDF](https://arxiv.org/pdf/2611.12689) · [HF](https://huggingface.co/papers/2611.12689)

Stellarators are fusion devices that use externally generated, three-dimensional magnetic fields to confine hot plasma and offer a promising route to commercial fusion. Their electromagnetic coils pose a challenging design problem: they must reproduce the target magnetic field while satisfying engineering constraints and remaining practical and cost-effective to manufacture. Finding suitable geometries is a highly…

## 119. PORT: Preference Optimization via Robust Token-Level Reweighting

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, language model, large language
- 作者：Ding Zhu, Xiukun Wei, Tian Xie, Zhihui Zhu, Xueru Zhang, Mohammad Mahdi Khalili
- 链接：[arXiv](https://arxiv.org/abs/2611.12763) · [PDF](https://arxiv.org/pdf/2611.12763) · [HF](https://huggingface.co/papers/2611.12763)

Preference optimization has become a central approach for aligning large language models with human values, but its effectiveness depends heavily on the quality of preference annotations. In practice, preference data is often noisy due to annotation errors and ambiguity. Existing robust preference optimization methods primarily operate at the sequence level, implicitly treating entire responses as uniformly correct…

## 120. Curbside Chatbots: Auditing the Mental Health Interventions Large Language Models Recommend to Clinicians, Caregivers, and Patients

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：language model, large language, spec
- 作者：Matthew Flathers, Jill Noorily, Phuong Anh Nguyen, Mark Kalinich, Mina Fallah, Victoria Lisowski, Christine Shi, Rebekah M. Bodner, Anna Simms, Mihika Hete, Meiting Chen, Samuel K. Powell, Tatum Williamson, Laura Ospina-Pinillos, Haruka Notsu, Julian Herpertz, John Torous
- 链接：[arXiv](https://arxiv.org/abs/2611.12814) · [PDF](https://arxiv.org/pdf/2611.12814) · [HF](https://huggingface.co/papers/2611.12814)

Users are asking language models mental health questions and are receiving answers. We audited what 41 language models recommend to users when the same clinical information reaches them from three footings: a clinician describing a patient, a caregiver describing a loved one, or a person describing themselves. Across 19 case vignettes and five questions, we collected 35,055 free-text responses, extracted every…
