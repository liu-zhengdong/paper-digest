# 每日 AI 论文

生成时间：2026-11-02 06:04 UTC  ·  共 15 篇（已按 arXiv ID 去重）

来源：Hugging Face Daily Papers + arXiv（cs.AI / cs.LG / cs.CL / cs.CV）。
排序：HF 上榜、点赞、多源命中、兴趣词。兴趣词可在 `config.json` 改。

## 1. R^2Orch: Recursive Self-Improvement for Agent Orchestration via Self-Play within a Skill-Internalization Loop

- 分数：28.0  ·  HF 赞：32  ·  来源：huggingface
- 兴趣命中：agent, evaluation
- 作者：Mingda Zhang, Yun Huang, Qiang Huang, Yanjin Li, Rui Qian, Qichao Zhao, Tiesunlong Shen, Na Zhao, Jian Wang, Xiaoying Tang
- 链接：[arXiv](https://arxiv.org/abs/2610.22740) · [PDF](https://arxiv.org/pdf/2610.22740) · [HF](https://huggingface.co/papers/2610.22740)

In recent years, agentic orchestration has been widely applied to solve complex human tasks. However, existing orchestration learning still faces key challenges, including hand-designed curricula, advantage collapse when a task's rollouts all reach the same outcome, and unreliable evaluation signals that judge each skill by one noisy score. To address these challenges, we propose R^2Orch, a new paradigm of Recursive…

## 2. Does Scaling Toward AGI Depend on What System-1 Lets System-2 Execute?

- 分数：27.5  ·  HF 赞：27  ·  来源：huggingface
- 兴趣命中：agent, tool use, reasoning
- 作者：Qi Wang, Yun Qu, Lizhou Cai, Heming Zou, Haoang Chi, Yiqin Lv, Xiang Li, Haiyan Feng, Mengyu Ge, Yize Geng, Yuhang Jiang, Yixiu Mao, Xiangyang Ji
- 链接：[arXiv](https://arxiv.org/abs/2610.39497) · [PDF](https://arxiv.org/pdf/2610.39497) · [HF](https://huggingface.co/papers/2610.39497)

Progress toward artificial general intelligence (AGI) has largely relied on scaling a resource-intensive executive, System-2, through larger models, more data and compute, longer reasoning, and more agents. We ask whether the next stage may come instead from co-designing it with System-1, a lightweight, semantically aware predictor that evaluates candidate interactions before execution, so that System-2 acts only on…

## 3. CEPO: A General Framework for Improving Prompt Optimization in Multi-Agent Systems

- 分数：21.5  ·  HF 赞：15  ·  来源：huggingface
- 兴趣命中：agent, benchmark, spec
- 作者：Jongha Kim, Seohyun Lee, Jonathan Minho Chung, Jinsung Yoon, Hyunwoo J. Kim
- 链接：[arXiv](https://arxiv.org/abs/2610.34722) · [PDF](https://arxiv.org/pdf/2610.34722) · [HF](https://huggingface.co/papers/2610.34722)

Multi-agent systems (MAS) require both effective coordination and specialized task execution. Existing prompt optimization approaches typically couple these functions within agent-specific prompts. We introduce Coordinator-Executor Prompt Optimization (CEPO), a general framework for improving prompt optimization in MAS. CEPO separates system-level coordination from agent-level execution through a shared coordinator…

## 4. CaPtain: A Pipeline for Post-Training Code-as-Policy Robot Agents

- 分数：21.0  ·  HF 赞：10  ·  来源：huggingface
- 兴趣命中：agent, tool-use, reinforcement learning, language model, coding
- 作者：Yijia Fan, Xilin He, Yilei Jiang, Dongming Wu, Jiaxu Wang, Xiangyu Yue
- 链接：[arXiv](https://arxiv.org/abs/2610.40799) · [PDF](https://arxiv.org/pdf/2610.40799) · [HF](https://huggingface.co/papers/2610.40799)

Across coding, web, and tool-use tasks, language-model agents are now routinely trained with the same recipe: supervised fine-tuning (SFT) to learn the interface, then multi-turn reinforcement learning (RL) to master it. Code-as-policy (CaP) casts robot manipulation in the same form, as the policy writes code against robot APIs and reads back the results, so the same recipe should apply. Yet existing CaP agents…

## 5. HiFOR: Hierarchical Foresight with Action-Guided World Grounding for Vision-Language-Action Model

- 分数：20.5  ·  HF 赞：13  ·  来源：huggingface
- 兴趣命中：benchmark, spec, retrieval
- 作者：Rongxing Ding, Hongyu Qu, Kehong Wu, Xudong Wang, Fan Zhang, Xinguang Xiang, Xiangbo Shu
- 链接：[arXiv](https://arxiv.org/abs/2610.40373) · [PDF](https://arxiv.org/pdf/2610.40373) · [HF](https://huggingface.co/papers/2610.40373)

Vision-Language-Action (VLA) models have demonstrated promising capabilities in robotic manipulation by integrating visual perception, language understanding, and action generation. Recent advances have further incorporated future prediction to enhance the understanding of environmental dynamics and task progression. However, existing methods often model short-term dynamics and long-term task objectives separately,…

## 6. FrameForge: Harnessing Priors of Video Foundation Models for Unified Image Generation

- 分数：19.5  ·  HF 赞：11  ·  来源：huggingface
- 兴趣命中：reasoning, coding, spec
- 作者：Yijing Lin, Zhendong Mao, Mengqi Huang, Yuxin Wang, Yongdong Zhang
- 链接：[arXiv](https://arxiv.org/abs/2610.36545) · [PDF](https://arxiv.org/pdf/2610.36545) · [HF](https://huggingface.co/papers/2610.36545)

Unified conditional image generation requires a single model to preserve different aspects of a visual input while producing a target image that follows textual guidance. Pretrained video models provide a promising foundation by encoding visual transformations across time, yet existing approaches typically assign the condition and target to fixed temporal positions. We observe that condition-target relationships…

## 7. Apriel Voice 27B Preview: An Open Model for Speech, Reasoning, and Tool Use

- 分数：18.5  ·  HF 赞：9  ·  来源：huggingface
- 兴趣命中：tool use, reasoning, language model
- 作者：Aman Tiwari, Akshay Kalkunte, Akintunde Oladipo, Jash Shah, Tara Bogavelli, Hoang Nguyen, Nishanth Madhusudhan, Vishal Juneja, Sridhar Nemala, Srinivas Sunkara, Sathwik Tejaswi Madhusudhan, Shruthan Radhakrishna, Masoud Hashemi, Kelechi Ogueji, Khalil Slimi, Saloni Mittal, Pulkit Pattnaik, Shashank Maiya, Dhruv Jhamb, Esakkivel Esakkiraja, Katrina Stankiewicz, Gabrielle Gauthier Melançon, Fanny Riols, Amit Saha, Lakshmi Sirisha Chodisetty, Nitin Aggarwal, Anil Madamala, Sagar Davasam, Segan Subramanian, Vikas Yadav, Sai Rajeswar Mudumba
- 链接：[arXiv](https://arxiv.org/abs/2610.40738) · [PDF](https://arxiv.org/pdf/2610.40738) · [HF](https://huggingface.co/papers/2610.40738)

A capable voice assistant must do more than recognize words; it must understand requests, reason over context, sustain conversations, and act through tools. We present Apriel Voice 27B Preview, an open speech-language model that unifies these capabilities within a shared reasoning backbone while retaining text and image input modalities. Built on the post-trained Gemma 4 26B-A4B checkpoint, Apriel Voice directly…

## 8. WorldBridge: Bridging Video and Action for Task Generalization in World Action Models

- 分数：18.0  ·  HF 赞：8  ·  来源：huggingface
- 兴趣命中：memory, benchmark, spec
- 作者：Jun Cen, Yubo Guo, Hao Li, Liangkai Li, Yaoxu Lyu, Meng Wei, Zeqi Xiao, Sizhe Yang, Yuqiang Yang, Yifan Ye, Shanghang Zhang, Duo Zheng
- 链接：[arXiv](https://arxiv.org/abs/2610.40748) · [PDF](https://arxiv.org/pdf/2610.40748) · [HF](https://huggingface.co/papers/2610.40748)

Achieving the broad task generalization of embodied models in physical environments remains a central challenge in robot learning. We study this challenge in World Action Models (WAMs) through two complementary capabilities: video generalization, which predicts the visual evolution of new tasks, and action generalization, which translates these predictions into executable behavior through a video-to-action bridge.…

## 9. RoboArchitect: Automating the Design of Robotic Agents with Persistent Memory

- 分数：18.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：agent, memory, benchmark, coding, spec
- 作者：Shengguang Wu, Suning Huang, Cherie Ho, Ria Doshi, Hao Zhu, Serena Yeung-Levy
- 链接：[arXiv](https://arxiv.org/abs/2610.42141) · [PDF](https://arxiv.org/pdf/2610.42141) · [HF](https://huggingface.co/papers/2610.42141)

Recent work shows that a frozen robot policy performs far better inside an agent harness, where control code decides when to query the policy, consult vision tools, or command the arm directly. Yet today these harnesses are built by hand and redesigned for each new robot or benchmark. We show that harness design can be automated, offering a strong alternative to finetuning on a novel setup. In RoboArchitect, a…

## 10. Wizard: Manipulate Any World in Real Time via Agentic Control

- 分数：17.0  ·  HF 赞：14  ·  来源：huggingface
- 兴趣命中：agent
- 作者：Yuzhe Wu, Zijun Lin, Yeying Jin
- 链接：[arXiv](https://arxiv.org/abs/2610.40339) · [PDF](https://arxiv.org/pdf/2610.40339) · [HF](https://huggingface.co/papers/2610.40339)

Recent advances in video world models have enabled the generation of increasingly realistic and interactive virtual environments, opening new possibilities for player-customizable gameplay. Agentic frameworks further advance this direction by decoupling explicit game logic and controllable world representations from visual generation. However, existing approaches support only simple game settings and predefined…

## 11. HALO: Human-Grounded Granular Evaluation of Proactive Agents

- 分数：17.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：agent, reasoning, evaluation, spec, retrieval
- 作者：Wenqi Pei, Xinyu Wang, Jinrui Liu, Cynthia Zhuge, Jie Sheng, Zihan Wang, Tenghao Huang, Muhao Chen
- 链接：[arXiv](https://arxiv.org/abs/2610.39086) · [PDF](https://arxiv.org/pdf/2610.39086) · [HF](https://huggingface.co/papers/2610.39086)

Proactive agents must decide whether, when, and how far to assist without an explicit request. Existing evaluations often rely on automated scores or binary verdicts, offering limited human diagnosis of evidence use and intervention quality. To address these gaps, we introduce HALO, Human-Grounded GrAnular EvaLuation of PrOactive Agents. HALO-Arena covers 4 proactive need types, Dependency, Blockage, Risk, and…

## 12. On the Origin and Evolution of Training-Inference Mismatch in LLM Reinforcement Learning

- 分数：15.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：reinforcement learning, language model, large language
- 作者：Yu Li, Yufa Zhou, Tian Lan
- 链接：[arXiv](https://arxiv.org/abs/2610.40945) · [PDF](https://arxiv.org/pdf/2610.40945) · [HF](https://huggingface.co/papers/2610.40945)

On-policy reinforcement learning for large language models assumes that training responses are sampled from the current policy. In practice, an inference engine samples the responses and a separate trainer computes the gradients, and the training-inference mismatch between the two makes the training data off-policy. The mismatch has two sources, the numerics of the engine and the stale weights of asynchronous…

## 13. Probing Spatial State Representations in Visual Foundation Models

- 分数：12.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：retrieval
- 作者：Baiqiao Yin, Zhongang Cai, Ruisi Wang, Qiwei Liang, Lei Yang, Ziwei Liu
- 链接：[arXiv](https://arxiv.org/abs/2610.40636) · [PDF](https://arxiv.org/pdf/2610.40636) · [HF](https://huggingface.co/papers/2610.40636)

An observer sees only part of the surrounding world, yet must keep track of what lies beyond the current view. Spatial perception therefore involves more than recognizing individual images: it calls for a persistent spatial state that is updated under self-motion and used to guide action. Do visual foundation models provide representations that support such a state? We study this question through four levels of…

## 14. WeFair: Fidelity-Aware Alignment from Human Feedback for Personalized Query Rewriting in Short-Video Search

- 分数：11.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：reasoning
- 作者：Yingtao Ren, Aolin Li, Cheng Cheng, Huiyun Hu, Huasheng Liang, Baoxing Xie, Jun Yuan, Haijun Wu, Yiwei Fu, Chenxing Wang
- 链接：[arXiv](https://arxiv.org/abs/2610.16927) · [PDF](https://arxiv.org/pdf/2610.16927) · [HF](https://huggingface.co/papers/2610.16927)

Short-video search needs compact query rewriters that recover users' personalized intent from ambiguous queries under strict latency constraints. Existing LLM-based methods have improved rewriting by using synthetic reasoning and subsequent consumption-behavioral feedback. However, overemphasizing subsequent consumption can favor engaging content over the user's immediate need, causing intent drift even when…

## 15. CausalWAM: Learning the Causes of Actions in World Action Models

- 分数：9.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：-
- 作者：Juntao Cheng, Jinzhou Tang, Fan Feng, Henrik I. Christensen, Yujia Zheng
- 链接：[arXiv](https://arxiv.org/abs/2610.42096) · [PDF](https://arxiv.org/pdf/2610.42096) · [HF](https://huggingface.co/papers/2610.42096)

World action models (WAMs) learn latent variables from observations and use these to both predict the evolution of the scene and to generate actions. The prediction has to be of the whole scene, whereas only a portion of the scene causes actions. WAMs fitted to demonstrations do not, in general, guarantee that they will generate actions solely from the latent causes of the demonstrated actions (the action-relevant…
