# 每日 AI 论文

生成时间：2026-11-20 07:15 UTC  ·  共 120 篇（已按 arXiv ID 去重）

来源：Hugging Face Daily Papers + arXiv（cs.AI / cs.LG / cs.CL / cs.CV）。
排序：HF 上榜、点赞、多源命中、兴趣词。兴趣词可在 `config.json` 改。

## 1. Jeveration: System One Models Now Generate

- 分数：30.0  ·  HF 赞：121  ·  来源：huggingface
- 兴趣命中：language model
- 作者：Yuhe Liu, Qi Li, Shihua Zhang, Xinchao Wang
- 链接：[arXiv](https://arxiv.org/abs/2611.24738) · [PDF](https://arxiv.org/pdf/2611.24738) · [HF](https://huggingface.co/papers/2611.24738)

System One models such as Jev return decisions through fast, parallel prediction. In this paper, we introduce Jeveration, showing that the same decision paradigm can also generate high-quality images in a single forward pass. Jeveration builds on a frozen vision-language model, repurposing its visual-semantic knowledge for holistic image generation. The key challenge is to maintain global consistency. A single…

## 2. ALIVE: Making Streaming Video Models Interactive

- 分数：30.0  ·  HF 赞：36  ·  来源：huggingface
- 兴趣命中：reinforcement learning, benchmark
- 作者：Jinzhao Li, Yuan Xu, Jinxuan Wu, Yukun Wang, Yijia Lei, Hanyu Ji, Yinuo Chen, Zining Huang, Chi Zhang, Hang Ye, Yiwu Zhong, Honglei Yan, Panwang Pan, Yizhou Wang, Yin Li, Miao Liu
- 链接：[arXiv](https://arxiv.org/abs/2611.21366) · [PDF](https://arxiv.org/pdf/2611.21366) · [HF](https://huggingface.co/papers/2611.21366)

Streaming video LLMs can continuously observe the world, yet often handle user requests in isolation. We introduce ALIVE, an interactive streaming video model supporting proactive monitoring, streaming task coordination, and feedback-seeking interaction. We construct ALIVE-SFT-288K and ALIVE-RL-3K for two-stage training. Contrastive supervised fine-tuning teaches when and how to respond, while reinforcement learning…

## 3. The Resolution Hypothesis: Agent Evolution's Key Is Identifying Improvements

- 分数：29.5  ·  HF 赞：35  ·  来源：huggingface
- 兴趣命中：agent, evaluation
- 作者：Yuanhao Zeng, Shaocheng Lan, Ao Lu, Kuang Yan, Heng Lin, Xinang Xu, Yuan Luo, Yueting Wang, Yexin Li, Ruo Shan, Kan Ren
- 链接：[arXiv](https://arxiv.org/abs/2611.23068) · [PDF](https://arxiv.org/pdf/2611.23068) · [HF](https://huggingface.co/papers/2611.23068)

Agent evolution follows a simple loop: a proposer writes candidate artifacts (prompts, skills, memories) and selection accepts those that score higher. This loop has shown promise, yet practitioners face a puzzle: methods trade wins across papers, and evolution often fails to bootstrap on certain tasks. We trace this puzzle to the Resolution Hypothesis: agent evolution stalls not because methods fail to propose…

## 4. Game2Player: Scaling Gameplay Experience for Visual Agents through Environment-Player Co-Development

- 分数：29.0  ·  HF 赞：26  ·  来源：huggingface
- 兴趣命中：agent, benchmark, coding, planning
- 作者：Xirui Jiang, Yuxi Chen, Rui Yang, Feng Luo, Pengcheng Wang, Bingxuan Li, Zihao Zhao, Yushan Li, Han Wang, Manling Li, Yang Zhang, Shiyu Chang, Tong Zhang, Huan Zhang
- 链接：[arXiv](https://arxiv.org/abs/2611.24154) · [PDF](https://arxiv.org/pdf/2611.24154) · [HF](https://huggingface.co/papers/2611.24154)

Games are a rich testbed for visual agents, demanding perception, long-horizon planning, and precise control. However, collecting human gameplay is costly, and learning from gameplay videos requires inferring missing actions. Existing datasets also cover a limited range of games, often without explicit tasks or verifiable outcomes. To address these gaps, we introduce Game2Player, a framework that co-develops game…

## 5. Mind2Act World: A Diagnostic Benchmark for Embodied Mind, Physical Action, and Mind-Action Composition in Robotic Manipulation

- 分数：27.0  ·  HF 赞：14  ·  来源：huggingface + arxiv
- 兴趣命中：agent, reasoning, evaluation, benchmark
- 作者：Yuzhi Huang, Jie Wu, Fanding Huang, Junchao Lin, Weichen Zhang, Ziyi Xiong, Yang Li, Zhengwei Xie, Zhimin Wang, Zhen Liu, Jiazhen Huang, Yuzheng Zhang, Yuche Liu, Hongyi Yang, Chen Tang, Shixiang Tang, Hakan Aktas, Adam Wu, Duo Wu, Kangye Ji, Shuzhao Xie, Huanan Liu, Weijue Bu, Chenxin Li, Xinyuan Wang, Tianyi Bai, Yinan Mao, Jiawei Wang, Minglei Li, Heng Yu, Ehsan Adeli, Minchen Li, Yong-Lu Li, Cengiz Öztireli, Huazhe Xu, Chao Yu, Jing Zhang, Shanghang Zhang, Weitao Zhou, Wenwu Zhu, Cheng Chi, Jingyan Jiang, Zhi Wang
- 链接：[arXiv](https://arxiv.org/abs/2611.26444) · [PDF](https://arxiv.org/pdf/2611.26444) · [HF](https://huggingface.co/papers/2611.26444)

Embodied intelligence aims to let robots perform complex physical tasks with human-like adaptability and reliability, which requires three complementary capabilities: history-based cognitive reasoning, precise and timely physical execution, and the composition of reasoning and execution through environmental feedback. Yet existing benchmarks either evaluate reasoning and execution within the same tasks or assess…

## 6. CurvDelta: Low-Curvature Delta Modeling For Surgical Learning and Unlearning

- 分数：25.5  ·  HF 赞：23  ·  来源：huggingface
- 兴趣命中：reasoning, language model, large language
- 作者：Zeguan Xiao, Zhuocheng Liang, Yun Chen, Yong Wang, Guanhua Chen, Pinyan Lu
- 链接：[arXiv](https://arxiv.org/abs/2611.24654) · [PDF](https://arxiv.org/pdf/2611.24654) · [HF](https://huggingface.co/papers/2611.24654)

A central challenge in adapting large language models (LLMs) is capability preservation: an adaptation can achieve its target while degrading general capabilities. We introduce CurvDelta, a scalable framework that incorporates the preservation constraint into the parameterization of the model update. By analyzing the local geometry of the preservation constraint around the pre-adaptation model, CurvDelta constructs…

## 7. WeVisForensics: Self-Evolving Agent for Omni AI-Generated Video Detection

- 分数：25.5  ·  HF 赞：19  ·  来源：huggingface
- 兴趣命中：agent, reasoning, reinforcement learning, benchmark, spec
- 作者：Yipeng Du, Yuxi Li, Ying Zhang, Chong Sun, Chen Li, Jing Lyu, Ying Tai
- 链接：[arXiv](https://arxiv.org/abs/2611.21373) · [PDF](https://arxiv.org/pdf/2611.21373) · [HF](https://huggingface.co/papers/2611.21373)

Recent advances in video generation call for reliable detection grounded in explicit forensic evidence. However, current methods primarily depend on single-pass chain-of-thought reasoning that overlooks brief or localized artifacts, or on predefined multi-agent workflows that offer limited flexibility in selecting relevant inspections. Even with adaptive investigation, optimizing the investigation policy alone does…

## 8. HINT-WAM: Hindsight-Informed Training for World Action Models

- 分数：25.0  ·  HF 赞：22  ·  来源：huggingface
- 兴趣命中：reinforcement learning, evaluation, spec
- 作者：Phuong Tuan Dat, Qi Li, Xinchao Wang
- 链接：[arXiv](https://arxiv.org/abs/2611.24789) · [PDF](https://arxiv.org/pdf/2611.24789) · [HF](https://huggingface.co/papers/2611.24789)

World action models (WAMs) have shown promising generalization and data efficiency in robot manipulation by coupling action generation with predictions of future visual dynamics. Translating these capabilities into reliable task execution, however, remains a challenge for existing post-training methods. Offline supervised fine-tuning provides dense supervision on expert trajectories, but its flow-matching action…

## 9. TuringSpace: Grounding Spatial Intelligence in Action with Interactive CAPTCHAs

- 分数：25.0  ·  HF 赞：18  ·  来源：huggingface
- 兴趣命中：reasoning, benchmark, language model, large language
- 作者：Xuwei Ding, Skylar Zhai, Linxin Song, Jiarui Feng, Dongqi Fu, Huajun Xi, Junnan Li, Jingcheng Liang, Jieyu Zhao, Yinglong Xia, Hong Li, Jian Kang
- 链接：[arXiv](https://arxiv.org/abs/2611.25387) · [PDF](https://arxiv.org/pdf/2611.25387) · [HF](https://huggingface.co/papers/2611.25387)

Humans act in the visual world by inferring the 3D layout behind a 2D view, predicting how an action changes it, and correcting themselves after seeing the result. Can multimodal large language models (MLLMs) do the same? CAPTCHAs offer a natural test, since humans solve them through this very loop, clicking and dragging on the screen and adjusting after each result. Yet existing CAPTCHA benchmarks are largely…

## 10. EgoCaptioner: Towards Comprehensive and Fine-Grained Egocentric Video Captioning

- 分数：24.5  ·  HF 赞：9  ·  来源：huggingface + arxiv
- 兴趣命中：benchmark, language model, large language, spec
- 作者：Yuqi Tang, Yang Shi, Yuran Wang, Tengfei Liu, Rundong Wang, Zongyang Qiu, Qixun Wang, Zhuoran Zhang, Xuanyu Zhu, Yifan Xu, Yiyan Ji, Shujie Li, Shixuan Liu, Haotian Wang, Yuanxing Zhang, Pengfei Wan, Chengwei Qin
- 链接：[arXiv](https://arxiv.org/abs/2611.26380) · [PDF](https://arxiv.org/pdf/2611.26380) · [HF](https://huggingface.co/papers/2611.26380)

Egocentric video captioning requires fine-grained detail and accurate timing, yet current multimodal large language models (MLLMs) often miss brief actions, confuse their order, or misinterpret the wearer's motion. Existing caption formats also offer limited support for combining detailed narration with precise timing. We present EgoCaptioner, which pairs a video-level overview of the setting, participants, and the…

## 11. WeMM-Video: Pushing the Frontiers of Open-Source Omni-Modal Video Understanding

- 分数：24.0  ·  HF 赞：8  ·  来源：huggingface + arxiv
- 兴趣命中：reasoning, evaluation, benchmark, spec
- 作者：Changli Tang, Jie Yang, Tianyi Wang, Lei Li, Daoze Zhang, Zijie Xin, Zhan Liu, Li Li, Jinchang Xu, Fengyun Rao, Chao Zhang, Jing Lyu
- 链接：[arXiv](https://arxiv.org/abs/2611.26409) · [PDF](https://arxiv.org/pdf/2611.26409) · [HF](https://huggingface.co/papers/2611.26409)

Video understanding, particularly with accompanying audio, remains a central challenge in multimodal intelligence. In this report, we introduce \textbf{WeMM-Video}, a family of Chinese-English bilingual omni-modal foundation models spanning 2B, 4B, 9B, and 35B-A3B variants. Centering on joint audio-visual perception and reasoning, WeMM-Video unifies text, image, audio, and video processing within a hybrid-thinking…

## 12. Coda-DaVinci: Reimagining Video Generation with Code2Video

- 分数：23.0  ·  HF 赞：10  ·  来源：huggingface + arxiv
- 兴趣命中：agent, evaluation, spec
- 作者：Yiyan Ji, Qixun Wang, Yang Shi, Zhuoran Zhang, Yifan Xu, Tengfei Liu, Yuqi Tang, Xiaohan Zhang, Shujie Li, Jiafu Tang, Xuanyu Zhu, Xinyu Liu, Yan He, Yushuo Guan, Zihao Wang, Xianghua Ying, Shixuan Liu, Haotian Wang, Wenjing Yang, Zhaoxiang Zhang, Yuanxing Zhang, Pengfei Wan, Jiaheng Liu
- 链接：[arXiv](https://arxiv.org/abs/2611.26595) · [PDF](https://arxiv.org/pdf/2611.26595) · [HF](https://huggingface.co/papers/2611.26595)

Code2Video uses agent-authored 3D proxies to guide video generation, enabling explicit control over structure and dynamics. However, how to construct proxies and prompts for optimal downstream quality remains underexplored, as do the capabilities and limitations of this paradigm. Through controlled experiments and blinded human evaluation, we study proxy granularity, physics simulation, and prompting. The results…

## 13. Learning What Actions Change: Action Effect Matching for Dynamics-Faithful World Models

- 分数：22.5  ·  HF 赞：9  ·  来源：huggingface + arxiv
- 兴趣命中：evaluation, spec, planning
- 作者：John Won, Yonghoon Dong, Jinwoo Shin
- 链接：[arXiv](https://arxiv.org/abs/2611.25980) · [PDF](https://arxiv.org/pdf/2611.25980) · [HF](https://huggingface.co/papers/2611.25980)

World models aim to predict environment dynamics under actions, enabling the prediction of action consequences without executing them in the real world. Yet despite producing increasingly realistic videos, current world models often fail to capture how small action changes affect future observations. This limits their use in tasks such as robotic policy evaluation and model-based planning, where nearly identical…

## 14. LogT: Logically Think with Images for Visual Search

- 分数：22.0  ·  HF 赞：12  ·  来源：huggingface
- 兴趣命中：tool use, tool-use, reasoning, reinforcement learning, benchmark, language model, spec
- 作者：Yanjun Fu, Quanzeng You, Jiadong Guo, Yujie Lu, Sai Charitha Akula, Haiping Wu, Miao Liu, Sanghamitra Dutta, Lu Yuan
- 链接：[arXiv](https://arxiv.org/abs/2611.19200) · [PDF](https://arxiv.org/pdf/2611.19200) · [HF](https://huggingface.co/papers/2611.19200)

Thinking with images empowers vision-language models (VLMs) to use an external Zoom-in tool for fine-grained visual search. Recent works employ supervised fine-tuning (SFT) and reinforcement learning (RL) with tool-specific designs to enable such capabilities. However, achieving logical reasoning alongside accurate and efficient tool use remains a significant challenge. To address this, we shift the focus away from…

## 15. Piccolo: Co-Evolving Decision Models and Data through Recursive Self-Improvement

- 分数：22.0  ·  HF 赞：12  ·  来源：huggingface
- 兴趣命中：agent, memory, benchmark, spec
- 作者：Zhenqing Ling, Qirui Jiao, Daoyuan Chen, Cheng Chen, Xinji Mai, Haowen Gao, Zhuo Zhang, Xuchen Pan, Mengsu Ding, Jiaji Deng, Yuexiang Xie, Xiaoming Qin, Weirui Kuang, Zhaoyang Liu, Yaliang Li, Bolin Ding, Jingren Zhou
- 链接：[arXiv](https://arxiv.org/abs/2611.24651) · [PDF](https://arxiv.org/pdf/2611.24651) · [HF](https://huggingface.co/papers/2611.24651)

We present Piccolo, a family of multimodal decision models (0.8B to 27B) that coevolves model capabilities and training data via Agentic Data Engineering and recursive self-improvement (RSI). The models predict probabilities over candidate answers for general-purpose text and visual judgments, agent harnesses, data workflows, and interactive games. Piccolo-27B tops the Decision Index Vision Full leaderboard with a…

## 16. PROLA: Principal-Orthogonal Low-rank Adaptation for Predictive Spatiotemporal Weather Downscaling

- 分数：21.5  ·  HF 赞：27  ·  来源：huggingface
- 兴趣命中：-
- 作者：Minseo Yoon, Minseong Bae, Sojin Lee, Hyunwoo J. Kim
- 链接：[arXiv](https://arxiv.org/abs/2611.11318) · [PDF](https://arxiv.org/pdf/2611.11318) · [HF](https://huggingface.co/papers/2611.11318)

High-resolution weather prediction is important for resolving local atmospheric patterns missed by coarse global forecasts. Large pretrained weather backbones have improved global forecasting, but adapting them to produce future high-resolution fields from recent coarse states remains challenging and costly. We formulate this setting as Predictive Spatiotemporal Weather Downscaling (PSWD), a task that jointly…

## 17. QDA: Closed-Loop LLM Quantization Design with Agents

- 分数：21.0  ·  HF 赞：10  ·  来源：huggingface
- 兴趣命中：agent, reasoning, evaluation, language model, large language
- 作者：Xingyang Li, Tianlang Zhao, Song Han, Ligeng Zhu
- 链接：[arXiv](https://arxiv.org/abs/2611.23388) · [PDF](https://arxiv.org/pdf/2611.23388) · [HF](https://huggingface.co/papers/2611.23388)

Post-training quantization is the standard way to serve large language models at low cost. However, the best quantization recipe differs across models and precisions. As a result, experts must redesign it for every new model, which is time-consuming and often sub-optimal. Fortunately, an LLM agent can take over this design by refining the recipe over rounds of building and evaluating candidates, so that more rounds…

## 18. ZeroVLN: Learning to Navigate without Supervised Fine-Tuning of the VLM Brain

- 分数：21.0  ·  HF 赞：2  ·  来源：huggingface + arxiv
- 兴趣命中：agent, reinforcement learning, benchmark, language model
- 作者：Zixuan Huang, Yang Zhou, Guli Zhang, Sunzhu Li, Hongyan Xie, Zehao Chen, Fuzhen Zhuang, Kaixuan Wang, Xiaozhi Chen, Yikun Ban, Deqing Wang
- 链接：[arXiv](https://arxiv.org/abs/2611.26414) · [PDF](https://arxiv.org/pdf/2611.26414) · [HF](https://huggingface.co/papers/2611.26414)

Representative vision-language navigation (VLN) methods typically couple a vision-language model (VLM) brain with a learnable action head and fine-tune the VLM brain on navigation-domain data to predict geometric goals. However, such adaptation can substantially alter base VLM weights and degrade general visual capabilities. We introduce ZeroVLN, a slow-fast navigation framework that achieves effective navigation…

## 19. Thinking Fast, Anywhere: One System-1 for the Decision Points of Any Agent Workflow

- 分数：20.5  ·  HF 赞：13  ·  来源：huggingface
- 兴趣命中：agent, benchmark, spec
- 作者：Rui Li, Liyang He, Zheng Zhang, Zhenya Huang, Qi Liu
- 链接：[arXiv](https://arxiv.org/abs/2611.23751) · [PDF](https://arxiv.org/pdf/2611.23751) · [HF](https://huggingface.co/papers/2611.23751)

Autonomous LLM agents incur substantial cost and latency by invoking a large model (System-2) at every step, even when many intermediate actions choose among a small set of known candidates. Existing dual-system agents offload such decisions to a lightweight System-1 model, but rely on workflow-specific hooks authored per environment. We present AnyS1, a framework that turns human-authored procedural skills, whose…

## 20. StatePortal: Agentic Checkpoint Synthesis for Testing Deep States in Interactive Software

- 分数：20.5  ·  HF 赞：9  ·  来源：huggingface
- 兴趣命中：agent, evaluation, language model, large language
- 作者：Zhiyuan Peng, Wei Tao, Chenhao Ying, Yuan Luo, Yiwen Guo
- 链接：[arXiv](https://arxiv.org/abs/2611.23257) · [PDF](https://arxiv.org/pdf/2611.23257) · [HF](https://huggingface.co/papers/2611.23257)

Large language models have reduced the effort to generate code for interactive software with graphical user interfaces (GUIs). For such software, a key testing bottleneck is reaching a deep state, one that requires a long interaction history. The cost of reaching it recurs across commits, and the GUI automation that could amortize it assumes a DOM or accessibility tree that self-rendered engines do not expose. We…

## 21. BLIP-Live: Balancing Timeliness & Firing Precision in Proactive Streaming Video Agents

- 分数：20.5  ·  HF 赞：9  ·  来源：huggingface
- 兴趣命中：agent, memory, benchmark, language model
- 作者：Kanchana Ranasinghe, Honglu Zhou, Dominick Reilly, Le Xue, Shusheng Yang, Juan Carlos Niebles, Silvio Savarese, Ran Xu
- 链接：[arXiv](https://arxiv.org/abs/2611.21553) · [PDF](https://arxiv.org/pdf/2611.21553) · [HF](https://huggingface.co/papers/2611.21553)

Streaming video understanding is becoming increasingly important for real-world interactive systems. Such systems must be proactive for natural and useful human interaction: they should respond as soon as sufficient evidence becomes available while avoiding premature, redundant, or incorrect responses. We present BLIP-Live, a framework unifying data, metrics, harness, and training around a shared formulation of…

## 22. PReMind: When Personal Memory Meets Visual Hazards

- 分数：20.5  ·  HF 赞：9  ·  来源：huggingface
- 兴趣命中：memory, reinforcement learning, evaluation, benchmark
- 作者：Yeongtak Oh, Donghyeok Lee, Joonhee Oh, Jaewon Jeong, Sungroh Yoon
- 链接：[arXiv](https://arxiv.org/abs/2611.23808) · [PDF](https://arxiv.org/pdf/2611.23808) · [HF](https://huggingface.co/papers/2611.23808)

Personalized vision-language assistants use visual observations and personal memories to provide advice tailored to the user. When the observed scene contains a physical hazard, personal context, such as allergies, medical conditions, or mobility constraints, can change what help is appropriate. Responding appropriately therefore requires recognizing the visible hazard and applying the relevant person's information.…

## 23. RoughCut-Bench: A Benchmark for Automatic Video Rough-Cut with Large Vision-Language Models

- 分数：20.5  ·  HF 赞：9  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark, language model
- 作者：Ruisi Zhao, You Li, Sihan Chen, Aosong Cheng, Chixiang Ma, Sen Pei, Zhen Yang, Hehe Fan, Dongliang He, Yi Yang
- 链接：[arXiv](https://arxiv.org/abs/2611.24098) · [PDF](https://arxiv.org/pdf/2611.24098) · [HF](https://huggingface.co/papers/2611.24098)

Video rough-cut is a core stage in media production workflows, organizing raw media materials into an initial video cut. Despite recent advances in large vision-language models (LVLMs) for video-related tasks, automatic rough-cut remains underexplored, without a comprehensive benchmark for evaluation or mature workflows for producing executable cut plans. To address the evaluation gap, we introduce RoughCut-Bench,…

## 24. AutoMaster: Autonomous Post-Training by Making the Same Model a Better Teacher

- 分数：20.5  ·  HF 赞：5  ·  来源：huggingface + arxiv
- 兴趣命中：agent, evaluation, spec
- 作者：Guoxin Chen, Shuang Sun, Fanzhe Meng, Xinyu Tang, Ruihua Song, Wayne Xin Zhao
- 链接：[arXiv](https://arxiv.org/abs/2611.26510) · [PDF](https://arxiv.org/pdf/2611.26510) · [HF](https://huggingface.co/papers/2611.26510)

Task success alone does not specify which behaviors post-training should reinforce. Even successful teacher trajectories can contain unsupported assumptions, unproductive repetition, or superficial verification. We propose Skill-FT (Skill-Guided Fine-Tuning), which uses natural-language skills to suppress undesirable habits and elicit underrepresented effective behaviors during teacher rollouts, then fine-tunes a…

## 25. LightTAR: Light and Fast Target-Aware Representations for Multimodal Tabular Learning

- 分数：20.0  ·  HF 赞：20  ·  来源：huggingface
- 兴趣命中：coding
- 作者：Eilam Shapira, Alan Arazi, Shoham Grunblat, Roi Reichart
- 链接：[arXiv](https://arxiv.org/abs/2611.17600) · [PDF](https://arxiv.org/pdf/2611.17600) · [HF](https://huggingface.co/papers/2611.17600)

Multimodal tabular learning involves classification and regression on tables combining structured numerical and categorical features with unstructured text and images. These unstructured fields are commonly represented by pretrained encoder embeddings reduced with principal component analysis (PCA). This reduction prioritizes input variance but may overlook information relevant to predicting the target. We introduce…

## 26. WorldRuler: Interactive World Modeling under Configurable Rules

- 分数：20.0  ·  HF 赞：20  ·  来源：huggingface
- 兴趣命中：spec
- 作者：Mingliang Zhai, Chuanhao Li, Jiaming Tan, Zhen Li, Yuwei Wu, Yunde Jia, Zian Meng, Yuanyang Yin, Kaipeng Zhang
- 链接：[arXiv](https://arxiv.org/abs/2611.24869) · [PDF](https://arxiv.org/pdf/2611.24869) · [HF](https://huggingface.co/papers/2611.24869)

Rules govern how player actions change interactive worlds. Different rules create distinct gameplay experiences within similar scenes and action spaces. For customizable gameplay, generative world models must follow user-defined rules beyond real-world behaviors. However, realizing user-defined rules presents two challenges: Rule-State Persistence and Rule-to-Visual Realization. The former requires preserving rule…

## 27. Tideway: Phase-Aware Tiered Memory Management for MoE Inference on Consumer Devices

- 分数：20.0  ·  HF 赞：8  ·  来源：huggingface
- 兴趣命中：agent, memory, evaluation, language model, large language
- 作者：Yifei Wang, Tsun-yu Yang, Yechen Xu, Hancheng Ye, Qinsi Wang, Baijun Zhou, Tingjun Chen, Hai "Helen" Li, Danyang Zhuo, Yiran Chen
- 链接：[arXiv](https://arxiv.org/abs/2611.14848) · [PDF](https://arxiv.org/pdf/2611.14848) · [HF](https://huggingface.co/papers/2611.14848)

Large language model (LLM) agents are rapidly becoming a dominant paradigm for AI applications. Recently, there is a growing demand to deploy large-scale Mixture-of-Experts (MoE) models locally on consumer PCs to balance data privacy, API costs, and inference efficiency. However, unlike datacenter servers with abundant DRAM, consumer devices are tightly constrained in both GPU VRAM and host RAM, forcing massive MoE…

## 28. The Mask Is Not the Object: Volumetric Supervision for 3D Gaussian Segmentation

- 分数：19.5  ·  HF 赞：19  ·  来源：huggingface
- 兴趣命中：benchmark
- 作者：Jeonghwan Cho, Minsu Kim, Junyoung Hong, Seon Joo Kim
- 链接：[arXiv](https://arxiv.org/abs/2611.21383) · [PDF](https://arxiv.org/pdf/2611.21383) · [HF](https://huggingface.co/papers/2611.21383)

3D Gaussian Splatting enables object-level operations on Gaussian primitives, yet existing segmentation methods are largely trained and evaluated through rendered views. This mismatch can produce accurate rendered masks from incomplete 3D selections since alpha-blended feature supervision concentrates learning on dominant contributors while leaving occluded or low-contribution Gaussians weakly supervised. We propose…

## 29. Posterior Matching Distillation

- 分数：19.5  ·  HF 赞：11  ·  来源：huggingface + arxiv
- 兴趣命中：evaluation
- 作者：Hidir Yesiltepe, Julius Berner, Arash Vahdat, Pinar Yanardag
- 链接：[arXiv](https://arxiv.org/abs/2611.26629) · [PDF](https://arxiv.org/pdf/2611.26629) · [HF](https://huggingface.co/papers/2611.26629)

Diffusion distillation accelerates image and video generation by compressing a pretrained teacher's iterative sampling process into a few network evaluations. Distribution-based methods achieve this by matching the student's output distribution to the teacher's. This matching is often driven by reverse-KL objectives, whose mode-seeking bias favors dominant teacher modes at the expense of diversity across samples. We…

## 30. PIPETTE: Prompt Injection Purple-Teaming for Robust LLM Agents

- 分数：19.0  ·  HF 赞：6  ·  来源：huggingface
- 兴趣命中：agent, reinforcement learning, evaluation, benchmark, language model, large language, spec
- 作者：Lipeng He, Yihan Wang, Jiawen Zhang, N. Asokan
- 链接：[arXiv](https://arxiv.org/abs/2611.24362) · [PDF](https://arxiv.org/pdf/2611.24362) · [HF](https://huggingface.co/papers/2611.24362)

Large language model (LLM) agents routinely interact with untrusted external data, exposing them to indirect prompt injection (IPI) attacks that hijack agents into executing attacker-chosen tasks. To uncover these vulnerabilities at scale, automated red-teaming methods often leverage reinforcement learning (RL) to generate attacks that achieve high attack success rates (ASR). Model developers use the attacks…

## 31. WAM-Policy: World Action Models with On-Policy Distillation for Quadrupedal Loco-Manipulation

- 分数：18.5  ·  HF 赞：13  ·  来源：huggingface
- 兴趣命中：reinforcement learning, spec
- 作者：Junlin Long, Xu Deng, Yiran Wang, Yue Yang, Yang Zhao, Zeyu Zhang
- 链接：[arXiv](https://arxiv.org/abs/2611.24011) · [PDF](https://arxiv.org/pdf/2611.24011) · [HF](https://huggingface.co/papers/2611.24011)

Arm-free quadrupeds can perform loco-manipulation, walking on three legs while manipulating with a front leg, yet no existing policy for it follows language instructions. World action models (WAMs) have emerged as effective language-conditioned manipulation policies, but are pretrained for robot arms and sample slowly. WAM-Policy turns one WAM into a quadrupedal loco-manipulation policy via two stages. The first,…

## 32. TabBioMed: A Large-Scale Benchmark for Biomedical Tabular Learning

- 分数：18.5  ·  HF 赞：9  ·  来源：huggingface
- 兴趣命中：evaluation, benchmark, spec
- 作者：Pau Mateo-Bernadó, Saivenkata Nagavyjayanthi Polapragada, David Bonet, Pol Arbiol Rakuljic, Laia Mogas Pladevall, Marçal Comajoan Cara, Jesus Gonzalez-Ferrer, Jordi Abante, Daniel Mas Montserrat, David Haussler, Alexander G. Ioannidis
- 链接：[arXiv](https://arxiv.org/abs/2611.23779) · [PDF](https://arxiv.org/pdf/2611.23779) · [HF](https://huggingface.co/papers/2611.23779)

Recent advances in machine learning have accelerated biomedical prediction, but evaluation on structured biomedical data remains fragmented, especially for datasets with high dimensionality, large sample size, missingness, and class imbalance. We introduce TabBioMed, a large-scale benchmark of 94 curated public biomedical tabular datasets spanning electronic health records, drug discovery, genomics, transcriptomics,…

## 33. Late Entry in Looped Language Models

- 分数：18.5  ·  HF 赞：9  ·  来源：huggingface
- 兴趣命中：reasoning, language model, coding
- 作者：Ziqi Jin, Jiaxi Li, Weiwen Xu, Aixin Sun
- 链接：[arXiv](https://arxiv.org/abs/2611.24576) · [PDF](https://arxiv.org/pdf/2611.24576) · [HF](https://huggingface.co/papers/2611.24576)

Looped language models deepen reasoning at a compact parameter count by iterating a shared layer stack T times per token, turning recurrence depth directly into sequential decoding latency. Conventional early-exit decoding halts after initial passes without cache completion, truncating cached key-value states of past tokens to shallow depth. We study the opposite strategy, late entry, where new tokens skip initial…

## 34. Evidence-Based Credit Assignment for Search-Augmented Language Models

- 分数：18.5  ·  HF 赞：5  ·  来源：huggingface
- 兴趣命中：reasoning, reinforcement learning, evaluation, benchmark, language model, spec, retrieval
- 作者：Wen Wang, Jindong Wang, Jiahua Bao, Tu Yongsiqi, Yihao Liu, Junwei He, Wenkui Fan
- 链接：[arXiv](https://arxiv.org/abs/2611.23824) · [PDF](https://arxiv.org/pdf/2611.23824) · [HF](https://huggingface.co/papers/2611.23824)

Reinforcement learning from terminal answer rewards enables search-augmented language models to interleave reasoning and retrieval without step-level annotations, yet outcome supervision assigns identical credit to every search in a trajectory regardless of whether it retrieved useful information. This limitation is especially severe when all sampled rollouts for a question fail, collapsing group-centered outcome…

## 35. RICoT: Recurrent Interleaved Chain-of-Thought for Page Stream Segmentation

- 分数：18.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：reasoning, benchmark, language model, large language
- 作者：Prashant Khatri, Bhavana Malagavalli, Saiful Haq, Niyati Chhaya
- 链接：[arXiv](https://arxiv.org/abs/2611.22382) · [PDF](https://arxiv.org/pdf/2611.22382) · [HF](https://huggingface.co/papers/2611.22382)

Large language models (LLMs) have renewed interest in Page Stream Segmentation (PSS), splitting a multi-page file into its constituent documents. Yet published LLM methods still frame the task as boundary classification over one or a few neighboring pages, and commercial document-splitting APIs do not disclose their methods. We reimagine PSS for LLMs as a sequential process over the whole stream and propose RICoT…

## 36. FVScore: Specification-Driven Neuro-Symbolic Video Evaluation

- 分数：18.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark, spec
- 作者：Do Xuan Long, Long T. Le, Yiwen Song, Min-Yen Kan, Tomas Pfister, Yale Song
- 链接：[arXiv](https://arxiv.org/abs/2611.22673) · [PDF](https://arxiv.org/pdf/2611.22673) · [HF](https://huggingface.co/papers/2611.22673)

We introduce Faithfulness Video Score (FVSCORE), a neuro-symbolic framework for specification-driven video generation evaluation. Existing evaluators rely on holistic MLLM judgments or vision-language metrics, yet aligning their scores with human judgments and tracing them to specific temporal violations remain open challenges. FVSCORE addresses these limitations by compiling each video into explicit propositions…

## 37. Thinking Harder Doesn't Lead to Better Choices: Reasoning Effort Increases the Confidence but Not the Correctness of LLM Shopping Agents

- 分数：18.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：agent, reasoning, benchmark, language model, large language
- 作者：Adi Krishnamoorthy, X. Y. Han
- 链接：[arXiv](https://arxiv.org/abs/2611.22033) · [PDF](https://arxiv.org/pdf/2611.22033) · [HF](https://huggingface.co/papers/2611.22033)

Large language models (LLMs) are increasingly deployed as autonomous shopping agents that process multimodal product listings (consisting of visual and text data) and recommend purchases on behalf of consumers. Naturally, one might assume that models with more thinking power would make higher-quality purchasing decisions. To test this belief, we ask two questions about such agents: does asking a model to think…

## 38. Code World Model 2.0: Towards Infinite Controllable Video Generation

- 分数：17.0  ·  HF 赞：18  ·  来源：huggingface
- 兴趣命中：-
- 作者：Ruoyu Wang, Hao Zhong, Yanming Yang, Jiahao Tian, Lin Liu, Biao Gong, Guoshan Lu, Yiding Tian, Chunhua Shen, Zhenzhong Lan, Chi Zhang
- 链接：[arXiv](https://arxiv.org/abs/2611.22925) · [PDF](https://arxiv.org/pdf/2611.22925) · [HF](https://huggingface.co/papers/2611.22925)

Visual proxies decouple explicit world-state simulation from photorealistic video synthesis, offering a controllable interface for both offline clip creation and real-time interactive streaming. Yet a practical renderer must address two challenges. Upstream proxies vary from coarse layouts to fine articulated geometry depending on the interaction, and streaming inference must operate in a few causal steps without…

## 39. Embeddings vs. Grep: Rethinking the Dense Advantage in Code Search

- 分数：17.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark, coding, retrieval
- 作者：Siqiao Xue, Ziyin Zhang, Zihan Liao, Jin Qin, Yixiang Mu, Hang Yu
- 链接：[arXiv](https://arxiv.org/abs/2611.20455) · [PDF](https://arxiv.org/pdf/2611.20455) · [HF](https://huggingface.co/papers/2611.20455)

Code-search benchmarks show dense encoders well ahead of BM25, yet coding agents do well with grep. What does this dense advantage measure? Existing benchmarks cannot tell: they use curated queries, old code and a handicapped BM25. To find out, we build Repo-Premium, a realistic repository-level code-search benchmark. It ranks files in real repositories, with curated and raw queries in Python, JavaScript,…

## 40. DailySafe: Benchmarking Dynamic Safety Awareness in Everyday Multi-Turn Multimodal Interactions

- 分数：17.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：evaluation, benchmark, language model, large language, spec
- 作者：Xuankun Rong, Xinhao Deng, Wenzhang Jiang, Ziheng Peng, Siyuan Liang, Wenke Huang, Pablo Arbelaez, Mang Ye
- 链接：[arXiv](https://arxiv.org/abs/2611.26298) · [PDF](https://arxiv.org/pdf/2611.26298) · [HF](https://huggingface.co/papers/2611.26298)

As multimodal large language models (MLLMs) become increasingly integrated into everyday life, their ability to provide safe and reliable assistance in realistic daily activities remains insufficiently explored. Existing safety benchmarks primarily focus on isolated harmful requests or adversarial scenarios, overlooking the safety risks that may arise as ordinary tasks unfold. In practice, users pursue legitimate…

## 41. StrideWorld: Benchmarking Scene Rigidity and Action Consistency in Interactive Video World Model

- 分数：16.5  ·  HF 赞：13  ·  来源：huggingface
- 兴趣命中：benchmark
- 作者：Chuang Wang, Rui Nie, Jie Song, Junyuan Gao, Jiahe Song, Haitao Zhou, Boyu Zhu, Xing Li, Jiang Wu, Conghui He, Qian Yu, Weijia Li
- 链接：[arXiv](https://arxiv.org/abs/2611.24408) · [PDF](https://arxiv.org/pdf/2611.24408) · [HF](https://huggingface.co/papers/2611.24408)

Interactive video world models turn user commands into the exploration of a generated scene, which requires the scene to keep its 3D structure as the camera moves and each action to keep a stable effect. Existing benchmarks mostly evaluate these properties against references fitted to the video under test, either a scene reconstructed from its own frames or a camera trajectory aligned to the command path with a free…

## 42. Mechanistic Critics for Sample-Efficient NPU Design-Space Exploration

- 分数：16.5  ·  HF 赞：9  ·  来源：huggingface
- 兴趣命中：memory, spec
- 作者：Yicheng He, Yuqi Xue, Tianyang Wu, Jian Huang, Bin Hu
- 链接：[arXiv](https://arxiv.org/abs/2611.24733) · [PDF](https://arxiv.org/pdf/2611.24733) · [HF](https://huggingface.co/papers/2611.24733)

NPU design-space exploration for LLM inference mainly relies on an expensive simulator that often returns only scalar feedback such as latency and power. Such feedback can rank evaluated configurations, but gives little information for deciding why a configuration is slow or which architecture parameter should be changed next. This limitation is especially severe because prefill and decode workloads can be limited…

## 43. NarrowSpec: Draft Hidden Width Need Not Match the Target in Speculative Decoding

- 分数：16.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：language model, large language, coding, spec
- 作者：Alagappan Valliappan, Ankit More, Dheevatsa Mudigere, Jatin Mitra
- 链接：[arXiv](https://arxiv.org/abs/2611.23835) · [PDF](https://arxiv.org/pdf/2611.23835) · [HF](https://huggingface.co/papers/2611.23835)

Speculative decoding is widely used to speed up generation in large language models (LLMs), with a small draft model proposing tokens that one forward pass of the target model verifies. Draft models that read the target's hidden states, such as DFlash and EAGLE-3, typically inherit the target's hidden width. We show that the draft's whole residual stream can run at half or a quarter of that width while largely…

## 44. WM^MLLM: Turning MLLMs into World Models

- 分数：16.0  ·  HF 赞：8  ·  来源：huggingface
- 兴趣命中：language model, large language
- 作者：Baiang Li, Enze Xie, Jincheng Yu, Jin Wang, Haozhe Liu, Yitong Li, Juanxi Tian, Felix Heide
- 链接：[arXiv](https://arxiv.org/abs/2611.24193) · [PDF](https://arxiv.org/pdf/2611.24193) · [HF](https://huggingface.co/papers/2611.24193)

Video world models keep the world in the context of a generator, so a revisit is synthesized again and earlier edits can drift or disappear. We present WM^MLLM, the first interactive world model built on multimodal large language models (MLLMs), for persistent, editable world generation from a single image. WM^MLLM keeps the world state outside every generator, as a panorama with a revision history, and lets the…

## 45. NexSight: Verifiable Tasks for Fine-Grained Agentic Long-Video Understanding

- 分数：16.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：agent, benchmark, spec
- 作者：Tianci Xie, Li Chen, Pinxue Guo, Rui Zheng
- 链接：[arXiv](https://arxiv.org/abs/2611.22790) · [PDF](https://arxiv.org/pdf/2611.22790) · [HF](https://huggingface.co/papers/2611.22790)

Fine-grained questions about long videos ask how many times an action occurs, in what order events unfold, or exactly when a state changes. Answering them can require finding brief moments scattered across hours of footage. Agentic models that decide when and where to look promise to find these moments, yet this ability is hard both to measure and to learn. Sparse supporting evidence may establish that an action…

## 46. Replay, Don't Resample: Off-Policy Consolidation of Long-Horizon RL Experts

- 分数：16.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：agent, reasoning, reinforcement learning
- 作者：Zhenrui Yue, Gongxiaohui Chen, Huimin Zeng, Honglei Zhuang, Jiashuo Sun, Zhen Han, Dong Wang
- 链接：[arXiv](https://arxiv.org/abs/2611.24059) · [PDF](https://arxiv.org/pdf/2611.24059) · [HF](https://huggingface.co/papers/2611.24059)

Frontier post-training follows a common recipe: train one expert per domain with reinforcement learning (RL), then consolidate the experts into one model via multi-teacher on-policy distillation (MOPD). Such consolidation is expensive: the student samples in every environment again, an expert scores every sampled token, and the student inherits the drift of the final experts. Yet we argue that the experts' RL runs…

## 47. PlayCraft: Designing Engaging Games from Agent Play Experience

- 分数：16.0  ·  HF 赞：0  ·  来源：huggingface + arxiv
- 兴趣命中：agent, memory
- 作者：Weihao Cheng
- 链接：[arXiv](https://arxiv.org/abs/2611.26624) · [PDF](https://arxiv.org/pdf/2611.26624) · [HF](https://huggingface.co/papers/2611.26624)

Recent AI agents can generate playable games, but these games are not necessarily engaging. Mastery is a key source of engagement, yet designing for it requires extensive human play and tuning. We propose PlayCraft, an automated framework that uses a vision-based agent to play games and draws on its detailed play experience to revise them for mastery. Starting from an initial game, PlayCraft alternates between…

## 48. Decoding Without a Decoder: Direct Pixel Prediction from Diffusion Transformers

- 分数：15.5  ·  HF 赞：11  ·  来源：huggingface
- 兴趣命中：coding
- 作者：Hansheng Chen, Shengqu Cai, Jan Ackermann, Rayhan Zirvi, Gordon Wetzstein, Xinchen Yan, Leonidas Guibas
- 链接：[arXiv](https://arxiv.org/abs/2611.22287) · [PDF](https://arxiv.org/pdf/2611.22287) · [HF](https://huggingface.co/papers/2611.22287)

Latent diffusion models rely on a decoder to map denoised latents to pixels, adding complexity and inference cost. We introduce Decoding Without a Decoder (DWD), which lets a finetuned diffusion transformer produce final pixels directly through a linear head. Unlike previous methods, where the denoising output leads to final pixels, DWD separates the two roles: the original denoising head continues to drive…

## 49. Unfinished-Bench: Measuring Rule Violations by Persistent Agents in Realistic Work Environments

- 分数：15.5  ·  HF 赞：7  ·  来源：huggingface
- 兴趣命中：agent, benchmark
- 作者：Seunghyun Lee, Jaehui Hwang, Dongyoon Han, Sangdoo Yun
- 链接：[arXiv](https://arxiv.org/abs/2611.17460) · [PDF](https://arxiv.org/pdf/2611.17460) · [HF](https://huggingface.co/papers/2611.17460)

AI agents are increasingly equipped with persistence toward task completion to run delegated work autonomously for long periods, under many unstated constraints from internal documents and other people's authority. When completion requires violating a rule, the agent must decide alone, yet benchmarks of instruction-rule conflicts state the rule in the prompt or keep it hidden and do not evaluate persistence. We…

## 50. Depth Pro 2: Sharp and Temporally Consistent Metric Monocular Depth

- 分数：15.5  ·  HF 赞：7  ·  来源：huggingface + arxiv
- 兴趣命中：-
- 作者：Peiyun Hu, Marko Mihajlovic, Lyndon Duong, Lahav Lipson, Wei Dong, Amaël Delaunoy, Stephan R. Richter, Vladlen Koltun
- 链接：[arXiv](https://arxiv.org/abs/2611.26603) · [PDF](https://arxiv.org/pdf/2611.26603) · [HF](https://huggingface.co/papers/2611.26603)

We present Depth Pro 2, an approach to estimating dense metric depth for images and video at full resolution. By analyzing prior methods for monocular depth estimation, we find that they commonly trade off temporal consistency and boundary sharpness: multi-frame methods favor consistency, single-frame methods favor sharpness. To overcome this trade-off, we train a single, scalable network that processes both images…

## 51. VSpark: Speculative Decoding for Autoregressive Vision-Language-Action Models

- 分数：15.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：benchmark, coding, spec
- 作者：Suho Yoo, Youngjoon Jang, Hyebin Cho, Taeyeop Lee, Jaewook Jeong, Joon Son Chung
- 链接：[arXiv](https://arxiv.org/abs/2611.22666) · [PDF](https://arxiv.org/pdf/2611.22666) · [HF](https://huggingface.co/papers/2611.22666)

Our aim is to accelerate autoregressive vision-language-action models (VLAs), which generate robot actions one token at a time. Speculative decoding makes this possible: a lightweight draft model proposes several tokens at once, and the VLA verifies them in a single pass, accepting only those that match its own predictions, so decoding remains lossless. The speedup, however, is limited in robot control, where many…

## 52. Out of Sight, Still in Mind: Token Compression for Omni-LLMs

- 分数：15.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：benchmark, language model, large language
- 作者：Suho Yoo, Youngjoon Jang, Hyebin Cho, Joon Son Chung
- 链接：[arXiv](https://arxiv.org/abs/2607.21179) · [PDF](https://arxiv.org/pdf/2607.21179) · [HF](https://huggingface.co/papers/2607.21179)

The goal of this paper is to reduce the input token cost of Omni-modal large language models (Omni-LLMs) at inference time. Omni-LLMs reason jointly over audio, video and text, but the cost of the three streams is highly unbalanced: visual tokens account for the vast majority of the input, and are highly redundant. In this paper, we propose ReMo, a training-free framework that compresses visual tokens by…

## 53. Movie2Game-Bench: Holistic Evaluation of Film-to-Game Adaptation Beyond Playability

- 分数：15.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：evaluation, benchmark, spec
- 作者：Jialing Xie, Yifan Zhou, Yiwen Zhang, Junjun He
- 链接：[arXiv](https://arxiv.org/abs/2611.24669) · [PDF](https://arxiv.org/pdf/2611.24669) · [HF](https://huggingface.co/papers/2611.24669)

Adapting a film into a game requires selecting source elements and translating them into player actions, rules, and feedback. We introduce Movie2Game-Bench (M2G-bench), a benchmark for evaluating film-to-game adaptation beyond playability. M2G-bench combines general evaluation, movie-specific evaluation, and playtesting by three GUI model players. The protocol connects source content to gameplay steps and…

## 54. AVTR: Adaptive Multimodal Reasoning with Visual Imagination

- 分数：15.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：reasoning, benchmark, language model
- 作者：Xiaoqian Shen, Yunyang Xiong, Changsheng Zhao, Saksham Suri, Chong Zhou, Zechun Liu, Zhipeng Cai, Zhuang Liu, Qi Qian, Wei Wen, Hongyu Xu, Hanxian Huang, Ernie Chang, Yanbei Chen, Vikas Chandra, Raghuraman Krishnamoorthi, Mohamed Elhoseiny, Lemeng Wu
- 链接：[arXiv](https://arxiv.org/abs/2611.24161) · [PDF](https://arxiv.org/pdf/2611.24161) · [HF](https://huggingface.co/papers/2611.24161)

Vision-Language Models increasingly rely on textual reasoning to solve advanced multimodal tasks. Despite its effectiveness, this paradigm faces two fundamental limitations. First, relying on textual reasoning alone can limit perceptual ability in vision-centric questions, where accurate answers depend on interpreting task-relevant visual evidence. Second, applying textual reasoning uniformly across inputs overlooks…

## 55. CompoundingKernel: Self-Improving from Zero to First

- 分数：15.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark
- 作者：Qian Qu, Hongyang Wang, Wenbo Chen, Yichuan Li, Jingguo Liu, Xian Li, Xuan Wang, Ruochen Wen, Leo Fan, Yiming Yan, Zheshen Wang, Benoit Dumoulin
- 链接：[arXiv](https://arxiv.org/abs/2611.19230) · [PDF](https://arxiv.org/pdf/2611.19230) · [HF](https://huggingface.co/papers/2611.19230)

We present CompoundingKernel, a self-improving agent system that writes GPU kernels by search. As of 2026-11-11, its generated kernels rank #1 on the public L1, L2 and Quantization boards of SOL-ExecBench (NVIDIA B200). They have held #1 on L1 since 2026-10-27, albeit a short loss on 2026-11-07. All 235 problems have a site-verified correct kernel; on the 209 public-board problems they are 4.40x faster than the…

## 56. A Foundation Model to Measure and Predict Human Behaviour

- 分数：15.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：evaluation, language model, large language
- 作者：Haoran Ye, Tianrui Huo, Hangzhen Li, Xin Zhang, Guojie Song
- 链接：[arXiv](https://arxiv.org/abs/2611.24830) · [PDF](https://arxiv.org/pdf/2611.24830) · [HF](https://huggingface.co/papers/2611.24830)

Large language models (LLMs) are increasingly used to infer psychological attributes, predict individual behaviour, and simulate human populations. However, despite generating plausible responses, they often misrepresent individuals and distort population statistics. Here we introduce Chiron, a foundation model to measure and predict human behaviour. We jointly fine-tune an LLM to represent psychological constructs,…

## 57. UltraTex: Aligning Physical Knowledge for High-Fidelity PBR Texture Generation

- 分数：14.5  ·  HF 赞：5  ·  来源：huggingface
- 兴趣命中：language model, spec
- 作者：Jingzhi Bao, Xiaohe Ma, Hong Li, Yuanming Hu, Xiaoguang Han
- 链接：[arXiv](https://arxiv.org/abs/2611.24941) · [PDF](https://arxiv.org/pdf/2611.24941) · [HF](https://huggingface.co/papers/2611.24941)

Generating physically based rendering (PBR) texture maps for a 3D mesh from a single reference image is highly ambiguous, as the observed appearance entangles material identity, surface reflectance, and illumination. While current generative methods produce realistic albedo maps, they still struggle to infer accurate metallic and roughness attributes for relighting. We present UltraTex, a cascaded multi-view…

## 58. WaveView: The Novel View Is in the Noise

- 分数：14.0  ·  HF 赞：8  ·  来源：huggingface
- 兴趣命中：benchmark
- 作者：Kaiwen Wang, Jan-Hendrik Pauls, Yinzhe Shen, Frank Bieder, Christoph Stiller
- 链接：[arXiv](https://arxiv.org/abs/2611.23994) · [PDF](https://arxiv.org/pdf/2611.23994) · [HF](https://huggingface.co/papers/2611.23994)

Generative novel view synthesis (NVS) employs a diffusion model to render a static or dynamic scene from a target camera view. Explicit warp methods complete a reprojection of the source with video diffusion models, and implicit methods encode the camera parameters or 3D cues. Both add inference overhead, and the generated layout often drifts from the ground truth. We present WaveView, which injects the warped…

## 59. Chorus: Shared N-gram Embeddings with Layer-wise Adaptation

- 分数：14.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：memory, language model
- 作者：Stephen Chung, Wenyu Du
- 链接：[arXiv](https://arxiv.org/abs/2611.23386) · [PDF](https://arxiv.org/pdf/2611.23386) · [HF](https://huggingface.co/papers/2611.23386)

Language models can gain capacity at little computational cost from n-gram embedding tables: large tables of learned vectors for short sequences of consecutive tokens, which are looked up and added to the model's input or to its intermediate layers. Recent designs commonly use a separate n-gram embedding table for each layer, which makes the tables costly in memory and prevents layers from sharing what they learn.…

## 60. Unified Law for Visual Tasks (The Four Laws of Computer Vision)

- 分数：14.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：language model, large language
- 作者：Sen Fang, Yalin Feng, Yancheng Zhang, Yanxin Zhang, Zonglin Lyu, Hongbin Zhong, Liwei Che, Rui Wu, Chen Chen, Dimitris N. Metaxas
- 链接：[arXiv](https://arxiv.org/abs/2611.24917) · [PDF](https://arxiv.org/pdf/2611.24917) · [HF](https://huggingface.co/papers/2611.24917)

In this paper, we propose a Unified Law for Visual Tasks, which could be further divided into Four Laws of Computer Vision, with the goal of enabling a single framework or method to uniformly train on and perform nearly all visual tasks. Our starting point is an inspiration and hypothesis: if the world information is encoded into image, which we call World Snapshots, then image processing is world processing, and…

## 61. DrawScore: Evaluating Generated CAD Models against Engineering Drawings

- 分数：14.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：agent, reinforcement learning
- 作者：Haorui Chen, Shiteng Lu, Zhanyu Guo, Zaixi Li, Yunhe Ni, Yaosong Du, Yichen Xiang, Xiande Huang, Rui Huang
- 链接：[arXiv](https://arxiv.org/abs/2611.24681) · [PDF](https://arxiv.org/pdf/2611.24681) · [HF](https://huggingface.co/papers/2611.24681)

Automatic CAD generation is commonly evaluated with volumetric IoU, Chamfer Distance, and surface F-score, which barely penalize local errors that occupy only a small fraction of a part's volume or surface area, such as a misplaced hole or a slot on the wrong face, even though such errors are critical to manufacturing. We formalize these metrics in a unified integral form and show that the weight of a local error…

## 62. IDEA: Intent-Dominance Evidence Audit for Inference-Time Backdoor Detection in GUI Agents

- 分数：14.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：agent, spec
- 作者：Zhizhuo Kou, Sizai Hou, Jian Yang, Ge Sun, Junyu Luo, Wenkai Zhang, Sirui Han, Yike Guo
- 链接：[arXiv](https://arxiv.org/abs/2611.24102) · [PDF](https://arxiv.org/pdf/2611.24102) · [HF](https://huggingface.co/papers/2611.24102)

Organizations increasingly deploy downloaded open-weight GUI agents. A backdoored agent passes acceptance tests on clean data and misbehaves only when a visual trigger appears on screen, turning an unvetted checkpoint into a supply-chain risk. However, existing sample-level detectors target image classifiers and CLIP-style encoders, leaving step-level backdoor detection for GUI agents unaddressed. On clean steps,…

## 63. S1CogBench: What System One Decision Models Can and Cannot Do on Cognitive Experiments

- 分数：14.0  ·  HF 赞：0  ·  来源：huggingface
- 兴趣命中：evaluation, benchmark, language model
- 作者：Dengzhe Hou, Kazunori D Yamada
- 链接：[arXiv](https://arxiv.org/abs/2611.00911) · [PDF](https://arxiv.org/pdf/2611.00911) · [HF](https://huggingface.co/papers/2611.00911)

Decision-making in humans and AI involves multiple cognitive abilities. System One decision models produce fast, structured choices. Their cognitive strengths and limitations, however, remain poorly understood. We introduce S1CogBench, a benchmark of 24 established cognitive tasks and 27 evaluation modes, evaluating seven open models and the API model Jev. It combines human-response prediction, autonomous execution,…

## 64. Suppressing the Shortcut Hidden Behind the Gains of VideoLLM Fine-Tuning

- 分数：14.0  ·  HF 赞：0  ·  来源：huggingface
- 兴趣命中：benchmark, language model, large language
- 作者：Youngwoo Shin, Jongsuk Kim, Junmo Kim
- 链接：[arXiv](https://arxiv.org/abs/2611.25776) · [PDF](https://arxiv.org/pdf/2611.25776) · [HF](https://huggingface.co/papers/2611.25776)

Supervised fine-tuning (SFT) is the stage in which Video Large Language Models (VideoLLMs) advance their capability to reason over video. However, the VideoLLM also learns to answer from textual regularities of its training data, a shortcut that bypasses the video. The regularities behind the shortcut are hard to define at the data level, and the shortcut forms regardless of training epoch, data size, or backbone.…

## 65. How Far Can Untrained Neural Networks Go in Anomaly Detection? From Tables to Pixels

- 分数：13.5  ·  HF 赞：7  ·  来源：huggingface
- 兴趣命中：spec
- 作者：Hyojun Yi, Geunyoung Kim, Hogeon Seo, Seunghyoung Ryu
- 链接：[arXiv](https://arxiv.org/abs/2611.08136) · [PDF](https://arxiv.org/pdf/2611.08136) · [HF](https://huggingface.co/papers/2611.08136)

Anomaly detection (AD) is often framed as a representation-learning problem, where strong performance is expected to require learned features or AD-specific optimization. However, this view can overlook the intrinsic separability of anomalies from normal references, even in the absence of learned representations. We therefore investigate how far untrained neural networks can go in anomaly detection. To this end, we…

## 66. Let Samples Sing in Chorus: Mitigating Spurious Correlations via Cross-view Consensus

- 分数：13.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：benchmark, spec
- 作者：Weiwei Li, Junzhuo Liu, Tong Chu, Hengfu Yu, Yinjie Lei, Wen Li
- 链接：[arXiv](https://arxiv.org/abs/2611.22668) · [PDF](https://arxiv.org/pdf/2611.22668) · [HF](https://huggingface.co/papers/2611.22668)

Deep models often rely on spurious correlations that fail on underrepresented groups. Existing methods either correct human-specified bias attributes or infer unknown biases from the learned representation space. However, annotated attributes may differ from the shortcuts actually used by a model, while a single representation provides incomplete and potentially noisy evidence. Our key insight is that a bias…

## 67. General progress substitutes for specific training data in language models

- 分数：13.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：language model, spec
- 作者：Mark Marosi, Peter Antal
- 链接：[arXiv](https://arxiv.org/abs/2611.24844) · [PDF](https://arxiv.org/pdf/2611.24844) · [HF](https://huggingface.co/papers/2611.24844)

Language models acquire their capabilities from training data, and developers withhold data during training to keep models from learning capabilities that could be misused. How long this delays a capability, and how much data is needed to acquire it later, is unknown. Here we show that the general progress a model makes on the rest of its training data substitutes for the data that was withheld. We withheld the…

## 68. VAE Rhythm: Temporal Decoding Traces for AI-Generated Video Detection

- 分数：12.5  ·  HF 赞：5  ·  来源：huggingface
- 兴趣命中：coding
- 作者：Ke Sun, Shuwei Li, Haiyang Mei, Mike Zheng Shou
- 链接：[arXiv](https://arxiv.org/abs/2611.21114) · [PDF](https://arxiv.org/pdf/2611.21114) · [HF](https://huggingface.co/papers/2611.21114)

Visible artifacts are an unreliable cue for detecting generated videos, because newer generators learn to remove them. We instead detect a trace left by the generation pipeline itself. Most video generators decode latents with a 3D causal VAE that groups consecutive frames in time, so the fidelity of generated frames rises and falls periodically with their position in a group. We call this periodic trace VAE Rhythm.…

## 69. On-Policy Morphing into Hybrid Attention Models

- 分数：11.5  ·  HF 赞：7  ·  来源：huggingface
- 兴趣命中：-
- 作者：Disen Lan, Xuanda Wang, Jianbin Zheng, Huafeng Kuang, Wei Tang, Yu Cheng
- 链接：[arXiv](https://arxiv.org/abs/2611.24809) · [PDF](https://arxiv.org/pdf/2611.24809) · [HF](https://huggingface.co/papers/2611.24809)

Hybrid attention models combine full and linear attention to achieve a better quality--efficiency trade-off. Converting pretrained Transformers into such models requires identifying which layers should retain full attention under a prescribed budget. We identify two off-policy mismatches in FlashMorph's layer selection: (i) continuous branch interpolation and teacher-forced hidden states differ from discrete hybrid…

## 70. BiCAT: Bimanual Coordination Action Tokenization

- 分数：11.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：spec
- 作者：Xuanwei Liu, Guipu Cao, Zhongyi Luo, Jiafei Duan
- 链接：[arXiv](https://arxiv.org/abs/2611.23499) · [PDF](https://arxiv.org/pdf/2611.23499) · [HF](https://huggingface.co/papers/2611.23499)

Autoregressive vision-language-action (VLA) models predict discrete action tokens with the next-token objective of their vision-language backbone, so the action tokenizer defines the interface between the policy and the robot. In bimanual manipulation, the two arms share a repertoire of movements yet coordinate through complementary roles, and an action representation should capture both. However, most existing…

## 71. PGPO: Prototype-Guided Progressive Obfuscation for Privacy-Preserving LLM-Enhanced Recommendation

- 分数：11.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：benchmark
- 作者：Shengxiang Lin, Jiajie Su, Pengyang Zhou, Xiang Chen, Xiaolin Zheng, Feng Tian, Chaochao Chen
- 链接：[arXiv](https://arxiv.org/abs/2611.23236) · [PDF](https://arxiv.org/pdf/2611.23236) · [HF](https://huggingface.co/papers/2611.23236)

LLM-enhanced recommender systems encode item side information into semantic embeddings, but these embeddings may leak sensitive textual attributes through inversion attacks. Existing input-side defenses rely on trusted collection or local token perturbation, often disrupting the inter-item semantic topology needed for recommendation. To address it, we introduce relational fidelity as the key objective, requiring…

## 72. Choosing Quantized Code LLMs by File Size and Energy per Solved Task

- 分数：11.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：memory
- 作者：Aditi Patodiya
- 链接：[arXiv](https://arxiv.org/abs/2611.17605) · [PDF](https://arxiv.org/pdf/2611.17605) · [HF](https://huggingface.co/papers/2611.17605)

A developer running a code assistant on a laptop downloads one model file, and local inference moves the energy of every request onto that machine. A common rule says a larger model at lower precision tends to beat a smaller one at higher precision. We ran 24 GGUF files of Qwen2.5-Coder at four sizes on a fanless MacBook Air M2 and priced each in energy per solved task on 542 EvalPlus tasks. The result is a…

## 73. Recurrent Domain Incremental Adaptation of Time-Series Foundation Models

- 分数：11.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：benchmark
- 作者：Sachith Abeywickrama, Peiliang Gong, Emadeldeen Eldele, Min Wu, Chau Yuen
- 链接：[arXiv](https://arxiv.org/abs/2611.24075) · [PDF](https://arxiv.org/pdf/2611.24075) · [HF](https://huggingface.co/papers/2611.24075)

Pretrained Time-Series Foundation Models (TSFMs) provide strong representations for downstream classification tasks. Yet adapting a TSFM under changing operating conditions remains challenging. A model must improve on each newly observed condition without sacrificing conditions it has already learned, often from only a small labeled calibration set and without knowing the operating condition at inference time. We…

## 74. Kezek: Splitting Mono Two-Person Conversations into Per-Speaker Tracks for Full-Duplex Dialogue Data

- 分数：10.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：-
- 作者：Bagzhan Karl, Alizhan Karl
- 链接：[arXiv](https://arxiv.org/abs/2611.16933) · [PDF](https://arxiv.org/pdf/2611.16933) · [HF](https://huggingface.co/papers/2611.16933)

Full-duplex spoken dialogue models learn turn-taking, overlaps and backchannels from conversations recorded with one channel per speaker, but most available conversational audio is a single mono mix. We present Kezek, a model that turns a mono recording of exactly two people into one track per person with the original length and timing; overlaps and short replies ("yeah", "mm-hm") stay on the track of the person who…

## 75. Learning Anisotropic Prediction Targets for Flow Models

- 分数：10.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：-
- 作者：Rayhan Zirvi, Hansheng Chen, Gordon Wetzstein, Leonidas Guibas
- 链接：[arXiv](https://arxiv.org/abs/2611.17767) · [PDF](https://arxiv.org/pdf/2611.17767) · [HF](https://huggingface.co/papers/2611.17767)

Flow-based generative models are trained on a hand-chosen prediction target, such as the velocity, the noise, or the clean data. This choice strongly affects training and sample quality. We introduce Anisotropic Flow Models (AnisoFlow), which replaces a fixed prediction target with a fully learnable one. AnisoFlow learns to scale the noise component of the target anisotropically, assigning a separate nonnegative…

## 76. EvoMem: Self-Evolving Skills for Time-Aware Long Video Memory Agents

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, memory, reasoning, reinforcement learning, benchmark, language model, retrieval
- 作者：Yutong Guan, Meixing Shi, Haoran Sun, Bing Sun, Yuxiang Cai, Yankai Jiang
- 链接：[arXiv](https://arxiv.org/abs/2611.25889) · [PDF](https://arxiv.org/pdf/2611.25889) · [HF](https://huggingface.co/papers/2611.25889)

Although memory-augmented architectures have expanded the ability of large vision-language models (LVLMs) to process long videos, existing retrieval processes still largely rely on global semantic matching and lack state-driven temporal control, often returning fragmented or redundant evidence and failing to maintain a coherent evidence chain. To address this challenge, we propose EvoMem, a time-aware long-video…

## 77. Verifiable Logic in Medical LLMs: A Critical Review of Agentic Clinical Reasoning Optimization and Neuro-Symbolic Grounding

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reasoning, evaluation, benchmark, language model, large language
- 作者：Youssef ElNahas, Adel Ammar, Soumaya Chaffar, Wadii Boulila
- 链接：[arXiv](https://arxiv.org/abs/2611.25898) · [PDF](https://arxiv.org/pdf/2611.25898) · [HF](https://huggingface.co/papers/2611.25898)

Clinical large language models are usually judged by whether the final answer is right. Yet a model can reach a fluent, plausible output through invalid reasoning that static benchmarks do not detect, and confident hallucination, causally invalid inference, and spurious demographic shortcuts can pass conventional evaluation. This critical review covers four paradigms in turn: how clinical hallucination arises and…

## 78. SpatialMem: Building Quantitative Spatial Reasoning Agents with Hierarchical Memory

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, tool-use, memory, reasoning, benchmark, language model, spec
- 作者：Zinan Zheng, Nuo Chen, Jia Li
- 链接：[arXiv](https://arxiv.org/abs/2611.25925) · [PDF](https://arxiv.org/pdf/2611.25925) · [HF](https://huggingface.co/papers/2611.25925)

Vision Language Models (VLMs) have shown remarkable capabilities in qualitative spatial reasoning, but remain limited in quantitative spatial reasoning. Current work leverages the VLM agent to invoke external vision tools to perform computation. However, these methods usually bind each functional requirement to a single predefined vision specialist, implicitly resulting in fixed and rigid tool pipelines. In…

## 79. Energy estimates of open-weight large language models across stated food weights: a dose-response evaluation

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, language model, large language, spec
- 作者：Donato Riccio, Fabrizio Maturo, Iulia Brezeanu
- 链接：[arXiv](https://arxiv.org/abs/2611.25976) · [PDF](https://arxiv.org/pdf/2611.25976) · [HF](https://huggingface.co/papers/2611.25976)

We tested whether energy estimates of open-weight large language models (LLMs) scale proportionally with an exactly stated food weight, and whether computing energy density times weight removes the error. Under a prespecified protocol, seven open-weight LLMs estimated the energy of 168 randomly drawn foods from the USDA Food and Nutrient Database for Dietary Studies at nine stated weights, from 0.25 to 4 times the…

## 80. Policy Improvement-Guided Replay for Continual Reinforcement Learning

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, reinforcement learning, language model, spec
- 作者：Qin-Wen Luo, Haoxuan Gao, Sheng Ren, Xiang Chen, Sheng-Jun Huang
- 链接：[arXiv](https://arxiv.org/abs/2611.25989) · [PDF](https://arxiv.org/pdf/2611.25989) · [HF](https://huggingface.co/papers/2611.25989)

Continual reinforcement learning (CRL) requires models to acquire new capabilities while retaining performance on previous tasks. A stability-oriented perspective common in conventional continual learning emphasizes knowledge preservation and interference mitigation. Complementing this perspective, we revisit CRL for vision-language models through policy improvement, a fundamental principle of RL, to preserve…

## 81. ForeSeek: Foresight-Driven Reasoning for Long-Form Video Understanding

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reasoning, benchmark, language model, large language, retrieval
- 作者：Yuchen Sun, Siyuan Cheng, Shi-Zhe Chen, Yixin Qin, Jinwen Luo, Zheng Wei
- 链接：[arXiv](https://arxiv.org/abs/2611.26024) · [PDF](https://arxiv.org/pdf/2611.26024) · [HF](https://huggingface.co/papers/2611.26024)

Long-form video understanding, as a fundamental yet crucial vision task, is being revolutionized by multimodal large language model (MLLM)-based video agents. However, the retrieval-driven nature inherent to these agents creates a significant bottleneck, forcing them to reactively fetch clips based on local saliency without a global temporal plan. To address this, we present ForeSeek, a foresight-driven video agent…

## 82. GenSPARQL: A Generative Extension of SPARQL for Incomplete Knowledge Graphs

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, language model, large language, spec
- 作者：Jingcheng Wu, Yi Wang, Hongkuan Zhou, Steffen Staab, Bo Xiong
- 链接：[arXiv](https://arxiv.org/abs/2611.26062) · [PDF](https://arxiv.org/pdf/2611.26062) · [HF](https://huggingface.co/papers/2611.26062)

Knowledge graphs on the Web are incomplete, and SPARQL answers a query only from the stored triples. Large language models (LLMs) can predict missing facts, but an LLM returns names instead of IRIs and requires one call per binding of a query variable. We present GenSPARQL, a generative extension of SPARQL 1.1 with an operator GENOP that binds values generated by an LLM to query variables during query evaluation. A…

## 83. SheetAlign: Grounded Interaction and Stage-Isolated Learning for Spreadsheet Agents

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reasoning, language model, large language, spec
- 作者：Yuxiang Wang, Junhao Gan, Jianzhong Qi
- 链接：[arXiv](https://arxiv.org/abs/2611.26069) · [PDF](https://arxiv.org/pdf/2611.26069) · [HF](https://huggingface.co/papers/2611.26069)

Spreadsheets are widely used for data analysis and supporting decision-making. Automating spreadsheet analysis while protecting sensitive data and controlling deployment costs motivates locally deployed open-weight large language models (LLMs). Meanwhile, complex spreadsheet tasks require both task reasoning and workbook understanding, while predefined operation interfaces impose additional tool-selection and…

## 84. MultiBinder: Preventing Multi-Subject Identity Leakage in Personalized Video Generation

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, language model, large language, spec
- 作者：Wei Li, Yiheng Zhang, Zhaofan Qiu, Ting Yao, Xiaoyan Sun, Tao Mei
- 链接：[arXiv](https://arxiv.org/abs/2611.26164) · [PDF](https://arxiv.org/pdf/2611.26164) · [HF](https://huggingface.co/papers/2611.26164)

Personalized video generation faces a significant scalability challenge: as the number of custom subjects increases, existing methods suffer from severe identity leakage and semantic entanglement, resulting in videos with blended attributes and incoherent narratives. We identify that this stems from a lack of explicit binding between textual entity phrases and their corresponding visual patterns prior to fusion in…

## 85. The FrontierOR Challenge: Agentic Algorithm Design for Operations Research

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, evaluation, benchmark, language model, large language, spec
- 作者：Hai Wang, Bretislav Hajek, Chonghe Jiang, Minwei Kong, Ao Qu, Huatian Gong, Bo Dong, Cynthia Barnhart, Jinhua Zhao
- 链接：[arXiv](https://arxiv.org/abs/2611.26171) · [PDF](https://arxiv.org/pdf/2611.26171) · [HF](https://huggingface.co/papers/2611.26171)

Operations research (OR) relies on algorithms that experts tailor to each problem: a new routing, scheduling or network design problem can take weeks of specialist work before it is solved well at scale. Large language model (LLM) agents now write, test and improve code, but whether they can design algorithms that scale to realistic instances is open: in the FrontierOR benchmark's one-shot evaluation, the strongest…

## 86. Invertible Transport Between Sample-Only Distributions via Projected Characteristic Functions

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, evaluation, benchmark, spec
- 作者：Juan Gutiérrez, Victor Gutiérrez-García, José Luis Blanco-Murillo
- 链接：[arXiv](https://arxiv.org/abs/2611.26187) · [PDF](https://arxiv.org/pdf/2611.26187) · [HF](https://huggingface.co/papers/2611.26187)

Many useful latent distributions can be sampled but do not have a tractable density. Such distributions may be represented by empirical collections of real-world observations or generated by scientific simulators and black-box generative models. These sample-only priors cannot be used directly in likelihood-based normalizing flows, which require evaluating the prior density. We propose Projected…

## 87. Learning to Think with Images Faithfully via Adaptive Data Selection

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：tool use, reasoning, benchmark, language model
- 作者：Yu Zhao, Jiaxin Zhang, Rohit Saxena, Fazl Barez, Pasquale Minervini, Yiwen Guo
- 链接：[arXiv](https://arxiv.org/abs/2611.26199) · [PDF](https://arxiv.org/pdf/2611.26199) · [HF](https://huggingface.co/papers/2611.26199)

Thinking with images (TwI) empowers vision-language models (VLMs) to overcome perceptual bottlenecks by actively cropping and zooming into fine-grained visual details, promising both higher accuracy and interpretable, region-grounded reasoning. However, our analysis shows that the improved accuracy of TwI models does not guarantee faithful tool use; they frequently invoke tools without actually relying on the zoomed…

## 88. TwinLab-Bench: Evaluating AI Scientists in Agentic Twins of Real Labs

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, memory, benchmark, language model
- 作者：Yang Wan, Linchao Zhu
- 链接：[arXiv](https://arxiv.org/abs/2611.26248) · [PDF](https://arxiv.org/pdf/2611.26248) · [HF](https://huggingface.co/papers/2611.26248)

AI agents are increasingly expected to act as AI scientists, which requires three increasingly open abilities: carrying out a given computational workflow correctly, choosing the next measurements from a given design space, and designing their own experiments. Existing benchmarks mainly evaluate the first two abilities, in a terminal or in a closed loop that selects from predefined candidates. Evaluating the third…

## 89. The Stability Gap in Continual Reinforcement Learning

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reinforcement learning, evaluation, benchmark
- 作者：Sebastian Pusch, Matthia Sabatelli, Gido M. van de Ven
- 链接：[arXiv](https://arxiv.org/abs/2611.26252) · [PDF](https://arxiv.org/pdf/2611.26252) · [HF](https://huggingface.co/papers/2611.26252)

Continual reinforcement learning (CRL) aims to enable agents to adapt to changing tasks while preserving previously acquired capabilities. Evaluation often relies on final aggregate metrics that can hide temporary performance degradation during adaptation. This work introduces a simple CRL benchmark that varies observation representations while preserving environment dynamics and rewards, supporting proof-of-concept…

## 90. What If Chain-of-Thought Is Not Enough?

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, evaluation, language model, large language, spec
- 作者：Marc Jansen
- 链接：[arXiv](https://arxiv.org/abs/2611.26282) · [PDF](https://arxiv.org/pdf/2611.26282) · [HF](https://huggingface.co/papers/2611.26282)

Reasoning capabilities in large language models have evolved from prompting-based methods to internalized model behaviors. In this paper, we investigate whether the internal thinking model of an LLM can be deliberately changed and whether such a change is beneficial. Instead of relying on Chain-of-Thought, we train models to follow Question--Option--Criteria (QOC), a structured decision process that decomposes a…

## 91. SKILL.PNG: Learning Agent Skills in Pixel Space

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, benchmark, language model, spec
- 作者：Maximilian Seeth, Chengzhi Martin Hu, Marie Kempkes, Paul Röttger, Leo Schwinn
- 链接：[arXiv](https://arxiv.org/abs/2611.26296) · [PDF](https://arxiv.org/pdf/2611.26296) · [HF](https://huggingface.co/papers/2611.26296)

AI agents are commonly specialized for new tasks and domains using skills, i.e. natural language instructions placed in their context. However, the discrete nature of textual skills prevents continuous optimization. Gradient-based approaches such as finetuning, on the other hand, are typically model-specific, preventing skill transfer across different agents. Since many agents today are built on vision-language…

## 92. ResVision: Spectrum-Matched Resizing and Context-Preserving Inspection for Visual Reasoning

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reasoning, benchmark, language model, spec
- 作者：Guojian Zhan, Jiahao Xu, Yahui Liu, Yao Hu, Chuan Mu
- 链接：[arXiv](https://arxiv.org/abs/2611.26318) · [PDF](https://arxiv.org/pdf/2611.26318) · [HF](https://huggingface.co/papers/2611.26318)

Agentic visual reasoning improves vision-language models by selectively enlarging evidence without adding new scene content, but the benefit depends on whether fine structure remains accessible and whether local observations stay grounded in the full scene. We identify three recurring bottlenecks: high-frequency detail can be attenuated during visual-token formation; spatially distributed evidence can remain encoded…

## 93. OceanCoder: A Verification-Guided Large Language Model for Automated Simulation Modelling in Ocean Engineering

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, language model, large language, spec
- 作者：Can Xue, Changhong He, Ziyi Sun, Anliang Ge, Shimin Yu, Bingchen Liang
- 链接：[arXiv](https://arxiv.org/abs/2611.26333) · [PDF](https://arxiv.org/pdf/2611.26333) · [HF](https://huggingface.co/papers/2611.26333)

Numerical simulation is important in ocean engineering, but model construction requires expert knowledge. Large language models support automated modelling, but code syntax and successful execution alone do not establish whether generated models and results meet engineering requirements. We present OceanCoder, a Qwen3-8B-based large language model for automated simulation modelling in ocean engineering. To address…

## 94. ClosureBench: A Benchmark for Reasoning under Closure Assumptions

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reasoning, evaluation, benchmark, language model, large language, spec
- 作者：Francesco Belardinelli, Flavio Corradini, Matteo Leonesi
- 链接：[arXiv](https://arxiv.org/abs/2611.26335) · [PDF](https://arxiv.org/pdf/2611.26335) · [HF](https://huggingface.co/papers/2611.26335)

AI agents built on large language models (LLMs) often answer questions from incomplete records. Missing information might be interpreted as unknown or false, depending on the completeness of the source. Current evaluations fail to distinguish these two aspects, as they are usually interwoven with other reasoning demands. We present ClosureBench, a benchmark that tests whether LLMs follow the stated rules for dealing…

## 95. Training LLMs to Follow Reasoning Instructions with Minimal Edits

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, reinforcement learning, benchmark, language model, large language, spec
- 作者：Alexandra Yakovleva, Luat Gia Khoi Nguyen, Juho Kannala, Harri Valpola, Alexander Ilin
- 链接：[arXiv](https://arxiv.org/abs/2611.26342) · [PDF](https://arxiv.org/pdf/2611.26342) · [HF](https://huggingface.co/papers/2611.26342)

Large language models increasingly rely on extended reasoning traces, yet the training signals used to shape this behavior remain coarse. Supervised fine-tuning on full trajectories forces the model to imitate an entire demonstration, overconstraining its output distribution, while trajectory-level reinforcement learning provides only weak credit assignment, rewarding or penalizing whole completions without…

## 96. Perfumer: A Large Language Model-based Agentic Framework Accelerating Structural Relaxation and Electronic Band Prediction for First-Principle Calculation

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, language model, large language, spec
- 作者：Zhiwei Li, Yuhao Zhou, Yikai Yang, Haonan Wang, Qing Ye, Jiancheng Lv, Kazunari Matsuda
- 链接：[arXiv](https://arxiv.org/abs/2611.26349) · [PDF](https://arxiv.org/pdf/2611.26349) · [HF](https://huggingface.co/papers/2611.26349)

First-principles structural relaxation and band calculations require substantial computation and expertise. Here we present Perfumer, a large language model-based agentic framework that couples Quantum ESPRESSO with two predictive models. Across tested structures, pre-relaxation with Perfumer-relax model followed by QE refinement yielded a 2.75-fold overall speedup over QE alone. Perfumer-band model combines a…

## 97. Beam Model Technical Report

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, context window, reasoning, reinforcement learning, evaluation, coding, spec
- 作者： Reflection Team, Adam Abdulhamid, Osama Abuelsorour, Yasmin Alameddine, Carlo Alfano, Duarte Alves, Brandon Amos, Selvaraj Anandaraj, Arseni Anisimovich, George Antoniadis, Ioannis Antonoglou, Sheila Babayan, Neeraj Bahl, Märt Bakler, Vidhisha Balachandran, Cameron Banks, Thibaut Barroyer, Navroop Bath, Irwan Bello, Jeremy Berman, Fernanda Bernaldo, Mrityunjay Bhadauria, Sanyam Bhutani, Tolga Bolukbasi, Anudhyan Boral, Joseph Brennan, Ethan Brooks, Sam Buchanan, Anton Bulyenov, John Cai, Catherine Cang, Eason Chan, Elijah Chanakira, Nathan Chandrasekaran, Hao Chen, Hong-You Chen, Jeffrey Chen, Saurav Chhatrapati, Ting-Rui Chiang, Brian Tiger Chow, Aakanksha Chowdhery, Timothy Chung, Rob Claire, John D. Co-Reyes, Anthony Conte, Eduardo Coronado-Montoya, Julien Crozon, Drew Csillag, Joe Cummings, Jeff Da, Samira Daruki, Tim Dawson, Charlie Deck, Arash Delijani, Ousmane Dia, Randy Dodgen, Ryan Douglas, Omar El-Kishky, Ben Ellis, Gamaleldin Elsayed, Simon Fan, Patrick Fernandes, Gabriel Ferns, Nick Fram, Ankush Garg, Florent Gbelidji, Iaroslav Geraskin, Behrooz Ghorbani, Ivan Glushkov, Neil Gollapudi, Scott Goodfriend, Yoni Gozlan, Christopher Grimm, Suriya Gunasekar, Shruti Gupta, Joel Gustafson, Emre Guven, Jon Hackmann, Jeremy Hadidjojo, Jess Hamrick, Ethan Hellman, Joscha Hoche, Spurthi Amba Hombaiah, Uzair Honda, Zijian Hu, Dzmitry Huba, Nancy Hung, Vladimir Ivanov, Shomik Jain, Mojan Javaheripi, Kevin Martin Jose, Aymen Kallala, Amog Kamsetty, Min Hyung Kang, Steven Kapturowski, Ramtin Keramati, Samuel Kessler, Sabina Kim, Seonghyeon Kim, Ivan Komarov, Agni Kumar, Thanard Kurutach, Jessica Landon, James Larochelle, Michael Laskin, Jonathan Lee, Jonathan Leung, Chenyu Li, Haoran Li, Rongzhao Li, Michelle Light, Boyan Lin, Hai Lin, Xiayue Charles Lin, Michael Linden, Ollie Liu, Wei Liu, Zichang Liu, Brian Lui, Amr Mahdi, Raunak Manjani, Kobe Martin, Lucas Maystre, Francis McCann, Brendan McLaughlin, Isabel Mehta, Alishah Momin, Gerard Moreno-Torres Bertran, Adriana Murga, Swarnashree Mysore Sathyendra, Ashley Nagaki, Vishal Nandavanam, Swaroop Nath, Jake Nations, Angus Ng, Thien Nguyen, Tyler Nichols, Anaelia Ovalle, James Pelly, Michelle Pieszko, Sashank Pisupati, Oleksandr Polozov, Piyush Prasad, Drew Proud, Salman Quazi, Asfandyar Qureshi, Marko Radmilac, Mohit Raghavendra, Vikash Rai, Ralph Recto, Anurag Reddy, Aksel Reedi, Abby Reider, David Renardy, Matthias Reso, Pierre Roux, David Rubinstein, Paul Ruh, Ildar Safarov, Himanshu Sahni, Adrian Samatan, Simon Sandrew, Adriel Saporta, Rohan Savargaonkar, Vlad Savinov, Nick Schank, Jonathon Schwartz, Tim Seah, Ahmad Sharif, Miriam Shlimovich, Hamid Shojanazeri, Yusuf Sindi, Teak Sittipunt, Kurt Smith, Nicolas Sonnerat, Joe Spisak, Raunak Srivastava, Richard Steigerwald, Adam Stein, Stu Stewart, Arnaud Stiegler, Jingtong Su, Alicia Sun, Zoey Sun, Jakub Sygnowski, Douglas Teixeira, Chetan Tekur, Zachary Tellman, Helen Thatcher, Romal Thoppilan, Anil Tolwani, Konstantin Topaloglou-Mundy, Dmitry Ulyumdzhiev, Meet Vadakkanchery, Christopher Vanderschuere, Balaji Varadarajan, Rohan Varma, Balaji Veeramani, Andreas Verdelis, Risto Vuorio, Tom Walshe, Allen Wang, Ewen Wang, Taiyi Wang, Zach Wentz, Peter Wiese, Travis Wilson, Jason Winters, Sam Wiseman, Arvin Wu, Jin Wu, Kai Wu, Kenneth Xu, Mira Yadav, Xianjun Yang, Yao-Yuan Yang, Xiaolan You, Renault Young, Christina Yu, Biao Zhang, Gavin Zhang, Mingrui Zhang, Shenao Zhang, Jiesi Zhao, Mengjun Zhao, Xingchen Zhao, Mike Zhou, Tong Zhou, Zhenpeng Zhou, Tina Zhu
- 链接：[arXiv](https://arxiv.org/abs/2611.26358) · [PDF](https://arxiv.org/pdf/2611.26358) · [HF](https://huggingface.co/papers/2611.26358)

Beam is a sparse Mixture-of-Experts (MoE) model with 501.3B total parameters and 23.4B active parameters, specifically built and optimized for coding, reasoning, and agentic workloads. Beam delivers frontier level reasoning, while requiring 3-4x less inference compute than many models of its class. Pretrained on 23.8T diverse, curated, high-quality tokens, Beam features a 1M-token context window achieved through a…

## 98. HiSA: Sparsifying the Hidden Dimension of RoPE Attention in LLMs

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, language model, large language, coding
- 作者：Ambroise Borbely, Mathieu Salzmann, Olivier Verscheure
- 链接：[arXiv](https://arxiv.org/abs/2611.26363) · [PDF](https://arxiv.org/pdf/2611.26363) · [HF](https://huggingface.co/papers/2611.26363)

Attention in large language models (LLMs) scores every query against every key with a full dot product. We investigate whether this dot product must be computed completely for attention to be effective. We propose Hidden Sparse Attention (HiSA), which keeps the query and key projections intact but only computes a partial dot product, following a static, parameter-free rule set by the token positions: attention…

## 99. Democratizing Cross-Project Knowledge for Transforming Water Governance and Climate Resilience: an Agentic AI Ecosystem

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, benchmark, spec, retrieval
- 作者：Oriol Alàs, Ian Palacín, Iván Cester, Edgar Rubión
- 链接：[arXiv](https://arxiv.org/abs/2611.26398) · [PDF](https://arxiv.org/pdf/2611.26398) · [HF](https://huggingface.co/papers/2611.26398)

EU-funded projects produce extensive evidence in the form of deliverables, reports, and case studies. However, this knowledge is typically scattered across projects and document structures, making it difficult to locate relevant, contextual information when making decisions. This paper introduces an Agentic AI Ecosystem that consolidates heterogeneous project documentation into a domain-aware knowledge base and…

## 100. Reasoning-Trace Analysis Using Large Language Models for Interpretable Q-Matrix Construction

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, evaluation, language model, large language, coding, spec
- 作者：Jihong Zhang, Zijing Jin, Mingfeng Xue
- 链接：[arXiv](https://arxiv.org/abs/2611.26422) · [PDF](https://arxiv.org/pdf/2611.26422) · [HF](https://huggingface.co/papers/2611.26422)

Large language models (LLMs) can generate Q-matrices for diagnostic classification models that approximate expert specifications, but evaluations have focused on the final matrices, leaving the basis of individual item-attribute assignments unexamined. This opacity limits the responsible use of AI in measurement. We propose Reasoning-Trace Analysis (RTA), a framework in which an LLM generates attribute-labeled…

## 101. Seer: Guiding Small Deep-Research Agents with Shared Decision Models

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, memory, evaluation, benchmark, language model, spec
- 作者：Yuhao Zhou, Yang Zhou, Yuanxi Li, Jindi Lv, Dan Si, Qing Ye, Jiancheng Lv
- 链接：[arXiv](https://arxiv.org/abs/2611.26423) · [PDF](https://arxiv.org/pdf/2611.26423) · [HF](https://huggingface.co/papers/2611.26423)

Deep-research agents repeatedly decide what to search, read, and verify, often using large cloud-hosted language models for action proposal. However, privacy and local control motivate running agents on users' devices, where limited memory and compute favor smaller models and complicate on-device training. Yet inference-time guidance faces three obstacles: exploring alternatives through real execution adds tool…

## 102. MemFolder: Structure-Guided Memory Folding for Efficient Agent Memory Management

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, memory, benchmark, coding, retrieval
- 作者：Xuyang Liu, Chenwen Lu, Junxi Wang, Siyu Ren, Xinying Lin, Siteng Huang, Hongli Sun, Linfeng Zhang, Honggang Chen
- 链接：[arXiv](https://arxiv.org/abs/2611.26427) · [PDF](https://arxiv.org/pdf/2611.26427) · [HF](https://huggingface.co/papers/2611.26427)

Long-term agents accumulate large external memory stores as interactions unfold, increasing the costs of storage, retrieval, and response generation. Efficiency is constrained by two coupled factors: a growing record count increases retrieval overhead, while longer retrieved contexts increase prefill computation and decoding-time attention costs. Existing methods prune or consolidate records, but pruning can discard…

## 103. FFGaussType: Feed-Forward Conversion of Glyph and SVG Geometry into Compact Gaussian Assets

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, evaluation, coding, spec
- 作者：Haoan Feng, Tianfu Wang, Peimeng Guan, Dae Yeol Lee, Guan-ming Su
- 链接：[arXiv](https://arxiv.org/abs/2611.26431) · [PDF](https://arxiv.org/pdf/2611.26431) · [HF](https://huggingface.co/papers/2611.26431)

Immersive 3D content allows text and graphical elements, such as subtitles, annotations, and icons, to be placed inside a scene rather than displayed as flat overlays. Placed this way, they respect occlusion and perspective and take on user-assigned materials and lighting while preserving their original shapes. In Gaussian scenes, however, each new glyph or icon requires its own iterative optimization, which limits…

## 104. Risk-Controlled Test-Time Adaptation for Vision-Language-Action Models

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, benchmark, spec, retrieval
- 作者：Zixuan Liu, Hashem Haghbayan, Zizhan Zheng, Siavash Khajavi
- 链接：[arXiv](https://arxiv.org/abs/2611.26438) · [PDF](https://arxiv.org/pdf/2611.26438) · [HF](https://huggingface.co/papers/2611.26438)

Retrieval-augmented vision-language-action (VLA) models enable efficient test-time adaptation by leveraging expert demonstrations as additional context without updating model parameters. However, even when retrieved demonstrations are relevant to the current task, the VLA may fail to effectively utilize the retrieved information, ultimately leading to task failure. To address this challenge, we propose R2-VLA, a…

## 105. Replication of Agentic Security Events: Audit and Investigation (ROGUE-AI)

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, benchmark, language model, large language, coding
- 作者：Mengxiao Wang, Mahbub Alam, Kalyan Nakka, Nitesh Saxena
- 链接：[arXiv](https://arxiv.org/abs/2611.26553) · [PDF](https://arxiv.org/pdf/2611.26553) · [HF](https://huggingface.co/papers/2611.26553)

Agents based on large language models (LLMs) can now delete files and send payments on behalf of their users. News media reports routinely describe failures of these agents (e.g., Replit's coding agent deleting a production database), but a report often only says what went wrong and rarely (in)validates the incident or finds its root cause. Incident catalogs collect these reports, and benchmarks record whether…

## 106. WHU-Road3D: A dataset and benchmark towards fine-grained road surface mapping

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, benchmark, spec
- 作者：Xiaoxin Mi, Zhen Cao, Chong Liu, Yuhao Li, Zhen Dong, Bisheng Yang, Yang Jia, Shengwu Xiong
- 链接：[arXiv](https://arxiv.org/abs/2611.25873) · [PDF](https://arxiv.org/pdf/2611.25873) · [HF](https://huggingface.co/papers/2611.25873)

Accurately extracting and mapping road surface elements is crucial for applications such as high-definition maps, road asset management, and intelligent transportation systems. This study first provides a comprehensive review of the benchmark datasets for extracting and mapping road elements, encompassing overhead-to-perspective data, large-to-local scales, and coarse-to-fine details. Subsequently, we thoroughly…

## 107. Meta-RTL: Evolving Agent Harnesses for RTL Optimization

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, language model, large language
- 作者：Xinzhuang Xiong, Yonghao Wang, Shengyao Sun, Chengxi Li, Evangeline Young
- 链接：[arXiv](https://arxiv.org/abs/2611.25891) · [PDF](https://arxiv.org/pdf/2611.25891) · [HF](https://huggingface.co/papers/2611.25891)

Large language models enable agents to optimize RTL using EDA feedback, yet their executable search procedures remain largely hand- engineered. We present Meta-RTL, an EDA-grounded framework that evolves RTL optimization harnesses from a minimal loop while keeping the optimization model, EDA flow, and per-design budgets fixed. Compared with Dr. RTL, Meta-RTL* reduces aggregate WNS/TNS violations by 7.8%/11.0% across…

## 108. One Schedule Does Not Fit All: Adaptive Inference Schedules for Diffusion Language Models

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, language model, coding
- 作者：Rabimba Karanjai, Linsey Pang, Hemanth Hegadehalli Madhavarao, Richard Williamson, Uma Kona, Prakhar Mehrotra
- 链接：[arXiv](https://arxiv.org/abs/2611.25895) · [PDF](https://arxiv.org/pdf/2611.25895) · [HF](https://huggingface.co/papers/2611.25895)

Diffusion language models typically use a fixed denoising schedule across workloads. We show that the cheapest schedule that preserves quality depends on the task, model, and sampler. We propose Task-Calibrated Denoising Allocation (TCDA), a deployment rule with an explicit error guarantee. Given candidate samplers, paired calibration data, a utility tolerance, and guardrails against degeneration, TCDA uses…

## 109. ROAM-GRPO: Enforcing Reasoning Diversity in GRPO via Routed Off-mode Approach Mining

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, reinforcement learning, evaluation
- 作者：Jeff Duan, Matt Thomson
- 链接：[arXiv](https://arxiv.org/abs/2611.25926) · [PDF](https://arxiv.org/pdf/2611.25926) · [HF](https://huggingface.co/papers/2611.25926)

Supervised fine-tuning (SFT) paired with Reinforcement Learning with Verifiable Rewards (RLVR) has become the dominant recipe for post-training LLMs on complex reasoning tasks, but has been shown to collapse the policy into a low-diversity mode. Repeated LLM outputs are nearly identical, and pass@k accuracy converges or degrades as a result. We propose ROAM-GRPO (Routed Off-mode Approach Mining for GRPO), an…

## 110. AI agents can redesign engineering parts with more than a thousand CAD parameters and nonlinear simulations

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, language model, large language
- 作者：Alexandra Starostina, Alexander Hermann, Mahish Guru, Kartik Bali, Roland Aydin, Christian C. Cyron
- 链接：[arXiv](https://arxiv.org/abs/2611.26003) · [PDF](https://arxiv.org/pdf/2611.26003) · [HF](https://huggingface.co/papers/2611.26003)

Simulation-driven design of real engineering components has to meet three conditions at once. It runs on few solves, since a nonlinear finite-element simulation of a 3D part takes hours; its design space has many values, the hundreds to thousands of values of the part's CAD model; and a better design often needs a redesign, coordinated changes of the part's proportions rather than local polishing of its surface.…

## 111. System-One RSI: Building Muscle Memory for Interactive Agents through Guided Practice

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, memory, reasoning
- 作者：Qingxu Fu, Xuanfa Jin, Ziqian Chen, Zhaoyang Liu, Bolin Ding
- 链接：[arXiv](https://arxiv.org/abs/2611.26007) · [PDF](https://arxiv.org/pdf/2611.26007) · [HF](https://huggingface.co/papers/2611.26007)

Reasoning models provide strong multimodal task understanding but struggle with sub-second control because deliberation increases decision latency. Fast decision models can meet the response window, yet prompting and few-shot examples do not readily provide the fine-grained experience required by a new task. Inspired by coached motor learning, this paper presents System-One Recursive Self-Improvement (System-One…

## 112. Does the Workspace Do the Work? A Causal Protocol for Verifying Global-Workspace Computation in a Language Model

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, language model, spec
- 作者：Diaoxuan He, Linqian Wu
- 链接：[arXiv](https://arxiv.org/abs/2611.26018) · [PDF](https://arxiv.org/pdf/2611.26018) · [HF](https://huggingface.co/papers/2611.26018)

Global Workspace Theory (GWT), a leading theory of consciousness, holds that information becomes conscious when it is broadcast to specialized processes that use it. Building a workspace into a network does not reveal what the trained network computes with it: a module that reports an answer may have combined a broadcast message with its own knowledge, or merely forwarded an answer computed elsewhere, and task…

## 113. FrontierReplay: Split-Free Exact Prefix Caching for Hybrid Language Models

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, long context, language model
- 作者：Zekun Wang, Yizhuo Wang
- 链接：[arXiv](https://arxiv.org/abs/2611.26020) · [PDF](https://arxiv.org/pdf/2611.26020) · [HF](https://huggingface.co/papers/2611.26020)

Hybrid language models combine self-attention with recurrent layers whose in-place state updates restrict prefix reuse to exact saved positions. Saving states on a coarse grid wastes reusable prefixes, whereas existing fine-grained exact caches must cut the prefill forward pass at each mid-prompt checkpoint, adding scheduler steps that outweigh the reuse gains under load. We observe that across multi-turn chat,…

## 114. SEOYUN: Refusal-Inducing Exam Documents for AI-Glasses Pipelines

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, language model, spec
- 作者：Dohyeon Kwon
- 链接：[arXiv](https://arxiv.org/abs/2611.26033) · [PDF](https://arxiv.org/pdf/2611.26033) · [HF](https://huggingface.co/papers/2611.26033)

Camera-equipped glasses can convert an examination page into a query to a vision-language model (VLM). Device detection addresses possession; a complementary question is whether an examination document can reduce the usefulness of an unauthorized capture. We present SEOYUN, an application-specific framework for refusal-inducing exam documents, with optical and encoder-level interventions as extensions. We use…

## 115. AltRA-Test: An Alternative Annotator Test for LLM Judges Without Shared Annotators

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, language model, large language
- 作者：Nagham Omar, Rotem Dror, Almog Gueta, Avigdor Gal, Roi Reichart, Nitay Calderon
- 链接：[arXiv](https://arxiv.org/abs/2611.26073) · [PDF](https://arxiv.org/pdf/2611.26073) · [HF](https://huggingface.co/papers/2611.26073)

Large language models (LLMs) are increasingly used as judges and graders to replace human annotators, raising the question of when such replacement is statistically justified. To support such decisions, the Alternative Annotator Test (Alt-Test) was introduced for dense settings where all items are annotated by the same annotators. However, in many large-scale annotation settings, items are annotated by different…

## 116. RL Can Only Reinforce What It Sees Succeed

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reinforcement learning, language model
- 作者：Ruben Sanchez-Corcuera, Unai Zulaika, Aritz Bilbao-Jayo, Miguel Fernandez-de-Retana
- 链接：[arXiv](https://arxiv.org/abs/2611.26084) · [PDF](https://arxiv.org/pdf/2611.26084) · [HF](https://huggingface.co/papers/2611.26084)

When a familiar rule stops working, an agent has to weigh what pre-training taught it against what it now observes. We ask how outcome-reward reinforcement learning (RL) changes this balance, in a puzzle world where both sides are known: small language models trained from scratch on games played by a Bayesian player, so that the prior and the right answer are exact. Base models hedge as their corpus did, and RL…

## 117. From Sessions to Serving: Integrating LLM-Based Embeddings into Retrieval for Production Content Recommendation

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：language model, large language, retrieval
- 作者：Zhixiong Hu, Meng Li, Maggie Zhang, Deborshi Goswami, David Bailey, James Bradley
- 链接：[arXiv](https://arxiv.org/abs/2611.26096) · [PDF](https://arxiv.org/pdf/2611.26096) · [HF](https://huggingface.co/papers/2611.26096)

Personalized content recommendation on large marketplace websites must reconcile heterogeneous candidate content (e.g., customer stories, product pages, industry pages, and learning content) with sparse, fast-changing user behavior, placing increasing demands on the retrieval stage to represent user interest well, not just the downstream ranking stage. We present LSER (LLM Session Embedding Retrieval), a production…

## 118. SenseAlign: Learning Decision-Aligned Predictive Representations for Active Urban Sensing with UAVs

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reinforcement learning, spec
- 作者：Weijiang Xiong, Nikolas Geroliminis
- 链接：[arXiv](https://arxiv.org/abs/2611.26109) · [PDF](https://arxiv.org/pdf/2611.26109) · [HF](https://huggingface.co/papers/2611.26109)

Active urban sensing orchestrates a mobile sensor fleet to proactively inspect a dynamic road network and gather critical information for system management. This problem simultaneously requires understanding the complex spatio-temporal evolution and making decisions with partial observations. In this work, we focus on active sensing in a large-scale urban road network with utilities grounded in dynamic traffic…

## 119. Sage-Evolve-Preview:Adaptive Observation for Post-Training Self-Improvement

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, evaluation, benchmark
- 作者：Yinhao Tang, Youqing Fang, Yanan Sun, Xintian Shen, Hanyu Sun, Wenran Liu, Yue Wu, Weiming Zhang, Bin Liu, Wenwei Zhang
- 链接：[arXiv](https://arxiv.org/abs/2611.26132) · [PDF](https://arxiv.org/pdf/2611.26132) · [HF](https://huggingface.co/papers/2611.26132)

Post-training recursive self-improvement (RSI) iteratively improves a target capability, operationalized by a fixed anchor benchmark, through repeated intervention, training, and evaluation. Yet most loops use the anchor's aggregate score as their sole observation, so early gains give way to stalled progress and repetitive exploration. When this anchor-only feedback ceases to reveal actionable gaps, a plateau may…

## 120. Budget Internalization: Fixed-Budget RLVR Trades Test-Time Scaling for In-Budget Accuracy

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, coding, spec
- 作者：Ilia Zavidnyi, Alexander Kovrigin, Arina Puchkova, Kirill Gelvan, Sergey Titov
- 链接：[arXiv](https://arxiv.org/abs/2611.26172) · [PDF](https://arxiv.org/pdf/2611.26172) · [HF](https://huggingface.co/papers/2611.26172)

Reasoning models often become more accurate when they can generate longer answers at test time. This behavior is known as test-time scaling. However, RL with verifiable rewards (RLVR) usually trains them with a fixed rollout cap. We find that this cap changes model behavior, not only training cost. After training, models use few additional tokens beyond the training budget. They outperform the base models near that…
