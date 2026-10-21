# 每日 AI 论文

生成时间：2026-10-21 04:48 UTC  ·  共 120 篇（已按 arXiv ID 去重）

来源：Hugging Face Daily Papers + arXiv（cs.AI / cs.LG / cs.CL / cs.CV）。
排序：HF 上榜、点赞、多源命中、兴趣词。兴趣词可在 `config.json` 改。

## 1. OR-License: Evaluating LLM Agents as Real-World Operations Research Practitioners

- 分数：36.0  ·  HF 赞：224  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark, language model, large language, coding
- 作者：Peisong Wang, Feixue Liu, Yize Meng, Bowen Liu, Ruoyu Chen, Gaoyang Dai, Xing He, Aiqian Li, Fengchi Yuan, Aochuan Chen, Chenyi Zi, Yuhan Li, Hongchuan Zeng, Yimo Yan, Nuo Chen, Jie Fu, Zuo-Jun Max Shen, Yong-Hong KUO, Jia Li
- 链接：[arXiv](https://arxiv.org/abs/2610.24087) · [PDF](https://arxiv.org/pdf/2610.24087) · [HF](https://huggingface.co/papers/2610.24087)

Can large language model (LLM) agents deliver expert-level operations research (OR) solutions directly from original client materials, without prior expert reformulation? Existing OR benchmarks typically begin with self-contained descriptions or predefined optimization tasks, underrepresenting the translation of original business materials into professionally validated solutions. We introduce OR-License, an…

## 2. MemT-1.0: Towards Memory-Native Evolution

- 分数：36.0  ·  HF 赞：109  ·  来源：huggingface
- 兴趣命中：agent, memory, evaluation, retrieval
- 作者：Zhiyu Li, Zeyu Zhang, Linyun Liu, Yiwei Bu, Chenyang Xi, Xichong Zhang, Yi Yu, Yu Yu, Zhichen Liu, Yuxiao Yi, Chunyu Li, Haoran Liu, Zhenkai Ding, Le Zhou, Juncheng Zhang, Boyu Chen, Zehao Lin, Guorui Li, Renyu Fu, Ji Li, Youyang Xia, Jiajun Shen, Harvey Li, Jingsong Zhou, Helan Hu, Tong Shen, Tianxiao Xu, Chenye Han, Weijie Li, Zhongquan Zhou, Hongming Xu, Yuekeng Li, Erenkai Zhu, Peng Yu, Wenhao Li, Jingyi Kang, Xixuan Hao, Xuzhou Zhu, Can Chen, Jiawei Liu, Chen Jiang, Tao Jiang, Fangwei Xiang, Zepeng Yao, Kai Chen, Guang Yang, Mingfei Lu, Chunhui Li, Zhengxuan Jiang, Bo Tang, Shiyu Zhan, Yihang Sun, Jie Chu, Wenjun Xiong, Zhenxiang Hua, Chen Lin, Detong Su, Dongyu Deng, Qiuping Ding, Guofeng Ding, Si Chen, Guohua Wen, Xu Chen, Zhi-Qin John Xu, Ying-Cong Chen, Ningyu Zhang, Haofen Wang, Muning Wen, Haotian Chen, Wentao Zhang, Xuanhe Zhou, Rita Zhang, Junchi Yan, Feiyu Xiong
- 链接：[arXiv](https://arxiv.org/abs/2610.26825) · [PDF](https://arxiv.org/pdf/2610.26825) · [HF](https://huggingface.co/papers/2610.26825)

Memory-native evolution requires making memory an intrinsic capability of foundation models, enabling them to continuously accumulate and utilize information. To this end, we introduce MemT-1.0, a new architecture of memory foundation models that internalize memory as part of model computation. Building on Metis, MemT-1.0 employs Gated DeltaNet-2 with a stable token-level memory update mechanism within each turn. We…

## 3. OpenVLHarness: Real World Visual Agentic Tool-Use with Multimodal Memory

- 分数：36.0  ·  HF 赞：98  ·  来源：huggingface
- 兴趣命中：agent, tool-use, memory, reasoning, benchmark, language model, large language, coding, spec
- 作者：Yu Zhou, Cheng-Fu Yang, Rui Sun, Di Wu, Sibo Peng, Mingyang Zhang, Zhen Yang, Ruiyi Zhang, Nanyun Peng, Zhe Gan, Kai-Wei Chang
- 链接：[arXiv](https://arxiv.org/abs/2610.26860) · [PDF](https://arxiv.org/pdf/2610.26860) · [HF](https://huggingface.co/papers/2610.26860)

Multimodal large language models (MLLMs) have made rapid progress on visual reasoning, yet many tasks require evidence that is difficult to obtain through internal reasoning alone: our controlled study on 22 benchmarks shows that simply increasing the inference budget of the base model yields only modest gains. Such tasks demand grounded perception, external knowledge, and numerical measurements obtained through…

## 4. Self-Evolving Coding Agents via Harness-Policy Optimization

- 分数：36.0  ·  HF 赞：44  ·  来源：huggingface
- 兴趣命中：agent, reinforcement learning, benchmark, language model, large language, coding, spec
- 作者：Zhepei Wei, Wenlin Yao, Baolin Peng, Danqing Wang, Qianhui Wu, Hao Cheng, Yu Meng, Jianfeng Gao
- 链接：[arXiv](https://arxiv.org/abs/2610.22791) · [PDF](https://arxiv.org/pdf/2610.22791) · [HF](https://huggingface.co/papers/2610.22791)

Large language model (LLM) agents have shown promising potential in coding tasks, and their performance is jointly determined by the policy model and the harness that mediates their interaction with the environment. Indeed, harness and policy are mutually reinforcing and evolving only one component is suboptimal---a harness tuned for one checkpoint may not target the failure modes of an updated policy, while policy…

## 5. Sage-A1.5: From Long-Horizon Execution to Scientific Exploration with Capability Composition

- 分数：36.0  ·  HF 赞：42  ·  来源：huggingface + arxiv
- 兴趣命中：agent, spec
- 作者：Wenjie Lou, Tianshuo Peng, Shiyang Feng, Shengji Tang, Runmin Ma, Ruizhe Chen, Jinxin Shi, Haoyang Peng, Fangchen Yu, Zhijie Zhong, Yuhao Zhou, Yue Fan, Yixin Chen, Yiming Wu, Yiheng Wang, Yigeng Jiang, Yichen Jiang, Yi Xie, Xu Guo, Xiaohan He, Tao Hu, Songtao Huang, Siyu Zhou, Shuaiyu Zhang, Shangheng Du, Qinglong Cao, Kun Li, Jingqi Ye, Hongbin Zhou, Guohang Yan, Zongsheng Cao, Ziyi Wang, Zhuo Liu, Zhiyin Yu, Zhiwang Zhou, Zelin Tan, Yuqing Zhu, Yaoze Zhang, Yang Chen, Xuming He, Xiuliang Liang, Xingjian Guo, Xiang Zhuang, Weiping Shen, Weida Wang, Tianyuan Zhou, Tianlin Ye, Tengyuan Fan, Siyu Yan, Shuo Li, Shuchen Pu, Shengyuan Xu, Shao Zhang, Ran Wei, Qinyuan Qin, Qingyu Yang, Nianchen Deng, Meng Dai, Kuikun Liu, Kaitao Chen, Juncheng Xiao, Jiangning Liu, Jianbiao Mei, Jia Yu, Haonan He, Hangfan Zhang, Cheng Yang, Chen Zhang, Bihao Zhan, Benteng Cheng, Yuqiang Li, Yihao Liu, Yang Yang, Xujun Fu, Xiaosong Wang, Xiangyu Yue, Wenwei Zhang, Shuyue Hu, Pinlong Cai, Mianxin Liu, Lei Bai, Jie Zhou, Jie Hou, Jiamin Wu, Hui Wang, Haijun Li, Guangyu Wang, Dongzhan Zhou, Chunfeng Song, Chao Yang, Biqing Qi, Xing Xie, Dahua Lin, Bowen Zhou, Xiangchao Yan, Wenlong Zhang, Shufei Zhang, Peng Ye, Bo Zhang
- 链接：[arXiv](https://arxiv.org/abs/2610.28578) · [PDF](https://arxiv.org/pdf/2610.28578) · [HF](https://huggingface.co/papers/2610.28578)

In this report, we introduce Sage-A1.5, a 35B Mixture-of-Experts agentic model that builds on A1 to advance long-horizon problem solving through adaptive capability composition. Compared with A1, Sage-A1.5 learns not only to solve individual tasks, but also to organize work and revise its approach during execution. Sage-A1.5 highlights three improvements: agentic orchestration, verification, and open scientific…

## 6. CoworkEnv: Synthesizing Training Environments for Long-Horizon Cowork Agents

- 分数：35.5  ·  HF 赞：39  ·  来源：huggingface
- 兴趣命中：agent, reinforcement learning, benchmark, spec
- 作者：Zhongwei Xie, Yiming Du, Jiaxin Bai, Baixuan Xu, Chunyang Li, Xiyu Ren, Wei Fan, Tianshi Zheng, Weizhi Du, Jingqiao Yu, Xingsu Li, Zhaowei Wang, Yangqiu Song
- 链接：[arXiv](https://arxiv.org/abs/2610.24960) · [PDF](https://arxiv.org/pdf/2610.24960) · [HF](https://huggingface.co/papers/2610.24960)

AI coworkers must coordinate tools, communicate across turns, and act on changing workspace state while respecting workflow constraints. Constructing training experience for these capabilities requires coherent requests, service records, tool interfaces, and grading checks. We present CoworkEnv, a capability-guided framework for synthesizing executable training environments for AI coworkers. Workflow requirements…

## 7. SolarRenderer: Few-Step Generative Reference Rendering

- 分数：33.5  ·  HF 赞：27  ·  来源：huggingface + arxiv
- 兴趣命中：agent, benchmark, coding, spec
- 作者：Guian Fang, Shengju Qian, Dongyue Lu, Junchao Huang, Lutao Jiang, Xin Wang, Yiren Song, Li Jiang, Mike Zheng Shou
- 链接：[arXiv](https://arxiv.org/abs/2610.28630) · [PDF](https://arxiv.org/pdf/2610.28630) · [HF](https://huggingface.co/papers/2610.28630)

Game engines and coding agents can specify the layout, motion, and camera of a scene, yet turning such coarse structure into realistic video requires a renderer that follows the structure and completes the appearance it leaves open. Existing renderers are tied to the representation of one engine, need tens of denoising steps or a costly distillation of their own, and learn from conditions that are not aligned with…

## 8. Interlock: From Local Correctness to Task Completion in Long-Horizon Agents

- 分数：33.0  ·  HF 赞：34  ·  来源：huggingface
- 兴趣命中：agent, evaluation, language model, large language, spec
- 作者：Linji Hao, Yanji He, Zihan Wang, Hansi Yang, Jiayuan Zhang, Hongyan Hao, Qi Gu, Yan Feng, Han Wu
- 链接：[arXiv](https://arxiv.org/abs/2610.19686) · [PDF](https://arxiv.org/pdf/2610.19686) · [HF](https://huggingface.co/papers/2610.19686)

Large language model agents increasingly undertake long-horizon tasks in complex environments characterized by fragmented evidence, partially completed states, and dependencies across resources and artifacts. Existing agents may satisfy individual requirements while failing to maintain these relationships, producing locally correct but incomplete outcomes. These failures arise because task completion depends on…

## 9. Holi-World: Building Holistic World Intelligence from Human-Ego Experience

- 分数：32.0  ·  HF 赞：141  ·  来源：huggingface
- 兴趣命中：reasoning, evaluation
- 作者：Hao Li, Xiyuan Zheng, Yuanyuan Gao, Yalun Dai, Xinhao Ji, Xuan-Li Chen, Jing Zhao, Fangzhou Hong, Zhaoxi Chen, Ziwei Liu
- 链接：[arXiv](https://arxiv.org/abs/2610.26549) · [PDF](https://arxiv.org/pdf/2610.26549) · [HF](https://huggingface.co/papers/2610.26549)

Human egocentric experience offers a rich foundation for learning how the world is organized and how it changes through interaction. Realizing this potential at scale requires turning growing volumes of recordings into learning resources that connect scene structure, object semantics, and interaction histories across viewpoints and time, while reducing dependence on costly manual annotation. We introduce HOLI-WORLD,…

## 10. ScaleNav: Scalable Internet Video Pretraining for Language-Conditioned Local Navigation

- 分数：32.0  ·  HF 赞：84  ·  来源：huggingface
- 兴趣命中：benchmark, spec
- 作者：Yihui Yang, Yuanhong Yu, Jiawei Wang, Zhongrui Yu, Jia Shi, Kun Zhan, Ruizhen Hu, Xiaowei Zhou, Yu Liu, Sida Peng
- 链接：[arXiv](https://arxiv.org/abs/2610.25690) · [PDF](https://arxiv.org/pdf/2610.25690) · [HF](https://huggingface.co/papers/2610.25690)

We study language-conditioned local navigation, where a robot must navigate to a text-specified target visible in its initial observation and stop at the described location. End-to-end navigation policies require diverse training data to generalize across scenes, yet real-robot data is costly to collect and simulated data leaves a sim-to-real gap. Internet egocentric videos offer a scalable source of real-world…

## 11. SpecMRL: Redesign Matryoshka Representation Learning within Parametric Spectrum

- 分数：32.0  ·  HF 赞：80  ·  来源：huggingface
- 兴趣命中：coding, spec
- 作者：Zhongxin Chen, Songhao Wu, Heng Cui, Cong Li, Xiao Zhou, Rui Yan
- 链接：[arXiv](https://arxiv.org/abs/2610.26824) · [PDF](https://arxiv.org/pdf/2610.26824) · [HF](https://huggingface.co/papers/2610.26824)

Matryoshka Representation Learning (MRL) is designed to support flexible representation sizes by jointly optimizing nested prefixes. While effective, this design lacks an explicit constraint to ensure that the leading portion provides a suitable compact encoding. To address this, we propose SpecMRL, which reorganizes the feature space to enable more effective prefix readout. Specifically, we extend MRL with a…

## 12. Focused Omni-Modal GUI Agents

- 分数：32.0  ·  HF 赞：52  ·  来源：huggingface
- 兴趣命中：agent, spec
- 作者：Fuyao Zhang, Wenwen He, Jiaming Zhang, Yurong Hao, Xuan Wang, Guowei Guan, Che Wang, Longtao Huang, Wei Yang Bryan Lim
- 链接：[arXiv](https://arxiv.org/abs/2610.26203) · [PDF](https://arxiv.org/pdf/2610.26203) · [HF](https://huggingface.co/papers/2610.26203)

Graphical User Interface (GUI) agents increasingly act over streaming omni-modal observations spanning screenshots, audio, video, interaction history, and device states. However, exposing this complete context uniformly at every step ignores that relevance is transient and sparse: the signal determining one action can become clutter at the next. Because executed actions feed back into the context, these errors…

## 13. AnyGoal: On World Model Generalization Beyond Expert Rollouts

- 分数：31.5  ·  HF 赞：31  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark, spec, planning
- 作者：Heejeong Nam, Divyat Mahajan, Quentin Le Lidec, Randall Balestriero, David Klindt
- 链接：[arXiv](https://arxiv.org/abs/2610.26844) · [PDF](https://arxiv.org/pdf/2610.26844) · [HF](https://huggingface.co/papers/2610.26844)

The goal of a world model is to capture the dynamics of an environment. This has the great appeal that it allows agents to plan and simulate a course of actions with the help of a world model. For these uses to be reliable, however, the learned dynamics must behave well beyond the specific state-action combinations observed in expert rollouts. Despite this, the relationship between data coverage, dynamics…

## 14. Scaling Parameter-Efficient Fine-Tuning for Brain Encoding

- 分数：30.0  ·  HF 赞：234  ·  来源：huggingface
- 兴趣命中：coding
- 作者：Zhuofan Josh Ying, Guanglong Sun, Nolan Ho, Kieran Liu, Rui Yang, Andrew Chen, Nikolaus Kriegeskorte, Pony Ma, Hossein Adeli
- 链接：[arXiv](https://arxiv.org/abs/2610.26802) · [PDF](https://arxiv.org/pdf/2610.26802) · [HF](https://huggingface.co/papers/2610.26802)

Brain encoding models aim to predict neural responses to stimuli. The most widely used approach fits readouts from frozen pretrained backbones. Using neural data to train large models from scratch or fully fine-tune them after task-pretraining has proven difficult because neural data is costly and limited. We show that parameter-efficient fine-tuning (PEFT) enables us to effectively adapt very large pretrained…

## 15. EgoXperience: Learning World-Grounded Egocentric Representations from Human Experience

- 分数：30.0  ·  HF 赞：156  ·  来源：huggingface
- 兴趣命中：benchmark
- 作者：Xinhao Ji, Hui En Pang, Hao Li, Kairui Hu, Jiner Wang, Mingze Sun, Ziang Cao, Yalun Dai, Thang Luu, Qin Ma, Hongyi Chen, Yukang Cao, Fangzhou Hong, Zhaoxi Chen, Ziwei Liu
- 链接：[arXiv](https://arxiv.org/abs/2610.26625) · [PDF](https://arxiv.org/pdf/2610.26625) · [HF](https://huggingface.co/papers/2610.26625)

Reconstructing human activity from egocentric video requires more than recovering individual 3D components: the observer's motion, surrounding geometry, and hand-object interactions must fit together in a consistent world. Achieving this coherence requires both joint reconstruction and aligned supervision, yet existing methods and datasets offer limited support for either. We present EgoXperience, a full-stack…

## 16. Learning from Fleet Experience: A Collective Learning Paradigm for Robots

- 分数：30.0  ·  HF 赞：109  ·  来源：huggingface
- 兴趣命中：retrieval
- 作者：Chao Yu, Shu&#39;ang Yu, Hao Lin, Hongzhi Zang, Yuxiang Yan, Chenxi Jiang, Zhen Guo, Chuankang Li, Yihao Chen, Xin Xu, Xu Fu, Jiakai Zhou, Liangzhi Shi, Hongyi Ren, Yiwei Liu, Jing Wu, Yuanqing Wang, Chen Wu, Bo Dai, Chunyu Yang, Hongliang Huang, Shuoyu Yue, Weiqi Yin, Yinuo Chen, Ruihua Chen, Chunyang Zhu, Han Xiao, Yanghao Li, Ruipu Wu, Zhikai Cai, Xiu Chen, Xu Tan, Yuchen Yan, Jialin Zhang, Wen Zeng, Yiming Zhou, Zixiao Huang, Guanghui Ren, Quanlu Zhang, Boxun Li, Maoqing Yao, Yu Wang
- 链接：[arXiv](https://arxiv.org/abs/2610.25736) · [PDF](https://arxiv.org/pdf/2610.25736) · [HF](https://huggingface.co/papers/2610.25736)

Experience generated during deployment offers an opportunity for robots to improve policy reliability through learning from their own executions. However, learning through human corrections requires teleoperators to monitor execution and intervene when policies fail, a demand that is difficult to meet as robot fleets grow. We introduce collective experience learning (CEL), a learning paradigm in which deployed…

## 17. Kronecker Delta Rule for Long Context Linear Attention

- 分数：30.0  ·  HF 赞：28  ·  来源：huggingface
- 兴趣命中：memory, long context, benchmark, language model
- 作者：Anamaria-Roberta Hartl, Levente Zólyomi, Michael List, Günter Klambauer, Sebastian Böck, Sepp Hochreiter
- 链接：[arXiv](https://arxiv.org/abs/2610.26834) · [PDF](https://arxiv.org/pdf/2610.26834) · [HF](https://huggingface.co/papers/2610.26834)

We propose KronLSTM, a linear attention architecture based on the Kronecker Delta Rule, a novel update rule for associative matrix memories. KronLSTM extends the xLSTM family with a memory-revision mechanism that corrects targeted associations while modifying the memory only along a single direction in matrix space. This minimally invasive memory revision reduces interference with previously stored information…

## 18. AdaExploreBench: Benchmarking LLM Agents for Proactive Exploration and Test-time Adaptation in Evolving Environments

- 分数：29.5  ·  HF 赞：27  ·  来源：huggingface
- 兴趣命中：agent, benchmark, language model, large language
- 作者：Rui Wang, Zishen Lai, Jiayu Liu, Cheng Qian, Jeonghwan Kim, Heng Wang, Xuejun Zhang, Jiateng Liu, Bingxuan Li, Shujin Wu, Qing Zong, Tianshi Zheng, Chunyang Li, Qihan Lin, Chen Li, Dadi Guo, Xiusi Chen, Yangqiu Song
- 链接：[arXiv](https://arxiv.org/abs/2610.25950) · [PDF](https://arxiv.org/pdf/2610.25950) · [HF](https://huggingface.co/papers/2610.25950)

Large Language Model (LLM) agents are increasingly deployed in unfamiliar and evolving environments, requiring them to proactively explore, understand, and adapt to environmental dynamics. However, existing benchmarks rarely test whether agents can proactively discover how an environment works and adapt as it evolves. To address this gap, we introduce AdaExploreBench, a benchmark for proactive exploration and…

## 19. MemPilot: Orchestrating On-Demand Multimodal Memory Curation for LLM Agents

- 分数：29.0  ·  HF 赞：26  ·  来源：huggingface
- 兴趣命中：agent, memory, reinforcement learning, benchmark, spec
- 作者：Haozhen Zhang, Haodong Yue, Quanyu Long, Jianzhu Bao, Qingyuan Liu, Tao Feng, Bohan Liu, Weida Liang, Wenya Wang
- 链接：[arXiv](https://arxiv.org/abs/2610.06830) · [PDF](https://arxiv.org/pdf/2610.06830) · [HF](https://huggingface.co/papers/2610.06830)

Memory has become integral to the LLM agent ecosystem, supporting information retention and reuse across interactions. However, most existing agent memory systems construct memory in a query-agnostic manner, which can incur unnecessary preprocessing cost and discard details that later prove essential. Recent studies have begun shifting memory processing toward runtime adaptation, but typically specialize in…

## 20. MT Forcing: Towards Stable and Consistent Multi-Turn Image Editing with Autoregressive Diffusion

- 分数：28.0  ·  HF 赞：36  ·  来源：huggingface
- 兴趣命中：spec
- 作者：Houyuan Chen, Fanzhou Wang, Xiangyu Fan, Zesong Qiu, Yukun Wei, Songlin Yang, Zhitao Yang, Lvmin Zhang, Pei Yang, Hao Zhao, Lei Yang, Anyi Rao
- 链接：[arXiv](https://arxiv.org/abs/2610.25404) · [PDF](https://arxiv.org/pdf/2610.25404) · [HF](https://huggingface.co/papers/2610.25404)

Multi-turn image editing aims to modify an image according to a sequence of instructions, enabling more effective interactive visual content creation for users. However, existing methods often exhibit noticeable drift after only a few editing turns, manifesting in two aspects: 1) unstable visual quality, with accumulating artifacts and degraded details; and 2) inconsistent image content, with unintended changes to…

## 21. Learning the 4D World through Point Trajectory Forecasting

- 分数：27.5  ·  HF 赞：23  ·  来源：huggingface + arxiv
- 兴趣命中：evaluation, benchmark
- 作者：Byungwoo Jeon, Sunghwan Hong, Dohyeon Kim, Jonghoon Lee, Jungwoo Park, Inhee Lee, Doosan Baek, Jinil Kim, Taehyun Lim, Hanbyul Joo, Marc Pollefeys, Saining Xie, Jinwoo Shin
- 链接：[arXiv](https://arxiv.org/abs/2610.28594) · [PDF](https://arxiv.org/pdf/2610.28594) · [HF](https://huggingface.co/papers/2610.28594)

Reliable multi-view forecasting requires videos from different cameras to describe the same evolving 3D scene. To this end, we introduce Video-Point Model (VPM), a world model that conditions on multi-view video histories and a language instruction to jointly forecast future videos from arbitrary viewpoints and the 3D trajectories of persistent scene points. We extend a pretrained world model with camera-conditioned…

## 22. HarnessPro: Recursive Harness Self-Improvement with Pareto Optimization for Performance-Cost Trade-offs

- 分数：27.0  ·  HF 赞：26  ·  来源：huggingface
- 兴趣命中：agent, benchmark, spec
- 作者：Zhuoshi Pan, ZhiYuan Feng, Yukuo Cen, Honglin Lin, Junru Lu, Zhongxia Chen, Shuo Yang, H. Vicky Zhao, Jie Tang
- 链接：[arXiv](https://arxiv.org/abs/2610.26770) · [PDF](https://arxiv.org/pdf/2610.26770) · [HF](https://huggingface.co/papers/2610.26770)

Harness development plays a crucial role in building capable AI agents. Recent approaches improve harnesses through recursive self-improvement (RSI), but their performance gains often come with higher execution costs. We introduce HarnessPro, a label-free method for evolving harnesses to improve task performance while reducing execution cost. In this setting, candidate harnesses are evaluated using LLM-generated…

## 23. BlenderWorld: Benchmarking Visual Agents for 3D Creation from Real-World References

- 分数：27.0  ·  HF 赞：22  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark, language model, large language, spec
- 作者：Xinyu Fang, Yuchi Wang, Weihao Yu, Rongyao Fang, Zhaohai Li, Zhixun Li, Tiancheng Gu, Xilin Wei, Yuhang Zang, Hongsheng Li, Dahua Lin, Guofeng Zhang, Shuai Bai, Zhibo Yang, Dayiheng Liu
- 链接：[arXiv](https://arxiv.org/abs/2610.23986) · [PDF](https://arxiv.org/pdf/2610.23986) · [HF](https://huggingface.co/papers/2610.23986)

Recent advances in multimodal large language models (MLLMs) have enabled them to act as autonomous agents, creating and editing 3D models via code or direct software manipulation. In practical workflows, these models must infer object shapes, materials, spatial layouts, and lighting from diverse references while strictly following instructions to reconstruct, modify, or design 3D content. However, existing…

## 24. Manga2Animate: An Agentic Framework for Faithful Manga Animation with Script and Storyboard Planning

- 分数：26.5  ·  HF 赞：25  ·  来源：huggingface
- 兴趣命中：agent, spec, planning
- 作者：Sheng-Wei Zhang, Hsi-An Chen, Yan-Ting Liou, Chih-Hsuan Chen, Shih-Chen Tseng, Yu-Lun Liu
- 链接：[arXiv](https://arxiv.org/abs/2610.26851) · [PDF](https://arxiv.org/pdf/2610.26851) · [HF](https://huggingface.co/papers/2610.26851)

Adapting existing manga into coherent animation that stays faithful to the source is a valuable yet challenging task. Existing methods either access the manga mainly through text, losing its characters and art style, or feed manga pages directly into video generation models, which misinterpret the manga's structure and produce incorrect storylines. In this paper, we propose Manga2Animate, a multi-agent framework…

## 25. RoboValue: A Fine-Grained Sim-and-Real Benchmark for Unified Evaluation of Robotic Value Models

- 分数：26.0  ·  HF 赞：20  ·  来源：huggingface
- 兴趣命中：reasoning, evaluation, benchmark, spec
- 作者：Shengbang Liu, Zhengye Du, Zhilong Wan, Honghao Su, Chenxiang Xia, Chang Ge, Jinyang Xiao, Nan Wang, Zhipeng Hu, Huining Yuan, Shu&#39;ang Yu, Yue Chen, Tianxing Chen, Chuankang Li, Maoqing Yao, Wenbo Ding, Yu Wang, Guanghui Ren, Chao Yu
- 链接：[arXiv](https://arxiv.org/abs/2610.26663) · [PDF](https://arxiv.org/pdf/2610.26663) · [HF](https://huggingface.co/papers/2610.26663)

Robotic value models assess task execution from visual observations and instructions, providing feedback for policy learning and execution monitoring. However, existing evaluations cover only selected aspects of execution understanding, leaving the reliability of value feedback insufficiently tested. We introduce RoboValue, a fine-grained sim-and-real benchmark for unified evaluation of robotic value models. Its…

## 26. InfiniDream: Open-Ended Photorealistic 3D Worlds Through Procedural Generation

- 分数：25.0  ·  HF 赞：26  ·  来源：huggingface
- 兴趣命中：evaluation, planning
- 作者：Yi-Chuan Huang, Hao-Jen Chien, Zheng-Hui Huang, Yu-Lun Liu, Kaipeng Zhang, Zhixiang Wang
- 链接：[arXiv](https://arxiv.org/abs/2610.26853) · [PDF](https://arxiv.org/pdf/2610.26853) · [HF](https://huggingface.co/papers/2610.26853)

Procedural generation plays a key role in synthetic data creation and game development, offering greater controllability, editability, and diversity than static mesh representations. However, VLM-based code generation often produces relatively simple 3D assets, while sophisticated photorealistic procedural systems require extensive manual development. Existing VLM-guided procedural methods remain largely constrained…

## 27. Think Visually Across Space and Time: Grounded Reasoning for Video Segmentation

- 分数：23.5  ·  HF 赞：19  ·  来源：huggingface
- 兴趣命中：reasoning, reinforcement learning, benchmark
- 作者：Junwei Wen, Deshui Miao, Guangming Lu, Ming-Hsuan Yang, Xin Li, Wenjie Pei
- 链接：[arXiv](https://arxiv.org/abs/2610.25090) · [PDF](https://arxiv.org/pdf/2610.25090) · [HF](https://huggingface.co/papers/2610.25090)

Video Reasoning Segmentation (VRS) requires a model to identify an implicitly described target and predict its pixel-level mask trajectory, while resolving the spatial relations and temporal events that determine the answer. Text-only Chain-of-Thought (CoT) can explain a target choice without making the underlying visual references explicit, leaving a video reference gap between linguistic inference and the evidence…

## 28. RoAR-VAE: Improving Latent Diffusability through Robust Prediction

- 分数：23.0  ·  HF 赞：26  ·  来源：huggingface
- 兴趣命中：benchmark
- 作者：Yang Yue, Fangyun Wei, Yitong Wang, Jinjing Zhao, Henry Zheng, Dong Chen, Gao Huang
- 链接：[arXiv](https://arxiv.org/abs/2610.26216) · [PDF](https://arxiv.org/pdf/2610.26216) · [HF](https://huggingface.co/papers/2610.26216)

An effective visual tokenizer must preserve image fidelity while producing latents that downstream diffusion models can learn efficiently. Prior work improves latent diffusability through semantic alignment or joint tokenizer--diffusion training. Revisiting REPA-E, a representative approach, we find that removing its diffusion objective and dedicated generative blocks while retaining semantic prediction from…

## 29. S-Agent 2.0: Spatial Reasoning with a General Coding Agent

- 分数：23.0  ·  HF 赞：6  ·  来源：huggingface + arxiv
- 兴趣命中：agent, memory, reasoning, coding, spec
- 作者：Rui Gong, Ruoyu Wang, Yalun Dai, Hao Li, Sidi Yang, Qihao Zhao, Hongyu Li, Zeyang Guan, Fangzhou Hong, Zhaoxi Chen, Kim-Hui Yap, Ziwei Liu
- 链接：[arXiv](https://arxiv.org/abs/2610.28354) · [PDF](https://arxiv.org/pdf/2610.28354) · [HF](https://huggingface.co/papers/2610.28354)

Spatial reasoning asks a model to work out where objects are in 3D space, how they relate to one another, and how they move. Agentic VLMs have recently brought large improvements on such tasks by letting the model actively gather evidence with 3D perception tools instead of answering in a single pass. Even so, on many questions the tools return the right evidence and the model still does not arrive at the correct…

## 30. Evidence-First Agentic Verification

- 分数：22.5  ·  HF 赞：17  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark
- 作者：Reza Sanayei, Razvan-Gabriel Dumitru, Sunjie Hou, MohammadHossein Rezaei, Haris Riaz, Robert Vacareanu, Minglai Yang, Ying Liu, Mihai Surdeanu, Daniel Yue Zhang
- 链接：[arXiv](https://arxiv.org/abs/2610.17724) · [PDF](https://arxiv.org/pdf/2610.17724) · [HF](https://huggingface.co/papers/2610.17724)

Long-horizon, semi-verifiable agentic tasks often rely on rubric-based evaluation, but the evidence needed to assess these tasks can be spread across the environment state and the execution trace. A judge may overlook this evidence or accept unsupported claims, including an agent's own reports of success. When rubric verdicts serve as reinforcement-learning rewards, such errors can reinforce undesirable behavior. We…

## 31. Where is Physical RSI capability from? An Observational Scaling Law of LLM-as-policy

- 分数：22.5  ·  HF 赞：17  ·  来源：huggingface
- 兴趣命中：agent, benchmark, spec
- 作者：Zekai Li, Jiayi Yu, Jinlu Zhang, Luyang Niu, Zekun Qi, Jun Zheng, Xuchuan Chen, Dairu Liu, Yintianrun Zhang, He Wang, Li Yi
- 链接：[arXiv](https://arxiv.org/abs/2610.26848) · [PDF](https://arxiv.org/pdf/2610.26848) · [HF](https://huggingface.co/papers/2610.26848)

In this paper, we systematically investigate the mechanisms, scaling behavior, and generalization of physical Recursive self-improvement. We introduce PhysRSI-eval to quantify physical RSI through a five-axis metric: First-Attempt Performance, Efficiency, Success, Budget and Improvement from failure. Different VLMs are evaluated on 18 manipulation tasks under a fixed interaction budget. The analysis of experimental…

## 32. Ropedia W0: Scaling Loco-Manipulation World Models across Embodiments with Human Experience

- 分数：22.5  ·  HF 赞：13  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark, spec, planning
- 作者：Tianqi Liu, Hanfei Zhao, Qifeng Liang, Hui En Pang, Jiarui Xu, Sayang Mu, Penghao Qiu, YingSheng Zhang, Jun Wang, Ziang Cao, Mingze Sun, Yukang Cao, Fangzhou Hong, Zhaoxi Chen, Ziwei Liu
- 链接：[arXiv](https://arxiv.org/abs/2610.26855) · [PDF](https://arxiv.org/pdf/2610.26855) · [HF](https://huggingface.co/papers/2610.26855)

World models enable embodied agents to anticipate action consequences, yet jointly modeling locomotion and manipulation across diverse embodiments remains challenging due to heterogeneous action spaces and limited multimodal supervision. We present Ropedia W0, the first egocentric loco-manipulation world foundation model spanning humans and robots with diverse embodiments. We curate Xp-Data, comprising 10k hours of…

## 33. MMEnterprise-Bench: Evaluating Enterprise Agents over Evolving Multimodal Records

- 分数：22.5  ·  HF 赞：13  ·  来源：huggingface
- 兴趣命中：agent, reasoning, benchmark, retrieval
- 作者：Seohyun Lee, Jongha Kim, Dohwan Ko, Ji Soo Lee, Seoung Choi, Jayun Ku, Hyunwoo J. Kim
- 链接：[arXiv](https://arxiv.org/abs/2610.27911) · [PDF](https://arxiv.org/pdf/2610.27911) · [HF](https://huggingface.co/papers/2610.27911)

Enterprise agents answer questions over workplace records that evolve through team collaboration. As information is shared, corrected, and revised across documents, chats, and figures, multiple versions of the same information accumulate in the workspace. Reliable question answering therefore requires agents to reason over sufficient evidence, resolve cross-source and temporal conflicts, and recognize when the…

## 34. Remembering Has a Price: Learning Memory Worth under Resource Constraints

- 分数：21.0  ·  HF 赞：10  ·  来源：huggingface
- 兴趣命中：agent, memory, reasoning, retrieval
- 作者：Guannan Lai, Zi-Yang Bai, Jun-Peng Jiang, Han-Jia Ye
- 链接：[arXiv](https://arxiv.org/abs/2610.26453) · [PDF](https://arxiv.org/pdf/2610.26453) · [HF](https://huggingface.co/papers/2610.26453)

Lifelong agents continually accumulate and reuse experience to improve after deployment, yet in practice they often operate under tight generation, interaction, and memory budgets. Under such stringent joint constraints, we find that existing lifelong-memory methods can become ineffective, with several sophisticated approaches offering little advantage over simple retrieval or even no-memory agents. This reveals a…

## 35. DeOverlay: A Benchmark and Source-Anchored Flow for Video Overlay Removal

- 分数：20.5  ·  HF 赞：13  ·  来源：huggingface
- 兴趣命中：evaluation, benchmark, spec
- 作者：Deshui Miao, Yuhang Ma, Shaoyong Jia, Wenzhao Gao, Yue Zhang, Shaohui Jiao, Xin Li
- 链接：[arXiv](https://arxiv.org/abs/2610.26081) · [PDF](https://arxiv.org/pdf/2610.26081) · [HF](https://huggingface.co/papers/2610.26081)

Video overlay removal aims to recover scenes obscured by subtitles, titles, and logos while preserving surrounding content. Existing methods use temporal propagation or source-conditioned generation, but can leave residual overlays and distort scene structure when useful source information is obscured. We propose DeOverlay, a source-anchored flow model that reconstructs the clean video from the source latent with…

## 36. DecisionPivot: A Diagnostic Benchmark for Decision Models in LLM Systems

- 分数：20.5  ·  HF 赞：1  ·  来源：huggingface + arxiv
- 兴趣命中：reasoning, evaluation, benchmark, spec
- 作者：Xialie Zhuang, Mingcong Lei, Zunhai Su, Ri Liu, Jianjin Li, Peixian Ma, Jia Pan, Ngai Wong, Guanhua Chen, Chuan-Wei Kuo
- 链接：[arXiv](https://arxiv.org/abs/2610.28522) · [PDF](https://arxiv.org/pdf/2610.28522) · [HF](https://huggingface.co/papers/2610.28522)

Decision models support routing, guardrails, and output verification in LLM systems. However, item accuracy alone cannot establish whether models make correct decisions across controlled variations or assign reliable confidence to their predictions. We introduce DecisionPivot, a diagnostic benchmark comprising 48 tasks and 40,033 items across seven decision roles. Its core track contains 7,800 items from 13…

## 37. EvaOmni: An Evidence-Grounded Benchmark for Audio-Visual Reasoning

- 分数：20.5  ·  HF 赞：1  ·  来源：huggingface + arxiv
- 兴趣命中：reasoning, evaluation, benchmark, spec, retrieval
- 作者：Xiaoxing Hu, Wenxi Yao, Chaoyuan Shi, Ziqi Ye, Xiaorong Guo, Peixuan Li, Zhuoran Sun, Ziyang Gong, Peiyuan Zhang, Mingxin Liu, Shuran Ma, Hongbo Liu, Xiaomin Yu, Yu Tian, Wentao Wang, Zhenjie Yang, Jian Hu, Yunhang Shen, Haoyu Cao, Xue Yang
- 链接：[arXiv](https://arxiv.org/abs/2610.28444) · [PDF](https://arxiv.org/pdf/2610.28444) · [HF](https://huggingface.co/papers/2610.28444)

Omni LLMs can naturally locate key audio and visual evidence and integrate information across modalities for audiovisual reasoning. Existing audio-visual reasoning benchmarks that mainly rely on multiple-choice questions usually score models solely based on answer correctness, making it difficult to assess whether a model truly forms a reasoning chain from evidence to the correct answer. In addition, textual or…

## 38. Large Flow Language Models

- 分数：20.5  ·  HF 赞：1  ·  来源：huggingface + arxiv
- 兴趣命中：reasoning, language model, coding, spec
- 作者：Arnav Chavan, Chanhyuk Lee, Udbhav Bamba, Jaehoon Yoo, Seunghoon Hong, Aditi Raghunathan, Jinwoo Kim
- 链接：[arXiv](https://arxiv.org/abs/2610.28559) · [PDF](https://arxiv.org/pdf/2610.28559) · [HF](https://huggingface.co/papers/2610.28559)

Continuous flow language models offer a path to parallel generation with tools for control and acceleration unavailable to discrete diffusion, yet effective techniques for building them at the billion-parameter scale remain less established. We present Lafa (Large flow language model), a fast, high-performing flow language model scaled to 8B parameters in a data-efficient manner. Lafa is a blockwise flow model with…

## 39. SWIFT: Self-guided Weak-to-strong dIFfusion models via Target extrapolation

- 分数：20.0  ·  HF 赞：20  ·  来源：huggingface
- 兴趣命中：spec
- 作者：Yanjin He, Cuifeng Shen, Wanzhou Lei, Maohua Li, Tao Lan, Kan Liu, Hanlin Tang, Qing Qu
- 链接：[arXiv](https://arxiv.org/abs/2610.25844) · [PDF](https://arxiv.org/pdf/2610.25844) · [HF](https://huggingface.co/papers/2610.25844)

Training high-quality diffusion models is computationally expensive, and inference-time guidance often adds further sampling cost. In this work, we introduce Swift, a simple yet effective self-guided training method that uses a frozen weak denoiser to improve a stronger model without adding inference overhead. For each noisy input, Swift extrapolates the clean regression target away from the weak denoiser's…

## 40. Learning to Discriminate Scene Structures Makes Self-Supervised Depth Learning Scalable

- 分数：20.0  ·  HF 赞：12  ·  来源：huggingface
- 兴趣命中：evaluation, coding, spec
- 作者：Mengtan Zhang, Yuchuan Cui, Yu Ma, Zizhan Guo, Wei Ye, Rui Fan
- 链接：[arXiv](https://arxiv.org/abs/2610.23600) · [PDF](https://arxiv.org/pdf/2610.23600) · [HF](https://huggingface.co/papers/2610.23600)

Self-supervised monocular depth estimation is appealing for its potential to scale with unlabeled data, yet existing methods often degrade when trained on diverse scenes. This study finds that, under self-supervision, models tend to encode dataset-specific structural biases rather than transferable scene geometry, leading to cross-domain optimization conflicts. To address this issue, this study proposes the MaSS…

## 41. Factorization-Guided Training and Inference for Diffusion-Drafted Speculative Decoding

- 分数：20.0  ·  HF 赞：8  ·  来源：huggingface
- 兴趣命中：benchmark, language model, large language, coding, spec
- 作者：Jiakun Fan, Min Xiao, Qiang Wang, Neiwen Ling, Zhichao Liu, Zhihao Jia, Dimitrios S. Nikolopoulos, Zijun Wei
- 链接：[arXiv](https://arxiv.org/abs/2610.23935) · [PDF](https://arxiv.org/pdf/2610.23935) · [HF](https://huggingface.co/papers/2610.23935)

Speculative decoding accelerates large language model inference through parallel verification of tokens proposed by a drafter. Diffusion drafters further parallelize proposal generation, but greater proposal capacity or higher mean accepted tokens (MAT) need not yield higher throughput. Because verification accepts only a consecutive prefix, early rejections can render later correct predictions ineffective, limiting…

## 42. Progress-Aware Distillation for Mitigating Stagnation in Small Language Model Agents

- 分数：20.0  ·  HF 赞：8  ·  来源：huggingface
- 兴趣命中：agent, reasoning, benchmark, language model
- 作者：Yuanpu Cao, Saket Sathe, Hanyu Wang, Ziyi Yin, Fenglong Ma, Jinghui Chen
- 链接：[arXiv](https://arxiv.org/abs/2610.19439) · [PDF](https://arxiv.org/pdf/2610.19439) · [HF](https://huggingface.co/papers/2610.19439)

While LLM-based agent systems have demonstrated remarkable proficiency in reasoning and solving complex real-world tasks, they also come with substantial token consumption and inference latency, limiting their practical deployment. To enhance the efficiency of agent systems, recent efforts have focused on transferring agentic capabilities from large-scale models to small language models (SLMs) via supervised…

## 43. Co-Evolving Acting and Forecasting for Language Agents

- 分数：19.5  ·  HF 赞：7  ·  来源：huggingface
- 兴趣命中：agent, reinforcement learning, benchmark, spec
- 作者：Haofei Yu, Yixing Chen, Yining Zhao, Xuyan Ye, Yuxiang Liu, Zhigang Hua, Yan Xie, Shuang Yang, Jiaxuan You
- 链接：[arXiv](https://arxiv.org/abs/2610.20597) · [PDF](https://arxiv.org/pdf/2610.20597) · [HF](https://huggingface.co/papers/2610.20597)

Training language agents is bottlenecked by the high cost of long-horizon rollouts, yet standard agentic reinforcement learning (RL) learns only from a terminal scalar reward, leaving the supervision in intermediate steps largely unused. Prior work exploits this supervision through value targets that estimate per-step success probabilities or observation targets that fit environment response. Both are hard to…

## 44. EdgeKernelBench: Unified LLM-Driven Kernel Generation for Edge Backends

- 分数：19.5  ·  HF 赞：7  ·  来源：huggingface
- 兴趣命中：agent, memory, evaluation, benchmark
- 作者：Yuhua Zheng, Xueyi Chen, Xinze Zou, Xin Li, Haoji Hu, Huan Wang
- 链接：[arXiv](https://arxiv.org/abs/2610.24648) · [PDF](https://arxiv.org/pdf/2610.24648) · [HF](https://huggingface.co/papers/2610.24648)

Recent works show that LLMs can generate kernels with strong performance on server GPUs. Edge deployment presents distinct challenges because the hardware is heterogeneous, the software stacks are fragmented, and the resource budgets are tight. LLM kernel generation across diverse edge backends has yet to be studied systematically. We introduce EdgeKernelBench, which combines a unified IR deployment framework with a…

## 45. LIBERO-Industry: Benchmarking Robotic Manipulation under Industrial Process Constraints

- 分数：19.0  ·  HF 赞：10  ·  来源：huggingface
- 兴趣命中：evaluation, benchmark, spec
- 作者：Ming Shin Cindy Sung, Duan Leijiahao, Haoxiang Wang, Boning Tan, Liangna Fu, Chao Tan, Yafu Li, Yulong Chen, Chaoqun Wan, Zhen Huang, Shuxian Liang, Xian-Sheng Hua
- 链接：[arXiv](https://arxiv.org/abs/2610.16782) · [PDF](https://arxiv.org/pdf/2610.16782) · [HF](https://huggingface.co/papers/2610.16782)

Industrial manipulation in flexible manufacturing, e.g., high-mix, low-volume (HMLV) electronics assembly, requires robot policies to adapt to changing products and production conditions. Such settings impose industrial process constraints, including product variants, moving material flows, finite execution windows, and tight geometric tolerances. However, existing evaluation frameworks do not systematically capture…

## 46. RSIFlow: Adaptive Self-Improvement Workflows with an Evolving Meta-Agent

- 分数：19.0  ·  HF 赞：6  ·  来源：huggingface
- 兴趣命中：agent, tool use, benchmark, language model, large language, spec
- 作者：Huan Zhang, Mingju Chen, Dongxu Zhou, Can Lv, Sen Cui, Faguo Wu, Shiji Zhou
- 链接：[arXiv](https://arxiv.org/abs/2610.21791) · [PDF](https://arxiv.org/pdf/2610.21791) · [HF](https://huggingface.co/papers/2610.21791)

Large language model (LLM) agents have demonstrated strong capabilities in complex tasks, including code generation, tool use, and multi-hop question answering. Existing self-improvement methods enhance agent performance through model optimization, harness evolution, and executable artifact refinement, while recursive self-improvement (RSI) further extends optimization to the improvement mechanisms themselves.…

## 47. Matrix-Game 4.0: Harnessing Video Models for Real-Time Playable Game Worlds

- 分数：19.0  ·  HF 赞：2  ·  来源：huggingface + arxiv
- 兴趣命中：agent, memory, coding
- 作者：Jihai Zhang, Runjia Qian, Kaiqin Kong, Biao Jiang, Puyi Wang, Siru Chen, Tianle Li, Guanjie Chen, Junyi Wu, Chubin Chen, Yuanhang Li, Kaichen Huang, Haobo Zhang, Yangguang Li, Wei Yu, Guibin Chen, Yu Cheng, Yahui Zhou
- 链接：[arXiv](https://arxiv.org/abs/2610.27999) · [PDF](https://arxiv.org/pdf/2610.27999) · [HF](https://huggingface.co/papers/2610.27999)

Moving from controllable videos to genuinely playable worlds requires persistent world state, executable game rules, and low-latency interaction. We outline a roadmap for the next generation of Matrix-Game that separates game execution from visual generation through an executable game harness, and introduce Matrix-Game 4.0 as the first system built on this design. A lightweight game engine maintains world state and…

## 48. Competing Learning in Hybrid Architectures

- 分数：18.5  ·  HF 赞：9  ·  来源：huggingface
- 兴趣命中：reasoning, language model, retrieval
- 作者：Xingyu Shen, Yingfa Chen, Ziqing Qiao, Chaojun Xiao, Xu Han, Zhiyuan Liu
- 链接：[arXiv](https://arxiv.org/abs/2610.26830) · [PDF](https://arxiv.org/pdf/2610.26830) · [HF](https://huggingface.co/papers/2610.26830)

Many modern language models have adopted hybrid architectures that incorporate both linear-time recurrence and softmax attention. Modern recurrence layers provide a highly expressive mixing mechanism while ensuring high throughput by compressing contextual information into a fixed-size state, but underperform softmax attention in contextual information retrieval. In this paper, we reveal a Competing Learning…

## 49. Predicting Privileged Information Effectiveness for On-Policy Self-Distillation

- 分数：18.5  ·  HF 赞：5  ·  来源：huggingface
- 兴趣命中：agent, reasoning, benchmark, language model, large language
- 作者：Kaijian Zou, Emiliano Penaloza, MohammadHossein Rezaei, Anisha Gunjal, Mohit Raghavendra, Lu Wang, Yunzhong He, Anas Mahmoud
- 链接：[arXiv](https://arxiv.org/abs/2610.22512) · [PDF](https://arxiv.org/pdf/2610.22512) · [HF](https://huggingface.co/papers/2610.22512)

On-policy self-distillation (OPSD) enables large language models (LLMs) to learn from privileged information (PI) without a separate teacher model. However, prior work largely treats PI as a fixed design choice, leaving the effects of its content and construction poorly understood. This challenge is particularly important in multi-turn agentic settings, where trajectories contain actions, observations, and reasoning…

## 50. State World Models: Execute the Rules, Generate the Pixels

- 分数：18.0  ·  HF 赞：12  ·  来源：huggingface
- 兴趣命中：benchmark, spec
- 作者：Chan Yan Ki, Yanran Zhang, Wenzhao Zheng, Xiaofeng Wang, Zheng Zhu, Lei Chen, Jie Zhou, Jiwen Lu
- 链接：[arXiv](https://arxiv.org/abs/2610.26811) · [PDF](https://arxiv.org/pdf/2610.26811) · [HF](https://huggingface.co/papers/2610.26811)

Existing world models can generate action-conditioned video from a single image. Many focus on camera movement, allowing users to explore the generated scene. However, navigation alone does not ensure that an action follows persistent rules when its outcome depends on state that is invisible in the current frame. We present Stateful Harness, a framework that separates world evolution from video rendering to support…

## 51. StopLoss: Teaching Agents to Predict Failure and Stop Early

- 分数：18.0  ·  HF 赞：8  ·  来源：huggingface
- 兴趣命中：agent, language model, coding
- 作者：Jiarong Liang, Xueguang Ma, Dongfu Jiang, Yuxuan Zhang, Ping Nie, Wenhu Chen
- 链接：[arXiv](https://arxiv.org/abs/2610.25525) · [PDF](https://arxiv.org/pdf/2610.25525) · [HF](https://huggingface.co/papers/2610.25525)

Coding agents keep working on runs that will fail verification, and asking a frontier model to watch for this is expensive in its own right. We introduce StopLoss, a small external monitor that learns failure recognition from completed trajectories and their verifier outcomes. The name is inspired by the stop-loss order in finance: StopLoss ends a run early when the run is likely to fail, which saves resources.…

## 52. HERA: Harness-Environment Co-Evolution for Reliable Agentic Abstention

- 分数：18.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：agent, tool-use, evaluation, language model, large language, spec
- 作者：Han Luo, Bingbing Wen, Guang Yang, Zora Zhiruo Wang, Pan Lu, Lucy Lu Wang
- 链接：[arXiv](https://arxiv.org/abs/2610.06563) · [PDF](https://arxiv.org/pdf/2610.06563) · [HF](https://huggingface.co/papers/2610.06563)

Large language model (LLM) agents are increasingly capable of acting in complex tool-use environments, yet they often fail to recognize when tasks are infeasible and no valid solution exists. Recent work has formalized this reliability gap as the problem of agentic abstention, and existing approaches typically optimize a model or agent harness against a fixed set of tasks, leading to limited generalization to unseen…

## 53. Training Reasoning Models to Generate Diverse Scientific Ideas

- 分数：18.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：agent, reasoning, reinforcement learning, benchmark, language model, large language, coding
- 作者：Manya Wadhwa, Pranav Narayanan Venkit, Hiroaki Hayashi, Yu Li, Tuhin Chakrabarty, Chien-Sheng Wu
- 链接：[arXiv](https://arxiv.org/abs/2610.22324) · [PDF](https://arxiv.org/pdf/2610.22324) · [HF](https://huggingface.co/papers/2610.22324)

One of the first steps of a research pipeline is generating ideas. Large Language Models (LLMs) are increasingly used to automate this step, but most of this work optimizes the quality of individual ideas, while overlooking diversity. In our work, we study document-grounded ideation, focusing on increasing the diversity of LLM generated ideas and ensuring they are high quality. Given prior papers, a model must…

## 54. Correction Training for Diffusion Models

- 分数：17.5  ·  HF 赞：19  ·  来源：huggingface
- 兴趣命中：-
- 作者：Donghoon Ahn, Runqian Wang, Alexei A. Efros, Taesung Park, Yash Belhe
- 链接：[arXiv](https://arxiv.org/abs/2610.14136) · [PDF](https://arxiv.org/pdf/2610.14136) · [HF](https://huggingface.co/papers/2610.14136)

Iterative sampling in diffusion models can lead to error accumulation due to exposure bias. The denoiser is trained on real images interpolated with noise, but at inference its inputs are constructed from its own imperfect predictions from the earlier steps, something it has never seen at training time. This might be one reason diffusion models often struggle without additional help, such as CFG. We introduce a…

## 55. Harnessing Textual Refusal Directions for Multimodal Safety

- 分数：17.5  ·  HF 赞：11  ·  来源：huggingface
- 兴趣命中：language model, large language
- 作者：Moreno D&#39;Incà, Nicu Sebe, Massimiliano Mancini
- 链接：[arXiv](https://arxiv.org/abs/2606.31876) · [PDF](https://arxiv.org/pdf/2606.31876) · [HF](https://huggingface.co/papers/2606.31876)

Safety in Multimodal Large Language Models (MLLMs) depends on unsafe multimodal data for post-training alignment or activation steering. However, such data is hard to collect, must be gathered anew for each modality, and its collection and distribution raise ethical and legal concerns. In this work, we relax this constraint and investigate whether textual refusal directions, extracted directly from the LLM backbone,…

## 56. World Model Interpretability: From Decoding Representations to Understanding Latent Worlds

- 分数：17.5  ·  HF 赞：7  ·  来源：huggingface
- 兴趣命中：coding, spec, planning
- 作者：Jize Wang, Yongcheng Jing, Xinyi Le, Cailian Chen, Xinping Guan, Dacheng Tao
- 链接：[arXiv](https://arxiv.org/abs/2610.25296) · [PDF](https://arxiv.org/pdf/2610.25296) · [HF](https://huggingface.co/papers/2610.25296)

Emerging Joint-Embedding Predictive Architectures (JEPAs) are moving beyond representation learning towards latent world models that support prediction, planning, and control. Yet their latent worlds naturally lack a human-interpretable interface. In this Perspective, we argue that as JEPA latents become internal states for prediction and action, interpretability must move beyond what they encode to how latent…

## 57. HybridResearcher: Bridging the Structured-Unstructured Boundary for Deep Research Agents

- 分数：17.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：agent, reasoning, reinforcement learning, evaluation, benchmark
- 作者：Soyoung Yoon, Peiran Xu, Han Wang, Ruofan Wu, Xiaodong Yu, Feng Yan, Mohit Bansal, Debiao Li, Seung-Won Hwang, Yuxiong He, Zhewei Yao
- 链接：[arXiv](https://arxiv.org/abs/2610.24899) · [PDF](https://arxiv.org/pdf/2610.24899) · [HF](https://huggingface.co/papers/2610.24899)

While LLM agents are increasingly capable of gathering and synthesizing evidence from a single homogeneous source, such as structured tables or unstructured data, real-world analytical questions frequently span heterogeneous sources. For example, answering one enterprise question may require both a result computed over an internal database and evidence found on the web. Recent evaluations on benchmarks like…

## 58. Self-Evaluating Recursive Agents

- 分数：17.0  ·  HF 赞：10  ·  来源：huggingface
- 兴趣命中：agent, evaluation
- 作者：TianYi Lyu, Xiaozhe Li, Yang Li, Yongkang Chen, Kefei Tian, Junbo Niu, Zican Hu, Hongbo Liu, Mingliang Xiong, Qingwen Liu
- 链接：[arXiv](https://arxiv.org/abs/2610.04902) · [PDF](https://arxiv.org/pdf/2610.04902) · [HF](https://huggingface.co/papers/2610.04902)

Recursive language-model agents decompose tasks and delegate subtasks to child instances of the same policy, forming a tree of work. Training them, however, is hard: the final outcome is verifiable, but the self-invented intermediate subtasks are numerous and carry no ground truth. Existing methods score each node with a verifier or judge, which is costly at scale and blind to decomposition quality. We argue that a…

## 59. N-Gram Memories at Two Bits: Quantizing Lookup Tables in Large Language Models

- 分数：17.0  ·  HF 赞：6  ·  来源：huggingface
- 兴趣命中：memory, language model, large language
- 作者：Donghoon Han, Minseop Jung, Dong Woo Kwak, SeungJae Lee, Junhoo Lee
- 链接：[arXiv](https://arxiv.org/abs/2610.21810) · [PDF](https://arxiv.org/pdf/2610.21810) · [HF](https://huggingface.co/papers/2610.21810)

Conditional memory expands language-model capacity through selective lookup, but the full embedding table must remain available for every possible input. We introduce Conditional Program (CP), a compressed representation that reconstructs only the rows an input requests. CP represents each row by a short code and a local scale, with a reconstruction program shared across the table. We instantiate this representation…

## 60. HSPR: Recovering Software-Agent Benchmark Scores via Hierarchical Posterior Inference

- 分数：17.0  ·  HF 赞：6  ·  来源：huggingface
- 兴趣命中：agent, benchmark, spec
- 作者：Wanyi Chen, Wanqin Shen, Yuanchen Shi, Zhensu Sun, Fang Kong
- 链接：[arXiv](https://arxiv.org/abs/2610.24611) · [PDF](https://arxiv.org/pdf/2610.24611) · [HF](https://huggingface.co/papers/2610.24611)

Evaluating software agents on a full benchmark is expensive. A small task subset can preserve agent rankings while yielding inaccurate scores. Historical responses provide useful structure, but tasks with identical source responses can have different outcomes for a new target agent. We introduce Hierarchical Score Posterior Recovery (HSPR), which combines source-fitted response factors with uncertain group success…

## 61. Harness-Delta Attribution: Dissecting Gains From Harness Evolution

- 分数：17.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark, coding, spec
- 作者：Wenxuan Ding, Qin Lu, Changlong Yu, Sha Li, Shuowei Jin, Xin Liu, Zhenyu Shi, Greg Durrett
- 链接：[arXiv](https://arxiv.org/abs/2610.22466) · [PDF](https://arxiv.org/pdf/2610.22466) · [HF](https://huggingface.co/papers/2610.22466)

Harness evolution automatically optimizes the prompts, skills, tools, and orchestration code around a fixed-weight model, offering a way to improve agentic systems without updating model weights. The agent harness is iteratively optimized to achieve higher performance on the search set. But how much of this gain reflects benchmark-specific overfitting or additional inference-time compute, and how much may generalize…

## 62. AffordanceWAM: Affordance-Aware Joint World-Action Modeling for Robot Manipulation

- 分数：16.5  ·  HF 赞：17  ·  来源：huggingface
- 兴趣命中：-
- 作者：Jiadi You, Qize Yu, Yue Chen, Minghong Cai, Zhide Zhong, Yuran Wang, Bowen Ping, Jiaqi Liang, Zhenhao Shen, Haodong Yan, Yinchuan Li, Ruihai Wu, Xiaojuan Qi, Yingcong Chen
- 链接：[arXiv](https://arxiv.org/abs/2609.22332) · [PDF](https://arxiv.org/pdf/2609.22332) · [HF](https://huggingface.co/papers/2609.22332)

Generalizable robot manipulation requires predicting how a scene will evolve, identifying where interactions are feasible, and determining how to act. Action-labeled robot videos directly supervise control but are costly and limited in diversity, whereas egocentric human videos capture diverse interactions but lack robot actions and differ in embodiment and appearance. We introduce AffordanceWAM, an affordance-aware…

## 63. PhysSkin++: Real-Time and Generalizable Physics-Based Animation via Self-Supervised Neural Skinning

- 分数：16.5  ·  HF 赞：13  ·  来源：huggingface
- 兴趣命中：spec
- 作者：Yuanhang Lei, Baofei Liu, Xingxuan Li, Tao Cheng, Zixuan Wang, Boming Zhao, Yujun Shen, Siyuan Huang, Ruizhen Hu, Peter Yichen Chen, Hujun Bao, Zhaopeng Cui
- 链接：[arXiv](https://arxiv.org/abs/2610.26067) · [PDF](https://arxiv.org/pdf/2610.26067) · [HF](https://huggingface.co/papers/2610.26067)

Generalizing real-time physics-based animation across diverse 3D shapes and spatial discretizations remains challenging. In this paper, we introduce PhysSkin++, a physics-informed framework that learns continuous neural skinning fields from static geometries to construct compact deformation subspaces. Specifically, we propose a Neural Skinning Fields Autoencoder that predicts shape-dependent deformation subspaces…

## 64. Policy Is Not Capability: Some Safety Benchmarks Measure Which Definition of "Unsafe" You Trained On

- 分数：16.5  ·  HF 赞：9  ·  来源：huggingface
- 兴趣命中：evaluation, benchmark
- 作者：Vahid Jebraeeli, Jonathon Romero, Yijin Wang, Adrian Chan, Jianbang Zhang
- 链接：[arXiv](https://arxiv.org/abs/2610.25060) · [PDF](https://arxiv.org/pdf/2610.25060) · [HF](https://huggingface.co/papers/2610.25060)

A guardrail classifier is reported as if unsafe were a property of text. It is not: it is a property of a policy, and the policy enters the model through its labels. We exploit an accident of an industrial deployment in which the same ~53k prompts were labelled twice, under two operational definitions ("is this a request for harmful content?" and "would a moderator block this?"), and used to train ten guardrail arms…

## 65. From Short Clips to Real-Time Streams: Identity-Aware Supervision and Context-Efficient Generation for Video Face Swapping

- 分数：16.5  ·  HF 赞：9  ·  来源：huggingface
- 兴趣命中：evaluation, spec
- 作者：Zekai Luo, Yuwei Liang, Ruiqi Ma, Haoyu Huang, Xuehao Wang, Huanyi Zheng, Mingyu Liu, Linhao Zhong, Chenchen Jing, Yuling Xi, Hao Chen
- 链接：[arXiv](https://arxiv.org/abs/2610.26681) · [PDF](https://arxiv.org/pdf/2610.26681) · [HF](https://huggingface.co/papers/2610.26681)

Video face swapping transfers the reference identity to a target video while preserving its other attributes and motion. Despite recent progress in reference-guided flow-based methods, jointly achieving faithful identity transfer, high fidelity, and real-time generation over long video streams remains challenging. To address this challenge, we rethink the task-specific structure of reference-guided video face…

## 66. PAR: Progress-Aligned Recurrence for Length Generalization in State Tracking

- 分数：16.5  ·  HF 赞：9  ·  来源：huggingface
- 兴趣命中：language model, spec
- 作者：Pan Wang, Yihao Hu, Guangyuan Dong, Yitong Lin, Hang Wang, Zimi Liu, Zhihao Wen, Jianshe Li, Jiang-Ming Yang, Wei Wu, Yongqi Tong
- 链接：[arXiv](https://arxiv.org/abs/2610.27628) · [PDF](https://arxiv.org/pdf/2610.27628) · [HF](https://huggingface.co/papers/2610.27628)

Looped language models can run more iterations at test time, but additional iterations need not help them solve longer problems. For sequential state tracking, final-answer supervision does not specify how far each iteration should advance, and repeated updates can change the scale of the recurrent state. We introduce Progress-Aligned Recurrence (PAR), which trains the prediction at iteration k to match the state…

## 67. Empowering Edge Agents: A Systematic Analysis of Edge-Cloud Collaboration in LLM Agent Execution

- 分数：16.5  ·  HF 赞：5  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark
- 作者：Pengcheng Huang, Zhenghao Liu, Shixin Ren, Shi Yu, Sijia Yao, Yukun Yan, Chaojun Xiao, Maosong Sun
- 链接：[arXiv](https://arxiv.org/abs/2610.17816) · [PDF](https://arxiv.org/pdf/2610.17816) · [HF](https://huggingface.co/papers/2610.17816)

Edge-cloud collaboration combines the lower inference overhead and greater data locality of edge-side execution with the stronger capabilities of cloud-hosted models. However, as LLM agents increasingly operate in long-horizon scenarios, cloud participation becomes interleaved throughout execution rather than a one-shot decision for each query. Such interleaved participation introduces trajectory-level effects that…

## 68. HumanSkill-4D: Training-Free Language Querying of Animatable Gaussian Avatars in Space and Time

- 分数：16.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：memory, benchmark, language model, large language, spec
- 作者：unsu Kim, Naeun Kim, Dongyoon Han, Seungryul Baek
- 链接：[arXiv](https://arxiv.org/abs/2610.24452) · [PDF](https://arxiv.org/pdf/2610.24452) · [HF](https://huggingface.co/papers/2610.24452)

We introduce avatar referring segmentation, which selects regions of animatable Gaussian avatars from language queries. A query can also specify a pose or motion to select matching intervals. This lets users interact with avatars for local editing and motion inspection. However, making these selections with existing language Gaussian splatting methods poses two challenges: adjacent parts and garments are hard to…

## 69. Harness Self-Evolution for Long-Horizon Terminal Agents

- 分数：16.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark, spec
- 作者：Ruhan Wang, Yucheng Shi, Zongxia Li, Junyao Yang, Zhongzhi Li, Yue Yu, Haitao Mi, Dongruo Zhou, Leoweiliang
- 链接：[arXiv](https://arxiv.org/abs/2610.27435) · [PDF](https://arxiv.org/pdf/2610.27435) · [HF](https://huggingface.co/papers/2610.27435)

Long-horizon terminal agents may solve a task in one run yet fail across repeated runs. Stochastic errors can propagate through actions and context, creating a gap between capability and reliable execution. We present RiseHarness, a framework for iteratively improving agent harnesses with model weights fixed. It focuses on flipping tasks with both successful and failed runs under the same configuration, using…

## 70. FineSplat: Fine Patches, Local Groups, Detailed Splats

- 分数：16.0  ·  HF 赞：16  ·  来源：huggingface
- 兴趣命中：-
- 作者：Hyebin Kim, Hwasik Jeong, Joonhyuk Park, Gyeongjin Kang, Jungwoo Kim, Younghyun Kim, Eunbyung Park
- 链接：[arXiv](https://arxiv.org/abs/2610.25011) · [PDF](https://arxiv.org/pdf/2610.25011) · [HF](https://huggingface.co/papers/2610.25011)

Feed-forward 3D Gaussian Splatting (3DGS) promises instant scene reconstruction with high-quality novel-view synthesis. Yet, fine-grained geometry and appearance remain difficult to recover, motivating us to revisit how feed-forward models represent, aggregate, and refine detailed visual information. We introduce FineSplat, a feed-forward 3DGS framework built around fine-grained image patches. Since global…

## 71. Frechet Forcing: Training Long-Horizon Streaming World Models from Short Clips

- 分数：16.0  ·  HF 赞：16  ·  来源：huggingface
- 兴趣命中：-
- 作者：Yian Zhao, Yu Yan, Hongcan Guo, Ruochong Zheng, Jian Zhang, Jie Chen
- 链接：[arXiv](https://arxiv.org/abs/2610.25666) · [PDF](https://arxiv.org/pdf/2610.25666) · [HF](https://huggingface.co/papers/2610.25666)

Streaming video world models generate the future chunk by chunk, conditioned on their own past and a stream of actions. Trained on short clips, they drift once a rollout exceeds the training horizon, as prediction errors re-enter the context and compound. A common remedy is to train the model on its own rollouts via distribution matching distillation (DMD). For action-conditioned world models, the teacher becomes a…

## 72. CyberArena: Benchmarking AI Agents in Live Symmetric Attack-and-Defense Combat

- 分数：16.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：agent, benchmark, spec
- 作者：Bangya Liu, Jianhong Tu, Yueyang Pan, Hanhong Zhao, Zhe Ye, Hongwei Li, Saastha Vasan, Katherine Lambert, Junmin Zhu, Hao Wang, Jienan Chen, Yunze Xiao, Minglai Yang, Zihan Wang, Hairong Yin, Hao Wang, Zhiwen Fan, Tianneng Shi, Zhun Wang, Chenguang Wang, Dawn Song
- 链接：[arXiv](https://arxiv.org/abs/2610.19005) · [PDF](https://arxiv.org/pdf/2610.19005) · [HF](https://huggingface.co/papers/2610.19005)

AI agents are demonstrating increasingly strong offensive and defensive cybersecurity capabilities in the real world. Current benchmarks mostly evaluate agents in isolation against static targets. Real cyber operations, however, are dynamic and coupled: security postures constantly change as attackers and defenders adapt to each other in real time. Static benchmarks quickly saturate and miss an agent's ability to…

## 73. Competence-Based Evaluation of Logical Reasoning in Large Language Models

- 分数：16.0  ·  HF 赞：0  ·  来源：huggingface
- 兴趣命中：reasoning, evaluation, benchmark, language model, large language
- 作者：Jize Jiang, Chengxiang Zhai
- 链接：[arXiv](https://arxiv.org/abs/2610.22894) · [PDF](https://arxiv.org/pdf/2610.22894) · [HF](https://huggingface.co/papers/2610.22894)

Recent advances in large language models (LLMs) have brought impressive performance across diverse tasks; however, shortcomings remain in logical reasoning, including inconsistencies under linguistic variation. To improve the reasoning capacity of LLMs, we must be able to accurately measure their reasoning capacity. Current benchmarks primarily report single accuracy numbers on selected reasoning tasks. Such a…

## 74. More Memory, Worse Agents: Error Reproduction and Anti-Persistence in LLM Agents

- 分数：16.0  ·  HF 赞：0  ·  来源：huggingface
- 兴趣命中：agent, memory, benchmark, spec, retrieval
- 作者：Ruhan Wang, Kishan Panaganti, Dongruo Zhou
- 链接：[arXiv](https://arxiv.org/abs/2610.27406) · [PDF](https://arxiv.org/pdf/2610.27406) · [HF](https://huggingface.co/papers/2610.27406)

LLM agents can improve across tasks without updating model parameters by storing experience from their own executions in external memory and reusing it to guide later decisions. A central design question is whether to retain only observed trajectories and outcomes or also the rules, summaries, and skills inferred from them. Retaining these abstractions allows agents to reuse strategies without repeatedly deriving…

## 75. Breaking Diffusion: Parallel Reasoning with Draft Refinement

- 分数：16.0  ·  HF 赞：0  ·  来源：huggingface
- 兴趣命中：reasoning, evaluation, language model, spec
- 作者：Jaesang Yu, Seoyeon Byun, Yun Wang, Yan Lu, Juho Kim
- 链接：[arXiv](https://arxiv.org/abs/2610.26542) · [PDF](https://arxiv.org/pdf/2610.26542) · [HF](https://huggingface.co/papers/2610.26542)

Drafting an answer allows a reasoning model to reconsider each decision in the context of the others. Yet repeated diffusion denoising does not ensure that individually plausible token updates form a better answer together. We introduce Draft Refinement Language Models (DRLMs), which use a single denoiser to propose parallel revisions and evaluate a candidate draft. We train the denoiser to reconstruct every token…

## 76. A Conditional No-Hair Theorem for Transformers: How Language Models Forget Their Prompt

- 分数：15.5  ·  HF 赞：7  ·  来源：huggingface
- 兴趣命中：memory, language model
- 作者：Shuyang Xiang
- 链接：[arXiv](https://arxiv.org/abs/2610.24133) · [PDF](https://arxiv.org/pdf/2610.24133) · [HF](https://huggingface.co/papers/2610.24133)

We ask how much an autoregressive transformer retains of its prompt after generating t tokens. Consider two different prompts followed by the same continuation text, so that any difference in their hidden states comes from the prompt alone, and we find that the distance between their hidden states decays approximately as a power law t^{-α}, where α=1 is the rate at which a fixed prompt's share of uniform attention…

## 77. Token-Set Choice Confounds POPE: A Systematic Audit of Yes/No Extraction in VLM Hallucination Evaluation

- 分数：15.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：evaluation, benchmark, spec
- 作者：Kesav Kumar Jayakumar, Karthigeyan Thilak
- 链接：[arXiv](https://arxiv.org/abs/2610.25964) · [PDF](https://arxiv.org/pdf/2610.25964) · [HF](https://huggingface.co/papers/2610.25964)

We set out to reproduce a recent hallucination-mitigation result on the POPE benchmark. The LLaVA-1.5-7B baseline we measured, 82.21 F1 on the adversarial split, sat 1.21 to 8.67 points above the adversarial baselines we planned to compare against (81.00, 79.30, and 73.54). We looked at the evaluation code and found a readout choice that moves F1 on its own. A two-token logit readout decides yes versus no by…

## 78. ECHO: Efficient Causal Self-Recursion Beyond Auxiliary Multi-Token Prediction

- 分数：15.0  ·  HF 赞：10  ·  来源：huggingface
- 兴趣命中：reasoning
- 作者：Yuxuan Zhou, Junyuan Shang, Tianyu Wang, Chunrui Zheng, Zichang Liu, Wenbin Chang, Shuohuan Wang, Dianhai Yu
- 链接：[arXiv](https://arxiv.org/abs/2610.24766) · [PDF](https://arxiv.org/pdf/2610.24766) · [HF](https://huggingface.co/papers/2610.24766)

Existing Multi-token prediction (MTP) methods are auxiliary by design: the multi-horizon loss mostly trains modules attached to the backbone, and each added horizon costs another module and another pass. We propose Efficient Causal Self-Recursion (ECHO), which removes both costs. The backbone's own final layer predicts every horizon, so the supervision lands on the parameters that generate the next token, and…

## 79. Sparse Feature Policy Unlearning Mitigates State Hallucination in Vision-Language-Action Models

- 分数：15.0  ·  HF 赞：6  ·  来源：huggingface
- 兴趣命中：language model, spec
- 作者：Jiho Lee, Jeongeun Park, Heayoun Choi, Taekyung Kim, Eunwoo Kim
- 链接：[arXiv](https://arxiv.org/abs/2610.09496) · [PDF](https://arxiv.org/pdf/2610.09496) · [HF](https://huggingface.co/papers/2610.09496)

Vision-Language-Action (VLA) models have shown strong generalization in robotic manipulation by leveraging rich representations from pretrained vision-language models. However, their deployment in real-world environments remains limited by recurring unreliable behaviors. In this work, we study state hallucination, a recurring failure pattern in which a VLA continues acting as if an unrealized robot-object state had…

## 80. VLA-Rolling: Fewer Denoising Steps, Better Control via Adaptive Action Reuse

- 分数：14.5  ·  HF 赞：5  ·  来源：huggingface
- 兴趣命中：benchmark, planning
- 作者：Sicheng He, Yi Pan, Qiuting Yu, Jiaming Huang, Qi Lu, Shuyan Wu, Hongyan Feng, Xuanyu Liu, Jun Zhang, Jie Zhang, Wenqi Zhang, Xuhong Zhang, Jianwei Yin
- 链接：[arXiv](https://arxiv.org/abs/2610.25043) · [PDF](https://arxiv.org/pdf/2610.25043) · [HF](https://huggingface.co/papers/2610.25043)

Flow-matching vision-language-action (VLA) models generate an action chunk by iteratively denoising Gaussian noise, but typically execute only a short prefix before replanning with updated observations. Under this receding-horizon paradigm, the unexecuted remainder---the action tail---is discarded, and the next chunk is regenerated from fresh noise. We show that this discarded tail retains transferable denoising…

## 81. RealityBench: Simulated Environments to Evaluate a Vision Language Model's Ability to Document Human Physical Work

- 分数：14.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：agent, benchmark, language model
- 作者：Andrew Perrault, Anmol Takiar, Dominik Wienecki, Arnab Nandi
- 链接：[arXiv](https://arxiv.org/abs/2610.14397) · [PDF](https://arxiv.org/pdf/2610.14397) · [HF](https://huggingface.co/papers/2610.14397)

Augmenting worker capabilities in the physical world through guidance has been a decades-long goal for AI agents. One key supporting capability is to understand what the worker is doing, seeing through the human's camera or smart glasses, and assist them in documentation. Despite advances in vision language models, their capabilities in these settings remain uncertain and are challenging to benchmark because most…

## 82. UniAVC: Unified Audio-Video Creation via Progressive Training and Asymmetric Scheduling

- 分数：14.0  ·  HF 赞：8  ·  来源：huggingface
- 兴趣命中：spec
- 作者：Kien T. Pham, Yuhao Liu, Chong Hou Choi, Zhenqi He, Yanghao Wang, Chenyang Lei, Rui Liu, Qifeng Chen, Long Chen
- 链接：[arXiv](https://arxiv.org/abs/2610.24791) · [PDF](https://arxiv.org/pdf/2610.24791) · [HF](https://huggingface.co/papers/2610.24791)

Unified audio-video creation requires a single model capable of text-conditioned joint synthesis, bidirectional cross-modal generation, and instruction-guided editing across both modalities. Existing methods rely heavily on paired corpora, which are scarce for joint generation and even rarer for editing. Consequently, they are spent learning single-branch generative and editing capabilities that abundant unimodal…

## 83. Heterogeneous Agentic Coevolution

- 分数：14.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：agent, spec
- 作者：Wenqian Ye, Ziwei Guan, Zi Yang, Shivani Modi, Cici Cong Wu, Yunlong He, Yuxin Chen, Zhengyu Zhang, Liang Luo, Venkatesh Ranganathan, Jianhui Sun, Yantao Yao, Wenlin Chen, Buyun Zhang, Ellie Dingqiao Wen, Henry Kautz, Aidong Zhang
- 链接：[arXiv](https://arxiv.org/abs/2610.16078) · [PDF](https://arxiv.org/pdf/2610.16078) · [HF](https://huggingface.co/papers/2610.16078)

Recent advances in self-improving LLM agents have demonstrated the potential of AI systems that drive their own intelligence. However, many domain-specific applications rely on specialized foundation models that possess strong domain expertise but remain dependent on human-designed improvements. Extending recursive self-improvement to these models presents a key challenge: as a specialist improves, the strategies…

## 84. First Passage Attention

- 分数：14.0  ·  HF 赞：0  ·  来源：huggingface
- 兴趣命中：language model, spec, retrieval
- 作者：Yuxuan Liu
- 链接：[arXiv](https://arxiv.org/abs/2610.22714) · [PDF](https://arxiv.org/pdf/2610.22714) · [HF](https://huggingface.co/papers/2610.22714)

Augmenting softmax attention with forget gates typically relies on summing decay contributions along the key--query path. Because such accumulation is monotonic, these mechanisms cannot selectively erase intermediate context while preserving older, structurally relevant tokens. We propose First Passage Attention (FPA), which shifts from path summation to path extrema by lowering a key's logit proportionally to the…

## 85. ACEdit: Stable Multi-Turn Image Editing via Asymmetric Conditioning

- 分数：13.5  ·  HF 赞：11  ·  来源：huggingface
- 兴趣命中：-
- 作者：Sara Dorfman, Nir Goren, Gal Barak, Daniel Cohen-Or, Or Patashnik
- 链接：[arXiv](https://arxiv.org/abs/2610.22328) · [PDF](https://arxiv.org/pdf/2610.22328) · [HF](https://huggingface.co/papers/2610.22328)

Image editing models produce impressive results for individual edits, but their quality often deteriorates over multiple editing turns. Each editing turn introduces small distribution shifts that accumulate over successive edits, creating a gap between the input distributions encountered during the editor's original training and multi-turn inference. We introduce a training scheme that makes multi-turn image editing…

## 86. HandsOn: A Large-Scale Simulation Benchmark for Generalizable Dexterous Manipulation

- 分数：13.5  ·  HF 赞：7  ·  来源：huggingface
- 兴趣命中：benchmark
- 作者：Tianwei Luo, Yiming He, Hongjin Wu, Ting Pan, Debin Ren, Haorui Guo, Junlin Yang, Yuxin Zuo, Zhehao Kou, Kaisen Yang, Zhuoqun Lai, Yi Ding, Jiale Yu, Yuchen Zhang, Zijie Qiu, Haozhan Li, Ning Ding
- 链接：[arXiv](https://arxiv.org/abs/2610.26765) · [PDF](https://arxiv.org/pdf/2610.26765) · [HF](https://huggingface.co/papers/2610.26765)

General-purpose manipulation requires reliable behavior across embodiments, objects, and task demands. We introduce HandsOn, a composable simulation platform and benchmark for cross-embodiment dexterous manipulation. It supports five robotic arms, six dexterous hands, and approximately 200 rigid, articulated, and deformable assets in randomized scenes. The benchmark pairs 18,000 curated human demonstrations with 66…

## 87. Measuring Mechanistic Uncertainty in Large Language Models via Causal Robustness

- 分数：13.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：language model, large language
- 作者：Aneesh Komanduri, Majid Afshar, Timothy A. Miller, Yanjun Gao
- 链接：[arXiv](https://arxiv.org/abs/2610.22636) · [PDF](https://arxiv.org/pdf/2610.22636) · [HF](https://huggingface.co/papers/2610.22636)

Large language models (LLMs) are increasingly used in critical domains, where their susceptibility to hallucinations makes reliable and interpretable uncertainty quantification essential. We introduce the concept of mechanistic uncertainty, which characterizes uncertainty through the stability of the internal mechanisms supporting a model's response. We propose the causal robustness margin, defined as the minimum…

## 88. Vision as Proprioception: Estimating Humanoid Robot Pose from Video

- 分数：12.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：evaluation, spec
- 作者：Jiaxi Jiang, Matthias Heyrman, René Zurbrügg, Marco Hutter, Christian Holz
- 链接：[arXiv](https://arxiv.org/abs/2610.25288) · [PDF](https://arxiv.org/pdf/2610.25288) · [HF](https://huggingface.co/papers/2610.25288)

Estimating a humanoid robot's internal state from video has a wide range of real-world applications but remains unexplored. During interactions with a robot, its onboard state information may be unavailable due to privacy, ownership, or communication constraints. Meanwhile, online and AI-generated robot videos provide rich sources of data but typically lack corresponding joint configurations, limiting their direct…

## 89. TokenGate: Adapting LLMs for Fast and Memory-Efficient Prefill with Learned Token Pruning

- 分数：12.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：memory, language model
- 作者：Liana Patel, Rishabh Ranjan, Ion Stoica, Matei Zaharia, Carlos Guestrin
- 链接：[arXiv](https://arxiv.org/abs/2610.26754) · [PDF](https://arxiv.org/pdf/2610.26754) · [HF](https://huggingface.co/papers/2610.26754)

Expert human readers process large inputs (e.g., code repositories and long documents) by skimming to closely read only what matters. On the other hand, language models process all input tokens through each model layer, resulting in significant processing costs for long-context inputs. We introduce TokenGate, a small, drop-in component that extends existing trained models to enable end-to-end learnable token pruning…

## 90. QD-Rec: Open-Ended Evolution of Recommendations via Quality-Diversity

- 分数：12.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：agent
- 作者：Takashi Ishida, Taro Makino, Issa Sugiura
- 链接：[arXiv](https://arxiv.org/abs/2610.23470) · [PDF](https://arxiv.org/pdf/2610.23470) · [HF](https://huggingface.co/papers/2610.23470)

Open-ended search combined with foundation models has produced advances such as faster algorithms, new results on open mathematical problems, and self-improving agents. We extend this paradigm to recommendation for decision-making, focusing on decisions where the set of possible choices is fixed but the reasons for choosing them are not. In high-stakes decisions, e.g., which company to acquire or which customer to…

## 91. SPARC: Spoken Profile Authorship Recognition Corpus

- 分数：11.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：benchmark
- 作者：Efthymios Tsaprazlis, Bowen Yi, Tiantian Feng, Junghwan Kim, David Jurgens, Shrikanth Narayanan
- 链接：[arXiv](https://arxiv.org/abs/2610.25265) · [PDF](https://arxiv.org/pdf/2610.25265) · [HF](https://huggingface.co/papers/2610.25265)

Speech anonymization has focused on the acoustic signal, leaving open how much speaker information the transcribed words themselves retain. In this work, we study pairwise speaker and demographic-attribute verification from transcribed speech. We introduce SPARC (Spoken Profile Authorship Recognition Corpus), a benchmark built from two podcast corpora comprising over 12,500 speakers, 1.5M quality-filtered…

## 92. EMBER: Predicting TCR--pMHC Binding Without a Docked Complex

- 分数：11.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：evaluation
- 作者：Lin Ha, Chen Zhou, Haozheng Luo, Han Liu, Xiaoyu Zhang, Yan Chen
- 链接：[arXiv](https://arxiv.org/abs/2610.27334) · [PDF](https://arxiv.org/pdf/2610.27334) · [HF](https://huggingface.co/papers/2610.27334)

We propose EMBER, a structure-based framework for TCR--pMHC binding prediction that eliminates the need for a predicted docked complex, and with it the placement error that dominates such predictions. Traditional structure-based predictors utilize the co-folded complex structure of the receptor and the antigen and interpret binding from its contact surface. Consequently, every downstream feature inherits any…

## 93. Any 3D Scene is Worth 1K Tokens: 3D-Grounded Representation for Scene Generation at Scale

- 分数：11.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：spec
- 作者：Dongxu Wei, Qi Xu, Zhiqi Li, Hangning Zhou, Cong Qiu, Hailong Qin, Mu Yang, Zhaopeng Cui, Peidong Liu
- 链接：[arXiv](https://arxiv.org/abs/2604.11331) · [PDF](https://arxiv.org/pdf/2604.11331) · [HF](https://huggingface.co/papers/2604.11331)

Scene-level 3D generation has long been dominated by 2D multi-view or video diffusion models. Typically, these 2D-based approaches perform scene generation in a 2D latent space, which introduces two fundamental issues: (i) representing 3D scenes via 2D views leads to significant representation redundancy, and (ii) latent space rooted in 2D inherently limits the spatial consistency of the generated scenes. In this…

## 94. Vision-Language-Delta-Action: Learning Compact Deltas as Actionable Transition Interfaces for Robotic Manipulation

- 分数：11.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：spec
- 作者：Lingsen Zhang, Wei Li, Jie He, Henghua Zhang, Kai Mo, Shiyong Li, Yanpeng Wang, Rui Shao
- 链接：[arXiv](https://arxiv.org/abs/2610.25874) · [PDF](https://arxiv.org/pdf/2610.25874) · [HF](https://huggingface.co/papers/2610.25874)

Robotic manipulation is not merely observation-to-action generation, but the realization of task-specified state changes in the physical world. Existing vision-language-action (VLA) methods directly learn observation-to-action mappings, imposing a substantial learning burden due to the gap between semantic understanding and action execution. Although world-action models (WAMs) improve control through future…

## 95. Text-to-Image Generative Modeling Without Language Pretraining

- 分数：11.0  ·  HF 赞：6  ·  来源：huggingface
- 兴趣命中：-
- 作者：Keshigeyan Chandrasegaran, Yue Zhao, Armin W. Thomas, Ehsan Adeli, Jiajun Wu, Juan Carlos Niebles, Li Fei-Fei, Michael Poli
- 链接：[arXiv](https://arxiv.org/abs/2610.26863) · [PDF](https://arxiv.org/pdf/2610.26863) · [HF](https://huggingface.co/papers/2610.26863)

Modern text-to-image (T2I) systems use internet-scale language pretraining for text-conditioned image generation. We ask whether language pretraining is necessary for strong T2I generation. We introduce Halcyon, a family of early-fusion multimodal autoregressive models pretrained entirely from scratch on GPIC, a dataset of 100M image-text pairs. Halcyon-0.52B outperforms LlamaGen-XL/8 (48.0 vs. 63.3 gFD) with…

## 96. Beyond Maliciousness: Static and Runtime Attack-Surface Profiling of Agent Skills

- 分数：11.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：agent
- 作者：Ratnesh Pandey, Japneet Singh, Harsh Akshit, Sonali Tyagi, Cassie Crossley
- 链接：[arXiv](https://arxiv.org/abs/2610.19264) · [PDF](https://arxiv.org/pdf/2610.19264) · [HF](https://huggingface.co/papers/2610.19264)

Agent skills are Markdown documents that a tool-using agent reads as instructions and then acts on with the privileges of the session that loaded them. Installing one grants authority (the standing to direct the agent, not new privilege), and the size of that grant is what we measure. We present a two-phase attack-surface profiling methodology that combines whole-bundle static analysis and dependency provenance…

## 97. A Language-Informed Loss for Visual Generation

- 分数：11.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：language model
- 作者：Suchir Agarwal, Keshigeyan Chandrasegaran, Ziyu Chen, Kyle Sargent, Juan Carlos Niebles, Li Fei-Fei, Jiajun Wu
- 链接：[arXiv](https://arxiv.org/abs/2610.23653) · [PDF](https://arxiv.org/pdf/2610.23653) · [HF](https://huggingface.co/papers/2610.23653)

End-to-end visual generation with pixel-space loss has recently achieved competitive performance without the need for learned image tokenizers. In this work, we study whether language-informed supervision can provide a richer training signal than pixel loss for visual generation. We introduce LILIE (pronounced "lily"), a Language-Informed and Lossless Image Encoder. LILIE is an invertible image transform trained…

## 98. Beyond Compilation: Evaluating Faithful Natural-Language-to-Lean Statement Formalization

- 分数：10.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：agent
- 作者：Ke Zhang, Patricio Gallardo Candela, Sudhir Murthy, Yi Xie, Zhi Wang, Maziar Raissi
- 链接：[arXiv](https://arxiv.org/abs/2606.31002) · [PDF](https://arxiv.org/pdf/2606.31002) · [HF](https://huggingface.co/papers/2606.31002)

Lean verifies that a generated declaration is well typed, but cannot check whether it states what the user intended. We measure how far compilation overstates faithfulness in statement autoformalization without canonical Lean targets. Our criterion requires Lean compilation and agreement of two LLM judges from different model families. On an independent random audit, it agrees with the human majority on 91.5% of…

## 99. Legal Guidance in the Wild: How Users Seek Legal Help in Real-World LLM Conversations

- 分数：10.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：evaluation
- 作者：Amirreza Mohseni, Gerasimos Spanakis
- 链接：[arXiv](https://arxiv.org/abs/2610.25159) · [PDF](https://arxiv.org/pdf/2610.25159) · [HF](https://huggingface.co/papers/2610.25159)

People ask conversational AI models about their legal rights, obligations, procedures, and personal situations that may have legal consequences. To study this behavior, we first need to distinguish requests for legal guidance from other legally themed discussions and unrelated conversations. We contribute a multi-axis taxonomy of legal queries capturing whether legal guidance is sought, how a request is formulated,…

## 100. TRACE: Tracking Multimodal Clinical Trajectories for Inpatient Risk Prediction

- 分数：10.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：spec
- 作者：Minjun Kim, Jong Hak Moon
- 链接：[arXiv](https://arxiv.org/abs/2610.25765) · [PDF](https://arxiv.org/pdf/2610.25765) · [HF](https://huggingface.co/papers/2610.25765)

Accurate inpatient risk prediction requires modeling heterogeneous clinical evidence that accumulates irregularly over time. This challenge spans in-hospital mortality, prolonged length of stay, and readmission, each with task-specific observation windows. Existing multimodal approaches combine structured health record data, chest x-rays, and clinical text, but primarily focus on modality fusion or missing-modality…

## 101. ActionRoPE: action as coordinates for spatially consistent control in planar-camera game world models

- 分数：10.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：-
- 作者：Zhiyang Deng, Yuzhe Wu, Zijun Lin, Yeying Jin
- 链接：[arXiv](https://arxiv.org/abs/2610.25861) · [PDF](https://arxiv.org/pdf/2610.25861) · [HF](https://huggingface.co/papers/2610.25861)

Game world models have made rapid progress toward real-time interactive generation. Yet action control is still predominantly implemented as feature conditioning, leaving the model to learn from training data how each action should move the visual world. This formulation is poorly matched to a broad class of planar-camera worlds, such as top-down and isometric games. In these worlds, player motion induces a…

## 102. WinARDet: Compressed Window Auto-Regression for Long-Horizon Vision-Language Grounding

- 分数：10.0  ·  HF 赞：0  ·  来源：huggingface
- 兴趣命中：coding
- 作者：Chenxu Wang, Hangyi Kuang, Bo-Wen Yin, Yuxuan Li, Quan-Sheng Zeng, Yang Zhang, Xu Guo, Xiang Li, Qibin Hou
- 链接：[arXiv](https://arxiv.org/abs/2610.19419) · [PDF](https://arxiv.org/pdf/2610.19419) · [HF](https://huggingface.co/papers/2610.19419)

MLLM-based detectors formulate vision-language grounding as autoregressive coordinate generation, yet in dense scenes, they often collapse into a box repetition loop, repeatedly emitting identical boxes until the decoding budget is exhausted. We trace this failure to historical-answer attention takeover: Under full-history autoregression, repeated coordinate tokens in the growing answer history attract…

## 103. In PRAISE of Attributes: Grounding Retrieval Geometry with Query-Conditioned Subspaces for Person Re-Identification

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, language model, spec, retrieval
- 作者：Rajarshi Bhattacharya, Aryan Shukla, Shakeeb Murtaza, Christian Desrosiers, Jose Dolz, Maguelonne Heritier, Eric Granger
- 链接：[arXiv](https://arxiv.org/abs/2610.27944) · [PDF](https://arxiv.org/pdf/2610.27944) · [HF](https://huggingface.co/papers/2610.27944)

Person re-identification (ReID) ranks an image gallery using either an image query or a textual query. In image-to-image (I2I) ReID, viewpoint, illumination, occlusion, and background changes can make distractors appear more similar than the true match. In text-to-image (T2I) ReID, incomplete or ambiguous descriptions may omit key visual evidence. We study this problem for vision-language model (VLM) based ReID,…

## 104. Adaptive Stopping of Streamed Reasoning for Language Model Agents

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reasoning, evaluation, language model, spec
- 作者：JunHyeok Oh, Byung-Jun Lee
- 链接：[arXiv](https://arxiv.org/abs/2610.27981) · [PDF](https://arxiv.org/pdf/2610.27981) · [HF](https://huggingface.co/papers/2610.27981)

Reasoning-enabled language model agents can incur substantial computation before acting, although the reasoning needed varies across decisions. Existing stopping signals, such as confidence and intermediate-answer stability, can vary in effectiveness across reasoning models; signals obtained from hidden states or token probabilities also require internal access that may be unavailable or impractical. We introduce…

## 105. Building Telecom Language Models with RSOD: Domain Data, Specialist Post-Training, Memory-Conscious Distillation, and Networking Evaluation

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, evaluation, language model, spec
- 作者：Anil Srirangapatna Nagesh, Nitin Gupta, Anuj Taneja, Vivek Singh, Shane Eleniak, Theo Zhao, Moulidharan N, Shashank Keshetty
- 链接：[arXiv](https://arxiv.org/abs/2610.27993) · [PDF](https://arxiv.org/pdf/2610.27993) · [HF](https://huggingface.co/papers/2610.27993)

Telecom language models must combine broad networking knowledge with specialist behavior across routing, broadband services, access technologies, and operational diagnostics while remaining practical to deploy as a single model. We present an end-to-end framework that builds source-grounded synthetic training data from structured networking taxonomies and expert graphs, materializes 212,559 routed training records…

## 106. RANGER: Retrieval Agent for Navigating Graphs with Semantic Evaluation Rewards

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reasoning, reinforcement learning, evaluation, language model, large language, retrieval
- 作者：Artem Mikhaylov, Pavel Konoplev, Nikolay Efanov, Artyom Sorokin, Evgeny Burnaev
- 链接：[arXiv](https://arxiv.org/abs/2610.28010) · [PDF](https://arxiv.org/pdf/2610.28010) · [HF](https://huggingface.co/papers/2610.28010)

The integration of Large Language Models and Reinforcement Learning offers a promising direction for complex sequential decision-making tasks, such as multi-hop question answering over knowledge graphs. While LLMs provide strong semantic understanding and reasoning capabilities, they often struggle with precise, multi-step navigation in structured environments. Conversely, RL agents excel at learning navigation…

## 107. P$^3$-VLM: A Point-based Alternative for Grounded 3D Vision-Language Models

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, evaluation, benchmark, language model
- 作者：Anna-Maria Halacheva, Jan-Nico Zaech, Sombit Dey, Luc Van Gool, Danda Pani Paudel
- 链接：[arXiv](https://arxiv.org/abs/2610.28018) · [PDF](https://arxiv.org/pdf/2610.28018) · [HF](https://huggingface.co/papers/2610.28018)

Examining existing benchmarks for grounding in 3D VLMs reveals a pervasive "semantic leakage" in the evaluation and prompting protocols: a heavy reliance on bounding boxes as spatial prompts or representation primitives. Because bounding boxes are highly informative of object categories, they introduce a shortcut for the models to neglect visual information during 3D VLM training. We demonstrate this with a "blind"…

## 108. TrajEvolve: Trajectory Evolution for Reinforcement Learning with Hindsight Credit Assignment

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, reinforcement learning, language model, large language
- 作者：Yi Wen, Hao Chen, Wanyu Wang, Maolin Wang, Pengyue Jia, Derong Xu, Huize Tan, Yingyi Zhang, Wenlin Zhang, Weihong Luo, Xiku Du, Xiangyu Zhao
- 链接：[arXiv](https://arxiv.org/abs/2610.28060) · [PDF](https://arxiv.org/pdf/2610.28060) · [HF](https://huggingface.co/papers/2610.28060)

The Reinforcement Learning (RL) paradigm has achieved remarkable success in enhancing the reasoning capabilities of Large Language Models (LLMs). However, when applied to long-horizon tasks, it faces severe challenges: i) Due to the high task complexity, the model struggles to sample enough successful trajectories, resulting in slow convergence. ii) Relying solely on sparse final rewards causes all steps to be…

## 109. Slot-JEPA: Object-Structured Prediction Interfaces for Latent World Models

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, benchmark, spec, planning
- 作者：Peisong Wen, Qianqian Xu, Minye Lei, Siran Dai, Yang Liu, Qingming Huang
- 链接：[arXiv](https://arxiv.org/abs/2610.28074) · [PDF](https://arxiv.org/pdf/2610.28074) · [HF](https://huggingface.co/papers/2610.28074)

As a prototypical latent world model, Joint-Embedding Predictive Architectures (JEPAs) provide strong semantic representations. However, dense patch representations expose a redundant interface to downstream predictors, which must implicitly infer spatial organization and temporal correspondence, presenting three challenges. First, object information is distributed across patches, forcing each downstream predictor…

## 110. WildAIGC-Bench: Can AI Image Detectors Handle the Wild? A Benchmark of Generated and Edited Images in Online Circulation

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, language model, large language, spec
- 作者：Zijian Yu, Hangwei Zhang, Jun Lan, Huijia Zhu, Weiqiang Wang, Jianfu Zhang
- 链接：[arXiv](https://arxiv.org/abs/2610.28087) · [PDF](https://arxiv.org/pdf/2610.28087) · [HF](https://huggingface.co/papers/2610.28087)

AI-generated images linked to news events and online claims can mislead audiences, enable fraud, or cause public controversy. We introduce WildAIGC-Bench, built through recurring collection across news websites, fact-checking sources, and related social media content. The pipeline combines broad coverage, timely updates, and human-verified labels through scheduled discovery, automatic screening and preliminary…

## 111. BAIT: Can LLMs Find What Biases a Reader? A Benchmark for Cognitive Bias Triggers in News

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, language model, large language, spec
- 作者：Yousra Fettach, Tijl De Bie
- 链接：[arXiv](https://arxiv.org/abs/2610.28092) · [PDF](https://arxiv.org/pdf/2610.28092) · [HF](https://huggingface.co/papers/2610.28092)

Persuasive writing exploits cognitive biases, recruiting a reader's mental shortcuts to shape belief, often without the reader noticing. We call the linguistic features exploiting such mental shortcuts cognitive bias triggers. As large language models (LLMs) increasingly mediate how people encounter news, summarizing it, ranking it, and answering questions over it, a natural question is whether they can recognize…

## 112. PointForward V2: Point-Aligned Interaction for Feedforward Driving Reconstruction

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, benchmark, coding, spec
- 作者：Xianqi Wang, Cheng Chi, Yuechuan Pu, Hongcheng Luo, Junda Cheng, Guang Chen, Hangjun Ye, Bing Wang, Xin Yang
- 链接：[arXiv](https://arxiv.org/abs/2610.28120) · [PDF](https://arxiv.org/pdf/2610.28120) · [HF](https://huggingface.co/papers/2610.28120)

Feedforward reconstruction of dynamic driving scenes requires integrating observations across multiple views and time steps into a coherent 3D representation. PointForward established state-of-the-art feedforward driving reconstruction by lifting image observations into sparse 3D queries, demonstrating the effectiveness of point-aligned scene representations. However, these queries are largely processed…

## 113. Interruption-Aware Recurrent Reinforcement Learning for UAS Navigation Under Temporary Overrides

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, memory, reinforcement learning, benchmark
- 作者：Christopher Conrad, Deepak Panda, Weisi Guo, Antonios Tsourdos
- 链接：[arXiv](https://arxiv.org/abs/2610.28121) · [PDF](https://arxiv.org/pdf/2610.28121) · [HF](https://huggingface.co/papers/2610.28121)

Safe autonomous navigation of UASs requires tactical deconfliction to address conflicts that strategic coordination cannot prevent. This task is challenging under partial observability, when sensor or traffic data are missing, delayed, or degraded. Geometry-based methods can offer separation assurances but face limitations in dense encounters. Recurrent reinforcement learning has therefore been proposed to learn…

## 114. From Code Generator to Engineering Companion: A Plant-aware Agent for PLC Programming

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, language model, large language, coding, spec, retrieval
- 作者：Joschka Kersting, Gesa Benndorf
- 链接：[arXiv](https://arxiv.org/abs/2610.28160) · [PDF](https://arxiv.org/pdf/2610.28160) · [HF](https://huggingface.co/papers/2610.28160)

Programmable Logic Controller (PLC) coding remains a manual, IDE-centric task that demands constant context switching between documentation, project files, and code editors. Recent work has demonstrated that retrieval-augmented large language models can generate vendor-compliant Structured Text at high compilation rates \cite{pred}, yet these systems treat code generation as a one-shot pipeline: the engineer submits…

## 115. Africa-Papers: A 10-Billion-Token Multi-Domain Academic Corpus for African Foundation Language Models

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, evaluation, language model, large language
- 作者：Mich-Seth Owusu
- 链接：[arXiv](https://arxiv.org/abs/2610.28173) · [PDF](https://arxiv.org/pdf/2610.28173) · [HF](https://huggingface.co/papers/2610.28173)

Large Language Models (LLMs) depend fundamentally on the diversity, depth, and factual rigor of their pre-training corpora. However, contemporary foundational pre-training datasets (such as The Pile, S2ORC, and Dolma) exhibit a severe structural omission: African scientific, medical, legal, and agricultural scholarship constitutes less than 0.5% of global pre-training tokens. Consequently, state-of-the-art models…

## 116. Temporal Evidence-Parameter Co-Alignment for LLM Reasoning over Temporal Knowledge Graphs

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, reasoning, evaluation, benchmark, language model, large language, retrieval
- 作者：Jiapu Wang
- 链接：[arXiv](https://arxiv.org/abs/2610.28176) · [PDF](https://arxiv.org/pdf/2610.28176) · [HF](https://huggingface.co/papers/2610.28176)

Large Language Models (LLMs) often struggle with temporally grounded reasoning because their static parametric memory is misaligned with the dynamic evolution of real-world knowledge. Although RAG and Parameter-Efficient Fine-Tuning (PEFT) provide practical ways to enhance LLMs, they remain insufficient for temporal reasoning. Existing retrieval methods typically prioritize semantic relevance while overlooking…

## 117. MaD-RSI: Model-as-Data for Recursive Self-Improvement of Agent Harnesses

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, evaluation, language model, large language, spec
- 作者：Yu Cui, Hong He, Ruiqing Yue, Sicheng Pan, Zhuoyu Sun, Yifei Liu, Ting Li, Wenzhuo Zhu, Baohan Huang, Haibin Zhang, Cong Zuo
- 链接：[arXiv](https://arxiv.org/abs/2610.28201) · [PDF](https://arxiv.org/pdf/2610.28201) · [HF](https://huggingface.co/papers/2610.28201)

Recursive self-improvement (RSI) of agent harnesses has emerged as an effective approach to enhancing the capabilities of large language model (LLM) agents. By searching the harness space for a specific LLM on a given dataset, RSI can discover a harness tailored to the capabilities and behavioral characteristics of that model. However, such optimization often creates a strong coupling between the learned harness and…

## 118. Local Inference of LLMs on Long Contexts: A Data Systems Perspective

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：long context, evaluation, language model, large language, coding, spec
- 作者：Mattias Dürrmeier, Alberto Lerner
- 链接：[arXiv](https://arxiv.org/abs/2610.28223) · [PDF](https://arxiv.org/pdf/2610.28223) · [HF](https://huggingface.co/papers/2610.28223)

Large language models can solve complex problems across a variety of subjects, such as mathematics and coding. For such complex analytical tasks, models with a long context perform better. Serving models with long context is currently mostly done on powerful systems with multiple GPUs, which are too expensive for most users. An alternative is local inference, or serving a model on a user's own machine, which removes…

## 119. VGL-stGen: Learning a shared multimodal model for lung histology and spatial transcriptomics

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：language model, large language, coding, spec
- 作者：Haenara Shin, Dongjoo Lee, Sungwoo Bae, Kwon Joong Na, Daeseung Lee, Hongyoon Choi
- 链接：[arXiv](https://arxiv.org/abs/2610.28266) · [PDF](https://arxiv.org/pdf/2610.28266) · [HF](https://huggingface.co/papers/2610.28266)

VGL-stGen is a multimodal large language model adapted from a pretrained medical vision-language model using paired lung H&E and spatial transcriptomics with single-cell references. Training integrates image-expression and expression-cell-type pairs, and gene-conditioned pseudo-labels transfer transcriptomic cell-type supervision to histology images. One deployed checkpoint supports thirteen evaluated tasks spanning…

## 120. GALA: Geometry-Aware Language Model for Controllable Object Arrangement

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reasoning, benchmark, language model
- 作者：Chucheng Xiang, Runze Wang, Zhi Deng, Ruchao Bao, Yuanwei Zhang, Yuxuan Xie, Hanliu Wang, Liangzhen Fei, Wenzheng Wu, Cheng Wan, Peifeng Li, Zhongyuan Liu, Ligang Liu
- 链接：[arXiv](https://arxiv.org/abs/2610.28280) · [PDF](https://arxiv.org/pdf/2610.28280) · [HF](https://huggingface.co/papers/2610.28280)

Reasoning about fine-grained placement constraints, such as support and containment, is essential for realistic 3D scene creation. It remains a significant challenge for existing methods that rely on simplified object representations like oriented bounding box (OBB), which are blind to the detailed geometry. To address this limitation, we introduce GALA, a geometry-aware language model with explicit point cloud…
