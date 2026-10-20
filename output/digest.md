# 每日 AI 论文

生成时间：2026-10-20 04:51 UTC  ·  共 120 篇（已按 arXiv ID 去重）

来源：Hugging Face Daily Papers + arXiv（cs.AI / cs.LG / cs.CL / cs.CV）。
排序：HF 上榜、点赞、多源命中、兴趣词。兴趣词可在 `config.json` 改。

## 1. HexaShell: A Thin Harness for Exploring the Limits of VLM Agents as Robot Coding Agents

- 分数：36.0  ·  HF 赞：286  ·  来源：huggingface
- 兴趣命中：agent, memory, reasoning, language model, coding
- 作者：Hongcheng Gao, Alex Zhou, Jay Zhu, Zelin Zheng, Shijia Ge, Xiping Li, Di Wu, Yazhe Wang, Jianshu Zeng, Xuan Shangguan, Yongli Wang, Yexing Wan, Lingyu He, Zhiqi Jia, Sihang Wu, Xiao He
- 链接：[arXiv](https://arxiv.org/abs/2610.23479) · [PDF](https://arxiv.org/pdf/2610.23479) · [HF](https://huggingface.co/papers/2610.23479)

Agents built on vision language models (VLMs) now compete with learned policies on robot manipulation leaderboards. We ask how far a coding agent can go when it controls a robot instead of a computer, and where it stops. Our system, HexaShell, keeps the harness thin: it only turns the agent's commands into robot motion. The agent drives a robot with two arms through one command line. It sees three RGB cameras and…

## 2. Has GPT-6-Astra Achieved Embodied Intelligence?

- 分数：36.0  ·  HF 赞：269  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark, spec
- 作者：SenseNova, Joint Research Team, Zhongang Cai, Ziang Cao, Tailai Chen, Han Chong Chua, Linjun Dai, Hanming Deng, Hokin Deng, Haiwen Diao, Chenjing Ding, Weichen Fan, Xiao Fu, Zerui Gong, Chenyang Gu, Zexin He, Zhi Hou, Bo Li, Qinyue Li, Quanzhou Li, Xiaowan Li, Zhichao Liao, Dahua Lin, Zilong Lin, Bo Liu, Chunxiao Liu, Pengfei Liu, Tianqi Liu, Ziwei Liu, Chen Change Loy, Lewei Lu, Jiapeng Luo, Yuexiao Ma, Liang Pan, Xingang Pan, Oscar Qian, Ziyi Shang, Yuyao Shao, Dawei Su, Dacheng Tao, Qingyi Tao, Quan Wang, Ruisi Wang, Xiaogang Wang, Ziyi Wang, Beichen Wen, Donghao Wu, Jiaxu Wu, Silei Wu, Xiaoming Wu, Zhonghua Wu, Hongcan Xiao, Weiye Xu, Atsushi Yamashita, Lei Yang, Zhe Yang, Baiqiao Yin, Wanqi Yin, Hanfei Zhao, Tianbo Zhong, Long Zhuo, Jing Zuo
- 链接：[arXiv](https://arxiv.org/abs/2610.22471) · [PDF](https://arxiv.org/pdf/2610.22471) · [HF](https://huggingface.co/papers/2610.22471)

GPT-6-Astra demonstrates a level of competence in robotic manipulation and navigation that challenges the conventional paradigm of building specialized models for individual tasks and embodiments. In this report, we ask not only how capable GPT-6-Astra is, but what its capabilities imply for the field. First, we probe the limits of standalone GPT-6-Astra. We conduct a large-scale evaluation across 12 representative…

## 3. BizBench: Unveiling Hidden Challenges in Deploying Long-Horizon Agents for Real-World Business

- 分数：36.0  ·  HF 赞：206  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark, spec
- 作者：Enhan Zhao, Yongqi Tong, Xuejun Yu, Hang Wang, Pan Wang, Yichao Wang, Di He, Jianshe Li, Wei Wu
- 链接：[arXiv](https://arxiv.org/abs/2610.20424) · [PDF](https://arxiv.org/pdf/2610.20424) · [HF](https://huggingface.co/papers/2610.20424)

Existing long-horizon agent benchmarks often emphasize final task success while providing limited assessment of intermediate execution validity. Yet real-world business operations require agents to navigate extensive, potentially outdated or conflicting policies while satisfying critical constraints throughout execution. These requirements are particularly consequential in high-stakes domains such as payments, where…

## 4. Learning to Think and Explore in 3D World

- 分数：36.0  ·  HF 赞：147  ·  来源：huggingface
- 兴趣命中：reinforcement learning, benchmark, language model, coding
- 作者：Yijiang Li, Bingyang Wang, Nuno Vasconcelos
- 链接：[arXiv](https://arxiv.org/abs/2610.21783) · [PDF](https://arxiv.org/pdf/2610.21783) · [HF](https://huggingface.co/papers/2610.21783)

We study how vision-language models (VLMs) can learn to think and actively explore in 3D space. Instead of providing multi-view images, videos, or 3D representations to the model, we preserve the native visual encoding of VLMs, i.e., a single image, one at a time, just like humans, and treat the 3D representation only as an environment with which the model can interact through actions (e.g., move left) and…

## 5. LiveMACE: Process-Aware Evaluation of LLM Agent Capabilities in Evolving Markets

- 分数：36.0  ·  HF 赞：113  ·  来源：huggingface
- 兴趣命中：agent, tool use, memory, evaluation, benchmark, spec
- 作者：Jun Zhao, Leiming Fu, Yanbo Wen, Yiding Wang, Xuantong Liu, Yang Shu, Yuyang Lu, Xuanran Xing, Jingqi Tong, Hao Xu, Qi Zhang, Xuanjing Huang
- 链接：[arXiv](https://arxiv.org/abs/2610.09872) · [PDF](https://arxiv.org/pdf/2610.09872) · [HF](https://huggingface.co/papers/2610.09872)

Evaluating agents by outcomes alone can obscure the capabilities that produce them. This problem is especially pronounced in evolving environments, where outcomes reflect a closed-loop interaction between agent behavior and changing external conditions. We introduce LiveMACEBench, a process-aware benchmark that uses live financial markets as a naturally evolving testbed for persistent LLM agents. Five frontier LLMs…

## 6. OpenMobile-2: Building Versatile Mobile Agents with Scalable Environments and App-Native Tools

- 分数：35.5  ·  HF 赞：39  ·  来源：huggingface
- 兴趣命中：agent, tool use, evaluation, benchmark
- 作者：Chenyang Yan, Yingying Zhang, Kanzhi Cheng, Qiushi Sun, Zhengyuan Pan, Zheng Ma, Hang Yan, Yian Wang, Nuo Chen, Jialin Cao, Xingdong Gong, Wenpo Song, Han Chen, Zichen Ding, Fangzhi Xu, Shujian Huang, Xinyu Dai, Yichen Liu, Tiankuo Yao, Bo Wang, Ben Kao, Jianbing Zhang, Lewei Lu, Dahua Lin
- 链接：[arXiv](https://arxiv.org/abs/2610.14157) · [PDF](https://arxiv.org/pdf/2610.14157) · [HF](https://huggingface.co/papers/2610.14157)

We introduce OpenMobile-2, a near-frontier mobile agent with fully open training environments and recipes. We make three key advances: (1) Diverse environments with simulated commercial apps: We build MobileGym++, featuring 35 realistic, functionally rich commercial-style apps with cross-app workflows, while preserving full controllability for reset and verification. Together with newly configured apps in Android…

## 7. OpenVLHarness: Real World Visual Agentic Tool-Use with Multimodal Memory

- 分数：35.5  ·  HF 赞：31  ·  来源：huggingface + arxiv
- 兴趣命中：agent, tool-use, memory, reasoning, benchmark, language model, large language, coding, spec
- 作者：Yu Zhou, Cheng-Fu Yang, Rui Sun, Di Wu, Sibo Peng, Mingyang Zhang, Zhen Yang, Ruiyi Zhang, Nanyun Peng, Zhe Gan, Kai-Wei Chang
- 链接：[arXiv](https://arxiv.org/abs/2610.26860) · [PDF](https://arxiv.org/pdf/2610.26860) · [HF](https://huggingface.co/papers/2610.26860)

Multimodal large language models (MLLMs) have made rapid progress on visual reasoning, yet many tasks require evidence that is difficult to obtain through internal reasoning alone: our controlled study on 22 benchmarks shows that simply increasing the inference budget of the base model yields only modest gains. Such tasks demand grounded perception, external knowledge, and numerical measurements obtained through…

## 8. Into the Unknown: Benchmarking AI agents on open scientific research problems

- 分数：34.0  ·  HF 赞：131  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark
- 作者：Seungone Kim, Jiayi Geng, Young-Jun Lee, Bo Liu, Juyoung Suk, Nicholas Lubbers, Mitchell Wood, Marcus Noack, Yong-Xin Yao, Yuan Shi, Roxana Bujack, Cristina Garcia Cardona, Austin Rodriguez, Ilon Joseph, Woojin Cho, Zora Zhiruo Wang, Chuanyang Jin, Ian Wu, Apurva Gandhi, Tianjian Li, Weiwei Sun, Carolin Lawrence, Kiril Gashteovski, Dongyeop Kang, Jay Shin, Akari Asai, Graham Neubig, Sean Welleck
- 链接：[arXiv](https://arxiv.org/abs/2610.19159) · [PDF](https://arxiv.org/pdf/2610.19159) · [HF](https://huggingface.co/papers/2610.19159)

Can AI agents carry out research on open scientific problems? We introduce Into the Unknown, a benchmark that provides an agent with a science paper along with a research direction to pursue and tasks it to write a follow-up paper. We work with scientists at US Department of Energy (DOE) national laboratories, who each contribute an unpublished follow-up direction from their own work together with the necessary…

## 9. Tree-Aware Posterior Distillation for Long-Horizon Agentic Reinforcement Learning

- 分数：34.0  ·  HF 赞：36  ·  来源：huggingface
- 兴趣命中：agent, reinforcement learning, benchmark, language model, large language, spec
- 作者：Heming Zou, Qi Wang, Yixiu Mao, Yun Qu, Yuyi Guo, Zeyuan Liu, Chenglin Li, Weijie Liu, Saiyong Yang, Xiangyang Ji
- 链接：[arXiv](https://arxiv.org/abs/2610.23181) · [PDF](https://arxiv.org/pdf/2610.23181) · [HF](https://huggingface.co/papers/2610.23181)

Reinforcement learning with verifiable rewards has become a scalable post-training paradigm for large language models. However, training agents over long-horizon interactions presents two challenges: using only terminal rewards makes turn-level credit assignment sparse and high-variance, while sequential mini-batch updates on a fixed rollout batch introduce policy staleness as the current policy drifts from the…

## 10. From Research Goals to Scientific Closure: Evaluating Agents Through Evidence-Supported Physics Research

- 分数：33.0  ·  HF 赞：38  ·  来源：huggingface
- 兴趣命中：agent, benchmark, spec
- 作者：Yijia Mao, Song Dai, Tao Chen, Xiangyu Lu, Linqian Zeng, Chenxi Hu, Sitong Zhou, Dongyang He, Xiaodan Mao, Linxuan Zhang, Tong Zhu, Yafu Li, Fangchen Yu, Peng Ye, Feng He, Yu Cheng, Yun Luo
- 链接：[arXiv](https://arxiv.org/abs/2610.21767) · [PDF](https://arxiv.org/pdf/2610.21767) · [HF](https://huggingface.co/papers/2610.21767)

Can AI agents organize scientific investigations that lead to well-supported conclusions? To evaluate this capability, we introduce PhysClosureBench, a benchmark of 50 expert-verified, goal-specified research tasks spanning strong-field, attosecond, and neighboring physics areas. Each task specifies the research objective and essential scientific constraints, while leaving the agent to organize the investigation and…

## 11. Pack Light, CarryOn: Building Object-Oriented Context for Long-Horizon Agents

- 分数：32.0  ·  HF 赞：102  ·  来源：huggingface
- 兴趣命中：agent, spec
- 作者：Yuchen Lu, Julian McAuley, Lei Zhang
- 链接：[arXiv](https://arxiv.org/abs/2610.18784) · [PDF](https://arxiv.org/pdf/2610.18784) · [HF](https://huggingface.co/papers/2610.18784)

Long-horizon agents accumulate progress in persistent task state, yet repeatedly process interaction histories describing how that progress was achieved. This raises a natural question: can long-horizon context instead be organized around reusable progress rather than the history that produced it? In this paper, we introduce CarryOn, an object-oriented context runtime that organizes continuation around reusable task…

## 12. Scene-Designer: Learning Design Intelligence for Agentic 3D Scene Generation

- 分数：32.0  ·  HF 赞：49  ·  来源：huggingface
- 兴趣命中：agent, spec
- 作者：Xuanyu Liu, Hongyan Feng, Miao Pan, Sunlai Chen, Lizhou Liang, Bing Sun, Wenqi Zhang, Xuhong Zhang
- 链接：[arXiv](https://arxiv.org/abs/2610.23121) · [PDF](https://arxiv.org/pdf/2610.23121) · [HF](https://huggingface.co/papers/2610.23121)

Generating complete, coherent, and usable 3D indoor scenes from natural language requires strong design intelligence: the ability to design high-quality scenes and critique their quality. However, existing approaches either rely on general-purpose models lacking domain-specific design experience or learn from static scenes. In this work, we introduce Scene-Designer, an agentic framework that learns design…

## 13. LEV: Thinking Fast and Deep with Looped Decision Models

- 分数：30.0  ·  HF 赞：178  ·  来源：huggingface
- 兴趣命中：language model
- 作者：Dingjie Song, Zhiling Yan, Yuxuan Zhang, Lichao Sun
- 链接：[arXiv](https://arxiv.org/abs/2610.20951) · [PDF](https://arxiv.org/pdf/2610.20951) · [HF](https://huggingface.co/papers/2610.20951)

Decision models answer typed questions about an input with one probability per option, computed in a single forward pass without generating text. Like the fast System 1 of dual-process theory, they answer at once, but their depth is fixed at training time, so they spend the same computation on easy and hard questions. Models that reason in generated text can think longer, but they pay for every extra step in decoded…

## 14. PremiseCheck: Efficient Fact-Checking of Human and AI Peer Reviews

- 分数：30.0  ·  HF 赞：75  ·  来源：huggingface
- 兴趣命中：benchmark
- 作者：Dingjie Song, Zhiling Yan, Ziqian Zhang, Yuxuan Zhang, Lichao Sun
- 链接：[arXiv](https://arxiv.org/abs/2610.21046) · [PDF](https://arxiv.org/pdf/2610.21046) · [HF](https://huggingface.co/papers/2610.21046)

Peer review is under strain from the growth of submissions, and review comments written by humans or AI can misstate what a paper says. We introduce ReviewFact, a benchmark that labels such factual errors in review comments under one definition across NLP, machine learning, and the natural sciences, and that measures cost and latency alongside accuracy. A frontier LLM checks comments well but must read the whole…

## 15. Speculative Sampling in Interactive Video Generation

- 分数：30.0  ·  HF 赞：70  ·  来源：huggingface
- 兴趣命中：spec
- 作者：Yubo Huang, Yuxuan Zhang, Jiaming Liu, Sirui Zhao, Enhong Chen
- 链接：[arXiv](https://arxiv.org/abs/2610.20556) · [PDF](https://arxiv.org/pdf/2610.20556) · [HF](https://huggingface.co/papers/2610.20556)

Interactive video generation commonly relies on small bidirectional chunks to reduce response latency. Yet our preliminary experiments show that larger chunks improve video quality and better utilize GPU parallelism, allowing more latents to be sampled with only a modest increase in sampling time. Motivated by these observations, we propose Speculative Sampling, a strategy that combines the modeling power of large…

## 16. Self-Evolving Coding Agents via Harness-Policy Optimization

- 分数：30.0  ·  HF 赞：28  ·  来源：huggingface
- 兴趣命中：agent, reinforcement learning, benchmark, language model, large language, coding, spec
- 作者：Zhepei Wei, Wenlin Yao, Baolin Peng, Danqing Wang, Qianhui Wu, Hao Cheng, Yu Meng, Jianfeng Gao
- 链接：[arXiv](https://arxiv.org/abs/2610.22791) · [PDF](https://arxiv.org/pdf/2610.22791) · [HF](https://huggingface.co/papers/2610.22791)

Large language model (LLM) agents have shown promising potential in coding tasks, and their performance is jointly determined by the policy model and the harness that mediates their interaction with the environment. Indeed, harness and policy are mutually reinforcing and evolving only one component is suboptimal---a harness tuned for one checkpoint may not target the failure modes of an updated policy, while policy…

## 17. Xiaomi-Lens-0 Technical Report

- 分数：29.5  ·  HF 赞：27  ·  来源：huggingface
- 兴趣命中：reasoning, benchmark, language model, large language, spec
- 作者：Pei Fu, Yike Liu, Yue Sun, Hanmo Wang, Xiuwen Xi, Ruoceng Zhang, Shaojie Zhang, Chao Jiang, Hang Li, Bingrui Liu, Zhenbo Luo, Heng Qu, Changjian Xu, Ming Xu, Jian Luan
- 链接：[arXiv](https://arxiv.org/abs/2610.23279) · [PDF](https://arxiv.org/pdf/2610.23279) · [HF](https://huggingface.co/papers/2610.23279)

Multimodal large language models (MLLMs) answer questions about whole images well, yet they still struggle with fine-grained region understanding. A key reason is that text-only supervision never specifies which regions support an answer. To close this gap, we present Xiaomi-Lens-0, a 4B MLLM built on Qwen3.5 that predicts masks from its own visual representations. Specifically, a lightweight decoder combines…

## 18. RAP: A Dataset for Paper-to-Poster Generation via Declarative Markup from Human-Crafted Exemplars

- 分数：28.0  ·  HF 赞：24  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark, coding
- 作者：Haonan Han, Yukang Lin, Minliang Lin, Haoxian Tan, Jun-Yan He, Rui Yang, Zhi-Qi Cheng, Jie Hu, Guanglu Wan, Xiu Li
- 链接：[arXiv](https://arxiv.org/abs/2610.23230) · [PDF](https://arxiv.org/pdf/2610.23230) · [HF](https://huggingface.co/papers/2610.23230)

Making a conference poster is visual coding in miniature: an entire paper must be compressed onto a single page, which exercises summarization, visual design, and code implementation at once, using nothing beyond the paper itself. Yet benchmarks for this task in the context of visual coding remain scarce: existing resources are small and annotated only with layout boxes, so evaluation must fall back on VLM-as-judge…

## 19. Execution Before Memory: Diagnosing Memory Failures in Video World Models

- 分数：28.0  ·  HF 赞：24  ·  来源：huggingface
- 兴趣命中：agent, memory, evaluation, benchmark
- 作者：Weiyang Jin, Jiwen Yu, Sihan Xu, Yuwei Niu, Xihui Liu
- 链接：[arXiv](https://arxiv.org/abs/2610.23542) · [PDF](https://arxiv.org/pdf/2610.23542) · [HF](https://huggingface.co/papers/2610.23542)

A memory test for a video world model should say whether the scene was set, whether the asked change was carried out, and whether the last frame shows the result. Current tests fold these into one number, so a low score is easy to read as forgetting. When the change is not carried out, the hidden state transition cannot appear, so the test is not really a test of memory. We introduce MIST, an evaluation that…

## 20. AnyGoal: On World Model Generalization Beyond Expert Rollouts

- 分数：28.0  ·  HF 赞：16  ·  来源：huggingface + arxiv
- 兴趣命中：agent, evaluation, benchmark, spec, planning
- 作者：Heejeong Nam, Divyat Mahajan, Quentin Le Lidec, Randall Balestriero, David Klindt
- 链接：[arXiv](https://arxiv.org/abs/2610.26844) · [PDF](https://arxiv.org/pdf/2610.26844) · [HF](https://huggingface.co/papers/2610.26844)

The goal of a world model is to capture the dynamics of an environment. This has the great appeal that it allows agents to plan and simulate a course of actions with the help of a world model. For these uses to be reliable, however, the learned dynamics must behave well beyond the specific state-action combinations observed in expert rollouts. Despite this, the relationship between data coverage, dynamics…

## 21. MOSS-Image Technical Report

- 分数：27.5  ·  HF 赞：27  ·  来源：huggingface
- 兴趣命中：agent, evaluation, spec
- 作者：MOSI. AI
- 链接：[arXiv](https://arxiv.org/abs/2610.23374) · [PDF](https://arxiv.org/pdf/2610.23374) · [HF](https://huggingface.co/papers/2610.23374)

Recent closed-source image generation systems can produce diverse visual content from simple compositions to information-dense graphics, yet open-weight text-to-image models still struggle with dense text and intricate layouts. To narrow this gap, we introduce MOSS-Image, an open generation system that combines high-fidelity visual synthesis with intent-aware composition. First, we pretrain a 5B single-stream…

## 22. BridgeWAM: Bridging Video and Action Experts via Latent Bridge Queries

- 分数：26.0  ·  HF 赞：36  ·  来源：huggingface
- 兴趣命中：-
- 作者：Jiaxin Fang, Ruitong Liu, Zeyu Lai, Xingyu Wang, Mingyuan Jia, Pingyue Sheng, Weikang Wan, Mengdi Xu, Yuxiang Gao
- 链接：[arXiv](https://arxiv.org/abs/2610.14746) · [PDF](https://arxiv.org/pdf/2610.14746) · [HF](https://huggingface.co/papers/2610.14746)

World Action Models (WAMs) commonly couple video and action experts through dense, layer-wise Mixture-of-Transformers (MoT) attention, exposing action prediction to irrelevant visual features while enforcing matched expert depths. This coupling hinders selective visual-feature use and introduces redundant computation. We introduce Bridge-of-Experts (BoE), instantiated as BridgeWAM, which aggregates visual, language,…

## 23. Lexical Reference Frames: Interpreting LM Residual Streams in Native Semantics

- 分数：26.0  ·  HF 赞：32  ·  来源：huggingface
- 兴趣命中：language model
- 作者：Jian Gu, Hongyu Zhang, Chunyang Chen, Aldeida Aleti
- 链接：[arXiv](https://arxiv.org/abs/2610.22169) · [PDF](https://arxiv.org/pdf/2610.22169) · [HF](https://huggingface.co/papers/2610.22169)

The vocabulary of a language model is its native semantics: the embedding and the unembedding fix the meaning of a state at the two ends of the residual stream. Between them, existing methods either reuse a fixed lens or treat the states as a point cloud, and neither reads a state the way the model does. We argue that every hidden state has a native reference frame, induced by the layers that read it next and…

## 24. DLite: History-free Speculative Decoding for Agentic AI

- 分数：26.0  ·  HF 赞：20  ·  来源：huggingface
- 兴趣命中：agent, language model, large language, coding, spec
- 作者：Jiaming Xu, Hanzhen Wang, Tianlang Zhao, Jiewen Xiao, Chengze Yuan, Jiayi Pan, Yongkang Zhou, Jiancai Ye, Yu Wang, Guohao Dai
- 链接：[arXiv](https://arxiv.org/abs/2610.23787) · [PDF](https://arxiv.org/pdf/2610.23787) · [HF](https://huggingface.co/papers/2610.23787)

Speculative decoding has become a mainstream technique for accelerating large language model (LLM) inference by using a lightweight draft model to generate candidate tokens that are subsequently verified by the target model. However, agentic workloads introduce long and continuously evolving contexts and frequent multi-turn interactions. Under such workloads, we observe that existing draft models suffer from up to…

## 25. OR-License: Evaluating LLM Agents as Real-World Operations Research Practitioners

- 分数：25.5  ·  HF 赞：19  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark, language model, large language, coding
- 作者：Peisong Wang, Feixue Liu, Yize Meng, Bowen Liu, Ruoyu Chen, Gaoyang Dai, Xing He, Aiqian Li, Fengchi Yuan, Aochuan Chen, Chenyi Zi, Yuhan Li, Hongchuan Zeng, Yimo Yan, Nuo Chen, Jie Fu, Zuo-Jun Max Shen, Yong-Hong KUO, Jia Li
- 链接：[arXiv](https://arxiv.org/abs/2610.24087) · [PDF](https://arxiv.org/pdf/2610.24087) · [HF](https://huggingface.co/papers/2610.24087)

Can large language model (LLM) agents deliver expert-level operations research (OR) solutions directly from original client materials, without prior expert reformulation? Existing OR benchmarks typically begin with self-contained descriptions or predefined optimization tasks, underrepresenting the translation of original business materials into professionally validated solutions. We introduce OR-License, an…

## 26. CoworkEnv: Synthesizing Training Environments for Long-Horizon Cowork Agents

- 分数：25.0  ·  HF 赞：18  ·  来源：huggingface
- 兴趣命中：agent, reinforcement learning, benchmark, spec
- 作者：Zhongwei Xie, Yiming Du, Jiaxin Bai, Baixuan Xu, Chunyang Li, Xiyu Ren, Wei Fan, Tianshi Zheng, Weizhi Du, Jingqiao Yu, Xingsu Li, Zhaowei Wang, Yangqiu Song
- 链接：[arXiv](https://arxiv.org/abs/2610.24960) · [PDF](https://arxiv.org/pdf/2610.24960) · [HF](https://huggingface.co/papers/2610.24960)

AI coworkers must coordinate tools, communicate across turns, and act on changing workspace state while respecting workflow constraints. Constructing training experience for these capabilities requires coherent requests, service records, tool interfaces, and grading checks. We present CoworkEnv, a capability-guided framework for synthesizing executable training environments for AI coworkers. Workflow requirements…

## 27. MT Forcing: Towards Stable and Consistent Multi-Turn Image Editing with Autoregressive Diffusion

- 分数：24.0  ·  HF 赞：28  ·  来源：huggingface
- 兴趣命中：spec
- 作者：Houyuan Chen, Fanzhou Wang, Xiangyu Fan, Zesong Qiu, Yukun Wei, Songlin Yang, Zhitao Yang, Lvmin Zhang, Pei Yang, Hao Zhao, Lei Yang, Anyi Rao
- 链接：[arXiv](https://arxiv.org/abs/2610.25404) · [PDF](https://arxiv.org/pdf/2610.25404) · [HF](https://huggingface.co/papers/2610.25404)

Multi-turn image editing aims to modify an image according to a sequence of instructions, enabling more effective interactive visual content creation for users. However, existing methods often exhibit noticeable drift after only a few editing turns, manifesting in two aspects: 1) unstable visual quality, with accumulating artifacts and degraded details; and 2) inconsistent image content, with unintended changes to…

## 28. RoAR-VAE: Improving Latent Diffusability through Robust Prediction

- 分数：23.5  ·  HF 赞：19  ·  来源：huggingface + arxiv
- 兴趣命中：benchmark
- 作者：Yang Yue, Fangyun Wei, Yitong Wang, Jinjing Zhao, Henry Zheng, Dong Chen, Gao Huang
- 链接：[arXiv](https://arxiv.org/abs/2610.26216) · [PDF](https://arxiv.org/pdf/2610.26216) · [HF](https://huggingface.co/papers/2610.26216)

An effective visual tokenizer must preserve image fidelity while producing latents that downstream diffusion models can learn efficiently. Prior work improves latent diffusability through semantic alignment or joint tokenizer--diffusion training. Revisiting REPA-E, a representative approach, we find that removing its diffusion objective and dedicated generative blocks while retaining semantic prediction from…

## 29. Belief-Trajectory Energy: Measuring the Path to a Prediction

- 分数：23.5  ·  HF 赞：15  ·  来源：huggingface
- 兴趣命中：reasoning, language model, large language, spec
- 作者：Jiahao Ying, Wei Tang, Boxian Ai, Yaoning Wang, Haotian Chen, Wenhe Sun, Caijun Xu, Haozhan Cai, Changyi Xiao, Yixin Cao
- 链接：[arXiv](https://arxiv.org/abs/2610.05114) · [PDF](https://arxiv.org/pdf/2610.05114) · [HF](https://huggingface.co/papers/2610.05114)

Large language models (LLMs) progressively revise their predictions across Transformer layers, yet we typically observe only the final output, discarding the trajectory through which it is formed. We introduce Belief-Trajectory Energy(BTE), a model-grounded measure that characterizes an input through the layerwise predictive revisions it induces in a model. By mapping intermediate states into a shared predictive…

## 30. Stuck on Shuffle: On Attribute-Object Binding in Vision-Language Models

- 分数：23.5  ·  HF 赞：15  ·  来源：huggingface
- 兴趣命中：benchmark, language model, coding, retrieval
- 作者：Netanel Y. Tamir, Michael Green, Issar Tzachor, Or Shimshi, Dvir Samuel, Or Patashnik, Rami Ben-Ari
- 链接：[arXiv](https://arxiv.org/abs/2610.22602) · [PDF](https://arxiv.org/pdf/2610.22602) · [HF](https://huggingface.co/papers/2610.22602)

Retrieval is a fundamental task in multimodal systems: given an image or text query, the goal is to find the most relevant images or texts in a collection, often using a shared embedding space. Reliable retrieval requires these embeddings to capture not only which concepts are present, but also how they are composed. One key compositional challenge is attribute--object binding: encoding which attributes belong to…

## 31. HarnessPro: Recursive Harness Self-Improvement with Pareto Optimization for Performance-Cost Trade-offs

- 分数：23.0  ·  HF 赞：10  ·  来源：huggingface + arxiv
- 兴趣命中：agent, benchmark, spec
- 作者：Zhuoshi Pan, ZhiYuan Feng, Yukuo Cen, Honglin Lin, Junru Lu, Zhongxia Chen, Shuo Yang, H. Vicky Zhao, Jie Tang
- 链接：[arXiv](https://arxiv.org/abs/2610.26770) · [PDF](https://arxiv.org/pdf/2610.26770) · [HF](https://huggingface.co/papers/2610.26770)

Harness development plays a crucial role in building capable AI agents. Recent approaches improve harnesses through recursive self-improvement (RSI), but their performance gains often come with higher execution costs. We introduce HarnessPro, a label-free method for evolving harnesses to improve task performance while reducing execution cost. In this setting, candidate harnesses are evaluated using LLM-generated…

## 32. OmniXRef: A Unified Framework for Multimodal Multi-Reference Video Editing

- 分数：22.5  ·  HF 赞：17  ·  来源：huggingface
- 兴趣命中：evaluation, benchmark, spec
- 作者：Xiaoyan Cong, Tianyu Wang, Hyeonho Jeong, Zhifei Zhang, Yuqian Zhou, Yijun Li, Shaoteng Liu, Zhe Lin, Srinath Sridhar, Soo Ye Kim
- 链接：[arXiv](https://arxiv.org/abs/2610.22744) · [PDF](https://arxiv.org/pdf/2610.22744) · [HF](https://huggingface.co/papers/2610.22744)

Creative intent in video editing can be expressed through text instructions (e.g., "remove the people"), image references (e.g., subject appearance), video references (e.g., camera movement), or a combination of the above. We introduce OmniXRef, a unified framework for multimodal multi-reference video editing that allows users to combine variable numbers of text, image, and video references to control diverse…

## 33. OfficeTown: Generative Organizations for Evolving Agent Intelligence

- 分数：22.5  ·  HF 赞：17  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark
- 作者：Hongchen Wei, Daohong Ying, Zhi Hong, Aidan Wu, Bei Liu, Ruichun Ma, Yifan Yang, Qi Dai, Kai Qiu, Rui Xu, Dongdong Chen, Zhenzhong Chen, Chong Luo
- 链接：[arXiv](https://arxiv.org/abs/2610.23194) · [PDF](https://arxiv.org/pdf/2610.23194) · [HF](https://huggingface.co/papers/2610.23194)

AI agents increasingly use files and software tools to produce professional deliverables. Such work draws on materials, decisions, and feedback accumulated across assignments. We introduce OfficeTown, a generative simulation framework for professional organizations in which tasks and their context arise from continuing organizational work. From a natural-language description of an organization's purpose and…

## 34. SciΠvot: Benchmarking Principal-Investigator Judgment at Pivotal Moments of Scientific AutoResearch Agents

- 分数：21.5  ·  HF 赞：11  ·  来源：huggingface
- 兴趣命中：agent, reasoning, evaluation, benchmark, language model, large language
- 作者：Youran Sun, Xingyu Ren, Chugang Yi, Kejia Zhang, Di Wu, Yingkang Cao, Allen Zhou, Jianping Ye, Suying Liu, Jiaxuan Guo, Jianda Du, Weicheng Ye, Kecheng Liu, Hefan Zhang, Haixin Wang, Jie Xiao, Eric Yang, Haizhao Yang
- 链接：[arXiv](https://arxiv.org/abs/2610.21082) · [PDF](https://arxiv.org/pdf/2610.21082) · [HF](https://huggingface.co/papers/2610.21082)

Large language model (LLM) agents can keep scientific experiments running for months with little human supervision, but reliable autonomous research also requires scientific judgment. Evaluating scientific judgment is difficult because research decisions are open-ended and depend on project context. We construct SciΠvot, a 248-case benchmark of scientific judgment based on human corrections. The benchmark draws on…

## 35. ScaleNav: Scalable Internet Video Pretraining for Language-Conditioned Local Navigation

- 分数：21.0  ·  HF 赞：18  ·  来源：huggingface
- 兴趣命中：benchmark, spec
- 作者：Yihui Yang, Yuanhong Yu, Jiawei Wang, Zhongrui Yu, Jia Shi, Kun Zhan, Ruizhen Hu, Xiaowei Zhou, Yu Liu, Sida Peng
- 链接：[arXiv](https://arxiv.org/abs/2610.25690) · [PDF](https://arxiv.org/pdf/2610.25690) · [HF](https://huggingface.co/papers/2610.25690)

We study language-conditioned local navigation, where a robot must navigate to a text-specified target visible in its initial observation and stop at the described location. End-to-end navigation policies require diverse training data to generalize across scenes, yet real-robot data is costly to collect and simulated data leaves a sim-to-real gap. Internet egocentric videos offer a scalable source of real-world…

## 36. Towards Looped Models Done Right, Part I: Topology, Input Injection, Recurrent-State Design

- 分数：21.0  ·  HF 赞：10  ·  来源：huggingface
- 兴趣命中：reasoning, benchmark, language model, coding, retrieval
- 作者：Benhao Huang, Chufan Shi, Junlin Chen, Shicheng Wen, Zhengzhong Liu, Eric Xing, Xuezhe Ma
- 链接：[arXiv](https://arxiv.org/abs/2610.23036) · [PDF](https://arxiv.org/pdf/2610.23036) · [HF](https://huggingface.co/papers/2610.23036)

Looped language models reuse physical Transformer blocks across logical depth, but established architectures entangle recurrence placement, input injection, and recurrent state organization. We isolate these axes in models trained from scratch at matched parameter scale, logical depth, and token budgets, and then test whether the resulting design principles transfer to resident- and active-parameter-matched…

## 37. InfiniDream: Open-Ended Photorealistic 3D Worlds Through Procedural Generation

- 分数：21.0  ·  HF 赞：10  ·  来源：huggingface + arxiv
- 兴趣命中：evaluation, planning
- 作者：Yi-Chuan Huang, Hao-Jen Chien, Zheng-Hui Huang, Yu-Lun Liu, Kaipeng Zhang, Zhixiang Wang
- 链接：[arXiv](https://arxiv.org/abs/2610.26853) · [PDF](https://arxiv.org/pdf/2610.26853) · [HF](https://huggingface.co/papers/2610.26853)

Procedural generation plays a key role in synthetic data creation and game development, offering greater controllability, editability, and diversity than static mesh representations. However, VLM-based code generation often produces relatively simple 3D assets, while sophisticated photorealistic procedural systems require extensive manual development. Existing VLM-guided procedural methods remain largely constrained…

## 38. DuoDiscover: Scaling Autonomous Discovery Beyond the Evaluation Bottleneck

- 分数：20.5  ·  HF 赞：9  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark, coding
- 作者：Shubham Agarwal, Akshat Gupta, Mike Heddes, Dilara Soylu, Rui Meng, Patrick Tser Jern Kon, Jiefeng Chen, Mert Cemri, Shu Liu, Abe Gonzalez, Akanksha Jain, Bhavana Dalvi Mishra, Linfeng Song, Vilobh Meshram, Xiangru Tang, Jinsung Yoon, Aditya Parameswaran, Ion Stoica, Vahab Mirrokni, Burak Gokturk, Parthasarathy Ranganathan, Tomas Pfister, Nanyun Peng, Chun-Liang Li
- 链接：[arXiv](https://arxiv.org/abs/2610.17184) · [PDF](https://arxiv.org/pdf/2610.17184) · [HF](https://huggingface.co/papers/2610.17184)

Evaluation has been central to advances in AI, and it is equally critical to autonomous discovery. Yet scaling autonomous discovery to real-world engineering challenges faces a fundamental bottleneck: the cost of evaluating progress. In real settings, a single true evaluation, such as a full benchmark or serving trace, can take hours, so a search can afford only a handful of true evaluations. We present DuoDiscover,…

## 39. Manga2Animate: An Agentic Framework for Faithful Manga Animation with Script and Storyboard Planning

- 分数：20.5  ·  HF 赞：5  ·  来源：huggingface + arxiv
- 兴趣命中：agent, spec, planning
- 作者：Sheng-Wei Zhang, Hsi-An Chen, Yan-Ting Liou, Chih-Hsuan Chen, Shih-Chen Tseng, Yu-Lun Liu
- 链接：[arXiv](https://arxiv.org/abs/2610.26851) · [PDF](https://arxiv.org/pdf/2610.26851) · [HF](https://huggingface.co/papers/2610.26851)

Adapting existing manga into coherent animation that stays faithful to the source is a valuable yet challenging task. Existing methods either access the manga mainly through text, losing its characters and art style, or feed manga pages directly into video generation models, which misinterpret the manga's structure and produce incorrect storylines. In this paper, we propose Manga2Animate, a multi-agent framework…

## 40. Remembering Has a Price: Learning Memory Worth under Resource Constraints

- 分数：20.5  ·  HF 赞：1  ·  来源：huggingface + arxiv
- 兴趣命中：agent, memory, reasoning, retrieval
- 作者：Guannan Lai, Zi-Yang Bai, Jun-Peng Jiang, Han-Jia Ye
- 链接：[arXiv](https://arxiv.org/abs/2610.26453) · [PDF](https://arxiv.org/pdf/2610.26453) · [HF](https://huggingface.co/papers/2610.26453)

Lifelong agents continually accumulate and reuse experience to improve after deployment, yet in practice they often operate under tight generation, interaction, and memory budgets. Under such stringent joint constraints, we find that existing lifelong-memory methods can become ineffective, with several sophisticated approaches offering little advantage over simple retrieval or even no-memory agents. This reveals a…

## 41. Can Visual Generation Expand What Unified Multimodal Models Know?

- 分数：20.0  ·  HF 赞：20  ·  来源：huggingface
- 兴趣命中：spec
- 作者：Wenkai Li, Wenyi Hong, Zhuoyi Yang, Jie Tang
- 链接：[arXiv](https://arxiv.org/abs/2610.21459) · [PDF](https://arxiv.org/pdf/2610.21459) · [HF](https://huggingface.co/papers/2610.21459)

Unified multimodal models (UMMs) receive image-generation supervision that exposes them to visual information not fully documented in text. Can learning to generate images expand what pretrained models know? We introduce Knowledge Transfer Probing (KTP), a controlled protocol that supplies new knowledge through image-generation training and tests its accessibility through text-only question answering. Across seven…

## 42. PRISM: PRIvileged Sibling-guided Multi-Agent Topology Design

- 分数：19.5  ·  HF 赞：7  ·  来源：huggingface
- 兴趣命中：agent, benchmark, language model, large language
- 作者：Phuong Tuan Dat, Qi Li, Xinchao Wang
- 链接：[arXiv](https://arxiv.org/abs/2610.20628) · [PDF](https://arxiv.org/pdf/2610.20628) · [HF](https://huggingface.co/papers/2610.20628)

Multi-agent systems (MAS) based on large language models (LLMs) have become a powerful way to address complex problems, and their effectiveness depends critically on the collaboration topology that decides which agents participate and how they communicate. Recent work learns to generate this topology from the task query, fitting the generator to corpora of execution-verified graphs. The post-training method for such…

## 43. DiscoveryRSI: Recursively Learning to Discover Valuable Hypotheses

- 分数：19.0  ·  HF 赞：14  ·  来源：huggingface
- 兴趣命中：agent, evaluation
- 作者：Jianyuan Zhong, Chenwei Wu, Zhaochen Yu, Xixian Jiang, Xuewei Li, Hao Xiao, Xilin Dai, Junyang Wang, Jiaru Zou, Zhiqing Cui, Boyuan Zheng, Jing Xiong, Zhen Zhang, Qiang Gao, Michael Morley, Luis Nakayama, Qiang Xu, Liyue Shen, Tao Gui, Leo Anthony Celi, James Zou, Zhenfei Yin, Yingcheng Wu, Ling Yang
- 链接：[arXiv](https://arxiv.org/abs/2610.23839) · [PDF](https://arxiv.org/pdf/2610.23839) · [HF](https://huggingface.co/papers/2610.23839)

Scientific discovery requires developing worthwhile hypotheses into practical investigations, yet learning from this evolving research process remains challenging. We introduce an operational definition of valuable and testable research hypotheses: evidence-grounded claims about consequential uncertainties, coupled with feasible investigations, explicit decision criteria, and alternative explanations. Our…

## 44. Scaling Parameter-Efficient Fine-Tuning for Brain Encoding

- 分数：19.0  ·  HF 赞：10  ·  来源：huggingface + arxiv
- 兴趣命中：coding
- 作者：Zhuofan Josh Ying, Guanglong Sun, Nolan Ho, Kieran Liu, Rui Yang, Andrew Chen, Nikolaus Kriegeskorte, Pony Ma, Hossein Adeli
- 链接：[arXiv](https://arxiv.org/abs/2610.26802) · [PDF](https://arxiv.org/pdf/2610.26802) · [HF](https://huggingface.co/papers/2610.26802)

Brain encoding models aim to predict neural responses to stimuli. The most widely used approach fits readouts from frozen pretrained backbones. Using neural data to train large models from scratch or fully fine-tune them after task-pretraining has proven difficult because neural data is costly and limited. We show that parameter-efficient fine-tuning (PEFT) enables us to effectively adapt very large pretrained…

## 45. Holi-World: Building Holistic World Intelligence from Human-Ego Experience

- 分数：19.0  ·  HF 赞：6  ·  来源：huggingface + arxiv
- 兴趣命中：reasoning, evaluation
- 作者：Hao Li, Xiyuan Zheng, Yuanyuan Gao, Yalun Dai, Xinhao Ji, Xuan-Li Chen, Jing Zhao, Fangzhou Hong, Zhaoxi Chen, Ziwei Liu
- 链接：[arXiv](https://arxiv.org/abs/2610.26549) · [PDF](https://arxiv.org/pdf/2610.26549) · [HF](https://huggingface.co/papers/2610.26549)

Human egocentric experience offers a rich foundation for learning how the world is organized and how it changes through interaction. Realizing this potential at scale requires turning growing volumes of recordings into learning resources that connect scene structure, object semantics, and interaction histories across viewpoints and time, while reducing dependence on costly manual annotation. We introduce HOLI-WORLD,…

## 46. EvoWeb: A Benchmark for Coding Agents on Evolving Web Applications

- 分数：18.5  ·  HF 赞：5  ·  来源：huggingface
- 兴趣命中：agent, benchmark, coding, spec
- 作者：David Nukrai, Bar Alon, Nativ Levy, Ido Andrew Atad, Ido Cohen, Itamar Zimerman, Lior Wolf, Eli David, Ilan Naiman
- 链接：[arXiv](https://arxiv.org/abs/2610.16402) · [PDF](https://arxiv.org/pdf/2610.16402) · [HF](https://huggingface.co/papers/2610.16402)

Web application development often proceeds through successive requests that extend an existing implementation. Yet web-generation benchmarks primarily evaluate development toward fixed specifications. We introduce EvoWeb, a novel benchmark comprising 320 cumulative requests over 32 web applications, grounded in real-world product features and structured by functional dependency graphs. Agents iteratively modify a…

## 47. Sparse Autoencoders Are a Shared Coordinate System for Symbolic Matching

- 分数：18.5  ·  HF 赞：5  ·  来源：huggingface
- 兴趣命中：reasoning, language model, large language, spec
- 作者：Xiaocong Yang, Xuanyu Meng, Yuji Zhang, Jiawei Han, ChengXiang Zhai
- 链接：[arXiv](https://arxiv.org/abs/2610.19636) · [PDF](https://arxiv.org/pdf/2610.19636) · [HF](https://huggingface.co/papers/2610.19636)

Large language models (LLMs) hold broad knowledge in one set of weights, but lack interpretability and trustworthy reasoning, especially in high-stakes use cases. A neuro-symbolic model, with its interpretable architecture and System 2 reasoning capacity, is a promising alternative if built at the scale of LLMs; however, its symbolic backbone is usually constructed with human effort, so existing neuro-symbolic…

## 48. Competing Learning in Hybrid Architectures

- 分数：18.5  ·  HF 赞：1  ·  来源：huggingface + arxiv
- 兴趣命中：reasoning, language model, retrieval
- 作者：Xingyu Shen, Yingfa Chen, Ziqing Qiao, Chaojun Xiao, Xu Han, Zhiyuan Liu
- 链接：[arXiv](https://arxiv.org/abs/2610.26830) · [PDF](https://arxiv.org/pdf/2610.26830) · [HF](https://huggingface.co/papers/2610.26830)

Many modern language models have adopted hybrid architectures that incorporate both linear-time recurrence and softmax attention. Modern recurrence layers provide a highly expressive mixing mechanism while ensuring high throughput by compressing contextual information into a fixed-size state, but underperform softmax attention in contextual information retrieval. In this paper, we reveal a Competing Learning…

## 49. MTEdit: Packed Trajectories Beat Rollouts for Multi-Turn Image Editing

- 分数：18.0  ·  HF 赞：16  ·  来源：huggingface
- 兴趣命中：benchmark
- 作者：Houyuan Chen, Fanzhou Wang, Xiangyu Fan, Songlin Yang, Zhitao Yang, Lvmin Zhang, Pei Yang, Hao Zhao, Lei Yang, Anyi Rao
- 链接：[arXiv](https://arxiv.org/abs/2610.23751) · [PDF](https://arxiv.org/pdf/2610.23751) · [HF](https://huggingface.co/papers/2610.23751)

Multi-turn image editing aims to modify an image according to a sequence of instructions, making it better aligned with human-AI collaborative creation than single-turn editing. However, constructing high-quality multi-turn training data remains challenging, as conventional sequential rollout accumulates errors and introduces visual-quality drift across editing turns. To address this challenge, we introduce MTEdit,…

## 50. Failure Recovery via Belief Updates and World Modeling for Long-Horizon Agents

- 分数：18.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：agent, reasoning, benchmark, spec
- 作者：Xiyang Wu, Zhichao Liu, Shengxin zhang, Zongxia Li, Ming Li, Tianyi Zhou, Dinesh Manocha
- 链接：[arXiv](https://arxiv.org/abs/2610.18082) · [PDF](https://arxiv.org/pdf/2610.18082) · [HF](https://huggingface.co/papers/2610.18082)

Long-horizon agents often struggle to recover from failures whose causes lie several steps earlier, beyond what local reflection or backtracking can resolve. We introduce BELIEFWEAVER, a framework that combines persistent evidence across attempts with prospective reasoning over repair directions. It maintains a relational belief state over frontiers, attempts, observations, and checkpoints. Execution evidence…

## 51. Game2Real-Bench: Do Toy Games Reveal and Transfer to Real-World Visual Reasoning?

- 分数：18.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：reasoning, evaluation, benchmark, language model, planning
- 作者：Qingan Liu, Juntong Feng, Yue Zhu, Yujie Cheng, Xinzhe Han, Shuai Hao, Yunzhi Zhuge, Haiwen Diao, Huchuan Lu
- 链接：[arXiv](https://arxiv.org/abs/2610.18834) · [PDF](https://arxiv.org/pdf/2610.18834) · [HF](https://huggingface.co/papers/2610.18834)

Visual reasoning is an important capability for vision-language models (VLMs) to understand visual evidence, spatial structure, constraints, and state changes. Existing evaluations mainly rely on real-world data or procedurally generated tasks. Real-world data preserve natural complexity, while procedural games provide controllable generation and verifiable solutions. However, it remains unclear whether abilities…

## 52. Librarian Agents: Training LLMs to Curate Long-Context Workspaces that Anticipate Future Queries

- 分数：18.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：agent, reasoning, reinforcement learning, language model, large language, retrieval
- 作者：Anikait Singh, Teresa Zhang, Yoonho Lee, Roshen Sanjay Nair, Aviral Kumar, Chelsea Finn
- 链接：[arXiv](https://arxiv.org/abs/2610.22273) · [PDF](https://arxiv.org/pdf/2610.22273) · [HF](https://huggingface.co/papers/2610.22273)

Reasoning over long document contexts remains a challenge for large language models (LLMs). Standard retrieval methods are inherently reactive, bottlenecking agents with complex, cross-document reasoning at inference time, while precomputed structures like knowledge graphs often fall short because they rely on rigid heuristics. Instead, can we allow agents to perform anticipatory directed curation: learning to…

## 53. Consistent Distribution Matching for Data-Free Diffusion Distillation

- 分数：17.5  ·  HF 赞：15  ·  来源：huggingface
- 兴趣命中：evaluation
- 作者：Yuxiang Fu, Qi Yan, Zike Wu, Yongxing Zhang, Purang Abolmaesumi, Lele Wang, Renjie Liao
- 链接：[arXiv](https://arxiv.org/abs/2610.09221) · [PDF](https://arxiv.org/pdf/2610.09221) · [HF](https://huggingface.co/papers/2610.09221)

Flow and diffusion models suffer from slow inference due to computationally expensive numerical integration. Distillation provides a promising way for a student model to learn from a teacher's dynamics, enabling one-step or few-step generation. However, existing methods often depend on curated distillation datasets, costly teacher rollouts, or auxiliary proxy networks, which complicate model training and scaling. In…

## 54. Embeddings Are Overpriced? A Frozen 16 MB Vocabulary for Small and Ternary Language Models

- 分数：17.5  ·  HF 赞：7  ·  来源：huggingface
- 兴趣命中：memory, evaluation, language model
- 作者：Sai Kiran Bathula
- 链接：[arXiv](https://arxiv.org/abs/2610.22428) · [PDF](https://arxiv.org/pdf/2610.22428) · [HF](https://huggingface.co/papers/2610.22428)

In a small language model the vocabulary is the single largest part. In Gemma 3 270M the embedding table holds 168M of 268M parameters, and because quantisation methods leave the embedding in 16-bit, it is also most of the file once the rest of the model is compressed. We ask what that table actually buys. We replace it with one frozen table of 512-bit codes, 16 MB, with no trainable parameters, derived once from a…

## 55. EgoXperience: Learning World-Grounded Egocentric Representations from Human Experience

- 分数：17.5  ·  HF 赞：7  ·  来源：huggingface + arxiv
- 兴趣命中：benchmark
- 作者：Xinhao Ji, Hui En Pang, Hao Li, Kairui Hu, Jiner Wang, Mingze Sun, Ziang Cao, Yalun Dai, Thang Luu, Qin Ma, Hongyi Chen, Yukang Cao, Fangzhou Hong, Zhaoxi Chen, Ziwei Liu
- 链接：[arXiv](https://arxiv.org/abs/2610.26625) · [PDF](https://arxiv.org/pdf/2610.26625) · [HF](https://huggingface.co/papers/2610.26625)

Reconstructing human activity from egocentric video requires more than recovering individual 3D components: the observer's motion, surrounding geometry, and hand-object interactions must fit together in a consistent world. Achieving this coherence requires both joint reconstruction and aligned supervision, yet existing methods and datasets offer limited support for either. We present EgoXperience, a full-stack…

## 56. Interlock: From Local Correctness to Task Completion in Long-Horizon Agents

- 分数：17.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：agent, evaluation, language model, large language, spec
- 作者：Linji Hao, Yanji He, Zihan Wang, Hansi Yang, Jiayuan Zhang, Hongyan Hao, Qi Gu, Yan Feng, Han Wu
- 链接：[arXiv](https://arxiv.org/abs/2610.19686) · [PDF](https://arxiv.org/pdf/2610.19686) · [HF](https://huggingface.co/papers/2610.19686)

Large language model agents increasingly undertake long-horizon tasks in complex environments characterized by fragmented evidence, partially completed states, and dependencies across resources and artifacts. Existing agents may satisfy individual requirements while failing to maintain these relationships, producing locally correct but incomplete outcomes. These failures arise because task completion depends on…

## 57. ReaDy: Recurrent States as Dynamic Context for Speculative Drafting in Hybrid Linear Attention Large Language Models

- 分数：17.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：benchmark, language model, large language, coding, spec, retrieval
- 作者：Bohan Sun, Zunhai Su, Xialie Zhuang, Jianjin Li, Ngai Wong, Chuan-Wei Kuo
- 链接：[arXiv](https://arxiv.org/abs/2610.20503) · [PDF](https://arxiv.org/pdf/2610.20503) · [HF](https://huggingface.co/papers/2610.20503)

Speculative decoding accelerates autoregressive generation by drafting multiple tokens per step, yet feature-based drafters rely on target hidden features whose contextual emphasis may not align with the needs of subsequent draft positions. Hybrid linear attention (HLA) models maintain compact recurrent states that accumulate historical associations, offering an efficient source of complementary context for…

## 58. Lean4AgenticRL: Advancing Agentic RL with Verifiable Multi-level Process Rewards

- 分数：17.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：agent, reinforcement learning, language model, large language, spec
- 作者：Ruida Wang, Gerald Friedland, Tong Zhang, Chris Kong
- 链接：[arXiv](https://arxiv.org/abs/2610.22448) · [PDF](https://arxiv.org/pdf/2610.22448) · [HF](https://huggingface.co/papers/2610.22448)

Enhancing the agentic capabilities of Large Language Models (LLMs) to tackle complex software engineering (SWE) and general terminal-usage problems is a pressing challenge. Current state-of-the-art LLMs often go through large-scale agentic Reinforcement Learning (RL). However, they mostly rely on high-level outcome rewards, with minimal consideration of low-level toolcall and mid-level workflow-stage rewards, which…

## 59. Skip the Compressor: Coding Agents Fix More Issues When They Pick Whole Files

- 分数：17.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：agent, context window, benchmark, coding
- 作者：Xiaocong Yang, Rishit Chatterjee, Himanshu Udupi, Vikram Ramavarapu, ChengXiang Zhai
- 链接：[arXiv](https://arxiv.org/abs/2610.21073) · [PDF](https://arxiv.org/pdf/2610.21073) · [HF](https://huggingface.co/papers/2610.21073)

A coding agent works on repositories that can be far larger than its context window can hold. Prompt compressors and retrievers offer solutions to this problem, but patching an issue needs two things at once: the files that must change, and their code exactly as written, since the model must reproduce the lines it edits. Retrievers rank code by its similarity to the issue rather than by whether it must change, and…

## 60. Selection Is Not Learning: Choosing Model Futures

- 分数：17.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：agent, reasoning, evaluation, language model
- 作者：Haoyi Yang, Kshitij Mishra, Nils Lukas, Salem Lahlou
- 链接：[arXiv](https://arxiv.org/abs/2610.22029) · [PDF](https://arxiv.org/pdf/2610.22029) · [HF](https://huggingface.co/papers/2610.22029)

Self-evolving language models train on tasks they generate, so every round must decide which updated model the next round inherits. Current loops such as R-Zero, Agent0, and Skill Self-Play make this decision through the task, admitting tasks that look learnable and inheriting every resulting update. We identify a selection-to-update gap in these loops, where a task that looks learnable need not produce a useful…

## 61. State World Models: Execute the Rules, Generate the Pixels

- 分数：17.5  ·  HF 赞：3  ·  来源：huggingface + arxiv
- 兴趣命中：benchmark, spec
- 作者：Chan Yan Ki, Yanran Zhang, Wenzhao Zheng, Xiaofeng Wang, Zheng Zhu, Lei Chen, Jie Zhou, Jiwen Lu
- 链接：[arXiv](https://arxiv.org/abs/2610.26811) · [PDF](https://arxiv.org/pdf/2610.26811) · [HF](https://huggingface.co/papers/2610.26811)

Existing world models can generate action-conditioned video from a single image. Many focus on camera movement, allowing users to explore the generated scene. However, navigation alone does not ensure that an action follows persistent rules when its outcome depends on state that is invisible in the current frame. We present Stateful Harness, a framework that separates world evolution from video rendering to support…

## 62. Dream2Discern: Learning from Hard Latent Variants for Runtime Failure Prediction in Multi-Agent Systems

- 分数：17.0  ·  HF 赞：6  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark
- 作者：Boxuan Zhang, jianing Zhu, Xiaotian Han, Ruixiang Tang
- 链接：[arXiv](https://arxiv.org/abs/2610.16071) · [PDF](https://arxiv.org/pdf/2610.16071) · [HF](https://huggingface.co/papers/2610.16071)

Reliable deployment of LLM-based multi-agent systems calls for runtime auditors that predict terminal outcomes from observed execution prefixes. These auditors typically learn from a limited corpus of trajectories with verified outcomes. Expanding this corpus requires costly execution and verification, yet broader failure coverage alone provides no explicit criterion for identifying prefixes that the current auditor…

## 63. Think Visually Across Space and Time: Grounded Reasoning for Video Segmentation

- 分数：17.0  ·  HF 赞：6  ·  来源：huggingface
- 兴趣命中：reasoning, reinforcement learning, benchmark
- 作者：Junwei Wen, Deshui Miao, Guangming Lu, Ming-Hsuan Yang, Xin Li, Wenjie Pei
- 链接：[arXiv](https://arxiv.org/abs/2610.25090) · [PDF](https://arxiv.org/pdf/2610.25090) · [HF](https://huggingface.co/papers/2610.25090)

Video Reasoning Segmentation (VRS) requires a model to identify an implicitly described target and predict its pixel-level mask trajectory, while resolving the spatial relations and temporal events that determine the answer. Text-only Chain-of-Thought (CoT) can explain a target choice without making the underlying visual references explicit, leaving a video reference gap between linguistic inference and the evidence…

## 64. DeOverlay: A Benchmark and Source-Anchored Flow for Video Overlay Removal

- 分数：17.0  ·  HF 赞：6  ·  来源：huggingface
- 兴趣命中：evaluation, benchmark, spec
- 作者：Deshui Miao, Yuhang Ma, Shaoyong Jia, Wenzhao Gao, Yue Zhang, Shaohui Jiao, Xin Li
- 链接：[arXiv](https://arxiv.org/abs/2610.26081) · [PDF](https://arxiv.org/pdf/2610.26081) · [HF](https://huggingface.co/papers/2610.26081)

Video overlay removal aims to recover scenes obscured by subtitles, titles, and logos while preserving surrounding content. Existing methods use temporal propagation or source-conditioned generation, but can leave residual overlays and distort scene structure when useful source information is obscured. We propose DeOverlay, a source-anchored flow model that reconstructs the clean video from the source latent with…

## 65. Co-Evolving Acting and Forecasting for Language Agents

- 分数：17.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：agent, reinforcement learning, benchmark, spec
- 作者：Haofei Yu, Yixing Chen, Yining Zhao, Xuyan Ye, Yuxiang Liu, Zhigang Hua, Yan Xie, Shuang Yang, Jiaxuan You
- 链接：[arXiv](https://arxiv.org/abs/2610.20597) · [PDF](https://arxiv.org/pdf/2610.20597) · [HF](https://huggingface.co/papers/2610.20597)

Training language agents is bottlenecked by the high cost of long-horizon rollouts, yet standard agentic reinforcement learning (RL) learns only from a terminal scalar reward, leaving the supervision in intermediate steps largely unused. Prior work exploits this supervision through value targets that estimate per-step success probabilities or observation targets that fit environment response. Both are hard to…

## 66. RSIFlow: Adaptive Self-Improvement Workflows with an Evolving Meta-Agent

- 分数：17.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：agent, tool use, benchmark, language model, large language, spec
- 作者：Huan Zhang, Mingju Chen, Dongxu Zhou, Can Lv, Sen Cui, Faguo Wu, Shiji Zhou
- 链接：[arXiv](https://arxiv.org/abs/2610.21791) · [PDF](https://arxiv.org/pdf/2610.21791) · [HF](https://huggingface.co/papers/2610.21791)

Large language model (LLM) agents have demonstrated strong capabilities in complex tasks, including code generation, tool use, and multi-hop question answering. Existing self-improvement methods enhance agent performance through model optimization, harness evolution, and executable artifact refinement, while recursive self-improvement (RSI) further extends optimization to the improvement mechanisms themselves.…

## 67. AdaExploreBench: Benchmarking LLM Agents for Proactive Exploration and Test-time Adaptation in Evolving Environments

- 分数：17.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：agent, benchmark, language model, large language
- 作者：Rui Wang, Zishen Lai, Jiayu Liu, Cheng Qian, Jeonghwan Kim, Heng Wang, Xuejun Zhang, Jiateng Liu, Bingxuan Li, Shujin Wu, Qing Zong, Tianshi Zheng, Chunyang Li, Qihan Lin, Chen Li, Dadi Guo, Xiusi Chen, Yangqiu Song
- 链接：[arXiv](https://arxiv.org/abs/2610.25950) · [PDF](https://arxiv.org/pdf/2610.25950) · [HF](https://huggingface.co/papers/2610.25950)

Large Language Model (LLM) agents are increasingly deployed in unfamiliar and evolving environments, requiring them to proactively explore, understand, and adapt to environmental dynamics. However, existing benchmarks rarely test whether agents can proactively discover how an environment works and adapt as it evolves. To address this gap, we introduce AdaExploreBench, a benchmark for proactive exploration and…

## 68. FC-SWE: Failure-Conditioned RL for Long-Horizon Software Engineering Agents

- 分数：16.5  ·  HF 赞：5  ·  来源：huggingface
- 兴趣命中：agent, tool-use, reinforcement learning
- 作者：Jia Liufu, Bin Hu, Linglin Jing, Terry Kong, Yuki Huang, Ashwath Aithal, Wenming Yang, Jun Yang
- 链接：[arXiv](https://arxiv.org/abs/2610.07898) · [PDF](https://arxiv.org/pdf/2610.07898) · [HF](https://huggingface.co/papers/2610.07898)

Repository-level software engineering (SWE) is a challenging long-horizon setting: agents must reason over extended interactions, use tools, and adapt to stateful environments. Recent work trains SWE agents with reinforcement learning methods such as Group Relative Policy Optimization (GRPO), which independently sample multiple trajectories per issue, test the resulting patches, and compare terminal rewards within a…

## 69. Factorization-Guided Training and Inference for Diffusion-Drafted Speculative Decoding

- 分数：16.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：benchmark, language model, large language, coding, spec
- 作者：Jiakun Fan, Min Xiao, Qiang Wang, Neiwen Ling, Zhichao Liu, Zhihao Jia, Dimitrios S. Nikolopoulos, Zijun Wei
- 链接：[arXiv](https://arxiv.org/abs/2610.23935) · [PDF](https://arxiv.org/pdf/2610.23935) · [HF](https://huggingface.co/papers/2610.23935)

Speculative decoding accelerates large language model inference through parallel verification of tokens proposed by a drafter. Diffusion drafters further parallelize proposal generation, but greater proposal capacity or higher mean accepted tokens (MAT) need not yield higher throughput. Because verification accepts only a consecutive prefix, early rejections can render later correct predictions ineffective, limiting…

## 70. Recognition Is Not Grounding: Benchmarking Multilingual Financial Evidence Extraction

- 分数：16.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：benchmark, language model, spec
- 作者：Lingfei Qian, Yan Wang, Xueqing Peng, Polydoros Giannouris, Nadhem Zmandar, Yi Han, Yanguang Liu, Víctor Gutiérrez-Basulto
- 链接：[arXiv](https://arxiv.org/abs/2610.19432) · [PDF](https://arxiv.org/pdf/2610.19432) · [HF](https://huggingface.co/papers/2610.19432)

Comparing financial disclosures across languages requires identifying shared accounting concepts and recovering all numerical facts that express them. Existing benchmarks evaluate aspects of these capabilities, but provide limited insight into whether both succeed on the same multilingual evidence. In particular, it remains unclear whether language models can recognize these concepts across languages and…

## 71. GlobeBench: Evaluating Text-Based World Model Capabilities for Scalable Environment Simulations

- 分数：16.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：agent, benchmark, spec
- 作者：Nicholas Saban, Charvi Bannur, Mariya Vasileva, Darshan Deshpande
- 链接：[arXiv](https://arxiv.org/abs/2610.22708) · [PDF](https://arxiv.org/pdf/2610.22708) · [HF](https://huggingface.co/papers/2610.22708)

Text-based world models have recently shown potential to simulate complex RL environment state transitions for a diverse set of use cases. However, no standardized benchmark exists to compare, study and improve these models. Through this paper, we attempt to solve this problem by building GlobeBench, a novel benchmark with 1,632 tasks across five separate domains and nineteen simulation skills. The tasks check…

## 72. Learning to Discriminate Scene Structures Makes Self-Supervised Depth Learning Scalable

- 分数：16.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：evaluation, coding, spec
- 作者：Mengtan Zhang, Yuchuan Cui, Yu Ma, Zizhan Guo, Wei Ye, Rui Fan
- 链接：[arXiv](https://arxiv.org/abs/2610.23600) · [PDF](https://arxiv.org/pdf/2610.23600) · [HF](https://huggingface.co/papers/2610.23600)

Self-supervised monocular depth estimation is appealing for its potential to scale with unlabeled data, yet existing methods often degrade when trained on diverse scenes. This study finds that, under self-supervision, models tend to encode dataset-specific structural biases rather than transferable scene geometry, leading to cross-domain optimization conflicts. To address this issue, this study proposes the MaSS…

## 73. AVC-Reward: Event-Centric Audio-Video Consistency Evaluation

- 分数：15.5  ·  HF 赞：7  ·  来源：huggingface
- 兴趣命中：evaluation, benchmark
- 作者：Yuruo Wu, Kaihang Pan, Kai Shen, Jiacheng Li, Shuyuan Tu, Jisheng Dang, Li Tuoyu, Juncheng Li, Siliang Tang
- 链接：[arXiv](https://arxiv.org/abs/2610.22321) · [PDF](https://arxiv.org/pdf/2610.22321) · [HF](https://huggingface.co/papers/2610.22321)

As joint audio-video generation models become more capable, they can generate audio-visual scenes exhibiting three forms of complexity: multi-event composition, multi-layer audio mixture, and asymmetric cross-modal relations. However, current evaluations largely reuse metrics from earlier simple and unidirectional tasks. They typically evaluate an audio-video clip as a whole and rely on simple predefined relations,…

## 74. World Model Interpretability: From Decoding Representations to Understanding Latent Worlds

- 分数：15.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：coding, spec, planning
- 作者：Jize Wang, Yongcheng Jing, Xinyi Le, Cailian Chen, Xinping Guan, Dacheng Tao
- 链接：[arXiv](https://arxiv.org/abs/2610.25296) · [PDF](https://arxiv.org/pdf/2610.25296) · [HF](https://huggingface.co/papers/2610.25296)

Emerging Joint-Embedding Predictive Architectures (JEPAs) are moving beyond representation learning towards latent world models that support prediction, planning, and control. Yet their latent worlds naturally lack a human-interpretable interface. In this Perspective, we argue that as JEPA latents become internal states for prediction and action, interpretability must move beyond what they encode to how latent…

## 75. OPMD: On-Policy Mechanism Distillation Beyond Output Supervision

- 分数：15.0  ·  HF 赞：10  ·  来源：huggingface
- 兴趣命中：reasoning
- 作者：Yingdong Shi, Zhihong Li, Changming Li, Jingyi Yu, Quan Li, Kan Ren
- 链接：[arXiv](https://arxiv.org/abs/2610.14022) · [PDF](https://arxiv.org/pdf/2610.14022) · [HF](https://huggingface.co/papers/2610.14022)

On-policy distillation (OPD) improves language-model by supervising a student on prefixes sampled from its own policy, but its supervision remains confined to the output space. Consequently, OPD transfers what a teacher predicts without supervising the intermediate computation that produces those predictions. Simply distilling intermediate representations like representation matching is insufficient since teacher…

## 76. Self-Evaluating Recursive Agents

- 分数：15.0  ·  HF 赞：6  ·  来源：huggingface
- 兴趣命中：agent, evaluation
- 作者：TianYi Lyu, Xiaozhe Li, Yang Li, Yongkang Chen, Kefei Tian, Junbo Niu, Zican Hu, Hongbo Liu, Mingliang Xiong, Qingwen Liu
- 链接：[arXiv](https://arxiv.org/abs/2610.04902) · [PDF](https://arxiv.org/pdf/2610.04902) · [HF](https://huggingface.co/papers/2610.04902)

Recursive language-model agents decompose tasks and delegate subtasks to child instances of the same policy, forming a tree of work. Training them, however, is hard: the final outcome is verifiable, but the self-invented intermediate subtasks are numerous and carry no ground truth. Existing methods score each node with a verifier or judge, which is costly at scale and blind to decomposition quality. We argue that a…

## 77. OS-Helix: Unifying GUI Interaction and Code Execution in Native Computer-Using Agents

- 分数：14.5  ·  HF 赞：9  ·  来源：huggingface
- 兴趣命中：agent
- 作者：Bowen Yang, Kaiming Jin, Zichen Ding, Zhenyu Wu, Zehao Li, Zhoumianze Liu, Kanzhi Cheng, Fangzhi Xu, Yanan Sun, Qiushi Sun, Yu Qiao
- 链接：[arXiv](https://arxiv.org/abs/2610.22234) · [PDF](https://arxiv.org/pdf/2610.22234) · [HF](https://huggingface.co/papers/2610.22234)

Real desktop automation is neither purely visual nor purely programmatic. Agents must understand user-facing interfaces while efficiently manipulating files, scripts, and system state. However, native GUI/code coordination cannot be obtained by prompt-level tool composition. In our preliminary experiments, naively adding a code tool degrades a GUI agent, revealing that GUI/code routing must be internalized through…

## 78. DAGFormer: Global Topology Prediction for Transformer Cross-Layer Connections

- 分数：14.5  ·  HF 赞：5  ·  来源：huggingface
- 兴趣命中：evaluation, language model
- 作者：Xiaocong Yang, Yuren Hao, ChengXiang Zhai
- 链接：[arXiv](https://arxiv.org/abs/2610.19625) · [PDF](https://arxiv.org/pdf/2610.19625) · [HF](https://huggingface.co/papers/2610.19625)

We propose DAGFormer, a Transformer language model whose cross-layer connections are planned by a jointly trained topology predictor. Beyond the residual connections in a standard Transformer, DAGFormer adds direct connections from earlier layers to later ones, and the predictor controls the strength of every connection based on input tokens. Unlike existing cross-layer routing architectures, which set each layer's…

## 79. Empowering Edge Agents: A Systematic Analysis of Edge-Cloud Collaboration in LLM Agent Execution

- 分数：14.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark
- 作者：Pengcheng Huang, Zhenghao Liu, Shixin Ren, Shi Yu, Sijia Yao, Yukun Yan, Chaojun Xiao, Maosong Sun
- 链接：[arXiv](https://arxiv.org/abs/2610.17816) · [PDF](https://arxiv.org/pdf/2610.17816) · [HF](https://huggingface.co/papers/2610.17816)

Edge-cloud collaboration combines the lower inference overhead and greater data locality of edge-side execution with the stronger capabilities of cloud-hosted models. However, as LLM agents increasingly operate in long-horizon scenarios, cloud participation becomes interleaved throughout execution rather than a one-shot decision for each query. Such interleaved participation introduces trajectory-level effects that…

## 80. TokenEconomizer: Experience-Driven Black-Box Cost Control for Coding Agents

- 分数：14.0  ·  HF 赞：0  ·  来源：huggingface
- 兴趣命中：agent, coding, spec
- 作者：Aaron J. Li, Weijia Xu, Chandan Singh, Zixiao Chen, Jeevana Priya Inala, Charlotte Siska, Acar Tamersoy, Bin Yu, Ion Stoica, Michel Galley, Jianfeng Gao
- 链接：[arXiv](https://arxiv.org/abs/2610.22732) · [PDF](https://arxiv.org/pdf/2610.22732) · [HF](https://huggingface.co/papers/2610.22732)

Advances in frontier coding agents have sharply increased the token costs of AI-assisted software engineering. Their token efficiency is typically evaluated on isolated tasks, whereas real-world developers use them to continuously build, update, and maintain large-scale projects. This mismatch motivates us to evaluate agents over sequences of realistic coding tasks, where we find that agents exhibit recurring…

## 81. Resisting Harmful Instructions through Training-Free Weight Editing

- 分数：13.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：benchmark, language model
- 作者：Ali Ebrahimpour-Boroojeny, Xiaocong Yang, Samuel Schapiro, Zahra Borhani, Francisco R. Ortega, Yujia Zheng, ChengXiang Zhai
- 链接：[arXiv](https://arxiv.org/abs/2610.21189) · [PDF](https://arxiv.org/pdf/2610.21189) · [HF](https://huggingface.co/papers/2610.21189)

Instruction-following language models can comply with requests that conflict with intended behaviors and safety alignment. We introduce a training-free weight-editing approach for reducing compliance with targeted undesirable instructions. Our method needs only forward passes on a small set of prompt pairs per target behavior, and because the edit is stored in the model's weights, changing or deleting instructions…

## 82. MorphAct: Robot Policies Morphing with the Worlds They Act In

- 分数：13.0  ·  HF 赞：6  ·  来源：huggingface
- 兴趣命中：evaluation
- 作者：Ziyan Liu, Jiting Liu, Weihong Zhong, Wenda Yu, Yeqiu Chen, Jason Li, Xiaojiang Peng, Shuyuan Hu, Kai Wang, Bo Zhao
- 链接：[arXiv](https://arxiv.org/abs/2610.20019) · [PDF](https://arxiv.org/pdf/2610.20019) · [HF](https://huggingface.co/papers/2610.20019)

Progress toward general intelligence in the physical world requires scaling robot learning across diverse environments and interactions. However, existing robot policies use shared parameters that remain fixed across interaction contexts. When different operations favor competing parameter adjustments, fitting their mixture can leave individual operations insufficiently adapted. Our atomic-task diagnostics reveal…

## 83. DuET: Note-Frame Dual Encoding for Piano Performance-to-Score Transcription

- 分数：13.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：evaluation, coding
- 作者：Wei Zeng, Ye Wang
- 链接：[arXiv](https://arxiv.org/abs/2610.21467) · [PDF](https://arxiv.org/pdf/2610.21467) · [HF](https://huggingface.co/papers/2610.21467)

Transcribing expressive piano performances into scores requires interpreting individual note timings within an underlying metrical structure. However, score attributes are associated with notes, whereas beats may occur without coincident note onsets. We introduce DuET, a Dual-Encoder Transformer that jointly learns note-level performance MIDI-to-score (PM2S) transcription and frame-level beat and downbeat tracking.…

## 84. Frechet Forcing: Training Long-Horizon Streaming World Models from Short Clips

- 分数：12.0  ·  HF 赞：8  ·  来源：huggingface
- 兴趣命中：-
- 作者：Yian Zhao, Yu Yan, Hongcan Guo, Ruochong Zheng, Jian Zhang, Jie Chen
- 链接：[arXiv](https://arxiv.org/abs/2610.25666) · [PDF](https://arxiv.org/pdf/2610.25666) · [HF](https://huggingface.co/papers/2610.25666)

Streaming video world models generate the future chunk by chunk, conditioned on their own past and a stream of actions. Trained on short clips, they drift once a rollout exceeds the training horizon, as prediction errors re-enter the context and compound. A common remedy is to train the model on its own rollouts via distribution matching distillation (DMD). For action-conditioned world models, the teacher becomes a…

## 85. BRACE: Adapting Whole-Body References for Force and Terrain Aware Humanoid Motion Tracking

- 分数：12.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：spec
- 作者：Sudarshan Harithas, Chen Yu, Juan Borbon, Shubhankar Mondal, Winston Zha, Srinath Sridhar, Dingqi Zhang, Jiuguang Wang
- 链接：[arXiv](https://arxiv.org/abs/2610.07052) · [PDF](https://arxiv.org/pdf/2610.07052) · [HF](https://huggingface.co/papers/2610.07052)

Whole-body tracking has become the interface through which operators drive humanoid robots, yet the references it consumes are recorded on level ground and carrying nothing, so the tracker is aware of neither the forces the robot must exchange with objects nor the terrain it must stand on. Existing controllers address one side of this gap: force-capable policies command an end-effector force but prescribe no…

## 86. What It Is, Not What It Says: Securing Agentic Browsing Interactions with Web Semantics

- 分数：11.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：agent
- 作者：Umar Iqbal
- 链接：[arXiv](https://arxiv.org/abs/2610.22697) · [PDF](https://arxiv.org/pdf/2610.22697) · [HF](https://huggingface.co/papers/2610.22697)

AI agents increasingly browse the web on users' behalf, yet they consume webpages as screenshots or text, exposing their LLMs to unvetted third-party content. Browsers enforce semantics under which what an element can do depends on what it is and where it comes from, not on what it says. Agents flatten these semantics, so injected text can persuade the LLM to exercise the user's authority for content that has none.…

## 87. StopWatch: Goal Grounding for Object-goal Navigation

- 分数：11.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：benchmark
- 作者：Xinhao Liu, Yunsheng Tian, Yuheng Qiu, Pieter Abbeel, Xi Chen, Guanya Shi, Chen Feng
- 链接：[arXiv](https://arxiv.org/abs/2610.23841) · [PDF](https://arxiv.org/pdf/2610.23841) · [HF](https://huggingface.co/papers/2610.23841)

Pretrained VLMs bring rich world knowledge and semantic priors to object-goal navigation, and fine-tuning a VLM into a navigation policy has become a common recipe. Despite this progress, success rates remain low, and it is unclear which capability these fine-tuned policies lack. Our diagnosis identifies goal grounding as the dominant failure. These policies explore well, yet often fail to notice that the goal is…

## 88. Persistent Planar Memory for Video World Models

- 分数：11.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：memory
- 作者：Yuze He, Bin Tan, Zelin Gao, Yujun Shen, Yong-Jin Liu, Nan Xue, Yinghao Xu
- 链接：[arXiv](https://arxiv.org/abs/2610.23795) · [PDF](https://arxiv.org/pdf/2610.23795) · [HF](https://huggingface.co/papers/2610.23795)

Video world models that generate and explore environments at scale need a persistent 3D memory of what they have produced. Plane primitives offer a natural candidate: a compact set of oriented planes captures the dominant structural elements (e.g., walls, floors, facades) of indoor and outdoor scenes, while requiring only 7 parameters per primitive. We present PPMem, a video world model that adopts plane primitives…

## 89. DisaggKD: Efficient Knowledge Distillation through Teacher-Student Disaggregation and a Fused Loss

- 分数：11.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：memory
- 作者：Ruixuan Tu, Yuyang Dong
- 链接：[arXiv](https://arxiv.org/abs/2610.17644) · [PDF](https://arxiv.org/pdf/2610.17644) · [HF](https://huggingface.co/papers/2610.17644)

Knowledge distillation (KD) frameworks place teacher and student on the same GPUs, so per-GPU memory limits the teachers that fit. DisaggKD separates them across nodes: teacher replicas stream hidden states to the student, a KD loss over row windows and vocabulary shards equals the full-vocabulary loss in exact arithmetic without forming the full-vocabulary logits, and a prefetch ring paces producer and trainer.…

## 90. GeoState: Learning View-Decoupled Geometry States for 3D World Modeling

- 分数：11.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：spec
- 作者：Hongchang Liu, Jian Liu, Yujuan Ding, Liang Peng, Xun Jiang, Fei Ma, Xing Xu, Yi Bin
- 链接：[arXiv](https://arxiv.org/abs/2610.22343) · [PDF](https://arxiv.org/pdf/2610.22343) · [HF](https://huggingface.co/papers/2610.22343)

Recent 3D world models increasingly use features from geometry foundation models (GFMs) as predictive world states, benefiting from their rich geometric priors. However, the view dependence of these features entangles scene dynamics with camera-induced variation, making the resulting state evolution harder to predict. We propose GeoState, a view-decoupled geometry representation for predictive 3D world modeling that…

## 91. Relational Learning as World Modeling

- 分数：10.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：spec
- 作者：Zheyu Zhang, Gjergji Kasneci
- 链接：[arXiv](https://arxiv.org/abs/2610.16763) · [PDF](https://arxiv.org/pdf/2610.16763) · [HF](https://huggingface.co/papers/2610.16763)

Relational learning typically predicts from a database state, but decision making asks a different question: how will that state change under an action? In operational systems, the answer depends on system-specific dynamics that may not be visible in the database itself. We view each such system as a relational "world" and ask whether a model can infer how it behaves from observed executions. We introduce TabWM…

## 92. QD-Rec: Open-Ended Evolution of Recommendations via Quality-Diversity

- 分数：10.0  ·  HF 赞：0  ·  来源：huggingface
- 兴趣命中：agent
- 作者：Takashi Ishida, Taro Makino, Issa Sugiura
- 链接：[arXiv](https://arxiv.org/abs/2610.23470) · [PDF](https://arxiv.org/pdf/2610.23470) · [HF](https://huggingface.co/papers/2610.23470)

Open-ended search combined with foundation models has produced advances such as faster algorithms, new results on open mathematical problems, and self-improving agents. We extend this paradigm to recommendation for decision-making, focusing on decisions where the set of possible choices is fixed but the reasons for choosing them are not. In high-stakes decisions, e.g., which company to acquire or which customer to…

## 93. SPARC: Spoken Profile Authorship Recognition Corpus

- 分数：10.0  ·  HF 赞：0  ·  来源：huggingface
- 兴趣命中：benchmark
- 作者：Efthymios Tsaprazlis, Bowen Yi, Tiantian Feng, Junghwan Kim, David Jurgens, Shrikanth Narayanan
- 链接：[arXiv](https://arxiv.org/abs/2610.25265) · [PDF](https://arxiv.org/pdf/2610.25265) · [HF](https://huggingface.co/papers/2610.25265)

Speech anonymization has focused on the acoustic signal, leaving open how much speaker information the transcribed words themselves retain. In this work, we study pairwise speaker and demographic-attribute verification from transcribed speech. We introduce SPARC (Spoken Profile Authorship Recognition Corpus), a benchmark built from two podcast corpora comprising over 12,500 speakers, 1.5M quality-filtered…

## 94. Learning from Fleet Experience: A Collective Learning Paradigm for Robots

- 分数：10.0  ·  HF 赞：0  ·  来源：huggingface
- 兴趣命中：retrieval
- 作者：Chao Yu, Shu&#39;ang Yu, Hao Lin, Hongzhi Zang, Yuxiang Yan, Chenxi Jiang, Zhen Guo, Chuankang Li, Yihao Chen, Xin Xu, Xu Fu, Jiakai Zhou, Liangzhi Shi, Hongyi Ren, Yiwei Liu, Jing Wu, Yuanqing Wang, Chen Wu, Bo Dai, Chunyu Yang, Hongliang Huang, Shuoyu Yue, Weiqi Yin, Yinuo Chen, Ruihua Chen, Chunyang Zhu, Han Xiao, Yanghao Li, Ruipu Wu, Zhikai Cai, Xiu Chen, Xu Tan, Yuchen Yan, Jialin Zhang, Wen Zeng, Yiming Zhou, Zixiao Huang, Guanghui Ren, Quanlu Zhang, Boxun Li, Maoqing Yao, Yu Wang
- 链接：[arXiv](https://arxiv.org/abs/2610.25736) · [PDF](https://arxiv.org/pdf/2610.25736) · [HF](https://huggingface.co/papers/2610.25736)

Experience generated during deployment offers an opportunity for robots to improve policy reliability through learning from their own executions. However, learning through human corrections requires teleoperators to monitor execution and intervene when policies fail, a demand that is difficult to meet as robot fleets grow. We introduce collective experience learning (CEL), a learning paradigm in which deployed…

## 95. AffordanceWAM: Affordance-Aware Joint World-Action Modeling for Robot Manipulation

- 分数：9.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：-
- 作者：Jiadi You, Qize Yu, Yue Chen, Minghong Cai, Zhide Zhong, Yuran Wang, Bowen Ping, Jiaqi Liang, Zhenhao Shen, Haodong Yan, Yinchuan Li, Ruihai Wu, Xiaojuan Qi, Yingcong Chen
- 链接：[arXiv](https://arxiv.org/abs/2609.22332) · [PDF](https://arxiv.org/pdf/2609.22332) · [HF](https://huggingface.co/papers/2609.22332)

Generalizable robot manipulation requires predicting how a scene will evolve, identifying where interactions are feasible, and determining how to act. Action-labeled robot videos directly supervise control but are costly and limited in diversity, whereas egocentric human videos capture diverse interactions but lack robot actions and differ in embodiment and appearance. We introduce AffordanceWAM, an affordance-aware…

## 96. ARC-SORT: Adaptive, Robust, Compensated Multi-Object Tracking with Interacting Multiple Models

- 分数：9.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：-
- 作者：Girish Kumar Adari
- 链接：[arXiv](https://arxiv.org/abs/2610.22306) · [PDF](https://arxiv.org/pdf/2610.22306) · [HF](https://huggingface.co/papers/2610.22306)

Multi-object tracking in sports broadcasts is hard for two reasons: athletes move fast and change direction abruptly, and the camera pans and zooms at the same time. We present ARC-SORT (Adaptive, Robust, Compensated SORT), a tracking-by-detection tracker that trains nothing and runs in real time. Its design rule: the tracker measures its own uncertainty, and that measurement decides how it acts. An Interacting…

## 97. AI-Driven Disaster Response and Displacement Monitoring

- 分数：9.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：-
- 作者：Noora Al-Emadi, Muhammad Imran, Yin Yang, Ingmar Weber, Fabjan Lashi, Gaia Rigodanza, Ivana Hajzmanova, Ferda Ofli
- 链接：[arXiv](https://arxiv.org/abs/2610.21482) · [PDF](https://arxiv.org/pdf/2610.21482) · [HF](https://huggingface.co/papers/2610.21482)

ARTIFICIAL INTELLIGENCE (AI) has demonstrated its potential across a wide range of humanitarian tasks, offering scalable and data-driven solutions to some of the world's most pressing challenges. For instance, in addressing climate change, AI-powered models are being used for faster and more accurate global weather forecasting, control and design of renewable energy, and monitoring deforestation. Machine learning…

## 98. Dusting the Phantom: Gaussian Allocation for Fading Dynamic Content

- 分数：9.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：-
- 作者：Minhyeok Roh, Minseo Lee, Jun Young Jeong, Byeonghyeon Lee, Lucas Yunkyu Lee, Jaesik Park, Eunbyung Park
- 链接：[arXiv](https://arxiv.org/abs/2610.21302) · [PDF](https://arxiv.org/pdf/2610.21302) · [HF](https://huggingface.co/papers/2610.21302)

Dynamic Gaussian representations have made high-quality, real-time volumetric video increasingly practical, yet challenging motion can still break their reconstruction: small fast-moving objects may disappear, and fine textures in highly dynamic regions are often lost. In particular, simply training longer or using more Gaussians may still fail to recover small, fast-moving objects. We argue that the key bottleneck…

## 99. DeepSEA: A Multilingual Evaluation Benchmark for Southeast Asia

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, evaluation, benchmark, language model, spec
- 作者：Jiuzhou Han, Abhishek Bijay Mishra, Trevor Cohn, Shubham Mittal
- 链接：[arXiv](https://arxiv.org/abs/2610.26155) · [PDF](https://arxiv.org/pdf/2610.26155) · [HF](https://huggingface.co/papers/2610.26155)

While language models have demonstrated remarkable capabilities, their performance remains disproportionately skewed towards high-resource languages. This disparity is particularly acute for the 700 million inhabitants of Southeast Asia, where vast linguistic diversity remains under-represented in existing benchmarks, often suffering from limited language coverage or narrow task scopes. To address this, we introduce…

## 100. MoveBench: A Rubric-Based Benchmark for Evaluating Large Language Models in Sports and Health Coaching

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, evaluation, benchmark, language model, large language, spec
- 作者：Yitong Li, Jiang Bian, Jingling Wang, Pan Ding, Chengying Gu
- 链接：[arXiv](https://arxiv.org/abs/2610.26185) · [PDF](https://arxiv.org/pdf/2610.26185) · [HF](https://huggingface.co/papers/2610.26185)

Despite rapid advances in large language models (LLMs), their deployment in the sports and health domain remains high-risk due to the absence of domain-specific evaluation benchmarks. Existing general-purpose benchmarks (e.g., MMLU and HELM) primarily assess broad knowledge and reasoning capabilities, but fail to capture critical domain requirements such as exercise safety, physiological appropriateness,…

## 101. Rethinking BPE: Merge Selection as Model Selection

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, language model, coding, spec
- 作者：Vijini Liyanage, François Yvon
- 链接：[arXiv](https://arxiv.org/abs/2610.26225) · [PDF](https://arxiv.org/pdf/2610.26225) · [HF](https://huggingface.co/papers/2610.26225)

Subword tokenization methods such as Byte-Pair Encoding (BPE) are a core component of modern language models; yet, tokenizer capacity remains typically determined by a fixed merge budget, chosen heuristically. Since larger vocabularies increase memory usage and computational cost, selecting compact and effective token inventories is essential for efficient language modeling. We study the optimization of a BPE merge…

## 102. Towards More Granular Reasoning: Mapping the DSA Transparency Database Taxonomy to Platform Terms and Conditions Using Large Language Models

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, language model, large language, spec
- 作者：Alyson Ranucci, Eline Leijten, David Graus
- 链接：[arXiv](https://arxiv.org/abs/2610.26226) · [PDF](https://arxiv.org/pdf/2610.26226) · [HF](https://huggingface.co/papers/2610.26226)

Article 24(5) of the Digital Services Act (DSA) requires providers of online platforms to submit every content moderation decision they make, with a corresponding Statement of Reasons (SoR), to the DSA Transparency Database (DSA-TDB). Such decisions are classified against seventeen high-level attribute categories that categorize the primary reason for the moderation decision. Because over 99.8% of statements cite a…

## 103. Heartbeat Thinking: Speculative Reasoning and Tool Execution While Listening in Realtime Voice Agents

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reasoning, benchmark, spec, retrieval
- 作者：Zhenyu Zhang, Kewei Fu, Yongqi Tong, Chenzhi Zheng, Wei Wu, Jiang-Ming Yang, Jianshe Li
- 链接：[arXiv](https://arxiv.org/abs/2610.26233) · [PDF](https://arxiv.org/pdf/2610.26233) · [HF](https://huggingface.co/papers/2610.26233)

Tool-using voice agents often leave users waiting after speech ends, even when actionable information arrives earlier in the request. Speculative approaches begin work during speech, but chunk-bounded or interrupt-on-update generation can truncate a tool call before its arguments are complete. This couples computation time to speech updates, limiting useful work completed in advance. We introduce Heartbeat Thinking,…

## 104. XGLASS: X-Ray, Gaze and Language Assisted Slice Sequencing for CT Volumes

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, language model, spec, retrieval
- 作者：Michael Glöckler, Timo Ropinski
- 链接：[arXiv](https://arxiv.org/abs/2610.26255) · [PDF](https://arxiv.org/pdf/2610.26255) · [HF](https://huggingface.co/papers/2610.26255)

Vision-language models (VLMs) achieve remarkable performance on 2D medical images, such as X-rays or pathology images, while 3D VLMs that directly process CT/MRI volumes lag behind due to limited 3D training data and the predominance of 2D foundation architectures. To leverage powerful 2D VLMs for analyzing medical volumes, which contain hundreds of slices, it is therefore necessary to focus only on those few…

## 105. From Cause to Effect: Generating Intermediate Event Chains in Videos

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, evaluation, benchmark, language model, spec
- 作者：Ridouane Ghermi, Vicky Kalogeiton, Ivan Laptev
- 链接：[arXiv](https://arxiv.org/abs/2610.26275) · [PDF](https://arxiv.org/pdf/2610.26275) · [HF](https://huggingface.co/papers/2610.26275)

Video-Language Models (VLMs) excel at visual recognition but struggle with causal reasoning. Current evaluations are flawed: multiple-choice QA allows shortcuts, and open-ended QA lacks robust automatic evaluation. We introduce Causal Chain Generation (CCG), a novel task where models have to generate the sequence of intermediate events connecting a cause and an effect. This structured setup demands genuine reasoning…

## 106. VibeTraining-Bench: Data-Trainer-Harness Co-Design for Iterative System Improvement

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, tool use, reasoning, evaluation, benchmark
- 作者：Ruotian Peng, Yuanyi Ren, Shuaiqi Liu, Xin Guo, Fang Zhu, Yangyi Huang, Yue Wu, Zheng Wang, Yandong Wen, Zhihang Fu
- 链接：[arXiv](https://arxiv.org/abs/2610.26342) · [PDF](https://arxiv.org/pdf/2610.26342) · [HF](https://huggingface.co/papers/2610.26342)

Recursive self-improvement (RSI) requires agents to diagnose system bottlenecks and coordinate improvements across training and inference. We refer to the agents' capability to jointly optimize training data, the trainer, and the inference harness as cross-component co-design. We introduce VibeTraining-Bench, a benchmark for evaluating this capability across tasks spanning terminal operation, software engineering,…

## 107. GAIDA: Generative AI for Human-in-the-Loop Document Annotation

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, language model, large language, spec
- 作者：Islam Mesabah, Ali Elhosary, Priyabanta Sandulu, Darko Obradovic, Sebastian J. Vollmer
- 链接：[arXiv](https://arxiv.org/abs/2610.26362) · [PDF](https://arxiv.org/pdf/2610.26362) · [HF](https://huggingface.co/papers/2610.26362)

Document annotation is a fundamental yet labor-intensive step in building document information extraction systems. While Optical Character Recognition (OCR) and Large Language Models (LLMs) can automate parts of this process, we argue that annotation systems should be judged not by how completely they remove human effort, but by how effectively they redirect it toward review and correction. We propose a modular…

## 108. Autonomous intelligence for mining productivity: a multi-agent AI approach to operational value creation

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, evaluation, benchmark, language model, large language, spec
- 作者：N Guerin, A Dehoux, M Nakhla
- 链接：[arXiv](https://arxiv.org/abs/2610.26369) · [PDF](https://arxiv.org/pdf/2610.26369) · [HF](https://huggingface.co/papers/2610.26369)

Integrated Remote Operation Centres (IROCs) are emerging as the architectural frontier of Industry 4.0 for capital-intensive sectors such as mining, oil and gas, and energy. Yet two intertwined gaps constrain their evolution towards full autonomy. First, no integrated agentic architecture has been proposed for mining IROCs that orchestrates Supervisory Control and Data Acquisition systems, digital twins, predictive…

## 109. When Coding Agents Outpace Review: Evaluating PRD-Driven Development in Mature Enterprise Repositories

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, evaluation, benchmark, coding
- 作者：Tianqi Liu, Yandong Guan, Songze Li, Wenkai Wang, Gang Yu, Chengfei Lv
- 链接：[arXiv](https://arxiv.org/abs/2610.26394) · [PDF](https://arxiv.org/pdf/2610.26394) · [HF](https://huggingface.co/papers/2610.26394)

Coding agents increasingly undertake development tasks in mature enterprise repositories, yet existing benchmarks offer limited insight into whether they fulfill complete Product Requirement Documents (PRDs) and where delivery breaks down. Issue resolution and development from scratch leave incremental PRD fulfillment underexplored, while isolated tests provide incomplete evidence of business and integration…

## 110. How Benchmark Graph Construction Shapes Multi-Hop KG Navigation: A Controlled Audit of PathQuestion and PathQuestion-Large

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, evaluation, benchmark, spec
- 作者：Eduin E. Hernandez, Sergio A. Diaz, Luis F. Garcia, Nurassyl Askar, Stefano Rini
- 链接：[arXiv](https://arxiv.org/abs/2610.26399) · [PDF](https://arxiv.org/pdf/2610.26399) · [HF](https://huggingface.co/papers/2610.26399)

Multi-hop knowledge-graph question answering (KGQA) benchmarks are often treated as fixed language-and-reasoning tasks, but for navigation-based methods, difficulty also depends on the graph in which those tasks are instantiated. This makes graph construction a consequential but often entangled part of the navigation task. To isolate this effect, we audit PathQuestion (PQ) and PathQuestion-Large (PQL) as…

## 111. Fake News, Real Crashes: Information Injection Attacks on LLM Financial Trading Agents

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, benchmark, language model, large language
- 作者：Mengxiao Wang, Nitesh Saxena
- 链接：[arXiv](https://arxiv.org/abs/2610.26438) · [PDF](https://arxiv.org/pdf/2610.26438) · [HF](https://huggingface.co/papers/2610.26438)

Large language model (LLM) agents now trade real capital using news as evidence, yet they cannot reliably tell fabricated headlines from real news. Because they read the same feeds under near-identical policies, a single fabricated post can push them into the same trade at the same moment. We present a systematic attack benchmark for information injection against LLM trading agents. Unlike prompt injection, which…

## 112. SPAR: Structural Pruning and Action Recovery for Vision-Language-Action Models

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reinforcement learning, language model, large language, spec
- 作者：Shenli Zheng, Zhou Fang, Yuan Du, Yijiang Liu, Li Du
- 链接：[arXiv](https://arxiv.org/abs/2610.26487) · [PDF](https://arxiv.org/pdf/2610.26487) · [HF](https://huggingface.co/papers/2610.26487)

The limited onboard computing resources of robots make the inference demands of vision-language-action (VLA) models costly to accommodate. Reducing these demands through aggressive compression, however, can degrade manipulation performance beyond what supervised fine-tuning alone recovers. We present SPAR (Structural Pruning and Action Recovery), which simultaneously prunes the hidden and feed-forward intermediate…

## 113. Mitigating Reward Hacking in Preference Reward Models with Evolving Penalties

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, reinforcement learning, benchmark, language model
- 作者：Afonso Baldo, António Farinhas, Marcos Treviso, Ricardo Rei, Nuno M. Guerreiro
- 链接：[arXiv](https://arxiv.org/abs/2610.26496) · [PDF](https://arxiv.org/pdf/2610.26496) · [HF](https://huggingface.co/papers/2610.26496)

Reinforcement learning for language models has moved from preference reward models to verifiable rewards, which sustain much longer optimization. Preference models are prone to reward hacking: the policy raises their score without improving response quality, or even while degrading it. Yet for open-ended tasks, where quality can neither be verified nor fully written down as rubrics, they remain valuable. We…

## 114. ScopeMem: Latent Memory That Learns Where to Revise Frozen GUI Agents

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, memory, language model, spec
- 作者：Zhicheng Zheng, Cheng Zhang, Shengping Yu, Tianxiang Zhao
- 链接：[arXiv](https://arxiv.org/abs/2610.26503) · [PDF](https://arxiv.org/pdf/2610.26503) · [HF](https://huggingface.co/papers/2610.26503)

Latent memory is gaining ground as a lightweight history supplement for GUI agents. It supplies history to a frozen vision-language model via prefix vectors trained with step-wise cross-entropy (CE). While resulting gains are naturally attributed to encoded history, our controlled experiments show they primarily stem from action revision. The prefix learns to alter the model's default actions. However, this revision…

## 115. RouterWorld: Scaling Conversational AI with Latency-Aware LLM Routing

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, evaluation, benchmark, language model, large language
- 作者：Jinyang Li, Denis Emelin, Simone Tedeschi, Weiwei Cheng, Cristina Morariu, Haytham Assem, Jens Lehmann, Emine Yilmaz, Angus Addlesee
- 链接：[arXiv](https://arxiv.org/abs/2610.26511) · [PDF](https://arxiv.org/pdf/2610.26511) · [HF](https://huggingface.co/papers/2610.26511)

Conversational AI systems built on Large Language Models (LLMs) require routing mechanisms that balance answer quality and response latency at scale. However, existing LLM routing benchmarks assume full observability of all candidate model outcomes, under-emphasize latency as a first-class metric, and fragment evaluation across heterogeneous protocols misaligned with real-world settings. We introduce RouterWorld, a…

## 116. Beyond Behavioral Accuracy: Evaluating Individual-Level Fidelity in LLM Investor Simulation

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, language model, large language, spec
- 作者：Jiajie He, Yuanhong Jiang, Xintong Chen, Dongling Ni, Wenjin Liu
- 链接：[arXiv](https://arxiv.org/abs/2610.26524) · [PDF](https://arxiv.org/pdf/2610.26524) · [HF](https://huggingface.co/papers/2610.26524)

Large language models (LLMs) are increasingly used as user simulators, but can they faithfully reproduce an individual's behavior and decision logic over time? We investigate this question in a longitudinal paper-trading study with 80 participants. Using rolling next-day predictions, we evaluate trading activity, buy-sell structure, asset selection, and portfolio outcomes, complemented by controlled input ablations…

## 117. Breaking Diffusion: Parallel Reasoning with Draft Refinement

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, evaluation, language model, spec
- 作者：Jaesang Yu, Seoyeon Byun, Yun Wang, Yan Lu, Juho Kim
- 链接：[arXiv](https://arxiv.org/abs/2610.26542) · [PDF](https://arxiv.org/pdf/2610.26542) · [HF](https://huggingface.co/papers/2610.26542)

Drafting an answer allows a reasoning model to reconsider each decision in the context of the others. Yet repeated diffusion denoising does not ensure that individually plausible token updates form a better answer together. We introduce Draft Refinement Language Models (DRLMs), which use a single denoiser to propose parallel revisions and evaluate a candidate draft. We train the denoiser to reconstruct every token…

## 118. Agentic Orchestration of EDC Data Space Retrieval and Natural Language Driven Data Processing

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reasoning, evaluation, benchmark, spec, retrieval
- 作者：Marla Grunewald, Fin Gentzen, Iulisloi Zacarias, Admela Jukan
- 链接：[arXiv](https://arxiv.org/abs/2610.26548) · [PDF](https://arxiv.org/pdf/2610.26548) · [HF](https://huggingface.co/papers/2610.26548)

Participating in a data space still requires the Dataspace Protocol (DSP) negotiation flow to be hand-coded against each provider's access policy. We present a multi-agent architecture that automates this process using natural language requests. Built on LangGraph over an Eclipse Dataspace Components (EDC), the design separates concerns into cooperating agents. The orchestrator's role is to route and plan. The data…

## 119. BetaMem: Learning to Remember a Changing World for Embodied Agents

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, memory, reinforcement learning, evaluation, spec, retrieval
- 作者：Mai Liu, He Sun, Siru Zhong, Kerun Chen, Hao Yan, Xiaohui Lv, Shuai Tao, Wulong Liu
- 链接：[arXiv](https://arxiv.org/abs/2610.26554) · [PDF](https://arxiv.org/pdf/2610.26554) · [HF](https://huggingface.co/papers/2610.26554)

Long-horizon embodied agents face temporal confusion and incomplete or distorted records, recurring errors from fixed memory rules, and growing storage and retrieval costs. We present BetaMem, a framework for building and evolving traceable long-term memory through six linked layers: working, spatial, entity, episodic, experiential, and procedural memory. A dual-level write contract constrains operation…

## 120. When the harness decides success: state that cannot be re-observed

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, context window, reasoning, benchmark, language model
- 作者：Raimondas Lencevicius
- 链接：[arXiv](https://arxiv.org/abs/2610.26632) · [PDF](https://arxiv.org/pdf/2610.26632) · [HF](https://huggingface.co/papers/2610.26632)

Agent harnesses decide what a language model sees across turns: they drop old turns, summarize them, or replay the model's own earlier reasoning. We ask when these choices change whether an agent succeeds, not only what it costs, and report three findings. First, in a pre-registered synthetic probe, truncating the context window costs a low-cost reasoning model nothing in success when a needed fact can be looked up…
