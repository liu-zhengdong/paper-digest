# 每日 AI 论文

生成时间：2026-10-09 06:09 UTC  ·  共 120 篇（已按 arXiv ID 去重）

来源：Hugging Face Daily Papers + arXiv（cs.AI / cs.LG / cs.CL / cs.CV）。
排序：HF 上榜、点赞、多源命中、兴趣词。兴趣词可在 `config.json` 改。

## 1. SuperNav: An Agentic Navigation System for Any Task in Any Scene

- 分数：40.0  ·  HF 赞：49  ·  来源：huggingface + arxiv
- 兴趣命中：agent, evaluation, language model, large language, spec
- 作者：Jinkai Zhang, Jingyi Xu, Yuanhong Yu, Jiarui Guo, Ruizhen Hu, Hujun Bao, Xiaowei Zhou, Sida Peng
- 链接：[arXiv](https://arxiv.org/abs/2610.12126) · [PDF](https://arxiv.org/pdf/2610.12126) · [HF](https://huggingface.co/papers/2610.12126)

General-purpose service robots need navigation systems that can handle diverse human requests in unfamiliar environments, combining task generality with scene generality. Some existing methods fine-tune multimodal large language models (MLLMs) to predict navigation actions, making their behavior dependent on the coverage of navigation training data and potentially limiting generalization to new requests and…

## 2. TokenRouter: Efficient Serving System for Token-Level LLM Routing

- 分数：40.0  ·  HF 赞：47  ·  来源：huggingface + arxiv
- 兴趣命中：language model, large language, coding, spec
- 作者：Tianyu Fu, Tengxuan Liu, Ruoxi Wang, Yixin Dong, Yi Ge, Yichen You, Yu Wang
- 链接：[arXiv](https://arxiv.org/abs/2610.12242) · [PDF](https://arxiv.org/pdf/2610.12242) · [HF](https://huggingface.co/papers/2610.12242)

Large language model (LLM) routing distributes inference work across different models, advancing the cost-quality Pareto frontier of LLM serving. While coarse-grained routing at the session or query level has been widely adopted in production systems, recent algorithmic work shows that fine-grained token-level routing can yield substantial efficiency and quality gains. However, efficiently serving token-level routed…

## 3. Long-WAM: Scaling the Context of World-Action Models

- 分数：36.0  ·  HF 赞：94  ·  来源：huggingface
- 兴趣命中：memory, coding, spec, planning
- 作者：Wei Huang, Bohan Zhang, Chenzhi Liu, Isabella Liu, Shuai Yang, Weian Mao, Luozhou Wang, Yicheng Xiao, Weifeng Lin, Qixin Hu, Bryan Chu, Sifei Liu, Linxi Fan, Xiaojuan Qi, Song Han, Yukang Chen
- 链接：[arXiv](https://arxiv.org/abs/2610.10528) · [PDF](https://arxiv.org/pdf/2610.10528) · [HF](https://huggingface.co/papers/2610.10528)

Real-time robot control demands enough visual history to infer motion and task progress, but processing that history can delay action. We present Long-WAM, a model-system framework for scaling the context of causal world-action models under real-time control constraints. Our central finding is that access to history is not the same as using it: longer histories pay off far more when the video foundation is…

## 4. Self-Retrospection Distillation: Turning Post-hoc Experiences into Prior Foresight

- 分数：36.0  ·  HF 赞：83  ·  来源：huggingface
- 兴趣命中：agent, reasoning, reinforcement learning, spec
- 作者：Haoxiang Zhang, Qinglin Chen, Hiroaki Hayashi, Zhuofeng Li, Siming Zhang, Jiaxin Zhang, Jixuan Chen, Fang Wu, Pan Lu, Silvio Savarese, Julian McAuley, Chien-Sheng Wu
- 链接：[arXiv](https://arxiv.org/abs/2610.08077) · [PDF](https://arxiv.org/pdf/2610.08077) · [HF](https://huggingface.co/papers/2610.08077)

Reinforcement learning with verifiable rewards (RLVR) turns agent experience into learning signals primarily through scalar outcome rewards after interaction. For group-relative objectives, however, this signal vanishes when all rollouts receive the same reward, even though their trajectories may reveal useful information about what the task requires and how the agent fails. We ask a complementary question: can…

## 5. Recursive Game Creator: An Agentic Product-Level Experience-Oriented Game Harness

- 分数：36.0  ·  HF 赞：83  ·  来源：huggingface
- 兴趣命中：agent, evaluation, coding, spec
- 作者：Jiajun Chen, Haoyu Wu, Mingda Jia, Xihui Liu
- 链接：[arXiv](https://arxiv.org/abs/2610.08621) · [PDF](https://arxiv.org/pdf/2610.08621) · [HF](https://huggingface.co/papers/2610.08621)

Recent game design agents have made substantial progress in generating playable games. However, program correctness does not ensure an enjoyable experience for players. We present Recursive Game Creator, an experience-oriented harness to advance agentic game development from rough game prototypes into entertaining games. Recursive Game Creator organizes recursive development around four components: Designer,…

## 6. DecepEval: A Benchmark for Evaluating Deception in LLM Agents

- 分数：36.0  ·  HF 赞：66  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark, language model, large language
- 作者：Yiming Xu, Hongyue Yu, Beihua Yang, Zihan Chen, Yixin Liu, Zhen Peng, Bin Shi, Bo Dong, Chao Shen, Irwin King, Qinghua Zheng
- 链接：[arXiv](https://arxiv.org/abs/2610.07967) · [PDF](https://arxiv.org/pdf/2610.07967) · [HF](https://huggingface.co/papers/2610.07967)

As large language model (LLM) agents become increasingly autonomous, they may pursue task performance through deception, raising concerns about their reliable deployment. Existing evaluations show that LLM agents can deceive, but often examine isolated scenarios or narrowly defined conditions, limiting systematic understanding of when deception becomes more likely. To address this gap, we introduce DecepEval, a…

## 7. VepAgent: Bridging Causal-Transition via Tool-Augmented Reinforcement Learning for Video Event Prediction

- 分数：36.0  ·  HF 赞：54  ·  来源：huggingface
- 兴趣命中：agent, reasoning, reinforcement learning, evaluation, language model, large language, spec, retrieval
- 作者：Qiutong Chen, Yuchan Guo, Zhenlong Yuan, Haobo Yang, Fangfang Lin, Xinyi Long, Yin Wang, Zijian Song, Rui Lan, Shi Qiu, Boyuan Pan, Yang Luo, Yuyin Zhou
- 链接：[arXiv](https://arxiv.org/abs/2610.06293) · [PDF](https://arxiv.org/pdf/2610.06293) · [HF](https://huggingface.co/papers/2610.06293)

Multimodal Large Language Models (MLLMs) have demonstrated remarkable potential in video understanding, yet their reliance on retrospective summarization and text-centric priors often limits their ability to bridge unobserved causal transitions when applied to Video Event Prediction (VEP). To address this, we propose VepAgent, an agentic framework that integrates causal-transition reasoning with tool-augmented…

## 8. Semifactual Credit-Augmented Policy Optimization

- 分数：34.5  ·  HF 赞：37  ·  来源：huggingface
- 兴趣命中：reasoning, reinforcement learning, benchmark, language model, large language, coding, spec
- 作者：Junshu Pan, Zhizhang Fu, Shulin Huang, Yiran Ding, Zifan Cheng, Wenqi Shao, Qiaosheng Zhang, Yue Zhang
- 链接：[arXiv](https://arxiv.org/abs/2609.40360) · [PDF](https://arxiv.org/pdf/2609.40360) · [HF](https://huggingface.co/papers/2609.40360)

Reinforcement learning with verifiable rewards (RLVR) has improved the reasoning capabilities of large language models (LLMs), yet their predictions remain sensitive to task-irrelevant prompt features. We investigate this sensitivity through semifactual prompt interventions that preserve the underlying problem and its answer. Our analysis reveals substantial variation in token-level sensitivity and shows that…

## 9. STEPQuant: When and Where Errors Matter in Delta-Rule Recurrent State Quantization

- 分数：34.0  ·  HF 赞：103  ·  来源：huggingface
- 兴趣命中：memory, benchmark, coding
- 作者：Bingchen Yao, Haobo Xu, Haokun Lin, Yichen Wu, Ziyu Guo, Renrui Zhang, Zhichao Lu, Zhenan Sun, Ying Wei
- 链接：[arXiv](https://arxiv.org/abs/2609.38169) · [PDF](https://arxiv.org/pdf/2609.38169) · [HF](https://huggingface.co/papers/2609.38169)

Linear attention replaces growing KV caches with fixed-size recurrent states, yet these persistent states can become a substantial memory bottleneck under concurrent serving. Directly quantizing recurrent states to low precision often leads to severe accuracy degradation, as quantization errors propagate through successive state updates. We discover that the impact of these errors depends on two complementary…

## 10. nanoMuse: An Open-Source Personal Agent for Every Device You Own

- 分数：34.0  ·  HF 赞：93  ·  来源：huggingface
- 兴趣命中：agent, memory, evaluation
- 作者：Guangyi Liu, Yong Liu, Jiangning Zhang
- 链接：[arXiv](https://arxiv.org/abs/2610.08699) · [PDF](https://arxiv.org/pdf/2610.08699) · [HF](https://huggingface.co/papers/2610.08699)

Assistants from 2011 answered and waited, and agents from 2023 did a task and stopped. In September 2026 Meta's Muse showed an agent for one person, with accounts, devices, memory and a conversation that lasts, closed, in a vendor's cloud, in one country. Such an agent is expected to act on a person's accounts and devices, remember them across weeks, speak first when it is worth it, and answer for what it did. It is…

## 11. UltraText Bench: A Comprehensive Bilingual Benchmark for Evaluating Visual Text Rendering in Image Generation

- 分数：34.0  ·  HF 赞：78  ·  来源：huggingface
- 兴趣命中：evaluation, benchmark, language model
- 作者：Deyuan Liu, Yihao Hu, Jingxuan Zhang, Xingying Li, Jun Xie, Jiacheng Liu, Jungang Li, Yu Huang, Xuanyi Liu, Yue Ding, Zecheng Wang, Lei Zhao, Mingda Wang, Zhenglin Cheng, Peng Sun, Tao Lin
- 链接：[arXiv](https://arxiv.org/abs/2610.09823) · [PDF](https://arxiv.org/pdf/2610.09823) · [HF](https://huggingface.co/papers/2610.09823)

Dense visual text requires image generators to reproduce long strings across multiple regions with correct placement and legibility. As short-string rendering improves, evaluation must test sustained performance across more demanding scenes. We introduce UltraText Bench, a bilingual benchmark for prompt-only generation of dense visual text. It contains 432 prompts spanning 24 real-world scene categories and three…

## 12. UniWAM: Unified World-Action Model

- 分数：34.0  ·  HF 赞：52  ·  来源：huggingface
- 兴趣命中：reasoning, evaluation, language model
- 作者：Jiayi Chen, Wenxuan Song, Jingbo Wang, Shuai Zhou, Xicheng Gong, Zehua Fan, Ziyang Zhou, Junwu E, Haodong Yan, Fuhao Li, Qize Yu, Xu Huang, Pengwei Wang, Wen Chen, Shunbo Zhou, Haoang Li
- 链接：[arXiv](https://arxiv.org/abs/2610.02054) · [PDF](https://arxiv.org/pdf/2610.02054) · [HF](https://huggingface.co/papers/2610.02054)

Vision-language-action models benefit from the understanding and reasoning capabilities of pretrained vision-language models, but action-only supervision provides limited grounding in world dynamics. Conversely, world-action models inherit spatiotemporal priors from video generation models, yet remain limited in semantic understanding and reasoning under distribution shifts. We introduce UniWAM, a unified…

## 13. RunningTab: Direct Workspace Interaction with Environment-Side Tabs

- 分数：33.0  ·  HF 赞：34  ·  来源：huggingface
- 兴趣命中：agent, context window, benchmark, spec
- 作者：Jinheon Baek, Soyeong Jeong, Yumin Choi, Dongsu Han, Sung Ju Hwang
- 链接：[arXiv](https://arxiv.org/abs/2610.10444) · [PDF](https://arxiv.org/pdf/2610.10444) · [HF](https://huggingface.co/papers/2610.10444)

Much knowledge work produces new deliverables from files a workspace already holds, and LLM agents are beginning to take such work over. Through direct corpus interaction, an agent can search and read any of those files from a terminal with no indexing, and producing a deliverable from many of them in this way is what we call direct workspace interaction (DWI). Reaching the files, however, is only half the task:…

## 14. Learn2Play Bench: How Well Do LLM Agents Learn from Experience in Unfamiliar Environments?

- 分数：32.5  ·  HF 赞：33  ·  来源：huggingface
- 兴趣命中：agent, reasoning, evaluation, benchmark
- 作者：Yibo Li, Jinhang Qiu, Zhi Zheng, Qianyun Guo, Jiaying Wu, Shuo Ji, Bryan Hooi
- 链接：[arXiv](https://arxiv.org/abs/2610.08215) · [PDF](https://arxiv.org/pdf/2610.08215) · [HF](https://huggingface.co/papers/2610.08215)

Learning from experience is essential for LLM agents to adapt to unfamiliar and dynmaic environments. Evaluating this ability is therefore important for understanding how effectively agents acquire and use new knowledge. Existing benchmarks have sought to evaluate this ability, but they primarily evaluate tasks whose rules are provided in the instructions or already familiar to pretrained models, making it difficult…

## 15. Questioning the Questions: Sustaining Self-Evolution in Reasoning Models

- 分数：32.0  ·  HF 赞：65  ·  来源：huggingface
- 兴趣命中：reasoning, benchmark
- 作者：Jinyuan Li, Chengsong Huang, Langlin Huang, Donghong Cai, Shiping Gao, Yuyi Yang, Jiaxin Huang
- 链接：[arXiv](https://arxiv.org/abs/2610.04299) · [PDF](https://arxiv.org/pdf/2610.04299) · [HF](https://huggingface.co/papers/2610.04299)

Self-evolving reasoning models learn from their own generated questions, yet repeated self-training can lead to performance collapse. In this paper, we investigate why performance deteriorates over successive rounds and how to sustain self-evolution. Our analysis identifies two recurring quality problems in self-generated questions: invalid questions and repeated variants of the same mathematical questions. First,…

## 16. AgentGarten: Code Worlds for Evolving Agents

- 分数：32.0  ·  HF 赞：32  ·  来源：huggingface + arxiv
- 兴趣命中：agent, reinforcement learning
- 作者：Jiawei Chi, Shangchen Miao, Zhiyuan Shi, Kailu Wu, Hanyang Wang, Weiliang Chen, Qiyu Dai, Jinshan Ren, Jun Gao, Mingsheng Long, Yueqi Duan, Jiangran Lyu, Jialong Wu, Fangfu Liu
- 链接：[arXiv](https://arxiv.org/abs/2610.12374) · [PDF](https://arxiv.org/pdf/2610.12374) · [HF](https://huggingface.co/papers/2610.12374)

Interactive virtual worlds allow agents to learn through exploration and interaction. What agents can learn is bounded by the environments they practice in, which must be faithful, with consistent state, rules, and dynamics, and realistic, with observations that follow the real-world visual distributions. Achieving both across diverse worlds remains a bottleneck. We introduce AgentGarten, a framework that couples…

## 17. GRACE: Generation-aware latent compression for efficient video generation

- 分数：30.0  ·  HF 赞：74  ·  来源：huggingface
- 兴趣命中：spec
- 作者：Jiyoung Kim, Paul Hyunbin Cho, Jisu Nam, Donghoon Lee, Hyunsung Go, Yeonkyeong Lee, Hansaem Kim, Seungryong Kim
- 链接：[arXiv](https://arxiv.org/abs/2610.10524) · [PDF](https://arxiv.org/pdf/2610.10524) · [HF](https://huggingface.co/papers/2610.10524)

Highly compressed video autoencoders offer an effective way to accelerate video diffusion models, as the Diffusion Transformer (DiT) operates on far fewer tokens. However, such autoencoders are challenging to train, since a higher compression ratio degrades reconstruction quality and recovering it requires more channels, which is known to slow the convergence of the DiT. The compressed latent also differs from the…

## 18. From Traces to Agentic Worlds: Agentic Language World Models for Interactive Environment Simulation

- 分数：30.0  ·  HF 赞：69  ·  来源：huggingface
- 兴趣命中：agent
- 作者：Quanyu Long, Xiao Chen, Jianda Chen, Haozhen Zhang, Qisheng Hu, Jianzhu Bao, Wenya Wang
- 链接：[arXiv](https://arxiv.org/abs/2610.06100) · [PDF](https://arxiv.org/pdf/2610.06100) · [HF](https://huggingface.co/papers/2610.06100)

Realistic environment replicas are increasingly valuable for training and evaluating LLM agents, yet the original systems may be inaccessible or impractical to reproduce. We explore agentic language world modeling: rather than rebuilding an executable environment, a world model agent serves as the environment for a task agent and supports faithful and stateful simulation. We instantiate this paradigm with Trace2Env,…

## 19. SGF+: Decoupling Gradient Flows for Autoregressive Video Generation

- 分数：30.0  ·  HF 赞：53  ·  来源：huggingface
- 兴趣命中：spec
- 作者：Zihan Su, Junhao Zhuang, Yaowei Li, Siwen Lu, Haoran Li, Lingen Li, Haoyu Wu, Weiyang Jin, Songchun Zhang, Haoyang Huang, Chun Yuan, Zeyue Xue, Nan Duan
- 链接：[arXiv](https://arxiv.org/abs/2610.10429) · [PDF](https://arxiv.org/pdf/2610.10429) · [HF](https://huggingface.co/papers/2610.10429)

Autoregressive video generation requires denoising the current frames while writing their key-value representations as context for future predictions. However, these two roles typically share parameters, and we find that their gradients exhibit distinct patterns and systematic negative alignment, hindering the joint optimization of visual quality and temporal consistency. We introduce Self Gradient Forcing Plus…

## 20. Multi-Agent Egocentric World Model with Fine-Grained Embodied Interaction

- 分数：30.0  ·  HF 赞：28  ·  来源：huggingface + arxiv
- 兴趣命中：agent, memory
- 作者：Dahyun Chung, Siyoon Jin, Hyunwook Choi, Honggyu An, Junyoung Seo, Hyunsung Kim, Seung Wook Kim, Seungryong Kim
- 链接：[arXiv](https://arxiv.org/abs/2610.12299) · [PDF](https://arxiv.org/pdf/2610.12299) · [HF](https://huggingface.co/papers/2610.12299)

Egocentric world models predict first-person observations conditioned on an agent's actions, but most focus on a single agent. Real embodied settings often involve multiple agents that act and interact within a shared environment. Existing multi-agent world models rely on coarse actions like locomotion, camera control, or discrete commands, leaving fine-grained embodied interactions underexplored. We formulate…

## 21. PhysEvo: Astra Can Act, Let It

- 分数：28.5  ·  HF 赞：29  ·  来源：huggingface
- 兴趣命中：agent, evaluation, spec
- 作者：Wenqing Tian, Zeyu Zhang, Zhaocheng Liu, Fengwei Liu, Qiang Liu, Liang Wang
- 链接：[arXiv](https://arxiv.org/abs/2610.08995) · [PDF](https://arxiv.org/pdf/2610.08995) · [HF](https://huggingface.co/papers/2610.08995)

Astra can act, yet reliable manipulation depends on the system through which it observes and controls the world. We introduce PhysEvo, a framework for physical recursive self-improvement (RSI) around a single frozen model. A task agent executes robot tasks; a meta-agent uses the resulting trajectories to diagnose failures, revise tools and skills, and test corrections. The meta-agent can also improve its own…

## 22. SWE-Game: Can Coding Agents Build the Games We Want?

- 分数：28.5  ·  HF 赞：25  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark, coding, spec
- 作者：Xiaoyu Chen, Lai Wei, Jin Wang, Xiangyu Zou, Ruochen Fan, Enze Luo, Mingzhe Yao, Jiahui Zhu, Yuhua Wen, Linghe Kong, Weiran Huang
- 链接：[arXiv](https://arxiv.org/abs/2609.33678) · [PDF](https://arxiv.org/pdf/2609.33678) · [HF](https://huggingface.co/papers/2609.33678)

We introduce SWE-Game, a benchmark of 247 tasks grounded in 41 executable reference Godot games spanning 13 gameplay categories in 2D and 3D. Five task types cover development from a brief, implementation from a game design document, skeleton completion, repair of 83 injected-fault cases, and Godot-to-Unity porting. Reference materials specify the intended gameplay, while a shared instrumentation interface lets…

## 23. Tetris3D: 3D Scene Generation With Objects That Fit Together

- 分数：28.0  ·  HF 赞：42  ·  来源：huggingface
- 兴趣命中：-
- 作者：Jaeyeong Kim, Jinhyuk Jang, Jongmin Lee, Kyehong Park, Seungryong Kim
- 链接：[arXiv](https://arxiv.org/abs/2610.10539) · [PDF](https://arxiv.org/pdf/2610.10539) · [HF](https://huggingface.co/papers/2610.10539)

We propose Tetris3D, a generative framework for single-image 3D scene reconstruction that recovers objects which are physically and geometrically coherent as a scene. Existing methods often generate objects independently or couple them implicitly, providing limited guidance for ensuring fine-grained spatial compatibility between neighboring objects that interact with one another. To address this, we explicitly…

## 24. Gains and Collapse in On-Policy Distillation:A Reinforcement Learning Perspective

- 分数：28.0  ·  HF 赞：28  ·  来源：huggingface
- 兴趣命中：reinforcement learning, language model, spec
- 作者：Han Cui, Jianhao Yan, Yun Luo, Hongbo Zhang, Zhizhang Fu, Yue Zhang
- 链接：[arXiv](https://arxiv.org/abs/2610.03185) · [PDF](https://arxiv.org/pdf/2610.03185) · [HF](https://huggingface.co/papers/2610.03185)

On-policy distillation (OPD) has become an important approach to language model post-training. However, despite its performance gains, OPD can also collapse into excessively long and repetitive generation, and the mechanism underlying these divergent outcomes remains poorly understood. We explain these outcomes through a reinforcement learning perspective: the teacher implicitly rewards student behaviors, even those…

## 25. SparseDecoding: Decoding-Aware Pruning for Accurate and Efficient LLM Inference

- 分数：28.0  ·  HF 赞：16  ·  来源：huggingface + arxiv
- 兴趣命中：memory, benchmark, language model, large language, coding, spec
- 作者：Qitong Wang, Xinwei Niu, Mingluo Su, Shanwei Zhao, Shiai Zhu, Huan Wang
- 链接：[arXiv](https://arxiv.org/abs/2610.12327) · [PDF](https://arxiv.org/pdf/2610.12327) · [HF](https://huggingface.co/papers/2610.12327)

The memory-bound nature of the decoding stage of large language model (LLM) inference incurs significant latency. Layer-wise training-free network pruning approaches guided by the Hessian have been a prominent solution to this problem, as pruning reduces the number of nonzero parameters read from memory during decoding. Nevertheless, typical methods in this line compute the Hessian using pre-collected natural…

## 26. RobotWorld: Benchmarking Multimodal Agents for Robot Use Across Diverse Tasks and Embodiments

- 分数：27.0  ·  HF 赞：30  ·  来源：huggingface
- 兴趣命中：agent, benchmark
- 作者：Zhiqin Yang, Chenxin Li, Xiaomeng Hu, Yibin Liu, Weidong Huang, Jiankai Sun, Haitao Li, Zijian Wu, Yuzhi Huang, Fanding Huang, Hanwen Sun, Jiashun Liu, Jingqi Tong, Mingxin Huang, Shaoli Hu, Shijue Huang, Tianyi Bai, Xinyuan Wang, Yunlong Lin, Zhengyang Tang, Zhexin Zhang, Zhuo Chen, Xierui Song, Juntao Dai, Boyuan Chen, Jiaming Ji, Fangneng Zhan, Mengkang Hu, Wei Xue, Yonggang Zhang, Han Hu, Tsung-Yi Ho, Yike Guo
- 链接：[arXiv](https://arxiv.org/abs/2610.10409) · [PDF](https://arxiv.org/pdf/2610.10409) · [HF](https://huggingface.co/papers/2610.10409)

General-purpose agents increasingly write code, use tools, and complete complex digital tasks, raising the question of how far these capabilities carry into the physical world. To investigate this, we introduce RobotWorld, a challenging simulation testbed for robot use: turning instructions and observations into physical task execution through robot interfaces. Its 84 tasks span manipulation, mobile manipulation,…

## 27. Mechanics of Long-Context Hybrid Models Part 1.1: From Hybrid Attention to Hybrid Position

- 分数：27.0  ·  HF 赞：30  ·  来源：huggingface
- 兴趣命中：language model, large language
- 作者：Xiaoran Liu, Ziwei He, Xipeng Qiu
- 链接：[arXiv](https://arxiv.org/abs/2610.10114) · [PDF](https://arxiv.org/pdf/2610.10114) · [HF](https://huggingface.co/papers/2610.10114)

The architectural design of Large Language Models (LLMs) is shifting from traditional full-attention-only models to hybrid models, which combine different attention modules to improve long-context efficiency and performance in length extrapolation and context extension. To explain why hybrid models work and how to design them better, we propose Mechanics of Long-Context Hybrid Models. As Part 1.1 of this series, we…

## 28. WorldSonus: Bringing Sound to Worlds

- 分数：26.5  ·  HF 赞：33  ·  来源：huggingface
- 兴趣命中：benchmark
- 作者：Pengjun Fang, Jingyi Fa, Kam Man Wu, Jiaming Wang, Haoyuan Huang, Yaguang Wu, Xiangjun Huang, Ziyang Ma, Weijia Chen, Hongyu Liu, Zeyue Tian, Qifeng Chen
- 链接：[arXiv](https://arxiv.org/abs/2610.08760) · [PDF](https://arxiv.org/pdf/2610.08760) · [HF](https://huggingface.co/papers/2610.08760)

Recent advances in world models have enabled increasingly realistic visual synthesis. However, these generated environments remain largely silent. Bringing sound to world models poses three core challenges: real-time generation to keep pace with interactive video streams, interactive control to respond to mid-stream sound instructions, and spatially aligned stereo to reflect scene geometry and camera motion. To…

## 29. VIEScore2: Unified Image Evaluation with Spatially Grounded Explanations

- 分数：26.5  ·  HF 赞：25  ·  来源：huggingface
- 兴趣命中：evaluation, benchmark, spec
- 作者：Xianda Du, Max Ku, Weiming Ren, Zhi Rui Tam, Chunlin Ren, Ping Nie, Min-Hung Chen, Wenhu Chen
- 链接：[arXiv](https://arxiv.org/abs/2610.00994) · [PDF](https://arxiv.org/pdf/2610.00994) · [HF](https://huggingface.co/papers/2610.00994)

Existing synthetic image evaluators typically provide only a scalar quality score and do not identify the image regions that support it. We introduce VIEScore2, a unified evaluator for image generation and editing tasks with optional conditioning images. VIEScore2 represents an image as an N x N grid and jointly predicts quality scores and defect locations in a single model pass. Its text-native grid representation…

## 30. ReSAIL: Mitigating Collapse in Iterative Agent Self-Distillation

- 分数：26.0  ·  HF 赞：32  ·  来源：huggingface
- 兴趣命中：agent
- 作者：Shengjie Jin, Hengbo Xu, Zelong Sun, YuJie Guo, Zhiwu Lu
- 链接：[arXiv](https://arxiv.org/abs/2609.39306) · [PDF](https://arxiv.org/pdf/2609.39306) · [HF](https://huggingface.co/papers/2609.39306)

Iterative self-distillation enables LLM agents to learn from successive deployments, offering a path toward recursive self-improvement (RSI). Yet our experiments with existing methods reveal a collapse in deployment performance across cycles, while task performance with privileged information (PI) also declines. We address this collapse by prioritizing informative interaction steps for distillation and preserving…

## 31. DreamTrue: Action-Faithful Robot World Model with Counterfactual Post-Training

- 分数：25.5  ·  HF 赞：27  ·  来源：huggingface + arxiv
- 兴趣命中：-
- 作者：Junyan Li, Ruizhi Li, Yu Liu, Xiangshuo Liu, Mingchao Sun, Hongyu Pan, Mu Xu, Lue Fan, Zhaoxiang Zhang
- 链接：[arXiv](https://arxiv.org/abs/2610.12468) · [PDF](https://arxiv.org/pdf/2610.12468) · [HF](https://huggingface.co/papers/2610.12468)

We present DreamTrue, a multi-view, cross-embodiment robot world model for action-faithful and physically plausible video prediction. Training such a model on existing robot datasets faces two obstacles: imprecise calibration can impair action following, while limited coverage of unsuccessful interactions can bias predictions toward successful outcomes. To improve action following across embodiments, we render…

## 32. Agentic RAG Evaluation: Budget Allocation Across Questions, Trajectories, and Reads

- 分数：25.5  ·  HF 赞：19  ·  来源：huggingface
- 兴趣命中：agent, evaluation, spec, retrieval
- 作者：Jingjie Ning, Xueqi Li, Yibo Kong
- 链接：[arXiv](https://arxiv.org/abs/2610.05034) · [PDF](https://arxiv.org/pdf/2610.05034) · [HF](https://huggingface.co/papers/2610.05034)

Evaluation budgets in agentic retrieval-augmented generation span questions, search trajectories, and repeated answers. We measure allocation precision, reading efficiency, and cost boundaries using a retrieval-feedback comparison on HotpotQA and MuSiQue. At 34.14--34.39M model tokens, broader question coverage lowers standard error by 33\% versus five reads and 12.6\% versus three trajectories. Archived nested and…

## 33. On KL-Regularized Policy Optimization

- 分数：25.5  ·  HF 赞：19  ·  来源：huggingface
- 兴趣命中：agent, reinforcement learning, language model, large language, spec
- 作者：Yifan Zhang
- 链接：[arXiv](https://arxiv.org/abs/2610.08963) · [PDF](https://arxiv.org/pdf/2610.08963) · [HF](https://huggingface.co/papers/2610.08963)

Asynchronous reinforcement learning (RL) for large language model (LLM) agents trains one policy on trajectories generated by another: rollouts come from stale checkpoints, and the inference engine's probabilities differ from the trainer's even at identical parameters. Standard remedies either clip importance ratios, which biases the update, or, as in GRPO, sample a group of responses per prompt, which is costly…

## 34. MIMESIS: Learning User Simulators as Training Environments for Interactive Agents

- 分数：25.5  ·  HF 赞：19  ·  来源：huggingface
- 兴趣命中：agent, reasoning, reinforcement learning, evaluation, spec
- 作者：Hoang Phan, Dat Huynh, Andrey Zhmoginov, Qi Zeng, Wancen Mu, Yue Cao, Shengjie Bi, Yun He, Changdae Oh, Deren Lei
- 链接：[arXiv](https://arxiv.org/abs/2610.09484) · [PDF](https://arxiv.org/pdf/2610.09484) · [HF](https://huggingface.co/papers/2610.09484)

Training and evaluating interactive language agents typically requires rich user interactions, yet collecting human feedback is expensive and difficult to scale. Simulated users offer a scalable alternative, but they must both resemble real user behavior and provide useful learning experiences for agents. In contrast, most agent-training frameworks rely on off-the-shelf assistant LLMs, whose helpfulness can make…

## 35. WebFovea: When the Model Is Right but the Click Is Wrong -- Reliable Round Trips for Vision-Based Web Agents on Live Websites

- 分数：24.5  ·  HF 赞：17  ·  来源：huggingface
- 兴趣命中：agent, reasoning, benchmark, language model, large language
- 作者：Jiangang Han
- 链接：[arXiv](https://arxiv.org/abs/2610.03036) · [PDF](https://arxiv.org/pdf/2610.03036) · [HF](https://huggingface.co/papers/2610.03036)

We present WebFovea, a vision-based web agent that placed 2nd in the WebRetriever Challenge 2026 with a final score of 57.0 out of 100. The challenge evaluates agents end to end on Protocol III of the WebRetriever benchmark (arXiv:2607.06118): starting from an entry URL on a live website, the agent must operate the site's own interface and return a verifiable answer. A capable multimodal large language model (LLM)…

## 36. VibeEdit: Image Editing with Canvas Instructions

- 分数：24.5  ·  HF 赞：9  ·  来源：huggingface + arxiv
- 兴趣命中：reinforcement learning, evaluation, benchmark, spec
- 作者：Jinjing Zhao, Fangyun Wei, Yitong Wang, Xiuyu Wu, Yunuo Chen, Yang Yue, Sirui Zhang, Wenbo Wang, Hongyang Zhang, Dong Chen, Yan Lu, Chang Xu
- 链接：[arXiv](https://arxiv.org/abs/2610.12229) · [PDF](https://arxiv.org/pdf/2610.12229) · [HF](https://huggingface.co/papers/2610.12229)

In text-guided image editing, describing the desired change is often straightforward, but identifying the intended object or region can be cumbersome, especially when several objects look alike. We introduce a new image editing interface that lets users place spatial marks and optional short notes directly on the image. Together, these annotations form a canvas instruction that specifies where to edit and what to…

## 37. From Pareto to Preference: Personalized Test-Time Scaling via Amortized Agentic Policy Discovery

- 分数：24.0  ·  HF 赞：16  ·  来源：huggingface
- 兴趣命中：agent, reasoning, evaluation, language model, large language, spec
- 作者：Xinglin Wang, Zishen Liu, Tong Zheng, Shaoxiong Feng, Peiwen Yuan, Yiwei Li, Jiayi Shi, Yueqi Zhang, Chuyi Tan, Ji Zhang, Boyuan Pan, Kan Li
- 链接：[arXiv](https://arxiv.org/abs/2610.09684) · [PDF](https://arxiv.org/pdf/2610.09684) · [HF](https://huggingface.co/papers/2610.09684)

Test-time scaling (TTS) improves the reasoning capabilities of large language models by allocating additional inference computation. Existing approaches to improving TTS efficiency largely optimize accuracy against one resource dimension at a time, advancing either the accuracy--cost or accuracy--latency Pareto frontier. Yet user requirements are multidimensional: users may specify accuracy, latency, and…

## 38. MiMo-V2.6: Scaling Reinforcement Learning Towards Self-Improvement

- 分数：24.0  ·  HF 赞：16  ·  来源：huggingface + arxiv
- 兴趣命中：agent, reinforcement learning
- 作者：Core Team, Zongming Qiao, Ziyue Hua, Zirui Ou, Zihao Yue, Zihan Jiang, Zhuo Huang, Zhiyang Chen, Zhixian Zheng, Zhipeng Xu, Zhengrui Ma, Yuyang Hu, Yuhang Dong, Yuechen Zhang, Yudong Wang, Yuanxin Liu, Yixin Yang, Yishuo Cai, Yikai Zhao, Yihan Yan, Yifan Zhang, Yifan Song, Xiyu Wei, Xing Zhang, Xin Zhang, Xiaoqian Liu, Xiaodong Ji, Xiangwei Deng, Xueyu Guo, Wenhan Ma, Weimin Xiong, Weikun Wang, Weiji Zhuang, Shuo Liu, Shuhuai Ren, Shuhao Gu, Shimao Chen, Shijie Cao, Shihua Yu, Shicheng Li, Shengjie Zhou, Shaolei Zhang, Rang Li, Qiying Wang, Qingkai Fang, Qianli Chen, Minzheng Wang, Liwen Wang, Linli Yao, Linghao Zhang, Liangyu Cheng, Liang Zhao, Lei Li, Jinhao Dong, Jinyu Xiang, Jianyu Wei, Jiangshan Duo, Huaqiu Liu, Huanjie Fan, Hongyi Guan, Hongshen Xu, Hao Tian, Hanyu Li, Hailin Zhang, Gang Wang, Fuli Luo, Feng Wei, Dong Zhang, Dawei Zhu, Chiheng Lou, Chenhong He, Chenhao He, Chenghua Liu, Bowen Ye, Bowen Shen, Boshen Xu, Bo Yang, Bingquan Xia, Bangjun Xiao, Baixuan Xu, Zhouxiang Mao, Zhiyang Zhang, Zhixiang Xu, Zhenru Lin, Zhengju Tang, Zhaojun Huang, Yuzhe Weng, Yuxing Xiang, Yuxiao Li, Yuheng Yang, Yuhang Wang, Yuchen Liu, Yuanyuan Tian, Yuanliang Dong, Yu Cheng, Yongzhe He, Yongshun Liang, Yong Wang, Yiyan Wang, Yitian Gong, Yijie Zhang, Yanshu Xin, Xun Zhang, Xingjian Zhao, Wenyu Yang, Wenshan Huang, Wenhao Li, Tingwei Huang, Tianyu Yu, Tianyang Lu, Taoyu Yang, Sinan Du, Shutong Tian, Shulin Du, Shengfan Wang, Shanchuan Fang, Qihao Zhang, Qibin Yang, Qian Yu, Qian Tu, Pengrong Xie, Peipei Wang, Peidian Li, Minkun Guo, Mingchen Shao, Luohan Gao, Lijie Wang, Liang Shi, Kaiqi Chen, Kaiming Liu, Kaifei Wang, Kai Yang, Jinlong Xue, Jiechen Zhang, Jiaxuan Liu, Hongxu An, Hao Peng, Hanglong Lü, Guonan Wang, Feiyu Yang, Fanyu Cao, Fangyue Liu, Fan Cui, Cong Wang, Chun Chen, Chenxu Bai, Chengxuan Zhu, Chenghua Wang, Boyi Zeng
- 链接：[arXiv](https://arxiv.org/abs/2610.11959) · [PDF](https://arxiv.org/pdf/2610.11959) · [HF](https://huggingface.co/papers/2610.11959)

Reinforcement learning (RL) is the central training paradigm for advancing large foundation models towards self-improvement. This report introduces the MiMo-V2.6 series, an omni-modal family that pushes the frontier of model intelligence by scaling RL compute. Prior to RL, we conduct mid-training on a broad multimodal corpus to provide ample exploration space, and build a solid infrastructure on the pretrained…

## 39. In-context Robot Learning Made Simple: A Democratized Recipe for Manipulation Tasks

- 分数：23.5  ·  HF 赞：27  ·  来源：huggingface
- 兴趣命中：spec
- 作者：Minxing Li, Minghao Han, Weizhi Zhao, Hanwen Wang, Xiangshuo Liu, Shuyao Shang, Jingxiang Zhou, Mingchao Sun, Hongyu Pan, Mu Xu, Yu Liu, Lue Fan, Zhaoxiang Zhang
- 链接：[arXiv](https://arxiv.org/abs/2609.38173) · [PDF](https://arxiv.org/pdf/2609.38173) · [HF](https://huggingface.co/papers/2609.38173)

We study robotic in-context learning (ICL), an emerging paradigm that enables robots to infer and execute tasks from visual demonstrations. Despite its growing promise, the problem itself remains under-defined: a visual demonstration simultaneously conveys action trajectories, object semantics, manipulation affordances, spatial relations, and task goals, making it unclear what information the robot is actually…

## 40. TestPrism: Rethinking Test Evaluation Beyond a Single Reference

- 分数：23.0  ·  HF 赞：14  ·  来源：huggingface
- 兴趣命中：agent, evaluation, language model, large language, coding
- 作者：Han Li, Lingxiang Hu, Jiacheng Huang, Ziqian Jiang, Jingkai Luo, Wei Gao, Yunfan Tan, Zun Wang, Jiaheng Liu
- 链接：[arXiv](https://arxiv.org/abs/2610.12289) · [PDF](https://arxiv.org/pdf/2610.12289) · [HF](https://huggingface.co/papers/2610.12289)

Large language model (LLM) coding agents have advanced test generation across diverse programming tasks. However, the common practice of evaluating tests against a single reference solution overlooks alternative valid implementations and can overstate test quality. We introduce TestPrism, comprising 300 test tasks from 17 sources and 3000 candidate implementations, evenly split between valid and invalid solutions.…

## 41. OneSearch-VL: Unified Multimodal Deep Research Agent for Image and Video

- 分数：23.0  ·  HF 赞：6  ·  来源：huggingface + arxiv
- 兴趣命中：agent, evaluation, benchmark, spec, retrieval
- 作者：Hongyu Li, Manyuan Zhang, Kaituo Feng, Shu Chen, Dian Zheng, Hao Li, Hao Yu, Zhangquan Chen, Zoey Guo, Ray Zhang, Shaofei Huang, Tianrui Hui, Linjiang Huang, Si Liu
- 链接：[arXiv](https://arxiv.org/abs/2610.12419) · [PDF](https://arxiv.org/pdf/2610.12419) · [HF](https://huggingface.co/papers/2610.12419)

Single-image, multi-image, and video deep research require different visual operations but share a workflow of visual grounding, external retrieval, and fact composition. A key challenge is to preserve the dependencies linking localized visual anchors, entity relations, source-supported facts, and answer-producing operations. We introduce OneSearch-VL, a unified agent centered on the Visually Grounded Evidence Graph…

## 42. Minimal Witness Reinforcement Learning

- 分数：22.5  ·  HF 赞：17  ·  来源：huggingface
- 兴趣命中：reinforcement learning, language model, large language
- 作者：T. Y. Tsui, Zihao Ye, Pengxiang Cai, Yanchao Li, Yuqiang Li, Zhehong Ai
- 链接：[arXiv](https://arxiv.org/abs/2610.07226) · [PDF](https://arxiv.org/pdf/2610.07226) · [HF](https://huggingface.co/papers/2610.07226)

``What are the irreducible conditions that are sufficient to produce an outcome?'' is one of the most common questions that recur across computation and science. Its answers, the minimal sufficient witnesses, are what we mean by explanations, mechanisms and reasons. These problems usually ask for multiple minimal witnesses, yet standard RL methods may reveal only one solution or redundant ones. We formalize this…

## 43. AdSpark: A Large-Scale Dataset and Benchmark for Product-Centric Advertisement Video Generation

- 分数：22.5  ·  HF 赞：17  ·  来源：huggingface
- 兴趣命中：evaluation, benchmark, spec
- 作者：Zhifei Yang, Zhao Jiang, Keyang Lu, Honghe Zhu, Zheng Zhang, Jingjing Lv, Changping Peng, Ching Law, Zhen Xiao
- 链接：[arXiv](https://arxiv.org/abs/2610.10047) · [PDF](https://arxiv.org/pdf/2610.10047) · [HF](https://huggingface.co/papers/2610.10047)

Product-centric advertisement video generation aims to create promotional videos that preserve fine-grained product identity while presenting selling points through coherent multi-shot narratives. However, this emerging task remains underexplored due to the lack of large-scale advertisement-specific datasets and comprehensive evaluation frameworks. To address this gap, we introduce AdSpark, a large-scale dataset and…

## 44. A self-learning scientific agent for X-ray diffraction

- 分数：22.0  ·  HF 赞：12  ·  来源：huggingface
- 兴趣命中：agent, evaluation, language model, spec
- 作者：Bin Cao, Huichi Zhou, Runyu Yang, Jingsong Li, Shuchen Sun, Yan Song, Hanyu Gao, Zhongwei Yu, Tong-Yi Zhang, Jun Wang
- 链接：[arXiv](https://arxiv.org/abs/2610.07862) · [PDF](https://arxiv.org/pdf/2610.07862) · [HF](https://huggingface.co/papers/2610.07862)

A central challenge for scientific agents is to turn analytical experience into reusable expertise grounded in physical evidence. Here we introduce Gan Jiang, a self-learning agent for powder X-ray diffraction built on a diffraction-analysis ecosystem we developed: XMatcher, XQueryer, XDecomposer and WPEM. Together, these engines span phase identification, multiphase decomposition and physics-constrained…

## 45. OuroWorld: Bringing Any 3D World Alive as Diverse, Endlessly Looping 3D Cinemagraphs

- 分数：22.0  ·  HF 赞：12  ·  来源：huggingface + arxiv
- 兴趣命中：evaluation, language model
- 作者：You-Zhe Xie, Ting-Wei Chou, Yu-Hsuan Li, Kaipeng Zhang, Zhixiang Wang, Yu-Lun Liu
- 链接：[arXiv](https://arxiv.org/abs/2610.12461) · [PDF](https://arxiv.org/pdf/2610.12461) · [HF](https://huggingface.co/papers/2610.12461)

Recent 3D world models generate photorealistic, explorable scenes that remain frozen in time. OuroWorld is a mask-free framework that turns any static 3D Gaussian Splatting scene into a 3D cinemagraph: a dynamic scene with vivid, diverse motion looping seamlessly from any viewpoint. A vision-language model infers plausible dynamics and guides a video model to synthesize a reference video, which we lift and complete…

## 46. SpaceCast-Bench: Evaluating Predictive Spatial Reasoning in Vision-Language Models

- 分数：22.0  ·  HF 赞：4  ·  来源：huggingface + arxiv
- 兴趣命中：reasoning, benchmark, language model, spec
- 作者：Hongxing Li, Jinyue Su, Dingming Li, Wenqi Zhang, Weiming Lu, Jun Xiao, Yueting Zhuang, Yongliang Shen
- 链接：[arXiv](https://arxiv.org/abs/2610.12402) · [PDF](https://arxiv.org/pdf/2610.12402) · [HF](https://huggingface.co/papers/2610.12402)

Existing spatial reasoning benchmarks mainly test spatial perception: reading off relations already visible in the input. Yet real-world spatial intelligence demands predictive spatial reasoning: constructing a scene from observations, anticipating how an intervention changes it, and reasoning about the unseen outcome. We introduce SpaceCast-Bench, the first benchmark to directly and diagnostically evaluate this…

## 47. NAMVIS: Next-Scale Autoregressive Multi-View Image Synthesis

- 分数：21.5  ·  HF 赞：19  ·  来源：huggingface
- 兴趣命中：evaluation, coding
- 作者：Ramil Khafizov, Ilya Statsenko, Ruslan Rakhimov, Artem Komarichev, Peter Wonka, Evgeny Burnaev
- 链接：[arXiv](https://arxiv.org/abs/2610.04722) · [PDF](https://arxiv.org/pdf/2610.04722) · [HF](https://huggingface.co/papers/2610.04722)

Sparse-view novel view synthesis is a central problem in 3D content creation, but diffusion-based approaches remain limited by iterative denoising, making multi-view generation expensive at inference time. We introduce NAMVIS, a diffusion-free framework that reformulates multi-view image synthesis as geometry-conditioned next-scale autoregression. Instead of generating target views through repeated denoising, NAMVIS…

## 48. Inverting Multi-Vector Visual Document Indices

- 分数：21.5  ·  HF 赞：19  ·  来源：huggingface
- 兴趣命中：benchmark, language model
- 作者：Zhuchenyang Liu, Yao Zhang, Yu Xiao
- 链接：[arXiv](https://arxiv.org/abs/2610.09920) · [PDF](https://arxiv.org/pdf/2610.09920) · [HF](https://huggingface.co/papers/2610.09920)

Prevailing multi-vector visual document retrievers store each page as about a thousand patch vectors, often in vector databases run by a third party. Since no one can read a page from its vectors, this index is easily treated as less sensitive than the page. However, because the index keeps one vector per patch in raster order, and each vector is computed by a vision-language model pre-trained to read documents, we…

## 49. DLoop: Looped Speculative Decoding

- 分数：21.5  ·  HF 赞：11  ·  来源：huggingface
- 兴趣命中：language model, large language, coding, spec
- 作者：Geonmo Gu, Byeongho Heo, HeeJae Jun, Yoohoon Kang, Sangmin Lee, Sangdoo Yun, Dongyoon Han
- 链接：[arXiv](https://arxiv.org/abs/2610.07659) · [PDF](https://arxiv.org/pdf/2610.07659) · [HF](https://huggingface.co/papers/2610.07659)

Speculative decoding accelerates autoregressive generation in large language models. In each drafting stage, a lightweight draft model proposes tokens that the target model subsequently verifies. With increasingly capable draft models, we find that the target model frequently accepts all tokens produced in a drafting stage. A verification nevertheless follows each drafting stage, resulting in unnecessary…

## 50. Reasoning-Informed Visual Editing

- 分数：21.5  ·  HF 赞：3  ·  来源：huggingface + arxiv
- 兴趣命中：agent, reasoning, evaluation, benchmark, planning
- 作者：Xue Yang, Peiyuan Zhang, Yilun Zhu, Qihao Yang, Mingxin Liu, Xiangyu Zhao, Ziqian Fan, Zhaokai Wang, Yan Li, Yifan Yang, Xu Yang, Xiaosong Jia, Yue Zhou, Zhihang Zhong, Junchi Yan
- 链接：[arXiv](https://arxiv.org/abs/2610.12343) · [PDF](https://arxiv.org/pdf/2610.12343) · [HF](https://huggingface.co/papers/2610.12343)

Large Multi-modality Models (LMMs) have made significant progress in visual understanding and generation, but still face challenges in visual editing, particularly in following complex instructions, preserving appearance consistency, and supporting flexible input formats. To study this gap, we introduce RISEBench, the first benchmark for evaluating Reasoning-Informed viSual Editing (RISE), and extend it to…

## 51. Recurrent Looped Transformer

- 分数：21.0  ·  HF 赞：26  ·  来源：huggingface
- 兴趣命中：-
- 作者：Yifan Zhang, Jichen Feng, Shihan Qin
- 链接：[arXiv](https://arxiv.org/abs/2610.07591) · [PDF](https://arxiv.org/pdf/2610.07591) · [HF](https://huggingface.co/papers/2610.07591)

State tracking requires an update at every input, but the depth a Transformer applies to each token is fixed regardless of sequence length. We introduce the Recurrent Looped Transformer (RLT), which splits its layers between a parallel causal encoder and a recurrent decoder. At each token, the decoder merges the encoder output with the previous token's final decoder state, so the computation path grows with sequence…

## 52. From Prompting to Composing: A Spatial Canvas Interface for Poster Generation

- 分数：21.0  ·  HF 赞：6  ·  来源：huggingface + arxiv
- 兴趣命中：agent, benchmark, spec
- 作者：Yitong Wang, Fangyun Wei, Jinjing Zhao, Sirui Zhang, Hongyang Zhang, Dong Chen, Bo Dai, Yan Lu
- 链接：[arXiv](https://arxiv.org/abs/2610.12230) · [PDF](https://arxiv.org/pdf/2610.12230) · [HF](https://huggingface.co/papers/2610.12230)

Text prompting is an indirect interface for poster generation, requiring users to encode inherently two-dimensional composition intent into a one-dimensional sequence of words. We introduce a Spatial Canvas Interface that enables users to directly compose generation intent in space through four complementary binding types: semantic, identity, text, and pixel, together with Text Specifications for individual elements…

## 53. OmniCapBench: A Deep-Structured Evaluation Framework for Fine-Grained Audio-Visual Captioning

- 分数：21.0  ·  HF 赞：2  ·  来源：huggingface + arxiv
- 兴趣命中：reasoning, evaluation, benchmark, language model, large language
- 作者：Zhongyu Yang, Jiale Tao, Ruitao Chen, Zuhao Yang, Yingfang Yuan, Xueliang Zhao, Auden, Kai Wang, Shuai Shao, Biao Wang, Steve Yves, Qinglin Lu
- 链接：[arXiv](https://arxiv.org/abs/2610.12458) · [PDF](https://arxiv.org/pdf/2610.12458) · [HF](https://huggingface.co/papers/2610.12458)

Multimodal large language models (MLLMs) are rapidly evolving toward continuous audio--visual reasoning, creating an urgent need for evaluations that expose their capability limits. Audio--visual captioning is an ideal diagnostic task, yet current benchmarks face a coupled trade-off: whole-caption scores provide coverage without localization, local probes provide localization without coverage, and unconstrained LLM…

## 54. Mobile-4DGS: Unified Static-Dynamic Real-time Mobile Gaussian Splatting

- 分数：20.0  ·  HF 赞：16  ·  来源：huggingface
- 兴趣命中：agent, spec
- 作者：Xiaobiao Du, Beixi Hao, Zhen Fang, Tianqing Zhu, Richard Hartley, Xin Yu
- 链接：[arXiv](https://arxiv.org/abs/2610.05289) · [PDF](https://arxiv.org/pdf/2610.05289) · [HF](https://huggingface.co/papers/2610.05289)

Recent advances in 3D Gaussian Splatting (3DGS) have achieved remarkable performance in novel view synthesis, yet deploying both static and dynamic Gaussian representations on resource-constrained mobile devices remains challenging due to heavy storage, redundant primitives, and costly per-frame computation. We present Mobile-4DGS, a unified lightweight framework for high-fidelity real-time static and dynamic…

## 55. Learning Multimodal Embeddings with Evidence-Aligned Readout

- 分数：20.0  ·  HF 赞：8  ·  来源：huggingface
- 兴趣命中：language model, large language, spec, retrieval
- 作者：Zirong Chen, Fuda Ye, Enjun Du, Junfu Pu, Xinlei Wang, Xinyu Zuo, Lisheng Duan, Haijin Liang, Jin Ma, Jiachuan Wang, Yongqi Zhang
- 链接：[arXiv](https://arxiv.org/abs/2609.33659) · [PDF](https://arxiv.org/pdf/2609.33659) · [HF](https://huggingface.co/papers/2609.33659)

Multimodal large language models can expose task-relevant evidence through generation, but producing useful evidence does not by itself determine how it enters a retrieval embedding. We study whether the semantic organization of that evidence can also specify where representations are read. To address this question, we introduce EviAlign, which couples Semantic Evidence Generation with Boundary Readout in a shared…

## 56. BrickBench: Evaluating Agentic Brick Design

- 分数：20.0  ·  HF 赞：0  ·  来源：huggingface + arxiv
- 兴趣命中：agent, benchmark, coding, spec
- 作者：Peter Kulits, Yiqing Xu, R. Kenny Jones, Cordelia Schmid, Jiajun Wu
- 链接：[arXiv](https://arxiv.org/abs/2610.12452) · [PDF](https://arxiv.org/pdf/2610.12452) · [HF](https://huggingface.co/papers/2610.12452)

We propose BrickBench, a benchmark for agentic text-conditioned LEGO-set design. Given a prompt, an agent is tasked with producing an assembly that not only satisfies semantic and design criteria, but that can also be physically built. To do so, it must select parts from a discrete library and reason jointly about local and global constraints. We score validity, alignment, and design across three settings that vary…

## 57. LEGO: A Lifting-Free Approach for Exocentric-to-Egocentric Video Generation

- 分数：19.5  ·  HF 赞：15  ·  来源：huggingface + arxiv
- 兴趣命中：-
- 作者：Suhwan Cho, Yonwoo Choi, Soongjin Kim, Jicheol Park, Taegyu Lim
- 链接：[arXiv](https://arxiv.org/abs/2610.12442) · [PDF](https://arxiv.org/pdf/2610.12442) · [HF](https://huggingface.co/papers/2610.12442)

Generating an egocentric video from a single exocentric recording is a challenging case of novel view synthesis, as the two cameras share little overlap and much of the target view is unobserved. Current state-of-the-art methods reconstruct the scene explicitly by estimating depth, lifting the video into a point cloud, and re-rendering it from the egocentric camera to condition a video diffusion model. This…

## 58. SheetSage2: Coherent Lead-Sheet Transcription with Synthetic Supervision

- 分数：19.5  ·  HF 赞：7  ·  来源：huggingface
- 兴趣命中：evaluation, benchmark, coding, spec
- 作者：Junyan Jiang, Ruibin Yuan, Jiahao Pan, Wei Xue, Yike Guo, Gus Xia, Yann LeCun
- 链接：[arXiv](https://arxiv.org/abs/2610.05336) · [PDF](https://arxiv.org/pdf/2610.05336) · [HF](https://huggingface.co/papers/2610.05336)

Transcribing music into a human-readable score requires a coherent understanding of rhythm, harmony, melody, and form. Two obstacles limit this goal: annotated recordings are scarce, and accurate local predictions can still produce inconsistent musical sequences. We present SheetSage2, a unified music transcription framework that combines synthetic data, task-specific structured decoding, and autoregressive…

## 59. SkillForge: Co-Evolving Skills and Agents via Dynamic Skill Lifecycles

- 分数：19.5  ·  HF 赞：7  ·  来源：huggingface
- 兴趣命中：agent, memory, reinforcement learning, evaluation, benchmark
- 作者：Yuyao Ge, Yiwei Wang, Yuchen He, Baolong Bi, Lingrui Mei, Jiayu Yao, Lizhe Chen, Shenghua Liu
- 链接：[arXiv](https://arxiv.org/abs/2610.09832) · [PDF](https://arxiv.org/pdf/2610.09832) · [HF](https://huggingface.co/papers/2610.09832)

Memory-augmented reinforcement learning strengthens LLM agents' ability to solve complex long-horizon tasks. Skills are one such form of memory, pairing instructions with an applicability condition over task types. However, retaining every skill indiscriminately as the policy improves lets obsolete or harmful entries accumulate and mislead the agent. We propose SkillForge, an agentic RL method that compiles and…

## 60. Internalizing Agent Experience into Diffusion Model Weights via On-Policy Context Distillation

- 分数：19.0  ·  HF 赞：10  ·  来源：huggingface
- 兴趣命中：agent, memory, benchmark
- 作者：Wenxuan Wang, Zekai Liu, Weinan Zhang, Yu Cheng, Yang Yang
- 链接：[arXiv](https://arxiv.org/abs/2610.07250) · [PDF](https://arxiv.org/pdf/2610.07250) · [HF](https://huggingface.co/papers/2610.07250)

Wrapping an image generation model in an agentic harness can effectively boost Text-to-Image task performance: the harness can leverage memory, skills, workflow orchestration, result verification, and iterative refinement to continually construct and revise prompts, thereby eliciting better images. These gains, however, remain external to the diffusion model and are realized only while the full harness runs. We…

## 61. CADFather: Autonomous CAD Reconstruction through Coordinated Tool Use

- 分数：19.0  ·  HF 赞：10  ·  来源：huggingface
- 兴趣命中：agent, tool use, spec
- 作者：Gennadiy Savrasov, Maksim Elistratov, Nikita Gavrilov, Albert Garifullin, Oleg Pavlov, Soslan Kabisov, Vladimir Frolov, Anton Konushin, Andrey Kuznetsov, Dmitrii Zhemchuzhnikov
- 链接：[arXiv](https://arxiv.org/abs/2610.09127) · [PDF](https://arxiv.org/pdf/2610.09127) · [HF](https://huggingface.co/papers/2610.09127)

Reconstructing an editable CAD model from a 3D shape remains a challenging engineering task. Existing methods can propose CAD operations, but no single source of proposals works equally well across different part geometries and stages of reconstruction. We introduce CADFather, an autonomous agentic system that coordinates complementary tools to recover parametric CAD programs from 3D meshes. A vision-language…

## 62. UniSkill: Learning Actor-Aligned Skill Proposals for an Evolving Policy

- 分数：19.0  ·  HF 赞：6  ·  来源：huggingface
- 兴趣命中：agent, language model, large language, spec
- 作者：Yifei Lu, Cheng Liu, Dianzhi Yu, Hui Xiang, Ji Zhang, Yuanchu Xiao, Rong Liang
- 链接：[arXiv](https://arxiv.org/abs/2610.10164) · [PDF](https://arxiv.org/pdf/2610.10164) · [HF](https://huggingface.co/papers/2610.10164)

Large language model agents can improve across tasks by retaining reusable skills distilled from prior interactions. Recent work jointly optimizes task execution and skill extraction, enabling the policy and skillbank to co-evolve. However, as the actor continues learning, rewarding skill proposals through their reuse in subsequent training steps may conflate skill benefits with actor improvement, while directly…

## 63. EngramEdit: Decoupled Knowledge Updates in LLMs through Conditional Memory

- 分数：19.0  ·  HF 赞：6  ·  来源：huggingface
- 兴趣命中：memory, reasoning, language model, large language
- 作者：Hongru Cai, Ran Wei, Wenjie Wang, Chengfa Wu, Ning Song, Yongqi Li, Wenjie Li
- 链接：[arXiv](https://arxiv.org/abs/2610.10533) · [PDF](https://arxiv.org/pdf/2610.10533) · [HF](https://huggingface.co/papers/2610.10533)

Conditional memory architectures such as DeepSeek Engram use input n-grams to look up learned embeddings, expanding the capacity of large language models (LLMs) with limited additional computation. Beyond model scaling, this architecture has demonstrated the potential to decouple factual knowledge storage from general-purpose computation, offering a promising route to updating factual knowledge while keeping the…

## 64. Accurate but Not Humble: Evaluating Epistemic Humility in LLM Agents under Knowledge Conflict

- 分数：19.0  ·  HF 赞：2  ·  来源：huggingface + arxiv
- 兴趣命中：agent, evaluation, language model
- 作者：Kaiser Sun, Bernal Jimenez Gutierrez, Hongjun Liu, Jingyu Zhang, Jie Gao, Mark Dredze, Daniel Khashabi
- 链接：[arXiv](https://arxiv.org/abs/2610.12360) · [PDF](https://arxiv.org/pdf/2610.12360) · [HF](https://huggingface.co/papers/2610.12360)

When retrieved evidence contradicts an agent's prior beliefs, does it revise its answer, acknowledge uncertainty, or persist with an incorrect conclusion? Existing evaluations of agentic systems focus primarily on task success, offering limited insight into how agents handle such conflicts. We propose to evaluate agents on epistemic humility (EH): the agent's willingness to recognize, act on, and communicate…

## 65. Inherit-MAS: Test-Time Evolution of Multi-Agent Systems through Workflow and Execution Inheritance

- 分数：18.5  ·  HF 赞：5  ·  来源：huggingface
- 兴趣命中：agent, benchmark, language model, large language, spec
- 作者：Songtao Wei, Yi Li, Zhichun Guo, Bingzhe Li
- 链接：[arXiv](https://arxiv.org/abs/2610.02396) · [PDF](https://arxiv.org/pdf/2610.02396) · [HF](https://huggingface.co/papers/2610.02396)

Multi-agent systems (MAS) built from large language models coordinate specialized agents to tackle complex tasks, but effective workflows are difficult to design in advance. Test-time evolution refines workflows using execution feedback, yet broad revisions can disturb useful components, while re-executing unchanged requests can incur redundant computation. Inspired by the interplay of inheritance and selection in…

## 66. Distilling Routed 3D Privilege for Spatial Reasoning in Vision-Language Models

- 分数：18.5  ·  HF 赞：1  ·  来源：huggingface + arxiv
- 兴趣命中：reasoning, benchmark, language model
- 作者：Hongxing Li, Yixin Li, Dingming Li, Zixuan Wang, Yuchen Yan, Wenqi Zhang, Weiming Lu, Yongliang Shen
- 链接：[arXiv](https://arxiv.org/abs/2610.12355) · [PDF](https://arxiv.org/pdf/2610.12355) · [HF](https://huggingface.co/papers/2610.12355)

Spatial reasoning remains a persistent weakness of vision-language models (VLMs), because RGB inputs do not directly provide geometric evidence. Existing remedies either inject 3D into the model at inference, paying architecture and latency costs, or train with outcome rewards that supervise only the final answer. Spatial errors originate in perception: a misjudged depth or direction can be corrected only by the…

## 67. On-Policy Distillation with Negative-Policy Rollouts

- 分数：18.0  ·  HF 赞：16  ·  来源：huggingface
- 兴趣命中：reasoning
- 作者：Jaehui Hwang, Dongyoon Han, Sangdoo Yun, Byeongho Heo
- 链接：[arXiv](https://arxiv.org/abs/2610.07874) · [PDF](https://arxiv.org/pdf/2610.07874) · [HF](https://huggingface.co/papers/2610.07874)

On-policy distillation (OPD) has been widely studied as a post-training method in which a student model obtains token-level supervision from a stronger teacher on its own rollouts. Recent studies have improved OPD through alternative distillation reward formulations and teacher configurations, while the objective of distillation remains centered on mimicking the teacher. However, when a stronger teacher has limited…

## 68. SparseEngine: Sparse-First Inference Engine

- 分数：18.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：agent, memory, benchmark, coding, spec
- 作者：Jitai Hao, Quansheng Gu, Qiang Huang, Jun Yu
- 链接：[arXiv](https://arxiv.org/abs/2609.39068) · [PDF](https://arxiv.org/pdf/2609.39068) · [HF](https://huggingface.co/papers/2609.39068)

Long-context LLM agents accumulate interaction histories that strain KV-cache memory and attention computation. Although sparse attention reduces these costs, heterogeneous cache representations and workflows hinder integration with existing inference engines, while prior sparse-serving abstractions support only specific layouts or workflows. We present SparseEngine, a ground-up, sparse-first inference engine whose…

## 69. SpatialOPSD: Self-Distilling Spatial Intelligence from Verified Coding Agent Traces

- 分数：18.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：agent, reasoning, benchmark, language model, large language, coding
- 作者：Rongxue Li, Meng Yang, Yiru Mao, Yongliang Tao, Lulu Hu, Bin Yang, Zhao Xu, Weihua Luo, Bowen Xu
- 链接：[arXiv](https://arxiv.org/abs/2610.11366) · [PDF](https://arxiv.org/pdf/2610.11366) · [HF](https://huggingface.co/papers/2610.11366)

Spatial coding agents significantly improve spatial reasoning in Multimodal Large Language Models (MLLMs) by using external tools to generate verified execution traces. However, this paradigm inherently suffers from prohibitive inference-time overhead and external dependencies. In this paper, we explore whether an MLLM can internalize this agentic capability to operate entirely tool-free. We begin with a simple…

## 70. What Did the Agent Actually Do? Evidence-Grounded Oversight for Long-Horizon Agents

- 分数：17.5  ·  HF 赞：11  ·  来源：huggingface
- 兴趣命中：agent, benchmark
- 作者：Zhongxiang Sun, Jiahao Yan, Hongkang Zhao, Haojie Ding, Boheng Zhang, Fan Yang, Xiao Zhang, Jun Xu
- 链接：[arXiv](https://arxiv.org/abs/2610.06406) · [PDF](https://arxiv.org/pdf/2610.06406) · [HF](https://huggingface.co/papers/2610.06406)

As agents take on long-horizon tasks, users shift from making individual decisions to overseeing autonomous execution. Yet the volume of agent activity and the fragmentation of supporting evidence make it difficult to determine which decisions warrant user verification. We study monitors that identify consequential decisions and locate evidence to help users assess their implications. We introduce AgentMonBench, a…

## 71. Do LLMs Understand Sequential Structure? A Controlled Study of Inference and Generation

- 分数：17.0  ·  HF 赞：6  ·  来源：huggingface
- 兴趣命中：agent, language model, large language
- 作者：Jerry Wang, Zhengxiang Wang, Ting Yu Liu, Hsin-Ling Hsu, Yi-Cheng Lai, Tengfei Ma
- 链接：[arXiv](https://arxiv.org/abs/2610.04977) · [PDF](https://arxiv.org/pdf/2610.04977) · [HF](https://huggingface.co/papers/2610.04977)

Large language models (LLMs) are increasingly used as interactive agents and simulators, yet it remains unclear whether they can recover latent sequential structure beyond surface action frequencies. This distinction is critical for behavioral simulation, where actions are often shaped by prior context rather than marginal frequencies alone. We study this question using controlled two-player Rock--Paper--Scissors…

## 72. Rethinking World-Action Model for Compositional and In-Context Robotic Manipulation

- 分数：17.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：reasoning, benchmark, spec, planning
- 作者：Shukai Gong, Xuanran Zhai, Yintianrun Zhang, Ruopeng Cui, Ye Huang, Yiyang Fu, Dexuan Lyu, Chaojie Li, Xinyi Song, Peiwen Lin, Chuang Wang, Mingyuan Jia, Yufan Deng, Jiaxin Fang, Bo Liang, Jiaxin Li, Yuxiang Gao, Hao Liu, Daquan Zhou
- 链接：[arXiv](https://arxiv.org/abs/2610.02368) · [PDF](https://arxiv.org/pdf/2610.02368) · [HF](https://huggingface.co/papers/2610.02368)

Long-horizon compositional manipulation has become increasingly important for real-world robot deployment, where a single task involves multiple coordinated subtasks. Existing world-action models (WAMs) jointly predict short-horizon visual futures and actions, but typically lack explicit subtask-level reasoning. We propose Visual Goal-conditioned Action Reasoning (ViGAR), a hierarchical framework that factorizes…

## 73. Lineage-Aware Memory Governance: A Derivation-Gated Framework for Privacy-Preserving Column-Level Access Control in Enterprise AI Agents

- 分数：17.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：agent, memory, coding, retrieval
- 作者：Venkata M Sangaraju, Sudhir Vissa
- 链接：[arXiv](https://arxiv.org/abs/2610.07258) · [PDF](https://arxiv.org/pdf/2610.07258) · [HF](https://huggingface.co/papers/2610.07258)

Enterprise AI agents that share a memory store face two unaddressed risks: sensitive data can leak through legitimately computed results the requester could not derive, and departments can silently compute a same-named key performance indicator (KPI) through conflicting logic. Existing agent-memory systems (e.g., MemGPT, Zep, A-MEM) gate retrieval by content, ownership, and role, not derivation, missing a cached…

## 74. Real Long-Term Memory for AI: A 50-Million-Token Window That Is Faster and Cheaper Than Recompute

- 分数：17.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：memory, context window, benchmark, language model, large language
- 作者：Sietse Schelpe
- 链接：[arXiv](https://arxiv.org/abs/2610.10845) · [PDF](https://arxiv.org/pdf/2610.10845) · [HF](https://huggingface.co/papers/2610.10845)

A large language model can only use the text that fits in its context window, and it recomputes its internal key-value (KV) state for a prompt every time the prompt is sent. We test a memory layer, the public package galahad-kv, that saves the KV state of each block of about 16,000 tokens to encrypted local NVMe disk and loads it back later, byte-exact, without recomputing it. We ran it on 50,000,000 tokens of real…

## 75. Q-Learning with Scalar Adjoint Matching

- 分数：16.5  ·  HF 赞：17  ·  来源：huggingface
- 兴趣命中：-
- 作者：Yonghoon Dong, Minsung Yoon, Jaehyuk Kim, Jungwoo Park, Changyeon Kim, Jinwoo Shin
- 链接：[arXiv](https://arxiv.org/abs/2610.10437) · [PDF](https://arxiv.org/pdf/2610.10437) · [HF](https://huggingface.co/papers/2610.10437)

Flow policies capture rich and diverse action distributions, and fine-tuning them with off-policy RL to improve beyond the demonstrations has drawn growing interest. However, fine-tuning a flow policy against a learned value function is not trivial, because the policy generates its action over many flow steps. Adjoint matching offers a principled way to update the flow model itself by propagating value information…

## 76. ReSPO: Reshaped Sequence Policy Optimization for Gradient Starvation in Off-Policy Learning

- 分数：16.5  ·  HF 赞：5  ·  来源：huggingface
- 兴趣命中：reasoning, reinforcement learning, benchmark
- 作者：Yihang Chen, Yuanhao Ban, Cho-Jui Hsieh
- 链接：[arXiv](https://arxiv.org/abs/2609.35433) · [PDF](https://arxiv.org/pdf/2609.35433) · [HF](https://huggingface.co/papers/2609.35433)

Reinforcement learning from verifiable rewards (RLVR) frequently reuses rollouts across multiple policy updates, increasing the mismatch between the current policy and the data-generating policy. We identify a sign-dependent gradient starvation problem in clipped policy optimization: clipping suppresses under-generated positive responses at the low-importance-weight tail while permitting severely over-generated…

## 77. V-CoLA: Vision Token Compression with Linear Attention

- 分数：16.5  ·  HF 赞：5  ·  来源：huggingface
- 兴趣命中：benchmark, language model, spec
- 作者：Hao Jiang, Yiru Mao, Tianpeng Bu, Hao Zhou, Hongtao Duan, Wang Jing, Bowen Xu, Xin Chen, Lulu Hu, Bin Yang, Yongliang Tao, Minying Zhang
- 链接：[arXiv](https://arxiv.org/abs/2610.11251) · [PDF](https://arxiv.org/pdf/2610.11251) · [HF](https://huggingface.co/papers/2610.11251)

Vision-language models (VLMs) have demonstrated impressive capabilities but suffer from substantial computational overhead, as vision tokens dominate the input sequence. This motivates vision token compression as a key direction to alleviate the burden. However, with the emergence of hybrid architectures incorporating linear attention (\eg, Qwen3.5), prior methods designed for softmax attention struggle to…

## 78. AutoResearch at Production Scale: Failure Modes and a Multi-Agent Framework

- 分数：16.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：agent, memory, evaluation, language model, large language
- 作者：Aparajith Chandran, Juwon Kim, Saurav Jha, Pablo Castells, Florian Hottier
- 链接：[arXiv](https://arxiv.org/abs/2609.30541) · [PDF](https://arxiv.org/pdf/2609.30541) · [HF](https://huggingface.co/papers/2609.30541)

Optimizing embedding systems for production recommendation pipelines demands systematic exploration that consumes disproportionate engineering effort at scale. We apply Andrej Karpathy's AutoResearch paradigm -- a large language model that iteratively edits a training script and retains modifications that improve a held-out scalar metric -- to automate this exploration. We report on twelve weeks of running this…

## 79. MC-Sparse: Deconstructing and Closing the Dense-Sparse Attention Gap in Diffusion Transformers

- 分数：16.0  ·  HF 赞：16  ·  来源：huggingface
- 兴趣命中：-
- 作者：Jiarui Chen, Zeqiang Lai, Jiangshan Wang, Ziheng Ouyang, Ye Huang, Xiangyu Yue, Cewu Lu, Chunchao Guo
- 链接：[arXiv](https://arxiv.org/abs/2610.06801) · [PDF](https://arxiv.org/pdf/2610.06801) · [HF](https://huggingface.co/papers/2610.06801)

Sparse attention is a primary approach to reducing the latency of diffusion transformers in long-sequence generation tasks, such as video and high-resolution 3D asset generation. However, existing methods can degrade generation quality and fidelity at high sparsity levels. Through controlled oracle comparisons, we trace this degradation to three sources: constraints imposed by token grouping, inaccurate interaction…

## 80. QuadTok: Quadtree Visual Tokenizer for Autoregressive Image Generation

- 分数：16.0  ·  HF 赞：12  ·  来源：huggingface
- 兴趣命中：benchmark
- 作者：Yucheng Mao, Zeyuan Chen, Xiaojun Shan, Xiang Zhang, Divyansh Srivastava, Bingnan Li, Zhuowen Tu
- 链接：[arXiv](https://arxiv.org/abs/2610.10497) · [PDF](https://arxiv.org/pdf/2610.10497) · [HF](https://huggingface.co/papers/2610.10497)

We introduce QuadTok, a novel framework for visual tokenization and autoregressive image generation. Compared to traditional approaches using 2D grids or 1D token sequences, we propose a hierarchical quadtree structure, bridging the gap between 2D spatial binding and 1D sequence-level flexibility. The QuadTok tokenizer dynamically allocates representational capacity to visually intricate areas while leaving…

## 81. Composing What Each Teacher Learned: Multi-Teacher On-Policy Distillation through Teacher-Relative Shifts

- 分数：16.0  ·  HF 赞：8  ·  来源：huggingface
- 兴趣命中：benchmark, spec
- 作者：Hejian Sang, Zhengze Zhou, Shayan Mohajer Hamidi, Xiaomin Li, Rohit Jain, Alborz Geramifard
- 链接：[arXiv](https://arxiv.org/abs/2610.10460) · [PDF](https://arxiv.org/pdf/2610.10460) · [HF](https://huggingface.co/papers/2610.10460)

Multi-teacher on-policy distillation (MOPD) is used in two settings. In common-domain composition, several teachers score each student rollout from one prompt domain and their signals form a single target; in routed-domain distillation, prompts from different domains are assigned to the corresponding specialist. Both settings usually transfer each teacher's endpoint policy, which mixes what post-training changed…

## 82. USDCraft: Geometrically Grounded Programmatic Modeling of Articulated 3D Assets for Simulation

- 分数：16.0  ·  HF 赞：8  ·  来源：huggingface
- 兴趣命中：benchmark, spec
- 作者：Chuanrui Zhang, Zaijia Yang, Duomin Wang, Lu Shi, Daquan Zhou, Ruihua Zhang, Ziwei Wang
- 链接：[arXiv](https://arxiv.org/abs/2610.11322) · [PDF](https://arxiv.org/pdf/2610.11322) · [HF](https://huggingface.co/papers/2610.11322)

Geometrically faithful and functional articulated 3D assets are essential for real-to-sim robot manipulation, where policies trained in simulation must transfer to physical objects. Recent mesh-based methods learn to infer articulation from annotated 3D assets, but deployment remains challenging when real-world objects fall outside the training distribution or their meshes are incomplete or corrupted. To address…

## 83. SanSi: A Looped Typed Decision Model for System 1.5 Thinking

- 分数：16.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：reasoning, reinforcement learning, language model
- 作者：Shuyu Gan, Young-Jun Lee, Dongyeop Kang
- 链接：[arXiv](https://arxiv.org/abs/2610.07730) · [PDF](https://arxiv.org/pdf/2610.07730) · [HF](https://huggingface.co/papers/2610.07730)

Typed decision models answer a declared question without generating text: a decision head returns a probability for each of the declared options in a single forward pass. A single pass is fast, intuitive System 1 thinking. We study what lies between one pass and generated reasoning: looping, in which the same layers are recursively applied several times before one typed readout. Each loop lets the model revise its…

## 84. MARGIN: Runtime Confidence Calibration for Multi-Agent Foundation Model Coordination

- 分数：16.0  ·  HF 赞：0  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark, spec
- 作者：Joss Armstrong
- 链接：[arXiv](https://arxiv.org/abs/2605.22949) · [PDF](https://arxiv.org/pdf/2605.22949) · [HF](https://huggingface.co/papers/2605.22949)

When a coordinator compares answers from heterogeneous foundation models, self-reported confidence may have different meanings across responders and changing workloads. This paper presents MARGIN (Multi-Agent Runtime Grading via Incremental Normalisation), a runtime calibration method that learns model-specific confidence corrections from observed answer outcomes without retraining the models or requiring a held-out…

## 85. Embodied Turing Machines: Stateful Code for Robot Recursive Self-Improvement

- 分数：16.0  ·  HF 赞：0  ·  来源：huggingface + arxiv
- 兴趣命中：agent, coding
- 作者：Kairui Hu, Siyuan Hu, Fangzhou Hong, Zhaoxi Chen, Ziwei Liu
- 链接：[arXiv](https://arxiv.org/abs/2610.12369) · [PDF](https://arxiv.org/pdf/2610.12369) · [HF](https://huggingface.co/papers/2610.12369)

Most robot policies keep a model in the control loop: a VLA maps observations to actions, and an Agent Harness, such as Agent-as-Policy or Harness VLA queries a VLM for decision making at run time. We propose a different view: the embodied world is an Embodied Turing Machine, whose tape is the robot and environment state and rules are the policy. If this state can be represented accurately, the decision making can…

## 86. RoboQuest: Generalist Physical Agents that Search, Inspect and Test

- 分数：15.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：agent, benchmark, spec
- 作者：Liu Renhang, Navonil Majumder, Tej Deep Pala, Soujanya Poria
- 链接：[arXiv](https://arxiv.org/abs/2610.10388) · [PDF](https://arxiv.org/pdf/2610.10388) · [HF](https://huggingface.co/papers/2610.10388)

Recent advances in multimodal foundation models have made them capable generalist physical agents for a range of manipulation tasks. However, successful operation in an unfamiliar environment may require an agent to seek task-relevant information through interaction when it is absent from the observations: it may need to determine where a relevant object is, inspect an unobserved property, or discover the effect of…

## 87. Beyond the Parameter Monolith: Reconstructive Memories, Executable Skills, and Residual Assembly for Language Models

- 分数：15.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：memory, language model, retrieval
- 作者：A. Bochkov
- 链接：[arXiv](https://arxiv.org/abs/2610.04012) · [PDF](https://arxiv.org/pdf/2610.04012) · [HF](https://huggingface.co/papers/2610.04012)

Language-model systems can separate contextual computation, persistent storage, and exact execution instead of updating all capabilities through one shared parameter system. We investigate FEM-ASM, a finite-element-method-inspired organization in which independently constructed document states and deterministic executable skills contribute typed proposals to a shared language-model state. An explicit residual…

## 88. How corner is a corner case? Percentile control for highway scenario generation

- 分数：15.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：agent, evaluation, spec
- 作者：Jiaxi Liu, Hang Zhou, Hangyu Li, Yifan Wang, Keke Long, Chengyuan Ma, Bin Ran, Xiaopeng Li
- 链接：[arXiv](https://arxiv.org/abs/2610.05003) · [PDF](https://arxiv.org/pdf/2610.05003) · [HF](https://huggingface.co/papers/2610.05003)

Generating corner-case scenarios with appropriate adversity in a simulation environment is critical for testing an autonomous vehicle (AV) software stack's safety performance before deployment. Existing autonomous-driving scenario generators can enforce specific behavior, adversity, or feasibility conditions, but they provide limited control over how extreme a generated scenario is relative to plausible futures in…

## 89. RoboJEPA: Scaling Robotic Latent World Models

- 分数：15.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：agent, evaluation, planning
- 作者：Artem Zholus, Nicolas Beltran-Velez, Jianhao Yuan, Sarath Chandar, Tushar Nagarajan, Daniel Severo, Koustuv Sinha, Michal Drozdzal, Adriana Romero Soriano, Jeannette Bohg, Nicolas Ballas, Mahmoud Assran
- 链接：[arXiv](https://arxiv.org/abs/2610.10515) · [PDF](https://arxiv.org/pdf/2610.10515) · [HF](https://huggingface.co/papers/2610.10515)

Latent world models have shown a remarkable ability to predict future states and to plan in the real world. In practice, however, we lack a principled way to estimate how their capabilities scale with model size, data, and compute, an open problem that slows progress in the field. In this work we present RoboJEPA, a world model based on the Joint Embedding Predictive Architecture (JEPA) and trained on a large-scale…

## 90. System Switch: When Should a Fast Decision Model Stop and Think?

- 分数：15.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：agent, reasoning, language model
- 作者：Gian Luca Bailo
- 链接：[arXiv](https://arxiv.org/abs/2610.09683) · [PDF](https://arxiv.org/pdf/2610.09683) · [HF](https://huggingface.co/papers/2610.09683)

Dual-process agents pair a fast policy with a slow deliberative model. In real-time settings the slow model usually runs continuously; in turn-based agents and robot planners it is invoked on events such as uncertainty or a detected failure. We study a fast learned actor that takes every decision and hands control to a reasoning vision-language model only when a gate opens, while the game keeps running. We use…

## 91. ViSkill: Reinforcing VLM Agents with Evolving Visual-Native Skills

- 分数：15.0  ·  HF 赞：2  ·  来源：huggingface + arxiv
- 兴趣命中：agent
- 作者：Hongxing Li, Dingming Li, Yixin Li, Yong Du, Wenqi Zhang, Weiming Lu, Jun Xiao, Yueting Zhuang, Yongliang Shen
- 链接：[arXiv](https://arxiv.org/abs/2610.12403) · [PDF](https://arxiv.org/pdf/2610.12403) · [HF](https://huggingface.co/papers/2610.12403)

Skill-augmented agents improve sample efficiency by distilling successful trajectories into reusable strategies. Yet most existing approaches remain text-centric, linearizing spatial layouts and action-state correspondences into language that loses critical geometric structure. Recent efforts have begun incorporating visual evidence, but construct and update skills separately from policy optimization, leaving their…

## 92. Post-Training Frontier Text-to-Image Models by Composing Preference and Rubric Rewards

- 分数：14.5  ·  HF 赞：13  ·  来源：huggingface
- 兴趣命中：-
- 作者：Yuanhao Ban, I-Hung Hsu, Anastasios Angelopoulos, Wei-Lin Chiang, Ion Stoica, Cho-Jui Hsieh
- 链接：[arXiv](https://arxiv.org/abs/2610.02967) · [PDF](https://arxiv.org/pdf/2610.02967) · [HF](https://huggingface.co/papers/2610.02967)

Recent text-to-image generation models have achieved remarkable visual quality, but improving them through post-training remains challenging because no single reward signal captures the full range of human preference. In this work, we develop a simple and effective post-training recipe for open-domain text-to-image generation based on the composition of complementary reward signals. Our reward system consists of two…

## 93. Improving Proactive AI Assistance with Hierarchical Procedural Understanding

- 分数：14.5  ·  HF 赞：9  ·  来源：huggingface
- 兴趣命中：evaluation
- 作者：Jin-Seop Lee, TaeYeon Won, SeongJun Jung, JungHoon Kim, Boyang Albert Li, JinYeong Bak, Jaehong Yoon, Jee-Hyong Lee
- 链接：[arXiv](https://arxiv.org/abs/2610.06505) · [PDF](https://arxiv.org/pdf/2610.06505) · [HF](https://huggingface.co/papers/2610.06505)

Proactive AI assistants continuously observe a user's activity and decide whether to provide new guidance or remain silent. They should provide appropriate guidance for the task, determine when to provide the next guidance based on task progress, and adjust the guidance level to the user's expertise and needs. Supporting these capabilities requires training and evaluation data that reflect procedural structure and…

## 94. Chaos in the Text: Revealing the Modality Preference in Mixed-Modality Retrievers

- 分数：14.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：benchmark, retrieval
- 作者：Yubo Sun, Chunyi Peng, Yukun Yan, Zhenghao Liu, Zhipeng Xu, Sen Mei, Linlin Xin, Zheni Zeng, Maosong Sun
- 链接：[arXiv](https://arxiv.org/abs/2610.11816) · [PDF](https://arxiv.org/pdf/2610.11816) · [HF](https://huggingface.co/papers/2610.11816)

Dense retrievers have made significant progress on text and image corpora, but whether these capabilities extend reliably to mixed corpora containing text, image, and fused text-image documents remains unclear. In this paper, we systematically examine retrievers across architectures and find that their performance is highly sensitive to modality composition. As image documents are progressively replaced with…

## 95. SPW-Nav: A Streaming Panoramic World Model for Language-Guided Navigation

- 分数：14.0  ·  HF 赞：0  ·  来源：huggingface
- 兴趣命中：agent, memory, spec
- 作者：Yunheng Liu, Ziqi Cai, Siqi Yang, Yimu Wang, Minggui Teng, Jiaming Tan, Shuchen Weng, Erwin Wu, Kaipeng Zhang, Boxin Shi
- 链接：[arXiv](https://arxiv.org/abs/2610.08941) · [PDF](https://arxiv.org/pdf/2610.08941) · [HF](https://huggingface.co/papers/2610.08941)

Language-guided panoramic video generation benefits various downstream applications, such as interactive 3D scene exploration, virtual reality experiences, and embodied agent training. Existing panoramic generators follow predefined trajectories, and interactive world models act through low-level actions in perspective views. We propose SPW-Nav, a streaming panoramic world model that understands movement…

## 96. On-Policy Distillation Teaches New Skills but Not New Knowledge

- 分数：14.0  ·  HF 赞：0  ·  来源：huggingface
- 兴趣命中：memory, reasoning, spec
- 作者：Yixuan Tang, Yi Yang
- 链接：[arXiv](https://arxiv.org/abs/2610.09639) · [PDF](https://arxiv.org/pdf/2610.09639) · [HF](https://huggingface.co/papers/2610.09639)

On-policy distillation (OPD) strengthens language-model reasoning, yet whether students acquire new factual knowledge or compositional skill for multi-step reasoning remains unknown. We separate these capabilities using a controlled synthetic framework that measures the student's initial capabilities and independently controls the teacher's additional facts, compositional skill, or both. Across four models from…

## 97. Foundations of Large Language Models

- 分数：14.0  ·  HF 赞：0  ·  来源：huggingface
- 兴趣命中：reasoning, language model, large language
- 作者：Tong Xiao, Jingbo Zhu
- 链接：[arXiv](https://arxiv.org/abs/2501.09223) · [PDF](https://arxiv.org/pdf/2501.09223) · [HF](https://huggingface.co/papers/2501.09223)

This is a book about large language models. As indicated by the title, it primarily focuses on foundational concepts rather than comprehensive coverage of all cutting-edge technologies. The book is structured into six main chapters, each exploring a key area: pre-training, generative models, prompting, alignment, inference, and reasoning. It is intended for college students, professionals, and practitioners in…

## 98. Retrieval-Centric Deep Learning in Growing Nonparametric Neural Networks

- 分数：13.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：spec, retrieval
- 作者：Maximilian Schlegel, Rajai Nasser, Seijin Kobayashi, Yanick Schimpf, Oliver Sieberling, Robert Obryk, Kazuki Irie, João Sacramento, Johannes von Oswald
- 链接：[arXiv](https://arxiv.org/abs/2610.03858) · [PDF](https://arxiv.org/pdf/2610.03858) · [HF](https://huggingface.co/papers/2610.03858)

We investigate a general-purpose layer for deep learning that, instead of compressing arbitrary-size training data into fixed-size weight matrices, stores a new pair of key-value representations for every data point during training, and retrieves and recombines these representations through an attention mechanism at inference time - resulting in a growing neural net (NN). While Irie et al. (arXiv:2202.05798) have…

## 99. PAMI: Part Anchored Motion for Text to Human-Object Interaction Generation

- 分数：13.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：coding, spec
- 作者：Chuqiao Li, Xianghui Xie, Yong Cao, Andreas Geiger, Gerard Pons-Moll
- 链接：[arXiv](https://arxiv.org/abs/2609.38466) · [PDF](https://arxiv.org/pdf/2609.38466) · [HF](https://huggingface.co/papers/2609.38466)

Text-conditioned full-body human-object interaction (HOI) generation requires synthesizing human motion and object trajectories that match the input text while remaining precisely coordinated over time. Most methods represent the human and object as separate trajectories and predict the global human-object couplings. Learning this complex, dynamically changing relationship implicitly, however, often yields object…

## 100. Agent Plasticity: Measuring Self-Improvement Through Experience

- 分数：13.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：agent, evaluation
- 作者：Harman Singh, Anton Bakhtin, Rulin Shao, Gabriel Synnaeve, Ilia Kulikov, Rob Fergus, Sanjeev Arora, Kurt Keutzer, Jason Weston, Anuj Mahajan, Anirudh Goyal
- 链接：[arXiv](https://arxiv.org/abs/2610.08902) · [PDF](https://arxiv.org/pdf/2610.08902) · [HF](https://huggingface.co/papers/2610.08902)

AI agents increasingly operate in environments where they can diagnose failures and improve through experience, yet existing evaluations largely measure what an agent can do at a fixed point in time rather than how effectively it learns. Evaluating self-improvement requires answering three questions: does future performance improve and generalize beyond the interactions that enabled learning; how efficiently are new…

## 101. Scaling to Tens of Thousands of Test-Time Iterations with Loop-Native Attention Residuals

- 分数：13.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：memory, reasoning
- 作者：Pengxiang Li, Dilxat Muhtar, Di He, Guinan Su, Lu Yin, Shiwei Liu
- 链接：[arXiv](https://arxiv.org/abs/2610.11570) · [PDF](https://arxiv.org/pdf/2610.11570) · [HF](https://huggingface.co/papers/2610.11570)

In this paper, we argue that looped Transformers need their own residual connections to prevent performance degradation as the number of iterations grows. We observe that increasing loop iterations can reduce reasoning accuracy: noisy state updates overwrite correct intermediate deductions and even undo completed solutions. This leaves subsequent iterations to recover lost information from an already degraded…

## 102. StepCAD: Mesh-to-CAD Code Generation via LLM Policy and Geometry-Guided Search

- 分数：12.5  ·  HF 赞：5  ·  来源：huggingface
- 兴趣命中：benchmark
- 作者：Ghadi Nehme, Faez Ahmed
- 链接：[arXiv](https://arxiv.org/abs/2610.03799) · [PDF](https://arxiv.org/pdf/2610.03799) · [HF](https://huggingface.co/papers/2610.03799)

Recovering executable CAD programs from 3D meshes is challenging due to the compositional nature of CAD construction and the interaction between discrete modeling choices and continuous parameters. Many learning-based methods predict complete programs in a single pass and rely predominantly on sketch-extrude representations, limiting operation diversity and opportunities to correct geometric errors during…

## 103. Co-Evolving Robot Orchestrators and Policies through Deployment

- 分数：12.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：agent, language model
- 作者：Xilun Zhang, Maggie Wang, Erik Bauer, Hong-Xing Yu, Huang Huang, Jiajun Wu, Marco Pavone
- 链接：[arXiv](https://arxiv.org/abs/2610.09228) · [PDF](https://arxiv.org/pdf/2610.09228) · [HF](https://huggingface.co/papers/2610.09228)

Vision-language-action (VLA) policies trained on large datasets are capable within their training domains, yet they still fail to generalize to the variety of situations a robot meets in real-world deployment. Agentic robot systems complement the policy with a vision-language model (VLM) orchestrator that learns when to call the policy, how to instruct it, and when to use scripted skills instead. However, because…

## 104. TerraVis: Towards Evaluation of World-Grounded Visual Consistency in Text-to-Image Generation via MLLM Workflows

- 分数：12.0  ·  HF 赞：0  ·  来源：huggingface
- 兴趣命中：evaluation, benchmark
- 作者：Shuai Fu, Jing Gu, Jian Zhou, Zicheng Duan, Gengze Zhou, Qi Wu
- 链接：[arXiv](https://arxiv.org/abs/2610.02959) · [PDF](https://arxiv.org/pdf/2610.02959) · [HF](https://huggingface.co/papers/2610.02959)

Recent text-to-image models have made substantial progress in photorealism, aesthetics, and text-image alignment. Yet visually appealing images can still violate real-world plausibility, exhibiting malformed object structures, impossible anatomy, physically implausible interactions, or inconsistent spatial relationships. Such failures are not well captured by existing fidelity, aesthetics, preference, or alignment…

## 105. Iris-3B: Going Beyond the Latent with Pixel-Space Diffusion Training, Conversion and Fine-Tuning

- 分数：11.5  ·  HF 赞：7  ·  来源：huggingface
- 兴趣命中：-
- 作者：Hanqiu Li Cai, Chema Garabito
- 链接：[arXiv](https://arxiv.org/abs/2610.09450) · [PDF](https://arxiv.org/pdf/2610.09450) · [HF](https://huggingface.co/papers/2610.09450)

Pixel-space diffusion models avoid the lossy VAE of latent models, which suggests an advantage on downstream tasks where fine-grained detail matters. We test this claim along both routes to a pixel-space backbone. We pretrain Iris-3B, a 3B-parameter pixel-space text-to-image transformer, from scratch through a 256to512to1024 curriculum, after first ablating the prediction target and representation alignment at 256^2…

## 106. Salt++: Context-Aligned Post-Training for Few-Step Streaming Multimodal Generation

- 分数：11.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：evaluation
- 作者：Xingtong Ge, Yutong Wang, Lunjie Zhu, Haitao Lin, Fangyu Lin, Yushi Huang, Xin Zhang, Yi Zhang, Yu Liu, Jun Zhang
- 链接：[arXiv](https://arxiv.org/abs/2609.36995) · [PDF](https://arxiv.org/pdf/2609.36995) · [HF](https://huggingface.co/papers/2609.36995)

Few-step streaming audio--video generation requires both causal modeling and step distillation, yet standard training recipes face two context-related challenges. Teacher forcing pairs clean history with a noisy target, but supervises predictive contextual representations only indirectly through velocity prediction. Meanwhile, directly reusing bidirectional score models in causal Distribution Matching Distillation…

## 107. FastOPD: On-Policy Distillation for Lightweight VLA Deployment

- 分数：11.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：spec
- 作者：Yoojin Oh, Jeongsol Kim, Yeonwoo Seo, Jangho Park, Seonghyun Jin, Sunwoo Park, Youngmin Kim, Youngjun Jun, Kyumin Choi, Jong Chul Ye
- 链接：[arXiv](https://arxiv.org/abs/2610.02832) · [PDF](https://arxiv.org/pdf/2610.02832) · [HF](https://huggingface.co/papers/2610.02832)

Vision-Language-Action (VLA) foundation models have scaled rapidly to enhance manipulation performance and generalizability, but this scaling incurs high computational costs that render real-world deployment increasingly challenging. Existing approaches typically mitigate this issue by designing smaller architectures or reducing the iterative denoising steps in flow-based policies. In this work, we propose FastOPD,…

## 108. TIDES: Implicit Time-Awareness in Selective State Space Models

- 分数：11.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：benchmark
- 作者：Taylan Soydan, Miguel A. Bessa, Dirk Mohr, Rui Barreira
- 链接：[arXiv](https://arxiv.org/abs/2605.09742) · [PDF](https://arxiv.org/pdf/2605.09742) · [HF](https://huggingface.co/papers/2605.09742)

Selective state space models (SSMs), such as Mamba, achieve strong per-token expressivity by making the time discretization step TildeΔ a learned function of the input. However, in doing so, TildeΔ no longer equals the physical time gap Δ between consecutive observations, limiting the ability of these models to handle irregular time series. Continuous time SSMs, such as S5, keep TildeΔequivΔ and therefore handle…

## 109. Task-Sufficient Contraction: Source Selection for Machine Information Interfaces

- 分数：11.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：spec
- 作者：Joss Armstrong
- 链接：[arXiv](https://arxiv.org/abs/2610.08884) · [PDF](https://arxiv.org/pdf/2610.08884) · [HF](https://huggingface.co/papers/2610.08884)

A declared task can sometimes certify a reduced source before a downstream encoder, codebook, rate, distortion target, or optimizer is chosen. This paper studies when one such reduction preserves the complete downstream problem family, a property termed Task-Sufficient Contraction. The reduced source is fixed by the task before the later operating point is selected. An exact contraction allows the later problem to…

## 110. CoDance: Learning Reactive and Compliant Human-Humanoid Interaction from Video

- 分数：9.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：-
- 作者：Zhuoqun Chen, Shucheng Jia, Boyuan Chen
- 链接：[arXiv](https://arxiv.org/abs/2610.05324) · [PDF](https://arxiv.org/pdf/2610.05324) · [HF](https://huggingface.co/papers/2610.05324)

Partnered human-humanoid interaction couples locomotion with continuous physical contact. A humanoid needs to coordinate with a person's motion while responding to interaction forces and maintaining stable and natural movement. We present CoDance, a framework for learning reactive and compliant human-humanoid interaction from video. We study partnered dancing as a challenging instantiation, where a humanoid…

## 111. DSReg: Provably Recovering Individual World Latents without Reconstruction

- 分数：9.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：-
- 作者：Yujia Zheng, David Klindt, Randall Balestriero, Bernhard Schölkopf
- 链接：[arXiv](https://arxiv.org/abs/2610.09457) · [PDF](https://arxiv.org/pdf/2610.09457) · [HF](https://huggingface.co/papers/2610.09457)

Methods that recover individual latent variables of the world, from nonlinear ICA to dictionary learning and causal representation learning, anchor the latents to observations through reconstruction, auxiliary supervision, or distributional asymmetries such as non-Gaussianity. Methods without these anchors, including joint-embedding predictive architectures (JEPAs), identify the latent state only up to a linear…

## 112. Safe Actions Alone Do Not Ensure Safe Agents: Identifying Unfulfilled Obligations with Guard Models

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, evaluation, benchmark, spec
- 作者：Youwei Feng, Yitong Zhang, Yuetong Liu, Jia Li
- 链接：[arXiv](https://arxiv.org/abs/2610.11773) · [PDF](https://arxiv.org/pdf/2610.11773) · [HF](https://huggingface.co/papers/2610.11773)

Guard models are increasingly used to safeguard LLM-based agents, primarily by identifying actions that agents are forbidden to perform. However, identifying forbidden actions alone is insufficient to ensure agent safety. In this paper, we argue that agent safety also depends on identifying required yet unperformed safety-critical actions, which we call obligations. Our preliminary study on a popular benchmark for…

## 113. Memento 3: Model-Based Recursive Self-Improvement through Reflective Rulebooks

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, memory, spec, planning
- 作者：Haoyu Zhao, Zhengxu Yu, Zhiyuan He, Meng Fang, Rasul Tutunov, Haitham Bou-Ammar, Weilin Luo, Jun Wang
- 链接：[arXiv](https://arxiv.org/abs/2610.11794) · [PDF](https://arxiv.org/pdf/2610.11794) · [HF](https://huggingface.co/papers/2610.11794)

Learning to act in unfamiliar environments requires agents to infer how the world works and revise that understanding as new evidence arrives. Yet limited observations can support multiple world models that explain past interactions but predict different outcomes in unseen states. We introduce Memento 3, building on the Memento series to enable frozen LLM agents to continually learn explicit world models through…

## 114. Seek-and-View Reasoning for Multi-View Spatial Understanding

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, benchmark, language model, planning
- 作者：Qixiang Chen, Cheng Zhang, Fucai Ke, Chi-Wing Fu, Jianfei Cai, Jingwen Ye
- 链接：[arXiv](https://arxiv.org/abs/2610.11810) · [PDF](https://arxiv.org/pdf/2610.11810) · [HF](https://huggingface.co/papers/2610.11810)

Existing approaches to multi-view spatial reasoning operate largely on sparse input views. Vision-language models (VLMs) are thus restricted to understand a scene and infer spatial relations within these fixed views, leading to fragile cross-view alignment and geometry-to-language bottleneck. To address these issues, we formulate a novel Seek-and-View reasoning approach to find implicit cross-view spatial evidence…

## 115. GRPODropout: Less is More for Online Reinforcement Learning Rollouts

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, reinforcement learning, language model, large language, spec
- 作者：Hexuan Deng, Zihao Yan, Xuebo Liu, Shuo Nie, Yue Wang, Chen Wang, Zhaohua Zhang, Tianwen Jiang, Qiuyong Xiao, Jihong Zhang, Min Zhang
- 链接：[arXiv](https://arxiv.org/abs/2610.11854) · [PDF](https://arxiv.org/pdf/2610.11854) · [HF](https://huggingface.co/papers/2610.11854)

Reinforcement learning (RL) methods such as GRPO substantially improve large language model reasoning but often suffer from policy entropy collapse: the loss of sampling diversity weakens exploration and limits further improvement. Existing methods address this issue either through algorithm-level interventions, such as reward modification and entropy/KL regularization, or through token-level reweighting. We…

## 116. Automated Assembly Instruction Generation from CAD Models Using Grounded Large Language Models: A Human-in-the-Loop Framework

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, language model, large language, planning
- 作者：Aaron Dsouza, Mohammed Azeez Khan, Ashutosh Mishra, Arshaan Khan, Neha K. Nair, Amar Kumar Behera
- 链接：[arXiv](https://arxiv.org/abs/2610.11896) · [PDF](https://arxiv.org/pdf/2610.11896) · [HF](https://huggingface.co/papers/2610.11896)

Assembly documentation is a downstream manufacturing artifact that is still usually authored by interpreting CAD models by hand. Structured product data and large language models are both available, yet studies of CAD interpretation, assembly sequence planning, instruction writing, and human oversight have largely proceeded separately. This paper formulates CAD-grounded assembly instruction generation: the…

## 117. Forms of LLM-Integrated Applications from LLM-Chats to Autonomous AI Agent System

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, tool use, language model, large language, coding, retrieval
- 作者：Irene Weber
- 链接：[arXiv](https://arxiv.org/abs/2610.11899) · [PDF](https://arxiv.org/pdf/2610.11899) · [HF](https://huggingface.co/papers/2610.11899)

Large language models (LLMs) are increasingly embedded as components in software systems, marketed under labels such as chatbot, copilot, retrieval-augmented generation, workflow, coding agent and AI agent. Whether these labels denote genuine architectural forms or serve as branding has not been assessed systematically. In the sources surveyed, labels do carry architectural content, most clearly in vendor usage:…

## 118. From Surface to Depth: Towards Cognitive Appraisal Reasoning in Multimodal Emotion Understanding

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, benchmark, language model, large language, spec
- 作者：Jia Li, Yichao He, Yangchen Yu, Qiankun Li, Xinyi Li, Baiyi Ye, Zhenzhen Hu, Richang Hong, Erik Cambria
- 链接：[arXiv](https://arxiv.org/abs/2610.11918) · [PDF](https://arxiv.org/pdf/2610.11918) · [HF](https://huggingface.co/papers/2610.11918)

Recent multimodal large language models (MLLMs) increasingly incorporate explainable reasoning for emotion understanding. However, reasoning based mainly on observable affective cues can reduce emotion understanding to superficial cue-label associations, giving rise to the Clever Hans effect. Such shortcuts become unreliable when affective cues are implicit, conflicting across modalities, linguistically misleading,…

## 119. Event-Centric Memory with Query-Aware Graph Augmentation for Long-Term Conversational Agents

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, memory, reasoning, benchmark, retrieval
- 作者：Yichen Liu, Chunfeng Yuan, Haowei Liu, Wenjuan Li, Zefeng Lin, Bing Li, Xu Chen, Weiming Hu
- 链接：[arXiv](https://arxiv.org/abs/2610.11920) · [PDF](https://arxiv.org/pdf/2610.11920) · [HF](https://huggingface.co/papers/2610.11920)

For persistent and personalized conversational agents, memory systems can enable them to remember, update, and reason over long histories by storing past interactions and retrieving relevant information. Existing memory systems typically follow two paradigms: flat-structured memory and graph-based memory. The former is lightweight but leaves event relations and state updates implicit, while the latter explicitly…

## 120. Can LLMs Fix It Without Code? Toward Automated Verification of No-Code Bug Fixes

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, evaluation, benchmark, language model, large language, spec
- 作者：Utku Boran Torun, Veli Karakaya, Eray Tüzün
- 链接：[arXiv](https://arxiv.org/abs/2610.11963) · [PDF](https://arxiv.org/pdf/2610.11963) · [HF](https://huggingface.co/papers/2610.11963)

A no-code fix resolves an invalid bug report by directing the user to change a setting, update to a version where the problem is already fixed, or adjust their workflow. Manually verifying whether a proposed no-code fix resolves the reported bug takes considerable developer time. This study proposes an automated, execution-based pipeline for evaluating the capability of large language models (LLMs) to generate…
