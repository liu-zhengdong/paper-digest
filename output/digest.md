# 每日 AI 论文

生成时间：2026-10-22 04:47 UTC  ·  共 120 篇（已按 arXiv ID 去重）

来源：Hugging Face Daily Papers + arXiv（cs.AI / cs.LG / cs.CL / cs.CV）。
排序：HF 上榜、点赞、多源命中、兴趣词。兴趣词可在 `config.json` 改。

## 1. Ropedia W0: Scaling Loco-Manipulation World Models across Embodiments with Human Experience

- 分数：36.0  ·  HF 赞：182  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark, spec, planning
- 作者：Tianqi Liu, Hanfei Zhao, Qifeng Liang, Hui En Pang, Jiarui Xu, Sayang Mu, Penghao Qiu, YingSheng Zhang, Jun Wang, Ziang Cao, Mingze Sun, Yukang Cao, Fangzhou Hong, Zhaoxi Chen, Ziwei Liu
- 链接：[arXiv](https://arxiv.org/abs/2610.26855) · [PDF](https://arxiv.org/pdf/2610.26855) · [HF](https://huggingface.co/papers/2610.26855)

World models enable embodied agents to anticipate action consequences, yet jointly modeling locomotion and manipulation across diverse embodiments remains challenging due to heterogeneous action spaces and limited multimodal supervision. We present Ropedia W0, the first egocentric loco-manipulation world foundation model spanning humans and robots with diverse embodiments. We curate Xp-Data, comprising 10k hours of…

## 2. S-Agent 2.0: Spatial Reasoning with a General Coding Agent

- 分数：36.0  ·  HF 赞：96  ·  来源：huggingface
- 兴趣命中：agent, memory, reasoning, coding, spec
- 作者：Rui Gong, Ruoyu Wang, Yalun Dai, Hao Li, Sidi Yang, Qihao Zhao, Hongyu Li, Zeyang Guan, Fangzhou Hong, Zhaoxi Chen, Kim-Hui Yap, Ziwei Liu
- 链接：[arXiv](https://arxiv.org/abs/2610.28354) · [PDF](https://arxiv.org/pdf/2610.28354) · [HF](https://huggingface.co/papers/2610.28354)

Spatial reasoning asks a model to work out where objects are in 3D space, how they relate to one another, and how they move. Agentic VLMs have recently brought large improvements on such tasks by letting the model actively gather evidence with 3D perception tools instead of answering in a single pass. Even so, on many questions the tools return the right evidence and the model still does not arrive at the correct…

## 3. SolarRenderer: Few-Step Generative Reference Rendering

- 分数：36.0  ·  HF 赞：47  ·  来源：huggingface
- 兴趣命中：agent, benchmark, coding, spec
- 作者：Guian Fang, Shengju Qian, Dongyue Lu, Junchao Huang, Lutao Jiang, Xin Wang, Yiren Song, Li Jiang, Mike Zheng Shou
- 链接：[arXiv](https://arxiv.org/abs/2610.28630) · [PDF](https://arxiv.org/pdf/2610.28630) · [HF](https://huggingface.co/papers/2610.28630)

Game engines and coding agents can specify the layout, motion, and camera of a scene, yet turning such coarse structure into realistic video requires a renderer that follows the structure and completes the appearance it leaves open. Existing renderers are tied to the representation of one engine, need tens of denoising steps or a costly distillation of their own, and learn from conditions that are not aligned with…

## 4. Agent World Model in the Wild: Computer-Use Agent Environment Synthesis

- 分数：36.0  ·  HF 赞：45  ·  来源：huggingface
- 兴趣命中：agent, tool use, benchmark, spec
- 作者：Zhaoyang Wang, Qianhui Wu, Haorui Wang, Simon Yu, Baolin Peng, Canwen Xu, Hao Cheng, Wenlin Yao, Boyi Liu, Yite Wang, Jianfeng Gao, Huaxiu Yao
- 链接：[arXiv](https://arxiv.org/abs/2610.26828) · [PDF](https://arxiv.org/pdf/2610.26828) · [HF](https://huggingface.co/papers/2610.26828)

Agent learning is shifting from learning from human data toward learning through interaction with the world. However, scaling such learning directly in real-world computer systems is challenging and can introduce substantial security risks. We therefore propose Agent World Model in the Wild (WildAWM), a scalable pipeline for synthesizing controllable environments and tasks for training general computer-use agents…

## 5. Matrix-Game 4.0: Harnessing Video Models for Real-Time Playable Game Worlds

- 分数：34.0  ·  HF 赞：182  ·  来源：huggingface
- 兴趣命中：agent, memory, coding
- 作者：Jihai Zhang, Runjia Qian, Kaiqin Kong, Biao Jiang, Puyi Wang, Siru Chen, Tianle Li, Guanjie Chen, Junyi Wu, Chubin Chen, Yuanhang Li, Kaichen Huang, Haobo Zhang, Yangguang Li, Wei Yu, Guibin Chen, Yu Cheng, Yahui Zhou
- 链接：[arXiv](https://arxiv.org/abs/2610.27999) · [PDF](https://arxiv.org/pdf/2610.27999) · [HF](https://huggingface.co/papers/2610.27999)

Moving from controllable videos to genuinely playable worlds requires persistent world state, executable game rules, and low-latency interaction. We outline a roadmap for the next generation of Matrix-Game that separates game execution from visual generation through an executable game harness, and introduce Matrix-Game 4.0 as the first system built on this design. A lightweight game engine maintains world state and…

## 6. Cache Engineering for Agents

- 分数：33.0  ·  HF 赞：34  ·  来源：huggingface
- 兴趣命中：agent, benchmark, language model, large language, coding, spec
- 作者：Tianyu Fu, Ruoxi Wang, Zihan Min, Zhongqi Ren, Zhihao Li, Tengxuan Liu, Shengxu Mu, Hanling Zhang, Yu Wang
- 链接：[arXiv](https://arxiv.org/abs/2610.28577) · [PDF](https://arxiv.org/pdf/2610.28577) · [HF](https://huggingface.co/papers/2610.28577)

Large Language Model (LLM) agents can handle increasingly complex tasks, navigating long trajectories of observations and actions. As these trajectories grow, key-value (KV) cache I/O and storage become the dominant cost. Trajectories can also exceed the LLM's maximum context length, requiring control over active cache growth. Prior work uses context engineering to reduce cache size by trimming or summarizing…

## 7. Focused Omni-Modal GUI Agents

- 分数：32.0  ·  HF 赞：226  ·  来源：huggingface
- 兴趣命中：agent, spec
- 作者：Fuyao Zhang, Wenwen He, Jiaming Zhang, Yurong Hao, Xuan Wang, Guowei Guan, Che Wang, Longtao Huang, Wei Yang Bryan Lim
- 链接：[arXiv](https://arxiv.org/abs/2610.26203) · [PDF](https://arxiv.org/pdf/2610.26203) · [HF](https://huggingface.co/papers/2610.26203)

Graphical User Interface (GUI) agents increasingly act over streaming omni-modal observations spanning screenshots, audio, video, interaction history, and device states. However, exposing this complete context uniformly at every step ignores that relevance is transient and sparse: the signal determining one action can become clutter at the next. Because executed actions feed back into the context, these errors…

## 8. PAR: Progress-Aligned Recurrence for Length Generalization in State Tracking

- 分数：32.0  ·  HF 赞：148  ·  来源：huggingface
- 兴趣命中：language model, spec
- 作者：Pan Wang, Yihao Hu, Guangyuan Dong, Yitong Lin, Hang Wang, Zimi Liu, Zhihao Wen, Jianshe Li, Jiang-Ming Yang, Wei Wu, Yongqi Tong
- 链接：[arXiv](https://arxiv.org/abs/2610.27628) · [PDF](https://arxiv.org/pdf/2610.27628) · [HF](https://huggingface.co/papers/2610.27628)

Looped language models can run more iterations at test time, but additional iterations need not help them solve longer problems. For sequential state tracking, final-answer supervision does not specify how far each iteration should advance, and repeated updates can change the scale of the recurrent state. We introduce Progress-Aligned Recurrence (PAR), which trains the prediction at iteration k to match the state…

## 9. Sage-A1.5: From Long-Horizon Execution to Scientific Exploration with Capability Composition

- 分数：32.0  ·  HF 赞：64  ·  来源：huggingface
- 兴趣命中：agent, spec
- 作者：Wenjie Lou, Tianshuo Peng, Shiyang Feng, Shengji Tang, Runmin Ma, Ruizhe Chen, Jinxin Shi, Haoyang Peng, Fangchen Yu, Zhijie Zhong, Yuhao Zhou, Yue Fan, Yixin Chen, Yiming Wu, Yiheng Wang, Yigeng Jiang, Yichen Jiang, Yi Xie, Xu Guo, Xiaohan He, Tao Hu, Songtao Huang, Siyu Zhou, Shuaiyu Zhang, Shangheng Du, Qinglong Cao, Kun Li, Jingqi Ye, Hongbin Zhou, Guohang Yan, Zongsheng Cao, Ziyi Wang, Zhuo Liu, Zhiyin Yu, Zhiwang Zhou, Zelin Tan, Yuqing Zhu, Yaoze Zhang, Yang Chen, Xuming He, Xiuliang Liang, Xingjian Guo, Xiang Zhuang, Weiping Shen, Weida Wang, Tianyuan Zhou, Tianlin Ye, Tengyuan Fan, Siyu Yan, Shuo Li, Shuchen Pu, Shengyuan Xu, Shao Zhang, Ran Wei, Qinyuan Qin, Qingyu Yang, Nianchen Deng, Meng Dai, Kuikun Liu, Kaitao Chen, Juncheng Xiao, Jiangning Liu, Jianbiao Mei, Jia Yu, Haonan He, Hangfan Zhang, Cheng Yang, Chen Zhang, Bihao Zhan, Benteng Cheng, Yuqiang Li, Yihao Liu, Yang Yang, Xujun Fu, Xiaosong Wang, Xiangyu Yue, Wenwei Zhang, Shuyue Hu, Pinlong Cai, Mianxin Liu, Lei Bai, Jie Zhou, Jie Hou, Jiamin Wu, Hui Wang, Haijun Li, Guangyu Wang, Dongzhan Zhou, Chunfeng Song, Chao Yang, Biqing Qi, Xing Xie, Dahua Lin, Bowen Zhou, Xiangchao Yan, Wenlong Zhang, Shufei Zhang, Peng Ye, Bo Zhang
- 链接：[arXiv](https://arxiv.org/abs/2610.28578) · [PDF](https://arxiv.org/pdf/2610.28578) · [HF](https://huggingface.co/papers/2610.28578)

In this report, we introduce Sage-A1.5, a 35B Mixture-of-Experts agentic model that builds on A1 to advance long-horizon problem solving through adaptive capability composition. Compared with A1, Sage-A1.5 learns not only to solve individual tasks, but also to organize work and revise its approach during execution. Sage-A1.5 highlights three improvements: agentic orchestration, verification, and open scientific…

## 10. VLA-Rolling: Fewer Denoising Steps, Better Control via Adaptive Action Reuse

- 分数：32.0  ·  HF 赞：60  ·  来源：huggingface
- 兴趣命中：benchmark, planning
- 作者：Sicheng He, Yi Pan, Qiuting Yu, Jiaming Huang, Qi Lu, Shuyan Wu, Hongyan Feng, Xuanyu Liu, Jun Zhang, Jie Zhang, Wenqi Zhang, Xuhong Zhang, Jianwei Yin
- 链接：[arXiv](https://arxiv.org/abs/2610.25043) · [PDF](https://arxiv.org/pdf/2610.25043) · [HF](https://huggingface.co/papers/2610.25043)

Flow-matching vision-language-action (VLA) models generate an action chunk by iteratively denoising Gaussian noise, but typically execute only a short prefix before replanning with updated observations. Under this receding-horizon paradigm, the unexecuted remainder---the action tail---is discarded, and the next chunk is regenerated from fresh noise. We show that this discarded tail retains transferable denoising…

## 11. Learning the 4D World through Point Trajectory Forecasting

- 分数：32.0  ·  HF 赞：42  ·  来源：huggingface
- 兴趣命中：evaluation, benchmark
- 作者：Byungwoo Jeon, Sunghwan Hong, Dohyeon Kim, Jonghoon Lee, Jungwoo Park, Inhee Lee, Doosan Baek, Jinil Kim, Taehyun Lim, Hanbyul Joo, Marc Pollefeys, Saining Xie, Jinwoo Shin
- 链接：[arXiv](https://arxiv.org/abs/2610.28594) · [PDF](https://arxiv.org/pdf/2610.28594) · [HF](https://huggingface.co/papers/2610.28594)

Reliable multi-view forecasting requires videos from different cameras to describe the same evolving 3D scene. To this end, we introduce Video-Point Model (VPM), a world model that conditions on multi-view video histories and a language instruction to jointly forecast future videos from arbitrary viewpoints and the 3D trajectories of persistent scene points. We extend a pretrained world model with camera-conditioned…

## 12. CoEvo-RSI: When Harnesses Evolve, Which Models Should Follow?

- 分数：30.0  ·  HF 赞：124  ·  来源：huggingface
- 兴趣命中：agent
- 作者：Jiaqi Su, Guibin Zhang, Jie-Jing Shao, Cong Pang, Tiankuo Yao, Ivor Tsang, Haiyan Yin, Shuicheng Yan
- 链接：[arXiv](https://arxiv.org/abs/2610.25078) · [PDF](https://arxiv.org/pdf/2610.25078) · [HF](https://huggingface.co/papers/2610.25078)

Model--harness co-evolution has emerged as a prominent paradigm for recursive self-improving (RSI) agents, jointly evolving their execution scaffolds and intrinsic capabilities. We study the persistent yet often overlooked brain--body mismatch problem in this paradigm, where an evolving harness (body) demands behaviors its model (brain) has not learned or restricts capabilities it already possesses. We introduce…

## 13. MMEnterprise-Bench: Evaluating Enterprise Agents over Evolving Multimodal Records

- 分数：29.0  ·  HF 赞：26  ·  来源：huggingface
- 兴趣命中：agent, reasoning, benchmark, retrieval
- 作者：Seohyun Lee, Jongha Kim, Dohwan Ko, Ji Soo Lee, Seoung Choi, Jayun Ku, Hyunwoo J. Kim
- 链接：[arXiv](https://arxiv.org/abs/2610.27911) · [PDF](https://arxiv.org/pdf/2610.27911) · [HF](https://huggingface.co/papers/2610.27911)

Enterprise agents answer questions over workplace records that evolve through team collaboration. As information is shared, corrected, and revised across documents, chats, and figures, multiple versions of the same information accumulate in the workspace. Reliable question answering therefore requires agents to reason over sufficient evidence, resolve cross-source and temporal conflicts, and recognize when the…

## 14. LLM2R: From Large Language Models to 3D Reassemblers

- 分数：27.0  ·  HF 赞：22  ·  来源：huggingface
- 兴趣命中：reasoning, language model, large language, spec
- 作者：Zhouhan Zhong, Qiuhong Shen, Xingyi Yang, Jinyi Xu, Xinchao Wang
- 链接：[arXiv](https://arxiv.org/abs/2610.18604) · [PDF](https://arxiv.org/pdf/2610.18604) · [HF](https://huggingface.co/papers/2610.18604)

3D part assembly aims to reconstruct a complete shape from a set of unassembled parts by predicting a rigid SE(3) transformation for each part. Because the placement of a part is rarely determined by its own geometry, the task demands reasoning over the entire part set, and existing methods, which rely on pairwise relations or iterative generation and verification, scale poorly to objects with many parts. We present…

## 15. Correction Training for Diffusion Models

- 分数：26.5  ·  HF 赞：37  ·  来源：huggingface
- 兴趣命中：-
- 作者：Donghoon Ahn, Runqian Wang, Alexei A. Efros, Taesung Park, Yash Belhe
- 链接：[arXiv](https://arxiv.org/abs/2610.14136) · [PDF](https://arxiv.org/pdf/2610.14136) · [HF](https://huggingface.co/papers/2610.14136)

Iterative sampling in diffusion models can lead to error accumulation due to exposure bias. The denoiser is trained on real images interpolated with noise, but at inference its inputs are constructed from its own imperfect predictions from the earlier steps, something it has never seen at training time. This might be one reason diffusion models often struggle without additional help, such as CFG. We introduce a…

## 16. Socratic Skill Learning: Interleaving Teaching and Practice for Transferable Agent Skills

- 分数：26.5  ·  HF 赞：25  ·  来源：huggingface
- 兴趣命中：agent, evaluation, spec
- 作者：Letian Zhu, Han Li, Yifan Yao, Xinping Lei, Xinyu Che, Jiahao Wang, Dianyi Wang, Yucheng Fu, Jiakai Wang, Zhiqi Bai, Wenbo Su, Jiaheng Liu
- 链接：[arXiv](https://arxiv.org/abs/2610.17860) · [PDF](https://arxiv.org/pdf/2610.17860) · [HF](https://huggingface.co/papers/2610.17860)

Agent Skills improve LLM agents by making task knowledge reusable across sessions. Learning transferable Skills requires evidence about a procedure and its conditions of use, which a successful task attempt can leave untested. We introduce Socratic Skill Learning (SSL), which interleaves expert teaching with Student practice. An Educator guides investigation while the Student remains the sole environment operator…

## 17. Memory-Centric Continual Learning for AI Agents

- 分数：26.5  ·  HF 赞：13  ·  来源：huggingface + arxiv
- 兴趣命中：agent, memory, evaluation, retrieval
- 作者：Dongfang Li, Zhuoen Chen, Bonian Jia, Zixuan Liu, Zhengxuan Lu, Can Deng, Yukun Shi, Yuhang Meng, Xin Zhang, Jiahe Huang, Fuhao Li, Junmai Wang, Shunyao Wen, Jingjun Sun, Jiaxu Tian, Jiangling Zhang, Zihan Wang, Liangyou Li, Yitong Yao, Shuangyong Song, Beilun Wang, Pengxu Wei, Hanlin Xu, Chang Liu, Yongxiang Li, Baotian Hu, Xiangyang Ji, Min Zhang
- 链接：[arXiv](https://arxiv.org/abs/2610.29357) · [PDF](https://arxiv.org/pdf/2610.29357) · [HF](https://huggingface.co/papers/2610.29357)

Autonomous agents powered by foundation models can reason, plan, and use tools, but their fixed weights and context limits hinder sustained learning from experience over long-term deployment. While external memory systems attempt to bridge this gap, they mostly act as passive retrieval caches, evaluated primarily by whether they can recall stored facts or past interactions. Whether memory can drive genuine continual…

## 18. Breaking Diffusion: Parallel Reasoning with Draft Refinement

- 分数：25.5  ·  HF 赞：19  ·  来源：huggingface
- 兴趣命中：reasoning, evaluation, language model, spec
- 作者：Jaesang Yu, Seoyeon Byun, Yun Wang, Yan Lu, Juho Kim
- 链接：[arXiv](https://arxiv.org/abs/2610.26542) · [PDF](https://arxiv.org/pdf/2610.26542) · [HF](https://huggingface.co/papers/2610.26542)

Drafting an answer allows a reasoning model to reconsider each decision in the context of the others. Yet repeated diffusion denoising does not ensure that individually plausible token updates form a better answer together. We introduce Draft Refinement Language Models (DRLMs), which use a single denoiser to propose parallel revisions and evaluate a candidate draft. We train the denoiser to reconstruct every token…

## 19. TraceForge: Distilling with Your Own Thinking

- 分数：25.5  ·  HF 赞：11  ·  来源：huggingface + arxiv
- 兴趣命中：reasoning, benchmark, coding, spec
- 作者：Yan Wang
- 链接：[arXiv](https://arxiv.org/abs/2610.29680) · [PDF](https://arxiv.org/pdf/2610.29680) · [HF](https://huggingface.co/papers/2610.29680)

Using an LLM to generate training data for another is among the most general ways to train one, and it remains common practice. Some frontier teams have closed that route for their own models: what comes back is an answer, or a short summary, without the detailed reasoning trace behind it. That is a little ironic: they were themselves built on distilling human knowledge, and distilling an open-source model is still…

## 20. SpecKCast: Spectral Kalman Forecasting for Diffusion Acceleration

- 分数：25.0  ·  HF 赞：22  ·  来源：huggingface
- 兴趣命中：memory, evaluation, spec
- 作者：Javad Rajabi, Hakki Can Karaimer, David B. Lindell, Babak Taati, Michael S. Brown
- 链接：[arXiv](https://arxiv.org/abs/2610.26837) · [PDF](https://arxiv.org/pdf/2610.26837) · [HF](https://huggingface.co/papers/2610.26837)

Diffusion Transformers (DiTs) achieve high-fidelity image and video generation, but they suffer from substantial inference costs due to repeated transformer evaluations across many denoising steps. Feature caching reduces this cost by reusing features across denoising steps. Recent forecasting methods extend this idea by extrapolating features to skipped steps instead of reusing them. However, existing forecasting…

## 21. Epi: Towards a Persistent, Self-Improving Agent for Autonomous Research

- 分数：25.0  ·  HF 赞：18  ·  来源：huggingface
- 兴趣命中：agent, memory, reasoning, benchmark, coding, planning
- 作者：Yue Huang, Zhangchen Xu, Xiaonan Luo, Zheyuan Liu, Lichi Li, Yiping Wang, Peiyang Song, Eric Gabriel Ramos, Enze Xie, Olexandr Isayev, Paul Liang, Nouha Dziri, Huan Sun, Jianfeng Gao, Ying Liu, Misha Sra, Xiangliang Zhang, Alex Pentland, Zichen Chen
- 链接：[arXiv](https://arxiv.org/abs/2610.24944) · [PDF](https://arxiv.org/pdf/2610.24944) · [HF](https://huggingface.co/papers/2610.24944)

We present Épi, an autonomous research agent that sustains investigations across model sessions and evolves its methods through accumulated experience. Épi combines persistent research history, hierarchical memory, branching and independent review to maintain research continuity, learn from experiments, and explore and revisit alternative approaches. Its experiments run across session boundaries, and a fixed…

## 22. EvaOmni: An Evidence-Grounded Benchmark for Audio-Visual Reasoning

- 分数：25.0  ·  HF 赞：18  ·  来源：huggingface
- 兴趣命中：reasoning, evaluation, benchmark, spec, retrieval
- 作者：Xiaoxing Hu, Wenxi Yao, Chaoyuan Shi, Ziqi Ye, Xiaorong Guo, Peixuan Li, Zhuoran Sun, Ziyang Gong, Peiyuan Zhang, Mingxin Liu, Shuran Ma, Hongbo Liu, Xiaomin Yu, Yu Tian, Wentao Wang, Zhenjie Yang, Jian Hu, Yunhang Shen, Haoyu Cao, Xue Yang
- 链接：[arXiv](https://arxiv.org/abs/2610.28444) · [PDF](https://arxiv.org/pdf/2610.28444) · [HF](https://huggingface.co/papers/2610.28444)

Omni LLMs can naturally locate key audio and visual evidence and integrate information across modalities for audiovisual reasoning. Existing audio-visual reasoning benchmarks that mainly rely on multiple-choice questions usually score models solely based on answer correctness, making it difficult to assess whether a model truly forms a reasoning chain from evidence to the correct answer. In addition, textual or…

## 23. Specter: Fast MoE Inference via Quantization-Enabled Multi-Step Speculative Offloading

- 分数：24.0  ·  HF 赞：20  ·  来源：huggingface
- 兴趣命中：memory, coding, spec
- 作者：Wenfeng Wang, Xiaofeng Hou, Xinfeng Xia, Xinkai WAng, Mingxuan Zhang, Peng Tang, Jiacheng Liu, Chao Li
- 链接：[arXiv](https://arxiv.org/abs/2511.14102) · [PDF](https://arxiv.org/pdf/2511.14102) · [HF](https://huggingface.co/papers/2511.14102)

Mixture-of-experts (MoE) models often exceed a single accelerator's memory capacity. Offloading experts to host memory creates a severe PCIe I/O bottleneck because data-dependent routing keeps transfers on the critical path. We present Specter, an inference system that uses quantization to combine speculative decoding with expert offloading. Its lightweight quantized draft model runs efficiently on device while…

## 24. AgenticRoboRL: Bringing Coding-Agent Post-Training to Agentic Robotics

- 分数：24.0  ·  HF 赞：16  ·  来源：huggingface
- 兴趣命中：agent, memory, reinforcement learning, coding, spec
- 作者：Xinxin Liu, Bingxin Xu, Wenrui Bao, Ming Li, Wentao Bao, Chen Chen, Yuzhang Shang
- 链接：[arXiv](https://arxiv.org/abs/2610.28589) · [PDF](https://arxiv.org/pdf/2610.28589) · [HF](https://huggingface.co/papers/2610.28589)

Agentic robotics systems combine planners with robot harnesses to perform complex manipulation tasks. Recent work improves these systems through better harnesses and external memory, but relies on powerful closed-source models as planners and does not improve the planners' own capabilities. In contrast, coding agents have improved substantially by post-training the model itself. We therefore investigate whether…

## 25. SWIFT: Self-guided Weak-to-strong dIFfusion models via Target extrapolation

- 分数：23.5  ·  HF 赞：27  ·  来源：huggingface
- 兴趣命中：spec
- 作者：Yanjin He, Cuifeng Shen, Wanzhou Lei, Maohua Li, Tao Lan, Kan Liu, Hanlin Tang, Qing Qu
- 链接：[arXiv](https://arxiv.org/abs/2610.25844) · [PDF](https://arxiv.org/pdf/2610.25844) · [HF](https://huggingface.co/papers/2610.25844)

Training high-quality diffusion models is computationally expensive, and inference-time guidance often adds further sampling cost. In this work, we introduce Swift, a simple yet effective self-guided training method that uses a frozen weak denoiser to improve a stronger model without adding inference overhead. For each noisy input, Swift extrapolates the clean regression target away from the weak denoiser's…

## 26. Looking Ahead: Modeling Future Evolution in Autoregressive Video Generation

- 分数：23.5  ·  HF 赞：23  ·  来源：huggingface + arxiv
- 兴趣命中：-
- 作者：Ruopeng Gao, Yukun Huang, Jiarui Hu, Shuai Wang, Wenbo Hu, Ying Shan, Limin Wang
- 链接：[arXiv](https://arxiv.org/abs/2610.29989) · [PDF](https://arxiv.org/pdf/2610.29989) · [HF](https://huggingface.co/papers/2610.29989)

Autoregressive video diffusion models generate videos chunk by chunk, yet producing plausible continuations does not guarantee that they capture how scenes evolve. Under teacher forcing, strong temporal redundancy may allow local visual continuity to serve as a shortcut for current-chunk denoising, reducing the pressure to model visual evolution. We introduce Future Chunk Prediction (FCP), an auxiliary objective…

## 27. FlowState: Execution State as Memory for Long-Horizon LLM Agents

- 分数：23.5  ·  HF 赞：15  ·  来源：huggingface
- 兴趣命中：agent, memory, reasoning, spec
- 作者：Minghao Li, Bangyan Li, Zifan Wang, Yulong Li, Hu Xu, Gan Zhang, Jingtong Wu, Wenqiang Xu
- 链接：[arXiv](https://arxiv.org/abs/2609.34565) · [PDF](https://arxiv.org/pdf/2609.34565) · [HF](https://huggingface.co/papers/2609.34565)

Long-horizon tasks require LLM agents to continually draw on information from earlier interactions. However, retaining the full history increases context costs, while compressing it risks losing details needed later, and the relevance of historical information often becomes apparent as the task progresses. To address these challenges, we propose FlowState, which treats execution state as memory that can be retained…

## 28. Event-STVG: Spatio-Temporal Video Grounding for Long-Form Event Reasoning

- 分数：23.5  ·  HF 赞：15  ·  来源：huggingface
- 兴趣命中：reasoning, benchmark, language model, large language, spec
- 作者：Yizhe Zhang, Xujia Wang, Songqi Tang, Xujie Tang, Leo Jiahao Jiang, Jiacheng Wang, Bowen Qu, JinBo Li, Qin Wang, Ji Qi, Lei Hou, Bin Xu, Juanzi Li
- 链接：[arXiv](https://arxiv.org/abs/2610.22444) · [PDF](https://arxiv.org/pdf/2610.22444) · [HF](https://huggingface.co/papers/2610.22444)

Spatio-Temporal Video Grounding (STVG) aims to jointly localize a target in space and time given a natural-language query. Despite continued advances, existing STVG benchmarks remain largely centered on localizing targets through instance-specific descriptions, leaving them largely decoupled from long-form reasoning increasingly emphasized in multimodal large language models (MLLMs). In this paper, we introduce…

## 29. DecisionPivot: A Diagnostic Benchmark for Decision Models in LLM Systems

- 分数：23.5  ·  HF 赞：15  ·  来源：huggingface
- 兴趣命中：reasoning, evaluation, benchmark, spec
- 作者：Xialie Zhuang, Mingcong Lei, Zunhai Su, Ri Liu, Jianjin Li, Peixian Ma, Jia Pan, Ngai Wong, Guanhua Chen, Chuan-Wei Kuo
- 链接：[arXiv](https://arxiv.org/abs/2610.28522) · [PDF](https://arxiv.org/pdf/2610.28522) · [HF](https://huggingface.co/papers/2610.28522)

Decision models support routing, guardrails, and output verification in LLM systems. However, item accuracy alone cannot establish whether models make correct decisions across controlled variations or assign reliable confidence to their predictions. We introduce DecisionPivot, a diagnostic benchmark comprising 48 tasks and 40,033 items across seven decision roles. Its core track contains 7,800 items from 13…

## 30. Multimodal Embodied Agents: A Unified Capability-centric Perspective from Computer-Use to Robot-Use

- 分数：23.5  ·  HF 赞：7  ·  来源：huggingface + arxiv
- 兴趣命中：agent, memory, reasoning, evaluation, benchmark, spec
- 作者：Yanzhe Chen, Ziyi Yang, Jifeng Zhu, Qiming Huang, Ruihe An, Peiyao Xu, Hesen Yang, Runda Liu, Chang Gong, Zhijun Cao, Zechen Bai, Wenzheng Zeng, Yiqi Lin, Guoqiang Liang, Kevin Yuchen Ma, Kevin Qinghong Lin, Mike Zheng Shou
- 链接：[arXiv](https://arxiv.org/abs/2610.30108) · [PDF](https://arxiv.org/pdf/2610.30108) · [HF](https://huggingface.co/papers/2610.30108)

Multimodal agents (MMAs) sustain interaction through reasoning, memory, tools, and feedback, most visibly as computer-use agents, while robotic systems (RSs) couple sensing and actuation under physical dynamics. We define multimodal embodied agents (MMEAs) as goal-directed systems that couple multimodal task reasoning with physical action and revise decisions from the resulting feedback. This raises a central…

## 31. Joints, Camera, Action! Co-Generating 3D Motion and Video for Arbitrary Rigs

- 分数：23.0  ·  HF 赞：22  ·  来源：huggingface
- 兴趣命中：evaluation, spec
- 作者：Noam Rotstein, Yoad Tewel, Chen Tessler, Haggai Maron, Gal Chechik, Or Litany, Yoni Kasten, Yuval Atzmon
- 链接：[arXiv](https://arxiv.org/abs/2610.28632) · [PDF](https://arxiv.org/pdf/2610.28632) · [HF](https://huggingface.co/papers/2610.28632)

Video generation models can now depict remarkably realistic motion. Yet it is unclear how to use this motion beyond pixels: to animate a specific 3D asset and replay the animation in its 3D scene. For instance, a video model can show a monkey jumping over a crossbar, but it cannot return that jump as replayable 3D motion placed in the 3D scene. Here we present a model that directly co-generates the video and 3D…

## 32. EdgeKernelBench: Unified LLM-Driven Kernel Generation for Edge Backends

- 分数：22.5  ·  HF 赞：13  ·  来源：huggingface
- 兴趣命中：agent, memory, evaluation, benchmark
- 作者：Yuhua Zheng, Xueyi Chen, Xinze Zou, Xin Li, Haoji Hu, Huan Wang
- 链接：[arXiv](https://arxiv.org/abs/2610.24648) · [PDF](https://arxiv.org/pdf/2610.24648) · [HF](https://huggingface.co/papers/2610.24648)

Recent works show that LLMs can generate kernels with strong performance on server GPUs. Edge deployment presents distinct challenges because the hardware is heterogeneous, the software stacks are fragmented, and the resource budgets are tight. LLM kernel generation across diverse edge backends has yet to be studied systematically. We introduce EdgeKernelBench, which combines a unified IR deployment framework with a…

## 33. Harness Scaling for Generalizable Agentic Reinforcement Learning

- 分数：22.5  ·  HF 赞：5  ·  来源：huggingface + arxiv
- 兴趣命中：agent, reinforcement learning, benchmark, spec
- 作者：Fei Bai, Huatong Song, Chuan Hao, Ran Tao, Jian Yang, Bryan Dai, Wayne Xin Zhao, Ji-Rong Wen
- 链接：[arXiv](https://arxiv.org/abs/2610.29458) · [PDF](https://arxiv.org/pdf/2610.29458) · [HF](https://huggingface.co/papers/2610.29458)

Agent harnesses have become a central component of modern agentic systems, shaping how models use tools, manage context, and coordinate long-horizon interaction. Realizing the benefits of these harnesses depends on how effectively the underlying model can make use of them, motivating reinforcement learning directly through the harness. However, existing approaches typically train through a single fixed harness,…

## 34. Evolving Agent Interfaces

- 分数：21.5  ·  HF 赞：19  ·  来源：huggingface
- 兴趣命中：agent, spec
- 作者：Saaket Agashe, Yuzhe Yang, Gonzalo Gonzalez-Pumariega, Bhuvan Chandra Koduru, Chih-Lun Li, Jiachen Yang, Ang Li, Xin Eric Wang
- 链接：[arXiv](https://arxiv.org/abs/2610.28601) · [PDF](https://arxiv.org/pdf/2610.28601) · [HF](https://huggingface.co/papers/2610.28601)

Computer-use agents are limited by the interfaces humans give them. An agent may type a spreadsheet cell by cell when a single line of code would do, or print all two thousand lines of a file through a shell to find one function. Both the interfaces and the knowledge of when to use each are built by hand, which cannot keep pace with new applications, workflows, and models. We argue that interface design should…

## 35. Harness Self-Evolution for Long-Horizon Terminal Agents

- 分数：21.5  ·  HF 赞：11  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark, spec
- 作者：Ruhan Wang, Yucheng Shi, Zongxia Li, Junyao Yang, Zhongzhi Li, Yue Yu, Haitao Mi, Dongruo Zhou, Leoweiliang
- 链接：[arXiv](https://arxiv.org/abs/2610.27435) · [PDF](https://arxiv.org/pdf/2610.27435) · [HF](https://huggingface.co/papers/2610.27435)

Long-horizon terminal agents may solve a task in one run yet fail across repeated runs. Stochastic errors can propagate through actions and context, creating a gap between capability and reliable execution. We present RiseHarness, a framework for iteratively improving agent harnesses with model weights fixed. It focuses on flipping tasks with both successful and failed runs under the same configuration, using…

## 36. Large Flow Language Models

- 分数：21.5  ·  HF 赞：11  ·  来源：huggingface
- 兴趣命中：reasoning, language model, coding, spec
- 作者：Arnav Chavan, Chanhyuk Lee, Udbhav Bamba, Jaehoon Yoo, Seunghoon Hong, Aditi Raghunathan, Jinwoo Kim
- 链接：[arXiv](https://arxiv.org/abs/2610.28559) · [PDF](https://arxiv.org/pdf/2610.28559) · [HF](https://huggingface.co/papers/2610.28559)

Continuous flow language models offer a path to parallel generation with tools for control and acceleration unavailable to discrete diffusion, yet effective techniques for building them at the billion-parameter scale remain less established. We present Lafa (Large flow language model), a fast, high-performing flow language model scaled to 8B parameters in a data-efficient manner. Lafa is a blockwise flow model with…

## 37. From Short Clips to Real-Time Streams: Identity-Aware Supervision and Context-Efficient Generation for Video Face Swapping

- 分数：20.5  ·  HF 赞：17  ·  来源：huggingface
- 兴趣命中：evaluation, spec
- 作者：Zekai Luo, Yuwei Liang, Ruiqi Ma, Haoyu Huang, Xuehao Wang, Huanyi Zheng, Mingyu Liu, Linhao Zhong, Chenchen Jing, Yuling Xi, Hao Chen
- 链接：[arXiv](https://arxiv.org/abs/2610.26681) · [PDF](https://arxiv.org/pdf/2610.26681) · [HF](https://huggingface.co/papers/2610.26681)

Video face swapping transfers the reference identity to a target video while preserving its other attributes and motion. Despite recent progress in reference-guided flow-based methods, jointly achieving faithful identity transfer, high fidelity, and real-time generation over long video streams remains challenging. To address this challenge, we rethink the task-specific structure of reference-guided video face…

## 38. HybridResearcher: Bridging the Structured-Unstructured Boundary for Deep Research Agents

- 分数：20.5  ·  HF 赞：9  ·  来源：huggingface
- 兴趣命中：agent, reasoning, reinforcement learning, evaluation, benchmark
- 作者：Soyoung Yoon, Peiran Xu, Han Wang, Ruofan Wu, Xiaodong Yu, Feng Yan, Mohit Bansal, Debiao Li, Seung-Won Hwang, Yuxiong He, Zhewei Yao
- 链接：[arXiv](https://arxiv.org/abs/2610.24899) · [PDF](https://arxiv.org/pdf/2610.24899) · [HF](https://huggingface.co/papers/2610.24899)

While LLM agents are increasingly capable of gathering and synthesizing evidence from a single homogeneous source, such as structured tables or unstructured data, real-world analytical questions frequently span heterogeneous sources. For example, answering one enterprise question may require both a result computed over an internal database and evidence found on the web. Recent evaluations on benchmarks like…

## 39. Building AI Research Teams for Autonomous Discovery of Linear Attention Architectures

- 分数：20.5  ·  HF 赞：9  ·  来源：huggingface
- 兴趣命中：agent, reasoning, language model, retrieval
- 作者：Yujian Liu, Li An, Zelin He, Jacob Helwig, Jiabao Ji, Rohit Jain, Siyu Zhu, Shiyu Chang
- 链接：[arXiv](https://arxiv.org/abs/2610.28887) · [PDF](https://arxiv.org/pdf/2610.28887) · [HF](https://huggingface.co/papers/2610.28887)

Autonomous agents can increasingly propose ideas, modify code, and run experiments, creating an opportunity to accelerate scientific discovery using teams of collaborative AI researchers. To escape local minima in the discovery, we propose to encourage orthogonal exploration by constructing the team using agents with varying expertise. However, realizing this design requires more than diverse backgrounds. When…

## 40. Training the Whole Agent, Not Just the Model

- 分数：20.5  ·  HF 赞：9  ·  来源：huggingface
- 兴趣命中：agent, reinforcement learning, evaluation, coding, spec
- 作者：Lingxiao Tang, Wei Tao, Yiwen Guo, Lingfeng Bao
- 链接：[arXiv](https://arxiv.org/abs/2610.28069) · [PDF](https://arxiv.org/pdf/2610.28069) · [HF](https://huggingface.co/papers/2610.28069)

Training coding agents typically updates the policy while keeping the harness fixed. During training, trajectories reveal flawed repair strategies and interaction problems that vary across tasks and change as the policy learns. We introduce HarnessAdapt-RL, which trains the policy and adapts its harness during reinforcement learning. For flawed repair strategies, a frozen teacher generates task-specific…

## 41. CulturalRiddles: A Multicultural Benchmark of Riddles

- 分数：20.5  ·  HF 赞：1  ·  来源：huggingface + arxiv
- 兴趣命中：reasoning, evaluation, benchmark, spec
- 作者：My Chiffon Nguyen, Tianyi Hu, Vinod Anbalagan, Henry Gagnier, Pouya Sadeghi, Farah Abdou, Tidor-Vlad Pricope, Diego MMS Oliveira, Jocelyn K D&#39;Arcy, Madeline Smith, Oluwaseun A Ajayi, Yusser Al Ghussin, Zena Al-Khalili, Micol Altomare, Shayan Amir, Ahanaf Aziz, Bryan Chen, Ruchira Dhar, Abdellah El Mekki, Rawan Mohammed Elframawy, Akhil Eppa, Silvia Fernandez, Alex Gimei, Arya Hariharan, Christian Hoang, RamMohanRao Kadiyala, Diana Kozachek, Peerat Limkonchotiwat, Ankita Maity, Di Mo, Ayush Munot, Aylin Naebzadeh, Anastasiia Nikitina, Dina Pisarevskaya, Divas Poudel, Jebish Purbey, Md Rabius Sany Apu, Ahmad Mufli Ramadhan, Ralitza Nikolova Rizova, Diogo M. Serrano-Miranda, Vivek Gopalkrishna Silimkhan, Luis Fernando Solis Navarro, Kaiser Sun, Arya Suneesh, Manaswitha Sunkara, Tejaswi Sunkara, Jonathan E Swindell, Hanna Yukhymenko, Jingyi Zheng, Esther Adenuga, Ilia Afanasev, Wafa Aissa, Lisa Alazraki, Lauren C Altomare, Priscilla Amondi Amuok, Emile Anand, Gabriel Assis, José Matías Avalos, Silvia Lorena Avila, Zakaria Baannou, Niyati Bafna, Yash Bagla, Sarah Bahrami, Bontu F Balcha, Vanya Bannihatti Kumar, Irene Baucells, Abdumutalib Begmuratov, Naman Bhatia, Souvik Bhattacharyya, Isabel Blanco Ferreiro, Felipe Bochini, Sayuru Bopitiya, Angana Borah, Tulika Bose, Olena Bugaiova, Juliana Carvalho, Nancy F Chen, Stephy Chen, Rochelle Choenni, Jayanth Krishna Chundru, Leandro A Cossio, Nebojša Damnjanović, Ona de Gibert, Marco De Santis, Pedro Delgado, Kaustubh Dholé, Adnan El Assadi, Wesam El-Sayed, Nadine M Elframawy, Oumayma Essarhi, Naome A Etori, Reuben Chagas Fernandes, Saanidhi Pravin Gade, Javier García Gilabert, Álvaro González-Escapa, Bin Hu, Kaiyu Huang, Abderrahmane Issam, Danka Jokić, Ulugbek Khalilov, Dominik Krzemiński, Roy Ka-Wei Lee, Haichang Li, Chen Cecilia Liu, Zhengyuan Liu, Cedric Lothritz, Houman Mehrafarin, Antonio Miranda-Escalada, Fengran Mo, Mehrnaz Mofakhami, Wafaa Mohammed, Felipe Moreno-Vera, Prahitha Movva, Jannatul Nayem, Van Ngo, Joy Olusanya, Marc Pàmies, Avinash Kuney Pandey, Yurii Paniv, Fred Philippy, Vladislav Poritski, Dikshya Poudel, Joanna Radoła, Sara Rajaee, Swati Rajwal, Prerana Rane, Muhammad Ravi Shulthan Habibi, Lucas Resck, Shubhashis Roy Dipta, Ananya Sahu, Eduardo Sánchez, Borja Sánchez Clemente, Aleix Sant, Nobin Sarwar, Istiak Shihab, Santhoshini Pranathi Singaraju, Jane Smith, David Stap, Emily Z Su, Ananth K Suresh, Sajag Swami, Ruiyang Tan, Nazia Tasnim, Khalid Tounoussi, Patteera Triamamornwooth, Muhammad Saad Umar, Shankar Venkitachalam, Oksana Volchek, Lingbo Wang, Debela Desalegn Yadeta, Rushikesh Zawar, Jinghan Zhang, Mike Zhang, Weihua Zheng, Marzieh Fadaee, Akhil Arora, Károly Boczka, Julia Kreutzer
- 链接：[arXiv](https://arxiv.org/abs/2610.29968) · [PDF](https://arxiv.org/pdf/2610.29968) · [HF](https://huggingface.co/papers/2610.29968)

As LLMs expand their language coverage, evaluating how well they understand and represent diverse cultures becomes increasingly important. However, many benchmarks remain English-centric, with limited cultural coverage and a focus on factual knowledge over its application in real-world cultural contexts. We propose CulturalRiddles, a benchmark of original, culturally grounded riddles created entirely by humans…

## 42. HarnessRL: Co-Evolving Policies with a Just-in-Time Training Harness for Open-Ended RL

- 分数：20.0  ·  HF 赞：12  ·  来源：huggingface
- 兴趣命中：memory, reinforcement learning, evaluation
- 作者：Xiaoqiang Wang, Ting-En Lin, Yuchuan Wu, Pinyi Zhang, Caixin Kang, Ling Li, Bingxue Qiu, Jieping Ye, Yongbin Li, Bang Liu
- 链接：[arXiv](https://arxiv.org/abs/2610.26426) · [PDF](https://arxiv.org/pdf/2610.26426) · [HF](https://huggingface.co/papers/2610.26426)

Rubric-based reinforcement learning (RL) trains policies for open-ended generation with natural-language criteria as rewards, but these rewards can become ineffective as training progresses. We identify two failure modes. Under non-discriminative rewards, scores collapse to uniformly low or high values due to insufficient exploration or a mismatch between task difficulty and policy capability. Under spurious…

## 43. Scaling in Games: Continued Pre-Training For Embodied Agents In Diverse Virtual Worlds

- 分数：20.0  ·  HF 赞：12  ·  来源：huggingface
- 兴趣命中：agent, benchmark, spec
- 作者：Kuan Zhang, Yukun Chen, Zhihao Yang, Yue Su, Xiangnan Wu, Zirong Chen, Run Luo, Jinkun Hou, Tao Tan, Yinhe Zheng, Yiming Li
- 链接：[arXiv](https://arxiv.org/abs/2610.28698) · [PDF](https://arxiv.org/pdf/2610.28698) · [HF](https://huggingface.co/papers/2610.28698)

Scaling data, diversity and model capacity has improved embodied learning in physical environments, where diverse experiences remain grounded in shared physical laws. Whether these gains extend to virtual worlds with different visual styles, dynamics, controls, and objectives remains unclear. We investigate this question through a controlled study of continued pre-training (CPT) across three axes: data volume,…

## 44. More Memory, Worse Agents: Error Reproduction and Anti-Persistence in LLM Agents

- 分数：20.0  ·  HF 赞：8  ·  来源：huggingface
- 兴趣命中：agent, memory, benchmark, spec, retrieval
- 作者：Ruhan Wang, Kishan Panaganti, Dongruo Zhou
- 链接：[arXiv](https://arxiv.org/abs/2610.27406) · [PDF](https://arxiv.org/pdf/2610.27406) · [HF](https://huggingface.co/papers/2610.27406)

LLM agents can improve across tasks without updating model parameters by storing experience from their own executions in external memory and reusing it to guide later decisions. A central design question is whether to retain only observed trajectories and outcomes or also the rules, summaries, and skills inferred from them. Retaining these abstractions allows agents to reuse strategies without repeatedly deriving…

## 45. ALPS: Visual State Encoders for World Models

- 分数：20.0  ·  HF 赞：4  ·  来源：huggingface + arxiv
- 兴趣命中：evaluation, spec, planning
- 作者：Yanqing Liu, Letian Zhang, Chengzhi Liu, Zijun Wang, Jieru Mei, Hongliang Fei, Yuyin Zhou, Cihang Xie
- 链接：[arXiv](https://arxiv.org/abs/2610.30120) · [PDF](https://arxiv.org/pdf/2610.30120) · [HF](https://huggingface.co/papers/2610.30120)

World models turn visual representations into predictions and actions. We argue that their visual foundation should combine physical-state information, native language alignment, and pixel reconstruction, so that a single representation can support prediction, instruction, and inspection. However, existing encoders typically specialize in only one or two of these capabilities; we therefore introduce ALPS, a…

## 46. Unsupervised Tool Evolution for Coding Agents in Data-Lake Analytics

- 分数：19.5  ·  HF 赞：11  ·  来源：huggingface
- 兴趣命中：agent, benchmark, coding
- 作者：Yuqing Yang, Yurong Liu, Deqing Fu, Manav Garg, Sravan Babu Bodapati, Fatma Ozcan, Alon Y. Halevy, Jiani Zhang
- 链接：[arXiv](https://arxiv.org/abs/2610.27327) · [PDF](https://arxiv.org/pdf/2610.27327) · [HF](https://huggingface.co/papers/2610.27327)

Coding agents can answer analytical questions over a data lake by discovering, cleaning, and joining the relevant data. However, they discard this work after each question and redo it from scratch for the next one. Tool evolution, which automatically builds and refines reusable tools across tasks, is a natural fit for this repetition. Since a ground-truth label for a data-lake question requires an expert to solve it…

## 47. Muse Glimmer 30B: An On-Device Agentic Model

- 分数：19.5  ·  HF 赞：7  ·  来源：huggingface
- 兴趣命中：agent, tool use, reasoning, benchmark, language model, planning
- 作者：Arash Ebrahim Abtahizadeh, Muna Aghamelu, Adil Ahmed, Juan C. Angeles Acuna, Alexis Audran-Reiss, Asaf Avrahamy, Yoram Bachrach, Can Balioglu, Amar Budhiraja, Onur Çelebi, Gaurav Chaurasia, Joy Chen, Lynn Cherif, Lucia Cipolina-Kun, Gal Cohen, Timothée Darcet, Beto de Paola, Digant Desai, Sam Devlin, Derek Dunfield, Ivan Evtimov, Maryam Fazel-Zarandi, Rob Fergus, Jean-Christophe Gagnon-Audet, Grant Gardner, Bhavul Gauri, Paris Giampouras, Sujan Kumar Gonugondla, Antoine Grosnit, Young Han, Michael Hassid, Monuril Islam, Masoud Jalili Sabet, Songhao Jia, Narine Kokhlikyan, Svetlana Kurtsman, Sandra Lefdal, Chee Hau Leow, Noam Levi, Mike Lewis, Sanae Lotfi, Xiyang Luo, Despoina Magka, Saeed Mahloujifar, Neal Mangaokar, Ishita Mediratta, Alexander H. Miller, Hela Momand, Saba Nazir, Kelvin Niu, Mattia Opper, Parth Pathak, Alberto Pepe, Danielle Pintz, Mikhail Plekhanov, Sidhartha Reddy Potu, Anton Protopopov, Shengyi Qian, Shashank Rajput, Joseph Rocca, Scott Roy, Luca Sbordone, Amin Shakeri, Tatiana Shavrina, Michael Shvartsman, Ruan Silva, Anya Sims, Eric Michael Smith, Hugo Touvron, Mabel Ubong, Isabel Urrego, Yanzheng Xiang, Zhiyuan Yao, Alex Yarmula, He Ye, Jade Yu, Luke Zettlemoyer, Arman Zharmagambetov, Perpetua Fathima Ahlijah, Tremo Ahmed, Enrique Alfonseca, Pedram Bashiri, Nikolay Bashlykov, Aaron Berman, Rohith Bhatia, Siddharth Bhattacharya, Prashant Bhende, Chloe Bi, Shuchao Bi, Clement Anthonioz Blanc, Allen Bolourchi, Andrea Caciolai, Erica Cai, Xiang Tony Cao, Yue Cao, Andrew Caples, Jinzhao Chang, Lele Chen, Moya Chen, Weijie Chen, Wenhu Chen, Xiaobai Chen, Yinyin Chen, Zhengxing Chen, Wei Cheng, Pavel Chikulaev, Edward Chou, Sy Choudhury, Brian Clerkin, Marta R. Costa-jussà, Curtis Davis, Myra Deng, Dujian Ding, Hantian Ding, Shuangrui Ding, Jesse Dodge, Shweta Doshi, Shirin Eghtesadi, Faith Eischen, Athyu Eleti, Alex Fabbri, Han Fang, Paula Farani, Aiman Farooq, Christoph Feichtenhofer, Darius Feher, Amanda Felix, Carl Chengyan Fu, Sean Gahagan, Yifan Gao, Itai Gat, Akashdeep Goel, Ahuva Goldstand, Bo He, David Heineman, Dylan Herman, Irene Hjelt, Joonas Hjelt, Alexander Holz, Rui Hou, Annie Hu, Yuan-Ting Hu, Bernie Huang, Jing Huang, Kun Huang, Pere-Lluís Huguet Cabot, Ashley Hunter, Srinivasan Iyer, Somya Jain, Michael Jiang, Song Jiang, Wenwen Jiang, Lin Jin, Jacob Kahn, Melanie Kambadur, Yingxin Kang, Justine Kao, Stephane Kasriel, Hossein Kavianihamedani, Ameya Khandekar, Yash Khare, Gefen Kohavi, Kavya Kopparapu, Praveen Krishnan, Venu Kuchibhotla, Ananya Kumar, Leona Lan, Jack Lanchantin, Hunter Lang, Nikolay Pavlovich Laptev, Yuanzhi Li, Yunlu Li, Asad Liaqat, Johnson Lin, Runwei Lin, Zhichao Lin, Shaun Lindsay, Yaron Lipman, Frederick Liu, Mengchen Liu, Qiang Liu, Yinghai Lu, Yujie Lu, Christopher Luc, Faye Ma, Pingchuan Ma, Tengyu Ma, Wufei Ma, Xiaodong Ma, Damir Maksyutov, Josh Malone, Udeep Manchanda, Thomas Mann, Kalyani Marathe, Roberto-Rafael Maura-Rivero, Ruslan Mavlyutov, Thomas Mesnard, Julian Michael, Sagar Miglani, Todor Mihaylov, Naureen Mitha, Archi Mitra, Leo Mok, Naila Murray, Muthukumaravel Muthuraman, Mergen Nachin, Nese Demir Nalci, Saaketh Narayan, Alyssa Newcomb, Peter Ney, Joycelyn Ng, Devin Norder, Maxwell Nye, Rajvardhan Oak, Cody Ohlsen, Artidoro Pagnoni, Yi Pan, Nilesh Pandey, Guan Pang, Richard Yuanzhe Pang, Mahesh Pasupuleti, Parth Patel, Yash Patel, Vladan Petrovic, Norman Ponte, Yundi Qian, Zengyi Qin, Jack Rae, Emmanuel Ramirez, Ramya Raghavendra, Nikhila Ravi, Hongyu Ren, Riandy Riandy, Harrison Rudolph, Kalyan Saladi, Eduardo Sánchez, Karthik Abinav Sankararaman, Aman Shankar, Paresh Shenoy, Alana Shine, Hamid Shojanazeri, Iva Simon-Bubalo, Mitesh Kumar Singh, Tiffany Siqi, Pawan Sisodiya, Ali Sol, Sten Sootla, Leslie St. Pierre, DiJia Su, Suraj Subramanian, Brian Sun, Tony Sun, Zhiqing Sun, Natacha Supper, Jason Talpalar, Ellen Xiaoqing Tan, Liang Tan, Jean-Christophe Testud, Parth Thakkar, Joseph Tighe, Ty Toledano, T Tse, Igor Tufanov, Alex Vaughan, Josh Walters, Alex Wang, Bethany Wang, Meng Wang, Rocky Wang, Weiyue Wang, Xiaolan Wang, Xin Wang, Zijian Wang, Bram Wasti, Quentin Wellens, Yeming Wen, Mary Williamson, Yuncheng Wu, Fei Xia, Tian Xie, David Xu, Jacob Xu, Puxin Xu, Zheng Xu, Shen Yan, Megan Yang, Yining Yang, Nick Yannopoulos, Kevin Yao, Michihiro Yasunaga, Haoxuan You, Michael You, Dingli Yu, Tianhe Yu, Summer Yue, Xiang Yue, Shuwei Zeng, Hanwen Zha, Chen Zhang, Hongming Zhang, Kaiyu Zhang, Meng Zhang, Mingyang Zhang, Yi Zhang, Shengjia Zhao, Chao Zhou, Claire Zhou, Shuyan Zhou, Yanjun Zhou, Yaxuan Zhou, Rosalie Zhu, Yun Zhu
- 链接：[arXiv](https://arxiv.org/abs/2610.24628) · [PDF](https://arxiv.org/pdf/2610.24628) · [HF](https://huggingface.co/papers/2610.24628)

We introduce Muse Glimmer, an open-source 30B parameter causal language model with perception encoder, purpose-built for autonomous agentic tasks on consumer hardware. Muse Glimmer integrates multi-step reasoning, reliable tool use and failure recovery into a single model that runs locally on consumer devices without requiring cloud infrastructure. The model accepts text and image inputs and produces text outputs,…

## 48. PVBench: Quantifying Physical Plausibility in Video Generation with Object-Level Physical Measurements

- 分数：19.0  ·  HF 赞：6  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark, language model, spec
- 作者：Kaiwei Chen, Moran Li, Zhenye Gan, Yabiao Wang, Chengjie Wang, Kexin Zhang, Yong Liu, Jiangning Zhang
- 链接：[arXiv](https://arxiv.org/abs/2610.26711) · [PDF](https://arxiv.org/pdf/2610.26711) · [HF](https://huggingface.co/papers/2610.26711)

Recent video generation models produce visually compelling outputs, yet their physical plausibility remains poorly measured. Physical plausibility asks whether generated objects obey geometry, kinematics, dynamics, and conservation laws. Existing benchmarks rely on coarse visual-language model judgments or target embodied world models rather than video generation itself. We introduce PVBench, a physical video…

## 49. Painting Change Map as guidance for generating painting processes

- 分数：18.5  ·  HF 赞：17  ·  来源：huggingface
- 兴趣命中：benchmark
- 作者：Markus Pobitzer, Chang Liu, Niccolò Biondi, Nicu Sebe
- 链接：[arXiv](https://arxiv.org/abs/2610.25369) · [PDF](https://arxiv.org/pdf/2610.25369) · [HF](https://huggingface.co/papers/2610.25369)

Digital art generation has undergone a massive paradigm shift, moving from static image synthesis to dynamic video generation that can mimic the human painting process. While existing models can synthesize visually stunning time-lapses of paintings being created or "unpainted," they largely treat the creative process as a black box. Current conditioning mechanisms are either too rigid, relying on static geometric…

## 50. PhysSkin++: Real-Time and Generalizable Physics-Based Animation via Self-Supervised Neural Skinning

- 分数：18.5  ·  HF 赞：17  ·  来源：huggingface
- 兴趣命中：spec
- 作者：Yuanhang Lei, Baofei Liu, Xingxuan Li, Tao Cheng, Zixuan Wang, Boming Zhao, Yujun Shen, Siyuan Huang, Ruizhen Hu, Peter Yichen Chen, Hujun Bao, Zhaopeng Cui
- 链接：[arXiv](https://arxiv.org/abs/2610.26067) · [PDF](https://arxiv.org/pdf/2610.26067) · [HF](https://huggingface.co/papers/2610.26067)

Generalizing real-time physics-based animation across diverse 3D shapes and spatial discretizations remains challenging. In this paper, we introduce PhysSkin++, a physics-informed framework that learns continuous neural skinning fields from static geometries to construct compact deformation subspaces. Specifically, we propose a Neural Skinning Fields Autoencoder that predicts shape-dependent deformation subspaces…

## 51. Evaluating Agentic Capabilities Before Post-Training: An End-to-End Approach

- 分数：18.5  ·  HF 赞：9  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark
- 作者：Jiarui Qin, Junjie Huang, Yunjia Xi, Di Yin, Yong Yu, Weinan Zhang, Xing Sun, Weiwen Liu
- 链接：[arXiv](https://arxiv.org/abs/2610.19425) · [PDF](https://arxiv.org/pdf/2610.19425) · [HF](https://huggingface.co/papers/2610.19425)

Agentic capabilities are increasingly important for modern LLMs, yet remain difficult to evaluate during pretraining. Existing approaches typically rely on static trajectory-derived tasks or likelihood-based proxies, which are lightweight but provide limited visibility into how base models behave in interactive environments. We introduce ASAP (Agent Scaffold Adaptation for Pretraining Evaluation), a lightweight…

## 52. Multimodal Reranking Is a System One Decision

- 分数：18.5  ·  HF 赞：5  ·  来源：huggingface
- 兴趣命中：benchmark, language model, spec, retrieval
- 作者：Zhuchenyang Liu, Yao Zhang, Yu Xiao
- 链接：[arXiv](https://arxiv.org/abs/2610.28435) · [PDF](https://arxiv.org/pdf/2610.28435) · [HF](https://huggingface.co/papers/2610.28435)

Multimodal rerankers are usually dedicated models: a vision-language model (VLM) is trained on retrieval data to score the candidates of a query. Scoring options is not specific to reranking. System One decision models such as Jev map a state and a typed question to one probability per option without generating text, and general models can make such decisions with little or no training. Reranking is one such…

## 53. Evolving with Open Worlds: Towards Recursive Self-Improvement for Future Forecasting

- 分数：18.5  ·  HF 赞：1  ·  来源：huggingface + arxiv
- 兴趣命中：agent, reasoning, evaluation
- 作者：Zhipeng Chen, Yunsen Liang, Yanxi Chen, Hongkang Zhao, Lingyun Feng, Ruiyang Ren, Guoxin Chen, Jia Deng, Feng Chang, Chuan Hao, Ran Tao, Jian Yang, Ji-Rong Wen, Bryan Dai, Wayne Xin Zhao
- 链接：[arXiv](https://arxiv.org/abs/2610.29784) · [PDF](https://arxiv.org/pdf/2610.29784) · [HF](https://huggingface.co/papers/2610.29784)

Most contemporary artificial intelligence (AI) systems are released with frozen parameters and improve through external updates, whereas an ideal system would keep improving from its own experience, a capacity we call recursive self-improvement (RSI). Yet studying RSI requires an environment that is continuously changing, objectively verifiable, and naturally grounded, posing a fundamental challenge for agent…

## 54. Good Judgment, Bad Advice: Decision-Model Controllers Raise Agent Cost Without Improving Success

- 分数：18.0  ·  HF 赞：12  ·  来源：huggingface
- 兴趣命中：agent, spec
- 作者：Naman Vats
- 链接：[arXiv](https://arxiv.org/abs/2610.24649) · [PDF](https://arxiv.org/pdf/2610.24649) · [HF](https://huggingface.co/papers/2610.24649)

Agent scaffolds increasingly delegate small decisions (whether to stop, verify, or change approach) to cheaper models. We ask whether a typed decision model, Jev 1.13, consulted only at deterministic decision points, makes a Claude Sonnet 5.5 terminal agent cheaper without making it worse. In a pre-specified study on Terminal-Bench 2.1, we hold one agent loop fixed and vary only the controller: none, deterministic…

## 55. On the Fragility of Tasks under Composition: Implicit Budgeting in Language Models

- 分数：18.0  ·  HF 赞：8  ·  来源：huggingface
- 兴趣命中：context window, reasoning, language model
- 作者：Chenpan Li, Thies Brockmoeller, Stefanie Jegelka, Sharut Gupta, Nikolaos Karalias
- 链接：[arXiv](https://arxiv.org/abs/2610.27190) · [PDF](https://arxiv.org/pdf/2610.27190) · [HF](https://huggingface.co/papers/2610.27190)

Modern language models are increasingly asked to handle several tasks within a single prompt. Doing so requires solving each task correctly while integrating the resulting answers into a coherent response. In this paper, we identify a fundamental limitation in this process, where models make substantially more errors when tasks are composed, even when they can solve every constituent task reliably in isolation. This…

## 56. On the Tip of the Tongue: First-Token Cueing as a Behavioral Probe of Recall Failures in LLMs

- 分数：18.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：reasoning, benchmark, language model, large language, coding
- 作者：Jaewon Sok, Jewon Yeom, Seonghyeon Park, Jeongjae Park, Hwiyeong Lee, Taesup Kim
- 链接：[arXiv](https://arxiv.org/abs/2610.23400) · [PDF](https://arxiv.org/pdf/2610.23400) · [HF](https://huggingface.co/papers/2610.23400)

Large language models often answer factual questions incorrectly in closed-book settings, and such errors are usually attributed to missing knowledge. Yet models often encode answers they fail to produce. We show that many closed-book errors are first-token recall failures: the model commits to a wrong first token, but once given the right one it completes the answer and often recognizes it as correct. We study this…

## 57. HumanSkill-4D: Training-Free Language Querying of Animatable Gaussian Avatars in Space and Time

- 分数：18.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：memory, benchmark, language model, large language, spec
- 作者：unsu Kim, Naeun Kim, Dongyoon Han, Seungryul Baek
- 链接：[arXiv](https://arxiv.org/abs/2610.24452) · [PDF](https://arxiv.org/pdf/2610.24452) · [HF](https://huggingface.co/papers/2610.24452)

We introduce avatar referring segmentation, which selects regions of animatable Gaussian avatars from language queries. A query can also specify a pose or motion to select matching intervals. This lets users interact with avatars for local editing and motion inspection. However, making these selections with existing language Gaussian splatting methods poses two challenges: adjacent parts and garments are hard to…

## 58. On the Limits of Scale: Inverse Scaling in Vision-Language Models

- 分数：18.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：reasoning, evaluation, benchmark, language model, spec
- 作者：Rohit Saxena, Alessandro Suglia, Marek Rei, Pasquale Minervini
- 链接：[arXiv](https://arxiv.org/abs/2610.27360) · [PDF](https://arxiv.org/pdf/2610.27360) · [HF](https://huggingface.co/papers/2610.27360)

Scaling laws suggest that increasing model size, training data, and compute generally yields monotonic performance improvements. While this often holds at the aggregate level, we present systematic evidence that vision-language models (VLMs) exhibit inverse scaling at the subtask level: specific question categories on which larger models perform worse than smaller counterparts within the same model family. We…

## 59. Slot-JEPA: Object-Structured Prediction Interfaces for Latent World Models

- 分数：18.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：memory, benchmark, spec, planning
- 作者：Peisong Wen, Qianqian Xu, Minye Lei, Siran Dai, Yang Liu, Qingming Huang
- 链接：[arXiv](https://arxiv.org/abs/2610.28074) · [PDF](https://arxiv.org/pdf/2610.28074) · [HF](https://huggingface.co/papers/2610.28074)

As a prototypical latent world model, Joint-Embedding Predictive Architectures (JEPAs) provide strong semantic representations. However, dense patch representations expose a redundant interface to downstream predictors, which must implicitly infer spatial organization and temporal correspondence, presenting three challenges. First, object information is distributed across patches, forcing each downstream predictor…

## 60. EAU: Environment-Agent-User Co-evolution for Training User-Centric Agents

- 分数：17.5  ·  HF 赞：11  ·  来源：huggingface
- 兴趣命中：agent, benchmark
- 作者：Min Cai, Dan Zhang, Gao Xing, Libin Ma, Zhaohui Xu, Xi Ye
- 链接：[arXiv](https://arxiv.org/abs/2610.16523) · [PDF](https://arxiv.org/pdf/2610.16523) · [HF](https://huggingface.co/papers/2610.16523)

Training LLM agents to interact with users over multiple turns is challenging because the learning signal depends not only on the agent, but also on the user simulator and environment, which jointly shape the agent's experience. Simulated users can be stochastic or inconsistent, while environments may contain unreliable tools, incomplete state coverage, and incorrect verifiers. Prior work mainly addresses the…

## 61. Spectral-Spatial Interpretation

- 分数：17.5  ·  HF 赞：11  ·  来源：huggingface
- 兴趣命中：evaluation, spec
- 作者：Haotian Ma, Ruqi Yang, Philip Townsend
- 链接：[arXiv](https://arxiv.org/abs/2610.21114) · [PDF](https://arxiv.org/pdf/2610.21114) · [HF](https://huggingface.co/papers/2610.21114)

Post-hoc image explanations usually show where a model looks using spatial heatmaps or indicate which channels matter using global channel scores. These separate views are limiting for multispectral data because channel relevance is often spatially localized and physically meaningful. We introduce Spectral-Spatial Interpretation (SSI), a full-grid attribution method over position-channel players (g,c). For each…

## 62. DONIC: Generalist Dexterous Bimanual Tracking Control from Human Demonstrations

- 分数：17.0  ·  HF 赞：10  ·  来源：huggingface + arxiv
- 兴趣命中：-
- 作者：Mingze Sun, Ziang Cao, Yuan Fei, Qiankuan Tao, Zihan Wang, Tianqi Liu, Junhao Chen, Haiwen Diao, Fangzhou Hong, Zhaoxi Chen, Ziwei Liu
- 链接：[arXiv](https://arxiv.org/abs/2610.29997) · [PDF](https://arxiv.org/pdf/2610.29997) · [HF](https://huggingface.co/papers/2610.29997)

Despite recent progress in dexterous reference tracking, existing models focus primarily on single-hand manipulation and a limited range of interactions, leaving the bimanual dexterous behaviors common in real life unaddressed. The scarcity of contact-rich bimanual manipulation data and the increased complexity of coordinating contacts make developing a generalist bimanual tracker particularly challenging.…

## 63. Sparsity Should Be ALLOTted by Output: Training-Free Allocation of Block-Sparse Attention for Video Diffusion Transformers

- 分数：17.0  ·  HF 赞：10  ·  来源：huggingface + arxiv
- 兴趣命中：-
- 作者：Tianze Xia, Xiaoling Zhou, Ruya Lan, Yiqiao Liao, Chengru Song, Shiming Xiang
- 链接：[arXiv](https://arxiv.org/abs/2610.29441) · [PDF](https://arxiv.org/pdf/2610.29441) · [HF](https://huggingface.co/papers/2610.29441)

Full 3D attention is costly in video Diffusion Transformers. Block-sparse attention reduces this cost by computing only selected attention blocks. However, existing methods either overlook the potential to optimize sparsity allocation or rely on heuristic rules or local metrics to guide it. In this work, we observe that sparsifying attention in different layers and at different denoising steps affects final-video…

## 64. Axiomatic World Modeling for Physics Reasoning

- 分数：17.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：reasoning, reinforcement learning, benchmark, spec
- 作者：Xinye Yang, Zhenyang Liu, Yuxuan Wang, Yuanyuan Lei
- 链接：[arXiv](https://arxiv.org/abs/2610.24519) · [PDF](https://arxiv.org/pdf/2610.24519) · [HF](https://huggingface.co/papers/2610.24519)

Recent research-level physics-reasoning benchmarks for LLMs reveal a failure mode that lies not in knowledge or execution, but in modeling the world being reasoned about. Models often silently alter given quantities, fabricate laws, or inject unstated assumptions to force a problem into familiar patterns, and then reason inside this corrupted world. We define this premise-level divergence as modeling drift: the gap…

## 65. Ask to Distill: Learning to Synthesize Data for On-Policy Distillation

- 分数：16.5  ·  HF 赞：9  ·  来源：huggingface
- 兴趣命中：agent, reasoning
- 作者：Jiashuo Sun, Hao Zhang, Xueqiang Xu, Heng Wang, Yixuan Xie, Pengcheng Jiang, Zhenrui Yue, Jiajun Fan, Peiran Li, Ge Liu, Shaowen Wang, Jiawei Han
- 链接：[arXiv](https://arxiv.org/abs/2610.27450) · [PDF](https://arxiv.org/pdf/2610.27450) · [HF](https://huggingface.co/papers/2610.27450)

On-policy distillation (OPD) can succeed with surprisingly few training questions, motivating a view of questions as carriers of distributional knowledge transfer. How can we assess whether a newly generated question is valuable for distillation, and learn to generate better questions---without access to its correct answer? We introduce Ask-to-Distill (\method), a framework that treats synthetic questions as…

## 66. StreamEval: Evaluating Interactive Streaming Video Generation Models

- 分数：16.5  ·  HF 赞：5  ·  来源：huggingface
- 兴趣命中：evaluation, benchmark, spec
- 作者：StreamEval Team
- 链接：[arXiv](https://arxiv.org/abs/2610.28402) · [PDF](https://arxiv.org/pdf/2610.28402) · [HF](https://huggingface.co/papers/2610.28402)

As streaming video generation advances, enabling real-time interaction with generated video is becoming increasingly important. We introduce StreamEval, a unified benchmark for interactive streaming video generation spanning five tasks: avatar dialogue, avatar performance, world generation, instruction editing, and reference editing. StreamEval comprises 300 scripted test cases lasting 15-300s, each specifying…

## 67. BiDex-100: A Comprehensive Benchmark for Bimanual Dexterous Manipulation Across 100+ Simulation Tasks

- 分数：16.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：memory, evaluation, benchmark, spec
- 作者：Yong Wang, Kecheng Zheng, Xing Zhu, Chao Xu, Yujun Shen, Shengze Cai
- 链接：[arXiv](https://arxiv.org/abs/2610.25459) · [PDF](https://arxiv.org/pdf/2610.25459) · [HF](https://huggingface.co/papers/2610.25459)

Bimanual manipulation with dexterous hands has attracted growing attention in research on robotic action models. However, few studies have developed benchmarks specifically tailored for dexterous manipulation, leaving the dexterous manipulation capabilities of existing models insufficiently characterized. In this paper, we present BiDex-100, a simulation benchmark for bimanual dexterous manipulation that combines…

## 68. Agentic World Action Models

- 分数：16.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：agent, reasoning, evaluation, planning
- 作者：Zhuoyang Liu, Dantong Niu, Botong Zhang, Boning Shao, Jing Wang, Ruijie Zheng, Yuvan Sharma, Runyu Lu, Jiaming Liu, Renrui Zhang, Roei Herzig, Yutong Bai, Ken Goldberg, Danfei Xu, Yuke Zhu, Guanzhi Wang, Linxi &#34;Jim&#34; Fan, Trevor Darrell
- 链接：[arXiv](https://arxiv.org/abs/2610.30136) · [PDF](https://arxiv.org/pdf/2610.30136) · [HF](https://huggingface.co/papers/2610.30136)

Recent world action models provide visual foresight and future prediction for robot manipulation, but lack explicit mechanisms for compositional skill reuse. Agentic robotics combines code-based planning and reasoning with reusable skills, but often lacks predictive grounding in physical dynamics. We introduce AW-0, an agentic world action model framework that integrates code-based planning with joint video and…

## 69. SpatialBrain: Spatial Intelligence Growing from Experience

- 分数：16.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：memory, reasoning, benchmark
- 作者：Yifan Zhou, Ziyang Gong, Xiaojun Ye, Yifei Liu, Donggang Li, Xiaolong Zhou, Zhihang Zhong, Xue Yang
- 链接：[arXiv](https://arxiv.org/abs/2610.29317) · [PDF](https://arxiv.org/pdf/2610.29317) · [HF](https://huggingface.co/papers/2610.29317)

Spatial reasoning requires more than access to geometric tools: a reasoner must decide when direct observation is sufficient and when to reconstruct, measure, or change reference frames. We present SpatialBrain, a framework that retains experience about these decisions while keeping its vision-language backbone fixed. The key distinction is between evidence about a scene and experience about how to reason with that…

## 70. ATEST: Adaptive Resource-Aware Test-Time Scaling for LLM Inference

- 分数：15.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：reasoning, language model, large language
- 作者：Mobina Kashaniyan, Ali Jannesari
- 链接：[arXiv](https://arxiv.org/abs/2610.25519) · [PDF](https://arxiv.org/pdf/2610.25519) · [HF](https://huggingface.co/papers/2610.25519)

Test-time scaling (TTS) improves large language model (LLM) reasoning by sampling multiple answers, but fixed sampling budgets ignore both query difficulty and the changing energy cost of inference under GPU contention. We measure up to a 4.1-fold increase in energy for the same four-sample query as GPU load rises. We present ATEST, a resource-aware TTS framework that jointly considers the expected value of…

## 71. Automating ML for Science: Can Frontier Agents Climb Scientific Hills in the Wild?

- 分数：15.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：agent, benchmark, coding
- 作者：Ming Zhong, Stacy Li, Nicholas Carlini, Matthew Jagielski
- 链接：[arXiv](https://arxiv.org/abs/2610.28763) · [PDF](https://arxiv.org/pdf/2610.28763) · [HF](https://huggingface.co/papers/2610.28763)

Frontier coding agents are increasingly framed as end-to-end automated researchers, and ML for science offers a demanding test of that promise: improving a scientific model often requires domain insight beyond routine ML engineering. We introduce Agent4Sci, a long-horizon testbed for measuring how far today's agents can improve the published best models on scientific ML benchmarks, spanning 20 benchmarks across 11…

## 72. Which Agent's Skill Should Change? Group-Relative Credit Assignment for Evolving Multi-Agent Teams

- 分数：15.0  ·  HF 赞：6  ·  来源：huggingface
- 兴趣命中：agent, retrieval
- 作者：Yanan Ma, Yang Wang, David Le, Chenhan Yuan, Yizheng Sun, Guangwei Zhang, Chenghao Xiao, Chenghua Lin, Imon Banerjee
- 链接：[arXiv](https://arxiv.org/abs/2610.27227) · [PDF](https://arxiv.org/pdf/2610.27227) · [HF](https://huggingface.co/papers/2610.27227)

Cooperative language-model agents can improve without weight updates by revising reusable skills, but only if a shared team reward is traced to the responsible agent and skill. Existing methods credit the skills present in each trajectory, yet presence is not responsibility: a harmful skill active in successful runs still earns positive credit. We present GRSE, Group-Relative Skill Evolution, which assigns…

## 73. Self-Credit: Credit Assignment for Long-Horizon Agentic RL via Intra-group Rescaling

- 分数：15.0  ·  HF 赞：6  ·  来源：huggingface
- 兴趣命中：agent, spec
- 作者：Fangcong Yin, Ming Yin, Tanvi Bhandarkar, Aashu Singh, Eryk Helenowski, Shlok Kumar Mishra, Saghar Hosseini, Karthik Abinav Sankararaman, Greg Durrett, Dinkar Juyal
- 链接：[arXiv](https://arxiv.org/abs/2610.28388) · [PDF](https://arxiv.org/pdf/2610.28388) · [HF](https://huggingface.co/papers/2610.28388)

LLM agents are commonly trained with RLVR, but the sparse nature of typical RLVR rewards makes credit assignment challenging, especially for long-horizon tasks. We propose Self-Credit, an end-to-end agentic RL method that creates dense supervision signals from sparse outcome rewards using self-generated credit assignment via intra-group rescaling. Self-Credit builds on group-based RL with three components. First,…

## 74. World Models with Configurable Perception

- 分数：15.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：spec, planning, retrieval
- 作者：Yijun Shen, Delong Chen, Xianming Hu, Kai Zhang, Pascale Fung
- 链接：[arXiv](https://arxiv.org/abs/2610.27914) · [PDF](https://arxiv.org/pdf/2610.27914) · [HF](https://huggingface.co/papers/2610.27914)

Real-world observations are noisy and often contain excessive task-irrelevant information. Effective world modeling and planning need to abstract observations into world state representations while filtering out irrelevant information. However, encoders in existing world models are typically non-adaptive, leading to state representations that are easily distracted by task-irrelevant information. As a result, the…

## 75. Real In, Real Out: What If We Only Use Real Data for Scene Text Editing?

- 分数：14.5  ·  HF 赞：9  ·  来源：huggingface
- 兴趣命中：benchmark
- 作者：Xingsong Ye, Yongkun Du, Jiaxin Zhang, Chong Sun, Zhineng Chen
- 链接：[arXiv](https://arxiv.org/abs/2610.27592) · [PDF](https://arxiv.org/pdf/2610.27592) · [HF](https://huggingface.co/papers/2610.27592)

Aiming to modify textual content while preserving the original style, Scene Text Editing (STE) has significant practical value in many applications. STE typically requires paired images before and after editing for training. However, recent approaches rely heavily on synthetic paired data and complex disentanglement strategies. They struggle to faithfully capture the diversity and complexity of natural scenes, often…

## 76. OmniCam: Omni-Camera Trajectory Generation via Geometry-Grounded Pose Token Learning

- 分数：14.5  ·  HF 赞：5  ·  来源：huggingface
- 兴趣命中：evaluation, spec
- 作者：Zhenyang Liu, Chenjie Cao, Yisu Zhang, Xuhui Zuo, Xiangyang Xue, Yanwei Fu, Tengfei Wang, Chunchao Guo
- 链接：[arXiv](https://arxiv.org/abs/2610.09513) · [PDF](https://arxiv.org/pdf/2610.09513) · [HF](https://huggingface.co/papers/2610.09513)

Camera trajectories control viewpoint changes in video generation, scene reconstruction, and robotic perception. Generating them from language requires both scene geometry and target-aware framing. We introduce OmniCam, an autoregressive model that generates camera pose sequences from a single panorama and textual trajectory descriptions. Its geometry-grounded pose token learning combines three components: a…

## 77. OverSeer: Multi-Agent World Models Beyond What Agents See

- 分数：14.5  ·  HF 赞：5  ·  来源：huggingface
- 兴趣命中：agent, spec
- 作者：Runjia Li, Kam Woh Ng, Minghao Chen, Junlin Han, Jianyuan Wang, Zhaochong An, Juan-Manuel Perez-Rua, Andrea Vedaldi, Shikun Liu
- 链接：[arXiv](https://arxiv.org/abs/2610.28554) · [PDF](https://arxiv.org/pdf/2610.28554) · [HF](https://huggingface.co/papers/2610.28554)

Despite the success of video world models, extending them to multiple agents is difficult because it requires generating several agent-specific video streams that are consistent in time and between agents. To address this gap, we introduce OverSeer, a multi-agent world model that augments egocentric agent views with auxiliary camera views. We suggest that, by fixing the auxiliary views in space, they act as a proxy…

## 78. Qwen-Audio-3.1-ASR Technical Report

- 分数：14.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：reasoning, evaluation, language model
- 作者：Chuanmeng Bian, Daren Chen, Peixin Chen, Zhigao Chen, Chong Deng, Zhiyun Fan, Zhifu Gao, Bo Gong, Qing Gu, Jiajun He, Yawei Hu, Yunjie Ji, Wei Ju, Jingbei Li, Xiangang Li, Xu Li, Zengxi Li, Zheng Li, Chengdong Liang, Baiji Liu, Yaming Liu, Ying Liu, Bin Ma, Yiping Peng, Yuezhang Peng, Zhendong Peng, Yu Pu, Yang Shi, Xin Shu, Jian Tang, Biao Tian, Peiyao Wang, Tianzi Wang, Wen Wang, Wupeng Wang, Cheng Wen, Yuzhong Wu, Zijian Xia, Yunchong Xiao, Nan Yang, Jianwei Yu, Jixing Yu, Binbin Zhang, Lei Zhang, Sitong Zhao, Guangdong Zhou, Yuan Zhou, Jianheng Zhuo
- 链接：[arXiv](https://arxiv.org/abs/2610.28711) · [PDF](https://arxiv.org/pdf/2610.28711) · [HF](https://huggingface.co/papers/2610.28711)

We present Qwen-Audio-3.1-ASR, a family of audio-language models that builds upon its predecesor Qwen-Audio-3.0-ASR with improved speech recognition and expanded capabilities in speaker-diarized transcription and general audio understanding. The family retains support for 30 languages and 16 Chinese dialects, together with instruction-controlled capabilities including historical-context conditioning, hierarchical…

## 79. RubatoCodec: Budgeted Adaptive Speech Tokenization with Streaming Decoding

- 分数：14.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：benchmark, coding, spec
- 作者：Chihiro Arata, Shohei Taniguchi, Gouki Minegishi, Kan Hatakeyama-Sato
- 链接：[arXiv](https://arxiv.org/abs/2610.29434) · [PDF](https://arxiv.org/pdf/2610.29434) · [HF](https://huggingface.co/papers/2610.29434)

Neural speech codecs provide discrete tokens for speech generation. Lower frame rates shorten token sequences, but each token must then carry more linguistic and acoustic information. Variable-frame-rate codecs address this trade-off by adapting token allocation to speech content, but threshold-based allocation lets content determine the token count, so the sequence length a speech generator must produce varies…

## 80. VX-One: Typed, Calibrated Decision Heads for Real-Time Perimeter Triage - An empirical study of unknown-attack honesty, cascade gray zones, and calibration under drift

- 分数：14.5  ·  HF 赞：1  ·  来源：huggingface + arxiv
- 兴趣命中：benchmark
- 作者：Juan S. Santillana
- 链接：[arXiv](https://arxiv.org/abs/2610.30090) · [PDF](https://arxiv.org/pdf/2610.30090) · [HF](https://huggingface.co/papers/2610.30090)

Perimeter triage faces a latency/semantics trade-off: signature engines are fast and format-safe but blind to unseen attacks, while generative models are semantic but slow and produce unparseable output. In late 2026 a class of commercial System One decision models (TypeSafe Jev; Microsoft-Decision-1) began selling typed decision primitives - binary gates, closed-set choices, ordinal scores - as product APIs, with…

## 81. ACE-Brain-0.6: Scaling Spatial Grounding for Physical Foundation Models

- 分数：14.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：reasoning, benchmark
- 作者：Yinhe Wang, Tao Tao, Zexin He, Shuang Luo, Wei Mao, Yao Mu, Feng Pan, Hanming Deng, Lewei Lu, Zhi Hou, Xingang Pan, Dahua Lin, Dacheng Tao, Xiaogang Wang
- 链接：[arXiv](https://arxiv.org/abs/2610.27040) · [PDF](https://arxiv.org/pdf/2610.27040) · [HF](https://huggingface.co/papers/2610.27040)

General-purpose multimodal models, including GPT-6 Astra and Claude Opus 5.5, demonstrate broad capabilities in embodied manipulation. Our analysis indicates that this generality is accompanied by strong spatial perception, as Astra can determine where to interact with task-relevant entities amid visual distractors. Because spatial perception connects high-level reasoning to the physical scene, we investigate…

## 82. HRoPE: Homography Relative Positional Encoding

- 分数：14.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：coding, spec
- 作者：Huachen Gao, Yang Yang, Xiaoqian Liang, Xingyu Chen, Youjia Zhang, Qi Zhang, Baorui Ma, Anpei Chen, Wei Yang
- 链接：[arXiv](https://arxiv.org/abs/2610.28284) · [PDF](https://arxiv.org/pdf/2610.28284) · [HF](https://huggingface.co/papers/2610.28284)

Geometric Relative Positional Encoding has become the primary mechanism for injecting spatial inductive biases into multi-view transformers. Existing designs condition attention on camera-level frustums or ray-marched depth, associating cross-view tokens through the sensor geometry. Such sensor-centric formulations, however, describe only where a token is observed from, leaving the rich surface geometry of the scene…

## 83. WinARDet: Compressed Window Auto-Regression for Long-Horizon Vision-Language Grounding

- 分数：13.5  ·  HF 赞：7  ·  来源：huggingface
- 兴趣命中：coding
- 作者：Chenxu Wang, Hangyi Kuang, Bo-Wen Yin, Yuxuan Li, Quan-Sheng Zeng, Yang Zhang, Xu Guo, Xiang Li, Qibin Hou
- 链接：[arXiv](https://arxiv.org/abs/2610.19419) · [PDF](https://arxiv.org/pdf/2610.19419) · [HF](https://huggingface.co/papers/2610.19419)

MLLM-based detectors formulate vision-language grounding as autoregressive coordinate generation, yet in dense scenes, they often collapse into a box repetition loop, repeatedly emitting identical boxes until the decoding budget is exhausted. We trace this failure to historical-answer attention takeover: Under full-history autoregression, repeated coordinate tokens in the growing answer history attract…

## 84. Beyond Compilation: Evaluating Faithful Natural-Language-to-Lean Statement Formalization

- 分数：13.5  ·  HF 赞：7  ·  来源：huggingface
- 兴趣命中：agent
- 作者：Ke Zhang, Patricio Gallardo Candela, Sudhir Murthy, Yi Xie, Zhi Wang, Maziar Raissi
- 链接：[arXiv](https://arxiv.org/abs/2606.31002) · [PDF](https://arxiv.org/pdf/2606.31002) · [HF](https://huggingface.co/papers/2606.31002)

Lean verifies that a generated declaration is well typed, but cannot check whether it states what the user intended. We measure how far compilation overstates faithfulness in statement autoformalization without canonical Lean targets. Our criterion requires Lean compilation and agreement of two LLM judges from different model families. On an independent random audit, it agrees with the human majority on 91.5% of…

## 85. DeLoop: Repeated Actions as Self-Supervision for Long-Horizon Agents

- 分数：13.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：agent, context window
- 作者：Tianle Chen, Pushkar Singh, Ketan Todi, Biswajit Paria, Qijia He, Wenqi Wang, Yuwen Tan, Jike Zhong, Sugato Basu, Deepti Ghadiyaram, Arjun Akula
- 链接：[arXiv](https://arxiv.org/abs/2610.19376) · [PDF](https://arxiv.org/pdf/2610.19376) · [HF](https://huggingface.co/papers/2610.19376)

Language-model agents that run long tasks often redo work they have already done: they re-issue a tool call they made earlier and get back exactly the same observation, a step that adds no new information. We identify this failure as a loop. Loops appear natively in Qwen, Llama, and Gemini agents and become far more common once the agent's history is compressed to fit its context window. To reduce these loops, we…

## 86. EMBER: Predicting TCR--pMHC Binding Without a Docked Complex

- 分数：12.5  ·  HF 赞：5  ·  来源：huggingface
- 兴趣命中：evaluation
- 作者：Lin Ha, Chen Zhou, Haozheng Luo, Han Liu, Xiaoyu Zhang, Yan Chen
- 链接：[arXiv](https://arxiv.org/abs/2610.27334) · [PDF](https://arxiv.org/pdf/2610.27334) · [HF](https://huggingface.co/papers/2610.27334)

We propose EMBER, a structure-based framework for TCR--pMHC binding prediction that eliminates the need for a predicted docked complex, and with it the placement error that dominates such predictions. Traditional structure-based predictors utilize the co-folded complex structure of the receptor and the antigen and interpret binding from its contact surface. Consequently, every downstream feature inherits any…

## 87. Toward Part-Aware Choral Transcription with singing voice assignment

- 分数：12.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：evaluation, spec
- 作者：Hanyu Meng, Zhanhong He, Zixun Guo, Yaolong Ju
- 链接：[arXiv](https://arxiv.org/abs/2610.09861) · [PDF](https://arxiv.org/pdf/2610.09861) · [HF](https://huggingface.co/papers/2610.09861)

Single-instrument automatic music transcription (AMT) has advanced substantially, yet choral applications require soprano, alto, tenor, and bass (SATB) to be transcribed as separate parts. Recent note-level choral AMT instead produces a single merged note track, limiting rehearsal, education, and score reconstruction. To address this limitation, we introduce Part-aware Choral Transcription (PawCT), to our knowledge…

## 88. Entertain, then Cancel: How Thinking Makes Reasoning Models Read Some and Or Literally

- 分数：12.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：reasoning, evaluation
- 作者：Zhizhuo Kou, Jian Yang, Pengfei Hao, Junyu Luo, Jingshu Peng, Sirui Han, Yike Guo
- 链接：[arXiv](https://arxiv.org/abs/2610.21204) · [PDF](https://arxiv.org/pdf/2610.21204) · [HF](https://huggingface.co/papers/2610.21204)

When a speaker says ``some students passed'', listeners infer that not all of them did. Reasoning models now let users decide how long a model thinks before it answers, but we do not know what extra thinking does to such everyday inferences. We study this directly: we keep a model's weights fixed, change only how much it thinks, and record which reading it chooses. A second tool cuts the model's own reasoning at…

## 89. Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models

- 分数：12.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：benchmark, spec
- 作者：Bryce Grant, Xijia Zhao, Peng Wang
- 链接：[arXiv](https://arxiv.org/abs/2603.19233) · [PDF](https://arxiv.org/pdf/2603.19233) · [HF](https://huggingface.co/papers/2603.19233)

A fine-tuned Vision-Language-Action (VLA) policy can easily place the alphabet soup in the basket on command, just as it saw during fine-tuning. However, if the basket is shifted five centimeters to the left, it drops the soup off the table. We developed an interpretability pipeline to investigate what such a policy is computing. Injecting task A's activations into the action expert while the policy looks at task…

## 90. TRACE: Tracking Multimodal Clinical Trajectories for Inpatient Risk Prediction

- 分数：12.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：spec
- 作者：Minjun Kim, Jong Hak Moon
- 链接：[arXiv](https://arxiv.org/abs/2610.25765) · [PDF](https://arxiv.org/pdf/2610.25765) · [HF](https://huggingface.co/papers/2610.25765)

Accurate inpatient risk prediction requires modeling heterogeneous clinical evidence that accumulates irregularly over time. This challenge spans in-hospital mortality, prolonged length of stay, and readmission, each with task-specific observation windows. Existing multimodal approaches combine structured health record data, chest x-rays, and clinical text, but primarily focus on modality fusion or missing-modality…

## 91. λ_0: Scaling Open-World Egocentric Human Data for Humanoid Loco-Manipulation

- 分数：11.0  ·  HF 赞：6  ·  来源：huggingface
- 兴趣命中：-
- 作者：humanoid Team
- 链接：[arXiv](https://arxiv.org/abs/2610.18950) · [PDF](https://arxiv.org/pdf/2610.18950) · [HF](https://huggingface.co/papers/2610.18950)

Humanoid loco-manipulation requires coordinated whole-body interaction with the physical world, yet collecting robot demonstrations at scale remains costly. Human demonstrations offer a scalable alternative, but existing egocentric human supervision often omits locomotion and posture, while embodiment differences and controller dynamics hinder accurate end-effector execution. We introduce HumanVerse, a 500-hour…

## 92. PhysLDM: Latent Diffusion for High-Fidelity Deformable Simulation

- 分数：11.0  ·  HF 赞：6  ·  来源：huggingface
- 兴趣命中：-
- 作者：Yu Zhang, Xudong Xu, Xingang Pan
- 链接：[arXiv](https://arxiv.org/abs/2610.07609) · [PDF](https://arxiv.org/pdf/2610.07609) · [HF](https://huggingface.co/papers/2610.07609)

Neural simulation of high-fidelity deformable bodies is a foundational challenge in computer graphics and physical AI. Long-horizon prediction for high-resolution 3D volumetric meshes is hard: autoregressive methods are prone to error accumulation, while direct multi-frame prediction at native resolution is computationally prohibitive. This motivates a compact spatiotemporal latent representation, which is largely…

## 93. What Makes a Good Symbol for Hybrid Discrete-Continuous Planning?

- 分数：11.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：planning
- 作者：Yiyuan Pan, Changliu Liu, Jiayuan Mao
- 链接：[arXiv](https://arxiv.org/abs/2610.23010) · [PDF](https://arxiv.org/pdf/2610.23010) · [HF](https://huggingface.co/papers/2610.23010)

The physical world has continuous state and action spaces, yet robot planning often benefits from hybrid discrete-continuous formulations that explicitly expose combinatorial structure, such as contact modes or discrete primitive actions. Existing methods typically rely on human-defined symbol sets or symbols derived from language supervision, without asking what makes a symbol computationally useful. In this paper,…

## 94. VideoMaMa++: Temporally Consistent Video Matting via Preserve-and-Refine Token

- 分数：11.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：benchmark
- 作者：Sangbeom Lim, Seoung Wug Oh, Heeji Yoon, Seungryong Kim, Joon-Young Lee
- 链接：[arXiv](https://arxiv.org/abs/2610.26857) · [PDF](https://arxiv.org/pdf/2610.26857) · [HF](https://huggingface.co/papers/2610.26857)

Diffusion-based video matting has recently emerged as a leading approach, leveraging video diffusion priors from internet-scale pretraining to achieve strong zero-shot generalization from limited synthetic data. However, the heavy compute of these diffusion backbones limits inference to a short chunk of just 6 to 24 frames, so even ordinary videos span multiple chunks. Because each chunk is matted independently from…

## 95. Answering in the User's Variety: Calibrated Accommodation Pairs for Post-Training

- 分数：10.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：reinforcement learning
- 作者：Zhizhuo Kou, Heming Li, Jian Yang, Junyu Luo, Jingshu Peng, Sirui Han, Yike Guo
- 链接：[arXiv](https://arxiv.org/abs/2610.28474) · [PDF](https://arxiv.org/pdf/2610.28474) · [HF](https://huggingface.co/papers/2610.28474)

People adapt how they talk to the person in front of them. However, chat models tend to respond in Standard English regardless of the dialect used by the user. A uniform answer can hide whether training treats these users alike, and output audits cannot tell as well. We trace how each post-training stage, from supervised fine-tuning (SFT) to preference optimization (DPO) and reinforcement learning, changes a model's…

## 96. Right On Q: Recovering Reasoning under Quantization via Self-Generated Trajectories

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, benchmark, language model, large language
- 作者：Boyuan Zheng, Jing Xiong, Chenwei Wu, Hui Shen, Zesen Zhao, Hei Ting Una Chan, Xueshen Liu, Zhen Zhang, Liyue Shen, Zechun Liu, Z. Morley Mao
- 链接：[arXiv](https://arxiv.org/abs/2610.29378) · [PDF](https://arxiv.org/pdf/2610.29378) · [HF](https://huggingface.co/papers/2610.29378)

Quantization-aware training (QAT) aims to recover reasoning capabilities in low-bit large language models (LLMs). Existing recipes typically supervise the quantized student with the original full-precision model on fixed response sequences. However, the resulting low-bit quantized models still struggle on long-horizon reasoning tasks and often fail to terminate within a token budget that suffices for the…

## 97. LLMSeg: Training-Free Text-Prompted Image Segmentation with B-Splines

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, language model, large language, spec
- 作者：Abdullah Hamdi
- 链接：[arXiv](https://arxiv.org/abs/2610.29409) · [PDF](https://arxiv.org/pdf/2610.29409) · [HF](https://huggingface.co/papers/2610.29409)

Promptable segmentation models such as SAM 3 achieve remarkable open-vocabulary performance but require dedicated architectures, large-scale annotation engines, and task-specific training. We ask a different question: can a general-purpose multimodal large language model (MLLM) segment images directly, without an added segmentation head, mask decoder, or training? We present LLMSeg, a training-free pipeline that…

## 98. BIRD-RL: Scaling Agentic Reinforcement Learning over Stateful Data-Centric Environments

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reasoning, reinforcement learning, evaluation, benchmark, language model, spec
- 作者：Ge Qu, Jinyang Li, Xiaohan Xu, Xiaolong Li, Bowen Qin, Nan Huo, Ziwei Tang, Chenhao Ma, Reynold Cheng
- 链接：[arXiv](https://arxiv.org/abs/2610.29426) · [PDF](https://arxiv.org/pdf/2610.29426) · [HF](https://huggingface.co/papers/2610.29426)

While agentic reinforcement learning (RL) has emerged as a promising paradigm for training small language models (SLMs), existing frameworks are predominantly tool-centric and struggle with data-centric environments. Specifically, applying tool-centric frameworks to stateful tasks like SQL debugging introduces severe spatial inefficiencies since proper environment isolation typically requires a separate database…

## 99. DynaWeave: Learning to Adapt through Dynamic Scenario Synthesis

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, evaluation, language model, large language
- 作者：Xuan Yang, Chunxiao Liu, Hongsheng Xin, Hao Xu, Ning Miao
- 链接：[arXiv](https://arxiv.org/abs/2610.29443) · [PDF](https://arxiv.org/pdf/2610.29443) · [HF](https://huggingface.co/papers/2610.29443)

Large language model (LLM) agents increasingly use tools to complete tasks in stateful environments. However, many training environments remain largely static apart from changes caused by the agent's own actions, whereas external events introduced by other users, services, or sudden contingencies in real environments can invalidate ongoing plans. To address this gap, we introduce DynaWeave, an automated synthesis…

## 100. Omnilingual-MsASR: Benchmarking Multimodal, Multilingual, Long-Form Multi-Speaker ASR of Omni Large Language Models

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, language model, large language, spec
- 作者：Yuan Ge, Pei Zhang, Xize Cheng, Lingzhou Mu, Mingyang Wang, Jin Xu, Baosong Yang, Shengxiang Gao, Jingbo Zhu, Zhengtao Yu, Tong Xiao
- 链接：[arXiv](https://arxiv.org/abs/2610.29455) · [PDF](https://arxiv.org/pdf/2610.29455) · [HF](https://huggingface.co/papers/2610.29455)

Omni-modal large language models (LLMs) have achieved remarkable progress in audio and video understanding. However, existing models struggle with long-form, multi-speaker videos, especially in understanding the entire video and recognizing who says what and when. To characterize the capability limit of current omni LLMs and guide future model development, we introduce Omnilingual-MsASR, a multilingual, multimodal…

## 101. PreCoMem: Predictive Cognitive Memory for Self-Evolving Long-Term Dialogue Agents

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, memory, coding, retrieval
- 作者：Jian Zhong, Zeyu Liu, Pingchuan Cao, Rongduo Han, Shunye Tang, Guohuan Xie, Mingyuan Qin, Ran Ji, Xiao Liang, Wei Wang, Haining Zhang
- 链接：[arXiv](https://arxiv.org/abs/2610.29467) · [PDF](https://arxiv.org/pdf/2610.29467) · [HF](https://huggingface.co/papers/2610.29467)

Long-horizon dialogue agents need to keep user memories stable enough for personalization while adapting when the user genuinely changes. Existing memory systems often append every observation or overwrite old entries by heuristic rules, which makes transient noise hard to distinguish from real belief drift. We introduce PreCoMem, a memory consolidation framework inspired by predictive coding that represents memory…

## 102. OmniSimulator: Aligning Small Language Models for Authentic Heterogeneous Behavior Modeling

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, language model, large language, spec
- 作者：Jiawei Chen, Ruoxi Xu, Boxi Cao, Zhuoqun Li, Ruotong Pan, Yunfei Zhang, Zhirui Yang, Jingyan Chen, Tingting Gao, Han Li, Yaojie Lu, Xianpei Han, Le Sun, Xiangyu Wu, Hongyu Lin
- 链接：[arXiv](https://arxiv.org/abs/2610.29472) · [PDF](https://arxiv.org/pdf/2610.29472) · [HF](https://huggingface.co/papers/2610.29472)

Large language models (LLMs) have shown great potential as general-purpose user simulators for interactive systems. Prior studies have demonstrated that training on high-quality data can substantially improve model reasoning and downstream task performance. However, the upper bound of user simulation is still constrained by the model's reasoning paradigm: native chain-of-thought often degenerates into shallow…

## 103. TenetBench: A Clause-Anchored Russian Corpus for Evaluating Language Models against Professional Codes of Ethics

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, evaluation, language model, large language, spec
- 作者：Yegor Anichkov, Valery Vinogradov, Andrey Furov, Marina Polukoshko, Sergey Bolovtsov
- 链接：[arXiv](https://arxiv.org/abs/2610.29477) · [PDF](https://arxiv.org/pdf/2610.29477) · [HF](https://huggingface.co/papers/2610.29477)

Codes of professional ethics guide and restrict specialists, who increasingly work with assistants built on large language models. Such an assistant can breach the user's code, or help the user breach it, without the user noticing. Evaluations reporting broad categories of harm cannot show how often this happens or which provision is breached. TenetBench pairs 3,433 requests conflicting with clauses of fifteen…

## 104. Balancing Foundation Models and Trait-Specific Learning for Forehead-Crease Recognition

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, language model, large language, spec
- 作者：Geetanjali Sharma, Aryan Jain, Dev Nagaich, Aditya Nigam, Raghavendra Ramachandra
- 链接：[arXiv](https://arxiv.org/abs/2610.29495) · [PDF](https://arxiv.org/pdf/2610.29495) · [HF](https://huggingface.co/papers/2610.29495)

Biometric recognition often degrades under partial facial vis- ibility, where conventional facial cues are occluded. The forehead region remains consistently visible and contains distinctive crease patterns that can serve as a complementary biometric trait. We present a unified eval- uation of forehead-crease recognition across explainable zero-shot rea- soning, domain-adaptive learning, and trait-specific modeling.…

## 105. Parallel Thinking for Large Language Model with Path Diversity

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, reinforcement learning, benchmark, language model, large language
- 作者：Jiaru Qian, Yihong Dong, Xue Jiang, Chun-Wah Hsu, Zhi Jin, Ge Li
- 链接：[arXiv](https://arxiv.org/abs/2610.29501) · [PDF](https://arxiv.org/pdf/2610.29501) · [HF](https://huggingface.co/papers/2610.29501)

Parallel thinking has emerged as a promising paradigm for enhancing the reasoning capabilities of Large Language Models (LLMs) by exploring multiple reasoning paths simultaneously. However, we identify that parallel thinking via Reinforcement Learning (RL) typically suffers from the mode collapse of reasoning paths, where parallel thinking trajectories degenerate into similar ones. This homogeneity undermines the…

## 106. Keeping Time vs. Understanding Time: Neither Alone Explains Temporal Reasoning in LLMs

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, evaluation, benchmark, spec
- 作者：Auss Abbood, Fernando Martínez-Plumed, José Hernández-Orallo, Nigel Collier
- 链接：[arXiv](https://arxiv.org/abs/2610.29507) · [PDF](https://arxiv.org/pdf/2610.29507) · [HF](https://huggingface.co/papers/2610.29507)

Temporal reasoning is widely assumed to decompose into two modes: temporal arithmetic (date and time calculations), and temporal semantics (understanding temporal and causal relations). This dichotomy shapes how benchmarks are designed, how models are trained, and how progress is measured, yet its empirical validity has never been directly tested. We provide two lines of evidence that challenge it. First, we test…

## 107. Mitigating Query Shortcuts in Chain-of-Thought with Context-Aware Decoding

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, benchmark, language model, large language, coding, spec
- 作者：Shin'ya Yamaguchi
- 链接：[arXiv](https://arxiv.org/abs/2610.29518) · [PDF](https://arxiv.org/pdf/2610.29518) · [HF](https://huggingface.co/papers/2610.29518)

While Chain-of-Thought (CoT) prompting improves the reasoning performance of large language models (LLMs), recent studies have shown that final answers do not always depend on the generated rationales. In particular, LLMs may rely on query-specific shortcuts rather than the information provided by their reasoning steps. In this paper, we investigate whether context-aware decoding (CAD), an existing contrastive…

## 108. RCSD: Reinforcement and Continual Learning for Domain-Specific Speculative Decoding

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, language model, large language, coding, spec
- 作者：Mingkang Liu, Weiming Meng, Peipei Jiao, Jiawei Zhang, Tianyuan Liu, Junyan Li, Lichen Pang
- 链接：[arXiv](https://arxiv.org/abs/2610.29527) · [PDF](https://arxiv.org/pdf/2610.29527) · [HF](https://huggingface.co/papers/2610.29527)

Speculative decoding accelerates large language model inference by employing a compact draft model to propose candidate tokens that are verified in parallel by a target model. Conventional training relies on soft-label distillation, which forces the draft model to mimic the target's full output distribution, including high-entropy regions that degrade acceptance rates and increase early rejection risk. We propose…

## 109. Melange: A Synthetic Visual Bias Benchmark for Multi-modal Large Language Models

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, language model, large language, spec
- 作者：Razieh Rezaei, Ehsaneddin Asgary, Masoud Jalili Sabet
- 链接：[arXiv](https://arxiv.org/abs/2610.29537) · [PDF](https://arxiv.org/pdf/2610.29537) · [HF](https://huggingface.co/papers/2610.29537)

Multi-modal Large Language Models (MLLMs) have seen broad adoption, but their biases are still far less examined than those of standard LLMs, creating possible social harms when deployed in real-world settings. Prior efforts to extend bias analyses from LLMs into the multi-modal space either cover only a few bias categories or do not ensure that the groups being compared are clearly addressed by visual cues in the…

## 110. Generalized CycleGRPO for Fine-Grained Multimodal Understanding and Grounding

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reinforcement learning, evaluation, benchmark, language model, large language, spec
- 作者：Xin Zhang, Haochen Wang, Beibei Lin, Zhaoxiang Zhang, Robby T. Tan, Jason Li, Dacheng Tao
- 链接：[arXiv](https://arxiv.org/abs/2610.29552) · [PDF](https://arxiv.org/pdf/2610.29552) · [HF](https://huggingface.co/papers/2610.29552)

Fine-grained multimodal intelligence requires models to both understand a designated region and localize it from language. Existing methods learn these directions with separate objectives and task-specific annotations. We present Generalized CycleGRPO, the first unified reinforcement learning framework coupling region understanding and localization across spatial, temporal, and spatio-temporal domains. Given a…

## 111. WRDO: Weighted Refusal Direction Optimization in Aligned Language Models

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, language model, large language, spec
- 作者：Grigoriy Evseev, Vladimir Solodkin, Dmitry Bylinkin, Daniil Medyakov, Vladimir Aletov, Aleksandr Beznosikov
- 链接：[arXiv](https://arxiv.org/abs/2610.29555) · [PDF](https://arxiv.org/pdf/2610.29555) · [HF](https://huggingface.co/papers/2610.29555)

Aligned large language models are trained to comply with benign requests while refusing harmful ones. However, recent work shows that this refusal behavior is fragile and can often be disrupted by simple activation- or weight-space interventions. In particular, refusal has been shown to be largely mediated by a single residual-stream direction, typically computed as a difference-of-means vector between harmful and…

## 112. CineEvolve: An Agentic Self-Evolution Framework for Cinematic Multi-Shot Video Generation

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reasoning, reinforcement learning, planning
- 作者：Jingzhe Zhang, Peixuan Zhang, Genying Li, Bing Ma, Shuchen Weng, Si Li, Boxin Shi
- 链接：[arXiv](https://arxiv.org/abs/2610.29590) · [PDF](https://arxiv.org/pdf/2610.29590) · [HF](https://huggingface.co/papers/2610.29590)

Cinematic multi-shot video generation requires both narrative planning and iterative refinement. Existing methods either lack narrative reasoning or rely on feed-forward workflows without policy updates. In this paper, we propose CineEvolve, an agentic self-evolution framework for cinematic multi-shot video generation that unifies a Director and a Critic within a single vision-language policy. Emulating real-world…

## 113. Overview of CHIP 2026 Shared Task 1: Patient-Specific Phenotype Concept Recognition in Full-Text Biomedical Literature

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, language model, large language, spec
- 作者：Xuanlyu Zhu, Feng Tian, Yang Zhong, Pengqi Zheng, Xiwen Bi, Ling Luo, Yuanyuan Sun, Jian Wang, Lingfei Lin
- 链接：[arXiv](https://arxiv.org/abs/2610.29606) · [PDF](https://arxiv.org/pdf/2610.29606) · [HF](https://huggingface.co/papers/2610.29606)

Automatic phenotype information extraction plays an important role in rare disease diagnosis, genotype-phenotype analysis, and precision medicine. However, accurately identifying phenotype concepts and determining their associations with specific patients remain challenging, particularly in full-text biomedical articles involving multiple patients and complex clinical descriptions. This paper presents an overview of…

## 114. Uni-Mem: Learning a Long-Horizon Agentic Memory Manager with Unified Online Policy Optimization

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, memory, reinforcement learning, spec, retrieval
- 作者：Zhiqian Xia, Jielong Tang, Ling-An Zeng, Shixiong Kai, Rong Yao, Hao Kong, Xiao Dong, Wei Wang, Mingxuan Yuan, Siyu Xia, Haifeng Xia
- 链接：[arXiv](https://arxiv.org/abs/2610.29671) · [PDF](https://arxiv.org/pdf/2610.29671) · [HF](https://huggingface.co/papers/2610.29671)

Long-term agent memory is shifting from predefined workflows toward learnable policies for memory construction and retrieval. Existing learning-based methods either optimize construction alone or combine retrieval-side online reinforcement learning (RL) with offline construction supervision, limiting co-adaptation between the two stages. In this paper, we explore end-to-end online RL for a unified memory manager…

## 115. Retrieval Augmented Generation Compositionality

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, evaluation, benchmark, language model, large language, retrieval
- 作者：Ido Levy, Segev Shlomov, Leshem Choshen
- 链接：[arXiv](https://arxiv.org/abs/2610.29722) · [PDF](https://arxiv.org/pdf/2610.29722) · [HF](https://huggingface.co/papers/2610.29722)

Retrieval Augmented Generation (RAG) grounds large language models in external knowledge. Modern pipelines combine embedding, chunking, retrieval, reranking, query augmentation, context compression, and agentic verification, yet these techniques are typically evaluated one at a time. It remains unclear whether their isolated gains survive composition, whether retrieval quality and answer faithfulness favor the same…

## 116. Structure-Aware Message Passing on Petri Nets through Directed Walks and Incidence Diffusion

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, coding, spec, retrieval
- 作者：Geri Skenderi
- 链接：[arXiv](https://arxiv.org/abs/2610.29725) · [PDF](https://arxiv.org/pdf/2610.29725) · [HF](https://huggingface.co/papers/2610.29725)

A common application of the process mining discipline is to connect observed event data with Petri nets, which are bipartite, directed graphical process models with rich formal underpinnings. Recent work learns vector representations of Petri nets to retrieve process models and relate them to event logs, but leaves implicit two key aspects hidden within the net's structure: directed cycles (process loops) and…

## 117. Metamodel-Guided LLM Decoding for Consistent DSL Generation

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, language model, large language, coding, spec
- 作者：Boqi Chen, Aren A. Babikian, José Antonio Hernández López
- 链接：[arXiv](https://arxiv.org/abs/2610.29749) · [PDF](https://arxiv.org/pdf/2610.29749) · [HF](https://huggingface.co/papers/2610.29749)

Large language models (LLMs) are increasingly used to generate software engineering artifacts written in domain-specific languages (DSLs). Correct DSL instances usually must comply with not only the concrete syntax but also the abstract syntax defined by a metamodel augmented with semantic well-formedness constraints. Existing constrained decoding approaches typically guarantee compliance only with concrete syntax…

## 118. Bridging Foundational and Agentic Capabilities of LLMs

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, evaluation, benchmark, language model, large language
- 作者：Wei Guo, Yuanjian Xu, Jianing Hao, Yongyao Duan, Ran Chen, Zhong Li, Guang Zhang
- 链接：[arXiv](https://arxiv.org/abs/2610.29751) · [PDF](https://arxiv.org/pdf/2610.29751) · [HF](https://huggingface.co/papers/2610.29751)

Large language models (LLMs) are increasingly deployed as agents, yet it remains unclear how their foundational capabilities translate into agentic capabilities. End-to-end scores leave unresolved whether low benchmark capability or weak deployment drives a failure, limiting actionable diagnosis. We bridge foundational and agentic capabilities through an operation-level measurement framework. We represent each model…

## 119. ALIAS: Evaluating Performance and Memorization in LLM-Written TLA+ Specifications

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, language model, large language, spec
- 作者：Arslan Bisharat, Mujtaba Nazari, Khushboo Bhadauria, Brian Ortiz, Eric Spencer, Beatriz Santos, TaiNing Wang, George K. Thiruvathukal, Konstantin Laufer, Mohammed Abuhamad
- 链接：[arXiv](https://arxiv.org/abs/2610.29767) · [PDF](https://arxiv.org/pdf/2610.29767) · [HF](https://huggingface.co/papers/2610.29767)

Memorization inflates the benchmark scores of large language models (LLMs), since a model can reproduce answers it saw in training. Researchers test for it with consistent identifier renaming (CIR), which gives every identifier in a task a new name, and treat a lower score on the renamed task as evidence of recall. We test this method on the Temporal Logic of Actions Plus (TLA+) language, whose model checker acts as…

## 120. MAPS: Macro-Adaptive Parallel Reasoning for Regulating Search Momentum in Retrieval-Augmented Generation

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, benchmark, language model, large language, retrieval
- 作者：Xinze Li, Dingwen Zhang, Zhenghao Liu, Yukun Yan, Shuo Wang, Yu Gu, Ge Yu, Maosong Sun
- 链接：[arXiv](https://arxiv.org/abs/2610.29792) · [PDF](https://arxiv.org/pdf/2610.29792) · [HF](https://huggingface.co/papers/2610.29792)

Retrieval-Augmented Generation (RAG) improves the performance of Large Language Models (LLMs) by retrieving external knowledge. Recently, some RAG methods interleave reasoning and retrieval, enabling LLMs to progressively generate sub-queries and retrieve external knowledge. However, these methods may suffer from redundant or ineffective sub-queries and insufficiently diverse query exploration. Moreover, due to the…
