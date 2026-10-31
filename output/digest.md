# 每日 AI 论文

生成时间：2026-10-31 05:41 UTC  ·  共 120 篇（已按 arXiv ID 去重）

来源：Hugging Face Daily Papers + arXiv（cs.AI / cs.LG / cs.CL / cs.CV）。
排序：HF 上榜、点赞、多源命中、兴趣词。兴趣词可在 `config.json` 改。

## 1. Your Benchmark Is an Empirical Measure Over Difficulty

- 分数：34.0  ·  HF 赞：140  ·  来源：huggingface
- 兴趣命中：evaluation, benchmark, spec
- 作者：Yifan Sun, Naicheng Yu, Jiawen Gong, Jingyan Shen, Huan Zhang
- 链接：[arXiv](https://arxiv.org/abs/2610.29927) · [PDF](https://arxiv.org/pdf/2610.29927) · [HF](https://huggingface.co/papers/2610.29927)

A benchmark is not merely a collection of test questions; it naturally induces an empirical measure over difficulty. In this work, we develop this measure-based view of benchmark evaluation. This perspective allows us to identify and formalize two central failure modes: measure mismatch, where the benchmark difficulty distribution differs from the intended difficulty distribution, and coverage gaps, where uncovered…

## 2. Look Only When Needed: Certificate-Guided Visual Routing for Efficient Diffusion VLMs

- 分数：34.0  ·  HF 赞：91  ·  来源：huggingface
- 兴趣命中：benchmark, language model, coding
- 作者：Donghyeon Cho, Joowon Kim, Seungho Shin, Eunho Yang
- 链接：[arXiv](https://arxiv.org/abs/2610.36671) · [PDF](https://arxiv.org/pdf/2610.36671) · [HF](https://huggingface.co/papers/2610.36671)

Diffusion vision-language models (DVLMs) process their entire input at every denoising step. Since visual tokens make up 89-97% of this input on the benchmarks we study, most of the decoding computation is spent repeatedly processing the same image. Visual token pruning methods partially relieve this burden by removing part of the visual tokens, but they lose the removed information and still process the remaining…

## 3. L3G-World: Real-Time Infinite World Generation with Latent 3D Gaussian Memory

- 分数：33.5  ·  HF 赞：35  ·  来源：huggingface + arxiv
- 兴趣命中：memory, coding
- 作者：Jinhyeok Choi, JoungBin Lee, Jongmin Lee, Minkyeong Jeon, Jiyoung Kim, Kaeun Han, Yoonjin Yoon, Seungryong Kim
- 链接：[arXiv](https://arxiv.org/abs/2610.40614) · [PDF](https://arxiv.org/pdf/2610.40614) · [HF](https://huggingface.co/papers/2610.40614)

Interactive world models generate visual content conditioned on user actions, yet maintaining spatial consistency over long-horizon exploration in real time remains challenging. Existing approaches rely on either temporal context or explicit 3D memory, both of which scale poorly because memory grows with the length of the generated stream. Moreover, explicit 3D memories condition latent video generators by…

## 4. Intrinsic Distribution Matching

- 分数：32.0  ·  HF 赞：239  ·  来源：huggingface
- 兴趣命中：evaluation, spec
- 作者：Deyuan Liu, Yansen Han, Kaiwen Zheng, Jun Xie, Jiacheng Liu, Zhenglin Cheng, Peng Sun, Jintao Zhang, Jianguo Li, Tao Lin
- 链接：[arXiv](https://arxiv.org/abs/2610.39633) · [PDF](https://arxiv.org/pdf/2610.39633) · [HF](https://huggingface.co/papers/2610.39633)

One-step and few-step text-to-image generation must accurately render the details specified in the prompt despite limited opportunities for refinement. Distribution matching distillation (DMD) uses score differences to bring the generated distribution closer to a reference distribution. Following prior work, we estimate this difference with internal velocity branches, avoiding a separate fake-score network. We ask…

## 5. A-RSI: Adaptive Task Refresh for Zero-Data Multimodal Self-Improvement

- 分数：32.0  ·  HF 赞：151  ·  来源：huggingface
- 兴趣命中：benchmark, spec
- 作者：Yu Liu, Youxing Li, Yuedong Tan, Zhiwei Yang, Zihan Su, Hanqi Feng, Shaojie Zhang, Libin Liao, Zihao Wan, Chenxu Wu, Cong Cao, Fangfang Yuan, Yanbing Liu, Ziheng Chen, Pei Fu, Radu Timofte, Zongwei Wu, Nicu Sebe, Barnabas Poczos, Jian Luan
- 链接：[arXiv](https://arxiv.org/abs/2610.38568) · [PDF](https://arxiv.org/pdf/2610.38568) · [HF](https://huggingface.co/papers/2610.38568)

Recursive self-improvement requires models not only to acquire useful training experience, but also to decide when their current experience has ceased to be useful. Existing methods often focus on what experience to generate next, while paying less attention to when fresh experience should be introduced. Many also construct training targets through self-consistency or majority voting, making supervision depend on…

## 6. Youtu-Parsing-Omni: One Encoder, One Schema, All Modalities

- 分数：32.0  ·  HF 赞：119  ·  来源：huggingface
- 兴趣命中：agent, language model
- 作者：Yunhang Shen, Zhangquan Chen, Xiaotian Li, Zhongpeng Cai, Qing Zhou, Zekai Zhang, Kun Zhang, Zezhong Wu, Jian Hu, Haihan Gao, Heting Gao, Xin Li, Yinsong Liu, Deqian Jiang, Di Yin, Haoyu Cao, Xing Sun, Bing Liu, Yanqiu Qu, Yunfei Wu, Kun Yin, Zhixiang Wei, Yongxiang Hua, Qianyu Li, Xiaoxing Hu, Peiyuan Zhang, Lijiang Li, Dong Xu, Zhenchuan Yang, Yiliang Jiang
- 链接：[arXiv](https://arxiv.org/abs/2610.39301) · [PDF](https://arxiv.org/pdf/2610.39301) · [HF](https://huggingface.co/papers/2610.39301)

We present Youtu-Parsing-Omni, an omni-modal parser that converts documents, images, audio, and video into structured records grounded in space and time, providing a perception layer for agents that read, locate, and cite evidence across modalities. Its design rests on one encoder for every modality and one schema for every task. Youtu-Omni-Encoder, initialized from a pre-trained language model to strengthen text…

## 7. Proving and Improving the Platonic Representation Hypothesis with JEPAs

- 分数：32.0  ·  HF 赞：54  ·  来源：huggingface
- 兴趣命中：benchmark, language model
- 作者：Randall Balestriero, Yann LeCun
- 链接：[arXiv](https://arxiv.org/abs/2610.39302) · [PDF](https://arxiv.org/pdf/2610.39302) · [HF](https://huggingface.co/papers/2610.39302)

Whether models trained on different modalities converge to the same representation of the world is central to AI. The Platonic Representation Hypothesis (PRH) conjectures that they do as they scale, but without a proof it offers neither a guarantee nor a recipe. We turn the hypothesis into a theorem. First, we prove a Platonic Representation Theorem: Joint-Embedding Predictive Architectures (JEPAs) trained…

## 8. Read, Allocate, Route: Role-Coupled Tokenization for Pixel-Space Generative Transformers

- 分数：32.0  ·  HF 赞：36  ·  来源：huggingface + arxiv
- 兴趣命中：spec
- 作者：Jiongfan Yang, Weichen Fan, Haiwen Diao, Zhongang Cai, Ziwei Liu
- 链接：[arXiv](https://arxiv.org/abs/2610.40647) · [PDF](https://arxiv.org/pdf/2610.40647) · [HF](https://huggingface.co/papers/2610.40647)

Pixel-space generative Transformers typically use one token per image patch, so capturing finer detail requires more tokens and makes global attention increasingly expensive. We observe that finer detail does not necessarily require more global communication: low-frequency structure benefits from global exchange, while high-frequency detail can be modeled locally. Based on this insight, we introduce SpecSlot, a…

## 9. WorkFactory: Turning Professional Intents into Executable Work for Scalable Agent Training

- 分数：31.0  ·  HF 赞：30  ·  来源：huggingface
- 兴趣命中：agent, benchmark, spec, planning
- 作者：Ziyang Zeng, Tingyang Chen, Jia Deng, Qiyao Wang, Shuo Tang, Yike Yang, Tao Ren, Wayne Xin Zhao, Feng Chang, Jujie He, Chuan Hao, Ran Tao, Bryan Dai
- 链接：[arXiv](https://arxiv.org/abs/2610.37161) · [PDF](https://arxiv.org/pdf/2610.37161) · [HF](https://huggingface.co/papers/2610.37161)

Scaling supervised training for working agents requires diverse professional tasks that yield reliable expert demonstrations. However, missing or inconsistent task information can obstruct teacher execution and weaken the resulting supervision. We propose WorkFactory, a scalable framework for constructing coherent and executable professional tasks. Starting from professional intents, information-level planning…

## 10. A Broader Look into MLLM's Retrieval Heads

- 分数：28.0  ·  HF 赞：28  ·  来源：huggingface
- 兴趣命中：language model, large language, retrieval
- 作者：Jia Wang, Yuqing Li, Jiangnan Li, Zheng Lin, Mo Yu
- 链接：[arXiv](https://arxiv.org/abs/2610.32411) · [PDF](https://arxiv.org/pdf/2610.32411) · [HF](https://huggingface.co/papers/2610.32411)

Locating relevant evidence in long inputs is a core capability of Multimodal Large Language Models. Prior studies attribute this capability to retrieval heads, a sparse set of attention heads that transfer information from the context to the output. However, these analyses are confined to a limited set of modalities and the corresponding models. Moreover, how retrieval heads can be leveraged to enhance the model…

## 11. VibeGame: Prompt-to-Game Development with AI-Native Engine and Self-Evolving Adversarial Agent Team

- 分数：26.0  ·  HF 赞：20  ·  来源：huggingface
- 兴趣命中：agent, language model, large language, spec
- 作者：Wenbo Hu, Ken Li, Jiazhe Wei, Yukang Cao, Weiyi Hong, Jiayi Dai, Chenjun Bai, Jiajun Liang, Yucheng Liao, Ruichuan An, Zeyu Lou, Haofan Wang, Yueming Lyu, Jingkang Yang, Ziwei Liu, Chenyang Si
- 链接：[arXiv](https://arxiv.org/abs/2610.33106) · [PDF](https://arxiv.org/pdf/2610.33106) · [HF](https://huggingface.co/papers/2610.33106)

Large language model agents have enabled software development through natural-language interaction, but extending this paradigm to end-to-end game development remains challenging. Building a playable game requires coordinating code, scenes, assets, animations, physics, and configurations, while allowing developers to validate their integrated behavior through interactive testing. We introduce VibeGame, a framework…

## 12. Co-Design Bench: Multimodal Collaborative Coding Evaluation for Agentic Models

- 分数：25.5  ·  HF 赞：19  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark, coding
- 作者：Xilin Wei, Shengyuan Ding, Xinyu Fang, Tiancheng Gu, Yuchi Wang, Zhixun Li, Ziyu Liu, Yuhang Zang, Weixiang Yu, Cheng Lu, Chonggao Sun, Tong Zhou, Dahua Lin, Hang Zhang, Shuai Bai, Dayiheng Liu
- 链接：[arXiv](https://arxiv.org/abs/2610.35138) · [PDF](https://arxiv.org/pdf/2610.35138) · [HF](https://huggingface.co/papers/2610.35138)

Evaluating human-AI co-design requires testing whether coding agents can translate real users' multimodal requests into working application revisions. We introduce Co-Design Bench, a reference-free benchmark of 273 tasks curated from 37,463 deduplicated queries across 26,314 real user coding sessions. Its two tracks, Multimodal Editing (ME) and Repository Editing (RE), cover localized edits with optional image,…

## 13. Glance: The Generator Is Its Own Reranker

- 分数：23.0  ·  HF 赞：10  ·  来源：huggingface + arxiv
- 兴趣命中：memory, evaluation, retrieval
- 作者：Adilet Metinov, Chingiz Arziev
- 链接：[arXiv](https://arxiv.org/abs/2610.40454) · [PDF](https://arxiv.org/pdf/2610.40454) · [HF](https://huggingface.co/papers/2610.40454)

Retrieval-augmented generation commonly serves separate models for reranking and answering, duplicating model residency and passage processing. We introduce Glance, which equips the generator with a lightweight decision adapter and pointer head to score candidate passages from a shared prefill. Short relevance probes branch from the cached context, producing one score per passage without separately prefilling each…

## 14. HairDeck: Animation-Ready Stylized Hair Cards from a Single Image

- 分数：21.0  ·  HF 赞：18  ·  来源：huggingface + arxiv
- 兴趣命中：-
- 作者：Yuze He, Yixiang Wei, Wang Zhao, Chuhao Chen, Yanning Zhou, Yong-Jin Liu
- 链接：[arXiv](https://arxiv.org/abs/2610.40599) · [PDF](https://arxiv.org/pdf/2610.40599) · [HF](https://huggingface.co/papers/2610.40599)

The hair of stylized characters in games and avatars is built from hair cards: artist-placed ribbons whose geometry is the visible hair, animated by spring bones. Existing image-based methods produce realistic hair or a single fused mesh, while CHARM, the only generator of stylized hair cards, decodes a hairstyle autoregressively as a long sequence of control points. Observing that a card hairstyle is an unordered…

## 15. IntReal: A Real-World Dataset and Benchmark for Multimodal Interleaved Generation

- 分数：21.0  ·  HF 赞：14  ·  来源：huggingface
- 兴趣命中：evaluation, benchmark, spec
- 作者：Shaohan Yu, Jie Qin, Wende Tan, Haiwen Diao, Limeng Qiao, Yueming Lyu, Chenyang Si
- 链接：[arXiv](https://arxiv.org/abs/2610.38425) · [PDF](https://arxiv.org/pdf/2610.38425) · [HF](https://huggingface.co/papers/2610.38425)

Humans routinely consume multimodal content, where textual and visual information is naturally interleaved. Although Unified Multimodal Models (UMMs) can jointly generate text and images, multimodal interleaved generation remains largely underexplored. Progress in this area is hindered by two key limitations: (1) the lack of well-defined interleaved generation tasks and corresponding training data, and (2) the…

## 16. Investor's Last Exam: Can AI Agents Do Equity Investment Without Seeing the Future?

- 分数：21.0  ·  HF 赞：10  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark, retrieval
- 作者：Huangfei Jiang, Anning Hu, Kai Sheng, Yuchen Cai, Rui Ge, Xiangyu Kong, Jianghao Lin, Shuzi Chen, Jiyi Weng, Junchi Yan
- 链接：[arXiv](https://arxiv.org/abs/2610.38342) · [PDF](https://arxiv.org/pdf/2610.38342) · [HF](https://huggingface.co/papers/2610.38342)

Financial agents must form forecasts and investment judgments from decision-time evidence, with predictions evaluated against subsequent outcomes. Existing benchmarks assess financial knowledge, research workflows, or forecasting, but evaluating the full research process requires a strictly frozen information set and professional evaluation criteria. We introduce Investor's Last Exam (ILE), an equity-research…

## 17. AskStream: When and What to Ask Proactively under Uncertainty in Streaming Video Understanding

- 分数：21.0  ·  HF 赞：10  ·  来源：huggingface
- 兴趣命中：agent, benchmark, language model, large language
- 作者：Lu Wang, Zhuoran Jin, Longxiang Wang, Junhong Chen, Yupu Hao, Yao Xu, Daojian Zeng, Yubo Chen, Kang Liu, Guang Liu, Jun Zhao
- 链接：[arXiv](https://arxiv.org/abs/2610.38678) · [PDF](https://arxiv.org/pdf/2610.38678) · [HF](https://huggingface.co/papers/2610.38678)

Recent advances in multimodal large language models have increased interest in interaction paradigms for video understanding. The evolution from offline to streaming and proactive interaction has gradually shifted models from passive responders toward more proactive agents that can decide when to answer. However, existing proactive paradigms typically assume that the information required to answer a query is…

## 18. WebAnything: From the Wild Web to Scalable Agent Environments

- 分数：19.5  ·  HF 赞：11  ·  来源：huggingface
- 兴趣命中：agent, evaluation, spec
- 作者：Tianci Xie, Zikun Cai, Chaoyun Zhang, Pinxue Guo, Bingxuan Li, Rui Zheng, Hang Yan
- 链接：[arXiv](https://arxiv.org/abs/2610.37786) · [PDF](https://arxiv.org/pdf/2610.37786) · [HF](https://huggingface.co/papers/2610.37786)

Web agents require diverse, executable, and resettable website environments for reproducible training and evaluation. Human-assisted mirrors demand per-site engineering, while generative construction can diverge from specified real websites. Capture-and-replay preserves observations, with interaction coverage constrained by captured content and replay capabilities.   We present WebAnything, a fully automated…

## 19. Multi-Token Prediction Done Right

- 分数：19.5  ·  HF 赞：11  ·  来源：huggingface
- 兴趣命中：reasoning, coding, spec
- 作者：Jayden Teoh
- 链接：[arXiv](https://arxiv.org/abs/2610.38331) · [PDF](https://arxiv.org/pdf/2610.38331) · [HF](https://huggingface.co/papers/2610.38331)

Multi-Token Prediction (MTP) is now a common ingredient in language-model pre-training, as it improves downstream performance and enables faster inference through speculative decoding. We identify a flaw in standard MTP training, in which a residual component of the MTP gradient interferes with both next-token and multi-token learning, increasingly so with scale. Specifically, the MTP cross-entropy gradient can be…

## 20. Online Dense Reinforcement Learning with Planning-Grounding Agent for UI Navigation on Live IOS Apps

- 分数：19.5  ·  HF 赞：7  ·  来源：huggingface
- 兴趣命中：agent, reinforcement learning, evaluation, benchmark, language model, spec, planning
- 作者：Peitong Duan, Khashayar Gatmiry, Jeffrey Nichols, Samy Bengio, Emmanuel Abbe
- 链接：[arXiv](https://arxiv.org/abs/2610.39264) · [PDF](https://arxiv.org/pdf/2610.39264) · [HF](https://huggingface.co/papers/2610.39264)

While frontier vision-language models demonstrate strong capabilities in user interface (UI) navigation, their high inference costs prohibit everyday use. Conversely, smaller models trained via supervised fine-tuning (SFT) or offline reinforcement learning often memorize static trajectories, leading to brittle execution and an inability to recover from errors. To address these limitations, we propose a novel online…

## 21. WeVisCut: The Whole Editing Room in One Agent From Narration to Long-Form Video

- 分数：19.0  ·  HF 赞：14  ·  来源：huggingface
- 兴趣命中：agent, benchmark
- 作者：Chenyu Mu, Wenming Weng, Qinrui Wang, Xingsong Ye, Hao Yu, Jun He, Chong Sun, Chen Li, Jing Lyu, Erkun Yang, Cheng Deng
- 链接：[arXiv](https://arxiv.org/abs/2610.38352) · [PDF](https://arxiv.org/pdf/2610.38352) · [HF](https://huggingface.co/papers/2610.38352)

Producing long-form videos from narration requires interdependent decisions that remain coherent across shots. Existing agentic editors often use multi-stage workflows driven by general models, leaving the quality-cost trade-off of compact, task-adapted policies unclear. We address this gap with WeVisCut, a long-form script-to-video system that connects tool execution with policy learning. Its agent harness…

## 22. EditAgent: Rethinking Agentic Image Editing

- 分数：18.5  ·  HF 赞：9  ·  来源：huggingface
- 兴趣命中：agent, benchmark, spec
- 作者：Haiyang Xu, Tianyu Wang, Jialu Li, Jiteng Mu, Yuanjun Xiong, Jianming Zhang, Zhuowen Tu, Mingze Xu
- 链接：[arXiv](https://arxiv.org/abs/2610.39664) · [PDF](https://arxiv.org/pdf/2610.39664) · [HF](https://huggingface.co/papers/2610.39664)

Agentic image editors decompose complex requests into steps, but when a step fails, they mostly retry with the same narrow set of tools and a judge that scores each output by eye directly. We argue that such agents are bounded by two spaces: the action space of what the agent can do, and the observation space of what its judge can see. On our expert-annotated benchmark, a general-purpose editor yields no usable…

## 23. PhysInsert: Physically Plausible Object Insertion with Geometric Priors and Bidirectional Object-Scene Interactions

- 分数：18.0  ·  HF 赞：8  ·  来源：huggingface + arxiv
- 兴趣命中：spec
- 作者：Yue Gong, Le Zhang, Rui Chen, Song Chang, Xiaochao Qu, Luoqi Liu, Ting Liu, Yebin Liu
- 链接：[arXiv](https://arxiv.org/abs/2610.40453) · [PDF](https://arxiv.org/pdf/2610.40453) · [HF](https://huggingface.co/papers/2610.40453)

We present PhysInsert, a framework for physically plausible reference-based object insertion that jointly adapts objects and their surrounding scenes. Existing methods often rely on masked inputs, generation-based pairs, or training pairs with limited viewpoint variation, leaving pose and illumination adaptation and bidirectional object-scene interactions insufficiently constrained. We construct the Insert World…

## 24. SO-101 Bench: Accessible Spatial Manipulation

- 分数：18.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：agent, memory, evaluation, benchmark, language model, planning
- 作者：Truman Hickok
- 链接：[arXiv](https://arxiv.org/abs/2610.36420) · [PDF](https://arxiv.org/pdf/2610.36420) · [HF](https://huggingface.co/papers/2610.36420)

Low-cost arms such as the SO-101 have become the most common entry point to robot learning, yet no released policy performs spatially constrained, language-conditioned tasks on them out of the box, and existing SO-101 benchmarks run only on physical hardware with simple tasks and few held-out objects. We introduce SO-101 Bench, a simulated benchmark for language-conditioned spatial manipulation built on an Isaac Lab…

## 25. Training Foundation Models with a Single Algorithm

- 分数：18.0  ·  HF 赞：4  ·  来源：huggingface + arxiv
- 兴趣命中：reinforcement learning, spec
- 作者：Yuda Song, Alvin Zhang, Fahim Tajwar, Daman Arora, Jeff Schneider, Daniel Khashabi, Ruslan Salakhutdinov, J. Andrew Bagnell, Aarti Singh, Andrea Zanette
- 链接：[arXiv](https://arxiv.org/abs/2610.40564) · [PDF](https://arxiv.org/pdf/2610.40564) · [HF](https://huggingface.co/papers/2610.40564)

Foundation models are typically trained in stages: pretraining, midtraining, supervised fine-tuning (SFT), and reinforcement learning (RL), with changes in both data and learning algorithms. We show that this algorithmic separation is not fundamental. By deriving suitable RL objectives as maximum-likelihood fitting to model-generated target distributions, we place all of these stages under a single likelihood-based…

## 26. CoSTA: Compressed Speech Token Adaptation for Efficient Spoken Dialogue Models

- 分数：17.5  ·  HF 赞：11  ·  来源：huggingface
- 兴趣命中：benchmark, coding
- 作者：Yingzhuo Deng, Chong Li, Bingxin Liu, Yi Shu, Tianyu Peng, Can Xie, Siyao Song, Shuo Ren, Jiajun Zhang
- 链接：[arXiv](https://arxiv.org/abs/2610.21143) · [PDF](https://arxiv.org/pdf/2610.21143) · [HF](https://huggingface.co/papers/2610.21143)

Spoken Dialogue Models (SDMs) typically share a speech-token space for generation and synthesis, leading to long autoregressive sequences and costly inference. Lower-rate speech tokenizers shorten sequences but may introduce compression-quality trade-offs and costly replacement without breaking this coupling. To address this limitation, we propose CoSTA, a compatibility-preserving post-hoc framework that decouples…

## 27. Scaling Lean Theorem Proving for Real-World Code Verification

- 分数：17.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：agent, reinforcement learning, benchmark, spec
- 作者：Debargha Ganguly, Divya Raghunathan, Dejan Jovanović, Vikash Singh, Soonho Kong, Aaron Tomb, Aman Goel, Ferhat Erata, Sam Bayless
- 链接：[arXiv](https://arxiv.org/abs/2610.38174) · [PDF](https://arxiv.org/pdf/2610.38174) · [HF](https://huggingface.co/papers/2610.38174)

We present EasyProver, a Lean proving system built from recursive agents with isolated contexts, asynchronous search, parallel tactic probing, and an elastic elaboration service. Using an off-the-shelf frontier model with no additional training, it proves 669/672 PutnamBench problems and all six IMO 2026 formalizations and resolves 597/600 NTP4VC verification conditions and all 189 VERINA tasks by proof or…

## 28. Weaken to Strengthen: Weakening-Induced On-Policy Self-Distillation for Large Reasoning Models

- 分数：16.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：reasoning, benchmark, coding, spec
- 作者：Yecheng Wu, Song Han, Han Cai
- 链接：[arXiv](https://arxiv.org/abs/2610.38681) · [PDF](https://arxiv.org/pdf/2610.38681) · [HF](https://huggingface.co/papers/2610.38681)

Self-distillation offers a way to improve reasoning models when a suitable external teacher is unavailable. However, common approaches rely on privileged information to construct a stronger self-teacher, limiting their use when only unlabeled prompts are available. In this paper, we introduce Weakening-Induced On-Policy Self-Distillation (WISD), which instead constructs a weaker counterpart of the original model and…

## 29. OpenFlyV2: An onboard vision-language-action model for aerial perception and navigation

- 分数：16.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：memory, reasoning, spec
- 作者：Junli Liu, Zhongrui You, Chenhui Li, Zhen Li, Yuyang Tian, Qizhen Chen, Delin Qu, Haoming Song, Dong Wang, Xuelong Li, Zhigang Wang, Bin Zhao
- 链接：[arXiv](https://arxiv.org/abs/2610.39287) · [PDF](https://arxiv.org/pdf/2610.39287) · [HF](https://huggingface.co/papers/2610.39287)

Human cognition flexibly draws on a shared perceptual foundation to understand environments, attend to referenced entities, reason about spatial relationships, and act. Endowing aerial robots with an analogous functional organization remains challenging, as existing systems are often specialized for individual capabilities, dependent on offboard computation, or unable to sustain closed-loop operation on…

## 30. ABF-Bench: A Verifiable Benchmark for Agentic Blockchain Forensics

- 分数：15.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：agent, memory, benchmark
- 作者：Xiaohang Yu, Hejia Geng, William Knottenbelt
- 链接：[arXiv](https://arxiv.org/abs/2610.23656) · [PDF](https://arxiv.org/pdf/2610.23656) · [HF](https://huggingface.co/papers/2610.23656)

Blockchain forensics is adversarial and open-ended: money launderers split, swap, and bridge funds, cut their trail at mixers or custodial services, and change tactics from one incident to the next. Investigators must keep adapting their tracing in response. Yet the immutability of public ledgers preserves every recorded movement in public view, making much of the investigation independently verifiable. We introduce…

## 31. Matched Capabilities, Different Behaviors: A Controlled Study of MCP and CLI Interfaces for Language Agents

- 分数：15.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：agent, benchmark, spec
- 作者：Zhenning Shi, Liang Pang, Yongqi Li
- 链接：[arXiv](https://arxiv.org/abs/2610.34298) · [PDF](https://arxiv.org/pdf/2610.34298) · [HF](https://huggingface.co/papers/2610.34298)

Language agents increasingly act through external tools and interactive environments, making the interface between the model and its executable capabilities part of the decision process. Model Context Protocol (MCP) and command-line interfaces (CLI) can expose the same semantic operations through markedly different model-facing representations. We study whether these representational differences change agent…

## 32. Broken on Arrival: Non-Functional Quantized LLM Artifacts in Public Model Registries and How to Catch Them

- 分数：15.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：language model, large language, spec
- 作者：Aditi Patodiya
- 链接：[arXiv](https://arxiv.org/abs/2609.05881) · [PDF](https://arxiv.org/pdf/2609.05881) · [HF](https://huggingface.co/papers/2609.05881)

Developers download quantized large language models (LLMs) from public registries to run them locally. None of the registries we examined documented functional testing of their files. We tested all 305 eligible code-capable GGUF tags (the llama.cpp format) across 15 model lines in the official Ollama library, plus 22 popular Hugging Face community files. A 15-task code screen identified suspects, which we retested…

## 33. EPSBench: Benchmarking LLM Agents for Earnings Forecasting

- 分数：14.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：agent, benchmark, spec
- 作者：Yanbin Yin, Chuyu Xu, Liqin Ye, Jing Peng, Chao Zhang
- 链接：[arXiv](https://arxiv.org/abs/2610.38293) · [PDF](https://arxiv.org/pdf/2610.38293) · [HF](https://huggingface.co/papers/2610.38293)

Quarterly earnings forecasting requires an agent to connect financial evidence to the income-statement line items that produce a company's reported earnings. We introduce EPSBench, a benchmark for studying this ability across 149 firm-quarters from 86 US companies. Agents read a fixed collection of filings, earnings-call transcripts, and news, then estimate company-specific income-statement drivers with cited…

## 34. Your LR Schedule May Not Be Principled: Effective Learning Rate Scheduling in Weight-Normalized Training

- 分数：13.5  ·  HF 赞：3  ·  来源：huggingface + arxiv
- 兴趣命中：-
- 作者：Qifan Yu, Xinyu Ma, Xingyan Bin, Di He
- 链接：[arXiv](https://arxiv.org/abs/2610.40362) · [PDF](https://arxiv.org/pdf/2610.40362) · [HF](https://huggingface.co/papers/2610.40362)

Weight-normalized (WN) training is emerging as a compelling alternative to conventional weight decay (WD), with recent studies reporting substantial pretraining loss gains. We show that these gains are driven primarily by the induced effective learning rate (ELR) trajectory rather than by normalization alone. Matching ELR trajectories largely collapses the training loss dynamics of WN and WD. Schedule design should…

## 35. After One-Click Video: The Inflow of Service-Type Content, the Failure of the Recommendation Pool Mechanism, and the BoLe System

- 分数：13.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：language model, large language
- 作者：Bo Zou, Chao Xu
- 链接：[arXiv](https://arxiv.org/abs/2610.37695) · [PDF](https://arxiv.org/pdf/2610.37695) · [HF](https://huggingface.co/papers/2610.37695)

In September 2026, a new large language model was released. Soon after, a new way of making explainer videos became very popular: people asked the model to write a program, and the program produced the video. "One-click video" content then appeared in large amounts on many platforms. On the surface, this is a rise in creative power at the level of the individual. We argue that, at a deeper level, it changes the…

## 36. FDSML: Formula-Driven Supervised Metric Learning with Parameter-Aware Triplet Loss

- 分数：12.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：spec, retrieval
- 作者：Hina Otake, Shinei Arakawa, Keitaro Tanaka, Yoshihiro Fukuhara, Hirokatsu Kataoka, Shigeo Morishima
- 链接：[arXiv](https://arxiv.org/abs/2610.39423) · [PDF](https://arxiv.org/pdf/2610.39423) · [HF](https://huggingface.co/papers/2610.39423)

Formula-Driven Supervised Learning (FDSL) enables vision pre-training without real images, but existing methods cast pre-training as classification on discretized labels, discarding continuity in the generative process. We propose Formula-Driven Supervised Metric Learning (FDSML), which derives relational supervision from image-generation parameters beyond discrete class labels. FDSML combines FineFractalDB, our…

## 37. AB-Attention: Accurate Block Attention for Accelerating Video Diffusion Transformers

- 分数：10.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：-
- 作者：Bin Xu, Mo Zhang, Zhengfeiyang Zhang, Xinfeng Yang, Yixing Ma, Wei Wang, HeXin Wang, Pengfei Zhou, Wangbo Zhao
- 链接：[arXiv](https://arxiv.org/abs/2610.39663) · [PDF](https://arxiv.org/pdf/2610.39663) · [HF](https://huggingface.co/papers/2610.39663)

Video diffusion transformers generate high-quality videos, but the quadratic cost of 3D full attention dominates their inference. Dynamic block-sparse attention reduces this cost by computing exact attention only on key/value blocks selected from current activations. However, its fidelity degrades under aggressive sparsity: blocks are scored from coarse summaries or formed by costly global clustering, pruned blocks…

## 38. Holo4D: Holistic 4D Reconstruction as Geometric Control for Video Diffusion

- 分数：9.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：-
- 作者：Yushi Lan, Zeren Jiang, Koichi Namekata, Xingang Pan, Chuanxia Zheng, Andrea Vedaldi
- 链接：[arXiv](https://arxiv.org/abs/2610.25276) · [PDF](https://arxiv.org/pdf/2610.25276) · [HF](https://huggingface.co/papers/2610.25276)

Synthesizing a monocular video from a new camera trajectory requires preserving the observed scene geometry and motion while completing regions that become newly visible. Feed-forward 4D reconstructors recover the structure of the observed scene, whereas video diffusion models provide a generative prior for completing unseen content. We introduce Holo4D, a video reshooting framework that uses reconstructed 3D…

## 39. Unlocking Any-Order Generation in Pretrained Autoregressive Image Models

- 分数：9.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：-
- 作者：Rishav Pramanik, Marco Pedersoli, Zhaozheng Yin
- 链接：[arXiv](https://arxiv.org/abs/2610.39293) · [PDF](https://arxiv.org/pdf/2610.39293) · [HF](https://huggingface.co/papers/2610.39293)

Autoregressive (AR) image generators are powerful in principle but inflexible in practice: training with a fixed raster-scan order hardcodes a single factorization of the image distribution into the model, leaving it unable to inpaint, outpaint, or edit at inference time. Existing solutions, including the modern discrete-diffusion family, train from scratch on a mixture of token orderings, paying roughly 3x the…

## 40. Bank-World: A Benchmark for Evaluating Agents on Banking Workflows

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, evaluation, benchmark, spec
- 作者：Daniel Rupawalla
- 链接：[arXiv](https://arxiv.org/abs/2610.39733) · [PDF](https://arxiv.org/pdf/2610.39733) · [HF](https://huggingface.co/papers/2610.39733)

Bank-World is a benchmark of 50 banking tasks across two simulated institutions. Completing banking work requires more than producing the right calculation: agents must reconcile records, obtain permission, execute transactions, and keep instructions and status reports consistent as circumstances change. Bank-World tests these requirements through single-turn assignments and multi-turn interactions with simulated…

## 41. Finding Is Not Returning, Returning Is Not Reconstructing: A Multi-Dimensional Evaluation of Agent Social Re-entry

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, memory, evaluation, language model, large language, spec, retrieval
- 作者：Sheng Wan, Cong Ma, Sichen Dong, Qian'Ang Mao, Chenhan Zhang, Daning Hu, Qiang Yang
- 链接：[arXiv](https://arxiv.org/abs/2610.39781) · [PDF](https://arxiv.org/pdf/2610.39781) · [HF](https://huggingface.co/papers/2610.39781)

As Large Language Model (LLM) agents increasingly participate in persistent social environments, understanding their long-term social interaction capabilities becomes increasingly important. While existing research has advanced long-term memory and conversational context retrieval, less attention has been paid to whether agents can autonomously re-engage with previously inactive conversations. In particular,…

## 42. Revisiting Over-refusal in Safety-aligned Large Language Models: A Representation and Optimization Perspective

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, language model, large language, spec
- 作者：Chao Chen, Pengyang Shao, Wei Qin, Shijie Hao, Fei Shen, Richang Hong
- 链接：[arXiv](https://arxiv.org/abs/2610.39802) · [PDF](https://arxiv.org/pdf/2610.39802) · [HF](https://huggingface.co/papers/2610.39802)

Over-refusal is a critical side effect of safety alignment in large language models (LLMs), causing harmless but superficially risky queries to be mistakenly rejected. Despite the effectiveness of existing mitigation methods, why safety-aligned LLMs may still reject harmless queries under correct safety supervision remains insufficiently understood. To address this gap, we analyze over-refusal through the lens of…

## 43. Aligning Medical Vision Language Models at the Capability Boundary with Entropy Adaptive Rubric Grounding

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, reinforcement learning, benchmark, language model, spec
- 作者：Hongyu Bai, Jiaqi Zeng, Chunzheng Zhu
- 链接：[arXiv](https://arxiv.org/abs/2610.39835) · [PDF](https://arxiv.org/pdf/2610.39835) · [HF](https://huggingface.co/papers/2610.39835)

Medical diagnostic reasoning requires verifiable links between visual evidence and clinical knowledge, yet current medical vision language models are aligned with objectives that reward the wrong behavior. Uniform supervised fine tuning lets easy cases dominate updates while clinically critical boundary cases saturate prematurely. Sparse rewards based only on final-answer correctness cannot assess anatomical…

## 44. DWISE: Denoising Workload-Informed Scheduling Engine

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：language model, large language, coding, spec
- 作者：Lie Li, Wen Li, Junxiao Shen, Jindong Gu, Guosheng Hu
- 链接：[arXiv](https://arxiv.org/abs/2610.39852) · [PDF](https://arxiv.org/pdf/2610.39852) · [HF](https://huggingface.co/papers/2610.39852)

Unlike autoregressive large language models (AR-LLMs), diffusion LLMs (dLLMs) generate text by iteratively denoising many tokens in parallel, offering a promising path to efficient inference. Existing serving frameworks, however, schedule dLLM requests with policies designed for AR models, namely first-come-first-served (FCFS) admission and prefill priority. We find that both policies are ill-suited to dLLMs,…

## 45. Attention, Dynamic Wave and Hybrid Sequence Mixers in Language Models

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, long context, language model, large language
- 作者：Dmytro Babarytskyi, Oleksandr Babarytskyi
- 链接：[arXiv](https://arxiv.org/abs/2610.39854) · [PDF](https://arxiv.org/pdf/2610.39854) · [HF](https://huggingface.co/papers/2610.39854)

Large Language Models (LLMs) rely on Multi-Head Attention (MHA) for sequence modeling, but scaling to long contexts is constrained by the quadratic cost of attention, motivating sub-quadratic recurrent alternatives. This paper formalizes a Dynamic Wave recurrent layer, based on input-dependent exponential damping and cosine phase modulation, and evaluates three 10.94M-parameter configurations (Pure Transformer, Pure…

## 46. Turing LLM Post-Training: Calibrated Distillation and Efficient Dynamic-MoE Execution

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, evaluation, benchmark, spec
- 作者：Yue He, Jiahui Hu, Shaman Tang, Hua Zhou, Qiman Wu, Menglin Li, Yizhao Wang, Yuheng Zhang, Da Zhu, Zhou Wang, Anhua Liu, Hanlin Chen, Mingyuan Wang, Rui Xin, Yuhua Wei, Shuang Su, Siqi Liu, Kai Yang, Weichao Huang, Hang Zhang, Honggou Yang, Xianming Liu
- 链接：[arXiv](https://arxiv.org/abs/2610.39876) · [PDF](https://arxiv.org/pdf/2610.39876) · [HF](https://huggingface.co/papers/2610.39876)

We study post-training for dynamically routed mixture-of-experts (MoE) models, focusing on integrating independently optimized specialists while keeping consolidation efficient. Our approach combines calibrated multi-teacher on-policy distillation (C-MOPD), which matches each selected teacher on a local Top-$K$ support with teacher-wise loss normalization and clipping, with an execution path that uses post-capacity…

## 47. PhysAg3D: Bridging 3D Generative and Agentic Models for High-Fidelity and Physically-Interactive Assets

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, tool use, reasoning, evaluation, benchmark
- 作者：Bi'an Du, Fanpeng Meng, Jiemin Fang, Chen Yang, Pufan Li, Daizong Liu, Qi Tian, Wei Hu
- 链接：[arXiv](https://arxiv.org/abs/2610.39924) · [PDF](https://arxiv.org/pdf/2610.39924) · [HF](https://huggingface.co/papers/2610.39924)

Generating interactive 3D assets from a single image requires realistic appearance, fidelity to the depicted object, and plausible physical behavior. Yet detailed geometry alone does not determine how an object should move or deform. We introduce PhysAg3D, which couples 3D generative models with agentic reasoning and tool use. A vision-language agent first infers semantic parts, candidate interactions, and physical…

## 48. Learning Calibrated Confidence for Multi-Agent Collaboration

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reasoning, reinforcement learning, spec, retrieval
- 作者：Chenxiao Fan, Chongming Gao, Gangyi Zhang, Yaxin Gong, Leyang Shen, Jiakai Wang, Dong Wang, Yang Liu, Haoyan Liu, Xinting Hu, Fuli Feng, Xiangnan He
- 链接：[arXiv](https://arxiv.org/abs/2610.39927) · [PDF](https://arxiv.org/pdf/2610.39927) · [HF](https://huggingface.co/papers/2610.39927)

Complex information seeking on the Web often requires collecting evidence from multiple documents and reasoning across them, as in multi-hop question answering. Multi-agent systems address such tasks by dividing work among specialized agents, where upstream agents produce intermediate answers and supporting evidence that downstream agents build upon. However, upstream answers vary in correctness, and most systems…

## 49. Low-Bit GDN Recurrent-State Quantization: Global Gradient-aware Allocation and Pure-Write Sliding Windows

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, reasoning, evaluation, spec
- 作者：Qinghang Huang, Xuchu Huang, Xunzhao Yin
- 链接：[arXiv](https://arxiv.org/abs/2610.39931) · [PDF](https://arxiv.org/pdf/2610.39931) · [HF](https://huggingface.co/papers/2610.39931)

Linear attention stores historical information in a recurrent state of fixed size, providing a compact memory representation for long-context inference. Reducing state precision further lowers per-request storage requirements, but quantized writeback errors enter subsequent recurrences, degrade prediction quality on long-reasoning tasks, and can be accompanied by repetitive generation and excessively long outputs.…

## 50. H$^2$R: Hierarchical Hint-Based Reward for Mathematical Reasoning via Reinforcement Learning

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, reinforcement learning, benchmark, language model, large language, spec
- 作者：He Tu, Siye Li, Hongyi Wen
- 链接：[arXiv](https://arxiv.org/abs/2610.39934) · [PDF](https://arxiv.org/pdf/2610.39934) · [HF](https://huggingface.co/papers/2610.39934)

Reinforcement Learning with Verifiable Rewards has shown great promise in enhancing mathematical reasoning in large language models. However, existing approaches provide limited intermediate supervision for complex, multi-step reasoning tasks. To bridge this gap, we propose \textbf{Hierarchical Hint-based Reward}, a framework that leverages the intrinsic sub-question structure of mathematical problems as structured…

## 51. MLLM-GS: Multimodal Large Language Model Prior-Guided Fast Novel View Synthesis in Extreme Environments

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, language model, large language, spec
- 作者：Zhiliang Wu, Xinye Zheng, Kun Li, Fei Wang, Hao Guo, Yanyan Wei, Guanghui Yue, Beier Zhu, Wei Zhou, Xun Yang
- 链接：[arXiv](https://arxiv.org/abs/2610.39936) · [PDF](https://arxiv.org/pdf/2610.39936) · [HF](https://huggingface.co/papers/2610.39936)

Novel view synthesis (NVS) in degraded scenes aims to reconstruct 3D scenes from multi-view observations affected by various degradations, and to generate clear and photorealistic images at unseen viewpoints. Despite recent advances, existing methods often rely on degradation-specific models, limiting their generalization across diverse extreme environments. Generative models provide rich visual priors, but their…

## 52. Mind The Gap (MTG-AD): Dataset and Fine-grained Evaluation for End-to-End Inline Audio Descriptions

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, language model, large language
- 作者：Subhashini Venugopalan, Jenny Tan, Taylor Roper, Jimmy Tobin, Anton Kast, Alicia Martin, Sam Sepah, Amy Pavel
- 链接：[arXiv](https://arxiv.org/abs/2610.39955) · [PDF](https://arxiv.org/pdf/2610.39955) · [HF](https://huggingface.co/papers/2610.39955)

Audio descriptions (AD) are essential for making visual media accessible to blind and low-vision (BLV) users. While Multimodal Large Language Models (MLLMs) offer a scalable solution for generating audio descriptions on-demand, their performance on ``inline'' audio descriptions -- which must fit within existing silences in a video -- remains under-explored, particularly for diverse user-generated content (UGC). We…

## 53. HEMO: Harness Self-Evolution for Multi-Objective Combinatorial Optimization

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, language model, large language, spec
- 作者：Jianghan Zhu, Cong Zhang, Ni Zhang, Yifan Yang, Yew Soon Ong, Zhiguang Cao
- 链接：[arXiv](https://arxiv.org/abs/2610.40023) · [PDF](https://arxiv.org/pdf/2610.40023) · [HF](https://huggingface.co/papers/2610.40023)

Automatic operator design (AOD) has increasingly adopted large language models (LLMs) to generate problem-specific search and variation operators for multi-objective combinatorial optimization (MOCO). Yet most methods evolve the operators while leaving the process that discovers them fixed. This limits adaptation as new Pareto trade-offs and operator interactions change where and how the search should proceed. We…

## 54. AI Cosmos: An Agentic Infra for Situated Learning

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, memory, reasoning, language model, large language, spec
- 作者： AI Cosmos Team, Jinfeng Zhou, Yuxuan Chen, Fangming Chang, Mingyu Su, Yifan Zhu, Yuan Wang, Bo Zhang, Bosi Wen, Chenhao Yuan, Chenwen Liao, Dazhi Jiang, Deyao Hong, Erle Zhu, Genrui Zhang, Guchan Li, Hongwen Gan, Huichao Bi, Jiahao Yan, Jincheng Fan, Kehan Zheng, Qinren Luo, Qiran Liu, Ruoqi Cao, Shizhi Zhang, Sihan Chen, Siyan Deng, Xuehan Zhou, Xujun Li, Yang Dang, Yanzhuo Zhu, Yu Zhang, Zheyu Chen, Hongning Wang, Manli Li
- 链接：[arXiv](https://arxiv.org/abs/2610.40031) · [PDF](https://arxiv.org/pdf/2610.40031) · [HF](https://huggingface.co/papers/2610.40031)

Large language models (LLMs) can improve task performance during learning, yet these gains do not necessarily reflect learners' ability to thereafter apply the knowledge and skills independently. We present AI Cosmos, an agentic infrastructure for situated learning that organizes learning around two complementary principles: scenario-based participation and cumulative assets of practice. AI Cosmos organizes learners…

## 55. It Takes Two to Probe, Thousands to Retrieve: Putting Vision--Language Probes to the Retrieval Test

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, language model, retrieval
- 作者：Ivana Beňová, Michal Gregor, Marián Šimko
- 链接：[arXiv](https://arxiv.org/abs/2610.40124) · [PDF](https://arxiv.org/pdf/2610.40124) · [HF](https://huggingface.co/papers/2610.40124)

Vision--language models (VLMs) are tested for fine-grained understanding with image--text matching probes, a model must prefer the correct image or caption over handcrafted negative. In retrieval, the correct item must beat thousands of alternatives. We measure how these two evaluation methods relate by using two probing benchmarks, \svo{} and SugarCrepe, for retrieval tasks. For 100 image and caption queries we…

## 56. VideoMemBench: How Well Do MLLMs Remember in Video Conversations?

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, evaluation, benchmark, language model, large language
- 作者：Zhengdong Hu, Chao Wang, Kaituo Feng, Huanjin Yao, Mingfei Lu, Hehe Fan, Yi Yang
- 链接：[arXiv](https://arxiv.org/abs/2610.40131) · [PDF](https://arxiv.org/pdf/2610.40131) · [HF](https://huggingface.co/papers/2610.40131)

Multimodal large language models (MLLMs) can now process hour-long videos, making extended multi-turn dialogue over a single video a natural mode of use. Sustaining such a dialogue requires more than answering each question in isolation: the model must retrieve and reuse information established earlier in the conversation, both what it has seen and what it has said, an ability we term in-context video memory.…

## 57. DynaRev: Benchmarking Web Agents under Dynamic Goal Revision

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, evaluation, benchmark, spec
- 作者：Shiqi Zhang, Guochen Zhou, Zesheng Wei, Hai Zhao, Zhisong Zhang
- 链接：[arXiv](https://arxiv.org/abs/2610.40133) · [PDF](https://arxiv.org/pdf/2610.40133) · [HF](https://huggingface.co/papers/2610.40133)

Web agents are typically evaluated with goals fully specified before execution and fixed thereafter, whereas real users often revise their requirements during interaction. To study such interactions, we introduce DynaRev, a benchmark of 181 tasks to evaluate web agents under dynamic goal revision. DynaRev uses semantic milestones to deliver revisions at task-defined stages, covers additive revisions, unconditional…

## 58. Locating and Closing Information Gaps in Multi-Agent Systems

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, tool use, reasoning, benchmark, planning
- 作者：Yaxin Gong, Chongming Gao, Gangyi Zhang, Chenxiao Fan, Leyang Shen, Jiakai Wang, Dong Wang, Yang Liu, Haoyan Liu, Xinting Hu
- 链接：[arXiv](https://arxiv.org/abs/2610.40186) · [PDF](https://arxiv.org/pdf/2610.40186) · [HF](https://huggingface.co/papers/2610.40186)

Multi-step Web tasks often require several LLM agents to gather and combine evidence. The communication graph of a fixed workflow restricts which agents can read each other's outputs: evidence retrieved by one agent may never reach the agent that needs it, leaving an information gap and an incomplete or incorrect answer. Adding a connection can deliver the missing evidence, but can also lead the receiver to adopt an…

## 59. Video Generation Meets Agent Harness: Agentic Video Generation, Agentic World Modeling and Recursive Self-Improvement

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, tool use, memory, evaluation, planning
- 作者：Liaoyuan Fan, Yuhao Zheng, Dongxing Mao, Hangyu Ran, Siyuan Hu, Weijia Mao, Rui Zhao, Weijia Wu, Guian Fang, Yanzhe Chen, Zeyu Zhu, Yuxin Jiang, Yiren Song, Yuchao Gu, Junchao Yi, Qi Hu, Dan Kong, Alex Jinpeng Wang, Kevin Qinghong Lin, Mike Zheng Shou, Wei Liu
- 链接：[arXiv](https://arxiv.org/abs/2610.40191) · [PDF](https://arxiv.org/pdf/2610.40191) · [HF](https://huggingface.co/papers/2610.40191)

Video generation is shifting from end-to-end synthesis toward agentic generation, where planning, tool use, and feedback enable coherent, controllable multi-shot videos. In parallel, video world models provide action-conditioned observations and predicted futures, serving as interactive environments for agents. We study their intersection through the agent harness: an executable runtime that constructs context,…

## 60. EnvOS: Auditing Computer-Use Agents When the World Moves On : Phenomenon-Based Task Construction, Certification, and Evidence-Based Evaluation

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reinforcement learning, evaluation, language model, large language
- 作者：Ankush Kadu, Athira Gopal, Niharika Singh, Arpit Jain, Aswanth Krishnan
- 链接：[arXiv](https://arxiv.org/abs/2610.40246) · [PDF](https://arxiv.org/pdf/2610.40246) · [HF](https://huggingface.co/papers/2610.40246)

Computer-use agents built on large language models (LLMs) work in software that can change while they act: an appointment moves, a policy is revised, a record is updated. Testing agents under such changes is harder than it looks. When an agent fails, the cause may be the agent, but it may also be a change that did not fire as intended, an update the agent never received, or a grader that scored the episode wrongly.…

## 61. When Requirements Interact: Scaling Long-Horizon Coding via Interdependent Specifications

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reasoning, reinforcement learning, benchmark, coding, spec
- 作者：Yishuo Cai, Minzheng Wang, Liang Zhao, Linghao Zhang, Lei Li, Shicheng Li, Xu Sun, Fuli Luo
- 链接：[arXiv](https://arxiv.org/abs/2610.40256) · [PDF](https://arxiv.org/pdf/2610.40256) · [HF](https://huggingface.co/papers/2610.40256)

To succeed in real-world long-horizon software development, coding agents must satisfy multi-dimensional task specifications, such as interface compatibility and error handling, and do so without breaking existing dependencies. However, current works lack specification in both quantity and diversity, often emphasizing primary goals while ignoring complex constraints. Synthesizing tasks to bridge this gap presents…

## 62. TaskFrame: Connecting Task-Level Planning with Frame-Level Control for Game Agents

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reasoning, evaluation, language model, spec, planning
- 作者：Guangzhi Wang, Junfu Pu, Yiran Wang, Xingyilang Yin, Honghao Chen, Cheng Cheng, Lingen Li, Yinan Zhou, Jiarui Wu, Yinuo Jiang, Hongbo Jin, Xiaodong Cun, Ying Shan
- 链接：[arXiv](https://arxiv.org/abs/2610.40276) · [PDF](https://arxiv.org/pdf/2610.40276) · [HF](https://huggingface.co/papers/2610.40276)

Building general game agents requires both high-level task reasoning and low-latency action control in rapidly changing visual environments. These capabilities favor models with substantially different computational profiles, making them difficult to realize within a single model. In this work, we present TaskFrame, a hierarchical planner-controller framework that connects task-level planning with frame-level…

## 63. Only Accepted Tokens Count: An Energy Accounting of Speculative Decoding Under Latency Targets

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, language model, large language, coding, spec
- 作者：Bole Ma, Ayesha Afzal, Jan Eitzinger, Harald Koestler, Gerhard Wellein
- 链接：[arXiv](https://arxiv.org/abs/2610.40287) · [PDF](https://arxiv.org/pdf/2610.40287) · [HF](https://huggingface.co/papers/2610.40287)

Large language model serving is limited by facility power. Energy per token determines how many tokens a datacenter can serve, while a latency target bounds how quickly each user receives them. During decode, every weight is read from memory for every generated token. Batching amortizes this read across users but makes no individual user faster. Speculative decoding does: a drafter proposes several future tokens,…

## 64. Don't Lose the Thread: Empowering Long-Horizon LLM Agents with Cognitive Resource Self-Allocation

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, memory, reasoning, benchmark, language model, large language, planning
- 作者：Zheng Zhu, Xiaozhuan Liang, Xi Chen, Bei Yu, Jiaya Jia
- 链接：[arXiv](https://arxiv.org/abs/2610.40350) · [PDF](https://arxiv.org/pdf/2610.40350) · [HF](https://huggingface.co/papers/2610.40350)

Agents powered by large language models (LLMs) have demonstrated remarkable progress in solving complex reasoning tasks. However, LLM agents often falter on long-horizon tasks due to cognitive overload, as their working memory becomes cluttered with expanding and irrelevant information, which dilutes their attention and hinders effective planning and reasoning. To mitigate this challenge, we introduce Cognitive…

## 65. The Athlete as a Scientist of One: Agentic Bayesian Experimental Design for Individualized Physiology from Consumer Wearables

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, benchmark, language model, large language, spec
- 作者：Behnam Moradi
- 链接：[arXiv](https://arxiv.org/abs/2610.40370) · [PDF](https://arxiv.org/pdf/2610.40370) · [HF](https://huggingface.co/papers/2610.40370)

Large language model (LLM) agents for personal health read wearable data and recommend, but do not learn about the individual in a way that can be audited or falsified. We present EpiCoach, an agentic system that treats one athlete, a cross-country mountain biker, as the subject of accountable N-of-1 science. Claims about the athlete live in an evidence-gated hypothesis registry: each must issue a probabilistic…

## 66. Agentic LLM reasoning in pediatric diabetes outcome prediction from multimodal medical records

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reasoning, language model, large language
- 作者：Daniel Palacios, Guantong Qi, Anna Kadi, Natali Borrego, Sukru Aras, Michael L. Ferm, Elizabeth Kubota-Mishra, Maria J. Redondo, Zhandong Liu, Mustafa Tosur, Hu Chen
- 链接：[arXiv](https://arxiv.org/abs/2610.40379) · [PDF](https://arxiv.org/pdf/2610.40379) · [HF](https://huggingface.co/papers/2610.40379)

Large language model (LLM) agents are proposed for clinical prediction but are untested in pediatrics, where cohorts are small and outcomes are uncommon. Using records from 2,489 youth with type 2 diabetes (T2D) and 4,018 with type 1 diabetes (T1D), spanning structured data, note-derived social determinants and, in T1D, continuous glucose monitoring data, we predicted seven T2D outcomes, four also in T1D, at 24…

## 67. Scaling Mathematical Proof Supervision from Structured Textbooks

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, evaluation, benchmark, language model
- 作者：Youqing Fang, Zhouqi Hua, Yinhao Tang, Yuzhe Gu, Lingkai Kong, Bin Liu, Weiming Zhang, Kai Chen, Yanan Sun, Wenwei Zhang
- 链接：[arXiv](https://arxiv.org/abs/2610.40394) · [PDF](https://arxiv.org/pdf/2610.40394) · [HF](https://huggingface.co/papers/2610.40394)

Mathematical supervision for language models is typically flattened into isolated problem-solution pairs, discarding the curricular organization and evidential structure of the original sources. We introduce TOME-Math (Textbook-Oriented Mathematical Evidence), a large-scale corpus that converts 2,118 textbooks spanning the core areas of university-level mathematics subjects into approximately 380K structured…

## 68. Retrieving from Your Own Mistakes: On-Policy Training of Embedding Models for Multi-Hop Retrieval-Augmented Generation

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, language model, coding, retrieval
- 作者：Chenjie Qiu, Zixuan Zeng, Shaobin Shi, Bingfeng Chen, Dongsheng Luo, Boyan Xu
- 链接：[arXiv](https://arxiv.org/abs/2610.40409) · [PDF](https://arxiv.org/pdf/2610.40409) · [HF](https://huggingface.co/papers/2610.40409)

Complex questions in retrieval-augmented generation require evidence spread over several documents, and an answer is reliable only when the retriever finds all of it. Chain embedding retrievers collect such evidence step by step, re-encoding the question together with the passages retrieved so far, and we find that they are already strong: trained only on gold histories, a small chain embedding retriever that calls…

## 69. Prefix Executability: Evaluating Tool-Using Agents Beyond Final Success

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, tool-use, evaluation, benchmark
- 作者：Amir H. Rezaeian, Weiyi Sun, Yassine Benajiba, Dan Roth
- 链接：[arXiv](https://arxiv.org/abs/2610.40444) · [PDF](https://arxiv.org/pdf/2610.40444) · [HF](https://huggingface.co/papers/2610.40444)

Tool-use benchmarks often score agents by final task success, but terminal outcomes can obscure whether the intermediate tool-call trajectory was executable. We propose prefix executability as a trajectory-level evaluation protocol for tool-using agents. The protocol measures whether every prefix of a predicted tool-call sequence remains executable under tool schemas, state preconditions, and data dependencies, and…

## 70. Reinforcement learning for control of partial differential equations

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reinforcement learning, evaluation, benchmark, spec
- 作者：Nicolò Botteghi, Matteo Tomasetto, Andrea Manzoni
- 链接：[arXiv](https://arxiv.org/abs/2610.40449) · [PDF](https://arxiv.org/pdf/2610.40449) · [HF](https://huggingface.co/papers/2610.40449)

Controlling dynamical systems governed by partial differential equations (PDEs) remains a challenging task in scientific computing, owing to high-dimensional state spaces, distributed actuation, nonlinear dynamics, and stringent real-time constraints. Reinforcement learning (RL) has emerged as a promising paradigm for synthesizing feedback controllers that adapt to varying operating conditions and can be deployed…

## 71. Training language models in simulation for psychiatric intake

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reinforcement learning, language model, planning
- 作者：Samuel Schmidgall, Tim Strother, Alex Bijamov, Min Woo Sun, Anil Palepu, Akshay Goel, Ulysse Marteau-Ferey, Théo Moutakanni, Yubin Kim, Joseph Breda, Christina Chen, Justin Chen, Paul Jhun, Andrew Marshall, Sarah Montgomery-Taylor, Eun Kyoung Hong, Shashank Ravi, Kameron C. Black, David J. H. Wu, Austin Schoeffler, John Lyon Havlik, Elizabeth C. Stade, Jared Moore, Johannes C. Eichstaedt, Logan Pierce, Jeff Jopling, Johannes Thrul, Thomas H. McCoy, Neguine Rezaii, Mark S. Chen, Ellen E. Fitzsimmons-Craft, Shirley Wang, Desmond C. Ong, Katharina Schultebraucks, Torrey Creed, Bhavna Daryani, Aleksandra Faust, S. Sara Mahdavi, Caroline Figueroa, Eric Lin, Kate H. Bentley, Ernest Lim, Zhihan Jiang, Xuhai "Orson" Xu, Daniel McDuff, John Torous, Yun Liu, Po-Hsuan Cameron Chen, Mike Schaekermann, Joelle Barral, Alvin Rajkomar, Tao Tu, Lin Yang, Isaac Galatzer-Levy, David Racz, Valentin Liévin
- 链接：[arXiv](https://arxiv.org/abs/2610.40476) · [PDF](https://arxiv.org/pdf/2610.40476) · [HF](https://huggingface.co/papers/2610.40476)

In psychiatric practice, the clinical intake interview remains a primary diagnostic instrument, requiring the clinician to establish rapport while disentangling complex, overlapping presentations. Here, we show that multi-turn reinforcement learning (RL) in simulation environments improves language model performance on structured text-based psychiatric intake, spanning history-taking, differential diagnosis, and…

## 72. Agentic University: Collaborative Agents for Personalized Learning

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, evaluation, language model, large language, spec
- 作者：Jingru Fan, Tianle Zhou, Yunjie Zhou, Zihao He, Yixuan Zhou, Kezhao Wu, Xinyu Zheng, Xiyuan Wang, Yuheng Wang, Zhi Li, Songhua Liu, Weinan E, Chen Qian
- 链接：[arXiv](https://arxiv.org/abs/2610.40492) · [PDF](https://arxiv.org/pdf/2610.40492) · [HF](https://huggingface.co/papers/2610.40492)

Large language models support personalized tutoring, content generation, and adaptive learning paths. However, capability development requires these resources and interactions to form a coherent learning process that evolves with the learner. A central challenge is to align goals, activities, and assessment while using learning evidence to decide what should follow. We introduce Human-Participatory Multi-Agent…

## 73. How I Aligned Your Model: Scaling Up Multilingual Safety Training with Templates

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, language model, large language, spec
- 作者：Max Neuwinger, Hanna Yukhymenko, Imanol Schlag
- 链接：[arXiv](https://arxiv.org/abs/2610.40516) · [PDF](https://arxiv.org/pdf/2610.40516) · [HF](https://huggingface.co/papers/2610.40516)

Safety alignment for Large Language Models is heavily focused on English with limited multilingual representation, particularly damaging low-resource language performance. Related open training datasets are often limited in size or do not follow region-localized harmful topics to broaden the scope of alignment beyond cultures. We propose a scalable template-based augmentation pipeline to produce massive multilingual…

## 74. CrossWeave: Cross-Modal Scene and Instance Retrieval from Sparse 2D-3D Alignment

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, coding, spec, retrieval
- 作者：Aadith Warrier, Gnana Prakash Punnavajhala, Siddharth Tourani, Muhammad Haris Khan, Avinash Sharma, Madhava Krishna
- 链接：[arXiv](https://arxiv.org/abs/2610.40525) · [PDF](https://arxiv.org/pdf/2610.40525) · [HF](https://huggingface.co/papers/2610.40525)

Cross-modal scene and instance retrieval aims to retrieve a corresponding 3D environment or object given query 2D images, serving as a foundational mechanism for spatial reasoning in robotics and AR/VR. Existing methods achieve this by learning alignment only at the level of whole scenes or objects, which provides no supervision for the fine-grained local structure within them. In this work, we show that supervision…

## 75. PhysCount: Do MLLMs Count Visual Appearances or Physical Entities?

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, language model, large language, spec
- 作者：Lidong Lu, Jiaxin Lv, Liangrui Dong, Xinyi Mao, Lidong Zou, Zhenquan Li, Tong Lu, Guo Chen
- 链接：[arXiv](https://arxiv.org/abs/2610.40530) · [PDF](https://arxiv.org/pdf/2610.40530) · [HF](https://huggingface.co/papers/2610.40530)

Images reveal appearances, but counting often asks about physical objects. A single entity may be visible directly, in several reflections, or through glass, so detecting every visible occurrence does not determine how many entities are present. Existing visual counting benchmarks rarely separate these two operations. We introduce PhysCount, a benchmark for evaluating whether multimodal large language models (MLLMs)…

## 76. On the Fundamental Limits of Prefill-Based Decoding Length Prediction

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, language model, large language, coding
- 作者：Haowen Shi, Xuzhe Yan, Fahao Chen, Peng Li
- 链接：[arXiv](https://arxiv.org/abs/2610.40541) · [PDF](https://arxiv.org/pdf/2610.40541) · [HF](https://huggingface.co/papers/2610.40541)

Predicting how many tokens a large language model (LLM) will decode, using only prefill-phase hidden states, is a key primitive for inference scheduling. We show that current benchmarks conflate predictor quality with task hardness: when the target model, dataset, or sampling configuration changes, reported accuracy collapses even though the predictor is unchanged. We trace this instability to an overlooked error…

## 77. Advancing Clinical Genomic Analysis with a Skill-Centred Agent

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, benchmark, spec, retrieval
- 作者：Qiaoyu Zheng, Weike Zhao, Yanjie Fan, Ye Cao, Mengqi Jiang, Xiao Zhou, Xiaoman Zhang, Pengcheng Qiu, Yongguo Yu, Yanfeng Wang, Ya Zhang, Chaoyi Wu, Weidi Xie
- 链接：[arXiv](https://arxiv.org/abs/2610.40556) · [PDF](https://arxiv.org/pdf/2610.40556) · [HF](https://huggingface.co/papers/2610.40556)

Clinical genomic analysis requires experts to integrate evolving guidelines, databases, and computational evidence. As sequencing has become increasingly accessible, this complex and labor-intensive process has become a major bottleneck to the timely use of genomic information in clinical decision-making. To fill this gap, we developed ClinGeX, a large-language-model agent that composes 105 curated executable skills…

## 78. VeriCUA: Verification as Agentic Exploration for Computer-Using Agents

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reinforcement learning, evaluation, language model, spec
- 作者：Qiushi Sun, Da Yu, Alexander Knop, Amer Sinha, Lingpeng Kong, Ben Kao, Ravi Kumar, Pritish Kamath
- 链接：[arXiv](https://arxiv.org/abs/2610.40578) · [PDF](https://arxiv.org/pdf/2610.40578) · [HF](https://huggingface.co/papers/2610.40578)

Building and scaling computer-using agents (CUAs) across desktop, mobile, and web environments requires reliable task-completion verification for data curation, evaluation, and reinforcement learning. Typical automated approaches prompt vision-language models (VLMs) to judge trajectories or generate programs to inspect application state. However, both rely on partial views of complex digital environments. VLM judges…

## 79. TextSeal2: Distortion-Free LLM Watermarking with Copula Mixing and Memoryless Races

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, language model, large language, coding, spec
- 作者：Tom Sander, Pierre Fernandez, Itai Gat, Haiming Bao, Jiaxin Shi, Jason Park, Valeriu Lacatusu, Sylvestre-Alvise Rebuffi, Hongyan Chang, Hady Elsahar, Tomáš Souček, Tuan Tran, Surya Parimi, Alexandre Mourachko
- 链接：[arXiv](https://arxiv.org/abs/2610.40613) · [PDF](https://arxiv.org/pdf/2610.40613) · [HF](https://huggingface.co/papers/2610.40613)

We present TextSeal2, a distortion-free watermark for large language models that keeps its signal under speculative decoding: tokens that replace rejected drafts remain watermarked with the same keys, and the acceptance rate is unchanged. It also preserves output diversity and adds no measurable inference latency. Its predecessor, TextSeal, restores diversity in the Gumbel-max scheme by routing each token to one of…

## 80. ShallowDefend: Harnessing Shallow Safety Alignment for Multi-Turn Defender

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reinforcement learning, benchmark, language model, large language
- 作者：Qiyao Ma, Xiaodong Liu, Weiwei Yang, Mingqian Feng, Chengquan Guo, Jialin Song, Carolyn Buractaon, Zhe Zhao, Junshan Zhang, Sandeep Atluri, Christopher White, Jianfeng Gao
- 链接：[arXiv](https://arxiv.org/abs/2610.40627) · [PDF](https://arxiv.org/pdf/2610.40627) · [HF](https://huggingface.co/papers/2610.40627)

Safety alignment has enabled large language models to reliably refuse harmful requests directly, yet the same request distributed across a multi-turn conversation still succeeds far too often. This brittleness has a mechanistic root: Alignment is shallow, with safety behavior concentrated in a model's first few output tokens, and existing defenses inherit the weakness, supervising the surface form of the response…

## 81. Elucidating the Design Space of LM Data Attribution

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, language model, retrieval
- 作者：Steven Yu, Sheng-Yu Wang, Kimia Hamidieh, Antonio Torralba, David Bau
- 链接：[arXiv](https://arxiv.org/abs/2610.40655) · [PDF](https://arxiv.org/pdf/2610.40655) · [HF](https://huggingface.co/papers/2610.40655)

Data attribution methods for Language Models (LMs) are typically evaluated using downstream tasks like fact retrieval. However, existing evaluations vary multiple dataset properties simultaneously, making it impossible to isolate exactly why an attribution algorithm fails. To diagnose these failures, we explore the design space of LLM data attribution, with a primary focus on evaluation. We introduce the Controlled…

## 82. PAPERBENCHX: Can AI Reproduce Science Across Disciplines?

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, benchmark, spec
- 作者：Ruoyu Wu, Zengji Tu, Aolong Sun, Tianyi Ma, Junren Li, Xinbo Xu, Li Fu, Ziyan Zhang, Pinrui Huang, Xiaochen Wang, Chengda Wu, Yutao Zhou, Jianjun Wu, Lin Chang, Baobao Chang, Liang Chen, Kuan Li
- 链接：[arXiv](https://arxiv.org/abs/2610.39744) · [PDF](https://arxiv.org/pdf/2610.39744) · [HF](https://huggingface.co/papers/2610.39744)

Before AI can be trusted to discover new science, it should be able to reproduce what science already knows. Reproduction provides a rigorous checkpoint for an AI scientist: the target claim is known, yet recovering it still requires translating an incomplete scientific description into an executable experiment and producing evidence that can be independently verified. Existing research-reproduction benchmarks…

## 83. Long-Term Agent Memory through Complementary Curation and Consolidation

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, memory, benchmark
- 作者：Abhishek Gupta, Dongge Han, Daniel Madrigal Diaz, Wei-Ning Chen, Mayukh Das, Victor Rühle, Saravan Rajmohan
- 链接：[arXiv](https://arxiv.org/abs/2610.39790) · [PDF](https://arxiv.org/pdf/2610.39790) · [HF](https://huggingface.co/papers/2610.39790)

Long-horizon dialogue agents require effective memory systems to recall facts, events, and relationships from interaction histories. In this work, we propose a hybrid-memory architecture comprising episodic memories and structured relational memories and a consolidation mechanism which preserves efficiency. We conduct an empirical study across two benchmarks: LoCoMo and LongMemEval-S. Our experiments demonstrate…

## 84. InferD: A Honeypot Framework for AI Inference Infrastructure

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, language model, large language
- 作者：Hicham Hammouchi, Gabriele Lenzini
- 链接：[arXiv](https://arxiv.org/abs/2610.39807) · [PDF](https://arxiv.org/pdf/2610.39807) · [HF](https://huggingface.co/papers/2610.39807)

Large language model serving stacks, commercial inference APIs, vector databases, and agent orchestration gateways are now ex- posed on the public internet and indexed by commodity scanners within hours of deployment. The threat characteristics of this sur- face are only beginning to be measured, and the honeypot frame- works that could measure it were designed for conventional net- work services rather than for AI…

## 85. GROME: GROunding Factorized MEmory into Video World Models

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, context window, retrieval
- 作者：Fang Yu, Xiaoxue Wu, Haiyu Zhang, Yangfu Li, Botong Zhao, Yu Qiao, Tianfan Xue, Yue Lu, Xinyuan Chen
- 链接：[arXiv](https://arxiv.org/abs/2610.39812) · [PDF](https://arxiv.org/pdf/2610.39812) · [HF](https://huggingface.co/papers/2610.39812)

Long-horizon consistency is essential for video world models, yet it becomes difficult to maintain once observed content falls outside the context window. Existing memory mechanisms either retrieve history as implicit context, which remains constrained by context capacity and entangles static and dynamic information or consolidate history into explicit global representations, which struggle to model evolving…

## 86. EvoTeam: Multi-Agent Collaboration via Evolving Teams

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, benchmark, spec
- 作者：Qinuo Cao, Xin He, Dianxuan Fu, Lizhi Zhang, Zhaoqing Xing, Jiapu Wang, Xin Wang, Na Zou, Yi Chang, Qinggang Zhang
- 链接：[arXiv](https://arxiv.org/abs/2610.39813) · [PDF](https://arxiv.org/pdf/2610.39813) · [HF](https://huggingface.co/papers/2610.39813)

LLM-based multi-agent systems (MAS) rely on collaboration among specialized agents to solve complex tasks. Existing methods improve MAS by refining the prompts, skills, and execution strategies of individual agents based on task feedback. However, improving individual agents does not necessarily lead to better team collaboration. Recent studies have therefore extended evolution to the collaboration level, using…

## 87. KV Cache Quantization for Diffusion Language Models

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, language model, coding
- 作者：Yan Tai, Yunan Ding, Guangzhao Li, Siqi Luo, Chaoyang Zhang, Guangtao Zhai, Guodong Guo, Xiaohong Liu
- 链接：[arXiv](https://arxiv.org/abs/2610.39853) · [PDF](https://arxiv.org/pdf/2610.39853) · [HF](https://huggingface.co/papers/2610.39853)

KV cache quantization is well studied for autoregressive language models, where cached prefix states are exact under causal attention and quantization is mainly a cache reconstruction problem. Diffusion language models (dLLMs) break this assumption. Fast dLLM inference reuses KV states across denoising steps, but bidirectional token representations can change as masked tokens are revealed, so the reused cache may…

## 88. Spectral Invariant Fusion and Refinement for Domain Generalized Semantic Segmentation

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, coding, spec
- 作者：Yansong Bai, Yunzhi Zhuge, Xinzhuo Yu, Lu Zhang, Jin Zhan, Pingping Zhang, Huchuan Lu
- 链接：[arXiv](https://arxiv.org/abs/2610.39926) · [PDF](https://arxiv.org/pdf/2610.39926) · [HF](https://huggingface.co/papers/2610.39926)

Domain generalized semantic segmentation is challenging because it requires accurate dense prediction on unseen domains without any access to target-domain data during training. Existing methods improve transferability through data diversification, invariant learning, or direct use of foundation models, but they often struggle to simultaneously suppress domain-sensitive interference and preserve fine-grained spatial…

## 89. Observability-Aligned Evidential Masked Pretraining for Reliable VRU Motion Prediction

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, coding
- 作者：Shang Gao, Franz Götz-Hahn, Konrad Doll, Bernhard Sick
- 链接：[arXiv](https://arxiv.org/abs/2610.39958) · [PDF](https://arxiv.org/pdf/2610.39958) · [HF](https://huggingface.co/papers/2610.39958)

Vulnerable road user (VRU) prediction must operate under partial observability and distribution shift, so reliable uncertainty matters alongside accuracy. Masked pretraining is attractive in this setting because it naturally exposes the model to missing content during self-supervision, but existing time-series masked autoencoding methods are typically deterministic and do not constrain how confidence should change…

## 90. Cheap Retrieval and Observation Credit Assignment from One Quantity: The Value of Information

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, reinforcement learning, retrieval
- 作者：Daniel Strauss, Nikolaos Sotirakis, Zhenshan Bing, Alois Knoll
- 链接：[arXiv](https://arxiv.org/abs/2610.40030) · [PDF](https://arxiv.org/pdf/2610.40030) · [HF](https://huggingface.co/papers/2610.40030)

Memory in reinforcement learning raises two problems. Attention finds the relevant item by scoring the whole store, which is costly for robots under latency and energy limits. When a retrieved memory pays off, credit for acquiring it must cross the whole sequence. We argue that both are governed by one quantity, the value of information, and propose to estimate it from archived rollouts with a learned world model.…

## 91. Hybrid AI Patterns: Thirteen Ways to Couple Language Models with Rules, and How to Choose Among Them

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reasoning, language model
- 作者：Siegfried Handschuh, Götz-Henrik Wiegand, Lorena Raichle
- 链接：[arXiv](https://arxiv.org/abs/2610.40036) · [PDF](https://arxiv.org/pdf/2610.40036) · [HF](https://huggingface.co/papers/2610.40036)

Language models handle text well, and rule engines give conclusions with proofs. Systems that combine the two are usually described by example, and the same coupling turns up under different names in agent frameworks, guardrail toolkits and neuro-symbolic research. This document defines thirteen patterns for coupling a language model with an executable rule language, in the catalogue form introduced for…

## 92. UPPAAi: Towards LLM-Assisted Modeling, Verification, Analysis and Synthesis

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：language model, large language, spec
- 作者：Peter Dolog, Kim G. Larsen, Marius Mikučionis, Frederik F. K. Rasmussen
- 链接：[arXiv](https://arxiv.org/abs/2610.40042) · [PDF](https://arxiv.org/pdf/2610.40042) · [HF](https://huggingface.co/papers/2610.40042)

For more than three decades, UPPAAL has supported the modelling and analysis of real-time and cyber-physical systems. Yet building a suitable model, formalising the intended properties, choosing analysis techniques and interpreting counterexamples remain iterative tasks that demand substantial expertise. Large language models (LLMs) can offer plausible explanations and even solutions, but they are not necessarily…

## 93. Upcycling Language Models for Multiple Specialized Domains

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：language model, large language, spec
- 作者：Mingzi Cao, Xi Wang, Nikolaos Aletras
- 链接：[arXiv](https://arxiv.org/abs/2610.40091) · [PDF](https://arxiv.org/pdf/2610.40091) · [HF](https://huggingface.co/papers/2610.40091)

Effective multi-domain adaptation of large language models requires prioritizing relevant domain knowledge while minimizing interference from irrelevant domains. Existing approaches commonly use Low-Rank Adaptation (LoRA) to train a separate adapter for each domain and combine these adapters within one model. However, they either weight adapters equally regardless of the input domain or dynamically weight adapters…

## 94. RepConTUR: A Report-Conditioned Volumetric Multimodal Model for Abdominal Tumor Segmentation

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：language model, spec, planning
- 作者：Seunghwan Lee, Sangjoon Park, Jongmin Lee, Yoon Jo Kim, Wonyoung Cho, Jin Sung Kim, Han Joo Chae
- 链接：[arXiv](https://arxiv.org/abs/2610.40094) · [PDF](https://arxiv.org/pdf/2610.40094) · [HF](https://huggingface.co/papers/2610.40094)

Tumor delineation is required for radiotherapy planning, yet automatic segmentation is limited by errors, predominantly false positives, that distort dose and increase editing time. The radiology report accompanies the scan and localizes disease at the suborgan level, but existing text-promptable models condition on short referring phrases, and most operate in 2D. We present RepConTUR, a single native-3D…

## 95. Escaping Path Mirages in Offline Goal-Conditioned Reinforcement Learning

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reinforcement learning, planning
- 作者：Junhyeon Bae, Jaebak Hwang, Gwanwoo Choi, Minung Kim, Seungyul Han
- 链接：[arXiv](https://arxiv.org/abs/2610.40130) · [PDF](https://arxiv.org/pdf/2610.40130) · [HF](https://huggingface.co/papers/2610.40130)

Offline goal-conditioned reinforcement learning remains challenging in stochastic long-horizon settings, where compounding value estimation errors hinder reliable goal reaching. While prior methods have sought to address this challenge through various approaches, a key challenge remains path mirage, where agents overcommit to spuriously successful trajectories in offline datasets induced by stochasticity, often…

## 96. Bridging Semantics and Structure: A Theoretically Grounded Framework for Link Prediction on TAGs

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, language model
- 作者：Chen Shao, Ruirui Wang, Tobias Kafer, Danai Koutra
- 链接：[arXiv](https://arxiv.org/abs/2610.40192) · [PDF](https://arxiv.org/pdf/2610.40192) · [HF](https://huggingface.co/papers/2610.40192)

Link prediction on text-attributed graphs (TAGs) is a fundamental problem with applications in knowledge discovery, recommendation and beyond. Recent progress has highlighted the promise of combining Graph Neural Networks (GNNs) with Language Models (LMs) in order to leverage the complementary structural and semantic signals. However, due to the distinct inductive biases of GNNs and LMs, the design of an optimal…

## 97. Benchmarking color judgment in multimodal LLMs with CIE-computable ground truth

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, language model, large language
- 作者：Shuwei Yue, Kaida Xiao, Zhihua Wang, Qiao Chen
- 链接：[arXiv](https://arxiv.org/abs/2610.40212) · [PDF](https://arxiv.org/pdf/2610.40212) · [HF](https://huggingface.co/papers/2610.40212)

Multimodal large language models (MLLMs) are now used as zero-shot judges of image quality, but their color judgments are rarely tested with colorimetric ground truth. We present a five-task benchmark based on the CIE colorimetric framework: AWB pair judgment, skin-tone bias direction, CCT estimation, CIE Delta E 2000 pair ordering, and color naming under changing illuminants. We test eight MLLM endpoints, including…

## 98. DYNAS: A Dynamic Network Penetration Testing Framework Using Deep Hierarchical Reinforcement Learning

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reinforcement learning, evaluation, spec
- 作者：Md. Rakibul Hassan, Majedul Islam, Md. Ashraful Alam, Muhammad Iqbal Hossain, Swakkhar Shatabda
- 链接：[arXiv](https://arxiv.org/abs/2610.40214) · [PDF](https://arxiv.org/pdf/2610.40214) · [HF](https://huggingface.co/papers/2610.40214)

As network scale and uncertainty complicate automated penetration testing, reinforcement learning (RL) environments must support controlled evaluation under defensive and non-stationary conditions. We present DYNAS (Dynamic Network Attack Simulator), which combines parameterized large-scale scenario generation with stateful intrusion detection responses, explicit scan false-positive and false-negative noise,…

## 99. Mobilizing the Archive: Bitext Extraction at Scale from Archival Documents for Extremely Low-resource Languages

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：language model, large language, spec
- 作者：Chutong Meng, Alec J. Bateman, Antonios Anastasopoulos
- 链接：[arXiv](https://arxiv.org/abs/2610.40233) · [PDF](https://arxiv.org/pdf/2610.40233) · [HF](https://huggingface.co/papers/2610.40233)

While mining parallel sentences from web pages has proven effective for low-resource machine translation, the majority of the world's languages have little to no web presence. What they do have, though, are resources that are the result of centuries of efforts by linguists, such as grammars, dictionaries, and other documentation materials. We propose extracting translation examples from such linguistic resources,…

## 100. Latent Path Exploration via Potential-Guided Subtrajectory Balance

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, benchmark, language model
- 作者：Xiaoling Zeng, Qi Zhang
- 链接：[arXiv](https://arxiv.org/abs/2610.40283) · [PDF](https://arxiv.org/pdf/2610.40283) · [HF](https://huggingface.co/papers/2610.40283)

Continuous latent reasoning enables language models to perform intermediate computation without generating explicit reasoning traces. Advances in stochastic latent reasoning allow multiple paths to be sampled in continuous space, but stochasticity alone does not ensure effective exploration. A key challenge is guiding stochastic transitions between intermediate latent states toward useful reasoning paths. We…

## 101. DolphinRouting: Cluster-Level Binary Routing for Disaggregated LLM Inference Serving

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, language model, large language
- 作者：Yishuo Yuan, Shaoyu Yang, Chunrong Fang
- 链接：[arXiv](https://arxiv.org/abs/2610.40292) · [PDF](https://arxiv.org/pdf/2610.40292) · [HF](https://huggingface.co/papers/2610.40292)

Prefill-decode (PD) disaggregation isolates the two phases of large language model serving, but request-level path selection must account for prefill work, cache reuse, and decode demand. We present DolphinRouting, which learns this choice from end-to-end SLO feedback under a given P/D resource allocation. Requests are clustered by raw prompt length, cache-adjusted input lengths on both worker pools, and…

## 102. Decision and System One models in rheumatology: accuracy and calibration on specialty-training examination questions and diagnostic case vignettes

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, spec
- 作者：Alfredo Madrid-García, Diego Benavent, Fabian Lechner, Phillip Kremer, Johannes Knitza, Beatriz Merino-Barbancho
- 链接：[arXiv](https://arxiv.org/abs/2610.40318) · [PDF](https://arxiv.org/pdf/2610.40318) · [HF](https://huggingface.co/papers/2610.40318)

Objectives: To evaluate the accuracy and calibration of Decision and System One models on rheumatology examination questions and diagnostic vignettes. Methods: Two benchmarks were analysed: 172 rheumatology questions from Spanish specialty-training examinations (expanded RheumaMIR dataset) in Spanish and English, and 70 English diagnostic vignettes from RheumBench with 5-18 candidate diagnoses, 52 of which included…

## 103. A Unified Hessian-Guided Framework for Post-Training Quantization

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, language model, large language
- 作者：Mads Toftrup, Marco Federici, Boris van Breugel, Paul Whatmough, Markus Nagel
- 链接：[arXiv](https://arxiv.org/abs/2610.40345) · [PDF](https://arxiv.org/pdf/2610.40345) · [HF](https://huggingface.co/papers/2610.40345)

Low-bit quantization enables efficient deployment of large language models by reducing memory footprint and computational cost. Achieving high accuracy at low precision requires selecting quantization ranges, linear transformations, and weight rounding decisions. Existing approaches typically optimize these components independently using local reconstruction objectives, which fail to account for the varying impact…

## 104. HiFOR: Hierarchical Foresight with Action-Guided World Grounding for Vision-Language-Action Model

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, spec, retrieval
- 作者：Rongxing Ding, Hongyu Qu, Kehong Wu, Xudong Wang, Fan Zhang, Xinguang Xiang, Xiangbo Shu
- 链接：[arXiv](https://arxiv.org/abs/2610.40373) · [PDF](https://arxiv.org/pdf/2610.40373) · [HF](https://huggingface.co/papers/2610.40373)

Vision-Language-Action (VLA) models have demonstrated promising capabilities in robotic manipulation by integrating visual perception, language understanding, and action generation. Recent advances have further incorporated future prediction to enhance the understanding of environmental dynamics and task progression. However, existing methods often model short-term dynamics and long-term task objectives separately,…

## 105. Beyond Selected Breakthroughs: Evaluating Language Models on Randomly Sampled Mathematical Conjectures

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, language model, spec
- 作者：Helen Jenne, Davis Brown, Jesse He, Henry Kvinge
- 链接：[arXiv](https://arxiv.org/abs/2610.40382) · [PDF](https://arxiv.org/pdf/2610.40382) · [HF](https://huggingface.co/papers/2610.40382)

The last year has seen a shift in AI-assisted mathematics, with frontier language models producing proofs of and counterexamples to long-standing open conjectures. However, studying only the current set of major breakthroughs provides an incomplete picture of LLM capabilities and the computational resources needed to achieve reported results. To address this, we introduce a new dataset, OpenConjecture, which…

## 106. Algebraic World Model: From Exploration to Proofs

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, coding, spec
- 作者：Guancheng Pan, Qixin Tan, Yang Yuan, Andrew Chi-Chih Yao
- 链接：[arXiv](https://arxiv.org/abs/2610.40503) · [PDF](https://arxiv.org/pdf/2610.40503) · [HF](https://huggingface.co/papers/2610.40503)

AI has made remarkable progress in mathematics, solving challenging problems with machine-checkable proofs in Lean, yet typically relying on predefined mathematical definitions and formal specifications. This raises a natural question: can it reason rigorously about an unknown world? We introduce the Algebraic World Model (AWM), a framework that turns interaction with unfamiliar environments into explicit…

## 107. A Low-Rank Space Captures Linear Alignment Between LLM and Human Neural Activity During Naturalistic Language Listening

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：language model, large language, coding
- 作者：Zach Paris, Emily Finn
- 链接：[arXiv](https://arxiv.org/abs/2610.40511) · [PDF](https://arxiv.org/pdf/2610.40511) · [HF](https://huggingface.co/papers/2610.40511)

Large language models (LLMs) are increasingly used as computational models of human language processing, yet it remains unclear which components of their representations drive alignment with neural activity. Here, we use ridge reduced-rank regression to identify the brain-predictive subspace of LLM representations: the representational directions that support linear prediction of neural responses. Across three…

## 108. IndicIPR-QA: A Benchmark for Extractive Question Answering on Indian IPR Laws

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, spec
- 作者：M. Mohaiminul Islam, Muhammad Abulaish
- 链接：[arXiv](https://arxiv.org/abs/2610.40518) · [PDF](https://arxiv.org/pdf/2610.40518) · [HF](https://huggingface.co/papers/2610.40518)

Legal Question Answering (QA) over statutory texts is a challenging task in Natural Language Processing (NLP), especially in low-resource settings with complex legal systems. It requires answers that are precise and grounded in the law. However, to the best of current knowledge, no existing extractive QA benchmark provides exact answer spans from statutory texts across all seven Indian Intellectual Property Rights…

## 109. BURGER: Benchmarking and Understanding Robotic Generalization via Embodied Drawing

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, benchmark, spec
- 作者：Xiangyu Xu, Bangshuai Peng, Ziyi Liu, Mengjie Zhao, Chenhao Lu, Zhengyang Fan, Huazhe Xu, Kaizhe Hu
- 链接：[arXiv](https://arxiv.org/abs/2610.40532) · [PDF](https://arxiv.org/pdf/2610.40532) · [HF](https://huggingface.co/papers/2610.40532)

How effectively can vision-language-action (VLA) models learn diverse language-conditioned behaviors as training data scales? Investigating this question requires large and varied robot datasets, whose collection on physical robots remains costly. We introduce BURGER, a language-conditioned robotic drawing benchmark with a scalable, prompt-driven pipeline for generating continuous drawing trajectories, both in…

## 110. Machine Learning-Based Detection of Mobile Money Scan Messages in Ghana: A Comparative Evaluation of Naive Bayes, Support Vector Machine, and Randon Forest Classifiers

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, evaluation, spec
- 作者：Ibrahim Salifu, Muhaisin Tiyumba Nantogmah
- 链接：[arXiv](https://arxiv.org/abs/2610.40544) · [PDF](https://arxiv.org/pdf/2610.40544) · [HF](https://huggingface.co/papers/2610.40544)

Mobile money (MoMo) is Ghana's preferred retail payment channel, recording GHC518.4 billion in transactions in December 2025 and over 26.7 million active accounts (Graphic Online, 2026). This growth has coincided with increased social-engineering fraud over Short Message Service (SMS) and Unstructured Supplementary Service Data (USSD), where fraudsters impersonate network operators, agents, relatives, or regulators…

## 111. Retrieval as Traversal: Value-Indexed Memory for Stateful Long-Context Agents

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, memory, retrieval
- 作者：Daniel Strauß, Zhenshan Bing, Alois Knoll
- 链接：[arXiv](https://arxiv.org/abs/2610.40545) · [PDF](https://arxiv.org/pdf/2610.40545) · [HF](https://huggingface.co/papers/2610.40545)

Long-context models repeatedly solve closely related retrieval problems. Attention or global retrieval can retain large stores, but each forward pass again searches for what matters. Recurrent compression avoids this search only by deciding earlier what information to preserve. Neither mechanism directly exploits that useful memories at neighbouring retrieval steps may substantially overlap. We propose an…

## 112. Gym-Anything for Robotics: Scaling physical simulations with digital agents

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, benchmark, coding
- 作者：Pranjal Aggarwal, Sean Welleck
- 链接：[arXiv](https://arxiv.org/abs/2610.40565) · [PDF](https://arxiv.org/pdf/2610.40565) · [HF](https://huggingface.co/papers/2610.40565)

Realistic, fast robotics simulations could enable large-scale training of embodied AI models that transfer to the real world. However, despite decades of progress, available simulations cover only a narrow range of real-world tasks and physical phenomena. The core bottleneck is that creating better simulations requires significant expert effort and therefore does not scale. To address this, we introduce Gym-Anything…

## 113. Every Token Needs Its Own Teacher: Multi-teacher Adaptive On-policy Self-distillation

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, language model, large language
- 作者：Yifu Luo, Chuang Ma, Zeyu Chen, Enkelejda Kasneci, Qi Chen, Gjergji Kasneci
- 链接：[arXiv](https://arxiv.org/abs/2610.40574) · [PDF](https://arxiv.org/pdf/2610.40574) · [HF](https://huggingface.co/papers/2610.40574)

On-policy Self-distillation (OPSD) has proven effective for post-training large language models by constructing a teacher conditioned on privileged references. However, existing approaches keep the teacher fixed either throughout training by consistently exposing it to the full reference, or within each response by adaptively varying partial reference exposure only across responses. In this paper, we argue that…

## 114. PIVOT: Progressive Intervention via Online Teacher Correction

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, reinforcement learning, benchmark
- 作者：Zhihao Yang, Boyuan Zheng, Puhui Tan, Yukun Chen, Kuan Zhang, Longze Chen, Jiaming Li, Renke Shan, Lu Wang, Xianpei Han
- 链接：[arXiv](https://arxiv.org/abs/2610.40576) · [PDF](https://arxiv.org/pdf/2610.40576) · [HF](https://huggingface.co/papers/2610.40576)

Reinforcement learning from verifiable rewards (RLVR) is limited by sparse outcome-level feedback on hard reasoning tasks: when all rollouts in a group fail, rewards provide no learning signal. Stronger teachers can provide additional guidance, but this raises a central question: how can such signals be incorporated into RLVR to support successful rollouts while remaining learnable for the student? We distinguish…

## 115. Collaborative AI agents for autonomous experimental research with solid-state quantum spins

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, language model, large language
- 作者：El Mustapha Mansouri, Eikichi Kimura, Masato Koga, Keigo Arai
- 链接：[arXiv](https://arxiv.org/abs/2610.40589) · [PDF](https://arxiv.org/pdf/2610.40589) · [HF](https://huggingface.co/papers/2610.40589)

An autonomous research laboratory could conduct an entire study, from formulating questions to preparing manuscripts. Artificial intelligence (AI) offers one route towards this goal. Recent AI systems take on several research roles, but may draw conclusions that the evidence does not support. Here, we present an autonomous research laboratory in which agents based on large language models assess one another's work…

## 116. When to Assist and What to Suggest: Joint Gating and Memory-Grounded Hint Generation in One Compact Decoder

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, evaluation, retrieval
- 作者：A. J. A. Jubayer Talukder, Mohammad Ariful Haque
- 链接：[arXiv](https://arxiv.org/abs/2610.40611) · [PDF](https://arxiv.org/pdf/2610.40611) · [HF](https://huggingface.co/papers/2610.40611)

Proactive assistants offer short, memory-grounded hints during a conversation, deciding when to assist and what to suggest. Current systems split this between a gate and a larger generator; we evaluate both together on 28,058 decision points. Stage-wise generation scores are oracle-gate ceilings: behind a real gate, end-to-end exact match is 0.2619 against a ceiling of 0.2971, and end-to-end precision is 0.2387,…

## 117. Testimony from Timelines: Evidence-Grounded Significance Testing of Temporal Clinical Hypotheses

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, language model, spec
- 作者：Chengyang He, Wenlong Zhang, Koduvayur Subbalakshmi, Ping Wang
- 链接：[arXiv](https://arxiv.org/abs/2610.40619) · [PDF](https://arxiv.org/pdf/2610.40619) · [HF](https://huggingface.co/papers/2610.40619)

Ask a language model whether sales tend to dip after a product recall, or whether one side effect tends to follow another after a vaccine, and it answers in a fluent sentence that reads like a finding, with no test behind it. Assertions about how events unfold across many cases fill the Web, and each is a temporal hypothesis that only a significance test over the right records can settle. The verifier must specify…

## 118. Rethinking Neural Thickets Without Weight Perturbations

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, language model, spec
- 作者：Nicolas Dufour, Elouan Gardès, Amil Dravid, Patrick Pérez, Loic Landrieu
- 链接：[arXiv](https://arxiv.org/abs/2610.40649) · [PDF](https://arxiv.org/pdf/2610.40649) · [HF](https://huggingface.co/papers/2610.40649)

The Neural Thickets hypothesis posits that pretrained language models lie in dense neighborhoods of task-specific experts in weight space, which random Gaussian perturbations can uncover. We reproduce the reported gains, but show that they do not require this geometric explanation. Perturbing a single decoder block already recovers much of the improvement, while keeping the model entirely frozen and adding a random…

## 119. The Importance of Speech Genre for End-of-Turn Detector Training

- 分数：5.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：coding, spec
- 作者：Rini Sharon, Kadri Hacioglu, Jeena Prakash, Andreas Stolcke
- 链接：[arXiv](https://arxiv.org/abs/2610.39742) · [PDF](https://arxiv.org/pdf/2610.39742) · [HF](https://huggingface.co/papers/2610.39742)

End-of-turn (EoT) detection has been studied mostly through features, models, and modalities, while the speech genre of the training data has drawn far less attention. We isolate this factor. Using one reproducible annotation pipeline, we build a matched pair of corpora, multi-turn human-human conversational and single-turn human-machine, and train the same streaming ConvLSTM EoT detector on each. Across four test…

## 120. Multi-output LSTM soft sensors for industrial anaerobic co-digestion using LSTM-beta-VAE generative data augmentation

- 分数：5.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, evaluation
- 作者：Rohit Murali, Benaissa Dekhici, Tao Chen, Dongda Zhang, Michael Short
- 链接：[arXiv](https://arxiv.org/abs/2610.39768) · [PDF](https://arxiv.org/pdf/2610.39768) · [HF](https://huggingface.co/papers/2610.39768)

Anaerobic digestion (AD) requires close monitoring of key process variables, including pH, the ratio of volatile organic acids to alkaline buffer capacity and biogas production, to maintain biological stability and prevent process failure. While mechanistic frameworks such as the Anaerobic Digestion Model No. 1 are highly parameterised, computationally expensive, and difficult to calibrate for real-time…
