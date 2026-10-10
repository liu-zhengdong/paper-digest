# 每日 AI 论文

生成时间：2026-10-10 05:53 UTC  ·  共 120 篇（已按 arXiv ID 去重）

来源：Hugging Face Daily Papers + arXiv（cs.AI / cs.LG / cs.CL / cs.CV）。
排序：HF 上榜、点赞、多源命中、兴趣词。兴趣词可在 `config.json` 改。

## 1. TokenRouter: Efficient Serving System for Token-Level LLM Routing

- 分数：40.0  ·  HF 赞：111  ·  来源：huggingface + arxiv
- 兴趣命中：language model, large language, coding, spec
- 作者：Tianyu Fu, Tengxuan Liu, Ruoxi Wang, Yixin Dong, Yi Ge, Yichen You, Yu Wang
- 链接：[arXiv](https://arxiv.org/abs/2610.12242) · [PDF](https://arxiv.org/pdf/2610.12242) · [HF](https://huggingface.co/papers/2610.12242)

Large language model (LLM) routing distributes inference work across different models, advancing the cost-quality Pareto frontier of LLM serving. While coarse-grained routing at the session or query level has been widely adopted in production systems, recent algorithmic work shows that fine-grained token-level routing can yield substantial efficiency and quality gains. However, efficiently serving token-level routed…

## 2. SuperNav: An Agentic Navigation System for Any Task in Any Scene

- 分数：40.0  ·  HF 赞：64  ·  来源：huggingface + arxiv
- 兴趣命中：agent, evaluation, language model, large language, spec
- 作者：Jinkai Zhang, Jingyi Xu, Yuanhong Yu, Jiarui Guo, Ruizhen Hu, Hujun Bao, Xiaowei Zhou, Sida Peng
- 链接：[arXiv](https://arxiv.org/abs/2610.12126) · [PDF](https://arxiv.org/pdf/2610.12126) · [HF](https://huggingface.co/papers/2610.12126)

General-purpose service robots need navigation systems that can handle diverse human requests in unfamiliar environments, combining task generality with scene generality. Some existing methods fine-tune multimodal large language models (MLLMs) to predict navigation actions, making their behavior dependent on the coverage of navigation training data and potentially limiting generalization to new requests and…

## 3. AgentGarten: Code Worlds for Evolving Agents

- 分数：36.0  ·  HF 赞：134  ·  来源：huggingface + arxiv
- 兴趣命中：agent, reinforcement learning
- 作者：Jiawei Chi, Shangchen Miao, Zhiyuan Shi, Kailu Wu, Hanyang Wang, Weiliang Chen, Qiyu Dai, Jinshan Ren, Jun Gao, Mingsheng Long, Yueqi Duan, Jiangran Lyu, Jialong Wu, Fangfu Liu
- 链接：[arXiv](https://arxiv.org/abs/2610.12374) · [PDF](https://arxiv.org/pdf/2610.12374) · [HF](https://huggingface.co/papers/2610.12374)

Interactive virtual worlds allow agents to learn through exploration and interaction. What agents can learn is bounded by the environments they practice in, which must be faithful, with consistent state, rules, and dynamics, and realistic, with observations that follow the real-world visual distributions. Achieving both across diverse worlds remains a bottleneck. We introduce AgentGarten, a framework that couples…

## 4. Learn2Play Bench: How Well Do LLM Agents Learn from Experience in Unfamiliar Environments?

- 分数：36.0  ·  HF 赞：109  ·  来源：huggingface
- 兴趣命中：agent, reasoning, evaluation, benchmark
- 作者：Yibo Li, Jinhang Qiu, Zhi Zheng, Qianyun Guo, Jiaying Wu, Shuo Ji, Bryan Hooi
- 链接：[arXiv](https://arxiv.org/abs/2610.08215) · [PDF](https://arxiv.org/pdf/2610.08215) · [HF](https://huggingface.co/papers/2610.08215)

Learning from experience is essential for LLM agents to adapt to unfamiliar and dynmaic environments. Evaluating this ability is therefore important for understanding how effectively agents acquire and use new knowledge. Existing benchmarks have sought to evaluate this ability, but they primarily evaluate tasks whose rules are provided in the instructions or already familiar to pretrained models, making it difficult…

## 5. MiMo-V2.6: Scaling Reinforcement Learning Towards Self-Improvement

- 分数：36.0  ·  HF 赞：58  ·  来源：huggingface + arxiv
- 兴趣命中：agent, reinforcement learning
- 作者：Core Team, Zongming Qiao, Ziyue Hua, Zirui Ou, Zihao Yue, Zihan Jiang, Zhuo Huang, Zhiyang Chen, Zhixian Zheng, Zhipeng Xu, Zhengrui Ma, Yuyang Hu, Yuhang Dong, Yuechen Zhang, Yudong Wang, Yuanxin Liu, Yixin Yang, Yishuo Cai, Yikai Zhao, Yihan Yan, Yifan Zhang, Yifan Song, Xiyu Wei, Xing Zhang, Xin Zhang, Xiaoqian Liu, Xiaodong Ji, Xiangwei Deng, Xueyu Guo, Wenhan Ma, Weimin Xiong, Weikun Wang, Weiji Zhuang, Shuo Liu, Shuhuai Ren, Shuhao Gu, Shimao Chen, Shijie Cao, Shihua Yu, Shicheng Li, Shengjie Zhou, Shaolei Zhang, Rang Li, Qiying Wang, Qingkai Fang, Qianli Chen, Minzheng Wang, Liwen Wang, Linli Yao, Linghao Zhang, Liangyu Cheng, Liang Zhao, Lei Li, Jinhao Dong, Jinyu Xiang, Jianyu Wei, Jiangshan Duo, Huaqiu Liu, Huanjie Fan, Hongyi Guan, Hongshen Xu, Hao Tian, Hanyu Li, Hailin Zhang, Gang Wang, Fuli Luo, Feng Wei, Dong Zhang, Dawei Zhu, Chiheng Lou, Chenhong He, Chenhao He, Chenghua Liu, Bowen Ye, Bowen Shen, Boshen Xu, Bo Yang, Bingquan Xia, Bangjun Xiao, Baixuan Xu, Zhouxiang Mao, Zhiyang Zhang, Zhixiang Xu, Zhenru Lin, Zhengju Tang, Zhaojun Huang, Yuzhe Weng, Yuxing Xiang, Yuxiao Li, Yuheng Yang, Yuhang Wang, Yuchen Liu, Yuanyuan Tian, Yuanliang Dong, Yu Cheng, Yongzhe He, Yongshun Liang, Yong Wang, Yiyan Wang, Yitian Gong, Yijie Zhang, Yanshu Xin, Xun Zhang, Xingjian Zhao, Wenyu Yang, Wenshan Huang, Wenhao Li, Tingwei Huang, Tianyu Yu, Tianyang Lu, Taoyu Yang, Sinan Du, Shutong Tian, Shulin Du, Shengfan Wang, Shanchuan Fang, Qihao Zhang, Qibin Yang, Qian Yu, Qian Tu, Pengrong Xie, Peipei Wang, Peidian Li, Minkun Guo, Mingchen Shao, Luohan Gao, Lijie Wang, Liang Shi, Kaiqi Chen, Kaiming Liu, Kaifei Wang, Kai Yang, Jinlong Xue, Jiechen Zhang, Jiaxuan Liu, Hongxu An, Hao Peng, Hanglong Lü, Guonan Wang, Feiyu Yang, Fanyu Cao, Fangyue Liu, Fan Cui, Cong Wang, Chun Chen, Chenxu Bai, Chengxuan Zhu, Chenghua Wang, Boyi Zeng
- 链接：[arXiv](https://arxiv.org/abs/2610.11959) · [PDF](https://arxiv.org/pdf/2610.11959) · [HF](https://huggingface.co/papers/2610.11959)

Reinforcement learning (RL) is the central training paradigm for advancing large foundation models towards self-improvement. This report introduces the MiMo-V2.6 series, an omni-modal family that pushes the frontier of model intelligence by scaling RL compute. Prior to RL, we conduct mid-training on a broad multimodal corpus to provide ample exploration space, and build a solid infrastructure on the pretrained…

## 6. Multi-Agent Egocentric World Model with Fine-Grained Embodied Interaction

- 分数：36.0  ·  HF 赞：44  ·  来源：huggingface + arxiv
- 兴趣命中：agent, memory
- 作者：Dahyun Chung, Siyoon Jin, Hyunwook Choi, Honggyu An, Junyoung Seo, Hyunsung Kim, Seung Wook Kim, Seungryong Kim
- 链接：[arXiv](https://arxiv.org/abs/2610.12299) · [PDF](https://arxiv.org/pdf/2610.12299) · [HF](https://huggingface.co/papers/2610.12299)

Egocentric world models predict first-person observations conditioned on an agent's actions, but most focus on a single agent. Real embodied settings often involve multiple agents that act and interact within a shared environment. Existing multi-agent world models rely on coarse actions like locomotion, camera control, or discrete commands, leaving fine-grained embodied interactions underexplored. We formulate…

## 7. Memento 3: Model-Based Recursive Self-Improvement through Reflective Rulebooks

- 分数：33.5  ·  HF 赞：27  ·  来源：huggingface + arxiv
- 兴趣命中：agent, memory, spec, planning
- 作者：Haoyu Zhao, Zhengxu Yu, Zhiyuan He, Meng Fang, Rasul Tutunov, Haitham Bou-Ammar, Weilin Luo, Jun Wang
- 链接：[arXiv](https://arxiv.org/abs/2610.11794) · [PDF](https://arxiv.org/pdf/2610.11794) · [HF](https://huggingface.co/papers/2610.11794)

Learning to act in unfamiliar environments requires agents to infer how the world works and revise that understanding as new evidence arrives. Yet limited observations can support multiple world models that explain past interactions but predict different outcomes in unseen states. We introduce Memento 3, building on the Memento series to enable frozen LLM agents to continually learn explicit world models through…

## 8. OuroWorld: Bringing Any 3D World Alive as Diverse, Endlessly Looping 3D Cinemagraphs

- 分数：31.5  ·  HF 赞：31  ·  来源：huggingface + arxiv
- 兴趣命中：evaluation, language model
- 作者：You-Zhe Xie, Ting-Wei Chou, Yu-Hsuan Li, Kaipeng Zhang, Zhixiang Wang, Yu-Lun Liu
- 链接：[arXiv](https://arxiv.org/abs/2610.12461) · [PDF](https://arxiv.org/pdf/2610.12461) · [HF](https://huggingface.co/papers/2610.12461)

Recent 3D world models generate photorealistic, explorable scenes that remain frozen in time. OuroWorld is a mask-free framework that turns any static 3D Gaussian Splatting scene into a 3D cinemagraph: a dynamic scene with vivid, diverse motion looping seamlessly from any viewpoint. A vision-language model infers plausible dynamics and guides a video model to synthesize a reference video, which we lift and complete…

## 9. U-Space: Uncovering When and Why Uncertainty Arises in Language Models

- 分数：31.0  ·  HF 赞：30  ·  来源：huggingface
- 兴趣命中：reasoning, evaluation, benchmark, language model, large language, spec
- 作者：Tobias Braun, Nils Loose, Alexander Herzog, Virginia Ceccatelli, Marcus Rohrbach, Thomas Eisenbarth, Lorenzo Cavallaro
- 链接：[arXiv](https://arxiv.org/abs/2610.09087) · [PDF](https://arxiv.org/pdf/2610.09087) · [HF](https://huggingface.co/papers/2610.09087)

Large language models are informing decisions with ever-higher stakes. As the consequences of their errors grow, a central question becomes harder to ignore: how much can we trust an individual answer? Yet recognizing when to defer remains difficult because language models can present incorrect conclusions with fluent explanations and an authoritative tone. Uncertainty quantification seeks to address this disconnect…

## 10. TestPrism: Rethinking Test Evaluation Beyond a Single Reference

- 分数：30.5  ·  HF 赞：29  ·  来源：huggingface
- 兴趣命中：agent, evaluation, language model, large language, coding
- 作者：Han Li, Lingxiang Hu, Jiacheng Huang, Ziqian Jiang, Jingkai Luo, Wei Gao, Yunfan Tan, Zun Wang, Jiaheng Liu
- 链接：[arXiv](https://arxiv.org/abs/2610.12289) · [PDF](https://arxiv.org/pdf/2610.12289) · [HF](https://huggingface.co/papers/2610.12289)

Large language model (LLM) coding agents have advanced test generation across diverse programming tasks. However, the common practice of evaluating tests against a single reference solution overlooks alternative valid implementations and can overstate test quality. We introduce TestPrism, comprising 300 test tasks from 17 sources and 3000 candidate implementations, evenly split between valid and invalid solutions.…

## 11. SparseDecoding: Decoding-Aware Pruning for Accurate and Efficient LLM Inference

- 分数：30.5  ·  HF 赞：21  ·  来源：huggingface + arxiv
- 兴趣命中：memory, benchmark, language model, large language, coding, spec
- 作者：Qitong Wang, Xinwei Niu, Mingluo Su, Shanwei Zhao, Shiai Zhu, Huan Wang
- 链接：[arXiv](https://arxiv.org/abs/2610.12327) · [PDF](https://arxiv.org/pdf/2610.12327) · [HF](https://huggingface.co/papers/2610.12327)

The memory-bound nature of the decoding stage of large language model (LLM) inference incurs significant latency. Layer-wise training-free network pruning approaches guided by the Hessian have been a prominent solution to this problem, as pruning reduces the number of nonzero parameters read from memory during decoding. Nevertheless, typical methods in this line compute the Hessian using pre-collected natural…

## 12. From Traces to Agentic Worlds: Agentic Language World Models for Interactive Environment Simulation

- 分数：30.0  ·  HF 赞：98  ·  来源：huggingface
- 兴趣命中：agent
- 作者：Quanyu Long, Xiao Chen, Jianda Chen, Haozhen Zhang, Qisheng Hu, Jianzhu Bao, Wenya Wang
- 链接：[arXiv](https://arxiv.org/abs/2610.06100) · [PDF](https://arxiv.org/pdf/2610.06100) · [HF](https://huggingface.co/papers/2610.06100)

Realistic environment replicas are increasingly valuable for training and evaluating LLM agents, yet the original systems may be inaccessible or impractical to reproduce. We explore agentic language world modeling: rather than rebuilding an executable environment, a world model agent serves as the environment for a task agent and supports faithful and stateful simulation. We instantiate this paradigm with Trace2Env,…

## 13. In-context Robot Learning Made Simple: A Democratized Recipe for Manipulation Tasks

- 分数：30.0  ·  HF 赞：41  ·  来源：huggingface
- 兴趣命中：spec
- 作者：Minxing Li, Minghao Han, Weizhi Zhao, Hanwen Wang, Xiangshuo Liu, Shuyao Shang, Jingxiang Zhou, Mingchao Sun, Hongyu Pan, Mu Xu, Yu Liu, Lue Fan, Zhaoxiang Zhang
- 链接：[arXiv](https://arxiv.org/abs/2609.38173) · [PDF](https://arxiv.org/pdf/2609.38173) · [HF](https://huggingface.co/papers/2609.38173)

We study robotic in-context learning (ICL), an emerging paradigm that enables robots to infer and execute tasks from visual demonstrations. Despite its growing promise, the problem itself remains under-defined: a visual demonstration simultaneously conveys action trajectories, object semantics, manipulation affordances, spatial relations, and task goals, making it unclear what information the robot is actually…

## 14. Beyond Spatio-Temporal Priors: A Generalizable Approach for Dense Correspondence Matching

- 分数：30.0  ·  HF 赞：32  ·  来源：huggingface + arxiv
- 兴趣命中：benchmark
- 作者：Luping Liu, Bingyi Kang, Yifan Wang, Dong Xu
- 链接：[arXiv](https://arxiv.org/abs/2610.12421) · [PDF](https://arxiv.org/pdf/2610.12421) · [HF](https://huggingface.co/papers/2610.12421)

Dense correspondence matching has historically been bounded by simplifying spatio-temporal priors, such as smooth motion and rigid geometry. While effective for classical tasks, these assumptions break down in image editing and reference-guided generation (IEG), where transformations can preserve visual identity while breaking physical continuity. To establish identity-preserving correspondence across such…

## 15. OneSearch-VL: Unified Multimodal Deep Research Agent for Image and Video

- 分数：29.5  ·  HF 赞：19  ·  来源：huggingface + arxiv
- 兴趣命中：agent, evaluation, benchmark, spec, retrieval
- 作者：Hongyu Li, Manyuan Zhang, Kaituo Feng, Shu Chen, Dian Zheng, Hao Li, Hao Yu, Zhangquan Chen, Zoey Guo, Ray Zhang, Shaofei Huang, Tianrui Hui, Linjiang Huang, Si Liu
- 链接：[arXiv](https://arxiv.org/abs/2610.12419) · [PDF](https://arxiv.org/pdf/2610.12419) · [HF](https://huggingface.co/papers/2610.12419)

Single-image, multi-image, and video deep research require different visual operations but share a workflow of visual grounding, external retrieval, and fact composition. A key challenge is to preserve the dependencies linking localized visual anchors, entity relations, source-supported facts, and answer-producing operations. We introduce OneSearch-VL, a unified agent centered on the Visually Grounded Evidence Graph…

## 16. DreamTrue: Action-Faithful Robot World Model with Counterfactual Post-Training

- 分数：29.0  ·  HF 赞：34  ·  来源：huggingface + arxiv
- 兴趣命中：-
- 作者：Junyan Li, Ruizhi Li, Yu Liu, Xiangshuo Liu, Mingchao Sun, Hongyu Pan, Mu Xu, Lue Fan, Zhaoxiang Zhang
- 链接：[arXiv](https://arxiv.org/abs/2610.12468) · [PDF](https://arxiv.org/pdf/2610.12468) · [HF](https://huggingface.co/papers/2610.12468)

We present DreamTrue, a multi-view, cross-embodiment robot world model for action-faithful and physically plausible video prediction. Training such a model on existing robot datasets faces two obstacles: imprecise calibration can impair action following, while limited coverage of unsuccessful interactions can bias predictions toward successful outcomes. To improve action following across embodiments, we render…

## 17. Reasoning-Informed Visual Editing

- 分数：28.5  ·  HF 赞：17  ·  来源：huggingface + arxiv
- 兴趣命中：agent, reasoning, evaluation, benchmark, planning
- 作者：Xue Yang, Peiyuan Zhang, Yilun Zhu, Qihao Yang, Mingxin Liu, Xiangyu Zhao, Ziqian Fan, Zhaokai Wang, Yan Li, Yifan Yang, Xu Yang, Xiaosong Jia, Yue Zhou, Zhihang Zhong, Junchi Yan
- 链接：[arXiv](https://arxiv.org/abs/2610.12343) · [PDF](https://arxiv.org/pdf/2610.12343) · [HF](https://huggingface.co/papers/2610.12343)

Large Multi-modality Models (LMMs) have made significant progress in visual understanding and generation, but still face challenges in visual editing, particularly in following complex instructions, preserving appearance consistency, and supporting flexible input formats. To study this gap, we introduce RISEBench, the first benchmark for evaluating Reasoning-Informed viSual Editing (RISE), and extend it to…

## 18. VibeEdit: Image Editing with Canvas Instructions

- 分数：26.5  ·  HF 赞：13  ·  来源：huggingface + arxiv
- 兴趣命中：reinforcement learning, evaluation, benchmark, spec
- 作者：Jinjing Zhao, Fangyun Wei, Yitong Wang, Xiuyu Wu, Yunuo Chen, Yang Yue, Sirui Zhang, Wenbo Wang, Hongyang Zhang, Dong Chen, Yan Lu, Chang Xu
- 链接：[arXiv](https://arxiv.org/abs/2610.12229) · [PDF](https://arxiv.org/pdf/2610.12229) · [HF](https://huggingface.co/papers/2610.12229)

In text-guided image editing, describing the desired change is often straightforward, but identifying the intended object or region can be cumbersome, especially when several objects look alike. We introduce a new image editing interface that lets users place spatial marks and optional short notes directly on the image. Together, these annotations form a canvas instruction that specifies where to edit and what to…

## 19. OmniCapBench: A Deep-Structured Evaluation Framework for Fine-Grained Audio-Visual Captioning

- 分数：25.5  ·  HF 赞：11  ·  来源：huggingface + arxiv
- 兴趣命中：reasoning, evaluation, benchmark, language model, large language
- 作者：Zhongyu Yang, Jiale Tao, Ruitao Chen, Zuhao Yang, Yingfang Yuan, Xueliang Zhao, Auden, Kai Wang, Shuai Shao, Biao Wang, Steve Yves, Qinglin Lu
- 链接：[arXiv](https://arxiv.org/abs/2610.12458) · [PDF](https://arxiv.org/pdf/2610.12458) · [HF](https://huggingface.co/papers/2610.12458)

Multimodal large language models (MLLMs) are rapidly evolving toward continuous audio--visual reasoning, creating an urgent need for evaluations that expose their capability limits. Audio--visual captioning is an ideal diagnostic task, yet current benchmarks face a coupled trade-off: whole-caption scores provide coverage without localization, local probes provide localization without coverage, and unconstrained LLM…

## 20. SpaceCast-Bench: Evaluating Predictive Spatial Reasoning in Vision-Language Models

- 分数：23.5  ·  HF 赞：7  ·  来源：huggingface + arxiv
- 兴趣命中：reasoning, benchmark, language model, spec
- 作者：Hongxing Li, Jinyue Su, Dingming Li, Wenqi Zhang, Weiming Lu, Jun Xiao, Yueting Zhuang, Yongliang Shen
- 链接：[arXiv](https://arxiv.org/abs/2610.12402) · [PDF](https://arxiv.org/pdf/2610.12402) · [HF](https://huggingface.co/papers/2610.12402)

Existing spatial reasoning benchmarks mainly test spatial perception: reading off relations already visible in the input. Yet real-world spatial intelligence demands predictive spatial reasoning: constructing a scene from observations, anticipating how an intervention changes it, and reasoning about the unseen outcome. We introduce SpaceCast-Bench, the first benchmark to directly and diagnostically evaluate this…

## 21. MC-Sparse: Deconstructing and Closing the Dense-Sparse Attention Gap in Diffusion Transformers

- 分数：23.0  ·  HF 赞：30  ·  来源：huggingface
- 兴趣命中：-
- 作者：Jiarui Chen, Zeqiang Lai, Jiangshan Wang, Ziheng Ouyang, Ye Huang, Xiangyu Yue, Cewu Lu, Chunchao Guo
- 链接：[arXiv](https://arxiv.org/abs/2610.06801) · [PDF](https://arxiv.org/pdf/2610.06801) · [HF](https://huggingface.co/papers/2610.06801)

Sparse attention is a primary approach to reducing the latency of diffusion transformers in long-sequence generation tasks, such as video and high-resolution 3D asset generation. However, existing methods can degrade generation quality and fidelity at high sparsity levels. Through controlled oracle comparisons, we trace this degradation to three sources: constraints imposed by token grouping, inaccurate interaction…

## 22. Foundations of Large Language Models

- 分数：23.0  ·  HF 赞：18  ·  来源：huggingface
- 兴趣命中：reasoning, language model, large language
- 作者：Tong Xiao, Jingbo Zhu
- 链接：[arXiv](https://arxiv.org/abs/2501.09223) · [PDF](https://arxiv.org/pdf/2501.09223) · [HF](https://huggingface.co/papers/2501.09223)

This is a book about large language models. As indicated by the title, it primarily focuses on foundational concepts rather than comprehensive coverage of all cutting-edge technologies. The book is structured into six main chapters, each exploring a key area: pre-training, generative models, prompting, alignment, inference, and reasoning. It is intended for college students, professionals, and practitioners in…

## 23. SparseEngine: Sparse-First Inference Engine

- 分数：22.5  ·  HF 赞：13  ·  来源：huggingface
- 兴趣命中：agent, memory, benchmark, coding, spec
- 作者：Jitai Hao, Quansheng Gu, Qiang Huang, Jun Yu
- 链接：[arXiv](https://arxiv.org/abs/2609.39068) · [PDF](https://arxiv.org/pdf/2609.39068) · [HF](https://huggingface.co/papers/2609.39068)

Long-context LLM agents accumulate interaction histories that strain KV-cache memory and attention computation. Although sparse attention reduces these costs, heterogeneous cache representations and workflows hinder integration with existing inference engines, while prior sparse-serving abstractions support only specific layouts or workflows. We present SparseEngine, a ground-up, sparse-first inference engine whose…

## 24. Embodied Turing Machines: Stateful Code for Robot Recursive Self-Improvement

- 分数：22.0  ·  HF 赞：12  ·  来源：huggingface + arxiv
- 兴趣命中：agent, coding
- 作者：Kairui Hu, Siyuan Hu, Fangzhou Hong, Zhaoxi Chen, Ziwei Liu
- 链接：[arXiv](https://arxiv.org/abs/2610.12369) · [PDF](https://arxiv.org/pdf/2610.12369) · [HF](https://huggingface.co/papers/2610.12369)

Most robot policies keep a model in the control loop: a VLA maps observations to actions, and an Agent Harness, such as Agent-as-Policy or Harness VLA queries a VLM for decision making at run time. We propose a different view: the embodied world is an Embodied Turing Machine, whose tape is the robot and environment state and rules are the policy. If this state can be represented accurately, the decision making can…

## 25. From Prompting to Composing: A Spatial Canvas Interface for Poster Generation

- 分数：22.0  ·  HF 赞：8  ·  来源：huggingface + arxiv
- 兴趣命中：agent, benchmark, spec
- 作者：Yitong Wang, Fangyun Wei, Jinjing Zhao, Sirui Zhang, Hongyang Zhang, Dong Chen, Bo Dai, Yan Lu
- 链接：[arXiv](https://arxiv.org/abs/2610.12230) · [PDF](https://arxiv.org/pdf/2610.12230) · [HF](https://huggingface.co/papers/2610.12230)

Text prompting is an indirect interface for poster generation, requiring users to encode inherently two-dimensional composition intent into a one-dimensional sequence of words. We introduce a Spatial Canvas Interface that enables users to directly compose generation intent in space through four complementary binding types: semantic, identity, text, and pixel, together with Text Specifications for individual elements…

## 26. A Closer Look at Agentic BBO: Benchmarking LLM Agents for Black-Box Optimization

- 分数：22.0  ·  HF 赞：4  ·  来源：huggingface + arxiv
- 兴趣命中：agent, evaluation, benchmark, language model, large language, spec
- 作者：Ming Chen, Rong-Xi Tan, Ke Xue, Yu-Jie Zhou, Taiye Lu, Zhi-Xuan Gao, Peng Xie, Zijun Shen, Chen Lu, Haopu Shang, Chao Qian
- 链接：[arXiv](https://arxiv.org/abs/2610.12183) · [PDF](https://arxiv.org/pdf/2610.12183) · [HF](https://huggingface.co/papers/2610.12183)

Black-box optimization (BBO) arises in many scientific and engineering problems where objective evaluations are expensive and limited. Recent large language model (LLM) agents offer a new way to approach BBO by combining task semantics, computation, optimization tools, and feedback-driven decision making, showing great potential due to the integration with mathematically rigorous tools. However, existing agentic BBO…

## 27. LEGO: A Lifting-Free Approach for Exocentric-to-Egocentric Video Generation

- 分数：21.5  ·  HF 赞：19  ·  来源：huggingface + arxiv
- 兴趣命中：-
- 作者：Suhwan Cho, Yonwoo Choi, Soongjin Kim, Jicheol Park, Taegyu Lim
- 链接：[arXiv](https://arxiv.org/abs/2610.12442) · [PDF](https://arxiv.org/pdf/2610.12442) · [HF](https://huggingface.co/papers/2610.12442)

Generating an egocentric video from a single exocentric recording is a challenging case of novel view synthesis, as the two cameras share little overlap and much of the target view is unobserved. Current state-of-the-art methods reconstruct the scene explicitly by estimating depth, lifting the video into a point cloud, and re-rendering it from the egocentric camera to condition a video diffusion model. This…

## 28. BrickBench: Evaluating Agentic Brick Design

- 分数：21.5  ·  HF 赞：3  ·  来源：huggingface + arxiv
- 兴趣命中：agent, benchmark, coding, spec
- 作者：Peter Kulits, Yiqing Xu, R. Kenny Jones, Cordelia Schmid, Jiajun Wu
- 链接：[arXiv](https://arxiv.org/abs/2610.12452) · [PDF](https://arxiv.org/pdf/2610.12452) · [HF](https://huggingface.co/papers/2610.12452)

We propose BrickBench, a benchmark for agentic text-conditioned LEGO-set design. Given a prompt, an agent is tasked with producing an assembly that not only satisfies semantic and design criteria, but that can also be physically built. To do so, it must select parts from a discrete library and reason jointly about local and global constraints. We score validity, alignment, and design across three settings that vary…

## 29. Pumpire: Unified Benchmark for Metric Distance Estimation

- 分数：21.0  ·  HF 赞：10  ·  来源：huggingface + arxiv
- 兴趣命中：evaluation, benchmark
- 作者：Siyu Chen, Zehan Wang, Jiayang Xu, Yihan Wu, Jialei Wang, Junming Chen, Ziang Zhang, Yutong Ying, Zhou Zhao
- 链接：[arXiv](https://arxiv.org/abs/2610.12423) · [PDF](https://arxiv.org/pdf/2610.12423) · [HF](https://huggingface.co/papers/2610.12423)

We present Pumpire, a unified benchmark for evaluating metric point-pair distance estimation capability of both image- and video-level 3D foundation models, with or without depth priors. In contrast to previous approaches that normally evaluate depth and camera intrinsics separately or evaluate point-clouds with geometric similarity metrics, which cannot directly reflect models' point-to-point distance estimation…

## 30. Post-Training Frontier Text-to-Image Models by Composing Preference and Rubric Rewards

- 分数：20.5  ·  HF 赞：25  ·  来源：huggingface
- 兴趣命中：-
- 作者：Yuanhao Ban, I-Hung Hsu, Anastasios Angelopoulos, Wei-Lin Chiang, Ion Stoica, Cho-Jui Hsieh
- 链接：[arXiv](https://arxiv.org/abs/2610.02967) · [PDF](https://arxiv.org/pdf/2610.02967) · [HF](https://huggingface.co/papers/2610.02967)

Recent text-to-image generation models have achieved remarkable visual quality, but improving them through post-training remains challenging because no single reward signal captures the full range of human preference. In this work, we develop a simple and effective post-training recipe for open-domain text-to-image generation based on the composition of complementary reward signals. Our reward system consists of two…

## 31. SanSi: A Looped Typed Decision Model for System 1.5 Thinking

- 分数：20.5  ·  HF 赞：13  ·  来源：huggingface
- 兴趣命中：reasoning, reinforcement learning, language model
- 作者：Shuyu Gan, Young-Jun Lee, Dongyeop Kang
- 链接：[arXiv](https://arxiv.org/abs/2610.07730) · [PDF](https://arxiv.org/pdf/2610.07730) · [HF](https://huggingface.co/papers/2610.07730)

Typed decision models answer a declared question without generating text: a decision head returns a probability for each of the declared options in a single forward pass. A single pass is fast, intuitive System 1 thinking. We study what lies between one pass and generated reasoning: looping, in which the same layers are recursively applied several times before one typed readout. Each loop lets the model revise its…

## 32. Opera: A Verbal Critic Framework for Long-horizon Coding Agents

- 分数：20.0  ·  HF 赞：8  ·  来源：huggingface
- 兴趣命中：agent, benchmark, coding, spec
- 作者：Kai Mei, Zhiyuan Hu, Yutong Dai, Juntao Tan, Yifan Zhang, Dingjie Song, Dimitris N. Metaxas, Silvio Savarese, Ran Xu, Zeyuan Chen
- 链接：[arXiv](https://arxiv.org/abs/2609.33987) · [PDF](https://arxiv.org/pdf/2609.33987) · [HF](https://huggingface.co/papers/2609.33987)

Long-horizon coding agents need timely corrections, yet feedback can be ineffective or even harmful when it misjudges ongoing work or fails to address the underlying problem. Existing critics focus on evaluating trajectories and generating feedback, but rarely track what happens after feedback is delivered. We present Opera, a verbal critic framework that treats each correction as a persistent note, followed until…

## 33. SpatialOPSD: Self-Distilling Spatial Intelligence from Verified Coding Agent Traces

- 分数：20.0  ·  HF 赞：8  ·  来源：huggingface
- 兴趣命中：agent, reasoning, benchmark, language model, large language, coding
- 作者：Rongxue Li, Meng Yang, Yiru Mao, Yongliang Tao, Lulu Hu, Bin Yang, Zhao Xu, Weihua Luo, Bowen Xu
- 链接：[arXiv](https://arxiv.org/abs/2610.11366) · [PDF](https://arxiv.org/pdf/2610.11366) · [HF](https://huggingface.co/papers/2610.11366)

Spatial coding agents significantly improve spatial reasoning in Multimodal Large Language Models (MLLMs) by using external tools to generate verified execution traces. However, this paradigm inherently suffers from prohibitive inference-time overhead and external dependencies. In this paper, we explore whether an MLLM can internalize this agentic capability to operate entirely tool-free. We begin with a simple…

## 34. What Did the Agent Actually Do? Evidence-Grounded Oversight for Long-Horizon Agents

- 分数：19.5  ·  HF 赞：15  ·  来源：huggingface
- 兴趣命中：agent, benchmark
- 作者：Zhongxiang Sun, Jiahao Yan, Hongkang Zhao, Haojie Ding, Boheng Zhang, Fan Yang, Xiao Zhang, Jun Xu
- 链接：[arXiv](https://arxiv.org/abs/2610.06406) · [PDF](https://arxiv.org/pdf/2610.06406) · [HF](https://huggingface.co/papers/2610.06406)

As agents take on long-horizon tasks, users shift from making individual decisions to overseeing autonomous execution. Yet the volume of agent activity and the fragmentation of supporting evidence make it difficult to determine which decisions warrant user verification. We study monitors that identify consequential decisions and locate evidence to help users assess their implications. We introduce AgentMonBench, a…

## 35. A GPU-Parallel Framework for Heterogeneous Multi-Task Reinforcement Learning

- 分数：19.5  ·  HF 赞：7  ·  来源：huggingface
- 兴趣命中：reinforcement learning, evaluation, benchmark, spec
- 作者：Rui Zhang, Qiwei Wu, Zhengyu Zhang, Tao Li, Hongyu Zhou, Xiang Li, Yunrong Guo, Junjie Lai, Renjing Xu, Weihua Zhang
- 链接：[arXiv](https://arxiv.org/abs/2606.03335) · [PDF](https://arxiv.org/pdf/2606.03335) · [HF](https://huggingface.co/papers/2606.03335)

GPU-parallel simulation provides abundant robot interaction, but existing benchmarks rarely combine this scale with heterogeneous manipulation tasks and standardized multi-task RL evaluation. We introduce Hebero (Heterogeneous Benchmark for Robot Learning), a GPU-parallel Isaac Lab benchmark that enables efficient joint training and evaluation of a single policy across all 40 heterogeneous tasks. Scaling experiments…

## 36. Accurate but Not Humble: Evaluating Epistemic Humility in LLM Agents under Knowledge Conflict

- 分数：19.5  ·  HF 赞：3  ·  来源：huggingface + arxiv
- 兴趣命中：agent, evaluation, language model
- 作者：Kaiser Sun, Bernal Jimenez Gutierrez, Hongjun Liu, Jingyu Zhang, Jie Gao, Mark Dredze, Daniel Khashabi
- 链接：[arXiv](https://arxiv.org/abs/2610.12360) · [PDF](https://arxiv.org/pdf/2610.12360) · [HF](https://huggingface.co/papers/2610.12360)

When retrieved evidence contradicts an agent's prior beliefs, does it revise its answer, acknowledge uncertainty, or persist with an incorrect conclusion? Existing evaluations of agentic systems focus primarily on task success, offering limited insight into how agents handle such conflicts. We propose to evaluate agents on epistemic humility (EH): the agent's willingness to recognize, act on, and communicate…

## 37. Distilling Routed 3D Privilege for Spatial Reasoning in Vision-Language Models

- 分数：19.5  ·  HF 赞：3  ·  来源：huggingface + arxiv
- 兴趣命中：reasoning, benchmark, language model
- 作者：Hongxing Li, Yixin Li, Dingming Li, Zixuan Wang, Yuchen Yan, Wenqi Zhang, Weiming Lu, Yongliang Shen
- 链接：[arXiv](https://arxiv.org/abs/2610.12355) · [PDF](https://arxiv.org/pdf/2610.12355) · [HF](https://huggingface.co/papers/2610.12355)

Spatial reasoning remains a persistent weakness of vision-language models (VLMs), because RGB inputs do not directly provide geometric evidence. Existing remedies either inject 3D into the model at inference, paying architecture and latency costs, or train with outcome rewards that supervise only the final answer. Spatial errors originate in perception: a misjudged depth or direction can be corrected only by the…

## 38. ViSkill: Reinforcing VLM Agents with Evolving Visual-Native Skills

- 分数：19.0  ·  HF 赞：10  ·  来源：huggingface + arxiv
- 兴趣命中：agent
- 作者：Hongxing Li, Dingming Li, Yixin Li, Yong Du, Wenqi Zhang, Weiming Lu, Jun Xiao, Yueting Zhuang, Yongliang Shen
- 链接：[arXiv](https://arxiv.org/abs/2610.12403) · [PDF](https://arxiv.org/pdf/2610.12403) · [HF](https://huggingface.co/papers/2610.12403)

Skill-augmented agents improve sample efficiency by distilling successful trajectories into reusable strategies. Yet most existing approaches remain text-centric, linearizing spatial layouts and action-state correspondences into language that loses critical geometric structure. Recent efforts have begun incorporating visual evidence, but construct and update skills separately from policy optimization, leaving their…

## 39. USDCraft: Geometrically Grounded Programmatic Modeling of Articulated 3D Assets for Simulation

- 分数：18.5  ·  HF 赞：13  ·  来源：huggingface
- 兴趣命中：benchmark, spec
- 作者：Chuanrui Zhang, Zaijia Yang, Duomin Wang, Lu Shi, Daquan Zhou, Ruihua Zhang, Ziwei Wang
- 链接：[arXiv](https://arxiv.org/abs/2610.11322) · [PDF](https://arxiv.org/pdf/2610.11322) · [HF](https://huggingface.co/papers/2610.11322)

Geometrically faithful and functional articulated 3D assets are essential for real-to-sim robot manipulation, where policies trained in simulation must transfer to physical objects. Recent mesh-based methods learn to infer articulation from annotated 3D assets, but deployment remains challenging when real-world objects fall outside the training distribution or their meshes are incomplete or corrupted. To address…

## 40. Do LLMs Understand Sequential Structure? A Controlled Study of Inference and Generation

- 分数：18.5  ·  HF 赞：9  ·  来源：huggingface
- 兴趣命中：agent, language model, large language
- 作者：Jerry Wang, Zhengxiang Wang, Ting Yu Liu, Hsin-Ling Hsu, Yi-Cheng Lai, Tengfei Ma
- 链接：[arXiv](https://arxiv.org/abs/2610.04977) · [PDF](https://arxiv.org/pdf/2610.04977) · [HF](https://huggingface.co/papers/2610.04977)

Large language models (LLMs) are increasingly used as interactive agents and simulators, yet it remains unclear whether they can recover latent sequential structure beyond surface action frequencies. This distinction is critical for behavioral simulation, where actions are often shaped by prior context rather than marginal frequencies alone. We study this question using controlled two-player Rock--Paper--Scissors…

## 41. V-CoLA: Vision Token Compression with Linear Attention

- 分数：18.5  ·  HF 赞：9  ·  来源：huggingface
- 兴趣命中：benchmark, language model, spec
- 作者：Hao Jiang, Yiru Mao, Tianpeng Bu, Hao Zhou, Hongtao Duan, Wang Jing, Bowen Xu, Xin Chen, Lulu Hu, Bin Yang, Yongliang Tao, Minying Zhang
- 链接：[arXiv](https://arxiv.org/abs/2610.11251) · [PDF](https://arxiv.org/pdf/2610.11251) · [HF](https://huggingface.co/papers/2610.11251)

Vision-language models (VLMs) have demonstrated impressive capabilities but suffer from substantial computational overhead, as vision tokens dominate the input sequence. This motivates vision token compression as a key direction to alleviate the burden. However, with the emergence of hybrid architectures incorporating linear attention (\eg, Qwen3.5), prior methods designed for softmax attention struggle to…

## 42. REMORY: Learning Residual Memory for Context Compaction

- 分数：18.5  ·  HF 赞：5  ·  来源：huggingface
- 兴趣命中：agent, memory, context window, benchmark
- 作者：Hanchen Xia, Baoyou Chen, Yutang Ge, Naihao Deng, Senqiao Yang, Zilong Dong, Weihao Yuan, Siyu Zhu
- 链接：[arXiv](https://arxiv.org/abs/2610.11287) · [PDF](https://arxiv.org/pdf/2610.11287) · [HF](https://huggingface.co/papers/2610.11287)

Long-horizon agents compact their history to continue within a finite context window, but a textual summary alone may not support every subsequent decision. We introduce REMORY, a neural memory network that supplements the summary with a bounded sequence of soft memory tokens. Given the history and summary, the network learns to generate tokens that help a frozen LLM approximate the continuation it would produce…

## 43. ReSPO: Reshaped Sequence Policy Optimization for Gradient Starvation in Off-Policy Learning

- 分数：18.0  ·  HF 赞：8  ·  来源：huggingface
- 兴趣命中：reasoning, reinforcement learning, benchmark
- 作者：Yihang Chen, Yuanhao Ban, Cho-Jui Hsieh
- 链接：[arXiv](https://arxiv.org/abs/2609.35433) · [PDF](https://arxiv.org/pdf/2609.35433) · [HF](https://huggingface.co/papers/2609.35433)

Reinforcement learning from verifiable rewards (RLVR) frequently reuses rollouts across multiple policy updates, increasing the mismatch between the current policy and the data-generating policy. We identify a sign-dependent gradient starvation problem in clipped policy optimization: clipping suppresses under-generated positive responses at the low-importance-weight tail while permitting severely over-generated…

## 44. WorldGuide: Goal-Directed Video World Model for Procedural Task Execution

- 分数：18.0  ·  HF 赞：4  ·  来源：huggingface + arxiv
- 兴趣命中：memory, planning
- 作者：Ankan Deria, Komal Kumar, Hisham Cholakkal, Fahad Shahbaz Khan, Salman Khan
- 链接：[arXiv](https://arxiv.org/abs/2610.12459) · [PDF](https://arxiv.org/pdf/2610.12459) · [HF](https://huggingface.co/papers/2610.12459)

Video generators and video-based world models can synthesize plausible visual trajectories, but long-horizon procedural tasks require generation to adapt to what has actually been produced. A model must determine the next action from its generated state, execute that action, and recognize when the task is complete. Open-loop generation cannot adapt to execution outcomes, while existing closed-loop systems often rely…

## 45. Investigating the Role of Reasoning-Language Alignment in Monolingual Retrieval-Augmented Generation

- 分数：17.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：agent, memory, reasoning, benchmark, language model, large language, retrieval
- 作者：Oliver Hauck, Mario Sanz-Guerrero, Katharina von der Wense
- 链接：[arXiv](https://arxiv.org/abs/2610.03136) · [PDF](https://arxiv.org/pdf/2610.03136) · [HF](https://huggingface.co/papers/2610.03136)

Reasoning traces improve large language models (LLMs), but current models are trained to reason mostly in English. It has been shown that forcing a model to reason in another language degrades accuracy, even when the reasoning language matches the language of the prompt -- but only for a setting where the model reasons over a short prompt. Here, we ask whether the same holds for retrieval-augmented generation (RAG),…

## 46. Frozen Models, Evolving Expertise: Model-Agnostic Learning from Deployment Experience for Multimodal Medical AI

- 分数：17.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：tool use, memory, reasoning, benchmark, language model, large language, spec
- 作者：Yexiao He, Yucheng Tang, Pengfei Guo, Yufan He, Andriy Myronenko, Can Zhao, Ang Li, Daguang Xu, Dong Yang
- 链接：[arXiv](https://arxiv.org/abs/2610.09146) · [PDF](https://arxiv.org/pdf/2610.09146) · [HF](https://huggingface.co/papers/2610.09146)

Large language models (LLMs) and vision-language models (VLMs) are usually frozen after deployment, so they do not learn from the cases they solve. This is especially concerning in medicine, where new clinical evidence, updated guidelines, and new therapies can change established practice. Fine-tuning can update the model, but it requires access to model weights and additional training. Parameter-free methods avoid…

## 47. SpecFold: Folding Multi-Branch Redundancy for Faster Speculative Decoding in Diffusion Language Models

- 分数：17.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：benchmark, language model, large language, coding, spec
- 作者：Chung-En Ho, Weiyu Sun, Cheng-Jhih Shih, He Li, Yong Liu, Yingyan Celine Lin
- 链接：[arXiv](https://arxiv.org/abs/2610.04875) · [PDF](https://arxiv.org/pdf/2610.04875) · [HF](https://huggingface.co/papers/2610.04875)

Diffusion large language models (DLLMs) generate text through iterative block denoising, and multi-branch speculative decoding accelerates this process by verifying a main branch together with multiple draft branches in a single forward pass. While prior DLLM acceleration methods primarily exploit temporal redundancy across denoising steps, we identify a complementary redundancy axis within each speculative…

## 48. Learning to Steer, Steering to See: Unveiling the Geometry of RLVR in Large Language Models via Trainable Vectors

- 分数：16.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：reasoning, reinforcement learning, language model, large language
- 作者：Yuchen Cai, Ding Cao, Qixiang Yin, Xin Xu, Kai Yang, Siye Wu, Pengyuan Wang, Jiaxuan Wang, Weijie Liu, Saiyong Yang, Guangzhong Sun, Guiquan Liu, Junfeng Fang
- 链接：[arXiv](https://arxiv.org/abs/2609.34344) · [PDF](https://arxiv.org/pdf/2609.34344) · [HF](https://huggingface.co/papers/2609.34344)

Reinforcement learning (RL) has become a key paradigm for enhancing the reasoning of large language models, yet the high dimensionality of parameter updates makes its training dynamics hard to analyze. We study reinforcement learning with verifiable rewards (RLVR) and use vector steering to identify a low-dimensional effective manifold in activation space associated with RL-induced gains. We uncover two geometric…

## 49. Incidental information contaminates patient notes and disrupts clinical reasoning in large language models

- 分数：16.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：reasoning, language model, large language, coding
- 作者：Krithik Vishwanath, Brandon Ye, Anton Alyakin, John E. Markert, Aaron Hsieh, Michał Mańkowski, Eric K. Oermann
- 链接：[arXiv](https://arxiv.org/abs/2610.08585) · [PDF](https://arxiv.org/pdf/2610.08585) · [HF](https://huggingface.co/papers/2610.08585)

Large language models (LLMs) are increasingly relied upon to support ambient documentation and clinical reasoning. Here we examine the impact of a failure mode shared between these two applications by assessing their sensitivity to information incidental to the patient encounter. In 576 patient-clinician dialogues, we found that frontier models inserted small-talk exchanges into 35% of notes, while mean quality…

## 50. MARGIN: Runtime Confidence Calibration for Multi-Agent Foundation Model Coordination

- 分数：16.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark, spec
- 作者：Joss Armstrong
- 链接：[arXiv](https://arxiv.org/abs/2605.22949) · [PDF](https://arxiv.org/pdf/2605.22949) · [HF](https://huggingface.co/papers/2605.22949)

When a coordinator compares answers from heterogeneous foundation models, self-reported confidence may have different meanings across responders and changing workloads. This paper presents MARGIN (Multi-Agent Runtime Grading via Incremental Normalisation), a runtime calibration method that learns model-specific confidence corrections from observed answer outcomes without retraining the models or requiring a held-out…

## 51. Retrieval-Centric Deep Learning in Growing Nonparametric Neural Networks

- 分数：16.0  ·  HF 赞：8  ·  来源：huggingface
- 兴趣命中：spec, retrieval
- 作者：Maximilian Schlegel, Rajai Nasser, Seijin Kobayashi, Yanick Schimpf, Oliver Sieberling, Robert Obryk, Kazuki Irie, João Sacramento, Johannes von Oswald
- 链接：[arXiv](https://arxiv.org/abs/2610.03858) · [PDF](https://arxiv.org/pdf/2610.03858) · [HF](https://huggingface.co/papers/2610.03858)

We investigate a general-purpose layer for deep learning that, instead of compressing arbitrary-size training data into fixed-size weight matrices, stores a new pair of key-value representations for every data point during training, and retrieves and recombines these representations through an attention mechanism at inference time - resulting in a growing neural net (NN). While Irie et al. (arXiv:2202.05798) have…

## 52. SatNav: A Scalable Benchmark for Long-Horizon UAV Vision-Language Navigation from Satellite Imagery

- 分数：16.0  ·  HF 赞：0  ·  来源：huggingface
- 兴趣命中：agent, memory, reasoning, benchmark, language model
- 作者：Jiajun Jiang, Chunliang Hua, Zichun Chen, Yanxing Wu, Zeyuan Yang, Jie Song, Xiao Hu
- 链接：[arXiv](https://arxiv.org/abs/2609.31507) · [PDF](https://arxiv.org/pdf/2609.31507) · [HF](https://huggingface.co/papers/2609.31507)

Urban uncrewed aerial vehicle (UAV) vision-language navigation (VLN) requires agents to follow instructions across extended urban spaces, inherently demanding long-term memory and geospatial grounding. However, scaling existing benchmarks remains difficult because of their reliance on costly reconstructed 3D assets, limiting geographic diversity and episode scale. To address this, we introduce SatNav, a scalable,…

## 53. MIRA: A Musical Intent Refinement Agent for Aligning Text-to-Music Generation with User Intent

- 分数：16.0  ·  HF 赞：0  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark, spec
- 作者：Zekai Liu, Zhilin Wang, Xuzheng He, Yu Cheng, Yang Yang
- 链接：[arXiv](https://arxiv.org/abs/2610.10355) · [PDF](https://arxiv.org/pdf/2610.10355) · [HF](https://huggingface.co/papers/2610.10355)

Text-to-music systems produce increasingly convincing audio, yet evaluation reveals little about whether the result matches user intent. A global text-audio relevance score can overlook the implicit intent in underspecified prompts and mask failures in specific requirements, such as instrumentation, structure, rhythm, or mood progression. To bridge this gap, we formulate text-to-music intent alignment as satisfying…

## 54. One Block, Multiple Depths: Recurrent Vision Transformers with Depth-Programmed Experts

- 分数：15.5  ·  HF 赞：3  ·  来源：huggingface + arxiv
- 兴趣命中：spec
- 作者：Adrian Bulat, Yassine Ouali, Georgios Tzimiropoulos
- 链接：[arXiv](https://arxiv.org/abs/2610.12448) · [PDF](https://arxiv.org/pdf/2610.12448) · [HF](https://huggingface.co/papers/2610.12448)

In this work, we show that a single Transformer block, applied recurrently, can match the accuracy of a full-depth vision encoder at comparable inference FLOPs without intermediate feature distillation. reViT restores depth-specific transformations by representing the FFN at each recurrent depth as a convex combination of a small shared expert bank. A continuous normalized-depth coordinate programs this mixture,…

## 55. SpaceFlow: Locally Controllable 3D Generation

- 分数：15.5  ·  HF 赞：3  ·  来源：huggingface + arxiv
- 兴趣命中：spec
- 作者：Neil De La Fuente, Joan Lafuente, Mukhammadali Sayfiddinov, Felicia Scharitzer, Marc Pollefeys, Ata Celen, Sayan Deb Sarkar, Elisabetta Fedele
- 链接：[arXiv](https://arxiv.org/abs/2610.12399) · [PDF](https://arxiv.org/pdf/2610.12399) · [HF](https://huggingface.co/papers/2610.12399)

Current 3D generation methods lack explicit local control: geometric adherence is often defined by a global control strength, and appearance cannot be specified locally. We present SpaceFlow, a training-free pipeline for locally controllable 3D generation from text descriptions and a collection of geometric primitives. Each primitive serves as a proxy for an object part and is assigned a local control level,…

## 56. You Changed Your Mind, The Model Didn't: Demystifying Intent in Multi-Turn Dialogue

- 分数：15.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：benchmark, language model, large language
- 作者：Junle Chen, Wei Chen, Zhengjun Huang, Zhoujin Tian, Yuxuan Liu, Kai Wang, Rui Chen, Xiaofang Zhou
- 链接：[arXiv](https://arxiv.org/abs/2610.06496) · [PDF](https://arxiv.org/pdf/2610.06496) · [HF](https://huggingface.co/papers/2610.06496)

When a large language model handles a multi-turn task and a user proposes a change but ultimately rejects it, the model should continue as if nothing changed. We find a surprising failure: merely mentioning a rejected change can derail task execution, even when the user's final intent remains unchanged. To systematically study language model behavior under evolving user intent, we introduce Intent-Eval, a controlled…

## 57. CARE: Certifying Acceleration for Vision-Language-Action Inference

- 分数：15.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：agent, evaluation, spec
- 作者：Rui Liu, Tong Zheng, Jindong Gu, Zhipeng Wang
- 链接：[arXiv](https://arxiv.org/abs/2610.08917) · [PDF](https://arxiv.org/pdf/2610.08917) · [HF](https://huggingface.co/papers/2610.08917)

While vision-language-action (VLA) models have advanced rapidly, running them at every control step remains expensive. Prior work accelerates VLA inference using techniques like action chunking and visual-token pruning, typically evaluating based on latency and average task success. However, acceleration may discard information and break tasks the original policy would solve, a risk hidden by average metrics.…

## 58. On-Policy Distillation Teaches New Skills but Not New Knowledge

- 分数：15.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：memory, reasoning, spec
- 作者：Yixuan Tang, Yi Yang
- 链接：[arXiv](https://arxiv.org/abs/2610.09639) · [PDF](https://arxiv.org/pdf/2610.09639) · [HF](https://huggingface.co/papers/2610.09639)

On-policy distillation (OPD) strengthens language-model reasoning, yet whether students acquire new factual knowledge or compositional skill for multi-step reasoning remains unknown. We separate these capabilities using a controlled synthetic framework that measures the student's initial capabilities and independently controls the teacher's additional facts, compositional skill, or both. Across four models from…

## 59. Can AI Agents Make Open-Ended Scientific Discovery? Evidence from Station

- 分数：14.5  ·  HF 赞：5  ·  来源：huggingface
- 兴趣命中：agent, spec
- 作者：Wenyu Du, Stephen Chung
- 链接：[arXiv](https://arxiv.org/abs/2610.08927) · [PDF](https://arxiv.org/pdf/2610.08927) · [HF](https://huggingface.co/papers/2610.08927)

Recent AI systems have made rapid progress in scientific discovery when given well-defined metrics, but whether they can autonomously undertake open-ended scientific discovery remains unclear. We investigate AI's ability to tackle open-ended tasks in Station, an open-world environment in which multiple agents simulate a scientific ecosystem. To tackle challenges specific to open-ended tasks, we propose augmenting…

## 60. Chaos in the Text: Revealing the Modality Preference in Mixed-Modality Retrievers

- 分数：14.5  ·  HF 赞：5  ·  来源：huggingface
- 兴趣命中：benchmark, retrieval
- 作者：Yubo Sun, Chunyi Peng, Yukun Yan, Zhenghao Liu, Zhipeng Xu, Sen Mei, Linlin Xin, Zheni Zeng, Maosong Sun
- 链接：[arXiv](https://arxiv.org/abs/2610.11816) · [PDF](https://arxiv.org/pdf/2610.11816) · [HF](https://huggingface.co/papers/2610.11816)

Dense retrievers have made significant progress on text and image corpora, but whether these capabilities extend reliably to mixed corpora containing text, image, and fused text-image documents remains unclear. In this paper, we systematically examine retrievers across architectures and find that their performance is highly sensitive to modality composition. As image documents are progressively replaced with…

## 61. Scaling to Tens of Thousands of Test-Time Iterations with Loop-Native Attention Residuals

- 分数：14.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：memory, reasoning
- 作者：Pengxiang Li, Dilxat Muhtar, Di He, Guinan Su, Lu Yin, Shiwei Liu
- 链接：[arXiv](https://arxiv.org/abs/2610.11570) · [PDF](https://arxiv.org/pdf/2610.11570) · [HF](https://huggingface.co/papers/2610.11570)

In this paper, we argue that looped Transformers need their own residual connections to prevent performance degradation as the number of iterations grows. We observe that increasing loop iterations can reduce reasoning accuracy: noisy state updates overwrite correct intermediate deductions and even undo completed solutions. This leaves subsequent iterations to recover lost information from an already degraded…

## 62. SPW-Nav: A Streaming Panoramic World Model for Language-Guided Navigation

- 分数：14.0  ·  HF 赞：0  ·  来源：huggingface
- 兴趣命中：agent, memory, spec
- 作者：Yunheng Liu, Ziqi Cai, Siqi Yang, Yimu Wang, Minggui Teng, Jiaming Tan, Shuchen Weng, Erwin Wu, Kaipeng Zhang, Boxin Shi
- 链接：[arXiv](https://arxiv.org/abs/2610.08941) · [PDF](https://arxiv.org/pdf/2610.08941) · [HF](https://huggingface.co/papers/2610.08941)

Language-guided panoramic video generation benefits various downstream applications, such as interactive 3D scene exploration, virtual reality experiences, and embodied agent training. Existing panoramic generators follow predefined trajectories, and interactive world models act through low-level actions in perspective views. We propose SPW-Nav, a streaming panoramic world model that understands movement…

## 63. The Lattice of Transition Laws

- 分数：14.0  ·  HF 赞：0  ·  来源：huggingface
- 兴趣命中：benchmark, coding, spec
- 作者：T. Y. Tsui, Jiatao Gu, Lingjie Liu
- 链接：[arXiv](https://arxiv.org/abs/2610.11216) · [PDF](https://arxiv.org/pdf/2610.11216) · [HF](https://huggingface.co/papers/2610.11216)

Diffusion and autoregression (AR) have long been seen as different categories of generative models, with diffusion specialising in continuous fields and AR specialising in discrete tokens. Recent work seeks to combine the advantages of the two models, and each hybrid fixes its decoding schedule by design. In this paper, we ask whether the performance of decoding schedules of one model can be predicted before…

## 64. Mara Chain: Rethinking Failure as a Stepping Stone for AI System Auto-Evolution

- 分数：13.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：spec, retrieval
- 作者：Yubin Lyu, Fu Li, Jiawei Fei, Yang Zhao, Weixing Mei, Yinan Wu
- 链接：[arXiv](https://arxiv.org/abs/2609.35855) · [PDF](https://arxiv.org/pdf/2609.35855) · [HF](https://huggingface.co/papers/2609.35855)

Optimizing deployed AI systems increasingly amounts to editing prompts, skills, harnesses, and code rather than model weights. Existing approaches commonly optimize these artifacts through propose-evaluate-select procedures, where candidate configurations are evaluated and only those meeting an acceptance criterion are selected. Yet our analysis shows that discarded candidates often contain information critical for…

## 65. Incremental Open-Ended Deep Research with Structured Harness

- 分数：13.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：evaluation, retrieval
- 作者：Meilin Chen, Hongyuan Bao
- 链接：[arXiv](https://arxiv.org/abs/2610.11566) · [PDF](https://arxiv.org/pdf/2610.11566) · [HF](https://huggingface.co/papers/2610.11566)

Existing Open-Ended Deep Research (OEDR) systems primarily generate reports from scratch, making them inefficient for scenarios where research reports need to be continuously maintained as new information emerges. We introduce Incremental Open-Ended Deep Research (Incremental-OEDR), a research setting that treats a report as an evolving research state and incrementally updates it by preserving valid knowledge,…

## 66. Skill Constellations: Tracing the Supply Chain of Agent Skills on GitHub

- 分数：12.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：agent, coding
- 作者：Fahd Seddik
- 链接：[arXiv](https://arxiv.org/abs/2610.11169) · [PDF](https://arxiv.org/pdf/2610.11169) · [HF](https://huggingface.co/papers/2610.11169)

Agent skills are SKILL.md instructions and scripts that AI coding agents such as Claude Code and Codex run with the permissions of their user. Developers share skills by copying them between repositories, which makes them a software supply chain without a registry, versions or provenance. The origin of a copied skill, the reach of a security fix and the repositories that warrant review are therefore unknown. Studies…

## 67. Behavioral Persistence and Incomplete Functional Transfer of Co-evolved Communication in Evolutionary Robotics

- 分数：12.0  ·  HF 赞：0  ·  来源：huggingface
- 兴趣命中：agent, spec
- 作者：Fernando Montes-Gonzalez
- 链接：[arXiv](https://arxiv.org/abs/2609.38527) · [PDF](https://arxiv.org/pdf/2609.38527) · [HF](https://huggingface.co/papers/2609.38527)

This work evaluates the direct transfer of a co-evolved communication protocol from a 2D simulation to a 3D physical environment, without retraining the network weights. Two e-puck-type robots, controlled by a GRU network with residual connection, were evaluated in a food-seeking task with social signaling. The sensory and motor translation layer required three corrections for stable physical operation, including…

## 68. TerraVis: Towards Evaluation of World-Grounded Visual Consistency in Text-to-Image Generation via MLLM Workflows

- 分数：12.0  ·  HF 赞：0  ·  来源：huggingface
- 兴趣命中：evaluation, benchmark
- 作者：Shuai Fu, Jing Gu, Jian Zhou, Zicheng Duan, Gengze Zhou, Qi Wu
- 链接：[arXiv](https://arxiv.org/abs/2610.02959) · [PDF](https://arxiv.org/pdf/2610.02959) · [HF](https://huggingface.co/papers/2610.02959)

Recent text-to-image models have made substantial progress in photorealism, aesthetics, and text-image alignment. Yet visually appealing images can still violate real-world plausibility, exhibiting malformed object structures, impossible anatomy, physically implausible interactions, or inconsistent spatial relationships. Such failures are not well captured by existing fidelity, aesthetics, preference, or alignment…

## 69. Evaluating the Transfer of Co-Evolved Communication from 2D to 3D Simulation

- 分数：12.0  ·  HF 赞：0  ·  来源：huggingface
- 兴趣命中：agent, evaluation
- 作者：Fernando Montes-Gonzalez
- 链接：[arXiv](https://arxiv.org/abs/2610.09280) · [PDF](https://arxiv.org/pdf/2610.09280) · [HF](https://huggingface.co/papers/2610.09280)

This work examines the transfer of a co-evolved communication mechanism between two robotic agents from a discrete two-dimensional (2D) simulator to a three-dimensional simulator with real physics (3D). The study focuses on whether a communication mechanism co-evolved in a 2D environment retains its functional role after transfer to a 3D physics-based simulator. To support this analysis, the effects of the episode…

## 70. Synthesis Through Simulation: Generating Coherent Enterprise Data via Scalable Agent-System Interaction

- 分数：11.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：agent
- 作者：Yipeng Li, Ashutosh Hathidara, Jane Lo, Harshavardhan Abichandani, Gunraj Singh, Atin Ghosh
- 链接：[arXiv](https://arxiv.org/abs/2610.10549) · [PDF](https://arxiv.org/pdf/2610.10549) · [HF](https://huggingface.co/papers/2610.10549)

Tool-calling agents have become central to enterprise AI, yet training and evaluating them at scale remains severely constrained due to business and legal restrictions on enterprise systems, data, and database schemas. Tabular data synthesis offers a natural alternative, but its effectiveness is fundamentally limited by structural validity and schema availability, while procedure-based approaches yield the opposite…

## 71. EDiS: Edge Disjoint Subgraph Sparsification Framework for Graph Neural Networks

- 分数：11.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：benchmark
- 作者：Sai Karthik Navuluru, Siddhartha Shankar Das, Franck Dernoncourt, S M Ferdous, Ryan A. Rossi, Nesreen K. Ahmed, Baris Coskunuzer, Alex Pothen, Lakshman Tamil, Mahantesh M Halappanavar
- 链接：[arXiv](https://arxiv.org/abs/2610.09059) · [PDF](https://arxiv.org/pdf/2610.09059) · [HF](https://huggingface.co/papers/2610.09059)

Sparse GNN training reduces computation, but deciding which edges to keep can be costly. Reusing one sparse graph is cheap, but locks training to a fixed topology, while varying it across epochs can require repeated sampling or recomputation. We introduce EDiS (Edge-Disjoint Subgraph sparsification framework), which separates one-time structural extraction from per-epoch graph composition. EDiS decomposes the graph…

## 72. Safe Actions Alone Do Not Ensure Safe Agents: Identifying Unfulfilled Obligations with Guard Models

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, evaluation, benchmark, spec
- 作者：Youwei Feng, Yitong Zhang, Yuetong Liu, Jia Li
- 链接：[arXiv](https://arxiv.org/abs/2610.11773) · [PDF](https://arxiv.org/pdf/2610.11773) · [HF](https://huggingface.co/papers/2610.11773)

Guard models are increasingly used to safeguard LLM-based agents, primarily by identifying actions that agents are forbidden to perform. However, identifying forbidden actions alone is insufficient to ensure agent safety. In this paper, we argue that agent safety also depends on identifying required yet unperformed safety-critical actions, which we call obligations. Our preliminary study on a popular benchmark for…

## 73. Seek-and-View Reasoning for Multi-View Spatial Understanding

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, benchmark, language model, planning
- 作者：Qixiang Chen, Cheng Zhang, Fucai Ke, Chi-Wing Fu, Jianfei Cai, Jingwen Ye
- 链接：[arXiv](https://arxiv.org/abs/2610.11810) · [PDF](https://arxiv.org/pdf/2610.11810) · [HF](https://huggingface.co/papers/2610.11810)

Existing approaches to multi-view spatial reasoning operate largely on sparse input views. Vision-language models (VLMs) are thus restricted to understand a scene and infer spatial relations within these fixed views, leading to fragile cross-view alignment and geometry-to-language bottleneck. To address these issues, we formulate a novel Seek-and-View reasoning approach to find implicit cross-view spatial evidence…

## 74. GRPODropout: Less is More for Online Reinforcement Learning Rollouts

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, reinforcement learning, language model, large language, spec
- 作者：Hexuan Deng, Zihao Yan, Xuebo Liu, Shuo Nie, Yue Wang, Chen Wang, Zhaohua Zhang, Tianwen Jiang, Qiuyong Xiao, Jihong Zhang, Min Zhang
- 链接：[arXiv](https://arxiv.org/abs/2610.11854) · [PDF](https://arxiv.org/pdf/2610.11854) · [HF](https://huggingface.co/papers/2610.11854)

Reinforcement learning (RL) methods such as GRPO substantially improve large language model reasoning but often suffer from policy entropy collapse: the loss of sampling diversity weakens exploration and limits further improvement. Existing methods address this issue either through algorithm-level interventions, such as reward modification and entropy/KL regularization, or through token-level reweighting. We…

## 75. Automated Assembly Instruction Generation from CAD Models Using Grounded Large Language Models: A Human-in-the-Loop Framework

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, language model, large language, planning
- 作者：Aaron Dsouza, Mohammed Azeez Khan, Ashutosh Mishra, Arshaan Khan, Neha K. Nair, Amar Kumar Behera
- 链接：[arXiv](https://arxiv.org/abs/2610.11896) · [PDF](https://arxiv.org/pdf/2610.11896) · [HF](https://huggingface.co/papers/2610.11896)

Assembly documentation is a downstream manufacturing artifact that is still usually authored by interpreting CAD models by hand. Structured product data and large language models are both available, yet studies of CAD interpretation, assembly sequence planning, instruction writing, and human oversight have largely proceeded separately. This paper formulates CAD-grounded assembly instruction generation: the…

## 76. Forms of LLM-Integrated Applications from LLM-Chats to Autonomous AI Agent System

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, tool use, language model, large language, coding, retrieval
- 作者：Irene Weber
- 链接：[arXiv](https://arxiv.org/abs/2610.11899) · [PDF](https://arxiv.org/pdf/2610.11899) · [HF](https://huggingface.co/papers/2610.11899)

Large language models (LLMs) are increasingly embedded as components in software systems, marketed under labels such as chatbot, copilot, retrieval-augmented generation, workflow, coding agent and AI agent. Whether these labels denote genuine architectural forms or serve as branding has not been assessed systematically. In the sources surveyed, labels do carry architectural content, most clearly in vendor usage:…

## 77. From Surface to Depth: Towards Cognitive Appraisal Reasoning in Multimodal Emotion Understanding

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, benchmark, language model, large language, spec
- 作者：Jia Li, Yichao He, Yangchen Yu, Qiankun Li, Xinyi Li, Baiyi Ye, Zhenzhen Hu, Richang Hong, Erik Cambria
- 链接：[arXiv](https://arxiv.org/abs/2610.11918) · [PDF](https://arxiv.org/pdf/2610.11918) · [HF](https://huggingface.co/papers/2610.11918)

Recent multimodal large language models (MLLMs) increasingly incorporate explainable reasoning for emotion understanding. However, reasoning based mainly on observable affective cues can reduce emotion understanding to superficial cue-label associations, giving rise to the Clever Hans effect. Such shortcuts become unreliable when affective cues are implicit, conflicting across modalities, linguistically misleading,…

## 78. Event-Centric Memory with Query-Aware Graph Augmentation for Long-Term Conversational Agents

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, memory, reasoning, benchmark, retrieval
- 作者：Yichen Liu, Chunfeng Yuan, Haowei Liu, Wenjuan Li, Zefeng Lin, Bing Li, Xu Chen, Weiming Hu
- 链接：[arXiv](https://arxiv.org/abs/2610.11920) · [PDF](https://arxiv.org/pdf/2610.11920) · [HF](https://huggingface.co/papers/2610.11920)

For persistent and personalized conversational agents, memory systems can enable them to remember, update, and reason over long histories by storing past interactions and retrieving relevant information. Existing memory systems typically follow two paradigms: flat-structured memory and graph-based memory. The former is lightweight but leaves event relations and state updates implicit, while the latter explicitly…

## 79. Can LLMs Fix It Without Code? Toward Automated Verification of No-Code Bug Fixes

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, evaluation, benchmark, language model, large language, spec
- 作者：Utku Boran Torun, Veli Karakaya, Eray Tüzün
- 链接：[arXiv](https://arxiv.org/abs/2610.11963) · [PDF](https://arxiv.org/pdf/2610.11963) · [HF](https://huggingface.co/papers/2610.11963)

A no-code fix resolves an invalid bug report by directing the user to change a setting, update to a version where the problem is already fixed, or adjust their workflow. Manually verifying whether a proposed no-code fix resolves the reported bug takes considerable developer time. This study proposes an automated, execution-based pipeline for evaluating the capability of large language models (LLMs) to generate…

## 80. CAPABLE: Capability-Aware Policy Adaptation via Behavioral Latent Encoding

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reinforcement learning, evaluation, coding, spec
- 作者：Mohammad Khoshnazar, Mohammad Dehghani Tezerjani, Deyuan Qu, Zhiyuan Gao, Yanxiang Zhan, Jeroen Schafer, Andrew Melnik, Qing Yang, Michael Beetz
- 链接：[arXiv](https://arxiv.org/abs/2610.11971) · [PDF](https://arxiv.org/pdf/2610.11971) · [HF](https://huggingface.co/papers/2610.11971)

Vision-language-action (VLA) policies assume the embodiment on which they were trained and can fail when a joint fault changes how commanded actions are physically executed. Existing fault-recovery methods often require task-specific retraining, fault labels, explicit diagnosis, or privileged embodiment information. We introduce CAPABLE, a unified capability-aware adaptation framework for frozen VLAs that integrates…

## 81. Specialized Decision Models vs. General-Purpose LLMs: Benchmarking Jev Across Knowledge, Reasoning, and Multilingual Tasks

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, benchmark, language model, large language, spec
- 作者：Xing Li, Qingcheng Chang, Jinzhong Ning, Changfeng Xu, Shenlong Zhang, Yijia Zhang, Ling Luo, Hongfei Lin
- 链接：[arXiv](https://arxiv.org/abs/2610.11978) · [PDF](https://arxiv.org/pdf/2610.11978) · [HF](https://huggingface.co/papers/2610.11978)

Jev is a "System One" model that returns a choice among given options instead of generating text. We study how such a specialized decision model compares with general-purpose large language models (LLMs). We evaluate Jev on 13 multiple-choice benchmarks covering knowledge, reasoning, and multilingual understanding, and compare it with 19 LLMs in three tiers: frontier, representative, and small. Jev is competitive…

## 82. Test-Time Compute for Tabular Foundation Models: Mechanisms, Gains, and Limits

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, evaluation, benchmark, retrieval
- 作者：Kanghui Ning, Marin Biloš, James T. Wilson, Yilang Zhang, Kashif Rasul, Dongjin Song, Anderson Schneider, Yuriy Nevmyvaka
- 链接：[arXiv](https://arxiv.org/abs/2610.12005) · [PDF](https://arxiv.org/pdf/2610.12005) · [HF](https://huggingface.co/papers/2610.12005)

Which forms of test-time compute improve the predictions of strong pretrained tabular foundation models (TFMs)? We systematically study this along three axes: adaptation, aggregation, and context construction. Our evaluation spans modern TFMs across the TabArena benchmark, supplemented by experiments on wide and large-scale tables from OpenML. For adaptation, we introduce DiagScale, a diagonal query-key similarity…

## 83. Examining Social Attribution in LLM Reasoning: A Theory-Guided Probing Methodology

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reasoning, benchmark, language model, large language, spec
- 作者：Zhaoxin Yu, Qingchao Kong, Dajun Zeng, Wenji Mao
- 链接：[arXiv](https://arxiv.org/abs/2610.12022) · [PDF](https://arxiv.org/pdf/2610.12022) · [HF](https://huggingface.co/papers/2610.12022)

Large language models (LLMs) are increasingly deployed in sociotechnical systems where social attribution, the reasoning process attributing external events to the causes and reasons of agents' social behaviors, plays a critical role. These processes involve judgments of social cause, responsibility, and blame/credit to agents. Although attributional models are well-studied in social psychology and cognition through…

## 84. Natural Language to First-Order Logic LLM-based Autoformalization

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, language model, large language
- 作者：Andrea Brunello, Cristian Curaba, Luca Geatti, Michele Mignani, Angelo Montanari, Nicola Saccomanno
- 链接：[arXiv](https://arxiv.org/abs/2610.12030) · [PDF](https://arxiv.org/pdf/2610.12030) · [HF](https://huggingface.co/papers/2610.12030)

Large Language Models (LLMs) have renewed interest in autoformalization. Yet, when First-Order Logic (FOL) is considered as the target formalism, the field still lacks a unified task formulation and a systematic survey. This paper addresses this gap: we first provide a principled definition for the FOL-autoformalization task by distinguishing Ontology Extraction from Logical Translation, showing how their conflation…

## 85. Look Back, Think Ahead: Visual Memory on Demand for Efficient Multimodal Reasoning

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, reasoning, benchmark, language model, large language, coding, spec
- 作者：Yicheng Xue, Han Wu, Jufeng Yang, Minjing Dong, Xinghao Chen, Hanting Chen, Jianyuan Guo
- 链接：[arXiv](https://arxiv.org/abs/2610.12060) · [PDF](https://arxiv.org/pdf/2610.12060) · [HF](https://huggingface.co/papers/2610.12060)

Processing long visual token sequences from high-resolution images makes multi-step reasoning computationally expensive for multimodal Large Language Models (MLLMs). Existing one-shot pruning and aggregation methods compress visual tokens into a fixed context before decoding. However, visual evidence needs can shift as reasoning unfolds, making it difficult for a fixed compressed context to retain all the details…

## 86. When Should Agents Think? Adaptive Reasoning via Cross-Turn Estimation

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reasoning, reinforcement learning, benchmark, language model, large language
- 作者：Yiruo Cheng, Shen Huang, Xiaoshuai Song, Jiejun Tan, Guanting Dong, Pengjun Xie, Ji-Rong Wen, Zhicheng Dou
- 链接：[arXiv](https://arxiv.org/abs/2610.12061) · [PDF](https://arxiv.org/pdf/2610.12061) · [HF](https://huggingface.co/papers/2610.12061)

Large language model (LLM)-based agents have demonstrated strong capabilities on complex tasks. They typically perform reasoning before each action throughout an interaction trajectory. However, reasoning may not be necessary at every turn, as reasoning produced earlier can continue to support subsequent actions. A key challenge is therefore to determine when existing reasoning remains sufficient and when a new…

## 87. Is Memorization Context-Sensitive? Prefix-Based Extraction Beyond Isolated Prefixes

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, language model, large language, spec, retrieval
- 作者：Ali Satvaty, Narjes Sharafi, Jirui Qi, Suzan Verberne, Fatih Turkmen
- 链接：[arXiv](https://arxiv.org/abs/2610.12085) · [PDF](https://arxiv.org/pdf/2610.12085) · [HF](https://huggingface.co/papers/2610.12085)

Large language models (LLMs) can expose memorized training sequences under prefix-based extraction: given a prefix from a training example, the model may assign high probability to the original continuation. In deployed systems, however, prefixes are rarely evaluated in isolation. They often appear together with instructions, retrieved documents, or other task-specific context, as in retrieval-augmented generation…

## 88. EvoAlloc: A Self-Evolving Resource Allocation Agent for Efficient Program Evolution

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, evaluation, benchmark, coding
- 作者：Yanning Dai, Yuhui Wang, Nanbo Li, Wenyi Wang, Jürgen Schmidhuber
- 链接：[arXiv](https://arxiv.org/abs/2610.12086) · [PDF](https://arxiv.org/pdf/2610.12086) · [HF](https://huggingface.co/papers/2610.12086)

LLM-based program evolution relies on evaluation feedback to guide the iterative search for high-performing programs. However, evaluation is often computationally expensive, making it essential to allocate limited resources to candidates that can most effectively advance the search. Existing LLM-based methods typically rely on fixed allocation strategies throughout the search, potentially wasting resources on…

## 89. Universal Textual Teaching for LLMs

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, evaluation, language model, large language, spec
- 作者：Zhanyi Lu, Huan Wang
- 链接：[arXiv](https://arxiv.org/abs/2610.12114) · [PDF](https://arxiv.org/pdf/2610.12114) · [HF](https://huggingface.co/papers/2610.12114)

Knowledge distillation (KD) transfers knowledge from stronger Teacher models to weaker Student models, but most methods require training the Student parameters, thereby binding the distilled knowledge to a specific architecture and checkpoint. This implicit representation is difficult to interpret or reuse across models and limits KD for API-only or costly-to-train models. This paper studies knowledge transfer for…

## 90. Use and Disuse: Intent-Structured Experience Consolidation for Memory and Learning in LLM Agents

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, memory, language model, large language
- 作者：Xiangyi Zeng, Baihang Liu, Xutong Wang, Ze Jin, Yunpeng Li, Qixu Liu
- 链接：[arXiv](https://arxiv.org/abs/2610.12124) · [PDF](https://arxiv.org/pdf/2610.12124) · [HF](https://huggingface.co/papers/2610.12124)

The evolution of Large Language Model agents from single-task execution to long-term autonomous operation highlights the critical challenge of transforming continuous experiences into reusable knowledge. To address this, we propose Hippocam, a hierarchical memory and continual learning architecture. Hippocam draws inspiration from two characteristics of human memory: cognitive processes selectively maintain…

## 91. Poster: A Preliminary Study of LLM Distillation Inference

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, language model, large language, spec
- 作者：Edward Chen, Yuntao Du
- 链接：[arXiv](https://arxiv.org/abs/2610.12137) · [PDF](https://arxiv.org/pdf/2610.12137) · [HF](https://huggingface.co/papers/2610.12137)

Unauthorized model distillation, in which a model is trained on the outputs of a proprietary large language model (LLM), is a growing threat to model providers. We study distillation inference: determining whether a suspect model was distilled from another model or trained independently. We formulate this problem as a hypothesis test and estimate the behavior expected under each hypothesis by training shadow models:…

## 92. Instruction-Conditioned Electromagnetic Spectrum Understanding via Budget-Adaptive Signal Tokenization

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：language model, large language, coding, spec
- 作者：Lei Zhai, Zhihao Chang, Shuyuan Yang, Zhixi Feng
- 链接：[arXiv](https://arxiv.org/abs/2610.12142) · [PDF](https://arxiv.org/pdf/2610.12142) · [HF](https://huggingface.co/papers/2610.12142)

Electromagnetic spectrum monitoring increasingly requires flexible analysis beyond task-specific recognition and detection. Multimodal large language models offer a unified interface, but extending vision-language models (VLMs) to raw I/Q signals requires tokenization that balances fidelity against a strict budget. For signals, dense encoding causes token costs to grow with observation length, whereas…

## 93. DataSense-Bench: The First Step Toward an AI Scientist

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, tool use, tool-use, evaluation, benchmark, spec
- 作者：Yudi Zhang, Mingyu Cao, Lu Yin, Mykola Pechenizkiy, Shiwei Liu
- 链接：[arXiv](https://arxiv.org/abs/2610.12190) · [PDF](https://arxiv.org/pdf/2610.12190) · [HF](https://huggingface.co/papers/2610.12190)

As claims about recursive self-improvement (RSI) and artificial general intelligence (AGI) proliferate, we ask a simple question: do frontier AI models have a sense of data, i.e., can they reliably select the right data for training? We introduce DataSense-Bench to study this capability through the fundamental problem of data selection and performance forecasting in machine learning. We ask AI agents to select and…

## 94. SciTBERT: A family of chronologically consistent language models for scientific and technological language processing

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, language model, spec, retrieval
- 作者：Thomas Gebhart, Russell J. Funk
- 链接：[arXiv](https://arxiv.org/abs/2610.12207) · [PDF](https://arxiv.org/pdf/2610.12207) · [HF](https://huggingface.co/papers/2610.12207)

Pre-trained transformer models are increasingly being used to study scientific and technological progress. Encoders tuned to paper or patent text outperform general-purpose models on downstream classification, regression, and proximity tasks within science and technology. However, the applicability of these models for studying time-dependent or archival properties of science, technology, and their interface is…

## 95. Language Models as AI Research World Models

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reasoning, evaluation, language model, spec
- 作者：Zijun Wang, Zewen Liu, Minhua Lin, Zhaotian Weng, Zhan Shi, Bing He, Yisi Sang, Dakuo Wang, Benoit Dumoulin, Wei Jin, Yuyin Zhou, Cihang Xie, Hanqing Lu
- 链接：[arXiv](https://arxiv.org/abs/2610.12235) · [PDF](https://arxiv.org/pdf/2610.12235) · [HF](https://huggingface.co/papers/2610.12235)

AI research agents automate the cycle of proposing, implementing, and evaluating experiments, opening a path toward recursive self-improvement. Yet their ability to propose experiments outpaces their capacity to execute them in real environments, making outcome prediction a key capability for sustained self-improvement under limited experimental budgets. We investigate language models as Research World Models…

## 96. DVD: Dynamic Vector Decoding for Efficient MLLM-based Perception

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, language model, large language, coding, spec
- 作者：Jinghua Hou, Zhe Liu, Hengshuang Zhao
- 链接：[arXiv](https://arxiv.org/abs/2610.12266) · [PDF](https://arxiv.org/pdf/2610.12266) · [HF](https://huggingface.co/papers/2610.12266)

Multimodal large language models have made remarkable progress in bridging vision and language, facilitating various perception tasks essential for human-machine interaction, robotics, and autonomous driving. However, existing MLLM-based perception methods predominantly rely on text-based coordinate representation, which suffers from excessive token overhead, or fixed-range quantization, which suffers from range and…

## 97. HarnessSQL: Harness-Native Training for SQL Agents in Realistic Database Environments

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reinforcement learning, benchmark, spec
- 作者：Haolin Yang, Jipeng Zhang, Jian Xie, Shuaishuai Gong, Sirui Han, Yike Guo
- 链接：[arXiv](https://arxiv.org/abs/2610.12274) · [PDF](https://arxiv.org/pdf/2610.12274) · [HF](https://huggingface.co/papers/2610.12274)

Text-to-SQL models are commonly trained to map questions directly to static queries, whereas real-world database agents operate through stateful, multi-turn interaction with live databases -- inspecting schemas, executing probe queries, diagnosing errors, and revising hypotheses. This creates a critical train-deploy mismatch, as the execution harness that mediates this interaction is introduced only at inference…

## 98. Unlocking the Regulatory Genome by ARGUS: An Evidence-Constrained Agentic Framework for Interpreting Single Nucleotide Variants

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reasoning, language model, large language, coding, spec, planning
- 作者：Pratik Dutta, Matthew B. Obusan, Max Chao, Rekha Sathian, Nimisha Papineni, Ramana V. Davuluri
- 链接：[arXiv](https://arxiv.org/abs/2610.12281) · [PDF](https://arxiv.org/pdf/2610.12281) · [HF](https://huggingface.co/papers/2610.12281)

Over 90% of disease-associated variants from genome-wide association studies fall in noncoding regulatory regions, yet their functional interpretation remains a central open problem in genomic medicine. Large language models prompted to interpret such variants routinely hallucinate transcription factor (TF) binding changes, fabricate experimental support, and assign biological significance to statistically…

## 99. Learning Probabilistic Logic Programs with Functional Gradient Guided Language Models

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, benchmark, language model, coding
- 作者：Saurabh Mathur, Sahil Sidheekh, Bhavan Vasu, Farbod Tavakkoli, Prasad Tadepalli, Kristian Kersting, Sriraam Natarajan
- 链接：[arXiv](https://arxiv.org/abs/2610.12303) · [PDF](https://arxiv.org/pdf/2610.12303) · [HF](https://huggingface.co/papers/2610.12303)

Declarative logic programs offer a powerful and interpretable abstraction for encoding relational structure and neurosymbolic reasoning, by expressing dependencies as weighted compositional rules. However, inducing them from data remains fundamentally hard, bottlenecked by the combinatorial explosion of symbolic search spaces. LLMs have recently emerged as powerful hypothesis generators, but when used in isolation,…

## 100. Looking Inside LLMs: Small-World Connectivity as a Signature of Reasoning Performance

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, evaluation, language model, large language, spec
- 作者：Zheng Huang, Sansheng Cao, Enpei Zhang, Weikang Qiu, Elynn Chen, Xiang Zhang, Yaoqing Yang, Rex Ying, Dawei Zhou, Yujun Yan
- 链接：[arXiv](https://arxiv.org/abs/2610.12304) · [PDF](https://arxiv.org/pdf/2610.12304) · [HF](https://huggingface.co/papers/2610.12304)

Understanding large language model (LLM) reasoning requires looking beyond behavioral performance to examine how reasoning ability is reflected in internal organization. Inspired by neuroscience findings linking higher intelligence to stronger small-world organization in functional brain networks, we investigate small-world connectivity as a structural signature of LLM reasoning. We construct functional graphs from…

## 101. Is In-Domain Training Enough for Fine-Grained Industrial Anomaly Understanding?

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reasoning, benchmark, language model, large language, spec
- 作者：Xingwu Zhang, Duanyang Du, Huiling Zhu, Jiayue Dai, Yixiao Liu, Guozhi Liu, Zhihan Zhang, Zijun Long
- 链接：[arXiv](https://arxiv.org/abs/2610.12310) · [PDF](https://arxiv.org/pdf/2610.12310) · [HF](https://huggingface.co/papers/2610.12310)

A single multimodal large language model (MLLM) struggles to excel simultaneously at detection, localization, description, and reasoning in multimodal industrial anomaly understanding (MM-IAU). We show that in-domain training does not close this gap. On MMAD, a widely adopted MM-IAU benchmark, trained specialists reach at most 75.5% accuracy in defect localization, against 92.3% for human experts, and even detect…

## 102. VFold: Symmetry-Aware Cross-Layer Value Cache Compression

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, context window, long context, language model, large language, coding
- 作者：Neha Verma, Sungwon Kim, Kenton Murray, Kevin Duh
- 链接：[arXiv](https://arxiv.org/abs/2610.12338) · [PDF](https://arxiv.org/pdf/2610.12338) · [HF](https://huggingface.co/papers/2610.12338)

While caching key-value (KV) states accelerates Large Language Model (LLM) decoding, this cache can dominate memory usage at long context lengths. One solution is to compress this memory by exploiting inter-layer cache similarities. However, most existing techniques necessitate architectural changes to LLMs and incur substantial overhead. In this work, we propose a symmetry-aware value cache merging strategy that…

## 103. Can AI Agents Learn Their Way to the Top? Evaluating Heuristic Learning in a Long-Running Game Agent Competition

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reinforcement learning, evaluation, benchmark, spec
- 作者：Kaisen Yang, Qingle Liu, Kejin Wang, Yicheng Zhao, Jieming Li, Shenghan Zheng, Ruize Yang, Bojun Yang, Heng Gong, Xiang Gao, Lanyue Zhang, Kaiyu Zhong, Zhuo Liu, Shaoxuan Li, Chengxi Li, Yong Yan, Weixuan Zhang, Tianwei Luo, Situ Wang, Youjie Zheng, Sihan Zhao, Shengyuan Wang, Huan-ang Gao, Jiazheng Xu, Xiaohui Xie, Wentao Han, Hongning Wang
- 链接：[arXiv](https://arxiv.org/abs/2610.12341) · [PDF](https://arxiv.org/pdf/2610.12341) · [HF](https://huggingface.co/papers/2610.12341)

Adversarial games have driven advances from heuristic search to reinforcement learning, yet learning and adapting strategies from limited samples remain challenging. AI agents offer an alternative by turning game experience into revisions of executable policies. Building on heuristic learning (HL), we formalize Adversarial Heuristic Learning (AHL), a paradigm that uses AI agents as learning engines to refine game…

## 104. Cited but Not Consulted: A Counterfactual Audit of Legal Chain-of-Thought Faithfulness

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, evaluation, benchmark, language model, large language
- 作者：Saisab Sadhu, Shreeyans Arora, Pratinav Seth
- 链接：[arXiv](https://arxiv.org/abs/2610.12361) · [PDF](https://arxiv.org/pdf/2610.12361) · [HF](https://huggingface.co/papers/2610.12361)

Large language models increasingly justify legal decisions by naming the statute or precedent behind a verdict, treated as evidence that the decision follows from it. We test this directly: holding case facts fixed, we substitute the named legal authority for an unrelated one and decode a model's evolving verdict from its hidden states. Across seven open-weight models (8B-70B) and four benchmarks spanning judicial…

## 105. GeoReform: Reflective Formalization Evolution for Multimodal Geometry Problem Solving

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, benchmark, language model, large language
- 作者：Jialu Wang, Ruichen Zhang, Xiaoou Liu, Hua Wei, Tianlong Chen
- 链接：[arXiv](https://arxiv.org/abs/2610.12391) · [PDF](https://arxiv.org/pdf/2610.12391) · [HF](https://huggingface.co/papers/2610.12391)

Multimodal large language models (MLLMs) often struggle to identify and use geometric relations in diagrams. Recent methods address this challenge by converting geometric entities, relations, and constraints into explicit textual representations for the model to reason over. However, effective formalization is highly non-trivial: on Geometry3K, structure injection fixes 28 errors but introduces 13 new ones among 200…

## 106. WOVEN: Weaving Visual World Modeling into Multimodal LLMs

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, benchmark, language model, large language, spec
- 作者：Zheyu Fan, Yue Zhang, Mingkai Deng, Kangrui Wang, Qineng Wang, Canyu Chen, Jie Hao, Xing Fan, Chenlei Guo, Eric P. Xing, Mohit Bansal, Manling Li
- 链接：[arXiv](https://arxiv.org/abs/2610.12417) · [PDF](https://arxiv.org/pdf/2610.12417) · [HF](https://huggingface.co/papers/2610.12417)

Multimodal large language models (MLLMs) struggle with spatial, embodied, physical, and temporal reasoning. We hypothesize that these failures reflect a shared deficit in visual transition reasoning, and test whether this capability can serve as a shared training primitive, one that different models can learn from different supervision sources and reuse across different tasks, with a systematic training recipe.…

## 107. FastBench: Can Streaming VLMs Perceive High-Dynamic Real-World Streams?

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, language model, large language, spec
- 作者：Yuxuan Hu, Weikang Shi, Yang Bo, Xudong Lu, Xintong Guo, Shuhan Li, Yuyang He, Huankang Guan, Peiwen Sun, Yunqiao Yang, Wenbo Li, Rui Liu, Hongsheng Li
- 链接：[arXiv](https://arxiv.org/abs/2610.12427) · [PDF](https://arxiv.org/pdf/2610.12427) · [HF](https://huggingface.co/papers/2610.12427)

Streaming Video Large Language Models (VLMs) enable continuous video understanding, yet existing benchmarks focus on low-dynamic scenarios. Under bounded context budgets, models must balance temporal history, spatial resolution, and temporal granularity; sparse sampling at 1--2 FPS misses fast events. We introduce FastBench to evaluate high-dynamic perception in real-world video streams. Its trajectory-grounded…

## 108. Predicting Cable Dynamics with Physical Attention Bias

- 分数：8.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：-
- 作者：Avihai Giuili, Rotem Atari, Avishai Sintov, Maya Bechler-Speicher
- 链接：[arXiv](https://arxiv.org/abs/2610.11975) · [PDF](https://arxiv.org/pdf/2610.11975) · [HF](https://huggingface.co/papers/2610.11975)

Learned simulators for deformable linear objects (DLOs) such as cables have to predict the motion of cables they were not trained on and stay stable over long rollouts. Most of their error occurs where the cable touches itself or the floor. Attention over all pairs of cable segments can represent contact between parts of the cable that are far apart along its length, but attention has no notion of geometry. A cable…

## 109. DPPM: Dual-Path Parametric Memory for Personalized Language Models

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, language model, spec
- 作者：Yuhao Chen, Shuochen Liu, Jiayao Shi, Jian Hong, Chen Cheng, Xinyun Ding, Tao Wang, Ya Li, Quan Liu, Tong Xu
- 链接：[arXiv](https://arxiv.org/abs/2610.11776) · [PDF](https://arxiv.org/pdf/2610.11776) · [HF](https://huggingface.co/papers/2610.11776)

Long-term personalization requires language models to use interaction history to track users' preferences across sessions. Parametric memory encodes this interaction history into model parameters or adapters, reducing the need to include it in the inference context. However, independent context compilation leaves cross-session integration unspecified, while recurrent updates can attenuate earlier evidence. To…

## 110. Skill-V: Verifiable Self-Evolving Skill Library for Interactive Agents

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, evaluation, spec
- 作者：Jie Ma, Zhipeng Qian, Yufei Ma, Zihan Liang, Jiayi Ji, Qingpeng Cai, Ben Chen, Peng Jiang, Xiaoshuai Sun
- 链接：[arXiv](https://arxiv.org/abs/2610.11781) · [PDF](https://arxiv.org/pdf/2610.11781) · [HF](https://huggingface.co/papers/2610.11781)

Interactive agents can turn experience into reusable skills, yet existing self-evolving skill libraries primarily improve by accumulating new knowledge. Failures may lead to new skills, while previously stored skills are less often revisited as new evidence arrives. However, growth alone does not ensure reliability, as a retrieved skill may be inapplicable under the current task conditions, and an existing skill may…

## 111. Compile the Table: Query-Calibrated Operator Compression for Tabular In-Context Learning

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, spec, retrieval
- 作者：Xu Zhao, Jiaming Zhao, Bin Zhao, Yong Yang
- 链接：[arXiv](https://arxiv.org/abs/2610.11784) · [PDF](https://arxiv.org/pdf/2610.11784) · [HF](https://huggingface.co/papers/2610.11784)

Tabular in-context learning (ICL) has emerged as a training-free and accurate paradigm for tabular prediction, but current approaches to compressing its in-context examples face an accuracy-throughput tradeoff: fixed subsets can sacrifice accuracy, while query-specific retrieval limits cache reuse and batching across queries, reducing throughput. We propose QCOC (Query-Calibrated Operator Compression), which…

## 112. AuraLuxMuse: Adaptive Fusion Modeling for Aesthetic Stage Lighting Design with Music and Expert Guidance

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, spec, retrieval
- 作者：Junyu Deng, Jiale Cao, Mengtian Li, Zhongxia Ji, Ruhua Chen, Yiyi He, Guangnan Ye, Zuo Hu
- 链接：[arXiv](https://arxiv.org/abs/2610.11792) · [PDF](https://arxiv.org/pdf/2610.11792) · [HF](https://huggingface.co/papers/2610.11792)

We present AuraLuxMuse, a novel system for automated aesthetic stage lighting design that integrates expert knowledge, representation learning, and preference-adaptive modeling. Lighting design in live performance settings requires the seamless translation of musical features into dynamic lighting behaviors. However, traditional workflows remain time-consuming, labor-intensive, and difficult to transfer. AuraLuxMuse…

## 113. From Pixels to Structure: Lightweight Vision-Language Models for Document OCR and Structured JSON Extraction

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, language model, spec
- 作者：Uddipan Basu Bir, Vincent Christlein, Andreas Maier, Mathias Zinnen
- 链接：[arXiv](https://arxiv.org/abs/2610.11818) · [PDF](https://arxiv.org/pdf/2610.11818) · [HF](https://huggingface.co/papers/2610.11818)

While massive, closed-source Vision-Language Models (VLMs) set strong benchmarks for document understanding, their dependence on commercial APIs limits adoption in institutional archives due to data autonomy concerns, recurring costs, and the environmental footprint of hyperscale computing. This is especially acute in heritage digitization, where documents include historical handwriting, domain-specific terminology…

## 114. From Suppression to Repair: Mitigating Object Hallucination in Large Vision-Language Models via Localized Distribution Alignment

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, language model, spec
- 作者：Chen Zhao, Xingping Dong, Jiachun Shi, Liang Peng, Chong Wang, Zhen Lei, Ran He, Bo Du
- 链接：[arXiv](https://arxiv.org/abs/2610.11826) · [PDF](https://arxiv.org/pdf/2610.11826) · [HF](https://huggingface.co/papers/2610.11826)

Object hallucination remains a major obstacle for large vision-language models (LVLMs) to generate reliable content. An intuitive mitigation strategy is to suppress hallucination-related components in hidden representations. However, these components may also contain useful information, and suppressing them can weaken the model's multimodal capabilities. In this paper, we propose ResOT, a training-free method that…

## 115. How Is Automated Research Evaluated? A Survey of Benchmarks and Evaluation Practices

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, spec
- 作者：Liulei Zhang, Dejing Zhou, Chuyue Huang, Guanhua Chen, Yutong Yao, Lidia S. Chao, Chi Man Vong, Derek F. Wong
- 链接：[arXiv](https://arxiv.org/abs/2610.11877) · [PDF](https://arxiv.org/pdf/2610.11877) · [HF](https://huggingface.co/papers/2610.11877)

Automated research systems support literature synthesis, ideation, experiments, writing, and peer review, but their evaluation is dispersed across tasks, benchmarks, and studies that are difficult to compare directly. We review this literature from the perspective of evaluation design and evidence, covering six targets: literature synthesis, research ideation, executable workflows, scholarly writing and…

## 116. Can Decision Models Understand Stance? Evaluating Jev Against General-Purpose LLMs

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：language model, large language, spec
- 作者：Xing Li, Jinzhong Ning, Yijia Zhang, Liang Yang, Hongfei Lin
- 链接：[arXiv](https://arxiv.org/abs/2610.11901) · [PDF](https://arxiv.org/pdf/2610.11901) · [HF](https://huggingface.co/papers/2610.11901)

Stance detection requires identifying an author's attitude toward a given target, sometimes based on conversational context. Jev, a specialized decision model designed for structured decision-making, offers an alternative to general-purpose large language models (LLMs). In this work, we evaluate Jev on two stance detection datasets, VAST (English texts) and ZS-CSD (Chinese conversations), comparing it with four…

## 117. Beyond Visual Enhancement: Adaptive Multi-Context Steering to Mitigate LVLM Hallucinations

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：language model, coding, spec
- 作者：Shuran Ma, JiaLe Li, Yuxin Dong, Shan Zheng, Qingyun Jiang, Xiang Chen, Qi Zhu, Deyi Ji, Yifan Yang, Jianfeng Pan, Yu Tian, Xue Yang
- 链接：[arXiv](https://arxiv.org/abs/2610.11907) · [PDF](https://arxiv.org/pdf/2610.11907) · [HF](https://huggingface.co/papers/2610.11907)

Hallucination remains a significant challenge in Large Vision-Language Models (LVLMs). Existing training-free methods generally mitigate hallucinations through contrastive decoding or visual enhancement, often increasing the relative influence of visual evidence during generation. This raises a fundamental question: Can LVLMs dynamically regulate the contributions of different context sources to suppress…

## 118. Not Every Change Is Necessary: Recoverable Drift in Large Language Model Unlearning

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, language model, large language
- 作者：Xunlei Chen, Qinghui Gong, Jingkun Xue, Qihe Liu, Shijie Zhou, Fei Ye
- 链接：[arXiv](https://arxiv.org/abs/2610.11915) · [PDF](https://arxiv.org/pdf/2610.11915) · [HF](https://huggingface.co/papers/2610.11915)

Machine unlearning in large language models aims to remove unwanted knowledge while preserving the model's remaining capabilities. Although existing methods use retention objectives or restrict where edits occur, achieving the desired forgetting level can still leave collateral changes that impair non-target behavior. Our recovery comparisons suggest that some of these changes can be reversed while preserving…

## 119. Revisiting Identity and Spectra Dispersion in Media-Bridged Time Series Forecasting: Linking Multivariate Signals and Narrative Flows

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, language model, spec
- 作者：Jierui Lei, Wenjian Zhang, Qingyi Yang, Yuyang Hong, Fangzheng Chen, Zhengbo Zhang, Haina Tang, Shiming Xiang
- 链接：[arXiv](https://arxiv.org/abs/2610.11924) · [PDF](https://arxiv.org/pdf/2610.11924) · [HF](https://huggingface.co/papers/2610.11924)

Media-bridged time series forecasting is expanding to encompass traditional "multivariate" and emerging "multimodal" (e.g., through textual assistance). Existing Time Series Forecasting (TSF) models still rely on paradigm-specific relation, fusion, and temporal modules, hindering a common forecasting backbone across numerical and pre-aligned narrative-flow settings. To explore this, we propose the Multimedia…

## 120. When History Helps and Hurts: Selective History Use across Multimodal Turns

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, language model
- 作者：Shuoyang Sun, Kerui Gu, Hao Fang, Shaoli Huang, Bin Chen
- 链接：[arXiv](https://arxiv.org/abs/2610.11948) · [PDF](https://arxiv.org/pdf/2610.11948) · [HF](https://huggingface.co/papers/2610.11948)

Reliable multimodal interaction depends on selective use of conversational history: an earlier question may remain relevant while its previous answer is outdated, whereas a current request may depend on historical evidence despite conflicting new observations. Existing multi-turn evaluations rarely separate these history-use demands from underlying question difficulty. To address this gap, we introduce ReTurn, a…
