# 每日 AI 论文

生成时间：2026-11-14 06:23 UTC  ·  共 120 篇（已按 arXiv ID 去重）

来源：Hugging Face Daily Papers + arXiv（cs.AI / cs.LG / cs.CL / cs.CV）。
排序：HF 上榜、点赞、多源命中、兴趣词。兴趣词可在 `config.json` 改。

## 1. PhysLoop: Harnessing LLMs' Physics Awareness for Self-Improving Video Generation Models

- 分数：40.0  ·  HF 赞：43  ·  来源：huggingface + arxiv
- 兴趣命中：evaluation, benchmark, language model, large language, spec
- 作者：Yuxuan Chen, Xiaojie Li, Hao Chen, Juncheng Ma, Kewei Zhang, Zhongjing Du, Guoqiang Wei, Fangfang Wang, Zhen Dong, Zhiyang Dou, Liming Zhao, Yan Zeng, Jianwei Zhang, Daquan Zhou
- 链接：[arXiv](https://arxiv.org/abs/2611.16748) · [PDF](https://arxiv.org/pdf/2611.16748) · [HF](https://huggingface.co/papers/2611.16748)

Video generation models produce visually realistic videos but still struggle with physical dynamics and causal consistency. Learning from generated videos requires fine-grained physical supervision, yet reliable quality judgments, correction pairs, and controlled variations are difficult to obtain. Large language models (LLMs) possess physical knowledge, but struggle to reliably guide video generation models in…

## 2. SO-Arena: Benchmarking the Capability Spectrum and Reliability of System One Models

- 分数：36.0  ·  HF 赞：82  ·  来源：huggingface
- 兴趣命中：reasoning, evaluation, benchmark, spec
- 作者：Lichen Li, Ziping Dong, Sicheng Feng, Qi Li, Xinchao Wang
- 链接：[arXiv](https://arxiv.org/abs/2611.15777) · [PDF](https://arxiv.org/pdf/2611.15777) · [HF](https://huggingface.co/papers/2611.15777)

System One models promise fast, general-purpose decision-making without lengthy token generation. However, understanding their capability spectrum and decision reliability requires more than aggregate performance on current benchmarks. Existing evaluations often provide limited insight into the breadth of model capabilities and the reliability of their decisions. We introduce SO-Arena, a benchmark characterizing the…

## 3. BirdDreams: Joint Perspective and BEV Video Generation for a Plausible, Reactive Driving World Model

- 分数：32.0  ·  HF 赞：48  ·  来源：huggingface
- 兴趣命中：evaluation, spec
- 作者：Junyoung Seo, Jaewoo Seo, Seungryong Kim, Laura Leal-Taixé, Xiuming Zhang, Seung Wook Kim
- 链接：[arXiv](https://arxiv.org/abs/2611.14815) · [PDF](https://arxiv.org/pdf/2611.14815) · [HF](https://huggingface.co/papers/2611.14815)

Driving world models aim to simulate how a scene unfolds under different ego actions. This requires plausible motion of surrounding vehicles as well as precise ego-trajectory control. Learning vehicle motion from perspective video alone is challenging because motion is entangled with appearance and vehicles can be occluded. Prior work therefore conditions video generation on layouts that specify vehicle motion,…

## 4. Duo: A Reciprocal World Model for Full-Duplex Interaction

- 分数：31.0  ·  HF 赞：38  ·  来源：huggingface
- 兴趣命中：reasoning, spec
- 作者：Hengyuan Cao, Biao Gong, Guoshan Lu, Qiyuan Zhang, Lin Liu, Yiding Tian, Yilei Jiang, Yuxin Ma, Chengzhang Wu, Kun Chen, Yiqian Xie, Ting Liu, Xin Zheng, Xijun Gu, Tianren Ma, Jiancheng Pan, Chi Zhang, Xuzhe Zheng, Siyi Li, Zhenzhong Lan
- 链接：[arXiv](https://arxiv.org/abs/2611.15131) · [PDF](https://arxiv.org/pdf/2611.15131) · [HF](https://huggingface.co/papers/2611.15131)

In this report, we introduce the Reciprocal World Model (RWM) and present Duo v1, a full-duplex world model that continuously perceives audiovisual inputs while responding to users in real time. The RWM treats intelligence and physical reality as equally fundamental to what constitutes a world. Existing world models largely focus on simulating the latter, leaving reasoning and decision-making as external controls…

## 5. Actor, Judge, or Teacher? Understanding Decision Models in Long-Horizon Agents

- 分数：31.0  ·  HF 赞：30  ·  来源：huggingface + arxiv
- 兴趣命中：agent, reinforcement learning
- 作者：Haochen Liu, Qianhao Zhu, Zixuan Wang, Dingming Li, Tongbo Chen, Peng Qiu, Yingqi Qu, Weiming Lu, Jun Xiao, Yongliang Shen
- 链接：[arXiv](https://arxiv.org/abs/2611.17167) · [PDF](https://arxiv.org/pdf/2611.17167) · [HF](https://huggingface.co/papers/2611.17167)

Decision models answer a question with a typed output, such as a choice among options with a probability for each, so one model can choose an agent's actions, evaluate actions already taken, or score every action to teach a policy with reinforcement learning. Prior work has studied them mainly as actors, judging their usefulness by how well they act. We ask whether a decision model that acts poorly can still teach…

## 6. G-STAR: Group-Scaled Token Capacity for Deeply Compressed Autoregressive Generation

- 分数：30.0  ·  HF 赞：41  ·  来源：huggingface
- 兴趣命中：benchmark
- 作者：Xu Huang, Ye Huang, Xiaotong Li, Zhengrong Yue, Jialv Zou, Minhao Jing, Haodong Li, Wenhao Yan, Yaxin Luo, Duomin Wang, Daquan Zhou
- 链接：[arXiv](https://arxiv.org/abs/2611.13004) · [PDF](https://arxiv.org/pdf/2611.13004) · [HF](https://huggingface.co/papers/2611.13004)

Discrete autoregressive models offer a scalable framework for image generation. However, they face a fundamental trade-off: long token sequences preserve representation quality but slow generation, while aggressive spatial compression reduces representation capacity. Based on product quantization, we show that, under a fixed nominal information budget, group size should scale quadratically with the per-axis spatial…

## 7. Open Vision Banana: A Fully Open Recipe for Generative Visual Perception

- 分数：30.0  ·  HF 赞：32  ·  来源：huggingface
- 兴趣命中：reasoning, evaluation, coding
- 作者：Arpit Jadon, Valentinos Pariza, Jona Ruthardt, Ryousuke Yamada, A. Sophia Koepke, Andrei Bursuc, Yuki M. Asano
- 链接：[arXiv](https://arxiv.org/abs/2611.15844) · [PDF](https://arxiv.org/pdf/2611.15844) · [HF](https://huggingface.co/papers/2611.15844)

Recent work suggests that pretrained image generators encode real-world understanding beyond image synthesis. Vision Banana exploits this by framing vision tasks as conditional image editing. However, its data, weights, code, and implementation details are not public. We present Open Vision Banana (OVB), a fully open and reproducible recipe for converting pretrained generators into unified multi-task perception…

## 8. On the Design of Hyper-Connections: Simplification, Stability, and Scalability

- 分数：27.0  ·  HF 赞：26  ·  来源：huggingface
- 兴趣命中：memory, language model, spec
- 作者：Xiangdong Zhang, Xiaohan Qin, Sunan Zou, Tuo Dai, Bizhao Shi, Zhuo Xia, Yebin Yang, Yizhou Chen, Yuliang Liu, Yu Cheng, Junchi Yan
- 链接：[arXiv](https://arxiv.org/abs/2611.05984) · [PDF](https://arxiv.org/pdf/2611.05984) · [HF](https://huggingface.co/papers/2611.05984)

Hyper-Connections (HC) architectures are increasingly adopted in frontier language models, yet their components remain insufficiently understood and introduce non-negligible training overhead. In this work, we systematically study the HC architecture to understand its components and identify simpler, more efficient designs. We find that learned read/write gating without mixing and unconstrained mixing with fixed…

## 9. Ropedia Xperience 2: A Gold Standard for Scaling Physical AI Environments and Behaviors

- 分数：27.0  ·  HF 赞：26  ·  来源：huggingface + arxiv
- 兴趣命中：language model
- 作者：Hao Li, Fangzhou Hong, Zhaoxi Chen, Hui En Pang, Kairui Hu, Mingze Sun, Runmao Yao, Xinhao Ji, Xiyuan Zheng, Xuanli Chen, Yalun Dai, Yap Kim Hui, Dingwen Zhang, Yuanyuan Gao, Ziang Cao, Cheng Huang Yean, Jackson Peng, Rui Duan, Yaobo Liu, Zetong Wang, Ziwei Liu
- 链接：[arXiv](https://arxiv.org/abs/2611.17060) · [PDF](https://arxiv.org/pdf/2611.17060) · [HF](https://huggingface.co/papers/2611.17060)

Large foundation models such as GPT-6 Astra and Claude Fable 5.1 have recently been shown to control robots directly from visual observations. They nevertheless remain brittle on long-horizon, contact-rich tasks in real-world environments. Further progress depends on two complementary resources: demonstrations of human behavior that supervise how tasks are performed, and interactive environments in which policies…

## 10. TTB: Test-time Baking for Efficient Rendering of Decoder-only View Synthesis Models

- 分数：26.5  ·  HF 赞：21  ·  来源：huggingface + arxiv
- 兴趣命中：benchmark, coding
- 作者：Chin-Yang Lin, Ryo Hachiuma, Jaesung Choe, Min-Hung Chen, Yu-Chiang Frank Wang, Yen-Yu Lin, Wei-Chen Chiu, Yu-Lun Liu, Cheng Sun
- 链接：[arXiv](https://arxiv.org/abs/2611.17331) · [PDF](https://arxiv.org/pdf/2611.17331) · [HF](https://huggingface.co/papers/2611.17331)

Decoder-only Large View Synthesis Models (LVSMs) with KV-cache have recently achieved state-of-the-art quality by regressing novel views from neural networks without reconstructing 3D geometry, while Test-Time Training (TTT) layers save computation but sacrifice quality. We propose Test-Time Baking (TTB), a strategy that learns to bake global scene information from cross-view attention into a lightweight MLP,…

## 11. Unbundling Multimodal Vision Encoding

- 分数：24.5  ·  HF 赞：13  ·  来源：huggingface + arxiv
- 兴趣命中：benchmark, language model, coding
- 作者：Ellis Brown, Chris Hoang, Shengyi Qian, Shang-Wen Li, Mike Lewis, Marjan Ghazvininejad, Luke Zettlemoyer, Lucas Beyer, Mengye Ren, Jakob Verbeek, Saining Xie, Hu Xu
- 链接：[arXiv](https://arxiv.org/abs/2611.17334) · [PDF](https://arxiv.org/pdf/2611.17334) · [HF](https://huggingface.co/papers/2611.17334)

How multimodal language models should encode visual input remains up for debate. Most models use a pretrained vision encoder, while some recent recipes train the encoder from scratch with the language model or remove it entirely. Vision encoders bundle together three design choices: a visual prior from upstream pretraining, dedicated vision capacity, and pre-fusion placement of that capacity (i.e., before the…

## 12. Factored One-sided Adam-Moment for Practical and Scalable SOAP

- 分数：24.0  ·  HF 赞：12  ·  来源：huggingface + arxiv
- 兴趣命中：memory, language model, large language
- 作者：Jaemyung Yu, Byeongho Heo, Sangdoo Yun, Dongyoon Han
- 链接：[arXiv](https://arxiv.org/abs/2611.16905) · [PDF](https://arxiv.org/pdf/2611.16905) · [HF](https://huggingface.co/papers/2611.16905)

Second-order optimizers (e.g., Shampoo, SOAP) have emerged as compelling alternatives to Adam/AdamW and promise faster per-step convergence than AdamW in transformer training. However, they still remain costly in practice, and even SOAP still pays substantial optimizer-state memory and eigendecomposition overhead. We ask whether the benefits of SOAP can be retained at nearly the efficiency of AdamW. In this paper,…

## 13. Learning the Task or Learning the Verifier? Rethinking Criteria Exposure in Embodied Self-Improvement

- 分数：23.5  ·  HF 赞：15  ·  来源：huggingface
- 兴趣命中：agent, benchmark, coding, spec
- 作者：Wenbo Huang, Jianxin Bi, Shunyu Yang, Ruiyang Si, Rui Ni, Qiang Wang, Shulong Jiang, Yintianrun Zhang, Feixiang Ruan, Kewei Zhang, Ye Huang, Shukai Gong, Daquan Zhou
- 链接：[arXiv](https://arxiv.org/abs/2611.08318) · [PDF](https://arxiv.org/pdf/2611.08318) · [HF](https://huggingface.co/papers/2611.08318)

Self-improving embodied agents are increasingly being developed and compared on robot simulation benchmarks. Several recent works expose the benchmark's success criteria to the learning agent, a practice we call Criteria Exposure (CE). These criteria, originally written to verify policies trained by imitation learning, often demand more than the corresponding language instructions, so a score from such a verifier…

## 14. WorldDraft: If Code Builds the World, Can Video Models Just Render It?

- 分数：23.0  ·  HF 赞：14  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark, coding, spec
- 作者：Zhiyu Hou, Wen-Jie Shu, Harold Haodong Chen, Weilin Ruan, Chenfei Liao, Liuzhou Zhang, Disen Lan, Xiaogang Xu, Qi Chen, Ser-Nam Lim
- 链接：[arXiv](https://arxiv.org/abs/2611.16217) · [PDF](https://arxiv.org/pdf/2611.16217) · [HF](https://huggingface.co/papers/2611.16217)

Multimodal coding agents decouple 4D world construction from visual generation, repurposing video models from world generators toward generative renderers. This division of labor raises a fundamental question: if code builds the world, can video models just render it? A reliable generative renderer hinges on two complementary criteria: (i) world preservation, retaining prescribed 4D kinematics and camera paths; and…

## 15. Experience-Handoff Reinforcement Learning for Recursive Self-Improvement

- 分数：21.0  ·  HF 赞：2  ·  来源：huggingface + arxiv
- 兴趣命中：agent, reinforcement learning, benchmark, language model, large language, spec
- 作者：Doyoung Kim, Byeongguk Jeon, Kailin Zhang, Sherry Yang
- 链接：[arXiv](https://arxiv.org/abs/2611.16409) · [PDF](https://arxiv.org/pdf/2611.16409) · [HF](https://huggingface.co/papers/2611.16409)

It is common to train Large Language Models (LLMs) for agentic tasks with Reinforcement Learning (RL) from scalar rewards. However, this throws away the fine-grained information about the environment that the agent experienced during the trial (e.g., error logs). To utilize this rich information, recent works wrap the agent in a harness that refines its own inputs through reflection or compaction and hands past…

## 16. The Value of Thinking: Learning When to Reason in Hybrid Decision Models

- 分数：19.0  ·  HF 赞：2  ·  来源：huggingface + arxiv
- 兴趣命中：agent, reasoning, spec
- 作者：Zhengxu Yu, Ke Xu, Meng Fang, Haitham Ammar, Weilin Luo, Jun Wang
- 链接：[arXiv](https://arxiv.org/abs/2611.16961) · [PDF](https://arxiv.org/pdf/2611.16961) · [HF](https://huggingface.co/papers/2611.16961)

Existing adaptive-reasoning methods shorten the explicit reasoning a model writes, or skip it by switching modes; either way the answer is still written out token by token. \emph{Rather than deciding how much to think}, we explore a different paradigm, \emph{zero-or-$T$ thinking}: a single model either answers from the implicit thinking inside one forward pass, generating no token, or performs full autoregressive…

## 17. Who Remembers What? Multi-Granularity Memory Extraction for Multi-User, Multi-Agent Interaction

- 分数：18.5  ·  HF 赞：5  ·  来源：huggingface
- 兴趣命中：agent, memory, evaluation, benchmark
- 作者：Yunzhe Wang, Mesut Erhan Unal, Sheng Zhang, Shabnam Ghadar, Peng Tang
- 链接：[arXiv](https://arxiv.org/abs/2611.10439) · [PDF](https://arxiv.org/pdf/2611.10439) · [HF](https://huggingface.co/papers/2611.10439)

Self-evolving agents improve their own skills, memory, and harness code from experience without retraining the base LLM, and group-evolving agents go further by sharing these lessons across agents. Yet most such systems overlook that sharing across users and heterogeneous agents requires deciding who can benefit from each lesson and what information must remain private. We present MixUA, a memory system that…

## 18. UniSpark: Exploring Hybrid Attention for Multimodal Understanding and Generation

- 分数：18.0  ·  HF 赞：12  ·  来源：huggingface + arxiv
- 兴趣命中：-
- 作者：Jiancheng Pan, Yuzheng Liu, Hengyuan Cao, Qiyuan Zhang, Yangyan Li, Biao Gong, Zheng Zhang, Ka Long Cheng, Xinyang Wang, Yujun Shen
- 链接：[arXiv](https://arxiv.org/abs/2611.16517) · [PDF](https://arxiv.org/pdf/2611.16517) · [HF](https://huggingface.co/papers/2611.16517)

We present UniSpark-9B, a unified multimodal model that investigates hybrid attention for visual understanding and generation. Built on a Mixture-of-Transformer-Experts backbone with approximately 9B parameters in each branch, UniSpark combines full attention for explicit token interactions with GatedDeltaNet linear attention for compact context propagation. Autoregressive text prediction and visual flow matching…

## 19. Agent-R^2: Scaling Agents for Realistic Productivity Work via Real-Source Data Synthesis

- 分数：17.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：agent, tool use, reasoning, reinforcement learning, evaluation, language model, large language, spec
- 作者：Teng Pan, Zixuan Wang, Yuchen Yan, Qifei Wu, Yao Chen, Yingqi Qu, Ruiqing Zhang, Yongliang Shen
- 链接：[arXiv](https://arxiv.org/abs/2611.08219) · [PDF](https://arxiv.org/pdf/2611.08219) · [HF](https://huggingface.co/papers/2611.08219)

Large language models have made rapid progress in agentic reasoning and tool use, raising expectations for agents that can take over realistic productivity work from humans. However, current agents still struggle to finish such tasks, where success requires following long-horizon professional workflows, understanding heterogeneous file contexts, and producing usable deliverables under fine-grained requirements. A…

## 20. HiVe-Mem: Interleaving Horizontal Memory Expansion and Vertical Evidence Composition for Multimodal Agents

- 分数：17.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：agent, memory, benchmark, retrieval
- 作者：Haozhen Zhang, Bohan Liu, Jianzhu Bao, Qingyuan Liu, Haodong Yue, Xiao Li, Zi Pong Lim, Wenya Wang
- 链接：[arXiv](https://arxiv.org/abs/2611.12872) · [PDF](https://arxiv.org/pdf/2611.12872) · [HF](https://huggingface.co/papers/2611.12872)

As multimodal agents accumulate increasingly long interaction histories, effectively retrieving and utilizing past information becomes critical for long-term interaction. Existing memory systems typically rely on semantic retrieval over compressed memories and expose predefined representations, which may miss relevant memories and overlook heterogeneous evidence needs across queries. We introduce \hivemem, a…

## 21. The Narrative Gap: Can LLMs Help Us Navigate Diverse Narratives Across Languages?

- 分数：17.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：benchmark, language model, large language, spec
- 作者：Nikhil Sharma, Kelly Marchisio, Kenton Murray, Ziang Xiao
- 链接：[arXiv](https://arxiv.org/abs/2611.12750) · [PDF](https://arxiv.org/pdf/2611.12750) · [HF](https://huggingface.co/papers/2611.12750)

Large language models (LLMs) increasingly mediate how people seek and consume information, including accounts that differ across languages and regions, especially on contested topics. Supporting diverse information seeking requires models to help users navigate competing narratives across languages and information streams. We define six capabilities necessary for diverse multilingual information seeking: three…

## 22. From Large Language Models to Efficient System One Models via Adaptive Computation

- 分数：17.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：benchmark, language model, large language, spec
- 作者：Minh-Anh Nguyen
- 链接：[arXiv](https://arxiv.org/abs/2611.16321) · [PDF](https://arxiv.org/pdf/2611.16321) · [HF](https://huggingface.co/papers/2611.16321)

Transferring LLMs into System One decision models typically replaces the language modeling head with a decision head while retaining the full backbone, making every decision pay for all layers. Yet it remains unclear how much depth such decisions require. We find that decision information is concentrated in intermediate layers, with early layers building essential features and the final six layers removable without…

## 23. JustRUA: A Controlled Study of GPT-6 Robot-Use Agents

- 分数：15.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：agent, benchmark, spec
- 作者：Zefan Wang, Yufan Dang, Xuanwei Shi, Mingqi Gao, Cheng Yin, SikYuen Tam, Hanyu Liu, Yasheng Wang, Yaxi Lu, Songyang Zhang, Xin Cong, Yuan Yao
- 链接：[arXiv](https://arxiv.org/abs/2611.16009) · [PDF](https://arxiv.org/pdf/2611.16009) · [HF](https://huggingface.co/papers/2611.16009)

GPT-6 Astra can drive a robot arm directly through a fixed harness, and scores of such robot-use agents on RoboDojo have risen quickly since. Reported systems differ in harness and test subset and often change several designs at once, so it is hard to tell which choices produce the gains. We take these designs apart and test them in one framework, along the harness around the model, the action interface, the reuse…

## 24. Consensus Capture in Reference-Based UAV Video Stabilization: A Benchmark on Dynamic Urban Scenes

- 分数：15.5  ·  HF 赞：3  ·  来源：huggingface + arxiv
- 兴趣命中：benchmark
- 作者：Robert Fonod, Nikolas Geroliminis
- 链接：[arXiv](https://arxiv.org/abs/2611.17190) · [PDF](https://arxiv.org/pdf/2611.17190) · [HF](https://huggingface.co/papers/2611.17190)

Reference-frame stabilization registers every frame of a hovering-drone video onto one reference frame, keeping object positions comparable. The registration pipelines it relies on are selected on feature-matching benchmarks in which only the camera moves. Over a busy intersection, vehicles moving together supply mutually consistent correspondences that can draw the robust homography estimate toward their motion:…

## 25. DeepStress: Stress-Testing Deep Search Agents

- 分数：15.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：agent, benchmark, retrieval
- 作者：Ismael Rousseau, Geraldine Damnati, Frederic Bechet
- 链接：[arXiv](https://arxiv.org/abs/2607.13920) · [PDF](https://arxiv.org/pdf/2607.13920) · [HF](https://huggingface.co/papers/2607.13920)

While search agents demonstrate impressive capabilities in multi-step question answering, their robustness to poor-quality evidence remains under-explored. Such evidence is rare in benchmark corpora, and resulting failures are hard to reproduce. We propose DeepStress, a dynamic stress-testing framework that subjects agents to degraded evidence at controlled rates. It replaces the retrieval module with a synthetic…

## 26. EgoX: Egocentric Cross-Embodiment Manipulation with Embodiment Dreaming

- 分数：14.5  ·  HF 赞：1  ·  来源：huggingface + arxiv
- 兴趣命中：agent
- 作者：Yaru Niu, Binghong Chen, Changwei Yao, Shangtao Li, Zhenlong Fang, Revanth Krishna Senthilkumaran, Shuai Zhou, Yuemin Mao, Kalie Ching, Po-Ju Chao, Yudong Luo, Peiqi Yu, Heng Zhang, Hao Zhang, Bingqing Chen, Chen Qiu, H. Eric Tseng, Ye Yuan, Umar Iqbal, Changliu Liu, Jonathan Francis, Ding Zhao
- 链接：[arXiv](https://arxiv.org/abs/2611.16728) · [PDF](https://arxiv.org/pdf/2611.16728) · [HF](https://huggingface.co/papers/2611.16728)

Generalist manipulation policies can benefit from the complementary experience of humans, real robots, and simulated agents. However, differences in morphology, sensing, and control interfaces make it difficult to learn effectively from their combined demonstrations. We introduce EgoX, an egocentric cross-embodiment learning framework that organizes heterogeneous demonstrations through semantically corresponding…

## 27. Evidence-Guided Recovery for AI Agents with Ambiguous Tool Outcomes and Partial Execution

- 分数：13.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：agent, planning
- 作者：Genliang Zhu, Xiaobo Chen, Ziyuan Wang, Chu Wang
- 链接：[arXiv](https://arxiv.org/abs/2610.41453) · [PDF](https://arxiv.org/pdf/2610.41453) · [HF](https://huggingface.co/papers/2610.41453)

Tool timeouts can leave AI agents facing ambiguous tool outcomes and partial execution: an action may have failed, committed or remained in flight while other workflow steps have already completed. We formulate evidence-guided task recovery over approved obligations, provider capabilities and states compatible with public evidence. A shared admissibility check handles key expiry, authorization timing, dependencies…

## 28. Do Multimodal Models Decide Consistently on Equivalent Optical Spectra?

- 分数：13.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：language model, spec
- 作者：Ziyuan Wang, Genliang Zhu, Xiaobo Chen
- 链接：[arXiv](https://arxiv.org/abs/2611.00428) · [PDF](https://arxiv.org/pdf/2611.00428) · [HF](https://huggingface.co/papers/2611.00428)

A spectrum can be given to a model as a table in nanometers or as a plot in photon energy, and the decision should not depend on which one it sees. When the data needed for an answer are missing, the model should say so. We test representation invariance and abstention on measured optical spectra of silicon metasurfaces (MOCLIP) and gold nanoparticles, with labels computed from the data. Each spectrum is shown as…

## 29. Back to Pixels: Lifting Latent Video Diffusion into Pixel Space

- 分数：13.0  ·  HF 赞：2  ·  来源：huggingface + arxiv
- 兴趣命中：-
- 作者：Yanke Song, Shuo Chen, Chris Rockwell, Guande He, Nan Liu, Desai Xie, Tianpei Gu, Yong-Hyun Park, Aryan V S, Dennis Yuren Menn, Ming-Hsuan Yang, Xun Huang
- 链接：[arXiv](https://arxiv.org/abs/2611.17336) · [PDF](https://arxiv.org/pdf/2611.17336) · [HF](https://huggingface.co/papers/2611.17336)

Frontier video generation models work in a VAE latent space that compresses video in both space and time. This compression made training tractable, but now limits high-resolution, controllable, and interactive generation -- doubling resolution quadruples token count, conditions apply to groups of frames rather than individual ones, and each response must wait for the rest of its multi-frame block. We present PixVid,…

## 30. A Cross-Scenario Survey and Analysis of Self-Evolving Multimodal Agents

- 分数：12.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：agent, reasoning
- 作者：Jingjing Jiang
- 链接：[arXiv](https://arxiv.org/abs/2611.14256) · [PDF](https://arxiv.org/pdf/2611.14256) · [HF](https://huggingface.co/papers/2611.14256)

Recent work shows that multimodal agents increasingly self-improve without recurring human annotation. However, each self-improvement mechanism is designed and evaluated within a single scenario, leaving its preconditions unverified under cross-scenario transfer. This survey investigates the structural source of asymmetric mechanism transfer across four scenarios: multimodal reasoning, multimodal generation, GUI and…

## 31. A frontier machine intelligence for human neuroimaging

- 分数：12.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：language model, spec
- 作者：Chenhui Zhao, Akshay Rao, Akhil Kondepudi, Yiwei Lyu, Xinhai Hou, Rikhil Seshadri, Cheng Jiang, Soumyanil Banerjee, Rushikesh Joshi, Samir Harake, Ashok Srinivasan, Shruti Mishra, Francisco Rivas-Rodriguez, Seunghong Rhee, Nathaniel Roddenberry, Neeraj Chaudhary, Zach Wilseck, Paul Park, Honglak Lee, Vikas Gulani, Aditya Pandey, Todd Hollon
- 链接：[arXiv](https://arxiv.org/abs/2611.15094) · [PDF](https://arxiv.org/pdf/2611.15094) · [HF](https://huggingface.co/papers/2611.15094)

Medical imaging is essential for diagnosing disease, guiding treatment and monitoring patients over time. Although artificial intelligence has advanced image interpretation, existing medical models often address restricted tasks, while general-purpose proprietary models lack access to private clinical imaging required to achieve medical expertise. Developing models that can interpret complex examinations and…

## 32. TurtLES: A Large-Scale Benchmark for Turbulent 3D Neural PDE Surrogates

- 分数：12.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：benchmark
- 作者：Jarno Platenburg, Armand Kassaï Koupaï, Paola Cinnella, Patrick Gallinari
- 链接：[arXiv](https://arxiv.org/abs/2611.09567) · [PDF](https://arxiv.org/pdf/2611.09567) · [HF](https://huggingface.co/papers/2611.09567)

Machine-learning surrogates are increasingly used to accelerate computational fluid dynamics, yet progress is limited by the lack of benchmarks capturing realistic, time-dependent turbulent flows. We introduce TurtLES, a 14 TB dataset of 3D turbulent cylinder wakes in the shear-layer transition regime, computed via high-fidelity implicit large-eddy simulations. The dataset contains 400 trajectories of 400 time steps…

## 33. Structured Confidence Perturbation via Fisher Geometry for Adversarial Training

- 分数：11.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：spec
- 作者：Chenlong Wei, Hanling Wang, Chong Zhang, Qinkai Yu, Fangyu Wu, Xiaobo Jin
- 链接：[arXiv](https://arxiv.org/abs/2611.14046) · [PDF](https://arxiv.org/pdf/2611.14046) · [HF](https://huggingface.co/papers/2611.14046)

Adversarial training is often plagued by "pseudo-attacks", perturbations that significantly increase the loss value but fail to truly alter the model's confidence structure. To address this, we propose two complementary approaches to directly attack and defend against confidence structure deformation. First, building upon the traditional loss maximization perspective, we introduce a hybrid objective that integrates…

## 34. Humanized but Still True? Auditing Facts and Detection in AI-Text Humanizers

- 分数：9.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：-
- 作者：Ziyuan Wang, Genliang Zhu, Xiaobo Chen
- 链接：[arXiv](https://arxiv.org/abs/2611.00359) · [PDF](https://arxiv.org/pdf/2611.00359) · [HF](https://huggingface.co/papers/2611.00359)

AI "humanizers" rewrite machine-generated text so that detectors classify it as human-written. Public leaderboards score evasion and embedding similarity, but not whether checkable details survive. We check whether numbers, dates, person and organization names, and quoted spans survive each rewrite, using a rule-based checker validated by two AI annotators (precision 0.84-1.00, recall 0.93-0.95; no human…

## 35. Bait: Mitigating Harmful Agentic Reinforcement Learning via Probing Reward Function

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reinforcement learning, language model, large language, spec
- 作者：Tiansheng Huang, Ananth Balashankar, Virat Shejwalkar, Santosh Pande, Ling Liu
- 链接：[arXiv](https://arxiv.org/abs/2611.16369) · [PDF](https://arxiv.org/pdf/2611.16369) · [HF](https://huggingface.co/papers/2611.16369)

We expose a safety vulnerability on nascent agentic reinforcement-learning-as-a-service. Specifically, with a cost as low as \$20, we show that safety alignment of a large language model (e.g., Inkling) can be completely subverted through rounds of harmful agentic reinforcement learning (agentic RL) with a toxic environment from its users. We also demonstrate that upon a successful harmful agentic RL attack via the…

## 36. Evidence-Governed Adoption of Self-Generated Updates in Autonomous AI Agents

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, evaluation, spec, planning
- 作者：Subodh Lonkar
- 链接：[arXiv](https://arxiv.org/abs/2611.16378) · [PDF](https://arxiv.org/pdf/2611.16378) · [HF](https://huggingface.co/papers/2611.16378)

Autonomous agents modify prompts, memories, tools, workflows, and policies using interaction histories. Yet a plausible modification is not necessarily suitable for persistent adoption: candidate selection is adaptive, evaluators may be imperfect, and local gains can hide degradation against an earlier baseline. We introduce Evidence-Governed Evolution (EGE), a framework for governing adoption of self-generated…

## 37. Beyond Compressing Everything: Contrastive Memory Learning for Selective Context Compression

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, benchmark, language model, large language
- 作者：Sikui Zhang, Haowei Liu, Ziyun Gan, Chunfeng Yuan, Guangze Gao, Nian Liu, Boyu Cai, Bo Li, Xiaolei Lv, Jun Gao, Bing Li, Weiming Hu
- 链接：[arXiv](https://arxiv.org/abs/2611.16384) · [PDF](https://arxiv.org/pdf/2611.16384) · [HF](https://huggingface.co/papers/2611.16384)

As large language models (LLMs) advance toward increasingly long inputs, soft context compression offers a promising approach to efficient inference by converting long inputs into compact memory slots. Under limited memory budgets, effective context compression remains challenging because task-relevant evidence varies substantially across queries, ranging from localized evidence to multiple distant spans or…

## 38. Teach with Blinks: Breaking Linguistic Momentum in On-Policy Distillation for Fine-Grained Multimodal Perception

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, benchmark, language model, large language
- 作者：Tangzheng Lian, Hang Zhang, Guanyu Hu, Renjiu Hu, Zhensong Zhang, Jiankang Deng, Jifei Song
- 链接：[arXiv](https://arxiv.org/abs/2611.16402) · [PDF](https://arxiv.org/pdf/2611.16402) · [HF](https://huggingface.co/papers/2611.16402)

On-policy distillation (OPD) has emerged as an effective post-training approach to improving fine-grained perception in multimodal large language models by amortizing costly inference-time zooming operations into a single-pass recipe. However, vanilla OPD is inherently susceptible to linguistic momentum: the teacher can follow the student's erroneous prefixes, thus weakening corrective supervision. To address this,…

## 39. Gravity and Flight: Learning to Navigate Fine-Grained Remote Sensing Scenes

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, evaluation, language model, spec
- 作者：Yuheng Zong, Minghua Wang, Xin Zhao, Xiaobin Liu, Yongjian Dong, Chanho Eom
- 链接：[arXiv](https://arxiv.org/abs/2611.16408) · [PDF](https://arxiv.org/pdf/2611.16408) · [HF](https://huggingface.co/papers/2611.16408)

Vision-language models are increasingly capable, yet their reasoning in complex remote sensing scenes can remain coarse-grained and insufficiently grounded in task-relevant visual evidence. We propose Gravity and Flight (G&F), a framework for scene specialization with limited supervision that separates visual and reasoning verification while coupling policy updates. It combines Evidence-of-Thought supervised…

## 40. RICapBench: A Fine-Grained Visual Understanding Benchmark Dataset for Vision-Language Models in Remote Sensing

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, language model, spec
- 作者：Xue Wang, Yubin Xu, Kun Tan
- 链接：[arXiv](https://arxiv.org/abs/2611.16413) · [PDF](https://arxiv.org/pdf/2611.16413) · [HF](https://huggingface.co/papers/2611.16413)

Advances in vision-language models (VLMs) have improved remote sensing image analysis and supported geospatial decision-making. However, fine-grained understanding of remote sensing imagery remains challenging for VLMs. Large variations in object scale, complex geospatial relations among instances, and limited visual detail hinder precise instance localization, visible attribute identification, and spatial relation…

## 41. Small Language Models for Inference-Capability Routing: Effects of Model Capacity and Prompt Optimization on Downstream Quality and Efficiency

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：tool use, reasoning, evaluation, language model, large language, spec, retrieval
- 作者：Sailendra Kolluru, Maheshkumar Duvvarapu
- 链接：[arXiv](https://arxiv.org/abs/2611.16414) · [PDF](https://arxiv.org/pdf/2611.16414) · [HF](https://huggingface.co/papers/2611.16414)

Optional reasoning, retrieval, web search, and tool use can improve large language model responses but incur unnecessary computation when activated indiscriminately. This study investigates whether prompt optimization can compensate for limited router capacity and whether classification gains translate into downstream efficiency. The proposed framework uses prompt-driven small language models to make four…

## 42. daVinci-Prover: Agent-Native Mid-Training for Formal Theorem Proving

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, memory, benchmark, language model, large language
- 作者：Wenhong Zhu, Xuefeng Li, Jiashuo Zhang, Yu Chen, Tiantian Mi, Qipeng Guo, Pengfei Liu
- 链接：[arXiv](https://arxiv.org/abs/2611.16433) · [PDF](https://arxiv.org/pdf/2611.16433) · [HF](https://huggingface.co/papers/2611.16433)

Advances in large language models (LLMs) are rapidly transforming formal theorem proving. Yet further progress remains constrained by the lack of a transparent and effective data recipe for systematically improving theorem-proving models. In this work, we argue that effective agentic provers require strong mathematical skill priors to ground theorem proving and agentic trajectories to enable long-horizon,…

## 43. Fine-Tuned Small Language Model for Synthetic Clinical Data Generation and Predictive Healthcare Analytics

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, language model, large language, spec
- 作者：Mihnea Sebastian Burlacu, Ionut Anghel, Tudor Cioara
- 链接：[arXiv](https://arxiv.org/abs/2611.16460) · [PDF](https://arxiv.org/pdf/2611.16460) · [HF](https://huggingface.co/papers/2611.16460)

The reduced availability of medical datasets represents an important challenge in the development of predictive models for remote healthcare solutions, especially when the available data are imbalanced or difficult to extend through traditional methods. Small Language Models (SLMs) have become a promising alternative to Large Language Models (LLMs) for addressing these limitations due to their lower computational…

## 44. How Should Planning Agents ReSHAPE Their Search Space?

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, benchmark, spec, planning
- 作者：Yilin Zhang, Xinran Zhao, Tong Chen, Ziming Yuan, Tongshuang Wu
- 链接：[arXiv](https://arxiv.org/abs/2611.16466) · [PDF](https://arxiv.org/pdf/2611.16466) · [HF](https://huggingface.co/papers/2611.16466)

Planning agents and benchmarks treat a user's initial specification as fixed. Yet the requests users write exclude plans they would gladly take, since they rarely discover the possible trade-offs they would accept until seeing the options. Agents already revise requests through interaction, but whether this helps planning is unknown. We formalize this step as the ReSHAPE task, which judges a revision by whether its…

## 45. Contain, Conform, Compare (Extended Version): A Red-Teamed Evaluation Kit for Small Coding Agents and the Full Record of Its Experiments

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, evaluation, coding, spec
- 作者：Nguyen Minh Thang
- 链接：[arXiv](https://arxiv.org/abs/2611.16485) · [PDF](https://arxiv.org/pdf/2611.16485) · [HF](https://huggingface.co/papers/2611.16485)

A hosted score in the Gemma 4 Developer Agent competition is one noisy number, so development needs a local evaluator that is fast, safe for agent-written code, and matching the hosted scorer's prompts. drydock-eval evaluates a small coding agent (Gemma 4 E4B) at about 250 runs per hour on one RTX 5090. Contain runs each job in a fresh container without network and passed 200 scripted escape tests; conform provides…

## 46. Time and Space: A Dual-Axis, Evidence-Grounded Context Substrate for Personal Agents

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, evaluation, spec, retrieval
- 作者：Haitao Cheng, Jerry Hu, Longdong Mao, Dong Huang, Dongming Li, Lijuan Zhang, Mengting Zhang
- 链接：[arXiv](https://arxiv.org/abs/2611.16492) · [PDF](https://arxiv.org/pdf/2611.16492) · [HF](https://huggingface.co/papers/2611.16492)

We argue that a binding constraint for personal agents is not model capacity but the form in which context is represented: the agent does not know which entity a phrase denotes, when a fact held, or which source record licenses a claim. We call the missing representation spatio-temporal context (STC) and define it on two axes. The temporal axis carries event time, validity intervals and ingestion time. The spatial…

## 47. ReA-Bench: Benchmarking Responsible Agent Auditing

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, long context, reasoning, benchmark, retrieval
- 作者：Zipeng Ye, Shenyu Dai, Yong Xie, Kun Wang, Jiyang Guan, Zhikai Chen, Jiaqi Weng, Jialing Tao, Hui Xue
- 链接：[arXiv](https://arxiv.org/abs/2611.16493) · [PDF](https://arxiv.org/pdf/2611.16493) · [HF](https://huggingface.co/papers/2611.16493)

As agents perform tasks autonomously in local and cloud environments, auditing their execution trajectories can help service providers identify risks and improve agent harnesses and foundation models. Our analysis of production and red-team trajectories shows that some risks are repeatedly missed across auditing configurations. Overall recall obscures which risks are missed and whether higher recall comes with more…

## 48. A Joint LLM and Optimization Agent Solution for Drone Scheduling in Victim Search Missions

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reasoning, language model, large language
- 作者：Yinghao Zhang, Yalin Liu, Hong-Ning Dai, Yan Zhang, Qubeijian Wang, Bishenghui Tao, Yaohan Li
- 链接：[arXiv](https://arxiv.org/abs/2611.16524) · [PDF](https://arxiv.org/pdf/2611.16524) · [HF](https://huggingface.co/papers/2611.16524)

Victim search in wilderness areas is time-critical. Drones enable rapid area search, but scheduling them is challenging because victims may continue moving, detection results are uncertain, and effective decisions must combine structured mission information with unstructured contextual clues and domain knowledge. To address this, we propose an agent-aided drone scheduling system. The system employs an agent at the…

## 49. ActWorld-JEPA: Action-Conditioned JEPA World Models Meet Latent Planning for End-to-End Autonomous Driving

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, spec, planning
- 作者：Ziying Song, Shengkai Zhang, Caiyan Jia, Lei Yang, Lin Liu, Yuchen Liu, Ziyang Liu, Zirui Li, Gang Wang, Peiliang Wu, Li Wang, Yadan Luo, Chen Lv
- 链接：[arXiv](https://arxiv.org/abs/2611.16579) · [PDF](https://arxiv.org/pdf/2611.16579) · [HF](https://huggingface.co/papers/2611.16579)

Joint-Embedding Predictive Architectures (JEPAs) enable future prediction in latent space without pixel reconstruction. However, latent predictive consistency alone does not establish the relative driving quality of candidate plans. We present ActWorld-JEPA, a joint-embedding formulation for candidate-based driving. Where Plan-Conditioned JEPA (PC-JEPA) uses global and step-wise trajectory intentions to guide…

## 50. Large Language Models as Digital Twins: a Distribution-Aware Questionnaire-Based Evaluation

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, language model, large language, spec
- 作者：Francesco Di Cursi, Chiara Boldrini, Andrea Passarella, Marco Conti
- 链接：[arXiv](https://arxiv.org/abs/2611.16586) · [PDF](https://arxiv.org/pdf/2611.16586) · [HF](https://huggingface.co/papers/2611.16586)

This paper investigates whether Large Language Models can answer a personality questionnaire as a specific individual would. Given a user's social-media posts, the model completes the BFI-2-60 Big Five questionnaire as that user. The predicted responses are converted into trait scores and compared with the user's actual scores. We evaluate GPT-4, Gemma, Llama 3.1, and Mistral on the MyPersonality dataset. To…

## 51. AstroMemBench: A Benchmark for Memory Systems in Embodied Spacecraft Agents

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, memory, evaluation, benchmark, retrieval
- 作者：You Wu, Guhong Zhang, Hongwei Li, Xinyue Hong, Yuan Jia
- 链接：[arXiv](https://arxiv.org/abs/2611.16590) · [PDF](https://arxiv.org/pdf/2611.16590) · [HF](https://huggingface.co/papers/2611.16590)

Long-term spacecraft autonomy requires embodied agents to use operational history under communication delays, time-critical operations, environmental uncertainty, complex physical interactions, power and computational constraints, and safety and reliability requirements. We introduce AstroMemBench and a Scenario-Challenge-Capability design method that maps these requirements to executable memory tests. The benchmark…

## 52. Reducing Batch Makespan for LLM Agent Workloads through Inference-Environment Coordination

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, memory, evaluation, benchmark
- 作者：Wei Feng, Meiling Chen, Boxiao Chen, Lu Liu, Bin Zi, Libin Ye, Xingyu Lu, Lei Xu, Jun Zhou
- 链接：[arXiv](https://arxiv.org/abs/2611.16661) · [PDF](https://arxiv.org/pdf/2611.16661) · [HF](https://huggingface.co/papers/2611.16661)

Efficient batch execution of agent tasks is critical to LLM training and development workflows, including benchmark evaluation, synthetic-data generation, and RL rollouts. Since these tasks alternate between LLM inference and environment interaction, we present coordinated optimizations to reduce batch makespan, the time required to complete all tasks in a batch. For hybrid LLMs, a workload-based resource model…

## 53. MuSeToM: Multi-Sensory Evaluation of Belief Revision with Textual Cues Across Six Senses

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, evaluation, benchmark, language model, large language, spec
- 作者：Chunkit Chan, Kawai Chung, Sze Heng Douglas Kwok, Yuxuan Liu, Yauwai Yim, Tianshi Zheng, Haochen Shi, Qing Zong, Wong Kai Chung, Pak Hin Lau, Calvin Yang, Yifan Gao, Xiaoman Pan, Ginny Wong, Simon See, Yangqiu Song
- 链接：[arXiv](https://arxiv.org/abs/2611.16662) · [PDF](https://arxiv.org/pdf/2611.16662) · [HF](https://huggingface.co/papers/2611.16662)

Theory of Mind (ToM), the ability to infer mental states in others, is pivotal for human social cognition. Existing evaluations of ToM in large language models (LLMs) mainly focus on static belief attribution and false-belief reasoning, leaving a critical aspect of social reasoning underexplored: can LLMs decide whether perceptual evidence is sufficient to justify another person's belief revision? To address this…

## 54. Towards Green Text Generation: Memory-Based Speculative Decoding

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, language model, large language, coding, spec
- 作者：Antal van den Bosch
- 链接：[arXiv](https://arxiv.org/abs/2611.16714) · [PDF](https://arxiv.org/pdf/2611.16714) · [HF](https://huggingface.co/papers/2611.16714)

Speculative decoding accelerates text generation with large language models by letting a cheap draft model propose tokens that a large verifier checks in a single forward pass. We introduce Olifant, a draft model built on a memory-based classifier. It predicts the next token from a four-token window in under 0.3 ms on CPU, requiring no GPU, no backpropagation, and no accelerator memory. We measure throughput and…

## 55. MusicRWKV: A Multimodal RWKV Framework for Music Representation Learning

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, evaluation, benchmark, spec, retrieval
- 作者：Terry Tan
- 链接：[arXiv](https://arxiv.org/abs/2611.16718) · [PDF](https://arxiv.org/pdf/2611.16718) · [HF](https://huggingface.co/papers/2611.16718)

Recent music foundation models have achieved remarkable progress in music representation learning, yet most existing approaches rely on Transformer architectures whose quadratic attention complexity introduces substantial computational and memory overhead when modeling long-duration music recordings. In this work, we propose MusicRWKV, a multimodal music representation learning framework built upon the RWKV…

## 56. Mind the Accuracy-Approval Gap: How Users Evaluate Sycophantic AI in Everyday Tasks

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, language model, large language, spec
- 作者：Wajiha Naveed, Brandon Fain
- 链接：[arXiv](https://arxiv.org/abs/2611.16722) · [PDF](https://arxiv.org/pdf/2611.16722) · [HF](https://huggingface.co/papers/2611.16722)

Large language models (LLMs) often exhibit sycophancy, a tendency to agree with users, flatter or affirm them, and preserve their face, even when independent judgment or critical feedback would be more useful. Prior work has largely evaluated sycophancy through benchmark evaluations, but less is known about how users perceive and respond to sycophantic AI in everyday tasks. We combine benchmark evaluations with two…

## 57. From Foundation VLM to Versatile Driving VLM: A Triplet Incremental Training Approach

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, benchmark, language model, spec, planning
- 作者：Shengtao Wu, Zichao Dong, Weixuan Qiao, Xiaolu Liu, Xin Zhan, Junbo Chen, Jianke Zhu
- 链接：[arXiv](https://arxiv.org/abs/2611.16727) · [PDF](https://arxiv.org/pdf/2611.16727) · [HF](https://huggingface.co/papers/2611.16727)

Adapting general Vision-Language Models (VLMs) to Autonomous Driving (AD) is thought to require heavy 3D spatial priors or intrusive architectural overhauls to compensate for a lack of spatial grounding. In this work, we present a counterintuitive pilot study: off-the-shelf general VLMs already exhibit remarkable adaptability across diverse driving tasks, while precise metric depth remains the primary missing link,…

## 58. Scale-Induced Semantic Shift in Visual Prompt Injection Against VLMs and Web Agents

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, evaluation, benchmark, language model, spec
- 作者：Yiheng Zhao, Runze Ji, Chenyu Yi, Yi Yu, Bingquan Shen, Alex Kot, Xudong Jiang
- 链接：[arXiv](https://arxiv.org/abs/2611.16744) · [PDF](https://arxiv.org/pdf/2611.16744) · [HF](https://huggingface.co/papers/2611.16744)

Visual content in multimedia systems may be resized, compressed, or re-rendered before it is interpreted by a vision-language model. We study a security failure mode in which these transformations change the machine-readable semantics of an image: a textual instruction is not recovered at a $512\times512$ presentation resolution under our evaluation protocol but becomes recoverable after aggressive downsampling. We…

## 59. Evaluating Video LLMs' Understanding of Corner Cases in Autonomous Driving

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, evaluation, benchmark, language model, large language
- 作者：Gabriel Manalu, Minh Son Hoang, Hyeontaek Hwang, Jaesung Lee, Hyojin Choi, Tran Tuan Phong, Seon Kwon Kim, Saad Wazir, Daeyoung Kim
- 链接：[arXiv](https://arxiv.org/abs/2611.16767) · [PDF](https://arxiv.org/pdf/2611.16767) · [HF](https://huggingface.co/papers/2611.16767)

Natural language explanations promised by modern Video Large Language Models (Video LLMs) offer autonomous driving systems a path toward detailed scene description and interpretable decision making on the road. While recent benchmarks have begun assessing these models on driving scenes, they mainly target routine traffic conditions and general comprehension tasks based on existing driving datasets and therefore fail…

## 60. Visual Cipher Bench: Benchmarking LLM Agents on Long-Horizon Visual Reasoning

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reasoning, evaluation, benchmark, coding, spec, planning
- 作者：Deyao Hong, Jiayi Jiang, Yuchun Chen, Yixuan Shi, Wenyi Li, Zheng Jiang, Chengxing Xie, Mingyu Su, Qingle Liu, Mingju Gao, Yizhe Chi, Youjie Zheng, Calvin Xiao, Kaisen Yang, Huan-ang Gao
- 链接：[arXiv](https://arxiv.org/abs/2611.16861) · [PDF](https://arxiv.org/pdf/2611.16861) · [HF](https://huggingface.co/papers/2611.16861)

While language-model agents excel at long-horizon coding and terminal tasks, this success relies on two conditions: explicit text specifications and immediate execution feedback. However, neither condition holds in real-world problems where critical information exists only in images, leaving it unclear whether long-horizon capability transfers from text to visual reasoning. In such visual settings, because rules and…

## 61. DPA: Decentralized Primal Averaging with Quasi-Global Momentum for Highly Heterogeneous Data

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, evaluation, benchmark, spec
- 作者：Diyako Ghaderyan, Stefan Werner
- 链接：[arXiv](https://arxiv.org/abs/2611.16871) · [PDF](https://arxiv.org/pdf/2611.16871) · [HF](https://huggingface.co/papers/2611.16871)

Decentralized training of deep learning models keeps training data local and supports on-device learning over networks. In realistic scenarios, heterogeneity across agents' local data poses an optimization challenge and can severely degrade test accuracy, especially on sparse communication graphs. Building on recent advances in centralized primal averaging, we propose Decentralized Primal Averaging (DPA), a…

## 62. Report of the 8th LSVOS Challenge: Mobile Unified Multimodal Understanding

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, evaluation, language model, coding
- 作者：Chang Liu, Henghui Ding, Tong Yang, Dayoung Kil, Seong-heum Kim, Qilin Xiang, Ronghao Zheng, Ziyang Zhang, Shanlin Jiang, Ruohan Shi, Qilin Fan, Chengfeng Qiu, Kaifeng Wei
- 链接：[arXiv](https://arxiv.org/abs/2611.16925) · [PDF](https://arxiv.org/pdf/2611.16925) · [HF](https://huggingface.co/papers/2611.16925)

This report summarizes the Mobile Unified Multimodal Understanding (MUMU) track of the 8th Large-scale Video Object Segmentation (LSVOS) Challenge, held in conjunction with ECCV 2026. MUMU asks for a single unified model that jointly performs multi-concept image tagging over quality, scene, and event vocabularies, open-vocabulary object detection, and concise image captioning, within a budget of 0.5B parameters and…

## 63. SPADE: Soft Prompts for Ai-text DEtection

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, language model, large language, spec
- 作者：Alex Jiang, Didier Schwab, Chuyuan Li
- 链接：[arXiv](https://arxiv.org/abs/2611.16929) · [PDF](https://arxiv.org/pdf/2611.16929) · [HF](https://huggingface.co/papers/2611.16929)

The easy access to Large Language Models (LLMs) has made AI-generated texts on the web increasingly ubiquitous, making AI-text detection a crucial task. Prompts greatly influence the generation process, but existing detectors focus solely on the generated texts --- supervised methods learn from labeled texts only, and zero-shot methods rely on the text's probability distributions --- ignoring the underlying…

## 64. AnalogLayoutWorld: An Open Benchmark for Agentic Analog Layout Design

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reasoning, benchmark, coding
- 作者： NovaSilicon Team
- 链接：[arXiv](https://arxiv.org/abs/2611.16991) · [PDF](https://arxiv.org/pdf/2611.16991) · [HF](https://huggingface.co/papers/2611.16991)

Coding agents have demonstrated strong capabilities in software development, yet their ability to tackle long-horizon engineering tasks governed by physical constraints remains less understood. We study this question through analog circuit layout, which demands domain knowledge, geometric reasoning, and iterative interaction with design and verification tools. We introduce \textbf{AnalogLayoutWorld}, an open-source…

## 65. Skill Adapter: Personalized Modification and Online Routing of General-Purpose Skills

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reinforcement learning, benchmark, language model, large language, spec
- 作者：Qijia Zhuang, Yanyi Gou, Wenbin Ma, Yuxiang Ren
- 链接：[arXiv](https://arxiv.org/abs/2611.17007) · [PDF](https://arxiv.org/pdf/2611.17007) · [HF](https://huggingface.co/papers/2611.17007)

Large language model (LLM) agents use external skills to reuse task procedures and experience with tools. General-purpose skills describe shared execution procedures, while specific tool choices, operating practices, and output requirements vary across users. In long-horizon tasks, subgoals, available inputs, and environmental states change as execution progresses. Agents must select currently applicable skills from…

## 66. AURA 2.0: From User-Driven Responses to Model-Initiated Conversations in Streaming Video

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, evaluation, benchmark, language model, large language, spec
- 作者：Shuhan Li, Huankang Guan, Xintong Guo, Yang Bo, Yuyang He, Dunyuan Xu, Jingyan Chen, Fang Liu, Tsz Kin Wan, Jinpeng Chen, Zhenqi He, Yuxuan Hu, Wenbo Li, Han Gao, Qijun Li, Long Chen, Hongsheng Li, Rui Liu
- 链接：[arXiv](https://arxiv.org/abs/2611.17048) · [PDF](https://arxiv.org/pdf/2611.17048) · [HF](https://huggingface.co/papers/2611.17048)

Most AI assistants respond only when prompted, remaining silent even when events in the video stream offer meaningful opportunities for conversation. To move beyond purely user-driven interaction, we present AURA 2.0, a streaming video large language model that introduces three core upgrades to AURA. The key advance is Model-Initiated Conversation (MIC), which enables the model to identify topics worth discussing in…

## 67. Auditing AI peer reviewers: a benchmark on real scientific papers

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, evaluation, benchmark, retrieval
- 作者：Íñigo Zubeldia, Boris Bolliet, Francisco Villaescusa-Navarro, Pablo Villanueva-Domingo, Miles Cranmer
- 链接：[arXiv](https://arxiv.org/abs/2611.17052) · [PDF](https://arxiv.org/pdf/2611.17052) · [HF](https://huggingface.co/papers/2611.17052)

LLM-based peer review is now used at production scale, but its evaluation remains limited. We introduce a benchmark that injects objective, localisable errors of four types (general issues, mathematics, numerics, citations) at three severity levels into real papers and measures each reviewer's detection rate by error type and severity, together with its false-positive rate on clean copies. We also present…

## 68. Discovering Effective Agent Memory Designs through Program Evolution

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, memory, evaluation, benchmark
- 作者：Xinheng Ding, Seyyed Saeid Cheshmi, Ziyang Zhang, Tairan Chen, Wenya Xie, Yu Hou, Rui Zhang, Zirui Liu
- 链接：[arXiv](https://arxiv.org/abs/2611.17068) · [PDF](https://arxiv.org/pdf/2611.17068) · [HF](https://huggingface.co/papers/2611.17068)

Program evolution provides a promising approach to discover agent memory designs and study the choices underlying their effectiveness. We introduce MAPE, a framework that evolves whole memory programs from minimal seeds through a standardized lifecycle interface and an iterative diagnosis-proposal loop. Experiments on LoCoMo and LongMemEval yield an absolute accuracy gain of up to 12% over manually designed…

## 69. Paper-Faithful Federated Learning: Scientific Checks for Practitioner and Agent Development

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, evaluation, coding, spec
- 作者：Ali Dadras, Alp Yurtsever
- 链接：[arXiv](https://arxiv.org/abs/2611.17129) · [PDF](https://arxiv.org/pdf/2611.17129) · [HF](https://huggingface.co/papers/2611.17129)

Federated learning experiments can produce reasonable-looking results even when the experiment implementation differs from the intended experimental protocol. Small errors in configuration, data partitioning, aggregation, randomness, evaluation, or checkpoint recovery may therefore affect a comparison without causing the program to fail. We present FedBrew, a research codebase for controlled and reproducible…

## 70. UAV-Flow++: A Unified Suite for Benchmarking and Learning Language-Guided UAV Flight

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, spec, planning
- 作者：Donglin Yang, Xiangyu Wang, Yantong Zhong, Wenhao Zheng, Zihan Ding, Yue Liao, Hongsheng Li, Ke Xu, Si Liu
- 链接：[arXiv](https://arxiv.org/abs/2611.17163) · [PDF](https://arxiv.org/pdf/2611.17163) · [HF](https://huggingface.co/papers/2611.17163)

Language-guided UAV navigation has largely focused on long-horizon route planning, leaving short-range, object-relative flight maneuvers underexplored. To address this gap, we formulate Flying-on-a-Word (Flow), a task requiring a UAV to convert concise natural-language instruction, egocentric visual observation, and current state dynamics into continuous flight actions. Flow encompasses both primitive motion…

## 71. Al-Ghasali: A Computational Framework for Simulating Islamic Jurisprudential Rulings via Finite State Automata and Large Language Models

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, language model, large language, coding
- 作者：Elnaserledinellah Mahmoud Abdelwahab
- 链接：[arXiv](https://arxiv.org/abs/2611.17235) · [PDF](https://arxiv.org/pdf/2611.17235) · [HF](https://huggingface.co/papers/2611.17235)

This paper presents Al Ghasali, a computational framework designed to formalize and simulate Islamic jurisprudential (Fiqh) rulings. Building upon recent set theoretic formalizations of al sabr wa al Taqsim that extract minimal operational rules as simple Horn clause logical programs, this work proves that the semantics of closed Fiqh chapters collapse completely to deterministic Finite State Automata (FSA). We…

## 72. Programming Quantum Circuit Parameters with Large Language Models

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, language model, large language, spec
- 作者：Tiago de Souza Farias, Caio Moraes Porto, Matheus da Silva Fonseca, Nicolas Armando Cabrera Carpi, Anderson de Araujo Oliveira, Celso Jorge Villas-Boas
- 链接：[arXiv](https://arxiv.org/abs/2611.17246) · [PDF](https://arxiv.org/pdf/2611.17246) · [HF](https://huggingface.co/papers/2611.17246)

Large language models (LLMs) have recently demonstrated the ability to generate parameters for variational quantum circuits without conventional optimization. However, the conditions under which this approach is effective remain unclear. Here, we investigate a frozen, general-purpose LLM that generates complete circuit parameter vectors from symbolic circuit and Hamiltonian descriptions, with optional iterative…

## 73. CoReMem: Cost-Internalizing Memory for Successive Coding Tasks with Prospective Valuation

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, memory, coding, spec
- 作者：Peiwen Li, Harshit Verma, Sophia Zhou, Haiwen Wang, Ngoc Bui, Heng Chang, Fei Fei, David van Dijk, Rex Ying
- 链接：[arXiv](https://arxiv.org/abs/2611.17316) · [PDF](https://arxiv.org/pdf/2611.17316) · [HF](https://huggingface.co/papers/2611.17316)

Coding agents tackle successive tasks on an evolving repository, carrying forward edits and writing memory before the next task is known. Selecting memory for unknown next tasks requires balancing future usefulness against the costs of writing and reading it. The actor must also decide when acting on available memory saves effort as the task unfolds. We introduce Coding-Repository Memory (CoReMem), a…

## 74. Learning When Diffusion Language Models Should Regenerate

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, reinforcement learning, benchmark, language model, coding
- 作者：Minhae Oh, Jeonghye Kim, Jinwoo Koo, Yeongoon Kim, Jimin Seo, Minsik Seol, Jungwoo Lee
- 链接：[arXiv](https://arxiv.org/abs/2611.17320) · [PDF](https://arxiv.org/pdf/2611.17320) · [HF](https://huggingface.co/papers/2611.17320)

Remasking allows diffusion language models to revisit generated text, but effective correction requires knowing when and what to revise. Our diagnosis on Sudoku reveals two gaps. Hidden states contain error information that token confidence does not reliably expose, and remasking an isolated error usually reproduces it when the surrounding context remains fixed. These findings motivate DiVR , a verifier that…

## 75. Description-Guided CLIP Adaptation with Local Evidence Calibration for Few-Shot Plant Disease Recognition

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, language model, spec
- 作者：Zhenkun Ye, Qian Zhou, Hua Zou
- 链接：[arXiv](https://arxiv.org/abs/2611.16373) · [PDF](https://arxiv.org/pdf/2611.16373) · [HF](https://huggingface.co/papers/2611.16373)

Accurate plant disease recognition is essential for intelligent agriculture, but few-shot settings provide limited labeled samples that may not capture diagnostic symptoms and intra-class variations. Pretrained vision-language models (VLMs), such as CLIP, offer transferable visual-semantic knowledge. However, existing CLIP-based methods often rely on coarse class semantics and global visual representations,…

## 76. Saidzoda-Kazakh-EmbeddingGemma-300M: How Far One Epoch of Generated Questions Takes a Small Kazakh Embedder

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：language model, spec, retrieval
- 作者：Tohir Saidzoda, Madina Abdusalomzoda, Abubakr Abdullozoda, Amin Jalilov, Faroiz Bobokhon, Aibek Shokanuly
- 链接：[arXiv](https://arxiv.org/abs/2611.16399) · [PDF](https://arxiv.org/pdf/2611.16399) · [HF](https://huggingface.co/papers/2611.16399)

EmbeddingGemma-300M is a small open embedder, and used as released it finds the right passage first for 60.8% of the Kazakh Belebele retrieval questions. We present Saidzoda-Kazakh-EmbeddingGemma-300M, the same model fully fine-tuned for one epoch on 208,511 pairs: 166,263 Kazakh questions that our own language model wrote about source passages from encyclopedias, Wikipedia, news and books, each checked by a second…

## 77. I See What You Want: Decoding Hierarchical Operator Intent from Visual Teleoperation History

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：language model, coding, planning
- 作者：Xiangyi Jia, Kaixian Qu, Shengzhi Wang, Chenyu Yang, Robert Katzschmann, Marco Hutter
- 链接：[arXiv](https://arxiv.org/abs/2611.16419) · [PDF](https://arxiv.org/pdf/2611.16419) · [HF](https://huggingface.co/papers/2611.16419)

Vision-language models (VLMs) have become a powerful foundation for robotic scene understanding, task planning, and language-conditioned control. A natural question follows: can these models also decode what a human operator intends while teleoperating a robot, without any explicit instruction? We formulate this as hierarchical intent prediction, jointly inferring the ongoing atomic action and the broader mission it…

## 78. PhysCapBench: A Cross-Domain Benchmark for Physically Grounded Video Captioning

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, spec
- 作者：Haofeng Wang, Pengcheng Wen, Ruiqi Li, Yuhao Zhang, Tiange Zhang, Boren Zheng, Xuanyi Liu, Siyu Tao, Danni Yu, Gan Lin, Haocheng Tang, Tianzizhe Guo, Mingyuan Su, Boyuan Chen, Zhongyuan Wang
- 链接：[arXiv](https://arxiv.org/abs/2611.16424) · [PDF](https://arxiv.org/pdf/2611.16424) · [HF](https://huggingface.co/papers/2611.16424)

Physical AI aims to learn transferable physical knowledge from real-world experience to understand, predict, and act in the physical world. Internet videos and embodied demonstrations provide complementary observations of motion, interaction, and state evolution. A foundational data challenge is to measure and preserve this physical information as training supervision. In video-language pretraining, captions express…

## 79. RMIT-ADM+S at TREC RAG 2026: Research Agents, Retriever Ablations, and Open-Weight Replication

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, evaluation, retrieval
- 作者：Oleg Zendel, Kun Ran, Chenglong Ma, Nguyen Khoi Vo, Shuai Wang
- 链接：[arXiv](https://arxiv.org/abs/2611.16425) · [PDF](https://arxiv.org/pdf/2611.16425) · [HF](https://huggingface.co/papers/2611.16425)

We describe the RMIT-ADM+S team's participation in the TREC 2026 Retrieval-Augmented Generation (RAG) track using the ClimbMix corpus. We submitted seven research-agent runs using proprietary OpenAI and open-weight models, exploring different retrieval strategies, writer models, and agent workflows. Pre-submission ablations identified writer selection and adjacent-chunk expansion as the main factors affecting answer…

## 80. SoScale: Second-Order Scale Search for FP4 Quantization

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, language model, large language
- 作者：Pengxiang Zhao, Xing Li, Hui-Ling Zhen, Weizhe Lin, Xianzhi Yu, Zhenhua Dong
- 链接：[arXiv](https://arxiv.org/abs/2611.16426) · [PDF](https://arxiv.org/pdf/2611.16426) · [HF](https://huggingface.co/papers/2611.16426)

Low-bit quantization reduces the memory footprint and inference cost of large language models (LLMs), yet accurate FP4 quantization remains challenging. Practical formats such as MXFP4, NVFP4, and HiF4 pair a 4-bit floating-point payload with block-wise or hierarchical scale codes, making accuracy highly sensitive to how each local distribution is scaled. Default maximum-absolute-value scaling preserves dynamic…

## 81. FPSRG: Heterogeneous User Simulation First-Person Post-Training and Multidimensional Semantic Response Grids

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：language model, large language, spec
- 作者：Ruimin Pei, Haibo Liu, Fang Zhang, Xunhua Guo
- 链接：[arXiv](https://arxiv.org/abs/2611.16445) · [PDF](https://arxiv.org/pdf/2611.16445) · [HF](https://huggingface.co/papers/2611.16445)

Simulating heterogeneous individuals with large language models is an active research direction, and heterogeneous user simulation requires models with different characteristics. We study profile construction: given dimensions, items, and scoring rules, build model configurations that can be retrieved by multidimensional target scores. We introduce First-Person Semantic Response Grids (FPSRG). Shared post-training…

## 82. Can an LVLM Perceive Event Boundaries Like a Human?

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, language model
- 作者：Hyolim Kang, Jungsoo Lee, Yeji Song, Whie Jung, Janghoon Cho, Juntae Lee
- 链接：[arXiv](https://arxiv.org/abs/2611.16452) · [PDF](https://arxiv.org/pdf/2611.16452) · [HF](https://huggingface.co/papers/2611.16452)

Large Vision-Language Models (LVLMs) reason effectively about video content, but whether they perceive its event boundaries in a manner consistent with humans remains unclear. We first investigate this through Generic Event Boundary Detection (GEBD), which identifies event boundaries naturally perceived by humans in continuous video, without relying on predefined event categories. On Kinetics-GEBD dataset, LVLMs…

## 83. EvenVLM: A Text and Multimodal Dataset for the Even Language with Vision-Language Fine-Tuning

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, spec
- 作者：Daniil Makovetskii, Ivan Bondarenko
- 链接：[arXiv](https://arxiv.org/abs/2611.16500) · [PDF](https://arxiv.org/pdf/2611.16500) · [HF](https://huggingface.co/papers/2611.16500)

We present EvenVLM, the first text and multimodal (VQA) dataset for Even (Lamut), an endangered Northern Tungusic language spoken by approximately 6,800 people in Siberia. Our dataset comprises 50,521 structured Even-Russian entries extracted from dictionary and phrasebook sources via GPT-4o Mini-based parsing, from which we synthetically generate 107,543 training examples spanning translation, grammar, reading…

## 84. AI has its own style in mathematical proving

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：language model, large language, spec
- 作者：Xiaokai Li, Ziyu Zhou, Qibin Cheng, Yangcheng Wu, An Zeng, Ying Fan
- 链接：[arXiv](https://arxiv.org/abs/2611.16527) · [PDF](https://arxiv.org/pdf/2611.16527) · [HF](https://huggingface.co/papers/2611.16527)

As large language models increasingly generate mathematical proofs, whether they develop a proving style distinct from that of human mathematicians remains an open question. This question is particularly pressing as mathematicians increasingly voice concerns that proofs generated by large language models are difficult to interpret. Here we ask three large language models to independently reprove all 465 propositions…

## 85. HALight: Heterogeneous Multi-Agent Reinforcement Learning for Traffic Signal Control under Lane-Level Missing Observations

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reinforcement learning, spec
- 作者：Chenkai Hu, Yingqian Zhang, Ming Xie, Yi Fang, Chengxiang Jin, Chao Li
- 链接：[arXiv](https://arxiv.org/abs/2611.16574) · [PDF](https://arxiv.org/pdf/2611.16574) · [HF](https://huggingface.co/papers/2611.16574)

Multi-agent reinforcement learning has shown great promise for traffic signal control. However, most existing methods rely on two key assumptions: (i) agents are assumed to be homogeneous with unified observation/action spaces; (ii) full and reliable lane-level traffic observations are available to all agents. In practice, urban road networks exhibit substantial structural heterogeneity (e.g., lane configurations…

## 86. Safety as a Budget: Calibrating the Control Channel of Constrained GRPO for Vision-Language Models

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reinforcement learning, benchmark, language model
- 作者：Bo Han
- 链接：[arXiv](https://arxiv.org/abs/2611.16628) · [PDF](https://arxiv.org/pdf/2611.16628) · [HF](https://huggingface.co/papers/2611.16628)

Reinforcement learning can teach vision-language models (VLMs) to decline harmful image-text requests, but how safe the result becomes is set indirectly, through reward weights found by trial runs. Stating safety as budgets on the rate of harmful assistance and the rate of over-refusal, enforced by Lagrange multipliers inside GRPO with an off-the-shelf scorer as the cost, is the natural fix, and it fails twice. The…

## 87. Asymmetric Multimodal Learning with Decomposed JEPAs

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, benchmark, spec
- 作者：Yusuf Shihata
- 链接：[arXiv](https://arxiv.org/abs/2611.16639) · [PDF](https://arxiv.org/pdf/2611.16639) · [HF](https://huggingface.co/papers/2611.16639)

Cross-modal alignment is the standard objective for building multimodal representations. We show that alignment as a \emph{sole} objective is lossy wherever modalities are informationally asymmetric---where neither can express what the other carries. Visual question answering is an obvious case: a question is a selective relational operator probing a dense visual field whose fine-grained features no query recovers,…

## 88. MobileProbe: Adaptive Security Evaluation of Mobile Agents via Trajectory-Aware Injection

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, evaluation, benchmark
- 作者：Yingbin Jin, Ji'an Wang, HaoYang Chai, Hanjun Luo, Li Hu, Xinfeng Li, Huadi Zheng, PeiZhao Hu, Qingqing Ye, Haibo Hu
- 链接：[arXiv](https://arxiv.org/abs/2611.16693) · [PDF](https://arxiv.org/pdf/2611.16693) · [HF](https://huggingface.co/papers/2611.16693)

Mobile GUI agents read the screen of a phone and operate apps on a user's behalf to complete multi-step tasks such as online shopping or messaging. Because the agent acts on whatever the screen shows, an attacker can embed malicious instructions into ordinary UI content and redirect its actions. We refer to this threat as environmental injection attack (EIA). Existing benchmarks measure this risk by pinning…

## 89. Efficient Periocular Recognition through Model Scaling and Cross Spectral VIS NIR Verification

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, evaluation, spec
- 作者：Fabian Stockhard, Juan E. Tapia, Christoph Busch
- 链接：[arXiv](https://arxiv.org/abs/2611.16764) · [PDF](https://arxiv.org/pdf/2611.16764) · [HF](https://huggingface.co/papers/2611.16764)

Periocular recognition offers an efficient alternative to full-face verification when facial regions are occluded or image resolution is limited. We present AdaEye, a systematic study of input and backbone scaling for periocular verification in visible-spectrum (VIS) and cross-spectral (VIS/NIR) settings. Using an AdaFace-style framework, we compare full-face, masked-face, and dedicated 80x40 periocular inputs while…

## 90. EG360: Efficient and Generalizable $360^\circ$ Depth Estimation via Adaptive Panorama-Perspective Distillation and Spherical Cross-Level Feature Fusion

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, spec
- 作者：Laiyan Ding, Chongxi Meng, Rui Huang
- 链接：[arXiv](https://arxiv.org/abs/2611.16793) · [PDF](https://arxiv.org/pdf/2611.16793) · [HF](https://huggingface.co/papers/2611.16793)

Generalized panorama depth estimation has witnessed great advances in recent years. These methods typically achieve robust zero-shot generalization performance using large pretrained models, but their high computational cost makes real-time inference on embedded platforms challenging. In contrast, previous lightweight panorama models have mostly been developed for single-domain evaluations and cannot generalize well…

## 91. Detection Is Not Early Warning: Evaluating Token-Level Alarms on Language Model Failures

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, language model, spec
- 作者：Marco De Negri, Luca Sartori, Lorenzo Baggi, Moritz Reihs, Eduard Frank Ďurech, Mennatallah El-Assady, Valentina Pyatkin, Anna Hedström
- 链接：[arXiv](https://arxiv.org/abs/2611.16803) · [PDF](https://arxiv.org/pdf/2611.16803) · [HF](https://huggingface.co/papers/2611.16803)

Many failures of language models begin at a specific token, the onset. A monitor that reads the model during generation can classify the finished response, detect the failure once it is under way, or warn before it begins, and only a warning leaves time to stop or steer the generation. Monitors are usually evaluated with response-level metrics such as AUROC, which ignore when the monitor fires. We introduce PREWARN,…

## 92. Calibration and Conformal Prediction for Medical Question Answering in Arabic and English: Evidence from Two Non-Parallel Benchmarks

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, language model, large language
- 作者： Mariya
- 链接：[arXiv](https://arxiv.org/abs/2611.16821) · [PDF](https://arxiv.org/pdf/2611.16821) · [HF](https://huggingface.co/papers/2611.16821)

Large language models (LLMs) are increasingly tested on medical exam questions, but accuracy alone does not show when an answer can be trusted. I study the calibration and uncertainty of two open-weight models, Qwen2.5-7B-Instruct and Jais-adapted-7B-chat (both run in 4-bit precision), on 2,816 English multiple-choice questions from MedMCQA and 4,927 Arabic multiple-choice questions from MedAraBench. Accuracy was…

## 93. A Modular Framework for ESG Prediction through Domain-Specific Language Modeling and Graph Learning

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, language model, spec
- 作者：Sofia Baiocco, Gianluca Bonifazi, Christopher Buratti, Michele Marchetti, Camilla Mazzoli, Federica Parlapiano, Giulia Quaglieri, Davide Traini, Domenico Ursino, Luca Virgili
- 链接：[arXiv](https://arxiv.org/abs/2611.16831) · [PDF](https://arxiv.org/pdf/2611.16831) · [HF](https://huggingface.co/papers/2611.16831)

Environmental, Social and Governance (ESG) scores are increasingly used to evaluate corporate sustainability, supporting investment decisions, ensuring regulatory compliance and assessing risk. However, current ESG evaluations largely rely on proprietary methodologies that often produce inconsistent ratings. This motivates the development of data-driven prediction frameworks. In this paper, we present ESGPred, a…

## 94. Shortcuts or Memorisation? Revisiting Data Corruption in Natural Language Understanding with Large Language Models

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, language model, large language
- 作者：Aarne Talman, Stergios Chatzikyriakidis
- 链接：[arXiv](https://arxiv.org/abs/2611.16843) · [PDF](https://arxiv.org/pdf/2611.16843) · [HF](https://huggingface.co/papers/2611.16843)

Pre-trained encoders fine-tuned on natural language inference (NLI) and other language understanding tasks keep much of their accuracy after the input is perturbed, e.g. by removing all nouns or shuffling the words. Does the same hold for large language models (LLMs), and if so, is it because they have seen the benchmarks during pre-training? In this paper we revisit these perturbation experiments with eight LLMs…

## 95. LLM-Assisted Verification in Dafny

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：language model, large language, spec
- 作者：Wieger Wesselink, Kees Huizing, Huub van de Wetering
- 链接：[arXiv](https://arxiv.org/abs/2611.16886) · [PDF](https://arxiv.org/pdf/2611.16886) · [HF](https://huggingface.co/papers/2611.16886)

Formal verification of complex algorithms requires expertise in program specification, invariant construction, mathematical proof, and the management of automated theorem provers. Although large language models (LLMs) can generate program code and proof fragments, reliably developing complete machine-checked verifications remains challenging: it requires an iterative process of constructing and validating…

## 96. S1-Evo: Experience-Guided Evidence Competition Attacks on Typed System-1 Decision Models

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, benchmark, coding
- 作者：Kaixiang Wang, Junjie Li, Zhaojiacheng Zhou, Jiong Lou, Jie Li
- 链接：[arXiv](https://arxiv.org/abs/2611.16937) · [PDF](https://arxiv.org/pdf/2611.16937) · [HF](https://huggingface.co/papers/2611.16937)

Typed System-1 (S1) decision models are increasingly deployed in LLM agents for routing, moderation, and authorization to cut inference cost, yet untrusted context can still manipulate typed outputs and alter execution branches. Unlike autoregressive System-2 (S2) models, S1 interfaces score dynamic rules and options without token-by-token decoding, mismatching attacks targeting text continuation or explicit…

## 97. Lara Mini Base: Language Diversity as a Resource, Not a Trade-off

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, benchmark, language model
- 作者： Translated, Maria Pia Adinolfi, Isabelle Andrieu, Grazia Fiorella Anfuso, Melania Annunziata, Daniele Antonini, Marta Arena, Luca Barone, Dana Barras Franco, Francesca Basiricò, Francesca Bee, Sofia Bertini, Nicola Bertoldi, Giorgio Biancini, Alessandra Bigi, Giulia Boccalini, Tommaso Bonomo, Enrico Boscardi, Sebastien Bratieres, Francesco Brigante, Giulia Brignola, Romolo Buondestino, Brenda Patricia Byrne, Giorgia Campora, Edoardo Cappelli, Veronica Carascosi, Francesca Carducci, Cody Carlson, Davide Caroselli, Ambra Cascio, Dario Cascio, Mauro Cassani, Andrea Castro, Alessandro Cattelan, Giulia Ceccacci, Paola Cellini, Giulia Chiriatti, Federico Cialini, Valentina Ciarlariello, Daniele Cocozza, Emanuela Coghe, Kathleen Compares, Marco Comunità, Davide Conti, Helen Rebecca Corfield, Michele Cortellessa, Anna Cracco, Aurora Cuppone, Arianna D'Andrea, Maurizio Davoli, Andrea De Angelis, Andrea De Blasi, Rebecca De Giorgi, Annalisa De Petra, Arianna De Pilla, Joris Demiraj, Elena Deufemia, Federica Di Antonio, Pierluigi Di Cianni, Vincenzo Di Cicco, Michela Di Clemente, Alan Di Francesco, Ylenia Di Gese, Federica Di Iulio, Claudia Di Lorenzo, Andrea Di Paola, Giulia Di Pilla, Jessica Dickson, Francesco Elefante, Ilaria Fabrizio, Alessandro Falappa, Viviana Fantozzi, Antonio Farina, Andrea Fernandez Tostado Ro. Diego Andrea, Andrea Ferrari, Sara Ferri, Simona Ferri, Fabio Fioramonti, Stefano Florio, Mariachiara Fornaro, Anna Maria Foti, Niccolò Fransoni, Alessandro Fusacchia, Emma Gamba, Francesco Gasperoni, Davide Gattini, Marta Giani, Claudia Giannetti, Valerio Giannini, Antonella Giudici, Mara Gramendola, Michele Grandinetti, Eleonora Graziani, L'Meese Hope Greaney, Dario Gubernari, Filomena Guglielmi, Jonathan Hammond, Stephen William Harris, Rowena Elizabeth Hogg, Marta Hontanon Del Olmo, Marco Ilari, Kenneth Larry Jackson, Sagar Joshi, Bartosz Alberto Karman, Iuliia Khimenko, Valerio Lanni, Giulio Leonardi, Veronica Levco, Matteo Licci, Alessio Ligios, Noemi Lomartire, Domenico Lupinetti, Jennifer Mirjam Maechtlen, Chiara Maggiori, Maria Luisa Malerba, Francesco Marconi, Domenico Marini, Francesca Marsili, Andrea Martinelli, James Mc Groary, Matteo Menicacci, Andrew Steven Miller, Marco Moauro, Giuliana Molon, Ilaria Mongelluzzi, Emiliano Morghen, Giovanni Moscati, Filippo Musmeci, Flavia Napoleoni, Nicola Giuseppe Ninni, Beatrice Ottoni, Federica Pagliani, Nicolò Palmiero, Daniele Palumbo, Chiara Pantani, Stefano Paolucci, Deborah Paritario, Michela Pascale, Thomas Passera, Daniele Patrioli, Chiara Patrizi, Silvia Patrizi, Giulia Pelos, Simone Giovanni Perone, Cristiano Perrone, Joshua Peterson, Katia Piredda, Francesca Piscitelli, Alessandra Posca, Lorenzo Pratesi, Francesca Prencipe, Daniela Proietto Cuco, Mattia Pupino Marangio, Disheng Qiu, Mirco Ramo, Federica Rapagnà, Waldo Luis Ribeiro, Federico Ricciuti, Alessia Ridoni, Eleonora Risi Valdettaro, Jon Matthew Ritzdorf, Serena Rivera, Federico Roma, Arianna Ruggiero, Eleonora Ruggiu, Mariafrancesca Sagliocco, Vanessa Salvi, Alessio Sampieri, Elena Santanelli, Roberto Sastre, Luca Scofano, Alessandro Sdei, Giuseppe Sebastiani, Claudia Nicole Siegenthaler, Monica Signoretti, Nicola Sobieski, Biancamaria Soellner, Valentina Stati, Michael Stevens, Arianna Stissi, Fabiana Stomaci, Leonardo Taddei, Christopher Thomas, Maurizio Tiberi, John Tinsley, Riccardo Tittarelli, Carla Tocco, Martina Totaro, Barbara Veronika Totzauer, Alessio Tranzocchi, Letizia Treossi, Mara Trombetti, Marco Trombetti, Andrea Valenzi, Kirti Vashee, Giulia Vestita, Teodosio Vezza, Giulia Vignola, Sara Virtuoso, Valentina Volpini, Francesca Vurro, Jolita Zaksauskaite, Giulia Zanarella, Paolo Zanotti, Francesca Zavettieri, Irene Zorzi
- 链接：[arXiv](https://arxiv.org/abs/2611.16956) · [PDF](https://arxiv.org/pdf/2611.16956) · [HF](https://huggingface.co/papers/2611.16956)

General-purpose language models are trained mostly on English: over open models we review, at most, non-English pretraining data makes up only a 12% share. Models built for European languages give them far more, but score well below general-purpose models of the same size. A common concern is that, in small models, languages compete for capacity. We present Lara Mini base, a model trained from scratch on 6T tokens…

## 98. From Delegation to Coordination: Learning Efficient Multi-Agent Deep Research

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reinforcement learning, benchmark
- 作者：Yuyang Wu, Yang Liu, Zequn Xie, Junjie Wang, Dan Yang, Zehao Tan, Ding-Chu Zhang, Junming Yang, Yue Shen, Jian Wang, Jinjie Gu
- 链接：[arXiv](https://arxiv.org/abs/2611.17041) · [PDF](https://arxiv.org/pdf/2611.17041) · [HF](https://huggingface.co/papers/2611.17041)

Multi-agent deep-research systems use delegation to parallelize search and keep long tool traces out of the main agent's context. Yet delegation helps only when task allocation and subtask execution are coordinated: the main agent must issue useful subtasks, while subagents must return reliable evidence. Existing training either optimizes only the main agent or broadcasts the same team advantage to all agents, which…

## 99. Infrastructure for Verifiable AI: Where Proof Costs Go and How Hardware Can Help

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, language model, large language
- 作者：Yihan Xia, Wenxin Xu, Taotao Wang
- 链接：[arXiv](https://arxiv.org/abs/2611.17042) · [PDF](https://arxiv.org/pdf/2611.17042) · [HF](https://huggingface.co/papers/2611.17042)

Users of artificial intelligence services, including those powered by large language models and other transformer-based models, need assurance that inference and training follow the declared computation without exposing private models or data. Zero-knowledge proofs can provide this assurance, but proof generation remains expensive. Hardware acceleration research often reports gains for individual cryptographic…

## 100. A Compact xDAWN-Guided Spatio-Temporal Network with Filter-Bank Convolution for P300 Detection

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, coding, spec
- 作者：Mohammad Mahdi Habibi Bina, Mohammad Reza Daliri
- 链接：[arXiv](https://arxiv.org/abs/2611.17101) · [PDF](https://arxiv.org/pdf/2611.17101) · [HF](https://huggingface.co/papers/2611.17101)

P300-based brain-computer interfaces (BCIs) enable communication by decoding stimulus-evoked EEG responses into character selections without requiring voluntary motor output. Reliable P300 detection remains difficult because of low response amplitude and signal-to-noise ratio, while practical spellers require accurate character selection with few stimulus repetitions and low computational cost. We propose a compact…

## 101. Parameter-Efficient Conciseness Adaptation: Differentiable Length Control for Concise Clinical Reasoning in Smaller Language Models

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, language model, spec
- 作者：Tanzeel Abbas, Ahmad Kamran Malik, Nafees Qamar, Sana Liaqat
- 链接：[arXiv](https://arxiv.org/abs/2611.17128) · [PDF](https://arxiv.org/pdf/2611.17128) · [HF](https://huggingface.co/papers/2611.17128)

Smaller language models (SLMs) make it feasible to deploy clinical natural language processing where large proprietary models are too costly, and parameter-efficient fine-tuning allows them to be specialised on commodity hardware. One obstacle persists after training: on medical tasks these models answer at far greater length than the clinical question requires. In clinical decision support and point-of-care use,…

## 102. Neural Render Proxies for Interactive and Differentiable Lighting

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, evaluation, spec
- 作者：Sergio Sancho, Alexander Rath, Marco Manzi, Pascal Chang, Amit H. Bermano, Derek Nowrouzezahrai, Markus Gross, Marios Papas
- 链接：[arXiv](https://arxiv.org/abs/2611.17185) · [PDF](https://arxiv.org/pdf/2611.17185) · [HF](https://huggingface.co/papers/2611.17185)

Within the CG animation production pipeline, the challenges artists tackle in Lighting can be immense. Even minor adjustments require re-rendering massive scenes with slow offline renderers; global illumination has to be sampled and complex shaders have to be evaluated, leading to iteration times of minutes to hours per frame. To accelerate this process, we introduce a novel neural render proxy (NRP) that enables…

## 103. Scalable Conversational Assessment: Chat-Based Exams with a Two-Agent LLM Pipeline

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reasoning, evaluation
- 作者：Geoffrey Challen, Craig Zilles
- 链接：[arXiv](https://arxiv.org/abs/2611.17220) · [PDF](https://arxiv.org/pdf/2611.17220) · [HF](https://huggingface.co/papers/2611.17220)

Oral exams are compelling because (1) students can be asked to provide their reasoning for an answer and (2) their interactive nature permits follow-up questions to resolve ambiguous answers. But oral exams scale poorly. In this paper, we present scalable conversational assessment, an LLM-based system that conducts interactive text-based conversations with students to assess their ability to make and support an…

## 104. When Both Sides Adapt: The Challenges of Evaluating Interactive LLM Systems

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, spec
- 作者：Hannah Li
- 链接：[arXiv](https://arxiv.org/abs/2611.17239) · [PDF](https://arxiv.org/pdf/2611.17239) · [HF](https://huggingface.co/papers/2611.17239)

In interactive systems where users engage with LLMs, users are adaptive and, after observing LLM responses, can change their prompting strategy, as well as the type and difficulty of subsequent tasks. Thus model responses can influence the set of prompts on which the model is subsequently evaluated. We study the implications of this user adaptivity and prompt endogeneity for the evaluation of LLMs. We define two…

## 105. LiveGeo: Benchmarking Geographic Agents in Continuously Evolving Worlds

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, evaluation, benchmark
- 作者：Pengcheng Zhou, Xuanyu Liu, Yanchen Yin, Tianjie Ju, Bobo Li, Shengqiong Wu, Hao Fei, Mong-Li Lee, Wynne Hsu
- 链接：[arXiv](https://arxiv.org/abs/2611.17267) · [PDF](https://arxiv.org/pdf/2611.17267) · [HF](https://huggingface.co/papers/2611.17267)

We introduce GeoWorld, a controllable and continuously evolving geographic environment platform for LLM agents, and LiveGeo, a benchmark for evaluating reliable decision-making in real-world geographic environments using GeoWorld. Unlike existing evaluations that largely reason and plan over fixed geographic states, GeoWorld is grounded in real-world geographic structure and allows external world states to evolve…

## 106. Negative-Only Policy Optimization for One-Sided Verifiable Rewards

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reinforcement learning, benchmark, spec
- 作者：Jiacheng Xu, Shuo He, Fuxiang Zhang, Chaojie Wang, Bo An
- 链接：[arXiv](https://arxiv.org/abs/2611.17287) · [PDF](https://arxiv.org/pdf/2611.17287) · [HF](https://huggingface.co/papers/2611.17287)

Reinforcement learning with verifiable rewards (RLVR) typically relies on a verifier that can reliably judge whether sampled solutions are correct. However, in many realistic settings, complete verification is generally unavailable, while cheap checks can only falsify failures. We formalize this regime as one-sided verifiability (OSV): verified negatives are reliable counterexamples, but verified positives are…

## 107. Metal Sandbox: Isolated Execution and Command Scheduling for GPU Coding Agents on Apple Silicon

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, evaluation, coding
- 作者：Haozhe Wang, Lina Chen, Fanqi Wan, Qi Han, Yinmin Zhang, Zheng Ge, Daxin Jiang, Junchi Yan
- 链接：[arXiv](https://arxiv.org/abs/2611.17294) · [PDF](https://arxiv.org/pdf/2611.17294) · [HF](https://huggingface.co/papers/2611.17294)

On-device inference requires kernels that make effective use of local accelerators. Efficient training and evaluation of models that generate Apple Metal kernels benefit from native macOS tools and concurrent agent sessions. These sessions alternate between model requests, development commands, and GPU execution, leaving GPU capacity idle for much of a rollout. We present Metal Sandbox, infrastructure that combines…

## 108. Sketching Language Models for Context Attribution

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, language model, retrieval
- 作者：Christopher Liaw, Aranyak Mehta, Grigoris Velegkas, Felix Zhou
- 链接：[arXiv](https://arxiv.org/abs/2611.17313) · [PDF](https://arxiv.org/pdf/2611.17313) · [HF](https://huggingface.co/papers/2611.17313)

Context attribution asks how removing parts of a prompt changes a language model's output. We study leave-one-out (LOO) attribution for a prompt of $n$ tokens and a fixed measurement function. Computing all LOO values directly requires $n$ model evaluations. Under a stability assumption, our algorithm estimates all LOO values to error proportional to $\varepsilon$ with constant probability using…

## 109. K2V: Generative Keyframing For Physically Plausible Video Generation

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, benchmark, language model
- 作者：Felix O'Mahony, Daniel Olmeda Reino, Roberto Cipolla, Ayush Tewari
- 链接：[arXiv](https://arxiv.org/abs/2611.17324) · [PDF](https://arxiv.org/pdf/2611.17324) · [HF](https://huggingface.co/papers/2611.17324)

Video diffusion models are able to generate samples with high-quality appearance and textural qualities. However, content produced by these methods is known to exhibit significant physical errors. This is because, in a classical video generation setting, all physical reasoning must take place simultaneously and exclusively within the diffusion process.We propose to resolve these issues by redistributing the task of…

## 110. Internalizing Investment Mandates: A Neurosymbolic RL Approach to Portfolio Allocation

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reinforcement learning, spec
- 作者：Zeynep Yıldız, Satchit Chatterji, Ercan Atam, Erman Acar
- 链接：[arXiv](https://arxiv.org/abs/2611.17329) · [PDF](https://arxiv.org/pdf/2611.17329) · [HF](https://huggingface.co/papers/2611.17329)

Institutional portfolios operate under investment policy statements that specify asset allocation constraints, often conditioned on market regime information. Deep reinforcement learning has been shown to optimize financial performance but typically does not enforce rule compliance, making it unsuitable for real-world deployment. Existing neurosymbolic methods such as Probabilistic Logic Policy Gradient (PLPG) offer…

## 111. Recursive State-Augmented Language Models: Persistent Latent-State Adaptation of Pretrained Language Models

- 分数：5.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：language model, coding
- 作者：Omer Haq
- 链接：[arXiv](https://arxiv.org/abs/2611.16375) · [PDF](https://arxiv.org/pdf/2611.16375) · [HF](https://huggingface.co/papers/2611.16375)

Language models rely on finite token contexts, limiting access to earlier interactions. We introduce Recursive State-Augmented Language Models (Recursive SALM), a framework in which a persistent latent state evolves with each observation and generates adaptations of a pretrained language model. A modular read-transition-write architecture separates observation encoding, latent dynamics, and predictor adaptation. We…

## 112. RADIANT: Redundancy-Aware Information Allocation for Universal Multi-Modal Fusion

- 分数：5.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, spec
- 作者：Shenghai Wu, Yue Lin
- 链接：[arXiv](https://arxiv.org/abs/2611.16382) · [PDF](https://arxiv.org/pdf/2611.16382) · [HF](https://huggingface.co/papers/2611.16382)

Universal multi-modal fusion often fails not because modalities are insufficiently aligned, but because the fusion process allocates information poorly: redundant evidence is repeatedly amplified, modality-unique evidence is over-smoothed during alignment, and task-dependent synergistic evidence is insufficiently activated. We present RADIANT (Redundancy-Aware Dynamic Information Allocation Network), a task-general…

## 113. TransXplainRRG: A Radiologist-Evaluated LVLM for Chest Radiograph Report Generation

- 分数：5.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, language model
- 作者：Chayan Mondal, Duc-Son Pham, Tele Tan, Ashu Gupta, Vincent T. Y. Tiong, Shreya Ghosh, Tom Gedeon
- 链接：[arXiv](https://arxiv.org/abs/2611.16393) · [PDF](https://arxiv.org/pdf/2611.16393) · [HF](https://huggingface.co/papers/2611.16393)

Recent advancements in Large Vision-Language Models (LVLM) enhance X-ray report generation, but often neglect clinical context, overlook workflow integration, and lack explainability, which hinders clinical adoption due to interpretability and reliability concerns. This paper addresses the dual challenges of performance and expert explainability in automated X-ray report generation for clinical AI applications. Our…

## 114. Model Distribution-Aware Multimodal Dataset Distillation

- 分数：5.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：spec, retrieval
- 作者：Jiajun Shen, Yonglin Wu, Ruonan Yu, Xinchao Wang
- 链接：[arXiv](https://arxiv.org/abs/2611.16418) · [PDF](https://arxiv.org/pdf/2611.16418) · [HF](https://huggingface.co/papers/2611.16418)

Multimodal dataset distillation (MDD) aims to reduce the cost of vision-language pre-training by synthesizing compact image-text datasets. Although recent feature-matching methods have improved distillation efficiency, synthetic data may become specialized to the model representations encountered during optimization, limiting generalization to unseen model states. We propose Model Distribution-Aware Multimodal…

## 115. DesignTaste: Benchmarking AI-Generator Visual Design Against Award-Wining Works

- 分数：5.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark
- 作者：Zhou Chen, JiaXiang Li, DanYing Pan, Ye Li, TianRui Yang, EnBao Zhang, YaNan Xiao, LiXin Sun, Anqi Liu, Dong Zhao, JianYuan Li, YuanYuan Ding, Kai Kong, Xinwen Xu, HuiTang Du, Min Zhou, Zhiqiang Li
- 链接：[arXiv](https://arxiv.org/abs/2611.16442) · [PDF](https://arxiv.org/pdf/2611.16442) · [HF](https://huggingface.co/papers/2611.16442)

Text-to-image benchmarks commonly assess text-image alignment or overall preference. Whether models can produce good designs when a brief leaves the appearance open remains less well understood. We introduce DesignTaste, a visual design benchmark that compares generated images with award-winning works. From these works and their publicly available context, we derive 403 design briefs: 100 poster tasks from 100 Beste…

## 116. HIFC-IQA: Train-Free Cross-Domain Image Quality Assessment via Dual-Process Cognition

- 分数：5.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, benchmark
- 作者：Yu Li, Zhengran Shen, Puchao Zhou, Yukang Ding, Yachun Mi, Boyuan Yang, Xi Zhai, Shaohui Liu
- 链接：[arXiv](https://arxiv.org/abs/2611.16451) · [PDF](https://arxiv.org/pdf/2611.16451) · [HF](https://huggingface.co/papers/2611.16451)

The gap between controlled synthetic distortions and complex real-world degradations introduces a critical domain shift challenge for No-Reference Image Quality Assessment. Although Unsupervised Domain Adaptation (UDA) approaches attempt to address this issue, they remain constrained by substantial retraining overhead and cumulative error propagation inherent in iterative pseudo-labeling. Inspired by the…

## 117. Rational Alignments of Superintelligences via Debates

- 分数：5.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, spec
- 作者：Thanawat Sornwanee
- 链接：[arXiv](https://arxiv.org/abs/2611.16455) · [PDF](https://arxiv.org/pdf/2611.16455) · [HF](https://huggingface.co/papers/2611.16455)

Artificial superintelligences (ASI) is artificial intelligences with greater capability. However, as human principal has to use it, we have to ensure that the agent will perform in the interest of the human. We investigate the framework of ASI-assisted question answering where ASI agents know the correct answer but the human does not. We provide some example of mechanism for rational alignment, where the agent…

## 118. One Model, Two Precisions: Does Disagreement Between Quantized Copies Tell You When a Small Model Is Wrong?

- 分数：5.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：language model, spec
- 作者：Mohammed Nayeem Khan, Allan Kevin T
- 链接：[arXiv](https://arxiv.org/abs/2611.16478) · [PDF](https://arxiv.org/pdf/2611.16478) · [HF](https://huggingface.co/papers/2611.16478)

Local language models often exist at several precisions, and quantization is known to change individual answers. This study asks whether the disagreement between two precisions of the same weights, an 8-bit copy that answers and a lower-precision copy that reads the same prompt, works as a per-question error score for abstention, escalation and re-asking. The cost is one extra forward pass over fewer bytes, with no…

## 119. HeMeR: Heterogeneous Memory Reconciliation for Embodied Agents via Structured KV Reuse

- 分数：5.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, memory
- 作者：Saehun Chun, Wonje Choi, Jinwoo Jang, Taeyoon Kwack, Honguk Woo
- 链接：[arXiv](https://arxiv.org/abs/2611.16487) · [PDF](https://arxiv.org/pdf/2611.16487) · [HF](https://huggingface.co/papers/2611.16487)

Embodied agents make decisions by combining information from heterogeneous memory modules, including declarative memory for explicit knowledge, procedural memory for learned routines, and working memory for current observations. During interaction, the memory contents required for decision making change with the agent's state, goal, and task progress, while many contents remain shared across consecutive decisions.…

## 120. Learning Temporal Dynamics with Derivative Representations for Time Series Forecasting

- 分数：5.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, spec
- 作者：Shujie Duan, Jia Hong Puah, Haocheng Wu, Yifei Mao, Hongting Zhou, Chenxuan Li, Zitao Fang, Yang Lu, Sim Kuan Goh
- 链接：[arXiv](https://arxiv.org/abs/2611.16514) · [PDF](https://arxiv.org/pdf/2611.16514) · [HF](https://huggingface.co/papers/2611.16514)

Time series forecasting aims to predict the future evolution of complex systems by learning their underlying dynamics from past observations. Despite recent advances in deep learning, Transformers in particular still struggle to capture the temporal evolution of system dynamics. Existing approaches have been largely driven by architectural innovation, with comparatively little attention paid to training strategies…
