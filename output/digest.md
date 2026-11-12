# 每日 AI 论文

生成时间：2026-11-12 07:11 UTC  ·  共 120 篇（已按 arXiv ID 去重）

来源：Hugging Face Daily Papers + arXiv（cs.AI / cs.LG / cs.CL / cs.CV）。
排序：HF 上榜、点赞、多源命中、兴趣词。兴趣词可在 `config.json` 改。

## 1. Tree-Ising: Repairing Language Models with Bit-Level Ising Edits

- 分数：40.0  ·  HF 赞：79  ·  来源：huggingface + arxiv
- 兴趣命中：agent, reasoning, evaluation, benchmark, language model, spec
- 作者：Hadi Salloum, Ammar Ali
- 链接：[arXiv](https://arxiv.org/abs/2611.14210) · [PDF](https://arxiv.org/pdf/2611.14210) · [HF](https://huggingface.co/papers/2611.14210)

Weight-space programming, introduced in recent MIT work by Takehi et al., enables a frontier LLM agent to read a network's weights and write a repair. Their GPT-6 Astra agent corrected the reasoning loops of Qwen3.5-0.8B without gradients, using 158 agent turns, 89.7 million tokens, and 50 forward-pass requests. Our method, Tree-Ising, casts this repair as a sparse discrete optimization problem over the model's own…

## 2. Don't Just Trust Your Memory: Evidence-Linked Memory Reduces Memory-Induced Degradation in LLM Agents

- 分数：40.0  ·  HF 赞：57  ·  来源：huggingface + arxiv
- 兴趣命中：agent, memory, benchmark, spec
- 作者：Yukyeong Lee, Yumin Choi, Jinheon Baek, Sung Ju Hwang
- 链接：[arXiv](https://arxiv.org/abs/2611.14320) · [PDF](https://arxiv.org/pdf/2611.14320) · [HF](https://huggingface.co/papers/2611.14320)

External memory enables LLM agents to improve from experience by distilling trajectories of past tasks into concise lessons for new tasks. However, memory can also lead to memory-induced degradation, where an agent fails on tasks it would solve without memory, often because it follows a lesson that is incorrect, or misapplies or misreads a valid one. This is because lessons are inferred from trajectories labeled…

## 3. Few-Step Streaming Video Generation via Condition Shifting

- 分数：36.0  ·  HF 赞：82  ·  来源：huggingface + arxiv
- 兴趣命中：memory, evaluation
- 作者：Deyuan Liu, Jungang Li, Kaiwen Zheng, Kai Jiang, Jintao Chen, Yaole Wang, Ming Lin, Tao Lin, Jianfei Chen, Jun Zhu, Jintao Zhang
- 链接：[arXiv](https://arxiv.org/abs/2611.14033) · [PDF](https://arxiv.org/pdf/2611.14033) · [HF](https://huggingface.co/papers/2611.14033)

Few-step sampling reduces the cost of streaming video generation. Distribution Matching Distillation (DMD) supervises few-step generators with a separate fake-score network, which adds training memory and computation and must track the evolving generator. We extend APEX to streaming video by using condition shifting to estimate the velocity field of the generated distribution within the generator. The original text…

## 4. MMDM: Measuring Massive Multitask Decision Making

- 分数：33.0  ·  HF 赞：26  ·  来源：huggingface + arxiv
- 兴趣命中：agent, long context, reasoning, evaluation, benchmark, spec, planning
- 作者：Junhao Shen, Qing Zong, Yue Guo, Zhanqiu Zhang, Yiwen Guo, Hong Cheng
- 链接：[arXiv](https://arxiv.org/abs/2611.14309) · [PDF](https://arxiv.org/pdf/2611.14309) · [HF](https://huggingface.co/papers/2611.14309)

System-1 Decision Models directly make structured probabilistic decisions over query-specified options given a state in a single forward pass, without autoregressively generating reasoning trajectories or textual responses. Recent evaluations cover diverse tasks but often rely on existing benchmarks, where prior exposure to test material can obscure generalization. Moreover, real-world decision making often involves…

## 5. dNaViT: Discrete Codes are General-Purpose Visual Representations

- 分数：32.5  ·  HF 赞：33  ·  来源：huggingface
- 兴趣命中：evaluation, benchmark, language model, coding, spec
- 作者：Xiaotong Li, Zhengrong Yue, Xu Huang, Jialv Zou, Minhao Jing, Wenhao Yan, Haodong Li, Hai Huang, Bo Zhao, Yan Feng, Peng Pei, Xunliang Cai
- 链接：[arXiv](https://arxiv.org/abs/2611.12426) · [PDF](https://arxiv.org/pdf/2611.12426) · [HF](https://huggingface.co/papers/2611.12426)

Discrete autoregressive modeling, notably through next-token prediction, has become a cornerstone of modern language models. Extending this paradigm to vision allows visual and language models to converge on a unified framework, thereby fostering shared methodology and infrastructure. This work investigates a central question: how far can a finite discrete vocabulary go in representing the richness of the visual…

## 6. World In-Context Learning for Agentic Robot Manipulation

- 分数：32.0  ·  HF 赞：66  ·  来源：huggingface
- 兴趣命中：agent, memory
- 作者：Heng Fang, Zehui Guo, Yuehan Zhang, Mingyang Du, Dingkang Liang, Xiang Bai
- 链接：[arXiv](https://arxiv.org/abs/2611.12885) · [PDF](https://arxiv.org/pdf/2611.12885) · [HF](https://huggingface.co/papers/2611.12885)

Trained action policies write manipulation skill into network weights, tying what is learned to the distribution it is learned from. In-context learning (ICL) avoids this coupling but has not matched trained policies, because a demonstration recorded in another scene carries no feedback from the world the robot currently faces. We observe that what an agent learns in context is semantic, recording task steps and…

## 7. One Table, Many Queries: Benchmarking Generalist Tabular Models Across Generation, Imputation, and Prediction

- 分数：28.0  ·  HF 赞：32  ·  来源：huggingface
- 兴趣命中：benchmark, spec
- 作者：Yuanrui Wang, Kaifang Li, Xuanyue Li, Ziyun Li, Yan Lu, Xingxuan Zhang, Peng Cui
- 链接：[arXiv](https://arxiv.org/abs/2611.13001) · [PDF](https://arxiv.org/pdf/2611.13001) · [HF](https://huggingface.co/papers/2611.13001)

Generation, imputation, and prediction query different aspects of the same tabular distribution, but are usually evaluated separately. This leaves unclear which capabilities they share, how their training objectives interact, and whether one model can perform all three well. We introduce the One Table Benchmark (), spanning 56 datasets, 46 registered methods, and 20 capability axes under aligned data splits and…

## 8. Scaling Mathematical Proof Supervision from Structured Textbooks

- 分数：28.0  ·  HF 赞：24  ·  来源：huggingface
- 兴趣命中：reasoning, evaluation, benchmark, language model
- 作者：Youqing Fang, Zhouqi Hua, Yinhao Tang, Yuzhe Gu, Lingkai Kong, Bin Liu, Weiming Zhang, Kai Chen, Yanan Sun, Wenwei Zhang
- 链接：[arXiv](https://arxiv.org/abs/2610.40394) · [PDF](https://arxiv.org/pdf/2610.40394) · [HF](https://huggingface.co/papers/2610.40394)

Mathematical supervision for language models is typically flattened into isolated problem-solution pairs, discarding the curricular organization and evidential structure of the original sources. We introduce TOME-Math (Textbook-Oriented Mathematical Evidence), a large-scale corpus that converts 2,118 textbooks spanning the core areas of university-level mathematics subjects into approximately 380K structured…

## 9. Embodied First Exam

- 分数：28.0  ·  HF 赞：24  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark, coding
- 作者：Kangrui Wang, Qineng Wang, Changhe Chen, Pingyue Zhang, Chi Gui, Feishi Wang, Canyu Chen, Wenli Xiao, Xiaoyu Huang, Tonghe Zhang, Linjie Li, Zihan Wang, Minyeong Kim, Yiyou Sun, Mingkai Deng, Jinyu Hou, Qi Zhu, Han Liu, Eric P. Xing, Huaxiu Yao, Zhiwen Fan, Yuejiang Liu, Dawn Song, Pieter Abbeel, Li Fei-Fei, Jiajun Wu, Yuke Zhu, Guanya Shi, Ruohan Zhang, Manling Li
- 链接：[arXiv](https://arxiv.org/abs/2611.12177) · [PDF](https://arxiv.org/pdf/2611.12177) · [HF](https://huggingface.co/papers/2611.12177)

Early successes on agentic robotics point to a potential paradigm shift toward using coding agents to control robots. Existing robotics benchmarks are built around visuomotor policy learning, leaving it open whether coding agents can reliably control diverse robots under physical-world constraints. We therefore introduce the Embodied First Exam, a unified, comprehensive, and agent-native evaluation framework where…

## 10. FINCOSMOS: An Open-World Evaluation Paradigm for Agents in Finance

- 分数：27.5  ·  HF 赞：23  ·  来源：huggingface
- 兴趣命中：agent, memory, evaluation, benchmark, coding, spec
- 作者：Yupeng Cao, Xueqing Peng, Lingfei Qian, Haohang Li, Yangyang Yu, Anke Xu, Wenbo Cao, Yan Wang, Yuechen Jiang, Yuyan Wang, Zhuohan Xie, Yankai Chen, Zehan Li, Jimin Huang, Xue Liu, Jian-Yun Nie, Sophia Ananiadou
- 链接：[arXiv](https://arxiv.org/abs/2611.07464) · [PDF](https://arxiv.org/pdf/2611.07464) · [HF](https://huggingface.co/papers/2611.07464)

Language agents increasingly work for users on the open Web, and finance is where trusting them is hardest. The data must come from the Web, the strategy lives in the user's head, and correctness depends on time, so an agent can fail silently: a strategy the user never asked for, unverified data, or a backtest that uses the future yields a report as convincing as a correct one. Existing benchmarks close the world…

## 11. MACaQ: Fast, Model Agnostic Calibrated Quantization for Low-Precision Weights and Activations

- 分数：23.0  ·  HF 赞：22  ·  来源：huggingface
- 兴趣命中：memory, spec
- 作者：Lorenz K. Muller, Philippe Bich, Chiara Boretti, Hyun-Min Chang, Jiawei Zhuang, Lukas Cavigelli
- 链接：[arXiv](https://arxiv.org/abs/2611.10649) · [PDF](https://arxiv.org/pdf/2611.10649) · [HF](https://huggingface.co/papers/2611.10649)

Weight-activation quantization can reduce the memory and compute cost of neural-network inference, but recent methods often require expensive optimization and architecture-specific propagation of basis transforms across layers. We introduce MACaQ, an MXFP4 W4A4 post-training quantization method that treats every linear layer independently. MACaQ applies a per-channel scale and a block-Hadamard transform online to…

## 12. Incentivizing Self-Learning in Large Language Models via Reinforcement Learning

- 分数：23.0  ·  HF 赞：14  ·  来源：huggingface
- 兴趣命中：reasoning, reinforcement learning, benchmark, language model, large language, spec, retrieval
- 作者：Lingkai Kong, Yuzhe Gu, Haiteng Zhao, Zijian Wu, Youqing Fang, Zhouqi Hua, Yanan Sun, Kai Chen, Wenwei Zhang
- 链接：[arXiv](https://arxiv.org/abs/2610.39671) · [PDF](https://arxiv.org/pdf/2610.39671) · [HF](https://huggingface.co/papers/2610.39671)

Large language models (LLMs) draw on parametric knowledge and retrieval-augmented generation (RAG) to solve knowledge-intensive tasks. Yet problem solving in unfamiliar domains calls for tightly coupled knowledge acquisition and reasoning, beyond factual retrieval and aggregation or learning solely from a preassembled context. We study self-learning -- autonomously retrieving, studying, and applying knowledge from…

## 13. DepthGraft: Structural Regularization through Hierarchical Cross-Layer KV Reconstruction

- 分数：23.0  ·  HF 赞：14  ·  来源：huggingface
- 兴趣命中：memory, language model, large language, retrieval
- 作者：Xiaohan Qin, Xiangdong Zhang, Yu Wang, Huaijin Wu, Zhuo Xia, Yebin Yang, Junchi Yan
- 链接：[arXiv](https://arxiv.org/abs/2611.03142) · [PDF](https://arxiv.org/pdf/2611.03142) · [HF](https://huggingface.co/papers/2611.03142)

Scaling depth is a key route to stronger large language models, but Pre-LN architectures often suffer from depth-wise information dilution, limiting the effective use of deep layers. While cross-layer connectivity has proven effective at mitigating this problem, existing designs usually introduce additional computation or memory access. We revisit cross-layer KV sharing as an efficient form of such connectivity.…

## 14. The Surprising Effectiveness of Deleting Weights in LLM Post-Training

- 分数：21.5  ·  HF 赞：11  ·  来源：huggingface
- 兴趣命中：reinforcement learning, language model, large language, spec
- 作者：Jack Lu, Zhenbang Yang, Mike Lasby, Tejas Pote, Yani Ioannou, Mengye Ren
- 链接：[arXiv](https://arxiv.org/abs/2611.10866) · [PDF](https://arxiv.org/pdf/2611.10866) · [HF](https://huggingface.co/papers/2611.10866)

How little of a pretrained large language model (LLM) has to change for it to acquire new capabilities? We find that zeroing fewer than 0.05% of its weights, with no other modification, matches full fine-tuning (FFT) at scale across three LLM post-training regimes: reinforcement learning with verifiable rewards, supervised fine-tuning, and on-policy distillation. Our method, Deletion Tuning, learns a binary mask…

## 15. EVAThink: Evidence Sufficiency-Guided Training for Adaptive Thinking in Video Understanding

- 分数：21.5  ·  HF 赞：3  ·  来源：huggingface + arxiv
- 兴趣命中：reasoning, reinforcement learning, benchmark, language model, spec
- 作者：Changti Wu, Ruizhe Fan, Bin Wang, Lei Zhang, Yuxiang Zhang
- 链接：[arXiv](https://arxiv.org/abs/2611.13907) · [PDF](https://arxiv.org/pdf/2611.13907) · [HF](https://huggingface.co/papers/2611.13907)

Under a fixed frame budget, video understanding with vision-language models (VLMs) depends on whether the sampled frames provide sufficient evidence for the question. Sufficient frame evidence supports direct answering, whereas less informative observations may benefit from reasoning that connects the available cues. We introduce EVAThink, which enhances video understanding through evidence sufficiency-guided…

## 16. DexForesight: Grounding Dexterous Policies with Implicit Spatial Foresight

- 分数：20.0  ·  HF 赞：24  ·  来源：huggingface
- 兴趣命中：-
- 作者：Zhongxi Chen, Yi Yang, Xinyi Chen, Mingzhe Ye, Yaping Li, Zhihong Liu, Congsheng Xu, Haonan Wang, Zhijie Deng
- 链接：[arXiv](https://arxiv.org/abs/2611.11166) · [PDF](https://arxiv.org/pdf/2611.11166) · [HF](https://huggingface.co/papers/2611.11166)

Dexterous manipulation requires rich spatial foresight over both the surrounding scene and the robot hand. Existing world-action models often acquire such predictive knowledge through explicit future prediction. We introduce DexForesight, a framework that learns spatial foresight implicitly by injecting dynamics-aware world representations into the latent space of a dexterous policy. During training, DexForesight…

## 17. WaveGen: Truly End-to-End Waveform Generation via Internal Spectral Trajectory Learning

- 分数：20.0  ·  HF 赞：16  ·  来源：huggingface
- 兴趣命中：benchmark, spec
- 作者：Sang-Hoon Lee, Ha-Yeong Choi
- 链接：[arXiv](https://arxiv.org/abs/2611.12527) · [PDF](https://arxiv.org/pdf/2611.12527) · [HF](https://huggingface.co/papers/2611.12527)

This work proposes WaveGen, a fully end-to-end diffusion-based text-to-waveform framework based on Spectral Forcing, which jointly learns an internal spectral trajectory and the target waveform trajectory within a single model, enabling direct end-to-end text-to-waveform generation. Unlike recent TTS pipelines, WaveGen does not rely on separately trained or externally decoded intermediate representations, such as…

## 18. GTAGym: Real AAA Game Tasks Environment for Evaluation and Reinforcement Learning

- 分数：20.0  ·  HF 赞：8  ·  来源：huggingface
- 兴趣命中：agent, reasoning, reinforcement learning, evaluation, benchmark, spec
- 作者：Jiajun Chen, Shicheng Fang, Jiahao Lu, Yuxin Wang, Xipeng Qiu
- 链接：[arXiv](https://arxiv.org/abs/2611.13028) · [PDF](https://arxiv.org/pdf/2611.13028) · [HF](https://huggingface.co/papers/2611.13028)

AAA games offer a rich testbed for evaluating agent perception, reasoning, and control. However, evaluating whether agents can complete tasks in AAA games is challenging and often human-annotated because task outcomes are often difficult to verify automatically, let alone applying it for Reinforcement Learning (RL). We introduce GTAGym, an environment and framework for evaluation and RL on GTA V tasks. Its…

## 19. Micius-Flash: Lightweight Agentic Intelligence for Engineering

- 分数：19.5  ·  HF 赞：7  ·  来源：huggingface
- 兴趣命中：agent, context window, reasoning, benchmark, coding, spec, planning
- 作者：Hongcheng Gao, Weiheng Li, Yipeng Wei, Yu Lei, Shuo Sun, Yi Li, Yajiao Wang, Jie Luo, Jianwei Wen, Xinyi Zhou, Hongda Li, Yibing Zhang, Henghui Sun, Yufan Zhou, Tianfang Hao, Naihao Xue, Hailong Qu, Jingjing Zhou, Peng Xu, Yongzheng Wei, Yichen Zhu, Ziying Wang, Yibo Wang, Jianshu Zeng, Yuhang Lei, Zeqiang Wang
- 链接：[arXiv](https://arxiv.org/abs/2611.10015) · [PDF](https://arxiv.org/pdf/2611.10015) · [HF](https://huggingface.co/papers/2611.10015)

We introduce Micius-Flash, a 27-billion-parameter model for engineering with native multimodal input, deep reasoning and a 256K-token context window. We design the Micius data pipeline as a knowledge-tree-driven data flywheel comprising three stages: knowledge tree construction and expansion, data synthesis, and quality validation with hard-example augmentation. From this data, we train expert models for…

## 20. PhyRubric: Rubric-Grounded Diagnostic Evaluation of Physical Commonsense in Text-to-Video Generation

- 分数：19.0  ·  HF 赞：10  ·  来源：huggingface
- 兴趣命中：evaluation, benchmark, spec
- 作者：Huiyi Chen, Weitai Kang, Shicheng Fan, Xinshuo Wang, Zhixiang Shen, Yan Yan, Philip S. Yu, Baoxin Li
- 链接：[arXiv](https://arxiv.org/abs/2611.13576) · [PDF](https://arxiv.org/pdf/2611.13576) · [HF](https://huggingface.co/papers/2611.13576)

As text-to-video (T2V) models are increasingly positioned as world simulators, it is essential to evaluate whether their videos conform to physical commonsense. However, existing benchmarks rely on annotators who rate each video with a single score based on intuition, yielding ratings that are subjective and do not tell which physical principle is violated. We introduce PhyRubric, a rubric-grounded diagnostic…

## 21. LEASH: Stay Safe in Agentic Robotics

- 分数：18.5  ·  HF 赞：5  ·  来源：huggingface
- 兴趣命中：agent, memory, evaluation, benchmark, spec
- 作者：Qinfeng Zhu, Weiguang Zhao, Ke Sun, Xihao Guo, Yunxi Jiang, Rui Zhang, Lei Fan, Kaizhu Huang
- 链接：[arXiv](https://arxiv.org/abs/2611.14115) · [PDF](https://arxiv.org/pdf/2611.14115) · [HF](https://huggingface.co/papers/2611.14115)

Foundation models such as GPT and Claude have shown strong capabilities in spatial understanding and embodied intelligence. These advances make agentic robotics a promising path toward artificial general intelligence in robotics. However, we find that using foundation models to control robots poses serious safety risks, and comprehensive safety evaluation is still lacking. We introduce RoboRisk, a comprehensive…

## 22. Test-Time Scaling for Diffusion Language Models with Frequency-Aware Remasking

- 分数：18.0  ·  HF 赞：8  ·  来源：huggingface
- 兴趣命中：reasoning, language model, coding
- 作者：Bowen Zuo, Yue Yu, Dongruo Zhou, Yinglun Zhu
- 链接：[arXiv](https://arxiv.org/abs/2611.10486) · [PDF](https://arxiv.org/pdf/2611.10486) · [HF](https://huggingface.co/papers/2611.10486)

Diffusion language models (DLMs) generate text through iterative denoising, where decisions about which tokens to commit or remask strongly affect output quality. Existing certainty-aware strategies rely on instantaneous confidence or entropy, but these local signals can be misleading on difficult reasoning problems. We formulate DLM test-time scaling as adaptive allocation of both inference compute and decoding…

## 23. Are Causal Neuron Circuits Unique and Transferable?

- 分数：17.0  ·  HF 赞：6  ·  来源：huggingface + arxiv
- 兴趣命中：spec
- 作者：Ömer Tekin Yavuz
- 链接：[arXiv](https://arxiv.org/abs/2611.13885) · [PDF](https://arxiv.org/pdf/2611.13885) · [HF](https://huggingface.co/papers/2611.13885)

Interpretability demonstrations often show that intervening on a group of neurons changes a model's answer. A recent example removes an 18-neuron group in Qwen3-32B and the model answers "Simba" instead of "Scar" to a two-hop Lion King riddle. Such a demonstration establishes that the group matters, but not how much of it is necessary, whether other groups could do the same, or whether the effect carries over to…

## 24. Ensemble Routing for Prompt-Adaptive Cost-Aware LLM Inference

- 分数：17.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：benchmark, language model, large language, spec
- 作者：Saul Urso, Emanuele Carlini, Patrizio Dazzi, Matteo Mordacchini
- 链接：[arXiv](https://arxiv.org/abs/2611.10193) · [PDF](https://arxiv.org/pdf/2611.10193) · [HF](https://huggingface.co/papers/2611.10193)

Large language models (LLMs) increasingly support Web-based services that must balance response quality and inference cost across heterogeneous requests. Conventional routing selects one model per prompt, while fixed ensembles cannot adapt their composition and cost to individual requests. We introduce PISA, a prompt-adaptive, cost-aware single-model router, and PISA-E, its extension to ensemble routing. At the core…

## 25. Sable: A Small-Field Sumcheck Argument for Bit-Exact Inference of Large Language Models

- 分数：17.0  ·  HF 赞：2  ·  来源：huggingface + arxiv
- 兴趣命中：language model, large language
- 作者：Tomer Solberg
- 链接：[arXiv](https://arxiv.org/abs/2611.14083) · [PDF](https://arxiv.org/pdf/2611.14083) · [HF](https://huggingface.co/papers/2611.14083)

We present Sable, an argument system and single-GPU prover for the statement that a committed, integer-quantized transformer produced a given token sequence from a given prompt, bit for bit. Sable fixes an integer function F_O with no floating-point step, in which every rounding, normalization, softmax and sampling decision is determined by its inputs, and proves it with a constraint system whose relations provably…

## 26. ProTEUS: A mutation-resolved world model for closed-loop protein evolution

- 分数：16.5  ·  HF 赞：13  ·  来源：huggingface
- 兴趣命中：evaluation
- 作者：Yikun Zhang, Minghao Guo, Guangxue Xu, Peter Yichen Chen, Wojciech Matusik, Wengong Jin, Jingjing Chai, Kaiyi Jiang
- 链接：[arXiv](https://arxiv.org/abs/2611.13348) · [PDF](https://arxiv.org/pdf/2611.13348) · [HF](https://huggingface.co/papers/2611.13348)

Protein engineering requires navigating rugged fitness landscapes, where small sequence changes can produce large functional differences, but experimental screening can only sample a small fraction of sequence space. Thus, a central challenge is to efficiently traverse the large combinatorial space of mutations in silico. We introduce ProTEUS, a mutation-resolved world model for closed-loop protein evolution.…

## 27. EarthRecord: From Pixels to Land Change with Multimodal Agents over Four Decades of Satellite Imagery

- 分数：16.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark
- 作者：Haoran Zhang, Huizhen Sun, Hanbin Wen, Jie Leng, Jiaxin Zhu, Zhaohua Sun
- 链接：[arXiv](https://arxiv.org/abs/2611.12934) · [PDF](https://arxiv.org/pdf/2611.12934) · [HF](https://huggingface.co/papers/2611.12934)

While multimodal agents now carry out complex data analysis with tools, their ability to turn decades of satellite imagery into reliable land-change analysis, crucial for Earth observation science, remains unmeasured. Existing benchmarks fall short: they pose questions on curated images or give agents preprocessed inputs, leaving out the raw multi-sensor archives where such analysis begins. We introduce EarthRecord,…

## 28. Shortcuts and Boundaries: Verifiable RL Misalignment and Contextual Safety Learning

- 分数：16.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：agent, reinforcement learning, coding
- 作者：Xinjie Shen
- 链接：[arXiv](https://arxiv.org/abs/2611.12865) · [PDF](https://arxiv.org/pdf/2611.12865) · [HF](https://huggingface.co/papers/2611.12865)

Reinforcement learning (RL) can improve an agent's task capability while reinforcing behavior that violates contextual execution requirements. We study this reward-driven misalignment, including reward hacking, through verifiable reward--context conflicts, where compliant task completion remains feasible while some executable shortcuts earn more reward than every compliant strategy. Encoding these conflicts in task…

## 29. ExRL: Sample-Efficient Online Adaptation of Long-Chunk Policies via Execution Length Control

- 分数：16.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：reinforcement learning, benchmark, spec
- 作者：Xu Luo, Jiaying Yang, Hao Wu, Junlin Xie, Zijin Hong, Ji Zhang, Lianli Gao, Jingkuan Song
- 链接：[arXiv](https://arxiv.org/abs/2611.13482) · [PDF](https://arxiv.org/pdf/2611.13482) · [HF](https://huggingface.co/papers/2611.13482)

Predicting long action chunks, often spanning dozens of timesteps, has become a key ingredient in increasingly capable robot policies. In this paper, we find that adapting these long-chunk policies with existing reinforcement learning (RL) methods can require many online samples due to the high dimensionality of the action chunks being optimized, making such adaptation impractical in real-world scenarios where…

## 30. Is Your Robot's Memory Just a Clock? Temporal Shortcuts in Memory-Augmented VLA Policies

- 分数：15.5  ·  HF 赞：7  ·  来源：huggingface
- 兴趣命中：memory, coding
- 作者：Chubin Zhang, Bo An
- 链接：[arXiv](https://arxiv.org/abs/2611.14488) · [PDF](https://arxiv.org/pdf/2611.14488) · [HF](https://huggingface.co/papers/2611.14488)

Memory-augmented vision-language-action (VLA) policies are meant to remember what happened. Many of them, however, fill memory by time: they sample frames uniformly across the episode and stamp each frame with its time step. Because time passes even when nothing happens, such a memory may not tell waiting from working. We show that it does not. On the counting tasks of RoboMME, we make the robot briefly pause or…

## 31. TorchCurves: Differentiable Parametric Curves

- 分数：15.5  ·  HF 赞：3  ·  来源：huggingface + arxiv
- 兴趣命中：evaluation
- 作者：Alex Shtoff
- 链接：[arXiv](https://arxiv.org/abs/2611.14516) · [PDF](https://arxiv.org/pdf/2611.14516) · [HF](https://huggingface.co/papers/2611.14516)

We present TorchCurves, a PyTorch library that treats vector-valued parametric curves as learnable primitives. Its central operation maps batches of scalar inputs to points on curves represented in B-spline or Legendre polynomial bases, with differentiation through both inputs and coefficients. Curve coefficients can be optimized jointly with the surrounding model or produced by another network. The library provides…

## 32. From Tool State to Scientific Action: Auditing Decision Provenance in Biomedical Research Agents

- 分数：15.0  ·  HF 赞：10  ·  来源：huggingface
- 兴趣命中：agent
- 作者：Xingyu Yi, Xinya Zhang, Yunshen Zhou, Haoyu Bao
- 链接：[arXiv](https://arxiv.org/abs/2611.01527) · [PDF](https://arxiv.org/pdf/2611.01527) · [HF](https://huggingface.co/papers/2611.01527)

A scientific agent can give the same verdict while reading and citing different evidence. BioAgent-DF tests this separation using paired reference and candidate values saved at the same scientific computation site. It restores or transplants those values at their original coordinates, then runs the agent on healthy hardware. Across eight SciFact batches, Qwen3.5-4B shows repeatable citation changes in three…

## 33. WMIP: A Working-Memory-Inspired Programmable Probe of Cumulative State Tracking in Large Language Models

- 分数：15.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：memory, language model, large language
- 作者：Dengzhe Hou, Lingyu Jiang, Deng Li, Zirui Li, Fangzhou Lin, Kazunori D Yamada
- 链接：[arXiv](https://arxiv.org/abs/2603.27343) · [PDF](https://arxiv.org/pdf/2603.27343) · [HF](https://huggingface.co/papers/2603.27343)

Human working memory lets people maintain and update information. Large language models (LLMs) face a related demand when tracking updates within a single prompt without writing out intermediate states, yet existing tests differ in their constraints on written steps. We introduce a working-memory-inspired probe of cumulative state tracking with program-computed answers, 3 to 100 updates, and final-state,…

## 34. Lipschitz-Controlled Flow Matching for Robust Image Restoration

- 分数：15.0  ·  HF 赞：2  ·  来源：huggingface + arxiv
- 兴趣命中：spec
- 作者：Sedjro Salomon Hotegni, Konstantin Sonntag, Paul-Christian Bürkner, Sebastian Peitz
- 链接：[arXiv](https://arxiv.org/abs/2611.13995) · [PDF](https://arxiv.org/pdf/2611.13995) · [HF](https://huggingface.co/papers/2611.13995)

Flow-matching models can produce high-quality image restorations, but their learned dynamics may amplify small input perturbations and make reconstructions unstable. We introduce LipsFlower to reduce this amplification. We derive stability bounds for Flow-from-$Y$, which initializes the ordinary differential equation from a noise-perturbed observation, as well as for observation-conditioned posterior sampling, which…

## 35. PhysOPSD: Code as Privilege for Physically Plausible Video Generation

- 分数：14.0  ·  HF 赞：8  ·  来源：huggingface
- 兴趣命中：reinforcement learning
- 作者：Harold Haodong Chen, Rui Peng, Lingteng Qiu, Kejie Qiu, Chao Xu, Zilong Dong
- 链接：[arXiv](https://arxiv.org/abs/2611.12411) · [PDF](https://arxiv.org/pdf/2611.12411) · [HF](https://huggingface.co/papers/2611.12411)

While modern video generative models achieve remarkable visual fidelity, they remain noticeably brittle when generating physically plausible dynamics and complex interactions. Targeted post-training is crucial, yet supervised fine-tuning suffers from offline state mismatch, and reinforcement learning is hindered by sparse, ill-defined physical reward functions. On-Policy (Self-)Distillation (OPSD) reconciles…

## 36. Blind Variation, Selective Retention: Improving Creative Idea Generation in AI Scientists

- 分数：14.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：evaluation, spec
- 作者：Guowei Xu, Jiaru Zou, Mete Erdogan, Haotian Ye, Pan Lu, James Zou
- 链接：[arXiv](https://arxiv.org/abs/2611.12184) · [PDF](https://arxiv.org/pdf/2611.12184) · [HF](https://huggingface.co/papers/2611.12184)

Scientific discovery requires ideas that are original, useful, and non-obvious. Yet AI scientists are typically given as much task information as possible during idea generation, which can anchor generation toward familiar approaches. Inspired by the cognitive framework of Blind Variation and Selective Retention (BVSR), we propose a discovery framework that separates these two roles of information: it generates…

## 37. DyCraft: An Agentic System for Long-Horizon 4D Scene Generation

- 分数：13.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：agent, coding
- 作者：Jeff Tan, Hang Dai, Zeqian Long, Yanzhe Lyu, R. Kenny Jones, Shangzhe Wu, Chen Geng, Jiajun Wu
- 链接：[arXiv](https://arxiv.org/abs/2610.40754) · [PDF](https://arxiv.org/pdf/2610.40754) · [HF](https://huggingface.co/papers/2610.40754)

While frontier coding agents can generate high-quality 3D scenes and articulated assets, they struggle to create coherent long-horizon animations. When equipped with general-purpose harnesses, they frequently produce physically implausible outputs, generating objects that interpenetrate, lack physical support, or move unnaturally. Such bare agents struggle to repair these errors because they default to scripting the…

## 38. Predictive Surprise as Self-Grounding Concept Bottleneck for Interpretable Time Series

- 分数：13.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：benchmark, language model
- 作者：Sachith Abeywickrama, Emadeldeen Eldele, Min Wu, Xiaoli Li, Chau Yuen
- 链接：[arXiv](https://arxiv.org/abs/2611.12955) · [PDF](https://arxiv.org/pdf/2611.12955) · [HF](https://huggingface.co/papers/2611.12955)

Time-series classifiers deployed in risk-sensitive domains must be (1) accurate, (2) interpretable, and (3) able to abstain when evidence is weak. Existing methods do not deliver all 3 at once, and the obstacle is structural, rather than logistical. Meaningful temporal patterns cannot be defined without knowing segment boundaries, yet meaningful boundaries cannot be placed without knowing which patterns to expect.…

## 39. CogBattery: Human-Referenced Evaluation of Cognitive Task Behavior and Structure in Language Models

- 分数：13.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：evaluation, language model
- 作者：Dengzhe Hou, Lingyu Jiang, Fangzhou Lin, Kazunori D Yamada
- 链接：[arXiv](https://arxiv.org/abs/2607.24999) · [PDF](https://arxiv.org/pdf/2607.24999) · [HF](https://huggingface.co/papers/2607.24999)

Human cognitive tasks let us compare language models with humans under controlled conditions. Yet a model can reproduce the direction of a human effect while making different errors. CogBattery evaluates 54 open-weight language models on text adaptations of 13 cognitive paradigms, comparing each with human data from its source study. Like humans, models respond more to n-back lures than to controls, yet they make…

## 40. Visual Similarity in Adult Word Extension and Artificial Word Learning

- 分数：13.0  ·  HF 赞：2  ·  来源：huggingface + arxiv
- 兴趣命中：-
- 作者：Patricio M. Vera
- 链接：[arXiv](https://arxiv.org/abs/2611.14116) · [PDF](https://arxiv.org/pdf/2611.14116) · [HF](https://huggingface.co/papers/2611.14116)

When two objects share a name, how much does their visual similarity explain, and what do the teaching examples add? First, we reanalyzed trial-level data from a large adult word-extension study (Lewis & Frank, 2018), computing each test image's distance to the examples shown in the space of a frozen self-supervised visual encoder (DINOv2). Distance was associated with extension (log odds -3.23 per standard…

## 41. Market-Conditioned JEPA: Learning from Unpredictable Market Shocks

- 分数：12.5  ·  HF 赞：5  ·  来源：huggingface
- 兴趣命中：spec
- 作者：Yuqi Wang, Fengyuan Liu, Mukai Li, Haochen Luo, Lei Li, Qi Liu
- 链接：[arXiv](https://arxiv.org/abs/2611.13572) · [PDF](https://arxiv.org/pdf/2611.13572) · [HF](https://huggingface.co/papers/2611.13572)

Much of the variation in financial time series is driven by market-wide shocks that cannot be predicted from an asset's own history. Per-asset self-supervised learning treats this variation as irreducible noise. Under a latent factor model, we show that conditioning prediction on the realized market factor makes the asset's market exposure necessary for optimal prediction, while reducing the noise against which the…

## 42. Prompt2Echo (P2Echo): Text-Prompted Multi-View Echocardiography Segmentation with One Model

- 分数：12.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：evaluation, spec
- 作者：Moein Heidari, Alvin Kimbowa, Mahdi Tabatabaei, Afshin Bozorgpour, Sina Ghorbani Kolahi, River Jiang, Wenjin Chen, David J. Foran, Jasmine Grewal, Dorit Merhof, Ilker Hacihaliloglu
- 链接：[arXiv](https://arxiv.org/abs/2611.13425) · [PDF](https://arxiv.org/pdf/2611.13425) · [HF](https://huggingface.co/papers/2611.13425)

Automated segmentation in multi-view echocardiography is essential for comprehensive cardiac assessment, yet remains challenging due to substantial anatomical and appearance variability across standard acoustic windows. In this paper, we present P2Echo, a unified framework capable of segmenting diverse cardiac structures across multiple standard echocardiographic views using a single model controlled by structured…

## 43. Are Dense Rewards Worth Their Tokens in GRPO?

- 分数：12.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：language model
- 作者：Vikash Singh, Weicong Chen, Debargha Ganguly, Yanyan Zhang, Mohsen Hariri, Sreehari Sankar, Wang Yang, Chaoda Song, Alexander Nemecek, Osama Zafar, Yuting Shao, Kai Ye, Biyao Zhang, Xinpeng Li, Shouren Wang, Erman Ayday, Jing Ma, Sanmukh Rao Kuppannagari, Vipin Chaudhary
- 链接：[arXiv](https://arxiv.org/abs/2611.13560) · [PDF](https://arxiv.org/pdf/2611.13560) · [HF](https://huggingface.co/papers/2611.13560)

RLVR trains language models to reason by rewarding correct final answers. A widely used algorithm, group-relative policy optimization (GRPO), gives every token of a solution the same credit, so dense process rewards have been proposed to credit intermediate steps, for example with a Monte-Carlo reward that scores each step by sampling continuations from it. Comparing such a reward with GRPO per training update, or…

## 44. Interactive Visual Gym: Evaluating Visual Interaction Models with Simulated Users in Interactive Worlds

- 分数：12.0  ·  HF 赞：0  ·  来源：huggingface
- 兴趣命中：evaluation, benchmark
- 作者：Chenhao Zheng, Zixian Ma, Kai Li, Kanchana Ranasinghe, Jieyu Zhang, Artemis Panagopoulou, Weikai Huang, Jianxu Shangguan, Yuanyuan Tan, Silvio Savarese, Juan Carlos Niebles, Ranjay Krishna, Ran Xu, Honglu Zhou
- 链接：[arXiv](https://arxiv.org/abs/2611.08286) · [PDF](https://arxiv.org/pdf/2611.08286) · [HF](https://huggingface.co/papers/2611.08286)

Visual interaction models that support users during ongoing physical tasks require evaluation in closed loop, where assistant responses can change subsequent user behavior and task outcomes. Existing benchmarks largely rely on offline replay and therefore cannot capture these effects. We introduce Interactive Visual Gym, a framework for closed-loop evaluation and training of visual interaction models through joint…

## 45. Learning to Act with World Models by Valuing What Comes Next

- 分数：11.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：agent
- 作者：Chenghao Gao, Zhi Zhang, Dian Jin, Yihe Pan, Doudou Zhou
- 链接：[arXiv](https://arxiv.org/abs/2611.12200) · [PDF](https://arxiv.org/pdf/2611.12200) · [HF](https://huggingface.co/papers/2611.12200)

A sparse terminal reward tells an agent little about its steps. Much of the missing information is implicit in the environment's dynamics, because each state transition can change the conditions for success long before the reward arrives. A world model trained on real transitions can learn to predict what each action changes, but a predicted observation does not by itself show whether success has become more likely.…

## 46. Module-Aware Optimization for Graph Neural Networks

- 分数：10.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：benchmark
- 作者：Guy Hadad, Haggai Roitman, Moshe Eliasof, Bracha Shapira
- 链接：[arXiv](https://arxiv.org/abs/2611.08379) · [PDF](https://arxiv.org/pdf/2611.08379) · [HF](https://huggingface.co/papers/2611.08379)

Different optimizers impose different geometries on parameter updates. Adaptive methods such as Adam and AdamW use coordinate-wise updates, while matrix-aware optimizers such as Muon utilize weight-matrix structure through orthogonalized updates. For Graph Neural Networks (GNNs), however, the effective geometry of its weight matrices is shaped not only by its learned channel-mixing weights, but also by the…

## 47. Read Less, Solve More: Token-Efficient Sparse Reading of External Content for AI Agents

- 分数：10.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：agent
- 作者：Zedong Liu, Jiaan Wu, Xinyang Ma, Le Xu, Kai Wang, Yuanchao Hu, Dingwen Tao, Guangming Tan
- 链接：[arXiv](https://arxiv.org/abs/2608.22237) · [PDF](https://arxiv.org/pdf/2608.22237) · [HF](https://huggingface.co/papers/2608.22237)

Web-facing AI agents repeatedly access webpages, documents, repositories, and tool responses, yet reading interfaces often expose entire objects when only sparse evidence is needed. This over-reading increases token and latency costs and can dilute relevant evidence. We present SparseRead, a reusable reading control layer that governs content admission without modifying the agent model. Its Read Intent Protocol…

## 48. LO-World: Unified BEV Latent Modeling for Joint 4D Occupancy and LiDAR Forecasting

- 分数：10.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：spec
- 作者：Zhimin Liao, Ping Wei, Kai Mao, Shuaijia Chen
- 链接：[arXiv](https://arxiv.org/abs/2611.11912) · [PDF](https://arxiv.org/pdf/2611.11912) · [HF](https://huggingface.co/papers/2611.11912)

LiDAR point clouds and 3D semantic occupancy represent two distinct modalities capturing fine-grained metric geometry and dense volumetric semantics, respectively, holding natural potential for mutual complementarity. However, existing world models typically forecast these modalities independently or cascade them heuristically, missing the opportunity for reciprocal cross-modal regularization. To address this, we…

## 49. A computational framework for understanding embodied plans

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reasoning, language model, spec, planning
- 作者：Aalap D. Shah, Basil Saeed, Joshua B. Tenenbaum, Tobias Gerstenberg, Hyowon Gweon, Ilker Yildirim
- 链接：[arXiv](https://arxiv.org/abs/2611.13669) · [PDF](https://arxiv.org/pdf/2611.13669) · [HF](https://huggingface.co/papers/2611.13669)

Reasoning about people's plans and goals based on their actions is fundamental to human social interaction and essential for cooperative, embodied artificial intelligence. Formalizing this capacity in naturalistic, embodied settings has been a longstanding challenge. Here, we present GenEA, a novel agent representation capable of reasoning over multi-step, long-horizon embodied plans. At the heart of GenEA lies a…

## 50. OpticalRAG: Pixel-Space Compression for Token-Efficient Retrieval-Augmented Generation

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：context window, benchmark, language model, large language, retrieval
- 作者：Senhao Liu, Yuheng Zhang, Chunyu Wei, Yueguo Chen, Xinran Zhang
- 链接：[arXiv](https://arxiv.org/abs/2611.13675) · [PDF](https://arxiv.org/pdf/2611.13675) · [HF](https://huggingface.co/papers/2611.13675)

Retrieval-augmented generation (RAG) is bottlenecked by the token budget of large language models: feeding long documents into the context window is expensive, while aggressive textual compression discards fine-grained information that is irreversibly lost in a one-dimensional token sequence. We argue that this bottleneck is not fundamental to information density but to the choice of compression \emph{modality}.…

## 51. On Private Knowledge Retrieval and Private Inference for secure multi-agent systems

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, memory, language model, large language, retrieval
- 作者：Vicenç Torra, Maria Bras-Amorós
- 链接：[arXiv](https://arxiv.org/abs/2611.13696) · [PDF](https://arxiv.org/pdf/2611.13696) · [HF](https://huggingface.co/papers/2611.13696)

Multi-agent systems provide a convenient framework for the massive deployment of agents based on Large Language Models (LLMs). It provides a sound framework where agents can interact with existing software to perform actions in an autonomous way. Agentic AI is the new term to denote these AI-based autonomous systems. In real multi-agent systems, agents need to deal with malicious agents some of which can exploit…

## 52. Broad-Persistent Advising in Interactive Reinforcement Learning via Latent State Encoding

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, reinforcement learning, coding, spec
- 作者：Zhuoran Liang, Francisco Cruz
- 链接：[arXiv](https://arxiv.org/abs/2611.13712) · [PDF](https://arxiv.org/pdf/2611.13712) · [HF](https://huggingface.co/papers/2611.13712)

Deep Interactive Reinforcement Learning (Deep IntRL) accelerates reinforcement learning training by incorporating external advice. However, conventional Deep IntRL uses each piece of advice only in the current step and discards it after a single interaction. Persistent Advising and Broad-Persistent Advising (BPA) extend this process by storing advice in persistent memory and reusing it in similar states through…

## 53. Toward Autonomous RTL and Synthesis Optimization: Benchmarking and Self-Improving Agents

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, evaluation, benchmark, language model, large language, spec
- 作者：Wenji Fang, Yao Lu, Jinghua Wang, Zhiyao Xie
- 链接：[arXiv](https://arxiv.org/abs/2611.13713) · [PDF](https://arxiv.org/pdf/2611.13713) · [HF](https://huggingface.co/papers/2611.13713)

Recent advances in large language models (LLMs) and autonomous agents are creating new opportunities for hardware design optimization. This paper examines three connected directions toward autonomous RTL and synthesis optimization: (1) Realistic benchmarking. We discuss reference-based and open-ended RTL optimization benchmarks that evaluate optimization opportunities under realistic EDA workflows. (2) Tool-grounded…

## 54. DisasterAgent: An Evidence-Driven Agent for Verifiable Disaster Report Generation From Remote Sensing Imagery

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, memory, reasoning, benchmark, language model, spec
- 作者：Zhijian Li, Jiawei Song, Chao Ren, Yidan Zhang, Peijin Wang, Xian Sun, Kun Fu
- 链接：[arXiv](https://arxiv.org/abs/2611.13776) · [PDF](https://arxiv.org/pdf/2611.13776) · [HF](https://huggingface.co/papers/2611.13776)

Remote sensing disaster assessment is moving from simple damage classification toward comprehensive report-level analysis. In this setting, responders need not only damage descriptions but also verifiable evidence to guide response and recovery. Recent vision-language models (VLMs) and tool-augmented agents offer strong multimodal reasoning and perception, but they struggle to provide the evidence required for…

## 55. Taxonomy-Agnostic Neurosymbolic Grounding of Robot Kinematics

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：context window, reasoning, evaluation, language model, large language
- 作者：Bastien Dussard, Aur{é}lie Clodic, Guillaume Sarthou
- 链接：[arXiv](https://arxiv.org/abs/2611.13850) · [PDF](https://arxiv.org/pdf/2611.13850) · [HF](https://huggingface.co/papers/2611.13850)

While symbolic reasoning for task allocation requires grounding a robot's physical capabilities, standard Unified Robot Description Format (URDF) files provide only low-level kinematics without the formal semantic context needed for reasoning. We present URDF2Ontology, an automated, taxonomy-agnostic neurosymbolic framework that transforms raw URDF files into populated, grounded OWL ontologies. It leverages a Large…

## 56. Beyond Passive Imitation: On-Policy Mid-Training Distillation for Language Models

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, language model, large language, spec
- 作者：Ruize Zheng, Xuyang Liu, Siyu Ren, Xiaobing Tu, Yinggui Wang, Jinkui Ren, Xiantao Zhang, Linfeng Zhang
- 链接：[arXiv](https://arxiv.org/abs/2611.13855) · [PDF](https://arxiv.org/pdf/2611.13855) · [HF](https://huggingface.co/papers/2611.13855)

Continual pre-training (CPT) adapts large language models (LLMs) to specialized domains, yet its standard next-token prediction (NTP) objective treats every corpus token as a fixed target, regardless of its utility to the current model. In a controlled study on the same 1B-token mathematical corpus, we observe sharply different outcomes across base models: NTP improves Llama-3.2-3B's performance on mathematical…

## 57. DroneSegEdit: Adapting Pretrained Generative Editors for UAV Segmentation with Language-Grounded Verification

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：language model, large language, coding, spec
- 作者：Dehua Chen, Long Xin, Jiangtao Wei
- 链接：[arXiv](https://arxiv.org/abs/2611.13890) · [PDF](https://arxiv.org/pdf/2611.13890) · [HF](https://huggingface.co/papers/2611.13890)

Recent work has shown that pretrained image generators can support diverse visual tasks. Yet directly applying them to language-guided unmanned aerial vehicle (UAV) segmentation exposes a key limitation: a plausible mask may correspond to the wrong instance among small and repeated objects. We call this mismatch between mask rendering and expression-level target selection the Grounding-Rendering Gap. We present…

## 58. Beyond Fluent Responses: Finding User Dissatisfaction in Human-AI Interactions

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, language model, large language, spec
- 作者：Yuka Saito, Ikumi Numaya, Jun Suzuki, Reina Akama
- 链接：[arXiv](https://arxiv.org/abs/2611.13894) · [PDF](https://arxiv.org/pdf/2611.13894) · [HF](https://huggingface.co/papers/2611.13894)

As large language models generate increasingly high-quality responses, recent work on response evaluation has moved beyond response-centered criteria, such as correctness and coherence, toward user-centered criteria, including user preferences and perceived usefulness. This shift is fundamentally important for developing technologies that are truly useful to real-world users. While conventional response evaluation…

## 59. Persistent Metric-Semantic Maritime Scene Memory from Open-Vocabulary 3D Scene Graphs

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, reasoning, language model, retrieval
- 作者：Kim Alexander Christensen, Dina Zimmermann, Martin Steinert, Eleni Kelasidi
- 链接：[arXiv](https://arxiv.org/abs/2611.13903) · [PDF](https://arxiv.org/pdf/2611.13903) · [HF](https://huggingface.co/papers/2611.13903)

Three-dimensional scene graphs (3DSGs) can provide robots with persistent metric-semantic representations for spatial reasoning, but the existing methods have primarily been developed for indoor and terrestrial environments. In this paper we investigate how a representative outdoor open-vocabulary method transfers to maritime environments and which adaptations are needed. Our experiments show that zero-shot…

## 60. TAPCO-G: LLM-Guided Design-Adaptive Timing and Power Co-Optimization with Graph-Based Physical Priors

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, language model, large language, spec
- 作者：Wuqian Tang, Zixiao Wang, Che-Chien Lin, Fong-Hua Fu, Laura Angélica Shion-Korsak, Xinyun Zhang, Bei Yu, Chun-Yao Wang
- 链接：[arXiv](https://arxiv.org/abs/2611.13931) · [PDF](https://arxiv.org/pdf/2611.13931) · [HF](https://huggingface.co/papers/2611.13931)

Post-placement timing and power co-optimization is critical to meeting setup timing targets and reducing power within placement constraints. A cell replacement can improve timing along one path while increasing power or reducing slack on others. Conventional optimizers follow fixed rules for scheduling and accepting repairs, limiting their ability to address design-specific bottlenecks. A large language model (LLM)…

## 61. TreeAgent: Structure-Aware Memory Agent for Processing Long Hierarchical Data

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, memory, context window, reasoning, language model, large language, spec, retrieval
- 作者：Wei Gu, Weiwei Qi, Jiajun Tang, Tianhang Zheng, Bo Chen, Zhibo Zhang, Jinfei Liu, Kui Ren
- 链接：[arXiv](https://arxiv.org/abs/2611.13946) · [PDF](https://arxiv.org/pdf/2611.13946) · [HF](https://huggingface.co/papers/2611.13946)

Practical Web applications increasingly require agents to interpret long conversations or documents. For inputs exceeding the context windows of large language models (LLMs), memory agents process segments sequentially and retain past information in bounded memory. However, they typically divide inputs into flat token segments without preserving structure or hierarchy, causing three limitations for structured data…

## 62. Controlled Knowledge Engineering for Taxonomy Induction with Tool-Grounded LLM Agents and Runtime-Adaptive Policies

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, memory, benchmark, language model, large language, retrieval
- 作者：Jonas Limniatis, Bennet Schaarmann, Georg Reuber, Robert Stahlbock
- 链接：[arXiv](https://arxiv.org/abs/2611.13966) · [PDF](https://arxiv.org/pdf/2611.13966) · [HF](https://huggingface.co/papers/2611.13966)

Taxonomies are structured knowledge representations that support semantic search, recommendation, product catalog organization, and retrieval-augmented generation. Their automated construction from a fixed set of candidate entities requires more than plausible text generation: the resulting hierarchy must be complete, structurally valid, and semantically coherent. Large Language Models (LLMs) are promising for this…

## 63. BioXArena-Pro: a research-grade benchmark for autonomous biomedical machine learning agents

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, benchmark, coding, spec
- 作者：Loka Li, Duzhen Zhang, Xingbo Du, Leonard Song, Kun Zhang, Le Song
- 链接：[arXiv](https://arxiv.org/abs/2611.13994) · [PDF](https://arxiv.org/pdf/2611.13994) · [HF](https://huggingface.co/papers/2611.13994)

Coding agents are increasingly proposed as autonomous builders of biomedical models, but existing benchmarks are small, near saturation or open to leaked information. We present BioXArena-Pro, 64 research-level modelling tasks from eight biomedical domains, each rebuilt from a published study; most hold out whole biological units such as species or cohorts. Across 22 agent configurations, the best scores 55.1 of…

## 64. Coding Agent Memory Post-Training II: Unlocking the Memory Potential of Pre-trained File Operations for Long-Horizon Tasks via On-Policy Distillation

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, memory, benchmark, coding
- 作者：Lirui Luo, Kelong Mao, Xinwei Yang, Rongqing Li, Luyu Chen, Kieran Wong, Yudong Guo, Xinrui Wang, Jiayin Zhu, Gu Simiu, Sulong Xu, Cong Fang
- 链接：[arXiv](https://arxiv.org/abs/2611.14009) · [PDF](https://arxiv.org/pdf/2611.14009) · [HF](https://huggingface.co/papers/2611.14009)

Language-model agents increasingly tackle long-horizon tasks whose interaction histories exceed the model's active context. They must therefore decide what to write down and what to read back, and when to do either. Recent work has begun to use on-policy distillation (OPD) to make memory control part of the policy, relying on memory tools and compaction protocols that lie outside either model's pre-training.…

## 65. One Sequence Is Enough: Fingerprinting Language Models from Fixed-Length Integer Sequences

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, language model, spec
- 作者：Fantong Meng, Chengjie Sun, Shuangjia Yang, Zhiyuan Zhao, Yansheng Pei, Xinyang Li
- 链接：[arXiv](https://arxiv.org/abs/2611.14010) · [PDF](https://arxiv.org/pdf/2611.14010) · [HF](https://huggingface.co/papers/2611.14010)

Users of model APIs and third-party platforms often rely on the declared model name to identify the model responding to their requests. However, the actual model may differ from the declared one, motivating identity verification based on observable outputs. Previous studies have shown that preferences in simple numerical-choice tasks can serve as model fingerprints. We investigate whether a single fixed-length…

## 66. Margin-Guided Token Credit for Reinforcement Learning with Verifiable Rewards

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reinforcement learning, evaluation, benchmark, language model
- 作者：Chi Liu, Xin Chen, Yuchuan Weng, Srinivasan Manoharan
- 链接：[arXiv](https://arxiv.org/abs/2611.14015) · [PDF](https://arxiv.org/pdf/2611.14015) · [HF](https://huggingface.co/papers/2611.14015)

In reinforcement learning with verifiable rewards, a language model is rewarded for a correct final answer, and GRPO passes that reward to every token of the solution in equal measure. We instead place the credit where the model hesitated, in a method we call MCPO (Margin-Credit Policy Optimization). We measure hesitation by the top-2 margin $M=p_1-p_2$ of the policy's next-token distribution, map it to a score with…

## 67. Personalized Memory Rubrics: Learning What to Remember per User via Rubric-Guided Credit Assignment

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, memory, evaluation, benchmark, spec
- 作者：Yupeng Han, Kai Zhang, Shuochen Liu, Ze Liu, Xianquan Wang, Zhihong Pan, Xiangyu Zhao, Qi Liu, Enhong Chen
- 链接：[arXiv](https://arxiv.org/abs/2611.14017) · [PDF](https://arxiv.org/pdf/2611.14017) · [HF](https://huggingface.co/papers/2611.14017)

Long-horizon personalized agents maintain an evolving memory by continuously deciding what to add, modify, or discard. However, learning an optimal update policy remains challenging. Conventional training relies solely on terminal question-answering accuracy, yielding a coarse feedback signal that treats all intermediate updates identically. Furthermore, update utility is inherently user-specific, as identical…

## 68. ZoomGain: Mining Global-to-Zoom Perception Gaps for Fine-Grained Visual Supervision

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, language model, spec
- 作者：Haozhan Shen, Liangbo He, Jun Lan, Huijia Zhu, Weiqiang Wang, Tiancheng Zhao, Jianwei Yin
- 链接：[arXiv](https://arxiv.org/abs/2611.14076) · [PDF](https://arxiv.org/pdf/2611.14076) · [HF](https://huggingface.co/papers/2611.14076)

Fine-grained visual perception requires Vision-Language Models (VLMs) to locate and interpret subtle evidence within complex scenes. Constructing supervision for this ability is challenging: questions must have correct, unambiguous answers that depend on actual fine-grained visual details rather than coarse cues or language priors. Verifying these properties makes manual annotation labor-intensive and automatic…

## 69. ProofCoder: Continuous Reasoning for Automated Software Verification

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reasoning, benchmark, language model, large language, coding, spec, retrieval
- 作者：Martim Afonso, Inês Lynce, Maurizio Morisio, João F. Ferreira
- 链接：[arXiv](https://arxiv.org/abs/2611.14106) · [PDF](https://arxiv.org/pdf/2611.14106) · [HF](https://huggingface.co/papers/2611.14106)

Formal verification using proof assistants provides strong correctness guarantees for software, but constructing proofs remains labor-intensive and requires significant expertise. Recent approaches based on large language models (LLMs) have shown promise in automating proof synthesis. However, these approaches typically constrain the model to a rigid tactic-generation loop, in which the surrounding system controls…

## 70. Looking One Step Ahead: An Anticipation-guided Agent for Object State Readout in Videos

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, evaluation, language model, large language, spec
- 作者：Yuanhe Tian, Yan Song
- 链接：[arXiv](https://arxiv.org/abs/2611.14113) · [PDF](https://arxiv.org/pdf/2611.14113) · [HF](https://huggingface.co/papers/2611.14113)

Understanding the progress of an activity requires tracking how the objects involved change over time. Object state readout provides this information by describing a target object's states and transitions across video frames. Although multimodal large language models (MLLMs) generate detailed visual descriptions, these descriptions may leave the attributes needed to distinguish successive states insufficiently…

## 71. Hx2Dx: From Anamnesis to Diagnosis - A Multimodal Arena for Conversational Clinical Reasoning in LLMs

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, evaluation, benchmark, language model, large language
- 作者：Federico Ravenda, Mirko Cesarini, Daniele Montagnani, Volodymyr Karpenko, Antonietta Mira, Andrea Raballo
- 链接：[arXiv](https://arxiv.org/abs/2611.14122) · [PDF](https://arxiv.org/pdf/2611.14122) · [HF](https://huggingface.co/papers/2611.14122)

Large language models (LLMs) achieve expert-level diagnostic accuracy in static evaluations, where the model receives a curated vignette or case report that already condenses the diagnostically relevant findings. Such evaluations measure inference over already selected evidence; the evaluations do not account for the inquiry used to obtain it. In clinical practice, however, diagnosis is an iterative process of…

## 72. Breakdown of Autoregressive Multi-Step Reasoning Under Concentrated vs. Diffuse Attention Head Dropout

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, benchmark, language model, large language
- 作者：Karol Struniawski
- 链接：[arXiv](https://arxiv.org/abs/2611.14209) · [PDF](https://arxiv.org/pdf/2611.14209) · [HF](https://huggingface.co/papers/2611.14209)

During extended wakefulness, mammalian neocortical networks experience localized periods of transient neuronal silence termed off-states. Here, we examine how analogous spatiotemporally concentrated disruptions affect sequential reasoning in autoregressive Large Language Models (LLMs). Evaluating 250 paired derivations on the GSM8K benchmark across two 8B models (Qwen3-8B and LLaMA-3.1-8B-Instruct), we contrast…

## 73. Chain of Physics: Supporting Fault Diagnosis with Engineering-Inspired Large Language Model Reasoning

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, benchmark, language model, large language, spec, retrieval
- 作者：Wenqi Zhou, Leonardo Baldo, Kai Goebel, Manuel Arias Chao
- 链接：[arXiv](https://arxiv.org/abs/2611.14263) · [PDF](https://arxiv.org/pdf/2611.14263) · [HF](https://huggingface.co/papers/2611.14263)

Fault diagnosis in complex systems requires linking observed changes in physical quantities to the failure mechanisms that produce them. Experienced engineers perform this task by combining sensor information with knowledge of system behavior and fault propagation. Large Language Models (LLMs) can support this process, but their diagnostic reasoning depends on the availability of asset-specific engineering knowledge…

## 74. LM-SimBench: A Unified Framework, Dataset, and Benchmark for Large Language Model Training Simulation

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, language model, large language
- 作者：Yu Dong, Hong Li, Qiang Sun, Xu Zhou, Jinbiao Huo, Qixiu Cheng, Zhiyuan Liu
- 链接：[arXiv](https://arxiv.org/abs/2611.14285) · [PDF](https://arxiv.org/pdf/2611.14285) · [HF](https://huggingface.co/papers/2611.14285)

Evaluating candidate parallelization strategies through distributed training runs makes strategy selection prohibitively expensive at scale. Performance simulation offers a lower cost alternative, yet controlled comparisons among existing simulators remain difficult because they differ in the training stages they model and the workloads on which they are evaluated. We introduce LM-SimBench, a unified framework,…

## 75. When Should Agents Remember? Falsification-Gated Self-Evolution for LLM Agents

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, tool-use, memory, benchmark
- 作者：Runxuan Tang, Haoyu Gao, Yuyan Ding, Junyi Yao, Zihao Zheng, Zecheng Sheng, Liwei Hou
- 链接：[arXiv](https://arxiv.org/abs/2611.14326) · [PDF](https://arxiv.org/pdf/2611.14326) · [HF](https://huggingface.co/papers/2611.14326)

LLM agents increasingly operate in long-horizon, verifier-rich environments, but current self-improvement mechanisms often write episode-derived lessons directly into memory, making local success an unreliable signal for reusable and safe knowledge. This paper addresses the core question of when an experience-derived behavioral update should be admitted into persistent agent state. We propose Falsification-Gated…

## 76. Cognitive Mapping of Learning by Thinking Mechanisms in Large Language Models

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, reasoning, language model, large language, spec
- 作者：Dong Han, Jin Zhang, Kunyue Yang
- 链接：[arXiv](https://arxiv.org/abs/2611.14382) · [PDF](https://arxiv.org/pdf/2611.14382) · [HF](https://huggingface.co/papers/2611.14382)

Large language models (LLMs) increasingly exhibit capabilities that resemble human Learning by Thinking (LbT), the acquisition of new insight through internal processes such as explanation and reasoning, without new external input. A systematic account of the cognitive mechanisms behind these capabilities, and of their limits, remains underdeveloped. This paper proposes a Cognitive LbT Framework that maps four…

## 77. Evaluating LLM-Generated World Models for Neuro-Symbolic Reasoning

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reasoning, benchmark, planning
- 作者：Souhaila Djaffal, Amna Jamal, Gagana Madhugiri Devaraja, Anidipta Pal, Jobst Heitzig
- 链接：[arXiv](https://arxiv.org/abs/2611.14419) · [PDF](https://arxiv.org/pdf/2611.14419) · [HF](https://huggingface.co/papers/2611.14419)

Formal world models can support planning, verification, and safety reasoning, but constructing them from open-ended natural-language situations is difficult, particularly in multi-agent settings where several formalizations may be plausible. We study whether five LLMs can generate such world models as partially observable stochastic games and whether mechanical validity is sufficient to establish that the resulting…

## 78. ReTrace: Distilling Tool-Using Agents into Planner-Free Workflows

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reasoning, language model, large language
- 作者：Kaiyuan Hou, Yang Ping Kuo, Indranil Bhattacharya, Rohith Nama, Arushi Gupta, Carlos D. Castillo, Prathap Ramachandra, Xiaofan Jiang, Francesco Carbone
- 链接：[arXiv](https://arxiv.org/abs/2611.14492) · [PDF](https://arxiv.org/pdf/2611.14492) · [HF](https://huggingface.co/papers/2611.14492)

Business process automation runs the same Standard Operating Procedure (SOP) again and again on new inputs. Large Language Model (LLM) agents can follow an SOP written in natural language, but they call an LLM to choose every step of every run, which adds latency and cost at scale. We present ReTrace, which turns an SOP and a few logged agent runs into a reusable workflow in which code, not an LLM, selects the next…

## 79. AutoScaffold: AI-Guided Scaffolding for Reinforcement Learning of Language Models

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, reinforcement learning, evaluation, language model, spec
- 作者：Zijian Zhang, Rizhen Hu, Jiangweizhi Peng, Shiyang Li, Sujay Bhatt, Sihan Zeng, Mingyi Hong
- 链接：[arXiv](https://arxiv.org/abs/2611.14515) · [PDF](https://arxiv.org/pdf/2611.14515) · [HF](https://huggingface.co/papers/2611.14515)

Reinforcement learning with verifiable rewards (RLVR) produces rich training experience, yet outcome rewards reduce each attempt to a single number and leave most of this information unused. Training-time scaffolds, such as strategies or hints added to the prompt during training, offer a natural way to turn this information into guidance, but their design and adaptation are largely left to humans and tailored to…

## 80. Benchmarking LLM Next-Step Recommendations with Knowledge Space Theory

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, spec
- 作者：Peter Steiner, Jan Hochweber
- 链接：[arXiv](https://arxiv.org/abs/2611.13667) · [PDF](https://arxiv.org/pdf/2611.13667) · [HF](https://huggingface.co/papers/2611.13667)

Selecting an LLM for next-step recommendation requires benchmarks that reflect the intended educational task and domain. We present a benchmarking method that uses Knowledge Space Theory (KST) as a formal evaluation reference. Given a task catalogue and an existing prerequisite relation, the method derives admissible knowledge states and the complete set of immediate next steps for each state. Recommendations…

## 81. Walrus Technical Report

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, language model, spec
- 作者：Alkis Koudounas, Osamu Take, Hayato Futami, Quentin Jodelet, Emiru Tsunoo
- 链接：[arXiv](https://arxiv.org/abs/2611.13689) · [PDF](https://arxiv.org/pdf/2611.13689) · [HF](https://huggingface.co/papers/2611.13689)

We present Walrus, a unified 8B speech-and-audio foundation model handling speech recognition (including code-switching and multi-talker speech), speech-to-text and speech-to-speech translation, text-to-speech, emotion recognition, audio captioning, and general audio understanding. Our main contribution is not a new architecture but a data-centric training recipe; we use a standard decoder-only backbone initialized…

## 82. Agentic AI Meets Formal Verification in the Era of Agentic Hardware Development

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reasoning, spec
- 作者：Wenji Fang, Yuchao Wu, Jing Wang, Zhiyao Xie
- 链接：[arXiv](https://arxiv.org/abs/2611.13705) · [PDF](https://arxiv.org/pdf/2611.13705) · [HF](https://huggingface.co/papers/2611.13705)

As AI agents become increasingly capable of generating and optimizing hardware circuits, ensuring the correctness of AI-generated designs becomes more important. Meanwhile, advances in AI lower the barriers to developing and applying formal methods, creating new opportunities to automate and improve hardware verification. This invited paper presents an overview of the methodologies and applications of hardware…

## 83. AutoManifold: Agentic Design of Data Visualisation Algorithms via Manifold Embedding

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, evaluation, spec
- 作者：Burak Susam, Ruiyuan Kang, Tingting Mu
- 链接：[arXiv](https://arxiv.org/abs/2611.13710) · [PDF](https://arxiv.org/pdf/2611.13710) · [HF](https://huggingface.co/papers/2611.13710)

Manifold embedding for data visualisation is dominated by a small set of hand-designed state-of-the-art (SOTA) algorithms. Their design targets are fixed at development time, resulting in inflexible algorithmic behaviour that cannot be readily steered towards user-specified structural priorities. Hand-designing new embedding algorithms to address user priority requires highly specialised expertise and is time…

## 84. Mixed Signals: Weight-Space Programming for EEG and ECG

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, language model, spec
- 作者：Dara Varam, Taraneh Aminosharieh Najafi, David Atienza
- 链接：[arXiv](https://arxiv.org/abs/2611.13758) · [PDF](https://arxiv.org/pdf/2611.13758) · [HF](https://huggingface.co/papers/2611.13758)

Weight-space programming allows language models to read a trained neural network's weights and edit them. This opens the door to ``training'' by reasoning rather than through gradient descent. Prior work has demonstrated its functionality and promise for game-playing networks and fixing specific failures in language models, even extending to diffusion models. In this work, we present its applicability to models…

## 85. CASCADE: Constraint-Aware SCAffolded DEcomposition for Logical Anomaly Detection

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, language model, spec
- 作者：Jinchan Kim, Jinhee Im, Hyunsouk Cho
- 链接：[arXiv](https://arxiv.org/abs/2611.13820) · [PDF](https://arxiv.org/pdf/2611.13820) · [HF](https://huggingface.co/papers/2611.13820)

Logical Anomaly Detection (LAD) requires verifying whether all category-specific constraints, such as object counts, pairing relations, and measurement ranges, are satisfied by a query image given only a few normal references. Recent LAD methods based on Large Vision-Language Models (LVLMs) formulate this as checklist verification, decomposing the decision into independent textual checks. This decomposition,…

## 86. Ceci n'est pas une pipe -- Toward a Symbolic Solver for the Abstraction and Reasoning Corpus Using Evolutionary Computation

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, benchmark, spec
- 作者：Luca Favole, Giorgio Mongardi, Giovanni Squillero, Alberto Tonda
- 链接：[arXiv](https://arxiv.org/abs/2611.13831) · [PDF](https://arxiv.org/pdf/2611.13831) · [HF](https://huggingface.co/papers/2611.13831)

The Abstraction and Reasoning Corpus (ARC) is a benchmark designed to assess the capability of Artificial Intelligence (AI) systems to generalize starting from a few samples, a task humans excel at. The ARC-AGI contests held since 2020 have been the focus of intense competition, with participants proposing approaches ranging from traditional symbolic AI to Transformer architectures. Despite a long history of…

## 87. Towards Text-Only Remote Sensing Scene Classification via Semantic Proxy

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, language model, spec
- 作者：Xianping Ma, Kunlin Wu, Xiaofeng Liu, Xiaokang Zhang, Yuanxin Ye
- 链接：[arXiv](https://arxiv.org/abs/2611.13851) · [PDF](https://arxiv.org/pdf/2611.13851) · [HF](https://huggingface.co/papers/2611.13851)

Remote sensing scene classification (RSSC) is traditionally formulated as a vision-centric problem, where inference relies on rich visual representations extracted from images. In this work, we revisit this assumption by introducing text-only RSSC, a new problem setting that investigates whether remote sensing scenes can be recognized using only textual semantic representations. To enable this study, we propose…

## 88. Spatial-Spectral Coupling as Attention: Scaling Shape Correspondence to High-Resolution Surfaces

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, benchmark, spec
- 作者：Bence Demeter, Kilian Ehrenreich, Amelie Kleber, Ioana Oprisiu, Philipp Spohn, Christian Wachinger, Fabian Bongratz, Lennart Bastian
- 链接：[arXiv](https://arxiv.org/abs/2611.13870) · [PDF](https://arxiv.org/pdf/2611.13870) · [HF](https://huggingface.co/papers/2611.13870)

Establishing dense correspondence between high-resolution 3D shapes remains challenging due to the spatial--spectral coupling at the core of many functional-map methods, which grows quadratically with mesh resolution. We observe that this coupling is equivalent to a scaled dot-product attention formulation, with learned descriptors serving as queries and keys and spectral basis functions as values. This connection…

## 89. A 10K drone image dataset with component-level annotations for rooftop photovoltaic inspection

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, spec
- 作者：Penglei Zhang, Wan Zhang, Ruizhe Deng, Bo Chen, Wenhao Duan, Jinhe Zhang, Yanzhen Zhang, Qi Chen, Zhiling Guo, Haoran Zhang, Yuntian Chen
- 链接：[arXiv](https://arxiv.org/abs/2611.13892) · [PDF](https://arxiv.org/pdf/2611.13892) · [HF](https://huggingface.co/papers/2611.13892)

Component-level information supports rooftop photovoltaic (PV) inspection, but recognizing individual components across complex scenes remains challenging. We present PVIS-10K, a dataset of 10,065 drone images with component-level annotations covering 63,632 physical PV modules across 22 rooftop installations. The high-resolution red-green-blue (RGB) images were acquired by unmanned aerial vehicles (UAVs, also known…

## 90. From Counterfactual Edits to Human Narratives: LLM-Driven Interpretations for Recommender System Explanations

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, language model, large language
- 作者：Vojtech Cahlik, Amir Reza Mohammadi, Rodrigo Alves, Pavel Kordik, Eva Zangerle
- 链接：[arXiv](https://arxiv.org/abs/2611.13914) · [PDF](https://arxiv.org/pdf/2611.13914) · [HF](https://huggingface.co/papers/2611.13914)

Recommender systems increasingly influence what users discover and consume online, yet the decision logic behind their outputs often remains opaque. Counterfactual explanation (CFX) methods provide an effective way to show which changes to a user's interaction history would alter a recommendation. In recommendation settings, however, CFXs often require many edits, producing long, low-level lists that are hard for…

## 91. Beyond Proxy Metrics: MLLMs as Human Surrogates for Explainable AI Evaluation

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, language model, large language
- 作者：Eoin M. Kenny, Salim I. Amoukou, Tom Bewley
- 链接：[arXiv](https://arxiv.org/abs/2611.13926) · [PDF](https://arxiv.org/pdf/2611.13926) · [HF](https://huggingface.co/papers/2611.13926)

Explainable AI (XAI) has expanded into a broad and impactful research area, but the fundamental question of how best to evaluate explanation techniques has proven frustratingly elusive. Methodologies typically revolve around either proxy metrics which tell us little about the utility of an explanation, or human evaluation which---while generally considered the gold standard---is expensive, difficult to scale, and…

## 92. From Attack Surface to Defense Architecture: Compositional Security for Agentic Coding Harnesses

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, language model, coding
- 作者：Simon Hegelich, Bardh Prenkaj, Habiba Sarhan, Morteza Shahrezaye, Kolja Hegelich, Christian Montag, Ralf Schneider, Erik Cambria
- 链接：[arXiv](https://arxiv.org/abs/2611.13960) · [PDF](https://arxiv.org/pdf/2611.13960) · [HF](https://huggingface.co/papers/2611.13960)

AI coding harnesses couple language models to shells, filesystems, and network sockets, turning the harness into an automated Living-off-the-Land (LotL) platform: once an adversary injects instructions into retrieved content, dual-use binaries such as bash, curl, and find become the payload. We argue that security in agentic systems is a structural property of the cognitive architecture and permission composition…

## 93. Understanding Mixture-of-Experts Language Models Beyond Expert Boundaries

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, language model, spec
- 作者：Zhenhong Zhou, Mao Zheng, Mingyang Song, Qiankun Li, Kun Wang, Junfeng Fang
- 链接：[arXiv](https://arxiv.org/abs/2611.13975) · [PDF](https://arxiv.org/pdf/2611.13975) · [HF](https://huggingface.co/papers/2611.13975)

In Mixture-of-Experts (MoE) models, the nature of expert specialization remains controversial. Reports of domain-associated expert preferences contrast with analyses attributing routing primarily to token identity or syntactic patterns. To clarify these differing accounts, we look beyond expert-level routing to investigate the neuron-level organization of domain-specialized computation using Routing-Aware Magnitude…

## 94. Specify Privacy Yourself: Assessing Inference-Time Personalized Privacy Preservation Ability of Large Vision-Language Models

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, language model, spec
- 作者：Xingqi Wang, Xiaoyuan Yi, Xing Xie, Jia Jia
- 链接：[arXiv](https://arxiv.org/abs/2611.13997) · [PDF](https://arxiv.org/pdf/2611.13997) · [HF](https://huggingface.co/papers/2611.13997)

Large Vision-Language Models (LVLMs) have demonstrated remarkable capabilities but raise significant privacy concerns due to their abilities to infer sensitive personal information from images with high precision. While current LVLMs are relatively well aligned to protect universal privacy, e.g., credit card data, we argue that privacy is inherently personalized and context-dependent. This work pivots towards a…

## 95. LUMIR: Decoupled Multimodal Representation Learning from Heterogeneous Data for Next-POI Recommendation

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：language model, large language, spec
- 作者：Zehui Wang, Wolfram Höpken, Dietmar Jannach
- 链接：[arXiv](https://arxiv.org/abs/2611.14004) · [PDF](https://arxiv.org/pdf/2611.14004) · [HF](https://huggingface.co/papers/2611.14004)

As multimodal tourism-related information collected from heterogeneous data sources has become increasingly available, learning effective representations has attracted attention for improving recommendation performance. Existing approaches often tightly couple multimodal fusion with the architecture and optimization objective of a specific downstream model, which limits the generality and reusability of the learned…

## 96. Interleaving anatomical inspection and diagnostic reasoning for explainable radiology report generation

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, evaluation, spec
- 作者：Chentao Huang, Runlong Lin, Zhijun Wang, Yunxiang Li, Yuanyuan Sun, Jian Wang, Hongfei Lin, Ling Luo
- 链接：[arXiv](https://arxiv.org/abs/2611.14018) · [PDF](https://arxiv.org/pdf/2611.14018) · [HF](https://huggingface.co/papers/2611.14018)

Automated radiology report generation can draft clinically plausible reports, yet the pathway from visual evidence to reported findings remains opaque, leaving the diagnostic basis of these reports unexplained and the generated reports difficult to review or revise. We introduce ARIVE (Anatomy-guided Reasoning with Interleaved Visual Evidence), an explainable report generation framework that interleaves anatomical…

## 97. Program-Aided Patchable Skill Evolution

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, benchmark, coding
- 作者：Jiahao Wang, Yuqi Xiong, Qing Yang, Zhipeng Xu, Zhenghao Liu, Zulong Chen, Yubin Bao
- 链接：[arXiv](https://arxiv.org/abs/2611.14019) · [PDF](https://arxiv.org/pdf/2611.14019) · [HF](https://huggingface.co/papers/2611.14019)

Agent skills have emerged as an effective means of enabling LLM agents to solve complex, interactive tasks by encoding reusable knowledge without modifying model parameters. Recent approaches further improve skill adaptation by distilling reusable experience from agent execution trajectories and evolving skills based on downstream task feedback. However, existing methods primarily represent skills as natural…

## 98. ScaleBrain: A Scale-Consistent Framework for EEG Foundation Models

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, spec
- 作者：Minyu Zhou, Yajing Wu, Yongqiang Tang, Wang Jia, Wensheng Zhang
- 链接：[arXiv](https://arxiv.org/abs/2611.14035) · [PDF](https://arxiv.org/pdf/2611.14035) · [HF](https://huggingface.co/papers/2611.14035)

Foundation models pre-trained on large unlabeled electroencephalography (EEG) corpora have emerged as a transformative paradigm for Brain-Computer Interface (BCI) applications. Recent EEG foundation models have shown that multi-scale representations derived from fixed-length patches can improve EEG representation learning. Existing frameworks commonly construct temporal scales through feature-level operations.…

## 99. MISO-BR: An Open Corpus for Misogyny Detection in Brazilian Portuguese

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：language model, large language, coding
- 作者：Fábio A. S. Passos, Péricles B. C. Miranda, Ana Paula Cavalcanti
- 链接：[arXiv](https://arxiv.org/abs/2611.14036) · [PDF](https://arxiv.org/pdf/2611.14036) · [HF](https://huggingface.co/papers/2611.14036)

Misogyny is among the most prevalent forms of online hate speech directed at Brazilian users, yet open and auditable resources dedicated to it in Brazilian Portuguese remain scarce. We introduce MISO-BR, an open, documented and versioned corpus of 896 balanced social media texts annotated for binary misogyny, released with its construction protocol and reproducible baselines. The corpus combines lexicon- and…

## 100. Can KV Cache Be Reused Across Model Updates? A DeepSeek-V4-Flash Case Study

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, language model, retrieval
- 作者：Zhikun Tao, Fangyong Jin, Junping Zhao
- 链接：[arXiv](https://arxiv.org/abs/2611.14051) · [PDF](https://arxiv.org/pdf/2611.14051) · [HF](https://huggingface.co/papers/2611.14051)

Reusing key--value (KV) caches across language model updates could avoid repeated computation of shared context, but changes in model weights raise a fundamental question about what these caches preserve. We investigate direct cache reuse across four model updates, with a detailed study of DeepSeek-V4-Flash to Flash-0731. Our central finding is that caches can retain useful task information without faithfully…

## 101. HandsOnAid: Building and Evaluating an Offline First-Aid Assistant for Emergency Response Scenarios

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, language model, retrieval
- 作者：Rezwan Islam Salvi, Saiyma Sittul Muna, Mushfiqur Rahman Mushfique
- 链接：[arXiv](https://arxiv.org/abs/2611.14059) · [PDF](https://arxiv.org/pdf/2611.14059) · [HF](https://huggingface.co/papers/2611.14059)

Emergencies can occur where there is no phone signal and no ambulance nearby. A small language model on a phone can be helpful in such situations, but its advice needs to be safe and accurate. We built HandsOnAid, a 4-bit Gemma 2B model fine-tuned with QLoRA on FirstAidQA dataset, a corpus of 5,550 first-aid question-answer pairs. We compared seven configurations, including the base, 4-bit and 8-bit fine-tuned…

## 102. What a CAGE 4 Score Measures: An Audit of a Learned Cyber-Defense Benchmark, Its Reference Defenders, and the Tables Built on Them

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, evaluation, benchmark
- 作者：James Rice, Ji Hwan Park, Andres Kwasinski
- 链接：[arXiv](https://arxiv.org/abs/2611.14068) · [PDF](https://arxiv.org/pdf/2611.14068) · [HF](https://huggingface.co/papers/2611.14068)

CAGE Challenge 4 is the benchmark on which learned multi-agent cyber defenders are compared. We reproduce its two reference defenders, KEEP and H-MARL Expert, in a pinned container and show that three things read from it measure less than they are taken to measure. First, the simulator silently discards any action asserted for an agent whose previous action is still running, and charges one point for a discarded…

## 103. From Bias to Positionality: A critical grammar for Large Language Models

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, language model, large language
- 作者：Dave Murray-Rust, Elisa Giaccardi, Federico Bomba, Maria Luce Lupetti
- 链接：[arXiv](https://arxiv.org/abs/2611.14079) · [PDF](https://arxiv.org/pdf/2611.14079) · [HF](https://huggingface.co/papers/2611.14079)

Bias has become a default lens for understanding what machine learning systems do and how we should relate to them. Bias is at root a deviation from a standard; in decision making systems we can supply a standard from outside: a law, a protected attribute, a benchmark, a statistical property. However, even there, biased is often used as a shorthand, without stating what the position taken is - a silent ``relative…

## 104. Model-Free Runtime Measurement of Task-Relevant Information

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reinforcement learning, spec
- 作者：Dimitris Panagopoulos, Adolfo Perrusquía, Yang Xing, Weisi Guo
- 链接：[arXiv](https://arxiv.org/abs/2611.14111) · [PDF](https://arxiv.org/pdf/2611.14111) · [HF](https://huggingface.co/papers/2611.14111)

Autonomous systems increasingly monitor physical kinematics, environmental states and task completion outcomes. While existing work provides methods to plan information seeking actions and interpret acquired observations, current approaches do not monitor whether the live process of information gathering is functioning properly. Consequently, such systems can remain operationally active without resolving outstanding…

## 105. TAMEing the Open-World Personalization: Towards Open-Set Personalized MLLM Assistant

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：language model, large language, spec
- 作者：Rongpei Hong, Jian Lang, Ting Zhong, Fan Zhou
- 链接：[arXiv](https://arxiv.org/abs/2611.14118) · [PDF](https://arxiv.org/pdf/2611.14118) · [HF](https://huggingface.co/papers/2611.14118)

Personalizing Multimodal Large Language Models (MLLMs) as intelligent assistants has recently emerged as an active research topic, where an MLLM is expected to go beyond generic, one-size-fits-all replies, and instead generate responses grounded in user-specific objects, entities, and concepts encountered during interactions. Nevertheless, existing studies mainly focus on personalizing MLLMs on a static, predefined…

## 106. CroCoMAE: Cross-modal self-supervised collaborative representation learning for SAR-optical remote sensing data

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, spec
- 作者：Vito Recchia, Giuseppe Guarino, Cássio Fraga Dantas, Giuseppina Andresini, Annalisa Appice, Dino Ienco
- 链接：[arXiv](https://arxiv.org/abs/2611.14124) · [PDF](https://arxiv.org/pdf/2611.14124) · [HF](https://huggingface.co/papers/2611.14124)

Remote sensing increasingly captures the Earth's surface through complementary sensors such as SAR and optical, yet ground-truth annotations remain scarce, limiting supervised approaches. Self-supervised learning (SSL) addresses the label scarcity, and cross-modal SSL further exploits the complementarity between co-located sensors, but existing cross-modal frameworks align modalities mostly through global…

## 107. Hierarchical Graph Representation Learning with Pooling-Induced Substructures

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, evaluation, benchmark
- 作者：Luca Sbicego, Xiaowen Dong, Dorina Thanou
- 链接：[arXiv](https://arxiv.org/abs/2611.14126) · [PDF](https://arxiv.org/pdf/2611.14126) · [HF](https://huggingface.co/papers/2611.14126)

Hierarchical graph-level tasks that require reasoning over substructures that extend beyond local neighborhoods are posing challenges for standard Graph Neural Networks (GNNs). While graph pooling aims to address this by coarsening graphs into hierarchical representations, existing methods often fail to explicitly preserve the substructures they induce, leading to inconsistent empirical performance. Moreover,…

## 108. DailyWildfireCAN: A Dataset and Benchmark for Next-Day Wildfire Spread Prediction in Canada

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, spec
- 作者：Mahacine Ettahri, Hager Radi Abdelwahed, Toluwaleke Olutayo, Daniel Aloise, Gaétan Marceau Caron
- 链接：[arXiv](https://arxiv.org/abs/2611.14207) · [PDF](https://arxiv.org/pdf/2611.14207) · [HF](https://huggingface.co/papers/2611.14207)

Wildfires represent a critical ecological and socio-economic challenge in Canada, where vast boreal forests and a warming climate have amplified the frequency and severity of extreme fire seasons. Predicting next-day wildfire spread can support fire management, but requires capturing complex interactions among weather, fuels, and terrain. Deep learning has emerged as a promising approach to learning these…

## 109. Verifiable Agentic Traffic Class: A Policed Quality-of-Service Mechanism for Agentic AI Traffic, Evaluated from Simulation to Real-Kernel Adversarial Testing

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, language model, large language
- 作者：Naveen Babu Narayanan Nair, Sajay Kurup
- 链接：[arXiv](https://arxiv.org/abs/2611.14211) · [PDF](https://arxiv.org/pdf/2611.14211) · [HF](https://huggingface.co/papers/2611.14211)

Software agents built on large language models generate traffic unlike human web traffic, yet routers have no class for it and cannot verify a sender's claim to be an agent. This paper proposes the Verifiable Agentic Traffic Class (VATC), which combines a reserved Differentiated Services Code Point (DSCP) value declaring agent traffic, a router-side classifier that demotes flows contradicting the declaration to a…

## 110. Federated Learning for Cross-Regional Epidemic Forecasting with Asynchronous Outbreaks

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, benchmark, spec
- 作者：Ruibin Liu, Francisco Fernandes, Xuanfeng Li, Zige Liu, André Salgado, Chitin Hon, Zifeng Yang, Arlindo Oliveira, Ana Teresa Freitas
- 链接：[arXiv](https://arxiv.org/abs/2611.14272) · [PDF](https://arxiv.org/pdf/2611.14272) · [HF](https://huggingface.co/papers/2611.14272)

Objective: Epidemic outbreaks are often asynchronous across regions, yet collaborative forecasting is hampered by privacy laws and heterogeneous public health interventions. We developed and evaluated, as a proof of concept, a federated learning (FL) framework for cross-regional COVID-19 forecasting under asynchronous outbreaks among Guangdong, Macau, and Portugal, while maintaining data sovereignty. Methods: Using…

## 111. AI Isn't Getting Dumber, We're Getting Pickier: Rising Standards in Human Evaluation of Large Language Models

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, language model, large language
- 作者：Zihan Chen, Lei Nico Zheng, Di Zhu
- 链接：[arXiv](https://arxiv.org/abs/2611.14333) · [PDF](https://arxiv.org/pdf/2611.14333) · [HF](https://huggingface.co/papers/2611.14333)

Users often complain that AI assistants such as ChatGPT are getting worse. Some versions do change, but human evaluation leaves a second possibility untested: the people judging may change. We separate the two on Chatbot Arena, a public platform where people compare answers from two anonymous large language models (LLMs) and pick the better one or say both are bad. We study 1,260,967 blind votes cast from May 2023…

## 112. CLADE: Category-Level Answering from Deficient Evidence in Retrieval-Augmented Language Models

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：language model, spec, retrieval
- 作者：S M Rayeed, Charles V. Stewart, Yao Ma
- 链接：[arXiv](https://arxiv.org/abs/2611.14355) · [PDF](https://arxiv.org/pdf/2611.14355) · [HF](https://huggingface.co/papers/2611.14355)

Retrieval-augmented systems often retrieve passages that are accurate and relevant but state the answer at a coarser level of granularity than the question requires. For example, a question may ask which specific disease a drug treats (familial hyperlipidemia), while the retrieved passage mentions the broader disease family (hyperlipidemia). Prior work on context sufficiency treats such coarse passages simply as…

## 113. EngineAgent: Agentizing On-Device LLM Inference Engines with Inference Stack Hierarchy Awareness and Hardware Abilities

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, coding, spec
- 作者：Zhengxiang Huang, Yujie Sun, Shengheng Chen, Zhaode Wang, Chaoyue Niu, Zeyu Zhao, Chengfei Lv, Fan Wu, Guihai Chen
- 链接：[arXiv](https://arxiv.org/abs/2611.14356) · [PDF](https://arxiv.org/pdf/2611.14356) · [HF](https://huggingface.co/papers/2611.14356)

Rapidly evolving LLM architectures and heterogeneous mobile hardware make supporting new models in on-device inference engines a recurring and costly system challenge. Each model may require coordinated changes across conversion, graph construction, operators, and hardware backends. Existing coding agents often miss these cross-layer dependencies and struggle to diagnose failures across host--device execution paths.…

## 114. ARE-bench: Benchmarking Agents' Research Ability in Real-World Researcher Sessions and Workspaces

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, benchmark, spec
- 作者：Jiahang Lin, Wanying Ren, Wanghan Xu, Huayu Sha, Yang Shu, Zhonghang Lu, Chengjun Pan, Yi Dong, Shichun Liu, Yuyang Hu, Shihan Dou, Honglin Guo, Huijie Lv, Pujun Zheng, Zhe Sun, Yuankai Ying, Yiding Wang, Jiahao Chen, Zhixiong Yang, Dingbo Yuan, Yicheng Zou, Zhecan Wang, Guoxiu He, Xiaoyu Xing, Qi Zhang, Tao Gui, Xuanjing Huang
- 链接：[arXiv](https://arxiv.org/abs/2611.14364) · [PDF](https://arxiv.org/pdf/2611.14364) · [HF](https://huggingface.co/papers/2611.14364)

Research agents achieve increasingly strong benchmark scores, yet these scores do not necessarily translate into reliable delivery in ongoing research projects. Many research-agent benchmarks emphasize standalone tasks and relatively self-contained workflows in clean or curated workspaces. However, researchers ask agents to complete one step within an ongoing project, where requests depend on earlier session…

## 115. An Energy-Based Perspective on Machine Learning

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reinforcement learning, spec, planning
- 作者：Bo Dai, Yilun Du
- 链接：[arXiv](https://arxiv.org/abs/2611.14383) · [PDF](https://arxiv.org/pdf/2611.14383) · [HF](https://huggingface.co/papers/2611.14383)

Energy-based models (EBMs) define a distribution through a scalar energy, $p_θ(x)\propto\exp(-E_θ(x))$, and are usually presented as one model family among many. This tutorial has a broader goal: beyond introducing EBMs, it uses them as a single lens that connects the different aspects of machine learning. Any EBM is specified by three choices, the energy, which determines what the model represents; the inference…

## 116. REAL Loss: Optimizing Real Expected Acceptance Length for Speculative Decoding

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, coding, spec
- 作者：Yu Tian
- 链接：[arXiv](https://arxiv.org/abs/2611.14399) · [PDF](https://arxiv.org/pdf/2611.14399) · [HF](https://huggingface.co/papers/2611.14399)

Speculative decoding accelerates LLM inference by having a draft model propose multiple tokens for the target model to verify in one pass. The speedup is governed by the expected acceptance length (EAL), yet standard training objectives such as cross-entropy, KL divergence, and total variation focus only on distribution matching or single-step overlap. Recent studies instead propose block-level training objectives,…

## 117. Precision on Demand: Escalating Weight Bits at Uncertain Decoding Steps in a Small Local Model

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, coding, spec
- 作者：Mohammed Nayeem Khan, Logesh L, Aliyas Ahmad Misri
- 链接：[arXiv](https://arxiv.org/abs/2611.14418) · [PDF](https://arxiv.org/pdf/2611.14418) · [HF](https://huggingface.co/papers/2611.14418)

Local decoding usually fixes one weight precision for the whole generation. We study a different allocation: store 8-bit weights, decode with their top 4 bits, and redo a step at 8 bits only when the low-precision output distribution looks uncertain (entropy above a threshold or a small top-two margin). Quantization is simulated, the model is Qwen3-0.6B, and the benchmark is GSM8K. Cost is counted in weight bytes…

## 118. OnlyAct: Extracting Action Representations from Foundation Models for World Models

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, spec
- 作者：Runjia Li, Minghao Chen, Junyu Xie, Philip Torr, Andrea Vedaldi, Tomas Jakab
- 链接：[arXiv](https://arxiv.org/abs/2611.14420) · [PDF](https://arxiv.org/pdf/2611.14420) · [HF](https://huggingface.co/papers/2611.14420)

Video world models promise general-purpose interactive simulators, but their training is limited by action supervision: action labels are scarce, fragmented across incompatible specifications, and do not scale with the unlabeled video pretraining corpus. A common workaround jointly trains an action encoder to compress consecutive frames into a latent action and a decoder to reconstruct the next frame from the…

## 119. Two Communities, One Problem: Branch-and-Bound vs. A* for Resource-Constrained Project Scheduling

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, benchmark, spec
- 作者：Izack Cohen, Dominik Kress, Lara Nehrke, Erwin Pesch, Shimrit Shtern
- 链接：[arXiv](https://arxiv.org/abs/2611.14426) · [PDF](https://arxiv.org/pdf/2611.14426) · [HF](https://huggingface.co/papers/2611.14426)

Branch-and-Bound (B&B) and $A^*$ are popular exact search methods originating from Operations Research and Artificial Intelligence, respectively. Although the two methods share fundamental search principles, their different ways of exploring the search space can lead to substantially different computational performance. We investigate these differences using the Resource-Constrained Project Scheduling Problem…

## 120. One Policy for 100 Household Tasks: Our Solution for the 2026 BEHAVIOR Challenge

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, evaluation, coding
- 作者：Ilia Larchenko, Gleb Zarin, Atindra Nair, Keerti Manney, Vitaly Kleban, Mirko Kiefer, Anjana Yodaiken
- 链接：[arXiv](https://arxiv.org/abs/2611.14432) · [PDF](https://arxiv.org/pdf/2611.14432) · [HF](https://huggingface.co/papers/2611.14432)

We describe our solution for the 2026 BEHAVIOR Challenge: 100 long-horizon household tasks in the OmniGibson simulator. We placed 9th on the final leaderboard, the only independent team in the top 10. The core of the solution is a single vision-language-action (VLA) model, one checkpoint for all 100 tasks, built on our 1st-place 2025 solution, which is based on $π_{0.5}$. On the 50 tasks shared with 2025, its Q…
