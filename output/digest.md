# 每日 AI 论文

生成时间：2026-10-30 05:49 UTC  ·  共 120 篇（已按 arXiv ID 去重）

来源：Hugging Face Daily Papers + arXiv（cs.AI / cs.LG / cs.CL / cs.CV）。
排序：HF 上榜、点赞、多源命中、兴趣词。兴趣词可在 `config.json` 改。

## 1. Efficient Streaming Audio-Visual Target Speaker Extraction for Real-World Acoustic Scenes

- 分数：32.0  ·  HF 赞：153  ·  来源：huggingface
- 兴趣命中：evaluation, benchmark
- 作者：Wendi Sang, Kai Li, Yifan Li, Jianqiang Huang, Xiaolin Hu
- 链接：[arXiv](https://arxiv.org/abs/2610.32749) · [PDF](https://arxiv.org/pdf/2610.32749) · [HF](https://huggingface.co/papers/2610.32749)

Streaming audio-visual target speaker extraction (AVTSE) is essential for latency-sensitive applications. However, current causal systems face two coupled gaps. First, standard benchmarks fix the number of speakers at two and ignore the near-/far-field interference, reverberation, and sudden noise of real scenes. Second, high-performance causal architectures are too heavy for edge deployment. Lightweight…

## 2. OmniShowcase: Omnidirectional Subject-Consistent Video Generation from Multi-View Images

- 分数：32.0  ·  HF 赞：49  ·  来源：huggingface
- 兴趣命中：evaluation, spec
- 作者：Junyeong Ahn, Geonwoo Kim, Kinam Kim, Gihwi Kim, Hoonjin Jung, Hyojin Jang, Jaegul Choo
- 链接：[arXiv](https://arxiv.org/abs/2610.35684) · [PDF](https://arxiv.org/pdf/2610.35684) · [HF](https://huggingface.co/papers/2610.35684)

Generating videos of a specific subject from a few reference images remains challenging when the camera reveals surfaces that are not visible in the input. Early subject-to-video (S2V) methods condition on a single reference image and must therefore infer the subject's unseen appearance and geometry as the viewpoint changes. To address this limitation, recent methods extend S2V to multiple reference views, providing…

## 3. Your Benchmark Is an Empirical Measure Over Difficulty

- 分数：30.0  ·  HF 赞：32  ·  来源：huggingface
- 兴趣命中：evaluation, benchmark, spec
- 作者：Yifan Sun, Naicheng Yu, Jiawen Gong, Jingyan Shen, Huan Zhang
- 链接：[arXiv](https://arxiv.org/abs/2610.29927) · [PDF](https://arxiv.org/pdf/2610.29927) · [HF](https://huggingface.co/papers/2610.29927)

A benchmark is not merely a collection of test questions; it naturally induces an empirical measure over difficulty. In this work, we develop this measure-based view of benchmark evaluation. This perspective allows us to identify and formalize two central failure modes: measure mismatch, where the benchmark difficulty distribution differs from the intended difficulty distribution, and coverage gaps, where uncovered…

## 4. RealCLI: Toward a Unified Evaluation of Human-Agent Collaboration for CLI Agents

- 分数：24.5  ·  HF 赞：17  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark, spec
- 作者：Yunqi Liu, Peiyu Wang, Bingli Wang, Leo Luo, Xuanwu Song, Xudong Ma, Hongxin Li, Yaxin Du, Weicheng Gu, Fanglin Xu, Yi Xing, XiangLong Liu, Jujie He, Zhange Zhang, Huatong Song, Zhaoyi Li, Deyang Kong, Chuan Hao, Peihao Wu, Mingjie Tang, Ran Tao, Jian Yang, Wayne Xin Zhao, Bryan Dai
- 链接：[arXiv](https://arxiv.org/abs/2610.22507) · [PDF](https://arxiv.org/pdf/2610.22507) · [HF](https://huggingface.co/papers/2610.22507)

Command-line interface (CLI) agents increasingly execute longer-horizon tasks, yet existing benchmarks either assume that user instructions remain fixed throughout execution or evaluate task outcomes without capturing runtime collaboration quality. In this paper, we present REALCLI, a paired benchmark that unifies the evaluation of task execution and human-agent collaboration quality on realistic CLI tasks. To…

## 5. TAO: Tool-Aware Joint Scheduling for LLM-Based Agentic Serving

- 分数：23.0  ·  HF 赞：18  ·  来源：huggingface
- 兴趣命中：agent, evaluation, spec
- 作者：Shuhuai Li, Shengdong Ye, Dongdong Ge, Yinyu Ye, Jianghao Lin
- 链接：[arXiv](https://arxiv.org/abs/2610.37230) · [PDF](https://arxiv.org/pdf/2610.37230) · [HF](https://huggingface.co/papers/2610.37230)

Agentic services alternate between model inference on clustered GPUs and external tools on distributed CPUs. In this scenario, existing systems (1) overlook tool-return readiness in service evaluation, wasting limited resources, and (2) use heuristic strategies to decide admission and placement on GPUs, resulting in suboptimal scheduling decisions. To bridge this gap, we present TAO, a tool-aware joint scheduling…

## 6. Sensorimotor Alignment: A Platonic Proxy for Embodied Policy Success

- 分数：22.5  ·  HF 赞：21  ·  来源：huggingface
- 兴趣命中：evaluation, language model
- 作者：Yunfei Xie, Howard H. Qian, Shiyi Lan, Kaiyu Hang, Chen Wei
- 链接：[arXiv](https://arxiv.org/abs/2610.31670) · [PDF](https://arxiv.org/pdf/2610.31670) · [HF](https://huggingface.co/papers/2610.31670)

Robot foundation models are typically evaluated through costly closed-loop rollouts, motivating low-cost offline proxies for model capability. The Platonic Representation Hypothesis (PRH) suggests that as representations improve, modalities such as vision and language converge toward a shared statistical model of reality. We ask whether motion trajectories form another such modality: as embodied models become more…

## 7. VibeGame: Prompt-to-Game Development with AI-Native Engine and Self-Evolving Adversarial Agent Team

- 分数：22.5  ·  HF 赞：13  ·  来源：huggingface
- 兴趣命中：agent, language model, large language, spec
- 作者：Wenbo Hu, Ken Li, Jiazhe Wei, Yukang Cao, Weiyi Hong, Jiayi Dai, Chenjun Bai, Jiajun Liang, Yucheng Liao, Ruichuan An, Zeyu Lou, Haofan Wang, Yueming Lyu, Jingkang Yang, Ziwei Liu, Chenyang Si
- 链接：[arXiv](https://arxiv.org/abs/2610.33106) · [PDF](https://arxiv.org/pdf/2610.33106) · [HF](https://huggingface.co/papers/2610.33106)

Large language model agents have enabled software development through natural-language interaction, but extending this paradigm to end-to-end game development remains challenging. Building a playable game requires coordinating code, scenes, assets, animations, physics, and configurations, while allowing developers to validate their integrated behavior through interactive testing. We introduce VibeGame, a framework…

## 8. Co-Design Bench: Multimodal Collaborative Coding Evaluation for Agentic Models

- 分数：22.0  ·  HF 赞：12  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark, coding
- 作者：Xilin Wei, Shengyuan Ding, Xinyu Fang, Tiancheng Gu, Yuchi Wang, Zhixun Li, Ziyu Liu, Yuhang Zang, Weixiang Yu, Cheng Lu, Chonggao Sun, Tong Zhou, Dahua Lin, Hang Zhang, Shuai Bai, Dayiheng Liu
- 链接：[arXiv](https://arxiv.org/abs/2610.35138) · [PDF](https://arxiv.org/pdf/2610.35138) · [HF](https://huggingface.co/papers/2610.35138)

Evaluating human-AI co-design requires testing whether coding agents can translate real users' multimodal requests into working application revisions. We introduce Co-Design Bench, a reference-free benchmark of 273 tasks curated from 37,463 deduplicated queries across 26,314 real user coding sessions. Its two tracks, Multimodal Editing (ME) and Repository Editing (RE), cover localized edits with optional image,…

## 9. WorkFactory: Turning Professional Intents into Executable Work for Scalable Agent Training

- 分数：21.5  ·  HF 赞：11  ·  来源：huggingface
- 兴趣命中：agent, benchmark, spec, planning
- 作者：Ziyang Zeng, Tingyang Chen, Jia Deng, Qiyao Wang, Shuo Tang, Yike Yang, Tao Ren, Wayne Xin Zhao, Feng Chang, Jujie He, Chuan Hao, Ran Tao, Bryan Dai
- 链接：[arXiv](https://arxiv.org/abs/2610.37161) · [PDF](https://arxiv.org/pdf/2610.37161) · [HF](https://huggingface.co/papers/2610.37161)

Scaling supervised training for working agents requires diverse professional tasks that yield reliable expert demonstrations. However, missing or inconsistent task information can obstruct teacher execution and weaken the resulting supervision. We propose WorkFactory, a scalable framework for constructing coherent and executable professional tasks. Starting from professional intents, information-level planning…

## 10. PersonaCUABench: Benchmarking Computer-Use Agents Serving Diverse Personas

- 分数：21.0  ·  HF 赞：14  ·  来源：huggingface
- 兴趣命中：agent, benchmark, spec
- 作者：Haoming Li, Defu Cao, Xu Hu, Yingtao Luo, Yiyang Wang, Xianghe Xu, Jiashu He, Wanting Jiang, Yifan Zhang, Yunhan Zhao, Siyang Wu, Chen Yang, Haixin Wang, Zheyuan Deng, Taoran Li, Jingwen Zhang, Zhejian Peng, Shushu Liang, Yue Zhao, Bingzhe Li, Feng Chen, Yifan Wang, Jintao Huang, Yijun Wang, Yuexing Hao, Xiaomin Li
- 链接：[arXiv](https://arxiv.org/abs/2610.22990) · [PDF](https://arxiv.org/pdf/2610.22990) · [HF](https://huggingface.co/papers/2610.22990)

Computer-use agents (CUAs) are commonly evaluated against fixed task specifications, but users may omit requirements, add constraints, or require approval before consequential actions. Completing the benchmark instruction does not guarantee serving the person who asked. We introduce PersonaCUABench, which holds 74 tasks across 11 domains fixed and varies only who asks. A persona agent, playing one of 44 personas in…

## 11. TauIndianBankBench: Procedure-Aware, Action-Oriented Evaluation of Tool-Using Conversational Agents

- 分数：20.5  ·  HF 赞：9  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark, language model
- 作者：Krishanu Adhikary, Prashant Devadiga
- 链接：[arXiv](https://arxiv.org/abs/2610.30161) · [PDF](https://arxiv.org/pdf/2610.30161) · [HF](https://huggingface.co/papers/2610.30161)

Many Indian banks serve customers through FAQ pages and scripted chatbots. Assistants based on language models could respond faster and carry out requests such as blocking a card, but only if they give correct information and follow the bank's rules. These rules prescribe a procedure, a set of required steps, such as obtaining a closure quote before closing a deposit. Adapting models to this domain requires…

## 12. A Broader Look into MLLM's Retrieval Heads

- 分数：20.0  ·  HF 赞：12  ·  来源：huggingface
- 兴趣命中：language model, large language, retrieval
- 作者：Jia Wang, Yuqing Li, Jiangnan Li, Zheng Lin, Mo Yu
- 链接：[arXiv](https://arxiv.org/abs/2610.32411) · [PDF](https://arxiv.org/pdf/2610.32411) · [HF](https://huggingface.co/papers/2610.32411)

Locating relevant evidence in long inputs is a core capability of Multimodal Large Language Models. Prior studies attribute this capability to retrieval heads, a sparse set of attention heads that transfer information from the context to the output. However, these analyses are confined to a limited set of modalities and the corresponding models. Moreover, how retrieval heads can be leveraged to enhance the model…

## 13. Amortizing Sequential Experimental Design in Reasoning LLMs

- 分数：19.0  ·  HF 赞：6  ·  来源：huggingface
- 兴趣命中：reasoning, benchmark, language model, large language, spec
- 作者：Anita Kriz, Antonin Berthon, Nicolás Astorga, Mihaela van der Schaar
- 链接：[arXiv](https://arxiv.org/abs/2610.20832) · [PDF](https://arxiv.org/pdf/2610.20832) · [HF](https://huggingface.co/papers/2610.20832)

Despite their extensive pretraining knowledge and strong reasoning capabilities, large language models (LLMs) struggle to adaptively gather information in experimental design tasks. We study how to amortize sequential Bayesian experimental design (BED) into an LLM by explicitly training the reasoning that guides action selection using information-gain rewards. Our approach specifies the experimental generative model…

## 14. LongZero: Enhancing Long-Context Reasoning in LLMs from Zero Data

- 分数：19.0  ·  HF 赞：6  ·  来源：huggingface
- 兴趣命中：reasoning, reinforcement learning, benchmark, language model, large language, retrieval
- 作者：Zhennan Wan, Jianfei Chen
- 链接：[arXiv](https://arxiv.org/abs/2610.30132) · [PDF](https://arxiv.org/pdf/2610.30132) · [HF](https://huggingface.co/papers/2610.30132)

Reinforcement learning (RL) is an effective way to strengthen the long-context reasoning of large language models (LLMs), but it needs training data that are long, diverse, challenging, and verifiable. Human annotation of such data is expensive, naturally occurring data are too scarce to sustain RL, and existing synthesis methods depend on external corpora or stronger teacher models, which become harder to obtain as…

## 15. IntReal: A Real-World Dataset and Benchmark for Multimodal Interleaved Generation

- 分数：18.5  ·  HF 赞：9  ·  来源：huggingface
- 兴趣命中：evaluation, benchmark, spec
- 作者：Shaohan Yu, Jie Qin, Wende Tan, Haiwen Diao, Limeng Qiao, Yueming Lyu, Chenyang Si
- 链接：[arXiv](https://arxiv.org/abs/2610.38425) · [PDF](https://arxiv.org/pdf/2610.38425) · [HF](https://huggingface.co/papers/2610.38425)

Humans routinely consume multimodal content, where textual and visual information is naturally interleaved. Although Unified Multimodal Models (UMMs) can jointly generate text and images, multimodal interleaved generation remains largely underexplored. Progress in this area is hindered by two key limitations: (1) the lack of well-defined interleaved generation tasks and corresponding training data, and (2) the…

## 16. AskStream: When and What to Ask Proactively under Uncertainty in Streaming Video Understanding

- 分数：18.5  ·  HF 赞：5  ·  来源：huggingface
- 兴趣命中：agent, benchmark, language model, large language
- 作者：Lu Wang, Zhuoran Jin, Longxiang Wang, Junhong Chen, Yupu Hao, Yao Xu, Daojian Zeng, Yubo Chen, Kang Liu, Guang Liu, Jun Zhao
- 链接：[arXiv](https://arxiv.org/abs/2610.38678) · [PDF](https://arxiv.org/pdf/2610.38678) · [HF](https://huggingface.co/papers/2610.38678)

Recent advances in multimodal large language models have increased interest in interaction paradigms for video understanding. The evolution from offline to streaming and proactive interaction has gradually shifted models from passive responders toward more proactive agents that can decide when to answer. However, existing proactive paradigms typically assume that the information required to answer a query is…

## 17. WebAnything: From the Wild Web to Scalable Agent Environments

- 分数：18.0  ·  HF 赞：8  ·  来源：huggingface
- 兴趣命中：agent, evaluation, spec
- 作者：Tianci Xie, Zikun Cai, Chaoyun Zhang, Pinxue Guo, Bingxuan Li, Rui Zheng, Hang Yan
- 链接：[arXiv](https://arxiv.org/abs/2610.37786) · [PDF](https://arxiv.org/pdf/2610.37786) · [HF](https://huggingface.co/papers/2610.37786)

Web agents require diverse, executable, and resettable website environments for reproducible training and evaluation. Human-assisted mirrors demand per-site engineering, while generative construction can diverge from specified real websites. Capture-and-replay preserves observations, with interaction coverage constrained by captured content and replay capabilities.   We present WebAnything, a fully automated…

## 18. CausGround: Causal Interaction Grounding for Adaptive Embodied Planning

- 分数：18.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：reasoning, benchmark, language model, large language, spec, planning
- 作者：Yijun Shen, Diqi He, Jinbang Guo, Wanyue Zhang, Jiaming Mi, Huan Yang, Zhongyuan Wang, Zhiwei Yu, Kai Zhang
- 链接：[arXiv](https://arxiv.org/abs/2610.29702) · [PDF](https://arxiv.org/pdf/2610.29702) · [HF](https://huggingface.co/papers/2610.29702)

Multimodal large language models (MLLMs) show promising reasoning capabilities, but reliable physical interaction requires planning that accounts for when actions are executable and how they change the world. These preconditions and effects are environment-dependent and often not captured by MLLMs, making adaptation challenging. Yet existing approaches either require costly environment-specific training or rely on…

## 19. Evaluating DeepSeek V4.1 Flash-1017 for loss of control and harmful manipulation risks

- 分数：18.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：agent, reasoning, evaluation, benchmark, language model
- 作者：Yao Huang, Zhiyuan Zeng, Yu Wang, Zhitong Zhu, Dingcheng Duan, Hao Li, Shangzhi Xu, Yifan Wang, Jinzhe Tu, Shukun Xiong, Yihe Zang, Han Yan, Hongchang Yang, Fuyu Gu, Wei Xu, Yinpeng Dong, Xiaojian Li
- 链接：[arXiv](https://arxiv.org/abs/2610.35671) · [PDF](https://arxiv.org/pdf/2610.35671) · [HF](https://huggingface.co/papers/2610.35671)

As frontier language models grow increasingly capable and autonomous, independent third-party evaluations are critical for characterizing their systemic safety risks. While closed-source releases are routinely accompanied by comprehensive system cards, open-weight models receive less scrutiny regarding frontier risks. To address this gap, we present an independent safety evaluation of DeepSeek V4.1 Flash-1017, the…

## 20. WeVisCut: The Whole Editing Room in One Agent From Narration to Long-Form Video

- 分数：17.0  ·  HF 赞：10  ·  来源：huggingface
- 兴趣命中：agent, benchmark
- 作者：Chenyu Mu, Wenming Weng, Qinrui Wang, Xingsong Ye, Hao Yu, Jun He, Chong Sun, Chen Li, Jing Lyu, Erkun Yang, Cheng Deng
- 链接：[arXiv](https://arxiv.org/abs/2610.38352) · [PDF](https://arxiv.org/pdf/2610.38352) · [HF](https://huggingface.co/papers/2610.38352)

Producing long-form videos from narration requires interdependent decisions that remain coherent across shots. Existing agentic editors often use multi-stage workflows driven by general models, leaving the quality-cost trade-off of compact, task-adapted policies unclear. We address this gap with WeVisCut, a long-form script-to-video system that connects tool execution with policy learning. Its agent harness…

## 21. EditAgent: Rethinking Agentic Image Editing

- 分数：16.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：agent, benchmark, spec
- 作者：Haiyang Xu, Tianyu Wang, Jialu Li, Jiteng Mu, Yuanjun Xiong, Jianming Zhang, Zhuowen Tu, Mingze Xu
- 链接：[arXiv](https://arxiv.org/abs/2610.39664) · [PDF](https://arxiv.org/pdf/2610.39664) · [HF](https://huggingface.co/papers/2610.39664)

Agentic image editors decompose complex requests into steps, but when a step fails, they mostly retry with the same narrow set of tools and a judge that scores each output by eye directly. We argue that such agents are bounded by two spaces: the action space of what the agent can do, and the observation space of what its judge can see. On our expert-annotated benchmark, a general-purpose editor yields no usable…

## 22. SO-101 Bench: Accessible Spatial Manipulation

- 分数：16.0  ·  HF 赞：0  ·  来源：huggingface
- 兴趣命中：agent, memory, evaluation, benchmark, language model, planning
- 作者：Truman Hickok
- 链接：[arXiv](https://arxiv.org/abs/2610.36420) · [PDF](https://arxiv.org/pdf/2610.36420) · [HF](https://huggingface.co/papers/2610.36420)

Low-cost arms such as the SO-101 have become the most common entry point to robot learning, yet no released policy performs spatially constrained, language-conditioned tasks on them out of the box, and existing SO-101 benchmarks run only on physical hardware with simple tasks and few held-out objects. We introduce SO-101 Bench, a simulated benchmark for language-conditioned spatial manipulation built on an Isaac Lab…

## 23. LOB-Impact Benchmark: Emergent Market Impact in Generative Limit Order Book Models

- 分数：15.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：agent, context window, benchmark
- 作者：George Nigmatulin, Valentin Mohl, Sascha Frey, Kang Li, Aramis Marti-Shahandeh, Mihai Cucuringu, Anisoara Calinescu, Jakob Foerster, Stefan Zohren
- 链接：[arXiv](https://arxiv.org/abs/2610.27100) · [PDF](https://arxiv.org/pdf/2610.27100) · [HF](https://huggingface.co/papers/2610.27100)

Realistic market impact is essential for generative limit order book (LOB) models to serve as world models for trading agents. If a simulator misprices this mechanism, agents learn policies that are optimal in the simulator but wrong in the real market. Existing metrics assess generated streams purely through distributional comparison with historical data, leaving counterfactual response to an agent's own orders…

## 24. OmniSpectra: A Unified Foundation Model for Universal Spectra Representation Learning

- 分数：15.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：benchmark, coding, spec
- 作者：Md Khairul Islam, Zeyu Xia, Adam S. Bolton, Judy Fox
- 链接：[arXiv](https://arxiv.org/abs/2601.15351) · [PDF](https://arxiv.org/pdf/2601.15351) · [HF](https://huggingface.co/papers/2601.15351)

Standard sequence models encode position by token rank rather than physical coordinate, typically forcing practitioners to destructively resample continuous physical signals such as spectra observed across heterogeneous instruments. We identify this coordinate mismatch as a structural limitation in cross-instrument representation learning, and propose OmniSpectra, a wavelength-native foundation model for spectral…

## 25. HairDeck: Animation-Ready Stylized Hair Cards from a Single Image

- 分数：13.5  ·  HF 赞：3  ·  来源：huggingface + arxiv
- 兴趣命中：-
- 作者：Yuze He, Yixiang Wei, Wang Zhao, Chuhao Chen, Yanning Zhou, Yong-Jin Liu
- 链接：[arXiv](https://arxiv.org/abs/2610.40599) · [PDF](https://arxiv.org/pdf/2610.40599) · [HF](https://huggingface.co/papers/2610.40599)

The hair of stylized characters in games and avatars is built from hair cards: artist-placed ribbons whose geometry is the visible hair, animated by spring bones. Existing image-based methods produce realistic hair or a single fused mesh, while CHARM, the only generator of stylized hair cards, decodes a hairstyle autoregressively as a long sequence of control points. Observing that a card hairstyle is an unordered…

## 26. CoSTA: Compressed Speech Token Adaptation for Efficient Spoken Dialogue Models

- 分数：13.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：benchmark, coding
- 作者：Yingzhuo Deng, Chong Li, Bingxin Liu, Yi Shu, Tianyu Peng, Can Xie, Siyao Song, Shuo Ren, Jiajun Zhang
- 链接：[arXiv](https://arxiv.org/abs/2610.21143) · [PDF](https://arxiv.org/pdf/2610.21143) · [HF](https://huggingface.co/papers/2610.21143)

Spoken Dialogue Models (SDMs) typically share a speech-token space for generation and synthesis, leading to long autoregressive sequences and costly inference. Lower-rate speech tokenizers shorten sequences but may introduce compression-quality trade-offs and costly replacement without breaking this coupling. To address this limitation, we propose CoSTA, a compatibility-preserving post-hoc framework that decouples…

## 27. After One-Click Video: The Inflow of Service-Type Content, the Failure of the Recommendation Pool Mechanism, and the BoLe System

- 分数：13.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：language model, large language
- 作者：Bo Zou, Chao Xu
- 链接：[arXiv](https://arxiv.org/abs/2610.37695) · [PDF](https://arxiv.org/pdf/2610.37695) · [HF](https://huggingface.co/papers/2610.37695)

In September 2026, a new large language model was released. Soon after, a new way of making explainer videos became very popular: people asked the model to write a program, and the program produced the video. "One-click video" content then appeared in large amounts on many platforms. On the surface, this is a rise in creative power at the level of the individual. We argue that, at a deeper level, it changes the…

## 28. PreView: Enhancing GUI Grounding with Preprocessed Views and Cues

- 分数：13.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：benchmark, spec
- 作者：Wenjun Hou, Kaishuai Xu
- 链接：[arXiv](https://arxiv.org/abs/2610.33645) · [PDF](https://arxiv.org/pdf/2610.33645) · [HF](https://huggingface.co/papers/2610.33645)

GUI grounding requires locating small controls in cluttered screenshots and identifying which control a natural-language instruction refers to. Cropping and enlargement can expose local detail, but the resulting image may still leave ambiguity about the intended target. We propose PreView, an auxiliary preprocessor that improves the inputs to an existing grounding model without further training that model. PreView…

## 29. HuGe: Scaling Humanoid Generalist Vision-Language-Action Models with Egocentric Experience

- 分数：13.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：benchmark, spec
- 作者：Yang Liu, Jiacheng Liu, Hengtao Li, Yuheng Huang, Zijian Yang, Ji Dai, Maoxin Wang, Yi Gao, Qishen Wang, Baohua Yin, Peiyang Li, Shuanghao Bai, Mingyang Sun, Pengxiang Ding, Jianqin Yin, Lixin Yang, Donglin Wang
- 链接：[arXiv](https://arxiv.org/abs/2610.34186) · [PDF](https://arxiv.org/pdf/2610.34186) · [HF](https://huggingface.co/papers/2610.34186)

Extending Vision-Language-Action models (VLAs) to humanoid robots requires coordinated whole-body control and diverse demonstrations that are costly to collect in real-world scenarios. Although egocentric human demonstrations provide a complementary source of task experience, differences in visual embodiment and missing robot proprioception complicate transfer to humanoid policies. To address these challenges, we…

## 30. Instruction Capacity: Behavior and Degradation of Language Models under Controlled Load

- 分数：13.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：language model, coding
- 作者：Hennadii Kutomanov
- 链接：[arXiv](https://arxiv.org/abs/2610.36095) · [PDF](https://arxiv.org/pdf/2610.36095) · [HF](https://huggingface.co/papers/2610.36095)

The quality with which language models follow instructions falls as the load grows, yet there is still no quantity that expresses the limit of a model in units of load with an uncertainty. We propose an instrument in which the load consists of rules that replace single-token words in a text without meaning: such an instruction is atomic, the rules are independent by the construction of the task, and the outcome of…

## 31. Your LR Schedule May Not Be Principled: Effective Learning Rate Scheduling in Weight-Normalized Training

- 分数：12.5  ·  HF 赞：1  ·  来源：huggingface + arxiv
- 兴趣命中：-
- 作者：Qifan Yu, Xinyu Ma, Xingyan Bin, Di He
- 链接：[arXiv](https://arxiv.org/abs/2610.40362) · [PDF](https://arxiv.org/pdf/2610.40362) · [HF](https://huggingface.co/papers/2610.40362)

Weight-normalized (WN) training is emerging as a compelling alternative to conventional weight decay (WD), with recent studies reporting substantial pretraining loss gains. We show that these gains are driven primarily by the induced effective learning rate (ELR) trajectory rather than by normalization alone. Matching ELR trajectories largely collapses the training loss dynamics of WN and WD. Schedule design should…

## 32. Intrinsic Distribution Matching

- 分数：12.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：evaluation, spec
- 作者：Deyuan Liu, Yansen Han, Kaiwen Zheng, Jun Xie, Jiacheng Liu, Zhenglin Cheng, Peng Sun, Jintao Zhang, Jianguo Li, Tao Lin
- 链接：[arXiv](https://arxiv.org/abs/2610.39633) · [PDF](https://arxiv.org/pdf/2610.39633) · [HF](https://huggingface.co/papers/2610.39633)

One-step and few-step text-to-image generation must accurately render the details specified in the prompt despite limited opportunities for refinement. Distribution matching distillation (DMD) uses score differences to bring the generated distribution closer to a reference distribution. Following prior work, we estimate this difference with internal velocity branches, avoiding a separate fake-score network. We ask…

## 33. Know, then Draw: A New Learning Paradigm for Visual Generation

- 分数：9.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：-
- 作者：Yucheng Mao, Chongjian Ge, Zhuowen Tu, Hao Tan, Hanwen Jiang
- 链接：[arXiv](https://arxiv.org/abs/2610.37626) · [PDF](https://arxiv.org/pdf/2610.37626) · [HF](https://huggingface.co/papers/2610.37626)

Visual generation requires both high-level semantic knowledge and fine-grained pixel details. We propose a learning paradigm that assigns these roles to autoregressive pretraining for knowledge acquisition and diffusion post-training for high-fidelity rendering. Within this framework, we study the objective, representation, and scaling of knowledge acquisition and rendering. Controlled comparisons identify…

## 34. Bank-World: A Benchmark for Evaluating Agents on Banking Workflows

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, evaluation, benchmark, spec
- 作者：Daniel Rupawalla
- 链接：[arXiv](https://arxiv.org/abs/2610.39733) · [PDF](https://arxiv.org/pdf/2610.39733) · [HF](https://huggingface.co/papers/2610.39733)

Bank-World is a benchmark of 50 banking tasks across two simulated institutions. Completing banking work requires more than producing the right calculation: agents must reconcile records, obtain permission, execute transactions, and keep instructions and status reports consistent as circumstances change. Bank-World tests these requirements through single-turn assignments and multi-turn interactions with simulated…

## 35. Finding Is Not Returning, Returning Is Not Reconstructing: A Multi-Dimensional Evaluation of Agent Social Re-entry

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, memory, evaluation, language model, large language, spec, retrieval
- 作者：Sheng Wan, Cong Ma, Sichen Dong, Qian'Ang Mao, Chenhan Zhang, Daning Hu, Qiang Yang
- 链接：[arXiv](https://arxiv.org/abs/2610.39781) · [PDF](https://arxiv.org/pdf/2610.39781) · [HF](https://huggingface.co/papers/2610.39781)

As Large Language Model (LLM) agents increasingly participate in persistent social environments, understanding their long-term social interaction capabilities becomes increasingly important. While existing research has advanced long-term memory and conversational context retrieval, less attention has been paid to whether agents can autonomously re-engage with previously inactive conversations. In particular,…

## 36. Revisiting Over-refusal in Safety-aligned Large Language Models: A Representation and Optimization Perspective

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, language model, large language, spec
- 作者：Chao Chen, Pengyang Shao, Wei Qin, Shijie Hao, Fei Shen, Richang Hong
- 链接：[arXiv](https://arxiv.org/abs/2610.39802) · [PDF](https://arxiv.org/pdf/2610.39802) · [HF](https://huggingface.co/papers/2610.39802)

Over-refusal is a critical side effect of safety alignment in large language models (LLMs), causing harmless but superficially risky queries to be mistakenly rejected. Despite the effectiveness of existing mitigation methods, why safety-aligned LLMs may still reject harmless queries under correct safety supervision remains insufficiently understood. To address this gap, we analyze over-refusal through the lens of…

## 37. Aligning Medical Vision Language Models at the Capability Boundary with Entropy Adaptive Rubric Grounding

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, reinforcement learning, benchmark, language model, spec
- 作者：Hongyu Bai, Jiaqi Zeng, Chunzheng Zhu
- 链接：[arXiv](https://arxiv.org/abs/2610.39835) · [PDF](https://arxiv.org/pdf/2610.39835) · [HF](https://huggingface.co/papers/2610.39835)

Medical diagnostic reasoning requires verifiable links between visual evidence and clinical knowledge, yet current medical vision language models are aligned with objectives that reward the wrong behavior. Uniform supervised fine tuning lets easy cases dominate updates while clinically critical boundary cases saturate prematurely. Sparse rewards based only on final-answer correctness cannot assess anatomical…

## 38. DWISE: Denoising Workload-Informed Scheduling Engine

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：language model, large language, coding, spec
- 作者：Lie Li, Wen Li, Junxiao Shen, Jindong Gu, Guosheng Hu
- 链接：[arXiv](https://arxiv.org/abs/2610.39852) · [PDF](https://arxiv.org/pdf/2610.39852) · [HF](https://huggingface.co/papers/2610.39852)

Unlike autoregressive large language models (AR-LLMs), diffusion LLMs (dLLMs) generate text by iteratively denoising many tokens in parallel, offering a promising path to efficient inference. Existing serving frameworks, however, schedule dLLM requests with policies designed for AR models, namely first-come-first-served (FCFS) admission and prefill priority. We find that both policies are ill-suited to dLLMs,…

## 39. Attention, Dynamic Wave and Hybrid Sequence Mixers in Language Models

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, long context, language model, large language
- 作者：Dmytro Babarytskyi, Oleksandr Babarytskyi
- 链接：[arXiv](https://arxiv.org/abs/2610.39854) · [PDF](https://arxiv.org/pdf/2610.39854) · [HF](https://huggingface.co/papers/2610.39854)

Large Language Models (LLMs) rely on Multi-Head Attention (MHA) for sequence modeling, but scaling to long contexts is constrained by the quadratic cost of attention, motivating sub-quadratic recurrent alternatives. This paper formalizes a Dynamic Wave recurrent layer, based on input-dependent exponential damping and cosine phase modulation, and evaluates three 10.94M-parameter configurations (Pure Transformer, Pure…

## 40. Turing LLM Post-Training: Calibrated Distillation and Efficient Dynamic-MoE Execution

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, evaluation, benchmark, spec
- 作者：Yue He, Jiahui Hu, Shaman Tang, Hua Zhou, Qiman Wu, Menglin Li, Yizhao Wang, Yuheng Zhang, Da Zhu, Zhou Wang, Anhua Liu, Hanlin Chen, Mingyuan Wang, Rui Xin, Yuhua Wei, Shuang Su, Siqi Liu, Kai Yang, Weichao Huang, Hang Zhang, Honggou Yang, Xianming Liu
- 链接：[arXiv](https://arxiv.org/abs/2610.39876) · [PDF](https://arxiv.org/pdf/2610.39876) · [HF](https://huggingface.co/papers/2610.39876)

We study post-training for dynamically routed mixture-of-experts (MoE) models, focusing on integrating independently optimized specialists while keeping consolidation efficient. Our approach combines calibrated multi-teacher on-policy distillation (C-MOPD), which matches each selected teacher on a local Top-$K$ support with teacher-wise loss normalization and clipping, with an execution path that uses post-capacity…

## 41. PhysAg3D: Bridging 3D Generative and Agentic Models for High-Fidelity and Physically-Interactive Assets

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, tool use, reasoning, evaluation, benchmark
- 作者：Bi'an Du, Fanpeng Meng, Jiemin Fang, Chen Yang, Pufan Li, Daizong Liu, Qi Tian, Wei Hu
- 链接：[arXiv](https://arxiv.org/abs/2610.39924) · [PDF](https://arxiv.org/pdf/2610.39924) · [HF](https://huggingface.co/papers/2610.39924)

Generating interactive 3D assets from a single image requires realistic appearance, fidelity to the depicted object, and plausible physical behavior. Yet detailed geometry alone does not determine how an object should move or deform. We introduce PhysAg3D, which couples 3D generative models with agentic reasoning and tool use. A vision-language agent first infers semantic parts, candidate interactions, and physical…

## 42. Learning Calibrated Confidence for Multi-Agent Collaboration

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reasoning, reinforcement learning, spec, retrieval
- 作者：Chenxiao Fan, Chongming Gao, Gangyi Zhang, Yaxin Gong, Leyang Shen, Jiakai Wang, Dong Wang, Yang Liu, Haoyan Liu, Xinting Hu, Fuli Feng, Xiangnan He
- 链接：[arXiv](https://arxiv.org/abs/2610.39927) · [PDF](https://arxiv.org/pdf/2610.39927) · [HF](https://huggingface.co/papers/2610.39927)

Complex information seeking on the Web often requires collecting evidence from multiple documents and reasoning across them, as in multi-hop question answering. Multi-agent systems address such tasks by dividing work among specialized agents, where upstream agents produce intermediate answers and supporting evidence that downstream agents build upon. However, upstream answers vary in correctness, and most systems…

## 43. Low-Bit GDN Recurrent-State Quantization: Global Gradient-aware Allocation and Pure-Write Sliding Windows

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, reasoning, evaluation, spec
- 作者：Qinghang Huang, Xuchu Huang, Xunzhao Yin
- 链接：[arXiv](https://arxiv.org/abs/2610.39931) · [PDF](https://arxiv.org/pdf/2610.39931) · [HF](https://huggingface.co/papers/2610.39931)

Linear attention stores historical information in a recurrent state of fixed size, providing a compact memory representation for long-context inference. Reducing state precision further lowers per-request storage requirements, but quantized writeback errors enter subsequent recurrences, degrade prediction quality on long-reasoning tasks, and can be accompanied by repetitive generation and excessively long outputs.…

## 44. H$^2$R: Hierarchical Hint-Based Reward for Mathematical Reasoning via Reinforcement Learning

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, reinforcement learning, benchmark, language model, large language, spec
- 作者：He Tu, Siye Li, Hongyi Wen
- 链接：[arXiv](https://arxiv.org/abs/2610.39934) · [PDF](https://arxiv.org/pdf/2610.39934) · [HF](https://huggingface.co/papers/2610.39934)

Reinforcement Learning with Verifiable Rewards has shown great promise in enhancing mathematical reasoning in large language models. However, existing approaches provide limited intermediate supervision for complex, multi-step reasoning tasks. To bridge this gap, we propose \textbf{Hierarchical Hint-based Reward}, a framework that leverages the intrinsic sub-question structure of mathematical problems as structured…

## 45. MLLM-GS: Multimodal Large Language Model Prior-Guided Fast Novel View Synthesis in Extreme Environments

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, language model, large language, spec
- 作者：Zhiliang Wu, Xinye Zheng, Kun Li, Fei Wang, Hao Guo, Yanyan Wei, Guanghui Yue, Beier Zhu, Wei Zhou, Xun Yang
- 链接：[arXiv](https://arxiv.org/abs/2610.39936) · [PDF](https://arxiv.org/pdf/2610.39936) · [HF](https://huggingface.co/papers/2610.39936)

Novel view synthesis (NVS) in degraded scenes aims to reconstruct 3D scenes from multi-view observations affected by various degradations, and to generate clear and photorealistic images at unseen viewpoints. Despite recent advances, existing methods often rely on degradation-specific models, limiting their generalization across diverse extreme environments. Generative models provide rich visual priors, but their…

## 46. Mind The Gap (MTG-AD): Dataset and Fine-grained Evaluation for End-to-End Inline Audio Descriptions

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, language model, large language
- 作者：Subhashini Venugopalan, Jenny Tan, Taylor Roper, Jimmy Tobin, Anton Kast, Alicia Martin, Sam Sepah, Amy Pavel
- 链接：[arXiv](https://arxiv.org/abs/2610.39955) · [PDF](https://arxiv.org/pdf/2610.39955) · [HF](https://huggingface.co/papers/2610.39955)

Audio descriptions (AD) are essential for making visual media accessible to blind and low-vision (BLV) users. While Multimodal Large Language Models (MLLMs) offer a scalable solution for generating audio descriptions on-demand, their performance on ``inline'' audio descriptions -- which must fit within existing silences in a video -- remains under-explored, particularly for diverse user-generated content (UGC). We…

## 47. HEMO: Harness Self-Evolution for Multi-Objective Combinatorial Optimization

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, language model, large language, spec
- 作者：Jianghan Zhu, Cong Zhang, Ni Zhang, Yifan Yang, Yew Soon Ong, Zhiguang Cao
- 链接：[arXiv](https://arxiv.org/abs/2610.40023) · [PDF](https://arxiv.org/pdf/2610.40023) · [HF](https://huggingface.co/papers/2610.40023)

Automatic operator design (AOD) has increasingly adopted large language models (LLMs) to generate problem-specific search and variation operators for multi-objective combinatorial optimization (MOCO). Yet most methods evolve the operators while leaving the process that discovers them fixed. This limits adaptation as new Pareto trade-offs and operator interactions change where and how the search should proceed. We…

## 48. AI Cosmos: An Agentic Infra for Situated Learning

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, memory, reasoning, language model, large language, spec
- 作者： AI Cosmos Team, Jinfeng Zhou, Yuxuan Chen, Fangming Chang, Mingyu Su, Yifan Zhu, Yuan Wang, Bo Zhang, Bosi Wen, Chenhao Yuan, Chenwen Liao, Dazhi Jiang, Deyao Hong, Erle Zhu, Genrui Zhang, Guchan Li, Hongwen Gan, Huichao Bi, Jiahao Yan, Jincheng Fan, Kehan Zheng, Qinren Luo, Qiran Liu, Ruoqi Cao, Shizhi Zhang, Sihan Chen, Siyan Deng, Xuehan Zhou, Xujun Li, Yang Dang, Yanzhuo Zhu, Yu Zhang, Zheyu Chen, Hongning Wang, Manli Li
- 链接：[arXiv](https://arxiv.org/abs/2610.40031) · [PDF](https://arxiv.org/pdf/2610.40031) · [HF](https://huggingface.co/papers/2610.40031)

Large language models (LLMs) can improve task performance during learning, yet these gains do not necessarily reflect learners' ability to thereafter apply the knowledge and skills independently. We present AI Cosmos, an agentic infrastructure for situated learning that organizes learning around two complementary principles: scenario-based participation and cumulative assets of practice. AI Cosmos organizes learners…

## 49. It Takes Two to Probe, Thousands to Retrieve: Putting Vision--Language Probes to the Retrieval Test

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, language model, retrieval
- 作者：Ivana Beňová, Michal Gregor, Marián Šimko
- 链接：[arXiv](https://arxiv.org/abs/2610.40124) · [PDF](https://arxiv.org/pdf/2610.40124) · [HF](https://huggingface.co/papers/2610.40124)

Vision--language models (VLMs) are tested for fine-grained understanding with image--text matching probes, a model must prefer the correct image or caption over handcrafted negative. In retrieval, the correct item must beat thousands of alternatives. We measure how these two evaluation methods relate by using two probing benchmarks, \svo{} and SugarCrepe, for retrieval tasks. For 100 image and caption queries we…

## 50. VideoMemBench: How Well Do MLLMs Remember in Video Conversations?

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, evaluation, benchmark, language model, large language
- 作者：Zhengdong Hu, Chao Wang, Kaituo Feng, Huanjin Yao, Mingfei Lu, Hehe Fan, Yi Yang
- 链接：[arXiv](https://arxiv.org/abs/2610.40131) · [PDF](https://arxiv.org/pdf/2610.40131) · [HF](https://huggingface.co/papers/2610.40131)

Multimodal large language models (MLLMs) can now process hour-long videos, making extended multi-turn dialogue over a single video a natural mode of use. Sustaining such a dialogue requires more than answering each question in isolation: the model must retrieve and reuse information established earlier in the conversation, both what it has seen and what it has said, an ability we term in-context video memory.…

## 51. DynaRev: Benchmarking Web Agents under Dynamic Goal Revision

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, evaluation, benchmark, spec
- 作者：Shiqi Zhang, Guochen Zhou, Zesheng Wei, Hai Zhao, Zhisong Zhang
- 链接：[arXiv](https://arxiv.org/abs/2610.40133) · [PDF](https://arxiv.org/pdf/2610.40133) · [HF](https://huggingface.co/papers/2610.40133)

Web agents are typically evaluated with goals fully specified before execution and fixed thereafter, whereas real users often revise their requirements during interaction. To study such interactions, we introduce DynaRev, a benchmark of 181 tasks to evaluate web agents under dynamic goal revision. DynaRev uses semantic milestones to deliver revisions at task-defined stages, covers additive revisions, unconditional…

## 52. Locating and Closing Information Gaps in Multi-Agent Systems

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, tool use, reasoning, benchmark, planning
- 作者：Yaxin Gong, Chongming Gao, Gangyi Zhang, Chenxiao Fan, Leyang Shen, Jiakai Wang, Dong Wang, Yang Liu, Haoyan Liu, Xinting Hu
- 链接：[arXiv](https://arxiv.org/abs/2610.40186) · [PDF](https://arxiv.org/pdf/2610.40186) · [HF](https://huggingface.co/papers/2610.40186)

Multi-step Web tasks often require several LLM agents to gather and combine evidence. The communication graph of a fixed workflow restricts which agents can read each other's outputs: evidence retrieved by one agent may never reach the agent that needs it, leaving an information gap and an incomplete or incorrect answer. Adding a connection can deliver the missing evidence, but can also lead the receiver to adopt an…

## 53. Video Generation Meets Agent Harness: Agentic Video Generation, Agentic World Modeling and Recursive Self-Improvement

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, tool use, memory, evaluation, planning
- 作者：Liaoyuan Fan, Yuhao Zheng, Dongxing Mao, Hangyu Ran, Siyuan Hu, Weijia Mao, Rui Zhao, Weijia Wu, Guian Fang, Yanzhe Chen, Zeyu Zhu, Yuxin Jiang, Yiren Song, Yuchao Gu, Junchao Yi, Qi Hu, Dan Kong, Alex Jinpeng Wang, Kevin Qinghong Lin, Mike Zheng Shou, Wei Liu
- 链接：[arXiv](https://arxiv.org/abs/2610.40191) · [PDF](https://arxiv.org/pdf/2610.40191) · [HF](https://huggingface.co/papers/2610.40191)

Video generation is shifting from end-to-end synthesis toward agentic generation, where planning, tool use, and feedback enable coherent, controllable multi-shot videos. In parallel, video world models provide action-conditioned observations and predicted futures, serving as interactive environments for agents. We study their intersection through the agent harness: an executable runtime that constructs context,…

## 54. EnvOS: Auditing Computer-Use Agents When the World Moves On : Phenomenon-Based Task Construction, Certification, and Evidence-Based Evaluation

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reinforcement learning, evaluation, language model, large language
- 作者：Ankush Kadu, Athira Gopal, Niharika Singh, Arpit Jain, Aswanth Krishnan
- 链接：[arXiv](https://arxiv.org/abs/2610.40246) · [PDF](https://arxiv.org/pdf/2610.40246) · [HF](https://huggingface.co/papers/2610.40246)

Computer-use agents built on large language models (LLMs) work in software that can change while they act: an appointment moves, a policy is revised, a record is updated. Testing agents under such changes is harder than it looks. When an agent fails, the cause may be the agent, but it may also be a change that did not fire as intended, an update the agent never received, or a grader that scored the episode wrongly.…

## 55. When Requirements Interact: Scaling Long-Horizon Coding via Interdependent Specifications

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reasoning, reinforcement learning, benchmark, coding, spec
- 作者：Yishuo Cai, Minzheng Wang, Liang Zhao, Linghao Zhang, Lei Li, Shicheng Li, Xu Sun, Fuli Luo
- 链接：[arXiv](https://arxiv.org/abs/2610.40256) · [PDF](https://arxiv.org/pdf/2610.40256) · [HF](https://huggingface.co/papers/2610.40256)

To succeed in real-world long-horizon software development, coding agents must satisfy multi-dimensional task specifications, such as interface compatibility and error handling, and do so without breaking existing dependencies. However, current works lack specification in both quantity and diversity, often emphasizing primary goals while ignoring complex constraints. Synthesizing tasks to bridge this gap presents…

## 56. TaskFrame: Connecting Task-Level Planning with Frame-Level Control for Game Agents

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reasoning, evaluation, language model, spec, planning
- 作者：Guangzhi Wang, Junfu Pu, Yiran Wang, Xingyilang Yin, Honghao Chen, Cheng Cheng, Lingen Li, Yinan Zhou, Jiarui Wu, Yinuo Jiang, Hongbo Jin, Xiaodong Cun, Ying Shan
- 链接：[arXiv](https://arxiv.org/abs/2610.40276) · [PDF](https://arxiv.org/pdf/2610.40276) · [HF](https://huggingface.co/papers/2610.40276)

Building general game agents requires both high-level task reasoning and low-latency action control in rapidly changing visual environments. These capabilities favor models with substantially different computational profiles, making them difficult to realize within a single model. In this work, we present TaskFrame, a hierarchical planner-controller framework that connects task-level planning with frame-level…

## 57. Only Accepted Tokens Count: An Energy Accounting of Speculative Decoding Under Latency Targets

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, language model, large language, coding, spec
- 作者：Bole Ma, Ayesha Afzal, Jan Eitzinger, Harald Koestler, Gerhard Wellein
- 链接：[arXiv](https://arxiv.org/abs/2610.40287) · [PDF](https://arxiv.org/pdf/2610.40287) · [HF](https://huggingface.co/papers/2610.40287)

Large language model serving is limited by facility power. Energy per token determines how many tokens a datacenter can serve, while a latency target bounds how quickly each user receives them. During decode, every weight is read from memory for every generated token. Batching amortizes this read across users but makes no individual user faster. Speculative decoding does: a drafter proposes several future tokens,…

## 58. Don't Lose the Thread: Empowering Long-Horizon LLM Agents with Cognitive Resource Self-Allocation

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, memory, reasoning, benchmark, language model, large language, planning
- 作者：Zheng Zhu, Xiaozhuan Liang, Xi Chen, Bei Yu, Jiaya Jia
- 链接：[arXiv](https://arxiv.org/abs/2610.40350) · [PDF](https://arxiv.org/pdf/2610.40350) · [HF](https://huggingface.co/papers/2610.40350)

Agents powered by large language models (LLMs) have demonstrated remarkable progress in solving complex reasoning tasks. However, LLM agents often falter on long-horizon tasks due to cognitive overload, as their working memory becomes cluttered with expanding and irrelevant information, which dilutes their attention and hinders effective planning and reasoning. To mitigate this challenge, we introduce Cognitive…

## 59. The Athlete as a Scientist of One: Agentic Bayesian Experimental Design for Individualized Physiology from Consumer Wearables

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, benchmark, language model, large language, spec
- 作者：Behnam Moradi
- 链接：[arXiv](https://arxiv.org/abs/2610.40370) · [PDF](https://arxiv.org/pdf/2610.40370) · [HF](https://huggingface.co/papers/2610.40370)

Large language model (LLM) agents for personal health read wearable data and recommend, but do not learn about the individual in a way that can be audited or falsified. We present EpiCoach, an agentic system that treats one athlete, a cross-country mountain biker, as the subject of accountable N-of-1 science. Claims about the athlete live in an evidence-gated hypothesis registry: each must issue a probabilistic…

## 60. Agentic LLM reasoning in pediatric diabetes outcome prediction from multimodal medical records

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reasoning, language model, large language
- 作者：Daniel Palacios, Guantong Qi, Anna Kadi, Natali Borrego, Sukru Aras, Michael L. Ferm, Elizabeth Kubota-Mishra, Maria J. Redondo, Zhandong Liu, Mustafa Tosur, Hu Chen
- 链接：[arXiv](https://arxiv.org/abs/2610.40379) · [PDF](https://arxiv.org/pdf/2610.40379) · [HF](https://huggingface.co/papers/2610.40379)

Large language model (LLM) agents are proposed for clinical prediction but are untested in pediatrics, where cohorts are small and outcomes are uncommon. Using records from 2,489 youth with type 2 diabetes (T2D) and 4,018 with type 1 diabetes (T1D), spanning structured data, note-derived social determinants and, in T1D, continuous glucose monitoring data, we predicted seven T2D outcomes, four also in T1D, at 24…

## 61. Scaling Mathematical Proof Supervision from Structured Textbooks

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, evaluation, benchmark, language model
- 作者：Youqing Fang, Zhouqi Hua, Yinhao Tang, Yuzhe Gu, Lingkai Kong, Bin Liu, Weiming Zhang, Kai Chen, Yanan Sun, Wenwei Zhang
- 链接：[arXiv](https://arxiv.org/abs/2610.40394) · [PDF](https://arxiv.org/pdf/2610.40394) · [HF](https://huggingface.co/papers/2610.40394)

Mathematical supervision for language models is typically flattened into isolated problem-solution pairs, discarding the curricular organization and evidential structure of the original sources. We introduce TOME-Math (Textbook-Oriented Mathematical Evidence), a large-scale corpus that converts 2,118 textbooks spanning the core areas of university-level mathematics subjects into approximately 380K structured…

## 62. Retrieving from Your Own Mistakes: On-Policy Training of Embedding Models for Multi-Hop Retrieval-Augmented Generation

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, language model, coding, retrieval
- 作者：Chenjie Qiu, Zixuan Zeng, Shaobin Shi, Bingfeng Chen, Dongsheng Luo, Boyan Xu
- 链接：[arXiv](https://arxiv.org/abs/2610.40409) · [PDF](https://arxiv.org/pdf/2610.40409) · [HF](https://huggingface.co/papers/2610.40409)

Complex questions in retrieval-augmented generation require evidence spread over several documents, and an answer is reliable only when the retriever finds all of it. Chain embedding retrievers collect such evidence step by step, re-encoding the question together with the passages retrieved so far, and we find that they are already strong: trained only on gold histories, a small chain embedding retriever that calls…

## 63. Prefix Executability: Evaluating Tool-Using Agents Beyond Final Success

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, tool-use, evaluation, benchmark
- 作者：Amir H. Rezaeian, Weiyi Sun, Yassine Benajiba, Dan Roth
- 链接：[arXiv](https://arxiv.org/abs/2610.40444) · [PDF](https://arxiv.org/pdf/2610.40444) · [HF](https://huggingface.co/papers/2610.40444)

Tool-use benchmarks often score agents by final task success, but terminal outcomes can obscure whether the intermediate tool-call trajectory was executable. We propose prefix executability as a trajectory-level evaluation protocol for tool-using agents. The protocol measures whether every prefix of a predicted tool-call sequence remains executable under tool schemas, state preconditions, and data dependencies, and…

## 64. Reinforcement learning for control of partial differential equations

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reinforcement learning, evaluation, benchmark, spec
- 作者：Nicolò Botteghi, Matteo Tomasetto, Andrea Manzoni
- 链接：[arXiv](https://arxiv.org/abs/2610.40449) · [PDF](https://arxiv.org/pdf/2610.40449) · [HF](https://huggingface.co/papers/2610.40449)

Controlling dynamical systems governed by partial differential equations (PDEs) remains a challenging task in scientific computing, owing to high-dimensional state spaces, distributed actuation, nonlinear dynamics, and stringent real-time constraints. Reinforcement learning (RL) has emerged as a promising paradigm for synthesizing feedback controllers that adapt to varying operating conditions and can be deployed…

## 65. Training language models in simulation for psychiatric intake

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reinforcement learning, language model, planning
- 作者：Samuel Schmidgall, Tim Strother, Alex Bijamov, Min Woo Sun, Anil Palepu, Akshay Goel, Ulysse Marteau-Ferey, Théo Moutakanni, Yubin Kim, Joseph Breda, Christina Chen, Justin Chen, Paul Jhun, Andrew Marshall, Sarah Montgomery-Taylor, Eun Kyoung Hong, Shashank Ravi, Kameron C. Black, David J. H. Wu, Austin Schoeffler, John Lyon Havlik, Elizabeth C. Stade, Jared Moore, Johannes C. Eichstaedt, Logan Pierce, Jeff Jopling, Johannes Thrul, Thomas H. McCoy, Neguine Rezaii, Mark S. Chen, Ellen E. Fitzsimmons-Craft, Shirley Wang, Desmond C. Ong, Katharina Schultebraucks, Torrey Creed, Bhavna Daryani, Aleksandra Faust, S. Sara Mahdavi, Caroline Figueroa, Eric Lin, Kate H. Bentley, Ernest Lim, Zhihan Jiang, Xuhai "Orson" Xu, Daniel McDuff, John Torous, Yun Liu, Po-Hsuan Cameron Chen, Mike Schaekermann, Joelle Barral, Alvin Rajkomar, Tao Tu, Lin Yang, Isaac Galatzer-Levy, David Racz, Valentin Liévin
- 链接：[arXiv](https://arxiv.org/abs/2610.40476) · [PDF](https://arxiv.org/pdf/2610.40476) · [HF](https://huggingface.co/papers/2610.40476)

In psychiatric practice, the clinical intake interview remains a primary diagnostic instrument, requiring the clinician to establish rapport while disentangling complex, overlapping presentations. Here, we show that multi-turn reinforcement learning (RL) in simulation environments improves language model performance on structured text-based psychiatric intake, spanning history-taking, differential diagnosis, and…

## 66. Agentic University: Collaborative Agents for Personalized Learning

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, evaluation, language model, large language, spec
- 作者：Jingru Fan, Tianle Zhou, Yunjie Zhou, Zihao He, Yixuan Zhou, Kezhao Wu, Xinyu Zheng, Xiyuan Wang, Yuheng Wang, Zhi Li, Songhua Liu, Weinan E, Chen Qian
- 链接：[arXiv](https://arxiv.org/abs/2610.40492) · [PDF](https://arxiv.org/pdf/2610.40492) · [HF](https://huggingface.co/papers/2610.40492)

Large language models support personalized tutoring, content generation, and adaptive learning paths. However, capability development requires these resources and interactions to form a coherent learning process that evolves with the learner. A central challenge is to align goals, activities, and assessment while using learning evidence to decide what should follow. We introduce Human-Participatory Multi-Agent…

## 67. How I Aligned Your Model: Scaling Up Multilingual Safety Training with Templates

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, language model, large language, spec
- 作者：Max Neuwinger, Hanna Yukhymenko, Imanol Schlag
- 链接：[arXiv](https://arxiv.org/abs/2610.40516) · [PDF](https://arxiv.org/pdf/2610.40516) · [HF](https://huggingface.co/papers/2610.40516)

Safety alignment for Large Language Models is heavily focused on English with limited multilingual representation, particularly damaging low-resource language performance. Related open training datasets are often limited in size or do not follow region-localized harmful topics to broaden the scope of alignment beyond cultures. We propose a scalable template-based augmentation pipeline to produce massive multilingual…

## 68. CrossWeave: Cross-Modal Scene and Instance Retrieval from Sparse 2D-3D Alignment

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, coding, spec, retrieval
- 作者：Aadith Warrier, Gnana Prakash Punnavajhala, Siddharth Tourani, Muhammad Haris Khan, Avinash Sharma, Madhava Krishna
- 链接：[arXiv](https://arxiv.org/abs/2610.40525) · [PDF](https://arxiv.org/pdf/2610.40525) · [HF](https://huggingface.co/papers/2610.40525)

Cross-modal scene and instance retrieval aims to retrieve a corresponding 3D environment or object given query 2D images, serving as a foundational mechanism for spatial reasoning in robotics and AR/VR. Existing methods achieve this by learning alignment only at the level of whole scenes or objects, which provides no supervision for the fine-grained local structure within them. In this work, we show that supervision…

## 69. PhysCount: Do MLLMs Count Visual Appearances or Physical Entities?

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, language model, large language, spec
- 作者：Lidong Lu, Jiaxin Lv, Liangrui Dong, Xinyi Mao, Lidong Zou, Zhenquan Li, Tong Lu, Guo Chen
- 链接：[arXiv](https://arxiv.org/abs/2610.40530) · [PDF](https://arxiv.org/pdf/2610.40530) · [HF](https://huggingface.co/papers/2610.40530)

Images reveal appearances, but counting often asks about physical objects. A single entity may be visible directly, in several reflections, or through glass, so detecting every visible occurrence does not determine how many entities are present. Existing visual counting benchmarks rarely separate these two operations. We introduce PhysCount, a benchmark for evaluating whether multimodal large language models (MLLMs)…

## 70. On the Fundamental Limits of Prefill-Based Decoding Length Prediction

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, language model, large language, coding
- 作者：Haowen Shi, Xuzhe Yan, Fahao Chen, Peng Li
- 链接：[arXiv](https://arxiv.org/abs/2610.40541) · [PDF](https://arxiv.org/pdf/2610.40541) · [HF](https://huggingface.co/papers/2610.40541)

Predicting how many tokens a large language model (LLM) will decode, using only prefill-phase hidden states, is a key primitive for inference scheduling. We show that current benchmarks conflate predictor quality with task hardness: when the target model, dataset, or sampling configuration changes, reported accuracy collapses even though the predictor is unchanged. We trace this instability to an overlooked error…

## 71. Advancing Clinical Genomic Analysis with a Skill-Centred Agent

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, benchmark, spec, retrieval
- 作者：Qiaoyu Zheng, Weike Zhao, Yanjie Fan, Ye Cao, Mengqi Jiang, Xiao Zhou, Xiaoman Zhang, Pengcheng Qiu, Yongguo Yu, Yanfeng Wang, Ya Zhang, Chaoyi Wu, Weidi Xie
- 链接：[arXiv](https://arxiv.org/abs/2610.40556) · [PDF](https://arxiv.org/pdf/2610.40556) · [HF](https://huggingface.co/papers/2610.40556)

Clinical genomic analysis requires experts to integrate evolving guidelines, databases, and computational evidence. As sequencing has become increasingly accessible, this complex and labor-intensive process has become a major bottleneck to the timely use of genomic information in clinical decision-making. To fill this gap, we developed ClinGeX, a large-language-model agent that composes 105 curated executable skills…

## 72. VeriCUA: Verification as Agentic Exploration for Computer-Using Agents

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reinforcement learning, evaluation, language model, spec
- 作者：Qiushi Sun, Da Yu, Alexander Knop, Amer Sinha, Lingpeng Kong, Ben Kao, Ravi Kumar, Pritish Kamath
- 链接：[arXiv](https://arxiv.org/abs/2610.40578) · [PDF](https://arxiv.org/pdf/2610.40578) · [HF](https://huggingface.co/papers/2610.40578)

Building and scaling computer-using agents (CUAs) across desktop, mobile, and web environments requires reliable task-completion verification for data curation, evaluation, and reinforcement learning. Typical automated approaches prompt vision-language models (VLMs) to judge trajectories or generate programs to inspect application state. However, both rely on partial views of complex digital environments. VLM judges…

## 73. TextSeal2: Distortion-Free LLM Watermarking with Copula Mixing and Memoryless Races

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, language model, large language, coding, spec
- 作者：Tom Sander, Pierre Fernandez, Itai Gat, Haiming Bao, Jiaxin Shi, Jason Park, Valeriu Lacatusu, Sylvestre-Alvise Rebuffi, Hongyan Chang, Hady Elsahar, Tomáš Souček, Tuan Tran, Surya Parimi, Alexandre Mourachko
- 链接：[arXiv](https://arxiv.org/abs/2610.40613) · [PDF](https://arxiv.org/pdf/2610.40613) · [HF](https://huggingface.co/papers/2610.40613)

We present TextSeal2, a distortion-free watermark for large language models that keeps its signal under speculative decoding: tokens that replace rejected drafts remain watermarked with the same keys, and the acceptance rate is unchanged. It also preserves output diversity and adds no measurable inference latency. Its predecessor, TextSeal, restores diversity in the Gumbel-max scheme by routing each token to one of…

## 74. ShallowDefend: Harnessing Shallow Safety Alignment for Multi-Turn Defender

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reinforcement learning, benchmark, language model, large language
- 作者：Qiyao Ma, Xiaodong Liu, Weiwei Yang, Mingqian Feng, Chengquan Guo, Jialin Song, Carolyn Buractaon, Zhe Zhao, Junshan Zhang, Sandeep Atluri, Christopher White, Jianfeng Gao
- 链接：[arXiv](https://arxiv.org/abs/2610.40627) · [PDF](https://arxiv.org/pdf/2610.40627) · [HF](https://huggingface.co/papers/2610.40627)

Safety alignment has enabled large language models to reliably refuse harmful requests directly, yet the same request distributed across a multi-turn conversation still succeeds far too often. This brittleness has a mechanistic root: Alignment is shallow, with safety behavior concentrated in a model's first few output tokens, and existing defenses inherit the weakness, supervising the surface form of the response…

## 75. Elucidating the Design Space of LM Data Attribution

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, language model, retrieval
- 作者：Steven Yu, Sheng-Yu Wang, Kimia Hamidieh, Antonio Torralba, David Bau
- 链接：[arXiv](https://arxiv.org/abs/2610.40655) · [PDF](https://arxiv.org/pdf/2610.40655) · [HF](https://huggingface.co/papers/2610.40655)

Data attribution methods for Language Models (LMs) are typically evaluated using downstream tasks like fact retrieval. However, existing evaluations vary multiple dataset properties simultaneously, making it impossible to isolate exactly why an attribution algorithm fails. To diagnose these failures, we explore the design space of LLM data attribution, with a primary focus on evaluation. We introduce the Controlled…

## 76. PAPERBENCHX: Can AI Reproduce Science Across Disciplines?

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, benchmark, spec
- 作者：Ruoyu Wu, Zengji Tu, Aolong Sun, Tianyi Ma, Junren Li, Xinbo Xu, Li Fu, Ziyan Zhang, Pinrui Huang, Xiaochen Wang, Chengda Wu, Yutao Zhou, Jianjun Wu, Lin Chang, Baobao Chang, Liang Chen, Kuan Li
- 链接：[arXiv](https://arxiv.org/abs/2610.39744) · [PDF](https://arxiv.org/pdf/2610.39744) · [HF](https://huggingface.co/papers/2610.39744)

Before AI can be trusted to discover new science, it should be able to reproduce what science already knows. Reproduction provides a rigorous checkpoint for an AI scientist: the target claim is known, yet recovering it still requires translating an incomplete scientific description into an executable experiment and producing evidence that can be independently verified. Existing research-reproduction benchmarks…

## 77. Long-Term Agent Memory through Complementary Curation and Consolidation

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, memory, benchmark
- 作者：Abhishek Gupta, Dongge Han, Daniel Madrigal Diaz, Wei-Ning Chen, Mayukh Das, Victor Rühle, Saravan Rajmohan
- 链接：[arXiv](https://arxiv.org/abs/2610.39790) · [PDF](https://arxiv.org/pdf/2610.39790) · [HF](https://huggingface.co/papers/2610.39790)

Long-horizon dialogue agents require effective memory systems to recall facts, events, and relationships from interaction histories. In this work, we propose a hybrid-memory architecture comprising episodic memories and structured relational memories and a consolidation mechanism which preserves efficiency. We conduct an empirical study across two benchmarks: LoCoMo and LongMemEval-S. Our experiments demonstrate…

## 78. InferD: A Honeypot Framework for AI Inference Infrastructure

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, language model, large language
- 作者：Hicham Hammouchi, Gabriele Lenzini
- 链接：[arXiv](https://arxiv.org/abs/2610.39807) · [PDF](https://arxiv.org/pdf/2610.39807) · [HF](https://huggingface.co/papers/2610.39807)

Large language model serving stacks, commercial inference APIs, vector databases, and agent orchestration gateways are now ex- posed on the public internet and indexed by commodity scanners within hours of deployment. The threat characteristics of this sur- face are only beginning to be measured, and the honeypot frame- works that could measure it were designed for conventional net- work services rather than for AI…

## 79. GROME: GROunding Factorized MEmory into Video World Models

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, context window, retrieval
- 作者：Fang Yu, Xiaoxue Wu, Haiyu Zhang, Yangfu Li, Botong Zhao, Yu Qiao, Tianfan Xue, Yue Lu, Xinyuan Chen
- 链接：[arXiv](https://arxiv.org/abs/2610.39812) · [PDF](https://arxiv.org/pdf/2610.39812) · [HF](https://huggingface.co/papers/2610.39812)

Long-horizon consistency is essential for video world models, yet it becomes difficult to maintain once observed content falls outside the context window. Existing memory mechanisms either retrieve history as implicit context, which remains constrained by context capacity and entangles static and dynamic information or consolidate history into explicit global representations, which struggle to model evolving…

## 80. EvoTeam: Multi-Agent Collaboration via Evolving Teams

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, benchmark, spec
- 作者：Qinuo Cao, Xin He, Dianxuan Fu, Lizhi Zhang, Zhaoqing Xing, Jiapu Wang, Xin Wang, Na Zou, Yi Chang, Qinggang Zhang
- 链接：[arXiv](https://arxiv.org/abs/2610.39813) · [PDF](https://arxiv.org/pdf/2610.39813) · [HF](https://huggingface.co/papers/2610.39813)

LLM-based multi-agent systems (MAS) rely on collaboration among specialized agents to solve complex tasks. Existing methods improve MAS by refining the prompts, skills, and execution strategies of individual agents based on task feedback. However, improving individual agents does not necessarily lead to better team collaboration. Recent studies have therefore extended evolution to the collaboration level, using…

## 81. KV Cache Quantization for Diffusion Language Models

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, language model, coding
- 作者：Yan Tai, Yunan Ding, Guangzhao Li, Siqi Luo, Chaoyang Zhang, Guangtao Zhai, Guodong Guo, Xiaohong Liu
- 链接：[arXiv](https://arxiv.org/abs/2610.39853) · [PDF](https://arxiv.org/pdf/2610.39853) · [HF](https://huggingface.co/papers/2610.39853)

KV cache quantization is well studied for autoregressive language models, where cached prefix states are exact under causal attention and quantization is mainly a cache reconstruction problem. Diffusion language models (dLLMs) break this assumption. Fast dLLM inference reuses KV states across denoising steps, but bidirectional token representations can change as masked tokens are revealed, so the reused cache may…

## 82. Spectral Invariant Fusion and Refinement for Domain Generalized Semantic Segmentation

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, coding, spec
- 作者：Yansong Bai, Yunzhi Zhuge, Xinzhuo Yu, Lu Zhang, Jin Zhan, Pingping Zhang, Huchuan Lu
- 链接：[arXiv](https://arxiv.org/abs/2610.39926) · [PDF](https://arxiv.org/pdf/2610.39926) · [HF](https://huggingface.co/papers/2610.39926)

Domain generalized semantic segmentation is challenging because it requires accurate dense prediction on unseen domains without any access to target-domain data during training. Existing methods improve transferability through data diversification, invariant learning, or direct use of foundation models, but they often struggle to simultaneously suppress domain-sensitive interference and preserve fine-grained spatial…

## 83. Observability-Aligned Evidential Masked Pretraining for Reliable VRU Motion Prediction

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, coding
- 作者：Shang Gao, Franz Götz-Hahn, Konrad Doll, Bernhard Sick
- 链接：[arXiv](https://arxiv.org/abs/2610.39958) · [PDF](https://arxiv.org/pdf/2610.39958) · [HF](https://huggingface.co/papers/2610.39958)

Vulnerable road user (VRU) prediction must operate under partial observability and distribution shift, so reliable uncertainty matters alongside accuracy. Masked pretraining is attractive in this setting because it naturally exposes the model to missing content during self-supervision, but existing time-series masked autoencoding methods are typically deterministic and do not constrain how confidence should change…

## 84. Cheap Retrieval and Observation Credit Assignment from One Quantity: The Value of Information

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, reinforcement learning, retrieval
- 作者：Daniel Strauss, Nikolaos Sotirakis, Zhenshan Bing, Alois Knoll
- 链接：[arXiv](https://arxiv.org/abs/2610.40030) · [PDF](https://arxiv.org/pdf/2610.40030) · [HF](https://huggingface.co/papers/2610.40030)

Memory in reinforcement learning raises two problems. Attention finds the relevant item by scoring the whole store, which is costly for robots under latency and energy limits. When a retrieved memory pays off, credit for acquiring it must cross the whole sequence. We argue that both are governed by one quantity, the value of information, and propose to estimate it from archived rollouts with a learned world model.…

## 85. Hybrid AI Patterns: Thirteen Ways to Couple Language Models with Rules, and How to Choose Among Them

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reasoning, language model
- 作者：Siegfried Handschuh, Götz-Henrik Wiegand, Lorena Raichle
- 链接：[arXiv](https://arxiv.org/abs/2610.40036) · [PDF](https://arxiv.org/pdf/2610.40036) · [HF](https://huggingface.co/papers/2610.40036)

Language models handle text well, and rule engines give conclusions with proofs. Systems that combine the two are usually described by example, and the same coupling turns up under different names in agent frameworks, guardrail toolkits and neuro-symbolic research. This document defines thirteen patterns for coupling a language model with an executable rule language, in the catalogue form introduced for…

## 86. UPPAAi: Towards LLM-Assisted Modeling, Verification, Analysis and Synthesis

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：language model, large language, spec
- 作者：Peter Dolog, Kim G. Larsen, Marius Mikučionis, Frederik F. K. Rasmussen
- 链接：[arXiv](https://arxiv.org/abs/2610.40042) · [PDF](https://arxiv.org/pdf/2610.40042) · [HF](https://huggingface.co/papers/2610.40042)

For more than three decades, UPPAAL has supported the modelling and analysis of real-time and cyber-physical systems. Yet building a suitable model, formalising the intended properties, choosing analysis techniques and interpreting counterexamples remain iterative tasks that demand substantial expertise. Large language models (LLMs) can offer plausible explanations and even solutions, but they are not necessarily…

## 87. Upcycling Language Models for Multiple Specialized Domains

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：language model, large language, spec
- 作者：Mingzi Cao, Xi Wang, Nikolaos Aletras
- 链接：[arXiv](https://arxiv.org/abs/2610.40091) · [PDF](https://arxiv.org/pdf/2610.40091) · [HF](https://huggingface.co/papers/2610.40091)

Effective multi-domain adaptation of large language models requires prioritizing relevant domain knowledge while minimizing interference from irrelevant domains. Existing approaches commonly use Low-Rank Adaptation (LoRA) to train a separate adapter for each domain and combine these adapters within one model. However, they either weight adapters equally regardless of the input domain or dynamically weight adapters…

## 88. RepConTUR: A Report-Conditioned Volumetric Multimodal Model for Abdominal Tumor Segmentation

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：language model, spec, planning
- 作者：Seunghwan Lee, Sangjoon Park, Jongmin Lee, Yoon Jo Kim, Wonyoung Cho, Jin Sung Kim, Han Joo Chae
- 链接：[arXiv](https://arxiv.org/abs/2610.40094) · [PDF](https://arxiv.org/pdf/2610.40094) · [HF](https://huggingface.co/papers/2610.40094)

Tumor delineation is required for radiotherapy planning, yet automatic segmentation is limited by errors, predominantly false positives, that distort dose and increase editing time. The radiology report accompanies the scan and localizes disease at the suborgan level, but existing text-promptable models condition on short referring phrases, and most operate in 2D. We present RepConTUR, a single native-3D…

## 89. Escaping Path Mirages in Offline Goal-Conditioned Reinforcement Learning

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reinforcement learning, planning
- 作者：Junhyeon Bae, Jaebak Hwang, Gwanwoo Choi, Minung Kim, Seungyul Han
- 链接：[arXiv](https://arxiv.org/abs/2610.40130) · [PDF](https://arxiv.org/pdf/2610.40130) · [HF](https://huggingface.co/papers/2610.40130)

Offline goal-conditioned reinforcement learning remains challenging in stochastic long-horizon settings, where compounding value estimation errors hinder reliable goal reaching. While prior methods have sought to address this challenge through various approaches, a key challenge remains path mirage, where agents overcommit to spuriously successful trajectories in offline datasets induced by stochasticity, often…

## 90. Bridging Semantics and Structure: A Theoretically Grounded Framework for Link Prediction on TAGs

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, language model
- 作者：Chen Shao, Ruirui Wang, Tobias Kafer, Danai Koutra
- 链接：[arXiv](https://arxiv.org/abs/2610.40192) · [PDF](https://arxiv.org/pdf/2610.40192) · [HF](https://huggingface.co/papers/2610.40192)

Link prediction on text-attributed graphs (TAGs) is a fundamental problem with applications in knowledge discovery, recommendation and beyond. Recent progress has highlighted the promise of combining Graph Neural Networks (GNNs) with Language Models (LMs) in order to leverage the complementary structural and semantic signals. However, due to the distinct inductive biases of GNNs and LMs, the design of an optimal…

## 91. Benchmarking color judgment in multimodal LLMs with CIE-computable ground truth

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, language model, large language
- 作者：Shuwei Yue, Kaida Xiao, Zhihua Wang, Qiao Chen
- 链接：[arXiv](https://arxiv.org/abs/2610.40212) · [PDF](https://arxiv.org/pdf/2610.40212) · [HF](https://huggingface.co/papers/2610.40212)

Multimodal large language models (MLLMs) are now used as zero-shot judges of image quality, but their color judgments are rarely tested with colorimetric ground truth. We present a five-task benchmark based on the CIE colorimetric framework: AWB pair judgment, skin-tone bias direction, CCT estimation, CIE Delta E 2000 pair ordering, and color naming under changing illuminants. We test eight MLLM endpoints, including…

## 92. DYNAS: A Dynamic Network Penetration Testing Framework Using Deep Hierarchical Reinforcement Learning

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reinforcement learning, evaluation, spec
- 作者：Md. Rakibul Hassan, Majedul Islam, Md. Ashraful Alam, Muhammad Iqbal Hossain, Swakkhar Shatabda
- 链接：[arXiv](https://arxiv.org/abs/2610.40214) · [PDF](https://arxiv.org/pdf/2610.40214) · [HF](https://huggingface.co/papers/2610.40214)

As network scale and uncertainty complicate automated penetration testing, reinforcement learning (RL) environments must support controlled evaluation under defensive and non-stationary conditions. We present DYNAS (Dynamic Network Attack Simulator), which combines parameterized large-scale scenario generation with stateful intrusion detection responses, explicit scan false-positive and false-negative noise,…

## 93. Mobilizing the Archive: Bitext Extraction at Scale from Archival Documents for Extremely Low-resource Languages

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：language model, large language, spec
- 作者：Chutong Meng, Alec J. Bateman, Antonios Anastasopoulos
- 链接：[arXiv](https://arxiv.org/abs/2610.40233) · [PDF](https://arxiv.org/pdf/2610.40233) · [HF](https://huggingface.co/papers/2610.40233)

While mining parallel sentences from web pages has proven effective for low-resource machine translation, the majority of the world's languages have little to no web presence. What they do have, though, are resources that are the result of centuries of efforts by linguists, such as grammars, dictionaries, and other documentation materials. We propose extracting translation examples from such linguistic resources,…

## 94. Latent Path Exploration via Potential-Guided Subtrajectory Balance

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, benchmark, language model
- 作者：Xiaoling Zeng, Qi Zhang
- 链接：[arXiv](https://arxiv.org/abs/2610.40283) · [PDF](https://arxiv.org/pdf/2610.40283) · [HF](https://huggingface.co/papers/2610.40283)

Continuous latent reasoning enables language models to perform intermediate computation without generating explicit reasoning traces. Advances in stochastic latent reasoning allow multiple paths to be sampled in continuous space, but stochasticity alone does not ensure effective exploration. A key challenge is guiding stochastic transitions between intermediate latent states toward useful reasoning paths. We…

## 95. DolphinRouting: Cluster-Level Binary Routing for Disaggregated LLM Inference Serving

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, language model, large language
- 作者：Yishuo Yuan, Shaoyu Yang, Chunrong Fang
- 链接：[arXiv](https://arxiv.org/abs/2610.40292) · [PDF](https://arxiv.org/pdf/2610.40292) · [HF](https://huggingface.co/papers/2610.40292)

Prefill-decode (PD) disaggregation isolates the two phases of large language model serving, but request-level path selection must account for prefill work, cache reuse, and decode demand. We present DolphinRouting, which learns this choice from end-to-end SLO feedback under a given P/D resource allocation. Requests are clustered by raw prompt length, cache-adjusted input lengths on both worker pools, and…

## 96. Decision and System One models in rheumatology: accuracy and calibration on specialty-training examination questions and diagnostic case vignettes

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, spec
- 作者：Alfredo Madrid-García, Diego Benavent, Fabian Lechner, Phillip Kremer, Johannes Knitza, Beatriz Merino-Barbancho
- 链接：[arXiv](https://arxiv.org/abs/2610.40318) · [PDF](https://arxiv.org/pdf/2610.40318) · [HF](https://huggingface.co/papers/2610.40318)

Objectives: To evaluate the accuracy and calibration of Decision and System One models on rheumatology examination questions and diagnostic vignettes. Methods: Two benchmarks were analysed: 172 rheumatology questions from Spanish specialty-training examinations (expanded RheumaMIR dataset) in Spanish and English, and 70 English diagnostic vignettes from RheumBench with 5-18 candidate diagnoses, 52 of which included…

## 97. A Unified Hessian-Guided Framework for Post-Training Quantization

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, language model, large language
- 作者：Mads Toftrup, Marco Federici, Boris van Breugel, Paul Whatmough, Markus Nagel
- 链接：[arXiv](https://arxiv.org/abs/2610.40345) · [PDF](https://arxiv.org/pdf/2610.40345) · [HF](https://huggingface.co/papers/2610.40345)

Low-bit quantization enables efficient deployment of large language models by reducing memory footprint and computational cost. Achieving high accuracy at low precision requires selecting quantization ranges, linear transformations, and weight rounding decisions. Existing approaches typically optimize these components independently using local reconstruction objectives, which fail to account for the varying impact…

## 98. HiFOR: Hierarchical Foresight with Action-Guided World Grounding for Vision-Language-Action Model

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, spec, retrieval
- 作者：Rongxing Ding, Hongyu Qu, Kehong Wu, Xudong Wang, Fan Zhang, Xinguang Xiang, Xiangbo Shu
- 链接：[arXiv](https://arxiv.org/abs/2610.40373) · [PDF](https://arxiv.org/pdf/2610.40373) · [HF](https://huggingface.co/papers/2610.40373)

Vision-Language-Action (VLA) models have demonstrated promising capabilities in robotic manipulation by integrating visual perception, language understanding, and action generation. Recent advances have further incorporated future prediction to enhance the understanding of environmental dynamics and task progression. However, existing methods often model short-term dynamics and long-term task objectives separately,…

## 99. Beyond Selected Breakthroughs: Evaluating Language Models on Randomly Sampled Mathematical Conjectures

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, language model, spec
- 作者：Helen Jenne, Davis Brown, Jesse He, Henry Kvinge
- 链接：[arXiv](https://arxiv.org/abs/2610.40382) · [PDF](https://arxiv.org/pdf/2610.40382) · [HF](https://huggingface.co/papers/2610.40382)

The last year has seen a shift in AI-assisted mathematics, with frontier language models producing proofs of and counterexamples to long-standing open conjectures. However, studying only the current set of major breakthroughs provides an incomplete picture of LLM capabilities and the computational resources needed to achieve reported results. To address this, we introduce a new dataset, OpenConjecture, which…

## 100. Glance: The Generator Is Its Own Reranker

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, evaluation, retrieval
- 作者：Adilet Metinov, Chingiz Arziev
- 链接：[arXiv](https://arxiv.org/abs/2610.40454) · [PDF](https://arxiv.org/pdf/2610.40454) · [HF](https://huggingface.co/papers/2610.40454)

Retrieval-augmented generation commonly serves separate models for reranking and answering, duplicating model residency and passage processing. We introduce Glance, which equips the generator with a lightweight decision adapter and pointer head to score candidate passages from a shared prefill. Short relevance probes branch from the cached context, producing one score per passage without separately prefilling each…

## 101. Algebraic World Model: From Exploration to Proofs

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, coding, spec
- 作者：Guancheng Pan, Qixin Tan, Yang Yuan, Andrew Chi-Chih Yao
- 链接：[arXiv](https://arxiv.org/abs/2610.40503) · [PDF](https://arxiv.org/pdf/2610.40503) · [HF](https://huggingface.co/papers/2610.40503)

AI has made remarkable progress in mathematics, solving challenging problems with machine-checkable proofs in Lean, yet typically relying on predefined mathematical definitions and formal specifications. This raises a natural question: can it reason rigorously about an unknown world? We introduce the Algebraic World Model (AWM), a framework that turns interaction with unfamiliar environments into explicit…

## 102. A Low-Rank Space Captures Linear Alignment Between LLM and Human Neural Activity During Naturalistic Language Listening

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：language model, large language, coding
- 作者：Zach Paris, Emily Finn
- 链接：[arXiv](https://arxiv.org/abs/2610.40511) · [PDF](https://arxiv.org/pdf/2610.40511) · [HF](https://huggingface.co/papers/2610.40511)

Large language models (LLMs) are increasingly used as computational models of human language processing, yet it remains unclear which components of their representations drive alignment with neural activity. Here, we use ridge reduced-rank regression to identify the brain-predictive subspace of LLM representations: the representational directions that support linear prediction of neural responses. Across three…

## 103. IndicIPR-QA: A Benchmark for Extractive Question Answering on Indian IPR Laws

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, spec
- 作者：M. Mohaiminul Islam, Muhammad Abulaish
- 链接：[arXiv](https://arxiv.org/abs/2610.40518) · [PDF](https://arxiv.org/pdf/2610.40518) · [HF](https://huggingface.co/papers/2610.40518)

Legal Question Answering (QA) over statutory texts is a challenging task in Natural Language Processing (NLP), especially in low-resource settings with complex legal systems. It requires answers that are precise and grounded in the law. However, to the best of current knowledge, no existing extractive QA benchmark provides exact answer spans from statutory texts across all seven Indian Intellectual Property Rights…

## 104. BURGER: Benchmarking and Understanding Robotic Generalization via Embodied Drawing

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, benchmark, spec
- 作者：Xiangyu Xu, Bangshuai Peng, Ziyi Liu, Mengjie Zhao, Chenhao Lu, Zhengyang Fan, Huazhe Xu, Kaizhe Hu
- 链接：[arXiv](https://arxiv.org/abs/2610.40532) · [PDF](https://arxiv.org/pdf/2610.40532) · [HF](https://huggingface.co/papers/2610.40532)

How effectively can vision-language-action (VLA) models learn diverse language-conditioned behaviors as training data scales? Investigating this question requires large and varied robot datasets, whose collection on physical robots remains costly. We introduce BURGER, a language-conditioned robotic drawing benchmark with a scalable, prompt-driven pipeline for generating continuous drawing trajectories, both in…

## 105. Machine Learning-Based Detection of Mobile Money Scan Messages in Ghana: A Comparative Evaluation of Naive Bayes, Support Vector Machine, and Randon Forest Classifiers

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, evaluation, spec
- 作者：Ibrahim Salifu, Muhaisin Tiyumba Nantogmah
- 链接：[arXiv](https://arxiv.org/abs/2610.40544) · [PDF](https://arxiv.org/pdf/2610.40544) · [HF](https://huggingface.co/papers/2610.40544)

Mobile money (MoMo) is Ghana's preferred retail payment channel, recording GHC518.4 billion in transactions in December 2025 and over 26.7 million active accounts (Graphic Online, 2026). This growth has coincided with increased social-engineering fraud over Short Message Service (SMS) and Unstructured Supplementary Service Data (USSD), where fraudsters impersonate network operators, agents, relatives, or regulators…

## 106. Retrieval as Traversal: Value-Indexed Memory for Stateful Long-Context Agents

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, memory, retrieval
- 作者：Daniel Strauß, Zhenshan Bing, Alois Knoll
- 链接：[arXiv](https://arxiv.org/abs/2610.40545) · [PDF](https://arxiv.org/pdf/2610.40545) · [HF](https://huggingface.co/papers/2610.40545)

Long-context models repeatedly solve closely related retrieval problems. Attention or global retrieval can retain large stores, but each forward pass again searches for what matters. Recurrent compression avoids this search only by deciding earlier what information to preserve. Neither mechanism directly exploits that useful memories at neighbouring retrieval steps may substantially overlap. We propose an…

## 107. Gym-Anything for Robotics: Scaling physical simulations with digital agents

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, benchmark, coding
- 作者：Pranjal Aggarwal, Sean Welleck
- 链接：[arXiv](https://arxiv.org/abs/2610.40565) · [PDF](https://arxiv.org/pdf/2610.40565) · [HF](https://huggingface.co/papers/2610.40565)

Realistic, fast robotics simulations could enable large-scale training of embodied AI models that transfer to the real world. However, despite decades of progress, available simulations cover only a narrow range of real-world tasks and physical phenomena. The core bottleneck is that creating better simulations requires significant expert effort and therefore does not scale. To address this, we introduce Gym-Anything…

## 108. Every Token Needs Its Own Teacher: Multi-teacher Adaptive On-policy Self-distillation

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, language model, large language
- 作者：Yifu Luo, Chuang Ma, Zeyu Chen, Enkelejda Kasneci, Qi Chen, Gjergji Kasneci
- 链接：[arXiv](https://arxiv.org/abs/2610.40574) · [PDF](https://arxiv.org/pdf/2610.40574) · [HF](https://huggingface.co/papers/2610.40574)

On-policy Self-distillation (OPSD) has proven effective for post-training large language models by constructing a teacher conditioned on privileged references. However, existing approaches keep the teacher fixed either throughout training by consistently exposing it to the full reference, or within each response by adaptively varying partial reference exposure only across responses. In this paper, we argue that…

## 109. PIVOT: Progressive Intervention via Online Teacher Correction

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, reinforcement learning, benchmark
- 作者：Zhihao Yang, Boyuan Zheng, Puhui Tan, Yukun Chen, Kuan Zhang, Longze Chen, Jiaming Li, Renke Shan, Lu Wang, Xianpei Han
- 链接：[arXiv](https://arxiv.org/abs/2610.40576) · [PDF](https://arxiv.org/pdf/2610.40576) · [HF](https://huggingface.co/papers/2610.40576)

Reinforcement learning from verifiable rewards (RLVR) is limited by sparse outcome-level feedback on hard reasoning tasks: when all rollouts in a group fail, rewards provide no learning signal. Stronger teachers can provide additional guidance, but this raises a central question: how can such signals be incorporated into RLVR to support successful rollouts while remaining learnable for the student? We distinguish…

## 110. Collaborative AI agents for autonomous experimental research with solid-state quantum spins

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, language model, large language
- 作者：El Mustapha Mansouri, Eikichi Kimura, Masato Koga, Keigo Arai
- 链接：[arXiv](https://arxiv.org/abs/2610.40589) · [PDF](https://arxiv.org/pdf/2610.40589) · [HF](https://huggingface.co/papers/2610.40589)

An autonomous research laboratory could conduct an entire study, from formulating questions to preparing manuscripts. Artificial intelligence (AI) offers one route towards this goal. Recent AI systems take on several research roles, but may draw conclusions that the evidence does not support. Here, we present an autonomous research laboratory in which agents based on large language models assess one another's work…

## 111. When to Assist and What to Suggest: Joint Gating and Memory-Grounded Hint Generation in One Compact Decoder

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, evaluation, retrieval
- 作者：A. J. A. Jubayer Talukder, Mohammad Ariful Haque
- 链接：[arXiv](https://arxiv.org/abs/2610.40611) · [PDF](https://arxiv.org/pdf/2610.40611) · [HF](https://huggingface.co/papers/2610.40611)

Proactive assistants offer short, memory-grounded hints during a conversation, deciding when to assist and what to suggest. Current systems split this between a gate and a larger generator; we evaluate both together on 28,058 decision points. Stage-wise generation scores are oracle-gate ceilings: behind a real gate, end-to-end exact match is 0.2619 against a ceiling of 0.2971, and end-to-end precision is 0.2387,…

## 112. Testimony from Timelines: Evidence-Grounded Significance Testing of Temporal Clinical Hypotheses

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, language model, spec
- 作者：Chengyang He, Wenlong Zhang, Koduvayur Subbalakshmi, Ping Wang
- 链接：[arXiv](https://arxiv.org/abs/2610.40619) · [PDF](https://arxiv.org/pdf/2610.40619) · [HF](https://huggingface.co/papers/2610.40619)

Ask a language model whether sales tend to dip after a product recall, or whether one side effect tends to follow another after a vaccine, and it answers in a fluent sentence that reads like a finding, with no test behind it. Assertions about how events unfold across many cases fill the Web, and each is a temporal hypothesis that only a significance test over the right records can settle. The verifier must specify…

## 113. Rethinking Neural Thickets Without Weight Perturbations

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, language model, spec
- 作者：Nicolas Dufour, Elouan Gardès, Amil Dravid, Patrick Pérez, Loic Landrieu
- 链接：[arXiv](https://arxiv.org/abs/2610.40649) · [PDF](https://arxiv.org/pdf/2610.40649) · [HF](https://huggingface.co/papers/2610.40649)

The Neural Thickets hypothesis posits that pretrained language models lie in dense neighborhoods of task-specific experts in weight space, which random Gaussian perturbations can uncover. We reproduce the reported gains, but show that they do not require this geometric explanation. Perturbing a single decoder block already recovers much of the improvement, while keeping the model entirely frozen and adding a random…

## 114. The Importance of Speech Genre for End-of-Turn Detector Training

- 分数：5.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：coding, spec
- 作者：Rini Sharon, Kadri Hacioglu, Jeena Prakash, Andreas Stolcke
- 链接：[arXiv](https://arxiv.org/abs/2610.39742) · [PDF](https://arxiv.org/pdf/2610.39742) · [HF](https://huggingface.co/papers/2610.39742)

End-of-turn (EoT) detection has been studied mostly through features, models, and modalities, while the speech genre of the training data has drawn far less attention. We isolate this factor. Using one reproducible annotation pipeline, we build a matched pair of corpora, multi-turn human-human conversational and single-turn human-machine, and train the same streaming ConvLSTM EoT detector on each. Across four test…

## 115. Multi-output LSTM soft sensors for industrial anaerobic co-digestion using LSTM-beta-VAE generative data augmentation

- 分数：5.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, evaluation
- 作者：Rohit Murali, Benaissa Dekhici, Tao Chen, Dongda Zhang, Michael Short
- 链接：[arXiv](https://arxiv.org/abs/2610.39768) · [PDF](https://arxiv.org/pdf/2610.39768) · [HF](https://huggingface.co/papers/2610.39768)

Anaerobic digestion (AD) requires close monitoring of key process variables, including pH, the ratio of volatile organic acids to alkaline buffer capacity and biogas production, to maintain biological stability and prevent process failure. While mechanistic frameworks such as the Anaerobic Digestion Model No. 1 are highly parameterised, computationally expensive, and difficult to calibrate for real-time…

## 116. The Role of Self-Concept In Language Models

- 分数：5.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：language model, spec
- 作者：Yijie Hao, Joyce C. Ho
- 链接：[arXiv](https://arxiv.org/abs/2610.39795) · [PDF](https://arxiv.org/pdf/2610.39795) · [HF](https://huggingface.co/papers/2610.39795)

When a language model says "I," does it refer to its parameter weights, its currently running process, its stable preferences, its model lineage, or the goals it pursues? Different choices can assign opposite meanings to the same event: deleting a checkpoint may be destruction, continuation, or no loss at all, depending on the referent "I". We install five such self-conceptions into five open-weight base models via…

## 117. AI at a Turning Point: From ChatGPT through Neural Networks to Neuromorphic AI

- 分数：5.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：coding, spec
- 作者：Volker Kempe
- 链接：[arXiv](https://arxiv.org/abs/2610.39796) · [PDF](https://arxiv.org/pdf/2610.39796) · [HF](https://huggingface.co/papers/2610.39796)

The tension between the established technologies of connectionist AI and their neuromorphic challengers is attracting growing attention, above all because of the enormous energy demand of the former and the low power consumption of the latter. Developing and running large AI models consumes gigawatt- to terawatt-hours of energy, while the human brain operates on a continuous 20 watts. Spiking neural networks (SNNs)…

## 118. Surprise Alone Learns Lies: Evidence-Gated Continual Learning for LLMs from Streaming Claims

- 分数：5.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：language model, large language
- 作者：Abdelkader Metales, Miriam Grabenheinrich
- 链接：[arXiv](https://arxiv.org/abs/2610.39840) · [PDF](https://arxiv.org/pdf/2610.39840) · [HF](https://huggingface.co/papers/2610.39840)

Continual learning methods for large language models increasingly decide what to learn by surprise, keeping the inputs the model finds least predictable. This rule is unsafe when the stream contains lies. A planted falsehood about something the model knows has low probability under the model's belief, so it is highly surprising by construction, and a surprise-driven learner absorbs nearly every such lie, at a rate…

## 119. KARMA: Training-Free Knowledge-Atomic Harness Evolution for Industrial Advertising Agents

- 分数：5.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, spec
- 作者：Xinhua Miao, Yuanzhen Rong, Weiru Zhang, Xiaoyi Zeng
- 链接：[arXiv](https://arxiv.org/abs/2610.39884) · [PDF](https://arxiv.org/pdf/2610.39884) · [HF](https://huggingface.co/papers/2610.39884)

Industrial advertising agents must continually adapt their decision knowledge to changing product offerings, traffic patterns, and operating policies. We present KARMA (Knowledge-Atomic, Regression-Gated Modular Adaptation), a training-free framework that evolves six typed knowledge modules while keeping model weights and executable harness code frozen. During our evolution, a deterministic Trace Verifier maps…

## 120. Prompts and probabilities in the linguistic assessment of language models: Evidence from semantic focus-sensitivity

- 分数：5.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：language model, spec
- 作者：Robert Pasternak
- 链接：[arXiv](https://arxiv.org/abs/2610.39923) · [PDF](https://arxiv.org/pdf/2610.39923) · [HF](https://huggingface.co/papers/2610.39923)

As language models (LMs) have improved, an increasingly common means of evaluating their linguistic competence is through explicit prompting (e.g., "Which sentence is more acceptable?"). Prior work indicates that such prompting underperforms compared to standard token-probability-based methods in smaller models, but improves in larger models. We test this in a new domain: semantic focus-sensitivity, responsible for…
