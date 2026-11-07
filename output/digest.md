# 每日 AI 论文

生成时间：2026-11-07 05:58 UTC  ·  共 120 篇（已按 arXiv ID 去重）

来源：Hugging Face Daily Papers + arXiv（cs.AI / cs.LG / cs.CL / cs.CV）。
排序：HF 上榜、点赞、多源命中、兴趣词。兴趣词可在 `config.json` 改。

## 1. VFlash: Fast, Accurate Visual Planning via Flash Primitive Decoding

- 分数：38.0  ·  HF 赞：96  ·  来源：huggingface + arxiv
- 兴趣命中：language model, coding, planning
- 作者：Yu-Cheng Chou, Shihao Wang, Jin Huang, Chi-Pin Huang, Chiao-An Yang, Xianzhe Fan, Jing Wang, Zhiqi Li, Yuanguo Kuang, Ruijie Zheng, Johan Bjorck, Sifei Liu, Hang Su, Abhishek Badki, Lei Zhang, Alan Yuille, Linxi &#34;Jim&#39;&#39; Fan, Jan Kautz, Zhiding Yu
- 链接：[arXiv](https://arxiv.org/abs/2611.08449) · [PDF](https://arxiv.org/pdf/2611.08449) · [HF](https://huggingface.co/papers/2611.08449)

Models for physical AI tasks, such as robotics and autonomous driving, need not reason solely in language. They can use visual plans--points, bounding boxes, and trajectories--to represent spatial goals and anticipate motion. However, autoregressive vision-language models generate these plans one coordinate token at a time, making richer predictions increasingly costly. We introduce VFlash, a method for fast,…

## 2. Harness-S: Learning from Sibling Harnesses for Generalizable Agent Training

- 分数：34.0  ·  HF 赞：55  ·  来源：huggingface
- 兴趣命中：agent, reinforcement learning, spec
- 作者：Kangning Zhang, Wenxiang Jiao, Bowen Fang, Shuai Shao, Jiachen Zhu, Rong Shan, Shijian Wang, Hao Wang, Yuan Lu, Weiwen Liu, Weinan Zhang
- 链接：[arXiv](https://arxiv.org/abs/2611.04277) · [PDF](https://arxiv.org/pdf/2611.04277) · [HF](https://huggingface.co/papers/2611.04277)

Harness evolution from a common base exhibits Locality, Complementarity, and Nonstationarity: variants repair different failures, and their utility changes as the policy learns. Rather than seeking a universally superior harness, we introduce Harness-S to selectively rescue failures of a base execution system through sibling harnesses and transfer the resulting capabilities into a single policy that remains…

## 3. Random Is Almost Enough? Stable and Low-Cost Benchmark Compression via BestRand

- 分数：34.0  ·  HF 赞：50  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark
- 作者：George Ling, Shanshan Zhong, Lijin Yang, Hao Yang, Nanxiang Li, Zhongzhan Huang
- 链接：[arXiv](https://arxiv.org/abs/2611.00883) · [PDF](https://arxiv.org/pdf/2611.00883) · [HF](https://huggingface.co/papers/2611.00883)

Benchmark compression reduces the often prohibitive time and cost of model evaluation by evaluating models on a small benchmark subset that closely matches full-benchmark results. To quantify estimation error, we derive an accurate analytical approximation to the error distribution when estimating full-benchmark scores from a subset, showing that most subsets yield small errors, while a few produce much larger…

## 4. WeLM-Image: A Unified Image Generation Model towards Visual Intelligence

- 分数：31.5  ·  HF 赞：39  ·  来源：huggingface
- 兴趣命中：evaluation, spec
- 作者：Canmiao Fu, Chen Li, Guohui Zhang, Hao Lu, Hongyang Wei, Huadong Wu, Huaisong Zhang, Hubery Yin, Liyuan Cui, Qixin Yan, Tong Shao, Xiaoqiang Zhou, Xinhang Leng, Ying Zhang, Zhenhai Liu, Zhipeng Huang
- 链接：[arXiv](https://arxiv.org/abs/2611.07392) · [PDF](https://arxiv.org/pdf/2611.07392) · [HF](https://huggingface.co/papers/2611.07392)

We present WeLM-Image, a unified image foundation model that integrates multimodal understanding into text-to-image generation, instruction-guided editing, and multi-reference synthesis. Designed for single-GPU deployment in WeChat's large-scale consumer applications, the model processes text, reference images, and target latents as one interleaved sequence. A Mixture-of-Transformers (MoT) backbone combines shared…

## 5. TailSteer: Trajectory-Tail Steering for Drift-Resistant Multi-turn Image Editing

- 分数：30.5  ·  HF 赞：37  ·  来源：huggingface
- 兴趣命中：benchmark, spec
- 作者：Ruikang Li, Zixuan Chen, Jiarui Wu, Mingde Yao, Yiyuan Zhang, Yujin Wang, Hanming Deng, Lewei Lu, Tianfan Xue
- 链接：[arXiv](https://arxiv.org/abs/2611.06741) · [PDF](https://arxiv.org/pdf/2611.06741) · [HF](https://huggingface.co/papers/2611.06741)

Strong single-turn editing performance does not guarantee reliable multi-turn interaction: as edited outputs are repeatedly reused, small unintended changes can accumulate into severe visual drift. This long-term drift is often mitigated through training on multi-turn data or cross-turn rollouts, potentially altering pretrained priors, or through specialized inference-time mechanisms that are difficult to scale to…

## 6. SLA: Scaling Spatial-Language-Action Model via Continual Pre-training

- 分数：30.0  ·  HF 赞：120  ·  来源：huggingface
- 兴趣命中：spec
- 作者：Fuhao Li, Wenxuan Song, Qizhou Huang, Ziyang Zhou, Jingbo Wang, Junwu E, Pengwei Wang, Yan Wang, Shunbo Zhou, Haoang Li
- 链接：[arXiv](https://arxiv.org/abs/2611.08373) · [PDF](https://arxiv.org/pdf/2611.08373) · [HF](https://huggingface.co/papers/2611.08373)

Reliable robotic manipulation requires both semantic understanding and precise control in three-dimensional space. However, vision-language-action (VLA) foundations largely inherit visual representations from 2D vision-language pre-training, while spatial supervision is often introduced only during task-specific adaptation. Developing spatial understanding as a transferable foundation-model capability therefore…

## 7. Towards Foundation Decision Models: Drex

- 分数：29.5  ·  HF 赞：19  ·  来源：huggingface + arxiv
- 兴趣命中：agent, reasoning, reinforcement learning, language model, large language, coding
- 作者：Nischay Dhankhar, Alisher Amantay, Zhanibek Datbayev, Darkhan Akhmetov, Yash Shah, Nurmukhamed Ubaidullayev, Raman Saparkhan, Dos Baha, Abulhair Saparov
- 链接：[arXiv](https://arxiv.org/abs/2611.07854) · [PDF](https://arxiv.org/pdf/2611.07854) · [HF](https://huggingface.co/papers/2611.07854)

Autoregressive approaches with large language models, such as long chain-of-thought reasoning, have become the default for new AI applications because they reach higher accuracy on a wide range of tasks. In production, however, they give inconsistent answers, require parsing of outputs, and add cost and latency. Decision models address this: given a question and a set of options supplied by the user, they return a…

## 8. EvoMemState: Evolving Memory State for Personal Agents

- 分数：26.0  ·  HF 赞：20  ·  来源：huggingface
- 兴趣命中：agent, memory, reasoning, reinforcement learning, benchmark, language model, large language, spec, retrieval
- 作者：Zhishang Xiang, Yunbo Tang, Zhongqiao Liu, Junkai Chen, Zerui Chen, Qingguo Hu, Yuxuan Zhang, William Grant, Qinggang Zhang, Jinsong Su
- 链接：[arXiv](https://arxiv.org/abs/2611.03743) · [PDF](https://arxiv.org/pdf/2611.03743) · [HF](https://huggingface.co/papers/2611.03743)

Long-term memory enables large language model (LLM) agents to provide continuous personalized assistance by retaining user information across interactions. Existing systems support this process through fact extraction, organization, updating, and retrieval, but largely maintain memories as independent facts. This fact-centric paradigm may overlook how new facts update, constrain, or conflict with earlier ones, while…

## 9. NPCBench: A Clinical Apprenticeship Benchmark for Multimodal Care-Pathway Reasoning in Nasopharyngeal Carcinoma

- 分数：21.0  ·  HF 赞：2  ·  来源：huggingface + arxiv
- 兴趣命中：reasoning, evaluation, benchmark, spec, planning
- 作者：Pengkai Wang, Wei-Wei Zhang, Yan Li, Min Tang, Zhitian Hou, Zeyu Liu, Guanghao Zhu, Yuanyi Wang, Yanggan Gu, Wenjun Wang, Minheng Ni, Congkai Xie, Zhijie Sang, Jianmin Wu, Ying Sun, Hongxia Yang
- 链接：[arXiv](https://arxiv.org/abs/2611.08369) · [PDF](https://arxiv.org/pdf/2611.08369) · [HF](https://huggingface.co/papers/2611.08369)

Current medical benchmarks typically break down clinical competence into isolated factual questions, single-image tasks, or static case vignettes. These tests score individual answers, but reveal less about whether a model can integrate subspecialty knowledge with multimodal evidence and track a patient's condition throughout a course of care. To close this gap, we introduce NPCBench, a clinical apprenticeship…

## 10. VisSearch-Bench: Evaluating Long Horizon Visual Search in Multimodal Agents

- 分数：20.5  ·  HF 赞：17  ·  来源：huggingface
- 兴趣命中：agent, retrieval
- 作者：ZhengXian Wu, Qianhao Nie, Zhuohong Chen, Junjie Gao, Yuyao Zhang, Yunyao Yu, Hangrui Xu, Cheng Cheng, Guiyu Ma, Jin Zhang, Xingzhong Xu, Kai Yang, Haoqian Wang
- 链接：[arXiv](https://arxiv.org/abs/2611.04894) · [PDF](https://arxiv.org/pdf/2611.04894) · [HF](https://huggingface.co/papers/2611.04894)

Multimodal agents use web and image tools to answer questions beyond their internal knowledge. Some search tasks use images mainly to identify an initial entity, then rely on text retrieval. These tasks offer limited insight into how agents connect information across images, objects, and search steps. We therefore focus on visual context management. This involves organizing and using visual information and linking…

## 11. On the Opportunities and Challenges of Prefill-to-Autoregressive Cross-Model Transfer

- 分数：20.0  ·  HF 赞：12  ·  来源：huggingface
- 兴趣命中：benchmark, language model, coding
- 作者：Zhenyi Shen, Junru Lu, Wei Liu, Jiangnan Ye, Jiazheng Li, Di Yin, Xing Sun, Tameem Adel, Yali Du, Lin Gui, Yulan He
- 链接：[arXiv](https://arxiv.org/abs/2611.06976) · [PDF](https://arxiv.org/pdf/2611.06976) · [HF](https://huggingface.co/papers/2611.06976)

Prefill-to-Autoregressive Cross-model Transfer (PACT), a form of latent communication between language models, combines a larger model's prompt representations with a smaller model's efficient generation, offering a promising way to balance capability and inference cost. However, existing systems provide limited support for independently evaluating large-small model collaboration, and improved task performance alone…

## 12. Open-HumanScale: An Open Recipe for Scaling Human and Robot Experience for Embodied Foundation Models

- 分数：19.5  ·  HF 赞：15  ·  来源：huggingface
- 兴趣命中：evaluation, benchmark
- 作者：Juncheng Ma, Jiaxin Li, Jiankai Tu, Bo Liang, Guodong Lv, Yufan Deng, Junzhe Tang, Liangzhu Yang, Chen Bian, Zicong Cao, Baohao Zhu, Jianxin Bi, Tengfei Yan, Yinyuan Zhang, Kewei Zhang, Xinglong Chen, Kaiqi Chen, Duomin Wang, Xiaotian Tang, Liang Tan, Li Li, Yuan Xu, Haosen Yang, Yuqi Wang, Jingfei Xia, Songyan Huang, Zhiyang Dou, Zhen Dong, Enze Xie, Tat-Seng Chua, Daquan Zhou
- 链接：[arXiv](https://arxiv.org/abs/2611.06817) · [PDF](https://arxiv.org/pdf/2611.06817) · [HF](https://huggingface.co/papers/2611.06817)

Egocentric human video offers a scalable source of manipulation priors for robot learning, yet translating raw data scale into generalizable robot policies demands rigorous data curation and training recipes. We introduce Open-HumanScale, the first fully open recipe for scaling egocentric pretraining to 50,000 hours, anchored by Open-HumanScale-50K---a curated egocentric video corpus densely annotated with hand…

## 13. Terminal-style Mathematical Modeling Bench: The First Agentic and Verifiable Benchmark for Mathematical Modeling

- 分数：19.5  ·  HF 赞：7  ·  来源：huggingface + arxiv
- 兴趣命中：agent, benchmark
- 作者：Xiaojun Wu, Cehao Yang, Xuhui Jiang, Chengjin Xu, Jia Li, Jian Guo
- 链接：[arXiv](https://arxiv.org/abs/2611.08237) · [PDF](https://arxiv.org/pdf/2611.08237) · [HF](https://huggingface.co/papers/2611.08237)

Mathematical modeling turns an open-ended real-world problem into assumptions, a model, a solution, and a defended recommendation, and its answers matter only if they are both close to a credible reference and physically feasible; existing benchmarks either score solver fragments or grade reports with an LLM judge, leaving those numbers unchecked. We introduce TB-MathModel (the Terminal-style Mathematical Modeling…

## 14. EDGAR: Efficient Diffusion-Driven Gaussian Avatar Refinement via Synthetic Failure

- 分数：19.0  ·  HF 赞：10  ·  来源：huggingface + arxiv
- 兴趣命中：evaluation
- 作者：Kwan Yun, Minhyeok Bang, Colette Suhjung Koo, Junyong Noh
- 链接：[arXiv](https://arxiv.org/abs/2611.07909) · [PDF](https://arxiv.org/pdf/2611.07909) · [HF](https://huggingface.co/papers/2611.07909)

Recent advances in Gaussian splatting have enabled efficient and photorealistic head avatar reconstruction, yet monocular video-based or image-based methods still suffer from under-constrained geometry and texture, leading to artifacts such as blurring, stretching, and temporal instability. We present EDGAR (Efficient Diffusion-Driven Gaussian Avatar Refinement), a conditional diffusion framework designed to enhance…

## 15. Decode Before You Hear: Speculative Listening for Chunk-Interleaved Full-Duplex Speech Language Models

- 分数：18.5  ·  HF 赞：5  ·  来源：huggingface
- 兴趣命中：benchmark, language model, coding, spec
- 作者：Yutong Bian, Yanglin Zhang, Yuxiang Wang, Luoyuan Zhang, Rongshen He, Zihao Wang, Junwen Qiu, Jiaqi Li, Zhizheng Wu
- 链接：[arXiv](https://arxiv.org/abs/2611.06982) · [PDF](https://arxiv.org/pdf/2611.06982) · [HF](https://huggingface.co/papers/2611.06982)

Chunk-interleaved full-duplex speech language models listen and speak in fixed time chunks, and each chunk must be processed before the next one arrives. Their workload is asymmetric across chunks: listen chunks leave compute idle while awaiting audio, and speak and tool-call chunks require serial generation, which delays responses and tool calls. Using the idle compute for the next chunk requires decoding it before…

## 16. Muir: Linear Attention with Sensitivity-Allocated Gating and Matched-Filter Readout

- 分数：18.5  ·  HF 赞：5  ·  来源：huggingface + arxiv
- 兴趣命中：memory, retrieval
- 作者：Tushaar Gangavarapu, Gil Tabak, Clemens JS Schaefer
- 链接：[arXiv](https://arxiv.org/abs/2611.08376) · [PDF](https://arxiv.org/pdf/2611.08376) · [HF](https://huggingface.co/papers/2611.08376)

Linear attention compresses context into a fixed-size key-value state for linear-time training and constant-memory inference. Gated delta-rule models decay this state and erase its prediction for an incoming key before writing a new value; Gated DeltaNet-2 (GDN-2) generalizes this with channel-wise decay and decoupled, full-rank erase and write gates. However, we show that state updates are far less sensitive to…

## 17. SwarmEvolve: Latent Agent Swarms for Evolutionary Discovery and Optimization

- 分数：17.5  ·  HF 赞：3  ·  来源：huggingface + arxiv
- 兴趣命中：agent, coding
- 作者：Qile Jiang, George Em Karniadakis
- 链接：[arXiv](https://arxiv.org/abs/2611.08483) · [PDF](https://arxiv.org/pdf/2611.08483) · [HF](https://huggingface.co/papers/2611.08483)

LLM-guided evolutionary search uses AI agents to improve programs for mathematical and computational problems by iteratively refining solutions and combining high-scoring methods. However, the process is often slow because the LLM generates a long textual chain of thought for each round and must repeat this generation many times to maintain population diversity. We present SwarmEvolve, a framework in which hundreds…

## 18. OpenFrontiers: A Collection of Open Research Problems and a Benchmark for Scientific Rediscovery

- 分数：17.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark, language model, large language, spec, retrieval
- 作者：Jiarui Yao, Ruida Wang, Tong Zhang
- 链接：[arXiv](https://arxiv.org/abs/2610.37739) · [PDF](https://arxiv.org/pdf/2610.37739) · [HF](https://huggingface.co/papers/2610.37739)

Large language models (LLMs) have shown increasing promise in research-level problem solving, yet a comprehensive collection of such problems is still missing, and evaluating them on research-level problems remains challenging. We introduce OpenFrontiers, a cross-disciplinary resource that combines a structured corpus of open research problems with a retrospective benchmark of recently resolved problems in…

## 19. Decoupled Predictive Decision Making: A Shared Conditional Predictor for Agents

- 分数：17.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：agent, reasoning, benchmark, language model, spec
- 作者：Lang Mo, Xingxuan Zhang, Qi Wang, Mingchao Hao, Hao Yuan, Chunjing Gan, Wang Lu, Peng Cui
- 链接：[arXiv](https://arxiv.org/abs/2611.02075) · [PDF](https://arxiv.org/pdf/2611.02075) · [HF](https://huggingface.co/papers/2611.02075)

Agent decisions depend on empirical relationships that deployment observations reveal and task descriptions alone may leave unresolved. We introduce Decoupled Predictive Decision Making (DPDM), an architecture that formulates heterogeneous agent decisions as conditional prediction with a shared pretrained learner. Language models provide semantic representations of current and historical records, while a…

## 20. SAE Interprets MoE: Sparse AutoEncoders Reveal That MoE Experts Exhibit Human-Interpretable Fine-Grained Specialization

- 分数：16.5  ·  HF 赞：5  ·  来源：huggingface + arxiv
- 兴趣命中：spec
- 作者：Anyuan Zhuo, Shaohua Zhang, Yuan Lin, Pinyan Lu
- 链接：[arXiv](https://arxiv.org/abs/2611.08089) · [PDF](https://arxiv.org/pdf/2611.08089) · [HF](https://huggingface.co/papers/2611.08089)

Mixture-of-Experts (MoE) models route each token to a few of many experts, yet what an individual expert is responsible for remains unsettled. Existing analyses count how often an expert is selected on domain-labeled corpora, an instrument that fixes the taxonomy in advance, stays coarse, and records selection rather than contribution. We instead study specialization in feature space by training a sparse autoencoder…

## 21. Tools Need Not Speak in Text: Latent Context Compression for Agents

- 分数：16.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：agent, benchmark, language model, large language
- 作者：Yuetong Liu, Zhehao Zhou, Yitong Zhang, Haorui Chen, Jia Li
- 链接：[arXiv](https://arxiv.org/abs/2611.06500) · [PDF](https://arxiv.org/pdf/2611.06500) · [HF](https://huggingface.co/papers/2611.06500)

Large language model (LLM) agents typically append raw tool outputs to their context. Over multi-step interactions, long and noisy observations incur substantial context overhead and dilute the agent's attention to task-relevant information. Existing token pruning and summarization methods remain constrained by discrete text representations, limiting the achievable compression ratios.   In this work, we challenge…

## 22. Information Games: Strategic Crowding and Firm Repositioning in Language-Model Space

- 分数：15.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：agent, language model, large language
- 作者：Marcus Gawronsky, Chun-Sung Huang
- 链接：[arXiv](https://arxiv.org/abs/2609.37820) · [PDF](https://arxiv.org/pdf/2609.37820) · [HF](https://huggingface.co/papers/2609.37820)

When firms respond to new market opportunities, their capacity choices alter the future discounted free cash flows available to both competitors and investors. In competitive markets, these investment decisions publicized in news articles and analyst reports, measuring the changes in capital structure, product mix, firm leadership, risk exposure and operating procedure made by the firm. Modern search engines rely on…

## 23. Reducing Representational Interference in Retrieval Embeddings with Trainable Prefix Tokens

- 分数：15.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：benchmark, coding, retrieval
- 作者：Seongtae Hong, Youngjoon Jang, Jungseob Lee, Chanjun Park, Heuiseok Lim
- 链接：[arXiv](https://arxiv.org/abs/2611.07298) · [PDF](https://arxiv.org/pdf/2611.07298) · [HF](https://huggingface.co/papers/2611.07298)

Embedding models compress variable-length text into fixed-size vector representations, but this compression can entangle semantic content with residual token-level information, such as artifacts arising from attention sink behavior. We propose a simple method that prepends trainable [DUMP] tokens to the input during embedding model training. The method keeps the model architecture, pooling strategy, and training…

## 24. From Autonomous Agents to Cognitive Symbionts: Toward AI-Augmented Human Intelligence

- 分数：14.5  ·  HF 赞：5  ·  来源：huggingface
- 兴趣命中：agent, memory
- 作者：Hao Fei
- 链接：[arXiv](https://arxiv.org/abs/2611.05376) · [PDF](https://arxiv.org/pdf/2611.05376) · [HF](https://huggingface.co/papers/2611.05376)

For a decade, progress in artificial intelligence has been measured by how much a machine can do on its own. Large foundation models now write code and run multistep tasks, and personal agents act on a person's behalf. Yet people still forget what they once knew, miss what they are not looking at, fail to find the right words, and face hard choices without the benefit of their own history, because the machine that…

## 25. HeLM: Hierarchical Explicit Language Memory for Non-Markovian Manipulation

- 分数：13.5  ·  HF 赞：7  ·  来源：huggingface
- 兴趣命中：memory
- 作者：Gyeonghun Kim, Donghoon Kim, Minsoo Choi, Suyun Lee
- 链接：[arXiv](https://arxiv.org/abs/2611.02660) · [PDF](https://arxiv.org/pdf/2611.02660) · [HF](https://huggingface.co/papers/2611.02660)

Recent advances in Vision-Language-Action (VLA) models have enabled fine manipulation capabilities, yet performing tasks that require working memory remains a key challenge. Most existing VLA architectures operate under a Markovian assumption, mapping only the current observation to an action, which leads to failure in non-Markovian environments. Inspired by the human 'inner monologue', we propose Hierarchical…

## 26. Identically Trained Language Models Break on Different Jailbreaks

- 分数：12.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：benchmark, language model
- 作者：Chi-Wei Chang, Mu-Tien Kuo, Kuan-Wei Lee, Meng-Hsun Tsai
- 链接：[arXiv](https://arxiv.org/abs/2610.34074) · [PDF](https://arxiv.org/pdf/2610.34074) · [HF](https://huggingface.co/papers/2610.34074)

Jailbreak benchmarks test one checkpoint and treat which jailbreaks break it as a property of its pretraining data and safety training. We ask whether another pretraining run of the same data, given the same safety training, would break on the same jailbreaks. For each of 25 pretraining data recipes, we take 1B base models from 3 pretraining seeds and give each the same safety post-training with 2 post-training…

## 27. Hard Sample-Conditioned Decorrelated Attention for Robust Face Recognition

- 分数：12.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：benchmark, spec
- 作者：Tahar Chettaoui, Guray Ozgur, Eduarda Caldeira, Naser Damer, Fadi Boutros
- 链接：[arXiv](https://arxiv.org/abs/2610.41789) · [PDF](https://arxiv.org/pdf/2610.41789) · [HF](https://huggingface.co/papers/2610.41789)

Multi-head attention in Vision Transformers (ViTs) allows independent attention patterns across heads, but without explicit regularization, heads may learn redundant patterns rather than complementary roles. Correlation-based penalties encourage head disentanglement, yet apply uniform regularization across all training samples. In face recognition (FR), hard samples whose embeddings lie close to competing identities…

## 28. Signed but Steerable: Measuring and Closing the Text-Vector Integrity Gap in Offline Retrieval-Augmented Generation

- 分数：12.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：language model, retrieval
- 作者：Georgios Feretzakis, Alexandros Papaspyridis
- 链接：[arXiv](https://arxiv.org/abs/2611.06498) · [PDF](https://arxiv.org/pdf/2611.06498) · [HF](https://huggingface.co/papers/2611.06498)

Offline retrieval-augmented generation (RAG) on edge devices is updated through signed knowledge packs that carry text and precomputed embedding vectors. A signature proves who published a pack, not that its vectors encode its text. We study this text-vector integrity gap. A verifier that recomputes vectors and accepts them within a cosine tolerance concedes a predictable share of queries to an attacker who controls…

## 29. Future Representation Distillation for Imagination-free World Action Models

- 分数：12.0  ·  HF 赞：8  ·  来源：huggingface
- 兴趣命中：-
- 作者：Jaehyeong Jo, Sangwon Jang, Sihyun Yu, Seonghyeon Ye, Yekyung Nah, Hojung Jung, Kimin Lee, Sung Ju Hwang
- 链接：[arXiv](https://arxiv.org/abs/2611.04527) · [PDF](https://arxiv.org/pdf/2611.04527) · [HF](https://huggingface.co/papers/2611.04527)

World Action Models (WAMs) use the predictive knowledge of pretrained video diffusion models for robot control through future video prediction. However, iterative video denoising is costly, and inaccurate visual predictions can compromise action prediction. Our key idea is to make this predictive knowledge available through visual representations computed from the current observation, enabling action prediction…

## 30. StepX-OPD: Rethinking Multi-Teacher On-Policy Distillation in Diffusion Models

- 分数：11.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：spec
- 作者：Chenru Wang, Xuanyang Zhang, Yucheng Han, Wenbo Nie, Wei Cheng, Xianfang Zeng, Gang YU, Chi Zhang
- 链接：[arXiv](https://arxiv.org/abs/2611.04386) · [PDF](https://arxiv.org/pdf/2611.04386) · [HF](https://huggingface.co/papers/2611.04386)

A deployable text-to-image diffusion model must hold several capabilities at once, such as instruction following, text rendering and human preference, and must sample in a few steps. Capabilities and few-step sampling are built in separate stages: a full-step model first consolidates capabilities through multi-teacher on-policy distillation, then serves as a fixed teacher for step distillation. Every full-step model…

## 31. Towards Real-Time Full-Waveform LiDAR Transformers via Intensity-Guided Token Reduction and Physics-Aware Augmentation

- 分数：11.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：benchmark
- 作者：Kotaro Oishi, Kazuma Ikeda, Ryosei Hara, Ryo Yoshida, Mariko Isogawa, Kentaro Yoshioka
- 链接：[arXiv](https://arxiv.org/abs/2611.07613) · [PDF](https://arxiv.org/pdf/2611.07613) · [HF](https://huggingface.co/papers/2611.07613)

LiDAR is a critical sensor for autonomous driving and robotics, yet it remains vulnerable to adverse conditions such as fog, rain, transparent objects, and low-reflectance surfaces. Full-waveform LiDAR (FWL) addresses these limitations by capturing the complete return waveform as a histogram, preserving rich reflection characteristics including multi-path echoes and weak signals. While recent Transformer-based…

## 32. ReferClaw: Disambiguating User Intent for Egocentric Assistance

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, evaluation, benchmark, spec
- 作者：Hangyu Qin, Junbin Xiao, Angela Yao
- 链接：[arXiv](https://arxiv.org/abs/2611.07683) · [PDF](https://arxiv.org/pdf/2611.07683) · [HF](https://huggingface.co/papers/2611.07683)

Users of egocentric AI assistants often ask short, ambiguous questions whose intended referents cannot be uniquely resolved from video and dialogue history. For example, "Where did I leave it?" may refer to several previously handled objects. Existing VideoQA systems typically commit to a single interpretation, risking plausible but intention-misaligned answers. We introduce ReferClaw, an agentic framework that…

## 33. MCPHallu: Benchmarking Reasoning, Execution, and Memory Hallucinations in MCP Agents

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, memory, reasoning, benchmark, language model, large language, spec
- 作者：Yizhen Jiang, Haowei Guo, Tianyi Bai, Zengjie Hu, Lu Ma, Zhengyang Zhao, Haoze Sun, Peng Pei, Wentao Zhang
- 链接：[arXiv](https://arxiv.org/abs/2611.07689) · [PDF](https://arxiv.org/pdf/2611.07689) · [HF](https://huggingface.co/papers/2611.07689)

Large language model agents are increasingly deployed through the Model Context Protocol (MCP), which allows them to discover and invoke tools across multiple servers at runtime. Existing MCP benchmarks primarily measure task completion; where they diagnose failures, they do so after execution rather than building specific reasoning, execution, and memory failure risks into task construction. We introduce MCPHallu,…

## 34. CAMP: Context-Aware Mapping and Placement for LLMs on 3D-IMC Arrays

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, language model, large language, spec
- 作者：Orhun Görkem, Athanasios Vasilopoulos, Georgios Pagonis, Victoria Clerico, Hadjer Benmeziane, Irem Boybat, Hsinyu Tsai, Abu Sebastian, William Andrew Simon
- 链接：[arXiv](https://arxiv.org/abs/2611.07707) · [PDF](https://arxiv.org/pdf/2611.07707) · [HF](https://huggingface.co/papers/2611.07707)

Large Language Models (LLMs) incur severe memory-access overheads due to the cost of loading large weight matrices and key-value (KV) caches. Analog In-Memory Computing (AIMC) is an emerging solution that enables computation directly on static weights stored in memory, substantially reducing energy and latency. 3D-IMC further stacks memory arrays into vertical tiers, increasing capacity but revealing a new…

## 35. Evaluating Token Probabilities as Confidence Estimators in Human Behavior Simulations: A Case Study in Luxembourgish Next Like Prediction

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, language model, large language, spec
- 作者：Nils Schwager, Simon Münker, Alistair Plum, Achim Rettinger
- 链接：[arXiv](https://arxiv.org/abs/2611.07735) · [PDF](https://arxiv.org/pdf/2611.07735) · [HF](https://huggingface.co/papers/2611.07735)

As large language models (LLMs) are increasingly used to simulate human behavior, their operational validity is typically assessed through accuracy alone, implicitly treating human behavior as deterministic. We argue that on noisy digital trace data, a model's performance depends not only on predicting the correct outcome but on its calibration. We present a case study testing whether the token probabilities of…

## 36. Automated Video-to-QA Pipeline: End-to-End Question Generation and Verification Using Large Language Models

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：language model, large language, spec, retrieval
- 作者：Jaival Chauhan, Vikram Singh, Pruthwik Mishra
- 链接：[arXiv](https://arxiv.org/abs/2611.07755) · [PDF](https://arxiv.org/pdf/2611.07755) · [HF](https://huggingface.co/papers/2611.07755)

The exponential growth of educational and informational video content on platforms like YouTube presents a challenge for efficient knowledge retrieval and assessment. This paper proposes an end-to-end automated pipeline for extracting structured summaries and generating high-fidelity Question-Answer (QA) pairs from video streams. The framework integrates a cascade of state-of-the-art models: audio extraction is…

## 37. BiGrounder: Bidirectional Training Unlocks the Potential of GUI Grounding

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reinforcement learning, evaluation, benchmark
- 作者：Dengyao Shi, Tianyu Fu, Fei Hu, Anyang Su, Hanning Wang, Shuo Wang, Minghui Wu, Chenxu Zhao, Zhen Lei
- 链接：[arXiv](https://arxiv.org/abs/2611.07765) · [PDF](https://arxiv.org/pdf/2611.07765) · [HF](https://huggingface.co/papers/2611.07765)

Graphical User Interface (GUI) grounding aims to map natural language instructions to precise operational coordinates, serving as a critical task for autonomous agent interaction. Current approaches formalize GUI grounding as predicting action-coordinate pairs from instructions, with end-to-end training supervised solely by final coordinates. Training datasets typically provide only a small number of descriptions…

## 38. PBPO: Prefix-Block Policy Optimization for Diffusion Language Models

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, language model, large language
- 作者：Katherine Tieu, Dongqi Fu, Si Zhang, Hanqing Zeng, Tianxin Wei, Chenglin Wei, Yinglong Xia, Hong Li, Jingrui He
- 链接：[arXiv](https://arxiv.org/abs/2611.07783) · [PDF](https://arxiv.org/pdf/2611.07783) · [HF](https://huggingface.co/papers/2611.07783)

Diffusion Large Language Models (dLLMs) commonly decode responses by proceeding autoregressively across blocks while iteratively denoising multiple tokens within each block. This structure makes block-level policy optimization a natural adaptation of autoregressive policy optimization. However, the exact likelihood of a completed block is intractable because it marginalizes over the intermediate states and reveal…

## 39. Generate-then-Rank: Learning Symbolic Goal Interpretation for Embodied Agents

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, benchmark, language model, large language, planning
- 作者：Jisen Lei, Huizhi Liang
- 链接：[arXiv](https://arxiv.org/abs/2611.07825) · [PDF](https://arxiv.org/pdf/2611.07825) · [HF](https://huggingface.co/papers/2611.07825)

Goal interpretation is to translate a natural language instruction into a formal symbolic goal that a planner can execute. It is critical for embodied agents because any error here propagates to every downstream planning and action step. Doing it well requires both generating suitable candidates and reliably selecting among them. We present a two-stage generate-then-rank approach to Goal Interpretation in the…

## 40. Instantiating the Knowledge Plane

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reasoning, language model, large language
- 作者：Francisco Pereira, Justine Sherry, Pratiksha Thaker
- 链接：[arXiv](https://arxiv.org/abs/2611.07827) · [PDF](https://arxiv.org/pdf/2611.07827) · [HF](https://huggingface.co/papers/2611.07827)

In 2003, Clark et al. proposed the "Knowledge Plane", a layer of intelligent agents that share rich information about network state in order to collaboratively manage the Internet across administrative boundaries. The technology of the day lacked the two capabilities it demanded most: reasoning and unstructured communication. Thus, automated network management has remained largely confined to single domains, while…

## 41. Which Signals of Code Correctness Survive Distribution Shift? Hidden-State and Causal Predictors of Program and Verdict Correctness

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, benchmark, language model, large language
- 作者：Viola Campos, Thomas Klassert, Adrian Ulges
- 链接：[arXiv](https://arxiv.org/abs/2611.07876) · [PDF](https://arxiv.org/pdf/2611.07876) · [HF](https://huggingface.co/papers/2611.07876)

Large language models increasingly judge code, yet without external feedback such judgments are unreliable, and verifying them by executing tests or by extended reasoning is costly. Instead, execution-free correctness predictors use signals from the model's output probabilities, sampled solutions, or hidden states to identify judgments that warrant further verification. However, these predictors may degrade under…

## 42. WAM-Sim0.1: World Anchored Memory Meets Online RL for Consistent and Realistic Driving Simulation

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, benchmark, language model, coding
- 作者：Jiahao Cui, Jiaye Li, Wenhao Zhang, Yaoyi Li, Shan Luan, Quanhui Tang, Jianhua Han, Lin Cheng, Hang Xu, Siyu Zhu
- 链接：[arXiv](https://arxiv.org/abs/2611.07939) · [PDF](https://arxiv.org/pdf/2611.07939) · [HF](https://huggingface.co/papers/2611.07939)

Autoregressive driving world models systematically suffer from structural drift, identity drift, and quality decay over long rollout horizons due to transient conditioning signals that lack persistent state. We present WAM-Sim, a driving world model anchored by a persistent hierarchical memory and optimized via online flow-matching RL. WAM-Sim structures persistent context across three temporal and semantic scales:…

## 43. Circe: Training-Free LLM Self-Evaluation via Component Interaction Consistency

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, language model, large language
- 作者：Shuyi Miao, Zheng Li, Xu Xie, Linrui Xu, Fei Shen, Xiaoyu Du, Tat-Seng Chua
- 链接：[arXiv](https://arxiv.org/abs/2611.07948) · [PDF](https://arxiv.org/pdf/2611.07948) · [HF](https://huggingface.co/papers/2611.07948)

As large language models (LLMs) are increasingly deployed in real-world applications, evaluating the correctness of their responses is crucial for reliable use. However, such evaluation is challenging because reference answers are rarely available in practice. Existing reference-free methods mainly rely on output signals, which may assign high scores to incorrect responses and thus do not necessarily reflect…

## 44. TCSExam: Evaluating Frontier LLMs on the Full Range of TCS Research

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, evaluation, benchmark, language model, large language, spec
- 作者：Yifan Luo, Zhengying Liu, Yang Yuan, Zhilin Yang, Andrew Chi-Chih Yao
- 链接：[arXiv](https://arxiv.org/abs/2611.07962) · [PDF](https://arxiv.org/pdf/2611.07962) · [HF](https://huggingface.co/papers/2611.07962)

Can large language models (LLMs) advance theoretical computer science and resolve its long-standing open conjectures? To study progress toward this goal, we introduce TCSExam, a unified framework and benchmark covering the full range of TCS research. It evaluates theorem proving, solver engineering, and constructions alongside direct attempts to resolve open conjectures, capturing both concrete research…

## 45. QRAE: Query-Relevant Attention Entropy for Context Compression in DeepSearch Agents

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reasoning, evaluation, benchmark, spec
- 作者：Yingjie Tan, Haiquan Qiu, Quanming Yao, Manyi Zhong, Xianzhi Yu, Yaqing Wang
- 链接：[arXiv](https://arxiv.org/abs/2611.07976) · [PDF](https://arxiv.org/pdf/2611.07976) · [HF](https://huggingface.co/papers/2611.07976)

DeepSearch LLM agents repeatedly search and carry retrieved sources into subsequent reasoning steps. This expanding context increases token consumption and latency, although many results do not contribute to later reasoning. We propose Query-Relevant Attention Entropy (QRAE), an online context compression method that uses sparse evidence-assessment heads to decide which intact retrieved chunks should persist across…

## 46. How Far Can Lightweight LLMs Go in Intent-to-SLO Translation?

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, evaluation, language model, large language
- 作者：Sabbir Ahmed, Hazem Abbas, Salimur Choudhury
- 链接：[arXiv](https://arxiv.org/abs/2611.07982) · [PDF](https://arxiv.org/pdf/2611.07982) · [HF](https://huggingface.co/papers/2611.07982)

Intent-based networking (IBN) promises QoS provisioning in which the network derives the configuration from operator-stated goals. Its first step, translating a natural-language intent into enforceable service-level objectives (SLOs) grounded in a live snapshot of the network state, increasingly relies on large language models (LLMs). These large models add cost and energy to the management loop and typically…

## 47. Compression Through a Context Lens: Evaluating Adaptation, Quantization, and Distillation in Arabic Legal LLMs

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, evaluation, benchmark, language model, large language, spec
- 作者：Md. Rafiul Biswas, George Mikros, Wajdi Zaghouani
- 链接：[arXiv](https://arxiv.org/abs/2611.07988) · [PDF](https://arxiv.org/pdf/2611.07988) · [HF](https://huggingface.co/papers/2611.07988)

Model compression can facilitate the deployment of large language models in resource-constrained legal settings, but its effects on domain-specific performance may depend on the evaluation protocol. We investigate this issue using ArabLegalEval, a Saudi Arabic legal benchmark, under both with-context and no-context evaluation. The former provides supporting legal passages, while the latter assesses performance…

## 48. Automatic keyphrase extraction and annotation: modern theoretical approaches and practical solutions for text and speech

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, language model, large language, spec
- 作者：Daria Guseva, Olga Mitrofanova
- 链接：[arXiv](https://arxiv.org/abs/2611.08006) · [PDF](https://arxiv.org/pdf/2611.08006) · [HF](https://huggingface.co/papers/2611.08006)

The exponential growth of textual and audiovisual information has made the task of automatic keyphrase extraction (KE) increasingly significant. This article provides a comprehensive analysis of contemporary theoretical approaches and practical solutions for KE across both text and speech modalities. The primary contribution of this work is its systematic synthesis of these often-disparate research strands into a…

## 49. DictLLM: Post-training Compression of Large Language Model with Dictionary Kernels

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, reasoning, benchmark, language model, large language, spec
- 作者：Jinho Park, Se Young Chun, Mingoo Seok
- 链接：[arXiv](https://arxiv.org/abs/2611.08082) · [PDF](https://arxiv.org/pdf/2611.08082) · [HF](https://huggingface.co/papers/2611.08082)

Efficient deployment of large language models (LLMs) on mobile devices requires balancing performance with compute and memory constraints. Post-training compression is an effective approach to managing this trade-off, while requiring much less computation than in-training counterparts. We propose DictLLM, a dictionary-based compression scheme in which weight matrices within grouped layers are decomposed into a…

## 50. PersonaAgent: Retrieval-Augmented Transaction Anomaly Scoring with Refreshable Multi-Entity Persona Memory

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, memory, benchmark, retrieval
- 作者：Zhengyu Fang, Liang Wang, Yingtong Dou, Yuzhong Chen, Shubham Jain, Junpeng Wang, Xiran Fan, Menghai Pan, Jiarui Sun, Yan Zheng, Yiwei Cai
- 链接：[arXiv](https://arxiv.org/abs/2611.08094) · [PDF](https://arxiv.org/pdf/2611.08094) · [HF](https://huggingface.co/papers/2611.08094)

In large-scale payment networks, entities (card, merchant, etc.) and their interactions play a key role in transaction anomaly detection. However, transaction patterns between different entities usually change more frequently than the production model refresh schedule. Meanwhile, entity embedding tables suffer from high-cardinality and sparse interaction issues. To resolve the above challenges, we present…

## 51. ProQuant: Progressive Quantization-aware Training for Edge MLLMs

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, benchmark, language model, large language, spec
- 作者：Yufei Xue, Yushi Huang, Jiawei Shao, Pingcheng Dong, Yonghao Tan, Shiyao Li, Kwang-Ting Cheng, Jun Zhang
- 链接：[arXiv](https://arxiv.org/abs/2611.08216) · [PDF](https://arxiv.org/pdf/2611.08216) · [HF](https://huggingface.co/papers/2611.08216)

Multi-modal large language models (MLLMs) with impressive perception and understanding capabilities will enable a range of downstream applications. However, their substantial computational and memory requirements hinder the real-world implementation, particularly for resource-constrained edge devices. Quantization has emerged as an effective solution for deploying large models. While post-training quantization (PTQ)…

## 52. Agent-R$^2$: Scaling Agents for Realistic Productivity Work via Real-Source Data Synthesis

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, tool use, reasoning, reinforcement learning, evaluation, language model, large language, spec
- 作者：Teng Pan, Zixuan Wang, Yuchen Yan, Qifei Wu, Yao Chen, Yingqi Qu, Ruiqing Zhang, Yongliang Shen
- 链接：[arXiv](https://arxiv.org/abs/2611.08219) · [PDF](https://arxiv.org/pdf/2611.08219) · [HF](https://huggingface.co/papers/2611.08219)

Large language models have made rapid progress in agentic reasoning and tool use, raising expectations for agents that can take over realistic productivity work from humans. However, current agents still struggle to finish such tasks, where success requires following long-horizon professional workflows, understanding heterogeneous file contexts, and producing usable deliverables under fine-grained requirements. A…

## 53. From Twisted Facts to Rogue Agents: Can LLMs Reliably Detect Multi-Dimensional Hallucinations?

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, benchmark, language model, large language
- 作者：Hanyu Qiu, Ze Liu, Zhe Zhao, Kuang Xiong, Blaze Chen, Zhenxiang Yan, Renfen Hu
- 链接：[arXiv](https://arxiv.org/abs/2611.08231) · [PDF](https://arxiv.org/pdf/2611.08231) · [HF](https://huggingface.co/papers/2611.08231)

Large language models (LLMs) are widely used for information access, content production, and agent-based task execution, but their outputs remain vulnerable to subtle, high-risk hallucinations. To systematically evaluate and advance post-generation hallucination detection, we introduce HaluCheck, a large-scale, bilingual benchmark comprising over 42k instances spanning both factual hallucinations in text and…

## 54. Signals, Evidence, and Context: User Scrutiny in Real-World LLM Conversations

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, language model, large language, spec
- 作者：Ahana Biswas, Yu-Ru Lin
- 链接：[arXiv](https://arxiv.org/abs/2611.08232) · [PDF](https://arxiv.org/pdf/2611.08232) · [HF](https://huggingface.co/papers/2611.08232)

Large language models (LLMs) often present synthesized answers without making their supporting evidence easy to inspect. We study how features of these answers relate to users' subsequent accepting, checking, and challenging in 489,283 assistant-user response pairs from ShareChat and WildChat. Broad attribution language appears in 31.9% of qualifying responses, compared with explicit URLs in 1.33%, revealing a gap…

## 55. Multimodal-SEA: Benchmarking AI Agent Security under Multimodal Social Engineering Attacks

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, evaluation, benchmark, spec
- 作者：Zhitao He, Chi Him Zhang, Chengru Han, Yi R Fung
- 链接：[arXiv](https://arxiv.org/abs/2611.08281) · [PDF](https://arxiv.org/pdf/2611.08281) · [HF](https://huggingface.co/papers/2611.08281)

Personal AI agents face social engineering attacks supported by forged multimodal content, but existing evaluations mainly focus on text-based dialogue, leaving their intrinsic security under such attacks insufficiently studied. We introduce Multimodal-SEA, an interactive benchmark comprising 608 expert-designed tasks grounded in real-world fraud cases, covering 14 domains and 152 attack scenarios with prepared…

## 56. AutoCompress: Automated Hardware-Guided Model Compression

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, benchmark, coding, spec
- 作者：Sheldon Liang, Ali Taghibakhshi, Saurav Muralidharan, Sharath Turuvekere Sreenivas, Ashwath Aithal, Pavlo Molchanov, Nima Tajbakhsh
- 链接：[arXiv](https://arxiv.org/abs/2611.08290) · [PDF](https://arxiv.org/pdf/2611.08290) · [HF](https://huggingface.co/papers/2611.08290)

LLM pruning must preserve quality while meeting hardware- and workload-specific constraints on latency, throughput, and memory. Existing pruning workflows often target parameter counts, requiring practitioners to manually select model sizes that meet latency, throughput, and GPU memory limits. However, parameter count alone does not predict these metrics, which depend on the model architecture, workload, hardware,…

## 57. RM-VLM: From Natural-Language Task Descriptions to Vision-Grounded Reward Machines

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reinforcement learning, language model, large language
- 作者：Roko Parac, Christos Ziakas, Leo Ardon, Alessandra Russo
- 链接：[arXiv](https://arxiv.org/abs/2611.08308) · [PDF](https://arxiv.org/pdf/2611.08308) · [HF](https://huggingface.co/papers/2611.08308)

Reward machines (RMs) have been proposed as a reward formulation in reinforcement learning (RL) to capture non-Markovian tasks where credit assignment depends on history. By representing reward functions as automata, RMs expose the task's temporal structure and allow such rewards to be handled within a Markovian framework. However, they assume a labelling function, a proposition-grounding oracle for observations,…

## 58. Benchmarking Large Language Models on Heterogeneous Cognitive and Biomedical Knowledge Graphs: The Role of Graph Grounding in Multi-Hop Reasoning and Hallucination Mitigation

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, benchmark, language model, large language, spec
- 作者：Ali Sarabadani, Kheirolah Rahsepar Fard, Tahereh Jeirani
- 链接：[arXiv](https://arxiv.org/abs/2611.08315) · [PDF](https://arxiv.org/pdf/2611.08315) · [HF](https://huggingface.co/papers/2611.08315)

Large language models (LLMs) are increasingly used in biomedical and cognitive neuroscience, but their ability to reason reliably over heterogeneous knowledge graphs (KGs) remains unclear. We benchmark five LLMs (GPT-5.1, Gemini 2.0 Pro, Llama 3, Qwen, and BioGPT) across five KGs: DrugBank, NeuroSynth, Cognitive Atlas, Brain Map, and GDPKG. We introduce a multitier query dataset to evaluate reasoning depth and…

## 59. Learning the Task or Learning the Verifier? Rethinking Criteria Exposure in Embodied Self-Improvement

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, benchmark, coding, spec
- 作者：Wenbo Huang, Jianxin Bi, Shunyu Yang, Ruiyang Si, Rui Ni, Qiang Wang, Shulong Jiang, Yintianrun Zhang, Feixiang Ruan, Kewei Zhang, Ye Huang, Shukai Gong, Daquan Zhou
- 链接：[arXiv](https://arxiv.org/abs/2611.08318) · [PDF](https://arxiv.org/pdf/2611.08318) · [HF](https://huggingface.co/papers/2611.08318)

Self-improving embodied agents are increasingly being developed and compared on robot simulation benchmarks. Several recent works expose the benchmark's success criteria to the learning agent, a practice we call Criteria Exposure (CE). These criteria, originally written to verify policies trained by imitation learning, often demand more than the corresponding language instructions, so a score from such a verifier…

## 60. SpecCTMC: Exact Speculative Simulation of Diffusion Language Model Continuous-Time Markov Chains

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, language model, coding, spec
- 作者：Siva Rajesh Kasa, Yasong Dai, Sumit Negi, Hongdong Li
- 链接：[arXiv](https://arxiv.org/abs/2611.08362) · [PDF](https://arxiv.org/pdf/2611.08362) · [HF](https://huggingface.co/papers/2611.08362)

Masked diffusion language models offer parallel text generation, but independently sampling multiple tokens can disrupt their dependencies and change the output distribution. Exact continuous-time sampling avoids this approximation, yet typically requires one sequential model evaluation per token. We introduce SpecCTMC, a training-free speculative sampler that reduces this sequential bottleneck without a separate…

## 61. StrataFlux: Memory-Hierarchy-Native Low-Bit LLM Inference

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, language model, large language, coding
- 作者：Jake Hyun, Ziyu Zhao, Jae-sun Seo, Mohamed S. Abdelfattah
- 链接：[arXiv](https://arxiv.org/abs/2611.08363) · [PDF](https://arxiv.org/pdf/2611.08363) · [HF](https://huggingface.co/papers/2611.08363)

Quantization reduces the memory and bandwidth demands of large language model (LLM) inference but can degrade accuracy; offloading higher-precision data can instead stall generation. We introduce StrataFlux, a framework that challenges this tradeoff by recovering accuracy lost to low-bit weight and key-value (KV) cache quantization while retaining quantization's memory and speed advantages. StrataFlux co-designs…

## 62. Benchmarks as Software: Terminal-Bench and the Case for Continuous Benchmarks

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, evaluation, benchmark, coding, spec
- 作者：E. Kelly Buchanan, Crystal Zhou, Scott W. Linderman, Christopher Ré
- 链接：[arXiv](https://arxiv.org/abs/2611.08417) · [PDF](https://arxiv.org/pdf/2611.08417) · [HF](https://huggingface.co/papers/2611.08417)

Coding agents are among the most economically consequential deployments of LLMs to date, making reliable evaluation increasingly important. Yet even benchmarks that are carefully validated at release can become stale. As models improve, they can discover valid solutions that existing verifiers reject, while changes to evaluation infrastructure can invalidate assumptions embedded in tasks and tests. We call the…

## 63. The Power of Meta Access in the Software of the Future --- Demonstrated on LLM Chat UIs and Chat AI

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, language model, large language, coding, retrieval
- 作者：Julian Kunkel, Ali Doosthosseini
- 链接：[arXiv](https://arxiv.org/abs/2611.08428) · [PDF](https://arxiv.org/pdf/2611.08428) · [HF](https://huggingface.co/papers/2611.08428)

Chat remains the default surface for many large language model (LLM) tasks, even as agentic tools such as OpenCode excel at coding and automation. Yet the model sees the current dialogue but not the workspace around it. We explore meta access---giving the assistant a structured, permissioned view of the interface itself and propose a ladder of levels: feature tutoring; metadata, settings, and preference access;…

## 64. SynthFaces: Balanced Large Scale Human Dataset

- 分数：8.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：-
- 作者：Sergey Karpukhin, Denis Bobkov, Kirill Morozov, Aibek Alanov
- 链接：[arXiv](https://arxiv.org/abs/2610.40119) · [PDF](https://arxiv.org/pdf/2610.40119) · [HF](https://huggingface.co/papers/2610.40119)

The pursuit of fair and equitable AI in human-centric tasks is critically hindered by the inherent biases and privacy risks of real-world datasets, which offer imbalanced representations of identity and often contain sensitive personal information. Consequently, state-of-the-art generative models trained on this skewed data exhibit unfair performance, particularly in identity-preserving generation. In this work we…

## 65. Multimodal Information Interactions Bottleneck for Multimodal Self-Supervised Learning

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, coding, spec
- 作者：Liangjian Wen, Jiangtao Zheng, Jiang Duan, Qun Dai, Yong Dai, Jianzhuang Liu, Jun Wang, Shu-Dong Huang, Xinwang Liu, Zenglin Xu, Zhao Kang
- 链接：[arXiv](https://arxiv.org/abs/2611.07718) · [PDF](https://arxiv.org/pdf/2611.07718) · [HF](https://huggingface.co/papers/2611.07718)

Multimodal self-supervised learning is challenged by heterogeneity, unequal informativeness, and complex information interactions across multimodal data sources such as images, text, audio, and tabular data. While contrastive methods effectively align shared semantics, they typically rely on strong multi-view redundancy assumptions, overlooking modality-specific and synergistic information, thus leading to…

## 66. Evaluating Language Model Features for Zero-Shot Time-Series Anomaly Detection Under Isolation Assumption

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, language model, large language
- 作者：Romain Hermary, Nesryne Mejri, Djamila Aouada
- 链接：[arXiv](https://arxiv.org/abs/2611.07720) · [PDF](https://arxiv.org/pdf/2611.07720) · [HF](https://huggingface.co/papers/2611.07720)

Time-Series Anomaly Detection (TSAD) is a fundamentally challenging task: it is unsupervised, requires high local precision capabilities, and suffers from limited labelled data. Recent work has explored adapting Large Language Models (LLMs) to time-series via cross-modal transfer. However, existing approaches are poorly suited to Multivariate TSAD (MTSAD), as tokenisation often obscures fine-grained temporal and…

## 67. Seeing Beyond the Next Step: World-Model-Guided Human-Like Navigation in Multi-Agent Scenes

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reasoning, evaluation
- 作者：Seong-Eun Hong, JuYeong Hwang, Jinhyun Kim, Hanyoung Jang, HyeongYeop Kang
- 链接：[arXiv](https://arxiv.org/abs/2611.07730) · [PDF](https://arxiv.org/pdf/2611.07730) · [HF](https://huggingface.co/papers/2611.07730)

Selecting a next motion in a populated scene is not just a matter of avoiding what is currently in the way: an action can be locally feasible yet drift onto the road instead of the crosswalk, cut into a stream of crossing pedestrians, or bottleneck a narrow passage. These failure modes are invisible from the current state alone, and acting on them requires reasoning about what each candidate action will cause. World…

## 68. MV-Sign: Multi-View 3D Motion Integration and Enhanced Text-to-Motion Conditioning for Sign Language Production

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, spec, retrieval
- 作者：Singyu Muk, Kaustubh Kundu, Kunyuan Xie, Weijie Wang, Kalin Stefanov
- 链接：[arXiv](https://arxiv.org/abs/2611.07811) · [PDF](https://arxiv.org/pdf/2611.07811) · [HF](https://huggingface.co/papers/2611.07811)

Sign language production (SLP) aims to generate appropriate sign language motion from spoken language text. However, current 3D SLP methods suffer from noisy supervision and weak text conditioning. Specifically, these methods typically rely on pseudo-3D motion data fitted from single-view frontal videos, which introduces severe self-occlusion and loses fine-grained hand details, ultimately degrading downstream…

## 69. Different Corpora, Different Skills? A Paired Study of Small Language Models

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, language model
- 作者：Edoardo Vaira, Georgios Chavales, Pierre Nugues
- 链接：[arXiv](https://arxiv.org/abs/2611.07812) · [PDF](https://arxiv.org/pdf/2611.07812) · [HF](https://huggingface.co/papers/2611.07812)

Small language models are often trained under tight data budgets, where the choice of pretraining corpus may matter as much as model size or training recipe. We compare two contrasting corpora at matched 10-million- and 37-million-word budgets: the 1911 Encyclopaedia Britannica and the BabyLM 2026 strict pretraining corpus. For each corpus, we train teacher models, distilled 58-million-parameter Baby-Llama students,…

## 70. Axis-LoRA: Probing and Adapting Embedding Models for Personal-Memory Retrieval

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, benchmark, retrieval
- 作者：Dohoon Kim, Junho Park, Hyunwoong Bae, Seyoon Kim, Taesup Moon
- 链接：[arXiv](https://arxiv.org/abs/2611.07820) · [PDF](https://arxiv.org/pdf/2611.07820) · [HF](https://huggingface.co/papers/2611.07820)

As LLMs are increasingly asked questions about a user's personal experiences, retrieval must distinguish memories by time, place, person, and event. Current personal-memory pipelines rely on frozen dense embedding models to embed memories for retrieval, but we find that these models do not capture the four axes well. Swapping a memory's date or place barely shifts its embedding, and a trained projection on top of…

## 71. Estimating Spectrum-Free Information Bounds for Generative Surrogates Beyond Conditional Collapse

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, spec
- 作者：Chaitanya Dumbre, Sourabh Dube
- 链接：[arXiv](https://arxiv.org/abs/2611.07826) · [PDF](https://arxiv.org/pdf/2611.07826) · [HF](https://huggingface.co/papers/2611.07826)

Conditional generative surrogates in high-energy physics, such as models that predict reconstructed jets from partons, are often evaluated on $1\text{D}$ marginal divergences among other metrics. Taken alone these metrics can reward conditional collapse. On a CMS simulation benchmark, a sampler that ignores the conditioner beats a trained Mixture Density Network (MDN) on all four target marginals under both KL and…

## 72. Computation, not weight access: large language models as auditors of clinical prediction networks

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：language model, large language, spec
- 作者：Zhiyu Liu, Xinyu Yang
- 链接：[arXiv](https://arxiv.org/abs/2611.07847) · [PDF](https://arxiv.org/pdf/2611.07847) · [HF](https://huggingface.co/papers/2611.07847)

Frontier large language models (LLMs) have been reported to read, edit and write the weights of small neural networks, raising the prospect of auditing clinical prediction models from their files alone. Public demonstrations, however, mixed reading raw weights with running code. We separated these conditions in internally pre-specified simulation experiments. Tanh networks of 105 to 38,401 weights were trained on…

## 73. Learning Robotic World Models with Semantic and Visual Feedback

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, spec, planning
- 作者：Hao Wu, Yuqi Li, Yizhou Zhao, Kun Wang, Xiao Luo, Yu Cheng, Bo An, Yingli Tian, Laszlo A. Jeni, Ming-Hsuan Yang
- 链接：[arXiv](https://arxiv.org/abs/2611.07850) · [PDF](https://arxiv.org/pdf/2611.07850) · [HF](https://huggingface.co/papers/2611.07850)

Robot world models predict action-conditioned future visual states to support robotic planning and decision making. However, visual reconstruction does not fully capture task progress, semantic evaluation alone provides limited constraints on fine-grained visual errors, and homogeneous predictions limit comparative feedback. We present RoboImagine, a framework for post-training autoregressive robotic world models…

## 74. FARR: Forecast-Aware Residual Refinement with Matched Endpoint Evidence for Long-Horizon Time-Series Forecasting

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, language model, large language
- 作者：Yiyang Zhang, Yuli Zheng, Bin Li, Meimei Zhang, Qiang Sun
- 链接：[arXiv](https://arxiv.org/abs/2611.07870) · [PDF](https://arxiv.org/pdf/2611.07870) · [HF](https://huggingface.co/papers/2611.07870)

Large language models use auxiliary conditioning to incorporate additional information into time-series forecasts. However, auxiliary conditioning does not consistently improve accuracy and can increase forecasting error when its influence is poorly matched to the observed temporal context. We propose Forecast-Aware Residual Refinement (FARR), which learns to correct forecasts using endpoint evidence. FARR obtains a…

## 75. When Bigger Becomes Brittle: Why Compression Hurts More as Language Models Scale

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, language model, retrieval
- 作者：Gautam Gupta, Dikshant Kukreja, Unique Kumar, Avni Mittal, Deepanshu Dabas, Kshitij Sah, Erik Cambria, Rajiv Ratn Shah, Zhengkui Wang, Avinash Anand
- 链接：[arXiv](https://arxiv.org/abs/2611.07891) · [PDF](https://arxiv.org/pdf/2611.07891) · [HF](https://huggingface.co/papers/2611.07891)

Quantization and pruning reduce the cost of deploying language models, but their effects are usually reported as benchmark scores. Such scores record only the loss that remains at the output. Inside the model, compression damages some components more than others, and the rest of the network can partly compensate. The observed loss therefore reflects both the damage and this compensation, which benchmark scores…

## 76. Structure from Collision via Hypothesis-Space Reasoning

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, benchmark, spec
- 作者：Takuhiro Kaneko
- 链接：[arXiv](https://arxiv.org/abs/2611.07900) · [PDF](https://arxiv.org/pdf/2611.07900) · [HF](https://huggingface.co/papers/2611.07900)

Knowledge of the hidden interior structure of an object, including the presence and location of cavities, is essential for predictive simulation, robotic manipulation, and nondestructive inspection. However, such cavities leave no direct signature on the static visible surface, making collision-induced deformation one of the few cues used to infer their presence. Structure from Collision (SfC) addresses this problem…

## 77. Adaptive Semantic Branching: Disagreement-Localized Cross-Trajectory Regeneration for Reasoning Candidate Expansion

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, evaluation, spec
- 作者：Jeong-Yoon Kim, Tae-Yoon Lee
- 链接：[arXiv](https://arxiv.org/abs/2611.07918) · [PDF](https://arxiv.org/pdf/2611.07918) · [HF](https://huggingface.co/papers/2611.07918)

Reasoning trajectories generated for the same problem often arrive at conflicting answers. These disagreements reveal alternative intermediate decisions that can be reused to explore new solutions. We introduce Adaptive Semantic Branching (ASB), a training-free inference procedure that turns cross-trajectory disagreement into targeted candidate generation. ASB first groups independently sampled trajectories by…

## 78. ZeroRAG: Adaptive Semantic Peer Routing for Decentralized Retrieval-Augmented Generation

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：language model, large language, retrieval
- 作者：Petru Neague, Quinten Stokkink, Martijn de Vos, Rafael Pires, Mathis Randl, Anne-Marie Kermarrec, Johan Pouwelse
- 链接：[arXiv](https://arxiv.org/abs/2611.07928) · [PDF](https://arxiv.org/pdf/2611.07928) · [HF](https://huggingface.co/papers/2611.07928)

Retrieval-augmented generation (RAG) is a standard approach to enhance the reliability of large language model (LLM) outputs by retrieving documents relevant to a query and supplying them in the LLM prompt. Today's RAG systems collect, index, and serve these documents from centralized stores. In practice, however, documents are owned by organizations, devices, and individuals who cannot or will not surrender custody…

## 79. Towards Scalable Diagnostic-Driven Whole-Slide Image Retrieval for Pathology Archives

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, benchmark, retrieval
- 作者：Jingsong Liu, Youssef Wally Han Li, Weiwei Zhou, Jing Dai, Elisabeth Wetzer, Peter J. Schüffler
- 链接：[arXiv](https://arxiv.org/abs/2611.07935) · [PDF](https://arxiv.org/pdf/2611.07935) · [HF](https://huggingface.co/papers/2611.07935)

The growing adoption of digital pathology has rapidly expanded collections of hematoxylin-and-eosin whole-slide images, yet efficient navigation through these archives remains challenging, as metadata is often inconsistent or unavailable. Content-based image retrieval addresses this challenge by identifying similar cases directly from visual representations instead of manual annotations or metadata. Existing…

## 80. CardioLM: A multilingual suite of small language models for the cardiology domain

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, language model, spec
- 作者：Manuela-Daniela Danu, Miguel Rodríguez-Ortega, Alberto Becerra-Tome, Pablo Arancibia, Fernando Gallego-Donoso, Lorenzo Pratesi, Xi Bai, Andrei-Damian Dinescu, Salvador Lima-López, Andrea Guala, Saskia Haitjema, Jonas Mack, Michele Miranda, Wesam Al Nabki, Jan Rodríguez-Miret, Vasile George Marica, Vladimír Kincl, Kateřina Dostálová, Michael Andrej, Alicia Ujil, Corinne Allaart, Machteld Boonstra, Malin Overmars, Anoop Shah, Giovanna Ceroni, Jonathan Kossoff, Domenico D'Amario, Renzo Laborante, Antonio Iaconelli, Isabella Fumarulo, Jacopo Lenkowicz, Livia Lilli, Emma Weiss, Alex Scafa, Felix Lindberg, Milou Gamage, Eulàlia Farré-Maduell, Sébastien Bratières, Martin Krallinger, Bram van Es
- 链接：[arXiv](https://arxiv.org/abs/2611.07940) · [PDF](https://arxiv.org/pdf/2611.07940) · [HF](https://huggingface.co/papers/2611.07940)

Background: Cardiovascular care generates large volumes of clinical free-text documentation in local languages. However, clinical natural language processing (NLP) resources remain concentrated in English, and no existing benchmark is cardiology-specific, multilingual, and broad in entity coverage. Methods: We present two contributions. The first is CardioCCC, a corpus of 508 cardiology case reports originally…

## 81. ChemE-as-Code: An Open-Source Platform for Agentic AI in Chemical Engineering

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, language model, large language
- 作者：Artur M. Schweidtmann
- 链接：[arXiv](https://arxiv.org/abs/2611.07947) · [PDF](https://arxiv.org/pdf/2611.07947) · [HF](https://huggingface.co/papers/2611.07947)

ChemE-as-Code provides an open-source environment in which AI agents built on large language models (LLMs) can carry out chemical engineering work and engineers can check it. Its calculation tools range from catalysis through process simulation to plant layout, HAZOP and life cycle assessment, and skills tell a general-purpose agent how to use them. Engineering files are linked, machine-readable and versioned in…

## 82. Beyond the Keyword: A Human-Annotated Benchmark for Arabic Anxiety-Related Discourse

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, retrieval
- 作者：Shimaa Ibrahim, Mabrouka Bessghaier, Md. Rafiul Biswas, Insaf Elouard, Wajdi Zaghouani
- 链接：[arXiv](https://arxiv.org/abs/2611.07949) · [PDF](https://arxiv.org/pdf/2611.07949) · [HF](https://huggingface.co/papers/2611.07949)

Keyword retrieval returns expressions of personal anxiety together with many other uses of anxiety-related language. We present a benchmark of 1,000 Arabic Twitter/X posts retrieved with the keyword qalaq ("anxiety/worry") and annotated for six discourse functions. Two native Arabic-speaking annotators labeled every post independently, reaching 51.1% raw agreement (Cohen's $κ= 0.378$). We then reviewed all 489…

## 83. Rotation Is Token-Blind: A Structural Criterion for Post-Training Quantization of Feed-Forward Geometry Transformers

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, benchmark, spec
- 作者：Huanfei He, Bohao Zhang, Jiaxin Zhang, Wei Sui, John See, Zeyd Boukhers, Cong Yang
- 链接：[arXiv](https://arxiv.org/abs/2611.07955) · [PDF](https://arxiv.org/pdf/2611.07955) · [HF](https://huggingface.co/papers/2611.07955)

Feed-forward 3D models use Transformers to predict camera poses, depth, and structure in one pass, avoiding iterative multi-view optimization. Long sequences and deep attention incur high compute and memory costs, motivating Post-Training Quantization (PTQ) for deployment. Existing PTQ methods mainly suppress channel-wise outliers by smoothing or orthogonal rotation. Geometry Transformers introduce a different…

## 84. CoRD: Coupled Rollouts Fill the Blind Spot of On-Policy Distillation

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, coding, spec
- 作者：Guhan Chen, Bohan Li, Jun Rao, Hejin Wang, Songtao Tian, Yexin Xie, Xiaojun Meng, Peng Yuan, Jiansheng Wei, Xuebo Liu, Zixiong Yu
- 链接：[arXiv](https://arxiv.org/abs/2611.07959) · [PDF](https://arxiv.org/pdf/2611.07959) · [HF](https://huggingface.co/papers/2611.07959)

On-policy distillation trains a student on its own rollouts, so states the teacher would reach but the student does not are seldom supervised. We introduce CoRD (coupled-rollout distillation), which keeps the on-policy loss and moves only the distribution of training states toward the teacher, drawing rollouts from a geometric interpolation of student and teacher through the maximal coupling of speculative decoding.…

## 85. NutriVisRAG: Multimodal Exemplar Grounding for Nutrient Estimation with Vision-Language Models

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：language model, spec, retrieval
- 作者：Lubnaa Abdur Rahman, Ioannis Papathanail, Maria Panagiotou, Nefeli Dimitropoulou, Margret Harðardóttir, Elisabeth J. den Brok, Bastiaan E. de Galan, Stavroula Georgia Mougiakakou
- 链接：[arXiv](https://arxiv.org/abs/2611.08054) · [PDF](https://arxiv.org/pdf/2611.08054) · [HF](https://huggingface.co/papers/2611.08054)

Diet is a major determinant of health, yet accurate dietary assessment from free-living meal images remains challenging. Existing retrieval-based Vision-Language Model (VLM) approaches to nutrient estimation typically rely on textual food representations, while, to our knowledge, direct grounding on visually similar annotated meals has not been investigated. We present NutriVisRAG, a retrieval-augmented generation…

## 86. Can an LLM Actually Reason and Program about Neural Network's Weights or is it just memorization on steroids? Exploring "Weight-Space Programming"

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, language model, large language
- 作者：Nazmus Sakib Ahmed
- 链接：[arXiv](https://arxiv.org/abs/2611.08070) · [PDF](https://arxiv.org/pdf/2611.08070) · [HF](https://huggingface.co/papers/2611.08070)

Large language models (LLMs) have recently been reported to read and write the raw weights of neural networks directly, a capability termed weight-space programming. We ask whether the reading side of this capability reflects reasoning about weight flows or a combination of local arithmetic at the network's edges and memorized priors over public datasets. We test Claude Opus 5.5 on small convolutional networks of…

## 87. Spatiotemporal Dynamics-Aware Industrial Anomaly Detection and Reasoning

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, language model, large language
- 作者：S-Wei Chen, Siangyu Yang, Yi-Chen Jan, Chun-Yi Lee, Shao-Yuan Lo
- 链接：[arXiv](https://arxiv.org/abs/2611.08080) · [PDF](https://arxiv.org/pdf/2611.08080) · [HF](https://huggingface.co/papers/2611.08080)

Industrial Anomaly Detection (IAD) is a long-established problem that aims to detect defects in industrial products during manufacturing for quality control. Most existing studies focus on static visual patterns as the basis for detection. However, in real manufacturing environments, many anomalies are dynamics-based, such as irregular movements that cannot be perceived from static cues alone. We observe that even…

## 88. TerraMesh-Masks: Open-Vocabulary Segmentation for Earth Observation

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, spec
- 作者：Benedikt Blumenstiel, Hugues Devimeux, Johannes Jakubik, Konrad Schindler
- 链接：[arXiv](https://arxiv.org/abs/2611.08081) · [PDF](https://arxiv.org/pdf/2611.08081) · [HF](https://huggingface.co/papers/2611.08081)

Open-vocabulary segmentation (OVS) enables models to segment a variety of concepts specified in natural language, removing the need for fixed label sets and fine-tuning. While recent OVS approaches have shown strong performance on natural images, they transfer poorly to Earth observation (EO) data due to differing semantics, scales, sensing modality, and geographic context. To date, large-scale EO-specific datasets…

## 89. Linguistic boundaries emerge from pressure-constrained processing dynamics

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, language model, large language
- 作者：Rui He, Philipp Homan, Wolfram Hinzen
- 链接：[arXiv](https://arxiv.org/abs/2611.08085) · [PDF](https://arxiv.org/pdf/2611.08085) · [HF](https://huggingface.co/papers/2611.08085)

Human cognition organizes continuous experience into bounded units while maintaining continuity across them. Linguistic elements are also organized into bounded structural units such as words and phrases, with sentence marking the final bound of a grammatical construction process. How do such boundaries emerge? We propose boundaries emerge from interacting demands to maintain unresolved dependencies, integrate…

## 90. MUSS: A Multi-scale and Sequence-based Model for Single-cell Gene Regulation

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：language model, coding, spec
- 作者：Kangjie Zheng, Amirhossein Vahidi, Liying Jin, Joseph Clarke, Vijaya Baskar MS, Connor Rogerson, Mengji Zhang, Muzlifah Haniffa, Anshul Kundaje, Mo Lotfollahi
- 链接：[arXiv](https://arxiv.org/abs/2611.08086) · [PDF](https://arxiv.org/pdf/2611.08086) · [HF](https://huggingface.co/papers/2611.08086)

Modeling gene regulation in single cells requires jointly representing DNA sequence, chromatin accessibility, and gene expression across regulatory scales. Sequence-based models capture DNA-level regulatory grammar but often lack cell-level resolution, whereas many single-cell omics models represent genes and peaks as fixed-vocabulary tokens without their underlying sequence. Here, we present MUSS, a sequence-based…

## 91. Gabor Gabor: E-Gaborformer, a Strictly Causal Speech Recognizer with Gabor-Dictionary Convolutions and Delta-Rule Memory

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, memory, coding
- 作者：Nir Krakowski, Tamir Cohen, Ohad Zohar, Chen Zarfati
- 链接：[arXiv](https://arxiv.org/abs/2611.08092) · [PDF](https://arxiv.org/pdf/2611.08092) · [HF](https://huggingface.co/papers/2611.08092)

Real-time voice agents need a speech recognizer that never waits for future audio and whose memory per call does not grow with the length of the call. We present E-Gaborformer, a strictly causal encoder that combines Gated DeltaNet-2 recurrent layers with sliding-window attention in a 3:1 ratio, and builds every temporal convolution from a fixed dictionary of causal Gabor atoms. Its streaming state is constant,…

## 92. Gradient Boosting for Efficient Rank Discovery in Tensor Network Kernel Machines

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, benchmark, spec
- 作者：Albert Saiapin, Kim Batselier
- 链接：[arXiv](https://arxiv.org/abs/2611.08093) · [PDF](https://arxiv.org/pdf/2611.08093) · [HF](https://huggingface.co/papers/2611.08093)

Tensor network kernel machines (TNKMs) combine nonlinear features with low-rank tensor representations to model complex relationships efficiently. However, selecting an appropriate tensor rank remains challenging, as conventional rank-search methods require training multiple candidate models, increasing computational costs. In this work, we focus on a canonical polyadic (CP) tensor network parameterization and…

## 93. Reinforcing End-to-End Autonomous Driving Safety via Negative-Aware Planning in a Unified World-Action Model

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, planning
- 作者：Zihao Zhang, Xinyu Zhang, Bing Zeng, Xingyu Chen, Zhenning Li, Bin Yu, Ziyuan Pu
- 链接：[arXiv](https://arxiv.org/abs/2611.08111) · [PDF](https://arxiv.org/pdf/2611.08111) · [HF](https://huggingface.co/papers/2611.08111)

World-action models (WAMs) jointly model future traffic states and driving actions for end-to-end autonomous driving in intelligent transportation systems. However, their action learning remains dominated by expert-trajectory imitation, leaving unsafe alternatives close to expert trajectories insufficiently constrained. To improve WAM robustness in safety-critical scenarios, we propose NegWAM, a safety post-training…

## 94. Create Your Own Work Stack: Deploying Self-hosted AI and Tooling in a Tech Startup

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, coding, retrieval
- 作者：Saad Ahmed Bazaz, Talha Amjad, Abdurrehman Subhani, Sohaib Ahmed Bazaz, Abdullah Aamir
- 链接：[arXiv](https://arxiv.org/abs/2611.08116) · [PDF](https://arxiv.org/pdf/2611.08116) · [HF](https://huggingface.co/papers/2611.08116)

Self-hosting AI is often presented as a way to reduce inference costs and increase control, but deployment introduces its own costs. We report our experience deploying a hybrid AI stack at Grayhat Developers, a small software company with an AI-intensive development workflow. Our initial motivation was to counter the growing cost of commercial AI usage: Claude/Codex incurred approximately \$325 per month, with more…

## 95. Detecting Silent Faults at the Environment-Trainer Boundary in Reinforcement Learning

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reinforcement learning, evaluation
- 作者：Zuo Gou, Chenhao Lu
- 链接：[arXiv](https://arxiv.org/abs/2611.08144) · [PDF](https://arxiv.org/pdf/2611.08144) · [HF](https://huggingface.co/papers/2611.08144)

Robot reinforcement learning increasingly runs environments outside the trainer: in another process, on another machine, in another language. Many faults at this boundary raise no error. We make the boundary a wire protocol and ask what notices a fault in it. On Pendulum, HalfCheetah, Hopper and a 7-joint arm (Pusher), we injected up to 23 faults into what crosses the wire and 2 into the trainer's log, from one…

## 96. A Generative Foundation Model for Multimodal Tokamak Tasks

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, spec
- 作者：Yingshuai Ji, Haodong Feng, Guohong Deng, Gelin Bian, Yue Wang
- 链接：[arXiv](https://arxiv.org/abs/2611.08153) · [PDF](https://arxiv.org/pdf/2611.08153) · [HF](https://huggingface.co/papers/2611.08153)

Tokamak experiments record diverse measurements, including waveforms, profiles, fields, and scalars, which are used to reconstruct the plasma, forecast its evolution, recover associated control signals, and estimate disruption risk. Most models are built separately for one task and a fixed set of inputs and outputs, and each relies on a prescribed subset of diagnostics rather than structuring the full multimodal…

## 97. BabyTheorist: A Benchmark for Learning to Theorize the World from Observation Alone

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, evaluation, benchmark
- 作者：Doojin Baek, Junyeob Baek, Mingyu Jo, Hosung Lee, Taegu Kang, Gyubin Lee, Sungjin Ahn
- 链接：[arXiv](https://arxiv.org/abs/2611.08177) · [PDF](https://arxiv.org/pdf/2611.08177) · [HF](https://huggingface.co/papers/2611.08177)

How would we know whether a machine truly understands the world? We argue that one key capability is \textit{observational theory learning}: acquiring reusable theories from pure observations and applying them to new situations. Current visual reasoning benchmarks focus primarily on the latter, presenting each task as a few-shot puzzle grouped by a common rule. We introduce BabyTheorist, a benchmark for controlled…

## 98. LeanContext: Disentangling Mathematical Resources from Local Formal Context in Lean Whole-Proof Generation

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, spec
- 作者：Hang Zhang, Qihao Ye, Litong Liu, Yunbei Zhang, Yugyung Lee, Yue Zhou, Bowen Liu, Emily First, Cheng Han, Qiao Zhuang
- 链接：[arXiv](https://arxiv.org/abs/2611.08277) · [PDF](https://arxiv.org/pdf/2611.08277) · [HF](https://huggingface.co/papers/2611.08277)

Neural theorem proving increasingly uses retrieved premises and project context to support proof generation. Evaluating these resources requires measuring the advantage of target-selected declarations over comparable alternatives and how this advantage depends on training. We introduce LeanContext, a benchmark of 129,826 Lean whole-proof generation problems, to investigate these questions. We group selected complete…

## 99. A Generative Model of Contextual Integrity: Appropriate vs. Inappropriate Information Sharing

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：language model, large language, spec
- 作者：Omer Ebead, Claude Formanek, Joel Z. Leibo
- 链接：[arXiv](https://arxiv.org/abs/2611.08284) · [PDF](https://arxiv.org/pdf/2611.08284) · [HF](https://huggingface.co/papers/2611.08284)

Contextual integrity (CI) holds that appropriate information flow depends on context-specific norms. The same disclosure may be appropriate in one context and inappropriate in another. We build a generative model of contextual integrity to study information sharing through simulated conversations. Two actors played by large language models exchange messages, with one holding private information and the other seeking…

## 100. Measured Coupling for Parallel Decoding in Diffusion Language Models

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, language model, coding
- 作者：Tal Oved, Lior Wolf
- 链接：[arXiv](https://arxiv.org/abs/2611.08307) · [PDF](https://arxiv.org/pdf/2611.08307) · [HF](https://huggingface.co/papers/2611.08307)

Diffusion language models can write many tokens per step, but must choose which tokens are safe to commit together. Mean-field decoding penalizes pairs of positions whose predictions look alike. We replace this proxy with the coupling itself: how much committing one token changes the model's confidence at another. Cheap probes inside the main forward pass measure it, with no training or extra model, and it plugs…

## 101. Polarity Classification with Multitask Learning Syntax Augmentation

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, coding, spec
- 作者：Muhammad Imran, Carlos Gómez-Rodríguez
- 链接：[arXiv](https://arxiv.org/abs/2611.08323) · [PDF](https://arxiv.org/pdf/2611.08323) · [HF](https://huggingface.co/papers/2611.08323)

Sentiment Analysis (SA) is a fundamental NLP task concerned with the identification and categorization of subjective information in text. While lexicon-based methods offer transparency, they often struggle with linguistic phenomena such as negation and intensification. Syntactic parsing has been integrated into SA pipelines to address this, but conventional parsers introduce significant computational overhead.…

## 102. FedReason: Large Language Models as Weight-Space Meta-Aggregators for Heterogeneous Federated Learning

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：language model, large language, spec
- 作者：Ali Mohammadi Ruzbahani, Abbas Yazdinejad, Hadis Karimipour
- 链接：[arXiv](https://arxiv.org/abs/2611.08383) · [PDF](https://arxiv.org/pdf/2611.08383) · [HF](https://huggingface.co/papers/2611.08383)

Federated learning servers combine client models with a fixed aggregation rule, and each rule in common use is designed for one kind of heterogeneity. We study whether a large language model (LLM) that inspects the client models can choose the rule itself, without any training on the server. In FedReason, the LLM is called every ten rounds. It analyses the weights by running code in a restricted server-side sandbox,…

## 103. Hybrid Machine Learning for Imbalanced Landing-Phase Safety Event Prediction from Flight Data

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, benchmark, spec
- 作者：Taha Asghar, Bilal Mufti, Syed Qasim Zaheer, Luqman Ahmed
- 链接：[arXiv](https://arxiv.org/abs/2611.08386) · [PDF](https://arxiv.org/pdf/2611.08386) · [HF](https://huggingface.co/papers/2611.08386)

Landing-phase safety-event prediction requires the detection of rare abnormal approaches within strongly imbalanced multivariate flight data. Capturing coupled temporal behavior while distinguishing event-specific signatures across airport operating contexts remains a central modeling challenge. This study proposes an interpretable hybrid feature-fusion framework for multiclass landing-phase safety-event prediction.…

## 104. StepBack: Step-Level Error-Localized Resampling for Efficient Test-Time Reasoning

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, benchmark, coding
- 作者：Yang Ouyang, Jung-Eun Kim
- 链接：[arXiv](https://arxiv.org/abs/2611.08403) · [PDF](https://arxiv.org/pdf/2611.08403) · [HF](https://huggingface.co/papers/2611.08403)

Self-consistency (SC) is a widely used decoding strategy for improving chain-of-thought reasoning, but it requires sampling many complete reasoning trajectories with a preset budget. Its efficient variants reduce the cost mainly by stopping full-trajectory sampling early or distributing the number of samples across questions. In this paper, we propose StepBack, a step-level error-localized resampling method for…

## 105. Spectral and Subspace Dynamics of LoRA in Supervised Fine-Tuning and Reinforcement Learning

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, reinforcement learning, spec
- 作者：Chenruo Liu, Zihan Wang, Yijun Dong, Qi Lei
- 链接：[arXiv](https://arxiv.org/abs/2611.08414) · [PDF](https://arxiv.org/pdf/2611.08414) · [HF](https://huggingface.co/papers/2611.08414)

Low-rank adaptation (LoRA) is commonly used in both supervised fine-tuning (SFT) and reinforcement learning (RL), often under similar optimizer settings. Yet, how the different dynamics of the two stages manifest in the low-rank increment that LoRA optimizes remains unclear. Tracking the singular spectrum and subspaces of LoRA updates on mathematical reasoning tasks, we find that RL concentrates the spectrum at…

## 106. InfMasking: A Unified Variational Framework for Synergistic Multimodal Learning

- 分数：5.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, spec
- 作者：Liangjian Wen, Qun Dai, Jiang Duan, Yong Dai, Jianzhuang Liu, Dongkai Wang, Jun Wang, Fuyuan Cao, Zenglin Xu, Zhao Kang
- 链接：[arXiv](https://arxiv.org/abs/2611.07702) · [PDF](https://arxiv.org/pdf/2611.07702) · [HF](https://huggingface.co/papers/2611.07702)

Multimodal models are expected to exploit synergistic information, that is, information available only when multiple modalities are observed together. In practice, however, a fusion module can fit the training objective by relying on a dominant modality or on information that modalities share, and the synergy between modalities is often left unused. We propose InfMasking, a unified multimodal learning framework…

## 107. FlyingDrones: A Dataset and Benchmark for Optical Flow Estimation from UAV motion

- 分数：5.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark
- 作者：Laurenz Ruzicka, Roman Pflugfelder, Daniel Cremers
- 链接：[arXiv](https://arxiv.org/abs/2611.07705) · [PDF](https://arxiv.org/pdf/2611.07705) · [HF](https://huggingface.co/papers/2611.07705)

Optical flow is an important cue for drone analysis in aerial surveillance, airspace monitoring, and long-range target tracking, where motion remains informative when appearance is weak. Estimating the motion of small Unmanned Aerial Vehicles, however, is difficult because distant targets occupy few pixels, have low contrast, and move against complex dynamic backgrounds. Standard optical-flow benchmarks emphasize…

## 108. Towards Generalist Graph-Level Anomaly Detection

- 分数：5.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, spec
- 作者：Junjun Pan, Yixin Liu, Yu Zheng, Fuyi Li, Alan Wee-Chung Liew, Shirui Pan
- 链接：[arXiv](https://arxiv.org/abs/2611.07706) · [PDF](https://arxiv.org/pdf/2611.07706) · [HF](https://huggingface.co/papers/2611.07706)

Graph-level anomaly detection (GLAD) aims to identify graphs that deviate significantly from the majority. While recent advances have achieved competitive performance, existing approaches mainly follow a dataset-specific paradigm, requiring substantial in-domain data and training cost when applied to new application scenarios. This limits their scalability and practicality in real-world applications where labeled…

## 109. Extending Reasoning in Typed Decision Models via Looping

- 分数：5.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, language model
- 作者：David Berghaus, Arber Zela, Behzad Shomali, Markus Frey, Mehdi Ali, Rafet Sifa, Volkan Cevher
- 链接：[arXiv](https://arxiv.org/abs/2611.07736) · [PDF](https://arxiv.org/pdf/2611.07736) · [HF](https://huggingface.co/papers/2611.07736)

Typed decision models choose among a fixed set of answer options in a single forward pass, so unlike generative language models they cannot spend more test-time compute on hard inputs by generating more tokens. Looping a block of layers offers this compute in latent space without adding parameters, but prior work found no gain from loops retrofitted into conventionally pretrained models. We show that such loops help…

## 110. Ordering Multivariate Time Series by Volatility Memory: A Temporal Convolutional Approach to Volatility Heredity

- 分数：5.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, benchmark
- 作者：Kaoutar El Azaar, Mohamed Hamlich, Moncef Garouani, Franck Ravat, Asmae Chakir, Mohamed Tabaa
- 链接：[arXiv](https://arxiv.org/abs/2611.07746) · [PDF](https://arxiv.org/pdf/2611.07746) · [HF](https://huggingface.co/papers/2611.07746)

Volatility dynamics can carry information about temporal relationships that is not apparent in the conditional mean. Extracting this information is difficult because the persistence of each variable can obscure its dependence on other variables. This paper presents QS-TCN, a method for ordering multivariate time series that combines statistical estimates of volatility memory with temporal convolutional learning.…

## 111. Foresee to Trade: Forecast-Augmented Policy Optimization for Portfolio Management

- 分数：5.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, evaluation
- 作者：Zeyu Liu, Xuanzhi Feng, Haoran Xu, Lai Sing Kwong, Yang Li, Hualei Zhang, Hao Chen, Jie Zhang, Xiaoyi Pang, Song Guo
- 链接：[arXiv](https://arxiv.org/abs/2611.07750) · [PDF](https://arxiv.org/pdf/2611.07750) · [HF](https://huggingface.co/papers/2611.07750)

Online investment services must translate asset opportunities into investment outcomes for users' accounts, yet the same market opportunity can warrant different account actions. We study how supervision from future asset opportunities can strengthen account-level trading decisions and propose Forecast-Augmented Relative Policy Optimization (FRPO). FRPO separately supervises asset opportunities and account decisions…

## 112. The Intrusion Pathway: How Non-Evidential Context Degrades Language Model Performance

- 分数：5.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：language model, retrieval
- 作者：Dikshant Kukreja, Gautam Gupta, Avni Mittal, Avinash Anand, Kritarth Prasad, Zhengkui Wang, Timothy Liu, Rajiv Ratn Shah, Aik Beng Ng, Simon See, Erik Cambria
- 链接：[arXiv](https://arxiv.org/abs/2611.07778) · [PDF](https://arxiv.org/pdf/2611.07778) · [HF](https://huggingface.co/papers/2611.07778)

Language models lose accuracy when a prompt contains non-evidential context: irrelevant statements from unrelated domains, or random off-distribution tokens, with no competing answer and no semantic overlap with the query. Such noise pervades retrieval-augmented, tool-using, and long-context deployments, yet the failure has lacked a mechanistic account. We trace the corruption to the Intrusion Pathway, which starts…

## 113. Dataset Collection and Fine-Tuning of NLLB for German--English Translation

- 分数：5.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, coding
- 作者：SK Deeraj, Yash Ingle, Pruthwik Mishra
- 链接：[arXiv](https://arxiv.org/abs/2611.07797) · [PDF](https://arxiv.org/pdf/2611.07797) · [HF](https://huggingface.co/papers/2611.07797)

This paper describes the curation of a high-quality parallel corpus from OPUS Books and the fine-tuning of Meta's NLLB-200 models for German--English translation. We detail a dataset extraction pipeline that filters 45k raw OPUS sentence pairs to 25k high-quality examples through encoding validation, length filtering, language identification, deduplication, and quality scoring. We present a reproducible fine-tuning…

## 114. Decodability Is Not Validity: Evaluating Nuisance Sensitivity in Language Model Concept Probes

- 分数：5.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：language model, spec
- 作者：Ayal Klein
- 链接：[arXiv](https://arxiv.org/abs/2611.07805) · [PDF](https://arxiv.org/pdf/2611.07805) · [HF](https://huggingface.co/papers/2611.07805)

Two concept probes can be equally accurate at predicting a concept from a language model's hidden states while their scores contain different mixtures of the target concept and a correlated nuisance attribute. In four target--nuisance settings (two aspect sentiments in CEBaB; occupation and gender in BiasBios; Amazon review sentiment with negation, and with first-person framing), two LLMs, and a population of…

## 115. THG-Omni: Traceable Human-Centric Graph Supervision for Video Reasoning

- 分数：5.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, evaluation
- 作者：Jisheng Dang, Kai Wei, Ronghao Lin, Bimei Wang, Hong Peng, Wei-Shi Zheng, Bin Hu, Qi Tian, Tat-Seng Chua
- 链接：[arXiv](https://arxiv.org/abs/2611.07836) · [PDF](https://arxiv.org/pdf/2611.07836) · [HF](https://huggingface.co/papers/2611.07836)

Omni-modal models can answer questions about video, but their predictions rarely show which participant, event, or interval supports an answer. Moreover, answer-level supervision alone does not teach a model to interpret structured video evidence. To systematically mitigate this issue, we present THG-Omni, a human-centric graph-supervision framework that links Segment Anything Model~3 participant tracks with…

## 116. CORE: Coarse-to-Fine Search with Context Management for Deep Research

- 分数：5.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, benchmark
- 作者：Hoang Tran Vuong, Ngoc Quan Pham, Hung Bui, Fatih Porikli, Dat Quoc Nguyen
- 链接：[arXiv](https://arxiv.org/abs/2611.07859) · [PDF](https://arxiv.org/pdf/2611.07859) · [HF](https://huggingface.co/papers/2611.07859)

Deep research agents answer complex questions through repeated search. They rely on a harness that runs their tool calls and returns evidence to their context. This creates a trade-off: Search works best over long passages, which give enough context for reliable semantic matching. But the returned evidence should be short, because every observation stays in the agent's context for the rest of the trajectory. We…

## 117. OcTreeMamba: Topology-Aware Mamba for 3D Medical Segmentation via Octree Sparsification

- 分数：5.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, spec
- 作者：Kaixiang Mai, Jiaqi Yu, Yuzhu Ji, Yiqun Zhang, Zhijie Wang, Haijun Zhang, Yiu-ming Cheung
- 链接：[arXiv](https://arxiv.org/abs/2611.07865) · [PDF](https://arxiv.org/pdf/2611.07865) · [HF](https://huggingface.co/papers/2611.07865)

Accurate segmentation of 3D anatomical structures is crucial to medical image analysis. Recently, Mamba-based approaches have achieved promising segmentation performance in capturing long-range dependencies with linear-time computational complexity. However, heuristic selective scanning strategies inherently disrupt the intrinsic spatial hierarchy and increase computational redundancy, ignoring the inherent sparsity…

## 118. Do Recommenders Need to Think in Words? Latent Reasoning for Efficient LLM-Based Recommendation

- 分数：5.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, benchmark
- 作者：Hongyang Su, Beibei Kong, Lei Cheng, Chengxiang Zhuo, Zang Li
- 链接：[arXiv](https://arxiv.org/abs/2611.07866) · [PDF](https://arxiv.org/pdf/2611.07866) · [HF](https://huggingface.co/papers/2611.07866)

LLM-based recommender systems increasingly generate chain-of-thought (CoT) text before each item prediction to activate the LLM's reasoning capacity, costing tens to hundreds of extra tokens per recommendation at inference. We ask whether inference-time reasoning artifacts (textual or latent) can be replaced by training-time supervision alone, without loss of accuracy. We propose LatentRec, a framework for LLM-based…

## 119. Network Effect Decomposition for Causal Effect Estimation under Network Interference

- 分数：5.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, spec
- 作者：Zhirong Huang, Wenzhen Zhang, Guangquan Lu, Boyan Chen, Debo Cheng, Shichao Zhang
- 链接：[arXiv](https://arxiv.org/abs/2611.07879) · [PDF](https://arxiv.org/pdf/2611.07879) · [HF](https://huggingface.co/papers/2611.07879)

Estimating causal effects from observational network data requires accounting for both individual treatment and neighborhood exposure. Existing outcome models commonly incorporate these intervention variables into a joint predictor and estimate causal effects through prediction contrasts, leaving the corresponding response components implicit. We propose the $\underline{N}$etwork $\underline{E}$ffect…

## 120. InnerLogic-Surg: An Open Surgical Foundation Model via Continual Pretraining

- 分数：5.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, spec
- 作者：Kun Yuan, Hao Ding, Yiqing Shen, Gasper Podobnik, Benjamin Killeen, Tito Porras, Axel Krieger, Mathias Unberath
- 链接：[arXiv](https://arxiv.org/abs/2611.07883) · [PDF](https://arxiv.org/pdf/2611.07883) · [HF](https://huggingface.co/papers/2611.07883)

Vision foundation models are the backbone of modern surgical image analysis, yet most surgical systems still rely on encoders pretrained on natural images or on specialist models trained from scratch on comparatively small datasets. Pretraining encoders on large amounts of surgery-specific data has the potential to generally enhance the performance of surgical image analysis methods simply by providing stronger…
