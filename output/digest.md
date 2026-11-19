# 每日 AI 论文

生成时间：2026-11-19 07:26 UTC  ·  共 120 篇（已按 arXiv ID 去重）

来源：Hugging Face Daily Papers + arXiv（cs.AI / cs.LG / cs.CL / cs.CV）。
排序：HF 上榜、点赞、多源命中、兴趣词。兴趣词可在 `config.json` 改。

## 1. TeleChat to Xing4: Advancing Frontier Agentic Models on Domestic Chips and Frameworks

- 分数：36.0  ·  HF 赞：154  ·  来源：huggingface
- 兴趣命中：agent, memory, reasoning, evaluation, language model, large language, coding, spec
- 作者：Xingchen AGI Lab, Baotian Hu, Bingkai Yang, Boyang Wang, Changzai Pan, Chao Lyu, Chao Wang, Chen Li, Chenshuo Pan, Chenyu Lin, Chenyuan Zhang, Chongming Liu, Dawei Fan, Di Wu, Dong Guo, Dong Li, Dongfang Li, Enlin Liu, Fanye Xiao, Fengkai Li, Fubei Yao, Gang Lin, Han Gao, Hanming Wu, Haowei He, Huapeng Liu, Hua Wang, Huinan Xu, Jiahong Xiong, Jiaxin Peng, Jianxiang Ma, Jianxing Zhuge, Jie Zhang, Ji Xiong, Jinglin Chen, Jingqi Li, Jingxuan Li, Jiwang Ye, Junchen Li, Junbiao Li, Junyang Wu, Kaidong Yu, Kaipeng Jia, Kehai Chen, Kuai Li, Laobin Liu, Lei Li, Libo Qin, Lingling Shi, Luwen Pu, Menghao Xu, Mengjiao Bao, Mengqi Chen, Min Zhang, Mingrui Wang, Naying Wang, Peicong Han, Peiming Guo, Pengfei Li, Qiang Feng, Qi Wang, Qingjun Zhu, Qingli Li, Qitai Ding, Qiyi Xie, Quanchao Zhao, Rongbao Han, Rui Xue, Ruiyu Fang, Ruiting Song, Shijie Li, Shiquan Wang, Shuangyong Song, Sishi Xiong, Teng Su, Wankang Bao, Weijie Zhang, Wei Mao, Weiwei Fu, Weiyang Huang, Wenmin Deng, Wenqing Hu, Wujie Zhong, Xi Yu, Xiaohui Hu, Xiaomin Fang, Xiaomeng Huang, Xiaoqiong Shi, Xiaotong Shang, Xiaoyu Li, Xinglei Xu, Xin Jiang, Xin Wang, Xin Zhang, Xinzhang Liu, Xue Liu, Xuefeng Bai, Xuewei He, Yahan Li, Yanhan Zhang, Yanlei Xue, Yanzhang Wu, Yang Yu, Yi Liu, Yin Zhang, Yingyan Li, Yitong Yao, Yixuan Li, Yongqiang Xia, Yongxiang Li, Yinzhou Zhu, Yu Zhao, Yuhao Jiang, Yunpeng Zhang, Yuting Lin, Yuxuan Wu, Yuyao Huang, Yuyi Wang, Zebo Peng, Zhenwu Pei, Zhenxiong Li, Zhao Wang, Zhaoxi Zhang, Zhihao Yang, Zhiqiang Dong, Zhiwei Yan, Zhilong Lu, Zhonghao Guo, Zhongheng Wu, Zhongjiang He, Zhongqiu Li, Zhu Yuan, Zhuoru Jiang, Zhuoyi Wei, Zijia Guo, Zilu Huang, Zhipeng Guo, Zirui Li, Zihan Wang
- 链接：[arXiv](https://arxiv.org/abs/2611.22115) · [PDF](https://arxiv.org/pdf/2611.22115) · [HF](https://huggingface.co/papers/2611.22115)

We present Xing 4, a series of large language models that extends the TeleChat lineage through coordinated advances in model architecture and training infrastructure on Ascend. This report describes the design principles and systems engineering behind the series, spanning architecture selection, large-scale pretraining, and reasoning and agentic post-training. We study how sparse activation, attention design, model…

## 2. AscendGYM: A Cost-Aware Kernel Optimization Benchmark for Real-World Workloads on Ascend NPUs

- 分数：36.0  ·  HF 赞：91  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark, language model, large language
- 作者：AI Training Platform Team, Bingwei Zhang, Jing Li, Amir Abdullin, Sihang Chen, Xin Chen, Liangjun Feng, Yingmeng Gao, Tao Guo, Junjie Huang, Dongfang Li, Zhanglian Lin, Jiajun Liu, Zekun Liu, Zhengxuan Lu, Xiaodong Luo, Jian Meng, Ivan Nosov, Linyuan Qiu, Weijian Sun, Wanrui Yan, Binfan Zheng, Zhicheng Zhou, Baotian Hu, Min Zhang, Haizhou Li, Zhiquan Luo
- 链接：[arXiv](https://arxiv.org/abs/2611.17621) · [PDF](https://arxiv.org/pdf/2611.17621) · [HF](https://huggingface.co/papers/2611.17621)

Kernel optimization is essential for efficient large language model (LLM) training and inference on Ascend NPUs. Existing Ascend kernel benchmarks primarily focus on kernel generation, with less emphasis on the ability of agents to optimize existing implementations under input configurations drawn from real workloads. To address this requirement, we introduce AscendGYM, a benchmark whose initial suite comprises 48…

## 3. Weight-Space Programming Doesn't Need Transformers

- 分数：36.0  ·  HF 赞：52  ·  来源：huggingface
- 兴趣命中：memory, benchmark, language model, large language
- 作者：Hyunjong Ok, Jaeho Lee
- 链接：[arXiv](https://arxiv.org/abs/2611.22055) · [PDF](https://arxiv.org/pdf/2611.22055) · [HF](https://huggingface.co/papers/2611.22055)

Standard neural architectures such as the Transformer were chosen because they train well with gradient descent and run fast on GPUs. In weight-space programming, a large language model (LLM) writes target weights by hand without gradient-based training, so those reasons no longer apply. Should we keep the Transformer? Given minimal guidance, ten labeled examples, and a sandbox, mainly on multiple-choice questions,…

## 4. Multi-Branch Transformer

- 分数：34.0  ·  HF 赞：45  ·  来源：huggingface
- 兴趣命中：long context, language model, coding
- 作者：Gaotang Li, Lingjie Chen, Chunyuan Deng, Zhiwei Xu, Hongzheng Chen, Christopher De Sa, Jingrui He, Yingheng Wang, Hanghang Tong
- 链接：[arXiv](https://arxiv.org/abs/2611.19800) · [PDF](https://arxiv.org/pdf/2611.19800) · [HF](https://huggingface.co/papers/2611.19800)

Transformer language models are commonly scaled by making their blocks wider or stacking them deeper. In this work, we explore a complementary path: branching, the parallel composition of full Transformer blocks. We introduce the Multi-Branch Transformer (MBT), which processes the input through shared initial layers, executes independently parameterized branches of sequential blocks in parallel, and fuses their…

## 5. Self-Improvement Memory Enables Continual Recursive Self-Improvement

- 分数：31.5  ·  HF 赞：31  ·  来源：huggingface
- 兴趣命中：memory, evaluation, benchmark, coding
- 作者：Xin Yu, Fei Xia, Jiaqi Pan, Youbao Tang, Chengzhi Liu, Adams Yu, Sicong Jiang, Yanfei Chen, Lingzhou Xue, Ting Yu
- 链接：[arXiv](https://arxiv.org/abs/2611.18856) · [PDF](https://arxiv.org/pdf/2611.18856) · [HF](https://huggingface.co/papers/2611.18856)

Harness optimization is often studied with a fixed policy model and benchmark. When either changes, the optimizer must decide which parts of an evolved harness to reuse or revise, but the harness alone may not explain why earlier edits were made or how they performed. In this work, we study Continual Recursive Self-Improvement (CRSI), a setting for continuing existing harness-optimization methods across compatible…

## 6. ForceHarness: Turning Force into Action and Physics for Frozen Frontier Models

- 分数：30.0  ·  HF 赞：41  ·  来源：huggingface
- 兴趣命中：benchmark
- 作者：Ke Sun, Kevin Yuchen Ma, Yike Zhang, Yanzhe Chen, Mike Zheng Shou
- 链接：[arXiv](https://arxiv.org/abs/2611.21099) · [PDF](https://arxiv.org/pdf/2611.21099) · [HF](https://huggingface.co/papers/2611.21099)

Frontier multimodal models can now control robots zero-shot from images, yet many manipulation tasks depend on contact forces that images cannot show. Bringing force to an API-only frozen model raises two challenges. First, contact evolves much faster than an API model can decide, so the system must close the loop on force beneath the model. Second, a frozen model cannot interpret raw force streams, so force must be…

## 7. Breath-Dx: A Time Series Classification Benchmark for Disease Screening with eNose

- 分数：30.0  ·  HF 赞：32  ·  来源：huggingface
- 兴趣命中：evaluation, benchmark, spec
- 作者：Ivan Poddiakov, Ivan Kruzhilov, Galina Zubkova, Svetlana Erofeeva, Andrey Savchenko, Pavel Blinov
- 链接：[arXiv](https://arxiv.org/abs/2611.15348) · [PDF](https://arxiv.org/pdf/2611.15348) · [HF](https://huggingface.co/papers/2611.15348)

Electronic nose (eNose) technology offers a portable, non-invasive route for disease screening via exhaled breath analysis. However, progress in the field is hindered by the lack of systematic benchmarks that compare machine learning methods under realistic conditions, particularly sensor drift, a known but rarely quantified failure mode. Most existing studies rely on small, private datasets with inconsistent…

## 8. Game2Player: Scaling Gameplay Experience for Visual Agents through Environment-Player Co-Development

- 分数：29.5  ·  HF 赞：19  ·  来源：huggingface + arxiv
- 兴趣命中：agent, benchmark, coding, planning
- 作者：Xirui Jiang, Yuxi Chen, Rui Yang, Feng Luo, Pengcheng Wang, Bingxuan Li, Zihao Zhao, Yushan Li, Han Wang, Manling Li, Yang Zhang, Shiyu Chang, Tong Zhang, Huan Zhang
- 链接：[arXiv](https://arxiv.org/abs/2611.24154) · [PDF](https://arxiv.org/pdf/2611.24154) · [HF](https://huggingface.co/papers/2611.24154)

Games are a rich testbed for visual agents, demanding perception, long-horizon planning, and precise control. However, collecting human gameplay is costly, and learning from gameplay videos requires inferring missing actions. Existing datasets also cover a limited range of games, often without explicit tasks or verifiable outcomes. To address these gaps, we introduce Game2Player, a framework that co-develops game…

## 9. Heave-Ho: Decentralized Long-Horizon Multi-Humanoid Collaboration

- 分数：26.5  ·  HF 赞：21  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark, planning
- 作者：Ting-Hsuan Chen, Siheng Zhao, Han Jiang, Qi Pan, Louison Lu, Jiaheng Luo, Henghui Bao, Yiyu Chen, Quan Nguyen, Yue Wang
- 链接：[arXiv](https://arxiv.org/abs/2611.22275) · [PDF](https://arxiv.org/pdf/2611.22275) · [HF](https://huggingface.co/papers/2611.22275)

Collaboration promises to extend humanoid capabilities beyond what individual robots can achieve. However, realizing this potential requires coordinated whole-body interactions, coherent long-horizon planning, and precise synchronization across robots. We introduce Heave-Ho, a decentralized framework for long-horizon collaborative multi-humanoid loco-manipulation. At the low level, we develop a multi-agent…

## 10. VideoNexus: Video Perception Beyond the Reasoning Context

- 分数：26.0  ·  HF 赞：20  ·  来源：huggingface
- 兴趣命中：agent, reasoning, evaluation, spec, planning
- 作者：Yancheng Long, Xuanyu Zheng, Wei Chen, Luoyuan Zhang, Haoyang Xu, Bin Wen, Tingting Gao
- 链接：[arXiv](https://arxiv.org/abs/2611.21392) · [PDF](https://arxiv.org/pdf/2611.21392) · [HF](https://huggingface.co/papers/2611.21392)

Understanding long videos requires locating evidence, resolving visual details, and integrating observations into an answer. Even when relevant evidence is present, performing these operations within long, dense visual sequences burdens both perception and reasoning. Video agents enable selective inspection, but returning frames to the planner still accumulates visual information in its reasoning context. Delegating…

## 11. Jeveration: System One Models Now Generate

- 分数：25.0  ·  HF 赞：22  ·  来源：huggingface + arxiv
- 兴趣命中：language model
- 作者：Yuhe Liu, Qi Li, Shihua Zhang, Xinchao Wang
- 链接：[arXiv](https://arxiv.org/abs/2611.24738) · [PDF](https://arxiv.org/pdf/2611.24738) · [HF](https://huggingface.co/papers/2611.24738)

System One models such as Jev return decisions through fast, parallel prediction. In this paper, we introduce Jeveration, showing that the same decision paradigm can also generate high-quality images in a single forward pass. Jeveration builds on a frozen vision-language model, repurposing its visual-semantic knowledge for holistic image generation. The key challenge is to maintain global consistency. A single…

## 12. Regularized Score Centering

- 分数：22.5  ·  HF 赞：13  ·  来源：huggingface
- 兴趣命中：agent, tool use, reasoning, reinforcement learning, evaluation, benchmark
- 作者：Hao Bai, Chenlu Ye, Xuanchang Zhang, Aviral Kumar, Tong Zhang
- 链接：[arXiv](https://arxiv.org/abs/2611.21791) · [PDF](https://arxiv.org/pdf/2611.21791) · [HF](https://huggingface.co/papers/2611.21791)

Asynchronous reinforcement learning increases training throughput, but data from stale policies and numerical mismatch between training and inference can destabilize learning. To stabilize off-policy learning, score centering (SC) removes the effect of reward baselines on the expected update. Our gradient diagnostics show less extreme gradients with SC than with importance sampling (IS), but SC can still fail when…

## 13. FastFrames: Video Generation at Interactive Latency

- 分数：22.0  ·  HF 赞：24  ·  来源：huggingface
- 兴趣命中：coding
- 作者：Gene Chou, Guandao Yang, Fujun Luan, Lars Mescheder, Wei Dong, Stephan Richter, Vladlen Koltun
- 链接：[arXiv](https://arxiv.org/abs/2611.23226) · [PDF](https://arxiv.org/pdf/2611.23226) · [HF](https://huggingface.co/papers/2611.23226)

Autoregressive video diffusion models generate frames based on new observations and inputs, making them a promising medium for interactive visual experiences. However, existing models are orders of magnitude too slow for fluid interaction. This paper introduces FastFrames, a family of fast autoregressive video diffusion models that achieves interactive latency without compromising quality. We profile the inference…

## 14. From Repositories to Training Environments: Scaling Long-Horizon Coding Agents with Environment Evolution Loop

- 分数：22.0  ·  HF 赞：12  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark, coding, spec
- 作者：Yang Tian, Tianyu Zheng, Xiyuan Yang, Yaxin Du, Chengran Yang, Bo Zhao, Jian Yang, Bryan Dai
- 链接：[arXiv](https://arxiv.org/abs/2611.21152) · [PDF](https://arxiv.org/pdf/2611.21152) · [HF](https://huggingface.co/papers/2611.21152)

Training coding agents for long-horizon tasks requires environments with verifiable feedback. Existing pipelines often follow a linear process that ends with validation, establishing usability but providing little guidance on improving training value. Recursive self-improvement (RSI) often requires model rollouts or model training followed by downstream evaluation, with costs and feedback delays amplified on…

## 15. Beyond Answering: Learning to Speak First and Act in Streaming Video

- 分数：21.0  ·  HF 赞：10  ·  来源：huggingface
- 兴趣命中：memory, evaluation, benchmark, language model, large language, spec
- 作者：Shuhan Li, Huankang Guan, Xintong Guo, Yang Bo, Yuyang He, Dunyuan Xu, Jingyan Chen, Fang Liu, Tsz Kin Wan, Jinpeng Chen, Zhenqi He, Yuxuan Hu, Wenbo Li, Han Gao, Qijun Li, Long Chen, Hongsheng Li, Rui Liu
- 链接：[arXiv](https://arxiv.org/abs/2611.17048) · [PDF](https://arxiv.org/pdf/2611.17048) · [HF](https://huggingface.co/papers/2611.17048)

Most AI assistants respond only when prompted, remaining silent even when events in the video stream offer meaningful opportunities for conversation. To move beyond purely user-driven interaction, we present AURA 2.0, a streaming video large language model that introduces three core upgrades to AURA. The key advance is Model-Initiated Conversation (MIC), which enables the model to identify topics worth discussing in…

## 16. MedJev: A System One Vision-Language Decision Model for Fast and Effective Medical Image Understanding

- 分数：21.0  ·  HF 赞：10  ·  来源：huggingface
- 兴趣命中：reasoning, benchmark, language model, spec
- 作者：Fan Zhang, Hao Wu, Jinyang Wu, Hongyu Qu, Zheng Lian, Dongfu Yin, Qingsong Wen, Pheng-Ann Heng
- 链接：[arXiv](https://arxiv.org/abs/2611.20992) · [PDF](https://arxiv.org/pdf/2611.20992) · [HF](https://huggingface.co/papers/2611.20992)

Medical image understanding with vision-language models (VLMs) typically relies on autoregressively generating reasoning and answer tokens. These unnecessary tokens make the inference cost scale with the response length and force the answer to be parsed from free-form text, incurring avoidable latency and decision errors. To this end, we introduce MedJev, a system one vision-language decision model that maps medical…

## 17. PIPETTE: Prompt Injection Purple-Teaming for Robust LLM Agents

- 分数：20.5  ·  HF 赞：1  ·  来源：huggingface + arxiv
- 兴趣命中：agent, reinforcement learning, evaluation, benchmark, language model, large language, spec
- 作者：Lipeng He, Yihan Wang, Jiawen Zhang, N. Asokan
- 链接：[arXiv](https://arxiv.org/abs/2611.24362) · [PDF](https://arxiv.org/pdf/2611.24362) · [HF](https://huggingface.co/papers/2611.24362)

Large language model (LLM) agents routinely interact with untrusted external data, exposing them to indirect prompt injection (IPI) attacks that hijack agents into executing attacker-chosen tasks. To uncover these vulnerabilities at scale, automated red-teaming methods often leverage reinforcement learning (RL) to generate attacks that achieve high attack success rates (ASR). Model developers use the attacks…

## 18. TCP4D: A Unified Tool-Center-Point Tracking and Generation Model for Robot Manipulation

- 分数：20.0  ·  HF 赞：24  ·  来源：huggingface
- 兴趣命中：-
- 作者：Haosong Peng, Xiangyang Liu, Zhengshen Zhang, Yunfeng Fan, Tianyu Qi, Xin Xia, Yufeng Zhan, Wenchao Xu
- 链接：[arXiv](https://arxiv.org/abs/2611.23143) · [PDF](https://arxiv.org/pdf/2611.23143) · [HF](https://huggingface.co/papers/2611.23143)

Robot manipulation videos provide a rich visual experience, yet recovering robot action and gripper-state annotations from RGB observations still remains challenging. Using the embodiment-agnostic tool-center-point (TCP) pose as the action space, we present TCP4D, a unified model in which a shared 4D scene representation both tracks observed TCP motion and generates future TCP trajectories. Given a monocular video…

## 19. WorldRuler: Interactive World Modeling under Configurable Rules

- 分数：19.5  ·  HF 赞：11  ·  来源：huggingface + arxiv
- 兴趣命中：spec
- 作者：Mingliang Zhai, Chuanhao Li, Jiaming Tan, Zhen Li, Yuwei Wu, Yunde Jia, Zian Meng, Yuanyang Yin, Kaipeng Zhang
- 链接：[arXiv](https://arxiv.org/abs/2611.24869) · [PDF](https://arxiv.org/pdf/2611.24869) · [HF](https://huggingface.co/papers/2611.24869)

Rules govern how player actions change interactive worlds. Different rules create distinct gameplay experiences within similar scenes and action spaces. For customizable gameplay, generative world models must follow user-defined rules beyond real-world behaviors. However, realizing user-defined rules presents two challenges: Rule-State Persistence and Rule-to-Visual Realization. The former requires preserving rule…

## 20. Movie2Game-Bench: Holistic Evaluation of Film-to-Game Adaptation Beyond Playability

- 分数：19.5  ·  HF 赞：3  ·  来源：huggingface + arxiv
- 兴趣命中：evaluation, benchmark, spec
- 作者：Jialing Xie, Yifan Zhou, Yiwen Zhang, Junjun He
- 链接：[arXiv](https://arxiv.org/abs/2611.24669) · [PDF](https://arxiv.org/pdf/2611.24669) · [HF](https://huggingface.co/papers/2611.24669)

Adapting a film into a game requires selecting source elements and translating them into player actions, rules, and feedback. We introduce Movie2Game-Bench (M2G-bench), a benchmark for evaluating film-to-game adaptation beyond playability. M2G-bench combines general evaluation, movie-specific evaluation, and playtesting by three GUI model players. The protocol connects source content to gameplay steps and…

## 21. Late Entry in Looped Language Models

- 分数：19.5  ·  HF 赞：3  ·  来源：huggingface + arxiv
- 兴趣命中：reasoning, language model, coding
- 作者：Ziqi Jin, Jiaxi Li, Weiwen Xu, Aixin Sun
- 链接：[arXiv](https://arxiv.org/abs/2611.24576) · [PDF](https://arxiv.org/pdf/2611.24576) · [HF](https://huggingface.co/papers/2611.24576)

Looped language models deepen reasoning at a compact parameter count by iterating a shared layer stack T times per token, turning recurrence depth directly into sequential decoding latency. Conventional early-exit decoding halts after initial passes without cache completion, truncating cached key-value states of past tokens to shallow depth. We study the opposite strategy, late entry, where new tokens skip initial…

## 22. PROLA: Principal-Orthogonal Low-rank Adaptation for Predictive Spatiotemporal Weather Downscaling

- 分数：19.0  ·  HF 赞：22  ·  来源：huggingface
- 兴趣命中：-
- 作者：Minseo Yoon, Minseong Bae, Sojin Lee, Hyunwoo J. Kim
- 链接：[arXiv](https://arxiv.org/abs/2611.11318) · [PDF](https://arxiv.org/pdf/2611.11318) · [HF](https://huggingface.co/papers/2611.11318)

High-resolution weather prediction is important for resolving local atmospheric patterns missed by coarse global forecasts. Large pretrained weather backbones have improved global forecasting, but adapting them to produce future high-resolution fields from recent coarse states remains challenging and costly. We formulate this setting as Predictive Spatiotemporal Weather Downscaling (PSWD), a task that jointly…

## 23. The Resolution Hypothesis: Agent Evolution's Key Is Identifying Improvements

- 分数：19.0  ·  HF 赞：14  ·  来源：huggingface
- 兴趣命中：agent, evaluation
- 作者：Yuanhao Zeng, Shaocheng Lan, Ao Lu, Kuang Yan, Heng Lin, Xinang Xu, Yuan Luo, Yueting Wang, Yexin Li, Ruo Shan, Kan Ren
- 链接：[arXiv](https://arxiv.org/abs/2611.23068) · [PDF](https://arxiv.org/pdf/2611.23068) · [HF](https://huggingface.co/papers/2611.23068)

Agent evolution follows a simple loop: a proposer writes candidate artifacts (prompts, skills, memories) and selection accepts those that score higher. This loop has shown promise, yet practitioners face a puzzle: methods trade wins across papers, and evolution often fails to bootstrap on certain tasks. We trace this puzzle to the Resolution Hypothesis: agent evolution stalls not because methods fail to propose…

## 24. VisualArtifactSpec 1.0: Evaluating Visual Artifacts under Task Specifications

- 分数：19.0  ·  HF 赞：6  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark, spec
- 作者：Shuyi Ouyang, Xiaojun Tang, Zijian Zou, Xintong Zhang, Mingli Song, Guannan Zhang, Hongwei Xue
- 链接：[arXiv](https://arxiv.org/abs/2611.21382) · [PDF](https://arxiv.org/pdf/2611.21382) · [HF](https://huggingface.co/papers/2611.21382)

Visual artifact tasks test agents' ability to translate task specifications and source materials into outputs that meet practical needs. Evaluation across artifact families helps distinguish broadly applicable authoring capabilities from strengths confined to a particular medium. We introduce VisualArtifactSpec 1.0 (VAS), a benchmark of 211 creation and modification tasks spanning presentations, static graphics,…

## 25. RoughCut-Bench: A Benchmark for Automatic Video Rough-Cut with Large Vision-Language Models

- 分数：19.0  ·  HF 赞：6  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark, language model
- 作者：Ruisi Zhao, You Li, Sihan Chen, Aosong Cheng, Chixiang Ma, Sen Pei, Zhen Yang, Hehe Fan, Dongliang He, Yi Yang
- 链接：[arXiv](https://arxiv.org/abs/2611.24098) · [PDF](https://arxiv.org/pdf/2611.24098) · [HF](https://huggingface.co/papers/2611.24098)

Video rough-cut is a core stage in media production workflows, organizing raw media materials into an initial video cut. Despite recent advances in large vision-language models (LVLMs) for video-related tasks, automatic rough-cut remains underexplored, without a comprehensive benchmark for evaluation or mature workflows for producing executable cut plans. To address the evaluation gap, we introduce RoughCut-Bench,…

## 26. π^4: A Foundation Model for 4D Scene Geometry and Motion

- 分数：18.5  ·  HF 赞：13  ·  来源：huggingface
- 兴趣命中：evaluation, benchmark
- 作者：Yifan Wang, Weiguang Zhao, Ni Yang, Haoyu Guo, Junting Dong, Weinan Zhang, Chunhua Shen
- 链接：[arXiv](https://arxiv.org/abs/2611.23144) · [PDF](https://arxiv.org/pdf/2611.23144) · [HF](https://huggingface.co/papers/2611.23144)

π^4 is a unified foundation model for 4D scene perception. From diverse, uncalibrated RGB observations in the wild---a single image, an unordered collection, or a video sequence---it recovers dense geometry, camera poses, and metric scale, together with 2D/3D point tracks and moving-object masks for multi-image inputs. It couples a geometry branch with a geometry-conditioned motion branch, which predicts image-space…

## 27. Tideway: Phase-Aware Tiered Memory Management for MoE Inference on Consumer Devices

- 分数：18.5  ·  HF 赞：5  ·  来源：huggingface
- 兴趣命中：agent, memory, evaluation, language model, large language
- 作者：Yifei Wang, Tsun-yu Yang, Yechen Xu, Hancheng Ye, Qinsi Wang, Baijun Zhou, Tingjun Chen, Hai &#34;Helen&#34; Li, Danyang Zhuo, Yiran Chen
- 链接：[arXiv](https://arxiv.org/abs/2611.14848) · [PDF](https://arxiv.org/pdf/2611.14848) · [HF](https://huggingface.co/papers/2611.14848)

Large language model (LLM) agents are rapidly becoming a dominant paradigm for AI applications. Recently, there is a growing demand to deploy large-scale Mixture-of-Experts (MoE) models locally on consumer PCs to balance data privacy, API costs, and inference efficiency. However, unlike datacenter servers with abundant DRAM, consumer devices are tightly constrained in both GPU VRAM and host RAM, forcing massive MoE…

## 28. A Foundation Model to Measure and Predict Human Behaviour

- 分数：18.5  ·  HF 赞：1  ·  来源：huggingface + arxiv
- 兴趣命中：evaluation, language model, large language
- 作者：Haoran Ye, Tianrui Huo, Hangzhen Li, Xin Zhang, Guojie Song
- 链接：[arXiv](https://arxiv.org/abs/2611.24830) · [PDF](https://arxiv.org/pdf/2611.24830) · [HF](https://huggingface.co/papers/2611.24830)

Large language models (LLMs) are increasingly used to infer psychological attributes, predict individual behaviour, and simulate human populations. However, despite generating plausible responses, they often misrepresent individuals and distort population statistics. Here we introduce Chiron, a foundation model to measure and predict human behaviour. We jointly fine-tune an LLM to represent psychological constructs,…

## 29. CADMAGEDDON: High-Fidelity CAD Reconstruction with Local Inference

- 分数：18.0  ·  HF 赞：8  ·  来源：huggingface
- 兴趣命中：agent, reasoning, benchmark
- 作者：Oleg Pavlov, Nikita Gavrilov, Soslan Kabisov, Gennadii Savrasov, Andrey Kuznetsov, Anton Konushin, Dmitrii Zhemchuzhnikov
- 链接：[arXiv](https://arxiv.org/abs/2611.22563) · [PDF](https://arxiv.org/pdf/2611.22563) · [HF](https://huggingface.co/papers/2611.22563)

CAD practitioners often work with proprietary parts that they are unwilling to share with external services. For individuals and small companies, bringing this work in-house also requires computational resources they can afford. We introduce CADMAGEDDON, an open-source agent that reconstructs editable CAD from meshes and can run locally on single-GPU systems and current-generation laptops. The method decomposes this…

## 30. QDA: Closed-Loop LLM Quantization Design with Agents

- 分数：18.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：agent, reasoning, evaluation, language model, large language
- 作者：Xingyang Li, Tianlang Zhao, Song Han, Ligeng Zhu
- 链接：[arXiv](https://arxiv.org/abs/2611.23388) · [PDF](https://arxiv.org/pdf/2611.23388) · [HF](https://huggingface.co/papers/2611.23388)

Post-training quantization is the standard way to serve large language models at low cost. However, the best quantization recipe differs across models and precisions. As a result, experts must redesign it for every new model, which is time-consuming and often sub-optimal. Fortunately, an LLM agent can take over this design by refining the recipe over rounds of building and evaluating candidates, so that more rounds…

## 31. PReMind: When Personal Memory Meets Visual Hazards

- 分数：18.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：memory, reinforcement learning, evaluation, benchmark
- 作者：Yeongtak Oh, Donghyeok Lee, Joonhee Oh, Jaewon Jeong, Sungroh Yoon
- 链接：[arXiv](https://arxiv.org/abs/2611.23808) · [PDF](https://arxiv.org/pdf/2611.23808) · [HF](https://huggingface.co/papers/2611.23808)

Personalized vision-language assistants use visual observations and personal memories to provide advice tailored to the user. When the observed scene contains a physical hazard, personal context, such as allergies, medical conditions, or mobility constraints, can change what help is appropriate. Responding appropriately therefore requires recognizing the visible hazard and applying the relevant person's information.…

## 32. ALIVE: Making Streaming Video Models Interactive

- 分数：17.5  ·  HF 赞：11  ·  来源：huggingface
- 兴趣命中：reinforcement learning, benchmark
- 作者：Jinzhao Li, Yuan Xu, Jinxuan Wu, Yukun Wang, Yijia Lei, Hanyu Ji, Yinuo Chen, Zining Huang, Chi Zhang, Hang Ye, Yiwu Zhong, Honglei Yan, Panwang Pan, Yizhou Wang, Yin Li, Miao Liu
- 链接：[arXiv](https://arxiv.org/abs/2611.21366) · [PDF](https://arxiv.org/pdf/2611.21366) · [HF](https://huggingface.co/papers/2611.21366)

Streaming video LLMs can continuously observe the world, yet often handle user requests in isolation. We introduce ALIVE, an interactive streaming video model supporting proactive monitoring, streaming task coordination, and feedback-seeking interaction. We construct ALIVE-SFT-288K and ALIVE-RL-3K for two-stage training. Contrastive supervised fine-tuning teaches when and how to respond, while reinforcement learning…

## 33. Agentic On-Policy Distillation Implicitly Reshapes LLMs' ReAct Patterns

- 分数：17.5  ·  HF 赞：7  ·  来源：huggingface
- 兴趣命中：agent, reasoning, spec
- 作者：Deyang Kong, Zhaoyi Li, Sijian Ren, Yuan Wei, Ying Wei, Defu Lian, Shikun Zhang, Wei Ye
- 链接：[arXiv](https://arxiv.org/abs/2611.19244) · [PDF](https://arxiv.org/pdf/2611.19244) · [HF](https://huggingface.co/papers/2611.19244)

On-policy distillation (OPD) transfers specialized capabilities to language-model agents, but its cross-domain effects on interaction remain unclear. We investigate how OPD reshapes ReAct interaction patterns across mathematics, ALFWorld, and τ^2-bench, focusing on reasoning, actions, and observation acquisition. General-reasoning supervision reduces mathematical tool attempts from 70.4% to 14.4% while increasing…

## 34. MillBill: A Machining Agent with Geometric Feedback

- 分数：17.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：agent, language model, spec, planning
- 作者：Gennadii Savrasov, Artem Slavin, Soslan Kabisov, Andrey Kuznetsov, Anton Konushin, Dmitrii Zhemchuzhnikov
- 链接：[arXiv](https://arxiv.org/abs/2611.22565) · [PDF](https://arxiv.org/pdf/2611.22565) · [HF](https://huggingface.co/papers/2611.22565)

Turning a CAD model into a machining program requires both process knowledge and geometric precision. Language models can generate such workflows by writing geometry and toolpath code for each part, but this makes numerical execution part of the model's task. We introduce MillBill, an agent that separates machining decisions from their geometric execution and verification. Given a boundary-representation part,…

## 35. LogT: Logically Think with Images for Visual Search

- 分数：17.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：tool use, tool-use, reasoning, reinforcement learning, benchmark, language model, spec
- 作者：Yanjun Fu, Quanzeng You, Jiadong Guo, Yujie Lu, Sai Charitha Akula, Haiping Wu, Miao Liu, Sanghamitra Dutta, Lu Yuan
- 链接：[arXiv](https://arxiv.org/abs/2611.19200) · [PDF](https://arxiv.org/pdf/2611.19200) · [HF](https://huggingface.co/papers/2611.19200)

Thinking with images empowers vision-language models (VLMs) to use an external Zoom-in tool for fine-grained visual search. Recent works employ supervised fine-tuning (SFT) and reinforcement learning (RL) with tool-specific designs to enable such capabilities. However, achieving logical reasoning alongside accurate and efficient tool use remains a significant challenge. To address this, we shift the focus away from…

## 36. M3OPD-Reasoner: An Open Recipe for Post-Training Multimodal Reasoning with Multi-Teacher On-Policy Distillation

- 分数：17.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：reasoning, reinforcement learning, benchmark, language model
- 作者：Nguyen Quang Trung, Hoang Phan, Shuo Sun, Longyin Zhang, AiTi Aw
- 链接：[arXiv](https://arxiv.org/abs/2611.23034) · [PDF](https://arxiv.org/pdf/2611.23034) · [HF](https://huggingface.co/papers/2611.23034)

Multi-Teacher On-Policy Distillation (MOPD) enables a single student to absorb the skills of several domain teachers by learning from its own generated responses. We present Multimodal Model Multi-Teacher On-Policy Distillation Reasoner (M3OPD-Reasoner), a fully open recipe for post-training vision-language models (VLMs) over three reasoning domains: image STEM, image perception, and video. We curate two datasets,…

## 37. DrawScore: Evaluating Generated CAD Models against Engineering Drawings

- 分数：17.0  ·  HF 赞：2  ·  来源：huggingface + arxiv
- 兴趣命中：agent, reinforcement learning
- 作者：Haorui Chen, Shiteng Lu, Zhanyu Guo, Zaixi Li, Yunhe Ni, Yaosong Du, Yichen Xiang, Xiande Huang, Rui Huang
- 链接：[arXiv](https://arxiv.org/abs/2611.24681) · [PDF](https://arxiv.org/pdf/2611.24681) · [HF](https://huggingface.co/papers/2611.24681)

Automatic CAD generation is commonly evaluated with volumetric IoU, Chamfer Distance, and surface F-score, which barely penalize local errors that occupy only a small fraction of a part's volume or surface area, such as a misplaced hole or a slot on the wrong face, even though such errors are critical to manufacturing. We formalize these metrics in a unified integral form and show that the weight of a local error…

## 38. Evidence-Based Credit Assignment for Search-Augmented Language Models

- 分数：17.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：reasoning, reinforcement learning, evaluation, benchmark, language model, spec, retrieval
- 作者：Wen Wang, Jindong Wang, Jiahua Bao, Tu Yongsiqi, Yihao Liu, Junwei He, Wenkui Fan
- 链接：[arXiv](https://arxiv.org/abs/2611.23824) · [PDF](https://arxiv.org/pdf/2611.23824) · [HF](https://huggingface.co/papers/2611.23824)

Reinforcement learning from terminal answer rewards enables search-augmented language models to interleave reasoning and retrieval without step-level annotations, yet outcome supervision assigns identical credit to every search in a trajectory regardless of whether it retrieved useful information. This limitation is especially severe when all sampled rollouts for a question fail, collapsing group-centered outcome…

## 39. Do LLM Agents Still Need to Be Told How to Self-Improve?

- 分数：16.5  ·  HF 赞：5  ·  来源：huggingface
- 兴趣命中：agent, benchmark, spec
- 作者：Shobhita Sundaram, Cansu Sancaktar, Phillip Isola
- 链接：[arXiv](https://arxiv.org/abs/2611.23219) · [PDF](https://arxiv.org/pdf/2611.23219) · [HF](https://huggingface.co/papers/2611.23219)

LLM agents increasingly drive their own learning. Self-improvement methods delegate various components of model optimization to the models themselves. As models become more capable, this motivates a basic question: do these increasingly capable models still need us to specify how they should self-improve? In this paper we study an autonomous paradigm in which, given basic primitives, resources, and a general goal…

## 40. WeightBench: Evaluating Language Models as Weight-Space Programmers

- 分数：16.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：agent, benchmark, language model, large language
- 作者：Aayush Marasini, Barsat Khadka, Nick Rahimi
- 链接：[arXiv](https://arxiv.org/abs/2611.18553) · [PDF](https://arxiv.org/pdf/2611.18553) · [HF](https://huggingface.co/papers/2611.18553)

Recent work shows that large language models (LLMs) can operate directly on the parameters of other neural networks. They can read what a network was trained to do, fix a network that fails, and write working networks from scratch, all without gradient descent. This capability has been termed Weight-Space Programming (WSP). Exploring this new paradigm systematically requires a robust benchmark. We introduce…

## 41. Thinking Harder Doesn't Lead to Better Choices: Reasoning Effort Increases the Confidence but Not the Correctness of LLM Shopping Agents

- 分数：16.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：agent, reasoning, benchmark, language model, large language
- 作者：Adi Krishnamoorthy, X. Y. Han
- 链接：[arXiv](https://arxiv.org/abs/2611.22033) · [PDF](https://arxiv.org/pdf/2611.22033) · [HF](https://huggingface.co/papers/2611.22033)

Large language models (LLMs) are increasingly deployed as autonomous shopping agents that process multimodal product listings (consisting of visual and text data) and recommend purchases on behalf of consumers. Naturally, one might assume that models with more thinking power would make higher-quality purchasing decisions. To test this belief, we ask two questions about such agents: does asking a model to think…

## 42. UltraTex: Aligning Physical Knowledge for High-Fidelity PBR Texture Generation

- 分数：16.5  ·  HF 赞：1  ·  来源：huggingface + arxiv
- 兴趣命中：language model, spec
- 作者：Jingzhi Bao, Xiaohe Ma, Hong Li, Yuanming Hu, Xiaoguang Han
- 链接：[arXiv](https://arxiv.org/abs/2611.24941) · [PDF](https://arxiv.org/pdf/2611.24941) · [HF](https://huggingface.co/papers/2611.24941)

Generating physically based rendering (PBR) texture maps for a 3D mesh from a single reference image is highly ambiguous, as the observed appearance entangles material identity, surface reflectance, and illumination. While current generative methods produce realistic albedo maps, they still struggle to infer accurate metallic and roughness attributes for relighting. We present UltraTex, a cascaded multi-view…

## 43. DNeo: Your Parallel Draft Model Needs Better Target Feature Encoding

- 分数：16.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：memory, coding, spec
- 作者：Jameson Sandler, Shane Bergsma, Mostafa Elhoushi, Bin Claire Zhang, Gavia Gray, Joel Hestness, Nolan Dey, Ferdinando Fioretto
- 链接：[arXiv](https://arxiv.org/abs/2611.21925) · [PDF](https://arxiv.org/pdf/2611.21925) · [HF](https://huggingface.co/papers/2611.21925)

Speculative-diffusion decoding uses a small parallel drafter model to generate b draft tokens in one forward pass, which then undergo parallel verification via a larger target model. Faster inference can be achieved when multiple draft tokens pass verification simultaneously. Recent parallel draft architectures (DFlash, DSpark) improve draft quality by conditioning on rich features computed by the target, through a…

## 44. AuXSpec: Learning to Autoformalize Program Specifications via Executable Postconditions

- 分数：15.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：evaluation, benchmark, spec
- 作者：Haocheng Wang, Weixuan Yuan, Florian Hübler, Yinya Huang, Zhijiang Guo, Sorrachai Yingchareonthawornchai, Rasmus Kyng
- 链接：[arXiv](https://arxiv.org/abs/2611.21421) · [PDF](https://arxiv.org/pdf/2611.21421) · [HF](https://huggingface.co/papers/2611.21421)

Formal specifications define intended program behavior and underpin verification, but writing them in theorem provers such as Lean is slow and expertise-intensive, making specification a major bottleneck to scaling formally correct code. Autoformalization from natural-language problems is promising, yet training specification models requires scalable feedback on whether generated specifications capture intended…

## 45. FMT: Lossless Image Compression in a Fixed Number of Parallel Steps

- 分数：15.0  ·  HF 赞：10  ·  来源：huggingface
- 兴趣命中：coding
- 作者：Ammar Ali
- 链接：[arXiv](https://arxiv.org/abs/2611.23108) · [PDF](https://arxiv.org/pdf/2611.23108) · [HF](https://huggingface.co/papers/2611.23108)

Learned lossless codecs make smaller files than common classical codecs, yet the images we archive and train on still use classical codecs. A main reason is time: a learned codec takes seconds to decode a photo that a classical codec opens in milliseconds, and their faster variants give up most of their gain in size. We argue that much of this time is spent waiting, not computing: the network waits for the values it…

## 46. Mechanistic Critics for Sample-Efficient NPU Design-Space Exploration

- 分数：15.0  ·  HF 赞：6  ·  来源：huggingface
- 兴趣命中：memory, spec
- 作者：Yicheng He, Yuqi Xue, Tianyang Wu, Jian Huang, Bin Hu
- 链接：[arXiv](https://arxiv.org/abs/2611.24733) · [PDF](https://arxiv.org/pdf/2611.24733) · [HF](https://huggingface.co/papers/2611.24733)

NPU design-space exploration for LLM inference mainly relies on an expensive simulator that often returns only scalar feedback such as latency and power. Such feedback can rank evaluated configurations, but gives little information for deciding why a configuration is slow or which architecture parameter should be changed next. This limitation is especially severe because prefill and decode workloads can be limited…

## 47. Attention at Absolute Zero

- 分数：15.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：reasoning, language model, retrieval
- 作者：Mostafa &#39;Neo&#39; Mohsenvand
- 链接：[arXiv](https://arxiv.org/abs/2611.11937) · [PDF](https://arxiv.org/pdf/2611.11937) · [HF](https://huggingface.co/papers/2611.11937)

Attention scores candidate supports of an answer, which we call witnesses, and reads the scores at a temperature. We build a higher-order attention layer whose state lives on pairs of items: for a pair (a, b), each third item k is a witness judged through its legs (a, k) and (k, b). It reads witnesses at zero temperature, keeping the best and the number tied with it, passes on only bits comparing such counts,…

## 48. TPHC: Improving Hyper-Connections with Tensor-Parallel Grouped Updates

- 分数：15.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：reasoning, benchmark, spec
- 作者：Xinying Hu, You Wu, Haoyi Wu, Jianchao Tan, Kefeng Zhang, Yuchen Xie, Kewei Tu
- 链接：[arXiv](https://arxiv.org/abs/2611.23026) · [PDF](https://arxiv.org/pdf/2611.23026) · [HF](https://huggingface.co/papers/2611.23026)

Hyper-Connections (HC) expand the residual stream of a Transformer into N parallel streams, and manifold-constrained HC (mHC) stabilizes them at scale. However, mHC benefits little from more than four streams, partly because each sublayer writes a single output to all streams, limiting how differently they can be updated. In this work, we propose TPHC, which integrates tensor-parallel (TP) shards with HC streams to…

## 49. MInfoVisQA: A Multilingual Benchmark for Information-Rich Visual Question Answering

- 分数：14.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：benchmark, language model, large language
- 作者：Changjiang Jiang, Jiang Zhou, Xinbin Yuan, Fan Zhang, Tao Feng, Zhuohan Xie
- 链接：[arXiv](https://arxiv.org/abs/2611.21644) · [PDF](https://arxiv.org/pdf/2611.21644) · [HF](https://huggingface.co/papers/2611.21644)

Multimodal large language models (MLLMs) excel in vision-language tasks; yet, whether they maintain consistent understanding of information-rich visuals (InfoVis) when the surface language changes remains unclear. To quantify this capability, we introduce MInfoVisQA, a parallel benchmark with 8,960 QA configurations derived from 128 seed instances across 24 languages. We construct seed-matched, language-parallel…

## 50. NexSight: Verifiable Tasks for Fine-Grained Agentic Long-Video Understanding

- 分数：14.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：agent, benchmark, spec
- 作者：Tianci Xie, Li Chen, Pinxue Guo, Rui Zheng
- 链接：[arXiv](https://arxiv.org/abs/2611.22790) · [PDF](https://arxiv.org/pdf/2611.22790) · [HF](https://huggingface.co/papers/2611.22790)

Fine-grained questions about long videos ask how many times an action occurs, in what order events unfold, or exactly when a state changes. Answering them can require finding brief moments scattered across hours of footage. Agentic models that decide when and where to look promise to find these moments, yet this ability is hard both to measure and to learn. Sparse supporting evidence may establish that an action…

## 51. Out of Sight, Still in Mind: Token Compression for Omni-LLMs

- 分数：14.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：benchmark, language model, large language
- 作者：Suho Yoo, Youngjoon Jang, Hyebin Cho, Joon Son Chung
- 链接：[arXiv](https://arxiv.org/abs/2607.21179) · [PDF](https://arxiv.org/pdf/2607.21179) · [HF](https://huggingface.co/papers/2607.21179)

The goal of this paper is to reduce the input token cost of Omni-modal large language models (Omni-LLMs) at inference time. Omni-LLMs reason jointly over audio, video and text, but the cost of the three streams is highly unbalanced: visual tokens account for the vast majority of the input, and are highly redundant. In this paper, we propose ReMo, a training-free framework that compresses visual tokens by…

## 52. MPEG-Diffusion: Mixed-Resolution Video Generation

- 分数：14.0  ·  HF 赞：8  ·  来源：huggingface
- 兴趣命中：coding
- 作者：Dennis Menn, Tianpei Gu, Guande He, Aryan V S, Yanke Song, Nan Liu, Desai Xie, Xun Huang, Chenfeng Xu, Diana Marculescu
- 链接：[arXiv](https://arxiv.org/abs/2611.12069) · [PDF](https://arxiv.org/pdf/2611.12069) · [HF](https://huggingface.co/papers/2611.12069)

Video diffusion transformers (DiTs) generate realistic videos, but their heavy computational cost limits broader real-world applications. Mixed-resolution generation reduces this cost by generating the visually important region at high resolution (HR) and the rest at low resolution (LR), yet existing methods suffer a severe quality drop on videos and require knowing the HR region in advance. We show that these…

## 53. Decoding Without a Decoder: Direct Pixel Prediction from Diffusion Transformers

- 分数：13.5  ·  HF 赞：7  ·  来源：huggingface
- 兴趣命中：coding
- 作者：Hansheng Chen, Shengqu Cai, Jan Ackermann, Rayhan Zirvi, Gordon Wetzstein, Xinchen Yan, Leonidas Guibas
- 链接：[arXiv](https://arxiv.org/abs/2611.22287) · [PDF](https://arxiv.org/pdf/2611.22287) · [HF](https://huggingface.co/papers/2611.22287)

Latent diffusion models rely on a decoder to map denoised latents to pixels, adding complexity and inference cost. We introduce Decoding Without a Decoder (DWD), which lets a finetuned diffusion transformer produce final pixels directly through a linear head. Unlike previous methods, where the denoising output leads to final pixels, DWD separates the two roles: the original denoising head continues to drive…

## 54. The novelty exposed: ablation, reproducibility and transparency in 40 technical reports of open-weight large language models (LLMs)

- 分数：13.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：language model, large language
- 作者：Bahaeddin Türkoğlu
- 链接：[arXiv](https://arxiv.org/abs/2611.20003) · [PDF](https://arxiv.org/pdf/2611.20003) · [HF](https://huggingface.co/papers/2611.20003)

In 2025 alone, 48 new large language model (LLM) architectures were added to the Hugging Face transformers library, and many of them arrive with a technical report that presents the model as new. What is actually new in these models, and is it tested? We put this question to LLM technical reports. We look at three things: what the reference code shows about how new open-weight architectures differ from earlier ones;…

## 55. Let Samples Sing in Chorus: Mitigating Spurious Correlations via Cross-view Consensus

- 分数：13.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：benchmark, spec
- 作者：Weiwei Li, Junzhuo Liu, Tong Chu, Hengfu Yu, Yinjie Lei, Wen Li
- 链接：[arXiv](https://arxiv.org/abs/2611.22668) · [PDF](https://arxiv.org/pdf/2611.22668) · [HF](https://huggingface.co/papers/2611.22668)

Deep models often rely on spurious correlations that fail on underrepresented groups. Existing methods either correct human-specified bias attributes or infer unknown biases from the learned representation space. However, annotated attributes may differ from the shortcuts actually used by a model, while a single representation provides incomplete and potentially noisy evidence. Our key insight is that a bias…

## 56. IDEA: Intent-Dominance Evidence Audit for Inference-Time Backdoor Detection in GUI Agents

- 分数：13.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：agent, spec
- 作者：Zhizhuo Kou, Sizai Hou, Jian Yang, Ge Sun, Junyu Luo, Wenkai Zhang, Sirui Han, Yike Guo
- 链接：[arXiv](https://arxiv.org/abs/2611.24102) · [PDF](https://arxiv.org/pdf/2611.24102) · [HF](https://huggingface.co/papers/2611.24102)

Organizations increasingly deploy downloaded open-weight GUI agents. A backdoored agent passes acceptance tests on clean data and misbehaves only when a visual trigger appears on screen, turning an unvetted checkpoint into a supply-chain risk. However, existing sample-level detectors target image classifiers and CLIP-style encoders, leaving step-level backdoor detection for GUI agents unaddressed. On clean steps,…

## 57. Unreasonable Confidence from Simulator Misspecification: Directional Robustness on the SPEED+ Sim-to-Real Benchmark

- 分数：12.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：benchmark, spec
- 作者：Nikolay Dolgov
- 链接：[arXiv](https://arxiv.org/abs/2611.20321) · [PDF](https://arxiv.org/pdf/2611.20321) · [HF](https://huggingface.co/papers/2611.20321)

Vision-based navigation systems for orbit must be trained almost entirely on synthetic imagery, because real labelled images of a given spacecraft in flight rarely exist. Benchmarks like SPEED+ are built for that situation: the training set comes from a simulator, and the test sets are real images of a satellite mockup under two kinds of lighting. That simulator approximates how light reflects off mylar and…

## 58. Code World Model 2.0: Towards Infinite Controllable Video Generation

- 分数：12.0  ·  HF 赞：8  ·  来源：huggingface
- 兴趣命中：-
- 作者：Ruoyu Wang, Hao Zhong, Yanming Yang, Jiahao Tian, Lin Liu, Biao Gong, Guoshan Lu, Yiding Tian, Chunhua Shen, Zhenzhong Lan, Chi Zhang
- 链接：[arXiv](https://arxiv.org/abs/2611.22925) · [PDF](https://arxiv.org/pdf/2611.22925) · [HF](https://huggingface.co/papers/2611.22925)

Visual proxies decouple explicit world-state simulation from photorealistic video synthesis, offering a controllable interface for both offline clip creation and real-time interactive streaming. Yet a practical renderer must address two challenges. Upstream proxies vary from coarse layouts to fine articulated geometry depending on the interaction, and streaming inference must operate in a few causal steps without…

## 59. Glyph: An Interpretability Engine for AI-Driven Scientific Discovery in Clinical Data

- 分数：12.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：agent
- 作者：Robbie Holland, Ashwin Kumar, Mateus A. Esmeraldo, David Le, Andrea Fisher, Jiazhen Pan, Louisa Fay, Magdalini Paschali, Vasiliki Sideri-Lampretsa, Ates Fettahoglu, Stefania Moroianu, Philipp Wesp, Ivan Lopez, Tom Nuno Wolf, McKenzie S. White, Eduardo Pontes Reis, Fatima Rodriguez, Curtis P. Langlotz, Vasilis Syrgkanis, Imon Banerjee, Akshay S. Chaudhari, Sergios Gatidis
- 链接：[arXiv](https://arxiv.org/abs/2611.08922) · [PDF](https://arxiv.org/pdf/2611.08922) · [HF](https://huggingface.co/papers/2611.08922)

Automated scientific discovery has the potential to advance understanding of disease mechanisms and accelerate identification of early disease markers. Manual data annotation is infeasible at population scale, motivating methods that automatically extract pre-defined phenotypes in multimodal and unstructured clinical data. Such pre-defined feature sets determine and limit which associations these approaches can…

## 60. ResWAM: Learning What Changes, Not What Stays, for World-Action Models

- 分数：12.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：benchmark
- 作者：Chongyu Fan, Gaowen Liu, Ramana Rao Kompella, Jason Corso, Sijia Liu
- 链接：[arXiv](https://arxiv.org/abs/2611.19559) · [PDF](https://arxiv.org/pdf/2611.19559) · [HF](https://huggingface.co/papers/2611.19559)

World-action models (WAMs) augment vision-language-action policies (VLAs) with future prediction so that the policy can anticipate how its actions will affect the physical world. Existing WAMs supervise complete future observations. However, observations typically change little over an action chunk, so the future loss is dominated by copying static background content rather than learning task-relevant robot and…

## 61. HubEgo-100K: In-the-Wild Egocentric Video of Skilled Work for Robot Learning

- 分数：12.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：benchmark
- 作者：Javad Amirian, Armin Kiani, Loïc Schaeffer, Tim Sprecher, Mohamed Taha, Karthik Yadati
- 链接：[arXiv](https://arxiv.org/abs/2611.21938) · [PDF](https://arxiv.org/pdf/2611.21938) · [HF](https://huggingface.co/papers/2611.21938)

Robot policies trained by imitation generalize poorly outside the environments and objects seen in training. Published data-scaling studies find that generalization grows with the diversity of training environments and objects rather than with more demonstrations per environment. Robot data is costly to collect across many environments, whereas egocentric human video can be recorded in the wild at scale; existing…

## 62. VAE Rhythm: Temporal Decoding Traces for AI-Generated Video Detection

- 分数：11.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：coding
- 作者：Ke Sun, Shuwei Li, Haiyang Mei, Mike Zheng Shou
- 链接：[arXiv](https://arxiv.org/abs/2611.21114) · [PDF](https://arxiv.org/pdf/2611.21114) · [HF](https://huggingface.co/papers/2611.21114)

Visible artifacts are an unreliable cue for detecting generated videos, because newer generators learn to remove them. We instead detect a trace left by the generation pipeline itself. Most video generators decode latents with a 3D causal VAE that groups consecutive frames in time, so the fidelity of generated frames rises and falls periodically with their position in a group. We call this periodic trace VAE Rhythm.…

## 63. Recurrent Domain Incremental Adaptation of Time-Series Foundation Models

- 分数：11.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：benchmark
- 作者：Sachith Abeywickrama, Peiliang Gong, Emadeldeen Eldele, Min Wu, Chau Yuen
- 链接：[arXiv](https://arxiv.org/abs/2611.24075) · [PDF](https://arxiv.org/pdf/2611.24075) · [HF](https://huggingface.co/papers/2611.24075)

Pretrained Time-Series Foundation Models (TSFMs) provide strong representations for downstream classification tasks. Yet adapting a TSFM under changing operating conditions remains challenging. A model must improve on each newly observed condition without sacrificing conditions it has already learned, often from only a small labeled calibration set and without knowing the operating condition at inference time. We…

## 64. GameRealm: Grounding Visual Learning in Interactive Games

- 分数：10.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：agent
- 作者：Weiguang Zhao, Yifan Wang, Ni Yang, Yating Wang, Xingyu Miao, Yankai Jiang, Mulin Yu, Tao Lu, Haoyu Guo, Junting Dong, Weinan Zhang, Chunhua Shen
- 链接：[arXiv](https://arxiv.org/abs/2611.23140) · [PDF](https://arxiv.org/pdf/2611.23140) · [HF](https://huggingface.co/papers/2611.23140)

Visual foundation models are central to physical intelligence, yet their development remains constrained by fragmented training datasets, inconsistent annotation quality, and limited multimodal supervision. To address these challenges, we introduce GameRealm, a large-scale, richly annotated dataset that grounds visual observations in synchronized, game-native supervision. GameRealm encompasses over 120 million RGB…

## 65. The Noise Floor of a Quantization Comparison: Engine, restart, batch and kernel drift, measured against 8-bit and 4-bit effects in two decision models

- 分数：10.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：-
- 作者：Aleks Blagojevich, Trevor Sunderland
- 链接：[arXiv](https://arxiv.org/abs/2611.15671) · [PDF](https://arxiv.org/pdf/2611.15671) · [HF](https://huggingface.co/papers/2611.15671)

A quantized model is usually judged by comparing it with its BF16 original, but that comparison changes more than the weights. It often changes the serving engine, it always runs on a different server instance, it may change how requests are batched, and on some stacks the library selects a different kernel depending only on which packages import. We measure each of these sources on the same 2,400 public decisions…

## 66. CONGA: Compiling Gaussian Fiber Geometry for Structured Bayesian Inference

- 分数：10.0  ·  HF 赞：0  ·  来源：huggingface
- 兴趣命中：spec
- 作者：Víctor Gallego
- 链接：[arXiv](https://arxiv.org/abs/2611.20995) · [PDF](https://arxiv.org/pdf/2611.20995) · [HF](https://huggingface.co/papers/2611.20995)

In structured Bayesian models, a large latent block is often Gaussian conditional on a smaller set of parameters, yet generic inference methods relearn this geometry during warmup. We study how this structure can be used to construct transports for posterior inference. The conditional mean and precision determine exact affine maps, including symmetric Brenier and triangular Knothe-Rosenblatt maps, that separate a…

## 67. Learning Anisotropic Prediction Targets for Flow Models

- 分数：9.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：-
- 作者：Rayhan Zirvi, Hansheng Chen, Gordon Wetzstein, Leonidas Guibas
- 链接：[arXiv](https://arxiv.org/abs/2611.17767) · [PDF](https://arxiv.org/pdf/2611.17767) · [HF](https://huggingface.co/papers/2611.17767)

Flow-based generative models are trained on a hand-chosen prediction target, such as the velocity, the noise, or the clean data. This choice strongly affects training and sample quality. We introduce Anisotropic Flow Models (AnisoFlow), which replaces a fixed prediction target with a fully learnable one. AnisoFlow learns to scale the noise component of the target anisotropically, assigning a separate nonnegative…

## 68. PanDWM: Panoramic 4D Driving World Models

- 分数：9.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：-
- 作者：Jiajun Sun, Zeyu Zhang, Zeyu Ren, Guangfeng Jiang, Yang Zhao, Hao Tang
- 链接：[arXiv](https://arxiv.org/abs/2611.19857) · [PDF](https://arxiv.org/pdf/2611.19857) · [HF](https://huggingface.co/papers/2611.19857)

Driving world models usually generate videos from six pinhole cameras with separate optical centres and small overlaps, and must learn to keep these views consistent. We present PanDWM, which stitches them into one 360^circ panoramic band. Camera boundaries then fall inside one image, so keeping the views consistent means keeping the image continuous, and each pixel still records its camera ray. Conditioned on…

## 69. Once Upon a Bias: Gender Stereotyping in LLM-Generated Children's Stories

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, language model, large language, spec
- 作者：Sayumi Muthukumarana, Roshan Godaliyadda, Parakrama Ekanayake, Roshan Ragel
- 链接：[arXiv](https://arxiv.org/abs/2611.24156) · [PDF](https://arxiv.org/pdf/2611.24156) · [HF](https://huggingface.co/papers/2611.24156)

Large language models are increasingly used to create stories for children. Since bedtime stories can shape children's perceptions of social roles, this raises concerns about whether LLMs adapt narrative portrayals according to the intended recipient's gender. We conducted a large-scale study to examine gender stereotyping in LLM-generated bedtime stories. Using matched daughter/son prompts and a five-generation…

## 70. Stabilizing Neural-to-Image Retrieval with Frequency-Domain Priors and Adaptive Supervision

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：language model, coding, spec, retrieval
- 作者：YaoYang Liu, ZhuoShi Tang, Haopeng Lai, Weijun Sun, Xiaozhao Fang, Jie Wen
- 链接：[arXiv](https://arxiv.org/abs/2611.24163) · [PDF](https://arxiv.org/pdf/2611.24163) · [HF](https://huggingface.co/papers/2611.24163)

Visual neural decoding aims to infer perceived visual stimuli from brain activity, offering important insights into human visual cognition while enabling transformative applications in brain computer interfaces and artificial intelligence. Recent advances in pretrained vision-language models have provided a semantically rich representation space for this task. However, reliable alignment between EEG/MEG signals and…

## 71. ViStep-RL: Stepwise Reinforcement Learning for Long-Horizon Visual Agents

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, memory, reasoning, reinforcement learning, benchmark, spec, retrieval
- 作者：Junyang Chen, Yao Qin, Xiao Li, Ningchao Wang, Yiguo Qiao, Wenbin Li, Xin Geng
- 链接：[arXiv](https://arxiv.org/abs/2611.24170) · [PDF](https://arxiv.org/pdf/2611.24170) · [HF](https://huggingface.co/papers/2611.24170)

Long-horizon visual agents must do more than inspect images: they must turn observations into evidence that remains usable as a task unfolds. Existing active-perception methods teach agents where and how to look, while a final-answer reward gives little structure for deciding which observations satisfy dependent subgoals or should be retained for later use. We present ViStep-RL (Visual Stepwise Reinforcement…

## 72. VideoACE: Benchmarking Agentic Video Understanding through High-Frame-Rate Actions

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, tool use, evaluation, benchmark, spec
- 作者：Luoyuan Zhang, Xuanyu Zheng, Yancheng Long, Haoyang Xu, Bin Wen, Tingting Gao
- 链接：[arXiv](https://arxiv.org/abs/2611.24184) · [PDF](https://arxiv.org/pdf/2611.24184) · [HF](https://huggingface.co/papers/2611.24184)

Agentic video understanding requires models to actively interact with video environments to gather evidence and form judgments. Evaluating this capability therefore requires assessing whether models can translate opportunities for interaction into better understanding. We introduce VideoACE, a benchmark for assessing video understanding under conditions that support sustained interaction. We focus on high-frame-rate…

## 73. Worth Another Look:Constrained World-Model Planning for Visual Inspection

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, benchmark, spec, planning
- 作者：Ziyue Kang, Zixi Qi, Yuchen Dai, Nana Lv, Xirong Cheng, Liang Liu, Ying Li, Haoyan Wei, Haiyang Yao
- 链接：[arXiv](https://arxiv.org/abs/2611.24187) · [PDF](https://arxiv.org/pdf/2611.24187) · [HF](https://huggingface.co/papers/2611.24187)

Visual inspection in field robotics and environmental monitoring must localize multiple targets under strict compute and sensing caps. Exhaustive sweeps waste calls on absent classes, while myopic and search-free policies stumble over heterogeneous tariff cliffs or discard viewport edits whose value emerges only after re-querying. We formulate inspection over frozen detectors as neuro-symbolic observation planning…

## 74. Learning to Coordinate: LLM-Guided Workflow Evolution for Token-Efficient Red Teaming

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, evaluation, language model, large language, planning
- 作者：Xiaoyang Xing, Wenyu Dai, Xiaoliang Gong, Asoke K Nandi, Anthony Cohn
- 链接：[arXiv](https://arxiv.org/abs/2611.24221) · [PDF](https://arxiv.org/pdf/2611.24221) · [HF](https://huggingface.co/papers/2611.24221)

Automated red teaming is essential for identifying safety failures in large language models (LLMs), but its practical scalability depends on the resources required to discover those failures. Multi-agent systems can combine complementary capabilities, yet repeated planning, redundant exchanges, and ineffective information routing can make their coordination expensive. Moreover, a target model's response indicates…

## 75. Do Thinking VLMs Need to Keep Looking at Long Videos? Write It Down, Then Look Away

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, reinforcement learning, benchmark, language model, coding
- 作者：Pengyu Li, Zhitao Gao, Lingling Zhang, Heng Wang, Chengqian Ma, WenHao Wang, Wenxuan Huang, Chen Zheng, Jun Liu
- 链接：[arXiv](https://arxiv.org/abs/2611.24259) · [PDF](https://arxiv.org/pdf/2611.24259) · [HF](https://huggingface.co/papers/2611.24259)

Vision-language models (VLMs) reason about long videos over hundreds to thousands of tokens. Every decoding step re-reads the key-value (KV) cache of the entire video. Must the model keep looking while it reasons? In LookAway, the model first writes timestamped notes on what the question needs and then puts the video away. Once the notes close, the inference engine hides the video's KV cache for the rest of the…

## 76. KnowledgeClaw: Towards Agentic Knowledge Engineering via Omnimodal Hypergraphs

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, memory, reasoning, benchmark, retrieval
- 作者：Haoran Luo, Jiapu Wang, Linhao Luo, Luu Anh Tuan
- 链接：[arXiv](https://arxiv.org/abs/2611.24294) · [PDF](https://arxiv.org/pdf/2611.24294) · [HF](https://huggingface.co/papers/2611.24294)

Knowledge engineering (KE) turns raw files into a reasoning-ready knowledge base, a task now within reach of LLM agents. KE has progressed from chunk and graph retrieval-augmented generation (RAG) to memory agents, agentic KE and multimodal KE. However, a live knowledge base needs omnimodality, a closed-loop lifecycle and multi-granular application at once, yet existing systems meet at most two and no benchmark…

## 77. Reducing Inference Cost of Coding Agents with Timeout Cascades

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, benchmark, language model, large language, coding
- 作者：Boxi Zhou, German Sviridov, Dmitrii Ustiugov, Haris Javaid
- 链接：[arXiv](https://arxiv.org/abs/2611.24324) · [PDF](https://arxiv.org/pdf/2611.24324) · [HF](https://huggingface.co/papers/2611.24324)

AI coding agents have become one of the most popular applications of large language models. Yet, agentic AI comes at the cost of a tremendous amount of GPU compute resources, which limits its profitability and its viability at scale. In this paper, we investigate whether smaller, cheaper models can cut this cost without sacrificing accuracy. We evaluate 36 popular large and small open-weight models released since…

## 78. Pixel2Perspective: A Benchmark for Multi-Modal and Multi-View Generalization in Vision-Language Models

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, language model, spec
- 作者：Aditya Gandhamal, Aniruddh Sikdar, Arya Kishor, Suresh Sundaram
- 链接：[arXiv](https://arxiv.org/abs/2611.24327) · [PDF](https://arxiv.org/pdf/2611.24327) · [HF](https://huggingface.co/papers/2611.24327)

Embodied AI systems, such as drones and autonomous vehicles, improve navigation by enhancing perception in environments containing unseen objects. While Visual Language Models (VLMs) offer strong image understanding, their real-world application is underexplored. For effective deployment, open-vocabulary semantic segmentation (OVSS) models, leveraging models like CLIP to assign pixel-level labels from text, must be…

## 79. Semantic Context Handoff with On-Demand Evidence for Long-Horizon Agents

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, context window, benchmark, retrieval
- 作者：Guolong Zheng, Chen Hou, Xu Yang, Jianshan Zhang, Tao Huang
- 链接：[arXiv](https://arxiv.org/abs/2611.24357) · [PDF](https://arxiv.org/pdf/2611.24357) · [HF](https://huggingface.co/papers/2611.24357)

Traditional long-horizon LLM agents often hand off context through full-history prompting, retaining all previous action--observation interactions. As execution proceeds, this history keeps growing, increasing inference cost and potentially degrading accuracy. Existing methods control this growth by preserving compact conclusions while removing earlier observations, but doing so can discard evidence that later…

## 80. CanopyKV: Remember beyond the Crop for Fast Active Visual Reasoning

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：tool use, memory, reasoning, spec
- 作者：Lei Yang, Dayan Wu, Yiliang Zhu, Xinze Liu, Hengjie Zhu, Zihao Zhang, Ding Wang, Peng Fu, Zheng Lin
- 链接：[arXiv](https://arxiv.org/abs/2611.24373) · [PDF](https://arxiv.org/pdf/2611.24373) · [HF](https://huggingface.co/papers/2611.24373)

Active visual reasoning enables multimodal models to answer challenging visual questions by gathering fine-grained evidence through iterative image inspection and tool use. However, accumulating crops and reasoning tokens expands the key-value (KV) cache, making compression important for reducing memory and inference costs. Existing KV compression methods typically select historical tokens based on attention,…

## 81. LLM-Assisted Multi-Fidelity Bayesian Optimization: Fusing Expert Knowledge with Numerical Data

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, language model, large language, spec
- 作者：Dongjun Han, Mingyu Lee, Ikjin Lee
- 链接：[arXiv](https://arxiv.org/abs/2611.24377) · [PDF](https://arxiv.org/pdf/2611.24377) · [HF](https://huggingface.co/papers/2611.24377)

Multi-fidelity Bayesian optimization (MFBO) reduces engineering design cost by combining inexpensive low-fidelity (LF) models with a few accurate high-fidelity (HF) evaluations and sequentially selecting designs to evaluate. However, when HF data are scarce, the LF-HF discrepancy is difficult to learn from numerical data alone, especially when physics omitted in the LF model makes it design-dependent. Yet even…

## 82. RSIBench-Infra: Can Agents Optimize Their Own Training and Inference Infrastructure at Production Scale?

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, evaluation, benchmark, spec
- 作者：Hanlin Wu, Yifei Wang, Zhicheng Cai, Huan-ang Gao, Wei-Ying Ma, Ya-Qin Zhang, Jingjing Liu, Hao Zhou
- 链接：[arXiv](https://arxiv.org/abs/2611.24395) · [PDF](https://arxiv.org/pdf/2611.24395) · [HF](https://huggingface.co/papers/2611.24395)

Improving the efficiency of training and inference infrastructure is a practical component of recursive self-improvement. Existing benchmarks for agent-driven optimization largely focus on individual software layers such as kernel, leaving unclear whether agents can deliver end-to-end performance gains under production workloads. We introduce RSIBench-Infra, a benchmark of 20 training and inference tasks spanning…

## 83. CaDO: Formal Verification-Guided Multi-Agent Framework for Causal Dataset Repair and Generation

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reasoning, spec, retrieval
- 作者：Songli Yu, Qi Luo
- 链接：[arXiv](https://arxiv.org/abs/2611.24406) · [PDF](https://arxiv.org/pdf/2611.24406) · [HF](https://huggingface.co/papers/2611.24406)

High-quality causal reasoning datasets are essential for developing models with reliable causal understanding, particularly in specialized domains. However, existing datasets frequently suffer from incorrect annotations and structural imbalances, which can lead to biased predictions and limited generalization. To address this issue, we propose CaDO (Causal-Engine-Guided Multi-Agent Data Optimization), a multi-agent…

## 84. MLIE-CoT: Chain-of-Thought Reasoning via Multi-Level Image Editing

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, benchmark, language model, large language
- 作者：Baichuan Yang, Dongyuan Xu, Zhao Yang, Yong Liu, Bing Su
- 链接：[arXiv](https://arxiv.org/abs/2611.24433) · [PDF](https://arxiv.org/pdf/2611.24433) · [HF](https://huggingface.co/papers/2611.24433)

Chain-of-thought (CoT) reasoning has proven effective in improving the reasoning abilities of large language models by breaking complex tasks into step-by-step solutions. In recent years, researchers have attempted to extend CoT reasoning to visual generative models to improve their ability to handle complex tasks. However, existing CoT methods for text-to-image generation still rely mainly on textual reasoning and…

## 85. NativeSeg: Native Vision Language Segmentation of 3D Computed Tomography via Spatial Visual Tokens and Verified Local Zoom

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, reasoning, evaluation, language model, coding
- 作者：Chengqian Ma, Gaole Dai, Zijie Meng, Weixuan Jin, Yijie Du, Yuexiao Ma, Xiawu Zheng, Fei Chao
- 链接：[arXiv](https://arxiv.org/abs/2611.24443) · [PDF](https://arxiv.org/pdf/2611.24443) · [HF](https://huggingface.co/papers/2611.24443)

Text prompted 3D computed tomography (CT) segmentation requires both full slice context and fine boundary precision across volumes where over $80\%$ of organ prompted slices lack the queried target. Existing medical vision language models (VLMs) are largely non native segmenters: they delegate pixel delineation outside the VLM by compressing reasoning into a 1D [SEG] vector for an external Segment Anything Model…

## 86. Cooperative UAV and Ground Station for Robust MEC of Dynamic Aquatic IoT: A Generative AI-Enhanced Approach

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reinforcement learning, benchmark, spec
- 作者：Jiahao You, Ziye Jia, Chao Dong, Qihui Wu, Zhu Han
- 链接：[arXiv](https://arxiv.org/abs/2611.24466) · [PDF](https://arxiv.org/pdf/2611.24466) · [HF](https://huggingface.co/papers/2611.24466)

The increasing aquatic Internet of Things (AIoTs) require computational support and coverage in applications such as maritime search and rescue. Unmanned aerial vehicles (UAVs) can offer low-cost, flexible aerial services, and ground stations (GSs) can provide powerful supports, which can cooperate to help the AIoTs in complex scenarios. However, the collaboration between UAVs and GSs for AIoTs faces challenges of…

## 87. ProbMedTOD: A Bayesian Network Guided Task-Oriented Dialogue System for Patient History Taking

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reasoning, language model, spec, retrieval
- 作者：Vishal Vivek Saley, Bhavesh Gurnani, Dinesh Raghu,  Mausam
- 链接：[arXiv](https://arxiv.org/abs/2611.24535) · [PDF](https://arxiv.org/pdf/2611.24535) · [HF](https://huggingface.co/papers/2611.24535)

Patient history taking is a strategic, multi-turn process that refines diagnostic hypotheses through iterative questioning, mirroring clinical reasoning where each inquiry updates beliefs over candidate diagnoses. Deploying AI in this setting is constrained by privacy, cost, and latency, making Small Language Models (SLMs) a more desirable backbone compared to larger LLMs. However, SLMs capture only the fast,…

## 88. NaviGATE: Noise-Aware Dual-View Generation for Multimodal Knowledge Graph Reasoning

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, benchmark, language model, coding, spec, retrieval
- 作者：Jie Peng, Yongxue Shan, Yongfu Zha, Cui Miao, Xiaodong Wang
- 链接：[arXiv](https://arxiv.org/abs/2611.24552) · [PDF](https://arxiv.org/pdf/2611.24552) · [HF](https://huggingface.co/papers/2611.24552)

Multimodal knowledge graph reasoning (MKGR) aims to infer missing facts by jointly exploiting relational structures, textual descriptions, and visual evidence. Existing embedding-based methods effectively capture graph topology, but their fixed multimodal representations are less effective for query-specific fine-grained semantic reasoning, while generation-based methods are vulnerable to noisy retrieval and may…

## 89. Beyond Appearance: Evidence-Guided Programmatic 3D Scene Reconstruction with Agentic Lighting Reasoning

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, memory, reasoning, spec
- 作者：Zeting Luo, Yifan Li, Shuai Yang
- 链接：[arXiv](https://arxiv.org/abs/2611.24565) · [PDF](https://arxiv.org/pdf/2611.24565) · [HF](https://huggingface.co/papers/2611.24565)

Image-to-code methods for 3D scene reconstruction produce executable code that generates editable digital content and supports visual simulation. However, existing methods primarily rely on appearance similarity, which provides limited guidance for distinguishing errors in geometry, materials, and illumination. Light shapes scene appearance through its interactions with geometry and materials, influencing shading,…

## 90. Large Language Models or AI Agents for English to Arabic Translation? An assessment on WikiEn-Ar190

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reasoning, language model, large language
- 作者：Fatima Zahra Iguenfer, Yousra Chtouki
- 链接：[arXiv](https://arxiv.org/abs/2611.24588) · [PDF](https://arxiv.org/pdf/2611.24588) · [HF](https://huggingface.co/papers/2611.24588)

This research investigates whether a large language model or an autonomous AI Agent performs better at translating from English to Arabic, which is considered a low-resource language. The authors introduce WikiEn-Ar190, a new dataset of 190 carefully selected Wikipedia articles from 18 different areas, which were created and verified by two native Arabic speakers to ensure that they accurately reflect both meaning…

## 91. Chain-of-Thought Hidden States Reveal Task-Solving Directions for Direct Answers

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, language model, large language, spec
- 作者：Houman Mehrafarin, Ioannis Konstas
- 链接：[arXiv](https://arxiv.org/abs/2611.24598) · [PDF](https://arxiv.org/pdf/2611.24598) · [HF](https://huggingface.co/papers/2611.24598)

Chain-of-Thought (CoT) prompting improves the performance of Large Language Models by eliciting intermediate reasoning steps. However, CoT is far from perfect: on some tasks, models perform worse than with direct-answer prompting, and on others they generate a few hundred tokens to reach the correct answer. We start by labelling each CoT hidden state as recovering if patching it into the direct prompt yields the…

## 92. GateWatch: Low-Overhead LLM Monitoring with Boolean Circuits

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, memory, language model, large language, spec
- 作者：Firas Spanioli, Yaniv David
- 链接：[arXiv](https://arxiv.org/abs/2611.24619) · [PDF](https://arxiv.org/pdf/2611.24619) · [HF](https://huggingface.co/papers/2611.24619)

As large language models (LLMs) and LLM-based agents are increasingly deployed, monitoring their behavior becomes important for detecting unsafe or unintended actions. Activation probes offer an efficient approach, but existing methods face trade-offs between accuracy, interpretability, and computational overhead. Probes on raw activations lack interpretable inputs, whereas sparse autoencoder (SAE) probes use…

## 93. Clover-35B-A3B-Preview Technical Report

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, memory, evaluation, language model
- 作者： DiffuSpace Technical Team
- 链接：[arXiv](https://arxiv.org/abs/2611.24636) · [PDF](https://arxiv.org/pdf/2611.24636) · [HF](https://huggingface.co/papers/2611.24636)

We introduce Clover-35B-A3B-Preview (Clover), a mixture-of-experts diffusion language model with 35 billion total parameters and 3 billion activated parameters, supporting thinking-mode generation. Clover adapts Gated Delta Networks to block diffusion by combining recurrent memory of previously generated context with bidirectional softmax attention inside the current block. Historical memory readout competes with…

## 94. Self-Rewarded Reinforcement Learning for Better-Structured Medical Explanations in Small Language Models

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, reinforcement learning, language model, large language
- 作者：Prakhar Mishra, Bhavya Yajush Awasthi,  Tanuja,  Nishant
- 链接：[arXiv](https://arxiv.org/abs/2611.24650) · [PDF](https://arxiv.org/pdf/2611.24650) · [HF](https://huggingface.co/papers/2611.24650)

Small language models (SLMs) can run on commodity hardware and support privacy-preserving, on-premises clinical deployment, but their medical explanations are often short and poorly structured compared with large language models. Recent supervised approaches such as Meerkat transfer chain-of-thought reasoning into 7B-8B backbones, yet their training objective does not directly target the style or organization of the…

## 95. Piccolo: Co-Evolving Decision Models and Data through Recursive Self-Improvement

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, memory, benchmark, spec
- 作者：Zhenqing Ling, Qirui Jiao, Daoyuan Chen, Cheng Chen, Xinji Mai, Haowen Gao, Zhuo Zhang, Xuchen Pan, Mengsu Ding, Jiaji Deng, Yuexiang Xie, Xiaoming Qin, Weirui Kuang, Zhaoyang Liu, Yaliang Li, Bolin Ding, Jingren Zhou
- 链接：[arXiv](https://arxiv.org/abs/2611.24651) · [PDF](https://arxiv.org/pdf/2611.24651) · [HF](https://huggingface.co/papers/2611.24651)

We present Piccolo, a family of multimodal decision models (0.8B to 27B) that coevolves model capabilities and training data via Agentic Data Engineering and recursive self-improvement (RSI). The models predict probabilities over candidate answers for general-purpose text and visual judgments, agent harnesses, data workflows, and interactive games. Piccolo-27B tops the Decision Index Vision Full leaderboard with a…

## 96. Depth Before Breadth: Reverse-to-Forward Curriculum with Advantage Decomposition for LLM Agent

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reinforcement learning, language model, large language, spec
- 作者：Siyuan Du, Yuxin Liu, Meng Tang, Haoran Li, Yechao Bai, Feiyang Pan, Jia He
- 链接：[arXiv](https://arxiv.org/abs/2611.24697) · [PDF](https://arxiv.org/pdf/2611.24697) · [HF](https://huggingface.co/papers/2611.24697)

Reinforcement learning (RL) has become a common approach for training large language model (LLM) agents on long-horizon tasks. However, learning from sparse terminal rewards makes credit assignment and exploration difficult. We approach these challenges through a policy-induced capability region, the set of states from which the current policy can reliably complete a task. Near its boundary, an agent may need only a…

## 97. Can Omni-modal LLMs Understand Spoken Intentions?

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, language model, large language, spec
- 作者：Zijie Xin, Tianyi Wang, Daoze Zhang, Jie Yang, Changli Tang, Qijie Wei, Fengyun Rao, Xirong Li
- 链接：[arXiv](https://arxiv.org/abs/2611.24706) · [PDF](https://arxiv.org/pdf/2611.24706) · [HF](https://huggingface.co/papers/2611.24706)

Omni-modal large language models (omni-modal LLMs) can respond to spoken requests directly through voice and video calls. Such requests rely on the scene shared by the user and the assistant, so the same utterance may call for different help or for no response. Most audio-visual benchmarks provide questions as separate text input, and interactive benchmarks mostly score a response as a whole. It thus remains unclear…

## 98. DRIFT: Detachable Reasoning for Runtime-Flexible and Efficient End-to-End Driving

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, benchmark, language model, planning
- 作者：Emad Aghajanzadeh, Bethany Anne Wong, Leonhard Kunze, Moritz Thoma, Maximilian Forstenhäusler, Nael Fasfous, Manoj Rohit Vemparala, Pierpaolo Mori, Christos Anagnostopoulos, Daniel Mueller-Gritschneder, Ulf Schlichtmann
- 链接：[arXiv](https://arxiv.org/abs/2611.24719) · [PDF](https://arxiv.org/pdf/2611.24719) · [HF](https://huggingface.co/papers/2611.24719)

The integration of vision-language models (VLMs) into end-to-end (E2E) autonomous driving has demonstrated strong potential by providing scene description and reasoning capabilities. However, VLMs are computationally expensive, and switching language reasoning on and off at runtime without hurting closed-loop performance has not been demonstrated, which hinders practical adoption. To address these issues, we propose…

## 99. A$^3$Bench: Compositional Reasoning over Aggressive Interactions in Videos

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, benchmark, language model, large language
- 作者：Austin C Baker, Raiyaan Abdullah, Daniel Zeev Yoffe, Shruti Vyas, Yogesh S Rawat
- 链接：[arXiv](https://arxiv.org/abs/2611.24762) · [PDF](https://arxiv.org/pdf/2611.24762) · [HF](https://huggingface.co/papers/2611.24762)

Recent Multimodal Large Language Models (MLLMs) have achieved strong performance on general video understanding benchmarks, yet their ability to reason about participant roles in aggressive interactions remains largely unexplored. Existing violence and crime datasets primarily evaluate whether aggression occurs, without testing whether models can identify who performed the action, who received it, and how…

## 100. LLM-Guided Cyber-Physical Attack Path Identification in Smart Grids

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, evaluation, language model, large language
- 作者：Amr Elshazly, Jesse Roberts, Rachad Atat, Muhammad Ismail
- 链接：[arXiv](https://arxiv.org/abs/2611.24765) · [PDF](https://arxiv.org/pdf/2611.24765) · [HF](https://huggingface.co/papers/2611.24765)

Identifying high-impact attack paths in cyber-physical power systems is critical for improving grid resilience. Existing methods typically rely on either structural topology analysis or simulation-based cascading-failure models. Topology-based approaches capture connectivity but lack adversarial reasoning, while simulation-driven methods are primarily suited for offline analysis and are less effective for rapid…

## 101. Ultimate3D: Teaching Multimodal LLMs 3D Camera-Object Relations by Large-Scale Visual Instruction Data

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, language model, large language, spec
- 作者：Liu He, Yizhi Song, Ruiqi Xu, Baris Sarper Tezcan, Xiao Zeng, Albert Y. C. Chen, Lu Xia, Shashwat Verma, Sankalp Dayal, Min Sun, Cheng-Hao Kuo, Daniel Aliaga
- 链接：[arXiv](https://arxiv.org/abs/2611.24795) · [PDF](https://arxiv.org/pdf/2611.24795) · [HF](https://huggingface.co/papers/2611.24795)

Multimodal Large Language Models (MLLMs) struggle with accurately capturing camera-object relations, especially for object orientation, camera viewpoint, and camera shots. This stems from the fact that existing MLLMs are trained on images with limited diverse camera-object relations and corresponding textual descriptions. To address this, we propose a synthetic generation pipeline to create large-scale 3D visual…

## 102. Kaer: Security-Aware Replanning for Multi-Agent Systems

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, benchmark, spec, planning
- 作者：Tushin Mallick, Evan Rose, Matthew Laws, Alina Oprea, Cristina Nita-Rotaru
- 链接：[arXiv](https://arxiv.org/abs/2611.24839) · [PDF](https://arxiv.org/pdf/2611.24839) · [HF](https://huggingface.co/papers/2611.24839)

One popular architecture for multi-agent systems (MAS) relies on an orchestrator that generates an initial plan, coordinates its execution, and dynamically revises the plan based on agent feedback when tasks cannot be fully specified in advance. This dynamic replanning introduces a critical vulnerability: malicious agents can embed instructions within their feedback to hijack the replanning process. Existing…

## 103. Atomic MathReasoner: Instance-Level Composition of Atomic Reasoning Skills for Mathematical LLMs

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, benchmark, language model, large language, spec
- 作者：Jiashu Li, Tianyu Gao, Qinglong Liu, Jinping Wang, Ye Wei, Zhiqiang Gao
- 链接：[arXiv](https://arxiv.org/abs/2611.24846) · [PDF](https://arxiv.org/pdf/2611.24846) · [HF](https://huggingface.co/papers/2611.24846)

Most existing approaches enhance mathematical reasoning in large language models (LLMs) as a monolithic capability, despite the fact that different mathematical problems require different reasoning skills. Recent work has explored a more fine-grained perspective by decomposing mathematical reasoning into atomic skills and developing specialized modules for individual capabilities. However, how to effectively utilize…

## 104. Can Programs Replace LLM Judges? Executable Program Judges for Scalable and Efficient Relevance Labeling

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, language model, large language, spec, retrieval
- 作者：Eugene Agichtein, Charles L. A. Clarke, Kaustubh Dhole, William Stern
- 链接：[arXiv](https://arxiv.org/abs/2611.24849) · [PDF](https://arxiv.org/pdf/2611.24849) · [HF](https://huggingface.co/papers/2611.24849)

Large language model (LLM) judges have become a common way to create large-scale relevance judgments for retrieval evaluation. However, each judgment requires a potentially expensive call to a frontier model, and the judgments are hard to interpret and may not be reproducible. In this paper, we ask whether an LLM can write a readable program for each topic that replaces its per-document judgments. To address these…

## 105. Ground, Iterate, Trace: Decomposing AI Research Ideation

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, benchmark, language model, large language, spec, retrieval
- 作者：Samson Yu, Qiran Zou, Jing Yu Lim, Rushi Shah, Anirudh Goyal, Dianbo Liu
- 链接：[arXiv](https://arxiv.org/abs/2611.24887) · [PDF](https://arxiv.org/pdf/2611.24887) · [HF](https://huggingface.co/papers/2611.24887)

Large language models have been widely used to generate plausible research ideas, yet it remains unclear what makes automated ideation effective and how generated novel proposals arise from prior scientific work. We introduce the Creative AI Researcher (CAR), an agentic framework combining literature grounding, iterative development and explicit conceptual operators. CAR constructs a semantic knowledge graph from…

## 106. Who are you? The Personal Imitation Game

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, language model, large language, spec
- 作者：Muhammad Rizky Wellyanto, Hajara-Yasmin Isa, Kexin Xue, Vishal Ravichandran, Wenpeng Lu, Jerry O. Talton, Ranjitha Kumar
- 链接：[arXiv](https://arxiv.org/abs/2611.24888) · [PDF](https://arxiv.org/pdf/2611.24888) · [HF](https://huggingface.co/papers/2611.24888)

Large Language Models (LLMs) now perform strongly on Alan Turing's 1950 Imitation Game, so we propose a harder challenge, the Personal Imitation Game, which asks whether a machine can replicate a specific individual in conversation rather than a generic human. Testing with 30 participants, we establish a human baseline and report the identity signals interrogators rely on: stylometric features, personality traits,…

## 107. PrismRestore: A Compact Restoration Toolbox for Agentic Image Restoration

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, evaluation, benchmark, spec
- 作者：Zhaocheng Yu, Kui Jiang, Jing Cao, Yiang Chen, Xiaocheng Feng, Junjun Jiang, Xianming Liu
- 链接：[arXiv](https://arxiv.org/abs/2611.24915) · [PDF](https://arxiv.org/pdf/2611.24915) · [HF](https://huggingface.co/papers/2611.24915)

Agentic image restoration composes operations to handle mixed degradations, yet its toolbox often requires storing multiple restoration networks. We propose PrismRestore, which constructs a compact bank of callable restoration actions from a single frozen all-in-one model. Our approach builds on task-dependent yet overlapping channel responses in the shared model. An offline task-prior search uses activation and…

## 108. Agentic Harness Engineering Beta: Requirement-Centered Evolution of Agent Harnesses

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, evaluation, benchmark, spec
- 作者：Jiahang Lin, Jiahao Chen, Yiding Wang, Shichun Liu, Chengjun Pan, Shihan Dou, Honglin Guo, Yuyang Hu, Changhao Jiang, Zhenhua Han, Hang Yan, Qi Zhang, Tao Gui, Xuanjing Huang
- 链接：[arXiv](https://arxiv.org/abs/2611.24924) · [PDF](https://arxiv.org/pdf/2611.24924) · [HF](https://huggingface.co/papers/2611.24924)

Real-world harness engineering is driven by explicit and implicit user requirements, which guide development and validation. However, existing harness evolution methods often overlook implicit requirements and interaction needs, while using a single evolution agent to modify the harness and benchmark scores to select changes. This process often produces narrow patches and leads to benchmark-specific local optima. We…

## 109. Jailbreak Detection on Large Language Models via Contrastive Prototype Structures

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, language model, large language, spec
- 作者：Yan Qiu, Yuanyuan Li
- 链接：[arXiv](https://arxiv.org/abs/2611.24936) · [PDF](https://arxiv.org/pdf/2611.24936) · [HF](https://huggingface.co/papers/2611.24936)

Jailbreak attempts and harmful prompts remain a challenge for the safe deployment of large language models. We study whether contrastively learned representations can support safety detection without training an additional downstream classifier. We propose Jailbreak Detection with Prototype Inference (JDPI), which uses binary safety labels to construct harmful and benign prototypes and makes predictions from…

## 110. PatchAdaNet: Unsupervised class incremental learning using local patches and global adapters

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, evaluation, spec
- 作者：Kamel Aouaidjia, Yanchao Duan, Zihui Zhen, Xin Li, Yongfei Lv, Chongsheng Zhang
- 链接：[arXiv](https://arxiv.org/abs/2611.24137) · [PDF](https://arxiv.org/pdf/2611.24137) · [HF](https://huggingface.co/papers/2611.24137)

Biological learning systems acquire knowledge incrementally through broad, reusable representations established early and kept largely stable, while integrating new experience with minimal interference with previously learned knowledge. Replay-based methods approximate this by storing samples or features from previous tasks and mixing them into the current task. However, memory buffers grow with the number of tasks…

## 111. AVTR: Adaptive Multimodal Reasoning with Visual Imagination

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, benchmark, language model
- 作者：Xiaoqian Shen, Yunyang Xiong, Changsheng Zhao, Saksham Suri, Chong Zhou, Zechun Liu, Zhipeng Cai, Zhuang Liu, Qi Qian, Wei Wen, Hongyu Xu, Hanxian Huang, Ernie Chang, Yanbei Chen, Vikas Chandra, Raghuraman Krishnamoorthi, Mohamed Elhoseiny, Lemeng Wu
- 链接：[arXiv](https://arxiv.org/abs/2611.24161) · [PDF](https://arxiv.org/pdf/2611.24161) · [HF](https://huggingface.co/papers/2611.24161)

Vision-Language Models increasingly rely on textual reasoning to solve advanced multimodal tasks. Despite its effectiveness, this paradigm faces two fundamental limitations. First, relying on textual reasoning alone can limit perceptual ability in vision-centric questions, where accurate answers depend on interpreting task-relevant visual evidence. Second, applying textual reasoning uniformly across inputs overlooks…

## 112. From Neural Tokens to Language: Dual-View EEG Semantic Bridging for Brain-to-Text Generation

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：language model, large language, spec
- 作者：YaoYang Liu, Jun Dai, ZhuoShi Tang, Weijun Sun, Xiaozhao Fang, Jie Wen
- 链接：[arXiv](https://arxiv.org/abs/2611.24197) · [PDF](https://arxiv.org/pdf/2611.24197) · [HF](https://huggingface.co/papers/2611.24197)

Visually evoked EEG-to-text generation aims to produce natural-language descriptions from neural responses elicited by visual stimuli. Existing approaches typically compress EEG signals into a single global representation and directly project it into the hidden space of a large language model (LLM), which may limit the preservation of complementary visual semantics under noisy and subject-dependent EEG signals. We…

## 113. GALA: Gallery-Level Alignment for Real-Life Vision Decoding from EEG

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, coding
- 作者：Philippe Forest, Giulia Lioi, Mai Pham Quyen, Alix Lamouroux, Javen Shi, Adrien Merlini
- 链接：[arXiv](https://arxiv.org/abs/2611.24206) · [PDF](https://arxiv.org/pdf/2611.24206) · [HF](https://huggingface.co/papers/2611.24206)

Neural decoding of visual experience from electroencephalography (EEG) has achieved strong performance in intra-subject settings, but current methods fail to generalize across individuals: on the standard 200-way benchmark THINGS-EEG-2, top-1 accuracy drops from above 80% within subjects to about 32% for an unseen subject. Adapting a pre-trained encoder to new subjects and sessions typically requires labeled data, a…

## 114. Target-Consistent Action Guidance via Semi-Unbalanced Optimal Transport for Drifting World Models

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, planning
- 作者：Md Abtahi Majeed Chowdhury, Md Rifat Ur Rahman, Md Sakib Hossain Shovon, Jaesik Choi, Minhyuk Sung
- 链接：[arXiv](https://arxiv.org/abs/2611.24222) · [PDF](https://arxiv.org/pdf/2611.24222) · [HF](https://huggingface.co/papers/2611.24222)

Action-conditioned world models let robots imagine the outcomes of their actions for planning and offline policy evaluation, but these uses need many rollouts, which multi-step diffusion makes expensive. Drifting models move the iteration from inference to training and generate samples in one network pass. DriftWorld brought this paradigm to action-conditioned world models; to strengthen action following, it repels…

## 115. What Survives the Shift from Text to Pixels? Conditional Protection against Prompt Injection in Image-Rendered Documents

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, language model, coding
- 作者：Haoyang Liu, Yinong Xu, Zhe Lang, Zhenyu Guan, Qianyun Zhang
- 链接：[arXiv](https://arxiv.org/abs/2611.24231) · [PDF](https://arxiv.org/pdf/2611.24231) · [HF](https://huggingface.co/papers/2611.24231)

Multimodal language models increasingly answer questions over external documents, exposing them to indirect prompt injection: commands planted in untrusted content to hijack the response. Rendering untrusted content as page images lowers attack success on average, leaving open which injected operations survive rendering, at what utility cost, and whether failed image attacks reflect unread commands or commands read…

## 116. Allocentric Memory, Egocentric Acting: A Dual-Frame VLA for Urban Aerial Navigation

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, reasoning, spec
- 作者：Haotian Xu, Yue Hu, Zhengqiu Zhu, Tuo Feng, Wenguan Wang, Quanjun Yin
- 链接：[arXiv](https://arxiv.org/abs/2611.24247) · [PDF](https://arxiv.org/pdf/2611.24247) · [HF](https://huggingface.co/papers/2611.24247)

Language-goal aerial navigation requires a UAV to reach a destination specified in natural language using observations collected during flight. A key challenge is linking changing egocentric perception with spatial evidence anchored to stable locations for long-range navigation. We propose CityNav-VLA, a dual-frame vision-language-action model for urban navigation integrating dynamic egocentric context with…

## 117. Look Closer, Look Back, or Wait for Agentic Streaming Video Understanding

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, memory, benchmark
- 作者：Pengyu Li, Zhitao Gao, Lingling Zhang, Wenxuan Huang, YiCheng Xiao, Chen Zheng, Jun Liu
- 链接：[arXiv](https://arxiv.org/abs/2611.24267) · [PDF](https://arxiv.org/pdf/2611.24267) · [HF](https://huggingface.co/papers/2611.24267)

Streaming video models must answer questions about a live video under strict memory and latency limits. Feeding only the latest few frames keeps present perception sharp, whereas adding past frames dilutes attention on the current scene and triggers hallucinations. Recent cascade methods retrieve past frames when uncertain, but they still fail when current frames are blurry or when decisive future clues have not…

## 118. LoopCache: Accelerating Long-Context Self-Speculative Decoding for Looped Transformers

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, coding, spec
- 作者：Zizhuo Fu, Haochen Huang, Shengxuan Qiu, Linye Wei, Ziyu Tang, Runsheng Wang, Meng Li
- 链接：[arXiv](https://arxiv.org/abs/2611.24301) · [PDF](https://arxiv.org/pdf/2611.24301) · [HF](https://huggingface.co/papers/2611.24301)

Looped Transformers achieve large effective depth with compact models by repeatedly applying a weight-shared block across R recurrent steps, each maintaining a loop-specific key-value (KV) cache. To accelerate sequential loop execution, recent wave-style self-speculative methods like WaveFront Decoding (WFD) and LoopSpec pipeline draft and target tokens across loops in a single step. However, they face two critical…

## 119. AutoPI: Taxonomy-Guided Adaptive Red Teaming for Prompt Injection in LLM Agents

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, evaluation, benchmark
- 作者：Stavros Damianakis, Konstantinos Psounis
- 链接：[arXiv](https://arxiv.org/abs/2611.24313) · [PDF](https://arxiv.org/pdf/2611.24313) · [HF](https://huggingface.co/papers/2611.24313)

Prompt injection is the dominant unsolved security risk for LLM agents, and the community now agrees that robustness must be measured against adaptive attackers rather than fixed benchmark injections. Many adaptive red teamers exist, and most are built to maximize attack success rate (ASR). Yet ASR counts how often a target breaks, not in how many different ways. A red teamer can achieve a high ASR by reusing a few…

## 120. Benchmarking LLM abilities on postdoc-level natural science problems

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, benchmark, spec
- 作者：Alina Avanesyan, Alexey Boldyrev, Liqun Deng, Denis Derkach, Mary Godunova, Mikhail Hushchyn, Dmitry Ilvovsky, Irina Knyazeva, Irina Piontkovskaya, Dmitry Polubotko, Fedor Ratnikov, Ekaterina Trofimova, Zhenhe Zhang
- 链接：[arXiv](https://arxiv.org/abs/2611.24321) · [PDF](https://arxiv.org/pdf/2611.24321) · [HF](https://huggingface.co/papers/2611.24321)

Scientific problems have no answer key, so evaluating an agent means deciding what counts as a better solution before any agent is run. Existing benchmarks either match a symbolic answer against a key or, where they require executable work, score it by unit tests, by a rubric, or by position on a competition leaderboard. None of these is the criterion by which a field decides that one published method beats another.…
