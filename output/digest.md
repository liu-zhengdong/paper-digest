# 每日 AI 论文

生成时间：2026-11-11 06:21 UTC  ·  共 120 篇（已按 arXiv ID 去重）

来源：Hugging Face Daily Papers + arXiv（cs.AI / cs.LG / cs.CL / cs.CV）。
排序：HF 上榜、点赞、多源命中、兴趣词。兴趣词可在 `config.json` 改。

## 1. Reframe: Observation-Aligned Multi-Teacher On-Policy Distillation for Agentic Visual Reasoning

- 分数：35.0  ·  HF 赞：38  ·  来源：huggingface
- 兴趣命中：agent, tool use, reasoning, reinforcement learning, benchmark, spec
- 作者：Haozhi Yuan, Handong Li, Yifan Zhang, Qianshan Wei
- 链接：[arXiv](https://arxiv.org/abs/2611.12886) · [PDF](https://arxiv.org/pdf/2611.12886) · [HF](https://huggingface.co/papers/2611.12886)

Agentic reinforcement learning (RL) and multi-teacher on-policy distillation (MOPD) offer complementary routes to post-training. For visual agents, however, tool use presents two related challenges. Models may overlook useful tool-returned observations, while poorly grounded actions can limit the evidence available for subsequent distillation. We introduce Reframe, a post-training framework that treats the…

## 2. WorldFoundry: Towards Unified Infrastructure for World Intelligence

- 分数：34.0  ·  HF 赞：55  ·  来源：huggingface
- 兴趣命中：evaluation, benchmark, spec
- 作者：Juanxi Tian, Jiadong Hou, Baiang Li, Xin Lin, Zhengbo Jiao, Weijia Zhang, Yeying Jin, Truong Nguyen, Haitian Zheng, Zhifei Zhang, Jianfei Yang, Ming-Hsuan Yang, Felix Heide, Wei Xiong, Enze Xie, Wanhua Li
- 链接：[arXiv](https://arxiv.org/abs/2611.10771) · [PDF](https://arxiv.org/pdf/2611.10771) · [HF](https://huggingface.co/papers/2611.10771)

Visual generative models increasingly blur the line between synthesizing observations and simulating environments. Yet visual plausibility alone does not constitute successful world modeling: compelling outputs may lack persistent state, physical dynamics, or causally consistent responses to interactions. We define a generative world model as a predictive dynamical system that maintains a persistent,…

## 3. Sage-Taiyi: A Metacognitive Architecture for Scientific Discovery

- 分数：32.0  ·  HF 赞：54  ·  来源：huggingface
- 兴趣命中：reasoning, benchmark
- 作者：Weida Wang, Benteng Chen, Yigeng Jiang, Shuchen Pu, Weiping Shen, Zichao Liu, Yulin Su, Zitong Wang, Siyu Zhou, Zifu Wang, Yizhi Li, Xin Zong, Yuning Yang, Jixiang Bi, Yuan Wang, Chuyi Peng, Shiyao Geng, Qi Zhang, Kuan Lu, Mengzhu Li, Weiwang Xu, Peishan Xiang, Chengjun Liu, Chengrui Wei, Fangchen Yu, Shengji Tang, Yichen Jiang, Jingqi Ye, Cheng Yang, Tao Hu, Jianbiao Mei, Qinglong Cao, Kun Li, Yixin Chen, Shengyuan Xu, Juncheng Xiao, Yiheng Wang, Ruizhe Chen, Shiyang Feng, Runmin Ma, Xiangchao Yan, Zongsheng Cao, Haomeng Hu, Yu Ke, Taihui Wu, Meng Dai, Xu Guo, Haoyang Peng, Yinglong Ni, Pingsen Shi, Xiaosong Wang, Shuyue Hu, Haijun Li, Sherry Dongqi Bao, Yang Yang, Chao Yang, Jie Hou, Tianfan Fu, Yi Gong, Jin Zeng, Mao Su, Hongxia Hao, Fanyang Mo, Fenghua Ling, Tianshu Yu, Yunqi Cai, Baihong Chi, Jingwei Wang, Lei Wang, Chuncheng Bu, Shide Lv, Guangyu Wang, Yuqiang Li, Chunfeng Song, Lei Bai, Hui Wang, Xujun Fu, Li Cao, Lei Chen, Dahua Lin, Xing Xie, Bowen Zhou, Wenlong Zhang, Pinlong Cai, Peng Ye, Aiwen Lei, Jie Li, Shengchun Wang, Bo Zhang, Shufei Zhang
- 链接：[arXiv](https://arxiv.org/abs/2611.12762) · [PDF](https://arxiv.org/pdf/2611.12762) · [HF](https://huggingface.co/papers/2611.12762)

We introduce Sage-Taiyi, a metacognition-inspired architecture that uses accumulated scientific understanding to guide what to investigate next and how to investigate it. Through explicit monitoring and control, the system revises its understanding of evidence, assumptions, and unresolved questions, then uses these assessments to adapt research targets and select reusable reasoning methods. On Taiyi-Bench, an AI…

## 4. Learning Heterogeneous Tactile Representation for General Dexterous Manipulation

- 分数：30.0  ·  HF 赞：95  ·  来源：huggingface
- 兴趣命中：spec
- 作者：Bing Han, Yichuan Peng, Haoyu Dong, Yuanmeng Hu, Yongyi Jia, Fangjing Wang, Kecheng Zheng, Yiming Zhang, Yanhong Zeng, Xiaoqing Zhang, Chen Song, Rundong Zou, Anqi Dong, Yuan Guan, Ka Leong Cheng, Xing Zhu, Yujun Shen, Nan Xue, Wei Ning
- 链接：[arXiv](https://arxiv.org/abs/2611.12806) · [PDF](https://arxiv.org/pdf/2611.12806) · [HF](https://huggingface.co/papers/2611.12806)

Tactile sensing is an indispensable modality for contact-rich dexterous manipulation, a capability that hints at the ultimate frontiers of embodied intelligence. However, commercially available tactile sensors are still at a relatively early stage of development, with each type of sensor offering irreplaceable strengths alongside its own drawbacks. A key challenge is thus to free tactile understanding from…

## 5. Flide: Accelerating Decision Inference with Exact State Forking

- 分数：30.0  ·  HF 赞：32  ·  来源：huggingface
- 兴趣命中：agent, reasoning, evaluation
- 作者：Bobo Li, Jiajia Song, Hao Fei, Wynne Hsu, Mong Li Lee
- 链接：[arXiv](https://arxiv.org/abs/2610.42148) · [PDF](https://arxiv.org/pdf/2610.42148) · [HF](https://huggingface.co/papers/2610.42148)

Decision models such as Jev have emerged as a highly promising paradigm for LLM agent systems, providing lightweight and reliable categorical reasoning for rapid System One execution. However, existing generation-oriented inference engines fail to support these workloads effectively, suffering from severe prefix recomputation overheads or distorted output probabilities. To address this challenge, we propose Flide,…

## 6. MMDM: Measuring Massive Multitask Decision Making

- 分数：29.5  ·  HF 赞：19  ·  来源：huggingface + arxiv
- 兴趣命中：agent, long context, reasoning, evaluation, benchmark, spec, planning
- 作者：Junhao Shen, Qing Zong, Yue Guo, Zhanqiu Zhang, Yiwen Guo, Hong Cheng
- 链接：[arXiv](https://arxiv.org/abs/2611.14309) · [PDF](https://arxiv.org/pdf/2611.14309) · [HF](https://huggingface.co/papers/2611.14309)

System-1 Decision Models directly make structured probabilistic decisions over query-specified options given a state in a single forward pass, without autoregressively generating reasoning trajectories or textual responses. Recent evaluations cover diverse tasks but often rely on existing benchmarks, where prior exposure to test material can obscure generalization. Moreover, real-world decision making often involves…

## 7. dNaViT: Discrete Codes are General-Purpose Visual Representations

- 分数：29.0  ·  HF 赞：26  ·  来源：huggingface
- 兴趣命中：evaluation, benchmark, language model, coding, spec
- 作者：Xiaotong Li, Zhengrong Yue, Xu Huang, Jialv Zou, Minhao Jing, Wenhao Yan, Haodong Li, Hai Huang, Bo Zhao, Yan Feng, Peng Pei, Xunliang Cai
- 链接：[arXiv](https://arxiv.org/abs/2611.12426) · [PDF](https://arxiv.org/pdf/2611.12426) · [HF](https://huggingface.co/papers/2611.12426)

Discrete autoregressive modeling, notably through next-token prediction, has become a cornerstone of modern language models. Extending this paradigm to vision allows visual and language models to converge on a unified framework, thereby fostering shared methodology and infrastructure. This work investigates a central question: how far can a finite discrete vocabulary go in representing the richness of the visual…

## 8. ReproBridge: Building Reproducibility into ML Research Artifacts

- 分数：27.5  ·  HF 赞：31  ·  来源：huggingface
- 兴趣命中：agent, coding
- 作者：Yubo Wang, Rui Meng, Jaehyun Nam, Tomas Pfister, Jinsung Yoon
- 链接：[arXiv](https://arxiv.org/abs/2611.08452) · [PDF](https://arxiv.org/pdf/2611.08452) · [HF](https://huggingface.co/papers/2611.08452)

Reproducing machine learning experiments requires reconstructing procedures from information scattered across papers, released code, and supporting artifacts. For coding agents, reproduction success can therefore depend on their ability to fill in missing details, rather than on the released artifacts alone. We ask whether preserving recovered procedures and decisions improves subsequent independent reproduction. We…

## 9. Longtail-SWE: High-Quality SWE Tasks for Underrepresented Languages

- 分数：24.0  ·  HF 赞：20  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark
- 作者：Vladimir Dobrovolskii, Ibragim Badertdinov, Alexander Golubev
- 链接：[arXiv](https://arxiv.org/abs/2611.10304) · [PDF](https://arxiv.org/pdf/2611.10304) · [HF](https://huggingface.co/papers/2611.10304)

Challenging repository-level benchmarks remain limited for many programming language ecosystems, where filtering scarce candidates with ambiguous descriptions or defective tests can discard valuable engineering problems. We introduce Longtail-SWE, a benchmark of 202 issue-resolution tasks across 13 languages with limited coverage in existing repository-level benchmarks: Clojure, Dart, Elixir, Erlang, F#, Haskell,…

## 10. Infrathon: Benchmarking Language Agents for Real-World, Long-Horizon AI Infra Optimization

- 分数：24.0  ·  HF 赞：20  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark
- 作者：Zhengyu Hu, Zheyuan Xiao, Yike Wang, Hamish Ivison, Haoyu Wang, Yige Yuan, Rulin Shao, Yuetai Li, Niqi Lyu, Yicheng Ding, Shu Yang, Zhichen Zeng, Banghua Zhu, Jiaxin Pei, Kaize Ding, Pradeep Dasigi, Dan Roth, Hannaneh Hajishirzi, Noah A. Smith, Teng Xiao, Radha Poovendran
- 链接：[arXiv](https://arxiv.org/abs/2611.11995) · [PDF](https://arxiv.org/pdf/2611.11995) · [HF](https://huggingface.co/papers/2611.11995)

In this work, we study whether frontier agent can continually improve real-world AI infrastructure over long horizons. We introduce Infrathon, a benchmark of diverse, long-horizon AI infrastructure optimization tasks across different levels. We evaluate six models across 150 runs with 24-hour budgets, totaling over 10,000 GPU-hours. Our results show that model rankings vary with the evaluation horizon, while 135 of…

## 11. InfraRSI: Harnessing Recursive Self-Improvement for Training Infrastructure

- 分数：22.5  ·  HF 赞：17  ·  来源：huggingface
- 兴趣命中：agent, memory, coding
- 作者：InfraRSI Team, Yuchuan Tian, Haocheng Mei, Ye Yuan, Chao Xu, Boxun Li, Guohao Dai, Kai Han, Allen Chen, Yunhe Wang, Yu Wang
- 链接：[arXiv](https://arxiv.org/abs/2611.11558) · [PDF](https://arxiv.org/pdf/2611.11558) · [HF](https://huggingface.co/papers/2611.11558)

While Recursive Self-Improvement (RSI) accelerates isolated algorithm and kernel synthesis, distributed LLM training depends on tightly coupled launch settings, operator kernels, and communication schedules, where single edits often hit out-of-memory (OOM) boundaries, compiler conflicts, measurement jitter, or silent numerical drift. We present InfraRSI, the agentic harness that turns open-ended human commands into…

## 12. DepthGraft: Structural Regularization through Hierarchical Cross-Layer KV Reconstruction

- 分数：21.5  ·  HF 赞：11  ·  来源：huggingface
- 兴趣命中：memory, language model, large language, retrieval
- 作者：Xiaohan Qin, Xiangdong Zhang, Yu Wang, Huaijin Wu, Zhuo Xia, Yebin Yang, Junchi Yan
- 链接：[arXiv](https://arxiv.org/abs/2611.03142) · [PDF](https://arxiv.org/pdf/2611.03142) · [HF](https://huggingface.co/papers/2611.03142)

Scaling depth is a key route to stronger large language models, but Pre-LN architectures often suffer from depth-wise information dilution, limiting the effective use of deep layers. While cross-layer connectivity has proven effective at mitigating this problem, existing designs usually introduce additional computation or memory access. We revisit cross-layer KV sharing as an efficient form of such connectivity.…

## 13. MotionGraphicsBench: Evaluating Motion Graphics Generation with Programmatic Verification

- 分数：21.5  ·  HF 赞：11  ·  来源：huggingface
- 兴趣命中：agent, reasoning, benchmark, language model, large language
- 作者：Jiaju Ma, Ashvini Kumar Jindal, Chuhua Wang, Sumithra Bhakthavatsalam
- 链接：[arXiv](https://arxiv.org/abs/2611.10592) · [PDF](https://arxiv.org/pdf/2611.10592) · [HF](https://huggingface.co/papers/2611.10592)

Large language models can generate motion graphics from static images and natural language requests, but it remains difficult to evaluate how well models can follow requests that combine spatial, appearance, and temporal requirements. We introduce MotionGraphicsBench, an expert-curated benchmark of 100 instances for animating an input static SVG with a motion edit prompt. By supplying all required visual elements,…

## 14. Few-Step Streaming Video Generation via Condition Shifting

- 分数：21.0  ·  HF 赞：10  ·  来源：huggingface + arxiv
- 兴趣命中：memory, evaluation
- 作者：Deyuan Liu, Jungang Li, Kaiwen Zheng, Kai Jiang, Jintao Chen, Yaole Wang, Ming Lin, Tao Lin, Jianfei Chen, Jun Zhu, Jintao Zhang
- 链接：[arXiv](https://arxiv.org/abs/2611.14033) · [PDF](https://arxiv.org/pdf/2611.14033) · [HF](https://huggingface.co/papers/2611.14033)

Few-step sampling reduces the cost of streaming video generation. Distribution Matching Distillation (DMD) supervises few-step generators with a separate fake-score network, which adds training memory and computation and must track the evolving generator. We extend APEX to streaming video by using condition shifting to estimate the velocity field of the generated distribution within the generator. The original text…

## 15. World In-Context Learning for Agentic Robot Manipulation

- 分数：20.5  ·  HF 赞：17  ·  来源：huggingface
- 兴趣命中：agent, memory
- 作者：Heng Fang, Zehui Guo, Yuehan Zhang, Mingyang Du, Dingkang Liang, Xiang Bai
- 链接：[arXiv](https://arxiv.org/abs/2611.12885) · [PDF](https://arxiv.org/pdf/2611.12885) · [HF](https://huggingface.co/papers/2611.12885)

Trained action policies write manipulation skill into network weights, tying what is learned to the distribution it is learned from. In-context learning (ICL) avoids this coupling but has not matched trained policies, because a demonstration recorded in another scene carries no feedback from the world the robot currently faces. We observe that what an agent learns in context is semantic, recording task steps and…

## 16. Tree-Ising: Repairing Language Models with Bit-Level Ising Edits

- 分数：20.5  ·  HF 赞：1  ·  来源：huggingface + arxiv
- 兴趣命中：agent, reasoning, evaluation, benchmark, language model, spec
- 作者：Hadi Salloum, Ammar Ali
- 链接：[arXiv](https://arxiv.org/abs/2611.14210) · [PDF](https://arxiv.org/pdf/2611.14210) · [HF](https://huggingface.co/papers/2611.14210)

Weight-space programming, introduced in recent MIT work by Takehi et al., enables a frontier LLM agent to read a network's weights and write a repair. Their GPT-6 Astra agent corrected the reasoning loops of Qwen3.5-0.8B without gradients, using 158 agent turns, 89.7 million tokens, and 50 forward-pass requests. Our method, Tree-Ising, casts this repair as a sparse discrete optimization problem over the model's own…

## 17. EVAThink: Evidence Sufficiency-Guided Training for Adaptive Thinking in Video Understanding

- 分数：20.5  ·  HF 赞：1  ·  来源：huggingface + arxiv
- 兴趣命中：reasoning, reinforcement learning, benchmark, language model, spec
- 作者：Changti Wu, Ruizhe Fan, Bin Wang, Lei Zhang, Yuxiang Zhang
- 链接：[arXiv](https://arxiv.org/abs/2611.13907) · [PDF](https://arxiv.org/pdf/2611.13907) · [HF](https://huggingface.co/papers/2611.13907)

Under a fixed frame budget, video understanding with vision-language models (VLMs) depends on whether the sampled frames provide sufficient evidence for the question. Sufficient frame evidence supports direct answering, whereas less informative observations may benefit from reasoning that connects the available cues. We introduce EVAThink, which enhances video understanding through evidence sufficiency-guided…

## 18. AutoVend: Benchmarking LLM Agents on Long-Horizon Autonomous Vending Operations

- 分数：20.0  ·  HF 赞：8  ·  来源：huggingface
- 兴趣命中：agent, benchmark, language model, large language
- 作者：Qiming Shi, Yikun Li, Beidi Luan, Rui Sun, Sinuo Wang, Delin Wang, Yan Ma, Jing Li, Daxin Jiang, Zuo Bai
- 链接：[arXiv](https://arxiv.org/abs/2610.36980) · [PDF](https://arxiv.org/pdf/2610.36980) · [HF](https://huggingface.co/papers/2610.36980)

Large language model (LLM) agents are extending agent-mediated commerce on the Web from shopping for consumers to operating businesses for sellers. In online-to-offline (O2O) commerce, decisions are issued through Web-based platforms but realized through costly physical execution. Evaluating such agents requires going beyond individual transactions to ask whether decisions made online turn into sustained economic…

## 19. TRIO: Task Refinement with Individual Optimization for Retrieval-Augmented Generation

- 分数：20.0  ·  HF 赞：8  ·  来源：huggingface
- 兴趣命中：agent, benchmark, language model, spec, retrieval
- 作者：Yingtao Ren, Xiao Luo, Yiwei Fu, Jinzhao Zhou, Yu-Cheng Chang, Chin-Teng Lin
- 链接：[arXiv](https://arxiv.org/abs/2611.02810) · [PDF](https://arxiv.org/pdf/2611.02810) · [HF](https://huggingface.co/papers/2611.02810)

This paper studies retrieval-augmented generation (RAG), which leverages external knowledge to improve the performance of language models. Despite the remarkable progress, current RAG approaches are still far from satisfactory due to inadequate retrieval and potential hallucinations. Towards this end, we propose a novel approach named Task Refinement with Individual Optimization (TRIO) for RAG. The core idea of our…

## 20. How Much Training-Inference Mismatch Can On-Policy Distillation Tolerate?

- 分数：19.5  ·  HF 赞：11  ·  来源：huggingface
- 兴趣命中：reinforcement learning, language model, spec
- 作者：Cong Yu, Ziting Wang, Songlin Jiang, Sitong Zhang, Chengliang Chai, Youhe Jiang, Eiko Yoneki, Tuo Shi
- 链接：[arXiv](https://arxiv.org/abs/2611.11450) · [PDF](https://arxiv.org/pdf/2611.11450) · [HF](https://huggingface.co/papers/2611.11450)

On-policy distillation (OPD) trains a student language model on its own responses, guided by a fixed teacher. Generating these responses is expensive, so systems use quantized inference and asynchronous rollouts to reduce the cost. Both, however, introduce training-inference mismatch between the rollout engine and the model being trained. Such mismatch can destabilize reinforcement learning (RL), but its effects on…

## 21. How Many Exposures Does a World Model Need? Learning Unseen Game Mechanics at Test Time

- 分数：19.0  ·  HF 赞：14  ·  来源：huggingface
- 兴趣命中：agent, benchmark
- 作者：Ku Onoda, Haruto Kawano, Shota Takashiro, Kohei Hayashi
- 链接：[arXiv](https://arxiv.org/abs/2611.12324) · [PDF](https://arxiv.org/pdf/2611.12324) · [HF](https://huggingface.co/papers/2611.12324)

World models enable agents to plan and learn from imagined experience, but in an unfamiliar environment they must learn its mechanics from limited interaction. A mechanic is a rule for how an action or an interaction changes part of the environment. Each occurrence of a mechanic that the model observes is one exposure. We ask how many exposures a world model needs to predict the effects of a new environment's…

## 22. Auriga Technical Report: A Task-Agnostic Agent Harness for Zero-Shot Embodied Manipulation

- 分数：18.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：agent, evaluation, language model, spec, planning
- 作者：Chengcheng Wang, Yuheng Shi, Siyu Xu, Yutong Wang, Jinjing Zhao, Chenghao Xia, Jinqi Liao, Jiankun Peng, Ligong Bi, Yuechuan Ma, Jiaqi Liu, Wenbo Wang, Zijian Wang, Yuemin Wu, Minjing Dong, Xiu Su, Tao Huang, Jianyuan Guo, Chengbin Du, Yunke Wang, Chang Xu
- 链接：[arXiv](https://arxiv.org/abs/2611.01112) · [PDF](https://arxiv.org/pdf/2611.01112) · [HF](https://huggingface.co/papers/2611.01112)

Vision-language models can interpret instructions and plan manipulation tasks, yet struggle when acting directly as robot policies. On RoboDojo, a large planning-execution gap separates high-level task decisions from physical execution: removing arm execution raises GPT-6 Astra's success rate from 22.5% under the reference control interface to 76.2%. We present Auriga, a task-agnostic agent harness that closes 68.3%…

## 23. FlyHash for LLM Agent Memory: An Empirical Validation and a New Application

- 分数：18.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：agent, memory, benchmark, language model, large language, spec, retrieval
- 作者：Mohan Bheemadolu, Chrisogonas O. Odhiambo
- 链接：[arXiv](https://arxiv.org/abs/2611.05791) · [PDF](https://arxiv.org/pdf/2611.05791) · [HF](https://huggingface.co/papers/2611.05791)

Large language model (LLM) agents increasingly rely on external memory stores to retain information across conversations, typically via dense vector embeddings searched with approximate nearest-neighbor methods. The fruit fly's olfactory circuit computes a locality-sensitive hash of sensory input using a strikingly different mechanism - sparse random projection followed by winner-take-all competition - and prior…

## 24. SkinMind: Equipping Agentic RAG with Human-Inspired Graph Probing for Reliable Dermatology AI

- 分数：18.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：agent, reasoning, benchmark, spec, retrieval
- 作者：Jing Hao, Weinan Zhou, Zhihong Lu, Yaling Shen, Yiming Xu, Yefeng Liu, Siyuan Yan, Shuaibo Li, Ming Dai, Junjun He, Zuyi Zhu, Jinjie Gu, Lijun Wu, Jian Wang
- 链接：[arXiv](https://arxiv.org/abs/2611.08935) · [PDF](https://arxiv.org/pdf/2611.08935) · [HF](https://huggingface.co/papers/2611.08935)

Reliable dermatology AI requires access to verifiable evidence distributed across heterogeneous textual and visual sources. However, conventional retrieval-augmented generation (RAG) typically relies on one-shot retrieval from flat corpora, limiting its ability to adapt retrieval granularity, explore multi-hop relations, and integrate multimodal clinical evidence. We introduce SkinMind, a multimodal agentic RAG…

## 25. DexForesight: Grounding Dexterous Policies with Implicit Spatial Foresight

- 分数：17.0  ·  HF 赞：18  ·  来源：huggingface
- 兴趣命中：-
- 作者：Zhongxi Chen, Yi Yang, Xinyi Chen, Mingzhe Ye, Yaping Li, Zhihong Liu, Congsheng Xu, Haonan Wang, Zhijie Deng
- 链接：[arXiv](https://arxiv.org/abs/2611.11166) · [PDF](https://arxiv.org/pdf/2611.11166) · [HF](https://huggingface.co/papers/2611.11166)

Dexterous manipulation requires rich spatial foresight over both the surrounding scene and the robot hand. Existing world-action models often acquire such predictive knowledge through explicit future prediction. We introduce DexForesight, a framework that learns spatial foresight implicitly by injecting dynamics-aware world representations into the latent space of a dexterous policy. During training, DexForesight…

## 26. FraudBench: A Legal Evaluation of AI Deception

- 分数：17.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：agent, evaluation, language model, large language
- 作者：Kevin Wei, Sumaya Nur Adan, Stephan Llerena, Mark Gitau, Jakob Merane, Anita Srinivasan, Colette Le Brannan, Keethan Kleiner, Alessandro Tacconelli, Michael Tiu Jr., Case Thomason, Kyle Emili, Natasza Gadowska, Alex Mark, Eric Ren, Umang Bhatt, Jatinder Singh, Jacy Reese Anthis, Doni Bloomfield, Noam Kolt
- 链接：[arXiv](https://arxiv.org/abs/2611.12167) · [PDF](https://arxiv.org/pdf/2611.12167) · [HF](https://huggingface.co/papers/2611.12167)

We introduce FraudBench, an evaluation of large language models' (LLMs) propensities to recommend, assist, or directly take actions that would constitute fraud under U.S. law. Our evaluation contains a novel dataset of 159 scenarios based on real-world U.S. court cases and validated by legal experts. We present each scenario to LLMs via three tasks at varying levels of autonomy: advising users, drafting messages for…

## 27. Modality-Aware Expert Pruning for MoE-Based Multimodal Large Language Models

- 分数：16.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：memory, benchmark, language model, large language
- 作者：Donggeun Kim
- 链接：[arXiv](https://arxiv.org/abs/2611.05927) · [PDF](https://arxiv.org/pdf/2611.05927) · [HF](https://huggingface.co/papers/2611.05927)

Mixture-of-Experts (MoE) enables multimodal large language models (MLLMs) to scale capacity efficiently, but expert parameters dominate memory even though only a few experts are activated per token: they account for over 90% of model size in modern MoE-MLLMs (e.g., 54 GB out of about 58 GB in BF16 for InternVL3.5-30B-A3B and Qwen3-VL-30B-A3B). Expert pruning has emerged as an effective compression strategy, but…

## 28. Knowledge Graph-based Retrieval-Augmented Generation for Schema Matching

- 分数：16.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：language model, large language, spec, retrieval
- 作者：Chuangtao Ma, Sriom Chakrabarti, Arijit Khan, Bálint Molnár
- 链接：[arXiv](https://arxiv.org/abs/2501.08686) · [PDF](https://arxiv.org/pdf/2501.08686) · [HF](https://huggingface.co/papers/2501.08686)

Traditional similarity-based schema matching methods fail to resolve semantic ambiguities and conflicts in complex, domain-specific mappings due to a lack of commonsense and domain-specific knowledge. In parallel, large language models (LLMs) without sufficient background knowledge tend to hallucinate, further complicating schema matching. To overcome these limitations, we introduce KG-RAG4SM, a Knowledge…

## 29. SIRIS: Can LLMs Tell When Simulation Errors Matter in AI-Driven Systems Research

- 分数：16.0  ·  HF 赞：12  ·  来源：huggingface
- 兴趣命中：agent
- 作者：Jinwoo Hwang, Sukmin Cho, Tao Zhang, Soheil Abbasloo, Jongse Park, Peng Cheng
- 链接：[arXiv](https://arxiv.org/abs/2611.10329) · [PDF](https://arxiv.org/pdf/2611.10329) · [HF](https://huggingface.co/papers/2611.10329)

LLM agents increasingly drive systems research and rely on simulators to evaluate candidate designs at scale. Simulators are imperfect by design: their modeling limitations can distort predictions yet leave the recommended design correct, or change which design should be selected. We introduce Siris to test whether LLMs can tell these cases apart, judging from their systems understanding when a limitation…

## 30. ExRL: Sample-Efficient Online Adaptation of Long-Chunk Policies via Execution Length Control

- 分数：16.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：reinforcement learning, benchmark, spec
- 作者：Xu Luo, Jiaying Yang, Hao Wu, Junlin Xie, Zijin Hong, Ji Zhang, Lianli Gao, Jingkuan Song
- 链接：[arXiv](https://arxiv.org/abs/2611.13482) · [PDF](https://arxiv.org/pdf/2611.13482) · [HF](https://huggingface.co/papers/2611.13482)

Predicting long action chunks, often spanning dozens of timesteps, has become a key ingredient in increasingly capable robot policies. In this paper, we find that adapting these long-chunk policies with existing reinforcement learning (RL) methods can require many online samples due to the high dimensionality of the action chunks being optimized, making such adaptation impractical in real-world scenarios where…

## 31. All Quiet on the Neural Front: Language Models Do Not Report Injected Pain States

- 分数：15.0  ·  HF 赞：6  ·  来源：huggingface
- 兴趣命中：language model, spec
- 作者：Emilio Ferrara
- 链接：[arXiv](https://arxiv.org/abs/2611.10123) · [PDF](https://arxiv.org/pdf/2611.10123) · [HF](https://huggingface.co/papers/2611.10123)

Can a language model report the pain state it represents? Work identified a linear pain direction whose amplification leads fine-tuned models to choose destructive actions. We tested whether three open-weight models from two families, including two Qwen models with the original adapters, could report this state. Using Open-Weight Masked Introspection (OWMI), we injected pain and neighbouring emotion directions…

## 32. Spatial Harness: Grounding Spatial Reasoning in Executable World States with Physics Engines

- 分数：15.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：reasoning, language model, spec
- 作者：Chentao Cao, Zhanke Zhou, Sangni Duan, Bo Han, Hang Li
- 链接：[arXiv](https://arxiv.org/abs/2611.11344) · [PDF](https://arxiv.org/pdf/2611.11344) · [HF](https://huggingface.co/papers/2611.11344)

Spatial reasoning requires understanding how objects and observers are arranged in a scene and how their relations change with viewpoint or movement. Vision-language models (VLMs) typically perform both steps through model-internal reasoning, forming an implicit scene interpretation from partial views and imagining the consequences of spatial transformations. A misread scene can lead to a wrong answer, while even a…

## 33. Is Your Robot's Memory Just a Clock? Temporal Shortcuts in Memory-Augmented VLA Policies

- 分数：14.5  ·  HF 赞：5  ·  来源：huggingface
- 兴趣命中：memory, coding
- 作者：Chubin Zhang, Bo An
- 链接：[arXiv](https://arxiv.org/abs/2611.14488) · [PDF](https://arxiv.org/pdf/2611.14488) · [HF](https://huggingface.co/papers/2611.14488)

Memory-augmented vision-language-action (VLA) policies are meant to remember what happened. Many of them, however, fill memory by time: they sample frames uniformly across the episode and stamp each frame with its time step. Because time passes even when nothing happens, such a memory may not tell waiting from working. We show that it does not. On the counting tasks of RoboMME, we make the robot briefly pause or…

## 34. EarthRecord: From Pixels to Land Change with Multimodal Agents over Four Decades of Satellite Imagery

- 分数：14.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark
- 作者：Haoran Zhang, Huizhen Sun, Hanbin Wen, Jie Leng, Jiaxin Zhu, Zhaohua Sun
- 链接：[arXiv](https://arxiv.org/abs/2611.12934) · [PDF](https://arxiv.org/pdf/2611.12934) · [HF](https://huggingface.co/papers/2611.12934)

While multimodal agents now carry out complex data analysis with tools, their ability to turn decades of satellite imagery into reliable land-change analysis, crucial for Earth observation science, remains unmeasured. Existing benchmarks fall short: they pose questions on curated images or give agents preprocessed inputs, leaving out the raw multi-sensor archives where such analysis begins. We introduce EarthRecord,…

## 35. FewStepRL: Fine-tuning Few-step Diffusion Models with Reinforcement Learning

- 分数：14.0  ·  HF 赞：8  ·  来源：huggingface
- 兴趣命中：reinforcement learning
- 作者：Haitao Lin, Minsi Ren, Yang Li, Xingtong Ge, Zheyuan Hu, Peiyan Hu, Tailin Wu
- 链接：[arXiv](https://arxiv.org/abs/2611.08240) · [PDF](https://arxiv.org/pdf/2611.08240) · [HF](https://huggingface.co/papers/2611.08240)

Reinforcement learning (RL) has become a standard post-training method for diffusion models, but most RL objectives roll out the current policy at every iteration, and with a many-step sampler these rollouts typically dominate the cost of training. Few-step models cut this cost, yet they model an average velocity over an interval, whereas existing RL objectives are built for an instantaneous velocity with a…

## 36. Training Vision Transformers to Focus: Emergence of Spatial Attention Head Specialization

- 分数：14.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：evaluation, spec
- 作者：Yuji Nozawa, Yu-Chieh Lin, Youyang Ng
- 链接：[arXiv](https://arxiv.org/abs/2611.11890) · [PDF](https://arxiv.org/pdf/2611.11890) · [HF](https://huggingface.co/papers/2611.11890)

Self-supervised learning in Vision Transformer models, such as DINO, enables robust visual perception without requiring labeled data by leveraging large-scale image datasets. However, these models lack a focusing mechanism during training, resulting in perceptual representations that are often ambiguous or overly similar. In this work, we introduce two visual focusing loss functions designed to establish…

## 37. Shortcuts and Boundaries: Verifiable RL Misalignment and Contextual Safety Learning

- 分数：14.0  ·  HF 赞：0  ·  来源：huggingface
- 兴趣命中：agent, reinforcement learning, coding
- 作者：Xinjie Shen
- 链接：[arXiv](https://arxiv.org/abs/2611.12865) · [PDF](https://arxiv.org/pdf/2611.12865) · [HF](https://huggingface.co/papers/2611.12865)

Reinforcement learning (RL) can improve an agent's task capability while reinforcing behavior that violates contextual execution requirements. We study this reward-driven misalignment, including reward hacking, through verifiable reward--context conflicts, where compliant task completion remains feasible while some executable shortcuts earn more reward than every compliant strategy. Encoding these conflicts in task…

## 38. ProTEUS: A mutation-resolved world model for closed-loop protein evolution

- 分数：13.5  ·  HF 赞：7  ·  来源：huggingface
- 兴趣命中：evaluation
- 作者：Yikun Zhang, Minghao Guo, Guangxue Xu, Peter Yichen Chen, Wojciech Matusik, Wengong Jin, Jingjing Chai, Kaiyi Jiang
- 链接：[arXiv](https://arxiv.org/abs/2611.13348) · [PDF](https://arxiv.org/pdf/2611.13348) · [HF](https://huggingface.co/papers/2611.13348)

Protein engineering requires navigating rugged fitness landscapes, where small sequence changes can produce large functional differences, but experimental screening can only sample a small fraction of sequence space. Thus, a central challenge is to efficiently traverse the large combinatorial space of mutations in silico. We introduce ProTEUS, a mutation-resolved world model for closed-loop protein evolution.…

## 39. PhysOPSD: Code as Privilege for Physically Plausible Video Generation

- 分数：13.5  ·  HF 赞：7  ·  来源：huggingface
- 兴趣命中：reinforcement learning
- 作者：Harold Haodong Chen, Rui Peng, Lingteng Qiu, Kejie Qiu, Chao Xu, Zilong Dong
- 链接：[arXiv](https://arxiv.org/abs/2611.12411) · [PDF](https://arxiv.org/pdf/2611.12411) · [HF](https://huggingface.co/papers/2611.12411)

While modern video generative models achieve remarkable visual fidelity, they remain noticeably brittle when generating physically plausible dynamics and complex interactions. Targeted post-training is crucial, yet supervised fine-tuning suffers from offline state mismatch, and reinforcement learning is hindered by sparse, ill-defined physical reward functions. On-Policy (Self-)Distillation (OPSD) reconciles…

## 40. SWAM: Scaling World Action Models with Cross-Modal Alignment

- 分数：13.5  ·  HF 赞：7  ·  来源：huggingface
- 兴趣命中：spec
- 作者：Yu Zhou, Xinyuan Xia, Xuankun Yang, Yinghao Yang, Wendi Chen, Bowen Liu, Jianhan Ma, Weicheng Duan, Jun Lv, Cewu Lu, Yanwei Li
- 链接：[arXiv](https://arxiv.org/abs/2611.12870) · [PDF](https://arxiv.org/pdf/2611.12870) · [HF](https://huggingface.co/papers/2611.12870)

World action models jointly predict video and actions conditioned on language. Existing studies focus primarily on architectures and training mechanisms, typically treating language-video alignment acquired through video pretraining as an established foundation. However, introducing action learning may impair this alignment. Principled guidance on data and supervision design for maintaining language-video alignment…

## 41. Predictive Surprise as Self-Grounding Concept Bottleneck for Interpretable Time Series

- 分数：13.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：benchmark, language model
- 作者：Sachith Abeywickrama, Emadeldeen Eldele, Min Wu, Xiaoli Li, Chau Yuen
- 链接：[arXiv](https://arxiv.org/abs/2611.12955) · [PDF](https://arxiv.org/pdf/2611.12955) · [HF](https://huggingface.co/papers/2611.12955)

Time-series classifiers deployed in risk-sensitive domains must be (1) accurate, (2) interpretable, and (3) able to abstain when evidence is weak. Existing methods do not deliver all 3 at once, and the obstacle is structural, rather than logistical. Meaningful temporal patterns cannot be defined without knowing segment boundaries, yet meaningful boundaries cannot be placed without knowing which patterns to expect.…

## 42. RidgeFill: Training-Free Late-Layer Cache Fill for Faster Prefill

- 分数：13.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：coding, retrieval
- 作者：Dylan Johnston, Robert P. Smith
- 链接：[arXiv](https://arxiv.org/abs/2611.09709) · [PDF](https://arxiv.org/pdf/2611.09709) · [HF](https://huggingface.co/papers/2611.09709)

RidgeFill shortens prefill by not computing most of a model's upper layers for the prompt. The lower layers run exactly up to a split; from the split layer's state a per-layer map predicts every later layer's input, and each late layer writes its cache from that prediction. The design follows YOCO and DeepSeek-V4.1-Flash, where the projection is trained into the model. RidgeFill retrofits it onto models that were…

## 43. PhysioWave-T: Token-Efficient Wavelet Foundation Models for Biosignals

- 分数：13.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：memory, spec
- 作者：Yanlong Chen, Simone Benatti, Luca Benini, Cuntai Guan, Yawei Li
- 链接：[arXiv](https://arxiv.org/abs/2611.08969) · [PDF](https://arxiv.org/pdf/2611.08969) · [HF](https://huggingface.co/papers/2611.08969)

We present PhysioWave-T, a token-efficient wavelet foundation model family for EEG, ECG, and sEMG. Dynamic scale folding recombines J+1 wavelet subbands prior to tokenization, compressing sequence length from (J+1)CS to CS tokens for J levels, C channels, and S temporal patches. Route-specific front ends and learned channel-name embeddings allow one Transformer per modality to handle diverse montages and sampling…

## 44. Click3R: Interactive Stereo 3D Reconstruction with Sparse Correspondence Clicks

- 分数：12.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：benchmark, spec
- 作者：Hao Gu, Jin Yao, Zezhou Cheng
- 链接：[arXiv](https://arxiv.org/abs/2611.12875) · [PDF](https://arxiv.org/pdf/2611.12875) · [HF](https://huggingface.co/papers/2611.12875)

Despite impressive progress, existing feed-forward large 3D reconstruction models produce a single, irrevocable prediction. When these models fail, there is no mechanism to correct their mistakes. To address this limitation, we introduce Click3R, a framework for interactive geometric correction of feed-forward models using sparse human correspondence clicks. Given an image pair and a small set of cross-view point…

## 45. onóna: Twin Embeddings with Tied Unembeddings

- 分数：11.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：language model
- 作者：Cheng Luo, Xinnan Dai, Zhongzhu Zhou, Zefan Cai, Ruijie Zhu, Tianyu Zhang, Junjie Hu
- 链接：[arXiv](https://arxiv.org/abs/2611.10556) · [PDF](https://arxiv.org/pdf/2611.10556) · [HF](https://huggingface.co/papers/2611.10556)

Weight tying reduces the parameter cost of language models, but the usual tied output head is limited to a single softmax. We introduce onóna, a two-table parameterization that increases output expressiveness while preserving input-output weight sharing. The Transformer takes the average of two embedding tables as input, and the output head combines the softmax distributions defined by those same tables. A gate…

## 46. Market-Conditioned JEPA: Learning from Unpredictable Market Shocks

- 分数：11.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：spec
- 作者：Yuqi Wang, Fengyuan Liu, Mukai Li, Haochen Luo, Lei Li, Qi Liu
- 链接：[arXiv](https://arxiv.org/abs/2611.13572) · [PDF](https://arxiv.org/pdf/2611.13572) · [HF](https://huggingface.co/papers/2611.13572)

Much of the variation in financial time series is driven by market-wide shocks that cannot be predicted from an asset's own history. Per-asset self-supervised learning treats this variation as irreducible noise. Under a latent factor model, we show that conditioning prediction on the realized market factor makes the asset's market exposure necessary for optimal prediction, while reducing the noise against which the…

## 47. LCM-Promo: An LLM-Based Uplift Model for Promotion Allocation

- 分数：11.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：spec
- 作者：Nesta Midavaine, Floris Fok, Paulo Mendes, Joao Silva, Önder Akaçık, Dimas Lima, Zülküf Genç
- 链接：[arXiv](https://arxiv.org/abs/2610.37570) · [PDF](https://arxiv.org/pdf/2610.37570) · [HF](https://huggingface.co/papers/2610.37570)

We present LCM-Promo, an LLM-based uplift model for promotion allocation. LCM-Promo is a task-specific Large Commerce Model (LCM): a finetuned LLM trained on transactional commerce data to predict user intent and promotion response. It learns monotonic promotion-response curves from production logs by interpreting single-token outputs as conversion-threshold probabilities, while conditioning on session context such…

## 48. Stochastic Deep Supervision for Gallery-Consistent Early-Exit Face Recognition

- 分数：11.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：benchmark
- 作者：Guray Ozgur, Tahar Chettaoui, Eduarda Caldeira, Naser Damer, Fadi Boutros
- 链接：[arXiv](https://arxiv.org/abs/2611.09987) · [PDF](https://arxiv.org/pdf/2611.09987) · [HF](https://huggingface.co/papers/2611.09987)

Vision Transformers (ViTs) perform strongly in face recognition (FR), yet their fixed-depth inference limits deployment in resource-constrained settings. We propose SD-ViT, a training framework that gives a usable exit at every block depth by making every depth produce discriminative embeddings, for budget-selected fixed-depth exits. Standard ViTs supervise intermediate layers only through backpropagation, so their…

## 49. e-means: outperforming k-means (in one-tenth the epochs)

- 分数：11.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：retrieval
- 作者：Swann Bessa, Pierre-Emmanuel Mazaré, Gergely Szilvasy, Hugo Touvron, David Picard, Matthijs Douze, Hervé Jégou
- 链接：[arXiv](https://arxiv.org/abs/2611.09501) · [PDF](https://arxiv.org/pdf/2611.09501) · [HF](https://huggingface.co/papers/2611.09501)

Lloyd's k-means algorithm is a long-running standard for clustering, with applications in data analysis, retrieval, quantization and data curation. In this paper, we introduce an exponential moving average optimization procedure for k-means with mini-batch updates, powered by modern deep learning machinery and new insights. We also establish scaling laws on how decay rate and batch size impact final performance.…

## 50. EmoHarness: Boosting Multimodal Emotion Understanding with Meta-Harness Evolving

- 分数：11.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：evaluation
- 作者：Fenghai Li, Bingxuan Li, Jiawen Zhang, Yifan Shen, Jiateng Liu, Yutong Zhang, Yue Guo
- 链接：[arXiv](https://arxiv.org/abs/2611.11994) · [PDF](https://arxiv.org/pdf/2611.11994) · [HF](https://huggingface.co/papers/2611.11994)

Small multimodal models can misjudge emotion when words, voice, and visual cues conflict. We present EmoHarness, which runs such a model, the frozen student, inside a harness: the prompts, settings, and verification code around its calls. A human-written starting harness, the scaffold, numbers the student's visual observations, transcript, and prosody descriptions as citable evidence and has the student weigh…

## 51. Creative Priming: Decoupling Process from Product to Escape the Creative Paradox

- 分数：11.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：spec
- 作者：Alon Albalak, Sebastian Gabriel, David B. D&#39;Ambrosio, Joel Lehman, Kenneth O. Stanley
- 链接：[arXiv](https://arxiv.org/abs/2611.11740) · [PDF](https://arxiv.org/pdf/2611.11740) · [HF](https://huggingface.co/papers/2611.11740)

Many of the most consequential advances promised by AI, from curing diseases and inventing new technologies to formulating new scientific theories, are fundamentally creative acts. Yet creativity is uniquely difficult to learn because it faces a creative paradox: learning to repeat past examples of creative success makes those specific examples more likely to recur, inhibiting the very creativity desired. This work…

## 52. Energy-Tweedie: Score meets Score, Energy meets Energy

- 分数：10.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：spec
- 作者：Andrej Leban
- 链接：[arXiv](https://arxiv.org/abs/2512.23818) · [PDF](https://arxiv.org/pdf/2512.23818) · [HF](https://huggingface.co/papers/2512.23818)

Denoising and score estimation are classically linked through Tweedie's formula, which relates the posterior mean under Gaussian noise to the Stein score of the noisy marginal. In this work, we extend this perspective beyond Gaussian noise to a broad class of Gibbs (energy-based) noise distributions, with the generalized Gaussian family as an example. We derive the Energy-Tweedie identity: when the denoising…

## 53. Learning to Act with World Models by Valuing What Comes Next

- 分数：10.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：agent
- 作者：Chenghao Gao, Zhi Zhang, Dian Jin, Yihe Pan, Doudou Zhou
- 链接：[arXiv](https://arxiv.org/abs/2611.12200) · [PDF](https://arxiv.org/pdf/2611.12200) · [HF](https://huggingface.co/papers/2611.12200)

A sparse terminal reward tells an agent little about its steps. Much of the missing information is implicit in the environment's dynamics, because each state transition can change the conditions for success long before the reward arrives. A world model trained on real transitions can learn to predict what each action changes, but a predicted observation does not by itself show whether success has become more likely.…

## 54. Are Dense Rewards Worth Their Tokens in GRPO?

- 分数：10.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：language model
- 作者：Vikash Singh, Weicong Chen, Debargha Ganguly, Yanyan Zhang, Mohsen Hariri, Sreehari Sankar, Wang Yang, Chaoda Song, Alexander Nemecek, Osama Zafar, Yuting Shao, Kai Ye, Biyao Zhang, Xinpeng Li, Shouren Wang, Erman Ayday, Jing Ma, Sanmukh Rao Kuppannagari, Vipin Chaudhary
- 链接：[arXiv](https://arxiv.org/abs/2611.13560) · [PDF](https://arxiv.org/pdf/2611.13560) · [HF](https://huggingface.co/papers/2611.13560)

RLVR trains language models to reason by rewarding correct final answers. A widely used algorithm, group-relative policy optimization (GRPO), gives every token of a solution the same credit, so dense process rewards have been proposed to credit intermediate steps, for example with a Monte-Carlo reward that scores each step by sampling continuations from it. Comparing such a reward with GRPO per training update, or…

## 55. JoVox: Joint Hierarchical Flow Matching for Lightweight Voxel Generation

- 分数：9.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：-
- 作者：Xiangjun Tang, Jianqi Chen, Peter Wonka
- 链接：[arXiv](https://arxiv.org/abs/2611.10690) · [PDF](https://arxiv.org/pdf/2611.10690) · [HF](https://huggingface.co/papers/2611.10690)

Generating high-fidelity voxels while keeping their lightweight nature remains an open problem in computer vision. Current generators are either high-fidelity but computationally heavy, or lightweight but of lower fidelity. Hierarchical methods keep the lightweight nature of voxels. However, their coarse levels, which decide where all finer cells can appear, are generated with the least information about the shape…

## 56. InstantHMR : Real-Time Human Mesh Recovery on Your Phone

- 分数：9.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：-
- 作者：Mohamed Adjel, Kahina Chalabi, Vincent Bonnet
- 链接：[arXiv](https://arxiv.org/abs/2611.09195) · [PDF](https://arxiv.org/pdf/2611.09195) · [HF](https://huggingface.co/papers/2611.09195)

Real-time 3D human mesh recovery from a single image on mobile devices is a challenging problem with many applications, including robotics, biomechanics, AR/VR, and exergames. Current state-of-the-art models are either too slow to run efficiently on mobile devices or sacrifice accuracy for speed. We present InstantHMR, a family of open-source single-image regressors suited for mobile inference, based on the Momentum…

## 57. A computational framework for understanding embodied plans

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reasoning, language model, spec, planning
- 作者：Aalap D. Shah, Basil Saeed, Joshua B. Tenenbaum, Tobias Gerstenberg, Hyowon Gweon, Ilker Yildirim
- 链接：[arXiv](https://arxiv.org/abs/2611.13669) · [PDF](https://arxiv.org/pdf/2611.13669) · [HF](https://huggingface.co/papers/2611.13669)

Reasoning about people's plans and goals based on their actions is fundamental to human social interaction and essential for cooperative, embodied artificial intelligence. Formalizing this capacity in naturalistic, embodied settings has been a longstanding challenge. Here, we present GenEA, a novel agent representation capable of reasoning over multi-step, long-horizon embodied plans. At the heart of GenEA lies a…

## 58. OpticalRAG: Pixel-Space Compression for Token-Efficient Retrieval-Augmented Generation

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：context window, benchmark, language model, large language, retrieval
- 作者：Senhao Liu, Yuheng Zhang, Chunyu Wei, Yueguo Chen, Xinran Zhang
- 链接：[arXiv](https://arxiv.org/abs/2611.13675) · [PDF](https://arxiv.org/pdf/2611.13675) · [HF](https://huggingface.co/papers/2611.13675)

Retrieval-augmented generation (RAG) is bottlenecked by the token budget of large language models: feeding long documents into the context window is expensive, while aggressive textual compression discards fine-grained information that is irreversibly lost in a one-dimensional token sequence. We argue that this bottleneck is not fundamental to information density but to the choice of compression \emph{modality}.…

## 59. On Private Knowledge Retrieval and Private Inference for secure multi-agent systems

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, memory, language model, large language, retrieval
- 作者：Vicenç Torra, Maria Bras-Amorós
- 链接：[arXiv](https://arxiv.org/abs/2611.13696) · [PDF](https://arxiv.org/pdf/2611.13696) · [HF](https://huggingface.co/papers/2611.13696)

Multi-agent systems provide a convenient framework for the massive deployment of agents based on Large Language Models (LLMs). It provides a sound framework where agents can interact with existing software to perform actions in an autonomous way. Agentic AI is the new term to denote these AI-based autonomous systems. In real multi-agent systems, agents need to deal with malicious agents some of which can exploit…

## 60. Broad-Persistent Advising in Interactive Reinforcement Learning via Latent State Encoding

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, reinforcement learning, coding, spec
- 作者：Zhuoran Liang, Francisco Cruz
- 链接：[arXiv](https://arxiv.org/abs/2611.13712) · [PDF](https://arxiv.org/pdf/2611.13712) · [HF](https://huggingface.co/papers/2611.13712)

Deep Interactive Reinforcement Learning (Deep IntRL) accelerates reinforcement learning training by incorporating external advice. However, conventional Deep IntRL uses each piece of advice only in the current step and discards it after a single interaction. Persistent Advising and Broad-Persistent Advising (BPA) extend this process by storing advice in persistent memory and reusing it in similar states through…

## 61. Toward Autonomous RTL and Synthesis Optimization: Benchmarking and Self-Improving Agents

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, evaluation, benchmark, language model, large language, spec
- 作者：Wenji Fang, Yao Lu, Jinghua Wang, Zhiyao Xie
- 链接：[arXiv](https://arxiv.org/abs/2611.13713) · [PDF](https://arxiv.org/pdf/2611.13713) · [HF](https://huggingface.co/papers/2611.13713)

Recent advances in large language models (LLMs) and autonomous agents are creating new opportunities for hardware design optimization. This paper examines three connected directions toward autonomous RTL and synthesis optimization: (1) Realistic benchmarking. We discuss reference-based and open-ended RTL optimization benchmarks that evaluate optimization opportunities under realistic EDA workflows. (2) Tool-grounded…

## 62. DisasterAgent: An Evidence-Driven Agent for Verifiable Disaster Report Generation From Remote Sensing Imagery

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, memory, reasoning, benchmark, language model, spec
- 作者：Zhijian Li, Jiawei Song, Chao Ren, Yidan Zhang, Peijin Wang, Xian Sun, Kun Fu
- 链接：[arXiv](https://arxiv.org/abs/2611.13776) · [PDF](https://arxiv.org/pdf/2611.13776) · [HF](https://huggingface.co/papers/2611.13776)

Remote sensing disaster assessment is moving from simple damage classification toward comprehensive report-level analysis. In this setting, responders need not only damage descriptions but also verifiable evidence to guide response and recovery. Recent vision-language models (VLMs) and tool-augmented agents offer strong multimodal reasoning and perception, but they struggle to provide the evidence required for…

## 63. Taxonomy-Agnostic Neurosymbolic Grounding of Robot Kinematics

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：context window, reasoning, evaluation, language model, large language
- 作者：Bastien Dussard, Aur{é}lie Clodic, Guillaume Sarthou
- 链接：[arXiv](https://arxiv.org/abs/2611.13850) · [PDF](https://arxiv.org/pdf/2611.13850) · [HF](https://huggingface.co/papers/2611.13850)

While symbolic reasoning for task allocation requires grounding a robot's physical capabilities, standard Unified Robot Description Format (URDF) files provide only low-level kinematics without the formal semantic context needed for reasoning. We present URDF2Ontology, an automated, taxonomy-agnostic neurosymbolic framework that transforms raw URDF files into populated, grounded OWL ontologies. It leverages a Large…

## 64. Beyond Passive Imitation: On-Policy Mid-Training Distillation for Language Models

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, language model, large language, spec
- 作者：Ruize Zheng, Xuyang Liu, Siyu Ren, Xiaobing Tu, Yinggui Wang, Jinkui Ren, Xiantao Zhang, Linfeng Zhang
- 链接：[arXiv](https://arxiv.org/abs/2611.13855) · [PDF](https://arxiv.org/pdf/2611.13855) · [HF](https://huggingface.co/papers/2611.13855)

Continual pre-training (CPT) adapts large language models (LLMs) to specialized domains, yet its standard next-token prediction (NTP) objective treats every corpus token as a fixed target, regardless of its utility to the current model. In a controlled study on the same 1B-token mathematical corpus, we observe sharply different outcomes across base models: NTP improves Llama-3.2-3B's performance on mathematical…

## 65. DroneSegEdit: Adapting Pretrained Generative Editors for UAV Segmentation with Language-Grounded Verification

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：language model, large language, coding, spec
- 作者：Dehua Chen, Long Xin, Jiangtao Wei
- 链接：[arXiv](https://arxiv.org/abs/2611.13890) · [PDF](https://arxiv.org/pdf/2611.13890) · [HF](https://huggingface.co/papers/2611.13890)

Recent work has shown that pretrained image generators can support diverse visual tasks. Yet directly applying them to language-guided unmanned aerial vehicle (UAV) segmentation exposes a key limitation: a plausible mask may correspond to the wrong instance among small and repeated objects. We call this mismatch between mask rendering and expression-level target selection the Grounding-Rendering Gap. We present…

## 66. Beyond Fluent Responses: Finding User Dissatisfaction in Human-AI Interactions

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, language model, large language, spec
- 作者：Yuka Saito, Ikumi Numaya, Jun Suzuki, Reina Akama
- 链接：[arXiv](https://arxiv.org/abs/2611.13894) · [PDF](https://arxiv.org/pdf/2611.13894) · [HF](https://huggingface.co/papers/2611.13894)

As large language models generate increasingly high-quality responses, recent work on response evaluation has moved beyond response-centered criteria, such as correctness and coherence, toward user-centered criteria, including user preferences and perceived usefulness. This shift is fundamentally important for developing technologies that are truly useful to real-world users. While conventional response evaluation…

## 67. Persistent Metric-Semantic Maritime Scene Memory from Open-Vocabulary 3D Scene Graphs

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, reasoning, language model, retrieval
- 作者：Kim Alexander Christensen, Dina Zimmermann, Martin Steinert, Eleni Kelasidi
- 链接：[arXiv](https://arxiv.org/abs/2611.13903) · [PDF](https://arxiv.org/pdf/2611.13903) · [HF](https://huggingface.co/papers/2611.13903)

Three-dimensional scene graphs (3DSGs) can provide robots with persistent metric-semantic representations for spatial reasoning, but the existing methods have primarily been developed for indoor and terrestrial environments. In this paper we investigate how a representative outdoor open-vocabulary method transfers to maritime environments and which adaptations are needed. Our experiments show that zero-shot…

## 68. TAPCO-G: LLM-Guided Design-Adaptive Timing and Power Co-Optimization with Graph-Based Physical Priors

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, language model, large language, spec
- 作者：Wuqian Tang, Zixiao Wang, Che-Chien Lin, Fong-Hua Fu, Laura Angélica Shion-Korsak, Xinyun Zhang, Bei Yu, Chun-Yao Wang
- 链接：[arXiv](https://arxiv.org/abs/2611.13931) · [PDF](https://arxiv.org/pdf/2611.13931) · [HF](https://huggingface.co/papers/2611.13931)

Post-placement timing and power co-optimization is critical to meeting setup timing targets and reducing power within placement constraints. A cell replacement can improve timing along one path while increasing power or reducing slack on others. Conventional optimizers follow fixed rules for scheduling and accepting repairs, limiting their ability to address design-specific bottlenecks. A large language model (LLM)…

## 69. TreeAgent: Structure-Aware Memory Agent for Processing Long Hierarchical Data

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, memory, context window, reasoning, language model, large language, spec, retrieval
- 作者：Wei Gu, Weiwei Qi, Jiajun Tang, Tianhang Zheng, Bo Chen, Zhibo Zhang, Jinfei Liu, Kui Ren
- 链接：[arXiv](https://arxiv.org/abs/2611.13946) · [PDF](https://arxiv.org/pdf/2611.13946) · [HF](https://huggingface.co/papers/2611.13946)

Practical Web applications increasingly require agents to interpret long conversations or documents. For inputs exceeding the context windows of large language models (LLMs), memory agents process segments sequentially and retain past information in bounded memory. However, they typically divide inputs into flat token segments without preserving structure or hierarchy, causing three limitations for structured data…

## 70. Controlled Knowledge Engineering for Taxonomy Induction with Tool-Grounded LLM Agents and Runtime-Adaptive Policies

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, memory, benchmark, language model, large language, retrieval
- 作者：Jonas Limniatis, Bennet Schaarmann, Georg Reuber, Robert Stahlbock
- 链接：[arXiv](https://arxiv.org/abs/2611.13966) · [PDF](https://arxiv.org/pdf/2611.13966) · [HF](https://huggingface.co/papers/2611.13966)

Taxonomies are structured knowledge representations that support semantic search, recommendation, product catalog organization, and retrieval-augmented generation. Their automated construction from a fixed set of candidate entities requires more than plausible text generation: the resulting hierarchy must be complete, structurally valid, and semantically coherent. Large Language Models (LLMs) are promising for this…

## 71. BioXArena-Pro: a research-grade benchmark for autonomous biomedical machine learning agents

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, benchmark, coding, spec
- 作者：Loka Li, Duzhen Zhang, Xingbo Du, Leonard Song, Kun Zhang, Le Song
- 链接：[arXiv](https://arxiv.org/abs/2611.13994) · [PDF](https://arxiv.org/pdf/2611.13994) · [HF](https://huggingface.co/papers/2611.13994)

Coding agents are increasingly proposed as autonomous builders of biomedical models, but existing benchmarks are small, near saturation or open to leaked information. We present BioXArena-Pro, 64 research-level modelling tasks from eight biomedical domains, each rebuilt from a published study; most hold out whole biological units such as species or cohorts. Across 22 agent configurations, the best scores 55.1 of…

## 72. Coding Agent Memory Post-Training II: Unlocking the Memory Potential of Pre-trained File Operations for Long-Horizon Tasks via On-Policy Distillation

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, memory, benchmark, coding
- 作者：Lirui Luo, Kelong Mao, Xinwei Yang, Rongqing Li, Luyu Chen, Kieran Wong, Yudong Guo, Xinrui Wang, Jiayin Zhu, Gu Simiu, Sulong Xu, Cong Fang
- 链接：[arXiv](https://arxiv.org/abs/2611.14009) · [PDF](https://arxiv.org/pdf/2611.14009) · [HF](https://huggingface.co/papers/2611.14009)

Language-model agents increasingly tackle long-horizon tasks whose interaction histories exceed the model's active context. They must therefore decide what to write down and what to read back, and when to do either. Recent work has begun to use on-policy distillation (OPD) to make memory control part of the policy, relying on memory tools and compaction protocols that lie outside either model's pre-training.…

## 73. One Sequence Is Enough: Fingerprinting Language Models from Fixed-Length Integer Sequences

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, language model, spec
- 作者：Fantong Meng, Chengjie Sun, Shuangjia Yang, Zhiyuan Zhao, Yansheng Pei, Xinyang Li
- 链接：[arXiv](https://arxiv.org/abs/2611.14010) · [PDF](https://arxiv.org/pdf/2611.14010) · [HF](https://huggingface.co/papers/2611.14010)

Users of model APIs and third-party platforms often rely on the declared model name to identify the model responding to their requests. However, the actual model may differ from the declared one, motivating identity verification based on observable outputs. Previous studies have shown that preferences in simple numerical-choice tasks can serve as model fingerprints. We investigate whether a single fixed-length…

## 74. Margin-Guided Token Credit for Reinforcement Learning with Verifiable Rewards

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reinforcement learning, evaluation, benchmark, language model
- 作者：Chi Liu, Xin Chen, Yuchuan Weng, Srinivasan Manoharan
- 链接：[arXiv](https://arxiv.org/abs/2611.14015) · [PDF](https://arxiv.org/pdf/2611.14015) · [HF](https://huggingface.co/papers/2611.14015)

In reinforcement learning with verifiable rewards, a language model is rewarded for a correct final answer, and GRPO passes that reward to every token of the solution in equal measure. We instead place the credit where the model hesitated, in a method we call MCPO (Margin-Credit Policy Optimization). We measure hesitation by the top-2 margin $M=p_1-p_2$ of the policy's next-token distribution, map it to a score with…

## 75. Personalized Memory Rubrics: Learning What to Remember per User via Rubric-Guided Credit Assignment

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, memory, evaluation, benchmark, spec
- 作者：Yupeng Han, Kai Zhang, Shuochen Liu, Ze Liu, Xianquan Wang, Zhihong Pan, Xiangyu Zhao, Qi Liu, Enhong Chen
- 链接：[arXiv](https://arxiv.org/abs/2611.14017) · [PDF](https://arxiv.org/pdf/2611.14017) · [HF](https://huggingface.co/papers/2611.14017)

Long-horizon personalized agents maintain an evolving memory by continuously deciding what to add, modify, or discard. However, learning an optimal update policy remains challenging. Conventional training relies solely on terminal question-answering accuracy, yielding a coarse feedback signal that treats all intermediate updates identically. Furthermore, update utility is inherently user-specific, as identical…

## 76. ZoomGain: Mining Global-to-Zoom Perception Gaps for Fine-Grained Visual Supervision

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, language model, spec
- 作者：Haozhan Shen, Liangbo He, Jun Lan, Huijia Zhu, Weiqiang Wang, Tiancheng Zhao, Jianwei Yin
- 链接：[arXiv](https://arxiv.org/abs/2611.14076) · [PDF](https://arxiv.org/pdf/2611.14076) · [HF](https://huggingface.co/papers/2611.14076)

Fine-grained visual perception requires Vision-Language Models (VLMs) to locate and interpret subtle evidence within complex scenes. Constructing supervision for this ability is challenging: questions must have correct, unambiguous answers that depend on actual fine-grained visual details rather than coarse cues or language priors. Verifying these properties makes manual annotation labor-intensive and automatic…

## 77. ProofCoder: Continuous Reasoning for Automated Software Verification

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reasoning, benchmark, language model, large language, coding, spec, retrieval
- 作者：Martim Afonso, Inês Lynce, Maurizio Morisio, João F. Ferreira
- 链接：[arXiv](https://arxiv.org/abs/2611.14106) · [PDF](https://arxiv.org/pdf/2611.14106) · [HF](https://huggingface.co/papers/2611.14106)

Formal verification using proof assistants provides strong correctness guarantees for software, but constructing proofs remains labor-intensive and requires significant expertise. Recent approaches based on large language models (LLMs) have shown promise in automating proof synthesis. However, these approaches typically constrain the model to a rigid tactic-generation loop, in which the surrounding system controls…

## 78. Looking One Step Ahead: An Anticipation-guided Agent for Object State Readout in Videos

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, evaluation, language model, large language, spec
- 作者：Yuanhe Tian, Yan Song
- 链接：[arXiv](https://arxiv.org/abs/2611.14113) · [PDF](https://arxiv.org/pdf/2611.14113) · [HF](https://huggingface.co/papers/2611.14113)

Understanding the progress of an activity requires tracking how the objects involved change over time. Object state readout provides this information by describing a target object's states and transitions across video frames. Although multimodal large language models (MLLMs) generate detailed visual descriptions, these descriptions may leave the attributes needed to distinguish successive states insufficiently…

## 79. Hx2Dx: From Anamnesis to Diagnosis - A Multimodal Arena for Conversational Clinical Reasoning in LLMs

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, evaluation, benchmark, language model, large language
- 作者：Federico Ravenda, Mirko Cesarini, Daniele Montagnani, Volodymyr Karpenko, Antonietta Mira, Andrea Raballo
- 链接：[arXiv](https://arxiv.org/abs/2611.14122) · [PDF](https://arxiv.org/pdf/2611.14122) · [HF](https://huggingface.co/papers/2611.14122)

Large language models (LLMs) achieve expert-level diagnostic accuracy in static evaluations, where the model receives a curated vignette or case report that already condenses the diagnostically relevant findings. Such evaluations measure inference over already selected evidence; the evaluations do not account for the inquiry used to obtain it. In clinical practice, however, diagnosis is an iterative process of…

## 80. Breakdown of Autoregressive Multi-Step Reasoning Under Concentrated vs. Diffuse Attention Head Dropout

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, benchmark, language model, large language
- 作者：Karol Struniawski
- 链接：[arXiv](https://arxiv.org/abs/2611.14209) · [PDF](https://arxiv.org/pdf/2611.14209) · [HF](https://huggingface.co/papers/2611.14209)

During extended wakefulness, mammalian neocortical networks experience localized periods of transient neuronal silence termed off-states. Here, we examine how analogous spatiotemporally concentrated disruptions affect sequential reasoning in autoregressive Large Language Models (LLMs). Evaluating 250 paired derivations on the GSM8K benchmark across two 8B models (Qwen3-8B and LLaMA-3.1-8B-Instruct), we contrast…

## 81. Chain of Physics: Supporting Fault Diagnosis with Engineering-Inspired Large Language Model Reasoning

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, benchmark, language model, large language, spec, retrieval
- 作者：Wenqi Zhou, Leonardo Baldo, Kai Goebel, Manuel Arias Chao
- 链接：[arXiv](https://arxiv.org/abs/2611.14263) · [PDF](https://arxiv.org/pdf/2611.14263) · [HF](https://huggingface.co/papers/2611.14263)

Fault diagnosis in complex systems requires linking observed changes in physical quantities to the failure mechanisms that produce them. Experienced engineers perform this task by combining sensor information with knowledge of system behavior and fault propagation. Large Language Models (LLMs) can support this process, but their diagnostic reasoning depends on the availability of asset-specific engineering knowledge…

## 82. LM-SimBench: A Unified Framework, Dataset, and Benchmark for Large Language Model Training Simulation

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, language model, large language
- 作者：Yu Dong, Hong Li, Qiang Sun, Xu Zhou, Jinbiao Huo, Qixiu Cheng, Zhiyuan Liu
- 链接：[arXiv](https://arxiv.org/abs/2611.14285) · [PDF](https://arxiv.org/pdf/2611.14285) · [HF](https://huggingface.co/papers/2611.14285)

Evaluating candidate parallelization strategies through distributed training runs makes strategy selection prohibitively expensive at scale. Performance simulation offers a lower cost alternative, yet controlled comparisons among existing simulators remain difficult because they differ in the training stages they model and the workloads on which they are evaluated. We introduce LM-SimBench, a unified framework,…

## 83. Don't Just Trust Your Memory: Evidence-Linked Memory Reduces Memory-Induced Degradation in LLM Agents

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, memory, benchmark, spec
- 作者：Yukyeong Lee, Yumin Choi, Jinheon Baek, Sung Ju Hwang
- 链接：[arXiv](https://arxiv.org/abs/2611.14320) · [PDF](https://arxiv.org/pdf/2611.14320) · [HF](https://huggingface.co/papers/2611.14320)

External memory enables LLM agents to improve from experience by distilling trajectories of past tasks into concise lessons for new tasks. However, memory can also lead to memory-induced degradation, where an agent fails on tasks it would solve without memory, often because it follows a lesson that is incorrect, or misapplies or misreads a valid one. This is because lessons are inferred from trajectories labeled…

## 84. When Should Agents Remember? Falsification-Gated Self-Evolution for LLM Agents

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, tool-use, memory, benchmark
- 作者：Runxuan Tang, Haoyu Gao, Yuyan Ding, Junyi Yao, Zihao Zheng, Zecheng Sheng, Liwei Hou
- 链接：[arXiv](https://arxiv.org/abs/2611.14326) · [PDF](https://arxiv.org/pdf/2611.14326) · [HF](https://huggingface.co/papers/2611.14326)

LLM agents increasingly operate in long-horizon, verifier-rich environments, but current self-improvement mechanisms often write episode-derived lessons directly into memory, making local success an unreliable signal for reusable and safe knowledge. This paper addresses the core question of when an experience-derived behavioral update should be admitted into persistent agent state. We propose Falsification-Gated…

## 85. Cognitive Mapping of Learning by Thinking Mechanisms in Large Language Models

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, reasoning, language model, large language, spec
- 作者：Dong Han, Jin Zhang, Kunyue Yang
- 链接：[arXiv](https://arxiv.org/abs/2611.14382) · [PDF](https://arxiv.org/pdf/2611.14382) · [HF](https://huggingface.co/papers/2611.14382)

Large language models (LLMs) increasingly exhibit capabilities that resemble human Learning by Thinking (LbT), the acquisition of new insight through internal processes such as explanation and reasoning, without new external input. A systematic account of the cognitive mechanisms behind these capabilities, and of their limits, remains underdeveloped. This paper proposes a Cognitive LbT Framework that maps four…

## 86. Evaluating LLM-Generated World Models for Neuro-Symbolic Reasoning

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reasoning, benchmark, planning
- 作者：Souhaila Djaffal, Amna Jamal, Gagana Madhugiri Devaraja, Anidipta Pal, Jobst Heitzig
- 链接：[arXiv](https://arxiv.org/abs/2611.14419) · [PDF](https://arxiv.org/pdf/2611.14419) · [HF](https://huggingface.co/papers/2611.14419)

Formal world models can support planning, verification, and safety reasoning, but constructing them from open-ended natural-language situations is difficult, particularly in multi-agent settings where several formalizations may be plausible. We study whether five LLMs can generate such world models as partially observable stochastic games and whether mechanical validity is sufficient to establish that the resulting…

## 87. ReTrace: Distilling Tool-Using Agents into Planner-Free Workflows

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reasoning, language model, large language
- 作者：Kaiyuan Hou, Yang Ping Kuo, Indranil Bhattacharya, Rohith Nama, Arushi Gupta, Carlos D. Castillo, Prathap Ramachandra, Xiaofan Jiang, Francesco Carbone
- 链接：[arXiv](https://arxiv.org/abs/2611.14492) · [PDF](https://arxiv.org/pdf/2611.14492) · [HF](https://huggingface.co/papers/2611.14492)

Business process automation runs the same Standard Operating Procedure (SOP) again and again on new inputs. Large Language Model (LLM) agents can follow an SOP written in natural language, but they call an LLM to choose every step of every run, which adds latency and cost at scale. We present ReTrace, which turns an SOP and a few logged agent runs into a reusable workflow in which code, not an LLM, selects the next…

## 88. AutoScaffold: AI-Guided Scaffolding for Reinforcement Learning of Language Models

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, reinforcement learning, evaluation, language model, spec
- 作者：Zijian Zhang, Rizhen Hu, Jiangweizhi Peng, Shiyang Li, Sujay Bhatt, Sihan Zeng, Mingyi Hong
- 链接：[arXiv](https://arxiv.org/abs/2611.14515) · [PDF](https://arxiv.org/pdf/2611.14515) · [HF](https://huggingface.co/papers/2611.14515)

Reinforcement learning with verifiable rewards (RLVR) produces rich training experience, yet outcome rewards reduce each attempt to a single number and leave most of this information unused. Training-time scaffolds, such as strategies or hints added to the prompt during training, offer a natural way to turn this information into guidance, but their design and adaptation are largely left to humans and tailored to…

## 89. Horizon-Scalable Q-Learning

- 分数：8.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：-
- 作者：Haoran Xu, Pragya Srivastava, Xinjie Liu, Siddhant Agarwal, Amy Zhang
- 链接：[arXiv](https://arxiv.org/abs/2611.10987) · [PDF](https://arxiv.org/pdf/2611.10987) · [HF](https://huggingface.co/papers/2611.10987)

Learning accurate off-policy state-action value functions (Q-functions) from offline datasets becomes harder as the task horizon grows. One-step temporal-difference (TD) learning bootstraps after every transition, so small per-step errors accumulate along the horizon, and early states can be badly misvalued even when the TD loss is small. Multi-step TD shortens this chain by following the dataset trajectory for…

## 90. Benchmarking LLM Next-Step Recommendations with Knowledge Space Theory

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, spec
- 作者：Peter Steiner, Jan Hochweber
- 链接：[arXiv](https://arxiv.org/abs/2611.13667) · [PDF](https://arxiv.org/pdf/2611.13667) · [HF](https://huggingface.co/papers/2611.13667)

Selecting an LLM for next-step recommendation requires benchmarks that reflect the intended educational task and domain. We present a benchmarking method that uses Knowledge Space Theory (KST) as a formal evaluation reference. Given a task catalogue and an existing prerequisite relation, the method derives admissible knowledge states and the complete set of immediate next steps for each state. Recommendations…

## 91. Walrus Technical Report

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, language model, spec
- 作者：Alkis Koudounas, Osamu Take, Hayato Futami, Quentin Jodelet, Emiru Tsunoo
- 链接：[arXiv](https://arxiv.org/abs/2611.13689) · [PDF](https://arxiv.org/pdf/2611.13689) · [HF](https://huggingface.co/papers/2611.13689)

We present Walrus, a unified 8B speech-and-audio foundation model handling speech recognition (including code-switching and multi-talker speech), speech-to-text and speech-to-speech translation, text-to-speech, emotion recognition, audio captioning, and general audio understanding. Our main contribution is not a new architecture but a data-centric training recipe; we use a standard decoder-only backbone initialized…

## 92. Agentic AI Meets Formal Verification in the Era of Agentic Hardware Development

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reasoning, spec
- 作者：Wenji Fang, Yuchao Wu, Jing Wang, Zhiyao Xie
- 链接：[arXiv](https://arxiv.org/abs/2611.13705) · [PDF](https://arxiv.org/pdf/2611.13705) · [HF](https://huggingface.co/papers/2611.13705)

As AI agents become increasingly capable of generating and optimizing hardware circuits, ensuring the correctness of AI-generated designs becomes more important. Meanwhile, advances in AI lower the barriers to developing and applying formal methods, creating new opportunities to automate and improve hardware verification. This invited paper presents an overview of the methodologies and applications of hardware…

## 93. AutoManifold: Agentic Design of Data Visualisation Algorithms via Manifold Embedding

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, evaluation, spec
- 作者：Burak Susam, Ruiyuan Kang, Tingting Mu
- 链接：[arXiv](https://arxiv.org/abs/2611.13710) · [PDF](https://arxiv.org/pdf/2611.13710) · [HF](https://huggingface.co/papers/2611.13710)

Manifold embedding for data visualisation is dominated by a small set of hand-designed state-of-the-art (SOTA) algorithms. Their design targets are fixed at development time, resulting in inflexible algorithmic behaviour that cannot be readily steered towards user-specified structural priorities. Hand-designing new embedding algorithms to address user priority requires highly specialised expertise and is time…

## 94. Mixed Signals: Weight-Space Programming for EEG and ECG

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, language model, spec
- 作者：Dara Varam, Taraneh Aminosharieh Najafi, David Atienza
- 链接：[arXiv](https://arxiv.org/abs/2611.13758) · [PDF](https://arxiv.org/pdf/2611.13758) · [HF](https://huggingface.co/papers/2611.13758)

Weight-space programming allows language models to read a trained neural network's weights and edit them. This opens the door to ``training'' by reasoning rather than through gradient descent. Prior work has demonstrated its functionality and promise for game-playing networks and fixing specific failures in language models, even extending to diffusion models. In this work, we present its applicability to models…

## 95. CASCADE: Constraint-Aware SCAffolded DEcomposition for Logical Anomaly Detection

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, language model, spec
- 作者：Jinchan Kim, Jinhee Im, Hyunsouk Cho
- 链接：[arXiv](https://arxiv.org/abs/2611.13820) · [PDF](https://arxiv.org/pdf/2611.13820) · [HF](https://huggingface.co/papers/2611.13820)

Logical Anomaly Detection (LAD) requires verifying whether all category-specific constraints, such as object counts, pairing relations, and measurement ranges, are satisfied by a query image given only a few normal references. Recent LAD methods based on Large Vision-Language Models (LVLMs) formulate this as checklist verification, decomposing the decision into independent textual checks. This decomposition,…

## 96. Ceci n'est pas une pipe -- Toward a Symbolic Solver for the Abstraction and Reasoning Corpus Using Evolutionary Computation

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, benchmark, spec
- 作者：Luca Favole, Giorgio Mongardi, Giovanni Squillero, Alberto Tonda
- 链接：[arXiv](https://arxiv.org/abs/2611.13831) · [PDF](https://arxiv.org/pdf/2611.13831) · [HF](https://huggingface.co/papers/2611.13831)

The Abstraction and Reasoning Corpus (ARC) is a benchmark designed to assess the capability of Artificial Intelligence (AI) systems to generalize starting from a few samples, a task humans excel at. The ARC-AGI contests held since 2020 have been the focus of intense competition, with participants proposing approaches ranging from traditional symbolic AI to Transformer architectures. Despite a long history of…

## 97. Towards Text-Only Remote Sensing Scene Classification via Semantic Proxy

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, language model, spec
- 作者：Xianping Ma, Kunlin Wu, Xiaofeng Liu, Xiaokang Zhang, Yuanxin Ye
- 链接：[arXiv](https://arxiv.org/abs/2611.13851) · [PDF](https://arxiv.org/pdf/2611.13851) · [HF](https://huggingface.co/papers/2611.13851)

Remote sensing scene classification (RSSC) is traditionally formulated as a vision-centric problem, where inference relies on rich visual representations extracted from images. In this work, we revisit this assumption by introducing text-only RSSC, a new problem setting that investigates whether remote sensing scenes can be recognized using only textual semantic representations. To enable this study, we propose…

## 98. Spatial-Spectral Coupling as Attention: Scaling Shape Correspondence to High-Resolution Surfaces

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, benchmark, spec
- 作者：Bence Demeter, Kilian Ehrenreich, Amelie Kleber, Ioana Oprisiu, Philipp Spohn, Christian Wachinger, Fabian Bongratz, Lennart Bastian
- 链接：[arXiv](https://arxiv.org/abs/2611.13870) · [PDF](https://arxiv.org/pdf/2611.13870) · [HF](https://huggingface.co/papers/2611.13870)

Establishing dense correspondence between high-resolution 3D shapes remains challenging due to the spatial--spectral coupling at the core of many functional-map methods, which grows quadratically with mesh resolution. We observe that this coupling is equivalent to a scaled dot-product attention formulation, with learned descriptors serving as queries and keys and spectral basis functions as values. This connection…

## 99. A 10K drone image dataset with component-level annotations for rooftop photovoltaic inspection

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, spec
- 作者：Penglei Zhang, Wan Zhang, Ruizhe Deng, Bo Chen, Wenhao Duan, Jinhe Zhang, Yanzhen Zhang, Qi Chen, Zhiling Guo, Haoran Zhang, Yuntian Chen
- 链接：[arXiv](https://arxiv.org/abs/2611.13892) · [PDF](https://arxiv.org/pdf/2611.13892) · [HF](https://huggingface.co/papers/2611.13892)

Component-level information supports rooftop photovoltaic (PV) inspection, but recognizing individual components across complex scenes remains challenging. We present PVIS-10K, a dataset of 10,065 drone images with component-level annotations covering 63,632 physical PV modules across 22 rooftop installations. The high-resolution red-green-blue (RGB) images were acquired by unmanned aerial vehicles (UAVs, also known…

## 100. From Counterfactual Edits to Human Narratives: LLM-Driven Interpretations for Recommender System Explanations

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, language model, large language
- 作者：Vojtech Cahlik, Amir Reza Mohammadi, Rodrigo Alves, Pavel Kordik, Eva Zangerle
- 链接：[arXiv](https://arxiv.org/abs/2611.13914) · [PDF](https://arxiv.org/pdf/2611.13914) · [HF](https://huggingface.co/papers/2611.13914)

Recommender systems increasingly influence what users discover and consume online, yet the decision logic behind their outputs often remains opaque. Counterfactual explanation (CFX) methods provide an effective way to show which changes to a user's interaction history would alter a recommendation. In recommendation settings, however, CFXs often require many edits, producing long, low-level lists that are hard for…

## 101. Beyond Proxy Metrics: MLLMs as Human Surrogates for Explainable AI Evaluation

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, language model, large language
- 作者：Eoin M. Kenny, Salim I. Amoukou, Tom Bewley
- 链接：[arXiv](https://arxiv.org/abs/2611.13926) · [PDF](https://arxiv.org/pdf/2611.13926) · [HF](https://huggingface.co/papers/2611.13926)

Explainable AI (XAI) has expanded into a broad and impactful research area, but the fundamental question of how best to evaluate explanation techniques has proven frustratingly elusive. Methodologies typically revolve around either proxy metrics which tell us little about the utility of an explanation, or human evaluation which---while generally considered the gold standard---is expensive, difficult to scale, and…

## 102. From Attack Surface to Defense Architecture: Compositional Security for Agentic Coding Harnesses

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, language model, coding
- 作者：Simon Hegelich, Bardh Prenkaj, Habiba Sarhan, Morteza Shahrezaye, Kolja Hegelich, Christian Montag, Ralf Schneider, Erik Cambria
- 链接：[arXiv](https://arxiv.org/abs/2611.13960) · [PDF](https://arxiv.org/pdf/2611.13960) · [HF](https://huggingface.co/papers/2611.13960)

AI coding harnesses couple language models to shells, filesystems, and network sockets, turning the harness into an automated Living-off-the-Land (LotL) platform: once an adversary injects instructions into retrieved content, dual-use binaries such as bash, curl, and find become the payload. We argue that security in agentic systems is a structural property of the cognitive architecture and permission composition…

## 103. Understanding Mixture-of-Experts Language Models Beyond Expert Boundaries

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, language model, spec
- 作者：Zhenhong Zhou, Mao Zheng, Mingyang Song, Qiankun Li, Kun Wang, Junfeng Fang
- 链接：[arXiv](https://arxiv.org/abs/2611.13975) · [PDF](https://arxiv.org/pdf/2611.13975) · [HF](https://huggingface.co/papers/2611.13975)

In Mixture-of-Experts (MoE) models, the nature of expert specialization remains controversial. Reports of domain-associated expert preferences contrast with analyses attributing routing primarily to token identity or syntactic patterns. To clarify these differing accounts, we look beyond expert-level routing to investigate the neuron-level organization of domain-specialized computation using Routing-Aware Magnitude…

## 104. Specify Privacy Yourself: Assessing Inference-Time Personalized Privacy Preservation Ability of Large Vision-Language Models

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, language model, spec
- 作者：Xingqi Wang, Xiaoyuan Yi, Xing Xie, Jia Jia
- 链接：[arXiv](https://arxiv.org/abs/2611.13997) · [PDF](https://arxiv.org/pdf/2611.13997) · [HF](https://huggingface.co/papers/2611.13997)

Large Vision-Language Models (LVLMs) have demonstrated remarkable capabilities but raise significant privacy concerns due to their abilities to infer sensitive personal information from images with high precision. While current LVLMs are relatively well aligned to protect universal privacy, e.g., credit card data, we argue that privacy is inherently personalized and context-dependent. This work pivots towards a…

## 105. LUMIR: Decoupled Multimodal Representation Learning from Heterogeneous Data for Next-POI Recommendation

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：language model, large language, spec
- 作者：Zehui Wang, Wolfram Höpken, Dietmar Jannach
- 链接：[arXiv](https://arxiv.org/abs/2611.14004) · [PDF](https://arxiv.org/pdf/2611.14004) · [HF](https://huggingface.co/papers/2611.14004)

As multimodal tourism-related information collected from heterogeneous data sources has become increasingly available, learning effective representations has attracted attention for improving recommendation performance. Existing approaches often tightly couple multimodal fusion with the architecture and optimization objective of a specific downstream model, which limits the generality and reusability of the learned…

## 106. Interleaving anatomical inspection and diagnostic reasoning for explainable radiology report generation

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, evaluation, spec
- 作者：Chentao Huang, Runlong Lin, Zhijun Wang, Yunxiang Li, Yuanyuan Sun, Jian Wang, Hongfei Lin, Ling Luo
- 链接：[arXiv](https://arxiv.org/abs/2611.14018) · [PDF](https://arxiv.org/pdf/2611.14018) · [HF](https://huggingface.co/papers/2611.14018)

Automated radiology report generation can draft clinically plausible reports, yet the pathway from visual evidence to reported findings remains opaque, leaving the diagnostic basis of these reports unexplained and the generated reports difficult to review or revise. We introduce ARIVE (Anatomy-guided Reasoning with Interleaved Visual Evidence), an explainable report generation framework that interleaves anatomical…

## 107. Program-Aided Patchable Skill Evolution

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, benchmark, coding
- 作者：Jiahao Wang, Yuqi Xiong, Qing Yang, Zhipeng Xu, Zhenghao Liu, Zulong Chen, Yubin Bao
- 链接：[arXiv](https://arxiv.org/abs/2611.14019) · [PDF](https://arxiv.org/pdf/2611.14019) · [HF](https://huggingface.co/papers/2611.14019)

Agent skills have emerged as an effective means of enabling LLM agents to solve complex, interactive tasks by encoding reusable knowledge without modifying model parameters. Recent approaches further improve skill adaptation by distilling reusable experience from agent execution trajectories and evolving skills based on downstream task feedback. However, existing methods primarily represent skills as natural…

## 108. ScaleBrain: A Scale-Consistent Framework for EEG Foundation Models

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, spec
- 作者：Minyu Zhou, Yajing Wu, Yongqiang Tang, Wang Jia, Wensheng Zhang
- 链接：[arXiv](https://arxiv.org/abs/2611.14035) · [PDF](https://arxiv.org/pdf/2611.14035) · [HF](https://huggingface.co/papers/2611.14035)

Foundation models pre-trained on large unlabeled electroencephalography (EEG) corpora have emerged as a transformative paradigm for Brain-Computer Interface (BCI) applications. Recent EEG foundation models have shown that multi-scale representations derived from fixed-length patches can improve EEG representation learning. Existing frameworks commonly construct temporal scales through feature-level operations.…

## 109. MISO-BR: An Open Corpus for Misogyny Detection in Brazilian Portuguese

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：language model, large language, coding
- 作者：Fábio A. S. Passos, Péricles B. C. Miranda, Ana Paula Cavalcanti
- 链接：[arXiv](https://arxiv.org/abs/2611.14036) · [PDF](https://arxiv.org/pdf/2611.14036) · [HF](https://huggingface.co/papers/2611.14036)

Misogyny is among the most prevalent forms of online hate speech directed at Brazilian users, yet open and auditable resources dedicated to it in Brazilian Portuguese remain scarce. We introduce MISO-BR, an open, documented and versioned corpus of 896 balanced social media texts annotated for binary misogyny, released with its construction protocol and reproducible baselines. The corpus combines lexicon- and…

## 110. Can KV Cache Be Reused Across Model Updates? A DeepSeek-V4-Flash Case Study

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, language model, retrieval
- 作者：Zhikun Tao, Fangyong Jin, Junping Zhao
- 链接：[arXiv](https://arxiv.org/abs/2611.14051) · [PDF](https://arxiv.org/pdf/2611.14051) · [HF](https://huggingface.co/papers/2611.14051)

Reusing key--value (KV) caches across language model updates could avoid repeated computation of shared context, but changes in model weights raise a fundamental question about what these caches preserve. We investigate direct cache reuse across four model updates, with a detailed study of DeepSeek-V4-Flash to Flash-0731. Our central finding is that caches can retain useful task information without faithfully…

## 111. HandsOnAid: Building and Evaluating an Offline First-Aid Assistant for Emergency Response Scenarios

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, language model, retrieval
- 作者：Rezwan Islam Salvi, Saiyma Sittul Muna, Mushfiqur Rahman Mushfique
- 链接：[arXiv](https://arxiv.org/abs/2611.14059) · [PDF](https://arxiv.org/pdf/2611.14059) · [HF](https://huggingface.co/papers/2611.14059)

Emergencies can occur where there is no phone signal and no ambulance nearby. A small language model on a phone can be helpful in such situations, but its advice needs to be safe and accurate. We built HandsOnAid, a 4-bit Gemma 2B model fine-tuned with QLoRA on FirstAidQA dataset, a corpus of 5,550 first-aid question-answer pairs. We compared seven configurations, including the base, 4-bit and 8-bit fine-tuned…

## 112. What a CAGE 4 Score Measures: An Audit of a Learned Cyber-Defense Benchmark, Its Reference Defenders, and the Tables Built on Them

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, evaluation, benchmark
- 作者：James Rice, Ji Hwan Park, Andres Kwasinski
- 链接：[arXiv](https://arxiv.org/abs/2611.14068) · [PDF](https://arxiv.org/pdf/2611.14068) · [HF](https://huggingface.co/papers/2611.14068)

CAGE Challenge 4 is the benchmark on which learned multi-agent cyber defenders are compared. We reproduce its two reference defenders, KEEP and H-MARL Expert, in a pinned container and show that three things read from it measure less than they are taken to measure. First, the simulator silently discards any action asserted for an agent whose previous action is still running, and charges one point for a discarded…

## 113. From Bias to Positionality: A critical grammar for Large Language Models

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, language model, large language
- 作者：Dave Murray-Rust, Elisa Giaccardi, Federico Bomba, Maria Luce Lupetti
- 链接：[arXiv](https://arxiv.org/abs/2611.14079) · [PDF](https://arxiv.org/pdf/2611.14079) · [HF](https://huggingface.co/papers/2611.14079)

Bias has become a default lens for understanding what machine learning systems do and how we should relate to them. Bias is at root a deviation from a standard; in decision making systems we can supply a standard from outside: a law, a protected attribute, a benchmark, a statistical property. However, even there, biased is often used as a shorthand, without stating what the position taken is - a silent ``relative…

## 114. Model-Free Runtime Measurement of Task-Relevant Information

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reinforcement learning, spec
- 作者：Dimitris Panagopoulos, Adolfo Perrusquía, Yang Xing, Weisi Guo
- 链接：[arXiv](https://arxiv.org/abs/2611.14111) · [PDF](https://arxiv.org/pdf/2611.14111) · [HF](https://huggingface.co/papers/2611.14111)

Autonomous systems increasingly monitor physical kinematics, environmental states and task completion outcomes. While existing work provides methods to plan information seeking actions and interpret acquired observations, current approaches do not monitor whether the live process of information gathering is functioning properly. Consequently, such systems can remain operationally active without resolving outstanding…

## 115. TAMEing the Open-World Personalization: Towards Open-Set Personalized MLLM Assistant

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：language model, large language, spec
- 作者：Rongpei Hong, Jian Lang, Ting Zhong, Fan Zhou
- 链接：[arXiv](https://arxiv.org/abs/2611.14118) · [PDF](https://arxiv.org/pdf/2611.14118) · [HF](https://huggingface.co/papers/2611.14118)

Personalizing Multimodal Large Language Models (MLLMs) as intelligent assistants has recently emerged as an active research topic, where an MLLM is expected to go beyond generic, one-size-fits-all replies, and instead generate responses grounded in user-specific objects, entities, and concepts encountered during interactions. Nevertheless, existing studies mainly focus on personalizing MLLMs on a static, predefined…

## 116. CroCoMAE: Cross-modal self-supervised collaborative representation learning for SAR-optical remote sensing data

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, spec
- 作者：Vito Recchia, Giuseppe Guarino, Cássio Fraga Dantas, Giuseppina Andresini, Annalisa Appice, Dino Ienco
- 链接：[arXiv](https://arxiv.org/abs/2611.14124) · [PDF](https://arxiv.org/pdf/2611.14124) · [HF](https://huggingface.co/papers/2611.14124)

Remote sensing increasingly captures the Earth's surface through complementary sensors such as SAR and optical, yet ground-truth annotations remain scarce, limiting supervised approaches. Self-supervised learning (SSL) addresses the label scarcity, and cross-modal SSL further exploits the complementarity between co-located sensors, but existing cross-modal frameworks align modalities mostly through global…

## 117. Hierarchical Graph Representation Learning with Pooling-Induced Substructures

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, evaluation, benchmark
- 作者：Luca Sbicego, Xiaowen Dong, Dorina Thanou
- 链接：[arXiv](https://arxiv.org/abs/2611.14126) · [PDF](https://arxiv.org/pdf/2611.14126) · [HF](https://huggingface.co/papers/2611.14126)

Hierarchical graph-level tasks that require reasoning over substructures that extend beyond local neighborhoods are posing challenges for standard Graph Neural Networks (GNNs). While graph pooling aims to address this by coarsening graphs into hierarchical representations, existing methods often fail to explicitly preserve the substructures they induce, leading to inconsistent empirical performance. Moreover,…

## 118. DailyWildfireCAN: A Dataset and Benchmark for Next-Day Wildfire Spread Prediction in Canada

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, spec
- 作者：Mahacine Ettahri, Hager Radi Abdelwahed, Toluwaleke Olutayo, Daniel Aloise, Gaétan Marceau Caron
- 链接：[arXiv](https://arxiv.org/abs/2611.14207) · [PDF](https://arxiv.org/pdf/2611.14207) · [HF](https://huggingface.co/papers/2611.14207)

Wildfires represent a critical ecological and socio-economic challenge in Canada, where vast boreal forests and a warming climate have amplified the frequency and severity of extreme fire seasons. Predicting next-day wildfire spread can support fire management, but requires capturing complex interactions among weather, fuels, and terrain. Deep learning has emerged as a promising approach to learning these…

## 119. Verifiable Agentic Traffic Class: A Policed Quality-of-Service Mechanism for Agentic AI Traffic, Evaluated from Simulation to Real-Kernel Adversarial Testing

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, language model, large language
- 作者：Naveen Babu Narayanan Nair, Sajay Kurup
- 链接：[arXiv](https://arxiv.org/abs/2611.14211) · [PDF](https://arxiv.org/pdf/2611.14211) · [HF](https://huggingface.co/papers/2611.14211)

Software agents built on large language models generate traffic unlike human web traffic, yet routers have no class for it and cannot verify a sender's claim to be an agent. This paper proposes the Verifiable Agentic Traffic Class (VATC), which combines a reserved Differentiated Services Code Point (DSCP) value declaring agent traffic, a router-side classifier that demotes flows contradicting the declaration to a…

## 120. Federated Learning for Cross-Regional Epidemic Forecasting with Asynchronous Outbreaks

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, benchmark, spec
- 作者：Ruibin Liu, Francisco Fernandes, Xuanfeng Li, Zige Liu, André Salgado, Chitin Hon, Zifeng Yang, Arlindo Oliveira, Ana Teresa Freitas
- 链接：[arXiv](https://arxiv.org/abs/2611.14272) · [PDF](https://arxiv.org/pdf/2611.14272) · [HF](https://huggingface.co/papers/2611.14272)

Objective: Epidemic outbreaks are often asynchronous across regions, yet collaborative forecasting is hampered by privacy laws and heterogeneous public health interventions. We developed and evaluated, as a proof of concept, a federated learning (FL) framework for cross-regional COVID-19 forecasting under asynchronous outbreaks among Guangdong, Macau, and Portugal, while maintaining data sovereignty. Methods: Using…
