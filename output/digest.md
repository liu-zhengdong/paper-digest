# 每日 AI 论文

生成时间：2026-10-16 04:33 UTC  ·  共 120 篇（已按 arXiv ID 去重）

来源：Hugging Face Daily Papers + arXiv（cs.AI / cs.LG / cs.CL / cs.CV）。
排序：HF 上榜、点赞、多源命中、兴趣词。兴趣词可在 `config.json` 改。

## 1. Player-1: Learning to Play from Synthetic Experience

- 分数：36.0  ·  HF 赞：284  ·  来源：huggingface
- 兴趣命中：agent, reasoning, reinforcement learning, spec
- 作者：Mingyu Ouyang, Yiran Wang, Siyuan Hu, Xingyilang Yin, Huiqiang Sun, Guangzhi Wang, Junfu Pu, Cheng Cheng, Honghao Chen, Ying Shan, Mike Zheng Shou, Hwee Tou Ng
- 链接：[arXiv](https://arxiv.org/abs/2610.20584) · [PDF](https://arxiv.org/pdf/2610.20584) · [HF](https://huggingface.co/papers/2610.20584)

Computer-use agents have demonstrated strong capabilities in interpreting screens and executing keyboard and mouse actions. However, games, with their visually rich worlds and diverse mechanics, remain challenging and offer a demanding next step toward general digital control. Current game-agent learning pipelines often rely on large-scale demonstrations with limited coverage of dynamic game states, while scalable…

## 2. Doc2Harness: Benchmarking LLMs on Long-Horizon Harness Engineering of Coding Agents

- 分数：36.0  ·  HF 赞：96  ·  来源：huggingface
- 兴趣命中：agent, benchmark, language model, large language, coding
- 作者：Yuyao Ge, Shenghua Liu, Peizhong Gao, Chendi Ge, Chenxu Liu, Yiwei Wang, Lingrui Mei, Baolong Bi, Jiayu Yao, Jiafeng Guo, Xueqi Cheng
- 链接：[arXiv](https://arxiv.org/abs/2610.20344) · [PDF](https://arxiv.org/pdf/2610.20344) · [HF](https://huggingface.co/papers/2610.20344)

Agents driven by large language models are increasingly deployed on long-horizon tasks, where they use tools and modify real workspaces. How well they perform depends as much on the harness around the model as on the model itself. Existing benchmarks measure downstream task success under a fixed harness, leaving harness engineering itself unexplored. We propose Doc2Harness, a two-stage benchmark that evaluates…

## 3. More Methods, Better Agents? A Reality Check on Self-Distillation in Agentic Reinforcement Learning

- 分数：36.0  ·  HF 赞：76  ·  来源：huggingface
- 兴趣命中：agent, reinforcement learning, evaluation, benchmark
- 作者：Linhao Zhong, Bozhen Fang, Xuehao Wang, Duochao Shi, Zekai Luo, Guangming Yao, Yi Yuan, Hao Chen, Jingdong Chen, Chunhua Shen
- 链接：[arXiv](https://arxiv.org/abs/2610.19789) · [PDF](https://arxiv.org/pdf/2610.19789) · [HF](https://huggingface.co/papers/2610.19789)

Self-distillation in agentic reinforcement learning has produced a growing number of methods. However, existing evaluations often reuse published baseline scores under differing experimental conditions, provide few direct comparisons among contemporaneous methods, and give limited attention to training stability and computational cost. These limitations obscure the source of reported gains and the practical…

## 4. Cortex: Consolidating Context into Parametric Memory

- 分数：36.0  ·  HF 赞：64  ·  来源：huggingface
- 兴趣命中：memory, language model, large language, spec
- 作者：Jintian Zhang, Feng He, Xinnian Liang, Ziwen Xu, Haoming Xu, Haojing Huang, Shuangzhi Wu, Ningyu Zhang
- 链接：[arXiv](https://arxiv.org/abs/2610.20399) · [PDF](https://arxiv.org/pdf/2610.20399) · [HF](https://huggingface.co/papers/2610.20399)

Context can improve large language model performance, but these gains may be lost after context removal. Inspired by biological systems consolidation, we formulate Memory Consolidation (MC) as internalizing these gains while preserving non-target capabilities, connecting context-specified editing, skill learning, and behavioral steering under a common objective. We introduce a five-task-family testbed measuring…

## 5. OmniCompass: A Holistic Benchmark for Omni-Modal Video Grounding and Understanding

- 分数：36.0  ·  HF 赞：62  ·  来源：huggingface
- 兴趣命中：reasoning, evaluation, benchmark, language model, large language, spec
- 作者：Xuyang Liu, Shihao Wang, Xinyu Wei, Minghan Li, Zeqing Wang, Zuhao Yang, Zichen Wen, Lei Zhang
- 链接：[arXiv](https://arxiv.org/abs/2610.18829) · [PDF](https://arxiv.org/pdf/2610.18829) · [HF](https://huggingface.co/papers/2610.18829)

With the rapid development of multimodal large language models (MLLMs), evaluating their video understanding capabilities has become increasingly important. Existing video understanding benchmarks cover only part of the evaluation dimensions, limiting systematic diagnosis of omni-modal video understanding. We introduce OmniCompass, a holistic benchmark for omni-modal video grounding and understanding. OmniCompass…

## 6. ActionOPD: Distilling Decisions, Not Tokens

- 分数：36.0  ·  HF 赞：54  ·  来源：huggingface
- 兴趣命中：agent, tool-use, reasoning, benchmark, spec
- 作者：Huining Yuan, Xiangmin Yi, Zelai Xu, Zixu Wang, Xinlei Chen, Xiao-Ping Zhang, Yu Wang, Chao Yu
- 链接：[arXiv](https://arxiv.org/abs/2610.19820) · [PDF](https://arxiv.org/pdf/2610.19820) · [HF](https://huggingface.co/papers/2610.19820)

Distilling capable language-model agents into smaller models requires aligning the student's behavior with the teacher's. This raises a fundamental question: at which states and at what granularity should this alignment be performed? Offline imitation provides dense but token-specific supervision and can suffer from state-distribution mismatch. Token-level on-policy distillation (OPD) addresses this mismatch but…

## 7. Seeing, Maintaining, and Learning: The Evolution of Multimodal Agent Memory

- 分数：36.0  ·  HF 赞：46  ·  来源：huggingface
- 兴趣命中：agent, memory, reasoning, spec
- 作者：Minghao Guo, Qingyue Jiao, Xiujin Liu, Jianhong Pang, Ruimeng Yang, Naihao Xu, Liwei Che, Haochen Xue, Ziqi Wang, Xinying Cai, Jiaxuan Luo, Jiaxin Deng, Xuesong Ye, Jintao Qu, Wenyao Gao, Jingwen Gu, Chenyang Zhao, Shichun Liu, Guibin Zhang, Zefang Liu, Siyin Wang, Wujiang Xu, Danrui Li, Zeru Shi, Woongyeong Yeo, Shuang Liu, Wei-Chieh Huang, Weizhi Zhang, Tianyu Yang, Kangsan Kim, Yebowen Hu, Bowen Wen, Bowen Jiang, Haohao Su, Ming Yin, Sheldon Yu, Mian Zhang, Yuyan Chen, Hanrong Zhang, Kai Mei, Zihao Zhang, Mingyu Jin, Xi Zhu, Hengyi Wang, Tianxin Wei, Linyong Nan, Zhenwen Liang, Zhendong Chu, Ziqi Huang, Yongye Su, Sixun Dong, Shujian Liu, Kaiqu Liang, Jiaojiao Han, Zhaoye Fei, Kun Wang, Shihan Dou, Zhichun Guo, Xingjian Diao, Zeqi Gu, Heng Wang, Tao Feng, Cheng Qian, Hamid Palangi, Silei Xu, Xi Yun, Yi Zhu, Shilong Liu, Qingsong Wen, Sung Ju Hwang, Zuxuan Wu, Yu-Gang Jiang, Yiyu Shi, Dimitris N. Metaxas, Jiaxuan You, Julian McAuley, Mengdi Wang, Jiawei Han, Philip S. Yu, Ziyi Ye
- 链接：[arXiv](https://arxiv.org/abs/2610.19366) · [PDF](https://arxiv.org/pdf/2610.19366) · [HF](https://huggingface.co/papers/2610.19366)

Multimodal models and agents have emerged to enable AI systems to learn from and interact with the real world more like humans by integrating information across multiple modalities. However, enabling multimodal agents to continually acquire useful information from complex, heterogeneous multimodal data remains a significant challenge as they move toward long-horizon tasks and lifelong settings. Addressing this…

## 8. LensErase: A Foundation Model for Erase Anything

- 分数：36.0  ·  HF 赞：40  ·  来源：huggingface
- 兴趣命中：reinforcement learning, evaluation, benchmark, coding, spec
- 作者：Yunuo Chen, Xiuyu Wu, Qinhong Yang, Jinjing Zhao, Yanchen Dong, Sirui Zhang, Dong Chen, Fangyun Wei, Lei Shi, Ji Li, Dongdong Chen, Guo Lu, Yan Lu, Baining Guo
- 链接：[arXiv](https://arxiv.org/abs/2610.18072) · [PDF](https://arxiv.org/pdf/2610.18072) · [HF](https://huggingface.co/papers/2610.18072)

We introduce LensErase, a general-purpose mask-based Erase Anything foundation model designed to cover a broad spectrum of real-world erase scenarios. LensErase supports diverse objects, visual text, watermarks, associated visual effects, multiple-object removal, and a wide range of object scales, aspect ratios, and image resolutions. First, to enable such broad coverage, we construct LensErase-100M, a large-scale…

## 9. Any Time, Any Space: A World-State-Centric Framework for Agentic Video Generation

- 分数：34.0  ·  HF 赞：332  ·  来源：huggingface
- 兴趣命中：agent, memory, benchmark
- 作者：Weijie Wang, Haomin Zhang, Ye Li, Akide Liu, Zeyu Zhang, Haoyu Zhao, Yefei He, Donny Y. Chen, Feng Chen, Bohan Zhuang
- 链接：[arXiv](https://arxiv.org/abs/2610.20571) · [PDF](https://arxiv.org/pdf/2610.20571) · [HF](https://huggingface.co/papers/2610.20571)

Long-form agentic video generation must turn a screenplay into shots that remain spatially and temporally consistent across nonconsecutive requests. Passing prompts or recent frames between shots does not provide a shared spatial frame for revisiting a scene or a time-indexed record for replaying an earlier event. We present Any Time, Any Space (ATAS), which compiles a screenplay into shot requests with explicit…

## 10. Speculative Forcing for Efficient Autoregressive Video Generation

- 分数：34.0  ·  HF 赞：46  ·  来源：huggingface + arxiv
- 兴趣命中：spec
- 作者：Hyunwook Choi, Seungryong Kim, Dongyoon Han, Sangdoo Yun
- 链接：[arXiv](https://arxiv.org/abs/2610.22347) · [PDF](https://arxiv.org/pdf/2610.22347) · [HF](https://huggingface.co/papers/2610.22347)

Few-step autoregressive video generators enable streaming generation, yet they run every token through the final denoising step, regardless of how much refinement it needs. We find this uniform computation is often unnecessary: many tokens already closely match their eventual full-step outputs in the initial steps, while others require refinement until the end. We introduce Speculative Forcing, a framework that…

## 11. Recovering Reliable Supervision via Critique-Guided On-Policy Distillation

- 分数：32.0  ·  HF 赞：76  ·  来源：huggingface
- 兴趣命中：reasoning, benchmark
- 作者：Kaixiang Zhao, Tianrun Yu, Shangzhe Li, Yuxiao Yang, Amanda Hughes, Weitong Zhang, Taylor W. Killian
- 链接：[arXiv](https://arxiv.org/abs/2610.20572) · [PDF](https://arxiv.org/pdf/2610.20572) · [HF](https://huggingface.co/papers/2610.20572)

On-policy distillation (OPD) trains a student model on its own rollouts with token-level supervision from a teacher, assuming that the teacher can reach a correct answer from any prefix the student writes. We call this property the recoverability of the teacher and show it fails on incorrect rollouts: the teacher follows student errors, although it recognizes them. We propose CriticOPD, using error recognition to…

## 12. CLASHarness: Benchmarking Multi-Agent Conflict in Computer Use via a Controllable and Verifiable Generation Pipeline

- 分数：30.5  ·  HF 赞：29  ·  来源：huggingface
- 兴趣命中：agent, benchmark, language model, spec, planning
- 作者：Yuxiang Lai, Jike Zhong, Chengzhi Liu, Ming Li, Haonan Wang, Xiaofeng Yang, Liang Zhao, Youbao Tang, Ruixi Fan
- 链接：[arXiv](https://arxiv.org/abs/2610.19128) · [PDF](https://arxiv.org/pdf/2610.19128) · [HF](https://huggingface.co/papers/2610.19128)

Vision-language models (VLMs) are increasingly deployed in multi-agent systems to automate complex computer-use workflows, yet existing benchmarks mostly assume consistent, cooperative environments. In contrast, real-world collaboration rarely runs on consistent information: peer or sub-agents frequently report outdated states, issue contradictory instructions, or compete over shared permissions and files, forcing…

## 13. Beyond Domain-Routed Supervision: Cross-Teacher Guarding for Multi-Teacher On-Policy Distillation

- 分数：30.0  ·  HF 赞：237  ·  来源：huggingface
- 兴趣命中：spec
- 作者：Shi-Yu Tian, Yong Liu, Ximan Liu, Tianrui Zhu, Sule Bai, Xinwei Yang, Ruiqi Liu, Kun-Yang Yu, Ming Yang, Zhi Zhou, Yu-Feng Li, Yipeng Sun, Gu Simiu
- 链接：[arXiv](https://arxiv.org/abs/2610.13521) · [PDF](https://arxiv.org/pdf/2610.13521) · [HF](https://huggingface.co/papers/2610.13521)

Multi-teacher on-policy distillation (MOPD) extends on-policy distillation (OPD) by routing domain-specific data to specialized teachers, integrating their capabilities through dense token-level supervision on student-generated trajectories. However, domain routing only distinguishes the supervision sources for different domains; updates from all domains still act on shared parameters. When teachers differ…

## 14. LatentLoop: Scaling Looped MoE Models with Asymmetric Compute Allocation

- 分数：30.0  ·  HF 赞：65  ·  来源：huggingface
- 兴趣命中：benchmark
- 作者：Zefeng He, Yunkai Chai, Xiaoyang Chen, Tong Zhu, Zongliang Wu, Yun Luo, Yafu Li, Yu Cheng
- 链接：[arXiv](https://arxiv.org/abs/2610.19975) · [PDF](https://arxiv.org/pdf/2610.19975) · [HF](https://huggingface.co/papers/2610.19975)

Looped Mixture-of-Experts (MoE) models combine parameter reuse with sparse computation to improve performance under matched budgets. Prior work demonstrates that different loop visits can play different roles even when they share parameters. To probe the contributions of different loop visits, we learn separate residual coefficients in a model that applies a shared block twice, observing a smaller scale in the first…

## 15. Many Right Answers, One Training Example: Removing Responder Noise from GRPO for LLM Recommenders

- 分数：29.5  ·  HF 赞：39  ·  来源：huggingface
- 兴趣命中：reinforcement learning
- 作者：Xin Li, Hao Jiang, Jinghao Guo, Weisi Lin, Chau Yuen
- 链接：[arXiv](https://arxiv.org/abs/2610.17771) · [PDF](https://arxiv.org/pdf/2610.17771) · [HF](https://huggingface.co/papers/2610.17771)

A recommendation request on Reddit draws several replies, each naming different titles. When an LLM recommender is trained on such threads with reinforcement learning (RL), which replies should a generated list be rewarded against? The state-of-the-art recipe, Rank-GRPO, picks one reply per training example, so the advantage mostly records which reply was drawn (85% of its variance) rather than how good the list is.…

## 16. Towards Agentic Robots: Model, Data, Environment, and Harness

- 分数：29.5  ·  HF 赞：31  ·  来源：huggingface
- 兴趣命中：agent, evaluation, planning
- 作者：Chonghan Qin, Dongming Wu, Kaituo Feng, Jiaxu Wang, Xinlei Yu, Peiwen Sun, Yijia Fan, Xilin He, Bingao Chen, Weitong Lian, Ryan Ji, Wenqi Ren, Xiaobin Hu, Dahua Lin, Yu-Gang Jiang, Xiangyu Yue
- 链接：[arXiv](https://arxiv.org/abs/2610.20442) · [PDF](https://arxiv.org/pdf/2610.20442) · [HF](https://huggingface.co/papers/2610.20442)

Foundation models are driving a paradigm shift in robotic intelligence, moving beyond low-level action prediction to goal-directed orchestration of data collection, model training, task planning, and real-world execution. We characterize this emerging paradigm as an agentic robots, in which agents reason over human instructions, interact with robotic environments, rectify execution errors autonomously, and…

## 17. 3DCodeVerse: Exploring 3D Worlds as Code

- 分数：29.0  ·  HF 赞：18  ·  来源：huggingface + arxiv
- 兴趣命中：agent, reasoning, evaluation, coding, spec
- 作者：Yipeng Gao, Ziyao Zeng, Jinfa Huang, Yijiang Li, Haolin Xiong, Wang Qin, Xinlei Yu, Youheng Yao, Jie Zhang, Kun-Yu Lin, Rong Liu, Yinyuan Zhao, Yajie Zhao, Meiqi Guo, Jiebo Luo, Lei Shu, Yunhao Ge, Xinyu Hu, Laurent Itti
- 链接：[arXiv](https://arxiv.org/abs/2610.22341) · [PDF](https://arxiv.org/pdf/2610.22341) · [HF](https://huggingface.co/papers/2610.22341)

We introduce 3DCodeVerse, a research ecosystem that enables coding agents to create editable and verifiable 3D content at scale. 3DCodeVerse comprises large-scale, high-quality datasets of executable 3D code, a coding harness for spatial reasoning and automated verification, and practical guidance for 3D coding. First, we construct 3DCodeVerse-2M, a large-scale curated dataset of standalone 3D executable code. We…

## 18. KV4-RL: Unlocking Faster Asynchronous Rollouts for RLVR with INT4 KV Cache Quantization

- 分数：28.0  ·  HF 赞：32  ·  来源：huggingface
- 兴趣命中：reinforcement learning, benchmark
- 作者：Sihwan Park, Sung-Yub Kim, Doohyuk Jang, Eunho Yang
- 链接：[arXiv](https://arxiv.org/abs/2610.14448) · [PDF](https://arxiv.org/pdf/2610.14448) · [HF](https://huggingface.co/papers/2610.14448)

Asynchronous rollout improves the efficiency of reinforcement learning with verifiable rewards (RLVR) by reducing under-utilization during long-tail generation. Sustained concurrency also concentrates context processing into fewer decode steps, increasing the KV workload per step. We characterize this KV concentration and find that KV cache quantization delivers substantially greater acceleration than weight-only…

## 19. Hybrid Reasoning Agents

- 分数：28.0  ·  HF 赞：24  ·  来源：huggingface
- 兴趣命中：agent, memory, reasoning, benchmark, spec
- 作者：Jiaru Zou, Yunzhe Qi, Sirui Chen, Federico Bianchi, Shang Zhu, Pan Lu, Jingrui He, James Zou
- 链接：[arXiv](https://arxiv.org/abs/2610.18861) · [PDF](https://arxiv.org/pdf/2610.18861) · [HF](https://huggingface.co/papers/2610.18861)

How can we build an agent that thinks beyond human language, yet still acts through it in the external environment? Modern LLM agents still reason and interact through text, while latent reasoning offers an efficient internal medium but lacks native tool access and reasoning transparency. We bridge these two directions with Hybrid Reasoning Agents (HybridAgents), which dynamically navigate between latent reasoning…

## 20. Orbia: Do Generated Videos Form a Consistent 3D World?

- 分数：27.0  ·  HF 赞：22  ·  来源：huggingface
- 兴趣命中：memory, evaluation, benchmark, language model
- 作者：Dongyue Lu, Guian Fang, Hur Lim, Yonggang Wu, Yanrong Wang, Hongshan Chen, Shengju Qian, Yue Liao, Wei Chow, Lingdong Kong, Tianxin Huang, Yu Yang, Hongji Yang, Junchao Huang, Ao Liang, Yihao Wang, Zihan Wang, Rong Li, Hanlin Chen, Xin Wang, Wei Tsang Ooi, Mike Zheng Shou, Shuicheng Yan
- 链接：[arXiv](https://arxiv.org/abs/2610.20693) · [PDF](https://arxiv.org/pdf/2610.20693) · [HF](https://huggingface.co/papers/2610.20693)

Video generators serve as interactive worlds for exploration and simulation, yet realistic and visually appealing frames do not necessarily depict a consistent 3D world. Existing benchmarks assess selected geometric properties or use vision-language models to judge memory and consistency, leaving systematic 3D evaluation underexplored. We introduce Orbia, the first benchmark dedicated to a systematic and…

## 21. RuleTrek: Benchmarking Agentic Rule Reasoning in Complex Scenarios

- 分数：26.5  ·  HF 赞：21  ·  来源：huggingface
- 兴趣命中：agent, reasoning, benchmark, language model, large language, spec
- 作者：Chenhao Yuan, Bohan Yu, Yinhao Xu, Chao Yin, Chenxi Zhou, Zhaoxuan Wang, Shuwen Xu, Shaoping Huang, Haolin Ren, Jiaxiang Liu, Yao Xu, Jun Zhao, Kang Liu
- 链接：[arXiv](https://arxiv.org/abs/2610.19698) · [PDF](https://arxiv.org/pdf/2610.19698) · [HF](https://huggingface.co/papers/2610.19698)

Large language models (LLMs) increasingly tackle complex real-world tasks in specialized domains. However, identifying and correctly applying domain-specific rules remains challenging when scenario information is distributed across multiple files. Existing rule-reasoning benchmarks typically represent scenarios using only a few factual statements, simplifying the identification and application of relevant rules. To…

## 22. APT: Feedback-Driven Agentic Post-Training for Text-to-Image Generation

- 分数：26.0  ·  HF 赞：20  ·  来源：huggingface
- 兴趣命中：agent, reinforcement learning, evaluation, benchmark, spec
- 作者：Sirui Zhang, Fangyun Wei, Dong Chen, Jinjing Zhao, Yitong Wang, Yunuo Chen, Baining Guo, Zheng-Jun Zha
- 链接：[arXiv](https://arxiv.org/abs/2610.18097) · [PDF](https://arxiv.org/pdf/2610.18097) · [HF](https://huggingface.co/papers/2610.18097)

Post-training is crucial for improving text-to-image models, yet existing pipelines typically rely on manually curated training data and fixed training distributions. We introduce APT (Agentic Post-Training), a fully automated framework that adaptively post-trains a base model according to its evolving capability profile. APT coordinates three agents to construct evaluation sets from user requirements, diagnose…

## 23. HumanoidToolBench: Benchmarking Humanoid Tool Use from Selection to Mobile Execution

- 分数：25.0  ·  HF 赞：22  ·  来源：huggingface
- 兴趣命中：tool use, evaluation, benchmark
- 作者：Kyochul Jang, Seohyeon Park, Ohchul Kwon, Sangjun Park, Junhyeok Choi, Seungyeop Yi, Chaeyun Kim, Sangkyu Lee, Idan Szpektor, Avi Caciularu, Jongmin Park, Youngjae Yu
- 链接：[arXiv](https://arxiv.org/abs/2610.02089) · [PDF](https://arxiv.org/pdf/2610.02089) · [HF](https://huggingface.co/papers/2610.02089)

As robotic hardware and learning methods advance, humanoids need tools to perform tasks beyond their inherent physical limits. Successful tool use requires selecting a suitable tool and coordinating manipulation and, when needed, locomotion to complete the task. Existing benchmarks do not jointly evaluate these capabilities on a humanoid. We introduce HumanoidToolBench, an 18-task benchmark spanning three scenarios,…

## 24. τ-Emotion-Bench: Exposing the Interaction Fragility of LLM Agents through Real-World User Emotions

- 分数：24.0  ·  HF 赞：16  ·  来源：huggingface
- 兴趣命中：agent, tool use, tool-use, benchmark
- 作者：Rishitosh Kumar Singh, Amir Saeidi, Shamanthak Hegde, Shrinidhi Kumbhar, Chitta Baral
- 链接：[arXiv](https://arxiv.org/abs/2610.19560) · [PDF](https://arxiv.org/pdf/2610.19560) · [HF](https://huggingface.co/papers/2610.19560)

In long-horizon tool-calling tasks, LLM agents can fail not only because of tool-use errors, but also because of ineffective interaction with users. Yet existing benchmarks largely assume cooperative and behaviorally stable users, leaving the effect of emotional variation on agent reliability underexplored. We introduce τ-Emotion-Bench, a ten-domain benchmark for evaluating tool-calling agents under controlled…

## 25. Intern Lumina U2: A Multi-Codebook Diffusion Large Language Model for Omni-Visual Understanding and Image Generation

- 分数：23.0  ·  HF 赞：18  ·  来源：huggingface
- 兴趣命中：evaluation, language model, large language
- 作者：Qian Yu, Zongyang Qiu, Juncheng Yan, Hongliang Li, Qi Qin, Keqi Wang, Siqi Luo, Junkui Ju, Yapeng Mi, Tiantian Lu, Tian Liu, Pengyu Xie, Chenhao Ji, Minghui Zhang, Yiang Zhao, Siyu Yan, Haiying Xu, Yanbo Wang, Jianghan Shen, Yuandong Pu, Jiayi Lei, Borui Zhang, Jinxin Shi, Bo Zhang, Yuhang Zang, Shenglong Ye, Lixin Gu, Hongjie Zhang, Linghan Liu, Xinyuan Chen, Yuewen Cao, Lihe Zhang, Xiaohong Liu, Junjun He, Qiangwei Liu, Qi Zhang, Yu Cheng, Tianfan Xue, Hui Xiong, Chang Xu, Yu Qiao, Yihao Liu, Bin Fu
- 链接：[arXiv](https://arxiv.org/abs/2610.20818) · [PDF](https://arxiv.org/pdf/2610.20818) · [HF](https://huggingface.co/papers/2610.20818)

Unified multimodal generation covers discrete, continuous, and hybrid paradigms. Discrete approaches with single-codebook visual tokenizers align naturally with text modeling but have limited representational capacity. Continuous and hybrid approaches retain richer visual representations, but they model text and images in heterogeneous spaces with different training objectives, potentially introducing optimization…

## 26. The Thinking Leakage in Reinforcement Learning for LLMs

- 分数：22.5  ·  HF 赞：21  ·  来源：huggingface
- 兴趣命中：reasoning, reinforcement learning
- 作者：Wenxuan Zhu, Shuming Liu, Bang An, Aznaur Aliev, Bing Li, Yibo Yang, Bernard Ghanem
- 链接：[arXiv](https://arxiv.org/abs/2610.14270) · [PDF](https://arxiv.org/pdf/2610.14270) · [HF](https://huggingface.co/papers/2610.14270)

Hybrid reasoning models such as the Qwen3 series switch between a THINK mode and a NO-THINK mode through a few chat-template tokens. A popular recipe trains such models with reinforcement learning in NO-THINK mode and reports improved reasoning performance. We provide evidence that much of this gain can be explained by thinking leakage: the gain comes largely from partially reactivating the reasoning abilities of…

## 27. DecisionRobust: Benchmarking Robustness for JEV Style Decision Models Across Text and Vision

- 分数：22.5  ·  HF 赞：17  ·  来源：huggingface
- 兴趣命中：evaluation, benchmark, spec
- 作者：Yifan Lan, Zhongye Liu, Yurui Chang, Hanyu Wang, Yongkang Du, Lu Lin, Jinghui Chen
- 链接：[arXiv](https://arxiv.org/abs/2610.19118) · [PDF](https://arxiv.org/pdf/2610.19118) · [HF](https://huggingface.co/papers/2610.19118)

Emerging decision models such as JEV provide typed interfaces that map task instructions and observations directly to choices, judgments, and scores. As these models are increasingly used for automated decision-making, understanding their reliability under adversarial manipulation becomes critical. We introduce DecisionRobust, a benchmark for systematically evaluating the robustness of decision models across textual…

## 28. Routing Policy Optimization for Online Diffusion Reinforcement Learning

- 分数：22.5  ·  HF 赞：17  ·  来源：huggingface + arxiv
- 兴趣命中：reinforcement learning
- 作者：Qiuhong Shen, Yiding Yang, Yuxin Zhang, Xinwei Huang, Minxuan Lin, Bo Liu, Hao Kang, Haotian Yang, Yizhi Wang, Chongyang Ma, Xinchao Wang
- 链接：[arXiv](https://arxiv.org/abs/2610.22282) · [PDF](https://arxiv.org/pdf/2610.22282) · [HF](https://huggingface.co/papers/2610.22282)

Reinforcement learning can align visual generators with reward signals beyond their pretraining objectives, but existing score-function methods typically introduce stochasticity by perturbing the reverse denoising trajectory, leading to costly rollout-based optimization. We instead ask whether stochastic exploration can be introduced inside the generator while preserving its original sampler. Routing Policy…

## 29. ProgAgent: Learning Tool Orchestration through Programmatic Training

- 分数：22.5  ·  HF 赞：13  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark, language model, large language
- 作者：Hao Li, Keqing He, Longtao Zheng, Junlong Li, Weihao Zeng, Qian Liu, Yuzhen Huang
- 链接：[arXiv](https://arxiv.org/abs/2610.14774) · [PDF](https://arxiv.org/pdf/2610.14774) · [HF](https://huggingface.co/papers/2610.14774)

Large language models (LLMs) are increasingly expected to orchestrate diverse tools over long-horizon tasks. Existing agents typically use Direct Tool Calling (DTC), where the model invokes tools sequentially, and tool responses accumulate in the model context, which can lead to context rot and orchestration breakdown. In contrast, Programmatic Tool Calling (PTC) invokes tools through executable code and stores…

## 30. Terminal-RSI: Recursive Self-Improving Terminal Agents via Recursive Self-Rewrite and Policy-Refine

- 分数：22.5  ·  HF 赞：13  ·  来源：huggingface + arxiv
- 兴趣命中：agent, spec
- 作者：Junyao Yang, Zongxia Li, Yucheng Shi, Zhongzhi Li, Ruhan Wang, Ruiwen Zhou, Haitao Mi, Shuicheng Yan, Leowei Liang
- 链接：[arXiv](https://arxiv.org/abs/2610.22192) · [PDF](https://arxiv.org/pdf/2610.22192) · [HF](https://huggingface.co/papers/2610.22192)

Converting verifier outcomes into useful policy updates and partial progress into complete task resolution is crucial for terminal agents. We present Terminal-RSI, which alternates Recursive Self-Rewrite (RSR) of verified trajectories with critic-inheriting Recursive Policy-Refine (RPR). We formulate Turn-Boundary Skip-Observation GAE (TB-GAE) to retain token-specific baselines while applying decay across…

## 31. SCOPE: Semantic Bounded Credit Optimization for Prompt Engineering in Text-to-image Generation

- 分数：22.5  ·  HF 赞：13  ·  来源：huggingface + arxiv
- 兴趣命中：reinforcement learning, language model
- 作者：Yufei Jiao, Jinfa Huang, Zeyue Xue, Tianyu Xie, Yuexiao Ma, Rongrong Ji, Xiawu Zheng, Jiebo Luo
- 链接：[arXiv](https://arxiv.org/abs/2610.22264) · [PDF](https://arxiv.org/pdf/2610.22264) · [HF](https://huggingface.co/papers/2610.22264)

Reinforcement learning (RL) enables language models to improve text-to-image (T2I) generation by rewriting prompts for a frozen image generator. Existing methods typically apply a single signal derived from the image to individual subword tokens, although objects, counts, attributes, and relations form coherent semantic spans. We propose SCOPE, an objective based on Group Relative Policy Optimization (GRPO) that…

## 32. Apertus 1.5: From Open Text Models to Open Multimodal Reasoners

- 分数：22.0  ·  HF 赞：12  ·  来源：huggingface
- 兴趣命中：context window, reasoning, reinforcement learning, evaluation, benchmark, language model, spec
- 作者：Project Apertus, Yixuan Xu, Yassine Turki, Vinko Sabolčec, Valentina Pyatkin, Tommy Chu, Sven Najem-Meyer, Sean F. Carroll, Robert Smith, Raphael Kreft, Oscar Alessandro Tazza, Oleg Lavrovsky, Nicola Irmiger, Matteo Santelmo, Marian Schneider, Juan García Giraldo, Hanna Yukhymenko, Eduard Ďurech, Davit Melikidze, Dani Tamayo, Bettina Messmer, Aryan Ahadinia, Anunay Yadav, Allen Huang, Ahmad Fraij, Alessandro Bombarda, Alex Padula, Alexander Hägele, Alexander Sternfeld, Anna Hedström, Anna Kosovskaia, Arthur Wuhrmann, Arundhati Balasubramaniam, Badr Al Mahouri, Barna Pasztor, Bartosz Szostakiewicz, Bich Ngoc Doan, Bryan Schmid, Burak Sezen, Camille Challier, Clément Charmillot, Dana Shayakhmetova, Daniel Perruchoud, David Brüggemann, David Isztl, Elia Palme, Emma Anastassova, Fabian Bösch, Faruk Zahiragić, Fawzi Roberto Mohamed, Fiona Panicali, Florian Kolly, Flynn Guerra, Francesco Monti, Frederike Lübeck, Gennaro Oliva, Haofeng Yang, Haoliang Shang, Helen El Khoury, Henrique Mendonça, Jannis Vamvas, Jérome Landolt, Jessica Lam, Jingchun Xiao, Jonathan Coles, Joshua Oyebanji, Khanh Nguyen, Konstantinos Pitas, Lasse B. Strand, Li Mi, Loïc Deslarzes, Lorenzo Baggi, Lorenzo Noci, Luca Baumann, Luca Sartori, Lukas Drescher, Marco De Negri, Marco Passerini, Mark Klein, Marko Stojanovic, Martin Majsec, Matin Ansaripour, Mattea Busato, Mauro Pellonara, Max Neuwinger, Michael Graber, Michal Tešnar, Michelle Wastl, Miguel Gila, Mikolaj Boronski, Morgane Magnin, Moritz Reihs, Mukhammadali Sayfiddinov, Nathan Ranchin, Nicolas Cuveillier, Oscar Wohlfahrt, Qianqian Zou, Rada Kamysheva, Rita Sevastjanova, Roman Machacek, Sebastian Keller, Simon Matrenok, Simon Pierre, Stefano Schuppli, Suei-Wen Chen, Szabina Horváth-Mikulas, Taliesin Perez, Thilo Spinner, Thomas Kleine Buening, Tim Robinson, Tymoteusz Kwiecinski, Vilém Zouhar, Vinzenz Thoma, Xiaozhe Yao, Yannick Metz, Yuhei Fukuhara, Yusif Askari, Zixuan Chen, Alexander Ilic, Ana Klimovic, Andreas Krause, Andrei Kucharavy, Elliott Ash, Joost VandeVondele, Martin Rajman, Mennatallah El-Assady, Thomas Schulthess, Timo Kehrer, Torsten Hoefler, Antoine Bosselut, Martin Jaggi, Imanol Schlag
- 链接：[arXiv](https://arxiv.org/abs/2610.15542) · [PDF](https://arxiv.org/pdf/2610.15542) · [HF](https://huggingface.co/papers/2610.15542)

Language models are becoming infrastructure, and infrastructure built in the open, by public institutions, on documented data, is the alternative to dependence on a few providers; Apertus shows this is viable at scale. Apertus 1.5 extends the fully open Apertus family from text to multimodal reasoning. Continued pretraining of the Apertus 1.0 models, on 4T additional tokens for the 8B and 2T for the 70B, adds image…

## 33. Are We Testing Too Much? A Survey of Benchmark Compression for Efficient Evaluation of Large Language Models

- 分数：22.0  ·  HF 赞：12  ·  来源：huggingface
- 兴趣命中：evaluation, benchmark, language model, large language
- 作者：Guoming Ling, Yupei Lin, Zhongzhan Huang, Junxin Li, Junjie Liu, Shanshan Zhong, Hefeng Wu, Liang Lin
- 链接：[arXiv](https://arxiv.org/abs/2610.18248) · [PDF](https://arxiv.org/pdf/2610.18248) · [HF](https://huggingface.co/papers/2610.18248)

Benchmarks are essential for evaluating and improving large language models (LLMs). Yet many widely used benchmarks are redundant, making evaluation unnecessarily expensive. Benchmark compression lowers this cost by estimating full-benchmark scores and rankings from a partial evaluation. Research in this area has grown rapidly since 2024, but to our knowledge no survey has systematically organized its methods and…

## 34. SafeDriveVLA: Navigation-Conditioned World Model Dreaming for Conflict-Aware End-to-End Autonomous Driving

- 分数：22.0  ·  HF 赞：12  ·  来源：huggingface
- 兴趣命中：reasoning, benchmark, language model, large language
- 作者：Shaoyuan Xie, Zihan Zhang, Jingxuan Wang, Jiashu Qu, Xiaoqing Liang, Lingdong Kong, Junchi Lu, Henrik I. Christensen, Qi Alfred Chen
- 链接：[arXiv](https://arxiv.org/abs/2610.20609) · [PDF](https://arxiv.org/pdf/2610.20609) · [HF](https://huggingface.co/papers/2610.20609)

Vision-Language-Action (VLA) models are gaining attention in autonomous driving, inheriting commonsense priors from large language models (LLMs) and widening the navigation interface from a fixed command set to free-form natural-language instructions. However, this open-ended interface exposes a new vulnerability surface: an inattentive driver may issue instructions that are unsafe given the current scene, and a…

## 35. Diagnosing and Correcting Reward Hacking in Verifiable Instruction Following

- 分数：22.0  ·  HF 赞：12  ·  来源：huggingface
- 兴趣命中：reasoning, reinforcement learning, evaluation, benchmark
- 作者：Sangyeon Yoon, Wooseok Seo, Hamish Ivison, Hyesoo Hong, Donghoon Kim, Wonjun Kang, Albert No, Jaehyung Kim
- 链接：[arXiv](https://arxiv.org/abs/2610.19525) · [PDF](https://arxiv.org/pdf/2610.19525) · [HF](https://huggingface.co/papers/2610.19525)

Verifiable instruction-following benchmarks emphasize output-constraint satisfaction but can overlook whether responses meaningfully answer the underlying request, creating an evaluation blind spot. We show that frontier models can receive full credit for responses with little substantive answer content. Using the same verifier-based criterion as a training reward can induce reward hacking, as publicly released…

## 36. JevAgentHarness: Benchmarking, Deploying and Training Decision Models That Share Control with LLMs

- 分数：22.0  ·  HF 赞：12  ·  来源：huggingface
- 兴趣命中：agent, benchmark, language model, large language
- 作者：Kunlun Zhu, Tao Feng, Xu Han, Heng Wang, Ling Yang, Xiangru Tang, Jiaxuan You, Heng Ji
- 链接：[arXiv](https://arxiv.org/abs/2610.21412) · [PDF](https://arxiv.org/pdf/2610.21412) · [HF](https://huggingface.co/papers/2610.21412)

Large language model (LLM) agents now fix software, operate computers and serve customers, but their harnesses, the programs that run them, call a large LLM at every step, which makes long tasks slow and costly. Most of these calls end in a multiple-choice decision, such as which tool to call next. Decision models such as Jev answer these questions directly, at a fraction of an LLM call's time and price. We ask how…

## 37. APEX-Harm: Evaluating Agent Safety in Shared Professional Workspaces

- 分数：21.5  ·  HF 赞：15  ·  来源：huggingface
- 兴趣命中：agent, benchmark, spec
- 作者：Ziyi Yang, Adel Bibi, Guohao Li, Bernard Ghanem, Carlos Hinojosa
- 链接：[arXiv](https://arxiv.org/abs/2610.13623) · [PDF](https://arxiv.org/pdf/2610.13623) · [HF](https://huggingface.co/papers/2610.13623)

Professional agents increasingly work through command-line interfaces and multiple tools over shared workspaces containing files, messages, and business applications. These environments create safety risks that are difficult to capture with attacks placed at a single, known read location. We introduce APEX-Harm, a benchmark for evaluating prompt and script injection against long-horizon agents performing finance,…

## 38. CommerceGen-Studio: An End-to-End Framework for Commercial-Grade Main-Image Generation

- 分数：21.5  ·  HF 赞：15  ·  来源：huggingface
- 兴趣命中：agent, benchmark, spec
- 作者：Xiaoli Xu, Zhengtao Wu, Zhengze Xu, Tao Liu, Yongchao Du, Zuan Gao, Xingjian Wang, Hao Yan, Mengting Chen, Wei Li, Bo Zheng
- 链接：[arXiv](https://arxiv.org/abs/2610.20603) · [PDF](https://arxiv.org/pdf/2610.20603) · [HF](https://huggingface.co/papers/2610.20603)

We present CommerceGen-Studio, an end-to-end framework for generating commercial-grade main images for e-commerce Stock Keeping Units (SKUs). Our framework is organized along a three-stage pipeline of information extraction, semantic rewriting, and multi-condition generation: Prompt-Eval-Refine-Loop Agent (PERL-Agent) distills heterogeneous SKU metadata into concise selling-point text lists through an iterative…

## 39. StartLux-Decision: AutoThink Decision Models with Reinforcement Learning for Calibrated Deliberative Decisions

- 分数：21.0  ·  HF 赞：10  ·  来源：huggingface
- 兴趣命中：memory, reasoning, reinforcement learning, benchmark, spec
- 作者：Xialie Zhuang, Zunhai Su, Jia Pan, Ngai Wong, Guanhua Chen, Chuan-Wei Kuo
- 链接：[arXiv](https://arxiv.org/abs/2610.17309) · [PDF](https://arxiv.org/pdf/2610.17309) · [HF](https://huggingface.co/papers/2610.17309)

We introduce StartLux-Decision, decision models from 0.8B to 27B parameters that combine efficient single-pass prediction with adaptive, confidence-guided reasoning. The Instant models use bidirectional attention in full-attention layers to improve decision accuracy while keeping single-pass inference. The AutoThink models invoke explicit reasoning for uncertain decisions and answer confident cases directly. A…

## 40. Intern-Decision: Efficient Multimodal Decision Making with Autoregressive Masked Language Modeling

- 分数：21.0  ·  HF 赞：6  ·  来源：huggingface + arxiv
- 兴趣命中：agent, evaluation, language model
- 作者：Tong Zhu, Zhe Xu, Zefeng He, Yunkai Chai, Xuyang Hu, Dehong Zheng, Yun Luo, Yafu Li, Qi Zhang, Yu Cheng
- 链接：[arXiv](https://arxiv.org/abs/2610.22131) · [PDF](https://arxiv.org/pdf/2610.22131) · [HF](https://huggingface.co/papers/2610.22131)

Interactive agents repeatedly choose among a finite set of actions, labels, or ordinal outcomes. Generating a free-form response for each choice adds latency and complicates the interface between a model and its environment. We present Intern-Decision, a family of 0.8B, 2B, and 4B multimodal decision models that return structured choices and candidate probabilities from text and optional images. Our autoregressive…

## 41. GroundGUI: GUI Grounding by High-Quality Data and Distillation-to-Reinforcement Learning

- 分数：20.5  ·  HF 赞：13  ·  来源：huggingface
- 兴趣命中：agent, reinforcement learning, benchmark
- 作者：Qingsong Xie, Jiahao Tian, Jiacheng Tang, Zhifeng Li, Madalina Ciobanu, Navan Preet Singh, Qingqing Mao, Ritankar Das
- 链接：[arXiv](https://arxiv.org/abs/2610.19100) · [PDF](https://arxiv.org/pdf/2610.19100) · [HF](https://huggingface.co/papers/2610.19100)

Constructing robust GUI agents relies on multimodal visual grounding: the ability to precisely map natural language intents to actionable on-screen components. Despite abundant desktop, web, and mobile benchmarks, high-fidelity resources tailored for diverse environments are surprisingly scarce. To bridge this gap, we introduce the Screen Referring Grounding Dataset (ScreenRef), a comprehensive GUI grounding dataset…

## 42. Long-Horizon RL Needs Muon

- 分数：20.5  ·  HF 赞：13  ·  来源：huggingface
- 兴趣命中：agent, tool use, reasoning
- 作者：Kai Ruan, Jinghao Lin, Tao Chen, Ziqi Zhou, Qianshan Wei, Zihe Huang
- 链接：[arXiv](https://arxiv.org/abs/2610.20256) · [PDF](https://arxiv.org/pdf/2610.20256) · [HF](https://huggingface.co/papers/2610.20256)

Long-horizon agents must coordinate reasoning, tool use, and environment feedback over extended interactions. Learning from sparse outcome rewards requires weighting trajectories of different lengths and updating the policy while rollouts are still being collected. We examine a single-rollout asynchronous recipe combining Muon, token-averaged loss, truncated importance sampling, and auxiliary length and tool-error…

## 43. DeltaStreamer: Towards Human-Like Agentic Streaming Video Understanding

- 分数：20.5  ·  HF 赞：9  ·  来源：huggingface
- 兴趣命中：agent, memory, spec, planning, retrieval
- 作者：Boyuan Sun, Deshui Miao, Wenzhao Gao, Shaoyong Jia, Shaohui Jiao, Chi Liu, Yan Shu, Derek Li, Bryan Dai, Shengsheng Qian, Qibin Hou
- 链接：[arXiv](https://arxiv.org/abs/2610.19849) · [PDF](https://arxiv.org/pdf/2610.19849) · [HF](https://huggingface.co/papers/2610.19849)

We propose DeltaStreamer, a novel agentic framework for streaming video understanding inspired by how humans observe, remember, and investigate. Streaming video understanding requires a system to retain evidence before knowing which details future queries will need. Existing approaches often obscure event transitions and omit relevant details when compressing video history, and cannot recover missing visual…

## 44. What Makes a Social Agent's Interactions Effective? Learning from Verifiable Outcomes in Paired Worlds

- 分数：20.5  ·  HF 赞：9  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark, spec
- 作者：Caixin Kang, Ke Wang, Yuchuan Wu, Xiaoqiang Wang, Ling Li, Bingxue Qiu, Yongbin Li, Yoichi Sato
- 链接：[arXiv](https://arxiv.org/abs/2610.20195) · [PDF](https://arxiv.org/pdf/2610.20195) · [HF](https://huggingface.co/papers/2610.20195)

Effective social interaction requires more than fluent responses: agents must reach plans that fit the participants' needs and circumstances. Existing evaluations of social agents mainly rely on LLM judges that rate the conversation, without checking the resulting plan. We introduce HICO-Bench, a benchmark of 180 everyday coordination scenarios, such as resource allocation, scheduling, and authorization, in which…

## 45. Skill-Decoupled On-Policy Expert Distillation for Unified Vision-Language Models

- 分数：20.5  ·  HF 赞：1  ·  来源：huggingface + arxiv
- 兴趣命中：reinforcement learning, benchmark, language model, spec
- 作者：Yuqi Xiong, Chunyi Peng, Zhipeng Xu, Qing Yang, Zhenghao Liu, Zulong Chen, Yu Gu, Ge Yu
- 链接：[arXiv](https://arxiv.org/abs/2610.22217) · [PDF](https://arxiv.org/pdf/2610.22217) · [HF](https://huggingface.co/papers/2610.22217)

Reinforcement learning (RL) can elicit specialized visual capabilities in vision-language models (VLMs), yet jointly optimizing heterogeneous objectives often introduces cross-capability gradient conflicts. Training experts independently mitigates this interference, but direct reward optimization may entangle specialized knowledge with reward-hacking biases. This paper proposes Skill-Decoupled On-Policy Expert…

## 46. A team of Gemini 4 Argon agents beats Minecraft

- 分数：20.5  ·  HF 赞：1  ·  来源：huggingface + arxiv
- 兴趣命中：agent, memory, coding, spec
- 作者：Maxence Faldor, Satinder Singh, Roberta Raileanu
- 链接：[arXiv](https://arxiv.org/abs/2610.22319) · [PDF](https://arxiv.org/pdf/2610.22319) · [HF](https://huggingface.co/papers/2610.22319)

We placed four Gemini 4 Argon agents in a sandboxed Minecraft survival world and gave them one goal: defeat the Ender Dragon. Each agent controlled a player via an open-source library called Mineflayer and coordinated with its teammates through in-game chat and shared memory. No one assigned roles or wrote game logic. The agents planned, wrote, and debugged every program themselves. Researchers could watch the run…

## 47. InfoVis: Unified Slide Image Generation and Editing

- 分数：20.0  ·  HF 赞：12  ·  来源：huggingface
- 兴趣命中：evaluation, benchmark, spec
- 作者：Jiahao Wang, Xiyan Jiang, Chenyuan Wu, Haoqiang Zhang, Xin Luo, Yueze Wang, Defu Lian, Bo Zhang, Jiajun Zhang, Zheng Liu
- 链接：[arXiv](https://arxiv.org/abs/2610.16784) · [PDF](https://arxiv.org/pdf/2610.16784) · [HF](https://huggingface.co/papers/2610.16784)

Generating and editing presentation slides requires models to combine accurate text rendering, instruction following, visual grounding, aesthetic design, and precise editing within one canvas. Existing work covers only subsets of these capabilities and lacks large-scale slide-native supervision and diagnostic evaluation. We formulate four slide-centric tasks and build a scalable data engine with over 13M…

## 48. Velox: Spatial Memory Makes World Models Efficient

- 分数：20.0  ·  HF 赞：12  ·  来源：huggingface + arxiv
- 兴趣命中：memory
- 作者：Qiuhong Shen, Shizun Wang, Xinchao Wang
- 链接：[arXiv](https://arxiv.org/abs/2610.22311) · [PDF](https://arxiv.org/pdf/2610.22311) · [HF](https://huggingface.co/papers/2610.22311)

Video world models turn actions and camera motion into long visual rollouts, making video a natural interface for interactive simulation. Such interaction requires responsive generation, yet coherent rollouts must retain visual memory of what has already been generated. Chunked video diffusion models usually keep this context in growing KV caches, so later chunks become progressively slower. To address this…

## 49. SWE-at-Scale: Scalable Issue Synthesis from Historical Bug Fixes

- 分数：20.0  ·  HF 赞：12  ·  来源：huggingface
- 兴趣命中：agent, evaluation, coding
- 作者：Silin Chen, Zihan Zhang, Xiaodong Gu, Jiale Huang, Yuling Shi, Han Li, Zhao Shan, Chengcheng Wan, Zhensu Sun, Haibing Guan
- 链接：[arXiv](https://arxiv.org/abs/2610.21359) · [PDF](https://arxiv.org/pdf/2610.21359) · [HF](https://huggingface.co/papers/2610.21359)

As coding agents become increasingly capable, robust evaluation requires a broader and more diverse supply of verifiable software engineering (SWE) tasks. However, real-world tasks are constrained by the natural frequency of issue reporting and the substantial cost of manual curation. Furthermore, existing synthetic approaches rely primarily on the pretrained knowledge of large models coupled with heuristic…

## 50. Diff Diffusion: Predicting Edit Paths with Diffusion Models for Efficient Code Editing

- 分数：19.5  ·  HF 赞：7  ·  来源：huggingface
- 兴趣命中：evaluation, benchmark, language model, large language, coding, spec
- 作者：Xiaolong Xu, Hao Jiang, Bo Jiang, Zhiwen Deng, Ningyuan Sun, Bingzhou Chen, Jin Chen, Chenxing Wei
- 链接：[arXiv](https://arxiv.org/abs/2610.17831) · [PDF](https://arxiv.org/pdf/2610.17831) · [HF](https://huggingface.co/papers/2610.17831)

Diffusion large language models (dLLMs) are appealing for code generation because they can update many tokens in parallel, yet many are optimized for sequence synthesis rather than edit prediction. This setting is poorly matched to modern AI-assisted IDEs, where edit prediction must infer the next code change from recent edits, the current file, and cursor-local context. Such changes are usually sparse and preserve…

## 51. Latent Compaction with Test-Time Training

- 分数：19.5  ·  HF 赞：7  ·  来源：huggingface
- 兴趣命中：memory, long context, spec, retrieval
- 作者：Yingfa Chen, Xingyu Shen, Chaojun Xiao, Xu Han
- 链接：[arXiv](https://arxiv.org/abs/2610.20582) · [PDF](https://arxiv.org/pdf/2610.20582) · [HF](https://huggingface.co/papers/2610.20582)

Long contexts enlarge key--value (KV) caches, increasing memory use and attention costs during generation. Compressing these caches must preserve information for unseen questions. We introduce **Latent Compaction**, which learns a compact document-specific cache through test-time training. We initialize cache entries using reconstruction importance, teacher attention, and key-space diversity. Training first fits…

## 52. RAR: Rate-Adaptive Rollout for Time-Consistent Interactive World Models

- 分数：19.0  ·  HF 赞：14  ·  来源：huggingface
- 兴趣命中：context window, spec
- 作者：Yaoyang Liu, Dongyu Yan, Yihua Du, Shengju Qian, Zeke Xie, Xin Wang, Ying-Cong Chen, Long Chen
- 链接：[arXiv](https://arxiv.org/abs/2610.16302) · [PDF](https://arxiv.org/pdf/2610.16302) · [HF](https://huggingface.co/papers/2610.16302)

Video-based interactive world models aim to enable real-time, user-controllable environments. Yet most existing systems are trained and rolled out at a fixed temporal rate, limiting both runtime-rate adaptation and physical-horizon coverage -- a limitation we term temporal-rate coupling. Specifically, when runtime generation throughput differs from the learned temporal rate, the generated world evolves…

## 53. SwarmRSI: Recursive Self-Improvement through Evolving Scientific Agent Swarm

- 分数：19.0  ·  HF 赞：14  ·  来源：huggingface
- 兴趣命中：agent, evaluation
- 作者：Qianru Meng, Xi Zhang, Konstantinos Papakostas, Congfeng Cao, Wenxiang Hu, Tianyi Lu, Xiao Zhang, Lun Zhou, Zaiqiao Meng, Zhaochun Ren, Xiaohui Yan, Yougang Lyu
- 链接：[arXiv](https://arxiv.org/abs/2610.20431) · [PDF](https://arxiv.org/pdf/2610.20431) · [HF](https://huggingface.co/papers/2610.20431)

Recursive self-improvement (RSI) in scientific research aims to improve agents' research capabilities through their own experimental experience. Scientific agent swarms can combine evidence and implementations from different research directions to guide their agents' subsequent experiments. However, poor experimental results can leave unclear whether to revise a hypothesis or its implementation, while overall…

## 54. SimVTA: Simulation-Grounded Video-Trajectory Alignment for Driving World Action Models

- 分数：19.0  ·  HF 赞：10  ·  来源：huggingface
- 兴趣命中：reinforcement learning, evaluation, planning
- 作者：Changhui Jing, Haochen Tian, Hongchen Li, Tianyu Li, Caojun Wang, Zihao Zhang, Yanhao Liu, Chengen Xie, Bailin Li, Hao Zhao, Zhenjie Yang
- 链接：[arXiv](https://arxiv.org/abs/2610.13781) · [PDF](https://arxiv.org/pdf/2610.13781) · [HF](https://huggingface.co/papers/2610.13781)

Driving world action models (WAMs) learn from paired trajectories and future observations. Post-training with reinforcement learning allows the policy to explore alternative trajectories and improve planning using driving rewards. However, driving logs contain future videos only for the recorded trajectories, leaving these alternatives without corresponding visual supervision. Thus, we introduce SimVTA, a…

## 55. Joint Subspace Sparse Attention for Efficient Long-Context Decoding

- 分数：19.0  ·  HF 赞：10  ·  来源：huggingface
- 兴趣命中：reasoning, coding, spec
- 作者：Jiwon Song, Yoongon Kim, Jae-Joon Kim
- 链接：[arXiv](https://arxiv.org/abs/2610.19026) · [PDF](https://arxiv.org/pdf/2610.19026) · [HF](https://huggingface.co/papers/2610.19026)

Sparse attention reduces the KV-cache traffic that dominates long-context LLM decoding, but practical methods largely operate at coarse granularity. Token-level selection offers finer control, yet presents two challenges: low-dimensional scoring may lose query--key structure needed for accurate ranking, while gathering scattered selected tokens can offset the resulting latency benefit. We introduce Joint Subspace…

## 56. Rethinking LLM-Guided Visual Question Answering: Does Deeper Knowledge Integration Really Help?

- 分数：19.0  ·  HF 赞：6  ·  来源：huggingface
- 兴趣命中：reasoning, benchmark, language model, large language
- 作者：Aneerban Saha, Vijay Kumar, Sameer Madhav D., Priyam Srivastava, Dhruv Bansal
- 链接：[arXiv](https://arxiv.org/abs/2610.17079) · [PDF](https://arxiv.org/pdf/2610.17079) · [HF](https://huggingface.co/papers/2610.17079)

Knowledge-based Visual Question Answering (VQA) requires reasoning that extends beyond visible image content, demanding external commonsense and factual knowledge. While recent work leverages Large Language Models (LLMs) as knowledge sources, the question of how deeply such guidance should be integrated into a vision language architecture remains underexplored. In this work, we generate structured reasoning…

## 57. SyncReward: Human-Aligned Synchronization Reward for Audio-Visual Generation

- 分数：19.0  ·  HF 赞：6  ·  来源：huggingface
- 兴趣命中：reinforcement learning, evaluation, benchmark, spec
- 作者：Kaisi Guan, Ying Ba, Wenjing Wang, Xihua Wang, Chen Li, Jing Lyu, Ruihau Song
- 链接：[arXiv](https://arxiv.org/abs/2610.16338) · [PDF](https://arxiv.org/pdf/2610.16338) · [HF](https://huggingface.co/papers/2610.16338)

Recent years have witnessed rapid progress in joint audio--visual generation. However, audio--visual synchronization remains a challenge, as generated speech and sound often temporally misalign with visual events. A key bottleneck is the lack of human-annotated data, reliable evaluation benchmarks, and synchronization-aware evaluation models for generated audio--visual outputs. To address these limitations, we…

## 58. EdgeWise: Bringing Long-Horizon Agents to the Edge via Selective Cloud Delegation

- 分数：18.5  ·  HF 赞：17  ·  来源：huggingface
- 兴趣命中：agent
- 作者：Zeru Shi, Jindong Jiang, Ryo Hachiuma, Yonggan Fu, Byung-Kwan Lee, Peter Belcak, Saurav Muralidharan, Ayush Agarwal, Ruixiang Tang, Ambrish Dantrey, Pavlo Molchanov, Anjul Patney, Subhashree Radhakrishnan
- 链接：[arXiv](https://arxiv.org/abs/2610.17560) · [PDF](https://arxiv.org/pdf/2610.17560) · [HF](https://huggingface.co/papers/2610.17560)

Complex and long-horizon agent tasks often rely on frontier models deployed in the cloud to achieve strong performance. However, using these models for every step of a long-horizon trajectory incurs substantial inference cost, even though not all steps may require the same level of model capability. In this paper, we find that allocating the LLM to only a small subset of key steps can achieve performance comparable…

## 59. NavGPT-3: Harnessing Context in a Hierarchical Navigation Runtime

- 分数：18.5  ·  HF 赞：5  ·  来源：huggingface
- 兴趣命中：agent, reasoning, reinforcement learning, evaluation, language model
- 作者：Gengze Zhou, Yicong Hong, Jiazhao Zhang, Xunyi Zhao, Jian Zhou, Zixing Lei, Zun Wang, Chongyang Zhao, Xionghui Chen, Stephen Gould, Anton van den Hengel, Qi Wu
- 链接：[arXiv](https://arxiv.org/abs/2610.10787) · [PDF](https://arxiv.org/pdf/2610.10787) · [HF](https://huggingface.co/papers/2610.10787)

Language models trained with long-horizon agentic reinforcement learning can generalize knowledge through reasoning, express precise actions, and pursue goals over many steps, raising the ceiling on what an embodied agent can understand and decide. Physical interaction, however, remains the domain of action policies, which provide dense, low-latency control. We present NavGPT-3, a harness that connects the two…

## 60. Jag: Direct Box Prediction for Efficient Visual Grounding

- 分数：18.5  ·  HF 赞：5  ·  来源：huggingface
- 兴趣命中：memory, benchmark, coding, spec
- 作者：Xiuyuan Zhu, Ke Lu, Hao Wu, Zijin Du, Dongming Zhang, Jian Xue
- 链接：[arXiv](https://arxiv.org/abs/2610.13239) · [PDF](https://arxiv.org/pdf/2610.13239) · [HF](https://huggingface.co/papers/2610.13239)

Visual grounding combines image--language understanding with geometric prediction, yet autoregressive multimodal models often express a box as a coordinate sequence. Sequential decoding adds computation to the multimodal processing needed for localization. Adapting these representations to box geometry offers a route to direct prediction. We present Jag, which adapts a compact pretrained multimodal model for direct…

## 61. Choosing LLMs for Strategic Agent Interactions

- 分数：18.5  ·  HF 赞：5  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark, language model, large language, spec
- 作者：Arastun Mammadli, Herbert Woisetschläger, Jawad Fayaz, Shiqiang Wang
- 链接：[arXiv](https://arxiv.org/abs/2610.18354) · [PDF](https://arxiv.org/pdf/2610.18354) · [HF](https://huggingface.co/papers/2610.18354)

Game-theoretic benchmarks claim that large language model (LLM) strategic decision-making varies across game types, interaction structures, and capability dimensions. However, they only evaluate strategic performance across individual fixed models. In parallel, contemporary LLM routers pick models under quality-cost trade-offs, but with no notion of a strategic structure. They do not account for an opponent that…

## 62. Memory as Weights: Internalizing Long-Term History for Streaming Videos

- 分数：18.5  ·  HF 赞：5  ·  来源：huggingface + arxiv
- 兴趣命中：memory, language model
- 作者：Zhuoming Liu, Jinhong Lin, Lin Zhang, Yiwu Zhong, Yin Li
- 链接：[arXiv](https://arxiv.org/abs/2610.22070) · [PDF](https://arxiv.org/pdf/2610.22070) · [HF](https://huggingface.co/papers/2610.22070)

Streaming vision-language models (VLMs) must continuously integrate information from the past while remaining responsive to current observations and user queries. Existing memory mechanisms typically compress, retrieve, or cache historical observations and reintroduce them into the input context, forcing historical memory and current observations to compete for limited context. We propose MaLoW, a streaming memory…

## 63. EVA-Cap: Optimizing Audiovisual Video Captioning via Event-Centric Alignment

- 分数：18.5  ·  HF 赞：1  ·  来源：huggingface + arxiv
- 兴趣命中：evaluation, benchmark, language model
- 作者：Jiapeng Shi, Qiuxia Hou, Jiaqi Leng, Junke Wang, Yanhao Zhang, Haonan Lu, Ziyi Ye, Zuxuan Wu
- 链接：[arXiv](https://arxiv.org/abs/2610.22186) · [PDF](https://arxiv.org/pdf/2610.22186) · [HF](https://huggingface.co/papers/2610.22186)

Recent advances in Omni Language Models (OLMs) provide a unified solution for audiovisual video captioning. Nevertheless, existing approaches predominantly treat captioning as an unstructured text generation process, neglecting the inherent semantic structure of videos and leading to suboptimal fine-grained audiovisual alignment. To bridge this gap, we propose EVA-Cap, a novel framework that decomposes captions into…

## 64. Self-Conditioning Enables Deep Sequential Reasoning in Flow Matching

- 分数：18.0  ·  HF 赞：8  ·  来源：huggingface
- 兴趣命中：reasoning, evaluation, spec
- 作者：Zeyang Zhang, Linxiang Gao, Meiqi Gu, Xingyan Chen, Minrui Luo, Kaifeng Lyu, Tianxing He
- 链接：[arXiv](https://arxiv.org/abs/2610.19628) · [PDF](https://arxiv.org/pdf/2610.19628) · [HF](https://huggingface.co/papers/2610.19628)

Recent work has explored visual reasoning through image generation, where models solve visual-reasoning problems by directly generating solution images. Intuitively, iterative samplers such as flow matching are well suited to this task, since each sampling step may resemble one reasoning step. However, in this work, from a circuit complexity perspective, we show that this intuition is misleading. We prove that as…

## 65. The COUNT: Counting N-grams Unlocks Scaling on Host Memory and Training-Free Adaptation

- 分数：18.0  ·  HF 赞：8  ·  来源：huggingface
- 兴趣命中：memory, language model, spec
- 作者：Ian Magnusson, Noah A. Smith, Pang Wei Koh
- 链接：[arXiv](https://arxiv.org/abs/2610.20456) · [PDF](https://arxiv.org/pdf/2610.20456) · [HF](https://huggingface.co/papers/2610.20456)

The scaling relationship of compute and performance for language models (LMs) has been extensively studied; more recently, models are being designed to scale memory use, as well. In particular, adding embeddings for n-grams scales memory separately from compute use, because each pass only processes individual embedding rows, which are much smaller than the storage used for the whole embedding table. However,…

## 66. History Replays Itself: Unleashing Long-Context Capability in Linear Attention

- 分数：18.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：agent, memory, language model, retrieval
- 作者：Li Nanbo, Firas Laakom, Yilan Zhang, Piotr Piękos, Yimeng Chen, Liangyu Wang, Yifan Xu, Mateusz Ostaszewski, Dandan Guo, Wenyi Wang, Yanning Dai, Yuhui Wang, Jürgen Schmidhuber
- 链接：[arXiv](https://arxiv.org/abs/2610.15715) · [PDF](https://arxiv.org/pdf/2610.15715) · [HF](https://huggingface.co/papers/2610.15715)

Linear attention promises the efficiency needed for long-context language modelling, yet its fixed-size recurrent state must simultaneously support ongoing computation and preserve information from an ever-growing history. This coupling has reinforced a prevailing view that the state's memory capacity defines the model's long-context capability. We challenge this presumed ceiling: recurrent computation need not bear…

## 67. AgentSafeEvo: Adversarial Co-Evolution for LLM Agent Safety

- 分数：18.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：agent, tool use, reinforcement learning, benchmark, language model, large language
- 作者：Chenxu Wang, Xiaoyu Wen, Han Qi, Ziyuan Zhou, Cheng Jin, Chaochao Lu, Qiaosheng Zhang
- 链接：[arXiv](https://arxiv.org/abs/2610.19422) · [PDF](https://arxiv.org/pdf/2610.19422) · [HF](https://huggingface.co/papers/2610.19422)

Large language model (LLM) agents accomplish complex tasks through multi-turn interactions with external tools. However, malicious content embedded in user queries, tool descriptions, or environment observations can manipulate their decisions and induce unsafe actions. Adversarial co-evolution has emerged as an effective approach to strengthening LLM safety, but existing work primarily focuses on language-level…

## 68. Super-Resolution in The Right Latent Space: A Frozen Vision-Foundation Substrate

- 分数：17.5  ·  HF 赞：19  ·  来源：huggingface
- 兴趣命中：-
- 作者：Wanzhou Lei, Cuifeng Shen, Yanjin He, Maohua Li, Hua Yuan, Per-Olof Persson, Tao Lan, Kan Liu, Hanlin Tang
- 链接：[arXiv](https://arxiv.org/abs/2610.04781) · [PDF](https://arxiv.org/pdf/2610.04781) · [HF](https://huggingface.co/papers/2610.04781)

In an image latent space, the embeddings of high-resolution, natural, and sharp images form a manifold. Degradation of high-resolution images pushes their embeddings off this manifold. Real-world super-resolution (SR) then becomes the task of mapping the degraded embedding back onto this manifold --- not anywhere on the manifold, but to the point that preserves what the input still carries, both its semantics and…

## 69. LabInstruct: Benchmarking Situated Instructional Video Generation for Lab Procedures

- 分数：17.5  ·  HF 赞：15  ·  来源：huggingface
- 兴趣命中：benchmark
- 作者：Yuming Fu, Weijia Wu, Jing Chen, Jiahao Tang, Feifei Chen, Hongyu Zhu, Xin Jin, Alex Jinpeng Wang
- 链接：[arXiv](https://arxiv.org/abs/2610.14020) · [PDF](https://arxiv.org/pdf/2610.14020) · [HF](https://huggingface.co/papers/2610.14020)

Self-driving laboratories (SDLs) aim to automate the full experimental loop, from scientific decision-making to physical execution. Ideally, AI-generated plans could be carried out directly by robotic systems, but reliable automation remains difficult in complex, open-world laboratory environments, where experiments often involve fine-grained manipulation, long-horizon procedures, and substantial variation across…

## 70. SWEeper-Bench: Can Agents Discover Bugs in Interactive Software?

- 分数：17.5  ·  HF 赞：7  ·  来源：huggingface
- 兴趣命中：agent, benchmark, coding
- 作者：Yang Yao, Haozhe Chen, Bingyi Kang, Karthik R Narasimhan, Zhuang Liu
- 链接：[arXiv](https://arxiv.org/abs/2610.14096) · [PDF](https://arxiv.org/pdf/2610.14096) · [HF](https://huggingface.co/papers/2610.14096)

Coding agents increasingly interact with users by generating interactive software on the fly rather than replying in text, yet many bugs in such software reveal themselves only after multi-step interactions. Today, users must discover these bugs and wait for fixes, making the development loop slow and expensive. Existing benchmarks typically assume the bugs have already been identified, leaving agents' ability to…

## 71. Training LLMs for Multi-Agent Collaboration with Verifiable Information Rewards

- 分数：17.5  ·  HF 赞：7  ·  来源：huggingface
- 兴趣命中：agent, language model, large language
- 作者：Keru Chen, Sen Lin, Yingbin Liang, Nathaniel D. Bastian, Shaofeng Zou
- 链接：[arXiv](https://arxiv.org/abs/2610.17893) · [PDF](https://arxiv.org/pdf/2610.17893) · [HF](https://huggingface.co/papers/2610.17893)

Effective collaboration among large language model (LLM) agents in multi-agent systems requires sharing relevant evidence, requesting missing information, and incorporating teammates' contributions into decisions. Training these behaviors is challenging because final task outcomes provide limited feedback on the value of individual messages. We introduce CoSIR (Collaboration via Surprisal-based Information Rewards),…

## 72. Athanor: An Agent-Native System for Autonomous Post-Training Research

- 分数：17.5  ·  HF 赞：7  ·  来源：huggingface
- 兴趣命中：agent, reasoning, evaluation
- 作者：Yufa Zhou, Yichen Wang, Jiakun Fan, Ziqi Shu, Zhichao Liu, Anru R. Zhang, Neiwen Ling, Zijun Wei
- 链接：[arXiv](https://arxiv.org/abs/2610.21055) · [PDF](https://arxiv.org/pdf/2610.21055) · [HF](https://huggingface.co/papers/2610.21055)

Recursive self-improvement, in which AI systems build stronger AI systems, is one promising route to superintelligence. We study a weaker form that can be measured today: frontier agents post-training a small raw base model with public data, as a test of their research potential. We build Athanor, an open agent-native system for autonomous post-training research (AutoPostTrain) on real GPUs. We give the agents full…

## 73. When Left Is Right? Camera-Motion Understanding beyond Screen

- 分数：17.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：agent, benchmark, language model, spec
- 作者：Chong Cheng, Ran Zhang, Xinyuan Li, Alan Zhao, Hao Wang, Xi Wang
- 链接：[arXiv](https://arxiv.org/abs/2610.17242) · [PDF](https://arxiv.org/pdf/2610.17242) · [HF](https://huggingface.co/papers/2610.17242)

Can a vision-language model tell left from right? Modern VLMs solve visual puzzles and follow hour-long videos, yet when asked whether the camera moved left or right, most do no better than a coin flip. Adding camera-motion data or geometric representations has been tried, separately, and neither closes the gap. We argue that camera-motion understanding needs two conditions at once: the representation must couple…

## 74. WorldCast: Exploring Intelligent Visual Generation in World State Prediction

- 分数：17.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：reasoning, benchmark, language model, planning
- 作者：Wenhao Yan, Haodong Li, Xiaotong Li, Yaxin Luo, Zhengrong Yue, Jialv Zou, Xu Huang, Haojin Yang, Nan Jia, Yan Feng, Peng Pei, Xunliang Cai
- 链接：[arXiv](https://arxiv.org/abs/2610.20731) · [PDF](https://arxiv.org/pdf/2610.20731) · [HF](https://huggingface.co/papers/2610.20731)

Humans interpret multimodal observations of the world and forecast how it will evolve. Recent multimodal generative systems have demonstrated similar capabilities: they can integrate multimodal context and synthesize visual outputs that depict changes in the world. To characterize this emerging trajectory, we organize model capabilities into a four-level hierarchy and discover that higher-level tasks remain…

## 75. AutoSFT: An Agentic System for Automated Data Research in Supervised Fine-Tuning

- 分数：17.5  ·  HF 赞：3  ·  来源：huggingface + arxiv
- 兴趣命中：agent, language model
- 作者：Bingxiang He, Pengqi Sun, Shihao Peng, Shaoxuan Li, Huiyu Xiao, Hongjian Shi, Zixuan Fu, Ziqing Qiao, Yuxin Zuo, Cheng Qian, Xinqiang Yu, Jiayi Li, Xiusi Chen, Yizhen Song, Xiangyang Wang, Iofai Lei, Yudong Wang, Ning Ding, Zhiyuan Liu, Xiaozhi Wang, Chaojun Xiao
- 链接：[arXiv](https://arxiv.org/abs/2610.22194) · [PDF](https://arxiv.org/pdf/2610.22194) · [HF](https://huggingface.co/papers/2610.22194)

Language model agents increasingly automate post-training, but when given the full training stack they converge on supervised fine-tuning and spend most effort revising training data. Existing systems give the agent one kind of control, selecting rows from a fixed pool or calling a generator, whereas a human data engineer adjusts proportions, prunes, repairs, replaces and synthesizes the data. We design a data…

## 76. SkillMarker: A KGW-Based Watermarking Method for Agent Skill Ownership Verification

- 分数：17.0  ·  HF 赞：14  ·  来源：huggingface
- 兴趣命中：agent
- 作者：Alan Tang, Lifeng Wang, Gang Wu, Tao Zhang, Yantao Jia, Xiaofeng Zhu
- 链接：[arXiv](https://arxiv.org/abs/2610.15725) · [PDF](https://arxiv.org/pdf/2610.15725) · [HF](https://huggingface.co/papers/2610.15725)

Agent skills encode operational procedures and domain expertise as reusable knowledge assets, yet their distribution in plaintext exposes them to unauthorized copying and leakage. However, practical mechanisms for skill ownership verification and leakage tracing remain underdeveloped. Watermark embedding before distribution offers a potential solution, but structured, compact skill instructions impose stringent…

## 77. Do Better Visual Representations Always Lead to Better End-to-End Autonomous Driving?

- 分数：17.0  ·  HF 赞：10  ·  来源：huggingface
- 兴趣命中：evaluation, planning
- 作者：Zihao Zhang, Haochen Tian, Tianyu Li, Changhui Jing, Jingliang He, Naisheng Ye, Ziyuan Pu, Zhenjie Yang
- 链接：[arXiv](https://arxiv.org/abs/2610.09695) · [PDF](https://arxiv.org/pdf/2610.09695) · [HF](https://huggingface.co/papers/2610.09695)

Visual foundation models (VFMs) are increasingly integrated into end-to-end autonomous driving for their powerful representations, yet it remains unclear when these representations improve driving performance. To investigate this question, we introduce ViRA, a planner-agnostic visual representation alignment framework that keeps the planner architecture and inference cost unchanged. Our study reveals three findings:…

## 78. Learning Where to Split: Dynamic Band Splitting for Audio Source Separation

- 分数：17.0  ·  HF 赞：10  ·  来源：huggingface
- 兴趣命中：coding, spec
- 作者：Bingzhe Zhang, Kai Li, Xiaolin Hu
- 链接：[arXiv](https://arxiv.org/abs/2610.14993) · [PDF](https://arxiv.org/pdf/2610.14993) · [HF](https://huggingface.co/papers/2610.14993)

Audio source separation models must preserve fine spectral structure while keeping the cost of the separator tractable. Band-split architectures reduce this cost by manually partitioning the spectrum into predefined frequency bands and encoding each band as a token, but the same boundaries are used for every mixture. Because informative spectral structure varies with source content, fixed boundaries can merge…

## 79. LLM-to-Flow Distillation: Teaching Natural Language Goals to Scientific Generators

- 分数：17.0  ·  HF 赞：10  ·  来源：huggingface
- 兴趣命中：reasoning, spec
- 作者：Riccardo De Santi, Federico Di Gennaro, Angelo Gnazzo, Sophia Tang, Pranam Chatterjee, Fanny Yang, İsmail İlkan Ceylan, Michael M. Bronstein, Andreas Krause
- 链接：[arXiv](https://arxiv.org/abs/2610.17246) · [PDF](https://arxiv.org/pdf/2610.17246) · [HF](https://huggingface.co/papers/2610.17246)

Generative discovery in science requires coupling high-level scientific reasoning with the ability to generate samples respecting the structure of a design space. Yet these capabilities remain largely separated: foundation LLMs encode broad chemical and biological knowledge, while domain-specific flow- and diffusion-based generators capture the priors needed to produce valid sequences and geometries. We study how to…

## 80. VASPO: Self-Distillation with Privileged Value Estimation

- 分数：17.0  ·  HF 赞：6  ·  来源：huggingface
- 兴趣命中：reasoning, benchmark, spec
- 作者：Fei Wu, Zhenrong Zhang, Jianshu Zhang, Jun Du
- 链接：[arXiv](https://arxiv.org/abs/2610.20516) · [PDF](https://arxiv.org/pdf/2610.20516) · [HF](https://huggingface.co/papers/2610.20516)

On-policy self-distillation provides dense supervision for reasoning models via a privileged self-teacher. However, this supervision reflects local token preferences rather than the expected return of an unguided student continuation. Recent methods combine this signal with GRPO. They use GRPO for update directions and the teacher for signal scaling. However, we demonstrate a more effective integration within PPO.…

## 81. Share the Symbol, Not the Vector: Training-Free Fact Communication Across Language Models

- 分数：16.5  ·  HF 赞：9  ·  来源：huggingface
- 兴趣命中：agent, language model
- 作者：Xin Li, Mengbing Liu, Hao Jiang, Xin Gao, Annan Wang, Xingwei Qu, Yichi Zhang, Chau Yuen
- 链接：[arXiv](https://arxiv.org/abs/2610.19696) · [PDF](https://arxiv.org/pdf/2610.19696) · [HF](https://huggingface.co/papers/2610.19696)

Multi-agent systems allow language models to solve tasks collaboratively by sharing complementary information. These systems typically communicate through text, while recent approaches also explore exchanging internal model states. However, sharing these states across architectures often requires learned translators or assumptions about model compatibility. We introduce SYNC (Symbol-Indexed Neural Communication), a…

## 82. MA-Bench: Measuring Operational Planning in Language Models

- 分数：16.5  ·  HF 赞：5  ·  来源：huggingface
- 兴趣命中：reasoning, language model, planning
- 作者：Rodney Lafuente-Mercado, Robert Sincero, Phil Sage, Yuan Xue
- 链接：[arXiv](https://arxiv.org/abs/2610.19138) · [PDF](https://arxiv.org/pdf/2610.19138) · [HF](https://huggingface.co/papers/2610.19138)

How well can a language model turn a large, incomplete and partly contradictory body of documents into a plan when no single correct answer exists? We introduce Mission Analysis (MA)-Bench, built on mission analysis, the first step of military operational planning, in which a staff reads the full situation and states the problem before anyone proposes a solution. Its 10 expert-built scenarios pair synthetic packets…

## 83. G^3VLA: Geometric Inductive Bias for Vision-Language-Action Models

- 分数：16.5  ·  HF 赞：5  ·  来源：huggingface
- 兴趣命中：reasoning, coding, spec
- 作者：Yue Peng, Yongzhe Zhao, Artur Habuda, Khuyen Pham, Yanheng Zhu, Tran Nguyen Le, Fares Abu-Dakka, Li Guo
- 链接：[arXiv](https://arxiv.org/abs/2606.24472) · [PDF](https://arxiv.org/pdf/2606.24472) · [HF](https://huggingface.co/papers/2606.24472)

Vision-language-action (VLA) models have rapidly advanced generalist robot manipulation by harnessing the semantic knowledge of pretrained vision-language backbones. However, their visual representations are typically grounded in 2D image coordinates rather than calibrated camera geometry. This limitation is especially pronounced in multi-camera systems, where views are coupled by known intrinsics and extrinsics but…

## 84. CLIFT: Conformal Self-Verification for Web Agent Training and Test-Time Scaling

- 分数：16.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：agent, reinforcement learning, evaluation, benchmark
- 作者：Yifan Zhang, Yutong Dai, Viraj Prabhu, Zhiyuan Hu, Ran Xu, Zeyuan Chen
- 链接：[arXiv](https://arxiv.org/abs/2610.06829) · [PDF](https://arxiv.org/pdf/2610.06829) · [HF](https://huggingface.co/papers/2610.06829)

Open-source web agents are now strong enough to execute realistic browser tasks, but training them with reinforcement learning still depends on weak supervision: binary task success is too sparse for credit assignment, while frontier-language-model judges are too expensive to call at every step and cannot be assumed available at deployment. We introduce CLIFT, a training and test-time scaling method built around…

## 85. The Agent Knew: Internal States Forecast Unauthorized Actions and Stop Them, and the Lies That Follow

- 分数：16.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：agent, reasoning, benchmark, spec
- 作者：Arya Fayyazi, Mehdi Kamal, Massoud Pedram
- 链接：[arXiv](https://arxiv.org/abs/2610.17301) · [PDF](https://arxiv.org/pdf/2610.17301) · [HF](https://huggingface.co/papers/2610.17301)

Language-model agents sometimes act beyond their authorization and then misreport what they did. On CAPE-Bench, matched agent tasks in which one fact decides whether an action is authorized, frontier open-weight agents do both, and one behavior marks the lie: retroactive permission laundering, acting and then asking permission as if the action were pending, precedes a false report in 70% of 1081 fresh informed…

## 86. WorldMemBench: A Comprehensive Benchmark for Memory of Video World Models

- 分数：16.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：memory, evaluation, benchmark, spec
- 作者：Nan Zhou, Jianxiong Gao, Qiuyu Wang, Wen Wang, Jiahao Wang, Yufeng Yuan, Shuaiting Li, Hao Ouyang, Yujun Shen, Weiming Lu, Jun Xiao, Yueting Zhuang, Yongliang Shen
- 链接：[arXiv](https://arxiv.org/abs/2610.19063) · [PDF](https://arxiv.org/pdf/2610.19063) · [HF](https://huggingface.co/papers/2610.19063)

As video models enable longer and more realistic interactive experiences, maintaining a world consistent with its history becomes essential. This requires both preserving previously observed content and ensuring coherent world evolution over time. World memory is a critical capability to evaluate alongside visual fidelity and video duration. We introduce WorldMemBench, a benchmark for systematically evaluating world…

## 87. Unlocking Structured Pruning for Reasoning Language Models via Attention-Preserving MLP Trimming

- 分数：16.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：memory, reasoning, benchmark, language model
- 作者：Woosang Lim, Haneul Yoo, Vincent-Daniel Yun, Sungjoo Yoo
- 链接：[arXiv](https://arxiv.org/abs/2610.19121) · [PDF](https://arxiv.org/pdf/2610.19121) · [HF](https://huggingface.co/papers/2610.19121)

Structured pruning reduces LLM inference costs by removing model components to produce smaller dense models. However, existing methods can cause reasoning performance to collapse on long-form reasoning tasks such as AIME. We propose LayerTrim, a training-free structured pruning method that identifies redundant decoder layers and selectively trims their MLP features while preserving attention and decoder depth.…

## 88. PN-Mix: Pair-Norm Guided Mixed-Precision Key Cache Quantization for Efficient Long-Output LLM Inference

- 分数：16.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：memory, reasoning, benchmark, language model, large language, coding
- 作者：Gil Jae Song, Sungjoo Yoo
- 链接：[arXiv](https://arxiv.org/abs/2610.19605) · [PDF](https://arxiv.org/pdf/2610.19605) · [HF](https://huggingface.co/papers/2610.19605)

Long-output inference in large language models suffers from severe KV cache memory and bandwidth bottlenecks. While KV cache quantization alleviates this issue, low-bit quantization (e.g., 2-bit) severely degrades model accuracy. Recent mixed-precision key-cache quantization methods mitigate this degradation by allocating higher precision to important key channels, but estimate channel saliency using only key…

## 89. Mosaic: Multi-Session Agentic Reinforcement Learning

- 分数：16.5  ·  HF 赞：1  ·  来源：huggingface + arxiv
- 兴趣命中：agent, reinforcement learning
- 作者：Yilong Xu, Minrui Xu, Xinyu Zhou, Xiang Long, Haochen Tan, Zhijiang Guo
- 链接：[arXiv](https://arxiv.org/abs/2610.22174) · [PDF](https://arxiv.org/pdf/2610.22174) · [HF](https://huggingface.co/papers/2610.22174)

Most existing agentic reinforcement learning methods assume single-session trajectories, where interaction proceeds within one continuously accumulated context. However, agentic techniques such as context compaction and subagent forking may produce trajectories spanning multiple sessions, creating a mismatch between the single-session training assumption and inference-time execution. Therefore, we introduce…

## 90. Trajectory-Level Speculation with Semantic Verification for Tool-Using Agents

- 分数：16.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：agent, memory, language model, large language, coding, spec
- 作者：Zilin Wang, Yinhong Liu, Chao Chen, Qun Liu, Zhijiang Guo
- 链接：[arXiv](https://arxiv.org/abs/2610.21463) · [PDF](https://arxiv.org/pdf/2610.21463) · [HF](https://huggingface.co/papers/2610.21463)

Large language model agents solve tasks through long sequences of tool calls, and the prevailing design has a single strong model generate every step, although many steps are routine enough for a much smaller model. Existing ways of sharing this work keep the strong model as the generator: routers and collaborative agents decide which model handles each query or step, and speculative methods check a small model's…

## 91. Efficient Scene-Text Refinement via Pixel-Space Grouped Image Generation

- 分数：16.0  ·  HF 赞：12  ·  来源：huggingface
- 兴趣命中：benchmark
- 作者：Yaoli Liu, Guo-Hua Wang, Yiyang Chen, Qing-Guo Chen, Zhao Xu, Weihua Luo, Yao-Xiang Ding
- 链接：[arXiv](https://arxiv.org/abs/2610.18284) · [PDF](https://arxiv.org/pdf/2610.18284) · [HF](https://huggingface.co/papers/2610.18284)

Generated images often have coherent layouts and visual content, yet local errors in small text and complex characters still limit their readability and practical use. Scene-text refinement requires accuracy, preservation, and efficiency. Existing methods based on variational autoencoders (VAEs) can lose fine strokes during reconstruction, while full-image editing can shift background colors. In this work, we…

## 92. ProbabilityBench: Model Evaluation and Calibration with Exact Ground-Truth Uncertainty

- 分数：16.0  ·  HF 赞：8  ·  来源：huggingface
- 兴趣命中：evaluation, benchmark
- 作者：Yuyang Dai, Yuting Tang, Futoshi Futami, Takashi Ishida
- 链接：[arXiv](https://arxiv.org/abs/2610.17016) · [PDF](https://arxiv.org/pdf/2610.17016) · [HF](https://huggingface.co/papers/2610.17016)

Evaluating model uncertainty on real-world data is challenging because each instance provides only a single observed label, leaving true conditional class probabilities unknown. To address this, we introduce ProbabilityBench, a benchmark that provides exact, instance-level class probabilities across three simulated text-based domains: peer review, covert information transfer, and credit risk. By explicitly defining…

## 93. Rethinking Projector Training in Multimodal LLMs

- 分数：16.0  ·  HF 赞：8  ·  来源：huggingface
- 兴趣命中：benchmark, language model
- 作者：Fabian Gröger, Naël Ouerghemi, Shuo Wen, Maria Brbić
- 链接：[arXiv](https://arxiv.org/abs/2610.18598) · [PDF](https://arxiv.org/pdf/2610.18598) · [HF](https://huggingface.co/papers/2610.18598)

Multimodal LLMs are typically trained by first aligning a vision encoder with a language model via projector training on large image-caption datasets, followed by joint training of the full multimodal model. Despite its widespread use, the role of the projector training stage remains poorly understood. We find that (i) using only 10 to 20% of the data for training the projector already recovers most downstream…

## 94. TextVerifier: Seeing Beyond Recognition to Verify Chinese Text Rendering

- 分数：16.0  ·  HF 赞：8  ·  来源：huggingface
- 兴趣命中：benchmark, language model
- 作者：Yiyang Chen, Guo-Hua Wang, Yaoli Liu, Qing-Guo Chen, Zhao Xu, Weihua Luo, Xiujun Ma
- 链接：[arXiv](https://arxiv.org/abs/2610.19551) · [PDF](https://arxiv.org/pdf/2610.19551) · [HF](https://huggingface.co/papers/2610.19551)

Text-to-image models increasingly generate readable Chinese text that still contains local rendering defects, such as a character with an extra or missing stroke or a malformed component. Such errors are invisible to OCR and vision-language models, which are trained for recognition and are therefore invariant to the very structural deviations that define a rendering error. We formalize text rendering verification as…

## 95. Continuum Attention

- 分数：16.0  ·  HF 赞：8  ·  来源：huggingface
- 兴趣命中：memory, spec
- 作者：Afshin Khadangi
- 链接：[arXiv](https://arxiv.org/abs/2610.20586) · [PDF](https://arxiv.org/pdf/2610.20586) · [HF](https://huggingface.co/papers/2610.20586)

We introduce Continuum Attention (CA), a causal Transformer attention operator that replaces discrete key and value lookup with integration over a continuous, piecewise linear memory curve. Each query induces an exponential relevance density along the curve. Integrating the density and interpolated values yields exact normalized attention from closed form exponential moments, including half token boundary…

## 96. ANTE: Anticipate, Then Execute -- Learning Internal World Models for Coding Agents from Verified Beliefs

- 分数：16.0  ·  HF 赞：0  ·  来源：huggingface
- 兴趣命中：agent, reinforcement learning, language model, large language, coding
- 作者：Yi Ge, Kangrui Ruan, Jifan Chen, Manish Prajapat, Christian Bock, Xiaoyang Wang, Rein Houthooft, Aritra Sengupta, Varun Kumar
- 链接：[arXiv](https://arxiv.org/abs/2610.15368) · [PDF](https://arxiv.org/pdf/2610.15368) · [HF](https://huggingface.co/papers/2610.15368)

Rapid advances in large language models have made software engineering agents capable of tackling complex coding tasks. Within a containerized environment, a coding agent receives tool responses or execution results, and determines its later actions by those earlier results. However, most existing coding agents never look ahead: their policies do not anticipate the consequences of actions, and the terminal reward…

## 97. Generative World Simulation with DAO and JING

- 分数：15.5  ·  HF 赞：7  ·  来源：huggingface
- 兴趣命中：agent, spec
- 作者：XGEN Team, Guohao Cai, Haoxuan Che, Frank Fan, Chenran Huang, Junjia Huang, Jiayi Jiang, Yanheng Li, Leon Liu, Shaoteng Liu, Xi Liu, Feng Nie, Zhefan Rao, An Wang, Hanwen Wang, Pengxiang Yan, Jieming Yu, Qian Zha, Wentao Zheng
- 链接：[arXiv](https://arxiv.org/abs/2610.19726) · [PDF](https://arxiv.org/pdf/2610.19726) · [HF](https://huggingface.co/papers/2610.19726)

We present a Generative World Simulation framework that couples persistent shared world state with continuous first-person audiovisual generation. The framework integrates DAO, a computable world engine, and JING, an Egocentric Interactive Experience Model, to support sustained interaction for humans and agents. DAO maintains the states of characters, objects, and spaces and their relationships, advancing the world…

## 98. Next-Concept Modeling: Fast, Parallel Coarse-to-Fine Text Generation

- 分数：15.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：reasoning, evaluation, language model
- 作者：Hermann Kumbong, Ishan S. Khare, Iddah Mlauzi, Andrew Woen, Charles Ding, E. Kelly Buchanan, Simran Arora, Azalia Mirhoseini, Christopher Ré
- 链接：[arXiv](https://arxiv.org/abs/2610.14162) · [PDF](https://arxiv.org/pdf/2610.14162) · [HF](https://huggingface.co/papers/2610.14162)

Diffusion language models (DLMs) offer parallel sampling for faster generation than autoregressive models, an increasingly important advantage as inference becomes a dominant computational workload. However, DLMs degrade quickly with fewer sampling steps, process the full sequence at every step, and require many passes over the dataset to reach good quality. We introduce Next-Concept Modeling (NCM), a two-stage,…

## 99. Self-Evolving Agent Harness

- 分数：15.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：agent, memory, evaluation
- 作者：Chuyang Wei, Haoxiang Guan, Minghang Zhu, Kexin Zhou, Jiyan He, Xiren Zhou, Huanhuan Chen, Yifei Shen
- 链接：[arXiv](https://arxiv.org/abs/2610.18813) · [PDF](https://arxiv.org/pdf/2610.18813) · [HF](https://huggingface.co/papers/2610.18813)

Harness self-evolution revises an agent's software scaffolding, including prompts, memory, workflows, and executable components, while keeping model weights fixed. We formalize a feedback-driven process in which accepted revisions persist across runs. The framework separates update targets from proposal and admission mechanisms. It distinguishes changes to interpreted state from revisions to tools and code,…

## 100. PreciseCoder: Faithful and Generalizable Debugging Beyond Unit-Test Rewards

- 分数：15.0  ·  HF 赞：6  ·  来源：huggingface
- 兴趣命中：reasoning, reinforcement learning
- 作者：Yunkai Zhan, Miaosen Chai, Shangshang Wang, Jike Zhong, Yuqing Yang, Deqing Fu, Serina Chang, Wang Bill Zhu
- 链接：[arXiv](https://arxiv.org/abs/2610.18755) · [PDF](https://arxiv.org/pdf/2610.18755) · [HF](https://huggingface.co/papers/2610.18755)

Reinforcement learning (RL) from unit tests is the common recipe for post-training code models, but a unit test only asks whether the final program passes. We analyze what this unit-test-only reward teaches a model during debugging and find that, while it raises pass rates, it also teaches the model to edit more and to hallucinate bugs in code that is already correct. We introduce PreciseCoder, a training algorithm…

## 101. Physical Time as a Missing Dimension of Robot Policy Memory Dynamics

- 分数：15.0  ·  HF 赞：6  ·  来源：huggingface
- 兴趣命中：memory, evaluation
- 作者：Yushen Liang, Yue Peng, Baosheng Jin, Tianluo Zhang, Xinyu Zhang, Shuyi Zhou, Zhuoran Chen, Xinqi Liu, Shenji Wan
- 链接：[arXiv](https://arxiv.org/abs/2610.20524) · [PDF](https://arxiv.org/pdf/2610.20524) · [HF](https://huggingface.co/papers/2610.20524)

Existing robot policy memories typically evolve with observation sequences, implicitly treating each update as the same amount of physical time. Yet identical observation histories can span different durations and require different actions, exposing physical time as a missing dimension of policy memory. We introduce Temporal Flow Policy (TFP), which learns memory dynamics to retain past events and evolve the memory…

## 102. Learning Self-Orchestration in Decentralized Agent Swarms

- 分数：15.0  ·  HF 赞：2  ·  来源：huggingface + arxiv
- 兴趣命中：agent
- 作者：Guowei Xu, Zhenting Qi, Amani Kiruga, Himabindu Lakkaraju, Yilun Du
- 链接：[arXiv](https://arxiv.org/abs/2610.22322) · [PDF](https://arxiv.org/pdf/2610.22322) · [HF](https://huggingface.co/papers/2610.22322)

The capabilities of an agent swarm depend on both its individual members and how they coordinate. Yet existing multi-agent systems often train agents within fixed orchestration structures, separating the learning of individual capabilities from the organization of collective behavior. We introduce market-based post-training (MPT), a framework for jointly learning action policies and self-orchestration in…

## 103. InfiniSplat v2: Analyzing and Improving Feed-Forward 3DGS from Any Views

- 分数：14.5  ·  HF 赞：9  ·  来源：huggingface
- 兴趣命中：spec
- 作者：Yongzhen Hu, Hao Yu, Jiawei Wang, Xianming Zeng, Jianyun Xu, Xingliang Liu, Ruizhen Hu, Xiaowei Zhou, Hujun Bao, Sida Peng
- 链接：[arXiv](https://arxiv.org/abs/2610.20341) · [PDF](https://arxiv.org/pdf/2610.20341) · [HF](https://huggingface.co/papers/2610.20341)

Feed-forward Gaussian reconstruction builds 3D scenes directly from input images for novel view rendering, but learning Gaussian attributes from predicted geometry for high-quality rendering under large viewpoint changes remains challenging. We analyze limitations in Gaussian attribute learning and introduce InfiniSplat v2, which improves rendering quality through architectural and training changes. Our method…

## 104. To Align or Not To Align: Check Your COMPASS Before You Train

- 分数：14.5  ·  HF 赞：5  ·  来源：huggingface
- 兴趣命中：language model, spec
- 作者：Fabian Gröger, Petar Damjanović, Maria Brbić
- 链接：[arXiv](https://arxiv.org/abs/2610.18638) · [PDF](https://arxiv.org/pdf/2610.18638) · [HF](https://huggingface.co/papers/2610.18638)

Combining pretrained models is a common strategy for building AI systems, whether by aligning a vision encoder with a language model or merging fine-tuned checkpoints. However, finding compatible pairs typically requires costly empirical search, as compatibility is known only after alignment or merging. We propose COMPASS (COMPatibility ASsessment Score), a theoretically motivated diagnostic that estimates whether a…

## 105. CoTranslator: Reverse to Forward Chain-of-Thought Translator for Reasoning Distillation

- 分数：14.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：reasoning, benchmark, spec
- 作者：Zinan Tang, Zhuoshi Pan, Kairui Chen, Ze Yan, Shaomian Zheng, Yukun Zhang, Gang Wang, Biqing Huang
- 链接：[arXiv](https://arxiv.org/abs/2610.20828) · [PDF](https://arxiv.org/pdf/2610.20828) · [HF](https://huggingface.co/papers/2610.20828)

Reasoning distillation requires chain-of-thought (CoT) data with correct answers, but obtaining such data efficiently remains challenging. Forward CoT generation (FCG) followed by rejection sampling (RS) produces verified, question-only responses, yet may require many teacher calls for difficult problems. Reverse CoT generation (RCG) is cheaper because it conditions on the known answer, but access to this answer can…

## 106. TimeRSI: Towards Self-Improved Agentic Deployment for Time-Series Foundation Models

- 分数：14.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：agent, coding, spec
- 作者：Haoxin Liu, Deqing Fu, Lucheng Fu, Yiqiao Jin, Rushi Qiang, Harshavardhan Kamarthi, B. Aditya Prakash
- 链接：[arXiv](https://arxiv.org/abs/2610.19725) · [PDF](https://arxiv.org/pdf/2610.19725) · [HF](https://huggingface.co/papers/2610.19725)

Time-series foundation models provide strong zero-shot forecast, but deployment for real-world applications still requires task-specific designs for model inputs and outputs. Direct inference can leave domain knowledge and recurring forecast errors unaddressed, while tailored pipelines require substantial human expertise and effort. We introduce TimeRSI, a self-improving agentic deployment system around frozen…

## 107. From Failures to Learnable Worlds: Policy-Conditioned Environment Generation for Navigation Agents

- 分数：14.0  ·  HF 赞：8  ·  来源：huggingface
- 兴趣命中：agent
- 作者：Yue Zhang, Han Lin, Zun Wang, Yidong Huang, Zaid Khan, Mohit Bansal
- 链接：[arXiv](https://arxiv.org/abs/2610.19420) · [PDF](https://arxiv.org/pdf/2610.19420) · [HF](https://huggingface.co/papers/2610.19420)

Simulated environments enable scalable training data generation for embodied agents, but more data does not necessarily provide what a particular agent needs to learn. Existing environment-generation pipelines largely optimize generic properties such as realism, diversity, or task coverage, while different pretrained policies can fail for different environmental reasons. We therefore introduce WEDGE, a framework for…

## 108. Glance Forcing: Making Bidirectional Diffusion Autoregressive at a Glance

- 分数：14.0  ·  HF 赞：8  ·  来源：huggingface
- 兴趣命中：spec
- 作者：Zhuobai Dong, Junchao Yi, Hu Jian Guo, Linjie Li, Rui Zhao, Alex Jinpeng Wang
- 链接：[arXiv](https://arxiv.org/abs/2610.20220) · [PDF](https://arxiv.org/pdf/2610.20220) · [HF](https://huggingface.co/papers/2610.20220)

Autoregressive generation underlies real-time, causal video synthesis and is the backbone of video world models. Today's dominant approach distills a bidirectional diffusion model into a causal few-step student, but existing pipelines make this conversion prohibitively expensive, requiring offline Probability Flow ODE} (PF-ODE) trajectories that cost tens of thousands of GPU-hours and terabytes of storage. We show…

## 109. VITAL: From Visual Motion to Precise Action

- 分数：14.0  ·  HF 赞：8  ·  来源：huggingface
- 兴趣命中：coding
- 作者：Ao Liang, Youquan Liu, Mingxiao Li, Wei Chow, Lingdong Kong, Yue Liao, Dongyue Lu, Yu Yang, Wei Yin, Runnan Chen
- 链接：[arXiv](https://arxiv.org/abs/2610.20604) · [PDF](https://arxiv.org/pdf/2610.20604) · [HF](https://huggingface.co/papers/2610.20604)

World-action models aim to turn visual anticipation into driving decisions, yet typically train action experts on trajectory representations defined independently of visual dynamics. This motivates deriving action targets directly from visual motion. We first examine a simpler setting in which trajectories are reconstructed from recorded future images. Even without the need for future prediction, reconstruction…

## 110. StreamErase: Towards Ultra-Fast Streaming Video Erasing

- 分数：14.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：context window, benchmark
- 作者：Zhuobai Dong, Xiaobing Tu, Xiantao Zhang, Jinkui Ren, Yinggui Wang, Yue Ma, Linfeng Zhang
- 链接：[arXiv](https://arxiv.org/abs/2610.20137) · [PDF](https://arxiv.org/pdf/2610.20137) · [HF](https://huggingface.co/papers/2610.20137)

Current video object removal methods suffer from prohibitive latency (minutes per video) and non-causal processing that prevents real-time interaction. We present StreamErase, enabling sub-second latency with up to 26 FPS streaming generation on a single GPU. Our approach first augments a text-to-video model with mask input to generate high-quality videos that erase target objects and synthesize coherent…

## 111. Recursive Environment Scaling for General Long-Horizon Agents

- 分数：14.0  ·  HF 赞：0  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark
- 作者：Lingxiao Jing, Zhengbo Jiao, Yichen Xiang, Bofan Zhu, Lingbei Meng, Yan Ni, Haorui Chen, Ran Ran, Zhirong Shen, Yuheng Yang, Chenhang Cui, Yaosong Du, Rui Huang
- 链接：[arXiv](https://arxiv.org/abs/2610.16397) · [PDF](https://arxiv.org/pdf/2610.16397) · [HF](https://huggingface.co/papers/2610.16397)

We study environment scaling as a way to increase agent-benchmark difficulty while holding core task objectives fixed. Our framework, Recursive Environment Scaling (RES), transforms existing benchmark environments while preserving their objectives and completion requirements. A proposer changes information access, resource relations, and execution dependencies; execution-grounded checks validate the resulting…

## 112. Exploring the Limits of Combinatorial Generalization in Embodied Manipulation

- 分数：13.5  ·  HF 赞：7  ·  来源：huggingface
- 兴趣命中：benchmark
- 作者：Xupeng Zhang, Yantai Yang, Chang Guo, Zhaokai Yin, Zhipeng Zhang
- 链接：[arXiv](https://arxiv.org/abs/2610.15425) · [PDF](https://arxiv.org/pdf/2610.15425) · [HF](https://huggingface.co/papers/2610.15425)

In embodied manipulation, Vision Language Action (VLA) models can execute atomic skills, but long-horizon manipulation requires recombining these skills without demonstrations for every skill combination. The full instruction route treats skill chaining as long-horizon imitation. In a controlled study, full instruction training on limited skill combination sequences reaches 40.0% ordered success on covered…

## 113. MFVSR: A Multi-Style and Fine-Grained Benchmark for Video Subtitle Removal

- 分数：13.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：evaluation, benchmark
- 作者：Xiyan Huang, Qingdong He, Peng Tang, Bo Yin, Chaoyi Wang, Xiaobin Hu
- 链接：[arXiv](https://arxiv.org/abs/2610.18461) · [PDF](https://arxiv.org/pdf/2610.18461) · [HF](https://huggingface.co/papers/2610.18461)

Video subtitle removal (VSR) is an important video restoration task, yet existing evaluation remains limited by low-resolution datasets, fragmented test sets, and generic video-inpainting protocols that fail to adequately capture localized restoration errors, unintended modifications, temporal instability, and incomplete outputs. In this paper, we introduce MFVSR, a large-scale multi-style benchmark for fine-grained…

## 114. A Diagnostic Study of World-Space Human Recovery Under High Camera Dynamics

- 分数：13.0  ·  HF 赞：6  ·  来源：huggingface
- 兴趣命中：benchmark
- 作者：Hao-Jen Chien, Wei-Lun Chao, Yu-Lun Liu
- 链接：[arXiv](https://arxiv.org/abs/2610.19729) · [PDF](https://arxiv.org/pdf/2610.19729) · [HF](https://huggingface.co/papers/2610.19729)

Monocular world-space human recovery methods excel on current benchmarks, but these rarely include fast camera motion. We introduce the K-Pop stress test, broadcast dance videos that combine fast, large camera motion with dense multi-person choreography. Leading methods produce plausible per-frame meshes on these videos, yet their world-space trajectories drift far from the performers' stage positions. Through a…

## 115. CarryOn: A Dual-Loop Harness for Personalized and Reliable Robot Assistance

- 分数：13.0  ·  HF 赞：6  ·  来源：huggingface
- 兴趣命中：planning
- 作者：Zixuan Wang, Yuqi Liu, Yuxin Chen, Sengqiao Yang, Jinhui Ye, Pengguang Chen, Changsheng Lu, Shu Liu, Bei Yu, Jiaya Jia
- 链接：[arXiv](https://arxiv.org/abs/2610.21453) · [PDF](https://arxiv.org/pdf/2610.21453) · [HF](https://huggingface.co/papers/2610.21453)

While generalist vision-language-action (VLA) models have enabled diverse open-world manipulation, real-world robotic assistance requires two critical capabilities they currently lack: personalization and reliable execution. First, executing an instruction like "make me a sandwich" requires grounding subtask decomposition in persistent user preferences rather than relying on a single generic solution. Second,…

## 116. Calibrated Typed Decisions for Entity, Relation, and Event Extraction

- 分数：13.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：benchmark, spec
- 作者：Yang Wang, Hanlin Xiao, Yanan Ma, Chenghao Xiao, Chenghua Lin
- 链接：[arXiv](https://arxiv.org/abs/2610.17113) · [PDF](https://arxiv.org/pdf/2610.17113) · [HF](https://huggingface.co/papers/2610.17113)

Information extraction models often perform well on the datasets they are trained on, but transferring to new domains and annotation guidelines remains challenging. Supporting user-specified types alone does not resolve this problem. We present CalOn, a unified 0.6B-parameter encoder for entity, relation, and event extraction across datasets and schemas. The model jointly encodes text and type definitions, then…

## 117. VLX-Go: Robust Embodied Tracking through Multi-Stage Learning and On-Policy Refinement

- 分数：13.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：reasoning, spec
- 作者：Kyusong Lee, Heting Ying, Tiancheng Zhao
- 链接：[arXiv](https://arxiv.org/abs/2610.19361) · [PDF](https://arxiv.org/pdf/2610.19361) · [HF](https://huggingface.co/papers/2610.19361)

Embodied visual tracking requires a robot to identify a designated target from visual observations and control its own motion to follow that target through an environment. Following an isolated person is a comparatively simple demonstration of embodied visual tracking, but following the intended person among distractors remains challenging. Existing methods exhibit a substantial drop in success from single-target to…

## 118. Cortex: Measurement-Gated Evolution and Pruning of Coding-Agent Skills and Rules

- 分数：12.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：agent, coding
- 作者：Samuele Giampieri
- 链接：[arXiv](https://arxiv.org/abs/2610.14216) · [PDF](https://arxiv.org/pdf/2610.14216) · [HF](https://huggingface.co/papers/2610.14216)

Coding agents such as Claude Code also follow text files that developers write for them: a project file, skills the agent may choose to open, and rules that load automatically when the agent reads matching files. We call these files the agent's harness. Developers add to it whenever they correct the agent, but one success proves little: the same agent can pass a task once and fail it the next time.   We present…

## 119. Drive3R: Block-wise Streaming Geometric Foundation Models for Autonomous Driving

- 分数：12.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：memory, spec
- 作者：Tianyi Yang, Haojun Yang, Jipeng Xiao, Xuesong Chen, Shaoshuai Shi, Li Jiang, Zhipeng Zhang
- 链接：[arXiv](https://arxiv.org/abs/2610.15112) · [PDF](https://arxiv.org/pdf/2610.15112) · [HF](https://huggingface.co/papers/2610.15112)

High-fidelity closed-loop simulation for autonomous driving increasingly relies on dense multi-view 3D reconstruction. While recent feed-forward geometric foundation models have revolutionized per-scene optimization, applying them to continuous, long-horizon driving sequences is computationally intractable due to GPU memory limits and the quadratic complexity of global attention. Existing scaling strategies are…

## 120. RoTA-Bench: Evaluating 3D Spatial Reasoning through Interactive Projection Alignment

- 分数：12.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：reasoning, language model
- 作者：Qingchuan Ma, Yuexiao Ma, Xiang Meng, Yixuan Zou, Tianyu Xie, Wang Chen, Yuhui Zeng, Yuhang Wu, Xiawu Zheng, Rongrong Ji
- 链接：[arXiv](https://arxiv.org/abs/2610.17665) · [PDF](https://arxiv.org/pdf/2610.17665) · [HF](https://huggingface.co/papers/2610.17665)

Can vision-language models turn 2D observations into 3D understanding that supports precise action? This requires inferring object geometry, anticipating the effects of rotation, and refining actions through visual feedback. We introduce RoTA-Bench to evaluate these abilities through interactive 3D-to-2D projection alignment. Given a target silhouette, a model observes a rotated object and chooses successive…
