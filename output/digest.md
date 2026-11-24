# 每日 AI 论文

生成时间：2026-11-24 09:54 UTC  ·  共 120 篇（已按 arXiv ID 去重）

来源：Hugging Face Daily Papers + arXiv（cs.AI / cs.LG / cs.CL / cs.CV）。
排序：HF 上榜、点赞、多源命中、兴趣词。兴趣词可在 `config.json` 改。

## 1. WeMM-Ecom: Advancing Multimodal Content Understanding for WeChat E-Commerce

- 分数：40.0  ·  HF 赞：43  ·  来源：huggingface + arxiv
- 兴趣命中：reinforcement learning, evaluation, benchmark, language model, large language, spec
- 作者：Binhui Xie, Jinmin Li, Haomiao Tang, Guangting Wang, Song Jin, Jianwei Zhu, Fengyun Rao, Jing Lyu
- 链接：[arXiv](https://arxiv.org/abs/2611.30662) · [PDF](https://arxiv.org/pdf/2611.30662) · [HF](https://huggingface.co/papers/2611.30662)

We present WeMM-Ecom, a family of multimodal large language models that deliver frontier e-commerce capabilities while achieving state-of-the-art general-purpose performance at their respective scales. The family spans five sizes, from a 0.8B dense model to a 35B mixture-of-experts model with 3B active parameters. Our training pipeline begins with two-stage continued pre-training that progressively raises the…

## 2. Embo-Harness: Towards Understanding Frontier-Model-as-Policy Harness

- 分数：36.0  ·  HF 赞：71  ·  来源：huggingface
- 兴趣命中：agent, tool use, tool-use, reasoning, planning
- 作者：Xiao-Ming Wu, Kang Liao, Yuexiao Ma, Taolin Zhang, Mingqian Zhou, Nuo Chen, Ziming Li, Yihang Luo, Rui Li, Zhonghua Wu, Tianyu Xie, Xiawu Zheng, Zhongang Cai, Zhi Hou, Chen Change Loy
- 链接：[arXiv](https://arxiv.org/abs/2611.31201) · [PDF](https://arxiv.org/pdf/2611.31201) · [HF](https://huggingface.co/papers/2611.31201)

Frontier multimodal models exhibit extraordinary generalization in generating robot actions from observations and instructions, enabling a new paradigm in which they serve directly as policies within closed-loop robotic harnesses. However, the design principles of such harnesses, and the capabilities underlying their strong performance, remain unclear. We present Embo-Harness, a framework for systematically studying…

## 3. 3AGameFactory-Motion: Agentic Rigging and Reliable Complex Motion Generation for Diverse 3D Assets

- 分数：36.0  ·  HF 赞：44  ·  来源：huggingface
- 兴趣命中：agent, benchmark, language model, large language, spec
- 作者：Bohan Zeng, Kaixin Zhu, Yifan Yang, Dongge Yu, Zihao Wu, Yifan Dai, Zhou Liu, Junbo Niu, Xiaochen Ma, Shiran Ge, Zimo Meng, Junzhu Liang, Huanyao Zhang, Jinhang Liu, Tianqi Xiao, Jinhao Zhang, Tianyi Bai, Zhixiong Zeng, Penghao Zhao, Yuanbo Peng, Key Zhang, Wentao Zhang
- 链接：[arXiv](https://arxiv.org/abs/2611.30013) · [PDF](https://arxiv.org/pdf/2611.30013) · [HF](https://huggingface.co/papers/2611.30013)

Animating arbitrary 3D assets from instructions requires both structural inference and motion control, yet existing motion benchmarks mostly cover conventional human or animal skeletons with simple instructions. We introduce DivDynBench, which evaluates rigging and motion generation across six morphology categories, with instructions requiring multi-phase part coordination and explicit timing, angle, repetition, and…

## 4. Clover-35B-A3B-Preview Technical Report

- 分数：36.0  ·  HF 赞：40  ·  来源：huggingface
- 兴趣命中：agent, memory, evaluation, language model
- 作者：DiffuSpace Technical Team
- 链接：[arXiv](https://arxiv.org/abs/2611.24636) · [PDF](https://arxiv.org/pdf/2611.24636) · [HF](https://huggingface.co/papers/2611.24636)

We introduce Clover-35B-A3B-Preview (Clover), a mixture-of-experts diffusion language model with 35 billion total parameters and 3 billion activated parameters, supporting thinking-mode generation. Clover adapts Gated Delta Networks to block diffusion by combining recurrent memory of previously generated context with bidirectional softmax attention inside the current block. Historical memory readout competes with…

## 5. Motion Mamba 2.0: Autoregressive Diffusion Mamba for Long-Horizon Humanoid Control

- 分数：34.0  ·  HF 赞：106  ·  来源：huggingface
- 兴趣命中：agent, memory, evaluation
- 作者：Yue Huang, Tianshan Zhang, Zeyu Zhang, Jayeon Kang, Akide Liu, Sungjoon Choi, Dacheng Tao, Hao Tang
- 链接：[arXiv](https://arxiv.org/abs/2611.29897) · [PDF](https://arxiv.org/pdf/2611.29897) · [HF](https://huggingface.co/papers/2611.29897)

Long-horizon, real-time controllable motion generation is essential for interactive animation and humanoid robotics, where an agent must respond to changing instructions and spatial goals while moving. Existing autoregressive diffusion methods generate motion incrementally, but bounded attention caches limit access to distant history, while repeated denoising introduces substantial inference overhead. We present…

## 6. Non-penetrating World Models

- 分数：34.0  ·  HF 赞：56  ·  来源：huggingface
- 兴趣命中：evaluation, benchmark, spec
- 作者：Yuhang Dai, Yinwei Wu, Ziyue Lin, Han Ji, Xingyi Yang
- 链接：[arXiv](https://arxiv.org/abs/2611.27963) · [PDF](https://arxiv.org/pdf/2611.27963) · [HF](https://huggingface.co/papers/2611.27963)

We study a new problem of preventing object penetration in interactive video world models. To understand how existing models handle this, we introduce NoPeBench, a benchmark that evaluates how world models respond to physical obstacles. Our evaluation reveals that none of the open-source models can reliably prevent such failures. Surprisingly, however, these models already encode the information needed to predict…

## 7. Learning Video Foresight Reasoning from Unlabeled Videos via On-Policy Self-Distillation

- 分数：34.0  ·  HF 赞：43  ·  来源：huggingface
- 兴趣命中：reasoning, language model, planning
- 作者：Jingchen Sun, Jiaxing Zhang, Qingqiao Hu, Dingqiang Ye, Yuqi Jia, Yijun Liang, Di Fu, Yunjie Tian, Dongdi Zhao, Changyou Chen
- 链接：[arXiv](https://arxiv.org/abs/2611.26954) · [PDF](https://arxiv.org/pdf/2611.26954) · [HF](https://huggingface.co/papers/2611.26954)

Video foresight reasoning requires vision-language models to anticipate future events or next actions from currently observed videos. Existing methods fit future captions, rationales, or full visual states, but face two limitations. First, they rely on annotations or external large models for supervision, limiting scalability. We address this with an on-policy self-distillation framework that turns past-future video…

## 8. WorldLeague: Benchmarking Physical Agency

- 分数：31.0  ·  HF 赞：30  ·  来源：huggingface
- 兴趣命中：agent, memory, benchmark, language model, planning
- 作者：Xinyang Zhou, Qi Li, Xinchao Wang
- 链接：[arXiv](https://arxiv.org/abs/2611.30989) · [PDF](https://arxiv.org/pdf/2611.30989) · [HF](https://huggingface.co/papers/2611.30989)

AI systems can now operate Blender, follow instructions in complex video games, and manipulate objects with robot arms. What range of physical goals can today's AI systems achieve autonomously? Answering this question requires testing systems on tasks that demand different combinations of perception, memory, planning, and action. We introduce WorldLeague, a benchmark that compares AI systems on a common set of 60…

## 9. ViDecide: Teaching Video Diffusion Models to Reason and Plan Step by Step

- 分数：28.5  ·  HF 赞：29  ·  来源：huggingface
- 兴趣命中：reasoning, benchmark, planning
- 作者：Kaiwen Zhang, Yiming Gao, Zeqi Xiao, Xintao Wang, Pengfei Wan, Kun Gai, Xingang Pan
- 链接：[arXiv](https://arxiv.org/abs/2611.26389) · [PDF](https://arxiv.org/pdf/2611.26389) · [HF](https://huggingface.co/papers/2611.26389)

Current leading video generation models can synthesize highly realistic videos, while still frequently violating physical and logical constraints in multi-step reasoning and planning, even after training with large-scale reasoning data or existing diffusion RL methods. We attribute these failures to the conventional video training paradigm, which treats a solution as a fixed-length clip rather than a chain of…

## 10. cmHC: Balancing Stream Mixing in Hyper-Connections via Geometric Contraction

- 分数：28.0  ·  HF 赞：94  ·  来源：huggingface
- 兴趣命中：-
- 作者：Haowei He, Ziwen Zhao, Chenshuo Pan, Gang Lin, Zhihao Yang, Chao Wang, Xinzhang Liu, Kaidong Yu, Han Gao, Dongfang Li, Menglin Yang, Shuangyong Song, Yongxiang Li
- 链接：[arXiv](https://arxiv.org/abs/2611.27193) · [PDF](https://arxiv.org/pdf/2611.27193) · [HF](https://huggingface.co/papers/2611.27193)

Manifold-constrained Hyper-Connections (mHC) extends residual connections to multiple streams and stabilizes residual propagation by constraining stream-mixing residual matrices to the Birkhoff polytope, the set of doubly stochastic matrices. In this work, we investigate how to effectively mix residual streams within the Birkhoff polytope. We reveal a mixing trade-off: when under-mixed residual matrices stay close…

## 11. MemOnce: A Scalable Memory Architecture for Large Language Models

- 分数：28.0  ·  HF 赞：24  ·  来源：huggingface
- 兴趣命中：memory, language model, large language, coding, spec
- 作者：Chang Nie, Chaoyou Fu, Songlin Liu, Yiqing Hu, Caifeng Shan
- 链接：[arXiv](https://arxiv.org/abs/2611.27973) · [PDF](https://arxiv.org/pdf/2611.27973) · [HF](https://huggingface.co/papers/2611.27973)

Deploying large language models (LLMs) in long-horizon and continual interactions requires maintaining reusable memory states for future inference, posing challenges for existing architectures. Standard Transformers accumulate layer-wise, token-level KV caches, incurring linear GPU memory growth and quadratic computational complexity as the context expands. In contrast, linear-time architectures compress history…

## 12. Reading the Unreadable: Text-Aware Image Super-Resolution Needs Reasoning

- 分数：27.0  ·  HF 赞：22  ·  来源：huggingface
- 兴趣命中：reasoning, benchmark, language model, large language, spec
- 作者：Jaeseong Lee, Jinwoo Kim, Jinho Jeong, Seon Joo Kim
- 链接：[arXiv](https://arxiv.org/abs/2611.15449) · [PDF](https://arxiv.org/pdf/2611.15449) · [HF](https://huggingface.co/papers/2611.15449)

Text-aware image super-resolution (TAISR) aims to recover high-resolution images from low-resolution inputs while preserving textual content. Existing methods treat this as a visual restoration problem, yet severely degraded text often cannot be read from local visual evidence alone. Humans instead read it by reasoning over image context, logical patterns, and prior knowledge. This raises a fundamental question:…

## 13. A Glimpse of Training VLMs as Foundation Models for Robotic Manipulation

- 分数：26.5  ·  HF 赞：25  ·  来源：huggingface
- 兴趣命中：benchmark, language model, spec
- 作者：Meng-Hao Guo, Yi Zhang, Zhe-Han Mo, Han-Zheng Wang, Jia-Jun Wang, Xin-Sheng Chen, Jiaxi Song, Yi-Xuan Deng, Jia-Ning Li, Xuanyu Chu, Hengrui Zhang, Huan-ang Gao, Yongming Rao, Shi-Min Hu
- 链接：[arXiv](https://arxiv.org/abs/2611.29338) · [PDF](https://arxiv.org/pdf/2611.29338) · [HF](https://huggingface.co/papers/2611.29338)

Recently, GPT-6 Astra demonstrates strong generalization in robot control, yet limited disclosure of its training leaves open how such capabilities can be reproduced. We introduce nanoAstra, an approach to training vision-language models (VLMs) for generalizable manipulation that combines semantic action modeling with capability-preserving supervised fine-tuning (CP-SFT). nanoAstra represents robot behavior as…

## 14. Plan4D: Generative Plannable 4D Worlds

- 分数：23.5  ·  HF 赞：27  ·  来源：huggingface
- 兴趣命中：spec
- 作者：Hangwei Zhang, Rujing Dang, Ruimin Lin, Jiahong Wu, Xiangxiang Chu, Chuanxia Zheng
- 链接：[arXiv](https://arxiv.org/abs/2611.26516) · [PDF](https://arxiv.org/pdf/2611.26516) · [HF](https://huggingface.co/papers/2611.26516)

Most world models for future prediction prioritize aestetic quality of generated videos, but offer only weak physical grounding and limited geometric consistency over time, due to the lack of explicit 4D modeling. In this paper, we introduce plan4d, a possible next milestone towards building a generative plannable 4D world model that predicts future RGB videos together with dense 4D geometry, including depth,…

## 15. AutoPILOT: A Visual Agent Harness for Real-Time Gameplay

- 分数：23.5  ·  HF 赞：27  ·  来源：huggingface
- 兴趣命中：agent
- 作者：Mark Zhao, Pengcheng Wang, Rui Yang, Jiarui Yao, Xirui Jiang, Yuxi Chen, Bingxuan Li, Hanyang Chen, Ke Yang, Manling Li, Tong Zhang, Huan Zhang
- 链接：[arXiv](https://arxiv.org/abs/2611.28202) · [PDF](https://arxiv.org/pdf/2611.28202) · [HF](https://huggingface.co/papers/2611.28202)

Multimodal foundation models can play video games well when the game waits for them, but often fail when it keeps running. We find that much of this gap lies in the harness, which decides what the model sees, what it remembers, and how its outputs become actions over time. Existing harnesses such as VISTA improve the first two, yet turn each model call into at most one action, so the agent acts only as often as its…

## 16. RUIBench: What Makes a Good Robot-Use Interface?

- 分数：22.5  ·  HF 赞：17  ·  来源：huggingface + arxiv
- 兴趣命中：agent
- 作者：Yanzhe Chen, Zhijun Cao, Zechen Bai, Wenzheng Zeng, Kevin Yuchen Ma, Yiqi Lin, Guoqiang Liang, Xiaokang Liu, Ke Sun, Kevin Qinghong Lin, Mike Zheng Shou
- 链接：[arXiv](https://arxiv.org/abs/2611.31115) · [PDF](https://arxiv.org/pdf/2611.31115) · [HF](https://huggingface.co/papers/2611.31115)

Foundation models can reason about complex physical tasks, yet translating this intelligence into reliable robot execution remains challenging. We argue that a critical, often overlooked factor is the robot-use interface (RUI), which determines how agents express and execute physical actions. To systematically study its impact, we introduce RUIBench, comprising 30 manipulation tasks across five suites spanning world…

## 17. GameDojo: Benchmarking Real-Time Interactive Agents in Video Games

- 分数：22.5  ·  HF 赞：5  ·  来源：huggingface + arxiv
- 兴趣命中：agent, benchmark, coding, spec
- 作者：Kuan Zhang, Zhihao Yang, Yukun Chen, Xingyilang Yin, Mingyu Ouyang, Yue Su, Xiangnan Wu, Jiaming Li, Longze Chen, Run Luo, Zirong Chen, Lu Wang, Yiming Li
- 链接：[arXiv](https://arxiv.org/abs/2611.30771) · [PDF](https://arxiv.org/pdf/2611.30771) · [HF](https://huggingface.co/papers/2611.30771)

Interactive intelligence requires agents to act on observations and adapt to the consequences of actions. Studying these abilities calls for diverse, challenging tasks under controlled conditions. We introduce GameDojo, a controllable interactive gameplay benchmark of 120 boss encounters across 20 games for evaluating model capabilities, learning algorithms, and agent harnesses. Coding agents reconstruct the…

## 18. GameAnything: From Any Inspirations to Playable Game Worlds

- 分数：22.0  ·  HF 赞：12  ·  来源：huggingface
- 兴趣命中：agent, memory, evaluation, benchmark, coding, spec
- 作者：Wenyi Wu, Siqi Liu, Yuru Feng, Zixuan Song, Aayush Salvi, Sibo Zhu, Kun Zhou, Biwei Huang
- 链接：[arXiv](https://arxiv.org/abs/2611.29238) · [PDF](https://arxiv.org/pdf/2611.29238) · [HF](https://huggingface.co/papers/2611.29238)

AI-driven game development holds the potential to transform diverse human inspirations into interactive experiences. However, existing systems and benchmarks primarily focus on explicit development specifications, with limited support for adapting multimodal references and evaluating actual gameplay experiences. We introduce GameAnything, an open-source agentic platform that transforms multimodal inspirations into…

## 19. DiLE: Discrimination-Aware Latent-Space Learning for Universal Multimodal Embeddings

- 分数：21.5  ·  HF 赞：11  ·  来源：huggingface
- 兴趣命中：reasoning, language model, large language, spec, retrieval
- 作者：Ben Kang, Junda Wang, Yuxuan Yuan, Hang Li, Yuhan Liu, Xin Chen, Wanting Geng, Tong Lin, Pei Fu, Dong Wang, Jian Luan, Huchuan Lu
- 链接：[arXiv](https://arxiv.org/abs/2611.25419) · [PDF](https://arxiv.org/pdf/2611.25419) · [HF](https://huggingface.co/papers/2611.25419)

Multimodal large language models have greatly improved input understanding in universal multimodal embedding models. However, this understanding does not ensure that their embeddings preserve the evidence needed to distinguish relevant items from confusable alternatives. To preserve essential discriminative evidence in embeddings, this paper proposes DiLE, a discrimination-aware latent-space learning framework that…

## 20. Lost in the Hallway: Benchmarking Persistent Spatial Memory Across Revisits

- 分数：21.0  ·  HF 赞：10  ·  来源：huggingface
- 兴趣命中：agent, memory, reasoning, evaluation, benchmark
- 作者：Henry Zheng, Weibo Gong, Yang Yue, Rui Huang, Yang Zhang, Gao Huang
- 链接：[arXiv](https://arxiv.org/abs/2611.21485) · [PDF](https://arxiv.org/pdf/2611.21485) · [HF](https://huggingface.co/papers/2611.21485)

Persistent spatial understanding is essential for embodied agents to operate reliably in environments they repeatedly encounter. It requires recognizing revisited places despite viewpoint changes, distinguishing them from similar-looking rooms, and updating memories as environments change. Yet existing evaluations often leave physical place identity across separated visits implicit. We introduce ReSpaceBench, a…

## 21. From Rewarding What Models Say to How They Think: Attention Process Reward Model for LLM Reinforcement Learning

- 分数：20.0  ·  HF 赞：0  ·  来源：huggingface + arxiv
- 兴趣命中：reasoning, reinforcement learning, language model, large language
- 作者：Kairong Han, Nuanqiao Shan, Ziyu Zhao, Xinpeng Dong, Zijing Hu, Dian Jin, Leyan Deng, Junjian Ye, Lujia Pan, Fei Wu, Kun Kuang
- 链接：[arXiv](https://arxiv.org/abs/2611.30627) · [PDF](https://arxiv.org/pdf/2611.30627) · [HF](https://huggingface.co/papers/2611.30627)

Reinforcement learning (RL) has become an important component in large language models (LLMs). However, existing RL approaches focus on final outputs or textual solution trajectories, leading to coarse-grained rewards and unreliable reasoning. Such paradigms focus mainly on what the model outputs while overlooking how the model internally reasons. Therefore, can we reward how a model thinks internally rather than…

## 22. Polytropos: What Do Vision-Language Model Descriptions Make of a Cultural Object?

- 分数：19.5  ·  HF 赞：11  ·  来源：huggingface
- 兴趣命中：benchmark, language model, spec
- 作者：Yuechen Jiang, Enze Zhang, Yuyan Wang, Mohsinul Kabir, Chenying Lin, Sijia Li, Qianqian Xie, Stavroula Golfomitsou, Konstantinos Arvanitis, Sophia Ananiadou
- 链接：[arXiv](https://arxiv.org/abs/2611.29355) · [PDF](https://arxiv.org/pdf/2611.29355) · [HF](https://huggingface.co/papers/2611.29355)

Vision-language models have become a new kind of describer, writing about almost anything people see, and their descriptions now shape how cultures are known by people and by other models. Descriptions of cultures tend to turn particular things into types, and what a description loses shows what its describer lacks. We introduce Polytropos, a benchmark that measures what model descriptions of cultural objects keep…

## 23. Embodied-Harness: Towards Recursive Self-Improvement for Robotic Manipulation

- 分数：19.5  ·  HF 赞：7  ·  来源：huggingface
- 兴趣命中：agent, memory, reasoning, evaluation, benchmark, language model, spec, planning
- 作者：Zhenxuan Fan, Zhuoya Wang, Yuqian Yuan, Wenqiao Zhang, Juncheng Li, Jun Xiao, Siliang Tang, Yueting Zhuang
- 链接：[arXiv](https://arxiv.org/abs/2611.27689) · [PDF](https://arxiv.org/pdf/2611.27689) · [HF](https://huggingface.co/papers/2611.27689)

Vision-language model (VLM)-based agents offer a promising approach to robotic manipulation, yet remain limited by inadequate memory organization, uncertain failure attribution, and limited reuse of execution experience. We propose Embodied-Harness, a dual-agent framework that improves manipulation by refining the execution harness without updating model parameters. The Actor interacts with the environment through a…

## 24. Duopra: From Full-Duplex Conversation to Full-Duplex Agency

- 分数：19.0  ·  HF 赞：18  ·  来源：huggingface
- 兴趣命中：agent
- 作者：Chiyu Chen, Pengzhou Cheng, Yuezhao Ma, Xiaocheng Li, Can Liu, Haonan Hu, Yao Yao, Yifei Yang, Yijie Lu, Taolei Wang, Yansi Li, Muhuan Wu, Chenglu Sun, Gongshen Liu, Zhuosheng Zhang
- 链接：[arXiv](https://arxiv.org/abs/2611.25773) · [PDF](https://arxiv.org/pdf/2611.25773) · [HF](https://huggingface.co/papers/2611.25773)

Full-duplex interaction models exhibit strong conversational agency, enabling natural, low-latency turn-taking, backchannels, and interruptions. However, completing tasks further requires task agency: timely tool invocation and argument revision following user corrections. Frontend-backend agents separate initiation from execution: the frontend decides whether and what to request, while the backend determines how.…

## 25. World Models as Native Latent Action Models

- 分数：19.0  ·  HF 赞：10  ·  来源：huggingface + arxiv
- 兴趣命中：benchmark
- 作者：Qinyue Li, Weijie Qiao, Qingyi Tao, Zerui Gong, Zhe Yang, Quanzhou Li, Taolin Zhang, Jinglin He, Zhonghua Wu, Chen Change Loy
- 链接：[arXiv](https://arxiv.org/abs/2611.30898) · [PDF](https://arxiv.org/pdf/2611.30898) · [HF](https://huggingface.co/papers/2611.30898)

Large and diverse video sources, such as egocentric human video and heterogeneous robot recordings, carry rich dynamics but come either without actions or without a shared action space. Latent action models (LAMs) can recover these dynamics, but they train their inverse- and forward-dynamics models (IDM, FDM) from scratch, trading off pixel reconstruction against latent capacity and accuracy. Pretrained video world…

## 26. What Makes Good Data for Training Coding Agents? A Systematic Study on SWE-Gym

- 分数：19.0  ·  HF 赞：6  ·  来源：huggingface
- 兴趣命中：agent, reinforcement learning, coding, spec
- 作者：Yikai Zhang, Mai Xu, Yunbei Zhang, Qirui Jin, Kenan Li, Yuwen Jia, Jinwei Yao, Xiangyu Zhang, Jielun Tan, Jin Pan, Zijian Jin, Xiao Sun
- 链接：[arXiv](https://arxiv.org/abs/2611.30207) · [PDF](https://arxiv.org/pdf/2611.30207) · [HF](https://huggingface.co/papers/2611.30207)

Reinforcement learning (RL) trains coding agents on software tasks whose hidden tests decide the reward, yet task collections check these tests only against the reference fix. We ask what makes a task good training data, focusing on the correctness of its reward labels. We audit SWE-Gym with two LLM families, and a suspected error counts only if execution reproduces it. We find that unsolved often means mislabelled:…

## 27. SynthDCB: World Distillation for Scalable Device Control Benchmarking

- 分数：18.5  ·  HF 赞：5  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark, spec
- 作者：Zichen Zhu, Dingye Liu, Nan Jiang, Danyang Zhang, Hang Zheng, Shijie Zheng, Situo Zhang, Kunyao Lan, Yingzi Ma, Sheng Jiang, Lu Chen, Kai Yu
- 链接：[arXiv](https://arxiv.org/abs/2611.18639) · [PDF](https://arxiv.org/pdf/2611.18639) · [HF](https://huggingface.co/papers/2611.18639)

Scaling device-control evaluation requires scaling both interactive worlds and the tasks agents must solve. We introduce SynthDCB, a benchmark for environment awareness and device control built through world distillation (WD). World distillation transforms knowledge of device behaviors, constraints, and environmental effects into modular executable components. A unified capability representation connects tool…

## 28. Composable Soft-Prompt Distillation of RL Experts: Toward Continual Post-Training

- 分数：18.0  ·  HF 赞：12  ·  来源：huggingface
- 兴趣命中：agent, benchmark
- 作者：Zhen Zhang, Changyi Yang, Xuehai He, Chengzhi Liu, Yutong Yin, Ziyue Liu, Zhuoran Yin, Yangmin Li, Zhihan Liu, Jisen Li, Mingyu Jin, Chuhan Li, Zhaotian Weng, Ruoyu He, Wenyao Gao, Jiaxin Deng, Chenwei Wu, Hui Shen, Wenhao Chai, Chenyang Zhao, Zhuofan Ying, Kieran Liu, Andrew Chen, Pony Ma, Zhaoran Wang, Alkesh Patel, Zhe Gan, Xin Eric Wang
- 链接：[arXiv](https://arxiv.org/abs/2611.27376) · [PDF](https://arxiv.org/pdf/2611.27376) · [HF](https://huggingface.co/papers/2611.27376)

RL post-training typically produces domain experts that must then be consolidated into one model, and as new experts keep arriving, this consolidation becomes a continual process. Weight merging and multi-teacher on-policy distillation (MOPD) must re-consolidate the whole model whenever an expert is added, and can erode capabilities outside the target domains. We propose Composable Soft-Prompt Distillation (CSPD),…

## 29. UUBench: Understanding the Unspoken toward Full-Duplex Multimodal Interaction

- 分数：18.0  ·  HF 赞：12  ·  来源：huggingface
- 兴趣命中：evaluation, benchmark
- 作者：Ye Pan, Chenfei Liao, Bin Ren, Hanqian Li, Haocong He, Jialei Chen, Jinlin He, Kunyu Peng, Mengyu Jin, Shijie Li, Wenqian Cui, Yuanqi Yao, Yuqian Fu, Kailong Ruan, Yuan Gao, Wei Wang, Xuming Hu, Irwin King, Nicu Sebe, Xu Zheng
- 链接：[arXiv](https://arxiv.org/abs/2611.30157) · [PDF](https://arxiv.org/pdf/2611.30157) · [HF](https://huggingface.co/papers/2611.30157)

Effective real-time, full-duplex multimodal interaction requires systems to understand not only what users say, but also the communicative needs conveyed through prosody, facial expressions, gestures, and context, and to generate audiovisual responses that appropriately address those needs. Existing evaluations offer limited insight into whether systems translate an understanding of such unspoken needs into…

## 30. StereoVLM: Binocular Vision-Language Models for Metric 3D Spatial Reasoning

- 分数：18.0  ·  HF 赞：8  ·  来源：huggingface
- 兴趣命中：reasoning, benchmark, language model
- 作者：Chi Yan, Guoyang Zhao, Wentao Yuan, Yixiao Ge, Yanning Zhou, Dan Xu
- 链接：[arXiv](https://arxiv.org/abs/2611.27915) · [PDF](https://arxiv.org/pdf/2611.27915) · [HF](https://huggingface.co/papers/2611.27915)

Vision-language models (VLMs) exhibit strong semantic understanding but remain limited in their ability to reason about metric 3D space in the physical world. Existing VLMs typically infer 3D scene structure from one or more images without known camera calibration or cross-view geometric constraints. This makes metric 3D inference inherently ambiguous and leaves it unclear whether their spatial predictions are…

## 31. Moving Generality from Model to Modeler: LLM Agents for PHM on a Deployment-Style Benchmark

- 分数：18.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：agent, benchmark, language model, large language, coding
- 作者：Zhenling Chen, Zhiguo Zeng, Anne Barros
- 链接：[arXiv](https://arxiv.org/abs/2611.25252) · [PDF](https://arxiv.org/pdf/2611.25252) · [HF](https://huggingface.co/papers/2611.25252)

Coding agents built on large language models (LLMs) now help develop many models published as general solutions. Should generality instead reside in the agent that builds a model for each new task? We examine this question in prognostics and health management (PHM), where every model must work on unseen equipment. Our deployment-style benchmark, NextUnit-Bench, covers 24 public datasets split into 58 folds that hold…

## 32. Intent Contracts: Taking Tools Away from Agents

- 分数：18.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：agent, reasoning, benchmark, planning
- 作者：Ziyuan Wang, Genliang Zhu, Xiaobo Chen, Chu Wang
- 链接：[arXiv](https://arxiv.org/abs/2611.24025) · [PDF](https://arxiv.org/pdf/2611.24025) · [HF](https://huggingface.co/papers/2611.24025)

Intent contracts are an authorization interface for tool-using LLM agents in which the planning model holds no tools. For each step it submits a short logged contract: a goal, a verbatim quotation of the user, and scope fields. Code validates the contract, and a small trusted model checks it against the user's words and writes the tool call itself. Provided the validation and dispatch code is correct, every executed…

## 33. Seeing the Invisible: How Vision-Language Models Read, Predict and Trace Radio Fields

- 分数：17.5  ·  HF 赞：7  ·  来源：huggingface
- 兴趣命中：reasoning, benchmark, language model
- 作者：Yiyang Zhu, Xin Li, Guangyuan Liu, Ziheng Liu, Jiayi Zhang, Chau Yuen
- 链接：[arXiv](https://arxiv.org/abs/2611.28123) · [PDF](https://arxiv.org/pdf/2611.28123) · [HF](https://huggingface.co/papers/2611.28123)

Operating in the physical world requires reasoning beyond what cameras directly capture. In a city, radio signals are invisible to the lens, yet their strength is governed by the buildings and streets an image does show. Given only these visible structures, can vision-language models (VLMs) infer the invisible radio field they shape? Probing true physical reasoning requires exact fields in real cities, alongside…

## 34. AgentRoboCritic: Understanding the Capability of Frontier Agents on Direct Robot Control

- 分数：17.5  ·  HF 赞：7  ·  来源：huggingface
- 兴趣命中：agent, benchmark, spec
- 作者：Yiyang Du, Yuxuan Kuang, Qitao Zhao, Yixuan Wang, Zhanqiu Guo, Yi Xu, Xin Li, Wenbin He, Liu Ren, Chenyan Xiong
- 链接：[arXiv](https://arxiv.org/abs/2611.26613) · [PDF](https://arxiv.org/pdf/2611.26613) · [HF](https://huggingface.co/papers/2611.26613)

Frontier multimodal language agents such as GPT-6 Astra have demonstrated strong capabilities in controlling robots directly via low-level numerical actions without high-level primitives. However, existing benchmarks report only episode-level success rates, which show neither how these agents succeed nor where they fail. In this paper, we present a systematic action-level analysis of frontier agents on direct robot…

## 35. HIVE-Bench: Evaluating Patch-Level Visual Representations for Egocentric Robot Manipulation

- 分数：17.0  ·  HF 赞：10  ·  来源：huggingface + arxiv
- 兴趣命中：-
- 作者：Qiwei Liang, Zhengtu Liang, Minghao Lai, Yikeng Chen, Yiming Wang, Boyang Cai, Yuetong Fang, Taowen Wang, Baiqiao Yin, Tianxing Chen, Yue Chen, Jiaming Liang, Guangyu Chen, Shaolong Zhu, Daolin Ma, Renjing Xu
- 链接：[arXiv](https://arxiv.org/abs/2611.30813) · [PDF](https://arxiv.org/pdf/2611.30813) · [HF](https://huggingface.co/papers/2611.30813)

Pretrained vision is a common start for robot learning, but most comparisons still score one pooled vector from a third-person image. Bimanual policies instead read dense patch tokens from cameras on the robot. We introduce HIVE-Bench: one shared flow-matching policy reads 20 encoders from seven families on 24 egocentric bimanual tasks, across adaptation, task sharing, and sweeps of data, model size, and layer.…

## 36. Distilling Visual Agents from Limited Interaction Experience

- 分数：16.5  ·  HF 赞：13  ·  来源：huggingface
- 兴趣命中：agent
- 作者：Siyu Zhou, Jing Jiang, Chengqi Zhang, Guodong Long
- 链接：[arXiv](https://arxiv.org/abs/2611.28618) · [PDF](https://arxiv.org/pdf/2611.28618) · [HF](https://huggingface.co/papers/2611.28618)

How much interaction experience is needed to distill a capable visual agent? We study learning from few tasks and recorded interaction histories. Our framework selects representative trajectories using skill-context coverage and ordered visual-decision similarity. On-policy distillation (OPD) learns through fresh interaction on selected tasks or fresh student responses at fixed histories. Across Navigation, Sokoban,…

## 37. Self-WSP: Can Language Models Improve Themselves Through Weight-Space Programming?

- 分数：16.5  ·  HF 赞：9  ·  来源：huggingface
- 兴趣命中：language model, spec
- 作者：Guoming Ling, Shanshan Zhong, Kaixuan Zhang, Zhongzhan Huang
- 链接：[arXiv](https://arxiv.org/abs/2611.28833) · [PDF](https://arxiv.org/pdf/2611.28833) · [HF](https://huggingface.co/papers/2611.28833)

Frontier language models can now read and edit the weights of a neural network much like code and thereby improve a small model, an approach known as Weight-Space Programming (WSP). We further explore applying WSP to a language model itself, which we call Self-WSP. Specifically, Qwen3.5-0.8B reads its own weights, proposes an edit, and then continues with the edited weights as both problem solver and editor. We find…

## 38. MORSE: Optimizing Streaming Memory Design via Open-World Auto-Research

- 分数：16.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：memory, benchmark, language model, spec
- 作者：Ce Zhang, Jianshu Zhang, Jinxi He, Xiyuan Yang, Pan Wang, Han Liu, Katia Sycara, Yaqi Xie
- 链接：[arXiv](https://arxiv.org/abs/2611.30011) · [PDF](https://arxiv.org/pdf/2611.30011) · [HF](https://huggingface.co/papers/2611.30011)

A streaming video system must decide in a single pass what evidence to retain under bounded frame storage, before it knows which details a future question will require. Recent recursive self-improvement methods automate the design of the harness that stores and retrieves this evidence. They revise the harness in response to failures, but the editor must still devise each repair from its prior knowledge and a…

## 39. ViDiHand2: Unifying Video Diffusion Priors and Hand Geometry for 3D Hand Motion Reconstruction in the Wild

- 分数：16.0  ·  HF 赞：4  ·  来源：huggingface + arxiv
- 兴趣命中：spec
- 作者：Yuxi Wang, Yufei Liu, Chengkai Jin, Qingyue Chen, Wenqi Ouyang, Tianyi Wei, Kerui Ren, Siyuan Huang, Zhiqi Shen, Hongsheng Li, Xingang Pan
- 链接：[arXiv](https://arxiv.org/abs/2611.30597) · [PDF](https://arxiv.org/pdf/2611.30597) · [HF](https://huggingface.co/papers/2611.30597)

Learning robot manipulation from egocentric human videos requires accurate metric 3D hand motion. Recent methods leverage pretrained video diffusion model (VDM) priors to recover occluded hands directly from full-frame videos, but their appearance-based depth regression generalizes poorly to unseen cameras. In this work, we propose ViDiHand2, a geometry-driven framework that reformulates VDM-based hand depth…

## 40. Distill the Correction, Not the Rewrite: Hindsight Twins for Self-Improving Text-to-Image Models

- 分数：16.0  ·  HF 赞：4  ·  来源：huggingface + arxiv
- 兴趣命中：spec
- 作者：Jiaze Li, Jingyang Chen, Wenhao Zhao, Haoran Xu, Zhenlong Yuan, Dianmo Sheng, Yuanxing Zhang
- 链接：[arXiv](https://arxiv.org/abs/2611.31048) · [PDF](https://arxiv.org/pdf/2611.31048) · [HF](https://huggingface.co/papers/2611.31048)

Text-to-image models can learn from their own mistakes by distilling a self-teacher conditioned on a vision-language critic's revised prompt. However, such self-teachers barely improve alignment, and both they and their hindsight-contrast variants absorb the critic's unintended additions to the scene, such as lighting or scenery. We attribute this to two factors: (1) the prompt already specifies the desired fix, so…

## 41. MMMem: Self-Improving Agents with Task-Aware Multimodal Experience Consolidation

- 分数：16.0  ·  HF 赞：0  ·  来源：huggingface
- 兴趣命中：agent, memory, benchmark, language model, spec, retrieval
- 作者：Yuxuan Chen, Changwei Lv, Yunfei Li, Zhongjing Du, Kehui Tan, Zijun Liao, Ruochong Zheng, Hao Chen, Can Deng, Zheni Zeng, Chang Liu, Jie Chen
- 链接：[arXiv](https://arxiv.org/abs/2611.30287) · [PDF](https://arxiv.org/pdf/2611.30287) · [HF](https://huggingface.co/papers/2611.30287)

AI agents accumulate conversations, images, and documents through long-term interactions with users. Answering later questions often requires connecting evidence across these records, yet the resulting understanding is rarely retained, allowing mistakes to recur on related questions. Existing multimodal memory methods largely focus on storing and retrieving records, with limited mechanisms for learning from…

## 42. SWEEP-Bench: Do Embodied Policies Act on the Speed They See?

- 分数：16.0  ·  HF 赞：0  ·  来源：huggingface + arxiv
- 兴趣命中：evaluation, benchmark
- 作者：Hiroaki Honda, Koya Sakamoto, Shu Morikuni, Yusuke Iwasawa, Taiki Miyanishi
- 链接：[arXiv](https://arxiv.org/abs/2611.30637) · [PDF](https://arxiv.org/pdf/2611.30637) · [HF](https://huggingface.co/papers/2611.30637)

Robot policies must adapt to the speed of moving objects, yet existing benchmarks rarely measure this ability across diverse tasks and speeds. We introduce SWEEP-Bench, a simulation benchmark with 80 conveyor-belt manipulation tasks spanning 16 skill categories, each evaluated at 13 belt speeds (0.10-0.40 m/s). Objects are transported through physical contact with a visibly moving belt. Each task has a static…

## 43. Explicit Style Extraction for Personalized Long-Form Text Generation

- 分数：15.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：language model, spec, retrieval
- 作者：Jenitha Reddy Patel, Sameeksha Kini, Amulya Rayasam, Anisa Dye, Abhinav Sharma, Sai Karthik Navuluru, Bo Ni, Li Li, Junda Wu, Tong Yu, Nedim Lipka, Xiaolei Huang, Tyler Derr, Yue Zhao, Zhengzhong Tu, Yu Wang, Hongjie Chen, Thien Huu Nguyen, Nesreen K. Ahmed, Franck Dernoncourt, Ryan A. Rossi
- 链接：[arXiv](https://arxiv.org/abs/2611.27211) · [PDF](https://arxiv.org/pdf/2611.27211) · [HF](https://huggingface.co/papers/2611.27211)

Personalized long-form generation asks a language model to write new text the way a specific user would. The standard recipe, retrieval-augmented generation, places a few of the user's past texts in the prompt but leaves the model to decide what to take from them. We introduce StylePrism, a taxonomy of 28 stylistic aspects in seven categories, and SP-Refine, an inference-time method that makes style extraction an…

## 44. PURE: A Diagnostic Benchmark for Multi-Granularity Multimodal Identity Matching

- 分数：15.0  ·  HF 赞：6  ·  来源：huggingface
- 兴趣命中：reasoning, benchmark
- 作者：Hengyu You, Xintong Wang, Jin Cao, Liang Ding
- 链接：[arXiv](https://arxiv.org/abs/2611.22343) · [PDF](https://arxiv.org/pdf/2611.22343) · [HF](https://huggingface.co/papers/2611.22343)

Identity matching asks whether two records denote the same identity, yet the answer depends on the target granularity. Two records may match at the base level but not at the variant level: they share an underlying design while differing in attributes such as color or size. Final matching accuracy does not separately characterize the capabilities involved. To study this problem, we use e-commerce as a challenging…

## 45. SAVIOR: Sample-efficient Adaptation of Vision-Language Models for OCR Representation

- 分数：15.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：evaluation, benchmark, language model
- 作者：Akshata A Bhat, Sharath Naganna, Saiful Haq, Prashant Khatri, Krishna Chaitanya Reddy Tamataam, Neha Arun, Niyati Chhaya, Pushpak Bhattacharyya
- 链接：[arXiv](https://arxiv.org/abs/2611.27319) · [PDF](https://arxiv.org/pdf/2611.27319) · [HF](https://huggingface.co/papers/2611.27319)

Optical Character Recognition (OCR) pipelines and vision-language models exhibit high accuracy on standard OCR and document-understanding benchmarks, yet they systematically underperform on document patterns that are operationally critical in financial workflows. These patterns include vertical or rotated text, logo-embedded vendor names, fine-print regulatory clauses, degraded scans, and complex multi-column…

## 46. ReWeave: Emergent Physical Task Topologies for Embodied Harness Optimization and Cross-Task Meta-Distillation

- 分数：15.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：agent, reasoning, spec
- 作者：Yicheng Xu, Wencan Jiang, Zihao Zhu, Keru Zhou, Chang Zhou, Li Liu, Maoqing Yao, Yong Liu, Jiangning Zhang
- 链接：[arXiv](https://arxiv.org/abs/2611.31053) · [PDF](https://arxiv.org/pdf/2611.31053) · [HF](https://huggingface.co/papers/2611.31053)

Long-horizon embodied tasks involve physical dependencies that may only become clear through interaction. As task understanding deepens, past trials can reveal new information for adaptation and transfer. However, coarse progress feedback cannot identify which physical preconditions held, leaving search unguided, while task-specific optimization easily overfits to individual scenes, making cross-task transfer…

## 47. WeaveVLA: 3D Relational Grounding for Vision-Language-Action Models

- 分数：15.0  ·  HF 赞：2  ·  来源：huggingface + arxiv
- 兴趣命中：spec
- 作者：Zien Wang, Yuhao Pan, Yunfeng Fan, Nan Cheng, Xin Xia, Wenchao Xu
- 链接：[arXiv](https://arxiv.org/abs/2611.31126) · [PDF](https://arxiv.org/pdf/2611.31126) · [HF](https://huggingface.co/papers/2611.31126)

Vision-language-action (VLA) models leverage pretrained vision-language representations for instruction-conditioned robot control, yet their understanding of task-relevant 3D relations and how these relations evolve during manipulation remains largely implicit. To address this challenge, we introduce \textbf{WeaveVLA}, a framework that enhances VLA action generation by explicitly modeling task-relevant relative 3D…

## 48. WeightCode: Installing New Capabilities into Neural Networks via Weight-Space Programming

- 分数：14.5  ·  HF 赞：9  ·  来源：huggingface
- 兴趣命中：language model
- 作者：Bo Li, Taoyong Cui, Bob Zhang, Mengran Li, Chengyang Zhang, Yang Zhang, Pheng Ann Heng, Wanli Ouyang, Zhenfei Yin, Yingcheng Wu, Ling Yang
- 链接：[arXiv](https://arxiv.org/abs/2611.25476) · [PDF](https://arxiv.org/pdf/2611.25476) · [HF](https://huggingface.co/papers/2611.25476)

Neural networks encode learned capabilities in their weights, yet extending those capabilities with explicit task knowledge remains a fundamental challenge. Here we show that Weight-Space Programming (WSP), in which executable programs read, construct or modify a network's weights directly, can install new capabilities within trained neural networks. WeightCode, a WSP framework, uses a frozen language model to write…

## 49. Open Vision Banana: An Open Framework for Unified Visual Perception through Generation in RGB Space

- 分数：14.5  ·  HF 赞：5  ·  来源：huggingface
- 兴趣命中：evaluation, spec
- 作者：Xu Lin, Ruilin Yao, Haoran Xu, Zixiang Wang, Ming Ma, Yu Zhao, Pu Miao, Chonghan Liu
- 链接：[arXiv](https://arxiv.org/abs/2611.28489) · [PDF](https://arxiv.org/pdf/2611.28489) · [HF](https://huggingface.co/papers/2611.28489)

Vision Banana showed that a closed image generator, instruction-tuned to paint perception outputs as RGB images, becomes a generalist vision model. Does this carry over to open generators, and if not, what fails? We answer with Open Vision Banana (OVB), an open framework that adapts the 7B diffusion generator of Qwen-Image-2.1 into one instruction-driven model for metric depth, semantic, instance, and referring…

## 50. A Pipeline-Parallel System for Depth-Recurrent Models

- 分数：14.5  ·  HF 赞：5  ·  来源：huggingface
- 兴趣命中：memory, spec
- 作者：Yunjia Xi, Jiarui Qin, Di Yin, Xing Sun
- 链接：[arXiv](https://arxiv.org/abs/2611.30581) · [PDF](https://arxiv.org/pdf/2611.30581) · [HF](https://huggingface.co/papers/2611.30581)

Depth-recurrent (Looped) models raise effective depth by applying a shared stack of blocks several times. Scaling them usually requires pipeline parallelism, but commonly used interleaved 1F1B is drawn for an acyclic stage graph in which each micro-batch enters each stage once. Once that stack is split across stages, the same stage is visited several times on one micro-batch and later stages feed earlier ones:…

## 51. How Feedback-Free Self-Evolution Reshapes Agent Skills: A Systematic Study

- 分数：14.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：agent, benchmark
- 作者：Litao Guo, Man Chen, Xinli Xu, Jinsong Zhou, Zixin Zhang, Ying-Cong Chen
- 链接：[arXiv](https://arxiv.org/abs/2611.25534) · [PDF](https://arxiv.org/pdf/2611.25534) · [HF](https://huggingface.co/papers/2611.25534)

Agent skills are documents in which experts write down procedural knowledge, and models increasingly maintain them by rewriting them without feedback. Such rewriting could adapt a skill to the model that uses it or erode the expert knowledge that makes it useful, yet how skills evolve under this feedback-free self-evolution has not been studied. We let models rewrite expert skills round after round without any task,…

## 52. Search From the Start: Search-Native Pretraining for Language Models

- 分数：14.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：language model, spec
- 作者：Kaustubh Ponkshe, Gyung Hyun Je, Stefan Taga, Colin Raffel, Martin Jaggi
- 链接：[arXiv](https://arxiv.org/abs/2611.26809) · [PDF](https://arxiv.org/pdf/2611.26809) · [HF](https://huggingface.co/papers/2611.26809)

Modern language models (LMs) are increasingly deployed with access to search tools at inference. Yet pretraining remains predominantly focused on predicting static text, with search capabilities typically introduced during post-training. We propose Search-Native Pretraining as a practical route to teach search capability during pretraining from ordinary text corpora. Specifically, we augment pretraining corpus at…

## 53. Write, Evolve, Read: Streaming Cameras into a Persistent World State for 4D Occupancy Forecasting

- 分数：13.5  ·  HF 赞：3  ·  来源：huggingface + arxiv
- 兴趣命中：-
- 作者：ZiAn Wang, Tianyi Wang, Zhihao Chen, Manni Cui, Junkai Chen, ZhiJin Chen, Ruiqi Liu, Junfei Wu, Huanyu Zhang, Shu Wu
- 链接：[arXiv](https://arxiv.org/abs/2611.30573) · [PDF](https://arxiv.org/pdf/2611.30573) · [HF](https://huggingface.co/papers/2611.30573)

4D occupancy forecasting predicts the 3D semantic occupancy of a driving scene seconds ahead. Over a few seconds, the scene changes little while the vehicle moves, so most of the space ahead has already been seen. Sorting the future into unchanged, changed, and unseen space, we find that current camera-based world models fall short on the unchanged part: they fail to hold on to what they have already seen, rather…

## 54. Which Dwarf Is This? Doppeldwarf-306 and Near-Identical Instance Retrieval

- 分数：13.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：benchmark, retrieval
- 作者：Turhan Can Kargin
- 链接：[arXiv](https://arxiv.org/abs/2611.27490) · [PDF](https://arxiv.org/pdf/2611.27490) · [HF](https://huggingface.co/papers/2611.27490)

Most established instance-retrieval benchmarks emphasise landmarks; small sculptures from visually similar series offer a complementary challenge. We introduce Doppeldwarf-306: 1,691 openly licensed photographs of 306 bronze dwarf statues in Wrocław, Poland, many made in themed series that share one style, with the photographer of each image recorded. With no training, nearest-neighbour search over frozen DINOv2…

## 55. MomentMem: Memorizing Key Moments for Robot Manipulation

- 分数：12.5  ·  HF 赞：5  ·  来源：huggingface
- 兴趣命中：memory
- 作者：Guangyu Zhao, Yongchang Zhang, Ruizhang Jiang, Zhihong Yu, Yuhao Zhang, Tao Wu, Qimin Zhou, Kunsong Shi, Haoran Wen, Zeyu Zhang, Yin Li, Kun Zhan, Yiwu Zhong
- 链接：[arXiv](https://arxiv.org/abs/2611.26745) · [PDF](https://arxiv.org/pdf/2611.26745) · [HF](https://huggingface.co/papers/2611.26745)

Robotic manipulation often requires remembering visual information that is no longer observable, such as the original location of an object. Existing approaches typically rely on full observation histories, which become redundant over long horizons, or text summaries, which may omit precise visual details. We study visual moment memory, the ability to retain such details from key moments for subsequent manipulation.…

## 56. Taking Apart and Putting Together: Tracking Objects Through Physical Transformations

- 分数：12.5  ·  HF 赞：5  ·  来源：huggingface
- 兴趣命中：benchmark
- 作者：Davide Gardenal, Mingxuan Liu, Flavio Vella, Quentin Guimard, Elisa Ricci
- 链接：[arXiv](https://arxiv.org/abs/2611.27398) · [PDF](https://arxiv.org/pdf/2611.27398) · [HF](https://huggingface.co/papers/2611.27398)

We introduce Transformation Tracking and Understanding (TTU), extending video object tracking to environments where objects undergo physical assemblies and disassemblies. TTU requires continuously tracking objects through transformations, identifying new entities, maintaining a state graph of their relationships, and assigning semantic labels to transformations. While foundation models (e.g., SAM 2/3) maintain…

## 57. Prism: Hierarchical Text Detection with Minimalist Design

- 分数：12.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：benchmark, spec
- 作者：Yuchen Su, Xuesheng Wang, Zhilong Ji, Jinfeng Bai, Shijian Lu, Zhineng Chen
- 链接：[arXiv](https://arxiv.org/abs/2611.26254) · [PDF](https://arxiv.org/pdf/2611.26254) · [HF](https://huggingface.co/papers/2611.26254)

Hierarchical text detection aims to localize words, text lines, and paragraphs while parsing their structural relationships. It provides essential structural cues for visual text understanding. To maximize accuracy, existing methods typically rely on complex multi-scale feature fusion necks and heavy-weight heads, resulting in bloated architectures and low inference efficiency. In this paper, we argue that a…

## 58. Fast-JEPA: Advancing the Success-Latency Frontier for Latent World Models

- 分数：12.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：benchmark, planning
- 作者：Yao Zhang, Bin Yu, Shijie Lian, Haishan Liu, Changti Wu, Yu Wu, Kai Chen
- 链接：[arXiv](https://arxiv.org/abs/2611.25927) · [PDF](https://arxiv.org/pdf/2611.25927) · [HF](https://huggingface.co/papers/2611.25927)

Latent world models predict the outcomes of action sequences, but comparing candidate plans through recursive rollout remains expensive at test time. We introduce Fast-JEPA, a latent world model planning framework that advances the success-latency Pareto frontier of predictive search. Fast-JEPA reorganizes predictive computation to support effective action-sequence search at low planning cost. It constructs a…

## 59. Feedback Shortcut: Speculative Decoding for Latent Feedback Transformers

- 分数：12.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：coding, spec
- 作者：Benhao Huang, Xuezhe Ma, Hector Liu
- 链接：[arXiv](https://arxiv.org/abs/2611.28227) · [PDF](https://arxiv.org/pdf/2611.28227) · [HF](https://huggingface.co/papers/2611.28227)

Feeding each position's top-layer hidden state back into the next position's input improves Transformer performance. However, this feedback breaks speculative decoding, since verifying a drafted token requires the top-layer state from its preceding position, which forces the draft to rely on an approximate stand-in. Training the model to adapt to this stand-in can lower the exact-decoding performance ceiling, while…

## 60. NoHairCache: Calibrate-Once KV Cache Eviction with One Power-Law Exponent

- 分数：12.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：coding, spec
- 作者：Shuyang Xiang
- 链接：[arXiv](https://arxiv.org/abs/2611.29006) · [PDF](https://arxiv.org/pdf/2611.29006) · [HF](https://huggingface.co/papers/2611.29006)

The decay exponent α in KV-cache eviction is an intrinsic property of the model: calibrated once on a single corpus, it transfers directly across domains. Attention-based accumulation (H2O) and recency-based sliding windows (StreamingLLM) are two dominant eviction frameworks, often treated as unrelated, but we show that they are the two endpoints of a single power-law family: by scoring each token as s_i = A_i cdot…

## 61. Typhoon OCR 2: From Thai Document Transcription to Multilingual, Multi-Task OCR

- 分数：12.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：evaluation, spec
- 作者：Surapon Nonesung, Natapong Nitarach, Sittipong Sripaisarnmongkol, Kunat Pipatanakul, Warit Sirichotedumrong
- 链接：[arXiv](https://arxiv.org/abs/2611.27494) · [PDF](https://arxiv.org/pdf/2611.27494) · [HF](https://huggingface.co/papers/2611.27494)

Typhoon OCR 1.5 focused on reading Thai documents. However, in real-world workflows, users often need to extract specific information or preserve the structure of an entire page for further processing. Typhoon OCR 2 handles both tasks in a single model, with prompt-driven extraction and structured full-page parsing. Full-page parsing covers Thai, English, and Chinese. We release compact 2B and 0.8B models adapted…

## 62. Prune to Expand: Training Prompt Enhancers with Less to Imitate

- 分数：12.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：spec
- 作者：Tianhe Wu, Qilin Sun, Kede Ma
- 链接：[arXiv](https://arxiv.org/abs/2611.27229) · [PDF](https://arxiv.org/pdf/2611.27229) · [HF](https://huggingface.co/papers/2611.27229)

Prompt enhancement (PE) refines concise user prompts into detailed descriptions to improve the compositional aesthetics of generated images while preserving user intent. A common practice constructs supervised fine-tuning (SFT) pairs by deriving short, user-like prompts from dense captions, implicitly assuming that captions that improve image generation also provide effective supervision. In this paper, however, we…

## 63. UniVEP: Unifying Velocity and Endpoint Prediction for Robot Manipulation

- 分数：12.0  ·  HF 赞：0  ·  来源：huggingface
- 兴趣命中：benchmark, spec
- 作者：Zhengtu Liang, Qiwei Liang, Tao Lin, Shihang Weng, Boyang Cai, Xiangyu Chen, Yikeng Chen, Jiaming Liang, Bohan Tan, Yu Yan, Renjing Xu
- 链接：[arXiv](https://arxiv.org/abs/2611.26103) · [PDF](https://arxiv.org/pdf/2611.26103) · [HF](https://huggingface.co/papers/2611.26103)

Flow-matching robot policies usually use one prediction target throughout action generation, even though recovering actions from noise and polishing nearly clean actions bring different challenges. We systematically compare velocity prediction (V), endpoint prediction (X), and velocity-weighted endpoint prediction (X--V) across multiple robot policies, benchmarks, and inference budgets. On StarVLA and LiLa-WAM, X--V…

## 64. Seeing Right, Writing Wrong: Where Short Chain-of-Thought Breaks Spatial VQA

- 分数：12.0  ·  HF 赞：0  ·  来源：huggingface
- 兴趣命中：reasoning, language model
- 作者：Chenhao Zhang
- 链接：[arXiv](https://arxiv.org/abs/2611.28665) · [PDF](https://arxiv.org/pdf/2611.28665) · [HF](https://huggingface.co/papers/2611.28665)

Asking a vision-language model (VLM) to think step by step often makes it worse at spatial questions, even though the image stays in context. We show that short chain-of-thought (CoT) turns a perception problem into a transcription problem. Once a VLM writes a spatial relation, its answer follows that sentence instead of the image, so whether CoT helps or hurts depends largely on whether the written relation is more…

## 65. From Points to Trajectories: Rethinking Multimodal Alignment for Physical Events

- 分数：11.5  ·  HF 赞：7  ·  来源：huggingface
- 兴趣命中：-
- 作者：Yiyang Zhu, Guangyuan Liu, Jingdi Lei, Li Wei, Chau Yuen
- 链接：[arXiv](https://arxiv.org/abs/2611.24249) · [PDF](https://arxiv.org/pdf/2611.24249) · [HF](https://huggingface.co/papers/2611.24249)

Advancing physical artificial intelligence (Physical AI) requires moving beyond static object recognition to ground how real-world mechanics (e.g., impact, friction, and force transfer) unfold over time. While multimodal aligners seek to capture these interactions by matching multi-sensor streams, prevailing architectures compress each temporal sequence into a single pooled embedding. We show that this paradigm…

## 66. AeroRSI: Recursive Self-Improvement for Aerial Vision-Language Navigation

- 分数：11.5  ·  HF 赞：7  ·  来源：huggingface
- 兴趣命中：-
- 作者：Shiwei Wu, Yuwen Pan, Zhi Li, Yaowen Li, Yan Zhou, Xuemiao Xu, Yu Liu
- 链接：[arXiv](https://arxiv.org/abs/2611.24077) · [PDF](https://arxiv.org/pdf/2611.24077) · [HF](https://huggingface.co/papers/2611.24077)

Vision-language-action (VLA) models enable unmanned aerial vehicles (UAVs) to follow natural-language instructions, yet still fail frequently in closed-loop flight. Correcting these failures requires repairs, i.e., actions that avoid them at the states the policy itself reaches, which human pilots cannot label at scale and rule-based planners cannot supply reliably. In this paper, we present AeroRSI, a recursive…

## 67. Exploited Before It Was Fixed? Vulnerability Timelines from Open, Machine-Readable Evidence

- 分数：11.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：spec
- 作者：Cédric Bonhomme, Alexandre Dulaunoy
- 链接：[arXiv](https://arxiv.org/abs/2611.22479) · [PDF](https://arxiv.org/pdf/2611.22479) · [HF](https://huggingface.co/papers/2611.22479)

-05-X-03), Known Exploited Vulnerabilities (KEV) catalogs, and exploitation sightings.   We introduce an evidence model implemented in Vulnerability-Lookup that selects the earliest evidence for each lifecycle event, distinguishes vulnerability-specific records, preserves date precision, and ensures traceability to original sources.   Among 3,758 vulnerability identifiers with exploitation evidence, 98% have…

## 68. Wactorz: Self-Writing LLM Agents That Discover, Repair, and Migrate at the Edge

- 分数：11.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：agent
- 作者：Panagiotis Kasnesis, Lazaros Toumanidis, Amalia Contiero Syropoulou, Christos Chatzigeorgiou
- 链接：[arXiv](https://arxiv.org/abs/2611.29619) · [PDF](https://arxiv.org/pdf/2611.29619) · [HF](https://huggingface.co/papers/2611.29619)

Most LLM agent frameworks build a crew that runs a task and exits. Physical environments (e.g., homes, labs, factory floors) need agents that stay up for months, survive their own bugs, and run on whatever hardware is already next to the sensors. We present Wactorz, an open-source runtime in which LLM-generated agents are long-lived, supervised actors: a planner turns a chat request into Python, compiles it into a…

## 69. Autoregressive View Model

- 分数：10.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：benchmark
- 作者：Jensen, Zhou, Samuel Rota Bulo, Denis Rozumny, Duncan Zauss, Peter Hedman, Nikhil Keetha, Philip Torr, Christian Rupprecht, Andrea Vedaldi, Peter Kontschieder
- 链接：[arXiv](https://arxiv.org/abs/2611.23417) · [PDF](https://arxiv.org/pdf/2611.23417) · [HF](https://huggingface.co/papers/2611.23417)

We present the Autoregressive View Model (AVM), which generates a scene as a stream of views without constructing an explicit 3D representation. Through a unified in-context interface, AVM conditions on images or videos to generate short clips along a requested camera path. Visual context grounds reconstruction and interpolation, while a learned prior enables extrapolation into unseen regions. AVM retrieves relevant…

## 70. How Complete Must an Environment Be to Train a Capable GUI Agent?

- 分数：10.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：agent
- 作者：Jingxing Wang, Teng Wang, Xingyu Lou, Zihan Guo, Jun Wang, Weiwen Liu, Weinan Zhang, Jianghao Lin
- 链接：[arXiv](https://arxiv.org/abs/2611.23946) · [PDF](https://arxiv.org/pdf/2611.23946) · [HF](https://huggingface.co/papers/2611.23946)

Graphical user interface (GUI) agents are widely trained in executable GUI environments. To lower cost, build environments in batches, and reduce manual effort, each work trades away part of the environment through its construction choices. We describe these choices along three dimensions: reward coverage, the goal-reaching trajectories the verifier rewards; data coverage, the application data the agent is exposed…

## 71. Beyond Attention Maps: Understanding and Improving Medical MLLMs via Visual Values

- 分数：10.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：benchmark
- 作者：Yichen Zhao, Fenghe Tang, Wenxin Ma, Rongsheng Wang, Zihao Wan, Shaohua Kevin Zhou
- 链接：[arXiv](https://arxiv.org/abs/2611.29361) · [PDF](https://arxiv.org/pdf/2611.29361) · [HF](https://huggingface.co/papers/2611.29361)

Current MLLM methods largely focus on whether models attend to the right visual regions, implicitly treating spatial attention map as the primary key of effective visual perception. To examine this assumption, we introduce a medical VQA dataset with paired non-contrast (NC) and contrast-enhanced (CE) images that share corresponding anatomy while providing different cues. We show that this view is incomplete: across…

## 72. GameWM: Toward Next-Generation Video Games with Interaction-Centric World Models

- 分数：10.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：-
- 作者：Bing He, Runze Wang, Fei Zha, Zhongyuan Wu, Ke Xu, Tao Zhuang, Yuxuan Xie, Zhongyuan Liu
- 链接：[arXiv](https://arxiv.org/abs/2611.19247) · [PDF](https://arxiv.org/pdf/2611.19247) · [HF](https://huggingface.co/papers/2611.19247)

For more than half a century, video games have pursued better graphics, more natural interaction, and more engaging gameplay. Generative video models (VMs) now bear on all three. Neural networks already draw most of the pixels in shipped games, and recent world models let a lightweight game engine keep the world state while a VM turns the engine's coarse proxy video into final frames. These systems, however, treat…

## 73. Deterministic, Reproducible Inference in Exact Integer Arithmetic, and Verifiable Distributed Inference as Its Consequence

- 分数：10.0  ·  HF 赞：0  ·  来源：huggingface
- 兴趣命中：language model
- 作者：Sayed Amir Karim
- 链接：[arXiv](https://arxiv.org/abs/2611.13730) · [PDF](https://arxiv.org/pdf/2611.13730) · [HF](https://huggingface.co/papers/2611.13730)

Optimized floating-point inference is not reproducible across environments: the same model on different hardware, compilers or thread counts can produce different bits. We present tritify, an open-source runtime that executes the forward pass of real models -- decoder-only language models, Mixture-of-Experts decoders, and the Segment Anything 2.1 image/video stack -- with the entire run-time path in exact integer…

## 74. Motion-Aware Reward Modeling for Instruction-Guided Video Editing

- 分数：9.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：-
- 作者：Li Li, Xiangbo Gao, Bo Ni, Samyadeep Basu, Viet Dac Lai, Jing Shi, Seunghyun Yoon, Gang Wu, Yu Wang, Thien Huu Nguyen, Tyler Derr, Franck Dernoncourt, Zhengzhong Tu, Yue Zhao
- 链接：[arXiv](https://arxiv.org/abs/2611.22495) · [PDF](https://arxiv.org/pdf/2611.22495) · [HF](https://huggingface.co/papers/2611.22495)

Reward models for instruction-guided video editing can favor temporal consistency at the expense of motion. We study this failure, termed motion collapse, using controlled motion-suppression variants of real edits. On VE-Bench, the evaluated composite reward prefers a motion-suppressed candidate in 97% of cases. Learned video rewards and a VLM judge also struggle with mild suppression, while latent optimization and…

## 75. RoboInF: A Benchmark for Instruction Fidelity in Robotic Manipulation

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, benchmark, spec, planning
- 作者：Jiawei Guo, Yu Huang, Dijiang Dong, Yue Liu, Peiran Ren, Wei Shen
- 链接：[arXiv](https://arxiv.org/abs/2611.30555) · [PDF](https://arxiv.org/pdf/2611.30555) · [HF](https://huggingface.co/papers/2611.30555)

Precise language control requires embodied models to follow instructions governing both task outcomes and execution. Although recent methods train policies to follow increasingly detailed commands, existing benchmarks often assess instruction following alongside perception, planning, and generalization to unfamiliar scenes. Higher task success therefore offers limited evidence of closer adherence to instructions. We…

## 76. Learning What to Change: State-Verified Reinforcement Learning for Educational Agents

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, tool use, reasoning, reinforcement learning, evaluation, benchmark
- 作者：Shengyao Wang, Siyuan Su, Siyu Song, Mengsong Wu, Yiming Luo, Wenbo Wu, Hao Hao, Aimin Zhou
- 链接：[arXiv](https://arxiv.org/abs/2611.30559) · [PDF](https://arxiv.org/pdf/2611.30559) · [HF](https://huggingface.co/papers/2611.30559)

Persistent tutoring agents do more than answer questions: they manage course files, practice records, and learner profiles that govern future lessons. In such stateful settings, knowing what to teach does not guarantee knowing what to change. We identify a pervasive failure mode, content-state decoupling, where agents deliver pedagogically sound responses while silently corrupting workspace state through unwarranted…

## 77. Auxiliary Clues Aware's Geometry Problem Solving

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, reinforcement learning, benchmark, language model, large language, spec
- 作者：Qigong Lei, Qingsong Wang, Wang Lin, Qianyi Yang, Chang Yao, Jingyuan Chen
- 链接：[arXiv](https://arxiv.org/abs/2611.30617) · [PDF](https://arxiv.org/pdf/2611.30617) · [HF](https://huggingface.co/papers/2611.30617)

Geometry Problem Solving (GPS) serves as a rigorous test of the complex reasoning capabilities of Multimodal Large Language Models (MLLMs), particularly when solutions require auxiliary constructions absent from the input diagram. However, explicit diagramming methods suffer from unstable image generation quality and cascading errors, while existing implicit attention mechanisms primarily focus on visible elements,…

## 78. Beyond the Black Box: A Diagnosis-Driven Agent for Interpretable MIP Solver Tuning

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, evaluation, benchmark, spec
- 作者：Yidong Luo, Weihuang Wen, Xuanhao Pan, Yinya Wang, Shanwen Pu, Chenghao Lan, Dongdong Ge, Tianshu Yu
- 链接：[arXiv](https://arxiv.org/abs/2611.30670) · [PDF](https://arxiv.org/pdf/2611.30670) · [HF](https://huggingface.co/papers/2611.30670)

Tuning a mixed-integer programming (MIP) solver is an instance-specific problem, where a poor configuration can increase solving time by orders of magnitude. Existing Bayesian optimization tuners treat solver tuning as a black-box optimization problem: each evaluation returns a single score, allowing the tuner to learn which configuration is faster, but not why. Inspired by the use of profilers in GPU-kernel…

## 79. Optimising VLM Harnesses to Localise Errors in Generated Videos

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, evaluation, benchmark, language model, spec
- 作者：Ankit Yadav, Nikhil Cherian Kurian, Arpit Garg, Lingqiao Liu
- 链接：[arXiv](https://arxiv.org/abs/2611.30673) · [PDF](https://arxiv.org/pdf/2611.30673) · [HF](https://huggingface.co/papers/2611.30673)

Identifying subtle errors in generated videos is an important step toward automated video generation, where errors must be detected to assess and refine generated clips. Recent work shows that pretrained vision-language models (VLMs) can localise such errors, but their effectiveness depends strongly on the workflow used: choices about which frames to inspect, which tools and model calls to make, and how to combine…

## 80. Transport-Safe Evaluation of LLM Agents: Trajectory-Dependent Judge Error and Anytime-Valid Auditing

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, evaluation, benchmark, language model, large language
- 作者：Yulliwas Ameur, Samia Bouzefrane, Soumya Banerjee
- 链接：[arXiv](https://arxiv.org/abs/2611.30742) · [PDF](https://arxiv.org/pdf/2611.30742) · [HF](https://huggingface.co/papers/2611.30742)

Large language model (LLM) agents are often ranked by an LLM judge whose error rates are measured once and reused for every agent. The corrected success rates can then be biased when the judge's errors depend on the trajectory and agents differ in the trajectories they produce for successes or failures. We derive the exact asymptotic bias and give a chain of checks from identification to simultaneous ranks. On a…

## 81. Bridging the Semantic Gap from Natural Language Specifications to RTL with Layered Formal Guidance

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, language model, large language, spec
- 作者：Yan Tan, Xiangchen Meng, Yangdi Lyu
- 链接：[arXiv](https://arxiv.org/abs/2611.30766) · [PDF](https://arxiv.org/pdf/2611.30766) · [HF](https://huggingface.co/papers/2611.30766)

While large language models (LLMs) have shown promise in generating register-transfer level (RTL) code from natural-language specifications, their reliability remains limited on designs with complex control logic and temporal behavior. This stems from a fundamental semantic gap: high-level natural language often leaves implementation-critical details underspecified, forcing LLMs to infer unstated assumptions. This…

## 82. What Quality Engineers Need to Know About Generative AI: Structured Data Extraction

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, language model, large language, spec
- 作者：Fadel M. Megahed, Ying-Ju Chen, Yamin Dahwich, Zhao-Wei Chen, Lucas K. Hung, Arthur Carvalho, L. Allison Jones-Farmer, Ibrahim Yousif, Inez M. Zwetsloot
- 链接：[arXiv](https://arxiv.org/abs/2611.30778) · [PDF](https://arxiv.org/pdf/2611.30778) · [HF](https://huggingface.co/papers/2611.30778)

In this expository paper, we explain how quality engineers can use large language models (LLMs) and vision-language models (VLMs) for structured data extraction. We introduce the relevant concepts, discuss structured extraction from a measurement-system perspective, and demonstrate its implementation in R and Python. We then present two freely available web-based applications (apps): (a) extracting information from…

## 83. Semantic-aware Decoding for Diverse Text-to-SQL under Schema Ambiguity

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, language model, large language, coding, spec
- 作者：Yuxuan Jiang, Anna Mitsopoulou, Apostolos Koukouvinis, Yannis Velegrakis, Georgia Koutrika
- 链接：[arXiv](https://arxiv.org/abs/2611.30873) · [PDF](https://arxiv.org/pdf/2611.30873) · [HF](https://huggingface.co/papers/2611.30873)

Real-world text-to-SQL systems often face schema ambiguity, where a question can map to multiple plausible schema elements. To support downstream disambiguation, SQL generation systems should include diverse interpretations among their top-k predictions. However, large language models (LLMs) typically favor a single interpretation, producing highly skewed outputs. We propose Semantic-aware Logit Adjustment (SLA), a…

## 84. Bridging Continuous-Time MAPF and Industrial AGV Fleet Coordination with Lazy Priority-Based Search

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reasoning, benchmark, planning
- 作者：Federico Signorile, Raffaele Carli, Alessandro Bertogli, Roberto Olmi, Sven Koenig, Mariagrazia Dotoli
- 链接：[arXiv](https://arxiv.org/abs/2611.30874) · [PDF](https://arxiv.org/pdf/2611.30874) · [HF](https://huggingface.co/papers/2611.30874)

Continuous-time multi-agent path finding on roadmaps (MAPF$_R$) offers a principled way to coordinate robot fleets with geometric collision avoidance, yet its deployment on industrial automated guided vehicle (AGV) infrastructures remains challenging, as highly connected and redundant roadmaps amplify both safe-interval reasoning and multi-agent interaction handling. To bridge this gap, we formalize…

## 85. AnchorCredit: Output-Anchored Credit Assignment for Structured Generation with Multiple Verifiable Rewards

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, reinforcement learning, benchmark, spec
- 作者：Gen Li, Pengyang Xie, Xiao Xiao, Chuanzhi Tong, Ziyang Ji, Zhigang Xu, Huiwen Bai, Zihao Xing, Yanxiang Zhou, Yifei Yuan, Xiaoqing Wang
- 链接：[arXiv](https://arxiv.org/abs/2611.30881) · [PDF](https://arxiv.org/pdf/2611.30881) · [HF](https://huggingface.co/papers/2611.30881)

In Reinforcement Learning with Verifiable Rewards (RLVR), Group Relative Policy Optimization (GRPO) and related methods typically compute group-relative advantages from response rewards and broadcast the same advantage to every generated token in a response to guide policy updates. However, we identify a systematic problem of cross-component credit misassignment in tasks with multiple verifiable results, such as…

## 86. GlanceNav: Efficient Vision-and-Language Navigation with Streaming Memory and Counterfactual Rewind

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, reinforcement learning, language model, large language
- 作者：Anh Dao, Quan-Dung Pham, Danh Vinh Le, Tuyen Pham Le, Quan Nguyen, Yuzhang Shang
- 链接：[arXiv](https://arxiv.org/abs/2611.30900) · [PDF](https://arxiv.org/pdf/2611.30900) · [HF](https://huggingface.co/papers/2611.30900)

Multimodal large language models (MLLMs) have become strong policies for vision-and-language navigation (VLN). However, most of them encode a sample of past frames again at every decision and are trained on isolated decisions, so computation is redundant and the usable history is short. They also learn from their own mistakes through outcome rewards that give one scalar to a whole episode. We ask whether a navigator…

## 87. DexLatentWorld: 3D Cross-Embodiment Latent Action World Models for Zero-Shot Robotic Manipulation

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, evaluation, spec, planning
- 作者：Vinay Udit Mohan, Xuchuan Huang, Rolandos Alexandros Potamias
- 链接：[arXiv](https://arxiv.org/abs/2611.30907) · [PDF](https://arxiv.org/pdf/2611.30907) · [HF](https://huggingface.co/papers/2611.30907)

World models facilitate planning and control in robotic manipulation by enabling agents to anticipate the consequences of their actions. However, they typically rely on action-labelled interaction data that is costly to acquire and difficult to scale. These models are also often tied to the specific embodiment they were trained on, limiting transferability to previously unseen robot morphologies. We introduce a 3D…

## 88. Replay Before You Reply: Second-Look Prompting for Unified Multimodal Encoding

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, benchmark, language model, coding
- 作者：Yicheng Zhang, Xun Zhang, Jingyuan Ma, Tianyu Yu, Yuan Yao
- 链接：[arXiv](https://arxiv.org/abs/2611.30909) · [PDF](https://arxiv.org/pdf/2611.30909) · [HF](https://huggingface.co/papers/2611.30909)

Solving multimodal tasks requires Vision-Language Models (VLMs) to form a unified understanding of the image and the question text. However, under causal attention in current VLMs, a token can attend only to what precedes it. Whichever modality comes first is therefore encoded under partial observation of the input, uninformed by the rest of the multimodal context. We introduce Second-Look Prompting (SLP), a…

## 89. PRIMEAPE: A Multilingual Benchmark for Fine-Grained Meta-Evaluation of Judge Models

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, language model, large language
- 作者：Vladislav Mikhailov, Sarfraz Ahmad, Momina Ahsan, Zoia Butenko, Vladimir Dobrovolskii, Preslav Nakov, Erik Velldal, Lilja Øvrelid, Ekaterina Artemova
- 链接：[arXiv](https://arxiv.org/abs/2611.30925) · [PDF](https://arxiv.org/pdf/2611.30925) · [HF](https://huggingface.co/papers/2611.30925)

Large language models increasingly serve as judges of other models, shaping benchmark rankings and model development. Yet, a judge whose rationale consistently supports its verdict may still disagree with human preferences. To study this, we introduce PRIMEAPE, a multilingual benchmark for evaluating judge verdicts and rationales. PRIMEAPE provides 2,205 response pairs covering 243 instructions in English, French,…

## 90. LimeTree: Linear-Memory Graph Neural Networks over Tree-Graphs for Resource-Efficient Language Modeling and Context Extrapolation

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, evaluation, language model, retrieval
- 作者：Elisabeth Fink
- 链接：[arXiv](https://arxiv.org/abs/2611.30934) · [PDF](https://arxiv.org/pdf/2611.30934) · [HF](https://huggingface.co/papers/2611.30934)

The search for computationally efficient alternatives to the Transformer has yielded numerous architectures in recent years; however, most exhibit severe weaknesses in associative recall-such as key-value (KV) retrieval-and length extrapolation, where even standard Transformers struggle. This paper introduces LimeTree, a linear-complexity architecture in both memory and compute for sequence modeling. By integrating…

## 91. Evaluable Language-Model Treatment Policies for Sepsis Resuscitation via Offline Value-Guided Selection

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reinforcement learning, evaluation, language model, large language, spec
- 作者：Yue Pei, Shining Bo, Yingying Zhang, Qinggang Ge, Zhiling Zhao, Jian Cheng, Haogang Zhu
- 链接：[arXiv](https://arxiv.org/abs/2611.30951) · [PDF](https://arxiv.org/pdf/2611.30951) · [HF](https://huggingface.co/papers/2611.30951)

Offline treatment learning must balance imitation, which stays close to logged evidence but ignores outcomes, against value maximisation, which uses outcomes but drifts toward treatments the records cannot verify. Numerical reinforcement learning strikes this balance during training. For large language models (LLMs), directly using sparse retrospective outcomes for fine-tuning raises challenges of delayed credit…

## 92. MedUIGym: Evaluating and Training GUI Agents for Clinical Workflows

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reasoning, reinforcement learning, evaluation, benchmark, language model
- 作者：Yitong Qiao, Lei Liu, Yue Shen, Jian Wang, Jinjie Gu, Zhixuan Chu
- 链接：[arXiv](https://arxiv.org/abs/2611.30983) · [PDF](https://arxiv.org/pdf/2611.30983) · [HF](https://huggingface.co/papers/2611.30983)

Automating clinical workflows requires vision-language agents that can navigate dense graphical user interfaces (GUIs) in electronic health records (EHRs) and execute precise actions, yet many medical agents still rely on text or structured tool calls. In this work, we introduce MedUIGym, a scalable interactive environment comprising 15,739 tasks from 17 benchmark sources across six clinical task families for…

## 93. RoboUniverse-10K: Toward the Scaling Era of Agentic Robotics via Real-to-Sim Environments

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reinforcement learning, evaluation, benchmark, coding
- 作者：Jinkun Liu, Yingze Wang, Situ Wang, Deyao Hong, Mingju Gao, Wenyi Li, Yizhe Chi, Youjie Zheng, Kaisen Yang, Xiangyang Wang, Bingxiang He, Yuxin Zuo, Boyuan Chen, Yue Chen, Cheng Qian, Tianxing Chen, Huichi Zhou, Huaxiu Yao, Hao Tang, Hao Zhou, Ya-Qin Zhang, Calvin Xiao, Tiga Altman, Huan-ang Gao
- 链接：[arXiv](https://arxiv.org/abs/2611.31002) · [PDF](https://arxiv.org/pdf/2611.31002) · [HF](https://huggingface.co/papers/2611.31002)

Agentic Robotics, in which foundation models act as coding agents to control robots through executable programs, has emerged as a compelling paradigm for embodied intelligence. Yet unlike software engineering, where massive executable environments power post-training, robotics remains constrained by small, manual benchmarks and in-distribution evaluation. To bridge this gap, we introduce RoboUniverse-10K, 10,807…

## 94. OmniV-Bench: Can MLLMs Comprehend Immersive Spatio-temporal Scenes?

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, tool use, reasoning, benchmark, language model, large language
- 作者：Liu Yang, Huiyu Duan, Yixuan Gao, Sirui Liu, Lu Liu, Zhaolin Cai, Ke Gu, Xiongkuo Min, Xiaoping Zhang, Guangtao Zhai
- 链接：[arXiv](https://arxiv.org/abs/2611.31022) · [PDF](https://arxiv.org/pdf/2611.31022) · [HF](https://huggingface.co/papers/2611.31022)

Omnidirectional videos (ODVs) capture dynamic environments with a full $360^\circ$ field of view, providing rich spatial context and temporal dynamics for applications such as virtual reality (VR), augmented reality (AR), and embodied intelligence. Recent multimodal large language models (MLLMs) have made great progress in spatial and temporal understanding, yet their ability to comprehend the immersive 360…

## 95. AI-Assisted Auto-formalization for Trustworthy Scientific Computing: Case Studies and Lessons Learned

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reasoning, coding, spec
- 作者：Mohit Tekriwal, Het Mankad, Naifeng Zhang, Keita Teranishi, Sahil Bhola, Daisuke Uchida, Jean-Baptiste Jeannin, Franz Franchetti, Karthik Duraisamy, Jeffrey Vetter, Yohann Dudouit
- 链接：[arXiv](https://arxiv.org/abs/2611.31033) · [PDF](https://arxiv.org/pdf/2611.31033) · [HF](https://huggingface.co/papers/2611.31033)

Agentic AI tools have recently had success in mathematical reasoning. Both general purpose coding agents such as Claude Code and Codex, and specialized mathematics agents such as Aristotle, have been used for formalizing mathematical problems such as Fermat's last theorem, Erdős problems and several IMO level math problems. However, much of these efforts are concentrated in the pure mathematics domain, which…

## 96. Grower-in-the-loop AI for Deployable Precision Fertilisation in Sustainable Agriculture

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：language model, large language, spec, planning
- 作者：Xulong Wang, Yu Zhang, Gaoshan Bi, Menghui Zhou, Simon Jeffery, Max Davis, Sam Maycock, Paul Harris, Po Yang
- 链接：[arXiv](https://arxiv.org/abs/2611.31044) · [PDF](https://arxiv.org/pdf/2611.31044) · [HF](https://huggingface.co/papers/2611.31044)

In agriculture, typically over half of the applied nitrogen fertiliser is lost to water and to air. Precision fertilisation aims to reduce these losses while maintaining yield and quality, yet existing tools struggle to capture farm-specific challenges in determining optimal nitrogen rates. Static recommendations are common and overlook on-farm constraints, such as delays due to weather or machinery availability, or…

## 97. Automatic Occupational Coding through Retrieval-Augmented Generation

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, language model, large language, coding, retrieval
- 作者：Mathijs A. Langezaal, Egon L. van den Broek, Lukas P. A. Arts, Marcel Goldberg, Grégoire Rey, Melissa C. Friesen, Sarah J. Locke, Nathaniel Rothman, Qing Lan, Roel C. H. Vermeulen, Susan Peters
- 链接：[arXiv](https://arxiv.org/abs/2611.31051) · [PDF](https://arxiv.org/pdf/2611.31051) · [HF](https://huggingface.co/papers/2611.31051)

Annually 1.9 million deaths and 89.7 million disability-adjusted life years are caused by exposure to agents during work (e.g., welding fumes, silica dust, and noise pollution). To improve worker health, high-quality exposure assessments are crucial. Therefore, free-text job descriptions from large-scale occupational cohorts are manually standardized through occupational classifications and linked to hazardous…

## 98. DKnown-Jev-2: Article-Level Answer-Evidence Classification and Efficient Inference with a Pre-trained Language Model

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, language model, coding, spec
- 作者：Qi Li, Jianjun Xu, Jiu Li, Pingtao Wei
- 链接：[arXiv](https://arxiv.org/abs/2611.31056) · [PDF](https://arxiv.org/pdf/2611.31056) · [HF](https://huggingface.co/papers/2611.31056)

Evidence selection in normative knowledge question answering requires determining whether a candidate article contains content that directly supports an answer under the applicable conditions of the question. We present DKnown-Jev-2, an article-level answer evidence classifier designed for evidence integration across multiple paragraphs. The model jointly encodes question conditions, article metadata, and paragraph…

## 99. From Local Errors to System Failures: Modeling and Benchmarking Error Propagation in Multi-Agent LLM Systems

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reasoning, evaluation, benchmark, language model, large language, retrieval
- 作者：Wenlong Yu, Bingxu Lu, Qilong Wang, Qinghua Hu, Qianru Sun
- 链接：[arXiv](https://arxiv.org/abs/2611.31063) · [PDF](https://arxiv.org/pdf/2611.31063) · [HF](https://huggingface.co/papers/2611.31063)

In multi-agent systems (MAS) built on large language models (LLMs), errors can propagate through intermediate messages and compromise final answers. However, outcome-based evaluation obscures how agents amplify, attenuate, or correct these errors. We propose Response-Aware Error Propagation among Agents (REPA), a structural model that connects measured local responses to system-level error propagation. REPA…

## 100. Look Back, Draft Ahead: Corrective Prefix Attention for Parallel Speculative Decoding

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, coding, spec
- 作者：Mohammad Mahdi Moradi, Ali Pourranjbar, Zongzuo Wang, Mingming Zhu, Ben Feng, Boxing Chen
- 链接：[arXiv](https://arxiv.org/abs/2611.31112) · [PDF](https://arxiv.org/pdf/2611.31112) · [HF](https://huggingface.co/papers/2611.31112)

Parallel speculative decoders propose an entire token block at once, yet one early inconsistency can cause the target to reject its remaining suffix. We introduce Corrective Prefix Attention (CPA), which combines prefix-aware selection with autoregressive supervision to improve these parallel drafts. CPA lets each candidate attend to earlier choices within the block. Fixed candidate shortlists allow all pairwise…

## 101. Self-Upgrading Embodied Agents

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, memory, reasoning, language model
- 作者：Jiajun Fan, Neil He, Qinglong Zheng, Changyi Yang, Tong Wei, Andy Mao, Zetian Li, Chaoran Cheng, Hui Ren, Ruihan Guo, Xianrui Zhong, Xizheng Yu, Jingyuan Li, Xi Zhu, Kaiqu Liang, Chang Xu, Zun Qian, Zidi Xiong, Yuezhu Zhao, Xu Huang, Ge Liu
- 链接：[arXiv](https://arxiv.org/abs/2611.31117) · [PDF](https://arxiv.org/pdf/2611.31117) · [HF](https://huggingface.co/papers/2611.31117)

An embodied agent built on a language model goes to work with the weights it was given and keeps them for life. To get better, it needs more training, or reflection, memory, search or prompts that cost every step and are lost when the task changes. Editing weights by reasoning, weight-space programming, could end this, but has stayed with models that only reason or relied on a far larger commercial model. We…

## 102. FATCAT: Fault Injection Attacks Targeting Chip-level Alignment

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, evaluation, language model, large language, spec
- 作者：Peter Horvath, Ilia Shumailov, Zhuoran Liu, Lukasz Chmielewski, Lejla Batina
- 链接：[arXiv](https://arxiv.org/abs/2611.31129) · [PDF](https://arxiv.org/pdf/2611.31129) · [HF](https://huggingface.co/papers/2611.31129)

Model alignment is the primary safety and security mechanism for enforcing refusal of malicious prompts in modern foundation models; yet, existing adversarial evaluations implicitly assume underlying hardware integrity. In this paper, we present FATCAT, the first physical fault-injection attacks capable of eliminating refusal in modern large language and vision-language models. Specifically, we present a…

## 103. Precision-Aware Learning Rate Transfer Across Block Count in LLM Post-Training

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, reinforcement learning, language model, large language
- 作者：Nan Chen, Soledad Villar, Soufiane Hayou
- 链接：[arXiv](https://arxiv.org/abs/2611.31166) · [PDF](https://arxiv.org/pdf/2611.31166) · [HF](https://huggingface.co/papers/2611.31166)

The post-training of pretrained large language models, including supervised finetuning (SFT), direct preference optimization (DPO), and reinforcement learning with verifiable reward (RLVR), is very sensitive to the learning rate, and tuning it through grid search is costly in both computation and memory. In this work, we propose \textbf{TipSweep}, a method to transfer the learning rate across the number of trainable…

## 104. CO-GRAFT: Attributing Reinforcement Learning Gains in Search Agents via Role-Level Policy Grafting

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reasoning, reinforcement learning, language model, large language, retrieval
- 作者：Ramraj Chandradevan, Sayontan Ghosh, Vinoth Selvendran
- 链接：[arXiv](https://arxiv.org/abs/2611.31185) · [PDF](https://arxiv.org/pdf/2611.31185) · [HF](https://huggingface.co/papers/2611.31185)

Reinforcement learning (RL) improves large language model search agents by up to 32 exact-match (EM) points over their pre-RL initializations, yet overall accuracy gains do not identify which underlying functional capabilities improve or interact during training. We introduce CO-GRAFT, a reward-agnostic interventional attribution framework in which an RL-trained agent and its pre-RL initialization jointly generate a…

## 105. WorldLatent: A Unified 4D Latent Space for World Perception and Generation

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, language model, large language, spec
- 作者：Jingxi Chen, Yujia Chen, Cornelia Fermuller, Yiannis Aloimonos, Wen-Sheng Chu, Du Tran
- 链接：[arXiv](https://arxiv.org/abs/2611.31209) · [PDF](https://arxiv.org/pdf/2611.31209) · [HF](https://huggingface.co/papers/2611.31209)

Generative Pre-Training (GPT) represents a profound milestone in natural language processing, serving as the foundation for most of today's state-of-the-art large language models. By casting diverse understanding and generation problems into a shared token representation, GPT enables a single architecture and unified optimization loop to master heterogeneous tasks across massive corpora, giving rise to powerful…

## 106. Seeking in Space: Benchmarking Purposeful Active Exploration of Vision-Language Models for Spatial Reasoning

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, reasoning, evaluation, benchmark, language model, spec
- 作者：Xiwei Liu, Yulong Li, Xuhui Li, Xinlin Zhuang, Zhixiang Lu, Haolin Yang, Jianxu Chen, Yifan Lu, Zhiran Zhang, Yutong Xie
- 链接：[arXiv](https://arxiv.org/abs/2611.31215) · [PDF](https://arxiv.org/pdf/2611.31215) · [HF](https://huggingface.co/papers/2611.31215)

Humans explore unfamiliar spaces with purpose, deciding where to look until they have gathered the evidence a spatial question requires. However, can vision-language models (VLMs), which reason increasingly well over curated images and videos, also seek in space when the evidence is not handed to them? We present ActSpace-Bench, a benchmark of 994 questions across 234 exploration episodes in 72 real-scanned indoor…

## 107. Agentic AI for Intent Management and Control in Autonomous Communication Networks

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reinforcement learning, language model, spec
- 作者：Burak Demirel, Yu Wang, Pablo Soldati
- 链接：[arXiv](https://arxiv.org/abs/2611.31223) · [PDF](https://arxiv.org/pdf/2611.31223) · [HF](https://huggingface.co/papers/2611.31223)

Artificial intelligence (AI)-driven automation will help future mobile networks translate high-level network intents into concrete network optimization or control actions. However, existing approaches often focus on intent management and orchestration, leaving the adaptation of underlying network optimization and control functions largely unaddressed. This article proposes a triadic agentic AI framework that…

## 108. Language Models Steer on Injected Uncertainty Tokens, but Fail to Self-Monitor In Situ

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reasoning, benchmark, language model
- 作者：Daniel Theron
- 链接：[arXiv](https://arxiv.org/abs/2611.31228) · [PDF](https://arxiv.org/pdf/2611.31228) · [HF](https://huggingface.co/papers/2611.31228)

Prompting language models to verbalize stepwise numerical confidence during generation is an increasingly popular approach for triggering backtracking and error correction in agentic reasoning. This strategy presupposes two capabilities: (1) in-situ monitoring fidelity (does confidence drop when an error occurs?) and (2) downstream steering control (does an uncertainty token causally steer the model to repair its…

## 109. The norm axiom and factor hyperfields

- 分数：8.0  ·  HF 赞：0  ·  来源：huggingface
- 兴趣命中：-
- 作者：Alessandro Linzi
- 链接：[arXiv](https://arxiv.org/abs/2611.29473) · [PDF](https://arxiv.org/pdf/2611.29473) · [HF](https://huggingface.co/papers/2611.29473)

Touchard and the author asked whether every valued hyperfield, in Krasner's sense with the norm axiom, is of the form H_ρ(K): a valued field K read up to relative error ρ. The question turns on the norm axiom. If a valued hyperfield is a quotient K^times/Tcup{0} of a field, the norm axiom forces T=1+m_ρ for a valuation on K. This completes the proof of a published proposition, and it makes the question equivalent to…

## 110. CyberDualEval: Measuring Dual-Use Cyber Risks in Frontier Language Models

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, language model
- 作者：Magnus Saebo, Francesco Piccoli, Maxwell Watson, Pranjali Thakur, Yangruibo Ding, Zhuo Zhang
- 链接：[arXiv](https://arxiv.org/abs/2611.30533) · [PDF](https://arxiv.org/pdf/2611.30533) · [HF](https://huggingface.co/papers/2611.30533)

While frontier language models are becoming capable cybersecurity assistants, they also create a dual-use cyber risk: the same capabilities that help defenders identify and analyze vulnerabilities can similarly help attackers weaponize them. Existing cyber benchmarks measure either raw offensive capability or generic refusal behavior, overlooking the dual-use cyber assessment of preserving benign security utility…

## 111. Near-Far Attention: Region-Aware Sparse Retrieval for Long-Context LLM Decoding

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, coding, retrieval
- 作者：YuanShuo Wang, Jianchao Tan, Lei Gong, Teng Wang, Wenqi Lou, Xuehai Zhou
- 链接：[arXiv](https://arxiv.org/abs/2611.30554) · [PDF](https://arxiv.org/pdf/2611.30554) · [HF](https://huggingface.co/papers/2611.30554)

Sparse attention reduces the cost of long-context decoding, but token selection introduces additional scoring and ranking overhead. Moreover, uniform page scoring overlooks differences in relevance between near and far context. We propose Near-Far Attention (NFA), which adapts retrieval to regional attention patterns while keeping candidate scoring lightweight. During prefill, the Lightweight Gate Estimator…

## 112. Seeing Is Locating: Spatial Awareness and Geographic Bias in Decision Language Models

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, language model, spec
- 作者：Wilson Wongso, Hada Melino Muhammad, Xiachong Lin, Hao Xue, Flora D. Salim
- 链接：[arXiv](https://arxiv.org/abs/2611.30564) · [PDF](https://arxiv.org/pdf/2611.30564) · [HF](https://huggingface.co/papers/2611.30564)

Decision models, which output probability distributions over candidate labels instead of generating text, are increasingly used as classifiers and evaluators for inputs associated with real-world locations. However, it remains unclear whether they can leverage spatial context and whether their predictions are geographically biased. We introduce GeoDecisions, a multimodal benchmark for evaluating the spatial…

## 113. Quantizing Diffusion LLMs under Parallel Decoding: Commitment Risk and the Parallelism Tax

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：language model, large language, coding
- 作者：Huan Xu, Maosen Zhao, Pengtao Chen, Tao Chen
- 链接：[arXiv](https://arxiv.org/abs/2611.30587) · [PDF](https://arxiv.org/pdf/2611.30587) · [HF](https://huggingface.co/papers/2611.30587)

Diffusion large language models (dLLMs) are served with accelerated decoders that cache context and commit, in one step, every masked position whose confidence clears a threshold. Yet post-training quantization of dLLMs has so far been calibrated and evaluated under fixed-step samplers without caching. We study W4A4 quantization under the deployed decoder and find that the decoder determines both where quantization…

## 114. CineAct: Interaction-State Agents for Playable, Branching Film Generation

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reasoning, benchmark
- 作者：Junyan Lin, Jianqi Ma, Shujie Duan, Hanxin Zhu, Zhihao Hu, Jinming Liu, Shuai Li, Jun Zhang, Xin Jin, Chang Wen Chen, Weidong Zhang
- 链接：[arXiv](https://arxiv.org/abs/2611.30613) · [PDF](https://arxiv.org/pdf/2611.30613) · [HF](https://huggingface.co/papers/2611.30613)

Open video generators such as MiniMax-H3 produce short clips of only several to a dozen seconds per run. To synthesize longer sequences, existing methods either rely on agentic systems following preset scripts, or roll out autoregressively from the previous clip's last frame, losing off-screen states and accumulating hallucinations across turns. Consequently, users still cannot take an explicit goal, choose how to…

## 115. Does the Mixer Matter ? Paired-Seed Ablations of Tiny Bilingual Language Models

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, language model, coding
- 作者：Ayoub Kirouane
- 链接：[arXiv](https://arxiv.org/abs/2611.30623) · [PDF](https://arxiv.org/pdf/2611.30623) · [HF](https://huggingface.co/papers/2611.30623)

We report paired-seed architecture ablations from the development of Sophea Artemis, our in-house Greek-English model family. Every arm trains on the same 3B targets with a shared tokenizer and recipe; models range from 54M to 759M total parameters and roughly 54M to 124M active parameters. The main finding is that, at this tiny scale, stored capacity matters far more than mixer design. On a fixed held-out test,…

## 116. Zhengrong: World Models with Pole-Based Action-Response Factorization for Direct Visual Planning

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, spec, planning
- 作者：Yu Zhang, Jingrui Li, Congyu Wang, Yuhang Cheng, Wenbo Chen, Xiaobo Zhang, Jing Zou, Yuxi Dai
- 链接：[arXiv](https://arxiv.org/abs/2611.30666) · [PDF](https://arxiv.org/pdf/2611.30666) · [HF](https://huggingface.co/papers/2611.30666)

Direct visual world models predict the effects of candidate action sequences without recursive latent rollout, yet they leave the temporal structure of action effects unspecified. We introduce Zhengrong (Zhengrong-PoleWM), a world model that decomposes a latent trajectory into an initial-condition anchor, a free response, and delayed responses to action innovations. Nonlinear networks map visual history and causal…

## 117. Uncovering Hidden Behaviours in Language Models via Limited-Parameter Finetuning

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, language model, large language
- 作者：Boyd Kane, Jo J. Jiao, Elizabeth Donoway, Bryce Woodworth, Alex Cloud, Alexander M. Turner
- 链接：[arXiv](https://arxiv.org/abs/2611.30672) · [PDF](https://arxiv.org/pdf/2611.30672) · [HF](https://huggingface.co/papers/2611.30672)

Large language models can have behaviours which only arise in hard-to-anticipate contexts. These hidden behaviours pose a challenge to alignment audits, which seek to uncover problematic model behaviour but are limited by the scenarios the auditor can anticipate. To address this challenge, we explore limited-parameter finetuning (LPF) on examples of a target behaviour. While training 3-25% of LoRA parameters, LPF…

## 118. Learn the Effects, Not the Examples: Implicit ICL via Attention Patching

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, language model, spec
- 作者：Seungwon Woo, Hyunseo Shin, Wonseok Hwang
- 链接：[arXiv](https://arxiv.org/abs/2611.30690) · [PDF](https://arxiv.org/pdf/2611.30690) · [HF](https://huggingface.co/papers/2611.30690)

In-context learning (ICL) enables language models to adapt to new tasks from demonstrations, but repeatedly including multiple examples increases context length and inference cost. Many existing implicit ICL methods encode demonstrations as fixed vectors, limiting adaptation of the intervention to individual queries and token positions. We propose Attention-Patching, an implicit ICL method that models contextual…

## 119. CocoonBench: Can Multilingual Search Agents Escape Language Information Cocoons?

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, benchmark, spec
- 作者：Hongchuan Zeng, Bowen Liu, Changjiang Gao, Senyu Han, Zhipei Xu, Peisong Wang, Xinbing Liang, Yuhan Li, Nuo Chen, Blaze Chen
- 链接：[arXiv](https://arxiv.org/abs/2611.30727) · [PDF](https://arxiv.org/pdf/2611.30727) · [HF](https://huggingface.co/papers/2611.30727)

Multilingual search agents can access the global Web, yet may remain trapped in a language environment with insufficient evidence; we refer to this failure as a language information cocoon. However, existing search benchmarks largely operate within a single language, especially English, overlooking entity connections across multiple languages. We introduce CocoonBench, a benchmark that evaluates whether multilingual…

## 120. Can Cities Have Personalities? Introducing the SCD City Personality Assessment

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reasoning, evaluation
- 作者：Andrei Khurshudov
- 链接：[arXiv](https://arxiv.org/abs/2611.30733) · [PDF](https://arxiv.org/pdf/2611.30733) · [HF](https://huggingface.co/papers/2611.30733)

Descriptions of cities are shaped by human experience and institutional narratives. We introduce the SCD City Personality Assessment (SCD-CPA), a method that instantiates document-grounded ChatGPT city personas and interrogates each with an identical 24-statement instrument inspired by the four-pair structure of the Myers-Briggs Type Indicator. Rather than asking a general-purpose model to characterize cities…
