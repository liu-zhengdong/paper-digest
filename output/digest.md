# 每日 AI 论文

生成时间：2026-11-25 08:34 UTC  ·  共 120 篇（已按 arXiv ID 去重）

来源：Hugging Face Daily Papers + arXiv（cs.AI / cs.LG / cs.CL / cs.CV）。
排序：HF 上榜、点赞、多源命中、兴趣词。兴趣词可在 `config.json` 改。

## 1. WorldLeague: Benchmarking Physical Agency

- 分数：36.0  ·  HF 赞：138  ·  来源：huggingface
- 兴趣命中：agent, memory, benchmark, language model, planning
- 作者：Xinyang Zhou, Qi Li, Xinchao Wang
- 链接：[arXiv](https://arxiv.org/abs/2611.30989) · [PDF](https://arxiv.org/pdf/2611.30989) · [HF](https://huggingface.co/papers/2611.30989)

AI systems can now operate Blender, follow instructions in complex video games, and manipulate objects with robot arms. What range of physical goals can today's AI systems achieve autonomously? Answering this question requires testing systems on tasks that demand different combinations of perception, memory, planning, and action. We introduce WorldLeague, a benchmark that compares AI systems on a common set of 60…

## 2. Embo-Harness: Towards Understanding Frontier-Model-as-Policy Harness

- 分数：36.0  ·  HF 赞：98  ·  来源：huggingface
- 兴趣命中：agent, tool use, tool-use, reasoning, planning
- 作者：Xiao-Ming Wu, Kang Liao, Yuexiao Ma, Taolin Zhang, Mingqian Zhou, Nuo Chen, Ziming Li, Yihang Luo, Rui Li, Zhonghua Wu, Tianyu Xie, Xiawu Zheng, Zhongang Cai, Zhi Hou, Chen Change Loy
- 链接：[arXiv](https://arxiv.org/abs/2611.31201) · [PDF](https://arxiv.org/pdf/2611.31201) · [HF](https://huggingface.co/papers/2611.31201)

Frontier multimodal models exhibit extraordinary generalization in generating robot actions from observations and instructions, enabling a new paradigm in which they serve directly as policies within closed-loop robotic harnesses. However, the design principles of such harnesses, and the capabilities underlying their strong performance, remain unclear. We present Embo-Harness, a framework for systematically studying…

## 3. 3AGameFactory-Motion: Agentic Rigging and Reliable Complex Motion Generation for Diverse 3D Assets

- 分数：36.0  ·  HF 赞：58  ·  来源：huggingface
- 兴趣命中：agent, benchmark, language model, large language, spec
- 作者：Bohan Zeng, Kaixin Zhu, Yifan Yang, Dongge Yu, Zihao Wu, Yifan Dai, Zhou Liu, Junbo Niu, Xiaochen Ma, Shiran Ge, Zimo Meng, Junzhu Liang, Huanyao Zhang, Jinhang Liu, Tianqi Xiao, Jinhao Zhang, Tianyi Bai, Zhixiong Zeng, Penghao Zhao, Yuanbo Peng, Key Zhang, Wentao Zhang
- 链接：[arXiv](https://arxiv.org/abs/2611.30013) · [PDF](https://arxiv.org/pdf/2611.30013) · [HF](https://huggingface.co/papers/2611.30013)

Animating arbitrary 3D assets from instructions requires both structural inference and motion control, yet existing motion benchmarks mostly cover conventional human or animal skeletons with simple instructions. We introduce DivDynBench, which evaluates rigging and motion generation across six morphology categories, with instructions requiring multi-phase part coordination and explicit timing, angle, repetition, and…

## 4. WeMM-Ecom: Advancing Multimodal Content Understanding for WeChat E-Commerce

- 分数：36.0  ·  HF 赞：54  ·  来源：huggingface
- 兴趣命中：reinforcement learning, evaluation, benchmark, language model, large language, spec
- 作者：Binhui Xie, Jinmin Li, Haomiao Tang, Guangting Wang, Song Jin, Jianwei Zhu, Fengyun Rao, Jing Lyu
- 链接：[arXiv](https://arxiv.org/abs/2611.30662) · [PDF](https://arxiv.org/pdf/2611.30662) · [HF](https://huggingface.co/papers/2611.30662)

We present WeMM-Ecom, a family of multimodal large language models that deliver frontier e-commerce capabilities while achieving state-of-the-art general-purpose performance at their respective scales. The family spans five sizes, from a 0.8B dense model to a 35B mixture-of-experts model with 3B active parameters. Our training pipeline begins with two-stage continued pre-training that progressively raises the…

## 5. Let the Fixer Decide: Training a Code Localizer from the Fixer's Likelihood

- 分数：36.0  ·  HF 赞：52  ·  来源：huggingface
- 兴趣命中：agent, reinforcement learning, evaluation, coding
- 作者：Khalil Hennara, Muhammad Hreden, Zeina Aldallal, Sara Chrouf, Safwan AlModhayan
- 链接：[arXiv](https://arxiv.org/abs/2611.12164) · [PDF](https://arxiv.org/pdf/2611.12164) · [HF](https://huggingface.co/papers/2611.12164)

Code localizers are usually trained to predict the files a reference patch edits, but the code a fixer needs to read is not the same as the code it changes. We propose Fixer-Guided Localization (FGL): the localizer proposes several localizations, a frozen fixer scores each by how likely it makes a verified patch, and the localizer is trained on these scores with weighted supervised fine-tuning, without running tests…

## 6. Nemotron-Labs-VisualCreation: Pixel as Code for Agentic Visual Creation

- 分数：36.0  ·  HF 赞：49  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark, coding, planning
- 作者：Guo Chen, Fuxiao Liu, Haoqin Tu, Yiyang Zhou, Andrew Tao, Bryan Catanzaro, Cihang Xie, Yuyin Zhou, Huaxiu Yao, Didong Lu, Zongxia Li, Guilin Liu
- 链接：[arXiv](https://arxiv.org/abs/2611.31358) · [PDF](https://arxiv.org/pdf/2611.31358) · [HF](https://huggingface.co/papers/2611.31358)

Visual creation demands expressive imagery together with precise control over text, layout, and structure. We introduce Nemotron-Labs-VisualCreation, an agentic framework that connects these capabilities through Pixel as Code. Raster images are represented by learned discrete visual tokens, while structured artifacts use explicit programs. A shared generation-and-rendering interface connects these representations to…

## 7. Motion Mamba 2.0: Autoregressive Diffusion Mamba for Long-Horizon Humanoid Control

- 分数：34.0  ·  HF 赞：187  ·  来源：huggingface
- 兴趣命中：agent, memory, evaluation
- 作者：Yue Huang, Tianshan Zhang, Zeyu Zhang, Jayeon Kang, Akide Liu, Sungjoon Choi, Dacheng Tao, Hao Tang
- 链接：[arXiv](https://arxiv.org/abs/2611.29897) · [PDF](https://arxiv.org/pdf/2611.29897) · [HF](https://huggingface.co/papers/2611.29897)

Long-horizon, real-time controllable motion generation is essential for interactive animation and humanoid robotics, where an agent must respond to changing instructions and spatial goals while moving. Existing autoregressive diffusion methods generate motion incrementally, but bounded attention caches limit access to distant history, while repeated denoising introduces substantial inference overhead. We present…

## 8. A Glimpse of Training VLMs as Foundation Models for Robotic Manipulation

- 分数：34.0  ·  HF 赞：55  ·  来源：huggingface
- 兴趣命中：benchmark, language model, spec
- 作者：Meng-Hao Guo, Yi Zhang, Zhe-Han Mo, Han-Zheng Wang, Jia-Jun Wang, Xin-Sheng Chen, Jiaxi Song, Yi-Xuan Deng, Jia-Ning Li, Xuanyu Chu, Hengrui Zhang, Huan-ang Gao, Yongming Rao, Shi-Min Hu
- 链接：[arXiv](https://arxiv.org/abs/2611.29338) · [PDF](https://arxiv.org/pdf/2611.29338) · [HF](https://huggingface.co/papers/2611.29338)

Recently, GPT-6 Astra demonstrates strong generalization in robot control, yet limited disclosure of its training leaves open how such capabilities can be reproduced. We introduce nanoAstra, an approach to training vision-language models (VLMs) for generalizable manipulation that combines semantic action modeling with capability-preserving supervised fine-tuning (CP-SFT). nanoAstra represents robot behavior as…

## 9. ACAP: Asynchronous Coding Agents for Efficient Robot Control

- 分数：34.0  ·  HF 赞：49  ·  来源：huggingface
- 兴趣命中：agent, reasoning, coding
- 作者：Zexin He, Rui Li, Yushi Lan, Chengkai Jin, Zhi Hou, Xingang Pan
- 链接：[arXiv](https://arxiv.org/abs/2611.31205) · [PDF](https://arxiv.org/pdf/2611.31205) · [HF](https://huggingface.co/papers/2611.31205)

Coding agents can construct and revise robot behavior during execution, but using one agent for the whole robot can delay otherwise independent work. We introduce Asynchronous Coding Agents as Policy (ACAP), an asynchronous framework that organizes one robot as a team of persistent agents. Each member reasons and acts for a configurable control group, such as an arm with its gripper or the torso and chassis,…

## 10. ViDecide: Teaching Video Diffusion Models to Reason and Plan Step by Step

- 分数：34.0  ·  HF 赞：41  ·  来源：huggingface
- 兴趣命中：reasoning, benchmark, planning
- 作者：Kaiwen Zhang, Yiming Gao, Zeqi Xiao, Xintao Wang, Pengfei Wan, Kun Gai, Xingang Pan
- 链接：[arXiv](https://arxiv.org/abs/2611.26389) · [PDF](https://arxiv.org/pdf/2611.26389) · [HF](https://huggingface.co/papers/2611.26389)

Current leading video generation models can synthesize highly realistic videos, while still frequently violating physical and logical constraints in multi-step reasoning and planning, even after training with large-scale reasoning data or existing diffusion RL methods. We attribute these failures to the conventional video training paradigm, which treats a solution as a fixed-length clip rather than a chain of…

## 11. Innata-0: A Native Embodied World System with Model-Agent Co-Design

- 分数：33.0  ·  HF 赞：34  ·  来源：huggingface
- 兴趣命中：agent, memory, evaluation, planning
- 作者：Innata Team, Yu Bai, Ziyi Bai, Yuxuan Cai, Chenrui He, Wenhao Li, Zhe Lin, Heng Wang, Hai Yuan, Zhiwei Yu, Yuanhang Zhang, Luyou Chen, Tiezhu Gao, Zheng Geng, Jinbang Guo, Dongxu Han, Diqi He, Börje F. Karlsson, Jintao Li, Zhiyu Li, Xiongkun Linghu, Guang Liu, You Liu, Zhen Luo, Mengsi Lyu, Yufeng Lyu, Zheng Lyu, Quanyue Ma, Chunlei Men, Ziqiang Ni, Tengfei Pan, Yijun Shen, Liang Sun, Shaoxuan Xie, Xiang Yang, Guocai Yao, Hongjun Zhang, Yingli Zhao, Yonghua Lin, Zhongyuan Wang, Huan Yang
- 链接：[arXiv](https://arxiv.org/abs/2611.30254) · [PDF](https://arxiv.org/pdf/2611.30254) · [HF](https://huggingface.co/papers/2611.30254)

The physical world is open-ended, dynamic, and partially observable. While foundation models have advanced embodied intelligence, standalone models struggle with long-horizon execution, and simply integrating models with agents may lead to inconsistencies between planning and physical control. To support reliable and adaptive behaviors in the physical world, we introduce Innata-0, a native embodied world system.…

## 12. Lazy Agents Answer Against Their Own Beliefs: Reinforcement Learning with Verifiable Beliefs Teaches Them to Act on What They Believe

- 分数：33.0  ·  HF 赞：26  ·  来源：huggingface + arxiv
- 兴趣命中：agent, reinforcement learning, evaluation, benchmark, language model
- 作者：Richmond Sin Jing Xuan, Peilin Feng, Wenbin Wang, Soujanya Poria
- 链接：[arXiv](https://arxiv.org/abs/2611.32884) · [PDF](https://arxiv.org/pdf/2611.32884) · [HF](https://huggingface.co/papers/2611.32884)

AI agents working on long tasks often commit to an answer before they have enough evidence, a behavior called laziness. In our evaluations, they frequently commit even while their stated belief still names several possible answers. An outcome reward at the end of the episode scores only the final answer, so it cannot teach the agent when to commit, because a lucky guess receives the same reward as an answer backed…

## 13. PartAgent: Agentic 3D Part Segmentation via Expert Integration and Closed-Loop Refinement

- 分数：32.5  ·  HF 赞：29  ·  来源：huggingface + arxiv
- 兴趣命中：agent, reasoning, spec
- 作者：Yang Cao, Zhe Zhu, Yiheng Zhang, Zhengqiang Zhang, Haoyuan Li, Le Wan, Dan Xu
- 链接：[arXiv](https://arxiv.org/abs/2611.32554) · [PDF](https://arxiv.org/pdf/2611.32554) · [HF](https://huggingface.co/papers/2611.32554)

Segmenting a 3D object into semantically meaningful parts requires joint reasoning about geometric structure and semantic context. Pretrained 3D experts provide spatially grounded region proposals, while 2D experts provide semantic cues for identifying object parts. The challenge is to integrate these complementary capabilities into a framework that can both produce meaningful part segmentations and progressively…

## 14. S-Mind: Internalizing Multi-View Geometry for Spatial Intelligence

- 分数：32.0  ·  HF 赞：32  ·  来源：huggingface
- 兴趣命中：agent, reasoning, benchmark, language model, large language
- 作者：Muxin Fu, Peike Yu, Guibin Zhang, Wenrui Zhou, Runze Liu, Lang Feng, Fuchao Yang, Feng Chen, Yixuan Li, Mengao Zhang, Shiying Zhang, Wen Shen, Ling Pan, Shuicheng Yan, Bo An
- 链接：[arXiv](https://arxiv.org/abs/2611.28649) · [PDF](https://arxiv.org/pdf/2611.28649) · [HF](https://huggingface.co/papers/2611.28649)

Spatial intelligence, the ability to reason about 3D space from visual observations, becomes essential as multimodal large language models (MLLMs) move into the physical world. Beyond perceiving each view, it rests on two cornerstones of human cognition: fusing multiple views into one coherent 3D scene and mentally transforming that scene to new viewpoints as reasoning unfolds. Yet our spatial probes reveal that…

## 15. Embodied AI Fails the Mirror Test: How a Simple Mirror Breaks Robot Policies

- 分数：31.0  ·  HF 赞：22  ·  来源：huggingface + arxiv
- 兴趣命中：agent, evaluation, benchmark, spec
- 作者：Xuanchen Liu, Hejun Zhang, Boxuan Dong, Ying Wu, Heshuai Li, Wen Gao, Yonghong Tian, Weihao Yu
- 链接：[arXiv](https://arxiv.org/abs/2611.33010) · [PDF](https://arxiv.org/pdf/2611.33010) · [HF](https://huggingface.co/papers/2611.33010)

Can a simple mirror expose the limitations of today's robotic manipulation policies? Inspired by the mirror self-recognition test in animal cognition, we investigate whether robot policies can reliably manipulate physical objects in scenes containing their reflections. We introduce RoboDojo-Mirror, a benchmark built on RoboDojo that preserves task objectives, success criteria, and policy checkpoints while comparing…

## 16. Rewirable Circuits in Transformers with Loom Attention

- 分数：30.0  ·  HF 赞：36  ·  来源：huggingface
- 兴趣命中：memory, language model
- 作者：Da Xiao, Qingye Meng, Shengping Li, Xingyuan Yuan
- 链接：[arXiv](https://arxiv.org/abs/2611.30634) · [PDF](https://arxiv.org/pdf/2611.30634) · [HF](https://huggingface.co/papers/2611.30634)

We propose loom attention, which allows a Transformer to dynamically rewire its circuits at every token by interweaving a head's vertical attention over the outputs of earlier heads (to obtain its query, key and value) with its horizontal attention over tokens. We instantiate vertical attention efficiently with normalized and gated linear attention over a per-token matrix memory, which stores the compressed head…

## 17. Don't Sleep, Keep Watch: Proactive Perception for Computer-Use Agents

- 分数：29.5  ·  HF 赞：31  ·  来源：huggingface
- 兴趣命中：agent, reasoning, language model
- 作者：Jiaqi Su, Jie-Jing Shao, Yichen Liu, Long-Kai Huang, Haiyan Yin
- 链接：[arXiv](https://arxiv.org/abs/2611.28947) · [PDF](https://arxiv.org/pdf/2611.28947) · [HF](https://huggingface.co/papers/2611.28947)

Computer-use agents (CUAs) built on vision-language models are increasingly entrusted with long-horizon tasks in live desktop, web, and mobile environments, where the screen keeps changing on its own. However, current CUAs lack real-time situational awareness: they perceive the environment through discrete snapshots, and the substantial inference latency of VLMs, compounded by highly dynamic interfaces, opens a…

## 18. LingSante MedGuard Technical Report

- 分数：27.5  ·  HF 赞：23  ·  来源：huggingface
- 兴趣命中：agent, reasoning, evaluation, benchmark, spec, retrieval
- 作者：LingSante MedGuard Team
- 链接：[arXiv](https://arxiv.org/abs/2611.25509) · [PDF](https://arxiv.org/pdf/2611.25509) · [HF](https://huggingface.co/papers/2611.25509)

As medical AI is increasingly used for patient consultation and clinical decision support, identifying harmful, non-compliant, or ethically problematic responses is essential for responsible deployment. Assessing these risks requires checking clinical claims against relevant evidence, verifying calculations, and applying medical requirements under their intended conditions. We introduce LingSante MedGuard, a…

## 19. AutoPILOT: A Visual Agent Harness for Real-Time Gameplay

- 分数：27.0  ·  HF 赞：34  ·  来源：huggingface
- 兴趣命中：agent
- 作者：Mark Zhao, Pengcheng Wang, Rui Yang, Jiarui Yao, Xirui Jiang, Yuxi Chen, Bingxuan Li, Hanyang Chen, Ke Yang, Manling Li, Tong Zhang, Huan Zhang
- 链接：[arXiv](https://arxiv.org/abs/2611.28202) · [PDF](https://arxiv.org/pdf/2611.28202) · [HF](https://huggingface.co/papers/2611.28202)

Multimodal foundation models can play video games well when the game waits for them, but often fail when it keeps running. We find that much of this gap lies in the harness, which decides what the model sees, what it remembers, and how its outputs become actions over time. Existing harnesses such as VISTA improve the first two, yet turn each model call into at most one action, so the agent acts only as often as its…

## 20. Composable Soft-Prompt Distillation of RL Experts: Toward Continual Post-Training

- 分数：27.0  ·  HF 赞：30  ·  来源：huggingface
- 兴趣命中：agent, benchmark
- 作者：Zhen Zhang, Changyi Yang, Xuehai He, Chengzhi Liu, Yutong Yin, Ziyue Liu, Zhuoran Yin, Yangmin Li, Zhihan Liu, Jisen Li, Mingyu Jin, Chuhan Li, Zhaotian Weng, Ruoyu He, Wenyao Gao, Jiaxin Deng, Chenwei Wu, Hui Shen, Wenhao Chai, Chenyang Zhao, Zhuofan Ying, Kieran Liu, Andrew Chen, Pony Ma, Zhaoran Wang, Alkesh Patel, Zhe Gan, Xin Eric Wang
- 链接：[arXiv](https://arxiv.org/abs/2611.27376) · [PDF](https://arxiv.org/pdf/2611.27376) · [HF](https://huggingface.co/papers/2611.27376)

RL post-training typically produces domain experts that must then be consolidated into one model, and as new experts keep arriving, this consolidation becomes a continual process. Weight merging and multi-teacher on-policy distillation (MOPD) must re-consolidate the whole model whenever an expert is added, and can erode capabilities outside the target domains. We propose Composable Soft-Prompt Distillation (CSPD),…

## 21. Self-Evolving Evaluation Environments for Computer-Use Agents

- 分数：26.0  ·  HF 赞：24  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark
- 作者：Wenhao Wang, Panrong Tong, Quyu Kong, Pengxiang Li, Haowen Yang, chenglin Cai, Siheng Chen, Yue Wang
- 链接：[arXiv](https://arxiv.org/abs/2611.30962) · [PDF](https://arxiv.org/pdf/2611.30962) · [HF](https://huggingface.co/papers/2611.30962)

Computer-use agents (CUAs) are rapidly improving, yet their evaluation remains largely static. Existing benchmarks provide a strong foundation, but fixed difficulty ceilings, limited feature coverage, and coarse aggregate scores progressively weaken their discriminative and diagnostic value. We introduce CUA-SEE, a closed-loop evaluation environment that co-evolves tasks and executable verifiers from rollout…

## 22. DiLE: Discrimination-Aware Latent-Space Learning for Universal Multimodal Embeddings

- 分数：25.0  ·  HF 赞：18  ·  来源：huggingface
- 兴趣命中：reasoning, language model, large language, spec, retrieval
- 作者：Ben Kang, Junda Wang, Yuxuan Yuan, Hang Li, Yuhan Liu, Xin Chen, Wanting Geng, Tong Lin, Pei Fu, Dong Wang, Jian Luan, Huchuan Lu
- 链接：[arXiv](https://arxiv.org/abs/2611.25419) · [PDF](https://arxiv.org/pdf/2611.25419) · [HF](https://huggingface.co/papers/2611.25419)

Multimodal large language models have greatly improved input understanding in universal multimodal embedding models. However, this understanding does not ensure that their embeddings preserve the evidence needed to distinguish relevant items from confusable alternatives. To preserve essential discriminative evidence in embeddings, this paper proposes DiLE, a discrimination-aware latent-space learning framework that…

## 23. Plan4D: Generative Plannable 4D Worlds

- 分数：24.5  ·  HF 赞：29  ·  来源：huggingface
- 兴趣命中：spec
- 作者：Hangwei Zhang, Rujing Dang, Ruimin Lin, Jiahong Wu, Xiangxiang Chu, Chuanxia Zheng
- 链接：[arXiv](https://arxiv.org/abs/2611.26516) · [PDF](https://arxiv.org/pdf/2611.26516) · [HF](https://huggingface.co/papers/2611.26516)

Most world models for future prediction prioritize aestetic quality of generated videos, but offer only weak physical grounding and limited geometric consistency over time, due to the lack of explicit 4D modeling. In this paper, we introduce plan4d, a possible next milestone towards building a generative plannable 4D world model that predicts future RGB videos together with dense 4D geometry, including depth,…

## 24. KMed-31B Technical Report

- 分数：24.5  ·  HF 赞：17  ·  来源：huggingface
- 兴趣命中：benchmark, language model, large language, spec
- 作者：KMed Team
- 链接：[arXiv](https://arxiv.org/abs/2611.28719) · [PDF](https://arxiv.org/pdf/2611.28719) · [HF](https://huggingface.co/papers/2611.28719)

We present KMed-31B, a medical large language model post-trained from an open-weight model for on-premises deployment with limited hardware. Post-training a model for diverse medical tasks remains difficult, because improving one kind of task can lower performance on another. We attribute this to differences between tasks in expected output and available feedback. Medical question answering and diagnosis prediction…

## 25. What Makes Good Data for Training Coding Agents? A Systematic Study on SWE-Gym

- 分数：24.5  ·  HF 赞：17  ·  来源：huggingface
- 兴趣命中：agent, reinforcement learning, coding, spec
- 作者：Yikai Zhang, Mai Xu, Yunbei Zhang, Qirui Jin, Kenan Li, Yuwen Jia, Jinwei Yao, Xiangyu Zhang, Jielun Tan, Jin Pan, Zijian Jin, Xiao Sun
- 链接：[arXiv](https://arxiv.org/abs/2611.30207) · [PDF](https://arxiv.org/pdf/2611.30207) · [HF](https://huggingface.co/papers/2611.30207)

Reinforcement learning (RL) trains coding agents on software tasks whose hidden tests decide the reward, yet task collections check these tests only against the reference fix. We ask what makes a task good training data, focusing on the correctness of its reward labels. We audit SWE-Gym with two LLM families, and a suspected error counts only if execution reproduces it. We find that unsolved often means mislabelled:…

## 26. World Models as Native Latent Action Models

- 分数：23.5  ·  HF 赞：27  ·  来源：huggingface
- 兴趣命中：benchmark
- 作者：Qinyue Li, Weijie Qiao, Qingyi Tao, Zerui Gong, Zhe Yang, Quanzhou Li, Taolin Zhang, Jinglin He, Zhonghua Wu, Chen Change Loy
- 链接：[arXiv](https://arxiv.org/abs/2611.30898) · [PDF](https://arxiv.org/pdf/2611.30898) · [HF](https://huggingface.co/papers/2611.30898)

Large and diverse video sources, such as egocentric human video and heterogeneous robot recordings, carry rich dynamics but come either without actions or without a shared action space. Latent action models (LAMs) can recover these dynamics, but they train their inverse- and forward-dynamics models (IDM, FDM) from scratch, trading off pixel reconstruction against latent capacity and accuracy. Pretrained video world…

## 27. Beam Model Technical Report

- 分数：23.5  ·  HF 赞：15  ·  来源：huggingface
- 兴趣命中：agent, context window, reasoning, reinforcement learning, evaluation, coding, spec
- 作者：Reflection Team, Adam Abdulhamid, Osama Abuelsorour, Yasmin Alameddine, Carlo Alfano, Duarte Alves, Brandon Amos, Selvaraj Anandaraj, Arseni Anisimovich, George Antoniadis, Ioannis Antonoglou, Sheila Babayan, Neeraj Bahl, Märt Bakler, Vidhisha Balachandran, Cameron Banks, Thibaut Barroyer, Navroop Bath, Irwan Bello, Jeremy Berman, Fernanda Bernaldo, Mrityunjay Bhadauria, Sanyam Bhutani, Tolga Bolukbasi, Anudhyan Boral, Joseph Brennan, Ethan Brooks, Sam Buchanan, Anton Bulyenov, John Cai, Catherine Cang, Eason Chan, Elijah Chanakira, Nathan Chandrasekaran, Hao Chen, Hong-You Chen, Jeffrey Chen, Saurav Chhatrapati, Ting-Rui Chiang, Brian Tiger Chow, Aakanksha Chowdhery, Timothy Chung, Rob Claire, John D. Co-Reyes, Anthony Conte, Eduardo Coronado-Montoya, Julien Crozon, Drew Csillag, Joe Cummings, Jeff Da, Samira Daruki, Tim Dawson, Charlie Deck, Arash Delijani, Ousmane Dia, Randy Dodgen, Ryan Douglas, Omar El-Kishky, Ben Ellis, Gamaleldin Elsayed, Simon Fan, Patrick Fernandes, Gabriel Ferns, Nick Fram, Ankush Garg, Florent Gbelidji, Iaroslav Geraskin, Behrooz Ghorbani, Ivan Glushkov, Neil Gollapudi, Scott Goodfriend, Yoni Gozlan, Christopher Grimm, Suriya Gunasekar, Shruti Gupta, Joel Gustafson, Emre Guven, Jon Hackmann, Jeremy Hadidjojo, Jess Hamrick, Ethan Hellman, Joscha Hoche, Spurthi Amba Hombaiah, Uzair Honda, Zijian Hu, Dzmitry Huba, Nancy Hung, Vladimir Ivanov, Shomik Jain, Mojan Javaheripi, Kevin Martin Jose, Aymen Kallala, Amog Kamsetty, Min Hyung Kang, Steven Kapturowski, Ramtin Keramati, Samuel Kessler, Sabina Kim, Seonghyeon Kim, Ivan Komarov, Agni Kumar, Thanard Kurutach, Jessica Landon, James Larochelle, Michael Laskin, Jonathan Lee, Jonathan Leung, Chenyu Li, Haoran Li, Rongzhao Li, Michelle Light, Boyan Lin, Hai Lin, Xiayue Charles Lin, Michael Linden, Ollie Liu, Wei Liu, Zichang Liu, Brian Lui, Amr Mahdi, Raunak Manjani, Kobe Martin, Lucas Maystre, Francis McCann, Brendan McLaughlin, Isabel Mehta, Alishah Momin, Gerard Moreno-Torres Bertran, Adriana Murga, Swarnashree Mysore Sathyendra, Ashley Nagaki, Vishal Nandavanam, Swaroop Nath, Jake Nations, Angus Ng, Thien Nguyen, Tyler Nichols, Anaelia Ovalle, James Pelly, Michelle Pieszko, Sashank Pisupati, Oleksandr Polozov, Piyush Prasad, Drew Proud, Salman Quazi, Asfandyar Qureshi, Marko Radmilac, Mohit Raghavendra, Vikash Rai, Ralph Recto, Anurag Reddy, Aksel Reedi, Abby Reider, David Renardy, Matthias Reso, Pierre Roux, David Rubinstein, Paul Ruh, Ildar Safarov, Himanshu Sahni, Adrian Samatan, Simon Sandrew, Adriel Saporta, Rohan Savargaonkar, Vlad Savinov, Nick Schank, Jonathon Schwartz, Tim Seah, Ahmad Sharif, Miriam Shlimovich, Hamid Shojanazeri, Yusuf Sindi, Teak Sittipunt, Kurt Smith, Nicolas Sonnerat, Joe Spisak, Raunak Srivastava, Richard Steigerwald, Adam Stein, Stu Stewart, Arnaud Stiegler, Jingtong Su, Alicia Sun, Zoey Sun, Jakub Sygnowski, Douglas Teixeira, Chetan Tekur, Zachary Tellman, Helen Thatcher, Romal Thoppilan, Anil Tolwani, Konstantin Topaloglou-Mundy, Dmitry Ulyumdzhiev, Meet Vadakkanchery, Christopher Vanderschuere, Balaji Varadarajan, Rohan Varma, Balaji Veeramani, Andreas Verdelis, Risto Vuorio, Tom Walshe, Allen Wang, Ewen Wang, Taiyi Wang, Zach Wentz, Peter Wiese, Travis Wilson, Jason Winters, Sam Wiseman, Arvin Wu, Jin Wu, Kai Wu, Kenneth Xu, Mira Yadav, Xianjun Yang, Yao-Yuan Yang, Xiaolan You, Renault Young, Christina Yu, Biao Zhang, Gavin Zhang, Mingrui Zhang, Shenao Zhang, Jiesi Zhao, Mengjun Zhao, Xingchen Zhao, Mike Zhou, Tong Zhou, Zhenpeng Zhou, Tina Zhu
- 链接：[arXiv](https://arxiv.org/abs/2611.26358) · [PDF](https://arxiv.org/pdf/2611.26358) · [HF](https://huggingface.co/papers/2611.26358)

Beam is a sparse Mixture-of-Experts (MoE) model with 501.3B total parameters and 23.4B active parameters, specifically built and optimized for coding, reasoning, and agentic workloads. Beam delivers frontier level reasoning, while requiring 3-4x less inference compute than many models of its class. Pretrained on 23.8T diverse, curated, high-quality tokens, Beam features a 1M-token context window achieved through a…

## 28. PhyCoVE: Benchmarking Physical Counterfactual Video Editing across Diverse Material Dynamics

- 分数：23.5  ·  HF 赞：15  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark, language model, coding, spec
- 作者：Conghan Yue, Yuanjie Chen, Yunyan Xiao, Zeyu Peng, Xingsong Ye, Ya Gao, Yanglin Huang, WeiYao Zhang, Yue Han, Zhineng Chen, Yu-Gang Jiang
- 链接：[arXiv](https://arxiv.org/abs/2611.29184) · [PDF](https://arxiv.org/pdf/2611.29184) · [HF](https://huggingface.co/papers/2611.29184)

Physical counterfactual video editing turns a source video and a language-specified physical edit at a given execution frame into a counterfactual video that shows how the scene would evolve after the edit. Existing evaluations with counterfactual target videos mainly cover object removal or specific rigid-body motions, although real scenes also involve elastic deformation, fluid flow, and interactions among rigid…

## 29. GameAnything: From Any Inspirations to Playable Game Worlds

- 分数：23.0  ·  HF 赞：14  ·  来源：huggingface
- 兴趣命中：agent, memory, evaluation, benchmark, coding, spec
- 作者：Wenyi Wu, Siqi Liu, Yuru Feng, Zixuan Song, Aayush Salvi, Sibo Zhu, Kun Zhou, Biwei Huang
- 链接：[arXiv](https://arxiv.org/abs/2611.29238) · [PDF](https://arxiv.org/pdf/2611.29238) · [HF](https://huggingface.co/papers/2611.29238)

AI-driven game development holds the potential to transform diverse human inspirations into interactive experiences. However, existing systems and benchmarks primarily focus on explicit development specifications, with limited support for adapting multimodal references and evaluating actual gameplay experiences. We introduce GameAnything, an open-source agentic platform that transforms multimodal inspirations into…

## 30. ThinkMorph-SSL: Scaling Interleaved Multimodal Reasoning with Pretext Tasks

- 分数：22.5  ·  HF 赞：17  ·  来源：huggingface
- 兴趣命中：reasoning, benchmark, spec
- 作者：Jiawei Gu, Linjie Li, Yiming Liu, Yunzhuo Hao, Huichen Wang, Guanzheng Chen, Zhichao Peng, Luxin Xu, Xinyu Zhang, Li Luo, Disen Lan, Zican Hu, Mingyang Song, David Valente, Alex Jinpeng Wang, Yafu Li, Ganqu Cui, Zhengyuan Yang, Qizhe Xie, Yejin Choi, Ranjay Krishna, Yu Cheng
- 链接：[arXiv](https://arxiv.org/abs/2611.32183) · [PDF](https://arxiv.org/pdf/2611.32183) · [HF](https://huggingface.co/papers/2611.32183)

People reason with pictures as well as words. Interleaved multimodal reasoning gives models a similar way to solve problems by creating intermediate images and using them to guide further reasoning. Training models with this ability usually relies on task-specific demonstrations, which are difficult to collect. We introduce ThinkMorph-SSL, a two-stage training recipe that uses images themselves as a source of…

## 31. Polytropos: What Do Vision-Language Model Descriptions Make of a Cultural Object?

- 分数：22.0  ·  HF 赞：16  ·  来源：huggingface
- 兴趣命中：benchmark, language model, spec
- 作者：Yuechen Jiang, Enze Zhang, Yuyan Wang, Mohsinul Kabir, Chenying Lin, Sijia Li, Qianqian Xie, Stavroula Golfomitsou, Konstantinos Arvanitis, Sophia Ananiadou
- 链接：[arXiv](https://arxiv.org/abs/2611.29355) · [PDF](https://arxiv.org/pdf/2611.29355) · [HF](https://huggingface.co/papers/2611.29355)

Vision-language models have become a new kind of describer, writing about almost anything people see, and their descriptions now shape how cultures are known by people and by other models. Descriptions of cultures tend to turn particular things into types, and what a description loses shows what its describer lacks. We introduce Polytropos, a benchmark that measures what model descriptions of cultural objects keep…

## 32. RUIBench: What Makes a Good Robot-Use Interface?

- 分数：21.0  ·  HF 赞：22  ·  来源：huggingface
- 兴趣命中：agent
- 作者：Yanzhe Chen, Zhijun Cao, Zechen Bai, Wenzheng Zeng, Kevin Yuchen Ma, Yiqi Lin, Guoqiang Liang, Xiaokang Liu, Ke Sun, Kevin Qinghong Lin, Mike Zheng Shou
- 链接：[arXiv](https://arxiv.org/abs/2611.31115) · [PDF](https://arxiv.org/pdf/2611.31115) · [HF](https://huggingface.co/papers/2611.31115)

Foundation models can reason about complex physical tasks, yet translating this intelligence into reliable robot execution remains challenging. We argue that a critical, often overlooked factor is the robot-use interface (RUI), which determines how agents express and execute physical actions. To systematically study its impact, we introduce RUIBench, comprising 30 manipulation tasks across five suites spanning world…

## 33. ToolSmith: An Automatic Tool-Generation Framework for Multimodal Search Agents

- 分数：21.0  ·  HF 赞：14  ·  来源：huggingface
- 兴趣命中：agent, reasoning, benchmark
- 作者：Rui Sun, Junhua Huang, Luca Zancato, Md Mofijul Islam, Kai-Wei Chang
- 链接：[arXiv](https://arxiv.org/abs/2611.31198) · [PDF](https://arxiv.org/pdf/2611.31198) · [HF](https://huggingface.co/papers/2611.31198)

Recent multimodal search agents use reasoning, vision, and live web search across many turns to answer questions beyond parametric knowledge by orchestrating a small library of hand-crafted search and visual tools. However, the library is laborious to create and maintain, and frozen when new query types, evidence formats, and failure modes are encountered in the wild. Human practitioners, by contrast, cope with…

## 34. MMMem: Self-Improving Agents with Task-Aware Multimodal Experience Consolidation

- 分数：21.0  ·  HF 赞：10  ·  来源：huggingface
- 兴趣命中：agent, memory, benchmark, language model, spec, retrieval
- 作者：Yuxuan Chen, Changwei Lv, Yunfei Li, Zhongjing Du, Kehui Tan, Zijun Liao, Ruochong Zheng, Hao Chen, Can Deng, Zheni Zeng, Chang Liu, Jie Chen
- 链接：[arXiv](https://arxiv.org/abs/2611.30287) · [PDF](https://arxiv.org/pdf/2611.30287) · [HF](https://huggingface.co/papers/2611.30287)

AI agents accumulate conversations, images, and documents through long-term interactions with users. Answering later questions often requires connecting evidence across these records, yet the resulting understanding is rarely retained, allowing mistakes to recur on related questions. Existing multimodal memory methods largely focus on storing and retrieving records, with limited mechanisms for learning from…

## 35. SAVIOR: Sample-efficient Adaptation of Vision-Language Models for OCR Representation

- 分数：20.5  ·  HF 赞：13  ·  来源：huggingface
- 兴趣命中：evaluation, benchmark, language model
- 作者：Akshata A Bhat, Sharath Naganna, Saiful Haq, Prashant Khatri, Krishna Chaitanya Reddy Tamataam, Neha Arun, Niyati Chhaya, Pushpak Bhattacharyya
- 链接：[arXiv](https://arxiv.org/abs/2611.27319) · [PDF](https://arxiv.org/pdf/2611.27319) · [HF](https://huggingface.co/papers/2611.27319)

Optical Character Recognition (OCR) pipelines and vision-language models exhibit high accuracy on standard OCR and document-understanding benchmarks, yet they systematically underperform on document patterns that are operationally critical in financial workflows. These patterns include vertical or rotated text, logo-embedded vendor names, fine-print regulatory clauses, degraded scans, and complex multi-column…

## 36. Qwen-Image-HD: Autoregressive Diffusion for High Definition Image Generation

- 分数：20.5  ·  HF 赞：13  ·  来源：huggingface + arxiv
- 兴趣命中：evaluation
- 作者：Zihao Liu, Zekai Zhang, Shengming Yin, Zikai Zhou, Donghao Zhou, Chenyang Zhu, Lihan Jiang, Ningyuan Tang, Bingxuan Zhao, Yanran Zhang, Yan Shu, Zhening Liu, Jiahao Li, Jie Zhang, Kaiyuan Gao, Kun Yan, Qihang Ai, Rui Song, Shuo Cao, Xiao Xu, Xiaoyue Chen, Yuxiang Chen, Zhendong Wang, Zhouyang Li, Bo Zheng, Jun Zhou, Xiu Li, Chenfei Wu
- 链接：[arXiv](https://arxiv.org/abs/2611.32736) · [PDF](https://arxiv.org/pdf/2611.32736) · [HF](https://huggingface.co/papers/2611.32736)

Fine-tuning a generator on a complete high-resolution canvas requires long image sequences and substantial computation, yet local regions can still exhibit unnatural repetitive stripes when training resources are limited. We introduce Qwen-Image-HD, which adapts Qwen-Image 2.0 to high-resolution synthesis through local training and blockwise autoregressive generation. Each prediction covers a target tile at 1K…

## 37. WorldLatent: A Unified 4D Latent Space for World Perception and Generation

- 分数：20.5  ·  HF 赞：9  ·  来源：huggingface
- 兴趣命中：benchmark, language model, large language, spec
- 作者：Jingxi Chen, Yujia Chen, Cornelia Fermuller, Yiannis Aloimonos, Wen-Sheng Chu, Du Tran
- 链接：[arXiv](https://arxiv.org/abs/2611.31209) · [PDF](https://arxiv.org/pdf/2611.31209) · [HF](https://huggingface.co/papers/2611.31209)

Generative Pre-Training (GPT) represents a profound milestone in natural language processing, serving as the foundation for most of today's state-of-the-art large language models. By casting diverse understanding and generation problems into a shared token representation, GPT enables a single architecture and unified optimization loop to master heterogeneous tasks across massive corpora, giving rise to powerful…

## 38. Distilling Visual Agents from Limited Interaction Experience

- 分数：20.0  ·  HF 赞：20  ·  来源：huggingface
- 兴趣命中：agent
- 作者：Siyu Zhou, Jing Jiang, Chengqi Zhang, Guodong Long
- 链接：[arXiv](https://arxiv.org/abs/2611.28618) · [PDF](https://arxiv.org/pdf/2611.28618) · [HF](https://huggingface.co/papers/2611.28618)

How much interaction experience is needed to distill a capable visual agent? We study learning from few tasks and recorded interaction histories. Our framework selects representative trajectories using skill-context coverage and ordered visual-decision similarity. On-policy distillation (OPD) learns through fresh interaction on selected tasks or fresh student responses at fixed histories. Across Navigation, Sokoban,…

## 39. ViDiHand2: Unifying Video Diffusion Priors and Hand Geometry for 3D Hand Motion Reconstruction in the Wild

- 分数：20.0  ·  HF 赞：20  ·  来源：huggingface
- 兴趣命中：spec
- 作者：Yuxi Wang, Yufei Liu, Chengkai Jin, Qingyue Chen, Wenqi Ouyang, Tianyi Wei, Kerui Ren, Siyuan Huang, Zhiqi Shen, Hongsheng Li, Xingang Pan
- 链接：[arXiv](https://arxiv.org/abs/2611.30597) · [PDF](https://arxiv.org/pdf/2611.30597) · [HF](https://huggingface.co/papers/2611.30597)

Learning robot manipulation from egocentric human videos requires accurate metric 3D hand motion. Recent methods leverage pretrained video diffusion model (VDM) priors to recover occluded hands directly from full-frame videos, but their appearance-based depth regression generalizes poorly to unseen cameras. In this work, we propose ViDiHand2, a geometry-driven framework that reformulates VDM-based hand depth…

## 40. Open Vision Banana: An Open Framework for Unified Visual Perception through Generation in RGB Space

- 分数：20.0  ·  HF 赞：16  ·  来源：huggingface
- 兴趣命中：evaluation, spec
- 作者：Xu Lin, Ruilin Yao, Haoran Xu, Zixiang Wang, Ming Ma, Yu Zhao, Pu Miao, Chonghan Liu
- 链接：[arXiv](https://arxiv.org/abs/2611.28489) · [PDF](https://arxiv.org/pdf/2611.28489) · [HF](https://huggingface.co/papers/2611.28489)

Vision Banana showed that a closed image generator, instruction-tuned to paint perception outputs as RGB images, becomes a generalist vision model. Does this carry over to open generators, and if not, what fails? We answer with Open Vision Banana (OVB), an open framework that adapts the 7B diffusion generator of Qwen-Image-2.1 into one instruction-driven model for metric depth, semantic, instance, and referring…

## 41. UUBench: Understanding the Unspoken toward Full-Duplex Multimodal Interaction

- 分数：20.0  ·  HF 赞：16  ·  来源：huggingface
- 兴趣命中：evaluation, benchmark
- 作者：Ye Pan, Chenfei Liao, Bin Ren, Hanqian Li, Haocong He, Jialei Chen, Jinlin He, Kunyu Peng, Mengyu Jin, Shijie Li, Wenqian Cui, Yuanqi Yao, Yuqian Fu, Kailong Ruan, Yuan Gao, Wei Wang, Xuming Hu, Irwin King, Nicu Sebe, Xu Zheng
- 链接：[arXiv](https://arxiv.org/abs/2611.30157) · [PDF](https://arxiv.org/pdf/2611.30157) · [HF](https://huggingface.co/papers/2611.30157)

Effective real-time, full-duplex multimodal interaction requires systems to understand not only what users say, but also the communicative needs conveyed through prosody, facial expressions, gestures, and context, and to generate audiovisual responses that appropriately address those needs. Existing evaluations offer limited insight into whether systems translate an understanding of such unspoken needs into…

## 42. MAGPIE: Agentic Multi-Reference Image Generation via Executable Scene Construction

- 分数：20.0  ·  HF 赞：12  ·  来源：huggingface
- 兴趣命中：agent, coding, spec
- 作者：Yifan Dai, Daili Hua, Bohan Zeng, Yuran Wang, Jialing Liu, Bozhou Li, Chengzhuo Tong, Yang Shi, Kai Zeng, Liu Yang, Xinyu Liu, Shujie Li, Yiyan Ji, Bingyin Mei, Yushuo Guan, Yuanxing Zhang, Fangcheng Fu, Wentao Zhang
- 链接：[arXiv](https://arxiv.org/abs/2611.32462) · [PDF](https://arxiv.org/pdf/2611.32462) · [HF](https://huggingface.co/papers/2611.32462)

Multi-reference image generation requires a model to preserve the appearance of selected subjects while arranging them according to an instruction. Despite recent progress in reference-based generation and compositional control, reliably organizing selected subjects into the intended scene remains challenging. Although existing methods provide various forms of compositional guidance, the planned relationships are…

## 43. SynthDCB: World Distillation for Scalable Device Control Benchmarking

- 分数：20.0  ·  HF 赞：8  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark, spec
- 作者：Zichen Zhu, Dingye Liu, Nan Jiang, Danyang Zhang, Hang Zheng, Shijie Zheng, Situo Zhang, Kunyao Lan, Yingzi Ma, Sheng Jiang, Lu Chen, Kai Yu
- 链接：[arXiv](https://arxiv.org/abs/2611.18639) · [PDF](https://arxiv.org/pdf/2611.18639) · [HF](https://huggingface.co/papers/2611.18639)

Scaling device-control evaluation requires scaling both interactive worlds and the tasks agents must solve. We introduce SynthDCB, a benchmark for environment awareness and device control built through world distillation (WD). World distillation transforms knowledge of device behaviors, constraints, and environmental effects into modular executable components. A unified capability representation connects tool…

## 44. GameDojo: Benchmarking Real-Time Interactive Agents in Video Games

- 分数：20.0  ·  HF 赞：8  ·  来源：huggingface
- 兴趣命中：agent, benchmark, coding, spec
- 作者：Kuan Zhang, Zhihao Yang, Yukun Chen, Xingyilang Yin, Mingyu Ouyang, Yue Su, Xiangnan Wu, Jiaming Li, Longze Chen, Run Luo, Zirong Chen, Lu Wang, Yiming Li
- 链接：[arXiv](https://arxiv.org/abs/2611.30771) · [PDF](https://arxiv.org/pdf/2611.30771) · [HF](https://huggingface.co/papers/2611.30771)

Interactive intelligence requires agents to act on observations and adapt to the consequences of actions. Studying these abilities calls for diverse, challenging tasks under controlled conditions. We introduce GameDojo, a controllable interactive gameplay benchmark of 120 boss encounters across 20 games for evaluating model capabilities, learning algorithms, and agent harnesses. Coding agents reconstruct the…

## 45. Embodied-Harness: Towards Recursive Self-Improvement for Robotic Manipulation

- 分数：20.0  ·  HF 赞：8  ·  来源：huggingface
- 兴趣命中：agent, memory, reasoning, evaluation, benchmark, language model, spec, planning
- 作者：Zhenxuan Fan, Zhuoya Wang, Yuqian Yuan, Wenqiao Zhang, Juncheng Li, Jun Xiao, Siliang Tang, Yueting Zhuang
- 链接：[arXiv](https://arxiv.org/abs/2611.27689) · [PDF](https://arxiv.org/pdf/2611.27689) · [HF](https://huggingface.co/papers/2611.27689)

Vision-language model (VLM)-based agents offer a promising approach to robotic manipulation, yet remain limited by inadequate memory organization, uncertain failure attribution, and limited reuse of execution experience. We propose Embodied-Harness, a dual-agent framework that improves manipulation by refining the execution harness without updating model parameters. The Actor interacts with the environment through a…

## 46. Antom 3-in-1 Transformer: A Payment Foundation Model

- 分数：19.0  ·  HF 赞：22  ·  来源：huggingface
- 兴趣命中：-
- 作者：Weiyu Han, Haoyu Jiang, Jie Sheng, Youxi Pan, Xianglong Liu, Zeqi Ren, Dongquan Yi, Yinhao Liu, Ruobing Zuo, Ze Zhao, Huilin He, Nairong Zhang, Xinyi He, Xiao Tan, Jun Wang, Pan Fang, Wei Zeng, Jianan Su, Kaixin Shen, Jingtong Wu, Hao Li, Shuai Chen, Jiangming Yang, Tianyi Zhang
- 链接：[arXiv](https://arxiv.org/abs/2611.25403) · [PDF](https://arxiv.org/pdf/2611.25403) · [HF](https://huggingface.co/papers/2611.25403)

We report the development of Antom 3-in-1 Transformer, a payment foundation model that integrates sequence, tabular, and graph representations for payment risk detection. The model contains approximately 7B parameters, with approximately 1.7B activated per task route. Antom 3-in-1 Transformer is pretrained to learn reusable behavioral and relational representations, primarily on Ant International's internal payment…

## 47. VideoJSON: A Minimal Harness Beats Purpose-Built Memory for Ultra-Long Video Understanding

- 分数：19.0  ·  HF 赞：6  ·  来源：huggingface
- 兴趣命中：agent, memory, benchmark, language model, coding, spec, retrieval
- 作者：Wenqi Marshall Guo, Kuan-Hao Huang, Junda Chen, Hao Zhang
- 链接：[arXiv](https://arxiv.org/abs/2611.28167) · [PDF](https://arxiv.org/pdf/2611.28167) · [HF](https://huggingface.co/papers/2611.28167)

Answering questions over days or weeks of video requires searching for scattered clues across long timelines. Existing video agents rely on complex memory graphs and fixed retrieval pipelines, which restrict how the agent can search. We propose VideoJSON, a minimal harness for ultra-long video understanding that keeps the memory simple and lets a coding agent write its own search programs. During indexing, a…

## 48. GlanceNav: Efficient Vision-and-Language Navigation with Streaming Memory and Counterfactual Rewind

- 分数：18.5  ·  HF 赞：5  ·  来源：huggingface
- 兴趣命中：memory, reinforcement learning, language model, large language
- 作者：Anh Dao, Quan-Dung Pham, Danh Vinh Le, Tuyen Pham Le, Quan Nguyen, Yuzhang Shang
- 链接：[arXiv](https://arxiv.org/abs/2611.30900) · [PDF](https://arxiv.org/pdf/2611.30900) · [HF](https://huggingface.co/papers/2611.30900)

Multimodal large language models (MLLMs) have become strong policies for vision-and-language navigation (VLN). However, most of them encode a sample of past frames again at every decision and are trained on isolated decisions, so computation is redundant and the usable history is short. They also learn from their own mistakes through outcome rewards that give one scalar to a whole episode. We ask whether a navigator…

## 49. Self-WSP: Can Language Models Improve Themselves Through Weight-Space Programming?

- 分数：18.0  ·  HF 赞：12  ·  来源：huggingface
- 兴趣命中：language model, spec
- 作者：Guoming Ling, Shanshan Zhong, Kaixuan Zhang, Zhongzhan Huang
- 链接：[arXiv](https://arxiv.org/abs/2611.28833) · [PDF](https://arxiv.org/pdf/2611.28833) · [HF](https://huggingface.co/papers/2611.28833)

Frontier language models can now read and edit the weights of a neural network much like code and thereby improve a small model, an approach known as Weight-Space Programming (WSP). We further explore applying WSP to a language model itself, which we call Self-WSP. Specifically, Qwen3.5-0.8B reads its own weights, proposes an edit, and then continues with the edited weights as both problem solver and editor. We find…

## 50. MORSE: Optimizing Streaming Memory Design via Open-World Auto-Research

- 分数：18.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：memory, benchmark, language model, spec
- 作者：Ce Zhang, Jianshu Zhang, Jinxi He, Xiyuan Yang, Pan Wang, Han Liu, Katia Sycara, Yaqi Xie
- 链接：[arXiv](https://arxiv.org/abs/2611.30011) · [PDF](https://arxiv.org/pdf/2611.30011) · [HF](https://huggingface.co/papers/2611.30011)

A streaming video system must decide in a single pass what evidence to retain under bounded frame storage, before it knows which details a future question will require. Recent recursive self-improvement methods automate the design of the harness that stores and retrieves this evidence. They revise the harness in response to failures, but the editor must still devise each repair from its prior knowledge and a…

## 51. Can an Agent Trust Its Own Zoom? Cross-Magnification Provenance Verification for Whole-Slide Images

- 分数：17.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark, language model, retrieval
- 作者：Yan Wang, Yiran Song, Zizhuo Gong, Jianxiang Qi, Zhongxing Xu, Lingfei Qian, Minquan Lin
- 链接：[arXiv](https://arxiv.org/abs/2611.29150) · [PDF](https://arxiv.org/pdf/2611.29150) · [HF](https://huggingface.co/papers/2611.29150)

Visual agents navigate whole-slide images through magnified observations associated with claimed locations. However, a visually plausible observation does not necessarily originate from its claimed location, particularly across magnifications and in regions with similar tissue structures. We formulate cross-magnification provenance verification (CMPV) to evaluate whether visual evidence supports a claimed spatial…

## 52. KernelShift: Benchmarking Kernel Optimization Across Evolving Hardware

- 分数：17.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：agent, benchmark, coding, spec
- 作者：Shuaiwei Huang, Weihua Du, Allen Wu, Ivan Fox, Manupa Karunaratne, Yiming Yang, Sean Welleck
- 链接：[arXiv](https://arxiv.org/abs/2611.29590) · [PDF](https://arxiv.org/pdf/2611.29590) · [HF](https://huggingface.co/papers/2611.29590)

Efficient AI computation depends on hardware that evolves over time, shifting the strategies needed to implement performant code. For CPU kernels, a key evolving factor is the set of available architectural extensions, which expose specialized hardware instructions that change the techniques used to optimize kernels. We study how effectively coding agents use these new, potentially unfamiliar extensions to write…

## 53. From Rewarding What Models Say to How They Think: Attention Process Reward Model for LLM Reinforcement Learning

- 分数：17.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：reasoning, reinforcement learning, language model, large language
- 作者：Kairong Han, Nuanqiao Shan, Ziyu Zhao, Xinpeng Dong, Zijing Hu, Dian Jin, Leyan Deng, Junjian Ye, Lujia Pan, Fei Wu, Kun Kuang
- 链接：[arXiv](https://arxiv.org/abs/2611.30627) · [PDF](https://arxiv.org/pdf/2611.30627) · [HF](https://huggingface.co/papers/2611.30627)

Reinforcement learning (RL) has become an important component in large language models (LLMs). However, existing RL approaches focus on final outputs or textual solution trajectories, leading to coarse-grained rewards and unreliable reasoning. Such paradigms focus mainly on what the model outputs while overlooking how the model internally reasons. Therefore, can we reward how a model thinks internally rather than…

## 54. Coding4Games: Can Modern Coding Agents Play Modern Video Games?

- 分数：17.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark, language model, coding, spec
- 作者：Shifang Zhao, Haoyu Wang, Yuyang Yin, Dong Chen, Xingyilang Yin, Yunkang Tao, Honghao Chen, Guangzhi Wang, Yiran Wang, Junfu Pu, Cheng Cheng, Xiaodong Cun, Ying Shan
- 链接：[arXiv](https://arxiv.org/abs/2611.31974) · [PDF](https://arxiv.org/pdf/2611.31974) · [HF](https://huggingface.co/papers/2611.31974)

Games, especially modern AAA games, challenge language models to perceive complex scenes, control actions, and make decisions over long horizons. Existing game benchmarks primarily test language models as computer-use agents that query a language model throughout play, incurring repeated inference cost and, in real-time games, acting while the environment continues to evolve. We ask whether coding agents can learn…

## 55. WeightCode: Installing New Capabilities into Neural Networks via Weight-Space Programming

- 分数：17.0  ·  HF 赞：14  ·  来源：huggingface
- 兴趣命中：language model
- 作者：Bo Li, Taoyong Cui, Bob Zhang, Mengran Li, Chengyang Zhang, Yang Zhang, Pheng Ann Heng, Wanli Ouyang, Zhenfei Yin, Yingcheng Wu, Ling Yang
- 链接：[arXiv](https://arxiv.org/abs/2611.25476) · [PDF](https://arxiv.org/pdf/2611.25476) · [HF](https://huggingface.co/papers/2611.25476)

Neural networks encode learned capabilities in their weights, yet extending those capabilities with explicit task knowledge remains a fundamental challenge. Here we show that Weight-Space Programming (WSP), in which executable programs read, construct or modify a network's weights directly, can install new capabilities within trained neural networks. WeightCode, a WSP framework, uses a frozen language model to write…

## 56. Unlocking the Power of Loops in Pretrained LLMs with Loop Residuals

- 分数：17.0  ·  HF 赞：14  ·  来源：huggingface
- 兴趣命中：benchmark
- 作者：Xuanlei Zhao, Hailun Xu, Kai Wang, Yang Luo, Yingxuan Ren, Zirui Zhu, Yuxuan Lou, Kun Xu, Yan Wang, Kanchan Sarkar, Yang You
- 链接：[arXiv](https://arxiv.org/abs/2611.31094) · [PDF](https://arxiv.org/pdf/2611.31094) · [HF](https://huggingface.co/papers/2611.31094)

Looped Transformers iterate a shared block of layers to increase computation without adding parameters, offering stronger performance and test-time scaling. However, this power has so far required training from scratch and yielded only modest gains for LLMs. Finetuning existing models into loops is far cheaper, yet also brings only marginal gains over SFT. We propose LoopRes, an effective, scalable, and simple…

## 57. DexDuet: Learning Contact-Preserving Bimanual Dexterity from Human Demonstrations

- 分数：17.0  ·  HF 赞：14  ·  来源：huggingface
- 兴趣命中：benchmark
- 作者：Haoran Zhang, Haokai Ding, Han Zhou, Zuxing Lu, Heng Zhang, Xingxing Zuo
- 链接：[arXiv](https://arxiv.org/abs/2611.30495) · [PDF](https://arxiv.org/pdf/2611.30495) · [HF](https://huggingface.co/papers/2611.30495)

Human demonstrations provide a rich source of bimanual dexterous skills, yet transferring them to robot hands remains challenging. Existing methods primarily optimize object trajectory tracking, often overlooking how human hands interact with the object. Even with accurate tracking, robots may contact incorrect object parts or slide their fingers, resulting in unstable manipulation. We present DexDuet, a framework…

## 58. VenusOCR2.0: Towards Efficient and Effective Document Parsing

- 分数：17.0  ·  HF 赞：6  ·  来源：huggingface + arxiv
- 兴趣命中：coding
- 作者：Lei Li, Zheng Wei, Yi Yuan, Qingbin Liu, Jiang Bian, Zang Li
- 链接：[arXiv](https://arxiv.org/abs/2611.32617) · [PDF](https://arxiv.org/pdf/2611.32617) · [HF](https://huggingface.co/papers/2611.32617)

We present VenusOCR2.0, a compact 1B-parameter vision-language recognizer designed for both high-accuracy and high-throughput document parsing across text, tables, and formulas. To continuously improve recognition quality without self-training collapse, we build a bounded recursive self-improvement (RSI) data engine where the model acts strictly as a weakness probe, while external multi-expert medoid consensus, VLM…

## 59. Residual Guidance for Real-Time Interactive Video Generation

- 分数：17.0  ·  HF 赞：6  ·  来源：huggingface + arxiv
- 兴趣命中：spec
- 作者：NaHyeon Park, Kyeong-Hwan Moon, Youjin Jeon, Hyunjung Shim
- 链接：[arXiv](https://arxiv.org/abs/2611.32820) · [PDF](https://arxiv.org/pdf/2611.32820) · [HF](https://huggingface.co/papers/2611.32820)

Real-time interactive video generation allows users to change the prompt during generation to steer the evolving video. However, existing streaming models, which generate videos chunk by chunk, often keep following the previous prompt after a switch. We trace this failure to context inertia, where the previous chunk acts as a strong prior that suppresses the new prompt. Furthermore, we find that this inertia…

## 60. Clinical3D-Bench: Evaluating and Improving Spatial Intelligence of Multimodal LLMs in Hospital Environments

- 分数：17.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：memory, reasoning, benchmark, language model, large language
- 作者：Yang Bai, Yingzhi Xia, Ling Lin, Jun Cheng, Lin Fu, Huazhu Fu
- 链接：[arXiv](https://arxiv.org/abs/2611.32094) · [PDF](https://arxiv.org/pdf/2611.32094) · [HF](https://huggingface.co/papers/2611.32094)

Spatial reasoning in hospitals requires tracking look-alike equipment, interpreting patient-relative directions, and judging passage widths, yet existing benchmarks provide limited coverage of these abilities. We introduce Clinical3D-Bench, a simulated benchmark with 3,368 questions of eight types on egocentric walkthroughs of 373 hospital-room layouts. Layouts follow hospital design guidelines, answers are computed…

## 61. Reinforcing Diffusion Models by Instantaneous Trajectory Distribution Matching

- 分数：16.5  ·  HF 赞：9  ·  来源：huggingface
- 兴趣命中：reinforcement learning, benchmark
- 作者：Yihong Luo
- 链接：[arXiv](https://arxiv.org/abs/2611.30986) · [PDF](https://arxiv.org/pdf/2611.30986) · [HF](https://huggingface.co/papers/2611.30986)

Forward diffusion reinforcement learning (RL)---enabling deterministic ODE sampling without trajectory backpropagation---has grown increasingly popular for efficiently aligning diffusion models. However, we reveal that existing methods essentially rely on signed reward-weighted regression (RWR), regressing the trainable policy velocity onto rollouts from a behavior distribution. Unbiased baseline subtraction…

## 62. EvoViM: Recursively Self-Evolving Visual Agents for Exploration with Deferred Queries

- 分数：16.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：agent, memory, language model, large language
- 作者：Xinyu Cao, Tianjie Ju, Zhuosheng Zhang
- 链接：[arXiv](https://arxiv.org/abs/2611.28574) · [PDF](https://arxiv.org/pdf/2611.28574) · [HF](https://huggingface.co/papers/2611.28574)

Multimodal large language model (MLLM) agents have shown promising capabilities in task-oriented environments. However, they still struggle when queries are deferred until after exploration, requiring them to retain visual evidence before knowing which details will matter. We introduce EvoViM, a recursively self-evolving framework in which a frozen multimodal model turns its own interaction experience into one…

## 63. ReFocus: Progress-Guided Adaptive Practice for Long-Horizon Robotic Manipulation Reinforcement Learning

- 分数：16.5  ·  HF 赞：1  ·  来源：huggingface + arxiv
- 兴趣命中：reinforcement learning, spec
- 作者：Haoyuan Li, Wei Huang, Jiehong Lin, Shengrong Zhang, Chenzhi Liu, Shengchao Zhou, Hehe Fan, Xiaojuan Qi, Yi Yang
- 链接：[arXiv](https://arxiv.org/abs/2611.32639) · [PDF](https://arxiv.org/pdf/2611.32639) · [HF](https://huggingface.co/papers/2611.32639)

Online reinforcement learning (RL) enables vision-language-action policies to improve through environmental interaction. However, in long-horizon manipulation, sparse success/failure feedback provides little information about where policies encounter bottlenecks. Moreover, repeated full-task rollouts also leave these bottlenecks weakly analyzed and insufficiently practiced. To this end, we introduce ReFocus, a…

## 64. LeadVLA: Learning Follower-Aware Route Execution for Robot Leading

- 分数：16.0  ·  HF 赞：12  ·  来源：huggingface
- 兴趣命中：benchmark
- 作者：Tianle Zeng, Hanjing Ye, Bingyi Xia, Yuchen Zhou, Zibo Zhang, Yufei Huang, Yonggen Ling, Hong Zhang
- 链接：[arXiv](https://arxiv.org/abs/2611.30149) · [PDF](https://arxiv.org/pdf/2611.30149) · [HF](https://huggingface.co/papers/2611.30149)

Robot leading requires executing a route while continuously adapting to a designated follower. Existing robot-leading systems often mediate follower understanding and physical route execution through explicit states, planners, or modular interfaces; directly learning this coupling through end-to-end trajectory prediction can instead entangle route execution with follower response. We introduce LeadVLA, a structured…

## 65. Can Latent Reasoning Drive LLM Outputs Without a Trace?

- 分数：16.0  ·  HF 赞：12  ·  来源：huggingface
- 兴趣命中：reasoning
- 作者：Tomer Ashuach, Zorik Gekhman, Avi Caciularu, Ori Ram, Jonathan Herzig
- 链接：[arXiv](https://arxiv.org/abs/2611.31015) · [PDF](https://arxiv.org/pdf/2611.31015) · [HF](https://huggingface.co/papers/2611.31015)

LLMs typically solve complex tasks with chain-of-thought (CoT) reasoning, which is also the main tool for monitoring them for misaligned behavior. However, standard transformers can also solve tasks with complete latent reasoning (CLR), carrying out the whole task internally and outputting only the final answer. Theory bounds the depth of CLR, the number of sequential steps it can carry out, and recent work measured…

## 66. A Pipeline-Parallel System for Depth-Recurrent Models

- 分数：16.0  ·  HF 赞：8  ·  来源：huggingface
- 兴趣命中：memory, spec
- 作者：Yunjia Xi, Jiarui Qin, Di Yin, Xing Sun
- 链接：[arXiv](https://arxiv.org/abs/2611.30581) · [PDF](https://arxiv.org/pdf/2611.30581) · [HF](https://huggingface.co/papers/2611.30581)

Depth-recurrent (Looped) models raise effective depth by applying a shared stack of blocks several times. Scaling them usually requires pipeline parallelism, but commonly used interleaved 1F1B is drawn for an acyclic stage graph in which each micro-batch enters each stage once. Once that stack is split across stages, the same stage is visited several times on one micro-batch and later stages feed earlier ones:…

## 67. AdProducer: Towards Agentic Advertising Video Generation

- 分数：16.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：agent, reinforcement learning, evaluation
- 作者：Kunyang Li, Chaoyang Wang, Mubarak Shah, Yuzhang Shang
- 链接：[arXiv](https://arxiv.org/abs/2611.31466) · [PDF](https://arxiv.org/pdf/2611.31466) · [HF](https://huggingface.co/papers/2611.31466)

Recent advances in video generation have made automated advertising production increasingly feasible. However, an effective advertisement must faithfully represent the product and communicate its selling points through compelling visual storytelling, which requires more than visual synthesis: it calls for deeper product understanding and strategic decisions about how to present product value. Crucially, product…

## 68. Single-Transformer Latent Diffusion

- 分数：15.5  ·  HF 赞：15  ·  来源：huggingface
- 兴趣命中：-
- 作者：Hao-Yu Hsu, Shenlong Wang, Alexander G. Schwing
- 链接：[arXiv](https://arxiv.org/abs/2611.29064) · [PDF](https://arxiv.org/pdf/2611.29064) · [HF](https://huggingface.co/papers/2611.29064)

Latent generative models typically rely on three separate networks: an encoder that tokenizes pixels, a generator that models the latent distribution, and a decoder that maps latents back to pixels. UNITE recently merged the first two into a single generative encoder trained in one stage, but its decoder remains a separate network. We ask whether this last network can be folded in too, so that one diffusion…

## 69. Measuring and Teaching Language Model Agents to Act on Delayed Consequences

- 分数：15.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：agent, evaluation, language model
- 作者：Shardul Bansal, Seth Schilbe, Jarrod Barnes
- 链接：[arXiv](https://arxiv.org/abs/2611.28158) · [PDF](https://arxiv.org/pdf/2611.28158) · [HF](https://huggingface.co/papers/2611.28158)

Language model agents are increasingly asked to run ongoing multi-day operations rather than finish isolated single-turn tasks. In daily operations, today's choices reshape later observations and cash constraints because empty shelves hide lost walk-in demand, short-shipped customers quietly shrink future orders weeks later, and emergency buying drains working capital. We introduce SMB Bench, a calibrated 90-day…

## 70. ReWeave: Emergent Physical Task Topologies for Embodied Harness Optimization and Cross-Task Meta-Distillation

- 分数：15.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：agent, reasoning, spec
- 作者：Yicheng Xu, Wencan Jiang, Zihao Zhu, Keru Zhou, Chang Zhou, Li Liu, Maoqing Yao, Yong Liu, Jiangning Zhang
- 链接：[arXiv](https://arxiv.org/abs/2611.31053) · [PDF](https://arxiv.org/pdf/2611.31053) · [HF](https://huggingface.co/papers/2611.31053)

Long-horizon embodied tasks involve physical dependencies that may only become clear through interaction. As task understanding deepens, past trials can reveal new information for adaptation and transfer. However, coarse progress feedback cannot identify which physical preconditions held, leaving search unguided, while task-specific optimization easily overfits to individual scenes, making cross-task transfer…

## 71. ApexID: Hierarchical Learning for Multi-Species Animal Re-Identification

- 分数：15.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：evaluation, spec, retrieval
- 作者：Seifeldin Elkerdany, Mohamed ElBassat, Gamal Abouelhamd, Assem Elkady, Jana Ghoneim, Matin Mahmood, Abigail Allen Martin, Gerard de Melo, Antonio Rueda-Toicen
- 链接：[arXiv](https://arxiv.org/abs/2611.29723) · [PDF](https://arxiv.org/pdf/2611.29723) · [HF](https://huggingface.co/papers/2611.29723)

Animal re-identification (Re-ID) must distinguish individuals across species and capture conditions. We introduce ApexID, a hierarchical SphereFace2-based loss that integrates global identity discrimination with balanced animal-category supervision. Using 132,533 images curated from 19 public datasets, we evaluate three model families and four objectives on four external datasets with observation-aware retrieval…

## 72. Self-Supervised Dataset Distillation via Mutual Information Maximization

- 分数：15.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：evaluation, benchmark, spec
- 作者：Mohammad Hossein Moslemi, Mahdi Beitollahi, Zhimin Mei, Jiale Cai, Bissan Ghaddar, Boyu Wang
- 链接：[arXiv](https://arxiv.org/abs/2611.31225) · [PDF](https://arxiv.org/pdf/2611.31225) · [HF](https://huggingface.co/papers/2611.31225)

Dataset distillation (DD) aims to compress a large dataset into a small synthetic one that remains effective for training neural networks. Despite its success in supervised learning, DD remains underexplored in self-supervised learning (SSL), where distilled data must preserve the information needed to learn representations that remain consistent across augmentations. To bridge this gap, we introduce Mutual…

## 73. RoomTokens: Masked Diffusion over Structured Tokens for Indoor Scene Synthesis

- 分数：14.5  ·  HF 赞：9  ·  来源：huggingface
- 兴趣命中：spec
- 作者：Xiaohao Sun, Angel X. Chang
- 链接：[arXiv](https://arxiv.org/abs/2611.30219) · [PDF](https://arxiv.org/pdf/2611.30219) · [HF](https://huggingface.co/papers/2611.30219)

Generating 3D indoor scenes requires a representation that captures object semantics, instance identity, height structure, and orientation while respecting room geometry. Methods that model scenes as sequences of object vectors learn spatial constraints implicitly, leaving collisions and boundary violations to losses or post-processing; semantic-map methods make occupancy explicit, but collapse instance and…

## 74. Let Vision-Language Models Generate Images through Their Representations

- 分数：14.5  ·  HF 赞：9  ·  来源：huggingface
- 兴趣命中：language model
- 作者：JB Kim, Byungwoo Jeon, Kyungmin Lee, Hyeonmo Kang, Cheonbok Park, Shinyoung Joo, Jinwoo Shin, Jeonghoon Kim
- 链接：[arXiv](https://arxiv.org/abs/2611.31237) · [PDF](https://arxiv.org/pdf/2611.31237) · [HF](https://huggingface.co/papers/2611.31237)

Recent unified multimodal models aim to combine visual understanding and generation within a single model, yet effectively integrating the two capabilities remains challenging. Leveraging pretrained vision-language models offers a way to build on already learned multimodal knowledge, but making this knowledge effectively accessible to visual generation remains nontrivial. We find that a central challenge lies in the…

## 75. LLMs Memorize Their Own Hallucinations During Post-Training

- 分数：14.5  ·  HF 赞：5  ·  来源：huggingface
- 兴趣命中：reasoning, reinforcement learning
- 作者：Anirudh Atmakuru, Tanya Goyal
- 链接：[arXiv](https://arxiv.org/abs/2611.26863) · [PDF](https://arxiv.org/pdf/2611.26863) · [HF](https://huggingface.co/papers/2611.26863)

Reasoning domains have shaped the post-training recipes of frontier models even though they are trained and deployed in domains beyond math and code. In this paper, we study the consequences of directly adopting reasoning-centric training recipes, e.g., the use of outcome-based rewards for reinforcement learning (RL), injection of "cognitive" behaviors such as proposing and backtracking from hypotheses in reasoning…

## 76. HEP-Ex-Bench: Evaluating Agentic Performance in High Energy Physics Experiment Data Analyses with Sealed Worlds

- 分数：14.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark
- 作者：Andrzej Novák, Yiyang Zhao, Dolores Garcia, Eric A. Moreno, Jeffrey Krupa, Víctor Bresó-Pla, Samuel Bright-Thonney, Lukas Heinrich, Michael Kagan, Philip Harris
- 链接：[arXiv](https://arxiv.org/abs/2611.28194) · [PDF](https://arxiv.org/pdf/2611.28194) · [HF](https://huggingface.co/papers/2611.28194)

Agentic systems are increasingly being explored for automating experimental high-energy physics measurements, but the correctness of their results can today be reliably evaluated only via extensive expert review. To address this, we propose a method to perform detailed quantitative evaluations of agent-driven analyses through the use of blind analysis and injection tests, which are critical in a typical expert…

## 77. LUCID: Statistically Grounded Self-Correction for LLM Reasoning Evaluation

- 分数：14.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：reasoning, evaluation, benchmark
- 作者：Satiyabooshan Murugaboopathy, Adel Daoud, Connor T. Jerzak
- 链接：[arXiv](https://arxiv.org/abs/2611.31595) · [PDF](https://arxiv.org/pdf/2611.31595) · [HF](https://huggingface.co/papers/2611.31595)

Cheap language-model raters grade chain-of-thought reasoning at scale, yet systematic step-rating errors can skew reasoning audits and solution rankings. We introduce LUCID (Loop for Unbiased Calibration via Inference-time Diagnosis), which pairs prompt self-correction with Design-based Supervised Learning (DSL). Without retraining or weight access, LUCID calibrates binary step ratings by aligning predicted and…

## 78. EEGJev: A System One Decision Model and Benchmark for Multi-Task EEG Question Answering

- 分数：14.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：benchmark, coding, spec
- 作者：Dengzhe Hou, Kazunori D. Yamada
- 链接：[arXiv](https://arxiv.org/abs/2611.32100) · [PDF](https://arxiv.org/pdf/2611.32100) · [HF](https://huggingface.co/papers/2611.32100)

A single electroencephalographic (EEG) recording can support multiple decoding tasks. Fixed-label tests cannot show how EEG foundation models handle changing questions or options. We introduce EEGJev, a fast decision model that scores candidate answers in one pass. Our benchmark, EEGJev-Bench, covers six question types across 19 public EEG sources. We held the recording and options fixed while switching between…

## 79. On-Policy Codec Distillation for Efficient All-in-One Video Generation

- 分数：14.0  ·  HF 赞：8  ·  来源：huggingface
- 兴趣命中：memory
- 作者：Boyang Wang, Kevin Blackburn-Matzen, Oindrila Saha, Matheus Gadelha, Zezhou Cheng
- 链接：[arXiv](https://arxiv.org/abs/2611.31184) · [PDF](https://arxiv.org/pdf/2611.31184) · [HF](https://huggingface.co/papers/2611.31184)

Modern visual generative models operate on tokens, and every visual asset they receive, whether an identity, a scribble, a depth map, or a motion video, is tokenized and appended to the input token sequence. Consequently, conditioning quickly dominates the computation cost. Yet most of these tokens carry redundant spatiotemporal information. Our key insight is that identifying what is genuinely new is exactly the…

## 80. LoopedWAM: Looped World Action Models for Elastic Inference

- 分数：14.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：memory, benchmark
- 作者：Anh Dao, Xinxin Liu, Hang Yu, Jeffrey A Chan Santiago, Yuzhang Shang
- 链接：[arXiv](https://arxiv.org/abs/2611.25595) · [PDF](https://arxiv.org/pdf/2611.25595) · [HF](https://huggingface.co/papers/2611.25595)

World action models (WAMs) couple generative video modeling with robotic action prediction but typically require large video and action transformers, limiting deployment efficiency. We present LoopedWAM, a compact WAM that recurrently applies a shared six-block core in each expert, executing 30 transformer layers while storing only 12 blocks per expert. To account for their asymmetric inference costs, the video and…

## 81. Fast-JEPA: Advancing the Success-Latency Frontier for Latent World Models

- 分数：14.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：benchmark, planning
- 作者：Yao Zhang, Bin Yu, Shijie Lian, Haishan Liu, Changti Wu, Yu Wu, Kai Chen
- 链接：[arXiv](https://arxiv.org/abs/2611.25927) · [PDF](https://arxiv.org/pdf/2611.25927) · [HF](https://huggingface.co/papers/2611.25927)

Latent world models predict the outcomes of action sequences, but comparing candidate plans through recursive rollout remains expensive at test time. We introduce Fast-JEPA, a latent world model planning framework that advances the success-latency Pareto frontier of predictive search. Fast-JEPA reorganizes predictive computation to support effective action-sequence search at low planning cost. It constructs a…

## 82. Feedback Shortcut: Speculative Decoding for Latent Feedback Transformers

- 分数：14.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：coding, spec
- 作者：Benhao Huang, Xuezhe Ma, Hector Liu
- 链接：[arXiv](https://arxiv.org/abs/2611.28227) · [PDF](https://arxiv.org/pdf/2611.28227) · [HF](https://huggingface.co/papers/2611.28227)

Feeding each position's top-layer hidden state back into the next position's input improves Transformer performance. However, this feedback breaks speculative decoding, since verifying a drafted token requires the top-layer state from its preceding position, which forces the draft to rely on an approximate stand-in. Training the model to adapt to this stand-in can lower the exact-decoding performance ceiling, while…

## 83. NoHairCache: Calibrate-Once KV Cache Eviction with One Power-Law Exponent

- 分数：13.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：coding, spec
- 作者：Shuyang Xiang
- 链接：[arXiv](https://arxiv.org/abs/2611.29006) · [PDF](https://arxiv.org/pdf/2611.29006) · [HF](https://huggingface.co/papers/2611.29006)

The decay exponent α in KV-cache eviction is an intrinsic property of the model: calibrated once on a single corpus, it transfers directly across domains. Attention-based accumulation (H2O) and recency-based sliding windows (StreamingLLM) are two dominant eviction frameworks, often treated as unrelated, but we show that they are the two endpoints of a single power-law family: by scoring each token as s_i = A_i cdot…

## 84. HIVE-Bench: Evaluating Patch-Level Visual Representations for Egocentric Robot Manipulation

- 分数：13.0  ·  HF 赞：10  ·  来源：huggingface
- 兴趣命中：-
- 作者：Qiwei Liang, Zhengtu Liang, Minghao Lai, Yikeng Chen, Yiming Wang, Boyang Cai, Yuetong Fang, Taowen Wang, Baiqiao Yin, Tianxing Chen, Yue Chen, Jiaming Liang, Guangyu Chen, Shaolong Zhu, Daolin Ma, Renjing Xu
- 链接：[arXiv](https://arxiv.org/abs/2611.30813) · [PDF](https://arxiv.org/pdf/2611.30813) · [HF](https://huggingface.co/papers/2611.30813)

Pretrained vision is a common start for robot learning, but most comparisons still score one pooled vector from a third-person image. Bimanual policies instead read dense patch tokens from cameras on the robot. We introduce HIVE-Bench: one shared flow-matching policy reads 20 encoders from seven families on 24 egocentric bimanual tasks, across adaptation, task sharing, and sweeps of data, model size, and layer.…

## 85. MomentMem: Memorizing Key Moments for Robot Manipulation

- 分数：13.0  ·  HF 赞：6  ·  来源：huggingface
- 兴趣命中：memory
- 作者：Guangyu Zhao, Yongchang Zhang, Ruizhang Jiang, Zhihong Yu, Yuhao Zhang, Tao Wu, Qimin Zhou, Kunsong Shi, Haoran Wen, Zeyu Zhang, Yin Li, Kun Zhan, Yiwu Zhong
- 链接：[arXiv](https://arxiv.org/abs/2611.26745) · [PDF](https://arxiv.org/pdf/2611.26745) · [HF](https://huggingface.co/papers/2611.26745)

Robotic manipulation often requires remembering visual information that is no longer observable, such as the original location of an object. Existing approaches typically rely on full observation histories, which become redundant over long horizons, or text summaries, which may omit precise visual details. We study visual moment memory, the ability to retain such details from key moments for subsequent manipulation.…

## 86. LoopDVR: Looped Transformer for Efficient Dense Visual Recognition

- 分数：13.0  ·  HF 赞：6  ·  来源：huggingface
- 兴趣命中：spec
- 作者：Sirui Liang, Xuanlong Yu, Longfei Liu, Xiaodong Cun, Xi Shen
- 链接：[arXiv](https://arxiv.org/abs/2611.32067) · [PDF](https://arxiv.org/pdf/2611.32067) · [HF](https://huggingface.co/papers/2611.32067)

We propose LoopDVR, a framework for converting pretrained Transformer-based dense visual recognition models into parameter-efficient looped networks. Rather than reducing the network width or depth directly, LoopDVR reuses Transformer blocks across layers in both the ViT backbone and Transformer decoder, reducing the number of parameters while retaining the original computational structure. However, naively sharing…

## 87. Prism: Hierarchical Text Detection with Minimalist Design

- 分数：13.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：benchmark, spec
- 作者：Yuchen Su, Xuesheng Wang, Zhilong Ji, Jinfeng Bai, Shijian Lu, Zhineng Chen
- 链接：[arXiv](https://arxiv.org/abs/2611.26254) · [PDF](https://arxiv.org/pdf/2611.26254) · [HF](https://huggingface.co/papers/2611.26254)

Hierarchical text detection aims to localize words, text lines, and paragraphs while parsing their structural relationships. It provides essential structural cues for visual text understanding. To maximize accuracy, existing methods typically rely on complex multi-scale feature fusion necks and heavy-weight heads, resulting in bloated architectures and low inference efficiency. In this paper, we argue that a…

## 88. Seeing Right, Writing Wrong: Where Short Chain-of-Thought Breaks Spatial VQA

- 分数：13.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：reasoning, language model
- 作者：Chenhao Zhang
- 链接：[arXiv](https://arxiv.org/abs/2611.28665) · [PDF](https://arxiv.org/pdf/2611.28665) · [HF](https://huggingface.co/papers/2611.28665)

Asking a vision-language model (VLM) to think step by step often makes it worse at spatial questions, even though the image stays in context. We show that short chain-of-thought (CoT) turns a perception problem into a transcription problem. Once a VLM writes a spatial relation, its answer follows that sentence instead of the image, so whether CoT helps or hurts depends largely on whether the written relation is more…

## 89. Context-Grounded Skill Internalization for Vision-Language Agents

- 分数：13.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：agent, reinforcement learning
- 作者：Jinlin Liu, Yumeng He, Qihan Huang, Kevin Qinghong Lin, Han Peng
- 链接：[arXiv](https://arxiv.org/abs/2611.30075) · [PDF](https://arxiv.org/pdf/2611.30075) · [HF](https://huggingface.co/papers/2611.30075)

Skill internalization offers a way for agents to learn useful behaviors from skills and use them without explicit guidance in context at inference time. A common approach is to generate demonstration trajectories with the skill in context and then fine-tune the same model on its own trajectories with the skill removed. However, this leads to the problem that the model may learn to reference the removed skill, which…

## 90. Typhoon OCR 2: From Thai Document Transcription to Multilingual, Multi-Task OCR

- 分数：13.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：evaluation, spec
- 作者：Surapon Nonesung, Natapong Nitarach, Sittipong Sripaisarnmongkol, Kunat Pipatanakul, Warit Sirichotedumrong
- 链接：[arXiv](https://arxiv.org/abs/2611.27494) · [PDF](https://arxiv.org/pdf/2611.27494) · [HF](https://huggingface.co/papers/2611.27494)

Typhoon OCR 1.5 focused on reading Thai documents. However, in real-world workflows, users often need to extract specific information or preserve the structure of an entire page for further processing. Typhoon OCR 2 handles both tasks in a single model, with prompt-driven extraction and structured full-page parsing. Full-page parsing covers Thai, English, and Chinese. We release compact 2B and 0.8B models adapted…

## 91. PINE: Point, Instance and Normal Estimation in One-Step Diffusion Model

- 分数：12.5  ·  HF 赞：5  ·  来源：huggingface
- 兴趣命中：coding
- 作者：Zeyu Ren, Jie Ni, Rui Qian, Jiahao Wei, Hao Tang, Yongtai Liu, Zeyu Zhang
- 链接：[arXiv](https://arxiv.org/abs/2611.29389) · [PDF](https://arxiv.org/pdf/2611.29389) · [HF](https://huggingface.co/papers/2611.29389)

Understanding a scene requires both geometry and semantics: geometry recovers its spatial structure, and semantics separates it into objects. Current models obtain the two from separate networks or separate passes. We present PINE, a one-step Omni Diffusion Transformer that predicts the point map, the surface normals, and the instance map of an image in one forward pass. PINE treats each map as a token stream, and a…

## 92. Distill the Correction, Not the Rewrite: Hindsight Twins for Self-Improving Text-to-Image Models

- 分数：12.5  ·  HF 赞：5  ·  来源：huggingface
- 兴趣命中：spec
- 作者：Jiaze Li, Jingyang Chen, Wenhao Zhao, Haoran Xu, Zhenlong Yuan, Dianmo Sheng, Yuanxing Zhang
- 链接：[arXiv](https://arxiv.org/abs/2611.31048) · [PDF](https://arxiv.org/pdf/2611.31048) · [HF](https://huggingface.co/papers/2611.31048)

Text-to-image models can learn from their own mistakes by distilling a self-teacher conditioned on a vision-language critic's revised prompt. However, such self-teachers barely improve alignment, and both they and their hindsight-contrast variants absorb the critic's unintended additions to the scene, such as lighting or scenery. We attribute this to two factors: (1) the prompt already specifies the desired fix, so…

## 93. Escriba-OCR: A 1B Vision-Language Model for Error-Preserving Transcription of Handwritten Portuguese Essays

- 分数：12.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：benchmark, language model
- 作者：Tardelli Ronan Coelho Stekel
- 链接：[arXiv](https://arxiv.org/abs/2611.29874) · [PDF](https://arxiv.org/pdf/2611.29874) · [HF](https://huggingface.co/papers/2611.29874)

Feedback tools and research on learner writing need transcriptions of handwritten essays that keep exactly what the student wrote: misspellings, line breaks, struck-through words and insertions. Vision-language models (VLMs) read handwriting well, but they also tend to rewrite it into correct language. We measure this on BRESSAY, 1,000 handwritten Brazilian Portuguese essays, with a benchmark that adds error…

## 94. Frontier models need only one text to unmask its human or AI author

- 分数：12.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：reasoning, spec
- 作者：Atrey Desai, Deniz Bölöni-Turgut, Ty Brassington, Minjoon Choi, Jenna Russell, Rishanth Rajendhran, Bradley Emi, Hila Gonen, Hal Daumé III, John Wieting, Marzena Karpinska, Mohit Iyyer
- 链接：[arXiv](https://arxiv.org/abs/2611.26216) · [PDF](https://arxiv.org/pdf/2611.26216) · [HF](https://huggingface.co/papers/2611.26216)

Given a single text and a simple zero-shot prompt (no web access, tools, candidate lists, or writing samples), frontier models can answer "who wrote this?" at three increasingly specific levels: (1) whether an AI or human wrote it, (2) if an AI, which lab, and (3) if a human, often exactly who. The latest models (Claude Fable 5.2, GPT-6.1 Sol, Gemini 4 Carbon) match trained detectors like Pangram while also…

## 95. Lyris: Layout-Guided Long Video Generation with Persistent 3D Memory

- 分数：12.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：memory, language model
- 作者：Chen Wang, Jiahui Huang, Riccardo de Lutio, Alex Trevithick, Bryan Chu, Jiawei Ren, Laura Leal-Taixé, Shengyu Huang, Lingjie Liu, Haithem Turki
- 链接：[arXiv](https://arxiv.org/abs/2611.31239) · [PDF](https://arxiv.org/pdf/2611.31239) · [HF](https://huggingface.co/papers/2611.31239)

Exploring a scene from as little as a single photo requires generating a long, camera-controlled walkthrough that extends far beyond what was captured, yet remains consistent upon return. Memory-based video generation methods preserve what they have already seen, but have no anchor beyond it, where the camera drifts from its path and a text prompt can name objects but not place them. Layout-conditioned methods…

## 96. SWEEP-Bench: Do Embodied Policies Act on the Speed They See?

- 分数：12.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：evaluation, benchmark
- 作者：Hiroaki Honda, Koya Sakamoto, Shu Morikuni, Yusuke Iwasawa, Taiki Miyanishi
- 链接：[arXiv](https://arxiv.org/abs/2611.30637) · [PDF](https://arxiv.org/pdf/2611.30637) · [HF](https://huggingface.co/papers/2611.30637)

Robot policies must adapt to the speed of moving objects, yet existing benchmarks rarely measure this ability across diverse tasks and speeds. We introduce SWEEP-Bench, a simulation benchmark with 80 conveyor-belt manipulation tasks spanning 16 skill categories, each evaluated at 13 belt speeds (0.10-0.40 m/s). Objects are transported through physical contact with a visibly moving belt. Each task has a static…

## 97. Factorized Context Attention: From Emulated to Native Grid Probing

- 分数：12.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：context window, language model
- 作者：Mohamed Eltahir, Manar Eyad, Yara Alzahrani, Fatimah Albesher, Duaa M. Tahir, Tanveer Hussain, Naeemullah Khan
- 链接：[arXiv](https://arxiv.org/abs/2611.32423) · [PDF](https://arxiv.org/pdf/2611.32423) · [HF](https://huggingface.co/papers/2611.32423)

Models read a book, an hour of video, or an image in one forward pass. As the context grows, this pass slows down, loses accuracy, and stops at the context window. Sparse attention is efficient, but keeps the other two limitations. Grid probing, a recent training-free method, recovers the accuracy and extends the reach by asking a frozen model the same question about short local and strided spans of the input, but…

## 98. RoMo Hands: A Large Scale Richly Organized Text to Hand Motion Dataset

- 分数：12.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：benchmark, spec
- 作者：Yizhak Ben-Shabat, Jiahao Zhang, Joseph Liu, Seonghyeon Moon, Young-Yoon Lee, Haomiao Jiang, Oren Jacob, Mubbasir Kapadia
- 链接：[arXiv](https://arxiv.org/abs/2611.31766) · [PDF](https://arxiv.org/pdf/2611.31766) · [HF](https://huggingface.co/papers/2611.31766)

While text-driven body motion generation has matured, pure-hand synthesis remains bottlenecked by data. Existing datasets often treat hands as rigid end-effectors, lack fine-grained captions, or are too limited in scale to support robust generalization. We introduce RoMo Hands, an in-the-wild, text-paired dataset of ~542K sequences (884 hours, 95.5M frames at 30 fps) which is an order of magnitude larger than prior…

## 99. Wactorz: Self-Writing LLM Agents That Discover, Repair, and Migrate at the Edge

- 分数：12.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：agent
- 作者：Panagiotis Kasnesis, Lazaros Toumanidis, Amalia Contiero Syropoulou, Christos Chatzigeorgiou
- 链接：[arXiv](https://arxiv.org/abs/2611.29619) · [PDF](https://arxiv.org/pdf/2611.29619) · [HF](https://huggingface.co/papers/2611.29619)

Most LLM agent frameworks build a crew that runs a task and exits. Physical environments (e.g., homes, labs, factory floors) need agents that stay up for months, survive their own bugs, and run on whatever hardware is already next to the sensors. We present Wactorz, an open-source runtime in which LLM-generated agents are long-lived, supervised actors: a planner turns a chat request into Python, compiles it into a…

## 100. UniVEP: Unifying Velocity and Endpoint Prediction for Robot Manipulation

- 分数：12.0  ·  HF 赞：0  ·  来源：huggingface
- 兴趣命中：benchmark, spec
- 作者：Zhengtu Liang, Qiwei Liang, Tao Lin, Shihang Weng, Boyang Cai, Xiangyu Chen, Yikeng Chen, Jiaming Liang, Bohan Tan, Yu Yan, Renjing Xu
- 链接：[arXiv](https://arxiv.org/abs/2611.26103) · [PDF](https://arxiv.org/pdf/2611.26103) · [HF](https://huggingface.co/papers/2611.26103)

Flow-matching robot policies usually use one prediction target throughout action generation, even though recovering actions from noise and polishing nearly clean actions bring different challenges. We systematically compare velocity prediction (V), endpoint prediction (X), and velocity-weighted endpoint prediction (X--V) across multiple robot policies, benchmarks, and inference budgets. On StarVLA and LiLa-WAM, X--V…

## 101. How Complete Must an Environment Be to Train a Capable GUI Agent?

- 分数：11.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：agent
- 作者：Jingxing Wang, Teng Wang, Xingyu Lou, Zihan Guo, Jun Wang, Weiwen Liu, Weinan Zhang, Jianghao Lin
- 链接：[arXiv](https://arxiv.org/abs/2611.23946) · [PDF](https://arxiv.org/pdf/2611.23946) · [HF](https://huggingface.co/papers/2611.23946)

Graphical user interface (GUI) agents are widely trained in executable GUI environments. To lower cost, build environments in batches, and reduce manual effort, each work trades away part of the environment through its construction choices. We describe these choices along three dimensions: reward coverage, the goal-reaching trajectories the verifier rewards; data coverage, the application data the agent is exposed…

## 102. Interpretable Prototype-Conditioned Adaptation for Weather Forecasting

- 分数：11.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：spec
- 作者：Zhixuan Li, Hao Jiang, Chen Hui, Kai Geng, Weisi Lin
- 链接：[arXiv](https://arxiv.org/abs/2611.25848) · [PDF](https://arxiv.org/pdf/2611.25848) · [HF](https://huggingface.co/papers/2611.25848)

Data-driven weather forecasting requires distinguishing local states and their temporal evolution. However, learned patterns remain implicit in neural forecasters, making their influence difficult to interpret. Failing to distinguish local evolution can lead to similar forecasts for locations that develop differently, increasing prediction error. This motivates explicit references for distinguishing and interpreting…

## 103. Deterministic, Reproducible Inference in Exact Integer Arithmetic, and Verifiable Distributed Inference as Its Consequence

- 分数：11.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：language model
- 作者：Sayed Amir Karim
- 链接：[arXiv](https://arxiv.org/abs/2611.13730) · [PDF](https://arxiv.org/pdf/2611.13730) · [HF](https://huggingface.co/papers/2611.13730)

Optimized floating-point inference is not reproducible across environments: the same model on different hardware, compilers or thread counts can produce different bits. We present tritify, an open-source runtime that executes the forward pass of real models -- decoder-only language models, Mixture-of-Experts decoders, and the Segment Anything 2.1 image/video stack -- with the entire run-time path in exact integer…

## 104. Beyond Attention Maps: Understanding and Improving Medical MLLMs via Visual Values

- 分数：11.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：benchmark
- 作者：Yichen Zhao, Fenghe Tang, Wenxin Ma, Rongsheng Wang, Zihao Wan, Shaohua Kevin Zhou
- 链接：[arXiv](https://arxiv.org/abs/2611.29361) · [PDF](https://arxiv.org/pdf/2611.29361) · [HF](https://huggingface.co/papers/2611.29361)

Current MLLM methods largely focus on whether models attend to the right visual regions, implicitly treating spatial attention map as the primary key of effective visual perception. To examine this assumption, we introduce a medical VQA dataset with paired non-contrast (NC) and contrast-enhanced (CE) images that share corresponding anatomy while providing different cues. We show that this view is incomplete: across…

## 105. PixelOne: From Options to Pixels in a Single Forward for GUI Grounding

- 分数：11.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：benchmark
- 作者：Kanghui Tian, Shuai Dong, Yuhan Zhu, Congcong Wang, Ji Zhao, Tianxiang Jiang, Zhixiong Zhang, Shengyuan Ding, Yi Wang, Jiaqi Wang, Yu Qiao
- 链接：[arXiv](https://arxiv.org/abs/2611.30235) · [PDF](https://arxiv.org/pdf/2611.30235) · [HF](https://huggingface.co/papers/2611.30235)

GUI grounding requires precise clicks at low latency. Recent models such as GUI-Decisions and GUI-Swift predict coordinates in one forward pass using fixed global bins with local refinement. However, screenshot downsampling removes detail needed to locate small controls, while fixed bins cover larger pixel ranges at higher resolutions. We introduce PixelOne, which transfers spatial knowledge from a search teacher to…

## 106. WeaveVLA: 3D Relational Grounding for Vision-Language-Action Models

- 分数：11.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：spec
- 作者：Zien Wang, Yuhao Pan, Yunfeng Fan, Nan Cheng, Xin Xia, Wenchao Xu
- 链接：[arXiv](https://arxiv.org/abs/2611.31126) · [PDF](https://arxiv.org/pdf/2611.31126) · [HF](https://huggingface.co/papers/2611.31126)

Vision-language-action (VLA) models leverage pretrained vision-language representations for instruction-conditioned robot control, yet their understanding of task-relevant 3D relations and how these relations evolve during manipulation remains largely implicit. To address this challenge, we introduce WeaveVLA, a framework that enhances VLA action generation by explicitly modeling task-relevant relative 3D relations…

## 107. Write, Evolve, Read: Streaming Cameras into a Persistent World State for 4D Occupancy Forecasting

- 分数：10.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：-
- 作者：ZiAn Wang, Tianyi Wang, Zhihao Chen, Manni Cui, Junkai Chen, ZhiJin Chen, Ruiqi Liu, Junfei Wu, Huanyu Zhang, Shu Wu
- 链接：[arXiv](https://arxiv.org/abs/2611.30573) · [PDF](https://arxiv.org/pdf/2611.30573) · [HF](https://huggingface.co/papers/2611.30573)

4D occupancy forecasting predicts the 3D semantic occupancy of a driving scene seconds ahead. Over a few seconds, the scene changes little while the vehicle moves, so most of the space ahead has already been seen. Sorting the future into unchanged, changed, and unseen space, we find that current camera-based world models fall short on the unchanged part: they fail to hold on to what they have already seen, rather…

## 108. Do learned image captioning metrics generalize? Auditing duplicated samples in human-judgment benchmarks

- 分数：10.0  ·  HF 赞：0  ·  来源：huggingface
- 兴趣命中：benchmark
- 作者：Xiaochen Zhang, Jin Li, Chunlong Xia, Longjiang Guo
- 链接：[arXiv](https://arxiv.org/abs/2611.30488) · [PDF](https://arxiv.org/pdf/2611.30488) · [HF](https://huggingface.co/papers/2611.30488)

Learned image captioning metrics are trained and tested on human judgments, so their reported correlation is a claim about generalization. We audit this claim for the three most recent collections of such judgments, Polaris, Nebula, and Spica, matching images at the pixel level. First, test samples reappear in training sets: the Spica training set contains about two-thirds of the Polaris test set, with identical…

## 109. Align the Pair, Not the Sample: Representation Alignment for Faster and Better One-Step Generato

- 分数：9.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：-
- 作者：Mingxiao Li, Xuantuo Huang, Encheng Su, Aoran Wang, Han Zhang, Jinouwen Zhang, Shixiang Tang
- 链接：[arXiv](https://arxiv.org/abs/2611.29547) · [PDF](https://arxiv.org/pdf/2611.29547) · [HF](https://huggingface.co/papers/2611.29547)

Representation alignment markedly accelerates diffusion training, but one-step generators raise a question that diffusion does not: which training path should receive the loss? A one-step generator sees two kinds of inputs. Corrupted real images come with their clean counterpart, which provides an instance-paired target. Samples generated from pure noise have no corresponding real image, yet this is where the final…

## 110. RecurSciBench: Benchmarking Recursive Self-Improvement in Data-Driven Scientific Research

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, benchmark, language model, large language
- 作者：Wenxi Xu, Chuan Qin, Zihan Wang, Zixing Chen, Le Zhang, Jingbo Zhou, Hao Wang, Yuanchun Zhou, Hengshu Zhu
- 链接：[arXiv](https://arxiv.org/abs/2611.32508) · [PDF](https://arxiv.org/pdf/2611.32508) · [HF](https://huggingface.co/papers/2611.32508)

Large language model (LLM)-based agents are advancing the automation of data-driven scientific research. Recent advances in recursive self-improvement (RSI) offer the potential for these agents to continuously improve through experience, but evaluating transfer across scientific tasks requires executable, scientifically verifiable tasks and independent assessment of self-improvement gains. We introduce…

## 111. GeoVLDrive: Geometry-Grounded Vision-Language Reasoning for Autonomous Driving

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reasoning, language model, planning
- 作者：JiaHui Huang, Songyan Zhang, Hanbing Li, Hanchao Leng, Kuiyuan Yang, Guang Chen, Hangjun Ye, Chen Lv
- 链接：[arXiv](https://arxiv.org/abs/2611.32510) · [PDF](https://arxiv.org/pdf/2611.32510) · [HF](https://huggingface.co/papers/2611.32510)

Vision-language-action (VLA) planners inherit semantic knowledge from pretrained vision-language models, but their reasoning is rarely grounded in 3D scene structure and its evolution over time. We introduce GeoVLDrive, a geometry-grounded VLA framework for 3D spatiotemporal reasoning and planning. Multi-layer features from a 3D foundation model augment the vision-language backbone through gated cross-attention. A…

## 112. Avalon-M1: Reinforcement Learning from Collective Rewards

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reinforcement learning, evaluation, benchmark, language model, spec
- 作者：Iliyan Zarov, Henry Course, Anthony Hartshorn, Ran Achiron, Louis Roche, Akshit Sinha, Chengxi Taylor, Ross Taylor
- 链接：[arXiv](https://arxiv.org/abs/2611.32539) · [PDF](https://arxiv.org/pdf/2611.32539) · [HF](https://huggingface.co/papers/2611.32539)

We introduce reinforcement learning from collective rewards (RLCR), a recipe for jointly training language models to act as agent organisations under latency constraints. A CEO and up to eight specialists share one policy, co-ordinate through a message board and workspace, and are trained with a common outcome-derived advantage. The deadline makes parallel work valuable when it increases the return earned before the…

## 113. HiCal: Offline Calibration for Hierarchical Scale Encoding in Accurate HiF4 Quantization

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, language model, large language, coding, spec
- 作者：Zhiyuan Zhang, Yanzhao Li, Hui Dong, Sifan Cheng, Mingen Zheng, Hui Wang
- 链接：[arXiv](https://arxiv.org/abs/2611.32624) · [PDF](https://arxiv.org/pdf/2611.32624) · [HF](https://huggingface.co/papers/2611.32624)

Block floating-point (BFP) quantization is widely adopted for efficient low-bit large language model (LLM) inference, where the choice of block scales plays a critical role in quantization accuracy. HiFloat4 (HiF4) employs a hierarchical scale encoding scheme consisting of a global E6M2 scale and two levels of binary scale extensions. However, its conventional rounding rule and fixed scale extension thresholds may…

## 114. ICLWorld: Benchmarking In-Context Learning of Agents from Digital to Physical Worlds

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, evaluation, benchmark, spec
- 作者：Qingle Liu, Jieming Li, Pei-lin Li, Shenghan Zheng, Ruize Yang, Sunqi Fan, Deyao Hong, Huan-ang Gao, Meng-Hao Guo, Shuojin Yang
- 链接：[arXiv](https://arxiv.org/abs/2611.32649) · [PDF](https://arxiv.org/pdf/2611.32649) · [HF](https://huggingface.co/papers/2611.32649)

In-context learning (ICL) lets agents acquire new rules from context and adapt to user-specific requirements at inference time. The same frontier agents now operate both computers and robots, yet their ICL remains insufficiently assessed: existing benchmarks are largely offline, rely on text or static images, and risk training-data contamination, while robot evaluations are limited to method-level ablations. We…

## 115. Bathys: Advancing Deep Search Agents

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, tool use, reinforcement learning, evaluation, spec, retrieval
- 作者：Zixuan Chen, Shengyou Yuan, Nang Yuan, Ming Ma, Zelin Xiao, Lin Zhou, Siyuan Luo, Jiaqi Su, Chengrui Wu, Tiankuo Yao, Nairong Zheng, Cong Pang, Jiapeng Luo
- 链接：[arXiv](https://arxiv.org/abs/2611.32660) · [PDF](https://arxiv.org/pdf/2611.32660) · [HF](https://huggingface.co/papers/2611.32660)

Deep search is a critical capability for agents tackling complex, open-ended tasks, where solving a problem requires iterative information gathering, query reformulation, and evidence-based verification rather than a single retrieval step. To address these requirements, we present Bathys 9B and 27B deep search agents built around a training framework that spans verifiable question synthesis, post-training, and…

## 116. Economic World Model

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, evaluation, benchmark, planning
- 作者：Qirui Mi, Yujia Ming, Bo Li, Haifeng Zhang
- 链接：[arXiv](https://arxiv.org/abs/2611.32663) · [PDF](https://arxiv.org/pdf/2611.32663) · [HF](https://huggingface.co/papers/2611.32663)

Can artificial intelligence reproduce the economic dynamics that emerge as households, firms and governments interact and adapt through markets and institutions? To answer this question, we define an economic world model (EWM) as an agent's internal representation of how an economic system works, enabling counterfactual simulation and decision-making under resource constraints. We then propose a general framework…

## 117. CAPTA: Identifying LLMs Behind AI Agents

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, evaluation, language model, large language, spec
- 作者：Kailun Yan, Yue Huang, Sisi Duan
- 链接：[arXiv](https://arxiv.org/abs/2611.32686) · [PDF](https://arxiv.org/pdf/2611.32686) · [HF](https://huggingface.co/papers/2611.32686)

Large language model (LLM)-based agents access remote services through tools to complete user tasks, often via API calls. In this setting, a remote service may want to identify the backend LLM of an agent to launch model-specific attacks, including prompt injection or selective delivery of manipulated content. However, the service cannot directly query the backend model and must instead collect observable responses…

## 118. Are We Rewarding the Wrong Module? Module-Specific Policy Optimization for Multimodal Reinforcement Learning

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, reinforcement learning, benchmark, language model, large language, spec
- 作者：HuiSeong Cho, Jun Yeong Park, Yu Rang Park
- 链接：[arXiv](https://arxiv.org/abs/2611.32687) · [PDF](https://arxiv.org/pdf/2611.32687) · [HF](https://huggingface.co/papers/2611.32687)

Reinforcement learning with verifiable rewards (RLVR) based on Group Relative Policy Optimization (GRPO) has been widely adopted to enhance the multimodal reasoning of multimodal large language models (MLLMs). However, existing methods share a common limitation of Module-Level Credit Entanglement, in which the vision encoder, projector, and LLM modules are jointly optimized using the same advantage signals even when…

## 119. Red-Teaming a Sovereign LLM, Its Reasoning and Its Training Stages

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, evaluation, language model, large language, spec
- 作者：Hatef Otroshi Shahreza
- 链接：[arXiv](https://arxiv.org/abs/2611.32710) · [PDF](https://arxiv.org/pdf/2611.32710) · [HF](https://huggingface.co/papers/2611.32710)

Open-weight large language models (LLMs) are increasingly deployed for applications with sensitive information. We investigate whether confidentiality instructions in system prompt can protect such information. We red-team Apertus v1.5, an open sovereign LLM, and five other model families across six languages and reasoning modes. We use synthetic personal records to evaluate direct disclosure, correction baits,…

## 120. ASCENT: A Benchmark for Evaluating and Advancing Stepwise Diagnostic Reasoning in Large Language Models on Common Clinical Scenarios

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, evaluation, benchmark, language model, large language
- 作者：Yera Choi, Yeong Hwa Kim, Jaedeok Lee, Taekang Kim, Sangdoo Yun, Seong-Eun Moon
- 链接：[arXiv](https://arxiv.org/abs/2611.32734) · [PDF](https://arxiv.org/pdf/2611.32734) · [HF](https://huggingface.co/papers/2611.32734)

Large language models (LLMs) excel at medical question answering yet are rarely evaluated on the stepwise diagnostic reasoning that defines real clinical workflows, where impressions are revised as information accumulates. We build Annotated Stepwise Clinical rEasoning for NaturalisTic Diagnosis (ASCENT), a clinician-annotated benchmark and training resource of 3,078 stepwise problems derived from MedQA-USMLE that…
