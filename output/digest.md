# 每日 AI 论文

生成时间：2026-10-07 06:01 UTC  ·  共 120 篇（已按 arXiv ID 去重）

来源：Hugging Face Daily Papers + arXiv（cs.AI / cs.LG / cs.CL / cs.CV）。
排序：HF 上榜、点赞、多源命中、兴趣词。兴趣词可在 `config.json` 改。

## 1. ALoDLM: Adaptively Looped Diffusion Language Models

- 分数：34.0  ·  HF 赞：60  ·  来源：huggingface
- 兴趣命中：benchmark, language model, coding
- 作者：Liancheng Fang, Zhuowei Li, Youngeun Kim, Tianchen Zhao, Rajat Koner, Jiaye Wu, Linghan Xu, Xuanbai Chen, Xiang Xu, Zheng Zhang, Jakub Zablocki, Nishant Sankaran, Yifan Xing
- 链接：[arXiv](https://arxiv.org/abs/2610.04198) · [PDF](https://arxiv.org/pdf/2610.04198) · [HF](https://huggingface.co/papers/2610.04198)

Diffusion language models (DLMs) enable fast generation by predicting multiple tokens in parallel, but their practical adoption remains limited by a persistent quality gap relative to comparably sized autoregressive (AR) models. We attribute this gap to a computation-difficulty mismatch: within a partially observed sequence, some unknown tokens are easy to predict, while others require substantially more…

## 2. Memadapter: Counterfactual Adaptation Against Memory-induced Sycophancy

- 分数：32.5  ·  HF 赞：33  ·  来源：huggingface
- 兴趣命中：agent, memory, reasoning, benchmark, spec
- 作者：Ruqing Ning, Haibo Meng, Zhishang Xiang, Zerui Chen, Jinsong Su, Xin Wang, Qinggang Zhang
- 链接：[arXiv](https://arxiv.org/abs/2610.05162) · [PDF](https://arxiv.org/pdf/2610.05162) · [HF](https://huggingface.co/papers/2610.05162)

Long-term memory enables LLM-based agents to retain and reuse information across tasks and sessions, supporting personalization and long-horizon interactions. However, persistent memories can also induce sycophancy, causing agents to over-align with users' historical beliefs even when they are inaccurate, outdated, or inconsistent with objective evidence. Existing mitigation methods assume that memory-induced…

## 3. LMBuild: Evaluating LLM Agents for Generating Buildable and Functional Structures

- 分数：31.5  ·  HF 赞：31  ·  来源：huggingface
- 兴趣命中：agent, reasoning, evaluation, benchmark, spec, retrieval
- 作者：Jiateng Liu, Rushi Wang, Cheng Qian, Xuejun Zhang, Sun Li, Jiayu Liu, Yifan Shen, Xu Cao, Jiarui Yao, Bingxuan Li, Ruhi Sarikaya, Heng Ji
- 链接：[arXiv](https://arxiv.org/abs/2610.04292) · [PDF](https://arxiv.org/pdf/2610.04292) · [HF](https://huggingface.co/papers/2610.04292)

LLM-based agents are increasingly capable of generating complex 3D structures, with the potential to reshape how objects are designed and realized in the physical world. Yet, producing elegant geometry is fundamentally different from producing objects that can be built and perform their intended functions. Existing evaluations largely focus on geometric quality while overlooking physical realizability. We introduce…

## 4. Kandinsky 6.0 Video: Foundation Models for Synchronized Video and Audio Generation

- 分数：30.0  ·  HF 赞：117  ·  来源：huggingface
- 兴趣命中：evaluation
- 作者：Team Kandinsky, Julia Agafonova, Bulat Akhmatov, Mikhail Aksyutin, Grigorii Alekseenko, Anastasia Aliaskina, Olga Androsova, Vladimir Arkhipkin, Anna Averchenkova, Alexander Belykh, Serafima Bocharova, Sofiya Bogakovskaya, Anton Bukashkin, Mark Bulygin, Kirill Buzygin, Irina Cheremnykh, Kirill Chernyshev, Mikhail Chernyshov, Vladimir Chernyy, David Chikovani, Georgy Daniltsev, Denis Dimitrov, Anna Dmitrienko, Vladimir Dokholyan, Sergey Emelyanov, Dmitry Ermilov, Georgii Fedorov, Polina Gavrilova, Nikolai Gerasimenko, Aleksandr Gordeev, Andrey Inozemtsev, Andrei Ivaniuta, Alexander Ivanov, Mikhail Karaev, Anastasiia Kargapoltseva, Ivan Kirillov, Nikita Kiselev, Valeria Kobenko, Yury Kolabushin, Denis Koposov, Anatoly Korobov, Vladimir Korviakov, Kirill Kozlov, Denis Krzhivokolskiy, Konstantin Kuklev, Alexander Kunitsyn, Sergey Kuzin, Vladislav Lakhtionov, Alexey Letunovskiy, Maxim Litvinov, Alexander Lyulkov, Georgy Makarov, Kirill Malakhov, Egor Malykh, Mikhail Mamaev, Dmitrii Mikhailov, Polina Mikhailova, Ivan Mikheev, Elizaveta Muromtseva, Nikolai Nazarkin, Tatiana Nikulina, Lev Novitskiy, Stanislav Onuchin, Nikita Osterov, Denis Parkhomenko, Anatoliy Parpara, Vladimir Polovnikov, Konstantin Reznikov, Azat Saginbaev, Nikita Samsonov, Alexander Sentsov, Nikita Shaimov, Artem Sherstyuk, Andrey Shutkin, Egor Silvestrov, Bulat Suleimanov, Matvey Suprunov, Sergey Taranov, Irina Tolstykh, Tatiana Trofimuk, Ilya Trushkin, Aleksandra Tsybina, Olga Varlashina, Viacheslav Vasilev, Ilya Vasiliev, Eugeny Vilisov, Sergey Yakubson, Konstantin Zakharov
- 链接：[arXiv](https://arxiv.org/abs/2610.05608) · [PDF](https://arxiv.org/pdf/2610.05608) · [HF](https://huggingface.co/papers/2610.05608)

We present Kandinsky 6.0 Video, a family of foundation diffusion models for synchronized text-to-audio-video generation, comprising Kandinsky 6.0 Video Lite (3B parameters) and Kandinsky 6.0 Video Pro (29B parameters). Both models generate 5-second video clips with synchronized 44 kHz audio, including lip-sync, in text-to-audio-video (T2AV) and image-to-audio-video (I2AV) modes; a built-in super-resolution model…

## 5. In-Distribution Forcing for Long Video Generation at Test Time

- 分数：29.5  ·  HF 赞：35  ·  来源：huggingface
- 兴趣命中：evaluation, benchmark
- 作者：Jeongwoo Shin, Youngyoon Choi, Sangwoo Jo, Hyunmog Kim, Sungjoon Choi, Joonseok Lee, Jaewoong Choi, Jaemoo Choi
- 链接：[arXiv](https://arxiv.org/abs/2610.03120) · [PDF](https://arxiv.org/pdf/2610.03120) · [HF](https://huggingface.co/papers/2610.03120)

Modern autoregressive (AR) video diffusion models excel at short-horizon video generation, yet generating long videos remains challenging due to drifting, where colors and textures shift, and motion dynamics decay. Existing works primarily rely on KV conditioning, which selects or modifies cached key-value (KV) entries to mitigate drifting. However, we observe that KV conditioning alone is insufficient as it assumes…

## 6. Rethinking Cross-Tokenizer On-Policy Distillation: From Alignment Coverage to Supervision Reliability

- 分数：28.0  ·  HF 赞：28  ·  来源：huggingface + arxiv
- 兴趣命中：reasoning
- 作者：Bingxi Hou, Guochao Jiang, Guofeng Quan, Weiqing Li, Wenfeng Feng, Guohua Liu, Yuewei Zhang
- 链接：[arXiv](https://arxiv.org/abs/2610.08448) · [PDF](https://arxiv.org/pdf/2610.08448) · [HF](https://huggingface.co/papers/2610.08448)

On-Policy Distillation (OPD) trains a student on its own generations using teacher feedback. With different tokenizers, comparing teacher and student predictions requires alignment at both sequence and vocabulary levels. In this paper, we examine whether expanding this alignment coverage improves learning. Across three heterogeneous teacher--student pairs on mathematical reasoning and code generation, strict 1:1…

## 7. Foundations of Proactive Agents: Principles, Technical Layers, and Proactivity-Gym

- 分数：27.5  ·  HF 赞：27  ·  来源：huggingface
- 兴趣命中：agent, evaluation, spec
- 作者：Jio Oh, Seunghyun Do, Young-Jun Lee, Steven Euijong Whang, Dongyeop Kang
- 链接：[arXiv](https://arxiv.org/abs/2609.37267) · [PDF](https://arxiv.org/pdf/2609.37267) · [HF](https://huggingface.co/papers/2609.37267)

Proactive LLM agents can turn idle compute into useful support before users ask. Yet even correct work can misread user context, impose review costs, or undermine trust. This work proposes foundations for designing, realizing, and evaluating proactive LLM agents around three joint principles (3T): Task Capability, anticipating relevant needs and correctly performing useful work; Temporal Allocation, allocating…

## 8. Optimizing the Optimizer: Language Models Discover Faster Molecular Relaxation

- 分数：26.0  ·  HF 赞：20  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark, language model
- 作者：Artem Tsypin, Vladimir Deshchenya, Kuzma Khrabrov, Denis Potapov, Maxim Radchenko, Artur Kadurin, Michael G. Medvedev
- 链接：[arXiv](https://arxiv.org/abs/2610.06577) · [PDF](https://arxiv.org/pdf/2610.06577) · [HF](https://huggingface.co/papers/2610.06577)

Geometry optimization is a major cost in many quantum-chemical workflows: each optimization step requires one force evaluation, and at the density-functional level that evaluation dominates the wall time. Research in this area has produced a broad range of optimization methods, and we ask whether a language model can improve on the best of them through autoresearch. An agent rewrites the optimizer itself to minimize…

## 9. Towards Looped Models Done Right, Part II: Rethinking at Fixed Points

- 分数：26.0  ·  HF 赞：20  ·  来源：huggingface
- 兴趣命中：reinforcement learning, language model, coding, spec
- 作者：Benhao Huang, Chufan Shi, Junlin Chen, Shicheng Wen, Zhengzhong Liu, Eric Xing, Xuezhe Ma
- 链接：[arXiv](https://arxiv.org/abs/2610.06833) · [PDF](https://arxiv.org/pdf/2610.06833) · [HF](https://huggingface.co/papers/2610.06833)

Every recurrence of a looped language model adds cost in training, decoding, prefill, and reinforcement learning (RL). The closer recurrent states get to fixed points, the less the path to them matters. This enables truncated backpropagation in training; terminal key-value (KV) sharing for decoding with almost no loss in accuracy; a distilled student that prefills up to 1.79x faster; and RL updates that compute…

## 10. SearchJev: A Fast and Calibrated System-1 Model for Search Agents

- 分数：25.5  ·  HF 赞：19  ·  来源：huggingface
- 兴趣命中：agent, reasoning, evaluation, benchmark, language model, planning
- 作者：Congfeng Cao, Lipeng Zuo, Konstantinos Papakostas, Qiwei Xu, Songwei Xu, Lun Zhou, Zhaochun Ren, Yougang Lyu, Xiaohui Yan
- 链接：[arXiv](https://arxiv.org/abs/2610.05107) · [PDF](https://arxiv.org/pdf/2610.05107) · [HF](https://huggingface.co/papers/2610.05107)

Search agents repeatedly make short decisions about relevance, evidence sufficiency, and search actions. Using generative language models for these decisions introduces latency and unreliable confidence. We present SearchJev, a fast and calibrated System-1 model that separates search decisions from System-2 reasoning and generation. Given a search state and a decision schema, SearchJev directly scores legal options…

## 11. ASCENT: Online Test-Time Training of Long-Horizon Agents via Self-Distillation of Verified Experience

- 分数：25.5  ·  HF 赞：19  ·  来源：huggingface
- 兴趣命中：agent, memory, reasoning, language model, large language, retrieval
- 作者：Haodong Lu, Dong Gong
- 链接：[arXiv](https://arxiv.org/abs/2610.05303) · [PDF](https://arxiv.org/pdf/2610.05303) · [HF](https://huggingface.co/papers/2610.05303)

A large language model (LLM) agent solves long-horizon tasks through many reasoning-action turns, with one verification signal at termination. Deployed agents face streams of related tasks, making their trajectories a natural resource for improvement. In-context adaptation agents store reflections, memories, or skills as text, so reuse depends on retrieving the right experience and on a frozen policy executing it.…

## 12. World Editing: Intervening on Executable Worlds at Increasing Depth

- 分数：24.5  ·  HF 赞：17  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark, coding
- 作者：Max Ku, Nok-Kan Law, Yu-Chien Tang, Shih-Ying Yeh, Ping Nie, Andy Zheng, Tat Hei Lai, Fei-Yueh Chen, Nikko Yu, Wei-Chieh Sun, Suzy Huang, Chiao-Wei Hsu, Chih-Chuan Huang, Chak-Wing Mak, Ho Yin Sam Ng, Edisy Kin Wai Chan, Min-Hung Chen, Ho Kei Cheng
- 链接：[arXiv](https://arxiv.org/abs/2610.02331) · [PDF](https://arxiv.org/pdf/2610.02331) · [HF](https://huggingface.co/papers/2610.02331)

Interactive world models are increasingly capable of generating environments and acting within them, yet deliberately editing an existing executable world remains underexplored. We formulate world editing as intervening on an existing world while preserving properties that should remain unchanged, and introduce intervention depth as an axis describing how strongly an edit couples world entities, dynamics, and…

## 13. AutoSciBench: Autonomous Benchmark Generation for Evaluating Scientific Agents

- 分数：24.5  ·  HF 赞：17  ·  来源：huggingface
- 兴趣命中：agent, reasoning, evaluation, benchmark, spec
- 作者：Dongki Kim, Namkyeong Lee, Surag Nair, Carl Edwards, Xiner Li, Edward De Brouwer, Jenna Lynn Collier, Sung Ju Hwang, Gabriele Scalia, Ehsan Hajiramezanali
- 链接：[arXiv](https://arxiv.org/abs/2610.05140) · [PDF](https://arxiv.org/pdf/2610.05140) · [HF](https://huggingface.co/papers/2610.05140)

As agents rapidly evolve, existing benchmarks can become saturated, limiting their ability to distinguish capabilities and reveal remaining failure modes. Particularly in scientific domains, constructing and updating benchmarks requires substantial time, labor, and domain expertise, making it difficult to keep evaluation aligned with advances in agent capabilities. We address this challenge by investigating whether…

## 14. OmniReasoning: Pushing the Limits of Audio-Visual Joint Reasoning

- 分数：24.0  ·  HF 赞：20  ·  来源：huggingface
- 兴趣命中：reasoning, benchmark, spec
- 作者：Junming Lin, Yuxuan Wang, Zhenxin Lei, Yuxin Liu, Ruixun Liu, Yinsong Yan, Ling Wang, Minghao Han, Yunfei Chu, Shun Lei, Xueyao Zhang, Qize Yang, Jin Xu, Yiwu Zhong
- 链接：[arXiv](https://arxiv.org/abs/2609.39490) · [PDF](https://arxiv.org/pdf/2609.39490) · [HF](https://huggingface.co/papers/2609.39490)

Recent advances have enabled unified omni-modal models in understanding audio, vision, and language. However, existing benchmarks, training data, and learning methods largely treat the modalities independently, leaving the capability of audio-visual joint reasoning poorly evaluated and insufficiently elicited. We address this gap with a benchmark, data engine, and learning method. First, we introduce…

## 15. Representation-Space MMD for Diffusion Language Models

- 分数：24.0  ·  HF 赞：20  ·  来源：huggingface
- 兴趣命中：benchmark, language model, coding
- 作者：Ilya Drobyshevskiy, Ilia Sudakov, Maksim Semenov, Denis Kuznedelev, Maksim Ignatov, Pavel Temirchev, Nikita Balagansky, Viacheslav Meshchaninov, Nikita Gushchin, Dmitry Baranchuk
- 链接：[arXiv](https://arxiv.org/abs/2610.06648) · [PDF](https://arxiv.org/pdf/2610.06648) · [HF](https://huggingface.co/papers/2610.06648)

We introduce a post-training method for diffusion language models (DLMs) that minimizes Maximum Mean Discrepancy (MMD) between generated and reference distributions in the feature space of a frozen pretrained DLM. To estimate MMD, we retain contextual features at individual token positions, obtaining multiple observations per sequence from a single extractor pass. We optimize this objective using policy gradients…

## 16. TRACE: Rollout-Guided Quantization-Aware Training for FP4 Reinforcement Learning of MoE Language Models

- 分数：24.0  ·  HF 赞：16  ·  来源：huggingface
- 兴趣命中：memory, reasoning, reinforcement learning, language model, large language, coding
- 作者：Xin Wang, Hao Yu, Zhengyang Zhuge, Bochao Mao, Zheng Li, Junda Feng, Yuyan Luo, Yi Zhang, Yizhong Cao, Mi Zhang, Dayiheng Liu, Jianwei Zhang
- 链接：[arXiv](https://arxiv.org/abs/2610.07767) · [PDF](https://arxiv.org/pdf/2610.07767) · [HF](https://huggingface.co/papers/2610.07767)

Reinforcement learning (RL) for post-training large language models (LLMs) incurs substantial computation and memory overhead during rollout generation, which motivates low-precision rollout for efficient RL training. However, existing FP4 RL methods suffer from a key limitation: they primarily optimize quantization accuracy on the training and rollout paths independently rather than directly reducing the…

## 17. DuoMatching: Joint-Marginal Distribution Matching for Few-Step Video Generation

- 分数：23.5  ·  HF 赞：27  ·  来源：huggingface
- 兴趣命中：evaluation
- 作者：Jiahao Zhan, Yan Wang, Yongrui Ma, Qunliang Xing, Ruchang Yao, Runtao Liu, Shijie Zhao, Tianfan Xue
- 链接：[arXiv](https://arxiv.org/abs/2610.03543) · [PDF](https://arxiv.org/pdf/2610.03543) · [HF](https://huggingface.co/papers/2610.03543)

Streaming video generation has benefited from distribution matching distillation (DMD), which matches the joint distribution of video frames to a video teacher's approximation of the real video distribution. Although this joint matching mitigates drift during autoregressive rollouts, limitations remain in visual quality and semantic alignment. To address these limitations, we propose DuoMatching, a distribution…

## 18. CANOPY: Adaptive-Granularity Evidence Compression for Multimodal RAG

- 分数：23.5  ·  HF 赞：19  ·  来源：huggingface
- 兴趣命中：benchmark, spec, retrieval
- 作者：Hyojeong Yun, Jueun Kim, Wook-Shin Han
- 链接：[arXiv](https://arxiv.org/abs/2610.00923) · [PDF](https://arxiv.org/pdf/2610.00923) · [HF](https://huggingface.co/papers/2610.00923)

Multimodal RAG retrieves text, tables, images, and videos, but choosing a retrieval granularity does not determine how much context to retain within each item. Coarse units include irrelevant content, while uniformly fine selection can remove context needed to interpret the evidence. Existing compressors address this trade-off with modality-specific mechanisms, leaving open a shared procedure for adapting the…

## 19. SEER: Self-Evolving Event Reasoning and Retrieval for Time Series Forecasting

- 分数：23.5  ·  HF 赞：15  ·  来源：huggingface
- 兴趣命中：memory, reasoning, benchmark, language model, retrieval
- 作者：Mingtian Tan, Palash Goyal, Mihir Parmar, Sarkar Snigdha Sarathi Das, Chun-Liang Li, Nanyun Peng, Thomas Hartvigsen, Jinsung Yoon, Tomas Pfister
- 链接：[arXiv](https://arxiv.org/abs/2610.04109) · [PDF](https://arxiv.org/pdf/2610.04109) · [HF](https://huggingface.co/papers/2610.04109)

Real-world time series are frequently driven by exogenous events and structural shifts, rendering conventional forecasting based solely on historical numerical observations insufficient. While language models can retrieve external news, standard retrieval-augmented approaches struggle with high noise, missing signals, and an inability to reason causally about event impacts. We propose SEER (Self-Evolving Event…

## 20. OSWorld-Pro: Process-based Evaluation for Computer Use Agents

- 分数：23.0  ·  HF 赞：22  ·  来源：huggingface
- 兴趣命中：agent, evaluation
- 作者：Zhilin Wang, Shaokun Zhang, Yifan Zhang, Hao Zhang, Jin Xu, Binfeng Xu, Jian Hu, Yunheng Zou, Karan Sapra, Andrew Tao, Jan Kautz, Yi Dong
- 链接：[arXiv](https://arxiv.org/abs/2609.24890) · [PDF](https://arxiv.org/pdf/2609.24890) · [HF](https://huggingface.co/papers/2609.24890)

Evaluation of Computer-Use Agents (CUAs) is often limited to the final deliverables they create (at the end of hundreds of steps) and assessed with functional verifiers, as seen in OSWorld. However, such evaluation of end-state performance lacks transparency into how and why agents fail in various tasks, obfuscating critical insight for subsequent improvement. For instance, agents that err during keyboard inputs…

## 21. Rethinking Long-Video Efficiency: A Joint Allocation Perspective on Frames, Pixels, and Front-End Latency

- 分数：22.0  ·  HF 赞：12  ·  来源：huggingface
- 兴趣命中：benchmark, language model, coding, spec
- 作者：Sixun Dong, Wei Li, Andong Deng, Qi Qian, Victor Zhu, Zhengping Ji, Chen Chen
- 链接：[arXiv](https://arxiv.org/abs/2610.04318) · [PDF](https://arxiv.org/pdf/2610.04318) · [HF](https://huggingface.co/papers/2610.04318)

Efficient long-video understanding with vision-language models (VLMs) is often framed as selecting informative frames or visual tokens at a fixed native resolution. We show that per-frame resolution can instead be traded for denser temporal coverage, while front-end decoding latency depends on the size of the candidate pool rather than the final token budget. An empirical study across multiple VLMs and long-video…

## 22. Base Models Can Reason By Taking a Cue From Training Data

- 分数：22.0  ·  HF 赞：12  ·  来源：huggingface
- 兴趣命中：reasoning, reinforcement learning, language model, coding
- 作者：Sophie L. Wang, Amil Dravid, Rulin Shao, Kevin Farhat, Sewon Min, Alexei A. Efros
- 链接：[arXiv](https://arxiv.org/abs/2610.06851) · [PDF](https://arxiv.org/pdf/2610.06851) · [HF](https://huggingface.co/papers/2610.06851)

In this paper, we study how training data creates associations between the tokens at the start of a base model's response and the reasoning behavior that follows. First, we demonstrate that fixing particular starting token cues makes a base model's performance competitive with that of its reinforcement learning (RL)-trained counterparts on math and coding. For instance, the cue ".\n\nOkay" raises Olmo-3-7B's…

## 23. HuatuoGPT-3: RL-Only Domain Adaptation from Base Models

- 分数：21.5  ·  HF 赞：15  ·  来源：huggingface
- 兴趣命中：language model, large language, spec
- 作者：Junying Chen, Xinyuan Xie, Ziniu Li, Wenyuan Gu, Jianquan Li, Xiang Wan, Guangjun Yu, Ruoyu Sun, Haizhou Li, Benyou Wang
- 链接：[arXiv](https://arxiv.org/abs/2610.05966) · [PDF](https://arxiv.org/pdf/2610.05966) · [HF](https://huggingface.co/papers/2610.05966)

Domain adaptation aims to turn a general-purpose large language model (LLM) into an expert for a target domain. While the dominant SFT+RL pipeline offers a convenient cold start, it may reduce exploration diversity and introduces additional complexity through multi-stage optimization. These limitations motivate RL-only adaptation. However, pure on-policy RL suffers from a cold-start problem, while mixed-policy RL…

## 24. Video2Skill: From Streaming Experience to Reusable Embodied Skills

- 分数：21.5  ·  HF 赞：11  ·  来源：huggingface
- 兴趣命中：agent, benchmark, language model, planning
- 作者：Jianshu Zhang, Ce Zhang, Xiyuan Yang, Chenwei Xu, Haoran Lu, Yijiang Li, Yaqi Xie, Katia P. Sycara, Han Liu
- 链接：[arXiv](https://arxiv.org/abs/2609.36691) · [PDF](https://arxiv.org/pdf/2609.36691) · [HF](https://huggingface.co/papers/2609.36691)

Manipulation behaviors vary widely across objects and scenes, but they share a small set of reusable skills, and planning with these skills helps embodied agents generalize to new tasks. Yet an agent can only plan with skills it knows. Recovering skills from observed experience, the inverse of planning, builds this knowledge over time and yields skill data for training future agents. Vision-Language Models (VLMs)…

## 25. QuantCode Model: Specializing Language Models for Executable Algorithmic Trading Code

- 分数：21.5  ·  HF 赞：11  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark, language model, large language, spec
- 作者：Alexey Chernysh, Orkhan Ekhtibarov, Dmitry Zmitrovich
- 链接：[arXiv](https://arxiv.org/abs/2609.39420) · [PDF](https://arxiv.org/pdf/2609.39420) · [HF](https://huggingface.co/papers/2609.39420)

Large language models are strong general-purpose code generators, but executable algorithmic trading remains a demanding specialization target: a model must translate a natural-language strategy specification into correct program logic for a specialized trading framework, execute on historical data, produce trades, and remain semantically faithful to the request. We study two complementary mechanisms for…

## 26. UndoBench: Separating Task Competence from Recovery Capability in Tool-Using AI Agents

- 分数：21.5  ·  HF 赞：11  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark, planning
- 作者：Dolly Sah, Tanmay Sah, Harshul Jain, Tanya Sah
- 链接：[arXiv](https://arxiv.org/abs/2610.05622) · [PDF](https://arxiv.org/pdf/2610.05622) · [HF](https://huggingface.co/papers/2610.05622)

Tool-using AI agents are increasingly deployed across enterprise software systems, yet widely used benchmarks primarily evaluate nominal task completion, conflating baseline planning competence with operational fault recovery. We introduce UndoBench, a benchmark spanning 36 base workflows and 36 fault scenarios across 8 enterprise domains, decoupling task competence from recovery capability via counterfactual paired…

## 27. LoGRA: Scaling LLM Reinforcement Learning with Low-Rank Gradient Sketches

- 分数：21.5  ·  HF 赞：11  ·  来源：huggingface
- 兴趣命中：memory, reasoning, reinforcement learning, language model, large language
- 作者：Shaokun Zhang, Yifan Zhang, Jian Hu, Yueying Li, Hao Zhang, Binfeng Xu, Jan Kautz, Yi Dong
- 链接：[arXiv](https://arxiv.org/abs/2610.06647) · [PDF](https://arxiv.org/pdf/2610.06647) · [HF](https://huggingface.co/papers/2610.06647)

Reinforcement learning (RL) has greatly advanced the capabilities of large language models (LLMs), but its memory demands remain a barrier to broader adoption. We introduce LoGRA, an approach to RL post-training that reduces memory by retaining useful learning signals in low-rank gradient sketches. These compact representations support both model updates and efficient policy synchronization. To prevent overly large…

## 28. RobotUse: Allocating Computation, Context, and Decisions

- 分数：21.0  ·  HF 赞：14  ·  来源：huggingface
- 兴趣命中：agent, spec, planning
- 作者：Junhoo Lee, Injun Baek, Seungyeon Kim, Suhyun Jeon, Minkyu Kim, Baekseung Kim, Nojun Kwak
- 链接：[arXiv](https://arxiv.org/abs/2610.04929) · [PDF](https://arxiv.org/pdf/2610.04929) · [HF](https://huggingface.co/papers/2610.04929)

Robot agents must connect their intended actions to observed outcomes while retaining the context needed to revise their choices over repeated attempts. Existing interfaces often leave these choices inside predefined tools or require agents to manage detailed execution code and its growing history. We introduce RobotUse, a robot agent harness that organizes computation, context, and decisions around specifying and…

## 29. Selection-Based Structured Reasoning: Toward Efficient Multimodal Search Agents

- 分数：21.0  ·  HF 赞：10  ·  来源：huggingface
- 兴趣命中：agent, reasoning, reinforcement learning, benchmark, spec
- 作者：Feiyu Gavin Zhu, Xiaoyu Zhu, Jiqi Yang, Rui Yang, Arnab Kumar Mondal, Yancheng Wang, Xinke Deng, Jean Oh, Reid Simmons, Joerg Liebelt, Xiang Kong, Zhongyu Jiang
- 链接：[arXiv](https://arxiv.org/abs/2610.01892) · [PDF](https://arxiv.org/pdf/2610.01892) · [HF](https://huggingface.co/papers/2610.01892)

Multimodal agents commonly generate free-form reasoning before each action. For small models, limited model capacity can result in lengthy reasoning that provides little useful guidance for action generation while incurring substantial inference cost. To address this challenge, we introduce Selection-based Structured Reasoning (SSR), a framework that reformulates reasoning as selection instead of open-ended…

## 30. What Matters for Latent Reasoning with Flow Matching

- 分数：21.0  ·  HF 赞：10  ·  来源：huggingface
- 兴趣命中：reasoning, benchmark, language model, large language
- 作者：Yassine Ouali, Adrian Bulat, Georgios Tzimiropoulos
- 链接：[arXiv](https://arxiv.org/abs/2610.06666) · [PDF](https://arxiv.org/pdf/2610.06666) · [HF](https://huggingface.co/papers/2610.06666)

Latent reasoning lets a large language model (LLM) think in a continuous space and verbalize only the answer. We argue that an effective latent thought must meet five requirements: it should be useful, helping produce the correct answer rather than merely changing it, diverse, so that resampling yields different reasoning trajectories, explainable, so that a decoded chain of thought (CoT) reflects reasoning the…

## 31. From Knowledge Access to Source Learning: Developing Source-Specific Competence

- 分数：20.5  ·  HF 赞：9  ·  来源：huggingface
- 兴趣命中：agent, memory, benchmark, language model, large language, spec
- 作者：Lucheng Fu, Kejing Xia, Yiyang Wang, Yiqiao Jin, Jinjin He, Xiyuan Yang, Haoxin Liu, Ye Yu, Haibo Jin, Yijia Xiao, Wenke Lee, B. Aditya Prakash, Haohan Wang
- 链接：[arXiv](https://arxiv.org/abs/2610.02150) · [PDF](https://arxiv.org/pdf/2610.02150) · [HF](https://huggingface.co/papers/2610.02150)

Large language model (LLM) agents increasingly rely on persistent external sources to solve sequences of knowledge-intensive tasks. Existing methods improve how source content is accessed and organized, while agent-memory systems preserve reusable knowledge from prior interactions, but repeated use of the same source is still largely treated as repeated access rather than an opportunity to progressively improve…

## 32. The Missing Primitive: Diagnosing and Repairing Mathematical Reasoning in Large Language Models

- 分数：20.5  ·  HF 赞：9  ·  来源：huggingface
- 兴趣命中：reasoning, benchmark, language model, large language
- 作者：Shuo Xing, Zilin Dai, Chengyuan Qian, Fangzhou Lin, Wenjing Chen, Ping He, Pan Lu, Alvaro Velasquez, Mohit Bansal, Zhengzhong Tu
- 链接：[arXiv](https://arxiv.org/abs/2610.02191) · [PDF](https://arxiv.org/pdf/2610.02191) · [HF](https://huggingface.co/papers/2610.02191)

While Large Language Models (LLMs) have demonstrated striking capabilities on frontier mathematical problems, it remains unclear whether they possess the structural mathematical understanding underlying their solutions. In this paper, we take a first step toward systematically studying mathematical understanding in LLMs, from diagnosing its distinct capabilities to leveraging these findings to improve post-training.…

## 33. Towards In-Parameter Memory Augmentation for Large Language Models

- 分数：20.5  ·  HF 赞：1  ·  来源：huggingface + arxiv
- 兴趣命中：agent, memory, language model, large language, coding
- 作者：Haoyu Huang, Zhongwei Xie, Jiaxin Bai, Yisen Gao, Hong Ting Tsang, Wuganjing Song, Huihao Jing, Yufei Li, Yangqiu Song
- 链接：[arXiv](https://arxiv.org/abs/2610.08630) · [PDF](https://arxiv.org/pdf/2610.08630) · [HF](https://huggingface.co/papers/2610.08630)

Recently Large Language Models (LLMs) and LLM-based agents increasingly need to incorporate knowledge acquired after pretraining, e.g., domain facts, user preferences, documents, and interaction experience. In-context learning (ICL) and ICL-based agent harness remain flexible, but they consume context capacity and incur repeated discretized encoding cost that grows with context length. \textbf{In-parameter memory}…

## 34. World Models' Last Exam in Physics

- 分数：20.5  ·  HF 赞：1  ·  来源：huggingface + arxiv
- 兴趣命中：evaluation, benchmark, language model, spec, planning
- 作者：Mingju Gao, Qingle Liu, Yuzhao Peng, Xinjie Lin, Ziming Qin, Zheng Jiang, Wenyi Li, Calvin Xiao, Youjie Zheng, Kaisen Yang, Qinhuai Na
- 链接：[arXiv](https://arxiv.org/abs/2610.08791) · [PDF](https://arxiv.org/pdf/2610.08791) · [HF](https://huggingface.co/papers/2610.08791)

Video world models can produce visually convincing yet physically inconsistent sequences, raising concerns about their reliability for prediction and planning in embodied AI systems. Existing evaluations often rely on model-based judgments or reference videos, while direct physical tests largely focus on mechanics. We introduce World Models' Last Exam in Physics, a measurement-based benchmark for evaluating physical…

## 35. Beyond Semantic Similarity: Performance and Costs of Agentic Retrieval for Complex Tasks

- 分数：20.0  ·  HF 赞：8  ·  来源：huggingface
- 兴趣命中：agent, reasoning, language model, large language, spec, retrieval
- 作者：Reza Esfandiarpoor, Radek Osmulski, Yauhen Babakhin, Gabriel de Souza P. Moreira, Oliver Holworthy, Jie He, Ronay Ak, Jiarui Cai, Ryan Chesler, Bo Liu, Even Oldridge
- 链接：[arXiv](https://arxiv.org/abs/2610.05750) · [PDF](https://arxiv.org/pdf/2610.05750) · [HF](https://huggingface.co/papers/2610.05750)

Modern information systems, including many agentic workflows, use dense retrieval to explore large amounts of unstructured data. However, dense retrieval relies on surface-level semantic similarity, which is insufficient for increasingly complex search applications. Here, we investigate agentic retrieval that combines the reasoning capabilities of Large Language Models (LLMs) with the efficient corpus exploration of…

## 36. Self-Generated Feedback Destabilizes Test-Time Training: A Causal Decomposition of Long-Horizon Adaptation

- 分数：19.5  ·  HF 赞：23  ·  来源：huggingface
- 兴趣命中：-
- 作者：Cheng Luo, Bing Li, Bernard Ghanem
- 链接：[arXiv](https://arxiv.org/abs/2610.05076) · [PDF](https://arxiv.org/pdf/2610.05076) · [HF](https://huggingface.co/papers/2610.05076)

Test-time training (TTT) lets a model store information in its weights during inference. When the model learns from its own output, however, each update also changes the model that generates the next training example. Across 128K-token streams, retaining generated-text updates worsens prediction on independent human-written text with three TTT-E2E model configurations (labeled 125M, 760M, and 3B). The same failure…

## 37. DeskForge: Dense Supervision from Desktop Environments for Computer-Use Agents

- 分数：19.5  ·  HF 赞：7  ·  来源：huggingface
- 兴趣命中：agent, benchmark, language model, spec
- 作者：A. Said Gurbuz, Ahmed Nassar, Sunghwan Hong, Marc Pollefeys, Peter W. J. Staar
- 链接：[arXiv](https://arxiv.org/abs/2610.02320) · [PDF](https://arxiv.org/pdf/2610.02320) · [HF](https://huggingface.co/papers/2610.02320)

Computer-use agents need to reliably ground action targets in complex desktop scenes, where multiple applications, overlapping windows, and visually similar controls compete for attention. Existing training data rarely pair such scenes with dense annotations or vary them in a controlled way. We introduce DeskForge, a controllable desktop environment that composes and explores real applications to generate…

## 38. TextReg: Mitigating Prompt Distributional Overfitting via Regularized Text-Space Optimization

- 分数：19.5  ·  HF 赞：7  ·  来源：huggingface
- 兴趣命中：reasoning, benchmark, language model, large language, spec
- 作者：Lucheng Fu, Ye Yu, Yiyang Wang, Yiqiao Jin, Haibo Jin, B. Aditya Prakash, Haohan Wang
- 链接：[arXiv](https://arxiv.org/abs/2605.21318) · [PDF](https://arxiv.org/pdf/2605.21318) · [HF](https://huggingface.co/papers/2605.21318)

Large language models (LLMs) are highly sensitive to the prompts used to specify task objectives and behavioral constraints. Many recent prompt optimization methods iteratively rewrite prompts using LLM-generated feedback, but the resulting prompts often become longer, accumulate narrow sample-specific rules, and generalize poorly beyond the training distribution. We study this failure mode as prompt distributional…

## 39. ALIVE: Interaction-Aligned Object Insertion for First-Frame-Guided Video Editing

- 分数：19.5  ·  HF 赞：3  ·  来源：huggingface + arxiv
- 兴趣命中：benchmark, language model, spec
- 作者：Zhenghong Zhou, Zhe Lin, Jiebo Luo, Yuqian Zhou
- 链接：[arXiv](https://arxiv.org/abs/2610.08779) · [PDF](https://arxiv.org/pdf/2610.08779) · [HF](https://huggingface.co/papers/2610.08779)

Current video editors can insert objects but often struggle to make them participate in interactions such as being picked up or manipulated. We introduce ALIVE, a framework that makes inserted objects "alive" through coherent interactions with the source video's contents, using an edited first frame and an instruction naming only the added object. We curate 35,800 editing pairs combining 3D-rendered,…

## 40. Dynamic Harness Search: Building Multi-Agent Systems Per-Query via Prediction

- 分数：19.0  ·  HF 赞：10  ·  来源：huggingface
- 兴趣命中：agent, benchmark, spec
- 作者：Som Sagar, Shasha Li, Hejie Cui, Ransalu Senanayake, Sercan Ö. Arık
- 链接：[arXiv](https://arxiv.org/abs/2610.04137) · [PDF](https://arxiv.org/pdf/2610.04137) · [HF](https://huggingface.co/papers/2610.04137)

Agent harnesses specify the roles, instructions, tools, and communication structure used to solve a task, and the right harness depends on the query. Because the value of each design choice is observable only through execution, tailoring a harness to each query has required either executing alternatives at inference time or costly manual design. We introduce SHIFT, which moves execution out of the per-query search…

## 41. Capability-Driven Self-Evolution of Agent Memory

- 分数：19.0  ·  HF 赞：10  ·  来源：huggingface
- 兴趣命中：agent, memory, spec
- 作者：Yaoqi Chen, Yuru Feng, Qianxi Zhang, Baotong Lu, Jianan Lu, Zhirui Wang, Shusen Xu, Zewen Jin, Zengzhong Li, Cheng Li, Qi Chen
- 链接：[arXiv](https://arxiv.org/abs/2610.06361) · [PDF](https://arxiv.org/pdf/2610.06361) · [HF](https://huggingface.co/papers/2610.06361)

Memory self-evolution uses task feedback to iteratively improve executable memory programs that store and retrieve information from past interactions. Existing approaches typically adopt holistic evolution, deriving revision directions from mixed feedback and judging progress by overall performance. This can obscure optimization directions and hide capability-specific gains offset by regressions elsewhere, leaving…

## 42. Code2Games: Enabling Coding Agents for Gaming World Generation

- 分数：19.0  ·  HF 赞：6  ·  来源：huggingface
- 兴趣命中：agent, reasoning, benchmark, coding, planning
- 作者：Wei Wu, Ziyang Xu, Zeyu Zhang, Yang Zhao, Hao Tang
- 链接：[arXiv](https://arxiv.org/abs/2610.05033) · [PDF](https://arxiv.org/pdf/2610.05033) · [HF](https://huggingface.co/papers/2610.05033)

Generating a high-quality gaming world from a natural-language game intent requires joint reasoning about scene structure, spatial layout, gameplay objectives, interactive entities, and executable gameplay logic. Existing coding agents can generate individual assets, scenes, or scripts, but often struggle to maintain consistency across these components. We propose Code2Games, an agentic framework that builds a…

## 43. VeriFine: Scaling Verification for Self-Improvement in Embodied Reasoning

- 分数：18.5  ·  HF 赞：1  ·  来源：huggingface + arxiv
- 兴趣命中：agent, reasoning, evaluation
- 作者：Zewei Zhou, Rachel Luo, Yulong Cao, Chaowei Xiao, Chensheng Peng, Boyi Li, Thomas Tian, Zheng Lian, Yan Wang, Jiaqi Ma, Boris Ivanovic, Marco Pavone, Wenhao Ding
- 链接：[arXiv](https://arxiv.org/abs/2610.08761) · [PDF](https://arxiv.org/pdf/2610.08761) · [HF](https://huggingface.co/papers/2610.08761)

Self-improving policies continually expose new failure patterns, changing what their judges must be able to verify. However, current fixed judges constrain both optimization feedback and the discovery of useful training examples, limiting further self-improvement. This challenge is even more acute in embodied reasoning, where reliable evaluation must account for spatial grounding, causal reasoning, and safety-aware…

## 44. HLA-WM: Hybrid Linear Attention for Long-Horizon Video World Models

- 分数：18.0  ·  HF 赞：8  ·  来源：huggingface
- 兴趣命中：memory, spec, retrieval
- 作者：Zhuokun Chen, Feng Chen, Xi Lin, Xiyu Wu, Jiahao He, Jianfei Cai, Bohan Zhuang
- 链接：[arXiv](https://arxiv.org/abs/2610.05739) · [PDF](https://arxiv.org/pdf/2610.05739) · [HF](https://huggingface.co/papers/2610.05739)

Long-horizon video world models require persistent memory to preserve scene consistency over extended rollouts. Softmax attention retains the full generation history through a growing KV cache, whereas recurrent linear attention compresses history into fixed-size states with substantially lower memory cost. However, we identify severe long-range forgetting in Gated DeltaNet (GDN), where information from distant but…

## 45. Hiding Tool Latency in On-Device Cascaded Voice Agent through Speculative Execution

- 分数：18.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：agent, language model, large language, spec
- 作者：Kyudan Jung, Hyunsin Park, Yoonhyung Lee, Jinhwan Park, Jinhyeok Yang, KiHyun Nam, Jaegul Choo, Jinkyu Lee
- 链接：[arXiv](https://arxiv.org/abs/2610.07641) · [PDF](https://arxiv.org/pdf/2610.07641) · [HF](https://huggingface.co/papers/2610.07641)

Tool-augmented speech assistants typically serialize automatic speech recognition, large language model inference, and external tool execution. As a result, tool latency is incurred only after the user has finished speaking and the LLM has identified the required tool calls. We present speculative tool execution for on-device cascaded voice agents, which predicts tool requests from partial ASR hypotheses and…

## 46. Data Unlearning via Inverse Distillation

- 分数：17.5  ·  HF 赞：19  ·  来源：huggingface
- 兴趣命中：-
- 作者：Aleksei Leonov, Nikita Kornilov, Zhenhe Zhang, Evgeny Burnaev, Iaroslav Koshelev, Alexander Korotin
- 链接：[arXiv](https://arxiv.org/abs/2609.36099) · [PDF](https://arxiv.org/pdf/2609.36099) · [HF](https://huggingface.co/papers/2609.36099)

Multi-step matching models, including flow and diffusion models, produce high-quality outputs but incur substantial inference costs and may reproduce unwanted components of their training datasets. We introduce Inverse Distillation Unlearning (IDU), a unified framework that simultaneously distills a teacher multi-step matching model into an efficient one-step student generator and suppresses outputs corresponding to…

## 47. ProgressCompass: Embodied Progress Reward Models Are Lost Without the Right Context

- 分数：17.5  ·  HF 赞：11  ·  来源：huggingface
- 兴趣命中：agent, benchmark
- 作者：Jianshu Zhang, Keliang Wu, Chengxuan Qian, Xiyuan Yang, Ce Zhang, Ariel Tian, Anbang Liu, Haoran Lu, Han Liu
- 链接：[arXiv](https://arxiv.org/abs/2609.36684) · [PDF](https://arxiv.org/pdf/2609.36684) · [HF](https://huggingface.co/papers/2609.36684)

Embodied agents now take on ever longer tasks. For long tasks, knowing only whether a task finally succeeds or fails says little; the steps along the way matter. Progress Reward Models (PRMs) score how far a task has come at every step, and serve as dense rewards, verifiers and monitors. Yet in long tasks the current frame alone often cannot tell how far the task has come, because progress depends on what happened…

## 48. EVISKILL: Grounding Skill Evolution in Replayable Evidence

- 分数：17.5  ·  HF 赞：11  ·  来源：huggingface
- 兴趣命中：agent, benchmark
- 作者：Yan Zhou, Yili Wang, Yiwei Dai, Qinggang Zhang, Xin Wang
- 链接：[arXiv](https://arxiv.org/abs/2610.05030) · [PDF](https://arxiv.org/pdf/2610.05030) · [HF](https://huggingface.co/papers/2610.05030)

Continual skill evolution enables LLM agents to accumulate and refine reusable procedural knowledge from interaction experience without updating model parameters. Its effectiveness depends on determining not only what to change, but also why a change is justified and when it should become persistent guidance. However, existing experience-driven methods can lose the behavioral evidence and task contexts supporting…

## 49. Making LLMs Say What They Think: Measuring and Improving CoT-Interpretability Alignment

- 分数：17.5  ·  HF 赞：7  ·  来源：huggingface
- 兴趣命中：reasoning, language model, large language
- 作者：Yihuai Hong, Shauli Ravfogel, Chen Zhao, Eunsol Choi
- 链接：[arXiv](https://arxiv.org/abs/2609.38972) · [PDF](https://arxiv.org/pdf/2609.38972) · [HF](https://huggingface.co/papers/2609.38972)

Chain-of-thought (CoT) traces often serve as a proxy for how Large Language Models (LLMs) arrive at their answers. However, growing evidence shows that models' CoT often fails to reflect their internal computations and can be changed without affecting their final answers. In this work, we measure and improve the alignment between the reasoning described in an LLM's CoT and what it computes internally. We propose…

## 50. GUI-HARVEST: Self-Improving GUI Agents through Evidence-Driven Harness Evolution

- 分数：17.5  ·  HF 赞：7  ·  来源：huggingface
- 兴趣命中：agent, evaluation, spec
- 作者：Geyi Yang, Zikun Qu, Xiang Li, Zhiyong Wang, Min Zhang, Shipei Zeng, Zhongxiang Dai
- 链接：[arXiv](https://arxiv.org/abs/2610.00948) · [PDF](https://arxiv.org/pdf/2610.00948) · [HF](https://huggingface.co/papers/2610.00948)

The executable harness surrounding a GUI model determines how observations are assembled, actions are executed, and verification, recovery, and termination are controlled. Compared with harness optimization for non-GUI agents, automatically optimizing this harness poses three coupled challenges: reconciling model intent with observed visual effects, diagnosing failures under variable execution outcomes, and…

## 51. Foresight: planning future perception in streaming VLMs without retraining

- 分数：17.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：evaluation, language model, coding, planning
- 作者：Ashok Prasad Neupane, Dipan Bartaula, Ankit Belbase, Saugat Adhikari, Samip Ghimire, Saroj Poudel, Binod Bhattarai, Danda Pani Paudel
- 链接：[arXiv](https://arxiv.org/abs/2610.03123) · [PDF](https://arxiv.org/pdf/2610.03123) · [HF](https://huggingface.co/papers/2610.03123)

Existing streaming vision-language models (VLMs) continuously perceive and reason over visual streams, but their computational pathways remain fixed throughout inference. Consequently, they cannot adapt computation to evolving scene dynamics, where different future events demand different levels and forms of perception. We show that streaming VLMs inherently possess the ability to anticipate the immediate future,…

## 52. Noise Out, Bias In: Targeted Bias Injection in Diffusion Language Models via Closed-Loop Activation Steering

- 分数：17.0  ·  HF 赞：14  ·  来源：huggingface
- 兴趣命中：language model
- 作者：Sarim Hashmi, Mukul Ranjan, Abdelrahman Elsayed, Muhammad Umer Sheikh, Fahad Shamshad, Nils Lukas
- 链接：[arXiv](https://arxiv.org/abs/2610.05894) · [PDF](https://arxiv.org/pdf/2610.05894) · [HF](https://huggingface.co/papers/2610.05894)

Masked diffusion language models (dLLMs) generate text by iteratively denoising masked positions, re-predicting each token multiple times before it is committed. An autoregressive decoder exposes an answer's distribution once, at the step that commits it; a dLLM exposes it at every denoising step before commitment, and we show that an adversary can exploit this. Since an answer remains open to revision over many…

## 53. When Does Selection Replace Extraction? A Pre-Registered Test of Agent Memory with a Typed Decision Model

- 分数：17.0  ·  HF 赞：10  ·  来源：huggingface
- 兴趣命中：agent, memory
- 作者：Rishabh Sharma, Rishika Lall
- 链接：[arXiv](https://arxiv.org/abs/2609.34227) · [PDF](https://arxiv.org/pdf/2609.34227) · [HF](https://huggingface.co/papers/2609.34227)

Does conversational memory need LLM-extracted facts, or is selecting the right raw turns enough? Published results disagree. Extraction-based systems report gains from distilled facts. Recent studies find raw history with good ranking does as well, but disagree about whether ranking matters. We ran a pre-registered study on held-out LoCoMo conversations and LongMemEval. At a tight budget on LoCoMo, raw turns…

## 54. OmniConfess: Eliciting Token Confessions to Mitigate Omni-Modal Hallucination

- 分数：17.0  ·  HF 赞：6  ·  来源：huggingface
- 兴趣命中：benchmark, language model, large language
- 作者：Huiqiang Rong, Haoran Luo, Hui Feng, Zhonghong Ou, Kaiwen Xue, Guoxin Zhang, Yifan Zhu
- 链接：[arXiv](https://arxiv.org/abs/2610.02999) · [PDF](https://arxiv.org/pdf/2610.02999) · [HF](https://huggingface.co/papers/2610.02999)

Omni-modal large language models (OmniLLMs) unify text, images, audio, and video, yet hallucinate when generation relies on the wrong evidence. Existing inference-time methods can reduce hallucinations, but rarely reveal which evidence sustains a generated commitment. We introduce OmniConfess, a training-free method for mitigating omni-modal hallucinations. It fixes a candidate response and re-scores it at token…

## 55. PerturBot: Breaking Shortcut Priors in Vision-Language-Action Models with Perturbative Training

- 分数：16.5  ·  HF 赞：13  ·  来源：huggingface
- 兴趣命中：evaluation
- 作者：Mingyu Liu, Chonghao Sima, Tianjian Feng, Hanqing Wang, Cong Chen, Hao Chen, Chunhua Shen
- 链接：[arXiv](https://arxiv.org/abs/2610.04616) · [PDF](https://arxiv.org/pdf/2610.04616) · [HF](https://huggingface.co/papers/2610.04616)

A vision--language--action (VLA) policy can complete complex tasks while ignoring the evidence that should determine its actions. An object held near the wrist camera can displace the instructed target. Language and action show the same pattern: a familiar noun can trigger the operation it was paired with in training even after the verb changes, and a gripper that closed on nothing may lift anyway. We call these…

## 56. Certification of Real Images through Calibrated Content Authentication

- 分数：16.5  ·  HF 赞：13  ·  来源：huggingface
- 兴趣命中：evaluation
- 作者：Sarim Hashmi, Abdelrahman Elsayed, Mohammed Talha Alam, Samuele Poppi, Nils Lukas
- 链接：[arXiv](https://arxiv.org/abs/2610.05870) · [PDF](https://arxiv.org/pdf/2610.05870) · [HF](https://huggingface.co/papers/2610.05870)

Generative models can synthesize high-quality inauthentic multimedia content that is already being misused at scale. We evaluate twenty deepfake detectors against ten generators released in the last four years and find accuracy decreasing over time, from near-perfect 99.5% to 76%. Adversarial perturbations further reduce every baseline detector to below 2% accuracy, effectively inverting the detector's assigned…

## 57. When to Switch: Reliable Action-Chunk Extension for Vision-Language-Action Models

- 分数：16.5  ·  HF 赞：13  ·  来源：huggingface
- 兴趣命中：benchmark
- 作者：Seonghoon Yu, Dongwon Kim, HyungRok Jung, Yoonjae Baek, Byung-kwan Lee, Suha Kwak, Jeany Son
- 链接：[arXiv](https://arxiv.org/abs/2610.05719) · [PDF](https://arxiv.org/pdf/2610.05719) · [HF](https://huggingface.co/papers/2610.05719)

Vision-Language-Action (VLA) models serve as unified policies for robotic manipulation, yet their expensive inference forces robots to pause between policy calls, resulting in stop-and-go execution that interrupts smooth motion and prolongs task completion. Extending the action chunk reduces policy calls and hence these pauses, but predicting farther into the future makes long-chunk execution unreliable. To…

## 58. OpenRUA: Robot-Use Agents Are Zero-Shot Visuomotor Policies

- 分数：16.5  ·  HF 赞：5  ·  来源：huggingface
- 兴趣命中：agent, coding, spec
- 作者：Zhaoyang Chu, Earl T. Barr, Claire Le Goues, Peter O&#39;Hearn, Mark Harman, Federica Sarro, He Ye
- 链接：[arXiv](https://arxiv.org/abs/2610.02459) · [PDF](https://arxiv.org/pdf/2610.02459) · [HF](https://huggingface.co/papers/2610.02459)

Coding agents are extending their reach into the physical world by writing and executing robot control programs. One might expect the agents to use the existing mature software stack that engineers have developed over decades to access sensors and control motion. Yet prior work primarily engineers complex custom harnesses to orchestrate agents for robot use, particularly by prescribing specialized workflows and…

## 59. Intent Interpretation at RIC Timescales: Jev Decision Models versus Large Language Models in 6G Open RAN

- 分数：16.5  ·  HF 赞：5  ·  来源：huggingface
- 兴趣命中：benchmark, language model, large language
- 作者：Delong Li, Xu Wang, Haochen Gong, Rui Lang, Guangsheng Yu
- 链接：[arXiv](https://arxiv.org/abs/2609.23136) · [PDF](https://arxiv.org/pdf/2609.23136) · [HF](https://huggingface.co/papers/2609.23136)

Intent-based Open RAN needs an interpreter that turns intents into A1 policies within the loop of the RAN intelligent controller (RIC). Decision models such as Jev-1.13.0 return typed policy fields, whereas generative large language models (LLMs) produce the policy token by token. We ask whether the extra delay of LLMs costs control deadlines, RIC capacity, or radio performance. We compare Jev-1.13.0 and two other…

## 60. Judged Useless, Queried Anyway: Tool-Using Agents Rarely Turn Their Own Evidence Judgments into Stopping Decisions

- 分数：16.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：agent, memory, reasoning, retrieval
- 作者：Chubin Zhang, Zhenglin Wan, Xingrui Yu, Jingxuan Wu, Yaxin Zhou, Ivor Tsang, Bo An
- 链接：[arXiv](https://arxiv.org/abs/2610.06191) · [PDF](https://arxiv.org/pdf/2610.06191) · [HF](https://huggingface.co/papers/2610.06191)

An agent whose tool keeps returning nothing useful should stop relying on it. In a retrieval environment with controlled source failures, we separate how agents judge results from what they do. We compare stopping at the same step after longer and shorter runs of results the agent judged useless; this contrast is zero for clock- or deadline-driven stopping. Where we record their judgments, the seven agents we test…

## 61. Harness Engineering for Software Engineering via Modular Executable Dev-Primitives

- 分数：16.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：agent, reasoning, benchmark, language model, large language
- 作者：Haibo Jin, Xinjie Li, Peng Kuang, Haohan Wang
- 链接：[arXiv](https://arxiv.org/abs/2610.07832) · [PDF](https://arxiv.org/pdf/2610.07832) · [HF](https://huggingface.co/papers/2610.07832)

Large language models (LLMs) equipped with terminal access have demonstrated strong capabilities in automating software engineering tasks. However, existing agents remain brittle on long-horizon workflows, where they must repeatedly reconstruct program state scattered across source files, configurations, tests, dependencies, and runtime behavior, leading to increasingly long interaction histories, context explosion,…

## 62. From Evidence to Action: How Tool-Using Agents Fail

- 分数：16.0  ·  HF 赞：12  ·  来源：huggingface
- 兴趣命中：agent
- 作者：Hongzhan Lin, Shidong Cao, Ziyang Luo, Wenhao Chai, Mong-Li Lee, Wynne Hsu
- 链接：[arXiv](https://arxiv.org/abs/2610.07753) · [PDF](https://arxiv.org/pdf/2610.07753) · [HF](https://huggingface.co/papers/2610.07753)

Tool-using agents make consequential changes to external state, yet correct outcomes do not guarantee that their actions were supported by evidence established beforehand. We study where this evidence-to-action chain breaks as agents move from deciding whether to act to executing single actions and dependent workflows. Across ten model-harness configurations, strong static action assessment can coexist with much…

## 63. Periscope: Extending Frozen Language Models Beyond Their Context Window

- 分数：16.0  ·  HF 赞：8  ·  来源：huggingface
- 兴趣命中：context window, language model
- 作者：Mohamed Eltahir, Anas Obayd, Raed Rashid, Abdulrahman Alghamdi, Abdulrahman Mousa, Abdallah Ahmed, Tanveer Hussain, Naeemullah Khan
- 链接：[arXiv](https://arxiv.org/abs/2610.04047) · [PDF](https://arxiv.org/pdf/2610.04047) · [HF](https://huggingface.co/papers/2610.04047)

A language model reads long text in one quadratic forward pass, stops at the context window, and loses accuracy with length before reaching it. We ask whether the read can be factorized when deciding over a finite set: which document is relevant, which option is supported, which passage is the evidence. Periscope, a training-free inference method, arranges the N chunks of a text on a K{times}K grid with…

## 64. The Numerical Linear Algebra of Large Language Models

- 分数：16.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：language model, large language, spec
- 作者：Abdelkader Baggag, Yousef Saad
- 链接：[arXiv](https://arxiv.org/abs/2610.04631) · [PDF](https://arxiv.org/pdf/2610.04631) · [HF](https://huggingface.co/papers/2610.04631)

Numerical Linear Algebra (NLA) has consistently played a vital role in advancing science by providing tools to solve fundamental problems encountered in scientific and engineering applications. Over the decades, it has continually evolved to meet the demands driven by successive waves of scientific discovery. For instance, during the 1950s and 1960s, substantial efforts were devoted to developing methods for solving…

## 65. Arm-wise Compositional Generalization in Dual-Arm Vision-Language-Action Models

- 分数：16.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：evaluation, benchmark, spec
- 作者：Zaibin Zhang, Binghao Ran, Yuhan Wu, Zhongbo Zhang, Yifan Wang, Junwei Jiang, Junlan Xiao, Wangcheng Shi, Li Kang, Yiran Qin, Zhenfei Yin, Lijun Wang, Huchuan Lu
- 链接：[arXiv](https://arxiv.org/abs/2610.06184) · [PDF](https://arxiv.org/pdf/2610.06184) · [HF](https://huggingface.co/papers/2610.06184)

Generalization in multi-arm collaboration can be studied as composing familiar atomic skills in new ways across arms. However, existing evaluations offer limited insight into which training and architectural choices support this ability under different coordination requirements. We introduce ACG-Bench, a benchmark for Arm-wise Compositional Generalization that provides a common testbed for studying skill…

## 66. World Action Learning via Interaction-Centric Spectral Latent Guidance

- 分数：15.5  ·  HF 赞：11  ·  来源：huggingface
- 兴趣命中：spec
- 作者：Zhiming Liu, Yikun Miao, Ying Chen, Hongrui Yin, Fangqi Zhu, Xiaoyi Pang, Quanxin Shou, Zhengyang Yan, Haodong Wang, Song Guo
- 链接：[arXiv](https://arxiv.org/abs/2610.03607) · [PDF](https://arxiv.org/pdf/2610.03607) · [HF](https://huggingface.co/papers/2610.03607)

Learning general-purpose robot policies requires large-scale real-world interaction data, yet collecting robot demonstrations remains expensive and difficult to scale. Egocentric videos offer abundant human interaction experience with task-relevant semantics for robotic manipulation, but direct transfer is challenging for two reasons: latent actions inferred from frame reconstruction can be dominated by nuisance…

## 67. RealtimeWAM: One-Step Asynchronous World Action Models

- 分数：15.5  ·  HF 赞：11  ·  来源：huggingface
- 兴趣命中：benchmark
- 作者：Chengtao Lv, Jinyang Du, Shuyi Feng, Yang Yong, Shiqiao Gu, Shunzi Yang, Ruihao Gong, Shen Ren, Tianwei Zhang, Wenya Wang
- 链接：[arXiv](https://arxiv.org/abs/2610.06617) · [PDF](https://arxiv.org/pdf/2610.06617) · [HF](https://huggingface.co/papers/2610.06617)

World Action Models (WAMs) incorporate visual representations from video generation backbones to guide action prediction. Recent efficient WAMs adopt Mixture-of-Transformers (MoT) architectures and compute video representations once for reuse by the action expert. However, intra-expert iteration (\ie, multi-step action denoising) and inter-expert waiting (\ie, sequential execution of the video and action experts)…

## 68. PluginRSI: Recursive Improvement of Agent Harnesses with Reusable Plugins

- 分数：15.5  ·  HF 赞：7  ·  来源：huggingface
- 兴趣命中：agent, language model
- 作者：Yaorui Shi, Yuchun Miao, Yuxin Chen, Jiayuan Zhang, Yueqing Sun, Xierui Song, Xiang Wang, An Zhang
- 链接：[arXiv](https://arxiv.org/abs/2609.32423) · [PDF](https://arxiv.org/pdf/2609.32423) · [HF](https://huggingface.co/papers/2609.32423)

The harness surrounding a language model is a central determinant of agent performance. Recent methods optimize harnesses by searching over complete programs, where individual mechanisms are difficult to isolate and reuse. We introduce PluginRSI, which represents a harness as a composition of atomized plugins and organizes harness evolution around these plugins. Individual plugins are improved independently and…

## 69. DEPICT: Scoring Text-to-Image Alignment by Answer Agreement

- 分数：15.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：evaluation, benchmark, language model
- 作者：Vasco Ramos, Sandra Godinho Silva, Joao Magalhaes, Ricardo Rei, Pedro Henrique Martins
- 链接：[arXiv](https://arxiv.org/abs/2610.03617) · [PDF](https://arxiv.org/pdf/2610.03617) · [HF](https://huggingface.co/papers/2610.03617)

Image-text alignment is a core problem in computer vision with applications in caption evaluation, hallucination detection, data curation, and the benchmarking of text-to-image (T2I) generators. As T2I models improve, benchmarking has become demanding, requiring metrics capable of finding a series of issues like missing objects, swapped attributes, miscounts, and ignored negations. Recent work addresses this by…

## 70. GeoSET: Generalist Foundation Model for SAR-to-EO Image Translation

- 分数：15.0  ·  HF 赞：6  ·  来源：huggingface
- 兴趣命中：benchmark, spec
- 作者：Jeonghyeok Do, Munchurl Kim
- 链接：[arXiv](https://arxiv.org/abs/2609.37496) · [PDF](https://arxiv.org/pdf/2609.37496) · [HF](https://huggingface.co/papers/2609.37496)

Paired synthetic aperture radar (SAR) and electro-optical (EO) imagery is increasingly available across sensors, resolutions, and geographic regions. Yet existing SAR-to-EO image translation (SET) methods are typically trained on a single, limited-scale dataset, producing models specialized to particular sensing conditions. We introduce GeoSET, the first generalist model for SET, built around a single pretrained…

## 71. COSMI: COmpositional Synthesis of Multi-object Interactions

- 分数：15.0  ·  HF 赞：6  ·  来源：huggingface
- 兴趣命中：benchmark, language model
- 作者：Daniel Eskandar, Ilya A. Petrov, Gerard Pons-Moll
- 链接：[arXiv](https://arxiv.org/abs/2610.03252) · [PDF](https://arxiv.org/pdf/2610.03252) · [HF](https://huggingface.co/papers/2610.03252)

Generative models of human-object interaction are bounded by the data that exists: everyday activities involve several objects, but most captured datasets record one at a time, as multi-object capture is combinatorially expensive. Our observation is that interactions are local, so single-object captures already contain the parts of multi-object activities. We compose them: contact-consistent clips of single…

## 72. EmbodiedSmith: Scaling Embodied Data through Recursive Self-Improvement Flywheel in Simulation

- 分数：15.0  ·  HF 赞：6  ·  来源：huggingface
- 兴趣命中：agent, evaluation
- 作者：Yikai Qin, Yifei Deng, Mingjian Liang, Wenxuan Song, Zepeng Lin, Zhiyi Jiang, Jiajun Fu, Qiao Sun, Huashuo Lei, Xicheng Gong, Jiayi Chen, Han Zhao, Shuanghao Bai, Pengxiang Ding, Pengwei Wang, Haoang Li
- 链接：[arXiv](https://arxiv.org/abs/2610.07969) · [PDF](https://arxiv.org/pdf/2610.07969) · [HF](https://huggingface.co/papers/2610.07969)

Scaling robotic foundation models requires diverse training data and reliable evaluation environments. Simulation offers a scalable solution, yet existing generation pipelines remain constrained by predefined assets and skills, a disconnect between scene generation and task generation, and limited support for complex embodiments and physics. We introduce EmbodiedSmith, a framework for scalable embodied data…

## 73. PaLoRA: Paced Low-Rank Adaptation for Continual Learning

- 分数：14.5  ·  HF 赞：9  ·  来源：huggingface
- 兴趣命中：benchmark
- 作者：Yuxuan Li, Fanhu Zeng, Hao Tang
- 链接：[arXiv](https://arxiv.org/abs/2610.04226) · [PDF](https://arxiv.org/pdf/2610.04226) · [HF](https://huggingface.co/papers/2610.04226)

LoRA-based continual learning methods mitigate catastrophic forgetting through various mechanisms, yet nearly all complement these with small learning rates as a heuristic to restrict gradient scaling magnitude. Such fixed heuristics lack theoretical guidance on how the strength of this restriction should evolve as tasks accumulate. We reveal that even under directional constraints such as nullspace projection,…

## 74. Labels Override Definitions in Jev-Style Typed Decision Models

- 分数：14.5  ·  HF 赞：5  ·  来源：huggingface
- 兴趣命中：language model, spec
- 作者：Seyedarmin Azizi, Erfan Baghaei Potraghloo, Massoud Pedram
- 链接：[arXiv](https://arxiv.org/abs/2610.02586) · [PDF](https://arxiv.org/pdf/2610.02586) · [HF](https://huggingface.co/papers/2610.02586)

A typed decision model answers a fixed question about an input by returning a probability for each of several caller-defined options. Each option carries a short label and a written definition, which is where a developer states the rule the model should apply. Jev introduced this interface for routing, moderation and triage, open implementations followed, and the same operation occurs whenever a language model is…

## 75. FairRSFM: A Biome-Aware Benchmark and Debiasing Framework for Remote Sensing Foundation Models

- 分数：14.5  ·  HF 赞：5  ·  来源：huggingface
- 兴趣命中：evaluation, benchmark
- 作者：Md Aminur Hossain, Omkumar Vaghasiya, Rajeev Ranjan Dwivedi, Vinod Kurmi, Biplab Banerjee
- 链接：[arXiv](https://arxiv.org/abs/2610.05790) · [PDF](https://arxiv.org/pdf/2610.05790) · [HF](https://huggingface.co/papers/2610.05790)

Remote sensing foundation models (RSFMs) are commonly evaluated using aggregate metrics, which can hide systematic performance disparities across ecological regions. We introduce FairRSFM, a biome-aware benchmark for evaluating ecological group robustness in RSFMs. FairRSFM maps georeferenced samples from 14 terrestrial biome classes into six ecologically meaningful macro-groups and evaluates models under a unified…

## 76. DistScene: Object-to-Scene Distillation for 3D Scene Generation

- 分数：14.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：evaluation, benchmark, spec
- 作者：Kunming Luo, Hongyu Yan, Ken Deng, Chengcheng Zhou, Tianyu Liu, Haipeng Li, Haibin Huang, Xuelong Li, Ping Tan
- 链接：[arXiv](https://arxiv.org/abs/2610.06960) · [PDF](https://arxiv.org/pdf/2610.06960) · [HF](https://huggingface.co/papers/2610.06960)

We present DistScene, a framework for single-image compositional 3D scene generation by jointly modeling the environment and individual objects. Unlike existing methods that represent scenes primarily as collections of objects, we model the environment as an explicit scene component to provide geometric context for object placement. Specifically, we introduce Scene-Frame Generation, which jointly generates separate…

## 77. AdvSim2Real : Training Web Agents Against Adaptive Prompt Injection in a Web World Model

- 分数：14.5  ·  HF 赞：1  ·  来源：huggingface + arxiv
- 兴趣命中：agent
- 作者：Sarim Hashmi, Mukul Ranjan, Kshitij Mishra, Mikhail Kuznetsov, Praneeth Vepakomma, Nils Lukas
- 链接：[arXiv](https://arxiv.org/abs/2610.08773) · [PDF](https://arxiv.org/pdf/2610.08773) · [HF](https://huggingface.co/papers/2610.08773)

Web agents complete user requests by reading and acting on pages that third parties write, so an instruction planted on a page can redirect the agent away from the user's goal. The agent cannot simply ignore the page, because the page also holds the values and controls the task requires. Current defenses fine-tune the agent on injections fixed before training, and attackers that adapt to the trained model bypass…

## 78. What Gradients Add to Text Leakage in Split Language Models, Counted per Token and per Document

- 分数：14.0  ·  HF 赞：8  ·  来源：huggingface
- 兴趣命中：language model
- 作者：Georgios Politis, Evangelos Pappas
- 链接：[arXiv](https://arxiv.org/abs/2610.04128) · [PDF](https://arxiv.org/pdf/2610.04128) · [HF](https://huggingface.co/papers/2610.04128)

Split learning lets a client train a language model on a server without sending its text. The client runs the first layers itself and sends the server only their output, a vector of numbers for each token. During training, the server sends gradients back. We show that an observer at the split can rebuild most of the client's text from this traffic, and we measure how much the gradients help. On GPT-2, an attacker…

## 79. Training Numerical Intelligence via Auto-Diagnosis and Skill Discovery

- 分数：14.0  ·  HF 赞：8  ·  来源：huggingface
- 兴趣命中：agent
- 作者：Peter Chen, Wotao Yin
- 链接：[arXiv](https://arxiv.org/abs/2610.03872) · [PDF](https://arxiv.org/pdf/2610.03872) · [HF](https://huggingface.co/papers/2610.03872)

AI agents are becoming increasingly capable of generating scientific code, but generating code is not the same as improving the algorithms behind it. For numerical solvers, execution feedback can expose poor performance, but rarely reveals its underlying cause and how to address it. We introduce Auto-Diagnosis and Skill Discovery (ADSD), a framework that links numerical diagnosis to reusable solver self-improvement.…

## 80. LLM-as-Jev: LLMs Are Already Jev-Style Decision Models -- When and How to Fine-Tune Them

- 分数：14.0  ·  HF 赞：8  ·  来源：huggingface
- 兴趣命中：spec
- 作者：Yinheng Li, Justin Wagle
- 链接：[arXiv](https://arxiv.org/abs/2610.02076) · [PDF](https://arxiv.org/pdf/2610.02076) · [HF](https://huggingface.co/papers/2610.02076)

Jev-style decision models return categorical probability distributions over predefined options without generating free-form text, enabling software systems to act on their outputs directly. In this work, we investigate the extent to which general-purpose LLMs already possess this capability out of the box, and when fine-tuning is actually necessary. We present LLM-as-Jev, an architecture-preserving framework that…

## 81. Adaptive Fused Prior Transfer for Controllable Generative Image Compression

- 分数：14.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：benchmark, spec
- 作者：Yifei Pei, Ying Liu, Nam Ling
- 链接：[arXiv](https://arxiv.org/abs/2605.16817) · [PDF](https://arxiv.org/pdf/2605.16817) · [HF](https://huggingface.co/papers/2605.16817)

Learned image compression achieves competitive rate-distortion performance, but very-low-bitrate reconstruction remains challenging because the transmitted representation cannot preserve fine textures and local structures. Perceptual and generative codecs synthesize missing details using reconstruction priors, while controllable codecs allow one model to cover different bitrate and reconstruction preferences.…

## 82. MEA: A Reward-Driven Multi-Agent System for Faithful Model Explanations

- 分数：14.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：agent, reasoning
- 作者：Yuyang Cheng, Raghav Kaushik Ravi, Srivarshinee Sridhar, Sriparna Saha, Akash Ghosh, Chirag Agarwal
- 链接：[arXiv](https://arxiv.org/abs/2610.02480) · [PDF](https://arxiv.org/pdf/2610.02480) · [HF](https://huggingface.co/papers/2610.02480)

Recent years have seen the employment of a plethora of machine learning (ML) models in high-stakes domains, but they remain largely opaque to the practitioners who act on their predictions. While post-hoc explanation methods offer a lens into this model behavior, wielding them effectively demands expertise most domain experts lack: navigating high-dimensional outputs, selecting the best explanations, and…

## 83. Agentic discovery of blood biomarker from distilled private health records

- 分数：14.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：agent, language model
- 作者：Seffi Cohen, Liat Antwarg Friedman, Amir Anisman, Ruth Johnson, Michelle M. Li, Ayush Noori, Ben Reis, Ran Balicer, Noa Dagan, Marinka Zitnik
- 链接：[arXiv](https://arxiv.org/abs/2610.04749) · [PDF](https://arxiv.org/pdf/2610.04749) · [HF](https://huggingface.co/papers/2610.04749)

Routine complete blood counts (CBCs) could yield new biomarkers, but the private records needed to evaluate candidates cannot be shared with frontier language model agents that excel at discovery. We distilled the evidence held in the Clalit Health Services panel of over 5.4 million patients into a released scoring tool: for each of 13 immune-mediated diseases, a graph attention network was trained inside the data…

## 84. Understanding and Enhancing Backdoor Persistency in LLM Agent Post-Training

- 分数：14.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：agent, reinforcement learning
- 作者：Qiusi Zhan, Nian Lyu, Stephanie Ding, Arnav Mehta, Xander Davies, Daniel Kang
- 链接：[arXiv](https://arxiv.org/abs/2610.07510) · [PDF](https://arxiv.org/pdf/2610.07510) · [HF](https://huggingface.co/papers/2610.07510)

Developers can build LLM agents by adapting third-party models through benign post-training. We study a supply-chain threat in which an attacker supplies a model with a backdoor: hidden behavior that produces malicious outputs when a particular input pattern appears. Focusing on software-engineering agents, we ask whether such backdoors survive the developer's supervised fine-tuning (SFT) and subsequent task-level…

## 85. Sharpen Without Search: On-Policy Distillation of Sequence-Level Power Distribution

- 分数：14.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：reasoning, language model
- 作者：Erfan Baghaei Potraghloo, Seyedarmin Azizi, Arya Fayyazi, Saeid Shokoufa, Mehdi Kamal, Souvik Kundu, Massoud Pedram
- 链接：[arXiv](https://arxiv.org/abs/2610.06804) · [PDF](https://arxiv.org/pdf/2610.06804) · [HF](https://huggingface.co/papers/2610.06804)

A language model can give a correct answer more probability than any single incorrect answer and still usually sample an incorrect one, because the incorrect answers together hold more probability. The power distribution raises each complete answer's probability to a power above one and renormalizes, shifting probability toward answers the model finds most likely (sharpening). Sampling from it improves reasoning…

## 86. The AI Theorist reveals excitonic structure in α-RuCl_3

- 分数：13.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：agent, spec
- 作者：Hongjian Zhou, Xianfan Nie, Sean Wu, Tarun Patel, Jinge Wu, Andrew Liu, Adam Wei Tsen, David A. Clifton
- 链接：[arXiv](https://arxiv.org/abs/2610.02417) · [PDF](https://arxiv.org/pdf/2610.02417) · [HF](https://huggingface.co/papers/2610.02417)

Advances in experimental instrumentation and automation generate increasingly rich datasets, but turning experimental observations into microscopic understanding remains a bottleneck in scientific discovery. To accelerate this process, we introduce AI Theorist, a system of artificial intelligence (AI) agents for autonomous discovery of physical models through hypothesis generation, first-principles calculations and…

## 87. Collaborative Personalized Preference Alignment for LLMs under Data Deficiency

- 分数：13.0  ·  HF 赞：6  ·  来源：huggingface
- 兴趣命中：spec
- 作者：Liyan Yang, Yige Yuan, Zhiqin Yang
- 链接：[arXiv](https://arxiv.org/abs/2610.05898) · [PDF](https://arxiv.org/pdf/2610.05898) · [HF](https://huggingface.co/papers/2610.05898)

Real-world users often exhibit highly heterogeneous preferences over multiple objectives for LLM responses. A lightweight aligner can tailor these responses to individual preferences, but scarce user-specific feedback makes personalized training difficult. Learning shared initializations across users can support few-shot adaptation. However, heterogeneous preferences and competing objectives cause gradient conflicts…

## 88. Learning to Learn a Language

- 分数：13.0  ·  HF 赞：6  ·  来源：huggingface
- 兴趣命中：language model
- 作者：Lennart Carstens-Behrens, Holger Fröhlich
- 链接：[arXiv](https://arxiv.org/abs/2610.05879) · [PDF](https://arxiv.org/pdf/2610.05879) · [HF](https://huggingface.co/papers/2610.05879)

We present the Prior-Fitted Language Model (PFLM), a 300M-parameter byte-level transformer pretrained only on samples from a synthetic non-linguistic prior. Given a prefix of real text, it learns to predict the language in context with frozen weights, having never seen a word of any real language. Every training sequence is generated by a recurrent structural causal model drawn fresh from a distribution over such…

## 89. Personal-Agent Mediated Recommendation with Cross-Platform User History

- 分数：13.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：agent, benchmark
- 作者：Yu Xia, Jiangfan Zhang, Jun Xiao, Julian McAuley, Xiangjun Fan
- 链接：[arXiv](https://arxiv.org/abs/2610.07588) · [PDF](https://arxiv.org/pdf/2610.07588) · [HF](https://huggingface.co/papers/2610.07588)

Modern recommendation is shifting from platform-centric personalization toward user-governed personalization, where a personal LLM agent can act on the user's behalf across services. We formalize this emerging paradigm as Personal-Agent Mediated Recommendation: a platform recommender ranks a candidate set using platform-local information, and a personal agent uses user-authorized cross-platform history to mediate…

## 90. HiPLEX: Hierarchical Policy Factorization for Full Duplex Speech Language Models

- 分数：13.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：reinforcement learning, language model
- 作者：Kyudan Jung, Hyunsin Park, Yoonhyung Lee, Jinhwan Park, Jinhyeok Yang, KiHyun Nam, Jaegul Choo, Jinkyu Lee
- 链接：[arXiv](https://arxiv.org/abs/2610.07727) · [PDF](https://arxiv.org/pdf/2610.07727) · [HF](https://huggingface.co/papers/2610.07727)

As human--AI interactions become more conversational, full-duplex speech language models capable of natural real-time dialogue are growing in importance. Beyond generating appropriate responses, these models must coordinate turn-taking, backchanneling, and floor management in real time. Reinforcement learning (RL) provides a way to refine these behaviors through direct feedback on interaction outcomes. However,…

## 91. How to Loop MoE: Flatten the Experts, Untie the Attention

- 分数：12.5  ·  HF 赞：9  ·  来源：huggingface
- 兴趣命中：-
- 作者：Shouren Wang, Chuang Ma, Mohsen Hariri, Debargha Ganguly, Wang Yang, Xiaoqing Tong, Qianying Liu, Xiaotian Han, Vipin Chaudhary
- 链接：[arXiv](https://arxiv.org/abs/2609.35751) · [PDF](https://arxiv.org/pdf/2609.35751) · [HF](https://huggingface.co/papers/2609.35751)

Looped Transformers reuse one block of layers several times: by spending extra computation they push a model of fixed size further, and so use its parameters more fully; while sparse mixture-of-experts (MoE) models activate only a few of many experts for each token. Looped MoE bridges these two design philosophies and gives MoE models new potential for better expert usage, but it raises a question: how to loop a…

## 92. LiFT: Loop Flow Transformers

- 分数：12.5  ·  HF 赞：9  ·  来源：huggingface
- 兴趣命中：-
- 作者：Mohammad Mahdi Derakhshani, Pedro M. P. Curvo, Gertjan J. Burghouts, Jan-Willem van de Meent, Cees G. M. Snoek
- 链接：[arXiv](https://arxiv.org/abs/2610.05538) · [PDF](https://arxiv.org/pdf/2610.05538) · [HF](https://huggingface.co/papers/2610.05538)

We introduce Loop Flow Transformers (LiFT), a family of looped generative models that scales computation by repeatedly applying a shared Diffusion Transformer (DiT) core, with only light changes to the standard architecture. Rather than asking every recurrent step for the final prediction, LiFT trains each step with a single regression target: a point on a straight path from the model's initial estimate to the…

## 93. Learning Steadily: Accumulating Relative Point Margin Scores for Face Image Quality Assessment

- 分数：12.5  ·  HF 赞：5  ·  来源：huggingface
- 兴趣命中：benchmark
- 作者：Guray Ozgur, Tahar Chettaoui, Eduarda Caldeira, Marco Huber, Jan Niklas Kolf, Naser Damer, Fadi Boutros
- 链接：[arXiv](https://arxiv.org/abs/2609.31662) · [PDF](https://arxiv.org/pdf/2609.31662) · [HF](https://huggingface.co/papers/2609.31662)

Face Image Quality Assessment determines the suitability of captured face images for automated face recognition (FR), a critical capability for reliable biometric systems. Existing state-of-the-art FR-integrated FIQA methods suffer from temporal instability: as the feature space evolves during training, single-epoch quality estimates fluctuate, creating a moving target that undermines reliable quality prediction. We…

## 94. Learning Latent Protein Languages for Autoregressive Generation

- 分数：12.5  ·  HF 赞：5  ·  来源：huggingface
- 兴趣命中：coding
- 作者：Mahdi Pourmirzaei, Farzaneh Esmaili, Amir Ziashahabi, Mohammadreza Pourmirzaei, Dong Xu
- 链接：[arXiv](https://arxiv.org/abs/2610.03978) · [PDF](https://arxiv.org/pdf/2610.03978) · [HF](https://huggingface.co/papers/2610.03978)

Autoregressive transformers remain comparatively weak for protein sequence and structure generation. We study the role of target representation: amino acid tokens encode residue identities without explicit contextual semantics, while backbone coordinates require a discrete representation in our framework. We introduce two learned latent protein languages. Protein Latent Language (PLL) maps sequences to a 4,096-state…

## 95. Closing the Context Gap: Activation Alignment for Tabular In-Context Learning

- 分数：12.5  ·  HF 赞：5  ·  来源：huggingface
- 兴趣命中：benchmark
- 作者：Yoel Zeldes
- 链接：[arXiv](https://arxiv.org/abs/2610.06679) · [PDF](https://arxiv.org/pdf/2610.06679) · [HF](https://huggingface.co/papers/2610.06679)

Tabular foundation models perform in-context learning (ICL) by conditioning predictions on labeled training examples provided as context. Unlike traditional models that separate training from inference, these models must process all training examples in every forward pass, making each prediction expensive. Restricting the number of training examples reduces this cost but substantially degrades performance. Instead…

## 96. Building Rome from a Single Image

- 分数：12.5  ·  HF 赞：1  ·  来源：huggingface + arxiv
- 兴趣命中：-
- 作者：Jiraphon Yenphraphai, Fang Li, Tianshuo Xu, Depu Meng, Quentin Herau, Yihan Hu, Raymond A. Yeh, Wei Zhan
- 链接：[arXiv](https://arxiv.org/abs/2610.08790) · [PDF](https://arxiv.org/pdf/2610.08790) · [HF](https://huggingface.co/papers/2610.08790)

Single-image scene generation aims to produce a complete 3D scene mesh from a single image, including surfaces the camera did not observe. While pretrained 3D object generators encode a strong shape prior, they are mainly designed for isolated objects in a fixed canonical volume and focus mostly on indoor scenes, since diverse 3D data for outdoor scenes are quite limited. In this work, we present a method that…

## 97. Prism: Dynamic Sparse Attention for Native 2K Joint Video-Audio Generation Model Training

- 分数：12.0  ·  HF 赞：8  ·  来源：huggingface
- 兴趣命中：-
- 作者：Shuyuan Tu, Qi Tian, Yinming Huang, Yue Wu, Xintong Han, Kaihang Pan, Weijie Kong, Jiangfeng Xiong, Jian-Wei Zhang, Zuxuan Wu, Yu-Gang Jiang
- 链接：[arXiv](https://arxiv.org/abs/2610.05416) · [PDF](https://arxiv.org/pdf/2610.05416) · [HF](https://huggingface.co/papers/2610.05416)

Natively training joint video-audio generation models at higher resolutions empowers them to learn richer visual details and sharper motion dynamics. However, full attention incurs quadratic cost and, as resolution increases, spreads attention over increasingly redundant tokens, diluting learning signals for informative content and disrupting pretrained priors. Existing sparse attention methods either target…

## 98. GeoCR: Learning a Generalist Cloud Removal Prior from Heterogeneous Observations

- 分数：12.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：spec
- 作者：Jeonghyeok Do, Munchurl Kim
- 链接：[arXiv](https://arxiv.org/abs/2609.32510) · [PDF](https://arxiv.org/pdf/2609.32510) · [HF](https://huggingface.co/papers/2609.32510)

Cloud removal methods are typically specialized to individual datasets and input configurations, limiting reuse across sensors, spectral bands, and observation settings. We introduce GeoCR, a generalist model that unifies RGB-only-based CR and multispectral-based CR from single- or multi-temporal cloudy observations, with optional SAR guidance, within a single network. To accommodate different spectral and sensing…

## 99. iADD: Improving Alignment and Diversity in Diffusion Policy Optimization

- 分数：12.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：reinforcement learning
- 作者：Ashok Prasad Neupane, Saugat Adhikari, Pramish Paudel, Ajad Chhatkuli, Danda Pani Paudel
- 链接：[arXiv](https://arxiv.org/abs/2610.01789) · [PDF](https://arxiv.org/pdf/2610.01789) · [HF](https://huggingface.co/papers/2610.01789)

Reinforcement learning based post training of diffusion models, such as Denoising Diffusion Policy Optimization (DDPO), optimizes a reverse diffusion process under a reward function. However, current approaches to reward optimizations do so at the cost of diversity and quality. In this paper, we provide better tradeoffs through careful theoretical considerations and method design. We analyze the theoretical…

## 100. CurveCodec 2: Skeleton-agnostic animation compression with a learned entropy model

- 分数：12.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：spec
- 作者：Mingyi Shi, Huancheng Lin, Xuelin Chen, Taku Komura
- 链接：[arXiv](https://arxiv.org/abs/2610.04211) · [PDF](https://arxiv.org/pdf/2610.04211) · [HF](https://huggingface.co/papers/2610.04211)

Skeletal motion is stored as every joint's transform at every frame, yet most of it is implied by the body rather than by what the motion is about. Compression is one way to ask what a motion must still say once the body is known, and a production codec must answer it for any skeleton with a stated error bound. Our earlier codec, CurveCodec, matched the mean error of ACL, the production library of modern game…

## 101. Adapting prior-data fitted networks for tabular anomaly detection

- 分数：12.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：benchmark
- 作者：Maximilian Bershtman, Niv Cohen
- 链接：[arXiv](https://arxiv.org/abs/2610.06693) · [PDF](https://arxiv.org/pdf/2610.06693) · [HF](https://huggingface.co/papers/2610.06693)

While deep features have transformed anomaly detection in images and video, their impact on tabular data has been less substantial, partly due to the limited availability of strong deep representations. Recently, prior-data fitted networks (PFNs) have emerged as a promising source of such representations for tabular data. In this work, we investigate how PFN representations can be adapted and leveraged for anomaly…

## 102. MEND: RL For Flow Models via Proximal Velocity Matching

- 分数：12.0  ·  HF 赞：0  ·  来源：huggingface
- 兴趣命中：reinforcement learning, spec
- 作者：Shreshth Saini, Neil Birkbeck, Yilin Wang, Balu Adsumilli, Alan C. Bovik
- 链接：[arXiv](https://arxiv.org/abs/2610.05954) · [PDF](https://arxiv.org/pdf/2610.05954) · [HF](https://huggingface.co/papers/2610.05954)

Reward post-training of flow models either reweights the model's own samples under a KL penalty or a frozen reference, often for thousands of updates, or backpropagates the reward and moves every sample without checking that the move is worth its size. We introduce MEND, a reinforcement learning method built on proximal velocity matching. MEND caps rewards within each prompt group, so samples that already score well…

## 103. DiVeR: Decision-Critical Verifier Learning for VLA Test-Time Scaling

- 分数：11.5  ·  HF 赞：7  ·  来源：huggingface
- 兴趣命中：-
- 作者：Seongheon Park, Heecheol Kim, Shulin Tian, Lilika Makabe, Namiko Saito, Katsushi Ikeuchi, Sharon Li, Yasuyuki Matsushita
- 链接：[arXiv](https://arxiv.org/abs/2610.04933) · [PDF](https://arxiv.org/pdf/2610.04933) · [HF](https://huggingface.co/papers/2610.04933)

Scaling robot data and model capacity has improved Vision-Language-Action (VLA) policies, but further progress is constrained by the high cost of robotic data. Verifier-guided test-time scaling offers an efficient alternative by sampling multiple action candidates and selecting the one most likely to lead to task success at inference time. Existing classification-based verifiers learn from trajectory-level outcomes…

## 104. Empirical Variational Autoencoder

- 分数：11.5  ·  HF 赞：7  ·  来源：huggingface
- 兴趣命中：-
- 作者：Kaede Shiohara
- 链接：[arXiv](https://arxiv.org/abs/2610.06545) · [PDF](https://arxiv.org/pdf/2610.06545) · [HF](https://huggingface.co/papers/2610.06545)

We present Empirical Variational Autoencoder, a general generative framework for continuous-valued (i.e., non-vector-quantized) sequences. EVA is based on the evidence lower bound of the Variational Autoencoder (VAE) but learns autoregressive latent priors empirically from training data, which can be implemented only by an additional single linear layer on top of VAEs. By replacing the conventional standard-Gaussian…

## 105. SoK: Semantic Decision Engines in Network Control Loops

- 分数：11.0  ·  HF 赞：6  ·  来源：huggingface
- 兴趣命中：-
- 作者：Delong Li, Chen Li, Xu Wang, Haochen Gong, Rui Lang, Guangsheng Yu
- 链接：[arXiv](https://arxiv.org/abs/2610.06425) · [PDF](https://arxiv.org/pdf/2610.06425) · [HF](https://huggingface.co/papers/2610.06425)

A semantic decision engine such as Jev can return a valid answer and still miss a network deadline, select an infeasible action or leave the service unverified. We systematize 139 paper families by decision interface, execution path and check ownership. Fifty families claim that their engine fits a control loop or time budget, but only four support the claim with matched measurement. Across all 139, four report…

## 106. Attacca: Goal-Directed Control under State Continuity for Long-Horizon Embodied Agents

- 分数：11.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：agent
- 作者：Gyusik Seo, Jaehong Yoon
- 链接：[arXiv](https://arxiv.org/abs/2610.07785) · [PDF](https://arxiv.org/pdf/2610.07785) · [HF](https://huggingface.co/papers/2610.07785)

A central capability of embodied agents is to accomplish complex objectives through sequences of interdependent tasks. Yet existing visual goal-conditioned policies underlying these agents are typically evaluated on isolated interactions where the target is already visible, and thus do not capture the conditions that arise during continuous long-horizon task execution. In such settings, each task begins from the…

## 107. MM-ABC: Towards Generalist Mobile Manipulation via Seeing, Coordinating and Imagining

- 分数：10.5  ·  HF 赞：5  ·  来源：huggingface
- 兴趣命中：-
- 作者：Qiwei Liang, Guangyu Chen, Shaolong Zhu, Zikuan Xiao, Jinxuan Lu, Yifan Xie, Renjing Xu, Wenbo Ding, Tianxing Chen
- 链接：[arXiv](https://arxiv.org/abs/2609.35652) · [PDF](https://arxiv.org/pdf/2609.35652) · [HF](https://huggingface.co/papers/2609.35652)

Mobile manipulation extends robot interaction beyond a fixed kinematic workspace by making the reachable region itself controllable. This flexibility introduces two central challenges: spatially grounded perception under continuous ego-motion and coordinated control of heterogeneous arm and base actions. Existing approaches strengthen geometry through explicit 3D representations or predictive world models, and often…

## 108. UnAct: Gradient-Free Unlearning via Targeted Activation Intervention

- 分数：10.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：-
- 作者：Saeed Abdul Muizz, Aayat Rafiq, Iqra Altaf Gillani, Janibul Bashir
- 链接：[arXiv](https://arxiv.org/abs/2610.04426) · [PDF](https://arxiv.org/pdf/2610.04426) · [HF](https://huggingface.co/papers/2610.04426)

Machine unlearning seeks to remove the influence of designated training data from a trained model without retraining from scratch. Retrain-free methods such as Selective Synaptic Dampening (SSD) and its label-free variant LFSSD avoid full retraining but still require backpropagation and parameter importance computed over the entire dataset. We ask: what happens when a deletion request arrives with only a few images…

## 109. InterMimicGen: Scaling Humanoid Loco-Manipulation through Self-Evolving Motion Imitation

- 分数：10.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：-
- 作者：Yucheng Zhang, Sirui Xu, Jinhong Li, Liuyu Bian, Anatulya Nandi, Derek Zhang, Xiangchen Liu, Xueting Li, Umar Iqbal, Yu-Xiong Wang, Liang-Yan Gui
- 链接：[arXiv](https://arxiv.org/abs/2610.06850) · [PDF](https://arxiv.org/pdf/2610.06850) · [HF](https://huggingface.co/papers/2610.06850)

Captured human-object interactions provide rich supervision for humanoid loco-manipulation, but they are sparse, heterogeneous, and not directly executable by robots. We introduce InterMimicGen, a self-evolving motion-imitation framework in which robot motion data and a tracking policy improve each other. First, we consolidate motion-captured human-object interaction datasets and retarget them into humanoid robot…

## 110. The Labeling Problem in Hallucination Detection Benchmarks: An Empirical Evaluation

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, language model, large language, spec
- 作者：Jorma Valjakka, Juhani Kivimäki, Juha Mylläri, Jukka K. Nurminen
- 链接：[arXiv](https://arxiv.org/abs/2610.08026) · [PDF](https://arxiv.org/pdf/2610.08026) · [HF](https://huggingface.co/papers/2610.08026)

In recent years, several methods for detecting when large language models (LLMs) hallucinate have been developed. These methods are often benchmarked with open-domain question answering (QA) datasets containing questions and corresponding short reference answers. First, an LLM is used to generate answers to questions within the QA dataset. Then, some automated labeling strategy is used to label these answers as…

## 111. DAEDALUS: Bootstrapping Agent Memory from Self-Generated Tasks

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, memory, benchmark, spec
- 作者：Antoine Edy, Max Conti, Victor Xing, Marc-Antoine Allard, Nawfal Benhamdane, Gautier Viaud
- 链接：[arXiv](https://arxiv.org/abs/2610.08048) · [PDF](https://arxiv.org/pdf/2610.08048) · [HF](https://huggingface.co/papers/2610.08048)

LLM agents often lack the operational knowledge to act reliably in new environments, as they must discover specific tool behaviors or environment conventions on their own. Without memory of past attempts, they repeat the same mistakes across tasks, leading to more task failures and longer trajectories. To address this, agentic systems typically rely on human-written guidelines or on procedural memory built from…

## 112. Self-Retrospection Distillation: Turning Post-hoc Experiences into Prior Foresight

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reasoning, reinforcement learning, spec
- 作者：Haoxiang Zhang, Qinglin Chen, Hiroaki Hayashi, Zhuofeng Li, Siming Zhang, Jiaxin Zhang, Jixuan Chen, Fang Wu, Pan Lu, Silvio Savarese, Julian McAuley, Chien-Sheng Wu
- 链接：[arXiv](https://arxiv.org/abs/2610.08077) · [PDF](https://arxiv.org/pdf/2610.08077) · [HF](https://huggingface.co/papers/2610.08077)

Reinforcement learning with verifiable rewards (RLVR) turns agent experience into learning signals primarily through scalar outcome rewards after interaction. For group-relative objectives, however, this signal vanishes when all rollouts receive the same reward, even though their trajectories may reveal useful information about what the task requires and how the agent fails. We ask a complementary question: can…

## 113. Surviving the Router: Optimizing Skill Injections for Retrieval and Execution

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, evaluation, benchmark, retrieval
- 作者：Haneen Najjar, Luca Scionis, Haritz Puerto, Sahar Abdelnabi
- 链接：[arXiv](https://arxiv.org/abs/2610.08098) · [PDF](https://arxiv.org/pdf/2610.08098) · [HF](https://huggingface.co/papers/2610.08098)

AI agents increasingly rely on modular third-party "skills" that are dynamically selected by skill routers to execute complex tasks. While recent studies highlight the threat of prompt injections embedded in these skills, existing evaluations often assume settings where the malicious skill is already selected for execution. We show that this assumption can substantially overestimate attack success. In realistic…

## 114. Beyond Corrected Memory: Execution Consistency in Multi-Agent Systems

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, memory, benchmark, spec
- 作者：Zhe Yu, Zixuan Wang, Peidong Wang, Hehai Lin, Ruochen Zhao, Chengwei Qin
- 链接：[arXiv](https://arxiv.org/abs/2610.08101) · [PDF](https://arxiv.org/pdf/2610.08101) · [HF](https://huggingface.co/papers/2610.08101)

Shared memory coordinates agents' actions, but correct records do not establish that those actions satisfy task requirements. Memory governance and failure diagnosis regulate or inspect recorded information; they do not by themselves establish whether it is sufficient to judge task duties. We define execution consistency through duties governing state use, information handoffs, and final-state agreement, with…

## 115. DSV-Mem: Evaluating Multimodal Memory in Professional Workflows for MLLM Agents

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, memory, reasoning, evaluation, benchmark, spec
- 作者：Jike Zhong, Ritwick Chaudhry, Xuanbai Chen, Tianchen Zhao, Linghan Xu, Yifan Xing, Nishant Sankaran
- 链接：[arXiv](https://arxiv.org/abs/2610.08102) · [PDF](https://arxiv.org/pdf/2610.08102) · [HF](https://huggingface.co/papers/2610.08102)

Conversational MLLM agents are increasingly expected to assist in professional workflows, from AI research and engineering design to product management and business operations. Yet this capability remains underexplored: existing benchmarks largely focus on informal, everyday interactions and personal-life scenarios featuring photographic natural images, isolated static artifacts, and recall-oriented questions. In…

## 116. ChartBmkAgent: Harness-Governed Multi-Agent Construction of Chart QA Benchmarks from Sparse Error-Taxonomy Specifications

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reasoning, benchmark, language model, large language, spec
- 作者：Langxi Huang, Pingping Zhang, Lanyun Zhu, Chunyang Jiang, Jiawei Shao, Haocheng Yuan, Peilin Chen
- 链接：[arXiv](https://arxiv.org/abs/2610.08106) · [PDF](https://arxiv.org/pdf/2610.08106) · [HF](https://huggingface.co/papers/2610.08106)

Multimodal large language models (MLLMs) advance rapidly, while conventional benchmark development lags behind, delaying investigation of newly observed capability gaps. Such investigation requires an expressive task format and an on-demand construction process: information-rich charts make chart question answering (Chart QA) suitable for probing coupled perception and reasoning. Automated Chart QA construction is…

## 117. Enhancing Diffusion Language Models with Autoregressive Post-Training Weights

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, reinforcement learning, language model, coding
- 作者：Yiming Qin, Ke Wang, Amel Abdelraheem, Adam Hazimeh, Pascal Frossard
- 链接：[arXiv](https://arxiv.org/abs/2610.08108) · [PDF](https://arxiv.org/pdf/2610.08108) · [HF](https://huggingface.co/papers/2610.08108)

Diffusion language models (dLLMs) have emerged as a promising alternative to autoregressive (AR) language models, offering flexible token-update orders and parallel decoding. Recent dLLMs are often initialized from pretrained AR models before diffusion conversion in order to inherit their learned representations. After the conversion, however, they typically ignore the extensive post-training ecosystem of their AR…

## 118. Test-Time Agent Evolution for Long-Horizon Legal Reasoning

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, memory, reasoning, spec
- 作者：Haotian Chen, Shuaicheng Niu, Haocong Rao, Kaisong Song, Jun Lin, Lizhen Cui, Zhiqi Shen, Yonghui Xu
- 链接：[arXiv](https://arxiv.org/abs/2610.08138) · [PDF](https://arxiv.org/pdf/2610.08138) · [HF](https://huggingface.co/papers/2610.08138)

Legal intelligence aims to support reliable decision-making across long-horizon legal processes involving evolving case states and multiple roles. However, real-world legal deployment exhibits substantial case heterogeneity in facts, evidence, and procedural contexts, exposing the limitations of static agent strategies. Moreover, legal reasoning is inherently interdependent across roles and procedural stages, making…

## 119. Penalty-Framed No-Valid-Option MCQA: Analyzing LLM Abstention under Invalid Choices

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：language model, large language, spec, retrieval
- 作者：Jinhyeok Kim, Hye-Young Jung
- 链接：[arXiv](https://arxiv.org/abs/2610.08153) · [PDF](https://arxiv.org/pdf/2610.08153) · [HF](https://huggingface.co/papers/2610.08153)

Multiple-choice question answering (MCQA) is commonly used to evaluate large language models under the assumption that one of the provided options is correct, typically using answer-selection accuracy. However, in real deployments, users or retrieval systems may provide invalid option sets in which none of the listed choices is correct, and selecting one of them may incur downstream cost. We study this setting as…

## 120. Token-Efficient Multi-Agent Collaboration via System One-Guided Computational Division of Labor

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reasoning, benchmark, language model, large language, spec
- 作者：Zihan Zhou, Xinzhe Hu, Hanxu Yang, Liangjian Wen, Zhao Kang
- 链接：[arXiv](https://arxiv.org/abs/2610.08155) · [PDF](https://arxiv.org/pdf/2610.08155) · [HF](https://huggingface.co/papers/2610.08155)

Large language model (LLM)-based multi-agent systems (MAS) have become a promising paradigm for complex information-seeking and reasoning tasks by enabling collaborative problem solving among specialized agents. However, existing MAS frameworks tightly couple task reasoning with coordination operations, including task selection, role assignment, message routing, and context management. As interactions grow, using…
