# 每日 AI 论文

生成时间：2026-10-13 06:47 UTC  ·  共 73 篇（已按 arXiv ID 去重）

来源：Hugging Face Daily Papers + arXiv（cs.AI / cs.LG / cs.CL / cs.CV）。
排序：HF 上榜、点赞、多源命中、兴趣词。兴趣词可在 `config.json` 改。

## 1. SoftwareGym: Scaling Computer-Use Agent Training with Diverse Synthesized Software Environments

- 分数：36.0  ·  HF 赞：85  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark, spec
- 作者：Tian Jin, Wenhao Wang, Jing Kang, Haoting Shi, Rui Ye, Yijun Lu, Siheng Chen
- 链接：[arXiv](https://arxiv.org/abs/2610.12611) · [PDF](https://arxiv.org/pdf/2610.12611) · [HF](https://huggingface.co/papers/2610.12611)

Computer-use agents (CUAs) are rapidly improving, yet synthesizing diverse and reliable software environments at scale remains challenging. Native application environments require substantial construction and integration effort, which limits application coverage and increases the risk of application-specific overfitting. Browser-hosted environments provide limited interaction depth and workflow complexity. These…

## 2. Scaling Agentic Data for Long-Horizon Terminal Intelligence

- 分数：36.0  ·  HF 赞：63  ·  来源：huggingface
- 兴趣命中：agent, reasoning, benchmark, coding
- 作者：Shun Zou, Ziyu Ma, Yi Zou, Yong Wang, Lin Chen, Zehui Chen, Guanhua Chen, Xiangxiang Chu, Feng Zhao
- 链接：[arXiv](https://arxiv.org/abs/2610.13166) · [PDF](https://arxiv.org/pdf/2610.13166) · [HF](https://huggingface.co/papers/2610.13166)

Terminal agents are moving beyond local operations toward completing real-world professional tasks. Short trajectories can demonstrate commands and tool calls, but they do not fully show how agents accumulate evidence through exploration, use it to inform judgments, continually adjust strategies based on feedback, and turn intermediate results into final deliverables. High-quality long-horizon trajectories capture…

## 3. VisionWeave: Weaving Elastic Visual Representations as a Native Capability of MLLMs

- 分数：36.0  ·  HF 赞：57  ·  来源：huggingface
- 兴趣命中：evaluation, benchmark, language model, large language, coding
- 作者：Yuan Feng, Qize Yang, Ruizhe Chen, Sibo Song, Haolin He, Muzhi Zhu, Zihan Liu, Yunfei Chu, Xize Cheng, Yuxuan Wang, Jin Xu, Xike Xie
- 链接：[arXiv](https://arxiv.org/abs/2610.07987) · [PDF](https://arxiv.org/pdf/2610.07987) · [HF](https://huggingface.co/papers/2610.07987)

Multimodal large language models have become the dominant paradigm for visual understanding, but incur substantial costs by encoding inputs into dense, fixed-size patch tokens. However, visual information is unevenly distributed: some regions require fine-grained detail, while others admit compact representations. Downsampling sacrifices this detail, while existing token pruning and adaptive approaches remain…

## 4. S-Space: Exploring Spatial Workspace in Multimodal Language Models

- 分数：34.0  ·  HF 赞：264  ·  来源：huggingface
- 兴趣命中：reasoning, language model, spec
- 作者：Zhiyuan Shi, Xiang Li, Xingzhuo Guo, Shangchen Miao, Weiliang Chen, Qiyu Dai, Jinshan Ren, Jiangran Lyu, Fangfu Liu, Mingsheng Long, Jialong Wu
- 链接：[arXiv](https://arxiv.org/abs/2610.13527) · [PDF](https://arxiv.org/pdf/2610.13527) · [HF](https://huggingface.co/papers/2610.13527)

Multimodal language models (MLLMs) exhibit promising spatial reasoning capabilities, yet the internal mechanisms supporting them remain poorly understood. We uncover S-Space, a linear representation subspace in which object-token representations encode continuous coordinates along horizontal, vertical, and distance axes. Although we identify these axes by differentiating spatial-answer scores with respect to…

## 5. EmbodiedCLBench: Evaluating Continual Learning for Self-Evolving Embodied Agents

- 分数：34.0  ·  HF 赞：63  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark
- 作者：Jie Huang, Yanan Chen, Ruixun Liu, Kaichen He, Xinyi He, Rui Huang, Zilong Zheng, Zhenliang Zhang, Yiwu Zhong
- 链接：[arXiv](https://arxiv.org/abs/2610.13021) · [PDF](https://arxiv.org/pdf/2610.13021) · [HF](https://huggingface.co/papers/2610.13021)

Continual learning requires models to accumulate past experience and transfer it to new tasks. Despite substantial research on continual learning, existing work remains largely confined to non-embodied settings, without extending to embodied environments. To address this gap, we introduce EmbodiedCLBench, the first benchmark in embodied simulation for evaluating the continual learning capability of self-evolving…

## 6. GroundingPI: A Grounding Foundation Model towards Physical Intelligence with Visual Primitives

- 分数：34.0  ·  HF 赞：51  ·  来源：huggingface
- 兴趣命中：reinforcement learning, benchmark, spec
- 作者：Qize Yu, Lianrui Fan, Boyu Chen, Jiaqi Liang, Xini Ding, Yue Chen, Zetian Song, Yuran Wang, Yi Zou, Kaixuan Wang, Tianxing Chen, Wenxuan Song, Bohan Zhou, Mingleyang Li, Siqiao Huang, Yuqi Ye, Caigao Jiang, Wei Wei, Ruihai Wu, Hang Zhang, Yixiao Ge, Shuchang Zhou, Shilong Liu, Xianming Liu, Ping Luo, Shiyu Huang
- 链接：[arXiv](https://arxiv.org/abs/2609.39601) · [PDF](https://arxiv.org/pdf/2609.39601) · [HF](https://huggingface.co/papers/2609.39601)

Precise grounding matters. It specifies which object is the target and where that object is, even in clutter and for tiny objects, and it has to be fast enough for closed-loop control. Yet vision-language-action (VLA) and world-action models (WAMs) take perception from general-purpose vision-language and video-generation backbones, which still fail in these settings. We introduce GroundingPI, a 4B grounding…

## 7. ProgramGym: Scaling Training Environments for Long-Horizon Program Reproduction Agents

- 分数：34.0  ·  HF 赞：49  ·  来源：huggingface
- 兴趣命中：agent, coding, spec
- 作者：Chengyi Yang, Renxu Bao, Jue Hou, Zongpei Teng, Ziheng Wang, Yujie Lin, Chengsong Huang, Junnan Zhu, Delai Qiu, Yining Wang, Shengping Liu, Fei Long, Jinsong Su
- 链接：[arXiv](https://arxiv.org/abs/2610.13395) · [PDF](https://arxiv.org/pdf/2610.13395) · [HF](https://huggingface.co/papers/2610.13395)

Coding agents are increasingly used to build programs from scratch as software engineers do rather than to resolve issues within a repository or to generate a repository from a given requirements document. However, scalable verifiable training environments that force agents to discover what is required and to decide how the system should be designed remain scarce. Moreover, existing agent workflows also cannot…

## 8. Work2Skill: Capturing Human GUI Experience for Reusable Agent Skill Induction

- 分数：34.0  ·  HF 赞：40  ·  来源：huggingface
- 兴趣命中：agent, evaluation, spec
- 作者：Yuqi Huang, Hui Li, Yifei Cao, Zikun Cai, Tianci Xie, Yangfan Gao, Pinxue Guo, Chaoyun Zhang, Bingxuan Li, Rui Zheng, Hang Yan, Ning Liao
- 链接：[arXiv](https://arxiv.org/abs/2610.12984) · [PDF](https://arxiv.org/pdf/2610.12984) · [HF](https://huggingface.co/papers/2610.12984)

Computer-use agents can perform increasingly complex GUI tasks, yet unfamiliar software and workflows requiring human domain knowledge remain challenging. Human demonstrations convey procedural knowledge through the same GUI interaction space, but reuse requires interpreting actions in context and separating workflow rules from task-specific details. We thus introduce Work2Skill, a framework that captures human GUI…

## 9. SoloQ: Calibration-Free Quantization for Diffusion Language Models

- 分数：32.5  ·  HF 赞：33  ·  来源：huggingface
- 兴趣命中：memory, reasoning, benchmark, language model, large language
- 作者：Donghyun Lee, Arkapravo Ghosh, Varun Manjunath, Bumjoon Kyle Rhee, Hyunho Kook, Shiting Xiao, Youngeun Kim, Priyadarshini Panda
- 链接：[arXiv](https://arxiv.org/abs/2610.07121) · [PDF](https://arxiv.org/pdf/2610.07121) · [HF](https://huggingface.co/papers/2610.07121)

Diffusion large language models dLLMs) have emerged as a promising alternative to autoregressive language models through bidirectional diffusion-based token generation. However, their growing model sizes and high inference costs make efficient deployment challenging: full-sequence denoising repeatedly invokes compute-intensive forward passes, while block-diffusion models additionally introduce a memory-intensive…

## 10. Can AI Agents Learn Their Way to the Top? Evaluating Heuristic Learning in a Long-Running Game Agent Competition

- 分数：32.5  ·  HF 赞：33  ·  来源：huggingface
- 兴趣命中：agent, reinforcement learning, evaluation, benchmark, spec
- 作者：Kaisen Yang, Qingle Liu, Kejin Wang, Yicheng Zhao, Jieming Li, Shenghan Zheng, Ruize Yang, Bojun Yang, Heng Gong, Xiang Gao, Lanyue Zhang, Kaiyu Zhong, Zhuo Liu, Shaoxuan Li, Chengxi Li, Yong Yan, Weixuan Zhang, Tianwei Luo, Situ Wang, Youjie Zheng, Sihan Zhao, Shengyuan Wang, Huan-ang Gao, Jiazheng Xu, Xiaohui Xie, Wentao Han, Hongning Wang
- 链接：[arXiv](https://arxiv.org/abs/2610.12341) · [PDF](https://arxiv.org/pdf/2610.12341) · [HF](https://huggingface.co/papers/2610.12341)

Adversarial games have driven advances from heuristic search to reinforcement learning, yet learning and adapting strategies from limited samples remain challenging. AI agents offer an alternative by turning game experience into revisions of executable policies. Building on heuristic learning (HL), we formalize Adversarial Heuristic Learning (AHL), a paradigm that uses AI agents as learning engines to refine game…

## 11. DiffusionART: Efficient, Stable and Scalable Reinforcement of Diffusion Models

- 分数：32.0  ·  HF 赞：234  ·  来源：huggingface
- 兴趣命中：reinforcement learning, spec
- 作者：Zhenglin Wan, Jiayu Chen, Zhengfeiyang Zhang, Pengfei Zhou, Wangbo Zhao, Fangyuan Kong, Pengfei Wan, Kun Gai, Yang You
- 链接：[arXiv](https://arxiv.org/abs/2610.12572) · [PDF](https://arxiv.org/pdf/2610.12572) · [HF](https://huggingface.co/papers/2610.12572)

Online reinforcement learning (RL) fine-tunes diffusion models with black-box rewards, but reverse-process methods such as Flow-GRPO are limited in efficiency by poor credit assignment, while forward-process methods such as DiffusionNFT are efficient yet unstable without carefully tuned exponential-moving-average (EMA) off-policy training. We show that NFT-style objectives contain a hidden forward--reverse…

## 12. Continually Post-training Small Models via Synthetic Self-distillation

- 分数：32.0  ·  HF 赞：41  ·  来源：huggingface
- 兴趣命中：evaluation, benchmark
- 作者：Woosung Koh, Hyunsoo Lee, Kyungjae Lee, Haeju Park, Dahyun Lee, Dasol Hwang, Moontae Lee
- 链接：[arXiv](https://arxiv.org/abs/2610.13113) · [PDF](https://arxiv.org/pdf/2610.13113) · [HF](https://huggingface.co/papers/2610.13113)

Continual post-training faces a dual challenge of acquisition and retention: models must learn new capabilities while preserving prior knowledge. While Self-Distillation Fine-Tuning (SDFT) mitigates this using self-supervision with in-context demonstrations, it relies on strong in-context learning and instruction-following abilities. Consequently, SDFT fails on smaller models critical for low-latency, on-device use.…

## 13. Reflex: Visually Grounded Reactive Humanoid Control

- 分数：30.0  ·  HF 赞：134  ·  来源：huggingface
- 兴趣命中：reinforcement learning
- 作者：Taoyang Jia, Weikai Huang, Linxin Song, Jared Darlington, Jieyu Zhao, Yue Wang, Jiafei Duan, Zhongzheng Ren, Ranjay Krishna
- 链接：[arXiv](https://arxiv.org/abs/2610.12772) · [PDF](https://arxiv.org/pdf/2610.12772) · [HF](https://huggingface.co/papers/2610.12772)

Humans effortlessly react to the world; they adeptly return a tennis shot, catch a falling cup, step aside from a passing cart, or pass a box tossed during truck unloading. These everyday actions require anticipating a moving target and reflexively responding with the whole body within about a second. Such visual reactive whole-body control remains challenging for humanoids, which must (1) coordinate whole-body…

## 14. Hear the World in Stereo: Learning Dynamic Spatial Correspondence for Immersive Joint Video-Audio Generation

- 分数：30.0  ·  HF 赞：52  ·  来源：huggingface
- 兴趣命中：evaluation
- 作者：Hanmo Chen, Chengcheng Liu, Tianxiao Chen, Zheyu Zhang, Siming Zheng, Jinwei Chen, Xu Yang, Cheng Deng, Bo Li, Peng-tao Jiang
- 链接：[arXiv](https://arxiv.org/abs/2609.38748) · [PDF](https://arxiv.org/pdf/2609.38748) · [HF](https://huggingface.co/papers/2609.38748)

Recent joint video-audio generation models have achieved strong semantic correspondence and temporal synchronization. However, applications such as AR/VR and interactive gaming further require stereo audio to provide an immersive sense, which remains largely overlooked. Effective stereo audio requires the perceived sound location to evolve consistently with the motion of its corresponding visual source. We refer to…

## 15. SepGen: Multi-Stem Audio-Video Separation and Generation in a Single Model

- 分数：29.5  ·  HF 赞：39  ·  来源：huggingface
- 兴趣命中：spec
- 作者：Aviad Dahan, Rajaei Khatib, Yonatan Bitton, Idan Szpektor, Lior Wolf, Raja Giryes
- 链接：[arXiv](https://arxiv.org/abs/2610.11361) · [PDF](https://arxiv.org/pdf/2610.11361) · [HF](https://huggingface.co/papers/2610.11361)

A 4D audio-visual scene comprises a video, the dynamic geometry it depicts, and the sound sources that populate it, each with its own position and trajectory. Rendering such a scene from a novel viewpoint requires that every source be available as an individual waveform, so that it can be localized in the scene and propagated to the observer before the signals are mixed. Joint audio-video generators can synthesize…

## 16. RSI-Anything: Unlocking Recursive Self-Improvement with World Models

- 分数：28.0  ·  HF 赞：32  ·  来源：huggingface
- 兴趣命中：evaluation, planning
- 作者：Taoyong Cui, Pinxian Zeng, Wanghan Xu, Hao Xiao, Shuhan Xue, Qiang Gao, Wanli Ouyang, Pheng Ann Heng, Zhenfei Yin, Yingcheng Wu, Ling Yang
- 链接：[arXiv](https://arxiv.org/abs/2610.13912) · [PDF](https://arxiv.org/pdf/2610.13912) · [HF](https://huggingface.co/papers/2610.13912)

Recursive self-improvement (RSI) aims to transform interaction experience into persistent improvements, yet external feedback is costly and world-model predictions may become unreliable as policies evolve. We introduce RSI-Anything, a domain-general framework built on JEPA-Anything that uses predictive world models to guide action and learning-data selection. Observed feedback drives policy or workflow improvement…

## 17. AgentSWE: Can Coding Agents Build the Agent You Actually Want?

- 分数：28.0  ·  HF 赞：28  ·  来源：huggingface
- 兴趣命中：agent, benchmark, coding
- 作者：Jiahao Wang, Hongjin Qian, Yuyang Hu, Jiajun Zhang, Zheng Liu
- 链接：[arXiv](https://arxiv.org/abs/2610.13361) · [PDF](https://arxiv.org/pdf/2610.13361) · [HF](https://huggingface.co/papers/2610.13361)

As the production of software passes into the hands of software itself, coding agents are increasingly commissioned to build agents fitted to their users' own workflows. This delegation carries a quiet assumption, that the delivered agent will faithfully serve the requirement it was built for, rather than merely appear to. No existing benchmark tests that assumption. We introduce AgentSWE, a benchmark for agent…

## 18. PolyOCR-Venus: Unified OCR Foundation Models for Text-Centric Visual Intelligence

- 分数：27.5  ·  HF 赞：31  ·  来源：huggingface
- 兴趣命中：reasoning, benchmark
- 作者：GuangJian Team, Kaili Huang, Yongshuo Zhang, Bingtao Fu, Changjiang Jiang, Chenfan Qu, Chenfeng Zhang, Fangming Cui, Gaoyang Zhang, Jiangwei Xie, Jianshu Li, Jing Huang, Jingwen Bai, Mingqi Fang, Tao Fang, Weihong Zhang, Wenbo Du, Xiongfei Bai, Xuekang Zhu, Yinan Xia, Zhenming Wang, Jian Liu, Jingjing Liu, Xiang Qi, Weiqiang Wang
- 链接：[arXiv](https://arxiv.org/abs/2609.37712) · [PDF](https://arxiv.org/pdf/2609.37712) · [HF](https://huggingface.co/papers/2609.37712)

Optical Character Recognition (OCR) is evolving from plain-text transcription toward general visual intelligence, requiring models to recognize, localize, and reason over textual information in complex visual environments. However, existing OCR systems often excel at only some tasks and struggle to balance recognition, parsing, and reasoning across scenarios. In this report, we present PolyOCR, a family of unified…

## 19. Multi-Stream Attention Residuals

- 分数：27.0  ·  HF 赞：30  ·  来源：huggingface
- 兴趣命中：benchmark, retrieval
- 作者：Xiaohan Qin, Xiangdong Zhang, Tuo Dai, Sunan Zou, Huaijin Wu, Yebin Yang, Zhuo Xia, Lin Yao, Yuliang Liu, Junchi Yan
- 链接：[arXiv](https://arxiv.org/abs/2610.13630) · [PDF](https://arxiv.org/pdf/2610.13630) · [HF](https://huggingface.co/papers/2610.13630)

Attention Residuals (AttnRes) enables content-dependent retrieval over network depth, which can be viewed as single-stream softmax attention along the depth axis. Inspired by the success of multi-head attention along the sequence axis, we introduce Multi-Stream Attention Residuals (MSAR), an extension of AttnRes that generalizes this mechanism to multi-head depth attention, yielding substantial performance gains…

## 20. Contextual Correction of Parallel Draftsfor Speculative Decoding

- 分数：26.5  ·  HF 赞：21  ·  来源：huggingface
- 兴趣命中：reasoning, benchmark, language model, large language, coding, spec
- 作者：Roy Eisenstadt, Harel Lidar, Tal Gonen, Omer Luxembourg, Itamar Zimerman, Lior Wolf, Eli David, Ilan Naiman
- 链接：[arXiv](https://arxiv.org/abs/2610.12570) · [PDF](https://arxiv.org/pdf/2610.12570) · [HF](https://huggingface.co/papers/2610.12570)

Speculative decoding accelerates large language model inference by using a lightweight drafter to propose multiple tokens that are subsequently verified in parallel by the target model. Recent diffusion-based drafters make this paradigm particularly attractive: deep attention-based neural backbones provide strong predictions, while drafting multiple future positions in parallel avoids the sequential cost of…

## 21. SWE-Duel: Towards a Self-Scaling Arena for Coding Agents

- 分数：26.0  ·  HF 赞：20  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark, coding
- 作者：Wei Minn, Zhensu Sun, Lwin Khin Shar, David Lo
- 链接：[arXiv](https://arxiv.org/abs/2610.12569) · [PDF](https://arxiv.org/pdf/2610.12569) · [HF](https://huggingface.co/papers/2610.12569)

Static coding benchmarks are fixed at release. Over time their tasks leak into training data, and stronger agents eventually saturate them. We argue that a benchmark should instead aim to be self-scaling: its tasks and oracles are created at evaluation time, so no content exists in advance to leak, and its difficulty is set by the participating agents rather than fixed at release. We introduce SWE-Duel, an arena in…

## 22. Stateless Language Agents: Scaling Long-Horizon Automated Research

- 分数：25.5  ·  HF 赞：19  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark, spec
- 作者：Qizheng Zhang, Changxiu Ji, Isaac Sun, Yuetai Li, Shubhangi Upasani, Sherry Ruan, Boyuan Ma, Fenglu Hong, Vamsidhar Kamanuru, Yoonho Lee, Yuzhen Mao, Genghan Zhang, Rulin Shao, Qiuyang Mang, Andy Dimnaku, Changran Hu, Radha Poovendran, Kunle Olukotun
- 链接：[arXiv](https://arxiv.org/abs/2610.07625) · [PDF](https://arxiv.org/pdf/2610.07625) · [HF](https://huggingface.co/papers/2610.07625)

Automated research systems increasingly run LLM agents over long horizons, but more inference does not by itself produce more progress: agents replay growing histories, duplicate one another's work, or stop experimenting while token consumption continues. Yet most evaluations use short budgets or benchmarks that saturate early, leaving these failure modes untested. We trace these failures to two choices: where…

## 23. Inducing Process Supervision from Outcome-Only Reinforcement Learning

- 分数：25.0  ·  HF 赞：18  ·  来源：huggingface
- 兴趣命中：agent, reasoning, reinforcement learning, benchmark
- 作者：Shengda Fan, Xin Cong, Zhong Zhang, Haotian Chen, Yankai Lin
- 链接：[arXiv](https://arxiv.org/abs/2609.36641) · [PDF](https://arxiv.org/pdf/2609.36641) · [HF](https://huggingface.co/papers/2609.36641)

Process reward models (PRMs) have become a key component for LLMs, as their step-level feedback supports both post-training and test-time reasoning. However, training strong PRMs remains costly: human step annotation is difficult to scale, while Monte Carlo estimation is computationally expensive and can drift from the intrinsic correctness of steps. To get effective PRMs at low cost, we introduce TIPS…

## 24. Recurrent Harness for Agentic Continual Learning

- 分数：25.0  ·  HF 赞：18  ·  来源：huggingface
- 兴趣命中：agent, memory, benchmark, language model, spec
- 作者：Yuxin Xiao, Zhiyun Lu, Jianyu Wang, Yangtian Zhang, Yang Song, Qifan Wang, Bailin Wang
- 链接：[arXiv](https://arxiv.org/abs/2610.12668) · [PDF](https://arxiv.org/pdf/2610.12668) · [HF](https://huggingface.co/papers/2610.12668)

Language model agents increasingly operate over long interaction streams, requiring online adaptation to distribution shifts through continual learning. However, existing agent harnesses typically either evolve their states only through forward information flow or rely on additional replay or validation data for harness optimization. To address this, we propose ReHarness, a recurrent harness framework for agentic…

## 25. Towards Physically Grounded Articulated 3D Assets: A Multi-Agent Pipeline and Benchmark

- 分数：25.0  ·  HF 赞：18  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark, spec
- 作者：Xudong Cai, Ruijie Zhu, Haoliang Shang, Ruining Li, Marc Pollefeys, Shangzhe Wu, Andrea Vedaldi, Chuanxia Zheng
- 链接：[arXiv](https://arxiv.org/abs/2610.13947) · [PDF](https://arxiv.org/pdf/2610.13947) · [HF](https://huggingface.co/papers/2610.13947)

In this paper, we study physically grounded articulated 3D asset generation---moving the goal from reproducing how objects look to capturing how they move and function. Inspired by the literature on procedural and agentic generation, we present Artisan, a system that extends the latest method Articraft by introducing a multi-agent pipeline with physical simulation feedback, enabling comprehensive attributes beyond…

## 26. SpatialASM: Internalizing Active Mentalization for Spatial Reasoning

- 分数：23.0  ·  HF 赞：14  ·  来源：huggingface
- 兴趣命中：reasoning, benchmark, language model, spec, planning
- 作者：Yuhong Liu, Shenxi Wu, Junyi Chi, Beichen Zhang, Xuanlang Dai, Jiaqi Wang, Yuhang Zang, Dahua Lin
- 链接：[arXiv](https://arxiv.org/abs/2610.13832) · [PDF](https://arxiv.org/pdf/2610.13832) · [HF](https://huggingface.co/papers/2610.13832)

When solving complex spatial reasoning tasks, ordinary humans naturally revisit the scenes from task-relevant viewpoints and mentally reconstruct the spatial layouts from those viewpoints. But can Large Vision-Language Models (LVLMs) proactively think in the same way? We term this ability Active Spatial Mentalization (ASM), an intrinsic component of visual intelligence that remains substantially underdeveloped in…

## 27. Surfing the Activation Wave: Analyzing the Information and Geometry of LLM Hidden States for Speculative Decoding

- 分数：22.5  ·  HF 赞：13  ·  来源：huggingface
- 兴趣命中：evaluation, language model, large language, coding, spec
- 作者：Raghavv Goel, Sudhanshu Agrawal, Mukul Gagrani, Risheek Garrepalli, Mingu Lee
- 链接：[arXiv](https://arxiv.org/abs/2610.12939) · [PDF](https://arxiv.org/pdf/2610.12939) · [HF](https://huggingface.co/papers/2610.12939)

Decoder hidden states from different layers of large language models (LLMs) often encode complementary information. However, existing speculative decoding methods typically rely on a small set of target-model layers chosen using fixed, position-based heuristics. Selecting an optimal subset of layers is inherently a combinatorial problem, making exhaustive evaluation infeasible even for moderately deep models. In…

## 28. MetaKernelBench: Measuring GPU Kernel Knowledge Transfer Beyond Code

- 分数：22.0  ·  HF 赞：16  ·  来源：huggingface
- 兴趣命中：agent, benchmark, spec
- 作者：Xueyi Chen, Shiyu Liu, Xin Jin, Yuhua Zheng, Xin Li, Haolei Bai, Junhan Zhu, Huan Wang
- 链接：[arXiv](https://arxiv.org/abs/2610.05014) · [PDF](https://arxiv.org/pdf/2610.05014) · [HF](https://huggingface.co/papers/2610.05014)

Recent GPU kernel optimization agents retain what they learn in knowledge bases or as distilled skills. Kernel benchmarks score each attempt's implementation for correctness and speed but leave the reuse value of retained experience unmeasured. We introduce MetaKernelBench, which measures whether experience distilled from an attempt in one kernel domain-specific language (DSL) improves a fresh attempt at the same…

## 29. Judging in Latent Space: Efficient Generative Reward Modeling via Semantics-Preserving Compression

- 分数：22.0  ·  HF 赞：16  ·  来源：huggingface
- 兴趣命中：reasoning, evaluation, benchmark
- 作者：Mingqing Yuan, Xiaobo Liang, Junwei Yang, Ziwei Chen, Zeren Zhang, Hejin Wang, Yubin Wang, Juntao Li
- 链接：[arXiv](https://arxiv.org/abs/2610.09788) · [PDF](https://arxiv.org/pdf/2610.09788) · [HF](https://huggingface.co/papers/2610.09788)

Reward modeling often requires jointly representing and reasoning over multiple evaluation criteria, yet verbalizing this process token by token can incur substantial inference cost. Recent work on latent reasoning suggests that continuous states may support this computation more compactly. We introduce LatentGRM, a latent evaluation framework built on semantic chunking, compression, and reconstruction. By using the…

## 30. Video-RSI: Recursive Self-Improvement of Video Understanding Agents via Harness Evolution

- 分数：22.0  ·  HF 赞：12  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark, language model
- 作者：Bingjun Luo, Jialin Guo, Siqi Li
- 链接：[arXiv](https://arxiv.org/abs/2609.37950) · [PDF](https://arxiv.org/pdf/2609.37950) · [HF](https://huggingface.co/papers/2609.37950)

Video understanding agents acquire evidence through an executable harness that controls what they observe and how they use those observations. However, execution traces contain only the evidence acquired by the current harness, leaving competing explanations for failure unresolved and limiting the basis for self-improvement. We introduce Video-RSI, a framework for recursive self-improvement in which a video…

## 31. From Given to Gathered Evidence: Agentic Learning for Longitudinal Medical Reasoning

- 分数：22.0  ·  HF 赞：12  ·  来源：huggingface
- 兴趣命中：agent, tool-use, reasoning, reinforcement learning, evaluation, benchmark, spec
- 作者：Minye Shao, Chaohui Yu, Yixuan Wu, Fan Wang, Ling Shao, Yang Long
- 链接：[arXiv](https://arxiv.org/abs/2609.39566) · [PDF](https://arxiv.org/pdf/2609.39566) · [HF](https://huggingface.co/papers/2609.39566)

Foundation models can serve as clinical agents through tool-use harnesses. However, conventional medical benchmarks assess reasoning over preselected evidence rather than the ability to seek it across clinical records and longitudinal imaging. We propose CASE: a series of role-specific Clinical Agents for Seeking Evidence, together with a tool-use harness and an agentic post-training framework for compact…

## 32. Thinking Inertia: LLMs Keep Thinking When Told Not To

- 分数：22.0  ·  HF 赞：12  ·  来源：huggingface
- 兴趣命中：reasoning, evaluation, language model, large language
- 作者：Dianqiao Lei, Kevin Qinghong Lin, Pan Lu, Philip Torr, James Zou
- 链接：[arXiv](https://arxiv.org/abs/2610.11765) · [PDF](https://arxiv.org/pdf/2610.11765) · [HF](https://huggingface.co/papers/2610.11765)

Large Language Models (LLMs) increasingly ship with explicit "thinking modes", yet their counterpart, "no-thinking", has received far less attention. We study LLMs' no-thinking behavior along two axes. a. How to measure no-thinking? Prior work typically defines no-thinking through proxies such as a disabled thinking mode or the absence of long traces. These proxies are unreliable: disabled thinking modes may still…

## 33. Learning Representations to Guide Pixel Diffusion Transformers

- 分数：21.5  ·  HF 赞：23  ·  来源：huggingface
- 兴趣命中：spec
- 作者：Zihao Pan, Mengting Chen, Cheng Shi, Taihang Hu, Zhengrong Yue, Zikang Wang, Yuan Wang, Wei Li, Sibei Yang
- 链接：[arXiv](https://arxiv.org/abs/2610.12978) · [PDF](https://arxiv.org/pdf/2610.12978) · [HF](https://huggingface.co/papers/2610.12978)

Visual representations are largely developed for understanding, yet what makes them useful for generation remains unclear. We study this question in pixel diffusion transformers and uncover two key insights. First, better representation quality does not necessarily translate into greater generative utility, as externally aligned semantics can be progressively lost during pixel synthesis. Second, architectural…

## 34. Coding-Agent Benchmarks Should Match Their Users' Task Flows

- 分数：21.5  ·  HF 赞：11  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark, coding, planning
- 作者：Igor Slinko, Yaroslav Golubev, Sergey Titov
- 链接：[arXiv](https://arxiv.org/abs/2610.09633) · [PDF](https://arxiv.org/pdf/2610.09633) · [HF](https://huggingface.co/papers/2610.09633)

The evaluation of coding agents generally strives to be as realistic as possible. In our study, we collect 4,782 agent sessions of real software engineers in JetBrains IDEs, which we call Production Sessions. Since our subject is interactive agents, we study the sessions with at least three user messages (33% of the sample). These long sessions differ from issue-derived benchmark tasks in two ways: (i) user requests…

## 35. PreSTO: Predictive Subtree Prefetching for Fast LLM Power Sampling

- 分数：21.5  ·  HF 赞：11  ·  来源：huggingface
- 兴趣命中：reasoning, language model, large language, spec
- 作者：Nan Jiang, Panagiotis Theodoropoulos, Wei Deng
- 链接：[arXiv](https://arxiv.org/abs/2610.13171) · [PDF](https://arxiv.org/pdf/2610.13171) · [HF](https://huggingface.co/papers/2610.13171)

Power sampling improves large language model (LLM) reasoning at test time by sampling from a sharpened version of the base model's distribution. Its sampler, PowerMH, is slow because its Metropolis--Hastings (MH) updates are sequential: each accept/reject decision sets the state from which the next proposal is generated. Prior work reduces this cost by changing the sampler or the model (e.g., sequential Monte Carlo,…

## 36. GroundAnything: Reconciling Parallel Decoding with Precise Visual Grounding at Flash Speed

- 分数：21.0  ·  HF 赞：14  ·  来源：huggingface
- 兴趣命中：benchmark, coding, spec
- 作者：Qize Yu, Lianrui Fan, Bowen Ping, Xini Ding, Zetian Song, Junbo Niu, Kaixuan Wang, Tianxing Chen, Yue Chen, Minghua He, Yuran Wang, Jie Huang, Haojun Zhang, Min Chen, Hao Li, Wenxuan Song, Ruihai Wu, Xianming Liu, Shilong Liu, Shuchang Zhou, Ping Luo, Shiyu Huang
- 链接：[arXiv](https://arxiv.org/abs/2609.39600) · [PDF](https://arxiv.org/pdf/2609.39600) · [HF](https://huggingface.co/papers/2609.39600)

Autoregressive (AR) grounding models serialize spatial predictions, introducing sequential latency and imposing a causal order on output tokens. We view grounding as visual evidence extraction: objects, locations, and spatial relations are jointly constrained by the image and query, yet their dependencies do not imply an intrinsic left-to-right generation order. This distinction makes bidirectional diffusion a…

## 37. Universal Textual Teaching for LLMs

- 分数：21.0  ·  HF 赞：10  ·  来源：huggingface
- 兴趣命中：reasoning, evaluation, language model, large language, spec
- 作者：Zhanyi Lu, Huan Wang
- 链接：[arXiv](https://arxiv.org/abs/2610.12114) · [PDF](https://arxiv.org/pdf/2610.12114) · [HF](https://huggingface.co/papers/2610.12114)

Knowledge distillation (KD) transfers knowledge from stronger Teacher models to weaker Student models, but most methods require training the Student parameters, thereby binding the distilled knowledge to a specific architecture and checkpoint. This implicit representation is difficult to interpret or reuse across models and limits KD for API-only or costly-to-train models. This paper studies knowledge transfer for…

## 38. DataVista: Diagnosing Multimodal LLMs on Data Video Understanding

- 分数：20.5  ·  HF 赞：13  ·  来源：huggingface
- 兴趣命中：reasoning, evaluation, benchmark
- 作者：Yupeng Xie, Zhenyang Wang, Jiayi Zhu, Yinghao Tang, Zhouan Shen, Yiyu Chen, Yuyu Luo
- 链接：[arXiv](https://arxiv.org/abs/2610.11993) · [PDF](https://arxiv.org/pdf/2610.11993) · [HF](https://huggingface.co/papers/2610.11993)

Data video is a media form that integrates data visualization with video narrative, widely adopted in news reporting and business analysis. Compared with general video understanding, data video understanding places greater emphasis on accurately reading data from animated charts, integrating evidence across charts and time, and understanding how narrative organization and visual design communicate information. Yet…

## 39. GraphDecisionBench: Benchmarking System One Models on Graph Tasks

- 分数：20.5  ·  HF 赞：13  ·  来源：huggingface
- 兴趣命中：benchmark, language model, large language
- 作者：Xianliang Yang, Yapu Zhang, Li Zhao
- 链接：[arXiv](https://arxiv.org/abs/2610.06354) · [PDF](https://arxiv.org/pdf/2610.06354) · [HF](https://huggingface.co/papers/2610.06354)

Large language models (LLMs) are increasingly explored for graph understanding and decision-making, while System One models such as Jev select directly from supplied options. However, the capabilities of System One models on graph-related tasks remain unclear. We introduce GraphDecide, a model-independent benchmark that combines structural task profiles, matched graph-text input contrasts and heuristic-proposal…

## 40. Systematic Multi-Agent Vision-and-Language Navigation: Formulation, Benchmark, and Method

- 分数：20.5  ·  HF 赞：9  ·  来源：huggingface
- 兴趣命中：agent, memory, benchmark, planning
- 作者：Yunzhe Xu, Zhe Liu
- 链接：[arXiv](https://arxiv.org/abs/2609.35965) · [PDF](https://arxiv.org/pdf/2609.35965) · [HF](https://huggingface.co/papers/2609.35965)

Vision-and-Language Navigation (VLN) has largely focused on a single agent following a single instruction, yet many real-world applications require teams of robots to tackle tasks beyond the capabilities of any individual agent. We present Systematic Multi-Agent Vision-and-Language Navigation, providing, to our knowledge, the first systematic formalization of multi-agent VLN as a constrained coordination problem:…

## 41. InstantFusion: A Shared Latent Interface for Heterogeneous Image Generators

- 分数：19.5  ·  HF 赞：19  ·  来源：huggingface
- 兴趣命中：spec
- 作者：Xuanlang Dai, Jiazi Bu, Yujie Zhou, Yuhong Liu, Beichen Zhang, Penghui Yang, Ziyu Liu, Yuhang Zang
- 链接：[arXiv](https://arxiv.org/abs/2610.13944) · [PDF](https://arxiv.org/pdf/2610.13944) · [HF](https://huggingface.co/papers/2610.13944)

Diffusion/flow models have emerged as the de facto paradigms for image generation, giving rise to a diverse family of modern generators with increasingly heterogeneous architectures and representations. Despite their remarkable generation capabilities, the cross-model alignment of latent representations and the consistency of their underlying denoising dynamics remain underexplored. In this work, we uncover an…

## 42. AMLworld-Compact: Importance-Weighted Downsampling for Cost-Effective LLM Evaluation and Error Diagnosis

- 分数：19.5  ·  HF 赞：11  ·  来源：huggingface
- 兴趣命中：evaluation, language model, large language
- 作者：Natapong Nitarach, Phume Ngampornsukswadi, Pittawat Taveekitworachai, Surapon Nonesung, Warit Sirichotedumrong, Kunat Pipatanakul
- 链接：[arXiv](https://arxiv.org/abs/2610.13627) · [PDF](https://arxiv.org/pdf/2610.13627) · [HF](https://huggingface.co/papers/2610.13627)

Evaluating large language models (LLMs) on AMLworld's smallest test splits is costly because each of over a million targets requires a separate graph prompt. Sampling reduces this cost, but small balanced subsets change unweighted precision and F1. We introduce AMLworld-Compact, an evaluation set that retains every illicit test transaction and samples benign transactions from supervised-score strata. Its HT-Coreset…

## 43. Humanity's Sixth Sense: Benchmarking Intuitive Visual Reasoning in Multimodal Models

- 分数：19.5  ·  HF 赞：7  ·  来源：huggingface
- 兴趣命中：agent, reasoning, benchmark, language model, large language
- 作者：Xingang Guo, Jing Gu, Brian Jang, Renxiong Wang, Utkarsh Tyagi, Daniel Quigley, Steven Li, David Yan, Daniel Yue Zhang, Darvin Yi, Forrest Huang, HiJae Kim, Tianyi Zhang, Jared Lichtarge, Jihua Huang, Le Xue, Manan Tomar, Qiuyi Richard Zhang, Ruofei Yu, Seth Neel, Yaning Hu, Marcella Valentine, Xinzhe Jiang, Daniel Evans, Chenguang Wang, Dustin Tran, Tong Zhao, Yinfei Yang, Yunzhong He
- 链接：[arXiv](https://arxiv.org/abs/2610.08966) · [PDF](https://arxiv.org/pdf/2610.08966) · [HF](https://huggingface.co/papers/2610.08966)

Humans perceive far more in a scene than what is explicitly depicted: a single glance captures past causes and future trajectories; a quick peek determines if a vehicle can fit between two parked cars; a few seconds of video reveals who holds authority in a room; and a fleeting clip highlights subtle abstract patterns like unwritten rules or hidden labels. This capacity reflects a form of humanity's sixth sense: an…

## 44. When Do Biological Reasoning Models Use Their Biological Inputs?

- 分数：19.0  ·  HF 赞：10  ·  来源：huggingface
- 兴趣命中：reasoning, benchmark, language model
- 作者：Ada Fang, Nikitha Thoduguli, Lukas Fesser, Hanlin Zhang, Sham M. Kakade, Marinka Zitnik
- 链接：[arXiv](https://arxiv.org/abs/2610.00898) · [PDF](https://arxiv.org/pdf/2610.00898) · [HF](https://huggingface.co/papers/2610.00898)

Biological reasoning models use post-training to connect LLMs to biological foundation model representations and biological text. Their benchmark accuracy is taken as evidence that LLMs reason over these inputs. We test this assumption in six biological reasoning models across DNA, protein, and single-cell tasks. We perturb one biological input while holding the query and other inputs fixed, construct evidence…

## 45. QuantMLA: Function-Aligned Dual-Path Quantization for Low-Bit MLA KV Caching

- 分数：19.0  ·  HF 赞：6  ·  来源：huggingface
- 兴趣命中：memory, reasoning, benchmark, spec
- 作者：Zunhai Su, Yuxuan Sun, Jianchao Tan, Tao Zhang, Ruihan Hu, Yuchen Xie, Xunliang Cai, Ngai Wong
- 链接：[arXiv](https://arxiv.org/abs/2609.36760) · [PDF](https://arxiv.org/pdf/2609.36760) · [HF](https://huggingface.co/papers/2609.36760)

Multi-Head Latent Attention (MLA) enables expressive multi-head attention with compact caches for its content and decoupled RoPE paths, yet cache memory still scales linearly with context length and batch size. In this work, we establish a systematic model of MLA's dual-path quantization errors, characterizing their distinct effects on attention-output distortion and explaining the pronounced amplification of…

## 46. Mental-Models for Multi-Agent Systems

- 分数：17.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：agent, memory, reasoning, benchmark
- 作者：Hanan Gani, Lulu Shao, Manmohan Chandraker
- 链接：[arXiv](https://arxiv.org/abs/2610.12453) · [PDF](https://arxiv.org/pdf/2610.12453) · [HF](https://huggingface.co/papers/2610.12453)

Large foundation models have accelerated progress toward general-purpose agents that interact with humans and other agents through language and multimodal signals. However, robust multi-agent decision-making requires reasoning about what other agents know, intend, and are likely to do under partial observability. Current agentic systems often operate through prompt design, memory, or end-to-end behavioral shaping,…

## 47. Clinician use of language models diverges from how the models are evaluated

- 分数：17.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：evaluation, benchmark, language model, large language, spec, retrieval
- 作者：Krithik Vishwanath, Haitong Lin, Anton Alyakin, Jin Vivian Lee, D. Brock Hewitt, Jie J. Yao, William Robert Small, Hammad A. Khan, Cordelia Orillac, Aakaash Varma, Brandon Ye, Daniel Alexander Alber, Gustavo Stolovitzky, Batia Wiesenfeld, Oded Nov, Wei Wu, Kang Zhang, Yindalon Aphinyanaphongs, Tim Requarth, Eric Karl Oermann, The International Digital Twin Consortium in Healthcare, Medicine
- 链接：[arXiv](https://arxiv.org/abs/2610.11069) · [PDF](https://arxiv.org/pdf/2610.11069) · [HF](https://huggingface.co/papers/2610.11069)

Large language model (LLM) assistants are being deployed to clinicians across health systems, and judgments about their readiness rest largely on benchmark scores, most of them derived from examination questions or curated cases. A benchmark predicts performance in deployment only to the extent that its items resemble real use, yet whether benchmarks reflect the work these systems receive has rarely been measured.…

## 48. Rethinking Relative Policy Differences Transfer of On-Policy Distillation

- 分数：17.0  ·  HF 赞：10  ·  来源：huggingface
- 兴趣命中：reinforcement learning, spec
- 作者：Rong Wu, Daocheng Fu, Yu Yang, Xuemeng Yang, Siqi Li, Shu Zou, Yao Zhu, Botian Shi, Bo Zhang, Cong Zhang, Pinlong Cai, Jianbiao Mei
- 链接：[arXiv](https://arxiv.org/abs/2610.13205) · [PDF](https://arxiv.org/pdf/2610.13205) · [HF](https://huggingface.co/papers/2610.13205)

On-policy distillation (OPD) trains a target policy on its own rollouts using token-level supervision from a stronger teacher, but typically relies on the teacher being substantially more capable than the target. Recent work relaxes this requirement by transferring the relative policy difference between an expert and a reference policy rather than the expert's absolute distribution. Yet it remains unclear which…

## 49. When to Rethink: Learning Multi-Perspective Self-Verification for Vision-Language Models

- 分数：17.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：reasoning, benchmark, language model, spec
- 作者：Ziquan Zhu, Hanruo Zhu, Si-Yuan Lu, Morris Yu-Chao Huang, Yicheng Lin, Wei Han, Tianlong Chen, Mingyuan Wu, Hanchao Yu, Gaojie Jin, Lu Liu, Bo Sun, Tianjin Huang
- 链接：[arXiv](https://arxiv.org/abs/2610.07018) · [PDF](https://arxiv.org/pdf/2610.07018) · [HF](https://huggingface.co/papers/2610.07018)

Vision-language models (VLMs) have achieved strong performance in multimodal reasoning, yet they remain prone to generating plausible but incorrect answers. Self-verification offers a practical way to improve answer reliability without relying on external judges, but existing methods typically depend on a single verification criterion or fixed prompt, resulting in incomplete and unstable reliability estimates. We…

## 50. Learning More by Training Less: Uncertainty-Guided Progressive Contraction for Efficient Reasoning Post-Training

- 分数：17.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：reasoning, benchmark, language model, large language, spec
- 作者：Suorong Yang, Jiaxin Wang, Jiaming Su, Chentao Yue, Furao Shen, Peng Ye, Soujanya Poria
- 链接：[arXiv](https://arxiv.org/abs/2610.12933) · [PDF](https://arxiv.org/pdf/2610.12933) · [HF](https://huggingface.co/papers/2610.12933)

Large language models have achieved remarkable advances in complex reasoning. However, scaling reasoning post-training with ever-larger corpora can substantially increase training cost without proportional performance gains. In this study, we therefore ask: how far can reasoning supervision be compressed without sacrificing capability? To this end, we propose an uncertainty-guided progressive contraction framework…

## 51. When Do We Need On-Policy Distillation? Distilling on Offline Student Rollouts Is Often Better

- 分数：16.5  ·  HF 赞：17  ·  来源：huggingface
- 兴趣命中：-
- 作者：Siyan Zhao, Yonggan Fu, Jindong Jiang, Shih-Yang Liu, Song Bian, Byung-Kwan Lee, Sharath Turuvekere Sreenivas, Wenliang Dai, Hanrong Ye, Aditya Grover, Pavlo Molchanov
- 链接：[arXiv](https://arxiv.org/abs/2610.11291) · [PDF](https://arxiv.org/pdf/2610.11291) · [HF](https://huggingface.co/papers/2610.11291)

On-policy distillation (OPD) has become increasingly popular for transferring teacher capabilities to student models. In this work, we ask a critical research question: Is on-policy sampling always beneficial for distilling arbitrary teacher-student pairs? We show that a simple alternative, Semi-OPD, which distills from offline rollouts generated by the initial student, can often outperform OPD in both accuracy and…

## 52. Relevance Does Not Imply Applicability: Experience Activation for Personal GUI Agents

- 分数：16.5  ·  HF 赞：13  ·  来源：huggingface
- 兴趣命中：agent
- 作者：Fuyao Zhang, Xuan Wang, Zherui Li, Jiaming Zhang, Longtao Huang, Wei Yang Bryan Lim
- 链接：[arXiv](https://arxiv.org/abs/2609.33304) · [PDF](https://arxiv.org/pdf/2609.33304) · [HF](https://huggingface.co/papers/2609.33304)

Personal Graphical User Interface (GUI) agents rely on interaction history to infer what a user wants from ambiguous instructions and to anticipate recurring routines. Existing approaches retrieve task-relevant history and append it to the policy's context, implicitly assuming that experience relevant to a task remains useful for each decision within it. We find that this help is largely spent at the first decision:…

## 53. MixTok: Adaptive Visual Tokenization with Global 1D Tokens and Sparse 2D Refinement

- 分数：16.5  ·  HF 赞：13  ·  来源：huggingface
- 兴趣命中：spec
- 作者：Chenge Li, Yefei He, Xinyu Liu, Feng Chen, Hong Zhou, Bohan Zhuang
- 链接：[arXiv](https://arxiv.org/abs/2610.13181) · [PDF](https://arxiv.org/pdf/2610.13181) · [HF](https://huggingface.co/papers/2610.13181)

Efficient visual tokenization requires balancing representation compactness with the preservation of fine-grained image content. Conventional grid-based tokenizers allocate tokens uniformly across spatial locations despite non-uniform visual complexity, whereas compact 1D tokenizers aggregate global information but can struggle to preserve local details. We introduce MixTok, a hybrid visual tokenizer that combines a…

## 54. Encore: Few-Shot Agentic Discovery of Manipulation Strategies

- 分数：16.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：agent, evaluation, language model, coding, spec
- 作者：Yifan Kang, Zihan Wang, Zhiwen Fan, Bangya Liu
- 链接：[arXiv](https://arxiv.org/abs/2609.37359) · [PDF](https://arxiv.org/pdf/2609.37359) · [HF](https://huggingface.co/papers/2609.37359)

Coding agents can now write, run, and debug programs with little human help. Robot tasks, however, are usually specified by a sentence that leaves out how to grasp, in what order to make contact, and what the result should look like, and an agent given only the sentence must find these details by trial and error. We introduce ENCORE, which gives the agent a few demonstrations as evidence to read rather than as…

## 55. Which Language Should a Skeleton Speak? Language Choices in Multilingual Reasoning

- 分数：16.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：reasoning, evaluation, benchmark, coding
- 作者：HyeonSeok Lim, SeungWoo Song, Inho Won, Hoyun Song, Jihyo Kim, KyungTae Lim
- 链接：[arXiv](https://arxiv.org/abs/2610.09607) · [PDF](https://arxiv.org/pdf/2610.09607) · [HF](https://huggingface.co/papers/2610.09607)

Skeleton-based reasoning prompting is a promising training-free approach for structuring LLM reasoning, but prior work largely assumes an English-centric setting. We propose the Language-Aware Skeleton Exploration Framework (LASEF) to study skeleton-language choice in multilingual mathematical reasoning. Across math benchmarks, model scales, and languages, we show that English skeletons yield a small positive…

## 56. Less from More: Reinforcing Sparse Video Reasoning from Dense References

- 分数：16.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：reasoning, benchmark, language model
- 作者：Wenfang Sun, Yingjun Du, Cees G. M. Snoek
- 链接：[arXiv](https://arxiv.org/abs/2610.10893) · [PDF](https://arxiv.org/pdf/2610.10893) · [HF](https://huggingface.co/papers/2610.10893)

Video-language models commonly assume that more temporal observations lead to more reliable reasoning. We question this assumption and argue that the key challenge is not merely processing more video frames efficiently, but learning to reason reliably under limited temporal evidence. We propose SAVER, a dense-to-sparse post-training framework that uses dense video views as training-time references for sparse-frame…

## 57. ThinkDrag: Semantic Drag-Based Image Editing with Visual Reasoning

- 分数：16.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：reasoning, benchmark, spec
- 作者：Armando Fortes, Tianyi Wei, Chindanai Trakantannarong, Shangchen Zhou, Xingang Pan
- 链接：[arXiv](https://arxiv.org/abs/2610.13316) · [PDF](https://arxiv.org/pdf/2610.13316) · [HF](https://huggingface.co/papers/2610.13316)

Drag-based image editing provides an intuitive interface for spatially controlled image manipulation by allowing users to specify handle and target points. Existing methods have made substantial progress through optimization-based, one-step, and feed-forward formulations, but they often interpret drag instructions as geometric displacements. This limits their effectiveness when the desired edit depends on…

## 58. TouchScale: 500 Hours of Human Vision and Touch for Visual-Tactile Learning

- 分数：15.0  ·  HF 赞：10  ·  来源：huggingface
- 兴趣命中：benchmark
- 作者：Dayou Li, Hao Wang, Qianqian Yang, Zihao Zhu, Haoquan Fang, Ziyao Zeng, Yan Han, Zihan Wang, Yan Wang, Baoru Huang, Dilin Wang, Kenji Shimada, Yiyue Luo, Manling Li, Teresa Lv, Mustafa Mukadam, Rakesh Ranjan, Ruohan Zhang, Qi He, Changliu Liu, Xu Chen, Marco Pavone, Bangya Liu, Jiachen Li, Masayoshi Tomizuka, Zhiwen Fan
- 链接：[arXiv](https://arxiv.org/abs/2610.10288) · [PDF](https://arxiv.org/pdf/2610.10288) · [HF](https://huggingface.co/papers/2610.10288)

Large-scale egocentric human interaction data is becoming an important source of physical supervision for embodied learning, yet video alone leaves the contact and pressure that characterize physical interaction unrecorded. Recent visual-tactile datasets provide this missing supervision, but their synchronized tactile data remain far smaller in volume than human video. Moreover, the largest resources often merge…

## 59. The value of information and the emergence of communication in evolved e-puck robots

- 分数：14.5  ·  HF 赞：9  ·  来源：huggingface
- 兴趣命中：agent
- 作者：Fernando Montes-Gonzalez
- 链接：[arXiv](https://arxiv.org/abs/2610.13118) · [PDF](https://arxiv.org/pdf/2610.13118) · [HF](https://huggingface.co/papers/2610.13118)

We study when communication emerges between autonomous agents and what role an innate action selection architecture plays. Two e-puck robots, reconstructed in PyBullet from their Webots model and validated against it, must find a feeding zone that can only be detected when a robot passes over it. Each robot can emit a one-bit signal whose direction is detected by the receiver. Control is provided by a GRU recurrent…

## 60. One Model to Loop Them All: Elastic Latent Recurrence for Language Models

- 分数：14.5  ·  HF 赞：5  ·  来源：huggingface
- 兴趣命中：memory, language model
- 作者：Faisal Ladhak, Shantanu Acharya, Santiago Akle Serano, Simeng Sun, Boris Ginsburg, Krishna C Puvvada
- 链接：[arXiv](https://arxiv.org/abs/2610.12582) · [PDF](https://arxiv.org/pdf/2610.12582) · [HF](https://huggingface.co/papers/2610.12582)

A latent recurrent language model applies a shared block of layers repeatedly, so one checkpoint can trade inference compute for accuracy by changing the loop count. At one loop, however, such models typically fall well short of a non-recurrent model of the same size, a one-loop tax that makes a separate non-recurrent model the better choice whenever latency matters. We present Elastic Latent Recurrence (ELR), a…

## 61. GATOR: Generative and Agentic 3D Object Reconstruction From Casual Images

- 分数：14.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：agent, reasoning, spec
- 作者：Qirui Wu, Stan Birchfield, Hesam Rabeti, Angel X. Chang, Bowen Wen
- 链接：[arXiv](https://arxiv.org/abs/2610.11215) · [PDF](https://arxiv.org/pdf/2610.11215) · [HF](https://huggingface.co/papers/2610.11215)

Reconstructing complete, scene-aligned 3D objects from casual images requires integrating sparse, uncertain observations and inferring surfaces hidden by occlusions. We present GATOR, a generative and agentic framework that recovers textured object assets and their scene-relative pose from one or more images. Our local modality mixer couples patch-aligned RGB, target-mask, and pointmap features before cross-view…

## 62. ARCS: Towards Precise Text-to-SQL via Structured Disambiguation

- 分数：13.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：benchmark, spec
- 作者：Yihao Hu, Yanlin Feng, Naoki Otani, Nikita Bhutani
- 链接：[arXiv](https://arxiv.org/abs/2610.09396) · [PDF](https://arxiv.org/pdf/2610.09396) · [HF](https://huggingface.co/papers/2610.09396)

As text-to-SQL systems move beyond demonstrations toward real-world deployment, ambiguity in user questions becomes a primary source of errors. Such ambiguities are often subtle, domain- or data-specific, and can silently cause system outputs to deviate from the user's true intent. Ambiguity is traditionally addressed through conversational clarification, which is often inefficient, cognitively demanding, and poorly…

## 63. SPLATIFY: Reproduce, Discover, Innovate! From Papers and Ideas to Trainable 3DGS Code

- 分数：12.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：agent, evaluation
- 作者：Seemandhar Jain, Keshav Gupta, Manmohan Chandraker
- 链接：[arXiv](https://arxiv.org/abs/2610.09116) · [PDF](https://arxiv.org/pdf/2610.09116) · [HF](https://huggingface.co/papers/2610.09116)

The rapid growth of 3D Gaussian Splatting (3DGS) research demands significant effort to reimplement papers before building on them. We introduce SPLATIFY, a multi-agent framework that converts 3DGS papers into trainable gsplat-based implementations, where generic paper-to-code methods and frontier models fail. SPLATIFY achieves this through five innovations: (1) A context-free grammar for gsplat over a modular…

## 64. Few-Step Generation via Data-Space Iteration

- 分数：12.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：evaluation, spec
- 作者：Shanchuan Lin, Yansong Peng, Fu-Yun Wang, Haoqi Fan
- 链接：[arXiv](https://arxiv.org/abs/2610.12102) · [PDF](https://arxiv.org/pdf/2610.12102) · [HF](https://huggingface.co/papers/2610.12102)

Flow matching has emerged as a scalable paradigm for training high-quality generative models, but sampling from the learned probability flow requires many network evaluations. Distillation can reduce this cost to one or a few evaluations; however, one-step generation often sacrifices quality, making few-step generation the practical operating regime. Existing few-step methods perform their iterative computation…

## 65. Dex-One2Many: Learning Dexterous Manipulation from a Single Human Demonstration

- 分数：12.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：tool-use, reinforcement learning
- 作者：Jusuk Lee, Sungha Kim, Yeonsoo Park, Jonguk Cheon, Yoonkyo Jung, Yongjun You, H. Jin Kim, Jia-Bin Huang, Furong Huang, Youngseok Jang, Seungjae Lee
- 链接：[arXiv](https://arxiv.org/abs/2610.12470) · [PDF](https://arxiv.org/pdf/2610.12470) · [HF](https://huggingface.co/papers/2610.12470)

While learning dexterous manipulation from a single human video offers a promising alternative to costly robot demonstrations, many recent methods predominantly imitate demonstrated motions. Such strict motion matching often limits generalization to initial object poses, goal poses, and grasps not shown in the video. Alternatively, discovering a policy via reinforcement learning (RL) allows for broad generalization,…

## 66. Distributionally Robust Mixture-of-Experts Training

- 分数：12.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：spec
- 作者：Xin Teng, Muxiao Li, Hongyi Wen
- 链接：[arXiv](https://arxiv.org/abs/2610.07207) · [PDF](https://arxiv.org/pdf/2610.07207) · [HF](https://huggingface.co/papers/2610.07207)

Mixture-of-Experts (MoE) transformers scale capacity by activating only a few experts per token, but this sparsity creates a hidden reliability problem: when routing is imperfect, load-balanced models may send tokens to experts that are insufficiently trained for the assigned inputs. We propose Distributionally Robust MoE Training (DRMoET), a drop-in objective that treats layer-wise experts as endogenous robustness…

## 67. T3lescope: Arbitrary-Resolution High-Fidelity Generative Surface Reconstruction from Images

- 分数：11.5  ·  HF 赞：7  ·  来源：huggingface
- 兴趣命中：-
- 作者：Atsuhiro Noguchi, Tianhan Xu, Yiming Liang, Yuta Kikuchi, Masahiro Ishiyama, Shintaro Takagi, Hitoshi Murai, Eiichi Matsumoto
- 链接：[arXiv](https://arxiv.org/abs/2610.03308) · [PDF](https://arxiv.org/pdf/2610.03308) · [HF](https://huggingface.co/papers/2610.03308)

We reconstruct high-fidelity 3D scene meshes from posed multi-view images without per-scene optimization, across scales ranging from single objects to large outdoor scenes. Per-scene optimization methods lack the learned 3D prior needed when observations are sparse or surfaces are glossy or transparent. Existing generative methods leverage such priors to complete geometry in sparsely observed regions, but typically…

## 68. Self-Preservation in Language Models

- 分数：11.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：language model
- 作者：Dongkyu Cho, Rumi Chunara, Ali Behrouz
- 链接：[arXiv](https://arxiv.org/abs/2610.12602) · [PDF](https://arxiv.org/pdf/2610.12602) · [HF](https://huggingface.co/papers/2610.12602)

Continual learning (CL) seeks to adapt pretrained models while preserving prior capabilities. Yet the tasks supplied for preservation cover only part of what a model knows, while forgetting can extend beyond them. Recent work shows that language models can supplement this limited evidence by generating useful replay without access to their original training data. This raises a question about self-preservation: can a…

## 69. SAGE: Salient Factor Discovery and Generation with Visual Foundation Representations

- 分数：11.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：spec
- 作者：Shuang Liang, Lejun Liao, Shiyuan Zhang, Max C. Zhang, Xiaolong Luo, Han Wang, Stefano Anzellotti, Yuan Yuan
- 链接：[arXiv](https://arxiv.org/abs/2609.39635) · [PDF](https://arxiv.org/pdf/2609.39635) · [HF](https://huggingface.co/papers/2609.39635)

Given a target dataset, such as faces with eyeglasses, and a background dataset, such as faces without, contrastive analysis separates salient factors specific to the target from common content shared by both. We aim for salient representations that capture target-specific detail in each image, such as the shape, color, and position of the glasses, so that they reveal subtypes without subtype labels and guide the…

## 70. Video-Conditioned Generative Joint 2D-3D Hand Motion Recovery

- 分数：10.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：benchmark
- 作者：Chen Xu, Yunqi Li, Binbin Huang, Brent Yi, Shenghua Gao, Yi Ma
- 链接：[arXiv](https://arxiv.org/abs/2610.10512) · [PDF](https://arxiv.org/pdf/2610.10512) · [HF](https://huggingface.co/papers/2610.10512)

Recovering faithful 3D hand motion from video remains challenging due to frequent occlusions and incomplete visual observations, which make frame-wise pose estimates unreliable and temporally inconsistent. To address this problem, we propose JoHan, a unified generative framework that recovers hand motion directly from video sequences without relying on intermediate per-frame pose predictions. Trained from scratch,…

## 71. MAMHOI: Factorizing Scene-Aware Human-Object Interaction through Affordances

- 分数：10.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：reasoning
- 作者：Mingyuan Lei, Yoonchang Sung, Tat-Jen Cham
- 链接：[arXiv](https://arxiv.org/abs/2610.12416) · [PDF](https://arxiv.org/pdf/2610.12416) · [HF](https://huggingface.co/papers/2610.12416)

Generating realistic human-object interactions (HOI) in complex 3D scenes requires two complementary capabilities: reasoning about interaction feasibility in the environment and synthesizing realistic human-object motion. However, supervision for these capabilities is rarely available jointly at scale. Human-scene datasets provide rich information about environment-aware motion, while human-object datasets capture…

## 72. The Life Cycle of a Massive Activation: Stochastic Birth, Weight-Decay-Driven Growth, and Competitive Consolidation

- 分数：9.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：-
- 作者：S. Aaron McClendon, Jorge Gallego-Feliciano, Antonios Saravanos
- 链接：[arXiv](https://arxiv.org/abs/2610.00423) · [PDF](https://arxiv.org/pdf/2610.00423) · [HF](https://huggingface.co/papers/2610.00423)

Massive activations, residual-stream coordinates with magnitudes far larger than typical activations, are associated with attention sinks in transformers, but how their scale is regulated during training remains incompletely understood. Combining training-trajectory analyses and controlled interventions, we trace their emergence, growth, and consolidation. Sink-carrying channels vary across random seeds but…

## 73. BudgetPix: Compute-Adaptive Tokenization for Pixel-Space Image Diffusion

- 分数：8.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：-
- 作者：Ozgur Kara, Yujia Chen, Daniel Watson, David Forsyth, James Matthew Rehg, Wen-Sheng Chu, Du Tran
- 链接：[arXiv](https://arxiv.org/abs/2610.12307) · [PDF](https://arxiv.org/pdf/2610.12307) · [HF](https://huggingface.co/papers/2610.12307)

Most image generation models rely on uniform tokenization, allocating the exact same computational budget to equally-sized image patches. This static paradigm cannot adapt to different resource constraints at inference time, and yields suboptimal quality-cost tradeoff by devoting the same effort to both plain backgrounds and intricate details. We propose BudgetPix, an adaptive tokenization framework that dynamically…
