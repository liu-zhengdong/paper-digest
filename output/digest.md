# 每日 AI 论文

生成时间：2026-11-23 07:39 UTC  ·  共 13 篇（已按 arXiv ID 去重）

来源：Hugging Face Daily Papers + arXiv（cs.AI / cs.LG / cs.CL / cs.CV）。
排序：HF 上榜、点赞、多源命中、兴趣词。兴趣词可在 `config.json` 改。

## 1. Non-penetrating World Models

- 分数：33.0  ·  HF 赞：38  ·  来源：huggingface
- 兴趣命中：evaluation, benchmark, spec
- 作者：Yuhang Dai, Yinwei Wu, Ziyue Lin, Han Ji, Xingyi Yang
- 链接：[arXiv](https://arxiv.org/abs/2611.27963) · [PDF](https://arxiv.org/pdf/2611.27963) · [HF](https://huggingface.co/papers/2611.27963)

We study a new problem of preventing object penetration in interactive video world models. To understand how existing models handle this, we introduce NoPeBench, a benchmark that evaluates how world models respond to physical obstacles. Our evaluation reveals that none of the open-source models can reliably prevent such failures. Surprisingly, however, these models already encode the information needed to predict…

## 2. Clover-35B-A3B-Preview Technical Report

- 分数：29.0  ·  HF 赞：26  ·  来源：huggingface
- 兴趣命中：agent, memory, evaluation, language model
- 作者：DiffuSpace Technical Team
- 链接：[arXiv](https://arxiv.org/abs/2611.24636) · [PDF](https://arxiv.org/pdf/2611.24636) · [HF](https://huggingface.co/papers/2611.24636)

We introduce Clover-35B-A3B-Preview (Clover), a mixture-of-experts diffusion language model with 35 billion total parameters and 3 billion activated parameters, supporting thinking-mode generation. Clover adapts Gated Delta Networks to block diffusion by combining recurrent memory of previously generated context with bidirectional softmax attention inside the current block. Historical memory readout competes with…

## 3. cmHC: Balancing Stream Mixing in Hyper-Connections via Geometric Contraction

- 分数：28.0  ·  HF 赞：49  ·  来源：huggingface
- 兴趣命中：-
- 作者：Haowei He, Ziwen Zhao, Chenshuo Pan, Gang Lin, Zhihao Yang, Chao Wang, Xinzhang Liu, Kaidong Yu, Han Gao, Dongfang Li, Menglin Yang, Shuangyong Song, Yongxiang Li
- 链接：[arXiv](https://arxiv.org/abs/2611.27193) · [PDF](https://arxiv.org/pdf/2611.27193) · [HF](https://huggingface.co/papers/2611.27193)

Manifold-constrained Hyper-Connections (mHC) extends residual connections to multiple streams and stabilizes residual propagation by constraining stream-mixing residual matrices to the Birkhoff polytope, the set of doubly stochastic matrices. In this work, we investigate how to effectively mix residual streams within the Birkhoff polytope. We reveal a mixing trade-off: when under-mixed residual matrices stay close…

## 4. Reading the Unreadable: Text-Aware Image Super-Resolution Needs Reasoning

- 分数：23.5  ·  HF 赞：15  ·  来源：huggingface
- 兴趣命中：reasoning, benchmark, language model, large language, spec
- 作者：Jaeseong Lee, Jinwoo Kim, Jinho Jeong, Seon Joo Kim
- 链接：[arXiv](https://arxiv.org/abs/2611.15449) · [PDF](https://arxiv.org/pdf/2611.15449) · [HF](https://huggingface.co/papers/2611.15449)

Text-aware image super-resolution (TAISR) aims to recover high-resolution images from low-resolution inputs while preserving textual content. Existing methods treat this as a visual restoration problem, yet severely degraded text often cannot be read from local visual evidence alone. Humans instead read it by reasoning over image context, logical patterns, and prior knowledge. This raises a fundamental question:…

## 5. MemOnce: A Scalable Memory Architecture for Large Language Models

- 分数：20.5  ·  HF 赞：9  ·  来源：huggingface
- 兴趣命中：memory, language model, large language, coding, spec
- 作者：Chang Nie, Chaoyou Fu, Songlin Liu, Yiqing Hu, Caifeng Shan
- 链接：[arXiv](https://arxiv.org/abs/2611.27973) · [PDF](https://arxiv.org/pdf/2611.27973) · [HF](https://huggingface.co/papers/2611.27973)

Deploying large language models (LLMs) in long-horizon and continual interactions requires maintaining reusable memory states for future inference, posing challenges for existing architectures. Standard Transformers accumulate layer-wise, token-level KV caches, incurring linear GPU memory growth and quadratic computational complexity as the context expands. In contrast, linear-time architectures compress history…

## 6. Lost in the Hallway: Benchmarking Persistent Spatial Memory Across Revisits

- 分数：18.5  ·  HF 赞：5  ·  来源：huggingface
- 兴趣命中：agent, memory, reasoning, evaluation, benchmark
- 作者：Henry Zheng, Weibo Gong, Yang Yue, Rui Huang, Yang Zhang, Gao Huang
- 链接：[arXiv](https://arxiv.org/abs/2611.21485) · [PDF](https://arxiv.org/pdf/2611.21485) · [HF](https://huggingface.co/papers/2611.21485)

Persistent spatial understanding is essential for embodied agents to operate reliably in environments they repeatedly encounter. It requires recognizing revisited places despite viewpoint changes, distinguishing them from similar-looking rooms, and updating memories as environments change. Yet existing evaluations often leave physical place identity across separated visits implicit. We introduce ReSpaceBench, a…

## 7. StereoVLM: Binocular Vision-Language Models for Metric 3D Spatial Reasoning

- 分数：16.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：reasoning, benchmark, language model
- 作者：Chi Yan, Guoyang Zhao, Wentao Yuan, Yixiao Ge, Yanning Zhou, Dan Xu
- 链接：[arXiv](https://arxiv.org/abs/2611.27915) · [PDF](https://arxiv.org/pdf/2611.27915) · [HF](https://huggingface.co/papers/2611.27915)

Vision-language models (VLMs) exhibit strong semantic understanding but remain limited in their ability to reason about metric 3D space in the physical world. Existing VLMs typically infer 3D scene structure from one or more images without known camera calibration or cross-view geometric constraints. This makes metric 3D inference inherently ambiguous and leaves it unclear whether their spatial predictions are…

## 8. Duopra: From Full-Duplex Conversation to Full-Duplex Agency

- 分数：15.0  ·  HF 赞：10  ·  来源：huggingface
- 兴趣命中：agent
- 作者：Chiyu Chen, Pengzhou Cheng, Yuezhao Ma, Xiaocheng Li, Can Liu, Haonan Hu, Yao Yao, Yifei Yang, Yijie Lu, Taolei Wang, Yansi Li, Muhuan Wu, Chenglu Sun, Gongshen Liu, Zhuosheng Zhang
- 链接：[arXiv](https://arxiv.org/abs/2611.25773) · [PDF](https://arxiv.org/pdf/2611.25773) · [HF](https://huggingface.co/papers/2611.25773)

Full-duplex interaction models exhibit strong conversational agency, enabling natural, low-latency turn-taking, backchannels, and interruptions. However, completing tasks further requires task agency: timely tool invocation and argument revision following user corrections. Frontend-backend agents separate initiation from execution: the frontend decides whether and what to request, while the backend determines how.…

## 9. AgentRoboCritic: Understanding the Capability of Frontier Agents on Direct Robot Control

- 分数：15.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：agent, benchmark, spec
- 作者：Yiyang Du, Yuxuan Kuang, Qitao Zhao, Yixuan Wang, Zhanqiu Guo, Yi Xu, Xin Li, Wenbin He, Liu Ren, Chenyan Xiong
- 链接：[arXiv](https://arxiv.org/abs/2611.26613) · [PDF](https://arxiv.org/pdf/2611.26613) · [HF](https://huggingface.co/papers/2611.26613)

Frontier multimodal language agents such as GPT-6 Astra have demonstrated strong capabilities in controlling robots directly via low-level numerical actions without high-level primitives. However, existing benchmarks report only episode-level success rates, which show neither how these agents succeed nor where they fail. In this paper, we present a systematic action-level analysis of frontier agents on direct robot…

## 10. Explicit Style Extraction for Personalized Long-Form Text Generation

- 分数：14.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：language model, spec, retrieval
- 作者：Jenitha Reddy Patel, Sameeksha Kini, Amulya Rayasam, Anisa Dye, Abhinav Sharma, Sai Karthik Navuluru, Bo Ni, Li Li, Junda Wu, Tong Yu, Nedim Lipka, Xiaolei Huang, Tyler Derr, Yue Zhao, Zhengzhong Tu, Yu Wang, Hongjie Chen, Thien Huu Nguyen, Nesreen K. Ahmed, Franck Dernoncourt, Ryan A. Rossi
- 链接：[arXiv](https://arxiv.org/abs/2611.27211) · [PDF](https://arxiv.org/pdf/2611.27211) · [HF](https://huggingface.co/papers/2611.27211)

Personalized long-form generation asks a language model to write new text the way a specific user would. The standard recipe, retrieval-augmented generation, places a few of the user's past texts in the prompt but leaves the model to decide what to take from them. We introduce StylePrism, a taxonomy of 28 stylistic aspects in seven categories, and SP-Refine, an inference-time method that makes style extraction an…

## 11. PURE: A Diagnostic Benchmark for Multi-Granularity Multimodal Identity Matching

- 分数：13.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：reasoning, benchmark
- 作者：Hengyu You, Xintong Wang, Jin Cao, Liang Ding
- 链接：[arXiv](https://arxiv.org/abs/2611.22343) · [PDF](https://arxiv.org/pdf/2611.22343) · [HF](https://huggingface.co/papers/2611.22343)

Identity matching asks whether two records denote the same identity, yet the answer depends on the target granularity. Two records may match at the base level but not at the variant level: they share an underlying design while differing in attributes such as color or size. Final matching accuracy does not separately characterize the capabilities involved. To study this problem, we use e-commerce as a challenging…

## 12. Prune to Expand: Training Prompt Enhancers with Less to Imitate

- 分数：11.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：spec
- 作者：Tianhe Wu, Qilin Sun, Kede Ma
- 链接：[arXiv](https://arxiv.org/abs/2611.27229) · [PDF](https://arxiv.org/pdf/2611.27229) · [HF](https://huggingface.co/papers/2611.27229)

Prompt enhancement (PE) refines concise user prompts into detailed descriptions to improve the compositional aesthetics of generated images while preserving user intent. A common practice constructs supervised fine-tuning (SFT) pairs by deriving short, user-like prompts from dense captions, implicitly assuming that captions that improve image generation also provide effective supervision. In this paper, however, we…

## 13. AeroRSI: Recursive Self-Improvement for Aerial Vision-Language Navigation

- 分数：9.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：-
- 作者：Shiwei Wu, Yuwen Pan, Zhi Li, Yaowen Li, Yan Zhou, Xuemiao Xu, Yu Liu
- 链接：[arXiv](https://arxiv.org/abs/2611.24077) · [PDF](https://arxiv.org/pdf/2611.24077) · [HF](https://huggingface.co/papers/2611.24077)

Vision-language-action (VLA) models enable unmanned aerial vehicles (UAVs) to follow natural-language instructions, yet still fail frequently in closed-loop flight. Correcting these failures requires repairs, i.e., actions that avoid them at the states the policy itself reaches, which human pilots cannot label at scale and rule-based planners cannot supply reliably. In this paper, we present AeroRSI, a recursive…
