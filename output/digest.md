# 每日 AI 论文

生成时间：2026-11-28 07:49 UTC  ·  共 22 篇（已按 arXiv ID 去重）

来源：Hugging Face Daily Papers + arXiv（cs.AI / cs.LG / cs.CL / cs.CV）。
排序：HF 上榜、点赞、多源命中、兴趣词。兴趣词可在 `config.json` 改。

## 1. Solve Vision with Code: Coding Agents Are Stronger Visual Reasoners Than Video Models

- 分数：36.0  ·  HF 赞：61  ·  来源：huggingface
- 兴趣命中：agent, reasoning, coding, spec
- 作者：Dezhi Luo, Fengyuan Yu, Haotian Zhang, Zehong Zhao, Ran Ji, Siyuan An, Huayi Qin, Qingying Gao, Zhongang Cai, Lei Yang, Ziqi Huang, Ruisi Wang, Maijunxian Wang, Hokin Deng
- 链接：[arXiv](https://arxiv.org/abs/2611.34813) · [PDF](https://arxiv.org/pdf/2611.34813) · [HF](https://huggingface.co/papers/2611.34813)

Video generation models are increasingly evaluated as visual reasoners: given a first frame and a natural-language prompt, can the model produce the video in which the specified task is carried out? The paradigm is considered advantageous because the reasoning is native to the visual medium, unfolding directly in the frames rather than through language or code. Whether this native route is in fact the more reliable…

## 2. OS-Omni: Benchmarking Generalist Computer-Using Agents on Long-Horizon Workflows Across Platforms

- 分数：34.0  ·  HF 赞：107  ·  来源：huggingface
- 兴趣命中：agent, benchmark, spec
- 作者：Hui Shen, Yunta Hsieh, Jianing Ma, Zhuoran Yin, Zhuhan Bao, Ziyuan Liu, Qi Han, Xiuqi Xu, Xianbang Wang, Wenhao Chai, Sihan Xu, Chenyang Zhao, Yanheng Shang, Dongfu Jiang, Rui Sun, Xingzhi Li, Chenqi Yin, Zesen Zhao, Boyuan Zheng, Jisen Li, Xiaoxia Wu, Ruoyan Zhang, Ruiyao Liu, Jing Xiong, He Xiao, Nan Zheng, Hangxiang Chen, Shengyang Tao, Deyang Luorong, Yifeng Liu, Jingxuan Zhang, Chaofan Tao, Yuren Wang, Jiaqi Mo, Rui Hu, Xing Wei, Xiaofeng Liu, Xin Xu, Han Wu, Mengyao Wen, Guobin Zhang, Shatong Zhu, Hei Ting Una Chan, Sicheng Chen, Kai Zhang, Mengkang Hu, Zhongwei Wan, Xin Wang, Chuanyang Zheng, Ziheng Zhang, Hengyuan Zhang, Zunhai Su, Kanzhi Cheng, Dehan Kong, Yian Wang, Hanrong Zhang, Jiawei Lu, Yifan Zhang, Junnan Li, Changyi Yang, Jintao Qu, Wenyao Gao, Jiaxuan Luo, Jiaxin Deng, Yuhao Chen, Xuesong Ye, Jingwen Gu, Yichi Zhang, Qun Lou, Shen Yan, Ben Athiwaratkun, Qiushi Sun, Mi Zhang, Ping Luo, Wenhu Chen, Ngai Wong
- 链接：[arXiv](https://arxiv.org/abs/2611.34232) · [PDF](https://arxiv.org/pdf/2611.34232) · [HF](https://huggingface.co/papers/2611.34232)

Computer-using agents are increasingly expected to complete realistic user goals rather than isolated GUI actions. However, existing benchmarks typically isolate web, mobile, or desktop environments, leaving it unclear whether a single generalist agent can execute long-horizon workflows that span multiple operating systems and persistent application states. We introduce OS-Omni, a live cross-platform benchmark and…

## 3. ProxyGenBench: Benchmarking Proxy-Guided Video Generation

- 分数：32.0  ·  HF 赞：36  ·  来源：huggingface
- 兴趣命中：evaluation, benchmark, spec
- 作者：Zhenchen Tang, Haolin Lu, Songlin Yang, Xiaotong Zhao, Ran Zhang, Bo Peng, Shuai Li, Haotian Fan, Haobin Zhong, Yanni Zhang, Songlian Li, Ning Zhang, Xun Gao, Alan Zhao, Jing Dong
- 链接：[arXiv](https://arxiv.org/abs/2611.34457) · [PDF](https://arxiv.org/pdf/2611.34457) · [HF](https://huggingface.co/papers/2611.34457)

Recent video generators produce realistic videos, yet controlling how scenes unfold remains challenging. Structural proxies, such as animated 3D blockouts, guide generation by specifying scene layout, motion, camera behavior, and event order. However, these coarse inputs leave details unspecified and may contain artifacts that should not be reproduced. Successful proxy-guided generation must therefore Preserve…

## 4. Stable Gated DeltaNet-2: Understanding and Mitigating Recurrent State Instability

- 分数：30.0  ·  HF 赞：128  ·  来源：huggingface
- 兴趣命中：retrieval
- 作者：Xichong Zhang, Xixuan Hao, Zhichen Liu, Le Zhou, Zeyu Zhang, Boyu Chen, Mingfei Lu, Zehao Lin, Bo Tang, Yonggang Zhang, Linyun Liu, Feiyu Xiong, Jianlin Su, Zhiyu Li
- 链接：[arXiv](https://arxiv.org/abs/2611.34051) · [PDF](https://arxiv.org/pdf/2611.34051) · [HF](https://huggingface.co/papers/2611.34051)

Linear attention offers an efficient solution for long-sequence modeling via linear complexity and fixed-size recurrent states. Gated DeltaNet-2 (GDN-2) introduces independent channel-wise control over erasure and writing, enhancing state-update expressiveness and in-context retrieval, yet it suffers from training failures during long-context training. We trace these failures to the asymmetry between reading and…

## 5. What a Forecasting Leaderboard Can Establish: Resolution Reporting for Zero-Shot Time-Series Models

- 分数：30.0  ·  HF 赞：58  ·  来源：huggingface
- 兴趣命中：benchmark
- 作者：Arya Sikder, Sriram Pillutla
- 链接：[arXiv](https://arxiv.org/abs/2611.31619) · [PDF](https://arxiv.org/pdf/2611.31619) · [HF](https://huggingface.co/papers/2611.31619)

A foundation model for time series is pretrained once and then asked to forecast series it has never seen, so the evidence for it is its score on held-out datasets. Such datasets are scarce, and a few public leaderboards carry most comparisons, yet none of them states how small a difference its datasets can detect. We call that quantity the resolution of a board and introduce Vernier, a tool that computes it from…

## 6. StateWeaver: Multi-Agent Coordination of Story-State Transitions for Long-Horizon Video Generation

- 分数：29.5  ·  HF 赞：27  ·  来源：huggingface
- 兴趣命中：agent, memory, benchmark, planning
- 作者：Modi Jin, Xuying Zhang, Yijing Guo, Haoran Li, Yanwen Ma, Jing Wang, Chenyu Ge, Ming-Ming Cheng, Haoyang Huang
- 链接：[arXiv](https://arxiv.org/abs/2611.34290) · [PDF](https://arxiv.org/pdf/2611.34290) · [HF](https://huggingface.co/papers/2611.34290)

Modern video foundation models generate high-quality short clips, but preserving long-video consistency and correctly depicting event-driven state changes remain challenging. Existing agentic workflows face these challenges because continual planning and repair accumulate context, while reference updates remain limited. We introduce StateWeaver, which combines Active States and Hierarchical Collaboration to connect…

## 7. DRBench Pro: A Knowledge-Centric Benchmark for Professional Deep Research Agents

- 分数：22.5  ·  HF 赞：17  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark
- 作者：Han Huang, Yuchen Yan, Xingyu Wu, Yijun Li, Chao Deng, Jie Liu, Jin Ma, Yongliang Shen
- 链接：[arXiv](https://arxiv.org/abs/2611.34852) · [PDF](https://arxiv.org/pdf/2611.34852) · [HF](https://huggingface.co/papers/2611.34852)

Deep research agents gather information from multiple sources and synthesize it into reports on complex, open-ended questions. Existing benchmarks assess report quality along several dimensions, but lack a dedicated knowledge-centric evaluation of which research directions a report covers and how deeply it explores them. We introduce DRBench Pro, a benchmark that makes structured knowledge coverage the primary…

## 8. ShowNow: Fine-Grained Speculative Streaming for Responsive World Models

- 分数：20.5  ·  HF 赞：21  ·  来源：huggingface
- 兴趣命中：spec
- 作者：Yiren Song, Guian Fang, Mike Zheng Shou
- 链接：[arXiv](https://arxiv.org/abs/2611.34693) · [PDF](https://arxiv.org/pdf/2611.34693) · [HF](https://huggingface.co/papers/2611.34693)

Interactive world models must generate video continuously while responding promptly to user actions. Real-time throughput alone leaves input latency unresolved: coarse generation blocks delay action updates, and generation after input adds work to the response path. We introduce ShowNow, a fine-grained speculative streaming framework that uses computation available during playback to prepare action-conditioned…

## 9. Revisiting LLMs as Context Engineers

- 分数：18.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：reasoning, benchmark, language model, large language
- 作者：Junrui Zhang, Zeyu Xu, Runchuan Zhu, Jie Peng, Long Zhang, Zixin Ding, Jiaxin Lin, Kai Wang, Jianmin Ji, Junyuan Hong
- 链接：[arXiv](https://arxiv.org/abs/2611.30494) · [PDF](https://arxiv.org/pdf/2611.30494) · [HF](https://huggingface.co/papers/2611.30494)

As large language models (LLMs) are used in more and more new tasks, context engineering becomes a fundamental method to efficiently steer LLMs by constructing instruction prompts or metadata without intensive training. A growing number of LLM context engineering (LCE) approaches automate the task by casting the LLM itself as the engineer that draws generalizable instructions or experiences from offline trials as…

## 10. Boundary-Aware Policy Learning for Agent-Orchestrated Robot Manipulation

- 分数：17.5  ·  HF 赞：7  ·  来源：huggingface
- 兴趣命中：agent, reasoning, spec
- 作者：Kaipeng Fang, Yuhao Wang, Ji Zhang, Yunsong Zhou, Jingkuan Song, Lianli Gao
- 链接：[arXiv](https://arxiv.org/abs/2611.32238) · [PDF](https://arxiv.org/pdf/2611.32238) · [HF](https://huggingface.co/papers/2611.32238)

Agent-orchestrated robot systems combine the general reasoning capability of multimodal agents with the precise physical control of learned visuomotor policies. Yet such systems often fail at the moment of handoff: a policy is reliable only from a limited set of start states, while the agent may invoke it outside this region. We call this region the policy's handoff boundary. Existing whole-task policies typically…

## 11. LayoutRecall: Preserving Appearance in Multi-Round 3D Layout-Controlled Image Editing

- 分数：15.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：memory, benchmark, spec
- 作者：Yankuan Chi, Xin Lin, Baihan Yang, Yuheng Liu, Jason Li, Truong Nguyen
- 链接：[arXiv](https://arxiv.org/abs/2611.33885) · [PDF](https://arxiv.org/pdf/2611.33885) · [HF](https://huggingface.co/papers/2611.33885)

3D layout-controlled image editing gives users explicit control over object placement and camera viewpoint. In a sequence of edits, however, the latest image can lose the appearance of an object when it is occluded or leaves view. The target layout specifies where the object should reappear, while its appearance must be recovered from earlier observations. We introduce LayoutRecall, a multi-round editor that stores…

## 12. Decision-Native Multimodal Clinical Modeling via Anatomical Grounding and Confidence Calibration

- 分数：14.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：evaluation, benchmark, coding
- 作者：Juntao Jiang, Wenqi Zhong, Guangyu Guo, Dexia Chen, Yilong Hu, Yunhao Bai, Zhenyu Yi, Jianwei Xu, Tony C. W. Mok, Muxuan Gao, Ling Zhang, Yong Liu, Jiangning Zhang, Zhongwei Qiu
- 链接：[arXiv](https://arxiv.org/abs/2611.32993) · [PDF](https://arxiv.org/pdf/2611.32993) · [HF](https://huggingface.co/papers/2611.32993)

Structured clinical decisions from volumetric computed tomography (CT) require anatomically grounded predictions and calibrated confidence estimates. However, existing 3D medical multimodal models often suffer from uncalibrated autoregressive decoding and shortcut reliance on irrelevant anatomical regions. We introduce Radev, a decision-native multimodal model that integrates anatomy-guided visual compression,…

## 13. Guarding with Judgment: Learning to Intervene for Multimodal Safety

- 分数：13.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：benchmark, spec
- 作者：Jipei He, Cheng Cheng, Liuguo Wang, Zihan Wen, Changlin Yu, Wentao Song, Suyun Zhao
- 链接：[arXiv](https://arxiv.org/abs/2611.28849) · [PDF](https://arxiv.org/pdf/2611.28849) · [HF](https://huggingface.co/papers/2611.28849)

When visual context makes an ordinary request unsafe to answer as asked, a blanket refusal may leave the user's need unresolved. Choosing how to help requires distinguishing an established hazard from a condition that still needs verification, a distinction that binary safety labels leave unspecified. We formulate this decision through four actions: allow, warn, review, and refuse. To ground these decisions in…

## 14. Generation as Reverse Encoding

- 分数：13.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：coding, spec
- 作者：Cheng Shi, Sibei Yang, Hanzhong Guo, Yipeng Qin, Pietro Lio, Yizhou Yu
- 链接：[arXiv](https://arxiv.org/abs/2611.34782) · [PDF](https://arxiv.org/pdf/2611.34782) · [HF](https://huggingface.co/papers/2611.34782)

Pretrained visual representations accelerate generative learning by abstracting away appearance and spatial detail. Yet the same abstraction makes the return to pixels far harder, shifting much of the burden onto a larger decoder. We ask why the representation-to-pixel path should be learned independently when the encoder already provides a learned pixel-to-semantics path (the semantic encoding path). We introduce…

## 15. BiSAT: Bidirectionally Aligned Semantic-Acoustic Tokenization for Speech Language Models

- 分数：12.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：reinforcement learning, language model
- 作者：Y. Lu, L. Wang, S. Okada
- 链接：[arXiv](https://arxiv.org/abs/2611.30723) · [PDF](https://arxiv.org/pdf/2611.30723) · [HF](https://huggingface.co/papers/2611.30723)

Speech language models (LMs) generate speech as sequences of discrete tokens. Their tokenizer must therefore preserve both acoustic detail and linguistic content at a low bitrate. Semantic-enhanced tokenizers may lose acoustic detail, whereas acoustic-oriented tokenizers retain acoustic variation that makes language modeling harder. Unified tokenizers combine both, but representing acoustic detail and linguistic…

## 16. When an AI agent makes a mistake in a database, what decides the damage?

- 分数：12.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：agent
- 作者：Abdullah Kaya, Cevheri Bozoglan, Yusuf Gundogdu
- 链接：[arXiv](https://arxiv.org/abs/2611.30483) · [PDF](https://arxiv.org/pdf/2611.30483) · [HF](https://huggingface.co/papers/2611.30483)

AI agents now run statements against production databases, and several of the incidents that followed deleted production data, which came back only through backups or the provider's help. We ask what decides the damage when such an agent makes a mistake: the model, a guard layer in front of the database, or the database engine itself. The study has two preregistered layers. In Layer A, a frozen library of 22…

## 17. Markdown Is Not a Firewall: four coding agents, one rules file, four boundaries

- 分数：12.0  ·  HF 赞：0  ·  来源：huggingface
- 兴趣命中：agent, coding
- 作者：Sandeep Dhuri
- 链接：[arXiv](https://arxiv.org/abs/2611.27112) · [PDF](https://arxiv.org/pdf/2611.27112) · [HF](https://huggingface.co/papers/2611.27112)

Teams put a one-page rules file in a repository and call it a control on coding agents. A registered study found agents rarely look up a repository's contribution rules. I asked the security question: what does a rules file do at a boundary, against a gate? I tested one 278-word rules file, with hypotheses and analysis code deposited first. Claude Code, Codex CLI, Gemini CLI and OpenCode with DeepSeek worked through…

## 18. InitFree-SfM: When Initialization-Free Bundle Adjustment meets Learned Structure-from-Motion

- 分数：12.0  ·  HF 赞：0  ·  来源：huggingface
- 兴趣命中：benchmark, spec
- 作者：Simon Weber, Mateo de Mayo, Je Hyeong Hong, Carl Olsson, Daniel Cremers, Ronald Clark
- 链接：[arXiv](https://arxiv.org/abs/2611.31516) · [PDF](https://arxiv.org/pdf/2611.31516) · [HF](https://huggingface.co/papers/2611.31516)

Initialization-free bundle adjustment (InitFree BA) aims to jointly recover camera poses and scene structure without requiring an initial global estimate. It is a very challenging problem, especially compared to traditional BA where a good estimation is assumed. While recent methods optimize surrogate Object Space Error (OSE) objectives from random initialization, a low objective value does not necessarily yield an…

## 19. Reading, Not Adapting: Unlocking Frozen Visual Knowledge for AI-Generated Image Detection

- 分数：11.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：benchmark
- 作者：Yuncheng Guo, Ying Dong, Xiaodong Gu
- 链接：[arXiv](https://arxiv.org/abs/2611.34719) · [PDF](https://arxiv.org/pdf/2611.34719) · [HF](https://huggingface.co/papers/2611.34719)

Generalization to unseen image generators has driven efforts to adapt pretrained visual representations for detection. Yet recent findings show that vision foundation models already encode transferable detection knowledge, while further adaptation can impair generalization. This motivates a shift from backbone adaptation to knowledge readout. Conventional linear probing offers a direct way to read this knowledge but…

## 20. Damped Atomic Wave Integration Neurons (DAWIN): A Universal Primitive for Continuous-Time Spatiotemporal Learning

- 分数：10.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：memory
- 作者：Byunggu Yu, Justin Kim
- 链接：[arXiv](https://arxiv.org/abs/2611.30025) · [PDF](https://arxiv.org/pdf/2611.30025) · [HF](https://huggingface.co/papers/2611.30025)

Conventional artificial neurons separate spatial feature aggregation from continuous physical time, limiting their ability to model irregular observations. We introduce the Damped Atomic Wave Integration Neuron (DAWIN), a continuous-time primitive for replacing standard neural layers in MLPs, Transformers, and graph neural networks. DAWIN couples spatial projection with elapsed-time-dependent wave excitation and…

## 21. Pretrained Tabular Features and the Measurement of Financial Proximity

- 分数：10.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：benchmark
- 作者：Marcus Gawronsky
- 链接：[arXiv](https://arxiv.org/abs/2611.31491) · [PDF](https://arxiv.org/pdf/2611.31491) · [HF](https://huggingface.co/papers/2611.31491)

Spatial arbitrage pricing theory (S-APT) extends factor models to allow returns to spill over between connected firms, beyond what common risk factors explain. In recent years, tabular foundation models (TFMs) have matched or outperformed tuned gradient-boosted and bagged ensembles on small and medium-sized tabular benchmarks. Although their predictive performance is strong, these models reveal little about what…

## 22. So Many Ways to Multiply 3times3 Matrices: A Large Dataset of Rank-23 Schemes

- 分数：10.0  ·  HF 赞：0  ·  来源：huggingface
- 兴趣命中：spec
- 作者：Andrew Igorevich Perminov
- 链接：[arXiv](https://arxiv.org/abs/2611.31155) · [PDF](https://arxiv.org/pdf/2611.31155) · [HF](https://huggingface.co/papers/2611.31155)

A publicly available dataset of 62029 rank-23 schemes for 3times3 matrix multiplication is presented. Every scheme in it has its own rank pattern, an invariant formed by the ranks of the factor matrices of a scheme, so all schemes are pairwise inequivalent. The schemes were obtained by a numerical method combining gradient descent with alternating least squares and by flip graph search, and have ternary, integer or…
