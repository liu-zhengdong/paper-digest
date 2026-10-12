# 每日 AI 论文

生成时间：2026-10-12 05:59 UTC  ·  共 28 篇（已按 arXiv ID 去重）

来源：Hugging Face Daily Papers + arXiv（cs.AI / cs.LG / cs.CL / cs.CV）。
排序：HF 上榜、点赞、多源命中、兴趣词。兴趣词可在 `config.json` 改。

## 1. ProgramGym: Scaling Training Environments for Long-Horizon Program Reproduction Agents

- 分数：29.0  ·  HF 赞：30  ·  来源：huggingface
- 兴趣命中：agent, coding, spec
- 作者：Chengyi Yang, Renxu Bao, Jue Hou, Zongpei Teng, Ziheng Wang, Yujie Lin, Chengsong Huang, Junnan Zhu, Delai Qiu, Yining Wang, Shengping Liu, Fei Long, Jinsong Su
- 链接：[arXiv](https://arxiv.org/abs/2610.13395) · [PDF](https://arxiv.org/pdf/2610.13395) · [HF](https://huggingface.co/papers/2610.13395)

Coding agents are increasingly used to build programs from scratch as software engineers do rather than to resolve issues within a repository or to generate a repository from a given requirements document. However, scalable verifiable training environments that force agents to discover what is required and to decide how the system should be designed remain scarce. Moreover, existing agent workflows also cannot…

## 2. VisionWeave: Weaving Elastic Visual Representations as a Native Capability of MLLMs

- 分数：27.5  ·  HF 赞：23  ·  来源：huggingface
- 兴趣命中：evaluation, benchmark, language model, large language, coding
- 作者：Yuan Feng, Qize Yang, Ruizhe Chen, Sibo Song, Haolin He, Muzhi Zhu, Zihan Liu, Yunfei Chu, Xize Cheng, Yuxuan Wang, Jin Xu, Xike Xie
- 链接：[arXiv](https://arxiv.org/abs/2610.07987) · [PDF](https://arxiv.org/pdf/2610.07987) · [HF](https://huggingface.co/papers/2610.07987)

Multimodal large language models have become the dominant paradigm for visual understanding, but incur substantial costs by encoding inputs into dense, fixed-size patch tokens. However, visual information is unevenly distributed: some regions require fine-grained detail, while others admit compact representations. Downsampling sacrifices this detail, while existing token pruning and adaptive approaches remain…

## 3. SoloQ: Calibration-Free Quantization for Diffusion Language Models

- 分数：26.0  ·  HF 赞：20  ·  来源：huggingface
- 兴趣命中：memory, reasoning, benchmark, language model, large language
- 作者：Donghyun Lee, Arkapravo Ghosh, Varun Manjunath, Bumjoon Kyle Rhee, Hyunho Kook, Shiting Xiao, Youngeun Kim, Priyadarshini Panda
- 链接：[arXiv](https://arxiv.org/abs/2610.07121) · [PDF](https://arxiv.org/pdf/2610.07121) · [HF](https://huggingface.co/papers/2610.07121)

Diffusion large language models dLLMs) have emerged as a promising alternative to autoregressive language models through bidirectional diffusion-based token generation. However, their growing model sizes and high inference costs make efficient deployment challenging: full-sequence denoising repeatedly invokes compute-intensive forward passes, while block-diffusion models additionally introduce a memory-intensive…

## 4. EmbodiedCLBench: Evaluating Continual Learning for Self-Evolving Embodied Agents

- 分数：24.5  ·  HF 赞：21  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark
- 作者：Jie Huang, Yanan Chen, Ruixun Liu, Kaichen He, Xinyi He, Rui Huang, Zilong Zheng, Zhenliang Zhang, Yiwu Zhong
- 链接：[arXiv](https://arxiv.org/abs/2610.13021) · [PDF](https://arxiv.org/pdf/2610.13021) · [HF](https://huggingface.co/papers/2610.13021)

Continual learning requires models to accumulate past experience and transfer it to new tasks. Despite substantial research on continual learning, existing work remains largely confined to non-embodied settings, without extending to embodied environments. To address this gap, we introduce EmbodiedCLBench, the first benchmark in embodied simulation for evaluating the continual learning capability of self-evolving…

## 5. Here the World in Stereo: Learning Dynamic Spatial Correspondence for Immersive Joint Video-Audio Generation

- 分数：21.0  ·  HF 赞：22  ·  来源：huggingface
- 兴趣命中：evaluation
- 作者：Hanmo Chen, Chengcheng Liu, Tianxiao Chen, Zheyu Zhang, Siming Zheng, Jinwei Chen, Xu Yang, Cheng Deng, Bo Li, Peng-tao Jiang
- 链接：[arXiv](https://arxiv.org/abs/2609.38748) · [PDF](https://arxiv.org/pdf/2609.38748) · [HF](https://huggingface.co/papers/2609.38748)

Recent joint video-audio generation models have achieved strong semantic correspondence and temporal synchronization. However, applications such as AR/VR and interactive gaming further require stereo audio to provide an immersive sense, which remains largely overlooked. Effective stereo audio requires the perceived sound location to evolve consistently with the motion of its corresponding visual source. We refer to…

## 6. Continually Post-training Small Models via Synthetic Self-distillation

- 分数：19.5  ·  HF 赞：15  ·  来源：huggingface
- 兴趣命中：evaluation, benchmark
- 作者：Woosung Koh, Hyunsoo Lee, Kyungjae Lee, Haeju Park, Dahyun Lee, Dasol Hwang, Moontae Lee
- 链接：[arXiv](https://arxiv.org/abs/2610.13113) · [PDF](https://arxiv.org/pdf/2610.13113) · [HF](https://huggingface.co/papers/2610.13113)

Continual post-training faces a dual challenge of acquisition and retention: models must learn new capabilities while preserving prior knowledge. While Self-Distillation Fine-Tuning (SDFT) mitigates this using self-supervision with in-context demonstrations, it relies on strong in-context learning and instruction-following abilities. Consequently, SDFT fails on smaller models critical for low-latency, on-device use.…

## 7. Inducing Process Supervision from Outcome-Only Reinforcement Learning

- 分数：19.0  ·  HF 赞：6  ·  来源：huggingface
- 兴趣命中：agent, reasoning, reinforcement learning, benchmark
- 作者：Shengda Fan, Xin Cong, Zhong Zhang, Haotian Chen, Yankai Lin
- 链接：[arXiv](https://arxiv.org/abs/2609.36641) · [PDF](https://arxiv.org/pdf/2609.36641) · [HF](https://huggingface.co/papers/2609.36641)

Process reward models (PRMs) have become a key component for LLMs, as their step-level feedback supports both post-training and test-time reasoning. However, training strong PRMs remains costly: human step annotation is difficult to scale, while Monte Carlo estimation is computationally expensive and can drift from the intrinsic correctness of steps. To get effective PRMs at low cost, we introduce TIPS…

## 8. Towards Physically Grounded Articulated 3D Assets: A Multi-Agent Pipeline and Benchmark

- 分数：19.0  ·  HF 赞：6  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark, spec
- 作者：Xudong Cai, Ruijie Zhu, Haoliang Shang, Ruining Li, Marc Pollefeys, Shangzhe Wu, Andrea Vedaldi, Chuanxia Zheng
- 链接：[arXiv](https://arxiv.org/abs/2610.13947) · [PDF](https://arxiv.org/pdf/2610.13947) · [HF](https://huggingface.co/papers/2610.13947)

In this paper, we study physically grounded articulated 3D asset generation---moving the goal from reproducing how objects look to capturing how they move and function. Inspired by the literature on procedural and agentic generation, we present Artisan, a system that extends the latest method Articraft by introducing a multi-agent pipeline with physical simulation feedback, enabling comprehensive attributes beyond…

## 9. RSI-Anything: Unlocking Recursive Self-Improvement with World Models

- 分数：18.5  ·  HF 赞：13  ·  来源：huggingface
- 兴趣命中：evaluation, planning
- 作者：Taoyong Cui, Pinxian Zeng, Wanghan Xu, Hao Xiao, Shuhan Xue, Qiang Gao, Wanli Ouyang, Pheng Ann Heng, Zhenfei Yin, Yingcheng Wu, Ling Yang
- 链接：[arXiv](https://arxiv.org/abs/2610.13912) · [PDF](https://arxiv.org/pdf/2610.13912) · [HF](https://huggingface.co/papers/2610.13912)

Recursive self-improvement (RSI) aims to transform interaction experience into persistent improvements, yet external feedback is costly and world-model predictions may become unreliable as policies evolve. We introduce RSI-Anything, a domain-general framework built on JEPA-Anything that uses predictive world models to guide action and learning-data selection. Observed feedback drives policy or workflow improvement…

## 10. DiffusionART: Efficient, Stable and Scalable Reinforcement of Diffusion Models

- 分数：18.0  ·  HF 赞：12  ·  来源：huggingface
- 兴趣命中：reinforcement learning, spec
- 作者：Zhenglin Wan, Jiayu Chen, Zhengfeiyang Zhang, Pengfei Zhou, Wangbo Zhao, Fangyuan Kong, Pengfei Wan, Kun Gai, Yang You
- 链接：[arXiv](https://arxiv.org/abs/2610.12572) · [PDF](https://arxiv.org/pdf/2610.12572) · [HF](https://huggingface.co/papers/2610.12572)

Online reinforcement learning (RL) fine-tunes diffusion models with black-box rewards, but reverse-process methods such as Flow-GRPO are limited in efficiency by poor credit assignment, while forward-process methods such as DiffusionNFT are efficient yet unstable without carefully tuned exponential-moving-average (EMA) off-policy training. We show that NFT-style objectives contain a hidden forward--reverse…

## 11. SWE-Duel: Towards a Self-Scaling Arena for Coding Agents

- 分数：17.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark, coding
- 作者：Wei Minn, Zhensu Sun, Lwin Khin Shar, David Lo
- 链接：[arXiv](https://arxiv.org/abs/2610.12569) · [PDF](https://arxiv.org/pdf/2610.12569) · [HF](https://huggingface.co/papers/2610.12569)

Static coding benchmarks are fixed at release. Over time their tasks leak into training data, and stronger agents eventually saturate them. We argue that a benchmark should instead aim to be self-scaling: its tasks and oracles are created at evaluation time, so no content exists in advance to leak, and its difficulty is set by the participating agents rather than fixed at release. We introduce SWE-Duel, an arena in…

## 12. Recurrent Harness for Agentic Continual Learning

- 分数：17.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：agent, memory, benchmark, language model, spec
- 作者：Yuxin Xiao, Zhiyun Lu, Jianyu Wang, Yangtian Zhang, Yang Song, Qifan Wang, Bailin Wang
- 链接：[arXiv](https://arxiv.org/abs/2610.12668) · [PDF](https://arxiv.org/pdf/2610.12668) · [HF](https://huggingface.co/papers/2610.12668)

Language model agents increasingly operate over long interaction streams, requiring online adaptation to distribution shifts through continual learning. However, existing agent harnesses typically either evolve their states only through forward information flow or rely on additional replay or validation data for harness optimization. To address this, we propose ReHarness, a recurrent harness framework for agentic…

## 13. Video-RSI: Recursive Self-Improvement of Video Understanding Agents via Harness Evolution

- 分数：16.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark, language model
- 作者：Bingjun Luo, Jialin Guo, Siqi Li
- 链接：[arXiv](https://arxiv.org/abs/2609.37950) · [PDF](https://arxiv.org/pdf/2609.37950) · [HF](https://huggingface.co/papers/2609.37950)

Video understanding agents acquire evidence through an executable harness that controls what they observe and how they use those observations. However, execution traces contain only the evidence acquired by the current harness, leaving competing explanations for failure unresolved and limiting the basis for self-improvement. We introduce Video-RSI, a framework for recursive self-improvement in which a video…

## 14. From Given to Gathered Evidence: Agentic Learning for Longitudinal Medical Reasoning

- 分数：16.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：agent, tool-use, reasoning, reinforcement learning, evaluation, benchmark, spec
- 作者：Minye Shao, Chaohui Yu, Yixuan Wu, Fan Wang, Ling Shao, Yang Long
- 链接：[arXiv](https://arxiv.org/abs/2609.39566) · [PDF](https://arxiv.org/pdf/2609.39566) · [HF](https://huggingface.co/papers/2609.39566)

Foundation models can serve as clinical agents through tool-use harnesses. However, conventional medical benchmarks assess reasoning over preselected evidence rather than the ability to seek it across clinical records and longitudinal imaging. We propose CASE: a series of role-specific Clinical Agents for Seeking Evidence, together with a tool-use harness and an agentic post-training framework for compact…

## 15. Stateless Language Agents: Scaling Long-Horizon Automated Research

- 分数：16.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark, spec
- 作者：Qizheng Zhang, Changxiu Ji, Isaac Sun, Yuetai Li, Shubhangi Upasani, Sherry Ruan, Boyuan Ma, Fenglu Hong, Vamsidhar Kamanuru, Yoonho Lee, Yuzhen Mao, Genghan Zhang, Rulin Shao, Qiuyang Mang, Andy Dimnaku, Changran Hu, Radha Poovendran, Kunle Olukotun
- 链接：[arXiv](https://arxiv.org/abs/2610.07625) · [PDF](https://arxiv.org/pdf/2610.07625) · [HF](https://huggingface.co/papers/2610.07625)

Automated research systems increasingly run LLM agents over long horizons, but more inference does not by itself produce more progress: agents replay growing histories, duplicate one another's work, or stop experimenting while token consumption continues. Yet most evaluations use short budgets or benchmarks that saturate early, leaving these failure modes untested. We trace these failures to two choices: where…

## 16. Surfing the Activation Wave: Analyzing the Information and Geometry of LLM Hidden States for Speculative Decoding

- 分数：16.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：evaluation, language model, large language, coding, spec
- 作者：Raghavv Goel, Sudhanshu Agrawal, Mukul Gagrani, Risheek Garrepalli, Mingu Lee
- 链接：[arXiv](https://arxiv.org/abs/2610.12939) · [PDF](https://arxiv.org/pdf/2610.12939) · [HF](https://huggingface.co/papers/2610.12939)

Decoder hidden states from different layers of large language models (LLMs) often encode complementary information. However, existing speculative decoding methods typically rely on a small set of target-model layers chosen using fixed, position-based heuristics. Selecting an optimal subset of layers is inherently a combinatorial problem, making exhaustive evaluation infeasible even for moderately deep models. In…

## 17. SepGen: Multi-Stem Audio-Video Separation and Generation in a Single Model

- 分数：16.0  ·  HF 赞：12  ·  来源：huggingface
- 兴趣命中：spec
- 作者：Aviad Dahan, Rajaei Khatib, Yonatan Bitton, Idan Szpektor, Lior Wolf, Raja Giryes
- 链接：[arXiv](https://arxiv.org/abs/2610.11361) · [PDF](https://arxiv.org/pdf/2610.11361) · [HF](https://huggingface.co/papers/2610.11361)

A 4D audio-visual scene comprises a video, the dynamic geometry it depicts, and the sound sources that populate it, each with its own position and trajectory. Rendering such a scene from a novel viewpoint requires that every source be available as an individual waveform, so that it can be localized in the scene and propagated to the observer before the signals are mixed. Joint audio-video generators can synthesize…

## 18. PolyOCR-Venus: Unified OCR Foundation Models for Text-Centric Visual Intelligence

- 分数：16.0  ·  HF 赞：8  ·  来源：huggingface
- 兴趣命中：reasoning, benchmark
- 作者：GuangJian Team, Kaili Huang, Yongshuo Zhang, Bingtao Fu, Changjiang Jiang, Chenfan Qu, Chenfeng Zhang, Fangming Cui, Gaoyang Zhang, Jiangwei Xie, Jianshu Li, Jing Huang, Jingwen Bai, Mingqi Fang, Tao Fang, Weihong Zhang, Wenbo Du, Xiongfei Bai, Xuekang Zhu, Yinan Xia, Zhenming Wang, Jian Liu, Jingjing Liu, Xiang Qi, Weiqiang Wang
- 链接：[arXiv](https://arxiv.org/abs/2609.37712) · [PDF](https://arxiv.org/pdf/2609.37712) · [HF](https://huggingface.co/papers/2609.37712)

Optical Character Recognition (OCR) is evolving from plain-text transcription toward general visual intelligence, requiring models to recognize, localize, and reason over textual information in complex visual environments. However, existing OCR systems often excel at only some tasks and struggle to balance recognition, parsing, and reasoning across scenarios. In this report, we present PolyOCR, a family of unified…

## 19. SoftwareGym: Scaling Computer-Use Agent Training with Diverse Synthesized Software Environments

- 分数：16.0  ·  HF 赞：0  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark, spec
- 作者：Tian Jin, Wenhao Wang, Jing Kang, Haoting Shi, Rui Ye, Yijun Lu, Siheng Chen
- 链接：[arXiv](https://arxiv.org/abs/2610.12611) · [PDF](https://arxiv.org/pdf/2610.12611) · [HF](https://huggingface.co/papers/2610.12611)

Computer-use agents (CUAs) are rapidly improving, yet synthesizing diverse and reliable software environments at scale remains challenging. Native application environments require substantial construction and integration effort, which limits application coverage and increases the risk of application-specific overfitting. Browser-hosted environments provide limited interaction depth and workflow complexity. These…

## 20. GraphDecisionBench: Benchmarking System One Models on Graph Tasks

- 分数：15.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：benchmark, language model, large language
- 作者：Xianliang Yang, Yapu Zhang, Li Zhao
- 链接：[arXiv](https://arxiv.org/abs/2610.06354) · [PDF](https://arxiv.org/pdf/2610.06354) · [HF](https://huggingface.co/papers/2610.06354)

Large language models (LLMs) are increasingly explored for graph understanding and decision-making, while System One models such as Jev select directly from supplied options. However, the capabilities of System One models on graph-related tasks remain unclear. We introduce GraphDecide, a model-independent benchmark that combines structural task profiles, matched graph-text input contrasts and heuristic-proposal…

## 21. Reflex: Visually Grounded Reactive Humanoid Control

- 分数：14.5  ·  HF 赞：9  ·  来源：huggingface
- 兴趣命中：reinforcement learning
- 作者：Taoyang Jia, Weikai Huang, Linxin Song, Jared Darlington, Jieyu Zhao, Yue Wang, Jiafei Duan, Zhongzheng Ren, Ranjay Krishna
- 链接：[arXiv](https://arxiv.org/abs/2610.12772) · [PDF](https://arxiv.org/pdf/2610.12772) · [HF](https://huggingface.co/papers/2610.12772)

Humans effortlessly react to the world; they adeptly return a tennis shot, catch a falling cup, step aside from a passing cart, or pass a box tossed during truck unloading. These everyday actions require anticipating a moving target and reflexively responding with the whole body within about a second. Such visual reactive whole-body control remains challenging for humanoids, which must (1) coordinate whole-body…

## 22. Learning Representations to Guide Pixel Diffusion Transformers

- 分数：14.5  ·  HF 赞：9  ·  来源：huggingface
- 兴趣命中：spec
- 作者：Zihao Pan, Mengting Chen, Cheng Shi, Taihang Hu, Zhengrong Yue, Zikang Wang, Yuan Wang, Wei Li, Sibei Yang
- 链接：[arXiv](https://arxiv.org/abs/2610.12978) · [PDF](https://arxiv.org/pdf/2610.12978) · [HF](https://huggingface.co/papers/2610.12978)

Visual representations are largely developed for understanding, yet what makes them useful for generation remains unclear. We study this question in pixel diffusion transformers and uncover two key insights. First, better representation quality does not necessarily translate into greater generative utility, as externally aligned semantics can be progressively lost during pixel synthesis. Second, architectural…

## 23. Judging in Latent Space: Efficient Generative Reward Modeling via Semantics-Preserving Compression

- 分数：14.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：reasoning, evaluation, benchmark
- 作者：Mingqing Yuan, Xiaobo Liang, Junwei Yang, Ziwei Chen, Zeren Zhang, Hejin Wang, Yubin Wang, Juntao Li
- 链接：[arXiv](https://arxiv.org/abs/2610.09788) · [PDF](https://arxiv.org/pdf/2610.09788) · [HF](https://huggingface.co/papers/2610.09788)

Reward modeling often requires jointly representing and reasoning over multiple evaluation criteria, yet verbalizing this process token by token can incur substantial inference cost. Recent work on latent reasoning suggests that continuous states may support this computation more compactly. We introduce LatentGRM, a latent evaluation framework built on semantic chunking, compression, and reconstruction. By using the…

## 24. AMLworld-Compact: Importance-Weighted Downsampling for Cost-Effective LLM Evaluation and Error Diagnosis

- 分数：14.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：evaluation, language model, large language
- 作者：Natapong Nitarach, Phume Ngampornsukswadi, Pittawat Taveekitworachai, Surapon Nonesung, Warit Sirichotedumrong, Kunat Pipatanakul
- 链接：[arXiv](https://arxiv.org/abs/2610.13627) · [PDF](https://arxiv.org/pdf/2610.13627) · [HF](https://huggingface.co/papers/2610.13627)

Evaluating large language models (LLMs) on AMLworld's smallest test splits is costly because each of over a million targets requires a separate graph prompt. Sampling reduces this cost, but small balanced subsets change unweighted precision and F1. We introduce AMLworld-Compact, an evaluation set that retains every illicit test transaction and samples benign transactions from supervised-score strata. Its HT-Coreset…

## 25. Rethinking Relative Policy Differences Transfer of On-Policy Distillation

- 分数：13.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：reinforcement learning, spec
- 作者：Rong Wu, Daocheng Fu, Yu Yang, Xuemeng Yang, Siqi Li, Shu Zou, Yao Zhu, Botian Shi, Bo Zhang, Cong Zhang, Pinlong Cai, Jianbiao Mei
- 链接：[arXiv](https://arxiv.org/abs/2610.13205) · [PDF](https://arxiv.org/pdf/2610.13205) · [HF](https://huggingface.co/papers/2610.13205)

On-policy distillation (OPD) trains a target policy on its own rollouts using token-level supervision from a stronger teacher, but typically relies on the teacher being substantially more capable than the target. Recent work relaxes this requirement by transferring the relative policy difference between an expert and a reference policy rather than the expert's absolute distribution. Yet it remains unclear which…

## 26. InstantFusion: A Shared Latent Interface for Heterogeneous Image Generators

- 分数：12.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：spec
- 作者：Xuanlang Dai, Jiazi Bu, Yujie Zhou, Yuhong Liu, Beichen Zhang, Penghui Yang, Ziyu Liu, Yuhang Zang
- 链接：[arXiv](https://arxiv.org/abs/2610.13944) · [PDF](https://arxiv.org/pdf/2610.13944) · [HF](https://huggingface.co/papers/2610.13944)

Diffusion/flow models have emerged as the de facto paradigms for image generation, giving rise to a diverse family of modern generators with increasingly heterogeneous architectures and representations. Despite their remarkable generation capabilities, the cross-model alignment of latent representations and the consistency of their underlying denoising dynamics remain underexplored. In this work, we uncover an…

## 27. MixTok: Adaptive Visual Tokenization with Global 1D Tokens and Sparse 2D Refinement

- 分数：10.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：spec
- 作者：Chenge Li, Yefei He, Xinyu Liu, Feng Chen, Hong Zhou, Bohan Zhuang
- 链接：[arXiv](https://arxiv.org/abs/2610.13181) · [PDF](https://arxiv.org/pdf/2610.13181) · [HF](https://huggingface.co/papers/2610.13181)

Efficient visual tokenization requires balancing representation compactness with the preservation of fine-grained image content. Conventional grid-based tokenizers allocate tokens uniformly across spatial locations despite non-uniform visual complexity, whereas compact 1D tokenizers aggregate global information but can struggle to preserve local details. We introduce MixTok, a hybrid visual tokenizer that combines a…

## 28. The value of information and the emergence of communication in evolved e-puck robots

- 分数：10.0  ·  HF 赞：0  ·  来源：huggingface
- 兴趣命中：agent
- 作者：Fernando Montes-Gonzalez
- 链接：[arXiv](https://arxiv.org/abs/2610.13118) · [PDF](https://arxiv.org/pdf/2610.13118) · [HF](https://huggingface.co/papers/2610.13118)

We study when communication emerges between autonomous agents and what role an innate action selection architecture plays. Two e-puck robots, reconstructed in PyBullet from their Webots model and validated against it, must find a feeding zone that can only be detected when a robot passes over it. Each robot can emit a one-bit signal whose direction is detected by the receiver. Control is provided by a GRU recurrent…
