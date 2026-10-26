# 每日 AI 论文

生成时间：2026-10-26 04:48 UTC  ·  共 12 篇（已按 arXiv ID 去重）

来源：Hugging Face Daily Papers + arXiv（cs.AI / cs.LG / cs.CL / cs.CV）。
排序：HF 上榜、点赞、多源命中、兴趣词。兴趣词可在 `config.json` 改。

## 1. UserArena: Benchmarking Interactive User Simulation for Long-Horizon Shopping Agents

- 分数：25.0  ·  HF 赞：22  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark
- 作者：Jujia Zhao, Jiakai Tang, Jing Yu, Wen Chen, Jian Wu, Han Zhu, Fei Sun, Suzan Verberne, Zhaochun Ren
- 链接：[arXiv](https://arxiv.org/abs/2610.30932) · [PDF](https://arxiv.org/pdf/2610.30932) · [HF](https://huggingface.co/papers/2610.30932)

Agentic recommendation pursues shopper goals through sequences of context-dependent decisions. Developing and evaluating such policies requires faithful recommendation world models that capture both the interactive shopping environment and users' behavioral responses over long interactions. Existing resources rarely provide long-horizon, fine-grained real-user trajectories or support trajectory-level evaluation and…

## 2. HiSTEVE 1.0: Harnessing Human-Interface VLA Agents for Open-World Games

- 分数：24.0  ·  HF 赞：16  ·  来源：huggingface
- 兴趣命中：agent, memory, reinforcement learning, spec, planning
- 作者：Zecong Tang, Zian Guan, Yuncheng Guo, Zhanqiu Zhang, Yiwen Guo, Bo Dai
- 链接：[arXiv](https://arxiv.org/abs/2610.31162) · [PDF](https://arxiv.org/pdf/2610.31162) · [HF](https://huggingface.co/papers/2610.31162)

Building virtual embodied agents that operate in open-ended games like human players is a long-standing goal requiring both long-horizon autonomy and reliable native-interface control. As a procedurally generated open world, Minecraft provides a natural testbed for studying the integration of these capabilities. Existing agents typically provide either native visuomotor control without long-horizon autonomy or…

## 3. RSIHub: A Composable Framework for Agent-Evolution Methods

- 分数：23.5  ·  HF 赞：19  ·  来源：huggingface
- 兴趣命中：agent, evaluation, spec
- 作者：Zimu Wang, Xiaobo Wang, Siyu Ye, Jiaqi Li, Silin Chen, Yuling Shi, Ruobing Wang, Jingjing Zhang, Chaofan Wang, Kai Wu, Mengnan Qi, Kai Cai, Xiaodong Gu, Zilong Zheng
- 链接：[arXiv](https://arxiv.org/abs/2610.32253) · [PDF](https://arxiv.org/pdf/2610.32253) · [HF](https://huggingface.co/papers/2610.32253)

Agent-evolution methods use execution feedback to improve prompts, skills, tools, and orchestration, but their implementations often rebuild the same experimental machinery. We present RSIHub, an open-source framework for building, comparing, and extending these methods on shared infrastructure. Recipes compose reusable operators and declare mutable resources; RSIHub supplies execution, evaluation, recovery, and…

## 4. RynnUnify: Towards Unified Embodied Brain

- 分数：22.5  ·  HF 赞：13  ·  来源：huggingface
- 兴趣命中：agent, reasoning, reinforcement learning, planning
- 作者：Minghao Zhu, Bohan Hou, Kun Xiang, Zixuan Wang, Yinzhou Tang, Yifei Yang, Zhikai Wang, Tianyi Zhang, Kehan Li, Haoyu Zhao, Siteng Huang, Leigang Qu, Sicong Leng, Dongchi Huang, Mingxiu Chen, Shijian Lu, Yue Wang, Xiaodan Liang, Zhenyu Zeng, Deli Zhao, Chengju Liu, Jianfei Yang, Xin Li
- 链接：[arXiv](https://arxiv.org/abs/2610.32965) · [PDF](https://arxiv.org/pdf/2610.32965) · [HF](https://huggingface.co/papers/2610.32965)

We introduce RynnUnify, a 16B unified embodied model that combines strong embodied understanding with long-horizon visual planning through interleaved video--language reasoning. With capabilities spanning spatial reasoning, physical prediction, and grounding, RynnUnify connects an understanding of the physical world with visual anticipation of how it evolves across successive subtasks. Building on these…

## 5. Omni-Woodpecker: Hallucination Correction via Evidence-Prior Rebalancing for Omni LLMs

- 分数：20.0  ·  HF 赞：8  ·  来源：huggingface
- 兴趣命中：reasoning, benchmark, coding, spec
- 作者：Zijian Liu, Chaoyou Fu, Yan Yang, Caifeng Shan, Ran He
- 链接：[arXiv](https://arxiv.org/abs/2610.27103) · [PDF](https://arxiv.org/pdf/2610.27103) · [HF](https://huggingface.co/papers/2610.27103)

Recent Omni LLMs (OLLMs) have demonstrated remarkable capabilities in joint audio-visual reasoning, yet cross-modal hallucinations remain a major challenge. Existing mitigation methods mainly operate at the output level, overlooking the entanglement of grounding evidence and learned priors within fused representations. To address this issue, we propose Omni-Woodpecker (OWP), a training-free framework that shifts…

## 6. Generalized CycleGRPO for Fine-Grained Multimodal Understanding and Grounding

- 分数：16.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：reinforcement learning, evaluation, benchmark, language model, large language, spec
- 作者：Xin Zhang, Haochen Wang, Beibei Lin, Zhaoxiang Zhang, Robby T. Tan, Jason Li, Dacheng Tao
- 链接：[arXiv](https://arxiv.org/abs/2610.29552) · [PDF](https://arxiv.org/pdf/2610.29552) · [HF](https://huggingface.co/papers/2610.29552)

Fine-grained multimodal intelligence requires models to both understand a designated region and localize it from language. Existing methods learn these directions with separate objectives and task-specific annotations. We present Generalized CycleGRPO, the first unified reinforcement learning framework coupling region understanding and localization across spatial, temporal, and spatio-temporal domains. Given a…

## 7. Dual Exam: Controlled Evaluation of Multimodal Agents and World Models

- 分数：13.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：agent, evaluation
- 作者：Zhefan Rao, Meng Chu, Xuan Zhang, Jingfan Chen, Guohao Cai, Runyi Li, Shiyi Du, Ning Lu, Xu Huang, Zhixuan Chen, Feng Nie, Harold Haodong Chen, Hanwen Wang, Wen-Jie Shu, Yajing Bai, Xianfeng Wu, Xuanhua He, Shuhan Guo, Ziyue Ma, Ruichuan An, Long Bai, Miaosen Chai, Wenhao Chai, Jingye Chen, Qi Chen, Xuhang Chen, Wei Chow, Minghao Fu, Yunhao Gou, Haokun Gui, Dong Huang, Wei Huang, Zi Cheng Huang, Haibo Jin, Lingdong Kong, Leung Chun Ho, Tianqin Li, Yanheng Li, Jiayuan Liu, Jiyang Liu, Mingyu Liu, Shaoteng Liu, Xiaocheng Lu, Yawen Luo, Zeyu Qin, Tiancheng Shen, Yueqi Song, Zhaolong Su, Hengkai Tan, Tianhao Tang, Yiran Tao, Juncheng Wang, Qinghe Wang, Shangshang Wang, Yingying Wang, Fang Wu, Tiange Xiang, Qiushi Yang, Weicai Ye, Weichen Yu, Jiarui Zhang, Jize Zhang, Liuzhou Zhang, Renrui Zhang, Sheng Zhang, Wenhu Zhang, Junru Zhao, Lingting Zhu, Yuxin Zuo, Yutong Bai, Long Chen, Yang Deng, Ziqi Huang, Yeying Jin, Weijia Li, Kevin Qinghong Lin, Quande Liu, See-Kiong Ng, Hongliang Ren, Hongru Wang, Shujun Wang, Qifeng Chen, Haoxuan Che
- 链接：[arXiv](https://arxiv.org/abs/2610.31066) · [PDF](https://arxiv.org/pdf/2610.31066) · [HF](https://huggingface.co/papers/2610.31066)

World Models (WMs) can support Multimodal Agents (MAs) through simulated experience, while Agent trajectories can inform World Model refinement. Evaluating this interaction requires separate evidence about action selection and state evolution. We introduce Dual Exam, which tests Agents under fixed environment response mechanisms and World Models under fixed action interventions across physical, digital, social, and…

## 8. Echo: Coupled Action and Task Status Signal Denoising for Vision Language Action Models

- 分数：13.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：spec, planning
- 作者：Yufeng Liu, Bohao Fan, Juntu Zhao, Xinyi Wang, Hang Yu, Wenzhuan Luo, Yingzhi Wang, Qinghai Li, Yingdong Hu, Junliang Guo, Richard Wang, Dequan Wang, Yang Gao, Cheng Ma
- 链接：[arXiv](https://arxiv.org/abs/2610.31569) · [PDF](https://arxiv.org/pdf/2610.31569) · [HF](https://huggingface.co/papers/2610.31569)

Recognizing task completion and failure enables robots to stop upon success and initiate recovery or replanning after failure. Existing methods augment Vision Language Action (VLA) policies with task status signal prediction to support these execution decisions. However, learning and integrating these signals can require fine-grained supervision, external monitoring models, or complex architectural designs.…

## 9. FLOMSS: Generative Music Source Separation by Flow Matching

- 分数：12.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：benchmark, spec
- 作者：Shuyang Cui, Zhi Zhong, Keisuke Toyama, Koichi Saito, Qiyu Wu, Yukara Ikemiya, Junghyun Koo, Kin Wai Cheuk, Woosung Choi, Giorgio Fabbro, Wei-Hsiang Liao, Shusuke Takahashi, Yuki Mitsufuji
- 链接：[arXiv](https://arxiv.org/abs/2610.17821) · [PDF](https://arxiv.org/pdf/2610.17821) · [HF](https://huggingface.co/papers/2610.17821)

Music source separation (MSS) has been conventionally addressed by discriminative methods. Recently, flow matching has emerged as a strong generative paradigm for modeling complex data distributions, with successful applications across diverse domains. These advances motivate us to systematically investigate flow matching for MSS in a four-source (Vocals, Bass, Drums, Other) setting in full-band stereo.…

## 10. HoloBoxing: A Simple Recipe for Humanoid Boxing with 7 Minutes of Single-GPU Training

- 分数：12.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：reinforcement learning, evaluation
- 作者：Xihan Ma, Bo Zhang, Boxiong Li, Yuhan Bao, Ziyue Liu, Yucheng Wang
- 链接：[arXiv](https://arxiv.org/abs/2610.32909) · [PDF](https://arxiv.org/pdf/2610.32909) · [HF](https://huggingface.co/papers/2610.32909)

HoloBoxing presents a simple recipe for learning humanoid boxing by building on a pretrained whole-body controller. The recipe separates reusable motor skills from task decisions: a compact planner requests future body-point targets, while the frozen controller handles joint-level execution. A learned decoder maps 32-dimensional actions to structured target windows, and measured-state imitation initializes the…

## 11. Easy-3Dfy: Object-Level Geometric Composition for Single-Image 3D Scene Construction

- 分数：11.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：spec
- 作者：Ziang Zhang, Wenyou Yi, Zehan Wang, Jiachen Xu, Xintong Han, Chunchao Guo, Zhou Zhao
- 链接：[arXiv](https://arxiv.org/abs/2610.32250) · [PDF](https://arxiv.org/pdf/2610.32250) · [HF](https://huggingface.co/papers/2610.32250)

Single-image 3D scene construction is a fundamental problem in 3D vision. Recent methods such as SAM-3Dfy enable end-to-end reconstruction of 3D assets and their scene layouts, but still struggle with fine-grained scene geometry and asset quality. Meanwhile, specialized 3D object generators provide detailed object geometry, while 3D foundation models offer strong and generalizable spatial understanding. We propose…

## 12. DirCast: Live Esports Directing and Commentary with a Single Streaming Video-Language Model

- 分数：10.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：language model
- 作者：Zixian Gao, Lixin Xiu, Penghao Luo, Xiangcheng Cao, Ziqi Cai, Zhen Li, Erwin Wu, Kaipeng Zhang
- 链接：[arXiv](https://arxiv.org/abs/2610.31734) · [PDF](https://arxiv.org/pdf/2610.31734) · [HF](https://huggingface.co/papers/2610.31734)

A live esports broadcast needs a director who chooses which camera goes on air and a caster who talks over that choice, every second and without knowing what comes next. Streaming video language models have learned to commentate, but only over a broadcast that a human director has already produced. We study live broadcast production, in which a model receives the raw camera of every player and must both direct and…
