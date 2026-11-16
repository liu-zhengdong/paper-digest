# 每日 AI 论文

生成时间：2026-11-16 06:30 UTC  ·  共 16 篇（已按 arXiv ID 去重）

来源：Hugging Face Daily Papers + arXiv（cs.AI / cs.LG / cs.CL / cs.CV）。
排序：HF 上榜、点赞、多源命中、兴趣词。兴趣词可在 `config.json` 改。

## 1. Envisioning Agentic Robotics: A New Era of Robotic Systems

- 分数：36.0  ·  HF 赞：40  ·  来源：huggingface
- 兴趣命中：agent, reasoning, evaluation, benchmark, spec
- 作者：Grid Robotics, Qingfeng Lan, Duo Li, Siyao Li, Yiheng Lyu, Shijian Lu, Zhenghao Qi, Shizun Wang, Xinchao Wang, Ming Yang, Zhiqin Yang, Zuhao Yang, Tao Yu
- 链接：[arXiv](https://arxiv.org/abs/2611.18359) · [PDF](https://arxiv.org/pdf/2611.18359) · [HF](https://huggingface.co/papers/2611.18359)

The release of GPT-6 Astra marks the emergence of a new paradigm in robotics: agentic robotics. Within weeks, frontier models with agentic harnesses matched or exceeded task-specific policies on many embodied benchmarks. Instead of training a dedicated policy for each family of tasks, an agentic robotic system applies a foundation model to open-world embodied tasks. It operates in a closed loop: observing the…

## 2. Gamer: A Generalist Vision-Language-Action Foundation Model for Long-Horizon Real-Time Game Agent

- 分数：30.0  ·  HF 赞：28  ·  来源：huggingface
- 兴趣命中：agent, memory, context window, reasoning, reinforcement learning, benchmark
- 作者：Run Luo, Kuan Zhang, Qi Deng, Yukun Chen, Zhihao Yang, Yufei Zhang, Renrong Hu, Yi Zhang, Guiyu Ma, Tianyu Fan, Longze Chen, Hao Sun, Jiaming Li, Jiaming Yang, Xiaohao Liu, Tao Tan, Minzheng Wang, Hangtian Jia, Shuai Yuan, Lvdi Wang, Xiao Liu, Chao Ma, Yuting Zou, Yinhe Zheng, Xiaobo Xia, Dawei Jiang, Shaoqing Ren
- 链接：[arXiv](https://arxiv.org/abs/2611.18397) · [PDF](https://arxiv.org/pdf/2611.18397) · [HF](https://huggingface.co/papers/2611.18397)

We introduce Gamer, a generalist agent framework built for long-horizon tasks in complex interactive environments. Its end-to-end architecture combines perception, memory management, and multi-step reasoning. A shared training and deployment pipeline supports interaction with both conventional 2D graphical interfaces and complex 3D simulated worlds. We first continue pre-training on a dataset constructed from tens…

## 3. MMFlash: Faster Speculative Decoding for Vision-Language Models

- 分数：21.5  ·  HF 赞：11  ·  来源：huggingface
- 兴趣命中：benchmark, language model, coding, spec
- 作者：Sicheng Feng, Zigeng Chen, Song Wang, Gongfan Fang, Xinchao Wang
- 链接：[arXiv](https://arxiv.org/abs/2611.18482) · [PDF](https://arxiv.org/pdf/2611.18482) · [HF](https://huggingface.co/papers/2611.18482)

Speculative decoding accelerates generation by letting a lightweight drafter propose tokens for parallel verification by a target model. Diffusion drafters such as DFlash propose an entire token block in a single forward pass, but mainly focus on text-only tasks, leaving multimodal drafting underexplored. To study this setting, we first introduce a metric of token-level visual dependence based on the KL divergence…

## 4. MEM-SQL: Memory-Empowered Text-to-SQL

- 分数：19.0  ·  HF 赞：10  ·  来源：huggingface
- 兴趣命中：memory, benchmark, language model
- 作者：Xiaoqi Wang, Wenqi Pei, Shizheng Hou, Yilai Liu, Han Chen, Boyan Li, Yuyu Luo, Hongyang Du
- 链接：[arXiv](https://arxiv.org/abs/2611.18338) · [PDF](https://arxiv.org/pdf/2611.18338) · [HF](https://huggingface.co/papers/2611.18338)

Text-to-SQL systems translate natural language questions into SQL queries over increasingly complex databases. However, widely used benchmarks evaluate questions independently, overlooking settings where earlier queries over the same database can supply joins or calculations for a new question. We introduce HARE (History-AwaRe Text-to-SQL BEnchmark) to measure the accuracy and cost of adapting historical SQL. HARE…

## 5. AI Reviews Are Biased Towards the Appendix

- 分数：18.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：agent, language model, large language, coding
- 作者：Saptarshi Ghosh, Mohammad Saim, Tianyu Jiang
- 链接：[arXiv](https://arxiv.org/abs/2611.17811) · [PDF](https://arxiv.org/pdf/2611.17811) · [HF](https://huggingface.co/papers/2611.17811)

Large language models (LLMs) are increasingly used by reviewers to highlight weaknesses during the reviewing process, and their outputs often shape the reviews that humans submit. Prior work studies how LLM reviews align with human ones, yet we know little about which parts of a paper these models actually criticize. In this work, we investigate 2,000 papers from ACL, EMNLP, COLM, and ICLR, and show that the latest…

## 6. Rethinking in Spikes: Mitigating Hallucinations in MDLMs with Step-Aware Decoding

- 分数：17.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：reasoning, benchmark, language model, coding
- 作者：Zhongxing Xu, Zhonghua Wang, Zhe Qian, Shiyan Su, Ming Hu, Xiaocheng Zou, Wei Feng, Mingquan Lin, Yuyin Zhou, Yifan Peng, Hamid Rezatofighi, Zongyuan Ge
- 链接：[arXiv](https://arxiv.org/abs/2611.12901) · [PDF](https://arxiv.org/pdf/2611.12901) · [HF](https://huggingface.co/papers/2611.12901)

Recent advancements in multimodal diffusion language models (MDLMs) have exhibited strong global modeling capabilities through iterative refinement. We observe that mask uncertainty follows an overall downward trend during iterative denoising, while a few denoising steps exhibit localized entropy spikes closely associated with hallucinations. We argue that anomalous steps can be identified by measuring the entropy…

## 7. Loopback Transformer: Towards a Unified View of Residual Looped Transformers

- 分数：16.5  ·  HF 赞：13  ·  来源：huggingface
- 兴趣命中：memory
- 作者：Xuan Ouyang, Zefan Cai, Chenlong Zhang, Cheng Luo, Ke Wan, Junjie Hu
- 链接：[arXiv](https://arxiv.org/abs/2611.07226) · [PDF](https://arxiv.org/pdf/2611.07226) · [HF](https://huggingface.co/papers/2611.07226)

Looped Transformers reduce parameter count by repeatedly applying shared blocks, but parameter sharing alone does not determine how the results of repeated computation are reused. We take the depth-memory view of residual connections and analyze which representation is stored after each block application and how later reads weight it. A full block output contains both its input and its new update, so weighting that…

## 8. JFinBench: A Continuously Refreshable Japanese Financial Benchmark from the Latest Certification Exams

- 分数：16.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark, language model, large language, coding, spec, planning
- 作者：Issa Sugiura, Taro Makino, Takashi Ishida
- 链接：[arXiv](https://arxiv.org/abs/2611.18130) · [PDF](https://arxiv.org/pdf/2611.18130) · [HF](https://huggingface.co/papers/2611.18130)

Large language models (LLMs) are increasingly applied to finance, creating a need for benchmarks that evaluate their capabilities across financial systems with different regulations and practices. However, existing financial benchmarks provide limited coverage of country-specific financial systems, and they are difficult to keep up to date as released questions leak into training data. We introduce JFinBench, a…

## 9. Emergent Biological Capabilities in a Foundation Model for Molecular Interactions

- 分数：14.0  ·  HF 赞：8  ·  来源：huggingface
- 兴趣命中：spec
- 作者：Adi Mashiach
- 链接：[arXiv](https://arxiv.org/abs/2611.14504) · [PDF](https://arxiv.org/pdf/2611.14504) · [HF](https://huggingface.co/papers/2611.14504)

Foundation models trained on large unlabeled corpora develop emergent capabilities, tasks that go beyond the training objective. We extend this paradigm to multimodal biology with Bonbon, a foundation model for molecular interactions trained on approximately 3.2 trillion tokens of paired protein-ligand sequences. From a single representation space, Bonbon exhibits three zero-shot emergent capabilities at…

## 10. JVT: Just Video Transformer makes pixel-space video diffusion simple

- 分数：13.5  ·  HF 赞：7  ·  来源：huggingface
- 兴趣命中：spec
- 作者：Jianjun Zhou, Hua Geng, Haoyu Guo
- 链接：[arXiv](https://arxiv.org/abs/2611.18549) · [PDF](https://arxiv.org/pdf/2611.18549) · [HF](https://huggingface.co/papers/2611.18549)

Direct diffusion modeling of high-dimensional raw video data is challenging, and existing pixel-space methods often rely on specialized architectures. We introduce JVT (Just Video Transformer), a simple large-patch DiT-style Transformer for pixel-space video diffusion, without a pretrained autoencoder, auxiliary detailers, cascaded stages, or U-Net-style skip connections. We systematically examine video patch…

## 11. Disen-Forcing: Disentangling Semantic Anchoring from Motion for Autoregressive Video Diffusion

- 分数：13.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：benchmark, spec
- 作者：Zhengyang Yu, Akio Hayakawa, Masato Ishii, Qingtao Yu, Xuesong Li, Takashi Shibuya, Yuki Mitsufuji, Jing Zhang
- 链接：[arXiv](https://arxiv.org/abs/2611.02822) · [PDF](https://arxiv.org/pdf/2611.02822) · [HF](https://huggingface.co/papers/2611.02822)

Autoregressive video diffusion models (AR-VDMs) enable real-time, long-horizon video generation but degrade rapidly once the inference horizon outruns the training horizon, due to compounding exposure bias. To stabilize long rollouts, recent methods heuristically adopt frame sink, keeping initial frames as a persistent model context, inspired by attention sinks in LLMs. We revisit this design and find that the…

## 12. GH-AWTrace: A Large-Scale Dataset of GitHub Agentic Workflow Execution Logs

- 分数：13.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：agent, tool use
- 作者：Jasem Khelifi, Hao Li, Ali Ouni, Mohammed Sayagh, Mohamed Aymen Saied
- 链接：[arXiv](https://arxiv.org/abs/2611.06866) · [PDF](https://arxiv.org/pdf/2611.06866) · [HF](https://huggingface.co/papers/2611.06866)

Agentic workflows enable AI agents to perform recurring repository tasks on schedules or in response to repository events. Existing studies examine workflow definitions and outputs, but provide limited evidence of what happens during execution. We present GH-AWTrace, a dataset linking 25,014 verified GitHub Agentic Workflows across 5,051 repositories to 4,112,526 run records and 562,877 nonempty execution log…

## 13. Aligning AI Teams

- 分数：13.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：agent, spec
- 作者：Siddarth Srinivasan, Morgan Jane Matthews, Jascha Sohl-Dickstein, Erik Jones
- 链接：[arXiv](https://arxiv.org/abs/2611.17820) · [PDF](https://arxiv.org/pdf/2611.17820) · [HF](https://huggingface.co/papers/2611.17820)

Previous work has shown that alignment training on individual LLM agents can fail to transfer to multi-agent settings. We investigate the underlying mechanisms for this failure, and explore interventions to preserve alignment transfer to multi-agent LLM teams. We focus on two software-engineering tasks (sepsis triage, a news recommender) and ten consulting-proposal generation tasks. We present four findings: (1) The…

## 14. HALO: Human-Aligned Data Collection for WhoLe-body MObile Manipulation

- 分数：12.0  ·  HF 赞：8  ·  来源：huggingface
- 兴趣命中：-
- 作者：Shuai Yang, Fangyi Xu, Yishu Shen, Kecheng Zheng, Yinghao Xu
- 链接：[arXiv](https://arxiv.org/abs/2611.16439) · [PDF](https://arxiv.org/pdf/2611.16439) · [HF](https://huggingface.co/papers/2611.16439)

Learning whole-body mobile manipulation requires demonstrations that coordinate bimanual actions with locomotion across extended workspaces. However, existing interfaces trade off direct robot control, perception and action alignment, and natural operator mobility, making such demonstrations difficult to collect. We introduce HALO, a human-aligned data collection system for whole-body mobile manipulation. The system…

## 15. CANTraj: Recovering Vehicle Trajectories from CAN Signals in Naturalistic Driving

- 分数：12.0  ·  HF 赞：0  ·  来源：huggingface
- 兴趣命中：evaluation, benchmark
- 作者：Yuhang Wang, Jingxin Yang, Chuheng Wei, Suyang Chen, Haozhuang Chi, Hao Zhou
- 链接：[arXiv](https://arxiv.org/abs/2611.18442) · [PDF](https://arxiv.org/pdf/2611.18442) · [HF](https://huggingface.co/papers/2611.18442)

Open driving releases and usage-based insurance programs often claim to prevent privacy breaches by omitting GPS records when sharing or collecting vehicle data. However, removing GPS coordinates from driving logs does not erase the location information carried by vehicle signals. While prior route-inference attacks have demonstrated that speed, steering, and driving events can be matched to road networks to…

## 16. eDIAR: Training-Free Open-Speaker Streaming Diarization for Long Meetings and Large Archives via e-means

- 分数：9.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：-
- 作者：Kyudan Jung, Jihwan Kim, Minwoo Lee, Eunji Shin, Jaegul Choo
- 链接：[arXiv](https://arxiv.org/abs/2611.18529) · [PDF](https://arxiv.org/pdf/2611.18529) · [HF](https://huggingface.co/papers/2611.18529)

Meetings last up to an hour, and nobody knows in advance how many people will speak. Neural diarizers with a fixed number of output slots, such as Streaming Sortformer and Nemotron-3, are accurate and run online, but they cannot name more speakers than they have slots. We remove this limit without retraining. The slot head keeps deciding who is active and when speech overlaps, and speaker embeddings are clustered…
