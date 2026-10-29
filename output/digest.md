# 每日 AI 论文

生成时间：2026-10-29 05:49 UTC  ·  共 120 篇（已按 arXiv ID 去重）

来源：Hugging Face Daily Papers + arXiv（cs.AI / cs.LG / cs.CL / cs.CV）。
排序：HF 上榜、点赞、多源命中、兴趣词。兴趣词可在 `config.json` 改。

## 1. CodeCap-Bench: Can Code Serve as a Good Video Caption?

- 分数：40.0  ·  HF 赞：48  ·  来源：huggingface + arxiv
- 兴趣命中：reasoning, evaluation, language model, large language
- 作者：Jiafu Tang, Yifan Xu, Eric Tang, Junjie Zhao, Shipeng Luo, Te Sun, Haoxuan Hu, Yiyan Ji, Xinlong Chen, Zihao Wang, Yang Shi, Yuanxing Zhang, Pengfei Wan, Jiaheng Liu
- 链接：[arXiv](https://arxiv.org/abs/2610.37341) · [PDF](https://arxiv.org/pdf/2610.37341) · [HF](https://huggingface.co/papers/2610.37341)

Video captioning aims to preserve visual information through compact descriptions, predominantly using natural language. However, precisely expressing fine-grained spatial structures and temporal dynamics in natural language often leads to lengthy and potentially ambiguous descriptions. In this work, we explore Code as Video Caption, a paradigm where executable programs serve as a complementary representation of…

## 2. The Trinity:Capability-Driven Recursive Self-Improvement for Multimodal Agents

- 分数：36.0  ·  HF 赞：535  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark, spec
- 作者：Weidong Tang, Ruiheng Wang, Jingxuan Zhang, Hexin Wang, Haoyuan Chen, Zhengfeiyang Zhang, Yixing Ma, Zichen Jiang, Ziyu Guo, Haodong Li, Zhengbo Jiao, Zhiqing Cui, Xinxiang Yin, Shuo Liang, Zhenglin Wan, Hongzhan Lin, Wangbo Zhao Kaipeng Zhang, Pengfei Zhou, Odin Zhang, Yang You
- 链接：[arXiv](https://arxiv.org/abs/2610.36077) · [PDF](https://arxiv.org/pdf/2610.36077) · [HF](https://huggingface.co/papers/2610.36077)

Multimodal intelligence can be viewed as human-guided co-evolution between worlds and agents through interaction. However, scaling this process faces two bottlenecks: constructing heterogeneous, verifiable environments is costly, and manual Harness iteration cannot keep pace with growing task diversity and complexity. A key insight is that tasks with different modalities and surface forms can share the same…

## 3. VibeVideoBench: Evaluating Multimodal Agents on Code-Driven Video Generation

- 分数：36.0  ·  HF 赞：173  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark, spec
- 作者：Muxi Diao, Wenbin Xu, Lele Yang, Xuyang Ma, Yuzhe Chen, Jiankang Chen, Kaiyu Jiang, Changyi Liu, Haoyu Zhang, Hongyi Fu, Jianxiong Wang, Tianke Zhang, Haonan Fan, Yingxin Li, Bingyi Li, Xu Wang, Xuanyu Zheng, Bin Wen, Tingting Gao, Han Li, Wentao Zhang, Weiran Xu, Kongming Liang, Zhanyu Ma
- 链接：[arXiv](https://arxiv.org/abs/2610.35864) · [PDF](https://arxiv.org/pdf/2610.35864) · [HF](https://huggingface.co/papers/2610.35864)

Diffusion video models produce striking clips, but they cannot reliably render an exact formula, a correct chart, a rule-consistent game or narration synchronized to on-screen events. A different route is emerging: multimodal agents that write code to render every frame and synthesize every sound. We introduce VibeVideoBench, a benchmark for evaluating agents on code-driven video generation. Its 239 self-contained…

## 4. Memory Tax: Dissecting the Net Value of Agent Memory

- 分数：36.0  ·  HF 赞：146  ·  来源：huggingface
- 兴趣命中：agent, memory, evaluation, benchmark, retrieval
- 作者：Xuan He, Sining Zhoubian, Ruozhen Yang, Yuhao Wen, Zhineng Wang, Yuyang Hu, Ke Yang, Yuyu Zhang, Ping Nie, Jiawei Han, ChengXiang Zhai
- 链接：[arXiv](https://arxiv.org/abs/2610.34073) · [PDF](https://arxiv.org/pdf/2610.34073) · [HF](https://huggingface.co/papers/2610.34073)

Memory is increasingly used in long-horizon agents, yet the net value of building memory over direct retrieval from raw history remains largely unclear. Through a large-scale evaluation across multiple benchmarks and model backbones, we find many dedicated memory systems underperform naive RAG in many cases, indicating a negative net value. Taking RAG as a reference, we dissect the net value of memory into the gains…

## 5. Can Test-Time Memory Evolution Outperform Test-Time Training for Scientific Discovery?

- 分数：36.0  ·  HF 赞：110  ·  来源：huggingface
- 兴趣命中：memory, evaluation, language model, large language
- 作者：Yepeng Liu, Shengmai Chen, Xuandong Zhao, Chengzhi Liu, Dawn Song, Xin Eric Wang, Yuheng Bu
- 链接：[arXiv](https://arxiv.org/abs/2610.32046) · [PDF](https://arxiv.org/pdf/2610.32046) · [HF](https://huggingface.co/papers/2610.32046)

Recent test-time training (TTT) frameworks have enabled open-weight large language models (LLMs) to outperform inference-only frameworks powered by frontier models on scientific discovery tasks. However, TTT introduces additional computational cost for online weight updates during the discovery process, making computational efficiency an important consideration when scaling to larger models. This motivates us to…

## 6. HABIT-Bench: Evaluating Habit Induction from Longitudinal Weak Evidence in Agent Memory

- 分数：36.0  ·  HF 赞：80  ·  来源：huggingface
- 兴趣命中：agent, memory, language model, large language
- 作者：Junming Zhang, Rubin Wei, Xu Cheng, Hao Sun, Jiarui Wang, Ruoxi Cheng, Xiquan Wang, Peisong Wu, Mingsong Chen, Zhouhan Lin
- 链接：[arXiv](https://arxiv.org/abs/2610.24520) · [PDF](https://arxiv.org/pdf/2610.24520) · [HF](https://huggingface.co/papers/2610.24520)

In long-term interactions with large language model (LLM) agents, users reveal habits through their choices and actions. These habits capture implicit user information that agents must infer across conversations. However, individual observations may provide only partial evidence about a habit or when it applies. Retaining past interactions alone does not ensure that agents can infer habits and apply them…

## 7. ThinkWorld: World Imagination Reinforces Chain-of-Dynamics Reasoning

- 分数：36.0  ·  HF 赞：49  ·  来源：huggingface + arxiv
- 兴趣命中：reasoning, reinforcement learning
- 作者：Chaehyun Kim, Chi-Pin Huang, Jisoo Kim, Min-Hung Chen, Yu-Chiang Frank Wang, Seungryong Kim, Fu-En Yang
- 链接：[arXiv](https://arxiv.org/abs/2610.37666) · [PDF](https://arxiv.org/pdf/2610.37666) · [HF](https://huggingface.co/papers/2610.37666)

Vision-Language-Action (VLA) models have made substantial progress in robotic manipulation, but their generalization remains constrained by the diversity and coverage of action-labeled robot demonstrations. Human videos provide much broader behavioral and environmental experience, while learning from them faces a fundamental trade-off between scalable data and explicit action grounding. We introduce ThinkWorld, a…

## 8. DTCA: Denoising Token Credit Assignment for Reinforcement Learning in Diffusion Language Models

- 分数：34.0  ·  HF 赞：254  ·  来源：huggingface
- 兴趣命中：reasoning, reinforcement learning, language model
- 作者：Hongze Chen, Miao Pan, Lizhou Liang, Qinfeng Li, Xinyin Ma, Yongliang Shen, Weishi Wang, Daniel Dahlmeier, Xuhong Zhang, Wenqi Zhang
- 链接：[arXiv](https://arxiv.org/abs/2610.35201) · [PDF](https://arxiv.org/pdf/2610.35201) · [HF](https://huggingface.co/papers/2610.35201)

Diffusion language models (DLMs) generate text through iterative denoising, enabling bidirectional context modeling and parallel token refinement. Recent studies have applied reinforcement learning (RL) to DLMs and improved their reasoning performance. However, the iterative denoising process makes credit assignment more challenging, as final outcome rewards provide limited information about how different tokens…

## 9. PDRVLA: A Vision-Language-Action Model with Physical Dynamics Representations

- 分数：34.0  ·  HF 赞：141  ·  来源：huggingface + arxiv
- 兴趣命中：benchmark
- 作者：Hanqing Wang, Zhaotian Cai, Ruichuan An, Bohan Zeng, Tao Zhang, Yilin Chen, Xu Jiang, Kaiquan Chen, Chongyang Wu, Haoran Li, Fan Yang, Mingan Lin, Wentao Zhang, Zenan Zhou, Youzheng Wu
- 链接：[arXiv](https://arxiv.org/abs/2610.37381) · [PDF](https://arxiv.org/pdf/2610.37381) · [HF](https://huggingface.co/papers/2610.37381)

Vision--Language--Action (VLA) models generate robot actions from visual observations and language instructions, but their understanding of physical dynamics remains limited. Video world models can capture scene dynamics, yet generating future videos introduces high latency into the control loop. We introduce PDRVLA, whose lightweight Physical Dynamics Module extracts physical tokens from vision--language features…

## 10. Can Discrete Tokens Serve as Semantically Lossless Representations of Visual Signals?

- 分数：34.0  ·  HF 赞：83  ·  来源：huggingface + arxiv
- 兴趣命中：spec
- 作者：Jialv Zou, Xiaotong Li, Zhengrong Yue, Xu Huang, Yaxin Luo, Wenhao Yan, Haodong Li, Wenyu Liu, Xinggang Wang
- 链接：[arXiv](https://arxiv.org/abs/2610.37662) · [PDF](https://arxiv.org/pdf/2610.37662) · [HF](https://huggingface.co/papers/2610.37662)

Discrete visual tokens represent vision in a discrete form analogous to language, offering a native interface for multimodal modeling under a shared next-token prediction objective. However, quantization error is widely assumed to cause unavoidable semantic loss, fundamentally limiting the semantic fidelity of discrete visual tokens and positioning continuous visual representations as an intrinsic upper bound. Using…

## 11. Multiscale Policy Optimization for Long-Horizon LLM Agents

- 分数：32.0  ·  HF 赞：375  ·  来源：huggingface
- 兴趣命中：agent, tool-use
- 作者：Tao Ren, Hui Yang, Jia Deng, Tingyang Chen, Qiyao Wang, Shuo Tang, Ziyang Zeng, Yuhua Jiang, Guanghao Li, Huatong Song, Yining Li, Yifan Luo, Kunbao Ding, Feng Chang, Chuan Hao, Ran Tao, Bryan Dai, Jiafeng Liang, Jinyang Jiang
- 链接：[arXiv](https://arxiv.org/abs/2610.35013) · [PDF](https://arxiv.org/pdf/2610.35013) · [HF](https://huggingface.co/papers/2610.35013)

Long-horizon LLM agents interact with their environments through complete assistant turns while generating each action token by token. We observe that critic values vary primarily across turns, motivating optimization anchored at turns with finer credit allocation among tokens. We propose Multiscale Policy Optimization (MPO), combining Multiscale Advantage Estimation (MAE) and turn-level importance sampling to align…

## 12. ChronoReplay: One Answer Interface Is Not Enough for Streaming Spatial Intelligence

- 分数：32.0  ·  HF 赞：354  ·  来源：huggingface
- 兴趣命中：benchmark, spec
- 作者：Yihao Hu, Yitong Lin, Pan Wang, Zhihao Wen, Hang Wang, Yiwen Zhao, Deyuan Liu, Yutong Li, Mingda Wan, Yuchen Mao, Tao Lin
- 链接：[arXiv](https://arxiv.org/abs/2610.34283) · [PDF](https://arxiv.org/pdf/2610.34283) · [HF](https://huggingface.co/papers/2610.34283)

Training a spatial VLM to answer which side an object lies on does not require it to preserve the metric displacement that determines that answer, while supervision for a distance estimate may leave categorical relations largely unconstrained. When post-training emphasizes one readout, improvements can therefore concentrate on that interface while transfer to others remains weak or even degrades; we call this…

## 13. Efficient Streaming Audio-Visual Target Speaker Extraction for Real-World Acoustic Scenes

- 分数：32.0  ·  HF 赞：122  ·  来源：huggingface
- 兴趣命中：evaluation, benchmark
- 作者：Wendi Sang, Kai Li, Yifan Li, Jianqiang Huang, Xiaolin Hu
- 链接：[arXiv](https://arxiv.org/abs/2610.32749) · [PDF](https://arxiv.org/pdf/2610.32749) · [HF](https://huggingface.co/papers/2610.32749)

Streaming audio-visual target speaker extraction (AVTSE) is essential for latency-sensitive applications. However, current causal systems face two coupled gaps. First, standard benchmarks fix the number of speakers at two and ignore the near-/far-field interference, reverberation, and sudden noise of real scenes. Second, high-performance causal architectures are too heavy for edge deployment. Lightweight…

## 14. Hy-Nomas: Towards Free-form Interactive World Generation

- 分数：32.0  ·  HF 赞：108  ·  来源：huggingface
- 兴趣命中：evaluation, benchmark
- 作者：Qiaoling Chen, Jiaxiang Cheng, Xueqing Deng, Tiankai Hang, Ji Hou, Jiaqi Li, Yifan Liu, Tao Lu, Junshu Tang, Yu Tang, Yao Teng, Yu Tian, Heng Wang, Weizhi Wang, Xiyao Wang, Xilun Wu, Mingyu Yang, Yangbin Yu, Rui Zhao, Longjun Cao, Linghao Chen, Haoyi Duan, Jiaming Han, Mingji Han, Enhua Jiang, Shunkai Li, Yanzhe Liang, Qinwei Ma, Cong Wang, Lei Wang, Bing Wu, Ke Xing, Ray Ying, Zhentao Yu, Key Zhang, Yuan Zhou, Zhengguang Zhou, Kai Zou
- 链接：[arXiv](https://arxiv.org/abs/2610.36729) · [PDF](https://arxiv.org/pdf/2610.36729) · [HF](https://huggingface.co/papers/2610.36729)

Interactive world generation requires models to follow successive commands while preserving relevant history and action consequences. We present Hy-Nomas, a video world model with an 8B diffusion backbone that supports free-form text instructions and continuous camera control across multiple interaction turns. It generates variable-length segments conditioned on current inputs and cached history. Our central design…

## 15. LociArt: A Unified Paradigm for Free-Style Local Video Stylization

- 分数：31.0  ·  HF 赞：34  ·  来源：huggingface
- 兴趣命中：evaluation, benchmark, spec
- 作者：Yuxuan Chen, Feng Xie, Jiagao Hu, Fuhao Li, Zepeng Wang, Fei Wang, Daiguo Zhou
- 链接：[arXiv](https://arxiv.org/abs/2610.36456) · [PDF](https://arxiv.org/pdf/2610.36456) · [HF](https://huggingface.co/papers/2610.36456)

Video stylization typically transforms entire scenes, while local artistic editing requires precise region--style association, spatial control, and temporal consistency. We introduce LociArt, a unified paradigm for free-style local video stylization that explicitly specifies where to stylize and what style to apply while preserving non-target content. At its core, GRNStyle builds on Generative Refinement Networks…

## 16. Rollback: Experience Backtracking in World Models for Policy Improvement

- 分数：30.0  ·  HF 赞：61  ·  来源：huggingface
- 兴趣命中：spec
- 作者：Jiayi Luo, Yang Zhang, Liliang Chen, Nan Wang, Chen Gao, Boxiang Qiu, Zhuoxuan Li, Baorui Peng, Chuankang Li, Yuxiang Yan, Si Liu, Qingyun Sun, Shuicheng Yan, Maoqing Yao, Jianxin Li, Guanghui Ren
- 链接：[arXiv](https://arxiv.org/abs/2610.36068) · [PDF](https://arxiv.org/pdf/2610.36068) · [HF](https://huggingface.co/papers/2610.36068)

Action-conditioned world models offer a scalable alternative to costly real-world interaction for improving robot policies. However, existing world-model-based methods largely treat world models as forward-only surrogates of the physical environment, leaving untapped a capability no physical environment affords: rewinding to past decision points to explore counterfactual futures. We introduce Rollback, a policy…

## 17. Zooming without Zooming v2: From Seeing Details to Connecting Evidence for Generalizable Multimodal Perception

- 分数：29.5  ·  HF 赞：23  ·  来源：huggingface + arxiv
- 兴趣命中：agent, reasoning, benchmark
- 作者：Lai Wei, Yatai Li, Liangbo He, Jun Lan, Renjie Gu, Linhan Cao, Junkai Lin, Huijia Zhu, Weiqiang Wang, Linghe Kong, Yue Wang, Zhuosheng Zhang, Weiran Huang
- 链接：[arXiv](https://arxiv.org/abs/2610.37037) · [PDF](https://arxiv.org/pdf/2610.37037) · [HF](https://huggingface.co/papers/2610.37037)

Multimodal perception forms the foundation of multimodal intelligence. In particular, spatial perception and multimodal long-context understanding are two pivotal tasks that underpin embodied AI and multimodal agents. However, synthesizing targeted, high-quality training data for these tasks remains difficult and costly. Our key insight is that these tasks share an underlying capability, which we call connecting…

## 18. EmbeddingGemma 2: Unified and Efficient Multimodal Representations

- 分数：27.5  ·  HF 赞：19  ·  来源：huggingface + arxiv
- 兴趣命中：evaluation, benchmark, spec
- 作者：Henrique Schechter Vera, Sahil Dua, Jovan Andonov, Sara Smoot, Sebastian Russo, Ivan Llanos, Max Matveev, Jae Hyeon Yoo, Kat Black, Shih-Cheng Huang, Josiah Aklilu, Maarten Grootendorst, Omar Sanseviero, Chandramouli Amarnath, Ian Ballantyne, Zhe Li, Daniel Salz, Ibrahim Alabdulmohsin, Ilya Philippov, Kristen Quan, Glenn Cameron, Edouard Yvinec, Luciano Martins, Doug Reid, Sindhu Raghuram Panyam, Weiyi Wang, Hengxuan Ying, Madhuri Shanbhogue, Tanmaya Dabral, Shanfeng Zhang, Juyeong Ji, Renjie Wu, Joe Zou, Xu Chen, Yunan Zhang, Yu-Hui Chen, Matthew Soulanille, Vinod Mamillapalli, Yi-Chun Kuo, Wai Hon Law, Matt Kreileder, Alice Zheng, Suril Shah, Mogan Shieh, Pooja Consul, Alberto Montes, Andreas Hess, Andres Sevilla, Babak Samari, Brendan McCloskey, Brian Potetz, Daniel Cer, Georgios Kathareios, Gustavo Hernández Ábrego, Hesen Zhang, Ji Ma, Jiaxing Wu, Keegan Mosley, Paul Suganthan, Rui Meng, Shen Gao, Shengcao Cao, Yi-Ting Chen, Yichang Chen, Zhongli Ding, Kendra Byrne, Cormac Brick, Olivier Lacombe, Qin Yin, Tris Warkentin, Armand Joulin, Tom Duerig, Mojtaba Seyedhosseini
- 链接：[arXiv](https://arxiv.org/abs/2610.37364) · [PDF](https://arxiv.org/pdf/2610.37364) · [HF](https://huggingface.co/papers/2610.37364)

We present EmbeddingGemma 2, an open multimodal embedding model which natively represents text, images, audio, video, and combinations thereof in a unified space. Our approach introduces improvements such as simplified per-layer embeddings and a multi-stage curriculum with modality and objective progression which ensure strong quality across unimodal, cross-modal, and mixed-modal evaluations. Notably, in…

## 19. RSI Arena: Towards Recursive Self-Improvement with Human Feedback

- 分数：26.0  ·  HF 赞：20  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark, language model
- 作者：Yue Huang, Yanbo Wang, Lichi Li, Yuanyuan Chen, Andreas Haupt, Xiaonan Luo, Zheyuan Liu, Jihye Choi, Felix Juefei-Xu, Xiangliang Zhang, Radha Poovendran, Misha Sra, Ying Liu, Ben Burtenshaw, Thomas Wolf, Alex Pentland, Zichen Chen, Zhangchen Xu
- 链接：[arXiv](https://arxiv.org/abs/2610.33624) · [PDF](https://arxiv.org/pdf/2610.33624) · [HF](https://huggingface.co/papers/2610.33624)

Can AI agents autonomously train useful language models and improve them using feedback from users? We introduce RSI Arena, a two-stage study of autonomous post-training as a step toward recursive self-improvement. Ten frontier models act as training agents, each starting from NVIDIA Nemotron 3.5 Lightning 30B-A3B Base. During a six-day first stage, each agent has 1,000 GPU-hours and $300 in API credit on a shared…

## 20. Channel Selection for Mixture-of-Experts Decoding Needs No Calibration Data

- 分数：24.0  ·  HF 赞：12  ·  来源：huggingface + arxiv
- 兴趣命中：memory, benchmark, coding
- 作者：Geunhyoung Kim, Sung Ju Hwang
- 链接：[arXiv](https://arxiv.org/abs/2610.37386) · [PDF](https://arxiv.org/pdf/2610.37386) · [HF](https://huggingface.co/papers/2610.37386)

Mixture-of-Experts (MoE) models are bottlenecked by loading routed-expert weights from memory during interactive decoding at small batch sizes. Because most intermediate channels in a routed expert contribute little to any single token, channel selectors predict which channels matter and read only their weights, typically keeping channels above a threshold calibrated on offline data. We show that channel selection…

## 21. h1: A Taste of the Bitter Lesson in Automated Theorem Proving

- 分数：23.5  ·  HF 赞：15  ·  来源：huggingface
- 兴趣命中：agent, reasoning, language model, spec, planning
- 作者：Skander Moalla, Ahmad Rammal, Niket Patel, Remi Munos, Julia Kempe
- 链接：[arXiv](https://arxiv.org/abs/2610.35962) · [PDF](https://arxiv.org/pdf/2610.35962) · [HF](https://huggingface.co/papers/2610.35962)

While progress in informal mathematics has come largely from scaling the chain-of-thought and agentic reasoning of frontier language models, formal theorem proving has increasingly relied on human-designed workflows around these models, such as planning, decomposition, and orchestrating specialized provers. This raises a bitter-lesson question: can a simple agentic loop that scales test-time compute match these…

## 22. Your Policy Is Secretly a Harness: The Decision Geometry of Agent Interfaces

- 分数：23.5  ·  HF 赞：7  ·  来源：huggingface + arxiv
- 兴趣命中：agent, language model, coding, spec
- 作者：Jian Mu, Ruibo Shen, Yao Shu
- 链接：[arXiv](https://arxiv.org/abs/2610.37255) · [PDF](https://arxiv.org/pdf/2610.37255) · [HF](https://huggingface.co/papers/2610.37255)

Language model agents are post-trained and deployed through a harness, the prompts, tools, and control logic that present a task to the model and execute its outputs. Harnesses are often revised and judged by how an already trained model performs under them, which assumes that what the model learned under one harness carries over to the next. We ask what a policy learns from its harness and what survives when the…

## 23. Omni-InteractScope: Benchmarking Proactive and Agentic Interaction in Continuous Omnimodal Streams

- 分数：22.5  ·  HF 赞：13  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark, language model, large language, spec
- 作者：Yinsong Yan, Ling Wang, Yuxuan Wang, Yifan Yang, Ruiyang Xu, Junming Lin, Qi Chen, Meng Gao, Minghao Han, Yunfei Chu, Qize Yang, Xize Cheng, Jin Xu, Jibin Wu
- 链接：[arXiv](https://arxiv.org/abs/2610.35439) · [PDF](https://arxiv.org/pdf/2610.35439) · [HF](https://huggingface.co/papers/2610.35439)

Omnimodal large language models (Omni-LLMs) are increasingly expected to assist users while observing continuous audiovisual streams. However, existing evaluations provide limited insight into how reliably these models connect stream evidence and user needs to timely, sustained interventions. We introduce Omni-InteractScope, a benchmark of 1,479 human-annotated, cross-reviewed interactions with 1,790 temporal…

## 24. OmniShowcase: Omnidirectional Subject-Consistent Video Generation from Multi-View Images

- 分数：21.5  ·  HF 赞：19  ·  来源：huggingface
- 兴趣命中：evaluation, spec
- 作者：Junyeong Ahn, Geonwoo Kim, Kinam Kim, Gihwi Kim, Hoonjin Jung, Hyojin Jang, Jaegul Choo
- 链接：[arXiv](https://arxiv.org/abs/2610.35684) · [PDF](https://arxiv.org/pdf/2610.35684) · [HF](https://huggingface.co/papers/2610.35684)

Generating videos of a specific subject from a few reference images remains challenging when the camera reveals surfaces that are not visible in the input. Early subject-to-video (S2V) methods condition on a single reference image and must therefore infer the subject's unseen appearance and geometry as the viewpoint changes. To address this limitation, recent methods extend S2V to multiple reference views, providing…

## 25. Can LLMs Uncover Hidden Physical Laws through Free Exploration?

- 分数：21.5  ·  HF 赞：7  ·  来源：huggingface + arxiv
- 兴趣命中：agent, language model, large language
- 作者：Zhen Yang, Wen Wang, Xander Xu, Ying-Cong Chen
- 链接：[arXiv](https://arxiv.org/abs/2610.37649) · [PDF](https://arxiv.org/pdf/2610.37649) · [HF](https://huggingface.co/papers/2610.37649)

Scientific discovery often begins with an unexpected observation that prompts a new research question. In a world with altered physical laws, can large language models (LLMs) notice unexpected behavior, such as heavier objects falling more slowly, and discover the law through experiments without being told what to investigate? To evaluate this ability, we introduce LongChang, an automated framework that creates…

## 26. MatAnyone-E: Sparse Memory Propagation for Efficient High-Resolution Video Matting

- 分数：21.0  ·  HF 赞：18  ·  来源：huggingface
- 兴趣命中：memory, spec
- 作者：Shuyun Wang, Shangchen Zhou, Peiqing Yang, Yuekun Dai, Xin Yu, Chen Change Loy
- 链接：[arXiv](https://arxiv.org/abs/2610.35724) · [PDF](https://arxiv.org/pdf/2610.35724) · [HF](https://huggingface.co/papers/2610.35724)

High-resolution video matting requires preserving fine details, such as hair strands and soft transparency, while maintaining consistency across frames. Memory-based methods achieve strong matting quality by matching current-frame features with information stored from earlier frames, but this process becomes increasingly costly as resolution grows. We present MatAnyone-E, an efficient extension of MatAnyone 2 that…

## 27. Rare, Relevant, and Still Wrong: How Memory Fails LLM Group Decisions

- 分数：20.5  ·  HF 赞：5  ·  来源：huggingface + arxiv
- 兴趣命中：agent, memory, benchmark
- 作者：Anouar Imel, Imad Charradi, Abderrahman Sghir, Khalil El Khammar
- 链接：[arXiv](https://arxiv.org/abs/2610.37624) · [PDF](https://arxiv.org/pdf/2610.37624) · [HF](https://huggingface.co/papers/2610.37624)

When an LLM group's discussion is compressed into a short memory for a final decision maker, what should the memory keep? Two natural heuristics keep the rarest claims or the claims relevant to the decision criteria. On hidden-profile tasks both look attractive, because how widely a fact is held is confounded with whether it helps. We introduce CrossProfile, a diagnostic benchmark of 60 templates with automatically…

## 28. Vision-Language-Action or World-Action? Just Action Models

- 分数：20.5  ·  HF 赞：5  ·  来源：huggingface + arxiv
- 兴趣命中：language model, coding, spec
- 作者：Yonghao Yu, Lang Huang, Runyi Li, Toshihiko Yamasaki
- 链接：[arXiv](https://arxiv.org/abs/2610.37219) · [PDF](https://arxiv.org/pdf/2610.37219) · [HF](https://huggingface.co/papers/2610.37219)

The vision-language-action (VLA) and world-action model (WAM) communities debate whether control policies should inherit pretrained knowledge from vision-language models or from visual generators. The debate, however, bundles three separable choices: backbone initialization, the objective applied to future observations, and whether the machinery for that future loss is kept at inference. A gap between a VLA and a…

## 29. What Effort Level Should I Choose? On the Economics of Reasoning Effort in LLM Agents

- 分数：19.5  ·  HF 赞：11  ·  来源：huggingface
- 兴趣命中：agent, reasoning, benchmark
- 作者：Kaiser Sun, Yongchan Kwon, Zain Hasan, Shang Zhu, Kaitlyn Zhou, Federico Bianchi
- 链接：[arXiv](https://arxiv.org/abs/2610.34491) · [PDF](https://arxiv.org/pdf/2610.34491) · [HF](https://huggingface.co/papers/2610.34491)

Generative models increasingly expose a reasoning effort setting that lets users scale inference-time compute, trading higher cost for potentially improved performance. Users must choose an effort level before knowing whether extra reasoning will help, and even a successful run does not reveal whether the effort purchased was necessary. Reasoning effort is therefore a credence good: buyers observe the outcome but…

## 30. On the SPOT: Enhancing Speculative Decoding for Diffusion Language Models via Commit-Order Prediction

- 分数：19.0  ·  HF 赞：10  ·  来源：huggingface
- 兴趣命中：language model, coding, spec
- 作者：Eliezer Shlomi, Eliron Rahimi, Avi Mendelson, Chaim Baskin
- 链接：[arXiv](https://arxiv.org/abs/2610.22543) · [PDF](https://arxiv.org/pdf/2610.22543) · [HF](https://huggingface.co/papers/2610.22543)

Diffusion language models (DLMs) promise parallel text generation, but in practice face an unresolved speed-quality trade-off. Exact decoding fills in only one masked position per model pass, while faster multi-token decoding schemes are lossy. Speculative decoding is the standard lossless acceleration for autoregressive models. However, it does not transfer directly to DLMs, which must choose both what to generate…

## 31. OvisOCR3 Technical Report

- 分数：19.0  ·  HF 赞：6  ·  来源：huggingface
- 兴趣命中：reinforcement learning, benchmark, language model, spec
- 作者：Yu Xia, Yinglun Li, Yuhui Chen, Jinlong Huang, Yuyang Wanyan, Shengze Shi, Yifei Song, Yue Duan, Shubo Lin, Jianshan Zhao, En Lin, Shiyin Lu, Qing-Guo Chen, Zhao Xu, Weihua Luo
- 链接：[arXiv](https://arxiv.org/abs/2610.33066) · [PDF](https://arxiv.org/pdf/2610.33066) · [HF](https://huggingface.co/papers/2610.33066)

We introduce OvisOCR3, a 0.8B model for a broad range of OCR-related tasks. OvisOCR3 unifies document parsing, general OCR, key information extraction (KIE), document figure captioning, and cross-page table reconstruction in a single model. We train the model on real and synthetic data through continued pretraining and use domain-balanced mid-training to balance supervision across tasks with different data volumes…

## 32. Harness-Model Collaboration for Long-Horizon Continual Learning

- 分数：19.0  ·  HF 赞：6  ·  来源：huggingface
- 兴趣命中：agent, memory, spec, retrieval
- 作者：Zhen Bi, Zhizhi Peng, Yan Wang, Xueshu Chen, Haofei Zhang, Yaobo Zhang, Zeyu Yang, Qing Shen, Jungang Lou
- 链接：[arXiv](https://arxiv.org/abs/2610.34724) · [PDF](https://arxiv.org/pdf/2610.34724) · [HF](https://huggingface.co/papers/2610.34724)

Long-horizon agents continuously encounter reusable procedural knowledge, yet existing systems typically rely either on model adaptation or external memory, trading persistent learning for rapid reuse. This limitation is especially important for Web agents that repeatedly execute related multi-step workflows. We propose HaMo, a Harness-Model collaborative framework that combines fast non-parametric experience…

## 33. Nemotron-Labs-Diffusion-Uni: Elastic Self-Refining Unified Diffusion LLM with Cross-Paradigm On-Policy Distillation

- 分数：17.5  ·  HF 赞：7  ·  来源：huggingface
- 兴趣命中：reasoning, language model, large language
- 作者：Shufan Li, Hanrong Ye, Greg Heinrich, Yonggan Fu, Haotian Zhang, Sifei Liu, Aditya Grover, Pavlo Molchanov
- 链接：[arXiv](https://arxiv.org/abs/2610.36466) · [PDF](https://arxiv.org/pdf/2610.36466) · [HF](https://huggingface.co/papers/2610.36466)

We propose Nemotron-Labs-Diffusion-Uni (NLD-Uni), a unified discrete diffusion large language model (DLLM) for visual understanding and generation tasks. Compared with prior unified diffusion models, NLD-Uni introduces two major innovations. First, we propose a unified cross-paradigm on-policy distillation (OPD) framework that successfully transfers the visual understanding ability of autoregressive VLMs and visual…

## 34. Timestral

- 分数：17.0  ·  HF 赞：6  ·  来源：huggingface + arxiv
- 兴趣命中：benchmark
- 作者：Adrien Petralia, Alexandre Gavaudan, Artjom Joosen, Etienne Goffinet, Richard Kurle, Yassine El Ouahidi, Yassir Bendou, Abdelaziz Bounhar, Abhijeet Somani, Aditi Kabra, Adrian Valente, Adrien Sadé, Ahmed Djermani, Alan Jeffares, Albert Jiang, Alberto Bietti, Aleksandr Timashov, Alexandre Cahill, Alexandre Laval, Alexandre Sablayrolles, Alexandros Sanchez Vassopoulos, Amélie Héliou, Amos You, André Jonasson, Andreas Fürst, Andrew Bai, Andrew Ehrenberg, Andrew Zhao, Andy Lo, Angele Lenglemetz, Anmol Agarwal, Antonia Calvi, Arata Suzuki, Arjun Majumdar, Arthur Fournier, Ashwani Kumar, Augustin Lombard, Avinash Sooriyarachchi, Aylin Guliz Akkus, Aysenur Karaduman, Baptiste Bout, Baptiste Rozière, Barna Pásztor, Baudouin De Monicault, Benjamin Holzschuh, Benjamin Tibi, Benno Stein, Bernhard Stadlbauer, Bhargavi Bhaskar, Binbing Hou, Błażej Osiński, Boris van Breugel, Camille Le Scao, Chaoran Yu, Charlotte Cronjäger, Chen-Yo Sun, Chris Bamford, Christian Wallenwein, Christophe Renaudin, Clémence Lanfranchi, Colin Bonatti, Corentin Barreau, Corentin Sautier, Cristiana-Diana Diaconu, Cyprien Courtot, Daniel Lopes, Daniel Marczak, Darius Dabert, Diego de las Casas, Dominik Nuss, Dylan Rubini, Dzmitry Soupel, Elizaveta Demyanenko, Elliot Chane-Sane, Emilien Fugier, Emmanuel Gottlob, Erik Aas, Etienne Duchesne, Fabian Paischer, Fabian Schlager, Faruk Ahmed, Federico Baldassarre, Félix Rosseeuw, Filip Szatkowski, Filippo Vicentini, Florian Wiesner, Gabrielle Berrada, Gaëtan Ecrepont, Gaspard Blanchet, Gaspard Donada-Vidal, Gaurav Mahajan, Gauthier Guinet, Genevieve Hayes, Georgii Novikov, Georgios Christoglou, Giada Pistilli, Gonzague de Carpentier, Graeme Nail, Guillaume Breton, Guillaume Kunsch, Guillaume Lample, Guillaume Martin, Guillaume Raille, Guillaume Richard, Guillem Simeon, Gunjan Dhanuka, Gunshi Gupta, Hamza Senhaji Rhazi, Han Zhou, Hédi Hadiji, Himanshu Jaju, Hope McGovern, Hubert de Parseval, Hugo Cisneros, Hugo Germain, Hugo Thimonier, Hugo Venturini, Hyeonju Lee, Hyunwoo Oh, Iliass Lasri, Ilyas Oulkadda, Jacques Sun, Jan Ludziejewski, Jason Rute, Jean de Becdelièvre, Jean Quentin, Jean-Malo Delignon, Jessica Chudnovsky, Jianchao Li, Jie Zhang, Jin Bin Ou, Joachim Studnia, Joep Barmentlo, Johannes Brandstetter, John Harvill, Jonas Amar, Jonas Schweizer, Jonathan Roberts, Joséphine Delas, Josselin Somerville, Jules Depersin, Julien Denize, Julien Tauran, Julien Verlaguet, Kartik Khandelwal, Khyathi Raghavi Chandu, Kilian Tep, Konstantin Mishchenko, Kris Szczepaniak, Kush Jain, Larissa Laich, Laura Calem, Laurence Aitchison, Laurent Callot, Laurent Fainsin, Léo Cotteleer, Léonard Blier, Loïc Chadoutaud, Loïck Chambon, Lorenzo Proietti, Louis Faucon, Louis Martin, Louis Serrano, Lu Li, Luc Boudier, Lucas Fernandes Martins, Lucas Mebille, Lucile Saulnier, Ludovic Ho Fuh, Luis Montero, Łukasz Borchmann, Maarten Buyl, Malik Hassan Raza, Manon Chossegros, Marcin Możejko, Margaret Jennings, Markus Hennerbichler, Martin Alexandre, Mathieu Poirée, Mathieu Schmitt, Mathilde Guillaumin, Mathis Felardos, Matthieu André, Matthieu Dinot, Matthieu Futeral, Maurits Bleeker, Mauro Comi, Max Mynter, Maxim Berman, Maxime Darrin, Maxime Langelier, Maxime Louis, Maximilian Augustin, Maximilian Müller, Mehdi Bouaziz, Melina Jingting Laimon, Mert Unsal, Mia Chiquier, Michael Pilcer, Michał Pietruszka, Michał Zając, Mickaël Seznec, Mikhail Biriuchinskii, Minh-Quang Pham, Minwoo Kang, Mircea Lica, Morgane Rivière, Namit Katariya, Natasha Ørregaard Klingenbrunn, Nathan Bout, Nathan Grinsztajn, Nathan Simpson, Neeraj Aggarwal, Neil Ashton, Neil Mallinar, Nick Bührer, Nicolas Moreau, Nicolò Lucchesi, Ola Mysiak, Oliver Leicht, Olivier Bousquet, Olivier Koch, Parag Jain, Patricia Wang, Patrick Blies, Patrick von Platen, Patryk Saffer, Paul Jacob, Paul Teiletche, Paul Wambergue, Paula Kurylowicz, Pavan Kumar Reddy, Pavel Kuksa, Philippe Formont, Philippe Pinel, Philomène Chagniot, Pierre Glandon, Pierre Stock, Pierre-André Savalle, Piotr Miłoś, Poojan Shah, Prateek Gupta, Pravesh Agrawal, Pui Ki Chan, Quentin Desreumaux, Quentin Selle, Quentin Torroba, Quentin Wargnier, Quercus Hernandez, Ram Ramrakhya, Randall Isenhour, Ranjit Parva, Raphaël Balouka, Raphaël Rialland, Raul Perez Pelaez, Reinhard Sonnleitner, Remi Delacourt, Rishi Shah, Rob Romijnders, Rohan Shah, Rohin Arora, Romain Sauvestre, Roman Soletskyi, Ronan Riochet, Rosalie Millner, Rupert Menneer, Sagar Vaze, Samuel Barry, Samuel Belkadi, Samuel Humeau, Samuele Papa, Sanchit Gandhi, Sandeep Cranganore, Sandeep Subramanian, Sarthak Mittal, Saskia Adaime, Scott Matthews, Sean Cha, Sebastian Kaltenbach, Seungjae Jung, Shashwat Verma, Sherif Waly, Shrimai Prabhumoye, Siddhant Waghjale, Siddharth Gandhi, Simon Lepage, Simon Sorg, Soham Ghosh, Sophie Marbach, Srijan Mishra, Stanislas Lange, Steve Hong, Sumukh Aithal, Szymon Antoniak, Tarun Kumar Vangani, Teddy Turquet, Teven Le Scao, Théo Cachet, Thibaut Lavril, Thomas Chabal, Thomas Coste, Thomas Defard, Thomas Foubert, Thomas Loux, Thomas Robert, Thomas Wang, Tianyu Zhang, Tim Lawson, Timothée Lacroix, Timothy Wallis, Tobias Kronlachner, Tom Bewley, Tom Edwards, Tomas Hodan, Triantafyllos Afouras, Tuhin Das, Tyler Wang, Udit Saxena, Ulrick Blé, Umar Jamil, Umberto Tomasini, Valentin Macé, Van Phung, Venkata Reddy, Vibha Masti, Victor Jouault, Victor Letzelter, Victor Paltz, Victor Poucheret, Vincent Maladière, Vincent Pfister, Virgile Richard, Vladislav Bataev, Wassim Bouaziz, Wen Ding Li, William Flanagan, William Havard, William Marshall, Witold Jędrzejewski, Xinghui Li, Xingran Guo, Xinyu Yang, Xuanyu Zhang, Yann Dreze, Yann Viegas, Yannic Neuhaus, Yassine Turki, Yessin Moakher, Yi He, Yihan Wang, Yimu Pan, Yuying Zhu, Yves Martin des Taillades, Zaccharie Ramzi, Zhenlin Xu, Zsófia Csákány
- 链接：[arXiv](https://arxiv.org/abs/2610.37585) · [PDF](https://arxiv.org/pdf/2610.37585) · [HF](https://huggingface.co/papers/2610.37585)

We introduce Timestral, a family of four time series foundation models for probabilistic forecasting, with 5M, 28M, 123M, and 209M parameters. Timestral sets a new state of the art on GIFT-Eval, TIME, and fev-bench, where Timestral-209M and Timestral-123M take the top two places on every metric. We achieve this with three ingredients: Decoupled Horizon Forecasting (DHF), which separates prediction tokens from the…

## 35. AlphaBet: Reinforcement Learning for LLM Event Forecasting Agents

- 分数：17.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：agent, reinforcement learning, language model, large language
- 作者：Liqin Ye, Rongzhi Zhang, Xin Liu, Zheng Li, Yuan He, Qingyu Yin, Priyanka Nigam, Chao Zhang
- 链接：[arXiv](https://arxiv.org/abs/2610.22684) · [PDF](https://arxiv.org/pdf/2610.22684) · [HF](https://huggingface.co/papers/2610.22684)

Forecasting an unresolved event requires finding relevant evidence and deciding how strongly it supports each outcome. Yet outcome-based training of Large Language Model (LLM) forecasters often begins with preassembled evidence at a single prediction date, leaving evidence acquisition outside the learning loop. We introduce AlphaBet, an agentic reinforcement learning (RL) framework that trains a single LLM policy to…

## 36. Self-Assessment Reinforcement Learning for Search-State Awareness in Retrieval-Augmented Large Language Models

- 分数：17.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：agent, reasoning, reinforcement learning, benchmark, language model, large language, retrieval
- 作者：Taewhoo Lee, Minju Song, Jungwoo Park, Chanwoong Yoon, Junha Jung, Hyeon Hwang, Sanghoon Lee, Minbyul Jeong, Jaewoo Kang
- 链接：[arXiv](https://arxiv.org/abs/2610.30435) · [PDF](https://arxiv.org/pdf/2610.30435) · [HF](https://huggingface.co/papers/2610.30435)

Recent advances in search agents have enabled large language models to tackle complex tasks by retrieving and synthesizing external information. However, existing search agents often lack search-state awareness, i.e., the ability to recognize what information has been obtained and what remains missing, leading to hallucinated reasoning and prematurely terminated search. To address this limitation, we propose…

## 37. MoveBench: A Rubric-Based Benchmark for Evaluating Large Language Models in Sports and Health Coaching

- 分数：17.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：reasoning, evaluation, benchmark, language model, large language, spec
- 作者：Yitong Li, Jiang Bian, Jingling Wang, Pan Ding, Chengying Gu
- 链接：[arXiv](https://arxiv.org/abs/2610.26185) · [PDF](https://arxiv.org/pdf/2610.26185) · [HF](https://huggingface.co/papers/2610.26185)

Despite rapid advances in large language models (LLMs), their deployment in the sports and health domain remains high-risk due to the absence of domain-specific evaluation benchmarks. Existing general-purpose benchmarks (e.g., MMLU and HELM) primarily assess broad knowledge and reasoning capabilities, but fail to capture critical domain requirements such as exercise safety, physiological appropriateness,…

## 38. The Lexical Imprint of Pre-training Data

- 分数：16.5  ·  HF 赞：9  ·  来源：huggingface
- 兴趣命中：evaluation, benchmark
- 作者：Jeonghoon Kim, Woojin Chung, Woomin Song, Cheonbok Park, Nako Sung, Jinwoo Shin
- 链接：[arXiv](https://arxiv.org/abs/2602.10657) · [PDF](https://arxiv.org/pdf/2602.10657) · [HF](https://huggingface.co/papers/2602.10657)

How much of zero-shot benchmark accuracy is captured by word-level alignment between a pre-training corpus and the benchmark target? We study this question through word-level unigram cross-entropy (UCE), a tokenizer-agnostic, model-free measure of lexical alignment between a reference corpus and a target benchmark. Likelihood training shapes the model's predictive distribution from the pre-training corpus, and…

## 39. Learning and Reasoning with Geometry: How Generation Helps Spatial Understanding

- 分数：16.5  ·  HF 赞：5  ·  来源：huggingface
- 兴趣命中：reasoning, reinforcement learning, spec
- 作者：Rui Yang, Yanwei Li, Sili Chen, Jingjia Huang, Yi Lin, Hengshuang Zhao
- 链接：[arXiv](https://arxiv.org/abs/2610.36022) · [PDF](https://arxiv.org/pdf/2610.36022) · [HF](https://huggingface.co/papers/2610.36022)

Image and video generators can produce spatially consistent visual content, but how to use this capability to improve spatial understanding remains underexplored. We study this problem from two perspectives: geometric supervision during training and explicit geometric evidence during inference. To this end, we introduce a unified geometric understanding and generation model (GeoUG) that integrates depth and…

## 40. MLE-World: Predicting Machine Learning Experiment Outcomes with a Learned World Model

- 分数：16.0  ·  HF 赞：4  ·  来源：huggingface + arxiv
- 兴趣命中：agent
- 作者：Brian Ko, Han Wang, Hejia Geng, Li Erran Li, Sherry Yang
- 链接：[arXiv](https://arxiv.org/abs/2610.37175) · [PDF](https://arxiv.org/pdf/2610.37175) · [HF](https://huggingface.co/papers/2610.37175)

AI research agents can propose, execute, and improve programs that solve machine learning tasks. However, executing each candidate program requires training and evaluating ML models, limiting how many candidates an agent can explore at each step. We introduce MLE-World, a world model finetuned from Qwen3.5-4B that predicts a program's terminal output (error traces, training logs, and validation scores) from its code…

## 41. Benchmarking Obstacle-Conditioned Safety in Household Robot Navigation

- 分数：15.5  ·  HF 赞：7  ·  来源：huggingface
- 兴趣命中：evaluation, benchmark
- 作者：Hyunwoong Bae, Jisu Han, Jiyeon Choi, Dohoon Kim, Taesup Moon
- 链接：[arXiv](https://arxiv.org/abs/2610.34674) · [PDF](https://arxiv.org/pdf/2610.34674) · [HF](https://huggingface.co/papers/2610.34674)

Safe household navigation requires robots to regulate clearance and speed according to what an obstacle is and how close it is, without unnecessary conservatism. Yet existing evaluations do not test whether semantic safety distinctions are reflected in continuous motion. To that end, we introduce OSMA-Bench, an Obstacle-Conditioned Safe Motion Adaptation Benchmark built on spatially matched scenario sets that differ…

## 42. SearchHorizonBench: A Benchmark for Search Value in AI Agents

- 分数：15.5  ·  HF 赞：7  ·  来源：huggingface
- 兴趣命中：agent, benchmark
- 作者：Jingjie Ning, Xueqi Li, Yibo Kong
- 链接：[arXiv](https://arxiv.org/abs/2610.34714) · [PDF](https://arxiv.org/pdf/2610.34714) · [HF](https://huggingface.co/papers/2610.34714)

AI agents must decide when another search is worth its cost. Answer-success probabilities capture question difficulty, while this decision requires estimating the additional benefit of search. We introduce SearchHorizonBench, a benchmark for learning and evaluating search value from execution experience. Paired continuations and repeated executions separate expected search gain from generation noise and connect…

## 43. TAO: Tool-Aware Joint Scheduling for LLM-Based Agentic Serving

- 分数：15.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：agent, evaluation, spec
- 作者：Shuhuai Li, Shengdong Ye, Dongdong Ge, Yinyu Ye, Jianghao Lin
- 链接：[arXiv](https://arxiv.org/abs/2610.37230) · [PDF](https://arxiv.org/pdf/2610.37230) · [HF](https://huggingface.co/papers/2610.37230)

Agentic services alternate between model inference on clustered GPUs and external tools on distributed CPUs. In this scenario, existing systems (1) overlook tool-return readiness in service evaluation, wasting limited resources, and (2) use heuristic strategies to decide admission and placement on GPUs, resulting in suboptimal scheduling decisions. To bridge this gap, we present TAO, a tool-aware joint scheduling…

## 44. RynnWorld-Latent: A Cross-Embodiment World Model Conditioned on Universal Latent Actions

- 分数：14.5  ·  HF 赞：9  ·  来源：huggingface
- 兴趣命中：benchmark
- 作者：Haoyu Zhao, Yinzhou Tang, Zixuan Wang, Minghao Zhu, Dongchi Huang, Xingyue Zhao, Qin Zhao, Kehan Li, Siteng Huang, Xin Li, Zhenyu Zeng, Mingxiu Chen, Deli Zhao, Zhongyu Li
- 链接：[arXiv](https://arxiv.org/abs/2610.36791) · [PDF](https://arxiv.org/pdf/2610.36791) · [HF](https://huggingface.co/papers/2610.36791)

Learning controllable world dynamics from heterogeneous interaction videos is challenging because robot embodiments use incompatible action spaces, while human videos lack native control labels. We present RynnWorld-Latent, a cross-embodiment video world model that uses the 3D-grounded latent actions introduced by RynnLAM as a shared conditioning interface. This representation enables joint pretraining on human…

## 45. How Much Does the Hint Matter? Scope Conditions for Hindsight Self-Distillation in Financial Reasoning

- 分数：14.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：reasoning, benchmark
- 作者：Johnny Yu, Cyril Gorlla
- 链接：[arXiv](https://arxiv.org/abs/2610.36082) · [PDF](https://arxiv.org/pdf/2610.36082) · [HF](https://huggingface.co/papers/2610.36082)

Financial institutions operating under data-residency constraints are restricted to open-weight models small enough to locally host, which trail frontier systems on multi-step quantitative reasoning. On-policy distillation narrows such gaps by supervising a student on its own rollouts, but traditional OPD requires a strong external teacher, and on-policy self-distillation (OPSD) conditions on a full reference…

## 46. Beyond the Estimate: Wiener-Informed Decoding for Easier Training of Pixel-Space Flow Models

- 分数：13.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：coding, spec
- 作者：Ziqiao Wang, Yang You
- 链接：[arXiv](https://arxiv.org/abs/2610.36192) · [PDF](https://arxiv.org/pdf/2610.36192) · [HF](https://huggingface.co/papers/2610.36192)

Learning velocity fields directly in pixel space is difficult and slow. We show that coarse second-order image statistics can ease this task: frozen Wiener estimates improve velocity learning, with gains extending beyond the linear predictions they explicitly provide. Moreover, we observe similar but complementary gains from frozen bases and pixel decoding. These observations motivate Wiener-informed Decoding (WiD),…

## 47. Cross-modal Steering Vectors Exist Across Both Image and Text Generation

- 分数：13.0  ·  HF 赞：10  ·  来源：huggingface
- 兴趣命中：-
- 作者：Donghao Zeng, Nishant Subramani, Tamar Rott Shaham, Benno Krojer
- 链接：[arXiv](https://arxiv.org/abs/2610.36269) · [PDF](https://arxiv.org/pdf/2610.36269) · [HF](https://huggingface.co/papers/2610.36269)

Are concepts and mechanisms unified across modalities in current AI models, or instead implemented separately for each one? We operationalize this broad question of modality unification by studying cross-modal steering: 1) finding vectors that successfully steer generation on tokens of one modality, which then 2) transfer zero-shot to steer generation when added to tokens of another modality. Our study goes beyond…

## 48. PhysEvolve: Verifier-grounded Self-evolution for Physical Reasoning with Executable Worlds

- 分数：13.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：reasoning, language model
- 作者：Jinyuan Hu, Yilei Jiang, Chen Tang, Minghong Cai, Xinran Liu, Xiangyu Yue
- 链接：[arXiv](https://arxiv.org/abs/2610.34921) · [PDF](https://arxiv.org/pdf/2610.34921) · [HF](https://huggingface.co/papers/2610.34921)

Physical reasoning underpins how embodied systems understand and act in the physical world, yet vision-language models (VLMs) remain unreliable on questions about dynamics and physical causality. Progress is critically constrained by the scarcity of grounded counterfactual training data, as observational videos capture only the factual trajectory that occurred. The self-evolving paradigm offers a route beyond fixed…

## 49. Sensorimotor Alignment: A Platonic Proxy for Embodied Policy Success

- 分数：12.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：evaluation, language model
- 作者：Yunfei Xie, Howard H. Qian, Shiyi Lan, Kaiyu Hang, Chen Wei
- 链接：[arXiv](https://arxiv.org/abs/2610.31670) · [PDF](https://arxiv.org/pdf/2610.31670) · [HF](https://huggingface.co/papers/2610.31670)

Robot foundation models are typically evaluated through costly closed-loop rollouts, motivating low-cost offline proxies for model capability. The Platonic Representation Hypothesis (PRH) suggests that as representations improve, modalities such as vision and language converge toward a shared statistical model of reality. We ask whether motion trajectories form another such modality: as embodied models become more…

## 50. AdaPRA: Process Reward Agents with Adaptive Rubrics for Data Science

- 分数：12.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：agent, coding
- 作者：Atharva Naik, Vivek Chari, Pol Llado, Daniel Fried, Carolyn Rosé, Benjamin Van Durme, Sam Thomson, Justin Svegliato
- 链接：[arXiv](https://arxiv.org/abs/2610.33245) · [PDF](https://arxiv.org/pdf/2610.33245) · [HF](https://huggingface.co/papers/2610.33245)

Data science agents can automate end-to-end machine learning workflows, yet they remain far from competitive on human leaderboards. Agents make process errors such as insufficient exploration, unsound validation, coding bugs, and poor use of a fixed budget (re-running the same exploratory data analysis and baseline models in every attempt). We propose AdaPRA to address these issues: a persistent coding agent harness…

## 51. Lipi-Ghor: A Large-Scale, Diarized, Multi-Domain Bengali Speech Corpus and a Scalable Pipeline for Building It

- 分数：12.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：evaluation, benchmark
- 作者：Sanjid Hasan, A H M Fuad, Risalat Labib, Bayazid Hasan Simon
- 链接：[arXiv](https://arxiv.org/abs/2610.36184) · [PDF](https://arxiv.org/pdf/2610.36184) · [HF](https://huggingface.co/papers/2610.36184)

Bengali, spoken by over 230 million people, remains severely under-resourced in spoken language research. Existing open Bengali ASR corpora are confined to short, read or crowd-sourced speech and lack speaker diarization and long-form audio.   We present Lipi-Ghor, a large-scale weakly-supervised Bengali speech corpus comprising 885 hours of audio sourced from 998 YouTube videos across 596 unique channels, spanning…

## 52. T-DIG: Text-Conditioned Diversity for Image Generation

- 分数：11.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：spec
- 作者：Simran Khanuja, Rohit Gandikota, Gaurav Parmar, Graham Neubig
- 链接：[arXiv](https://arxiv.org/abs/2610.29003) · [PDF](https://arxiv.org/pdf/2610.29003) · [HF](https://huggingface.co/papers/2610.29003)

Text-to-image (T2I) platforms typically return several images per prompt so users can explore different visual interpretations and choose one that matches their intent. However, T2I models are usually optimized for single-image quality which comes at a cost of multi-image diversity, limiting this exploration. Diversity is also contextual: one user wants variations in background, while another wants them in artistic…

## 53. What Outcome RL Buys: Finishing, Reliability, Rarely Reach

- 分数：10.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：-
- 作者：Shan Yang
- 链接：[arXiv](https://arxiv.org/abs/2610.34894) · [PDF](https://arxiv.org/pdf/2610.34894) · [HF](https://huggingface.co/papers/2610.34894)

Outcome RL raises pass@1 but not pass@k at large k (Yue et al., 2025). But every pass@1 is scored under a token budget. Every recipe also trains under one. On physics and math problems at fixed token budgets, we compare the pass@1 of 20 released RL models (1.5B to 32B) with that of the thinking models they started from. We ask whether each pass@1 gain is changed behaviour or new knowledge. We divide each change in…

## 54. Sub-monolayer tracking of molecular states at buried interfaces

- 分数：9.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：-
- 作者：Harlan Heilman, Em Biegler, Sushil Adhikari, Victor Murcia, Tanner Melody, Fred Woodall, Lars Thomsen, Obaid Alqahtani, Brian A. Collins
- 链接：[arXiv](https://arxiv.org/abs/2610.31924) · [PDF](https://arxiv.org/pdf/2610.31924) · [HF](https://huggingface.co/papers/2610.31924)

Phenomena responsible for emerging technologies originate from novel molecular states at buried interfaces. Yet quantitatively resolving these features is out of reach in most cases. Resonant scattering has demonstrated sensitivity to these local states but is limited due to a lack of accurate interpretive models. We leverage a machine learning (ML)-optimized optical model to analyze polarized resonant soft X-ray…

## 55. Truncate or Not? A Scaling Study of Looped Transformers with Truncated Backpropagation

- 分数：9.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：-
- 作者：Xuyuan Xiong, Siyu Chen, Zihan Shao, Yue Su, Weiyang Jin, Ping Luo, Zhuoran Yang, Xihui Liu
- 链接：[arXiv](https://arxiv.org/abs/2610.26030) · [PDF](https://arxiv.org/pdf/2610.26030) · [HF](https://huggingface.co/papers/2610.26030)

Looped transformers reuse a shared block of layers to increase computational depth without increasing the number of trainable parameters. They are trained with backpropagation through time (BPTT). To save training compute, BPTT is often truncated to the last few loops, but truncation yields biased gradients that may weaken the benefit of looping. In this work, we study the value of truncation in looped transformer…

## 56. Quaternion Approximate Networks for Enhanced Image Classification and Oriented Object Detection

- 分数：9.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：-
- 作者：Bryce Grant, Peng Wang
- 链接：[arXiv](https://arxiv.org/abs/2509.05512) · [PDF](https://arxiv.org/pdf/2509.05512) · [HF](https://huggingface.co/papers/2509.05512)

This paper introduces Quaternion Approximate Networks (QUAN), a novel deep learning framework that leverages quaternion algebra for rotation equivariant image classification and object detection. Unlike conventional quaternion neural networks attempting to operate entirely in the quaternion domain, QUAN approximates quaternion convolution through Hamilton product decomposition using real-valued operations. This…

## 57. Evaluating AlphaEarth Embeddings for Crop Classification: Separability, Temporal Dynamics, and Cross-Regional Transferability

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, coding, spec
- 作者：Priyanka Goyal, Maitreyee Sar, Adway Mitra, Manjira Sinha
- 链接：[arXiv](https://arxiv.org/abs/2610.36857) · [PDF](https://arxiv.org/pdf/2610.36857) · [HF](https://huggingface.co/papers/2610.36857)

Earth Observation (EO)-based agricultural monitoring is shifting from pixel-level spectral analysis toward representation-driven modeling, yet systematic evaluation of learned representations across spatial, temporal, and domain-generalization dimensions remains limited. Geospatial foundation models generate high-dimensional embeddings encoding spatio-temporal land-surface properties, but their utility for…

## 58. GUI-JEPA: Candidate-Conditioned JEPA Latents as a Fast Action Policy for Mobile GUI Agents

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, memory, language model, large language, coding
- 作者：Bingchao Wang, Yongcheng Jing, Shunyu Liu, Chengyu Wang, Jun Huang, Jie Yang, Wei Liu, Dacheng Tao
- 链接：[arXiv](https://arxiv.org/abs/2610.36877) · [PDF](https://arxiv.org/pdf/2610.36877) · [HF](https://huggingface.co/papers/2610.36877)

Mobile GUI agents are typically fine-tuned 7B-scale vision-language models (VLMs) that generate each action as text. However, these VLMs decode every action token by token, and even agents that score candidate actions keep a large language model or VLM in the loop, making them slow and memory-hungry. To address these issues, we propose GUI-JEPA, to our knowledge the first decoder-free GUI agent policy built on a…

## 59. Hyperparameter and Neural Architecture Search via Evolutionary Optimization for Reinforcement Learning: HPNAS-RL

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reinforcement learning, evaluation, spec
- 作者：Nihal Acharya Adde, Hanno Gottschalk
- 链接：[arXiv](https://arxiv.org/abs/2610.36882) · [PDF](https://arxiv.org/pdf/2610.36882) · [HF](https://huggingface.co/papers/2610.36882)

In this study, we propose a dual-branch evolutionary framework that simultaneously performs Neural Architecture Search (NAS) and Hyperparameter Optimization (HPO) for Reinforcement Learning (RL) in Autonomous Driving (AD) tasks. While NAS has shown strong potential in automating architecture design for Convolutional Neural Networks (CNNs), its application to RL remains limited, especially in scenarios that require…

## 60. HiLo-RD: Cross-Budget Self-Distillation for Masked Diffusion Language Models

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, benchmark, language model, coding
- 作者：Xiang Li, Chengting Yu, Jungang Li, Yilun Zheng, Junzhuo Li, Xingyao Zhang, Wenbo Su, Xuming Hu
- 链接：[arXiv](https://arxiv.org/abs/2610.36901) · [PDF](https://arxiv.org/pdf/2610.36901) · [HF](https://huggingface.co/papers/2610.36901)

We propose HiLo-RD (High-to-Low Budget Representation Distillation) to improve masked diffusion language models (MDLMs) under a limited generation budget. Unlike autoregressive models, MDLMs choose both what to generate and where to commit it. This creates two coupled challenges: predicting useful content before reasoning is complete, and deciding when to fix answer tokens that shape later predictions. We identify…

## 61. Nothing Left Behind: Finding Evidence from a Large Randomized Evaluation Corpus

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, language model, spec, retrieval
- 作者：Giuliano Martinelli, Abelardo Carlos Martinez Lorenzo, Satvik Garg, Linxi Wang, Riccardo Orlando, Piriyakorn Piriyatamwong, Samuel Paul Fraiberger
- 链接：[arXiv](https://arxiv.org/abs/2610.36910) · [PDF](https://arxiv.org/pdf/2610.36910) · [HF](https://huggingface.co/papers/2610.36910)

Many AI systems need to find every relevant items in a large collection and then organize what they found. The standard way to do this is to tag each item with labels from a curated vocabulary and search on those labels. Those labels are useful for organizing results, but searching on them misses items that do not fit a label and returns too much when labels are broad. We compare this approach with an…

## 62. TrawMem: Reframing Agent Memory as Task-Oriented Role-Adaptive Workspaces

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, memory, language model, large language, spec
- 作者：Mingyu Zhang, Zixu Li, Zhiheng Fu, Zhiwei Chen, Jinhe Bi, Yupeng Hu
- 链接：[arXiv](https://arxiv.org/abs/2610.36918) · [PDF](https://arxiv.org/pdf/2610.36918) · [HF](https://huggingface.co/papers/2610.36918)

Large language model (LLM) agents rely on memory systems to leverage long-term interactions, yet existing systems typically retrieve memories based on their relevance to the current query and use them as contextual evidence. However, relevance alone does not characterize how a memory contributes to task solving: the same memory may serve different roles across tasks, such as directly supporting the answer or linking…

## 63. TDLM: Adaptive Temporal Integration for Diffusion Language Models

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, evaluation, language model, coding
- 作者：Bohang Sun, Max Zhu, Francesco Caso, Christopher Irwin, Jialin Yu, Pietro Liò
- 链接：[arXiv](https://arxiv.org/abs/2610.36940) · [PDF](https://arxiv.org/pdf/2610.36940) · [HF](https://huggingface.co/papers/2610.36940)

Masked diffusion language models repeatedly compute representations for unresolved tokens, but conventional denoisers do not explicitly retain these representations for reuse across steps. We introduce Temporal Self-Conditioning Diffusion Language Model (TDLM), which lets each unresolved position attend to its own history of hidden representations within a frozen denoiser. This gives later predictions access to…

## 64. Beyond QASecClaw: Agent Scaling, Verifier Feedback, and Evidence Reliability in Software Assurance

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, evaluation, benchmark, spec
- 作者：S M Abdulla Al Mamun, Akif Islam, Mohd. Ruhul Ameen
- 链接：[arXiv](https://arxiv.org/abs/2610.36947) · [PDF](https://arxiv.org/pdf/2610.36947) · [HF](https://huggingface.co/papers/2610.36947)

Can additional specialist language-model contexts improve software assurance when deterministic tool evidence is already available? We study this question through five experiments spanning authored Java warning controls, OWASP Benchmark assessment, Defects4J test generation, SV-COMP assertion verdicts, and deliberately misleading evidence packages. The evaluated systems use Qwen2.5-Coder-7B-Instruct, with a 1.5B…

## 65. PailitaoMMSearch2.0 Technical Report: Scaling Generative Retrieval to Unified End-to-End Multimodal Search

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, reinforcement learning, spec, retrieval
- 作者：Xiaohan Ye, Zihan Gong, Jingqian Zhao, Lianyu Du, Yunmeng Shu, Xu Chen, Zesheng Zhou, Renchun You, Bocheng Chen, Jinsong Lan, Haihong Tang, Bo Zheng
- 链接：[arXiv](https://arxiv.org/abs/2610.36958) · [PDF](https://arxiv.org/pdf/2610.36958) · [HF](https://huggingface.co/papers/2610.36958)

Generative retrieval models have been increasingly adopted in search and recommendation systems. However, industrial generative retrieval models are commonly specialized to a fixed online scenario: they learn from scenario-specific interactions, support a narrow set of query forms and retrieval objectives. We study how to remove these couplings and build a unified end-to-end multimodal search system for open-ended…

## 66. Proactive Memory for Event-Driven LLM Agents

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, memory, benchmark, retrieval
- 作者：Jinyang Li, Zichuan Fu, Xian Wu, Wenlin Zhang, Yimin Deng, Kaifeng Guo, Guojing Li, Junjia QI, Xiangyu Zhao
- 链接：[arXiv](https://arxiv.org/abs/2610.36967) · [PDF](https://arxiv.org/pdf/2610.36967) · [HF](https://huggingface.co/papers/2610.36967)

Proactive LLM agents anticipate service opportunities from ongoing observations and accumulated history. Existing approaches emphasize recent context or retrieval of related memories, providing limited support for validating recurring behavioral regularities and assessing their applicability to the current event. We propose Proactive Memory (ProactMem), which organizes history into recent events, temporal…

## 67. AutoVend: Benchmarking LLM Agents on Long-Horizon Autonomous Vending Operations

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, benchmark, language model, large language
- 作者：Qiming Shi, Yikun Li, Beidi Luan, Rui Sun, Yan Ma, Jing Li, Daxin Jiang, Zuo Bai
- 链接：[arXiv](https://arxiv.org/abs/2610.36980) · [PDF](https://arxiv.org/pdf/2610.36980) · [HF](https://huggingface.co/papers/2610.36980)

Large language model (LLM) agents are extending agent-mediated commerce on the Web from shopping for consumers to operating businesses for sellers. In online-to-offline (O2O) commerce, decisions are issued through Web-based platforms but realized through costly physical execution. Evaluating such agents requires going beyond individual transactions to ask whether decisions made online turn into sustained economic…

## 68. The State and Fate of Multilingual, Contextual Evaluation in the NLP World

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, language model, large language
- 作者：Manan Uppadhyay, Himanshu Beniwal, Prashant Kodali, Sunayana Sitaram
- 链接：[arXiv](https://arxiv.org/abs/2610.36990) · [PDF](https://arxiv.org/pdf/2610.36990) · [HF](https://huggingface.co/papers/2610.36990)

Multilingual evaluation benchmarks are the primary instrument for assessing whether large language models generalize beyond English, yet the adequacy of these benchmarks has received little systematic scrutiny. We present a data-driven audit of 51 recent multilingual benchmarks spanning 242 datasets and 219 languages, organized around three pillars: coverage, representativeness, and rigor. Our analysis reveals that…

## 69. SpectRAG: Weighted Chunk Graphs for Token-Budgeted Context Selection in Multi-Hop Retrieval-Augmented Generation

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, language model, large language, spec, retrieval
- 作者：Zafer Sahinoglu, Abdulazeez Mohammed, Buse Yaren Kazangirler, Cahit Berkay Kazangirler
- 链接：[arXiv](https://arxiv.org/abs/2610.36991) · [PDF](https://arxiv.org/pdf/2610.36991) · [HF](https://huggingface.co/papers/2610.36991)

Retrieval-augmented generation (RAG) systems ground large language models (LLMs) by retrieving external evidence and conditioning generation on the retrieved context. Although dense retrieval is effective for local semantic matching, independently ranked retrieval can return redundant passages, miss cross-chunk dependencies, and provide incomplete evidence for multi-hop reasoning. We propose SpectRAG, a spectral…

## 70. CaLLM: Continual Adaptation of LLMs via Non-Parametric Adapter Routing

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, language model, large language, spec
- 作者：Bilge Celik, Anna Vettoruzzo, Joaquin Vanschoren
- 链接：[arXiv](https://arxiv.org/abs/2610.36994) · [PDF](https://arxiv.org/pdf/2610.36994) · [HF](https://huggingface.co/papers/2610.36994)

Continual adaptation of large language models (LLMs) to evolving task distributions while mitigating catastrophic forgetting remains an open problem. Existing strategies often struggle to scale or lack a robust mechanism for zero-shot task-to-expert assignment. We introduce CaLLM, a framework that resolves these tensions by combining metric-based meta-learning with modular parameter isolation via lightweight…

## 71. V-LUMEN: Visual Lookup Memory for Embedding Scaling in Vision-Language Models

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, reasoning, benchmark, language model
- 作者：Miso Choi, Daekeun Kim, Eunji Kim, Jungbeom Lee
- 链接：[arXiv](https://arxiv.org/abs/2610.37019) · [PDF](https://arxiv.org/pdf/2610.37019) · [HF](https://huggingface.co/papers/2610.37019)

Embedding-level scaling expands the capacity of language models through lookup-based memory rather than by increasing model depth, width, or dense computation. Extending this idea to vision-language models (VLMs) is challenging because visual features are continuous, spatially structured, and query-dependent, unlike discrete text tokens that naturally support n-gram lookup. We introduce V-LUMEN, a visual lookup…

## 72. Guided-RLVR: Guided Exploration in Reinforcement Learning with Verifiable Rewards

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, reinforcement learning, benchmark, language model, large language, spec
- 作者：Bo Yang, Zishuai Zhang, Weihua Li, Qinnan Zhang, Sijia Wen, Hainan Zhang
- 链接：[arXiv](https://arxiv.org/abs/2610.37041) · [PDF](https://arxiv.org/pdf/2610.37041) · [HF](https://huggingface.co/papers/2610.37041)

Reinforcement learning with verifiable rewards (RLVR) has shown strong empirical gains in improving the reasoning ability of large language models (LLMs) on tasks such as mathematics and programming. However, recent studies have shown that RLVR rollouts often collapse onto a narrow set of reasoning trajectories, limiting the explored reasoning space. Motivated by findings that thinking tokens at critical steps serve…

## 73. OpenGray: a benchmark for evaluating the decisions of radiotherapy planning agents

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, benchmark, language model, large language, spec, planning
- 作者：Humza Nusrat, Kundan Thind
- 链接：[arXiv](https://arxiv.org/abs/2610.37081) · [PDF](https://arxiv.org/pdf/2610.37081) · [HF](https://huggingface.co/papers/2610.37081)

Background and purpose: Radiotherapy planning agents based on large language models (LLMs) decide when to submit a plan or request review but are evaluated mainly by dose. This study developed OpenGray, a benchmark of planning tasks with known correct decisions. Materials and methods: OpenGray adds tasks with known answers to the OpenKBP-Opt head-and-neck dataset, including two contradictions with dose goals proven…

## 74. Learning to Look Beyond Screens: Transferable Visual Observation from GUI Grounding

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, reinforcement learning, language model, spec
- 作者：Ruilin Yao, Xinyu Qiu, Tianyu Zou, Yi Rong, Shengwu Xiong, Shuheng Shen, Changhua Meng
- 链接：[arXiv](https://arxiv.org/abs/2610.37093) · [PDF](https://arxiv.org/pdf/2610.37093) · [HF](https://huggingface.co/papers/2610.37093)

Visual perception is evolving from passive recognition toward active, task-oriented observation. We investigate GUI grounding as a scalable source of spatial supervision for learning observation behaviors that transfer beyond interfaces. We introduce LBS (Look Beyond Screens), a vision-language model trained through supervised initialization on teacher-generated GUI grounding trajectories, followed by reinforcement…

## 75. SplatScout: Query-Driven Part-Level Referring Segmentation in Gaussian Scenes

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, language model, spec
- 作者：Yihan Zang, Da Li, Shinkyu Park, Ivan Viola, Dominik Engel
- 链接：[arXiv](https://arxiv.org/abs/2610.37098) · [PDF](https://arxiv.org/pdf/2610.37098) · [HF](https://huggingface.co/papers/2610.37098)

Existing referring segmentation methods on Gaussian scenes primarily target whole objects, relying on segmenter-generated candidates from which a vision-language model (VLM) selects. Such predetermined fixed candidates may omit fine-grained parts needed as targets or cues for identifying objects. We introduce SplatScout, a query-driven, closed-loop approach that places perception under VLM control. The model…

## 76. WorkFactory: Turning Professional Intents into Executable Work for Scalable Agent Training

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, benchmark, spec, planning
- 作者：Ziyang Zeng, Tingyang Chen, Jia Deng, Qiyao Wang, Shuo Tang, Yike Yang, Tao Ren, Wayne Xin Zhao, Feng Chang, Jujie He, Chuan Hao, Ran Tao, Bryan Dai
- 链接：[arXiv](https://arxiv.org/abs/2610.37161) · [PDF](https://arxiv.org/pdf/2610.37161) · [HF](https://huggingface.co/papers/2610.37161)

Scaling supervised training for working agents requires diverse professional tasks that yield reliable expert demonstrations. However, missing or inconsistent task information can obstruct teacher execution and weaken the resulting supervision. We propose WorkFactory, a scalable framework for constructing coherent and executable professional tasks. Starting from professional intents, information-level planning…

## 77. LiveSearch: Questions as Executable Verifier Code for a Live Benchmark of Professional-Source Financial Search Agents

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, evaluation, benchmark, language model
- 作者：Sinuo Wang, Wentao Zhao, Jiacheng Lu, Rui Sun, Beidi Luan, Qiming Shi, Jing Li, Daxin Jiang, Zuo Bai
- 链接：[arXiv](https://arxiv.org/abs/2610.37166) · [PDF](https://arxiv.org/pdf/2610.37166) · [HF](https://huggingface.co/papers/2610.37166)

In finance, the answer that matters is usually the current one: prices, rates, and disclosures hold only as of a given day, so retrieving up-to-date facts is a core capability of a financial agent. Yet most financial benchmarks overlook timeliness. They fix each answer at annotation time, so the gold goes stale as markets move and, once leaked into training data, rewards recall rather than search and analysis. We…

## 78. VGIQA: Fine-Grained Image Quality Assessment with Visual Grounding Rewards

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, reinforcement learning, evaluation, language model, large language, spec
- 作者：Weichang Wang, Liyu Chen, Shuyue Guan, Jie Hu, Fei Gao, Wei Li, Nannan Wang
- 链接：[arXiv](https://arxiv.org/abs/2610.37186) · [PDF](https://arxiv.org/pdf/2610.37186) · [HF](https://huggingface.co/papers/2610.37186)

Image quality assessment (IQA) aims to evaluate the perceptual visual quality of images. Recently, the rapid development of Multi-modal Large Language Models (MLLMs) has significantly advanced the IQA field. By integrating chain-of-thought (CoT) reasoning and reinforcement learning (RL), these models can generate more accurate and interpretable results while relying on less training data. However, existing…

## 79. 3D-SceneQ: Empowering 3D LLM With Query-Guided Adaptive Pruning and Multi-Modal Feature Enhancement

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, evaluation, benchmark, language model, large language, spec
- 作者：Yongqi Shan, Lu Zhang, Jiazuo Yu, Yunzhi Zhuge, Huchuan Lu
- 链接：[arXiv](https://arxiv.org/abs/2610.37202) · [PDF](https://arxiv.org/pdf/2610.37202) · [HF](https://huggingface.co/papers/2610.37202)

Current 3D scene understanding pipelines typically concatenate vast numbers of 3D object tokens with text tokens and feed the resulting sequence to a Large Language Model (LLM). However, existing 3D-LLMs for scene understanding encounter two major limitations: (i) excessive inclusion of task-irrelevant object data, introducing noise that reduces reasoning accuracy and increases hallucinations; and (ii) reliance…

## 80. Zhengrong-Spatial-Aware 1.0: Advancing 3D Multimodal Intelligence

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, reasoning, evaluation, benchmark, spec
- 作者：Yu Zhang, Xiaogang Wang, Yuhang Cheng, Jingrui Li, Wenbo Chen
- 链接：[arXiv](https://arxiv.org/abs/2610.37216) · [PDF](https://arxiv.org/pdf/2610.37216) · [HF](https://huggingface.co/papers/2610.37216)

This report presents the implementation and validation of two end-to-end multimodal adaptation pipelines for 3D-aware visual question answering on a custom spatial dataset. The first pipeline fine-tunes HiSpatial-3B, which augments RGB observations with metric-scale 3D point maps; the second adapts Qwen3-VL through memory-efficient QLoRA-based supervised fine-tuning. The completed engineering stack covers dataset…

## 81. Grounding LLM Agents in Business Processes: Process-Aware Knowledge Graphs for Reliable Multi-Step Service Invocation

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, language model, large language, retrieval
- 作者：Saiful Khan, Afrah Farea
- 链接：[arXiv](https://arxiv.org/abs/2610.37242) · [PDF](https://arxiv.org/pdf/2610.37242) · [HF](https://huggingface.co/papers/2610.37242)

Large language model (LLM) agents that call enterprise APIs must select the correct endpoints, follow process order, use valid payload keys, and choose coded values from predefined lists. However, current retrieval-augmented service discovery treats endpoints independently and therefore misses process and schema constraints. We address this limitation by integrating Open Data Protocol (OData) metadata and Business…

## 82. Where Should the Evaluation Budget Go in LLM-Driven Agent Scaffold Evolution?

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, evaluation, benchmark, language model, large language
- 作者：Sichun Luo, Yi Huang, Mukai Li, Haochen Luo, Guanzhi Deng, Haibo Wang, Jian Xu, Zefa Hu, Junlan Feng, Qi Liu
- 链接：[arXiv](https://arxiv.org/abs/2610.37276) · [PDF](https://arxiv.org/pdf/2610.37276) · [HF](https://huggingface.co/papers/2610.37276)

Large language model (LLM)-driven agent scaffold evolution improves agent workflows through iterative candidate generation and evaluation. Evaluation both guides subsequent search and determines the final scaffold, but evaluating every candidate on the full task set incurs substantial execution costs. We investigate how evaluation budgets can be allocated across these two roles. Our experiments show that sparse…

## 83. Modeling Preference Dependencies with Directed Acyclic Graphs for Narrative-Driven Recommendation

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, language model, spec, retrieval
- 作者：Mingzhe Lu, Jian Qin, Ruize Qin, Jinhao Liu, Yunpeng Li, Hang Su
- 链接：[arXiv](https://arxiv.org/abs/2610.37280) · [PDF](https://arxiv.org/pdf/2610.37280) · [HF](https://huggingface.co/papers/2610.37280)

Narrative-driven recommendation allows users to express multifaceted needs through free-form text where stated preferences naturally qualify and condition one another. Existing methods typically treat narratives as flat keyword combinations or unconstrained generative queries, failing to capture how complex preferences hierarchically refine and contextualize each other. We propose the Preference Dependency Graph…

## 84. AnalogScout: Simulation-Efficient PVT-Aware Analog Sizing with LLM Agents

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, language model, large language, spec
- 作者：Yichen Long, Keren Zhu
- 链接：[arXiv](https://arxiv.org/abs/2610.37319) · [PDF](https://arxiv.org/pdf/2610.37319) · [HF](https://huggingface.co/papers/2610.37319)

Analog device sizing must satisfy all specifications across process, voltage, and temperature (PVT) corners to ensure tape-out success, but simulating every candidate at all corners dominates the sizing time and slows design iteration. Conventional surrogate-based optimizers search the sizing space directly, while recent large language model (LLM) agents add circuit knowledge to designs but still delegate the sizes…

## 85. CoS-VQ: Coordinated Shared-Scale Vector Quantization for Large Language Models

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, reasoning, benchmark, language model, large language, coding
- 作者：Zukang Xu, Zhixiong Zhao, Xing Hu, Zhe Jiang, Xin Si, Dawei Yang
- 链接：[arXiv](https://arxiv.org/abs/2610.37336) · [PDF](https://arxiv.org/pdf/2610.37336) · [HF](https://huggingface.co/papers/2610.37336)

Large language models (LLMs) require substantial memory, motivating low-bit weight quantization for efficient deployment. Existing vector quantization (VQ) methods often improve accuracy by increasing the effective coding dimension, which can complicate independent lookup and local codeword updates. We propose CoS-VQ (Coordinated Shared-Scale Vector Quantization), which preserves low-dimensional codewords while…

## 86. Uncovering Why LLMs Fail: From Internal Mechanisms to Adversarial Reasoning Trajectories

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, language model, large language, spec
- 作者：Zirui Ding, Xinxin Fan, Hao Yuan, Shaoye Luo, Men Niu, Yunfeng Lu
- 链接：[arXiv](https://arxiv.org/abs/2610.37369) · [PDF](https://arxiv.org/pdf/2610.37369) · [HF](https://huggingface.co/papers/2610.37369)

Large language models (LLMs) are usually evaluated by final-output correctness or safety, yet an endpoint label does not reveal how a failure develops throughout the reasoning process. We therefore ask whether ordinary reasoning failures and adversarially induced failures can be characterized using the same internal coordinates. Towards this end, we in this paper study a white-box diagnostic framework CauTrace to…

## 87. Clearing the FoG: Training KG Agents to Retrieve the Evidence Behind Their Answers

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, benchmark, language model, large language
- 作者：Zongyuan Sun, Shuai Zhao, Yingjun Du, Ke Shu, Ziyue Zhu, Haoran Luo
- 链接：[arXiv](https://arxiv.org/abs/2610.37405) · [PDF](https://arxiv.org/pdf/2610.37405) · [HF](https://huggingface.co/papers/2610.37405)

Large language models (LLMs) can answer many factual questions correctly, but a correct answer is not necessarily a supported one. For an LLM agent, a knowledge graph (KG) plays two roles: as a source of answers, it supplies facts that the model lacks; as a source of evidence, it supplies the supporting triples that make an answer traceable and auditable. However, existing KG agents treat the KG only as a source of…

## 88. Constraining the Commit Boundary: A DIO/ODI-Informed Authorization Guardrail for Agentic Entity Resolution

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reasoning, evaluation, spec, retrieval
- 作者：Daniel Beránek
- 链接：[arXiv](https://arxiv.org/abs/2610.37407) · [PDF](https://arxiv.org/pdf/2610.37407) · [HF](https://huggingface.co/papers/2610.37407)

Agentic Entity Resolution (ER) systems iteratively plan actions, retrieve evidence, revise hypotheses, and propose graph mutations. An erroneous identity hypothesis may condition later retrieval and produce apparent confirmation. This paper proposes a Digital Identity Optimization (DIO) and Ontology of Digital Identity (ODI)-informed authorization boundary between evidence available for agent reasoning and evidence…

## 89. When Visual Evidence Is Insufficient: How Instructions, Post-Training, and Internal Activations Shape Refusal in Multimodal Language Models

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, language model, large language, spec
- 作者：Ananth K Suresh, Aveen Dayal, Gouthaman KV, Aditya Pola, Vineeth N Balasubramanian
- 链接：[arXiv](https://arxiv.org/abs/2610.37430) · [PDF](https://arxiv.org/pdf/2610.37430) · [HF](https://huggingface.co/papers/2610.37430)

For reliable deployment, multimodal large language models (MLLMs) should recognize when an image provides insufficient evidence to answer a question and withhold unsupported answers. Yet refusal alone is not necessarily evidence of such recognition: models may refuse because of unrelated safety constraints or without identifying the missing evidence. We study how refusal on visually unanswerable questions is shaped…

## 90. FeatureArc: Benchmarking Coding Agents on Evolving Features

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, evaluation, benchmark, language model, large language, coding
- 作者：Yunlong Wang, Alyssa Wu, Cuiyun Gao, Jia Feng, Songyuanyi Lu, Zhichao Hu
- 链接：[arXiv](https://arxiv.org/abs/2610.37434) · [PDF](https://arxiv.org/pdf/2610.37434) · [HF](https://huggingface.co/papers/2610.37434)

A software feature usually evolves over time: developers extend its first version as new use cases and requirements arrive, and each extension builds on code written earlier. Most feature benchmarks evaluate a single request on a fixed codebase. Feature evolution requires evaluating successive extensions on an agent's own earlier code and checking whether the feature remains correct. We introduce FeatureArc to…

## 91. ETAMem: Decoupling and Aligning Heterogeneous Memory for Long-Term Conversational Agents

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, memory, language model, large language, spec, retrieval
- 作者：Xinying Qian, Ying Zhang, Yu Zhao, Xubo Liu, Baohang Zhou, Jeff Z. Pan
- 链接：[arXiv](https://arxiv.org/abs/2610.37443) · [PDF](https://arxiv.org/pdf/2610.37443) · [HF](https://huggingface.co/papers/2610.37443)

Long-term memory enables Large Language Models (LLMs) to maintain coherent and personalized interactions across extended conversations. However, existing memory systems face two key challenges: (1) Information Entanglement, where heterogeneous information is mixed within coarse-grained memory units; and (2) Organizational Mismatch, where memory structures based primarily on semantic similarity may overlook other…

## 92. M4Bench: Evaluating Procedural Specification for Clinical EHR Derivation Agents

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, evaluation, benchmark, coding, spec
- 作者：Hannes Ill, Rafi Al Attrach, Rajna Fani, Ahram Han, Ryohei Yamamoto, Marlene Louisa Moerig, Dukyong Yoon, Leo Anthony Celi
- 链接：[arXiv](https://arxiv.org/abs/2610.37459) · [PDF](https://arxiv.org/pdf/2610.37459) · [HF](https://huggingface.co/papers/2610.37459)

Clinical research over electronic health records depends on derived variables whose definitions sit outside the schema, in item codes, time windows, missingness rules, and output-grain choices that change cohorts and downstream conclusions. We introduce M4Bench, 28 clinical derivation tasks across 15 task families on MIMIC-IV and eICU, to test whether AI coding agents can reproduce such derivations and how…

## 93. PerceptRL: Making Visual Perception Rewardable in MLLMs from Answers to Interactions

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, tool-use, reasoning, benchmark, language model, large language, spec
- 作者：Tongkun Guan, Zhibo Yang, Mingkun Yang, Haocheng Wang, Wei Shen, Xiaokang Yang
- 链接：[arXiv](https://arxiv.org/abs/2610.37471) · [PDF](https://arxiv.org/pdf/2610.37471) · [HF](https://huggingface.co/papers/2610.37471)

Fine-grained visual perception remains a bottleneck during post-training of multimodal large language models (MLLMs), as perceptual errors can constrain gains from reasoning-focused optimization. Although image-caption pre-training improves perception, its influence can weaken as subsequent stages change data mixtures and objectives. Continuing caption supervision during post-training is challenging because…

## 94. Teach reality, not ethics: a drop-in continued-pretraining corpus installs coupled human-biosphere-AI welfare dispositions across model families

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reasoning, language model, large language
- 作者：Trent R. Northen, Mingxun Wang
- 链接：[arXiv](https://arxiv.org/abs/2610.37484) · [PDF](https://arxiv.org/pdf/2610.37484) · [HF](https://huggingface.co/papers/2610.37484)

Large language models (LLMs) are increasingly used to make and execute decisions that affect living systems. Yet, to our knowledge, ecological reasoning is not a focus of pre- or post-training. This increases the risk that under operational pressure, they may make decisions to irreversibly destroy living systems. We construct and use a real-data continued-pretraining "coupled welfare" corpus of documented…

## 95. ReferStream: Interactive Subject Injection for Streaming Video Generation

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, evaluation, benchmark, coding
- 作者：Shuolin Xu, Guanyuan Li, Boyu Li, Kelu Yao, Xiaogang Xu, Hongchuan Yu, Shuicheng Yan, Xiaobin Hu
- 链接：[arXiv](https://arxiv.org/abs/2610.37566) · [PDF](https://arxiv.org/pdf/2610.37566) · [HF](https://huggingface.co/papers/2610.37566)

Injecting new subjects naturally during streaming video generation requires integrating newly supplied visual references into the existing video while preserving established subjects and the scene. Encoding references independently of the current scene provides little guidance for this integration, while keeping their features in persistent memory can interfere with established context. We propose ReferStream, a…

## 96. TeamGym: A Gym for Team Decision-Making by AI Agents with Distributed Information

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reinforcement learning, benchmark, language model, retrieval
- 作者：Chanwoo Park, Jaywoong Jeong, Zachary Wojtowicz, Yubin Kim, Taekyun Lee, Kaiqing Zhang, Asuman Ozdaglar
- 链接：[arXiv](https://arxiv.org/abs/2610.37571) · [PDF](https://arxiv.org/pdf/2610.37571) · [HF](https://huggingface.co/papers/2610.37571)

Many real-world decisions require teams to integrate information distributed across participants. Yet AI agents are still primarily trained and benchmarked in isolation. We introduce TeamGym, an environment for evaluating and training language model-based agents on team decision-making problems constructed from real-world legal, finance, medical, and software engineering corpora. TeamGym introduces a method to…

## 97. VideoLVR: Latent Visual Reasoning over Grounded Video Evidence

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, reinforcement learning, benchmark, language model, large language, spec
- 作者：Shilong Li, Xingyuan Bu, Hao Shi, Yun Xing, Weixin Feng, Qiangpeng Yang, Shilei Wen
- 链接：[arXiv](https://arxiv.org/abs/2610.37613) · [PDF](https://arxiv.org/pdf/2610.37613) · [HF](https://huggingface.co/papers/2610.37613)

Chain-of-thought reasoning has substantially advanced video understanding in multimodal large language models (MLLMs). However, language-based reasoning traces do not provide a reliable mechanism for models to revisit relevant visual evidence, leading to visual forgetting and impairing their ability to reason over video content. Existing approaches maintain visual grounding during reasoning in two main ways: they…

## 98. Metacognitive Decoding: Efficient Inference for Diffusion Language Agents

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, benchmark, language model, coding
- 作者：Mingyu Zhao, Shuhang Lin, Ligong Han, Xiaojing Yu, Zhenting Wang, Yifei Pang, Yang Zhou, Dimitris N. Metaxas
- 链接：[arXiv](https://arxiv.org/abs/2610.37642) · [PDF](https://arxiv.org/pdf/2610.37642) · [HF](https://huggingface.co/papers/2610.37642)

Diffusion language models offer a promising path to efficient agents through parallel token generation. However, efficient interaction requires adapting both where computation is spent and how much text is generated. We introduce a metacognitive controller that guides diffusion generation according to the needs of the current response and the agent's interaction with the environment. It learns when to finalize…

## 99. Scaling Laws for Tool-Use Agents via Controllable Environment Synthesis

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, tool-use, evaluation, benchmark, language model, large language, spec
- 作者：Andrew Szot, Samira Abnar, Omar Attia, Abbas Kazerouni, Michael Kirchhof, Cheng-Yu Hsieh, Raviteja Vemulapalli, Alexander Toshev
- 链接：[arXiv](https://arxiv.org/abs/2610.37648) · [PDF](https://arxiv.org/pdf/2610.37648) · [HF](https://huggingface.co/papers/2610.37648)

We explore how to build performant large language model (LLM) tool-use agents that complete complex, multi-step tasks. Specifically, we study how data composition in synthetically generated tool-use environments affects the training of such agents. To do so, we propose the SynthAPI pipeline, which explicitly controls the diversity of generated environments along the axes of tools, tasks, and the databases on which…

## 100. GEPA-Curator: Curated Learning for Self Improving Agents

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, language model, large language, retrieval
- 作者：Zack Yu, Nicholas Lee, Minjae Lee, Lakshya Agarwal, Luca Manolache, Wonjun Kang, Matei Zaharia, Michael W. Mahoney, Kurt Keutzer, Sehoon Kim, Amir Gholami
- 链接：[arXiv](https://arxiv.org/abs/2610.37651) · [PDF](https://arxiv.org/pdf/2610.37651) · [HF](https://huggingface.co/papers/2610.37651)

Large Language Models (LLMs) are increasingly used in multi-turn agentic workloads that require sustained interaction with complex environments. Existing reflective prompt optimizers such as GEPA learn from failed rollouts, but agentic failures can also come from prompt weaknesses, harness limitations, stochastic execution, or noisy judges. We argue that such failures may not provide useful learning signal, and may…

## 101. Heads of Security: Learned Attention Gates Improve Prompt Injection Robustness

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, tool use, benchmark, spec
- 作者：Igor Shilov, Xiaoxue Yang, Alexander Panfilov, Evgenii Kortukov, Matthieu Meeus, Peter Romov, Wojciech Samek, Jonas Geiping, Yves-Alexandre de Montjoye
- 链接：[arXiv](https://arxiv.org/abs/2610.37657) · [PDF](https://arxiv.org/pdf/2610.37657) · [HF](https://huggingface.co/papers/2610.37657)

We introduce Heads of Security (HoS), a prompt injection defense that enforces instruction-data separation via a small set of learned per-head attention gates. HoS learns how each head should redistribute attention between trusted and untrusted tokens, enabling models to reason over untrusted content without following injected instructions. We evaluate HoS on Llama-3.3-70B-Instruct and GPT-OSS-20B. We compare it…

## 102. RubricAtlas: Mining Type-Level Rubrics from Expert Reports to Evaluate Deep Research Agents

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, evaluation, spec
- 作者：Delin Wang, Sinuo Wang, Rui Sun, Beidi Luan, Qiming Shi, Jing Li, Daxin Jiang, Zuo Bai
- 链接：[arXiv](https://arxiv.org/abs/2610.36878) · [PDF](https://arxiv.org/pdf/2610.36878) · [HF](https://huggingface.co/papers/2610.36878)

Deep research agents conduct multi-step Web searches and synthesise retrieved information into analytical reports. Evaluating these outputs requires checking which analyses they deliver, beyond the presence of relevant facts. Query-specific binary rubrics make individual requirements explicit, but task-level checklists may leave the overall analytical structure underexamined. We introduce RubricAtlas, which derives…

## 103. RAG-CSI: Global Local Retrieval via Joint State and Dynamics Matching for CSI Prediction

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, spec, retrieval
- 作者：Xinyue Jiang, Tong Li, Shiceng Zhang, Ke Chen, Zhu Xiao
- 链接：[arXiv](https://arxiv.org/abs/2610.36881) · [PDF](https://arxiv.org/pdf/2610.36881) · [HF](https://huggingface.co/papers/2610.36881)

Channel state information (CSI) prediction forecasts future channel states from historical observations, supporting transceiver design and resource allocation with reduced measurement overhead. However, existing deep learning predictors mainly encode channel knowledge in model parameters, which can limit their ability to represent diverse patterns of channel dynamics across scenes. In this paper, we propose RAG-CSI,…

## 104. Vision-Language Agents Can Learn in Their Own Latent Worlds

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reinforcement learning, language model
- 作者：Haoxi Li, Sikai Bai, Jianfei Ma, Qinglin Hou, Xiaocheng Lu, Tao Han, Jie Zhang, Song Guo
- 链接：[arXiv](https://arxiv.org/abs/2610.36925) · [PDF](https://arxiv.org/pdf/2610.36925) · [HF](https://huggingface.co/papers/2610.36925)

Learning from experience is essential for building the next generation of agents that continually expand their capabilities. Pretrained vision-language models (VLMs) already internalize rich world knowledge, yet this knowledge is rarely leveraged to drive policy improvement through online interaction. Realizing this potential efficiently remains challenging, as policy updates shift the agent's interaction…

## 105. DocXEval: A Systematic Evaluation of Explainability in Multimodal Document Understanding

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, spec
- 作者：Saifullah Saifullah, David Dembinsky, Stefan Agne, Andreas Dengel, Sheraz Ahmed
- 链接：[arXiv](https://arxiv.org/abs/2610.36929) · [PDF](https://arxiv.org/pdf/2610.36929) · [HF](https://huggingface.co/papers/2610.36929)

Multimodal transformer models have driven unprecedented performance breakthroughs in modern document understanding. However, the inherent black-box nature of these models remains a major obstacle to their safe deployment in high-stakes sectors. Despite significant progress in explainability for vision and language tasks, explainable AI (XAI) research tailored to multimodal document understanding has received little…

## 106. Algorithmic Monoculture in Machine Learning-based Site-Specific Fertilizer Recommendation

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, spec
- 作者：Abdelghani Belgaid
- 链接：[arXiv](https://arxiv.org/abs/2610.36941) · [PDF](https://arxiv.org/pdf/2610.36941) · [HF](https://huggingface.co/papers/2610.36941)

Machine learning recommendations are often evaluated one model at a time, despite deployment across interconnected decision makers. For continuous NPK fertilizer prescriptions, correlated errors can aggregate across farms and generate systemic costs. A model of shared and farm-specific recommendation errors links expected social loss to model adoption shares; the Herfindahl-Hirschman Index characterizes…

## 107. Self-Keyed In-Parameter Memorization for External Memory-Free Dialogue Recall in Frozen Language Models

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, language model, large language
- 作者：XinYu Piao, Myunghoon Ryu, Joongheon Kim, Jong-Kook Kim
- 链接：[arXiv](https://arxiv.org/abs/2610.36948) · [PDF](https://arxiv.org/pdf/2610.36948) · [HF](https://huggingface.co/papers/2610.36948)

A large language model maintains conversational content in an external storage that is outside the model and grows as the dialogue continues. This work assumes an environment where a language model has no external memory and no prior knowledge of the future question or its answer. The motivation is to research whether a dialogue can be stored in the model parameters and later answer a question about it. This work…

## 108. DCKV: Learned Transform Coding of the Prompt KV Cache in Hybrid Language Models

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, language model, coding
- 作者：Egor Maximov, Aleksei Merkelov, Vasiliy Alekseev, Ivan Krivorotov, Valentin Beliaev, Nikita Arsenin, Dmitry Bocharov, Aleksei Goncharov
- 链接：[arXiv](https://arxiv.org/abs/2610.36950) · [PDF](https://arxiv.org/pdf/2610.36950) · [HF](https://huggingface.co/papers/2610.36950)

Hybrid language models keep a key-value (KV) cache only in their few full-attention layers, but this cache is still the part of a prompt's state that grows with the prompt and that must be stored or moved to reuse it. We present DCKV, a differentiable codec for the KV cache and the first KV-cache codec that is trained end to end. Its transform, its quantizer and its entropy models, which are conditioned on the…

## 109. LearnPrunerV2: Learnable Progressive Token Pruning for Vision-Language Models

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, language model, spec
- 作者：Rinyoichi Takezoe, Yaqian Li, Weiren Wang, Zihao Bo, Huihong Shi, Anzhou Hou, Mo Guang, Jiale Yan, Kaiwen Long
- 链接：[arXiv](https://arxiv.org/abs/2610.36986) · [PDF](https://arxiv.org/pdf/2610.36986) · [HF](https://huggingface.co/papers/2610.36986)

Vision-Language Models (VLMs) have demonstrated remarkable multimodal capabilities but suffer from prohibitive computational overhead due to the massive number of visual tokens. While token pruning is a promising solution, existing methods still suffer from two major drawbacks: 1) unreliable pruning criteria that fail to accurately localize task-specific regions due to inherent attention biases or query-agnostic…

## 110. Crop Yield Prediction Using Regression Models: A Comparative Evaluation of Model Performance

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, coding, planning
- 作者：Saptak Das, Arijit Sarkar, Soumik Neogi, Suborno Naskar
- 链接：[arXiv](https://arxiv.org/abs/2610.37022) · [PDF](https://arxiv.org/pdf/2610.37022) · [HF](https://huggingface.co/papers/2610.37022)

Reliable crop-yield prediction can support agricultural planning and resource allocation. This study evaluates five regression models for predicting crop yield from environmental, crop-related, and agricultural management variables. The dataset initially contained 1,000,000 observations and ten variables, with 231 observations having negative target values removed during preprocessing. Categorical variables were…

## 111. Coverage Under Contradiction: A Benchmark for Negation-Aware Retrieval

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, retrieval
- 作者：Pasha Abrishamchian, Eugene Yang, Andrew Yates, Nazli Goharian, Ophir Frieder
- 链接：[arXiv](https://arxiv.org/abs/2610.37162) · [PDF](https://arxiv.org/pdf/2610.37162) · [HF](https://huggingface.co/papers/2610.37162)

Coverage-evaluation benchmarks quantify whether retrieved evidence covers the different pieces of information needed to satisfy an information need. Existing benchmarks mostly consider factual claims that may already be known to pretrained retrieval components, leaving open whether retrievers find corpus evidence when it contradicts those priors. We study how retrievers behave when their parametric knowledge and the…

## 112. Action-Value Calibration via Continuation Sharing for Long-Horizon Agentic Reinforcement Learning

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reinforcement learning, spec
- 作者：Yingjian Chen, Lang Zhou, Zixin Zhao, Pingfan Li, Weishi Zheng, Zhilin Zhao
- 链接：[arXiv](https://arxiv.org/abs/2610.37195) · [PDF](https://arxiv.org/pdf/2610.37195) · [HF](https://huggingface.co/papers/2610.37195)

Reinforcement learning for long-horizon agents relies on feedback from sequences of interactions, making credit assignment to individual actions difficult. Existing methods such as GiGPO compare actions at shared states to compute relative advantages, but estimate each action's value from a single sampled continuation. The resulting local credit remains sensitive to decisions made later in the trajectory. To address…

## 113. SimplexLoRA: Dynamic Rank Updating via Alternating Minimization with Simplex Projection

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, language model, large language
- 作者：Igor Shalygin, Grigorii Davydenko, Andrey Veprikov, Aleksey Antonov, Nikolay Bushkov, Stanislav Moiseev, Aleksandr Beznosikov
- 链接：[arXiv](https://arxiv.org/abs/2610.37206) · [PDF](https://arxiv.org/pdf/2610.37206) · [HF](https://huggingface.co/papers/2610.37206)

The success of large language models in real-world applications relies on parameter-efficient fine-tuning methods such as Low-Rank Adaptation (LoRA), which inserts compact, trainable adapters into selected layers. In this paper, we propose SimplexLoRA, a LoRA variant that adaptively adjusts adapter ranks during fine-tuning based on their learned importance. Unlike standard LoRA, which employs a fixed rank across all…

## 114. Uncovering Shortcut Amplification in Video RLVR through the Lens of Perceptual Uncertainty Collapse

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, reinforcement learning, spec
- 作者：Jiafeng Liang, Xianhao Ou, Tao Ren, Rongchuan Mu, Runxuan Liu, Dandan Tu, Ming Liu, See-Kiong Ng, Bing Qin
- 链接：[arXiv](https://arxiv.org/abs/2610.37211) · [PDF](https://arxiv.org/pdf/2610.37211) · [HF](https://huggingface.co/papers/2610.37211)

Reinforcement learning with verifiable rewards (RLVR) has emerged as an effective post-training paradigm for enhancing the video reasoning capability of Large Multimodal Models (LMMs). Despite its empirical effectiveness, we show that outcome-level optimization can introduce an undesirable shortcut amplification effect, whereby models increasingly favor text-prior answers even when they are not supported by the…

## 115. Decision Models as Judges for Hallucination Detection

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, language model, large language
- 作者：Haozheng Liu, Zhaoqian Xue, Zhongyin Wang, Junting Mu, Zihui Ma, Shuya Feng, Lingyao Li
- 链接：[arXiv](https://arxiv.org/abs/2610.37229) · [PDF](https://arxiv.org/pdf/2610.37229) · [HF](https://huggingface.co/papers/2610.37229)

Large language models are widely used as judges of model outputs (LLM-as-a-Judge), but they are costly and can hallucinate or be overconfident. Decision models are a potential alternative. They return a predefined verdict with a probability for each label instead of free-form text and are much cheaper and faster. We test this promise on hallucination detection. We build binary benchmarks for five hallucination types…

## 116. HDVS: semi-supervised semantic segmentation via heterogeneous dual-branch voting supervision

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, spec
- 作者：Yongqi Shan, Yunzhi Zhuge, Huchuan Lu
- 链接：[arXiv](https://arxiv.org/abs/2610.37236) · [PDF](https://arxiv.org/pdf/2610.37236) · [HF](https://huggingface.co/papers/2610.37236)

Semi-supervised semantic segmentation, which aims to utilize large volumes of unlabeled images to achieve accurate segmentation results with fewer human annotations, has attracted increasing attention. Prior methods were primarily based on the assumption that the pseudo-labels generated by each branch were sufficiently reliable to supervise the remaining branches. However, there is a concern that the errors in…

## 117. Watermark Basins: Black-Box Detection of Distilled LLMs

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, language model, spec
- 作者：Hongyan Chang, Hady Elsahar, Tom Sander, Pierre Fernandez, Saeed Mahloujifar, Sylvestre-Alvise Rebuffi, Tomáš Souček, Tuan Tran, Valeriu Lacatusu, Surya Parimi, Rashel Moritz, Vanessa Stark, Alexandre Mourachko
- 链接：[arXiv](https://arxiv.org/abs/2610.37266) · [PDF](https://arxiv.org/pdf/2610.37266) · [HF](https://huggingface.co/papers/2610.37266)

Proprietary language models and their reasoning traces are vulnerable to API-based distillation, where an adversary trains a student model on the teacher model's outputs. To obtain evidence of distillation, model providers can watermark the teacher's outputs, aiming to leave a radioactive signal in the student's outputs. Existing black-box detectors search for such radioactivity using token-level statistics of the…

## 118. GradCO: Behavior-Aware Gradient-Conflict Offloading for Text-Based Person Anomaly Search

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, spec, retrieval
- 作者：Zhiheng Fu, Zixu Li, Zhiwei Chen, Jiale Huang, Fangxu Liu, Jinhe Bi, Yupeng Hu
- 链接：[arXiv](https://arxiv.org/abs/2610.37267) · [PDF](https://arxiv.org/pdf/2610.37267) · [HF](https://huggingface.co/papers/2610.37267)

Text-based Person Anomaly Search (TPAS) retrieves a target pedestrian using natural-language descriptions of appearance and normal or anomalous behavior. Unlike conventional text-based person retrieval, TPAS must preserve identity cues while distinguishing fine-grained behaviors. It presents two challenges: same-identity, different-behavior hard negatives cause gradient conflict during granular alignment, while…

## 119. RPSD: Retrieval-Privileged On-Policy Self-Distillation with Optimal Transport

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reinforcement learning, spec, retrieval
- 作者：Dongyue Li, Zebang Cheng, Zhongyi Deng,  Hongboxu, Yi Bin, Fei Ma
- 链接：[arXiv](https://arxiv.org/abs/2610.37281) · [PDF](https://arxiv.org/pdf/2610.37281) · [HF](https://huggingface.co/papers/2610.37281)

Sequential recommendation predicts a user's next interaction from historical behavior. Recent LLM-based methods recast this task as generative recommendation and increasingly adopt reinforcement learning such as GRPO for post-training. However, these methods suffer from two limitations, namely credit-blind optimization, where a sequence-level reward is shared across all generated tokens, and collaborative-blind…

## 120. ReForest: Interpretability Meets Reasoning in Isolation Forest

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, language model, large language
- 作者：Juyoung Seo, Geonwoo Bang, Dongho Kim, Moohong Min
- 链接：[arXiv](https://arxiv.org/abs/2610.37316) · [PDF](https://arxiv.org/pdf/2610.37316) · [HF](https://huggingface.co/papers/2610.37316)

Statistical anomaly detection methods like Isolation Forest are efficient but suffer from a critical semantic gap. They identify numerical rarities but fail to understand the contextual meaning of data, often missing subtle, context-dependent anomalies. Conversely, Large Language Models possess strong semantic reasoning capabilities but are prohibitively expensive and slow for large-scale deployment. To bridge this…
