# 每日 AI 论文

生成时间：2026-11-17 07:55 UTC  ·  共 120 篇（已按 arXiv ID 去重）

来源：Hugging Face Daily Papers + arXiv（cs.AI / cs.LG / cs.CL / cs.CV）。
排序：HF 上榜、点赞、多源命中、兴趣词。兴趣词可在 `config.json` 改。

## 1. Envisioning Agentic Robotics: A New Era of Robotic Systems

- 分数：36.0  ·  HF 赞：118  ·  来源：huggingface
- 兴趣命中：agent, reasoning, evaluation, benchmark, spec
- 作者：Grid Robotics, Qingfeng Lan, Duo Li, Siyao Li, Yiheng Lyu, Shijian Lu, Zhenghao Qi, Shizun Wang, Xinchao Wang, Ming Yang, Zhiqin Yang, Zuhao Yang, Tao Yu
- 链接：[arXiv](https://arxiv.org/abs/2611.18359) · [PDF](https://arxiv.org/pdf/2611.18359) · [HF](https://huggingface.co/papers/2611.18359)

The release of GPT-6 Astra marks the emergence of a new paradigm in robotics: agentic robotics. Within weeks, frontier models with agentic harnesses matched or exceeded task-specific policies on many embodied benchmarks. Instead of training a dedicated policy for each family of tasks, an agentic robotic system applies a foundation model to open-world embodied tasks. It operates in a closed loop: observing the…

## 2. Gamer: A Generalist Vision-Language-Action Foundation Model for Long-Horizon Real-Time Game Agent

- 分数：36.0  ·  HF 赞：101  ·  来源：huggingface
- 兴趣命中：agent, memory, context window, reasoning, reinforcement learning, benchmark
- 作者：Run Luo, Kuan Zhang, Qi Deng, Yukun Chen, Zhihao Yang, Yufei Zhang, Renrong Hu, Yi Zhang, Guiyu Ma, Tianyu Fan, Longze Chen, Hao Sun, Jiaming Li, Jiaming Yang, Xiaohao Liu, Tao Tan, Minzheng Wang, Hangtian Jia, Shuai Yuan, Lvdi Wang, Xiao Liu, Chao Ma, Yuting Zou, Yinhe Zheng, Xiaobo Xia, Dawei Jiang, Shaoqing Ren
- 链接：[arXiv](https://arxiv.org/abs/2611.18397) · [PDF](https://arxiv.org/pdf/2611.18397) · [HF](https://huggingface.co/papers/2611.18397)

We introduce Gamer, a generalist agent framework built for long-horizon tasks in complex interactive environments. Its end-to-end architecture combines perception, memory management, and multi-step reasoning. A shared training and deployment pipeline supports interaction with both conventional 2D graphical interfaces and complex 3D simulated worlds. We first continue pre-training on a dataset constructed from tens…

## 3. VibePrevisBench: Evaluating Agentic Coding for 4D Scene Generation in Blender

- 分数：36.0  ·  HF 赞：87  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark, coding, spec
- 作者：Yuzhe Chen, Muxi Diao, Lele Yang, Wenbin Xu, Xuyang Liu, Qile Su, Changyi Liu, Jiankang Chen, Kaiyu Jiang, Haoyu Zhang, Hongyi Fu, Jianxiong Wang, Tianke Zhang, Haonan Fan, Yingxin Li, Bingyi Li, Xu Wang, Xuanyu Zheng, Bin Wen, Tingting Gao, Wentao Zhang, Jiale Cao
- 链接：[arXiv](https://arxiv.org/abs/2611.15789) · [PDF](https://arxiv.org/pdf/2611.15789) · [HF](https://huggingface.co/papers/2611.15789)

Controllable real-world video generation models can condition on a rendered graybox proxy video, which fixes layout, motion and camera. Coding agents can build such videos by reconstructing a 4D scene in Blender, yet no benchmark checks both these videos and the long, multi-shot scenes behind them. We introduce VibePrevisBench, a benchmark for 4D scene reconstruction: an agent turns a brief into an executable 4D…

## 4. MIRIX-2.0: Multi-Agent Memory System

- 分数：36.0  ·  HF 赞：48  ·  来源：huggingface
- 兴趣命中：agent, memory, benchmark, spec, retrieval
- 作者：Wei-Chieh Huang, Weizhi Zhang, Jiayan Nan, Peng Xia, Yu Wang
- 链接：[arXiv](https://arxiv.org/abs/2611.12068) · [PDF](https://arxiv.org/pdf/2611.12068) · [HF](https://huggingface.co/papers/2611.12068)

Long-term memory lets LLM agents personalize, stay consistent, and reuse what worked before. Parametric memories need training, consolidation can lose details for good, and keeping every record leaves a growing store to search. We present MIRIX-2.0, a multi-agent memory system designed to be practical, accurate, and efficient at once. It is the most accurate of the compared systems on four of five QA benchmarks. It…

## 5. K2-Horizon: A Frontier Fleet of Open Source Language Models

- 分数：35.5  ·  HF 赞：31  ·  来源：huggingface + arxiv
- 兴趣命中：agent, reasoning, evaluation, benchmark, language model, coding
- 作者：K2 Team, Zhengzhong Liu, Haonan Li, Xuezhe Ma, Alexander Moreno, Subham Sekhar Sahoo, Rupesh Kumar Srivastava, Mikhail Yurochkin, Hadi Abdine, Yash Akhauri, Adharsh Babu, David Bellamy, Jalaj Bhandari, Dani Bouch, Wail Bouhedja, Weili Cao, Ahmad Chamma, Po-Chun Chang, Junlin Chen, Lingjie Chen, Zhoujun Cheng, Kyle Chickering, Ryandito Diandaru, Evan Dufraisse, Chaitanya Dwivedi, Bilal El Bouardi, Desai Fan, Richard Fan, Chengqian Gao, Rifo Ahmad Genadi, Jonathan Geuter, Charles Guille-Escuret, Willis Guo, Dhawal Gupta, Seungwook Han, Tingxu Han, Shibo Hao, Besher Hassan, Guowei He, Ming Shan Hee, Joel Hestness, Yu Huang, Yuan Huang, Haolong Jia, Linghao Jin, Junu Kim, Lingjing Kong, Nurkhan Laiyk, Andrej Leban, Liqun Ma, John Maggs, Amr Mohamed, Mukhesh Narra, Omkar Pangarkar, Aldo Pareja, Khiem Pham, Varad Pimpalkhute, Nikhil Ranjan, Elizaveta Rebrova, Hector Ren, Shaurya Rohatgi, Guokan Shang, Jianshu She, Chufan Shi, Aaryamonvikram Singh, Daria Soboleva, Kartik Sreenivasan, Suqi Sun, Yuekai Sun, Bowen Tan, Liping Tang, Shengkun Tang, Muzi Tao, Mallikarjuna Tupakula, Micah Villmow, Hongyi Wang, Huijuan Wang, Renxi Wang, Yongxin Wang, Yuqi Wang, Zhenting Wang, Shicheng Wen, Yingquan Wu, Anze Xie, Andrew Xing, Matthew Yang, Shuanghai Yu, Kerem Zaman, Zenan Zhai, Hongli Zhan, Xuezhou Zhang, Anshun Asher Zheng, Zhe Zhou, Richard Zhuang, Eric P. Xing
- 链接：[arXiv](https://arxiv.org/abs/2611.21003) · [PDF](https://arxiv.org/pdf/2611.21003) · [HF](https://huggingface.co/papers/2611.21003)

We present K2-Horizon, a fleet of six fully open language models, from a 0.9B dense model to a 375B-A23B MoE, built for general-purpose reasoning and agentic work across math and science, software engineering, deep research, office automation, and beyond. The models lead or are competitive with strong open models of their size on agentic and coding benchmarks. On the modeling side, to strengthen reasoning, we…

## 6. Rethinking in Spikes: Mitigating Hallucinations in MDLMs with Step-Aware Decoding

- 分数：34.0  ·  HF 赞：36  ·  来源：huggingface
- 兴趣命中：reasoning, benchmark, language model, coding
- 作者：Zhongxing Xu, Zhonghua Wang, Zhe Qian, Shiyan Su, Ming Hu, Xiaocheng Zou, Wei Feng, Mingquan Lin, Yuyin Zhou, Yifan Peng, Hamid Rezatofighi, Zongyuan Ge
- 链接：[arXiv](https://arxiv.org/abs/2611.12901) · [PDF](https://arxiv.org/pdf/2611.12901) · [HF](https://huggingface.co/papers/2611.12901)

Recent advancements in multimodal diffusion language models (MDLMs) have exhibited strong global modeling capabilities through iterative refinement. We observe that mask uncertainty follows an overall downward trend during iterative denoising, while a few denoising steps exhibit localized entropy spikes closely associated with hallucinations. We argue that anomalous steps can be identified by measuring the entropy…

## 7. MMFlash: Faster Speculative Decoding for Vision-Language Models

- 分数：33.5  ·  HF 赞：35  ·  来源：huggingface
- 兴趣命中：benchmark, language model, coding, spec
- 作者：Sicheng Feng, Zigeng Chen, Song Wang, Gongfan Fang, Xinchao Wang
- 链接：[arXiv](https://arxiv.org/abs/2611.18482) · [PDF](https://arxiv.org/pdf/2611.18482) · [HF](https://huggingface.co/papers/2611.18482)

Speculative decoding accelerates generation by letting a lightweight drafter propose tokens for parallel verification by a target model. Diffusion drafters such as DFlash propose an entire token block in a single forward pass, but mainly focus on text-only tasks, leaving multimodal drafting underexplored. To study this setting, we first introduce a metric of token-level visual dependence based on the KL divergence…

## 8. V-JEPA-LM: Video-Language Models That Read Dynamics Beyond Static, Text-Aligned Representations

- 分数：25.5  ·  HF 赞：27  ·  来源：huggingface
- 兴趣命中：benchmark, language model
- 作者：Keuntae Kim, Dongjun Kim, Yong Suk Choi
- 链接：[arXiv](https://arxiv.org/abs/2611.17831) · [PDF](https://arxiv.org/pdf/2611.17831) · [HF](https://huggingface.co/papers/2611.17831)

World-model video encoders such as V-JEPA learn how scenes change (direction, speed, order, state) from video alone. To answer questions, they are joined to a language model trained on captions and question-answer pairs. But each caption or question names only a few attributes of a clip, so the model learns to retrieve those attributes rather than to read the clip, and the dynamics the encoder carries go unused: on…

## 9. G-CAST: Governed Continual Self-Training for E-Commerce Agents under Evolving Demands

- 分数：25.0  ·  HF 赞：18  ·  来源：huggingface
- 兴趣命中：agent, evaluation, language model, large language
- 作者：Yuechun Yu, Wenzheng Kong, Xiaofeng Mao, Jin Zhang
- 链接：[arXiv](https://arxiv.org/abs/2611.17814) · [PDF](https://arxiv.org/pdf/2611.17814) · [HF](https://huggingface.co/papers/2611.17814)

With the rapid advancement of Large Language Models (LLMs), an increasing number of users are turning to LLM-powered agents for conversational shopping in e-commerce. However, the user needs continue to change as new product categories, procurement scenarios, and feature requests emerge. At the same time, the product's execution harness-including its tools, skills, and operating procedures-continues to evolve to…

## 10. Calpha: Toward Native Biomolecular Intelligence in a General-Purpose Language Model

- 分数：25.0  ·  HF 赞：10  ·  来源：huggingface + arxiv
- 兴趣命中：reasoning, language model, large language, spec
- 作者：Yong Liu, Zhanpeng Shi, Peicong Lin, Zhenyi Zhong, Yizhou Dang, Wendi Wu, Haoling Li, Shuangjia Zheng
- 链接：[arXiv](https://arxiv.org/abs/2611.20986) · [PDF](https://arxiv.org/pdf/2611.20986) · [HF](https://huggingface.co/papers/2611.20986)

Biomolecular foundation models predict the structures of proteins and their complexes accurately, and large language models (LLMs) reason in natural language, but the two remain separate: the abilities of the former are not part of a general-purpose LLM, and the reasoning of the latter does not enter a structure prediction. Calpha aims at one general model that folds proteins and complexes, understands protein…

## 11. Accelerate Bench: Evaluating Agents for Application-Level Program Optimization

- 分数：24.5  ·  HF 赞：9  ·  来源：huggingface + arxiv
- 兴趣命中：agent, benchmark, coding, spec
- 作者：Bowen Liu, Yuhan Li, Nuo Chen, Weile Luo, Miao Peng, Qintong Zhang, Qifan Zhang, Jia Li, Ziqi Gao, Lydell Huang
- 链接：[arXiv](https://arxiv.org/abs/2611.20882) · [PDF](https://arxiv.org/pdf/2611.20882) · [HF](https://huggingface.co/papers/2611.20882)

Application optimization requires coding agents to discover useful changes and coordinate them across a complete program while preserving the required computation. We introduce Accelerate Bench, a benchmark of 32 CPU optimization tasks adapted from scientific applications and supercomputing competitions. Each task provides a working program and specifies the workload, correctness requirements, timing boundaries, and…

## 12. AllocFlow: End-to-End Portfolio Trading Action Generation from Raw Market Data

- 分数：24.0  ·  HF 赞：28  ·  来源：huggingface
- 兴趣命中：reinforcement learning
- 作者：Annan Wang, Yuchen Xie, Yu Cen, Leon Liangyu Chen, Qianyu Julie Zhu, Xin Li, Tianyi Wei, Weisi Lin
- 链接：[arXiv](https://arxiv.org/abs/2611.19937) · [PDF](https://arxiv.org/pdf/2611.19937) · [HF](https://huggingface.co/papers/2611.19937)

Real-world portfolio management requires converting noisy market observations into coordinated, simultaneous allocations across multiple assets under shared capital constraints. Advances in forecasting models and alpha discovery help identify opportunities. However, traditional pipelines often decouple signal forecasting from portfolio construction, potentially misaligning learning with allocation and execution…

## 13. Mobile AI Factory: Building Specialized Language Models for Your Mobile Device

- 分数：24.0  ·  HF 赞：20  ·  来源：huggingface
- 兴趣命中：agent, language model, spec
- 作者：Evan Li, Krishna Deshpande, Wen Cheng, Shyamnath Gollakota
- 链接：[arXiv](https://arxiv.org/abs/2611.13509) · [PDF](https://arxiv.org/pdf/2611.13509) · [HF](https://huggingface.co/papers/2611.13509)

Small language models (SLMs) running on mobile devices can keep user data private and work without connectivity. But they perform well only when fine-tuned for the target task and sized for the target device, a process that today requires repeated expert tuning. We present {\it Mobile AI Factory}, an agentic system that builds a fine-tuned, quantized SLM for a given task and phone. Given a task specification and a…

## 14. MEM-SQL: Memory-Empowered Text-to-SQL

- 分数：22.5  ·  HF 赞：17  ·  来源：huggingface
- 兴趣命中：memory, benchmark, language model
- 作者：Xiaoqi Wang, Wenqi Pei, Shizheng Hou, Yilai Liu, Han Chen, Boyan Li, Yuyu Luo, Hongyang Du
- 链接：[arXiv](https://arxiv.org/abs/2611.18338) · [PDF](https://arxiv.org/pdf/2611.18338) · [HF](https://huggingface.co/papers/2611.18338)

Text-to-SQL systems translate natural language questions into SQL queries over increasingly complex databases. However, widely used benchmarks evaluate questions independently, overlooking settings where earlier queries over the same database can supply joins or calculations for a new question. We introduce HARE (History-AwaRe Text-to-SQL BEnchmark) to measure the accuracy and cost of adapting historical SQL. HARE…

## 15. WebArena-Pro: A Heterogeneous, Multimodal, Reproducible Benchmark for Web Agents

- 分数：22.0  ·  HF 赞：12  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark, language model, large language
- 作者：Imene Kerboua, Fatemeh Pesaran Zadeh, Xing Han Lù, Weijian Qi, Alexander Miller, Junyi Song, Yunjia Tian, Dongjin Kang, Seyeon Choi, Marzia Nouri, Ewen Gueguen, Matteo Boglioni, Fengyuan Liu, Zeyi Liao, Mengqi Yuan, Yue Li, Alexandre Lacoste, Alexandre Drouin, Spandana Gella, Huan Sun, Gunhee Kim, Siva Reddy
- 链接：[arXiv](https://arxiv.org/abs/2611.17955) · [PDF](https://arxiv.org/pdf/2611.17955) · [HF](https://huggingface.co/papers/2611.17955)

Web agents powered by large language and vision-language models are increasingly applied to realistic browser work that spans heterogeneous applications, multimodal content, and stateful workflows. However, existing reproducible web-agent benchmarks cover only a small number of web applications drawn from a few software categories, and restrict modality to text and vision. Live benchmarks broaden site coverage but…

## 16. Interpreting Coding Agents Through Their Behavioral Trajectories

- 分数：21.5  ·  HF 赞：11  ·  来源：huggingface
- 兴趣命中：agent, reasoning, benchmark, coding
- 作者：Ibragim Badertdinov, Alexander Golubev
- 链接：[arXiv](https://arxiv.org/abs/2611.17440) · [PDF](https://arxiv.org/pdf/2611.17440) · [HF](https://huggingface.co/papers/2611.17440)

Standard coding-agent benchmarks primarily evaluate binary task success, treating execution as a black box and obscuring the behaviors that produce those outcomes. We analyze a large corpus of 143,209 execution trajectories from 125 agent configurations spanning 117 unique models. To enable comparisons across heterogeneous agent interfaces, we develop a rule-based parser that maps raw execution traces to high-level…

## 17. Evidence-Governed Adoption of Self-Generated Updates in Autonomous AI Agents

- 分数：21.5  ·  HF 赞：11  ·  来源：huggingface
- 兴趣命中：agent, evaluation, spec, planning
- 作者：Subodh Lonkar
- 链接：[arXiv](https://arxiv.org/abs/2611.16378) · [PDF](https://arxiv.org/pdf/2611.16378) · [HF](https://huggingface.co/papers/2611.16378)

Autonomous agents modify prompts, memories, tools, workflows, and policies using interaction histories. Yet a plausible modification is not necessarily suitable for persistent adoption: candidate selection is adaptive, evaluators may be imperfect, and local gains can hide degradation against an earlier baseline. We introduce Evidence-Governed Evolution (EGE), a framework for governing adoption of self-generated…

## 18. SPILLWAY: Separating Target Admission from Sanitization to Defend Tool-Using Agents against Prompt Injection

- 分数：21.0  ·  HF 赞：18  ·  来源：huggingface
- 兴趣命中：agent, language model
- 作者：Woosang Lim, Yeseul Chang, Jaewoo Lee
- 链接：[arXiv](https://arxiv.org/abs/2611.07222) · [PDF](https://arxiv.org/pdf/2611.07222) · [HF](https://huggingface.co/papers/2611.07222)

Tool-using agents act on email, files, and payments, so an instruction hidden in a web page or a shared document can make an agent send data or money to an attacker. Many runtime defenses put a language model on the decision that lets an action through, so the decision depends on a model that may read the attacker's text and adds model calls to every step. Provenance defenses keep the model off the final check but…

## 19. AI Reviews Are Biased Towards the Appendix

- 分数：21.0  ·  HF 赞：10  ·  来源：huggingface
- 兴趣命中：agent, language model, large language, coding
- 作者：Saptarshi Ghosh, Mohammad Saim, Tianyu Jiang
- 链接：[arXiv](https://arxiv.org/abs/2611.17811) · [PDF](https://arxiv.org/pdf/2611.17811) · [HF](https://huggingface.co/papers/2611.17811)

Large language models (LLMs) are increasingly used by reviewers to highlight weaknesses during the reviewing process, and their outputs often shape the reviews that humans submit. Prior work studies how LLM reviews align with human ones, yet we know little about which parts of a paper these models actually criticize. In this work, we investigate 2,000 papers from ACL, EMNLP, COLM, and ICLR, and show that the latest…

## 20. Loopback Transformer: Towards a Unified View of Residual Looped Transformers

- 分数：20.5  ·  HF 赞：21  ·  来源：huggingface
- 兴趣命中：memory
- 作者：Xuan Ouyang, Zefan Cai, Chenlong Zhang, Cheng Luo, Ke Wan, Junjie Hu
- 链接：[arXiv](https://arxiv.org/abs/2611.07226) · [PDF](https://arxiv.org/pdf/2611.07226) · [HF](https://huggingface.co/papers/2611.07226)

Looped Transformers reduce parameter count by repeatedly applying shared blocks, but parameter sharing alone does not determine how the results of repeated computation are reused. We take the depth-memory view of residual connections and analyze which representation is stored after each block application and how later reads weight it. A full block output contains both its input and its new update, so weighting that…

## 21. JFinBench: A Continuously Refreshable Japanese Financial Benchmark from the Latest Certification Exams

- 分数：20.5  ·  HF 赞：9  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark, language model, large language, coding, spec, planning
- 作者：Issa Sugiura, Taro Makino, Takashi Ishida
- 链接：[arXiv](https://arxiv.org/abs/2611.18130) · [PDF](https://arxiv.org/pdf/2611.18130) · [HF](https://huggingface.co/papers/2611.18130)

Large language models (LLMs) are increasingly applied to finance, creating a need for benchmarks that evaluate their capabilities across financial systems with different regulations and practices. However, existing financial benchmarks provide limited coverage of country-specific financial systems, and they are difficult to keep up to date as released questions leak into training data. We introduce JFinBench, a…

## 22. MovieRoll: A Systematic Framework for Rolling Out Long-Form Videos

- 分数：20.0  ·  HF 赞：4  ·  来源：huggingface + arxiv
- 兴趣命中：memory, evaluation, coding
- 作者：Yunyang Ge, Weijie Kong, Ryan Xu, Yue Wu, Qi Tian, Jiangfeng Xiong, Bin Lin, Mingzhe Zheng, Shenghai Yuan, Zheyuan Liu, Jianwei Zhang, Li Yuan
- 链接：[arXiv](https://arxiv.org/abs/2611.21339) · [PDF](https://arxiv.org/pdf/2611.21339) · [HF](https://huggingface.co/papers/2611.21339)

Streaming video generation must sustain quality beyond the training horizon while handling self-generated history and growing cache costs. To address these challenges, we present MovieRoll, a base-to-distilled framework that connects streaming fine-tuning, long-rollout distillation, and long-horizon inference. We first establish a robust multi-step base through Window-wise Teacher Forcing (WinTF), which jointly…

## 23. DySENSE: Dynamic Spatiotemporal ENergy Synthesis and Emulation with Satellite Imagery

- 分数：19.5  ·  HF 赞：23  ·  来源：huggingface
- 兴趣命中：-
- 作者：Kailai Sun, Zijie Gao, Mingyi He, Can Rong, Alok Prakash, Baoshen Guo, Shenhao Wang, Jinhua Zhao
- 链接：[arXiv](https://arxiv.org/abs/2611.17878) · [PDF](https://arxiv.org/pdf/2611.17878) · [HF](https://huggingface.co/papers/2611.17878)

Cities account for over two-thirds of the world's energy and more than 70% of global carbon dioxide emissions. City energy is essential for achieving the 2050 net-zero target and the UN's Sustainable Development Goals 7 and 11. Although existing studies have made progress, they are limited by data and methodological gaps. Existing studies are largely predictive for existing cities rather than generative for future…

## 24. Continual-ARC: Measuring Skill Acquisition over a Working Lifetime

- 分数：19.0  ·  HF 赞：10  ·  来源：huggingface
- 兴趣命中：agent, memory, benchmark
- 作者：Daniel Lenton, Yusha Arif, Haris Mahmood
- 链接：[arXiv](https://arxiv.org/abs/2611.14505) · [PDF](https://arxiv.org/pdf/2611.14505) · [HF](https://huggingface.co/papers/2611.14505)

Agent harnesses have emerged as a promising mechanism for continual learning, alongside test-time parametric learning. However, the current benchmarks have several limitations: they generally focus on a single applied domain, serve each instance only once, and assume a single family of learner, so memory-based and weight-based systems are rarely compared on the same scale. We propose Continual-ARC, a lifelong stream…

## 25. PaperCritic: Training AI Reviewers to Assess the Soundness of Papers

- 分数：18.5  ·  HF 赞：17  ·  来源：huggingface
- 兴趣命中：reinforcement learning
- 作者：Hyun Ryu, Ji Yong Cho, Eunho Yang, Moontae Lee, June Yong Yang, Sean Welleck, Carolyn Rose
- 链接：[arXiv](https://arxiv.org/abs/2611.17834) · [PDF](https://arxiv.org/pdf/2611.17834) · [HF](https://huggingface.co/papers/2611.17834)

As AI conference submissions grow rapidly, AI reviewers are being considered as an alternative. However, simply imitating human reviewing is problematic because reviewing serves multiple purposes, including evaluating papers' soundness, interestingness, and clarity, the last two of which are subjective. In this work, we focus solely on evaluating soundness, the most important and objective criterion, and define the…

## 26. GH-AWTrace: A Large-Scale Dataset of GitHub Agentic Workflow Execution Logs

- 分数：18.0  ·  HF 赞：12  ·  来源：huggingface
- 兴趣命中：agent, tool use
- 作者：Jasem Khelifi, Hao Li, Ali Ouni, Mohammed Sayagh, Mohamed Aymen Saied
- 链接：[arXiv](https://arxiv.org/abs/2611.06866) · [PDF](https://arxiv.org/pdf/2611.06866) · [HF](https://huggingface.co/papers/2611.06866)

Agentic workflows enable AI agents to perform recurring repository tasks on schedules or in response to repository events. Existing studies examine workflow definitions and outputs, but provide limited evidence of what happens during execution. We present GH-AWTrace, a dataset linking 25,014 verified GitHub Agentic Workflows across 5,051 repositories to 4,112,526 run records and 562,877 nonempty execution log…

## 27. Aligning AI Teams

- 分数：18.0  ·  HF 赞：12  ·  来源：huggingface
- 兴趣命中：agent, spec
- 作者：Siddarth Srinivasan, Morgan Jane Matthews, Jascha Sohl-Dickstein, Erik Jones
- 链接：[arXiv](https://arxiv.org/abs/2611.17820) · [PDF](https://arxiv.org/pdf/2611.17820) · [HF](https://huggingface.co/papers/2611.17820)

Previous work has shown that alignment training on individual LLM agents can fail to transfer to multi-agent settings. We investigate the underlying mechanisms for this failure, and explore interventions to preserve alignment transfer to multi-agent LLM teams. We focus on two software-engineering tasks (sepsis triage, a news recommender) and ten consulting-proposal generation tasks. We present four findings: (1) The…

## 28. CANTraj: Recovering Vehicle Trajectories from CAN Signals in Naturalistic Driving

- 分数：18.0  ·  HF 赞：12  ·  来源：huggingface
- 兴趣命中：evaluation, benchmark
- 作者：Yuhang Wang, Jingxin Yang, Chuheng Wei, Suyang Chen, Haozhuang Chi, Hao Zhou
- 链接：[arXiv](https://arxiv.org/abs/2611.18442) · [PDF](https://arxiv.org/pdf/2611.18442) · [HF](https://huggingface.co/papers/2611.18442)

Open driving releases and usage-based insurance programs often claim to prevent privacy breaches by omitting GPS records when sharing or collecting vehicle data. However, removing GPS coordinates from driving logs does not erase the location information carried by vehicle signals. While prior route-inference attacks have demonstrated that speed, steering, and driving events can be matched to road networks to…

## 29. JVT: Just Video Transformer makes pixel-space video diffusion simple

- 分数：17.5  ·  HF 赞：15  ·  来源：huggingface
- 兴趣命中：spec
- 作者：Jianjun Zhou, Hua Geng, Haoyu Guo
- 链接：[arXiv](https://arxiv.org/abs/2611.18549) · [PDF](https://arxiv.org/pdf/2611.18549) · [HF](https://huggingface.co/papers/2611.18549)

Direct diffusion modeling of high-dimensional raw video data is challenging, and existing pixel-space methods often rely on specialized architectures. We introduce JVT (Just Video Transformer), a simple large-patch DiT-style Transformer for pixel-space video diffusion, without a pretrained autoencoder, auxiliary detailers, cascaded stages, or U-Net-style skip connections. We systematically examine video patch…

## 30. MemInStream: Memorizing or Merely Recognizing? Rethinking Streaming Video Memory Evaluation

- 分数：17.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：memory, evaluation, benchmark, retrieval
- 作者：Zhenqi He, Dunyuan Xu, Yang Bo, Kien T. Pham, Yanghao Wang, Shuhan Li, Xintong Guo, Yuyang He, Fang Liu, Huankang Guan, Jingyan Chen, Rui Liu, Long Chen
- 链接：[arXiv](https://arxiv.org/abs/2611.15640) · [PDF](https://arxiv.org/pdf/2611.15640) · [HF](https://huggingface.co/papers/2611.15640)

Streaming video understanding aims to continuously process incoming visual observations, making the retention and retrieval of relevant information increasingly important as the video history grows. Although existing benchmarks include memory-related questions, question-answering accuracy alone does not reliably measure memory capabilities. Incorrect predictions may arise from failures in visual understanding rather…

## 31. Reducing Batch Makespan for LLM Agent Workloads through Inference-Environment Coordination

- 分数：17.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：agent, memory, evaluation, benchmark
- 作者：Wei Feng, Meiling Chen, Boxiao Chen, Lu Liu, Bin Zi, Libin Ye, Xingyu Lu, Lei Xu, Jun Zhou
- 链接：[arXiv](https://arxiv.org/abs/2611.16661) · [PDF](https://arxiv.org/pdf/2611.16661) · [HF](https://huggingface.co/papers/2611.16661)

Efficient batch execution of agent tasks is critical to LLM training and development workflows, including benchmark evaluation, synthetic-data generation, and RL rollouts. Since these tasks alternate between LLM inference and environment interaction, we present coordinated optimizations to reduce batch makespan, the time required to complete all tasks in a batch. For hybrid LLMs, a workload-based resource model…

## 32. Disen-Forcing: Disentangling Semantic Anchoring from Motion for Autoregressive Video Diffusion

- 分数：16.5  ·  HF 赞：9  ·  来源：huggingface
- 兴趣命中：benchmark, spec
- 作者：Zhengyang Yu, Akio Hayakawa, Masato Ishii, Qingtao Yu, Xuesong Li, Takashi Shibuya, Yuki Mitsufuji, Jing Zhang
- 链接：[arXiv](https://arxiv.org/abs/2611.02822) · [PDF](https://arxiv.org/pdf/2611.02822) · [HF](https://huggingface.co/papers/2611.02822)

Autoregressive video diffusion models (AR-VDMs) enable real-time, long-horizon video generation but degrade rapidly once the inference horizon outruns the training horizon, due to compounding exposure bias. To stabilize long rollouts, recent methods heuristically adopt frame sink, keeping initial frames as a persistent model context, inspired by attention sinks in LLMs. We revisit this design and find that the…

## 33. ScaleVLA: Scaling Vision-Language-Action Models to 552 Billion Parameters

- 分数：16.5  ·  HF 赞：5  ·  来源：huggingface
- 兴趣命中：agent, reasoning, language model
- 作者：Ruixi Yu, Dairu Liu, Xuchuan Chen, Zekun Qi, Zekai Li, Zhuo Cao, Luyang Niu, Yingsheng Zhang, Sikai Liang, Ke Fan, He Wang, Li Yi
- 链接：[arXiv](https://arxiv.org/abs/2611.21607) · [PDF](https://arxiv.org/pdf/2611.21607) · [HF](https://huggingface.co/papers/2611.21607)

Frontier Vision-Language Models (VLMs) such as GPT-6 Astra have demonstrated remarkable capabilities in robot control, suggesting that broad pretraining provides knowledge valuable for physical action. Yet most Vision-Language-Action (VLA) policies still rely on much smaller VLM backbones, leaving this potential largely untapped. We ask whether frontier-scale representations can provide a stronger foundation for…

## 34. LoopFill: Pipelined Multi-Token Speculative Decoding for Looped Transformers

- 分数：15.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：benchmark, coding, spec
- 作者：Siqi Zhu, Suozhi Huang, Yi Zhao, Jiaxuan You
- 链接：[arXiv](https://arxiv.org/abs/2611.19649) · [PDF](https://arxiv.org/pdf/2611.19649) · [HF](https://huggingface.co/papers/2611.19649)

Looped Transformers improve parameter efficiency by repeatedly applying the same Transformer layers. During autoregressive decoding, however, generating each token requires several sequential passes through these layers, leading to high decoding latency. Pipelined self-speculative methods use shallow-loop predictions to process tokens at different loops in the same batch, but each token must reach the drafting depth…

## 35. Emergent Biological Capabilities in a Foundation Model for Molecular Interactions

- 分数：15.0  ·  HF 赞：10  ·  来源：huggingface
- 兴趣命中：spec
- 作者：Adi Mashiach
- 链接：[arXiv](https://arxiv.org/abs/2611.14504) · [PDF](https://arxiv.org/pdf/2611.14504) · [HF](https://huggingface.co/papers/2611.14504)

Foundation models trained on large unlabeled corpora develop emergent capabilities, tasks that go beyond the training objective. We extend this paradigm to multimodal biology with Bonbon, a foundation model for molecular interactions trained on approximately 3.2 trillion tokens of paired protein-ligand sequences. From a single representation space, Bonbon exhibits three zero-shot emergent capabilities at…

## 36. Do Underwater Image Quality Metrics Agree with Human Perception? A Benchmark with Human Choices, Simple Edits and Generative Drift

- 分数：15.0  ·  HF 赞：10  ·  来源：huggingface
- 兴趣命中：benchmark
- 作者：Rishii Kumar Singh, Abhinav Rajput, Dinesh Kumar Vishwakarma
- 链接：[arXiv](https://arxiv.org/abs/2611.18429) · [PDF](https://arxiv.org/pdf/2611.18429) · [HF](https://huggingface.co/papers/2611.18429)

Underwater image enhancement is challenging to evaluate due to the lack of clean reference images, so researchers rely on no-reference image quality assessment (NR-IQA) metrics. However, it remains unclear whether these metrics agree with human judgments. We evaluate 73 handcrafted underwater, learned underwater, vision-language and general-purpose metrics against human preferences on five references: four published…

## 37. VoxMel TTS Technical Report

- 分数：15.0  ·  HF 赞：6  ·  来源：huggingface
- 兴趣命中：evaluation, spec
- 作者：Wenhao Guan, Jiaxin Ye, Haitao Li, Yifan Duan, Junxi Liu, Wangjin Zhou, Lin Li, Qingyang Hong, Xie Chen
- 链接：[arXiv](https://arxiv.org/abs/2611.20254) · [PDF](https://arxiv.org/pdf/2611.20254) · [HF](https://huggingface.co/papers/2611.20254)

Continuous autoregressive TTS relies on an acoustic target that enables stable next-latent modeling while preserving fine-grained acoustic details. While existing approaches employ learned compressed representations (e.g., continuous VAE latents) to render prediction tractable, they rely on complex neural encoders that often cap generation fidelity. Conversely, training-free targets like mel-spectrograms eliminate…

## 38. EvenVLM: A Text and Multimodal Dataset for the Even Language with Vision-Language Fine-Tuning

- 分数：15.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：evaluation, benchmark, spec
- 作者：Daniil Makovetskii, Ivan Bondarenko
- 链接：[arXiv](https://arxiv.org/abs/2611.16500) · [PDF](https://arxiv.org/pdf/2611.16500) · [HF](https://huggingface.co/papers/2611.16500)

We present EvenVLM, the first text and multimodal (VQA) dataset for Even (Lamut), an endangered Northern Tungusic language spoken by approximately 6,800 people in Siberia. Our dataset comprises 50,521 structured Even-Russian entries extracted from dictionary and phrasebook sources via GPT-4o Mini-based parsing, from which we synthetically generate 107,543 training examples spanning translation, grammar, reading…

## 39. eDMD: Endpoint Distribution Matching for Few-Step Diffusion Distillation

- 分数：14.5  ·  HF 赞：13  ·  来源：huggingface
- 兴趣命中：-
- 作者：Tong Zhao, Xianfang Zeng, Yucheng Han, Ruoyu Wang, Mingkun Lei, Gang Yu, Chi Zhang
- 链接：[arXiv](https://arxiv.org/abs/2611.17194) · [PDF](https://arxiv.org/pdf/2611.17194) · [HF](https://huggingface.co/papers/2611.17194)

Distribution matching distillation (DMD) has emerged as a leading paradigm for distilling diffusion models into few-step students, where an auxiliary fake score model tracks the student's distribution and the discrepancy between the teacher and fake predictions drives the student toward the teacher. In multi-step distillation, although only the student's final output is delivered, existing methods train the fake…

## 40. DominoBench: Evaluating Multi-Step Physical Reasoning from Still Images

- 分数：14.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：reasoning, benchmark, language model
- 作者：Emilio Ferrara
- 链接：[arXiv](https://arxiv.org/abs/2611.20385) · [PDF](https://arxiv.org/pdf/2611.20385) · [HF](https://huggingface.co/papers/2611.20385)

Can a vision-language model look at a picture of a chain reaction and tell what will happen? Recent multimodal models describe scenes fluently and solve textbook physics problems, which suggests they should also predict how a scene of ramps, ledges, pendulums, seesaws and dominoes plays out once a ball is pushed. We tested this claim on 30 models from 10 families and reached a clear conclusion: unaided, no model…

## 41. Re-Search: Dissecting LLM Ideation Through a Two-Player Questioning Game

- 分数：14.0  ·  HF 赞：8  ·  来源：huggingface
- 兴趣命中：evaluation
- 作者：Muhan Gao, Hangxiao Zhu, Xinqi Su, Yu Zhang, Daniel Khashabi, Kuan-Hao Huang
- 链接：[arXiv](https://arxiv.org/abs/2611.14487) · [PDF](https://arxiv.org/pdf/2611.14487) · [HF](https://huggingface.co/papers/2611.14487)

Research ideation is iterative: researchers refine their ideas step by step based on feedback. Yet existing evaluations obscure this search process, making it difficult to understand how LLMs explore the space of research ideas and what limits their progress. We introduce Re-Search, which adapts the format of Twenty Questions to research ideation: given only the research problem of a published paper, a model must…

## 42. Parsed, Plausible, Wrong: Output Format Controls Silent Errors in Small-Model Semantic Parsing

- 分数：14.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：benchmark, coding
- 作者：Umar Ahmed, Maxim Dunaev, Mohammad Nour Al Awad, Sergey Ivanov, Ivan Khodnenko
- 链接：[arXiv](https://arxiv.org/abs/2611.17169) · [PDF](https://arxiv.org/pdf/2611.17169) · [HF](https://huggingface.co/papers/2611.17169)

A small fine-tuned parser that emits a well-formed but wrong tree fails silently: nothing downstream can tell. We ask whether the output format, a free design choice, controls how often this happens. On the PIZZA ordering benchmark we fine-tune two sub-billion models (Qwen3.5-0.8B and LFM2.5-350M) with LoRA on six lossless encodings of the same target tree, from 44.3 down to 10.9 tokens per order, including two…

## 43. Reflection Anchors for Propagation-Aware Visual Retention in Long-Chain Multimodal Reasoning

- 分数：14.0  ·  HF 赞：0  ·  来源：huggingface
- 兴趣命中：reasoning, benchmark, language model
- 作者：Xuan Gong, Hanbo Huang, Hao Zheng, Yiran Zhang, Wenbin Dai, Weishu Zhao, Shiyu Liang
- 链接：[arXiv](https://arxiv.org/abs/2605.09614) · [PDF](https://arxiv.org/pdf/2605.09614) · [HF](https://huggingface.co/papers/2605.09614)

Long chain-of-thought (CoT) reasoning improves large vision--language models, but visual information often fades during generation, limiting long-horizon multimodal reasoning. Existing methods either re-inject vision at inference or train policies for stronger grounding, but where to intervene relies on perception heuristics rather than principled gain analysis, and how local visual influence propagates remains…

## 44. eDIAR: Training-Free Open-Speaker Streaming Diarization for Long Meetings and Large Archives via e-means

- 分数：13.5  ·  HF 赞：11  ·  来源：huggingface
- 兴趣命中：-
- 作者：Kyudan Jung, Jihwan Kim, Minwoo Lee, Eunji Shin, Jaegul Choo
- 链接：[arXiv](https://arxiv.org/abs/2611.18529) · [PDF](https://arxiv.org/pdf/2611.18529) · [HF](https://huggingface.co/papers/2611.18529)

Meetings last up to an hour, and nobody knows in advance how many people will speak. Neural diarizers with a fixed number of output slots, such as Streaming Sortformer and Nemotron-3, are accurate and run online, but they cannot name more speakers than they have slots. We remove this limit without retraining. The slot head keeps deciding who is active and when speech overlaps, and speaker embeddings are clustered…

## 45. LuthorSQL: A One-Pass Text-to-SQL Model as System 1 for a Slower LLM Agent

- 分数：13.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：agent, benchmark
- 作者：Ibrahim Memon, Armin Karamzade, M. Hanif Jhaveri, Roy Fox
- 链接：[arXiv](https://arxiv.org/abs/2611.17780) · [PDF](https://arxiv.org/pdf/2611.17780) · [HF](https://huggingface.co/papers/2611.17780)

Frontier LLM agents that query databases with tools are among the most accurate text-to-SQL systems, but per-query calls to a hosted model are slow, costly, and expose sensitive organizational queries to external APIs. For example, a Claude Opus 5.5 agent serving 10,000 queries a day costs over $70,000 a year at list price. To what extent can local hardware already owned by an organization offload this burden…

## 46. HALO: Human-Aligned Data Collection for WhoLe-body MObile Manipulation

- 分数：13.0  ·  HF 赞：10  ·  来源：huggingface
- 兴趣命中：-
- 作者：Shuai Yang, Fangyi Xu, Yishu Shen, Kecheng Zheng, Yinghao Xu
- 链接：[arXiv](https://arxiv.org/abs/2611.16439) · [PDF](https://arxiv.org/pdf/2611.16439) · [HF](https://huggingface.co/papers/2611.16439)

Learning whole-body mobile manipulation requires demonstrations that coordinate bimanual actions with locomotion across extended workspaces. However, existing interfaces trade off direct robot control, perception and action alignment, and natural operator mobility, making such demonstrations difficult to collect. We introduce HALO, a human-aligned data collection system for whole-body mobile manipulation. The system…

## 47. Iris-Z: Scaling One Generative Model Past Specialist Geometry Models

- 分数：13.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：benchmark, spec
- 作者：Alejandro Cañada, Chema Garabito
- 链接：[arXiv](https://arxiv.org/abs/2611.16010) · [PDF](https://arxiv.org/pdf/2611.16010) · [HF](https://huggingface.co/papers/2611.16010)

Language moved from many task-specific models to one unified model: a single generative model with a single generative training task that handles all of them within the same backbone, and keeps improving with data, parameters and compute. We believe the bitter lesson applies just as much to computer vision, 3D and spatial understanding, in the end to visual intelligence: the effort should go into general…

## 48. UMM-JEPA: Generative Pretraining via Masked Next-Scale Representation Prediction for Unified Multimodal Models

- 分数：12.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：benchmark, spec
- 作者：Yucheng Zhou, Yunjia Xi, Di Yin, Jianbing Shen
- 链接：[arXiv](https://arxiv.org/abs/2611.18668) · [PDF](https://arxiv.org/pdf/2611.18668) · [HF](https://huggingface.co/papers/2611.18668)

Unified multimodal models can support both visual understanding and generation, yet generative training does not necessarily improve understanding. We argue that this limitation may arise from a mismatch between the representation targeted by generation and the perceptual representation used for understanding. Conventional generation objectives primarily optimize synthesis-oriented spaces such as discrete visual…

## 49. Alloy: A Multi-Material Physics Engine for Robot Learning

- 分数：12.0  ·  HF 赞：0  ·  来源：huggingface
- 兴趣命中：agent, coding
- 作者：Pranay Gupta, Deepanshu Rohilla
- 链接：[arXiv](https://arxiv.org/abs/2611.16312) · [PDF](https://arxiv.org/pdf/2611.16312) · [HF](https://huggingface.co/papers/2611.16312)

Robots handle much more than rigid objects: towels, cables, water, sand. The simulators used to train robots at scale are strongest on rigid bodies, and adding another material usually means a second engine and hand-written glue between the two. We present Alloy, an open-source physics engine for robot learning in which rigid robots, cloth, cables, liquids, granular material and soft bodies share one scene. Each…

## 50. Restoring Diversity in Distilled Image and Video Generators by Probing Activations

- 分数：11.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：benchmark
- 作者：Furkan Horoz, Ozgur Kara, Kaan Oktay, Adil Kaan Akan, Atakan Kara, Anand Bhattad, James Matthew Rehg
- 链接：[arXiv](https://arxiv.org/abs/2611.18550) · [PDF](https://arxiv.org/pdf/2611.18550) · [HF](https://huggingface.co/papers/2611.18550)

Distilling diffusion models into few-step student models substantially reduces sampling latency, but induces severe diversity collapse: samples generated from different random seeds show minimal variation. In this work, we investigate the root cause of this failure by probing the internal representations of student models relative to their teachers. We find that distilled students maintain total activation variance…

## 51. Dual Flow: Joint Image-Measurement Interpolation for Inverse Problems

- 分数：11.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：spec
- 作者：Sevket Ege Yesilyurt, Figen S. Oktem
- 链接：[arXiv](https://arxiv.org/abs/2611.05843) · [PDF](https://arxiv.org/pdf/2611.05843) · [HF](https://huggingface.co/papers/2611.05843)

Generative model-based approaches to linear inverse problems typically use the acquired noisy measurement to condition or guide sampling in the image domain. In this work, we introduce Dual Flow, a novel joint-flow model for solving linear inverse problems by jointly estimating the clean image and corresponding noise-free measurement from the observation. Specifically, Dual Flow formulates image reconstruction and…

## 52. OneSteer: Unlocking Steerable General Humanoid Motion Tracking via One-Step Diffusion Whole-Body Control

- 分数：11.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：spec
- 作者：Yifei Huang, Yazhao Yang, Li Weijia, Tianle Shi, Ji Jin, Zhihui Cai, Zihao Liu, Jianzhuang Zhao, Songlin Dong, Xinyuan Chang, Yihong Gong, Dian Shen, Zhiheng Ma
- 链接：[arXiv](https://arxiv.org/abs/2610.41354) · [PDF](https://arxiv.org/pdf/2610.41354) · [HF](https://huggingface.co/papers/2610.41354)

Deployment objectives often specify desired outcomes without providing revised trajectories, while parts of the original reference must still be followed. We present OneSteer, a one-step diffusion whole-body controller that combines general motion tracking with selective test-time steering. To accommodate new objectives, differentiable task costs guide optimization of the generator's input noise with frozen weights,…

## 53. GlyphAtlas: Disentangling Stroke Detail from Layout for Scene Text Synthesis

- 分数：10.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：spec
- 作者：Luozheng Qin, Changhai Zhou, Yiyi Zhou
- 链接：[arXiv](https://arxiv.org/abs/2611.20192) · [PDF](https://arxiv.org/pdf/2611.20192) · [HF](https://huggingface.co/papers/2611.20192)

Scene text synthesis requires stroke-accurate characters rendered in a specified layout, as well as visual coherence with the surrounding scene. To achieve this, existing methods commonly pre-render the target text at its intended locations to form a glyph image that jointly specifies layout and glyph structure. However, this representation ties the resolution of each glyph to its target region, limiting…

## 54. Latent Feedback Is a Compute and Data Amplifier

- 分数：9.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：-
- 作者：Benhao Huang, Chaitanya Dwivedi, Xuezhe Ma, Alexander Moreno, Hector Liu
- 链接：[arXiv](https://arxiv.org/abs/2611.20404) · [PDF](https://arxiv.org/pdf/2611.20404) · [HF](https://huggingface.co/papers/2611.20404)

When high-quality data runs out, a common practice is to train on it for several epochs, but each repeat is worth less than the last. Latent feedback, which feeds each token's top-layer state into the next token's input, is another way to spend that compute, yet it has not been tested against a vanilla Transformer that spends the same compute on more epochs. We run this test across a ladder of model sizes, unique…

## 55. Ego Guidance: Enhancing Robot Policy Learning with Action-Free Human Egocentric Videos

- 分数：9.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：-
- 作者：Lin Long, Tianren Ma, Zhong Chu, Di Wu, Maosong Cao, Qixiang Ye, Junbo Zhao, Shanghang Zhang
- 链接：[arXiv](https://arxiv.org/abs/2611.13685) · [PDF](https://arxiv.org/pdf/2611.13685) · [HF](https://huggingface.co/papers/2611.13685)

In this paper, we investigate how human egocentric videos can benefit robot policy learning without action supervision. Building on a pretrained VLM, we propose Shared Prediction on Action and Representation (SPAR), an MoT architecture in which future visual state prediction can provide independent and complementary learning signals alongside action prediction. We find that representations learned from egocentric…

## 56. BrickFlow: Connectivity-Guided Brick Reconstruction

- 分数：9.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：-
- 作者：Peter Kulits, Cordelia Schmid
- 链接：[arXiv](https://arxiv.org/abs/2611.17321) · [PDF](https://arxiv.org/pdf/2611.17321) · [HF](https://huggingface.co/papers/2611.17321)

Given a set of LEGO parts and an image of an assembled object, our task is to infer the pose of each part to assemble the object. In contrast with traditional 3D reconstruction, doing so requires satisfying discrete physical constraints, which provide structure but render the problem combinatorial and highly sensitive to small pose errors. To learn a prior over how parts fit together, we train a set-conditioned…

## 57. ProSE: Probing Reconstruction Error for Semantic-guided Expert Skipping in MoE-MLLMs

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, language model, large language, spec
- 作者：Jiameng Li, Minye Wu, Matthew B. Blaschko
- 链接：[arXiv](https://arxiv.org/abs/2611.20885) · [PDF](https://arxiv.org/pdf/2611.20885) · [HF](https://huggingface.co/papers/2611.20885)

Mixture-of-Experts Multimodal Large Language Models (MoE-MLLMs) offer scalable inference through sparse expert activation, yet substantial computational redundancy remains among the activated experts. Existing expert skipping methods typically calibrate thresholds based on target skipping ratios or final-output divergence, overlooking the accumulation of skipping-induced error across layers and the varying semantic…

## 58. SciWorldBench: Do Video World Models Really Understand Scientific Experiments?

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, language model, spec
- 作者：Xue Yang, Haonan Cai, Xinyu Hang, Zhimeng Huang, Xuanyi Liu, Chuanmin Jia, Siwei Ma
- 链接：[arXiv](https://arxiv.org/abs/2611.20899) · [PDF](https://arxiv.org/pdf/2611.20899) · [HF](https://huggingface.co/papers/2611.20899)

While the ability of video generation models to accurately depict scientific phenomena has received growing attention, determining whether these models genuinely understand the underlying principles remains a critical challenge. Existing benchmarks typically evaluate video samples in isolation, making it difficult to expose models that simply fit superficial visual priors. In scientific experiments, a small change…

## 59. Multi-LLM Agentic AI at the Edge: Joint Agent Scheduling and Resource Allocation

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, benchmark, language model, large language, spec, retrieval
- 作者：Yuanyan Song, Kezhi Wang, Xinmian Xu, Yongmin Li
- 链接：[arXiv](https://arxiv.org/abs/2611.20915) · [PDF](https://arxiv.org/pdf/2611.20915) · [HF](https://huggingface.co/papers/2611.20915)

In this paper, an edge-enabled multi-large language model (LLM) agentic AI architecture is proposed, where one supervisor AI agent and multiple worker AI agents cooperatively execute users' requests at the edge. The supervisor AI agent decouples the user request into a series of sub-tasks and dynamically dispatches them to LLM-equipped worker AI agents via two agentic workflows, i.e., parallel and serial workflows,…

## 60. Navital Gym: Rule-Graded Agent Environments for Indian Workflows

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, evaluation, language model, planning
- 作者：Daksh Bathla
- 链接：[arXiv](https://arxiv.org/abs/2611.20924) · [PDF](https://arxiv.org/pdf/2611.20924) · [HF](https://huggingface.co/papers/2611.20924)

AI agents are being deployed on Indian workflows such as payments, tax, forms, travel and customer support in Hindi and Hinglish. Public agent evaluations rarely cover these workflows, and many score with another language model. We present Navital Gym, a set of six open environments with 321 public tasks in five task families: trip planning, UPI payments and disputes, GST invoicing and returns, form filling…

## 61. Razavi-Bench: Tracking AI Progress in Analog Circuit Reasoning

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, benchmark, language model, large language
- 作者：Zhishuai Zhang, Oscar Toomey, Taekwang Jang
- 链接：[arXiv](https://arxiv.org/abs/2611.20935) · [PDF](https://arxiv.org/pdf/2611.20935) · [HF](https://huggingface.co/papers/2611.20935)

We propose Razavi-Bench, a benchmark built from the 50 questions in Razavi's two Analog Design Experiments With AI articles and graded by GPT-6 Luna against reference answers and rubrics, and use it to track how fast AI models improve at analog circuit analysis. Across 73 multimodal large language models released between May 2024 and November 2026, the top score rose from 28.83% to 98.33% in 30 months, mostly before…

## 62. ReAccess: Look Once, Stay Focused with Efficient Test Time Memory

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, reasoning, language model, coding, retrieval
- 作者：Tianhao Chen, Yilong Fan, Yuheng Wu, Xiaobin Hu, Dongman Lee
- 链接：[arXiv](https://arxiv.org/abs/2611.20936) · [PDF](https://arxiv.org/pdf/2611.20936) · [HF](https://huggingface.co/papers/2611.20936)

Despite recent advances, vision-language models (VLMs) still struggle with fine-grained visual understanding, often failing to effectively utilize critical evidence already encoded in their visual representations. Existing approaches address this limitation through repeated visual processing or explicit reasoning, introducing substantial computational overhead. In this paper, we propose ReAccess, a lightweight…

## 63. MedJev: A System One Vision-Language Decision Model for Fast and Effective Medical Image Understanding

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, benchmark, language model, spec
- 作者：Fan Zhang, Hao Wu, Jinyang Wu, Hongyu Qu, Zheng Lian, Dongfu Yin, Qingsong Wen, Pheng-Ann Heng
- 链接：[arXiv](https://arxiv.org/abs/2611.20992) · [PDF](https://arxiv.org/pdf/2611.20992) · [HF](https://huggingface.co/papers/2611.20992)

Medical image understanding with vision-language models (VLMs) typically relies on autoregressively generating reasoning and answer tokens. These unnecessary tokens make the inference cost scale with the response length and force the answer to be parsed from free-form text, incurring avoidable latency and decision errors. To this end, we introduce \textsc{MedJev}, a \emph{system one} vision-language decision model…

## 64. MemDoctor: Stage-wise Error Attribution and Repair for MLLM Agent Memory

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, memory, language model, large language
- 作者：Ruiyang Jiang, Xinyang Liao, Weikai Huang, Yuqi Niu, Junjie Zhou, Yubin Zheng
- 链接：[arXiv](https://arxiv.org/abs/2611.21019) · [PDF](https://arxiv.org/pdf/2611.21019) · [HF](https://huggingface.co/papers/2611.21019)

Multimodal large language models (MLLMs) now assist users across sessions of images and text, carried by an external memory of what was said and shown. When such an assistant answers wrongly, the failure usually began earlier, in how a record was written, updated or retrieved, and the answer alone does not say where. We formalize multimodal memory as four stages, Write, Update, Retrieve and Answer, and define nine…

## 65. SWE-OPD: On-Policy Distillation for Agentic Coding

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reasoning, benchmark, coding, spec
- 作者：Yuhang He, Yanyu Chen, Chuanzhe Guo, Jie Zhu, Zichen Tian, Hongyu Ge, Zixuan Ren, Huang He, Bingjin Chen, Junyuan Shang, Shuohuan Wang, Yongqi Zhang, Irwin King, Jing Liu
- 链接：[arXiv](https://arxiv.org/abs/2611.21020) · [PDF](https://arxiv.org/pdf/2611.21020) · [HF](https://huggingface.co/papers/2611.21020)

In this work, we study on-policy distillation (OPD) for transferring agentic coding capabilities from a large teacher model to a smaller student model. Prior work has focused primarily on reasoning and short-horizon agentic tasks. We present SWE-OPD, a minimal OPD study for software engineering, where the student interacts with executable repositories and the teacher supervises the prefixes visited by the student.…

## 66. Evaluation-Free Recursive Self-Improvement for Coding Agents

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, evaluation, benchmark, coding, spec
- 作者：Zhe Ren, Guowei Rong, Yimeng Chen, Nanbo Li, Piotr Piękos, Mateusz Ostaszewski, Dandan Guo, Jürgen Schmidhuber
- 链接：[arXiv](https://arxiv.org/abs/2611.21056) · [PDF](https://arxiv.org/pdf/2611.21056) · [HF](https://huggingface.co/papers/2611.21056)

Recent self-improving coding agents have achieved strong benchmark performance by iteratively modifying their own executable implementations. A common pattern uses downstream task-derived evidence to decide which candidates or lineages continue evolving, which we term evaluate-and-select. Obtaining this signal requires repeatedly executing evolved agents on downstream tasks, so broader exploration incurs increasing…

## 67. Sage S2.1 Flash Technical Report

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, tool use, benchmark, coding, spec
- 作者：Kun Cai, Haodong Chen, Guangran Cheng, Qingxiu Cheng, Xu Dai, Guanting Dong, Qiming Ge, Lixin Gu, Tao Gui, Honglin Guo, Yuyang Hu, Zixian Huang, Jiajie Jin, Alexander Lam, Jiaqiang Li, Yining Li, Jiahang Lin, Yanjiang Liu, Xinyu Lu, Haijun Lv, Ningsheng Ma, Zerun Ma, Minlong Peng, Jianmin Qian, Huayu Sha, Junlin Shang, Shuo Shen, Qisheng Su, Jiajun Sun, Yanan Sun, Zhichao Sun, Ran Tao, Zhongbo Tian, Guoqiang Wang, Hui Wang, Rui Wang, Yiding Wang, Zhecan Wang, Hao Xiang, Xinchen Xie, Shuhao Xing, Xiaoyu Xing, Wanghan Xu, Xinyu Yang, Yajie Yang, Dingbo Yuan, Yuhang Zang, Hongjie Zhang, Chengfeng Zhao, Haoran Zhao, Penghao Zhao, Ruojun Zhou, Dongsheng Zhu, Yicheng Zou, Qiye Cai, Yifei Cao, Xinmeng Che, Hongji Chen, Jiabei Chen, Jiadong Chen, Jiahao Chen, Jiayi Chen, Xinjie Chen, Yujia Chen, Xin Deng, Yi Dong, Yichen Dong, Wenjie Fu, Jianing Geng, Chenyang Gu, Ding Han, Han Han, Feiyang Hao, Haotan He, Qiushi He, Xufeng He, Xin Hong, Jie Hou, Binze Hu, Yongkang Hu, Zijian Hu, Enfu Huang, Junhao Huang, Changhao Jiang, Huicheng Jiang, Jiazhen Jiang, Shufan Jiang, Wenqing Jing, Jiahao Kuang, Bowen Lai, Bo Li, Qi Li, Qilong Li, Zhuoqun Li, Tianhao Liang, Jiaxiang Liu, Junzhang Liu, Shaofan Liu, Shuainan Liu, Tong Liu, Yi Liu, Ziyu Liu, Zhonghang Lu, Jianwen Luo, Xuan Luo, Yanyi Luo, Huijie Lv, Mingyu Ma, Houcheng Min, Hongjun Mo, Songhao Ni, Chengjun Pan, Qiyuan Peng, Xiaoxuan Peng, Wanying Ren, Runhui Ruan, Jifei Shan, Zixin Shang, Bing Shao, Zhuohui Sheng, Jiayang Shi, Qingyun Shi, Yang Shu, Aierpanjiang Simayi, Sirui Song, Yuxiao Song, Jiahao Sun, Zhe Sun, Wenzhe Tan, Guoxiang Wang, Hanchen Wang, Jie Wang, Pengbo Wang, Qing Wang, Rui Wang, Weihang Wang, Xiaotao Wang, Yuhui Wang, Zhekai Wang, Zihan Wang, Zile Wang, Jinke Wu, Liwei Wu, Xuansheng Wu, Yida Wu, Yihao Wu, Yinqi Wu, Yue Wu, Yuhan Wu, Yuwa Wu, Zhiheng Xi, Ying Xiao, Zhide Xie, Caijun Xu, Xingle Xu, Yichen Xu, Yongfeng Xu, Xiaolei Yang, Zhixiong Yang, Jiacheng Yao, Dingcheng Yi, Shihong Yi, Jinhui Yin, Peizhou Yu, Shan Yu, Hao Yuan, Junjie Yuan, Xiongyao Zha, Bo Zhang, Caixian Zhang, Kaicheng Zhang, Pengxiang Zhang, Qiuyinzhe Zhang, Wei Zhang, Xiaoqian Zhang, Xinsen Zhang, Jiyuan Zhao, Shuyu Zhao, Pujun Zheng, Zheyu Zheng, Xiaoxue Zhong, Peiheng Zhou, Xiaohao Zhou, Xinyu Zhou, Fangyi Zhu, Guanru Zhu, Yulun Zhu, Jiabao Zhuang, Pengfei Cao, Zhicheng Dou, Xianpei Han, Ben He, Guoxiu He, Xuanjing Huang, Tao Ji, Yu-Gang Jiang, Dahua Lin, Hongyu Lin, Kang Liu, Yaojie Lu, Le Sun, Ji-Rong Wen, Jun Zhao, Yutao Zhu, Qi Zhang, Bowen Zhou
- 链接：[arXiv](https://arxiv.org/abs/2611.21072) · [PDF](https://arxiv.org/pdf/2611.21072) · [HF](https://huggingface.co/papers/2611.21072)

We introduce Sage S1.5 Flash, a 320-billion-parameter general-purpose mixture-of-experts model designed to reason over scientific evidence and act in interactive environments. Sage Sci-Perception uses dedicated encoders for molecular graphs and biological sequences and represents spectra as ordered patches of measurements. Modality-specific projectors map these representations into the input space of a shared…

## 68. Think2Listen: Evidence-Centric Learning For Agentic Audio Understanding With LALMS

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reasoning, evaluation, benchmark, language model
- 作者：Jin Wang, Liang Lin, Kaiwen Luo, Weiliu Wang, Yuxuan Li, Zengxin Han, Gan Zhang, Jingtong Wu, Yufei Guo, Kun Wang
- 链接：[arXiv](https://arxiv.org/abs/2611.21083) · [PDF](https://arxiv.org/pdf/2611.21083) · [HF](https://huggingface.co/papers/2611.21083)

Recent advances in large audio-language models (LALMs) have broadened audio understanding across speech, sound, and music, with tool-based agents further supporting these tasks by invoking predefined audio tools. However, a persistent gap remains between perceiving acoustic content and using it as evidence for reasoning: recognizing what is audible does not ensure that a model can identify which cues resolve an…

## 69. CivilBench: Benchmarking Vision-Language Models for Multimodal Information Integration in Civil Engineering

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, evaluation, benchmark, language model, large language, spec, planning
- 作者：Dan Yuan, Yue Wen, Zhili He, Zhenkui Zhou, Shicen Liu, Ziqiang Zheng
- 链接：[arXiv](https://arxiv.org/abs/2611.21105) · [PDF](https://arxiv.org/pdf/2611.21105) · [HF](https://huggingface.co/papers/2611.21105)

Artificial intelligence (AI), particularly large language models (LLMs) and vision-language models (VLMs), is increasingly applied in civil and structural engineering for disaster assessment, structural analysis, and engineering decision support. However, the extent to which current VLMs possess the reasoning capabilities required for reliable engineering judgments remains unclear. In this work, we introduce…

## 70. From Repositories to Training Environments: Scaling Long-Horizon Coding Agents with Environment Evolution Loop

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, evaluation, benchmark, coding, spec
- 作者：Yang Tian, Tianyu Zheng, Xiyuan Yang, Yaxin Du, Chengran Yang, Bo Zhao, Jian Yang, Bryan Dai
- 链接：[arXiv](https://arxiv.org/abs/2611.21152) · [PDF](https://arxiv.org/pdf/2611.21152) · [HF](https://huggingface.co/papers/2611.21152)

Training coding agents for long-horizon tasks requires environments with verifiable feedback. Existing pipelines often follow a linear process that ends with validation, establishing usability but providing little guidance on improving training value. Recursive self-improvement (RSI) often requires model rollouts or model training followed by downstream evaluation, with costs and feedback delays amplified on…

## 71. Edit Recommendation: Can LLMs Anticipate Edit Requests from Users, and When?

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, benchmark, language model, large language
- 作者：Daisuke Kikuta
- 链接：[arXiv](https://arxiv.org/abs/2611.21155) · [PDF](https://arxiv.org/pdf/2611.21155) · [HF](https://huggingface.co/papers/2611.21155)

After a large language model (LLM) agent generates an artifact, users often send edit requests for it. This paper studies whether an LLM can anticipate these requests before they are sent. Such anticipation is useful in practice because it reduces the effort of user review and feedback. We formalize this task as edit recommendation and build EditRecBench, a benchmark for evaluating the performance of LLMs on this…

## 72. Scientific Coding with Large Language Models: Evidence from Finite Element Analysis

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, language model, large language, coding
- 作者：Erfan Hamdi, Joel Shor, Emma Lejeune
- 链接：[arXiv](https://arxiv.org/abs/2611.21176) · [PDF](https://arxiv.org/pdf/2611.21176) · [HF](https://huggingface.co/papers/2611.21176)

Large language models (LLMs) offer a potential route to automating scientific programming, but their usefulness depends on consistently producing numerically correct code. We extend FEM-Bench to 17 finite element tasks involving nonlinear and history-dependent mechanics and structural dynamics, and evaluate 15 models on implementation and test generation without execution feedback. The best model succeeds in 87.1%…

## 73. TRACK: Tool-Augmented Reasoning over Time Series for Fault Diagnosis in Power Management System

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, benchmark, language model, spec
- 作者：Erkan Bayram, Debanjan Ghosh, Li Zhu, Sambarta Dasgupta
- 链接：[arXiv](https://arxiv.org/abs/2611.21178) · [PDF](https://arxiv.org/pdf/2611.21178) · [HF](https://huggingface.co/papers/2611.21178)

Fault diagnosis in power management systems running multiple loads relies on experts manually inspecting current and voltage waveforms, which fails to scale across deployed units. We present TRACK, which pairs a time series encoder with a Small Language Model to produce structured, physics-grounded diagnostic reports, calling tools for exact, verifiable calculations. It operates on-device, keeping proprietary sensor…

## 74. Seeing Isn't Resolving: Visual and Linguistic Disambiguation with Conversational Grounding

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, language model, spec
- 作者：Edoardo Cecchinato, Shun Inadumi, Angel García Contreras, Giuseppe Riccardi, Koichiro Yoshino
- 链接：[arXiv](https://arxiv.org/abs/2611.21183) · [PDF](https://arxiv.org/pdf/2611.21183) · [HF](https://huggingface.co/papers/2611.21183)

Visual grounding benchmarks usually do not consider the contextual uncertainty of real-world scenarios. In this study, we construct a novel benchmark, the Japanese evaluation for Ambiguous visual Grounding with Dialogue (JAG-D) dataset. It consists of human-robot conversational multimodal interactions covering different types of ambiguity, arising from visual and linguistic categories. We evaluate the capabilities…

## 75. Validating LLM-Based Essay Scorers: A Comparative Analysis in Critical Online Reasoning in Medical Education

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, evaluation, language model, large language, spec
- 作者：Daniel Baumartz, Alexander Mehler, Mevlüt Bagci, Maxim Konca
- 链接：[arXiv](https://arxiv.org/abs/2611.21208) · [PDF](https://arxiv.org/pdf/2611.21208) · [HF](https://huggingface.co/papers/2611.21208)

Automated essay scorers (AES) based on large language models (LLMs) promise human-level accuracy. However, training, fine-tuning, and evaluating LLMs for specific assessment tasks is costly. In particular, the question arises whether these AES should be trained for specific domains or whether models based on generic LLMs might be sufficient. Human annotations, by contrast, are often more valid but far more…

## 76. InclusionMed: Benchmarking AI for Inclusive Healthcare

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, evaluation, benchmark, language model, large language, spec
- 作者： The InclusionMed Collaboration
- 链接：[arXiv](https://arxiv.org/abs/2611.21218) · [PDF](https://arxiv.org/pdf/2611.21218) · [HF](https://huggingface.co/papers/2611.21218)

Advancing medical AI for inclusive healthcare requires evaluation across diverse healthcare roles, tasks, and care settings, but benchmark coverage remains uneven. We introduce InclusionMed, an open medical AI evaluation initiative for inclusive healthcare. The InclusionMed Atlas organizes benchmarks across three healthcare roles and three AI capabilities. For the first release, we selected four public benchmarks…

## 77. A Generative AI-Driven Architecture for Whole-Home Intelligent Services: Edge Models, Memory Management, and Household Applications

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, evaluation, benchmark, spec, planning
- 作者：Mo Zhou
- 链接：[arXiv](https://arxiv.org/abs/2611.21232) · [PDF](https://arxiv.org/pdf/2611.21232) · [HF](https://huggingface.co/papers/2611.21232)

Generative artificial intelligence is entering the home. Cloud-based assistants face governance limitations in data transmission, continuous availability, and the reliability of physical actions, which are especially salient in households where devices remain online, data accumulate over time, and commands trigger real-world actions. Using the home local server as a unifying organizing axis, this article develops a…

## 78. CAE-Bench: Benchmarking AI Agents for Reusable CAE Solver Development

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reasoning, benchmark, spec
- 作者：Zhiyu Zhou, Tianyou Liu, Xinping Yang, Yiyao Liu, Jiayi Dong, Yihan Lin, Haokai Ye, Yifan Lu, Zeyu Dong, Yansong Li, Shengqi Zhang
- 链接：[arXiv](https://arxiv.org/abs/2611.21273) · [PDF](https://arxiv.org/pdf/2611.21273) · [HF](https://huggingface.co/papers/2611.21273)

We developed CAE-Bench, a benchmark to evaluate AI agents on Computer-Aided Engineering (CAE) solver development. A CAE solver is more than a PDE solver; it must be able to generalize across various inputs, such as different boundary conditions, geometries, and material properties. CAE-Bench evaluates the generalizability of AI-developed CAE solvers by providing the same task, such as a heat transfer problem,…

## 79. Benchmarking Large Language Models for Linguistic Annotation

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, language model, large language, spec
- 作者：Ondřej Tichý, Anna Marklová, Barbora Bulantová, Magdalena Titlbachová, Jiří Milička
- 链接：[arXiv](https://arxiv.org/abs/2611.21291) · [PDF](https://arxiv.org/pdf/2611.21291) · [HF](https://huggingface.co/papers/2611.21291)

Assessing large language models for linguistic annotation requires task-specific evaluation under documented conditions. We present dhAIBench, a Python benchmarking and annotation tool with a web interface for exploring and sharing results. It records prompts, configurations and predictions, enabling comparisons of annotation quality, confidence calibration, repeatability and estimated cost. We demonstrate the…

## 80. AnachroBench: Evaluating Historical Consistency in Large Vision-Language Models

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, language model, spec
- 作者：Keunhyeung Park, Byeonggeuk Lim, Kahyeon Kim, Sunhee Jo, Hayeong Ryu, Hoejoon Kwon, Jinhee Jang, YoungBin Kim
- 链接：[arXiv](https://arxiv.org/abs/2611.21292) · [PDF](https://arxiv.org/pdf/2611.21292) · [HF](https://huggingface.co/papers/2611.21292)

Existing Large Vision-Language Model benchmarks primarily evaluate visual understanding in general everyday scenarios, leaving historical consistency with a specified era and country largely underexplored. To address this gap, we propose AnachroBench, a controlled discriminative benchmark for evaluating historical consistency in visual scenes. It contains 1,600 image pairs from eight countries spanning the late 19th…

## 81. Deep Learning for Physicists: From Linear Regression to Reasoning Models

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, reinforcement learning, language model, large language
- 作者：Masanori Hanada
- 链接：[arXiv](https://arxiv.org/abs/2611.21295) · [PDF](https://arxiv.org/pdf/2611.21295) · [HF](https://huggingface.co/papers/2611.21295)

These lecture notes are based on an introductory course on neural networks and deep learning that the author taught in the School of Mathematical Sciences at Queen Mary University of London in 2023/24 and 2024/25. The author, however, is a physicist, and it shows: wherever possible, ideas are explained with physical intuition rather than heavy formalism. Readers with a background in physics or mathematics who want a…

## 82. Agent-Native by Design: A Programming Language for Agentic Applications

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, tool use, benchmark, language model, large language, coding, spec
- 作者：Jayanaka Dantanarayana, Savini Kashmira, Xiaoyu Ma,  Malitha, Malitha Prabhashana, Lingjia Tang, Jason Mars
- 链接：[arXiv](https://arxiv.org/abs/2611.21298) · [PDF](https://arxiv.org/pdf/2611.21298) · [HF](https://huggingface.co/papers/2611.21298)

Building agentic applications requires combining large language model (LLM) operations, workflow structure and application state, and model-guided routing. With SDKs and agent frameworks, developers connect these components through supporting code that prepares model inputs, propagates state, and dispatches model-selected steps. Workflow changes can require coordinated updates to this code, increasing development…

## 83. Turing Agent: Agentic Formal Verification for Mathematical Research

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, evaluation, benchmark, language model, large language, coding
- 作者：Yang Chen, Qianyi Wang, Ronghui Yang, Zhanhao Li, Yu Cong, Chen Zhang, Hangfan Zhang, Shao Zhang, Shuai Li, Toru Takisaka, Chao Xu, Yi Zhou, Zhihao Tang, Xiao Wang, Bo Zhang, Shuyue Hu
- 链接：[arXiv](https://arxiv.org/abs/2611.21299) · [PDF](https://arxiv.org/pdf/2611.21299) · [HF](https://huggingface.co/papers/2611.21299)

Large language models (LLMs) are rapidly advancing mathematical discovery, moving beyond benchmark-level problem solving to tackle frontier research problems. This progress is ushering mathematics into an era of proof abundance, raising a fundamental challenge: how can we ensure the correctness of the ever-growing volume of AI-generated proofs and transform them into trustworthy, machine-verified mathematical…

## 84. Latent Bridge: Asking for Help Without Words

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, benchmark, coding, spec
- 作者：Qichao Wang, Tingyu Qu, Pengcheng Wu, Yiran Zhong, Feida Zhu, Zhiqi Shen, Peilin Zhao, Steven Hoi
- 链接：[arXiv](https://arxiv.org/abs/2611.21301) · [PDF](https://arxiv.org/pdf/2611.21301) · [HF](https://huggingface.co/papers/2611.21301)

Text-based model collaboration requires a large model to generate intermediate responses before a smaller model can use its guidance, adding large-model decoding cost to inference. We introduce POND (Prefill-Only, No-Decode), a method that uses a frozen large sender for prefill and a small receiver for all autoregressive decoding. A trainable bridge maps the sender's hidden states to additional attention keys and…

## 85. LATTE-WordSeg-Lite: Multi-Granularity Thai Word Segmentation on a CPU, with a Reproducible Benchmark

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, language model, large language, coding
- 作者：Thodsaporn Chay-intr, Kobkrit Viriyayudhakorn, Thanaruk Theeramunkong
- 链接：[arXiv](https://arxiv.org/abs/2611.21300) · [PDF](https://arxiv.org/pdf/2611.21300) · [HF](https://huggingface.co/papers/2611.21300)

Large language models read Thai through subword tokens, without a word segmenter. Yet Thai treebanks, speech metrics and morphological resources are built on words, often at several granularities, and word boundaries resolve ambiguities that subword tokens leave open. LATTE (Lattice ATTentive Encoding) reads a text at several granularities at once, through a lattice of dictionary words, but it is a large GPU model.…

## 86. TRIAGE-CPG: A Cross-Model Study of Budgeted Static Malware Triage with Large Language Models

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, language model, large language, spec
- 作者：Paul-Andrei Sava, Alexander Küchler, Daniel Kowatsch, Bernhard Grill, Jennifer Pullman, Yanick Fratantonio, Luca Invernizzi
- 链接：[arXiv](https://arxiv.org/abs/2611.21331) · [PDF](https://arxiv.org/pdf/2611.21331) · [HF](https://huggingface.co/papers/2611.21331)

When triaging unknown binaries, security analysts must decide which samples to clear as benign, flag as malicious, or escalate for deeper analysis. Large Language Models (LLMs) could support these decisions by interpreting decompiled code, but a binary can contain hundreds or thousands of functions, making exhaustive LLM analysis impractical. We study how current LLMs behave when static triage is formulated as…

## 87. WeVisForensics: Self-Evolving Agent for Omni AI-Generated Video Detection

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reasoning, reinforcement learning, benchmark, spec
- 作者：Yipeng Du, Yuxi Li, Ying Zhang, Chong Sun, Chen Li, Jing Lyu, Ying Tai
- 链接：[arXiv](https://arxiv.org/abs/2611.21373) · [PDF](https://arxiv.org/pdf/2611.21373) · [HF](https://huggingface.co/papers/2611.21373)

Recent advances in video generation call for reliable detection grounded in explicit forensic evidence. However, current methods primarily depend on single-pass chain-of-thought reasoning that overlooks brief or localized artifacts, or on predefined multi-agent workflows that offer limited flexibility in selecting relevant inspections. Even with adaptive investigation, optimizing the investigation policy alone does…

## 88. A Crowd-Audited Atlas of Implicit Bias in LLM-Powered Agents

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, language model, large language, spec
- 作者：Jason Alexander, Yuxuan Li, Michael Licamele, Wesley Hanwen Deng, Sauvik Das
- 链接：[arXiv](https://arxiv.org/abs/2611.21376) · [PDF](https://arxiv.org/pdf/2611.21376) · [HF](https://huggingface.co/papers/2611.21376)

Prior work has shown that large language models (LLMs) express implicit biases in high-publicity, one-off decision scenarios such as hiring and intelligence assessment. However, as people increasingly employ autonomous, LLM-powered AI agents that make decisions on their behalf in doing day-to-day tasks, it is of critical importance that we understand how implicit biases, based on sociodemographic assumptions, emerge…

## 89. VisualArtifactSpec 1.0: Evaluating Visual Artifacts under Task Specifications

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, evaluation, benchmark, spec
- 作者：Shuyi Ouyang, Xiaojun Tang, Zijian Zou, Xintong Zhang, Mingli Song, Guannan Zhang, Hongwei Xue
- 链接：[arXiv](https://arxiv.org/abs/2611.21382) · [PDF](https://arxiv.org/pdf/2611.21382) · [HF](https://huggingface.co/papers/2611.21382)

Visual artifact tasks test agents' ability to translate task specifications and source materials into outputs that meet practical needs. Evaluation across artifact families helps distinguish broadly applicable authoring capabilities from strengths confined to a particular medium. We introduce VisualArtifactSpec 1.0 (VAS), a benchmark of 211 creation and modification tasks spanning presentations, static graphics,…

## 90. VideoNexus: Video Perception Beyond the Reasoning Context

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reasoning, evaluation, spec, planning
- 作者：Yancheng Long, Xuanyu Zheng, Wei Chen, Luoyuan Zhang, Haoyang Xu, Bin Wen, Tingting Gao
- 链接：[arXiv](https://arxiv.org/abs/2611.21392) · [PDF](https://arxiv.org/pdf/2611.21392) · [HF](https://huggingface.co/papers/2611.21392)

Understanding long videos requires locating evidence, resolving visual details, and integrating observations into an answer. Even when relevant evidence is present, performing these operations within long, dense visual sequences burdens both perception and reasoning. Video agents enable selective inspection, but returning frames to the planner still accumulates visual information in its reasoning context. Delegating…

## 91. Rubric-Based AES with LLM Ensembles: Scoring of Student Responses in Critical Online Reasoning Using Ensembles of LLMs

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, language model, large language, spec
- 作者：Daniel Baumartz, Alexander Mehler, Patrick Schrottenbacher, Leon Hammerla, Sebastian Gombert
- 链接：[arXiv](https://arxiv.org/abs/2611.21422) · [PDF](https://arxiv.org/pdf/2611.21422) · [HF](https://huggingface.co/papers/2611.21422)

Grading student responses is costly and time-consuming. Moreover, human annotators are prone to bias, fatigue, and rater drift, which further limits grading reliability. Various methods have been employed to develop automated essay scoring (AES) systems to reduce these costs and address bias-related issues. These methods range from early text-feature-based systems to current machine-learning and transformer-based…

## 92. Learning to Reason with Predictive Gains for Generative Recommendation

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, benchmark, language model, large language, spec
- 作者：Zhuoyang Li, Teng Shi, Jiakai Tang, Weijie Yu, Guofu Xie, Xiao Zhang, Lei Kou, Yang Yu, Lei Shen, Xin Chen, Bing Wang, Xiaoyi Zeng, Jun Xu
- 链接：[arXiv](https://arxiv.org/abs/2611.21441) · [PDF](https://arxiv.org/pdf/2611.21441) · [HF](https://huggingface.co/papers/2611.21441)

Reasoning-enhanced generative recommendation (GR) has attracted increasing attention for leveraging the reasoning capabilities of large language models (LLMs) to improve next-item prediction. However, existing methods primarily optimize reasoning through Group Relative Policy Optimization (GRPO) with rule-based rewards determined by final recommendation performance, which faces two key limitations: (i) unmeasured…

## 93. Out of Sight, Into Memory: Compact Visual Latents Retain Local Evidence in Ultra-High-Resolution Remote Sensing

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, language model, large language, spec
- 作者：Meng Tang, Siyuan Du, Yuxin Liu, Shuaishuai Cao, Di Wang, Haonan Guo
- 链接：[arXiv](https://arxiv.org/abs/2611.21457) · [PDF](https://arxiv.org/pdf/2611.21457) · [HF](https://huggingface.co/papers/2611.21457)

Question answering over ultra-high-resolution (UHR) remote sensing scenes poses a tension for multimodal large language models: global overviews obscure small objects and local attributes, whereas detailed crops consume substantial context. Compressing inspected crops into short sequences of continuous visual latents offers a compact memory once crop tokens are discarded, yet diagnostic studies on natural images…

## 94. RESILAGENT: A Three-Pillar Architecture for Cyber-Physical Resilience in Electrical Power and Energy Systems

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, benchmark, language model, large language
- 作者：Nikolaos Kekatos, Georgios Koutidis, Konstantinos Antonakopoulos, Stylianos Basagiannis, Sokratis Katsikas, Georgios Kavallieratos, Alexios Lekidis, Tom Nianios, Elpiniki Papageorgiou
- 链接：[arXiv](https://arxiv.org/abs/2611.21480) · [PDF](https://arxiv.org/pdf/2611.21480) · [HF](https://huggingface.co/papers/2611.21480)

Electrical Power and Energy Systems face hybrid threats that combine cyber intrusions, physical sabotage and climate-driven stress, and routinely outpace today's siloed monitoring stacks. We present RESILAGENT, a concept architecture organised around three operational pillars, Sensing & Data Intelligence, Resilience Analytics & Reporting, and Incident Response & Recovery, mediated by a Cloud-based Orchestrator and…

## 95. Lost in the Hallway: Benchmarking Persistent Spatial Memory Across Revisits

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, memory, reasoning, evaluation, benchmark
- 作者：Henry Zheng, Weibo Gong, Yang Yue, Rui Huang, Yang Zhang, Gao Huang
- 链接：[arXiv](https://arxiv.org/abs/2611.21485) · [PDF](https://arxiv.org/pdf/2611.21485) · [HF](https://huggingface.co/papers/2611.21485)

Persistent spatial understanding is essential for embodied agents to operate reliably in environments they repeatedly encounter. It requires recognizing revisited places despite viewpoint changes, distinguishing them from similar-looking rooms, and updating memories as environments change. Yet existing evaluations often leave physical place identity across separated visits implicit. We introduce ReSpaceBench, a…

## 96. Evaluating Cultural Reasoning and Robustness in LLMs for Spanish Political Discourse

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, evaluation, language model, large language, spec
- 作者：Jorge Valverde-Rebaza, Nathan Garcia-Larios, Karime Ruvalcaba-Perez, Alejandro Rendon, Santiago Sanchez-Ballesteros, Alejandro Martin del Campo
- 链接：[arXiv](https://arxiv.org/abs/2611.21535) · [PDF](https://arxiv.org/pdf/2611.21535) · [HF](https://huggingface.co/papers/2611.21535)

Large language models (LLMs) are increasingly used to interpret, generate, and mediate public-facing language, which makes their reliability especially consequential in politically sensitive settings. Although sentiment analysis is a common task in this area, affective meaning in social media discourse is often conveyed through culturally situated and pragmatically indirect cues that are not well captured by…

## 97. BLIP-Live: Balancing Timeliness & Firing Precision in Proactive Streaming Video Agents

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, memory, benchmark, language model
- 作者：Kanchana Ranasinghe, Honglu Zhou, Dominick Reilly, Le Xue, Shusheng Yang, Juan Carlos Niebles, Silvio Savarese, Ran Xu
- 链接：[arXiv](https://arxiv.org/abs/2611.21553) · [PDF](https://arxiv.org/pdf/2611.21553) · [HF](https://huggingface.co/papers/2611.21553)

Streaming video understanding is becoming increasingly important for real-world interactive systems. Such systems must be proactive for natural and useful human interaction: they should respond as soon as sufficient evidence becomes available while avoiding premature, redundant, or incorrect responses. We present BLIP-Live, a framework unifying data, metrics, harness, and training around a shared formulation of…

## 98. Mitigating Catastrophic Forgetting with Physics-Indexed Specialist Memory: the Evolutionary Neuroplastic Agent

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, memory, reinforcement learning, spec, retrieval
- 作者：Blas Eugenio Vicco Zarate, Miguel Hernán Vicco
- 链接：[arXiv](https://arxiv.org/abs/2611.21598) · [PDF](https://arxiv.org/pdf/2611.21598) · [HF](https://huggingface.co/papers/2611.21598)

Continual reinforcement learning requires adaptation to changing conditions while preserving performance under previously encountered dynamics. It was investigated whether specialists generated by evolutionary search can provide a reusable memory when combined with environment detection and failure-driven search. The Evolutionary Neuroplastic Agent (ENA) evolves small neural networks without gradients, archives…

## 99. ViRA: Toward Ultra-High-Resolution Visual Agents via Cross-Input Relative Policy Optimization

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reasoning, reinforcement learning, evaluation, benchmark
- 作者：Huawei Lin, Jinting Liu, Tongyan Wang, Xuyang Chen, Ruihua Shi, Zhichao Xu, Jiaxin Qin, Guoshenghui Zhao, Baijian Yang, Yingjie Victor Chen, Tan Yu, Weijie Zhao
- 链接：[arXiv](https://arxiv.org/abs/2611.21605) · [PDF](https://arxiv.org/pdf/2611.21605) · [HF](https://huggingface.co/papers/2611.21605)

Visual agents answer questions about ultra-high-resolution photos by zooming into the relevant regions. However, existing agents often answer from common sense instead of reading the evidence. Reinforcement learning (RL) on the final answer cannot correct this, because a guess earns the same reward as reading. We propose Cross-Input Relative Policy Optimization (CrossRPO), which trains agents on contrast sets. A…

## 100. Latent Lattice Language Models

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, reasoning, language model, coding
- 作者：Shivam Duggal, Zongze Wu, William T. Freeman, Antonio Torralba, Richard Zhang, Eli Shechtman
- 链接：[arXiv](https://arxiv.org/abs/2611.21608) · [PDF](https://arxiv.org/pdf/2611.21608) · [HF](https://huggingface.co/papers/2611.21608)

Language models typically increase per-token computation through deeper or looped layers and latent reasoning steps, while richer residual connections improve information flow across layers. We instead increase computational capacity: the number of active computational states a model maintains. We introduce the Lattice of Latents, a set of per-layer horizontal latent streams that run recurrently along time,…

## 101. Re-Reading Is Not Free: Token Traces and Cache-Aware Energy Estimation for LLM Agents in Software Engineering

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, language model, large language
- 作者：Tina Vartziotis, Ketevan Peranidze, Rodopi Kosteli, Ezgi Sarikayak, George Dasoulas, Michael Keckeisen, Sotirios Kotsopoulos, Francesca Dominici
- 链接：[arXiv](https://arxiv.org/abs/2611.20873) · [PDF](https://arxiv.org/pdf/2611.20873) · [HF](https://huggingface.co/papers/2611.20873)

As large language models (LLMs) evolve from conversational assistants into autonomous agents embedded in software development workflows, estimating their environmental footprint requires moving beyond conventional token-based accounting. Existing energy estimators focus on isolated request-response interactions, overlooking the repeated processing of accumulated context, cache reuse, and work delegated to subagents.…

## 102. Auditing a Moving Target: Evidence Anchoring and the Expiry of Fairness Audits of Provider-Served Language Models

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, language model, large language
- 作者：Mika Facchini
- 链接：[arXiv](https://arxiv.org/abs/2611.20901) · [PDF](https://arxiv.org/pdf/2611.20901) · [HF](https://huggingface.co/papers/2611.20901)

Organizations increasingly use large language models (LLMs) for decisions about people, such as hiring, investment and employee evaluation, and rely on them over long periods of time. Fairness audits of such systems, however, are conducted only once. We examine how the biases of LLMs change over time. In a venture screening setting, models from five providers decided whether and how much to invest in startups whose…

## 103. EviBridge: Encoding Predictive Visual Evidence for Proactive Interaction

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, coding, spec
- 作者：Zhichao Huang, Changheng Cai, Song Ren, Zhichen Zhao, Hongsen Liu, Chaoyang Zheng, Wenxi Wu, Yichen Long, Yuan Fang, Luya Wang, Gufeng Liu, Yuchen Wang
- 链接：[arXiv](https://arxiv.org/abs/2611.20916) · [PDF](https://arxiv.org/pdf/2611.20916) · [HF](https://huggingface.co/papers/2611.20916)

Tool-handover interaction calls for preparation before a response is warranted. The model waits until interaction cues appear, then prepares while assessing whether the accumulating evidence supports a response or calls for cancellation. We introduce EviBridge, a framework that integrates predictive visual representations into a vision-language interaction model for joint state and tool prediction. A trainable…

## 104. Living Context Graphs: Continual Semantic Learning for Enterprise Data Reasoning

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, evaluation, retrieval
- 作者：Varun Agrawal, Ayush Srivastava, Eshan Gujar, Kaushal Kumar, Ayush Gupta
- 链接：[arXiv](https://arxiv.org/abs/2611.20976) · [PDF](https://arxiv.org/pdf/2611.20976) · [HF](https://huggingface.co/papers/2611.20976)

Enterprise AI can now perform analytics, reporting, and data-driven workflows, yet the data foundations it relies on remain hard to operationalize: business meaning, relationships, metric definitions, and reporting conventions are absent from database schemas and scattered across undocumented systems and tribal knowledge. We introduce the Living Context Graph (LCG), a continually learned context layer that makes…

## 105. GRACE: Parallel Best-of-N Multi-Agent Analysis of Closed-Form Questions over Dataframes with Guardrail Selection and Adaptive Retry

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, benchmark, spec
- 作者：Fabio Picariello, Salvatore Cipolla, Susanna Bonura, Vito Morreale
- 链接：[arXiv](https://arxiv.org/abs/2611.20983) · [PDF](https://arxiv.org/pdf/2611.20983) · [HF](https://huggingface.co/papers/2611.20983)

LLM agents answer closed-form questions over a tabular dataframe by writing and executing Python, almost always as a single rollout: one interpretation, one script, one result, accepted without comparison. The few pipelines that produce several candidates reconcile them by answer-agreement voting, which needs a single comparable scalar and always returns one, even when every candidate is wrong. We present GRACE…

## 106. Hivemind: A Federated Protocol for AI-Mediated Tacit Knowledge Sharing in Organisations

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, memory, reasoning
- 作者：Srinivasan Sundaresan
- 链接：[arXiv](https://arxiv.org/abs/2611.20988) · [PDF](https://arxiv.org/pdf/2611.20988) · [HF](https://huggingface.co/papers/2611.20988)

This paper presents Hivemind, a federated protocol that enables AI agents to exchange tacit knowledge on behalf of their users, asynchronously and without requiring any direct human interaction. Individual AI memory systems capture the decisions, reasoning, and contextual knowledge that surface during AI-assisted work. Hivemind creates the shared space in which this captured knowledge can flow between individuals…

## 107. Digits in Notation Are Not Numbers: A Scoring Pitfall in PDF-to-Markdown Conversion of Japanese Technical Documents (Preliminary Evaluation)

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, language model, spec
- 作者：Mitsumasa Wada
- 链接：[arXiv](https://arxiv.org/abs/2611.20993) · [PDF](https://arxiv.org/pdf/2611.20993) · [HF](https://huggingface.co/papers/2611.20993)

Converting PDFs to Markdown is now routine preprocessing for search and language models, yet scoring the numbers in the output is easy to get wrong. We evaluate MinerU, a plain-text OCR baseline (NDLOCR-Lite), and a deterministic post-processing pipeline (anchor insertion, footnote reordering, fixes of look-alike characters in fixed contexts, gated formula repair using two independent OCR partners, and heading…

## 108. Does the Voice Matter? Evaluating Frustration Detection on Deployed Clinical Voice-Agent Calls

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, language model, spec
- 作者：Annika Michael, Zachary Ellis, Yuxiang Zhou, Samuel Thio, Yajie Vera He, Spencer Hazel, Jared Joselowitz
- 链接：[arXiv](https://arxiv.org/abs/2611.21001) · [PDF](https://arxiv.org/pdf/2611.21001) · [HF](https://huggingface.co/papers/2611.21001)

Autonomous voice agents now conduct routine clinical follow-up calls, so some automated triage is unavoidable. A patient becoming frustrated is one thing that triage should catch. These systems typically read only the transcript the speech-to-text stage produces, not the voice, and whether that is enough is largely untested on real clinical speech. We study per-turn frustration detection on real patient calls from a…

## 109. System 1 agents: a method for local, reliable and fast agentic AI

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, language model, large language
- 作者：Eleftherios Tzanis, Michail E. Klontzas
- 链接：[arXiv](https://arxiv.org/abs/2611.21053) · [PDF](https://arxiv.org/pdf/2611.21053) · [HF](https://huggingface.co/papers/2611.21053)

Agentic artificial intelligence could automate analyses of sensitive clinical data, but current agents depend on large language models (LLMs). Cloud LLMs expose patient data. Local LLMs hallucinate, and an invented value in a tool call propagates through every later step. Here we present a method to build System 1 agents: local agents that call tools without generating text. A deterministic compiler turns each…

## 110. Multi-CONDOR: Learning Multistable Motion Primitives from Demonstration

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, coding, spec
- 作者：Gabriele Giuseppe Di Marzo, Mariano Ramírez Montero, Maximilian Stölzle, Rodrigo Pérez-Dattari, Cosimo Della Santina
- 链接：[arXiv](https://arxiv.org/abs/2611.21059) · [PDF](https://arxiv.org/pdf/2611.21059) · [HF](https://huggingface.co/papers/2611.21059)

Dynamical-system-based motion policies provide a framework for learning reactive robot motions with stability and convergence properties. Many manipulation tasks, however, admit several distinct goals or a continuous set of acceptable outcomes, requiring motion primitives that preserve these alternatives. Accommodating both goal structures within a unified framework with continuous, autonomous dynamics remains an…

## 111. Conflict-Aware Multi-Teacher On-Policy Distillation in Aligned Action Spaces for Cross-Game Generalization

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reinforcement learning, language model, spec
- 作者：Jing Yi, Cehao Yang, Hualei Zhang, Haitao Li
- 链接：[arXiv](https://arxiv.org/abs/2611.21094) · [PDF](https://arxiv.org/pdf/2611.21094) · [HF](https://huggingface.co/papers/2611.21094)

Zero-shot cross-game generalization aims to consolidate accessible source-game experts into a single vision-language model (VLM) that controls unseen games from raw pixels without target-game parameter updates. While multi-teacher on-policy distillation (MOPD) mitigates offline exposure bias and single-game reinforcement learning (RL) overfitting, scaling it to autoregressive VLMs faces two bottlenecks. First,…

## 112. SWE-WhatIf: Simulating Real Users of Coding Agents from Recorded Session

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, coding, spec
- 作者：Tae Soo Kim, Tongshuang Wu, Juho Kim
- 链接：[arXiv](https://arxiv.org/abs/2611.21095) · [PDF](https://arxiv.org/pdf/2611.21095) · [HF](https://huggingface.co/papers/2611.21095)

Recorded sessions between users and coding agents offer a way to evaluate how agents complete real-world tasks and interact with users. However, these sessions cannot simply be replayed with new agents, because recorded user replies may no longer apply when an agent takes a different trajectory. We introduce SWE-WhatIf, which replays recorded sessions with new agents by modeling the user's intents, the criteria for…

## 113. GRAZE: Text-Free Grasp Synthesis for Unseen Objects from Human Gaze

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, coding, spec
- 作者：Jeongho Lee, Boeun Kim, Hyung Jin Chang, Jungchan Cho, Sang-Il Choi
- 链接：[arXiv](https://arxiv.org/abs/2611.21104) · [PDF](https://arxiv.org/pdf/2611.21104) · [HF](https://huggingface.co/papers/2611.21104)

Text-conditioned hand-object interaction (HOI) generation provides intuitive semantic control, but language is an indirect way to specify where an interaction should occur on an object. Naming the part to grasp requires object-specific words, and naming the approach side requires a reference frame that a prompt lacks. We propose GRAZE (GRAsp from gaZE), which generates hand-object grasp motion from recorded gaze…

## 114. IGRecon4D: Dynamic-Object-Aware Feed-Forward Reconstruction of Driving Scenes

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, spec
- 作者：Yifei Tong, Ziyang Huang, Yizhao Han, Xiaoxiao Long, Hao Zhu
- 链接：[arXiv](https://arxiv.org/abs/2611.21126) · [PDF](https://arxiv.org/pdf/2611.21126) · [HF](https://huggingface.co/papers/2611.21126)

Feed-forward 4D driving-scene reconstruction enables efficient modeling of dynamic autonomous-driving scenes, but current methods suffer from two complementary failure modes: semantic leakage of traffic participants into the static representation and geometric drift of Gaussian locations across viewpoints. We propose \textbf{IGRecon4D}, a feed-forward dynamic scene reconstruction framework that addresses these…

## 115. Linglong Agent Service: A Runtime for Centralized Agent Reasoning and Distributed Execution

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reasoning, spec
- 作者：Hua Zhang, Min Jiang
- 链接：[arXiv](https://arxiv.org/abs/2611.21129) · [PDF](https://arxiv.org/pdf/2611.21129) · [HF](https://huggingface.co/papers/2611.21129)

LLM agents can use remote tools and cloud sandboxes, but integrating reasoning, session state, and heterogeneous execution sites remains a runtime design problem. We present Linglong Agent Service (agentsvc), a self-hosted HTTP service and embeddable Python runtime that treats execution site as a configurable dimension alongside model, tools, and context. A parent service retains inference orchestration, tool…

## 116. Beyond Token Stacking: Multi-scale Visual Modulation and Adaptive Fused-feature Calibration for MLLMs

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：language model, large language, spec
- 作者：Ye Xiao, Shesheng Song, Yi Ren, Shasha Li, Bin Ji, Xiaodong Liu, Jun Ma, Jie Yu
- 链接：[arXiv](https://arxiv.org/abs/2611.21168) · [PDF](https://arxiv.org/pdf/2611.21168) · [HF](https://huggingface.co/papers/2611.21168)

Current Multimodal Large Language Models (MLLMs) have advanced rapidly and follow two main paradigms: one involves concatenating visual and textual tokens for input into Large Language Model (LLM), while the other injects visual knowledge into Feed-Forward Networks (FFNs) of the LLM. However, the former introduces a large number of redundant visual tokens, substantially increasing computational overhead. The latter…

## 117. MiSTiQ: MicroScaling Trellis Quantization for Extreme KV Cache Compression

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, language model, large language
- 作者：Ofir Gordon, Lior Dikstein, Paul Balanca, Idan Achituve, Douglas Orr, Hai Victor Habi
- 链接：[arXiv](https://arxiv.org/abs/2611.21216) · [PDF](https://arxiv.org/pdf/2611.21216) · [HF](https://huggingface.co/papers/2611.21216)

Modern large language models (LLMs) increasingly support longer contexts and serve more concurrent requests, increasing both sequence lengths and batch sizes. Both trends increase KV-cache size and memory traffic during inference. KV-cache quantization reduces these costs, with recent approaches using codebook-based vector quantization to achieve extremely low bit widths. However, hardware constraints limit codebook…

## 118. Stream of Belief: Eliciting Collective Intelligence through Latent Belief Dynamics

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reasoning, spec
- 作者：Yu Yao, Jiayi Dong, Yilun Du
- 链接：[arXiv](https://arxiv.org/abs/2611.21250) · [PDF](https://arxiv.org/pdf/2611.21250) · [HF](https://huggingface.co/papers/2611.21250)

In this work, we view multi-agent reasoning as a process of seeking a collective equilibrium of implicit belief dynamics and introduce Stream of Belief (SoB), where agents maintain continuous latent beliefs and iteratively refine them through communication and reflection. Our method seeks a collective belief state of a multi-agent system where further communication induces no meaningful information propagation.…

## 119. Beyond Bilingual: Studying Quadrilingual Code-Switching with Conversational AI

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, language model, large language
- 作者：Annika Bush, Melika Minnaar, Salys Sultan, Tasnimul Hasan Tashin, Ankur Bhatt, Meltem Aksoy
- 链接：[arXiv](https://arxiv.org/abs/2611.21394) · [PDF](https://arxiv.org/pdf/2611.21394) · [HF](https://huggingface.co/papers/2611.21394)

Multilingual speakers choose languages by topic and conversation partner. Large language models (LLMs) support these languages unequally. Research on code-switching with conversational AI has mostly examined bilingual pairs of well-resourced languages. In Curaçao and Aruba, many people use Dutch, English, Spanish, and the low-resource Creole Papiamentu/o. In a preregistered study, 42 university students held two…

## 120. Efficient Modeling of Multi-Agent Systems via Structure-Aware Physics-Informed Learning

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, memory, spec
- 作者：Yulun Wu, Nicola Bastianello, Karl Henrik Johansson, Matthieu Barreau
- 链接：[arXiv](https://arxiv.org/abs/2611.21404) · [PDF](https://arxiv.org/pdf/2611.21404) · [HF](https://huggingface.co/papers/2611.21404)

Modeling large multi-agent systems poses challenges for trajectory inference and parameter identification, as network size and coupling increase computational demands and partial observations require reconstructing unobserved states. We propose MAS-PINN, a neural-network architecture with a tailored training algorithm for a physics-informed learning framework that leverages the network topology and the agents'…
