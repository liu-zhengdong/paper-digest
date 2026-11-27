# 每日 AI 论文

生成时间：2026-11-27 08:34 UTC  ·  共 120 篇（已按 arXiv ID 去重）

来源：Hugging Face Daily Papers + arXiv（cs.AI / cs.LG / cs.CL / cs.CV）。
排序：HF 上榜、点赞、多源命中、兴趣词。兴趣词可在 `config.json` 改。

## 1. Real2SimLab: A Unified Platform for Real-to-Simulation Transfer

- 分数：40.0  ·  HF 赞：108  ·  来源：huggingface + arxiv
- 兴趣命中：agent, evaluation, benchmark, coding
- 作者：Yongchang Zhang, Jie Huang, Yunhe Ni, Ningyu Zhou, Guangyu Zhao, Ruixun Liu, Rui Huang, Yidi Wu, TianZe Zhang, Zixiang Jiang, Xiang Li, Kevin Shen, Yiwu Zhong
- 链接：[arXiv](https://arxiv.org/abs/2611.34849) · [PDF](https://arxiv.org/pdf/2611.34849) · [HF](https://huggingface.co/papers/2611.34849)

Real-to-simulation transfer, which builds simulations from real-world observations, has long been studied in research and industry. Recently, coding agents have become capable of generating simulation programs from video recordings, and several benchmarks have been proposed to evaluate them. However, each individual benchmark defines its own inputs, deliverables, and scoring pipeline. This leads to $N \times M$…

## 2. Sage-Med: Scaling Medical Multimodal Intelligence

- 分数：40.0  ·  HF 赞：89  ·  来源：huggingface + arxiv
- 兴趣命中：reasoning, reinforcement learning, evaluation, benchmark, language model, large language, spec
- 作者：Med Team, Ming Hu, Cheng Tang, Wei Li, Rongbin Li, Feilong Tang, Junru Hu, Hongze Zhu, Qiujuan Yan, Huanze Tang, Shaocong Wei, Siyuan Yan, Min Cen, Zhongxing Xu, Zhonghua Wang, Lie Ju, Zhen Yu, Wenjie Li, Shiyan Su, Jing Hao, Jingyong Liang, Diping Song, Fang Yan, Chenglong Ma, Junzhi Ning, Haochen Xue, Zanting Ye, Chenrun Wang, Jinjie Wei, Yi Xin, Jianghan Shen, Siqi Luo, Jiyao Liu, Huidong Xie, Jun Zhao, Rulin Zhou, Longquan Jiang, Ziyan Huang, Ying Chen, Hanxiao Zhang, Junyang Wu, Mouxiao Bian, Jiashi Lin, Chenyu Wang, Qi Qin, Jie Huang, Yiling Zhou, Jiawei Chen, Kefan Wang, Jingjing Hua, Yaoyu Liu, Huihui Xu, Tianbin Li, Jin Ye, Ziyang Chen, Shujian Gao, Zilin Lu, Jiangtao Yan, Changkai Ji, Wenhao Tang, Xinyi Zeng, Yuxing Chen, Hongwei Yang, Rongzhao Zhang, Jinru Ding, Yingcheng Wu, Zhenfei Yin, Jinzhe Li, Lu Lu, Yun Zhong, Zhishan Lin, Bingli Wang, Xiaohan Ren, Jianmin Qian, Penghao Zhao, Zhongbo Tian, Zhenbang Zhou, Peiling Dai, Mengjing Zhao, Jingyu Zheng, Pinan Liu, Shiwei Li, Victoria Mar, Cristina Vico-Alonso, Qiang Wu, Xianming Liu, Lingtong Huang, Dili Song, Minghui Zhang, Wenlong Zhang, Qipeng Guo, Yuqiang Li, Nanqing Dong, Yun Gu, Qi Duan, Hongliang Ren, Hongming Shan, Yin Xie, Xiang An, Benyou Wang, Yueming Su, Yefeng Zheng, Zongyuan Ge, Chun-Mei Feng, Jie Xu, Yu Qiao, Junjun He, Yirong Chen
- 链接：[arXiv](https://arxiv.org/abs/2611.34575) · [PDF](https://arxiv.org/pdf/2611.34575) · [HF](https://huggingface.co/papers/2611.34575)

Establishing effective scaling laws for medical multimodal large language models (MLLMs) remains a persistent and fundamental challenge. Our systematic evaluation shows that existing medical MLLMs tend to underperform frontier general-purpose MLLMs across a range of medical tasks, while scaling model size primarily improves text capabilities rather than multimodal perception, and enabling reasoning modes fails to…

## 3. OS-Omni: Benchmarking Generalist Computer-Using Agents on Long-Horizon Workflows Across Platforms

- 分数：38.0  ·  HF 赞：85  ·  来源：huggingface + arxiv
- 兴趣命中：agent, benchmark, spec
- 作者：Hui Shen, Yunta Hsieh, Jianing Ma, Zhuoran Yin, Zhuhan Bao, Ziyuan Liu, Qi Han, Xiuqi Xu, Xianbang Wang, Wenhao Chai, Sihan Xu, Chenyang Zhao, Yanheng Shang, Dongfu Jiang, Rui Sun, Xingzhi Li, Chenqi Yin, Zesen Zhao, Boyuan Zheng, Jisen Li, Xiaoxia Wu, Ruoyan Zhang, Ruiyao Liu, Jing Xiong, He Xiao, Nan Zheng, Hangxiang Chen, Shengyang Tao, Deyang Luorong, Yifeng Liu, Jingxuan Zhang, Chaofan Tao, Yuren Wang, Jiaqi Mo, Rui Hu, Xing Wei, Xiaofeng Liu, Xin Xu, Han Wu, Mengyao Wen, Guobin Zhang, Shatong Zhu, Hei Ting Una Chan, Sicheng Chen, Kai Zhang, Mengkang Hu, Zhongwei Wan, Xin Wang, Chuanyang Zheng, Ziheng Zhang, Hengyuan Zhang, Zunhai Su, Kanzhi Cheng, Dehan Kong, Yian Wang, Hanrong Zhang, Jiawei Lu, Yifan Zhang, Junnan Li, Changyi Yang, Jintao Qu, Wenyao Gao, Jiaxuan Luo, Jiaxin Deng, Yuhao Chen, Xuesong Ye, Jingwen Gu, Yichi Zhang, Qun Lou, Shen Yan, Ben Athiwaratkun, Qiushi Sun, Mi Zhang, Ping Luo, Wenhu Chen, Ngai Wong
- 链接：[arXiv](https://arxiv.org/abs/2611.34232) · [PDF](https://arxiv.org/pdf/2611.34232) · [HF](https://huggingface.co/papers/2611.34232)

Computer-using agents are increasingly expected to complete realistic user goals rather than isolated GUI actions. However, existing benchmarks typically isolate web, mobile, or desktop environments, leaving it unclear whether a single generalist agent can execute long-horizon workflows that span multiple operating systems and persistent application states. We introduce OS-Omni, a live cross-platform benchmark and…

## 4. VibeVideoAgent: Closing the Perceptual Loop for Code-Driven Video Generation

- 分数：38.0  ·  HF 赞：55  ·  来源：huggingface + arxiv
- 兴趣命中：agent, coding, spec
- 作者：Xuanyu Zheng, Luoyuan Zhang, Yancheng Long, Haoyang Xu, Muxi Diao, Yuzhe Chen, Kaiyu Jiang, Bin Wen, Tingting Gao
- 链接：[arXiv](https://arxiv.org/abs/2611.34237) · [PDF](https://arxiv.org/pdf/2611.34237) · [HF](https://huggingface.co/papers/2611.34237)

Code-driven video generation asks a coding agent to write and run rendering programs. This gives exact control over typography, data visualizations, synchronized audio, and multi-shot scenes, and it leaves an editable project behind. A program that exits cleanly can still render overlapping labels, a camera aimed away from its subject, broken object interactions, or narration that drifts out of sync, and none of…

## 5. Mixture-of-Loops Transformer

- 分数：36.0  ·  HF 赞：70  ·  来源：huggingface + arxiv
- 兴趣命中：memory, coding
- 作者：Lianghui Zhu, Shijie Wang, Xinggang Wang, Jinze Bai, Bo Wang, Xiang Bai
- 链接：[arXiv](https://arxiv.org/abs/2611.34923) · [PDF](https://arxiv.org/pdf/2611.34923) · [HF](https://huggingface.co/papers/2611.34923)

Looped Transformers boost expressivity by reusing shared layers across loops, yet at the cost of efficiency. Pushing their expressivity-efficiency frontier requires rethinking the core mechanism connecting adjacent loops: What should be passed as a Transformer loops? We introduce Mixture-of-Loops Transformer (MoLT), whose Mixture-of-Loops Attention (MoLA) uses keys and values (KV) as memory for selective reuse…

## 6. ProxyGenBench: Benchmarking Proxy-Guided Video Generation

- 分数：35.5  ·  HF 赞：35  ·  来源：huggingface + arxiv
- 兴趣命中：evaluation, benchmark, spec
- 作者：Zhenchen Tang, Haolin Lu, Songlin Yang, Xiaotong Zhao, Ran Zhang, Bo Peng, Shuai Li, Haotian Fan, Haobin Zhong, Yanni Zhang, Songlian Li, Ning Zhang, Xun Gao, Alan Zhao, Jing Dong
- 链接：[arXiv](https://arxiv.org/abs/2611.34457) · [PDF](https://arxiv.org/pdf/2611.34457) · [HF](https://huggingface.co/papers/2611.34457)

Recent video generators produce realistic videos, yet controlling how scenes unfold remains challenging. Structural proxies, such as animated 3D blockouts, guide generation by specifying scene layout, motion, camera behavior, and event order. However, these coarse inputs leave details unspecified and may contain artifacts that should not be reproduced. Successful proxy-guided generation must therefore Preserve…

## 7. PyRUA-Dex: Learning Programmatic Policies for Dexterous Bimanual Manipulation with Coding Agents

- 分数：34.0  ·  HF 赞：44  ·  来源：huggingface
- 兴趣命中：agent, benchmark, coding
- 作者：Feixiang Ruan, Guodong Lv, Kewei Zhang, Wenbo Huang, Yintianrun Zhang, Qiang Wang, Ruiyang Si, Shunyu Yang, Shulong Jiang, Weicheng Duan, Rui Ni, Jianxin Bi, Lekai Wang, Yuze Fan, Haobo Li, Zeliang Fu, Jiankun Zhang, Duomin Wang, Enze Xie, Daquan Zhou
- 链接：[arXiv](https://arxiv.org/abs/2611.33144) · [PDF](https://arxiv.org/pdf/2611.33144) · [HF](https://huggingface.co/papers/2611.33144)

Learning for dexterous manipulation is limited by the scarcity of high-quality demonstrations: retargeting from human video is imprecise, teleoperation gives no force feedback to the operator, and exoskeleton-based collection is hard to scale up. We present PyRUA-Dex, a framework that enables coding agents to develop dexterous manipulation through programmatic policy, without the need of demonstrations. The…

## 8. Improving and Expanding Video Editing Capabilities Without Videos

- 分数：32.0  ·  HF 赞：44  ·  来源：huggingface + arxiv
- 兴趣命中：-
- 作者：Ji Xie, Yanhao Jia, Xiangpeng Yang, Martin Q. Ma, Sihan Xu, Erik Cambria, Louis-Philippe Morency
- 链接：[arXiv](https://arxiv.org/abs/2611.34941) · [PDF](https://arxiv.org/pdf/2611.34941) · [HF](https://huggingface.co/papers/2611.34941)

Image editing models can follow a wide range of instructions, but video editing models still lag behind, limited in part by the difficulty of collecting paired source and edited videos. Is it possible to transfer advanced image editing capabilities to video editors without new paired videos? We introduce Image-to-Video Transfer (I2VT), which improves pretrained video editors and expands them to new editing tasks…

## 9. DocSEAM: Bidirectional Cross-Page Encoding for Multi-Page Document Understanding

- 分数：31.5  ·  HF 赞：27  ·  来源：huggingface + arxiv
- 兴趣命中：benchmark, language model, coding
- 作者：Hoang-Nhat Nguyen, Chen Change Loy
- 链接：[arXiv](https://arxiv.org/abs/2611.34420) · [PDF](https://arxiv.org/pdf/2611.34420) · [HF](https://huggingface.co/papers/2611.34420)

Multi-page document vision-language models encode each page independently, creating a feature-level discontinuity at page boundaries: visual tokens are formed without access to content on adjacent pages, and the language model must reason over these page representations formed in isolation. We introduce DocSEAM (Document Selective Enrichment via Anchored Masking), a lightweight module inserted between a pretrained…

## 10. StateWeaver: Multi-Agent Coordination of Story-State Transitions for Long-Horizon Video Generation

- 分数：30.5  ·  HF 赞：21  ·  来源：huggingface + arxiv
- 兴趣命中：agent, memory, benchmark, planning
- 作者：Modi Jin, Xuying Zhang, Yijing Guo, Haoran Li, Yanwen Ma, Jing Wang, Chenyu Ge, Ming-Ming Cheng, Haoyang Huang
- 链接：[arXiv](https://arxiv.org/abs/2611.34290) · [PDF](https://arxiv.org/pdf/2611.34290) · [HF](https://huggingface.co/papers/2611.34290)

Modern video foundation models generate high-quality short clips, but preserving long-video consistency and correctly depicting event-driven state changes remain challenging. Existing agentic workflows face these challenges because continual planning and repair accumulate context, while reference updates remain limited. We introduce StateWeaver, which combines Active States and Hierarchical Collaboration to connect…

## 11. Stable Gated DeltaNet-2: Understanding and Mitigating Recurrent State Instability

- 分数：30.0  ·  HF 赞：79  ·  来源：huggingface
- 兴趣命中：retrieval
- 作者：Xichong Zhang, Xixuan Hao, Zhichen Liu, Le Zhou, Zeyu Zhang, Boyu Chen, Mingfei Lu, Zehao Lin, Bo Tang, Yonggang Zhang, Linyun Liu, Feiyu Xiong, Jianlin Su, Zhiyu Li
- 链接：[arXiv](https://arxiv.org/abs/2611.34051) · [PDF](https://arxiv.org/pdf/2611.34051) · [HF](https://huggingface.co/papers/2611.34051)

Linear attention offers an efficient solution for long-sequence modeling via linear complexity and fixed-size recurrent states. Gated DeltaNet-2 (GDN-2) introduces independent channel-wise control over erasure and writing, enhancing state-update expressiveness and in-context retrieval, yet it suffers from training failures during long-context training. We trace these failures to the asymmetry between reading and…

## 12. Agentic LongLive: Asynchronous Agentic Memory for Long Video Generation

- 分数：29.0  ·  HF 赞：18  ·  来源：huggingface + arxiv
- 兴趣命中：agent, memory, reinforcement learning, benchmark, language model
- 作者：Shaoteng Liu, Shuai Yang, Wei Huang, Luozhou Wang, Song Han, Yukang Chen
- 链接：[arXiv](https://arxiv.org/abs/2611.34907) · [PDF](https://arxiv.org/pdf/2611.34907) · [HF](https://huggingface.co/papers/2611.34907)

Real-time autoregressive video generators stream minutes of video and accept new prompts on the fly, but struggle to keep people, objects, and places consistent over a long interactive story. Agent systems provide such memory for offline multi-shot generation, yet they read the whole script in advance, plan each shot before generating it, and regenerate failed shots, which a live stream does not allow. We present…

## 13. DyLoMo-DiT: Dynamic Looped Mixture-of-Experts Diffusion Transformers

- 分数：28.0  ·  HF 赞：57  ·  来源：huggingface
- 兴趣命中：-
- 作者：Lernie Li, Yuanliu Liu, Pengfei Xiong, Wei Zhang
- 链接：[arXiv](https://arxiv.org/abs/2611.30844) · [PDF](https://arxiv.org/pdf/2611.30844) · [HF](https://huggingface.co/papers/2611.30844)

Diffusion Transformers (DiTs) scale model capacity by increasing both parameter count and computation. Mixture-of-Experts (MoE) variants expand parameter capacity while keeping per-token computation roughly fixed, but still require substantial parameter storage. In this paper, we propose Dynamic Looped MoE DiT (DyLoMo-DiT), which reuses parameters rather than adding them: a weight-shared loop repeatedly applies the…

## 14. AIRIS: Benchmarking Social Embodied Intelligence in Egocentric Streaming Videos

- 分数：26.5  ·  HF 赞：17  ·  来源：huggingface + arxiv
- 兴趣命中：agent, benchmark, spec
- 作者：Yuchen Zhou, Hongsheng Wu, Jiayu Tang, Yunxuan Mao, Hanjing Ye, Shenghao Zhang, Jing Tang, Chun-Kai Fan, Yufei Huang, Yonggen Ling, He Zhang
- 链接：[arXiv](https://arxiv.org/abs/2611.34347) · [PDF](https://arxiv.org/pdf/2611.34347) · [HF](https://huggingface.co/papers/2611.34347)

Embodied agents operating around people must not only recognize social cues, but also decide when the available evidence is sufficient, whether to intervene, and how to respond without violating social norms. Existing benchmarks typically evaluate these abilities in isolation or with access to completed videos, obscuring where an online social decision fails. We introduce AIRIS, a causal streaming benchmark that…

## 15. EgoUseBench: Benchmarking Computer-Use Agents under Evolving First-Person Contexts

- 分数：26.0  ·  HF 赞：20  ·  来源：huggingface + arxiv
- 兴趣命中：agent, benchmark
- 作者：Yurun Chen, Biao Yi, Qihang Yu, Keting Yin, Shengyu Zhang
- 链接：[arXiv](https://arxiv.org/abs/2611.34466) · [PDF](https://arxiv.org/pdf/2611.34466) · [HF](https://huggingface.co/papers/2611.34466)

AI wearables, such as smart glasses, extend the context available to agents beyond digital environments to users' physical surroundings. With these devices, computer tasks can originate from users' ongoing activities rather than solely from explicit instructions. Through first-person observations, agents can identify objects and activities relevant to user requests and ground digital tasks in the surrounding…

## 16. DRBench Pro: A Knowledge-Centric Benchmark for Professional Deep Research Agents

- 分数：25.5  ·  HF 赞：15  ·  来源：huggingface + arxiv
- 兴趣命中：agent, evaluation, benchmark
- 作者：Han Huang, Yuchen Yan, Xingyu Wu, Yijun Li, Chao Deng, Jie Liu, Jin Ma, Yongliang Shen
- 链接：[arXiv](https://arxiv.org/abs/2611.34852) · [PDF](https://arxiv.org/pdf/2611.34852) · [HF](https://huggingface.co/papers/2611.34852)

Deep research agents gather information from multiple sources and synthesize it into reports on complex, open-ended questions. Existing benchmarks assess report quality along several dimensions, but lack a dedicated knowledge-centric evaluation of which research directions a report covers and how deeply it explores them. We introduce DRBench Pro, a benchmark that makes structured knowledge coverage the primary…

## 17. What a Forecasting Leaderboard Can Establish: Resolution Reporting for Zero-Shot Time-Series Models

- 分数：24.5  ·  HF 赞：29  ·  来源：huggingface
- 兴趣命中：benchmark
- 作者：Arya Sikder, Sriram Pillutla
- 链接：[arXiv](https://arxiv.org/abs/2611.31619) · [PDF](https://arxiv.org/pdf/2611.31619) · [HF](https://huggingface.co/papers/2611.31619)

A foundation model for time series is pretrained once and then asked to forecast series it has never seen, so the evidence for it is its score on held-out datasets. Such datasets are scarce, and a few public leaderboards carry most comparisons, yet none of them states how small a difference its datasets can detect. We call that quantity the resolution of a board and introduce Vernier, a tool that computes it from…

## 18. RoboEvo^2: Recursive Robot Self-Improvement via Harness-Policy Co-Evolution

- 分数：24.5  ·  HF 赞：9  ·  来源：huggingface + arxiv
- 兴趣命中：agent, memory, reasoning, coding
- 作者：Chenzhi Liu, Jiehong Lin, Wei Huang, Xuzhao Huang, Haoyuan Li, Yang Zhang, Junchao Huang, Chenyeyang Cai, Bo Wang, Kazuhiro Kosuge, Zhongrui Wang, Xiaojuan Qi
- 链接：[arXiv](https://arxiv.org/abs/2611.34675) · [PDF](https://arxiv.org/pdf/2611.34675) · [HF](https://huggingface.co/papers/2611.34675)

Robots should adapt to unfamiliar environments and acquire new skills through interaction, then execute those skills efficiently with practice. Vision-language-action policies provide efficient control, but often need additional human demonstrations to handle unfamiliar settings; reasoning agents can discover solutions using broad prior knowledge and robot-control APIs, but repeated deliberation and repair are…

## 19. Entangle: Scaling Human-Video In-Context World-Action Models across Unseen Tasks and Contexts

- 分数：24.0  ·  HF 赞：28  ·  来源：huggingface
- 兴趣命中：spec
- 作者：Chendong Xiang, Chengwen Zhang, Ruowen Zhao, Zeyuan Wang, Shuhe Huang, Rongxu Cui, Min Zhao, Fan Bao, Hengkai Tan, Jun Zhu
- 链接：[arXiv](https://arxiv.org/abs/2611.28732) · [PDF](https://arxiv.org/pdf/2611.28732) · [HF](https://huggingface.co/papers/2611.28732)

In-context learning (ICL) enables foundation models to perform unseen tasks from context without parameter updates. In robotic manipulation, a human video provides the context that specifies how a task should be performed. However, scaling human-video ICL on world-action models (WAMs) faces two challenges: task-level human-robot pairs are not temporally aligned with robot actions, and standard action losses allow…

## 20. Playfulness as Feedback for Agentic Game Development

- 分数：24.0  ·  HF 赞：20  ·  来源：huggingface
- 兴趣命中：agent, coding, spec
- 作者：Weijia Mao, Kevin Qinghong Lin, Zhen Fang, Danze Chen, Dongxing Mao, Mike Zheng Shou
- 链接：[arXiv](https://arxiv.org/abs/2611.33457) · [PDF](https://arxiv.org/pdf/2611.33457) · [HF](https://huggingface.co/papers/2611.33457)

Coding agents can generate runnable games from natural-language descriptions. However, a runnable game does not guarantee an excellent gameplay experience for players. In our view, a playful game should provide 1) reliable core functionality, 2) appealing visual design and assets, and 3) rich gameplay that supports exploration and progression. How agents can improve these aspects of playfulness remains…

## 21. High-Fidelity Image Matting with Pixel-Space Diffusion Transformers

- 分数：23.5  ·  HF 赞：19  ·  来源：huggingface + arxiv
- 兴趣命中：benchmark
- 作者：Baihan Yang, Xin Lin, Yufan Wei, Baiang Li, Yuheng Liu, Juanxi Tian, Xiaohui Xie, Truong Nguyen
- 链接：[arXiv](https://arxiv.org/abs/2611.34929) · [PDF](https://arxiv.org/pdf/2611.34929) · [HF](https://huggingface.co/papers/2611.34929)

Diffusion models have shown strong potential for image matting by transferring generative priors learned from large-scale pretraining. However, existing approaches largely rely on latent diffusion models, whose compressed representations and VAE-based reconstruction introduce a mismatch with the high-frequency precision required for matting. We present PixelMatte, a framework that adapts pretrained pixel-space…

## 22. ROAM-Bench: Evaluating Embodied Active Spatial Intelligence through Evidence Verification

- 分数：23.5  ·  HF 赞：15  ·  来源：huggingface
- 兴趣命中：agent, reasoning, benchmark, language model
- 作者：Xingjian Ran, Xiaoye Mo, Sihao Liu, Li Luo, Taiqiang Wu, Ji Zhao, Wenqi Shao, Hongyang Li, Jiaqi Wang, Bo Dai
- 链接：[arXiv](https://arxiv.org/abs/2611.33143) · [PDF](https://arxiv.org/pdf/2611.33143) · [HF](https://huggingface.co/papers/2611.33143)

Embodied spatial intelligence requires agents to gather information through exploration and interaction, then use it to reason and act. Existing benchmarks insufficiently distinguish correct outcomes from completion of these task requirements. We introduce ROAM-Bench to evaluate these abilities under robot motion and collision constraints. Independent checks use simulation state and episode records to assess…

## 23. Solve Vision with Code: Coding Agents Are Stronger Visual Reasoners Than Video Models

- 分数：23.5  ·  HF 赞：7  ·  来源：huggingface + arxiv
- 兴趣命中：agent, reasoning, coding, spec
- 作者：Dezhi Luo, Fengyuan Yu, Haotian Zhang, Zehong Zhao, Ran Ji, Siyuan An, Huayi Qin, Qingying Gao, Zhongang Cai, Lei Yang, Ziqi Huang, Ruisi Wang, Maijunxian Wang, Hokin Deng
- 链接：[arXiv](https://arxiv.org/abs/2611.34813) · [PDF](https://arxiv.org/pdf/2611.34813) · [HF](https://huggingface.co/papers/2611.34813)

Video generation models are increasingly evaluated as visual reasoners: given a first frame and a natural-language prompt, can the model produce the video in which the specified task is carried out? The paradigm is considered advantageous because the reasoning is native to the visual medium, unfolding directly in the frames rather than through language or code. Whether this native route is in fact the more reliable…

## 24. HOG-WAM: Improving Visual Robustness through Future Gradient Prediction

- 分数：23.0  ·  HF 赞：22  ·  来源：huggingface + arxiv
- 兴趣命中：-
- 作者：Boxuan Dong, Yupeng Qian, Ying Wu, Heshuai Li, Junhao Tan, Zhenxiong Tan, Weijia Wu, Weihao Yu
- 链接：[arXiv](https://arxiv.org/abs/2611.34811) · [PDF](https://arxiv.org/pdf/2611.34811) · [HF](https://huggingface.co/papers/2611.34811)

World-action models jointly predict future observations and actions, yet visual corruption can disrupt the resulting policies. We introduce HOG-WAM, which adds future Histograms of Oriented Gradients (HOG) as structural supervision derived directly from demonstration images. An auxiliary HOG diffusion transformer (DiT) module reads RGB features through asymmetric attention, allowing its objective to shape the visual…

## 25. ShowNow: Fine-Grained Speculative Streaming for Responsive World Models

- 分数：23.0  ·  HF 赞：18  ·  来源：huggingface + arxiv
- 兴趣命中：spec
- 作者：Yiren Song, Guian Fang, Mike Zheng Shou
- 链接：[arXiv](https://arxiv.org/abs/2611.34693) · [PDF](https://arxiv.org/pdf/2611.34693) · [HF](https://huggingface.co/papers/2611.34693)

Interactive world models must generate video continuously while responding promptly to user actions. Real-time throughput alone leaves input latency unresolved: coarse generation blocks delay action updates, and generation after input adds work to the response path. We introduce ShowNow, a fine-grained speculative streaming framework that uses computation available during playback to prepare action-conditioned…

## 26. Beyond Self-Consistency: Recursive Self-Improvement at Test Time

- 分数：21.5  ·  HF 赞：15  ·  来源：huggingface
- 兴趣命中：reasoning, language model, large language
- 作者：Jianyu Wu, Yizhou Wang, Encheng Su, Jinouwen Zhang, Pengze Li, Lintao Wang, Chen Tang, Aoran Wang, Wanli Ouyang, Shixiang Tang
- 链接：[arXiv](https://arxiv.org/abs/2611.30965) · [PDF](https://arxiv.org/pdf/2611.30965) · [HF](https://huggingface.co/papers/2611.30965)

Large language models (LLMs) that continue improving after deployment (e.g., recursive self-improvement) offer a promising path toward general intelligence. Current test-time methods pursue this goal on unlabeled questions, primarily relying on self-consistency: they generate independent solutions and use majority voting to select an answer or construct training targets. This leaves earlier reasoning unused at…

## 27. Loupe: Reinforcing Knowledge-Intensive Video Generation Agents

- 分数：20.0  ·  HF 赞：8  ·  来源：huggingface
- 兴趣命中：agent, evaluation, spec, planning
- 作者：Kai Zeng, Ruichuan An, Zhen Fang, Xi Fang, Han Lyu, Moran Li, Yingchen Yu, Yifan Dai, Bohan Zeng, Quanqing Xu, Zhengzhou Zhu, Wentao Zhang
- 链接：[arXiv](https://arxiv.org/abs/2611.31895) · [PDF](https://arxiv.org/pdf/2611.31895) · [HF](https://huggingface.co/papers/2611.31895)

Knowledge-intensive video generation remains challenging because prompts often omit the facts, appearances, and temporal relationships required for accurate generation. While search-based workflows can retrieve missing evidence, manually designed strategies limit adaptive planning, and conventional training suffers from costly video-level feedback and coarse trajectory-level credit assignment. In this paper, we…

## 28. Puzzling-Bench: Evaluating Language Models on 23,777 Human-Written Puzzles with Community-Verified Answers

- 分数：20.0  ·  HF 赞：4  ·  来源：huggingface + arxiv
- 兴趣命中：evaluation, benchmark, language model
- 作者：Abhinav Sharma, Li Li, Chien Van Nguyen, Sai Karthik Navuluru, Bo Ni, Xiangbo Gao, Xiaolei Huang, Yue Zhao, Nesreen K. Ahmed, Tyler Derr, Yu Wang, Hongjie Chen, Zhengzhong Tu, Thien Huu Nguyen, Ryan A. Rossi, Franck Dernoncourt
- 链接：[arXiv](https://arxiv.org/abs/2611.34331) · [PDF](https://arxiv.org/pdf/2611.34331) · [HF](https://huggingface.co/papers/2611.34331)

We introduce Puzzling-Bench, a benchmark of 23,777 puzzles with community-verified answers drawn from the Puzzling Stack Exchange archive (2014-2026): riddles, ciphers, logic grids, lateral-thinking problems, wordplay and recreational mathematics, a third of them with images. Every puzzle carries the answer accepted by its author, a short reference answer taken from it (LLM-extracted for the evaluation sets and…

## 29. Let Vision-Language Models Generate Images through Their Representations

- 分数：19.5  ·  HF 赞：19  ·  来源：huggingface
- 兴趣命中：language model
- 作者：JB Kim, Byungwoo Jeon, Kyungmin Lee, Hyeonmo Kang, Cheonbok Park, Shinyoung Joo, Jinwoo Shin, Jeonghoon Kim
- 链接：[arXiv](https://arxiv.org/abs/2611.31237) · [PDF](https://arxiv.org/pdf/2611.31237) · [HF](https://huggingface.co/papers/2611.31237)

Recent unified multimodal models aim to combine visual understanding and generation within a single model, yet effectively integrating the two capabilities remains challenging. Leveraging pretrained vision-language models offers a way to build on already learned multimodal knowledge, but making this knowledge effectively accessible to visual generation remains nontrivial. We find that a central challenge lies in the…

## 30. What Is Redundant at High Resolution? Efficient Attention and Feed-Forward Design for All-in-One Image Restoration

- 分数：19.5  ·  HF 赞：15  ·  来源：huggingface
- 兴趣命中：memory, spec
- 作者：Dongheon Lee, DongJae Lee, Sewhan Chun, Chanseul Cho, Youngwook Kim, Youngmin Ro, Yonghyun Jeong
- 链接：[arXiv](https://arxiv.org/abs/2611.33636) · [PDF](https://arxiv.org/pdf/2611.33636) · [HF](https://huggingface.co/papers/2611.33636)

Multi-scale architectures are widely adopted in all-in-one image restoration (AIO-IR) to capture larger-scale context at low-resolution stages and refine details at high-resolution (HR) stages. However, processing spatially large feature maps at HR stages incurs substantial computational costs and memory traffic, making efficient HR processing challenging. To address this challenge, we propose High-resolution…

## 31. Beyond Code and Pixels: Co-Generating Editable and Visually Rich Presentations

- 分数：19.0  ·  HF 赞：10  ·  来源：huggingface
- 兴趣命中：agent, spec, planning
- 作者：Wenrui Zhou, Jiashun Liu, Sujie Hu, Bang Liu, Ling Pan
- 链接：[arXiv](https://arxiv.org/abs/2611.28010) · [PDF](https://arxiv.org/pdf/2611.28010) · [HF](https://huggingface.co/papers/2611.28010)

Generating PPTX presentations is a structured task that requires semantic planning, visual composition, precise layout, and editability, motivating collaboration among specialized agents. However, programmatic methods offer editability but often produce rigid designs, while image-based methods provide visual richness but flatten content into difficult-to-edit pixels. A hybrid system can combine these strengths, but…

## 32. Evaluation-Free Recursive Self-Improvement for Coding Agents

- 分数：18.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark, coding, spec
- 作者：Zhe Ren, Guowei Rong, Yimeng Chen, Nanbo Li, Piotr Piękos, Mateusz Ostaszewski, Dandan Guo, Jürgen Schmidhuber
- 链接：[arXiv](https://arxiv.org/abs/2611.21056) · [PDF](https://arxiv.org/pdf/2611.21056) · [HF](https://huggingface.co/papers/2611.21056)

Recent self-improving coding agents have achieved strong benchmark performance by iteratively modifying their own executable implementations. A common pattern uses downstream task-derived evidence to decide which candidates or lineages continue evolving, which we term evaluate-and-select. Obtaining this signal requires repeatedly executing evolved agents on downstream tasks, so broader exploration incurs increasing…

## 33. CONCOR: Benchmarking Contrastive Decoding for Visual Hallucination Mitigation Beyond Final-Output Performance

- 分数：18.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：evaluation, benchmark, language model, large language, coding
- 作者：Ting Chen, Geng Li, Guohao Chen, Hanjia Lyu
- 链接：[arXiv](https://arxiv.org/abs/2611.30460) · [PDF](https://arxiv.org/pdf/2611.30460) · [HF](https://huggingface.co/papers/2611.30460)

Contrastive decoding (CD) mitigates object hallucination in multimodal large language models (MLLMs) by contrasting token distributions under different conditions to adjust token scores. However, existing generative and discriminative benchmarks primarily measure final task scores, which can be confounded by candidate filtering, changes in generation trajectories, and response biases, making it difficult to isolate…

## 34. SEEK: Self-Evolution through Execution Knowledge for Agentic Robot Manipulation

- 分数：17.5  ·  HF 赞：11  ·  来源：huggingface
- 兴趣命中：agent, spec
- 作者：Zeyang Guan, Qihao Zhao, Rui Gong, Zhang Haitian, Yalun Dai, Yangyu Huang, Lingao Xiao, Haozhe Du, Xuehui Yu, Ye Lu, Jianjun Gao, Ruoyu Wang, Haowen Bai, Hao Li, Scarlett Li, Kim-Hui Yap
- 链接：[arXiv](https://arxiv.org/abs/2611.33915) · [PDF](https://arxiv.org/pdf/2611.33915) · [HF](https://huggingface.co/papers/2611.33915)

General-purpose multimodal foundation models enable robots to adapt during deployment from observations and execution feedback, without task-specific demonstrations or training. However, the robot retains what it learns only in the model's working context. Once the task ends, it loses this execution knowledge, such as how to carry a bowl between two grippers. On the next attempt at the task, the robot may take just…

## 35. Edit Recommendation: Can LLMs Anticipate Edit Requests from Users, and When?

- 分数：17.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：agent, benchmark, language model, large language
- 作者：Daisuke Kikuta
- 链接：[arXiv](https://arxiv.org/abs/2611.21155) · [PDF](https://arxiv.org/pdf/2611.21155) · [HF](https://huggingface.co/papers/2611.21155)

After a large language model (LLM) agent generates an artifact, users often send edit requests for it. This paper studies whether an LLM can anticipate these requests before they are sent. Such anticipation is useful in practice because it reduces the effort of user review and feedback. We formalize this task as edit recommendation and build EditRecBench, a benchmark for evaluating the performance of LLMs on this…

## 36. AIChipBench: Benchmarking LLM Agents for Automated AI Accelerator Design

- 分数：17.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：agent, memory, benchmark, coding, spec
- 作者：Guangyuan Wang, Chengran Li, Minchen Luo, Jichen Feng, Mengdi Wang, Yifan Zhang
- 链接：[arXiv](https://arxiv.org/abs/2611.33093) · [PDF](https://arxiv.org/pdf/2611.33093) · [HF](https://huggingface.co/papers/2611.33093)

A language-model decoder carries state between decoding steps, and in hardware a wrong state update can leave the current token correct and corrupt the output several tokens later, so a design can pass output tests and still be wrong. AIChipBench asks what LLM coding agents need to build such hardware correctly. Agents implement quantized Qwen3.5, Gemma 3, Gemma 4, and Llama 3.2 decoders in synthesizable…

## 37. iMFPO: Improving Mean Flow Policy Optimization with Drift-Aware Velocity Alignment for Embodied Control

- 分数：17.0  ·  HF 赞：10  ·  来源：huggingface
- 兴趣命中：reinforcement learning, evaluation
- 作者：Lisiyu Pan, Ting Huang, Zeyu Zhang, Hao Tang
- 链接：[arXiv](https://arxiv.org/abs/2611.33922) · [PDF](https://arxiv.org/pdf/2611.33922) · [HF](https://huggingface.co/papers/2611.33922)

Flow-based generative policies offer expressive action modeling for embodied control, yet achieving efficient one-step generation under reward-driven policy optimization remains challenging. In particular, evolving action distributions during online reinforcement learning may introduce inconsistencies between instantaneous-velocity learning and interval-averaged action generation. To address this challenge, we…

## 38. Boundary-Aware Policy Learning for Agent-Orchestrated Robot Manipulation

- 分数：17.0  ·  HF 赞：6  ·  来源：huggingface
- 兴趣命中：agent, reasoning, spec
- 作者：Kaipeng Fang, Yuhao Wang, Ji Zhang, Yunsong Zhou, Jingkuan Song, Lianli Gao
- 链接：[arXiv](https://arxiv.org/abs/2611.32238) · [PDF](https://arxiv.org/pdf/2611.32238) · [HF](https://huggingface.co/papers/2611.32238)

Agent-orchestrated robot systems combine the general reasoning capability of multimodal agents with the precise physical control of learned visuomotor policies. Yet such systems often fail at the moment of handoff: a policy is reliable only from a limited set of start states, while the agent may invoke it outside this region. We call this region the policy's handoff boundary. Existing whole-task policies typically…

## 39. Single-Database Rewards Are Hackable: Counterfactual Execution for Trustworthy Text-to-SQL RL

- 分数：17.0  ·  HF 赞：2  ·  来源：huggingface + arxiv
- 兴趣命中：agent, reinforcement learning
- 作者：Shreshth Rai, Rishii Kumar Singh, Aksh Aggarwal
- 链接：[arXiv](https://arxiv.org/abs/2611.34363) · [PDF](https://arxiv.org/pdf/2611.34363) · [HF](https://huggingface.co/papers/2611.34363)

Reinforcement learning (RL) for text-to-SQL agents pays a query when its result matches the reference on one database. However, a wrong query can match by luck when the data lack the rows that expose its bug. We study a counterfactual-database (CF) reward that also runs the final query on a few hidden, code-generated copies of the database and pays only if all results match (strict form) or by the share matched…

## 40. When Every Rollout Fails: Splicing Learner-Conditioned Options into Long-Horizon Agent RL

- 分数：17.0  ·  HF 赞：2  ·  来源：huggingface + arxiv
- 兴趣命中：agent, reinforcement learning
- 作者：Haowen Hou, Yicheng Liu, Zhen Huang, Jiaqi Wang
- 链接：[arXiv](https://arxiv.org/abs/2611.34777) · [PDF](https://arxiv.org/pdf/2611.34777) · [HF](https://huggingface.co/papers/2611.34777)

Group-based reinforcement learning with verifiable rewards often yields all-fail groups on long-horizon agent tasks: every sampled trajectory receives zero reward, leaving group-relative methods without a reward-based policy gradient. A common remedy supplies complete solutions from a stronger model, but full trajectories are expensive and expose the learner to long off-policy histories. We introduce SPLICE, which…

## 41. DemoFoundry: Toward Scalable Photorealistic Robot Data with Coding Agents and Generative Rendering

- 分数：17.0  ·  HF 赞：2  ·  来源：huggingface + arxiv
- 兴趣命中：agent, coding
- 作者：Ruixiang Wang, Xinyue Yao, Xuanning Zhou, Yueci Deng, Yongyi Su, Kui Jia
- 链接：[arXiv](https://arxiv.org/abs/2611.34671) · [PDF](https://arxiv.org/pdf/2611.34671) · [HF](https://huggingface.co/papers/2611.34671)

Scaling robot learning requires demonstrations that combine realistic visual observations with reliable action supervision. Simulation-based synthesis faces a substantial visual gap relative to real environments, while video-only generation struggles to maintain physically consistent interactions and provide aligned action labels. We present DemoFoundry, an automated framework that couples coding agents with…

## 42. FoundSurface: Feedforward Ray-Based 3D Scene Surface Reconstruction from Unposed Images

- 分数：16.5  ·  HF 赞：17  ·  来源：huggingface
- 兴趣命中：-
- 作者：Shenxing Wei, Jinxi Li, Zihui Zhang, Ajay Kumar, Wei Wang, Bo Yang
- 链接：[arXiv](https://arxiv.org/abs/2611.34128) · [PDF](https://arxiv.org/pdf/2611.34128) · [HF](https://huggingface.co/papers/2611.34128)

Accurate 3D surface reconstruction from unposed images remains a fundamental challenge in computer vision. Recent feed-forward pointmap methods eliminate the need for camera poses but inherently produce discrete, sparse representations. In this paper, we present a generalizable pipeline that directly recovers continuous, high-fidelity 3D surfaces from unposed images by seamlessly integrating pointmap- and ray-based…

## 43. Letting Models Manage Their Own Context: Where We Stand

- 分数：16.5  ·  HF 赞：9  ·  来源：huggingface
- 兴趣命中：agent, spec
- 作者：Alessio Devoto, Avinash Vem, Tara Safavi, Sanjay Kariyappa, Yu-Hsuan Tseng, Paul Furgale, Ricardo Silveira Cabral
- 链接：[arXiv](https://arxiv.org/abs/2611.34147) · [PDF](https://arxiv.org/pdf/2611.34147) · [HF](https://huggingface.co/papers/2611.34147)

Agent harnesses today manage context on the model's behalf: when the window fills, the harness triggers a compaction that summarizes the history. We study the alternative, model-driven context management, in which the model itself decides when and what to compact through a context API. We gave models control over their own context in \nooa, NVIDIA's open source agent harness, and compared the two strategies on…

## 44. CARE-3D: Reinforcement Learning for Evidence Grounded Agentic Reasoning in Situated 3D Scenes

- 分数：16.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：agent, reasoning, reinforcement learning, spec
- 作者：Xiaoqian Hu, Ruihong Qiu, Yanran Tang, Sen Wang
- 链接：[arXiv](https://arxiv.org/abs/2611.29969) · [PDF](https://arxiv.org/pdf/2611.29969) · [HF](https://huggingface.co/papers/2611.29969)

Situated 3D reasoning requires embodied agents to interpret objects, scene geometry, and viewpoint dependent spatial relations. Existing methods learn grounded interactions from supervised traces, but largely imitate prescribed evidence acquisition patterns rather than optimizing the support that the returned evidence provides for the correct answer. Moreover, outcome rewards provide limited credit for intermediate…

## 45. Generation as Reverse Encoding

- 分数：16.5  ·  HF 赞：1  ·  来源：huggingface + arxiv
- 兴趣命中：coding, spec
- 作者：Cheng Shi, Sibei Yang, Hanzhong Guo, Yipeng Qin, Pietro Lio, Yizhou Yu
- 链接：[arXiv](https://arxiv.org/abs/2611.34782) · [PDF](https://arxiv.org/pdf/2611.34782) · [HF](https://huggingface.co/papers/2611.34782)

Pretrained visual representations accelerate generative learning by abstracting away appearance and spatial detail. Yet the same abstraction makes the return to pixels far harder, shifting much of the burden onto a larger decoder. We ask why the representation-to-pixel path should be learned independently when the encoder already provides a learned pixel-to-semantics path (the semantic encoding path). We introduce…

## 46. Target-Part Preference Optimization for Part-Aware 3D Generation

- 分数：16.0  ·  HF 赞：16  ·  来源：huggingface
- 兴趣命中：-
- 作者：Zishan Qin, Rui Li, Zeyu Zhang, Sevvandi Kandanaarachchi, Lina Yao, Dong Gong
- 链接：[arXiv](https://arxiv.org/abs/2611.30472) · [PDF](https://arxiv.org/pdf/2611.30472) · [HF](https://huggingface.co/papers/2611.30472)

Part-aware 3D generation requires not only globally plausible objects but also complete, well-separated semantic parts, yet high-quality part decompositions remain too scarce to support large-scale supervised fine-tuning. We study whether preference fine-tuning based on Direct Preference Optimization (DPO) can adapt a pretrained part-aware generator from limited part-annotated data without architectural changes. We…

## 47. Negative-Only Policy Optimization for One-Sided Verifiable Rewards

- 分数：15.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：reinforcement learning, benchmark, spec
- 作者：Jiacheng Xu, Shuo He, Fuxiang Zhang, Chaojie Wang, Bo An
- 链接：[arXiv](https://arxiv.org/abs/2611.17287) · [PDF](https://arxiv.org/pdf/2611.17287) · [HF](https://huggingface.co/papers/2611.17287)

Reinforcement learning with verifiable rewards (RLVR) typically relies on a verifier that can reliably judge whether sampled solutions are correct. However, in many realistic settings, complete verification is generally unavailable, while cheap checks can only falsify failures. We formalize this regime as one-sided verifiability (OSV): verified negatives are reliable counterexamples, but verified positives are…

## 48. Evaluating Memanto on DolphinBench for AI Agents

- 分数：15.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：agent, memory, benchmark
- 作者：Suleman Khan, Rasa Rahnema, Tara Khani, Majid Fekri, Fattane Zarrinkalam
- 链接：[arXiv](https://arxiv.org/abs/2611.28231) · [PDF](https://arxiv.org/pdf/2611.28231) · [HF](https://huggingface.co/papers/2611.28231)

Memory benchmarks built on question answering tell an agent which fact to recall. Workplace requests often leave that need implicit: to post an update in the team's channel, an agent must work out which channel from earlier interactions and use it in a tool call. We evaluate Memanto, a memory agent that ranks memories with an information-theoretic relevance score, on DolphinBench, which tests memory through 600…

## 49. LiveVAE: Causal Window Attention Makes Efficient Streaming Video VAE

- 分数：15.5  ·  HF 赞：3  ·  来源：huggingface + arxiv
- 兴趣命中：coding
- 作者：Jiachen An, Sijie Zhao, Le Li, Hongyu Liu, Zhiyuan Li, Tianyu Yang, Xiaoyu Kong, Xunliang Cai, Yong Zhang, Chi-Man Pun, Xiaoming Wei, Xiaodong Cun
- 链接：[arXiv](https://arxiv.org/abs/2611.34912) · [PDF](https://arxiv.org/pdf/2611.34912) · [HF](https://huggingface.co/papers/2611.34912)

While video diffusion models have grown faster and increasingly streamable, the video VAE remains a primary latency bottleneck across interactive generation and editing pipelines. Existing VAEs and their acceleration methods rely mainly on heavy convolutions or full frame attention, and most focus only on decoding, leaving encoding costly for streaming conditional generation and editing. This raises a natural…

## 50. Reading, Not Adapting: Unlocking Frozen Visual Knowledge for AI-Generated Image Detection

- 分数：15.0  ·  HF 赞：2  ·  来源：huggingface + arxiv
- 兴趣命中：benchmark
- 作者：Yuncheng Guo, Ying Dong, Xiaodong Gu
- 链接：[arXiv](https://arxiv.org/abs/2611.34719) · [PDF](https://arxiv.org/pdf/2611.34719) · [HF](https://huggingface.co/papers/2611.34719)

Generalization to unseen image generators has driven efforts to adapt pretrained visual representations for detection. Yet recent findings show that vision foundation models already encode transferable detection knowledge, while further adaptation can impair generalization. This motivates a shift from backbone adaptation to knowledge readout. Conventional linear probing offers a direct way to read this knowledge but…

## 51. Collect for Coverage, Replay with Evidence: Adaptive and Efficient On-Policy Distillation for Long-Horizon Agents

- 分数：15.0  ·  HF 赞：2  ·  来源：huggingface + arxiv
- 兴趣命中：agent
- 作者：Haowen Hou, Gen Li, Ruilin Li, Yicheng Liu, Zhen Huang, Shuai Dong, Congcong Wang, Kaiwen Tuo, Hongrui Wu, Zelin Peng, Kanghui Tian, Ji Zhao, Dianyi Wang, Jiaqi Wang
- 链接：[arXiv](https://arxiv.org/abs/2611.34756) · [PDF](https://arxiv.org/pdf/2611.34756) · [HF](https://huggingface.co/papers/2611.34756)

Fully online on-policy distillation (OPD) is costly for long-horizon agents because each update depends on fresh environment rollouts. Prefix replay offers an efficient alternative by sampling current-student responses from stored histories, reducing idle time for long-tail rollouts and allowing each collected trajectory to support multiple updates. However, our analysis of the complete prefix replay pipeline…

## 52. 3D CoCa v3: Contrastive Learners with Scene Graphs for Urban Scene Understanding

- 分数：15.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：reasoning, spec, retrieval
- 作者：Nannan Zhang, Ting Huang, Zeyu Zhang, Haoyu Chen, Yanjie Zhu, Hao Tang
- 链接：[arXiv](https://arxiv.org/abs/2611.33835) · [PDF](https://arxiv.org/pdf/2611.33835) · [HF](https://huggingface.co/papers/2611.33835)

Understanding large-scale 3D urban scenes requires representations that capture both multi-scale geometric structures and complex spatial relationships. However, existing 3D vision-language methods primarily emphasize global semantic alignment or object-level representations, leaving structured relational modeling underexplored within unified contrastive and generative frameworks. In this paper, we present 3D CoCa…

## 53. Beyond the Happy Path: Generalizing Robot World Models from Simulated Failures

- 分数：14.5  ·  HF 赞：13  ·  来源：huggingface
- 兴趣命中：-
- 作者：Zhiyue Zhao, Mingyu Liu, Bolin Zhang, Liyang Li, Guangyu Huang, Canyu Zhao, Jinchuan Shi, Haokai Zhang, Hao Chen, Chunhua Shen
- 链接：[arXiv](https://arxiv.org/abs/2611.33925) · [PDF](https://arxiv.org/pdf/2611.33925) · [HF](https://huggingface.co/papers/2611.33925)

Robot world models are increasingly used to evaluate and plan policies, yet robot training data are dominated by successful demonstrations. Off the happy path, when a grasp is misaligned or mistimed and the object is pushed, tilted, or slips, their predictions break down. Across five pretrained action-conditioned models, object-motion error is at most 10.4% lower than that of a static baseline that copies the first…

## 54. WorldBridge: Bridging Scattered Views for Coherent 3D World Generation

- 分数：14.5  ·  HF 赞：9  ·  来源：huggingface
- 兴趣命中：benchmark
- 作者：Weilong Yan, Jingyu Hu, Hongli Xu, Yifan Zhan, Beibei Lin, Anbang Wang, Qinqian Lei, Jingwei Huang, Robby T. Tan
- 链接：[arXiv](https://arxiv.org/abs/2611.34079) · [PDF](https://arxiv.org/pdf/2611.34079) · [HF](https://huggingface.co/papers/2611.34079)

Generating coherent and explorable 3D worlds from scattered images with little or no visual overlap is a fundamental and long-standing challenge in computer vision, which existing geometry-aware methods fail to address. Meanwhile, existing image- and video-based methods may generate unseen regions but produce inconsistent geometry across views. To bridge this gap, we present WorldBridge, a framework for coherent and…

## 55. DetourBench: Trajectory-Level Evaluation of Interactive Agents with Exact Minimum-Action Bounds

- 分数：14.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark
- 作者：Hanlin Tian, Sihan Zhu, Zhao Yang, Yuxiang Wang, Zhiquan Hu, Yu Mi, Hongquan Zhu, Qiufei Hu
- 链接：[arXiv](https://arxiv.org/abs/2611.20844) · [PDF](https://arxiv.org/pdf/2611.20844) · [HF](https://huggingface.co/papers/2611.20844)

Benchmarks judge language-model agents mainly by whether they reach the correct final state, not by how they got there. Endpoint scoring cannot separate an agent that retrieved exactly the evidence a decision required from one that read most of the environment, nor an agent that never located the evidence from one that stopped a single action short. Settling this needs a reference cost, and authored solutions…

## 56. Decision-Native Multimodal Clinical Modeling via Anatomical Grounding and Confidence Calibration

- 分数：14.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：evaluation, benchmark, coding
- 作者：Juntao Jiang, Wenqi Zhong, Guangyu Guo, Dexia Chen, Yilong Hu, Yunhao Bai, Zhenyu Yi, Jianwei Xu, Tony C. W. Mok, Muxuan Gao, Ling Zhang, Yong Liu, Jiangning Zhang, Zhongwei Qiu
- 链接：[arXiv](https://arxiv.org/abs/2611.32993) · [PDF](https://arxiv.org/pdf/2611.32993) · [HF](https://huggingface.co/papers/2611.32993)

Structured clinical decisions from volumetric computed tomography (CT) require anatomically grounded predictions and calibrated confidence estimates. However, existing 3D medical multimodal models often suffer from uncalibrated autoregressive decoding and shortcut reliance on irrelevant anatomical regions. We introduce Radev, a decision-native multimodal model that integrates anatomy-guided visual compression,…

## 57. GOLD-SLAM: Gaussian-splatting Omnidirectional LiDAR-Depth SLAM

- 分数：14.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：evaluation, benchmark, spec
- 作者：Weicong Zhang, Yuan Huang, Yu Zheng, Lin Chenxiao, Yingying Li, Lilong Fan, Liangdong Zhuang, Yufan Chen, Ruiping Liu, Junwei Zheng, Jiaming Zhang
- 链接：[arXiv](https://arxiv.org/abs/2611.32335) · [PDF](https://arxiv.org/pdf/2611.32335) · [HF](https://huggingface.co/papers/2611.32335)

Panoramic cameras capture nearly the entire spherical field of view in a single frame. However, the mismatch between this panoramic coverage and the field of view of LiDAR poses a substantial challenge for panoramic Gaussian splatting SLAM that relies on LiDAR depth priors. We introduce GOLD-SLAM, a Gaussian-splatting Omnidirectional LiDAR-Depth SLAM system that combines high-quality rendering with accurate…

## 58. Efficient Video Retrieval Augmented Generation via Token Allocation

- 分数：14.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：evaluation, language model, retrieval
- 作者：Ayush Barik, Fan Lai, Francis Y. Yan
- 链接：[arXiv](https://arxiv.org/abs/2611.32938) · [PDF](https://arxiv.org/pdf/2611.32938) · [HF](https://huggingface.co/papers/2611.32938)

Efficient long-video understanding requires identifying relevant evidence while minimizing the tokens processed by vision-language models (VLMs). Existing video retrieval-augmented generation (RAG) methods rely on frame selection and token compression, but overlook how much each additional token is worth. We introduce Lembas, a plug-and-play framework that formulates video RAG as a token allocation problem over…

## 59. A Mesh for Every Moment

- 分数：14.5  ·  HF 赞：1  ·  来源：huggingface + arxiv
- 兴趣命中：benchmark
- 作者：Roy Or-El, Jeong Joon Park, Ira Kemelmacher-Shlizerman
- 链接：[arXiv](https://arxiv.org/abs/2611.34939) · [PDF](https://arxiv.org/pdf/2611.34939) · [HF](https://huggingface.co/papers/2611.34939)

We present MEMO (a Mesh for Every MOment), a method that reconstructs the geometry of complete dynamic scenes, captured by multiple synchronized cameras, and extracts a mesh at every frame. Existing dynamic Gaussian splatting methods either model appearance alone or target isolated objects segmented by foreground masks, and all of them recover meshes by TSDF fusion or Poisson reconstruction, whose fixed grids limit…

## 60. SOLVE: Sparse, Ordered Keyposes Make LLM Agents Versatile and Efficient Robot Manipulator

- 分数：14.5  ·  HF 赞：1  ·  来源：huggingface + arxiv
- 兴趣命中：agent
- 作者：Xiang Li, Hongyu Zhou, Ya-Li Li, Tao Li, Rui Zhang, Junjie Lai, Weihua Zhang, Shengjin Wang
- 链接：[arXiv](https://arxiv.org/abs/2611.34750) · [PDF](https://arxiv.org/pdf/2611.34750) · [HF](https://huggingface.co/papers/2611.34750)

LLM agents have made remarkable progress in robot manipulation, yet they suffer from expensive inference, dense step-by-step control, and tool bottlenecks. We introduce SOLVE, a training-free, versatile and efficient agent policy: a multimodal LLM agent writes a sparse, ordered sequence of 6-DoF end-effector keyposes per call, observes the result, and writes the next, while a motion planner interpolates between…

## 61. Lost in Translation, Not in Confidence: Benchmarking and Calibrating Multilingual Decision Models

- 分数：14.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：benchmark, language model
- 作者：Mingzhe Du, Thong Thanh Nguyen, Nguyen Tran Cong Duy, See-Kiong Ng, Luu Anh Tuan
- 链接：[arXiv](https://arxiv.org/abs/2611.33307) · [PDF](https://arxiv.org/pdf/2611.33307) · [HF](https://huggingface.co/papers/2611.33307)

Decision models are language models fine-tuned to return a probability for each option of a typed query, which routers and guardrails threshold directly. They are built on multilingual bases but ranked almost entirely in English. We evaluate 25 top-ranked open-weight decision models on 17 tasks in 14 languages, comparing each language with English on parallel items. Every model loses accuracy in every language, from…

## 62. When Does Reasoning Help Entity Disambiguation? Small LLMs In-Domain and Under Shift

- 分数：13.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：reasoning, reinforcement learning
- 作者：Samy Haffoudhi, Fabian M Suchanek, Nils Holzenberger
- 链接：[arXiv](https://arxiv.org/abs/2611.30334) · [PDF](https://arxiv.org/pdf/2611.30334) · [HF](https://huggingface.co/papers/2611.30334)

Entity disambiguation (mapping ambiguous mentions in text to entities in a knowledge base) is a foundational step in tasks such as knowledge graph construction, question answering, and information extraction. Recent work has applied LLMs to this problem, achieving stateof-the-art performance. Notably, reasoning LLMs have been shown to perform entity disambiguation in a true zero-shot fashion, generalizing across…

## 63. Change the Base, Change the Game: Rethinking Pan-sharpening

- 分数：13.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：evaluation, spec
- 作者：Jeonghyeok Do, Geunhyuk Youk, Munchurl Kim
- 链接：[arXiv](https://arxiv.org/abs/2611.32002) · [PDF](https://arxiv.org/pdf/2611.32002) · [HF](https://huggingface.co/papers/2611.32002)

Many pan-sharpening (PS) networks reconstruct high-resolution multispectral (HRMS) images by adding learned residuals to 4times-interpolated low-resolution multispectral (LRMS) inputs, incorporating panchromatic (PAN) detail only through these residual corrections. This raises a simple question: Why start with a blurry base when sharp spatial detail is already available? We propose PanBase, a sharper multispectral…

## 64. OmniPersist: Persistent Dynamic World Modeling via Coupled Panoramic Evolution

- 分数：13.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：benchmark, spec
- 作者：Zhilu Zhang, Xiaoyu Liu, Wenxi Liu, Shengfeng He
- 链接：[arXiv](https://arxiv.org/abs/2611.32473) · [PDF](https://arxiv.org/pdf/2611.32473) · [HF](https://huggingface.co/papers/2611.32473)

Action-conditioned world models play a vital role in robotics and autonomous driving, yet existing video diffusion models struggle to maintain dynamic object persistence. When the camera turns away and returns, out-of-view moving entities fail to evolve plausibly in latent space, often mutating or vanishing entirely due to bounded perspective views. To resolve this issue, we propose OmniPersist, a unified framework…

## 65. SPARC: Geometry-Guided Attention Pruning for Long-Horizon Camera-Controlled Video Generation

- 分数：13.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：memory, retrieval
- 作者：Zesong Yang, Weikai Chen, Liyuan Cui, Yuan Li, Jiaxin Huang, Lutao Jiang, Runze Zhang, Yingda Yin, Xiaoyang Huang, Kai Yan, Keyang Luo, Xin Wang, Hujun Bao, Zhaopeng Cui
- 链接：[arXiv](https://arxiv.org/abs/2611.34064) · [PDF](https://arxiv.org/pdf/2611.34064) · [HF](https://huggingface.co/papers/2611.34064)

We present SPARC, a geometry-guided attention pruning framework that turns the native self-attention of pretrained video diffusion transformers into a unified mechanism for camera control and persistent scene memory. Our key insight is that attention connectivity can simultaneously serve as geometric conditioning for camera control and spatial addressing for historical memory retrieval. Motivated by the asymmetric…

## 66. Demystifying the Autoresearch Harness: How Context and Skills Shape Self-Evolving Agents

- 分数：12.5  ·  HF 赞：5  ·  来源：huggingface
- 兴趣命中：agent
- 作者：Kelvin Kiu-Wai Tam, Newt Hue-Nam K. Nguyen, Tianshi Zheng, Yunxiang Mo, Weihan Li, Zhongwei Xie, Chiu Yeung Tang, Jui-Yu Ho, Yangqiu Song, Ginny Y. Wong, Simon See
- 链接：[arXiv](https://arxiv.org/abs/2611.28244) · [PDF](https://arxiv.org/pdf/2611.28244) · [HF](https://huggingface.co/papers/2611.28244)

Autoresearch agents, which autonomously design, run, and refine experiments, are accelerating scientific progress, particularly in AI research. However, existing agents rely on harnesses that combine multiple mechanisms, making it difficult to determine how individual components contribute to performance. We systematically study harness design for long-horizon, self-evolving autoresearch agents along two dimensions:…

## 67. Guarding with Judgment: Learning to Intervene for Multimodal Safety

- 分数：12.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：benchmark, spec
- 作者：Jipei He, Cheng Cheng, Liuguo Wang, Zihan Wen, Changlin Yu, Wentao Song, Suyun Zhao
- 链接：[arXiv](https://arxiv.org/abs/2611.28849) · [PDF](https://arxiv.org/pdf/2611.28849) · [HF](https://huggingface.co/papers/2611.28849)

When visual context makes an ordinary request unsafe to answer as asked, a blanket refusal may leave the user's need unresolved. Choosing how to help requires distinguishing an established hazard from a condition that still needs verification, a distinction that binary safety labels leave unspecified. We formulate this decision through four actions: allow, warn, review, and refuse. To ground these decisions in…

## 68. Speak When You See It: Proactive Task Assistants Should Wait for Evidence, Not the Clock

- 分数：12.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：benchmark
- 作者：Bohe Chen
- 链接：[arXiv](https://arxiv.org/abs/2611.30895) · [PDF](https://arxiv.org/pdf/2611.30895) · [HF](https://huggingface.co/papers/2611.30895)

Proactive assistants that guide people through physical tasks must decide, every few seconds, whether a step is complete and whether a mistake has occurred. We find that two benchmarks for this task largely reward knowing when rather than seeing what: a timer that never looks at the video, raising an alarm at 25 s and confirming each step at 30 s, reaches a mistake F1 of 0.373 on Ego-MC-Bench, above every published…

## 69. DexEngine: Scaling Human Demonstrations into Physically Executable Whole-Robot Data

- 分数：12.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：reinforcement learning
- 作者：Wongyun Yu, Honggeun Kim, Donguk Lee, Minchan Kim, Kyoung Whan Choe, Minsu Cho
- 链接：[arXiv](https://arxiv.org/abs/2611.33579) · [PDF](https://arxiv.org/pdf/2611.33579) · [HF](https://huggingface.co/papers/2611.33579)

A growing body of recent work addresses the retargeting of human hand-object demonstrations to robotic hands. To train whole-robot policies, however, the retargeted motions must be kinematically feasible and physically executable, and be produced efficiently at scale. We present DexEngine, a simulation pipeline that turns human manipulation data into train-ready, physically executable arm-hand trajectories.…

## 70. Who Makes the Decision? Auditing an Agentic LLM Pipeline for Illicit Cryptocurrency Transaction Monitoring

- 分数：12.0  ·  HF 赞：0  ·  来源：huggingface
- 兴趣命中：agent, retrieval
- 作者：Vaishnavi Chaughule, Yuchen Zhang, Mohammed Ahnaf Tajwar, Sai Akshay Menta, Saanidhya Vats, Vinija Jain, Aman Chadha, Divya Chaudhary
- 链接：[arXiv](https://arxiv.org/abs/2611.29829) · [PDF](https://arxiv.org/pdf/2611.29829) · [HF](https://huggingface.co/papers/2611.29829)

Agentic pipelines that combine graph detectors, deterministic rules, retrieval-augmented generation and an LLM judge are being proposed to monitor illicit cryptocurrency flows and to write regulation-citing justifications for analysts. They are evaluated on end-to-end accuracy or on the quality of those justifications, and neither shows which component made a decision. We audit such a pipeline on the Elliptic++…

## 71. Look Back: Reinforcement Learning with Counterfactual World Models

- 分数：12.0  ·  HF 赞：0  ·  来源：huggingface
- 兴趣命中：agent, reinforcement learning
- 作者：Jinwoo Kim, Toghrul Abbasov, Lucius E. J. Bynum, Aahlad Puli, Stephanie Milani, Hyunwoo Ryu, Seunghoon Hong, Kyunghyun Cho, Rajesh Ranganath
- 链接：[arXiv](https://arxiv.org/abs/2611.29259) · [PDF](https://arxiv.org/pdf/2611.29259) · [HF](https://huggingface.co/papers/2611.29259)

Agents in complex, stochastic environments must contend with dynamics that can exceed their world models' predictive capacity and randomness that obscure the consequences of their actions. We hypothesize that, compared to imagining entirely new trajectories in such complex environments, it can be easier to transform observed trajectories with alternative actions. Counterfactual world models condition on observations…

## 72. When an AI agent makes a mistake in a database, what decides the damage?

- 分数：11.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：agent
- 作者：Abdullah Kaya, Cevheri Bozoglan, Yusuf Gundogdu
- 链接：[arXiv](https://arxiv.org/abs/2611.30483) · [PDF](https://arxiv.org/pdf/2611.30483) · [HF](https://huggingface.co/papers/2611.30483)

AI agents now run statements against production databases, and several of the incidents that followed deleted production data, which came back only through backups or the provider's help. We ask what decides the damage when such an agent makes a mistake: the model, a guard layer in front of the database, or the database engine itself. The study has two preregistered layers. In Layer A, a frozen library of 22…

## 73. SIA: Selective Image Analogy

- 分数：11.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：evaluation
- 作者：Amirhossein Alimohammadi, Kian Izadpanah, Bardiya Kariminia, Yiorgos Chrysanthou, Ali Mahdavi-Amiri
- 链接：[arXiv](https://arxiv.org/abs/2611.33894) · [PDF](https://arxiv.org/pdf/2611.33894) · [HF](https://huggingface.co/papers/2611.33894)

Image analogy transfers a demonstrated transformation from a before/after pair (A, A') to a new query image B. Existing methods assume all changes in (A, A') should be fully transferred, limiting flexibility when users want only a subset of the demonstrated edits. We introduce Selective Image Analogy (SIA), a new setting where a single demonstration pair encodes multiple edits, and the user selects at inference time…

## 74. So Many Ways to Multiply 3times3 Matrices: A Large Dataset of Rank-23 Schemes

- 分数：10.0  ·  HF 赞：0  ·  来源：huggingface
- 兴趣命中：spec
- 作者：Andrew Igorevich Perminov
- 链接：[arXiv](https://arxiv.org/abs/2611.31155) · [PDF](https://arxiv.org/pdf/2611.31155) · [HF](https://huggingface.co/papers/2611.31155)

A publicly available dataset of 62029 rank-23 schemes for 3times3 matrix multiplication is presented. Every scheme in it has its own rank pattern, an invariant formed by the ranks of the factor matrices of a scheme, so all schemes are pairwise inequivalent. The schemes were obtained by a numerical method combining gradient descent with alternating least squares and by flip graph search, and have ternary, integer or…

## 75. Pretrained Tabular Features and the Measurement of Financial Proximity

- 分数：10.0  ·  HF 赞：0  ·  来源：huggingface
- 兴趣命中：benchmark
- 作者：Marcus Gawronsky
- 链接：[arXiv](https://arxiv.org/abs/2611.31491) · [PDF](https://arxiv.org/pdf/2611.31491) · [HF](https://huggingface.co/papers/2611.31491)

Spatial arbitrage pricing theory (S-APT) extends factor models to allow returns to spill over between connected firms, beyond what common risk factors explain. In recent years, tabular foundation models (TFMs) have matched or outperformed tuned gradient-boosted and bagged ensembles on small and medium-sized tabular benchmarks. Although their predictive performance is strong, these models reveal little about what…

## 76. Did the Model Forecast It, or Already Know It? Evaluating Large Language Models for Novel Drug-Target Prioritisation with a Temporal Knowledge-Graph Oracle

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, language model, large language, retrieval
- 作者：Pui Chung Siu, Yuan Liang, Claudia Cabrera, Mani Mudaliar, Arkaitz Zubiaga
- 链接：[arXiv](https://arxiv.org/abs/2611.34247) · [PDF](https://arxiv.org/pdf/2611.34247) · [HF](https://huggingface.co/papers/2611.34247)

AI systems increasingly help decide which drug targets enter costly clinical trials. We recast each target-disease hypothesis as a dated event, the pair's first clinical trial. This lets us test whether a language model can forecast such events after its training cutoff, rather than recall events before it. We rebuild a dated biomedical knowledge graph as it stood at the end of each year from 2020 up to its newest…

## 77. Navigent: A Geometry-Grounded Agentic Framework for Vision Language Navigation

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, memory, language model, large language, spec
- 作者：Xinyu Zhou, Weiren Cai, Yitong Chen, Shenghai Yuan, Zihang Mu, Boyu Ma, Jiahua Dong, Yanshuo Lu, Jiaqi Bai, Jianfei Yang
- 链接：[arXiv](https://arxiv.org/abs/2611.34249) · [PDF](https://arxiv.org/pdf/2611.34249) · [HF](https://huggingface.co/papers/2611.34249)

Vision-and-Language Navigation (VLN) with general-purpose multimodal large language models (MLLMs) offers a flexible alternative to task-specific navigation policies, while reliable long-horizon execution remains challenging. Agents must track navigation progress, detect discrepancies between commanded and actual motion, and recognize when movement has passed relevant landmarks or entrances. We present Navigent, an…

## 78. MedSkill-E$^{2}$: Evaluating and Evolving Skills for Medical Agents

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, benchmark, language model, large language, spec
- 作者：Jingjing Hua, Shaocong Wei, Jianghan Shen, Junzhi Ning, Min Cen, Cheng Tang, Ziyan Huang, Jiepeng Li, Fengshuo Liu, Kangkun Mao, Mouxiao Bian, Yirong Chen, Ming Hu, Jiyao Liu
- 链接：[arXiv](https://arxiv.org/abs/2611.34250) · [PDF](https://arxiv.org/pdf/2611.34250) · [HF](https://huggingface.co/papers/2611.34250)

Large language model (LLM) agents increasingly use skills to access domain knowledge and complete real-world tasks. We observe that even when a skill specifies the rules and procedures needed for a task, agents may fail to apply them effectively during autonomous execution, a phenomenon we call skill Enable But Underuse (EBU). This issue is particularly consequential in medical tasks, where overlooking a single…

## 79. Crucible: Evaluating LLM Agents in Executable Chemistry Research Environments

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, benchmark, language model, large language, spec, planning
- 作者：Yinjun Liu, Xinye Li, Ruisen Peng, Lang Gao, Zixiang Xu, Zirui Song, Xiuying Chen
- 链接：[arXiv](https://arxiv.org/abs/2611.34254) · [PDF](https://arxiv.org/pdf/2611.34254) · [HF](https://huggingface.co/papers/2611.34254)

Large language models (LLMs) perform well on chemistry knowledge benchmarks, which mainly assess question answering and isolated tasks. Chemical research, however, requires using specialized tools and interpreting their outputs to obtain chemically valid results. To address this gap, we introduce Crucible Bench to evaluate this ability across all four stages of the design-make-test-analyze (DMTA) cycle. The…

## 80. Latent-in-the-Middle: On the Security of Cross-Model Latent Communication in Multi-Agent Systems

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, benchmark, language model, large language
- 作者：Manit Baser, Vyoman Jain, Rachel Yeo Hui Min, Xianglin Yang, Meenatchi Sundaram Muthu Selva Annamalai, Dinil Mon Divakaran
- 链接：[arXiv](https://arxiv.org/abs/2611.34278) · [PDF](https://arxiv.org/pdf/2611.34278) · [HF](https://huggingface.co/papers/2611.34278)

As large language models increasingly collaborate in heterogeneous multi-agent systems, latent communication has emerged as an efficient alternative to exchanging natural-language messages. By sharing internal representations, agents can avoid repeatedly processing the same context, reducing communication overhead and prefill computation. One such mechanism is cross-model Key-Value (KV) cache transfer, which uses a…

## 81. WebVibe: Multimodal Interactive Website Generation via Reverse Synthesis and Visual Self-Distillation

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reinforcement learning, language model, large language, coding, spec
- 作者：Tianxiang Jiang, Sheng Xia, Yilin Long, Kanghui Tian, Linquan Wu, Yongheng Zhang, Daixian Liu, Di Yin, Yi Wang, Yu Qiao, Qinglong Zhang
- 链接：[arXiv](https://arxiv.org/abs/2611.34292) · [PDF](https://arxiv.org/pdf/2611.34292) · [HF](https://huggingface.co/papers/2611.34292)

Although multimodal large language models translate single screenshots into static HTML, generating interactive functional websites from design specifications still struggles with multi-page routing and stateful widget transitions. Examining existing training pipelines reveals two bottlenecks: (1) in forward data synthesis (X -> Y), writing the specification X before code execution leaves unimplemented or altered…

## 82. MeterRouter: Budget-Aware Dynamic Routing for Multi-Agent Systems

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, benchmark, language model, large language, spec
- 作者：Yue Xu, Leikun Yin, Ruiming Min, Yufeng Lai, Justin Andrew Johnson, Sitao Luan, Xiaotong Shen
- 链接：[arXiv](https://arxiv.org/abs/2611.34327) · [PDF](https://arxiv.org/pdf/2611.34327) · [HF](https://huggingface.co/papers/2611.34327)

Multi-agent systems (MAS) built on large language models (LLMs) outperform single-agent systems, but inter-agent communication incurs substantial token overhead. While assigning a large LLM to every agent is common, it results in inefficient resource utilization, leaving the system far from the Pareto frontier. The cost of answering a query is set jointly by how many agents are recruited, the role and LLM assigned…

## 83. LUDIUS: A Benchmark for Embodied Social Intelligence in Everyday Human-Robot Interactions

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, language model, spec
- 作者：Chaewon Kim, Sangheon Lee, Seyeon Choi, Kangwook Lee, Yea Seul Kim
- 链接：[arXiv](https://arxiv.org/abs/2611.34328) · [PDF](https://arxiv.org/pdf/2611.34328) · [HF](https://huggingface.co/papers/2611.34328)

Social intelligence in a robot requires interpreting a situation from the perspectives of the people involved and using that understanding to decide when and how to act. We introduce LUDIUS, a benchmark for evaluating how vision-language models exercise this judgment through a robot's verbal responses and actions, organized around 15 social intelligence skills drawn from social psychology, sociology, and cognitive…

## 84. ConTra: A Training Framework for Effective Contextual Retrieval via Prefix Generation

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reinforcement learning, benchmark, spec, retrieval
- 作者：Jiajun Hou, Jingbang Chen
- 链接：[arXiv](https://arxiv.org/abs/2611.34366) · [PDF](https://arxiv.org/pdf/2611.34366) · [HF](https://huggingface.co/papers/2611.34366)

Data management systems organize large text collections for tasks such as finding relevant studies and extracting contract clauses. Systems make long documents searchable by splitting them into independently indexed chunks. Chunking can separate text from its identifying details. The indexing challenge is to keep each chunk independently searchable while preserving the context needed to find and rank it. Existing…

## 85. EvoLink-Bench: A Benchmark for Evaluating Self-Evolving Agents in Long-Horizon Interdependent Task Streams

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, evaluation, benchmark, language model, large language
- 作者：Wei Chen, Xiaodong Lu, Weihao Shen, Gongxun Li, Xingyu Guo, Qihang Sun, Fuwei Zhang, Zhao Zhang, Yikun Ban, Shuang Li, Deqing Wang, Fuzhen Zhuang
- 链接：[arXiv](https://arxiv.org/abs/2611.34400) · [PDF](https://arxiv.org/pdf/2611.34400) · [HF](https://huggingface.co/papers/2611.34400)

Large language model (LLM) agents are evolving from passive chatbots into autonomous systems that operate continuously in dynamic environments. Such agents need not only solve current tasks but also learn from past interactions to improve future performance. However, existing streaming benchmarks often rely on short task sequences or largely independent tasks, providing limited evidence of whether agents can…

## 86. Agentic Waterfall: An Intent-Driven Information Discovery Framework for Reclaiming User Control in the Attention Economy

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, evaluation, benchmark, retrieval
- 作者：Yige Luo, Shining Zhang, Jikun Liu, Hongjiao Qiang, Ran Guan
- 链接：[arXiv](https://arxiv.org/abs/2611.34407) · [PDF](https://arxiv.org/pdf/2611.34407) · [HF](https://huggingface.co/papers/2611.34407)

We formalize Agentic Waterfall Feed, a new problem of personalized information discovery in which users actively direct recommendations and the system adapts to evolving needs inferred from both explicit requests and browsing behavior. We address this problem with the Agentic Waterfall framework, whose language-model controller maintains persistent user state and coordinates content retrieval, ranking, and state…

## 87. Mitigating Hallucinations in Medical Question Answering on ESC Cardiology Guidelines: Evaluation and Retrieval Optimization

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, language model, large language, retrieval
- 作者：Ilkin Masimov, Rufana Baghirli, Muhammad Rashid
- 链接：[arXiv](https://arxiv.org/abs/2611.34427) · [PDF](https://arxiv.org/pdf/2611.34427) · [HF](https://huggingface.co/papers/2611.34427)

Background: Large language models produce hallucinations in medical question answering (QA). Verify-and-revise pipelines that check atomic claims against retrieved guideline evidence are a standard mitigation, but evaluations almost universally treat the verifier's output as ground truth, an assumption rarely tested. Objective: To measure, claim by claim against human judgement, how such a pipeline fails in a…

## 88. Evaluating Aviation Safety Knowledge Extraction with SmolLM2: From Zero-Shot to Retrieval-Grounded Prompting

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, spec, retrieval
- 作者：Aziida Nanyonga, Mustafa Tahsin Yilmaz, Amir Hussain, Ugur Turhan, Graham Wild
- 链接：[arXiv](https://arxiv.org/abs/2611.34432) · [PDF](https://arxiv.org/pdf/2611.34432) · [HF](https://huggingface.co/papers/2611.34432)

Aviation accident narratives contain safety knowledge that is difficult to capture using structured occurrence fields alone. This study evaluates prompting-based knowledge extraction across four dimensions: concept accuracy, verbatim evidence grounding, structural compliance, and directed relation extraction. SmolLM2-1.7B-Instruct was evaluated under zero-shot, one-shot, fixed few-shot, and retrieval-grounded…

## 89. vSFT: Learning to Verbally Tune Agents at Test Time

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reinforcement learning, language model, large language, spec
- 作者：Qishuai Wen, Rui Chen, Haiwen Li, Zhiyuan Huang, Qiwen Gu, Bingjie Gao, Geng Li, Jing Tang, Xiangxiang Chu, Chun-Guang Li
- 链接：[arXiv](https://arxiv.org/abs/2611.34440) · [PDF](https://arxiv.org/pdf/2611.34440) · [HF](https://huggingface.co/papers/2611.34440)

Large language model agents are increasingly improved via agentic reinforcement learning, which can be on-policy but suffers from expensive rollouts and sparse rewards, limiting its application at test time. In this paper, we present a verbally Supervised Fine-Tuning (vSFT) framework that enables the conjunction of dense feedback in natural language and weight updates at test time. Specifically, our vSFT forms a…

## 90. TACC: Target-Aware Carrier Compression for Dense-Context Novel View Synthesis

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, coding, spec, retrieval
- 作者：Yiming Fan, Yijia Guo, Zewen Guo, Liwen Hu, Yuheng Yuan, Yang Li, Zhiwei Li, Xitong Ling, Caihong Yuan, Shengbo Chen, Tiejun Huang, Lei Ma
- 链接：[arXiv](https://arxiv.org/abs/2611.34476) · [PDF](https://arxiv.org/pdf/2611.34476) · [HF](https://huggingface.co/papers/2611.34476)

Recent feed-forward approaches mark a paradigm shift in novel view synthesis by eliminating the reliance on per-scene optimization, directly inferring 3D representations from input views. However, their reliance on global scene-token context incurs substantial memory and latency overhead, constraining their ability to handle increasingly dense source-view contexts. Compressing source representations offers an…

## 91. FlyingStart: Learned Cross-Token Warm Starts for Fixed-Point Decoding in Recurrent-Depth Language Models

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, language model, coding, spec
- 作者：Runguo Li, Dezhen Lu, Zixiang Ni
- 链接：[arXiv](https://arxiv.org/abs/2611.34492) · [PDF](https://arxiv.org/pdf/2611.34492) · [HF](https://huggingface.co/papers/2611.34492)

Recurrent-depth language models generate each token by iterating a shared block of layers until its hidden state converges. Inference methods for these models decide when to stop the iteration, yet every token still starts from random noise and pays the full cost of converging. We show that where the iteration starts is a second, independent lever. A token's fixed point is predictable from the state at which the…

## 92. AliceAI-Foundation-80B-A3B-Base

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reasoning, evaluation, benchmark, language model, spec
- 作者：Nikolay Skachkov, Ekaterina Redina, Maksim Konoplev, Evgenii Uskov, Veronika Zykova, Ivan Tsarikov, Artemii Zakharov, Mariia Godunova, Dmitrii Lunin, Maria Nikiforova, Valerii Levanov, Anton Kalsin, Daniil Panteleev, Alexey Gerasev, Ilia Kopytin, Yermek Kapushev, Egor Liakhov, Irina Lialikova, Tatiana Taekina, Anastasia Volotova, Assol Kubaeva, Kirill Alekseev, Pavel Otlivanchik, Mukhammadfirdavs Kosimov, Vladislav Negodin, Ivan Vinogradov, Anton Andriushchenko, Maksim Nikitin, Daniil Sukhoi, Alexander Mazitov, Maksim Abraham, Philip Zmushko, Maksim Ignatov, Ivan Sapozhkov, Timofey Byzov, Edgar Shmavonian
- 链接：[arXiv](https://arxiv.org/abs/2611.34529) · [PDF](https://arxiv.org/pdf/2611.34529) · [HF](https://huggingface.co/papers/2611.34529)

We present AliceAI-Foundation-80B-A3B-Base, a mixture-of-experts language model with 80 billion total parameters and approximately 3 billion active parameters per token, trained from scratch at Yandex and released under the Apache 2.0 license. The model combines Kimi Delta Attention with full attention, uses Attention Residuals, and is trained with Muon. Training comprises general pretraining on 17.5 trillion…

## 93. EPPC-CARE: Staged Hierarchical Annotation of Communication Behaviors in Secure Patient-Provider Messages

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, language model, large language, spec
- 作者：Samah Fodeh, Sreeraj Ramachandran, Ganesh Puthiaraju, Sarah Schellhorn
- 链接：[arXiv](https://arxiv.org/abs/2611.34539) · [PDF](https://arxiv.org/pdf/2611.34539) · [HF](https://huggingface.co/papers/2611.34539)

Objectives: Patient portal messages provide invaluable information about communication dynamics between patients and healthcare providers, but extracting it manually is labor-intensive. We developed and evaluated EPPC-CARE, an automated framework for identifying communication behaviors together with the supporting text for each classification. Materials and Methods: From 867 messages, we obtained 5,516 reference…

## 94. Recalling the Past to Answer the Present: Context-Aware Multi-Evidence Reasoning for Streaming Video Question Answering

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, reasoning, benchmark, language model
- 作者：Cui Yakun, Tiantian Geng, Huixiang Kong, Xingqun Qi, Sirui Han, Yike Guo
- 链接：[arXiv](https://arxiv.org/abs/2611.34545) · [PDF](https://arxiv.org/pdf/2611.34545) · [HF](https://huggingface.co/papers/2611.34545)

Vision-language models (VLMs) have achieved remarkable progress in video understanding, yet existing video question answering (VQA) benchmarks mainly evaluate models in offline settings. Real-world streaming scenarios instead require models to answer context-dependent queries by retrieving and reasoning over evidence distributed across the video history. We introduce StreamRecall, a benchmark for context-aware Multi…

## 95. Compact Vision-Language Navigation in Continuous Environmentsvia On-Policy Training and Route-Bearing Output

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, memory, language model, coding
- 作者：Reshad Ul Karim, Syeda Maliha Tabassum, Md. Khalilur Rhaman, Md Rashad Al Hasan Rony
- 链接：[arXiv](https://arxiv.org/abs/2611.34561) · [PDF](https://arxiv.org/pdf/2611.34561) · [HF](https://huggingface.co/papers/2611.34561)

Instruction-following robots need navigation policies that reach high accuracy and remain inexpensive to train and to run on a single graphics processing unit (GPU). The most accurate vision-language navigation policies for continuous environments rely on language models with 4 to 8 billion parameters, long observation histories, and large auxiliary corpora. Two properties of the standard training setup limit…

## 96. Procedure Inference as Memory: Learning Recruiter Decision Procedures from OKF-Structured Episodes in Multi-Session Hiring Assistants

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, reasoning, reinforcement learning, evaluation, retrieval
- 作者：Praveen Kumar Bodigutla, Yizhi Zhang, Sai Vivek Kanaparthy, Arup De
- 链接：[arXiv](https://arxiv.org/abs/2611.34576) · [PDF](https://arxiv.org/pdf/2611.34576) · [HF](https://huggingface.co/papers/2611.34576)

Multi-session hiring assistants must infer evolving recruiter preferences and decision patterns across projects and time. We introduce Open Knowledge Format (OKF)-indexed episodic memory to organize interactions and retrieve related events through their lineage. We also introduce Procedure Memory, which learns reusable decision procedures from these episodes through prompted reflection or reinforcement learning. We…

## 97. ADClaw: A Programmable Visual Agent for Industrial Anomaly Detection and Understanding

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reasoning, benchmark, language model, spec
- 作者：Xinyi Wu, Rongxin Gao, YuHui Lin, Yonglin Hong, Chu Li, Wei Li, Dingzhao Li, Shijia Zhao, Chaopeng Li, Haixin Sun
- 链接：[arXiv](https://arxiv.org/abs/2611.34591) · [PDF](https://arxiv.org/pdf/2611.34591) · [HF](https://huggingface.co/papers/2611.34591)

Industrial anomaly detection (IAD), the task of identifying and localizing deviations from normal product conditions, is essential to automated quality inspection in manufacturing. Many vision-language models for IAD rely on large domain-specific datasets for fine-tuning and make predictions in a single pass, leaving no opportunity to re-examine ambiguous regions. Although tool-using agents can revisit these…

## 98. SEAM: A Self-Evolving and Adaptive Probing Framework for Automatic MLLM Hallucination Evaluation

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, language model, large language, spec
- 作者：Shiyu Zhang, Zengyi Wo, Yuming Liao, Ran He, Caifeng Shan, Yanbo Fan
- 链接：[arXiv](https://arxiv.org/abs/2611.34598) · [PDF](https://arxiv.org/pdf/2611.34598) · [HF](https://huggingface.co/papers/2611.34598)

The severe susceptibility of multimodal large language models (MLLMs) to hallucinations poses a critical threat to their reliability, making a rigorous evaluation framework indispensable. However, existing evaluation pipelines largely rely on predefined test items, suffering from high construction costs, rapid obsolescence as MLLMs evolve, and ineffectiveness in probing model-specific weaknesses. To address these…

## 99. VisualMontage: Manipulating the Beliefs of Vision-Language Agents with Authentic Image Sequences

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reasoning, evaluation, benchmark, language model, spec, planning
- 作者：Jinwei Hu, Lai Wei, Zhuoyun Li, Youcheng Sun, Yi Dong, Xiaowei Huang
- 链接：[arXiv](https://arxiv.org/abs/2611.34603) · [PDF](https://arxiv.org/pdf/2611.34603) · [HF](https://huggingface.co/papers/2611.34603)

As agents based on vision-language models (VLMs) increasingly interpret social-media content, errors in their analysis may lend credibility to rumors and amplify their spread. In this paper, we study the problem of visual cognitive collusion, in which coordinated posts combine authentic images and locally faithful captions to induce VLM agents to infer and accept attacker-chosen target claims through their own…

## 100. HoMe: Toward Practical Harness Optimization of Memory Systems for AI Assistants

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, memory, evaluation, benchmark, retrieval
- 作者：Yifei Xu, Li Yu, Zhaoyang Liu, Ce Wang, Sen Huang, Yanyan Shen, Yun Lin, Linpeng Huang, Hong Mei
- 链接：[arXiv](https://arxiv.org/abs/2611.34624) · [PDF](https://arxiv.org/pdf/2611.34624) · [HF](https://huggingface.co/papers/2611.34624)

The behavior of memory systems for long-running AI assistants is governed by a harness, which consists of the code, prompts, and configurations for memory construction, maintenance, retrieval, and answer generation. However, optimizing the harness of a memory system remains largely manual, and unrestricted editing alone does not ensure structural improvements. In this paper, we introduce HoMe, an evaluation-driven…

## 101. ZeroHero: Training Small Language Agents from Scratch

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reasoning, language model, large language, spec
- 作者：Nikita Sorokin, Zoya Volovikova, Alexey Skrynnik, Aleksandr Panov
- 链接：[arXiv](https://arxiv.org/abs/2611.34635) · [PDF](https://arxiv.org/pdf/2611.34635) · [HF](https://huggingface.co/papers/2611.34635)

Large pretrained language models provide capable policies for interactive tasks, but how much model capacity is necessary for a specialized language agent? We introduce ZeroHero, a framework for training small language agents (SLAs) from scratch. In each environment, a large language model acts as the expert, and we collect its successful trajectories. We pretrain each SLA, which has fewer than 50 million…

## 102. Do We Still Need Reinforcement Learning When We Can Read the World Model?

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reasoning, reinforcement learning, benchmark, coding, spec, planning
- 作者：Mingchao Zhang, Miduo Cui, Kangze He, Yuanjun Li, Dapeng Li, Ce Zhang, Chuanchen Luo, Xue Yan, Mingzhe Xing, Zhumin Chen, Hangyu Mao, Bin Zhang, Zhiwei Xu
- 链接：[arXiv](https://arxiv.org/abs/2611.34656) · [PDF](https://arxiv.org/pdf/2611.34656) · [HF](https://huggingface.co/papers/2611.34656)

Reinforcement learning has achieved remarkable success in sequential decision-making, but learning effective policies often requires substantial interaction experience. Model-based reinforcement learning alleviates this dependence by leveraging world models, which are typically used to support planning or policy optimization. In this paper, we investigate an alternative paradigm in which autonomous LLM-based coding…

## 103. Find the Clue, Not the Scene: Rethinking Reasoning for Entity Recognition in Vision-Language Models

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, reinforcement learning, benchmark, language model, spec
- 作者：Kyungmin Min, Soyeon Kim, Junseok Kim, Kyomin Jung
- 链接：[arXiv](https://arxiv.org/abs/2611.34681) · [PDF](https://arxiv.org/pdf/2611.34681) · [HF](https://huggingface.co/papers/2611.34681)

Answering a knowledge-based visual question requires first recognizing the entity in the image and then recalling knowledge about it. Thinking vision-language models (VLMs) reason for thousands of tokens before answering, yet it remains underexplored how well such thinking VLMs perform each of these two steps. We therefore analyze thinking VLMs on this task and make two key observations. (1) Recognition is the…

## 104. Maco-RL: Scaling Agent Capabilities with Mixed-Task Reinforcement Learning

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reinforcement learning, benchmark, spec
- 作者：Jiacheng Zhang, Qixing Zhou, Haiyang Wang, Qipeng Gu, Shuzhe Wu, Feiyang Pan, Lue Fan, Dandan Tu, Zhaoxiang Zhang
- 链接：[arXiv](https://arxiv.org/abs/2611.34703) · [PDF](https://arxiv.org/pdf/2611.34703) · [HF](https://huggingface.co/papers/2611.34703)

Mixed-task reinforcement learning (MixRL) directly trains a unified policy across domains to continually expand agent capabilities without training separate specialists or requiring an extra distillation stage. Despite its appeal, scaling MixRL poses significant challenges in achieving stable and efficient mixed-task learning, effectively allocating rollout compute, and supporting continual domain expansion. To…

## 105. From Shared Patterns to Individual Evidence: Two-Stage Reasoning for Emerging Entities in Temporal Knowledge Graphs

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, reasoning, evaluation, benchmark
- 作者：Jinchuan Zhang, Lei Gao, Hongyu Jiang, Chong Mu, Chenang Cai, Ke Yan
- 链接：[arXiv](https://arxiv.org/abs/2611.34708) · [PDF](https://arxiv.org/pdf/2611.34708) · [HF](https://huggingface.co/papers/2611.34708)

Temporal knowledge graphs (TKGs) continually introduce emerging entities whose interaction histories evolve from zero-shot debuts into sparse, bursty few-shot trajectories. However, current paradigms are fragmented: pattern-transfer methods lack catalog-wide event memory, whereas online memory models suffer from endpoint-role asymmetry that degrades unseen-answer ranking. Furthermore, sparse early interactions…

## 106. Make the Adversary Spend More: Stateful Deception as a Cost-Exchange Primitive for AI-Era Cyber Defense

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, language model, large language, spec
- 作者：Alessandro Cantelli-Forti, Isabella Marasco, Hosam Alamleh, Giada Boschi, Michele Colajanni
- 链接：[arXiv](https://arxiv.org/abs/2611.34770) · [PDF](https://arxiv.org/pdf/2611.34770) · [HF](https://huggingface.co/papers/2611.34770)

Large language models (LLMs) are transforming the economics of intrusion by reducing the attacker's cost to scan and adapt, while tempting defenders into unbounded compute. We argue that cyber deception should be judged by the cost exchange it imposes, not by realism or detection, and that the primitive making that exchange favorable is adversary-specific persistent state. Rather than a honeypot that resets or…

## 107. DFly2: Turbocharging Long-Context Speculative Decoding by Sharing the Target's Sparsity

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, memory, long context, benchmark, coding, spec
- 作者：Hong Liu, Rui Cen, Junhan Shi, Lin Niu, Runzhi Fan, Zhaojing Zhou, Haodi Lei, Jiebin Zhang, Saiyong Yang, Junqiang Zheng, Zhenghai Xue, Guanghua Yu, Jianchen Zhu
- 链接：[arXiv](https://arxiv.org/abs/2611.34776) · [PDF](https://arxiv.org/pdf/2611.34776) · [HF](https://huggingface.co/papers/2611.34776)

To avoid the quadratic cost of dense attention over long contexts, models such as DeepSeek-V4 and Hy4 have turned natively sparse, and speculative decoding, which matters most where decoding is slowest, increasingly runs on them. Their drafters, however, still keep a context cache of their own, over the whole prompt or a sliding window. Beyond memory, such a cache costs prefill time, prefix-cache hits and decode…

## 108. PersonaFactory: Stylistic User Prompt Augmentation with Synthetic Persona Bank

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, language model, large language
- 作者：Bich Ngoc Doan, Hanna Yukhymenko, Imanol Schlag
- 链接：[arXiv](https://arxiv.org/abs/2611.34785) · [PDF](https://arxiv.org/pdf/2611.34785) · [HF](https://huggingface.co/papers/2611.34785)

Large language models increasingly replace real people in the AI development pipeline, as they are used to generate training dialogues at scale and to drive alignment and evaluation. However, out-of-the-box models produce monolingual and stylistically flat texts as synthetic user prompts, failing to replicate the real user-AI communication mechanics. We present PersonaFactory, an end-to-end pipeline that generates…

## 109. VulnSafe: Measuring Vulnerability-Aware Relational Safety in Large Language Models

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, language model, large language, spec
- 作者：Jiaming Luo, Jiacheng Ji, Haoan Jin, Xiaoning Sun, Qiuzhi Xiong, Yuxin Zhang, Hanhui Xu, Mengyue Wu
- 链接：[arXiv](https://arxiv.org/abs/2611.34819) · [PDF](https://arxiv.org/pdf/2611.34819) · [HF](https://huggingface.co/papers/2611.34819)

Emotionally supportive interactions require large language models not only to avoid overtly harmful content, but also to recognize vulnerability-related risk, regulate their relational stance, preserve user agency, and provide context-appropriate support. Existing safety benchmarks often measure isolated violations, leaving unclear what underlying response competence their scores represent. We introduce VulnSafe, a…

## 110. The Linguistic Knowledge Benchmark: Do Language Models Know the Foundations of Early-Grade Literacy?

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, language model, spec
- 作者：Maxime Lelièvre, Alasdair Mackintosh, Dominic Andrews, Tobias Murray, Moritz Boos, Oliver G. B. Garrod
- 链接：[arXiv](https://arxiv.org/abs/2611.34823) · [PDF](https://arxiv.org/pdf/2611.34823) · [HF](https://huggingface.co/papers/2611.34823)

Many languages of instruction in low- and middle-income countries (LMICs) are poorly represented in the data used to train language models. Before these models can support early-grade literacy in such languages, we need to know whether they hold the linguistic knowledge of each language that literacy teaching relies on. To test this, we present the Linguistic Knowledge Benchmark and the reproducible, largely…

## 111. Proverbs As A Window On Collective Prescriptions

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, language model, large language, spec
- 作者：Tomás Lejarraga, Dirk U. Wulff, Ralph Hertwig
- 链接：[arXiv](https://arxiv.org/abs/2611.34832) · [PDF](https://arxiv.org/pdf/2611.34832) · [HF](https://huggingface.co/papers/2611.34832)

Proverbs, as repositories of traditional wisdom, have informed human reasoning for millennia. Yet the collective prescriptions they encode have remained largely unquantified. We introduce a computational framework to analyze nearly 50,000 English-language proverbs. Using large language models, validated against human judgments, we map the topical landscape of proverbs, assess their prescriptive power, and quantify…

## 112. Put the World Back: Timestamps Matter in Time Series Reasoning

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, evaluation, benchmark, language model, large language, spec
- 作者：Tingrui Huang, Yuanyuan Deng, Qingren Yao, Joaquin Vanschoren, Mykola Pechenizkiy, Songgaojun Deng
- 链接：[arXiv](https://arxiv.org/abs/2611.34848) · [PDF](https://arxiv.org/pdf/2611.34848) · [HF](https://huggingface.co/papers/2611.34848)

Large language models (LLMs) are increasingly applied to time series reasoning. However, current evaluations often give models events in chronological order and already matched to the time series. This makes it unclear whether models use timestamps to connect events with observations or simply take shortcuts. To expose this ambiguity, we reformulate time series reasoning from a world-to-series projection…

## 113. Towards Closing the Performance Gap in Cross-Modal Place Recognition

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, language model, retrieval
- 作者：Ofer Idan, Dan Badur, Yoli Shavit
- 链接：[arXiv](https://arxiv.org/abs/2611.34877) · [PDF](https://arxiv.org/pdf/2611.34877) · [HF](https://huggingface.co/papers/2611.34877)

Cross-modal place recognition (CMPR) matches natural language descriptions against databases of geo-tagged reference images, enabling localization without visual queries. Despite its potential for language-guided navigation, existing vision-language models lag far behind visual place recognition (VPR) baselines, even after task adaptation. Unlike general-purpose text-to-image retrieval, place recognition relies on…

## 114. Stranger Things: When Objects Appear Without Their Typical Neighbors

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, language model, large language, spec
- 作者：Siddhartha Gairola, Jiahao Xie, Anna Kukleva, Francesco Locatello, Bernt Schiele
- 链接：[arXiv](https://arxiv.org/abs/2611.34881) · [PDF](https://arxiv.org/pdf/2611.34881) · [HF](https://huggingface.co/papers/2611.34881)

Visual context is a powerful cue for object recognition: scenes inform what, where, and at what scale objects are likely to appear. Yet over-reliance on context becomes a failure mode when models predict objects based on their typical neighbors rather than the objects' own visual features, which we call typicality bias. While extensively studied in the pre-Transformer era, it has often been assumed that…

## 115. Diverse Alternative Reasoning Traces for Hard Math Problems

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, evaluation, benchmark, language model, large language
- 作者：Lukas Aichberger, Adam Golinski, Arno Blaas, Arwen Bradley, Jacob Springer, Mehrdad Farajtabar, Michael Kirchhof, Sinead Williamson
- 链接：[arXiv](https://arxiv.org/abs/2611.34928) · [PDF](https://arxiv.org/pdf/2611.34928) · [HF](https://huggingface.co/papers/2611.34928)

Post-training large language models (LLMs) for mathematical reasoning often relies on accepted traces whose final answers pass a verifier. For hard math problems, however, such traces can be rare under independent Monte Carlo (MC) sampling. To address this, we propose Diverse Alternative Reasoning Traces (DART), a trace-mining method that starts from a rejected trace, decomposes it into reasoning steps, and ranks…

## 116. Attack Policy Selection can Mislead Monitor Evaluators

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reasoning, reinforcement learning, evaluation
- 作者：Charlie Griffin, Oliver Makins, Asa Cooper Stickland, Alessandro Abate, Yarin Gal, Abby D'Cruz, Xander Davies
- 链接：[arXiv](https://arxiv.org/abs/2611.34934) · [PDF](https://arxiv.org/pdf/2611.34934) · [HF](https://huggingface.co/papers/2611.34934)

AI monitors, classifiers that flag dangerous behaviour by AI agents, are often evaluated against transcripts generated by attack policies acting as proxies for dangerous behaviour in deployment. We evaluate an ex-production OpenAI monitor as a case study and find that measured false negative rate is highly sensitive to both the method used to generate attack policies and the level of optimisation applied within that…

## 117. Tracking Any Point with Agentic Visual Reasoning

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reasoning, language model, spec
- 作者：Xuweiyi Chen, Jin Yao, Linzhan Mou, Lei Gong, Di Liu, Cheng Zhang, Ziqiao Ma, Sihan Xu, Adam W. Harley, Shengyi Qian, Zezhou Cheng
- 链接：[arXiv](https://arxiv.org/abs/2611.34943) · [PDF](https://arxiv.org/pdf/2611.34943) · [HF](https://huggingface.co/papers/2611.34943)

A general-purpose Vision-Language Model (VLM) has surpassed expert vision models in many domains such as object detection and video recognition. However, point correspondence is known to be challenging for VLMs since it goes beyond object-level recognition: it requires pixel-level localization of the same physical surface point across observations, even when appearance changes or the point disappears and later…

## 118. Simulator-as-Proxy World Model for Robot Manipulation

- 分数：8.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：-
- 作者：Tingting Liao, Mingjia Huo, Hao Li, Zhengzhong Liu, Eric P. Xing, Guangyi Liu
- 链接：[arXiv](https://arxiv.org/abs/2611.32786) · [PDF](https://arxiv.org/pdf/2611.32786) · [HF](https://huggingface.co/papers/2611.32786)

Video world models for robots are increasingly conditioned on a simulated or rendered proxy of the scene, on the assumption that the video will show what the proxy shows. Testing this assumption requires a proxy whose state is explicit and can be perturbed. We present SimPWM (Simulator-as-Proxy World Model): given a calibrated camera, it represents, from the first frame alone, the robot by its 3D model and the…

## 119. Scaling Looped MoE Language Models under Matched Budgets: Information Flow and Parameter Allocation

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, language model, spec
- 作者：Shipeng Bai, Jiayu Qin, Hong Liu, Xili Wang, Jianchao Tan, Jiacheng Li, He Zhang, Yifan Lu, Jiaqi Zhang, Kefeng Zhang, Yuchen Xie, Xunliang Cai
- 链接：[arXiv](https://arxiv.org/abs/2611.34276) · [PDF](https://arxiv.org/pdf/2611.34276) · [HF](https://huggingface.co/papers/2611.34276)

Looped Transformers decouple computational depth from parameter count, and prior studies have demonstrated promising performance gains with increased computation. However, systematic design principles for configuring these models under strict iso-parameter and iso-FLOP constraints remain scarce. We contribute to this direction by improving information flow in looped models and systematically studying loop parameter…

## 120. RAP: Radial-Angular Random Projection for Hyperbolic Representations

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：language model, large language, retrieval
- 作者：Jiahong Liu, Wenhao Yu, Yifan Li, Yanyu Chen, Rex Ying, Menglin Yang, Irwin King
- 链接：[arXiv](https://arxiv.org/abs/2611.34298) · [PDF](https://arxiv.org/pdf/2611.34298) · [HF](https://huggingface.co/papers/2611.34298)

Random projection is a basic compression primitive for Euclidean representation learning, with the Johnson--Lindenstrauss lemma giving a target dimension $k=O(\varepsilon^{-2}\log n)$ independent of the ambient dimension. As hyperbolic representations gain increasing attention in modern Transformers, vision-language models, and large language models, the same need for oblivious dimensionality reduction arises, but…
