# 每日 AI 论文

生成时间：2026-11-09 06:29 UTC  ·  共 14 篇（已按 arXiv ID 去重）

来源：Hugging Face Daily Papers + arXiv（cs.AI / cs.LG / cs.CL / cs.CV）。
排序：HF 上榜、点赞、多源命中、兴趣词。兴趣词可在 `config.json` 改。

## 1. Beneath the Surface: What We Overlook When We Talk About Agent Evolution

- 分数：24.5  ·  HF 赞：17  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark, coding, spec
- 作者：Xiaobo Wang, Zimu Wang, Siyu Ye, Jiaqi Li, Min Tang, Jun Bai, Yuling Shi, Ruobing Wang, Jingjing Zhang, Chaofan Wang, Kai Wu, Mengnan Qi, Kai Cai, Xiaodong Gu, Qi Liu, Zilong Zheng
- 链接：[arXiv](https://arxiv.org/abs/2611.07624) · [PDF](https://arxiv.org/pdf/2611.07624) · [HF](https://huggingface.co/papers/2611.07624)

Agent harness evolution enables recursive self-improvement (RSI) without updating model weights. We examine whether higher benchmark scores yield reliable, efficient, and transferable improvement. We evaluate four methods across harnesses, general and coding tasks. Repeated evaluations, controlled agent expansion, component interventions, and admission replays reveal recurring patterns. All sixteen evolved agents…

## 2. EvoWorld: Towards Out-of-Sight World Evolution in Generative Video Models

- 分数：19.5  ·  HF 赞：15  ·  来源：huggingface
- 兴趣命中：reasoning, language model
- 作者：Yequan Bie, Dengyang Jiang, Zhixuan Chen, Xiaozhuan Liang, Haoxuan Che, Quande Liu, Xi Chen, Hao Chen
- 链接：[arXiv](https://arxiv.org/abs/2611.06748) · [PDF](https://arxiv.org/pdf/2611.06748) · [HF](https://huggingface.co/papers/2611.06748)

Generative video models are increasingly used as visual world simulators, yet their primary strength lies in rendering plausible pixels rather than reasoning about how a world should evolve. Coherent world evolution requires more than visual fidelity: when an event occurs, a model must infer its consequences for the entities in the world and then render the resulting state. For example, after a wild beast appears,…

## 3. Exploring Weight-Space Programming: Capabilities, Generalization, and Limitations

- 分数：19.0  ·  HF 赞：6  ·  来源：huggingface
- 兴趣命中：agent, reasoning, evaluation, benchmark, spec
- 作者：Junru Hu, Cheng Tang, Wei Li, Hongze Zhu, Chun-Mei Feng, Qi Zhang, Yirong Chen, Ming Hu
- 链接：[arXiv](https://arxiv.org/abs/2611.09382) · [PDF](https://arxiv.org/pdf/2611.09382) · [HF](https://huggingface.co/papers/2611.09382)

Weight-Space Programming (WSP) enables reasoning agents to directly inspect and modify neural network parameters, offering an alternative to gradient-based model adaptation. However, its capabilities, cross-task generalization, and practical limitations remain insufficiently understood. We systematically investigate WSP through 16 editing trajectories across seven benchmarks and two model scales (Qwen3.5-0.8B and…

## 4. Video-Coder: Reinforcing Agentic Coding for Video Generation

- 分数：17.5  ·  HF 赞：7  ·  来源：huggingface
- 兴趣命中：agent, reinforcement learning, coding
- 作者：Chaoyang Wang, Sicheng Gao, Junan Hu, Kunyang Li, Dongyang Chen, Yiyang Zhou, Huaxiu Yao, Yong Jae Lee, Radu Timofte, Yuzhang Shang
- 链接：[arXiv](https://arxiv.org/abs/2611.09894) · [PDF](https://arxiv.org/pdf/2611.09894) · [HF](https://huggingface.co/papers/2611.09894)

Recent years have witnessed remarkable progress in video generation in terms of visual quality and temporal consistency. However, generating videos with precise spatial structure, coherent motion dynamics, and controllable scene composition remains challenging. In this paper, we introduce Video-Coder, the first attempt to train a code-driven video generation agent, which autonomously writes and executes code to…

## 5. Frontier3DBench: Benchmarking Coding Agents for 3D Creation across Objects, Scenes, and Interactive Open Worlds

- 分数：17.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark, coding, spec
- 作者：Xinjie Lin, Qingle Liu, Wenyi Li, John Lam, Xiaoqiu Wang, Deyao Hong, Mingju Gao, Zheng Jiang, Yizhe Chi, Youjie Zheng, Calvin Xiao, Kaisen Yang, Huan-ang Gao
- 链接：[arXiv](https://arxiv.org/abs/2611.09017) · [PDF](https://arxiv.org/pdf/2611.09017) · [HF](https://huggingface.co/papers/2611.09017)

Coding agents combine visual understanding with program execution, offering a new route to automated 3D creation. By translating images and instructions into editable programs, they bring reconstruction, generation, and editing into a shared workflow. Yet existing benchmarks fragment evaluation across task scopes and protocols, leaving their capabilities across construction levels unclear. We propose…

## 6. AgentBaton: Efficient Model Collaboration in Agentic Tasks

- 分数：16.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：agent, reasoning, benchmark
- 作者：Junlong Li, Jindong Jiang, Yonggan Fu, Jiarui Yao, Hanrong Ye, Wonmin Byeon, Peter Belcak, Hao Zhang, Pavlo Molchanov
- 链接：[arXiv](https://arxiv.org/abs/2610.35959) · [PDF](https://arxiv.org/pdf/2610.35959) · [HF](https://huggingface.co/papers/2610.35959)

Solving long-horizon agentic tasks requires language agents to interact with their environments over multiple steps, and reliable performance often comes from the expensive capable models available through cloud providers. Meanwhile, alternative efficient models with inferior performance but a much lower cost are emerging, including lower-tier cloud models and smaller open-weights models deployable on local…

## 7. OneTrans-GSR: A Generative Slate Ranking Paradigm Unifying Reranking and Mix-Ranking with One Autoregressive Transformer

- 分数：16.0  ·  HF 赞：0  ·  来源：huggingface
- 兴趣命中：reinforcement learning, evaluation, coding, spec
- 作者：Feng Cheng, Yu-Hsuan Huang, Fengyi Wang, Chaofan Zhou, Zhennan Zhu, Huan He, Bo Zhang, Ruoqi Zhang, Zhanfeng Mo, Ziwei Liu, Lanyi Li, Yifeng Pan, Junhua Long, Ziqiu Zhou, Yue Lin, Shaowei Liu
- 链接：[arXiv](https://arxiv.org/abs/2611.04720) · [PDF](https://arxiv.org/pdf/2611.04720) · [HF](https://huggingface.co/papers/2611.04720)

Industrial recommender systems allocate substantial computation to pointwise candidate scoring, yet separate reranking and mix-ranking stages still assemble the final exposure slate using hand-crafted rules and specialized low-capacity models. Mix-ranking combines product cards, short videos, livestreams, and advertising cards supplied by distinct upstream business channels. Although these rules and models encode…

## 8. Confucius4-R2T2: A Stable-Prefix Streaming ASR Model for Real Real-Time Transcription

- 分数：15.0  ·  HF 赞：6  ·  来源：huggingface
- 兴趣命中：agent, evaluation
- 作者：Daniel Huang, Qi He, Shaoxiong Duan, Yingjie Li, Qiao Cheng, Yitao Duan
- 链接：[arXiv](https://arxiv.org/abs/2611.06043) · [PDF](https://arxiv.org/pdf/2611.06043) · [HF](https://huggingface.co/papers/2611.06043)

Streaming speech recognition is increasingly consumed by machines, such as translators and voice agents, that act on each token as it appears. A token that is later revised costs wasted work or a wrong action. In this work, we present Confucius4-R2T2 (short for Real Real-Time Transcription), a stable-prefix streaming ASR model that never modifies its earlier output while maintaining high accuracy and low latency.…

## 9. "PRISM" Is Not All You Need: Cross-Topic Name Collisions and Scientific Paper Retrieval

- 分数：14.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：evaluation, spec, retrieval
- 作者：Jingjie Ning, Xueqi Li, Yibo Kong
- 链接：[arXiv](https://arxiv.org/abs/2611.01362) · [PDF](https://arxiv.org/pdf/2611.01362) · [HF](https://huggingface.co/papers/2611.01362)

Scientific names increasingly connect papers from different research topics, leaving readers to recover a paper's identity from context. We study this convergence in 564,861 AI-related arXiv records. Cross-topic name collision grows 4.33-fold from a pooled 2020-2022 reference to 2026, compared with 1.12-fold within topics. A second sentence encoder reproduces the pattern, and name-group resampling quantifies its…

## 10. LLMs Don't Know What They Know: Benchmarking Temporal Self-Knowledge for Financial Backtesting

- 分数：14.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：benchmark, language model, large language
- 作者：Lingfei Qian, Yan Wang, Xueqing Peng, Yupeng Cao, Yuechen Jiang, Zhuohan Xie, Anke Xu, Wenbo Cao, Jiarui Chen, Zehan Li, Jimin Huang, Alejandro Lopez-Lira, Yuehua Tang, Sophia Ananiadou, Jian-Yun Nie
- 链接：[arXiv](https://arxiv.org/abs/2611.06808) · [PDF](https://arxiv.org/pdf/2611.06808) · [HF](https://huggingface.co/papers/2611.06808)

Financial backtests of large language models (LLMs) are meaningful only if the model did not already know the outcomes it is asked to predict. Practitioners guard against this by trusting a vendor's stated knowledge cutoff, by asking the model what it knows, or by instructing it to answer as of a past date. To verify whether any of these safeguards can be trusted, we introduce FinDendro, a benchmark of 2,226 dated…

## 11. The Last Mile to the Real World: Agent-Native Primitives as Reusable Building Blocks for Solving Real-World Tasks

- 分数：14.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：agent, benchmark, spec
- 作者：Haibo Jin, Peng Kuang, Xiaopeng Yuan, Lucheng Fu, Jerry Wang, Xucheng Yu, Yaoning Yu, Dehao Wu, Runguo Li, Colin Su, Jingxuan Sun, Xuyang Liu, Haojing Luo, Haohan Wang
- 链接：[arXiv](https://arxiv.org/abs/2611.07461) · [PDF](https://arxiv.org/pdf/2611.07461) · [HF](https://huggingface.co/papers/2611.07461)

How can an agent handle a real-world task end to end? Frontier models with their own harnesses still fall short on real-world benchmarks: on Terminal-Bench 4.0, GPT-5.6 Sol with Codex resolves 37.3% of the tasks and Claude Opus 5 with Claude Code 51.8%. These tasks fail at the step from reaching a resource to applying it, which we call the last mile to the real world. Existing approaches put the resource within…

## 12. Sketchpad: certified exact arithmetic with a small vision-language model

- 分数：14.0  ·  HF 赞：0  ·  来源：huggingface
- 兴趣命中：tool use, memory, language model
- 作者：Mostafa 'Neo' Mohsenvand
- 链接：[arXiv](https://arxiv.org/abs/2611.04434) · [PDF](https://arxiv.org/pdf/2611.04434) · [HF](https://huggingface.co/papers/2611.04434)

Language models are accurate on most long-arithmetic problems, but their accuracy is estimated on samples and carries no guarantee for an unseen input; tool use is exact but moves the computation outside the network. We show that exactness at all input lengths becomes a finite, checkable property of a network when each of its steps reads only a bounded view of an external working memory. In Sketchpad, Qwen3.5-0.8B…

## 13. PREEN: Exemplar-Based Color Style Transfer with Smartphone Editor Presets

- 分数：11.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：benchmark
- 作者：Beomjin Ahn
- 链接：[arXiv](https://arxiv.org/abs/2610.36896) · [PDF](https://arxiv.org/pdf/2610.36896) · [HF](https://huggingface.co/papers/2610.36896)

We present PREEN (Preset Regression via an Exemplar-based Editor Network), which casts color style transfer as regression onto the 29 parameters of a deterministic image editor. Given a content image and a style reference, PREEN predicts a preset, a vector of editor slider values that is interpretable and editor-consumable, not a raster image. The key obstacle is supervision, since an arbitrary real reference lacks…

## 14. OmniLatent: Unified Latent for 3D Part Modeling

- 分数：8.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：-
- 作者：Yunhan Yang, Yunfei Zhao, Zeqiang Lai, Jiachen Xu, Minxiu Wang, Xintong Han, Xiangyu Yue, Xihui Liu, Chunchao Guo
- 链接：[arXiv](https://arxiv.org/abs/2611.09055) · [PDF](https://arxiv.org/pdf/2611.09055) · [HF](https://huggingface.co/papers/2611.09055)

3D part decomposition is a central capability for editable asset creation, yet existing workflows typically segment a completed mesh as a post-processing step, making the result sensitive to geometric artifacts, texture ambiguity, and limited part-level annotations. We present OmniLatent, a unified latent modeling framework for 3D part decomposition. Instead of predicting part labels in isolation, OmniLatent learns…
