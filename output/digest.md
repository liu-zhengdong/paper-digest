# 每日 AI 论文

生成时间：2026-11-18 07:29 UTC  ·  共 120 篇（已按 arXiv ID 去重）

来源：Hugging Face Daily Papers + arXiv（cs.AI / cs.LG / cs.CL / cs.CV）。
排序：HF 上榜、点赞、多源命中、兴趣词。兴趣词可在 `config.json` 改。

## 1. TeleChat to Xing4: Advancing Frontier Agentic Models on Domestic Chips and Frameworks

- 分数：36.0  ·  HF 赞：131  ·  来源：huggingface
- 兴趣命中：agent, memory, reasoning, evaluation, language model, large language, coding, spec
- 作者：Xingchen AGI Lab, Baotian Hu, Bingkai Yang, Boyang Wang, Changzai Pan, Chao Lyu, Chao Wang, Chen Li, Chenshuo Pan, Chenyu Lin, Chenyuan Zhang, Chongming Liu, Dawei Fan, Di Wu, Dong Guo, Dong Li, Dongfang Li, Enlin Liu, Fanye Xiao, Fengkai Li, Fubei Yao, Gang Lin, Han Gao, Hanming Wu, Haowei He, Huapeng Liu, Hua Wang, Huinan Xu, Jiahong Xiong, Jiaxin Peng, Jianxiang Ma, Jianxing Zhuge, Jie Zhang, Ji Xiong, Jinglin Chen, Jingqi Li, Jingxuan Li, Jiwang Ye, Junchen Li, Junbiao Li, Junyang Wu, Kaidong Yu, Kaipeng Jia, Kehai Chen, Kuai Li, Laobin Liu, Lei Li, Libo Qin, Lingling Shi, Luwen Pu, Menghao Xu, Mengjiao Bao, Mengqi Chen, Min Zhang, Mingrui Wang, Naying Wang, Peicong Han, Peiming Guo, Pengfei Li, Qiang Feng, Qi Wang, Qingjun Zhu, Qingli Li, Qitai Ding, Qiyi Xie, Quanchao Zhao, Rongbao Han, Rui Xue, Ruiyu Fang, Ruiting Song, Shijie Li, Shiquan Wang, Shuangyong Song, Sishi Xiong, Teng Su, Wankang Bao, Weijie Zhang, Wei Mao, Weiwei Fu, Weiyang Huang, Wenmin Deng, Wenqing Hu, Wujie Zhong, Xi Yu, Xiaohui Hu, Xiaomin Fang, Xiaomeng Huang, Xiaoqiong Shi, Xiaotong Shang, Xiaoyu Li, Xinglei Xu, Xin Jiang, Xin Wang, Xin Zhang, Xinzhang Liu, Xue Liu, Xuefeng Bai, Xuewei He, Yahan Li, Yanhan Zhang, Yanlei Xue, Yanzhang Wu, Yang Yu, Yi Liu, Yin Zhang, Yingyan Li, Yitong Yao, Yixuan Li, Yongqiang Xia, Yongxiang Li, Yinzhou Zhu, Yu Zhao, Yuhao Jiang, Yunpeng Zhang, Yuting Lin, Yuxuan Wu, Yuyao Huang, Yuyi Wang, Zebo Peng, Zhenwu Pei, Zhenxiong Li, Zhao Wang, Zhaoxi Zhang, Zhihao Yang, Zhiqiang Dong, Zhiwei Yan, Zhilong Lu, Zhonghao Guo, Zhongheng Wu, Zhongjiang He, Zhongqiu Li, Zhu Yuan, Zhuoru Jiang, Zhuoyi Wei, Zijia Guo, Zilu Huang, Zhipeng Guo, Zirui Li, Zihan Wang
- 链接：[arXiv](https://arxiv.org/abs/2611.22115) · [PDF](https://arxiv.org/pdf/2611.22115) · [HF](https://huggingface.co/papers/2611.22115)

We present Xing 4, a series of large language models that extends the TeleChat lineage through coordinated advances in model architecture and training infrastructure on Ascend. This report describes the design principles and systems engineering behind the series, spanning architecture selection, large-scale pretraining, and reasoning and agentic post-training. We study how sparse activation, attention design, model…

## 2. Sage S2.1 Flash Technical Report

- 分数：36.0  ·  HF 赞：93  ·  来源：huggingface
- 兴趣命中：agent, tool use, benchmark, coding, spec
- 作者：Kun Cai, Haodong Chen, Guangran Cheng, Qingxiu Cheng, Xu Dai, Guanting Dong, Qiming Ge, Lixin Gu, Tao Gui, Honglin Guo, Yuyang Hu, Zixian Huang, Jiajie Jin, Alexander Lam, Jiaqiang Li, Yining Li, Jiahang Lin, Yanjiang Liu, Xinyu Lu, Haijun Lv, Ningsheng Ma, Zerun Ma, Minlong Peng, Jianmin Qian, Huayu Sha, Junlin Shang, Shuo Shen, Qisheng Su, Jiajun Sun, Yanan Sun, Zhichao Sun, Ran Tao, Zhongbo Tian, Guoqiang Wang, Hui Wang, Rui Wang, Yiding Wang, Zhecan Wang, Hao Xiang, Xinchen Xie, Shuhao Xing, Xiaoyu Xing, Wanghan Xu, Xinyu Yang, Yajie Yang, Dingbo Yuan, Yuhang Zang, Hongjie Zhang, Chengfeng Zhao, Haoran Zhao, Penghao Zhao, Ruojun Zhou, Dongsheng Zhu, Yicheng Zou, Qiye Cai, Yifei Cao, Xinmeng Che, Hongji Chen, Jiabei Chen, Jiadong Chen, Jiahao Chen, Jiayi Chen, Xinjie Chen, Yujia Chen, Xin Deng, Yi Dong, Yichen Dong, Wenjie Fu, Jianing Geng, Chenyang Gu, Ding Han, Han Han, Feiyang Hao, Haotan He, Qiushi He, Xufeng He, Xin Hong, Jie Hou, Binze Hu, Yongkang Hu, Zijian Hu, Enfu Huang, Junhao Huang, Changhao Jiang, Huicheng Jiang, Jiazhen Jiang, Shufan Jiang, Wenqing Jing, Jiahao Kuang, Bowen Lai, Bo Li, Qi Li, Qilong Li, Zhuoqun Li, Tianhao Liang, Jiaxiang Liu, Junzhang Liu, Shaofan Liu, Shuainan Liu, Tong Liu, Yi Liu, Ziyu Liu, Zhonghang Lu, Jianwen Luo, Xuan Luo, Yanyi Luo, Huijie Lv, Mingyu Ma, Houcheng Min, Hongjun Mo, Songhao Ni, Chengjun Pan, Qiyuan Peng, Xiaoxuan Peng, Wanying Ren, Runhui Ruan, Jifei Shan, Zixin Shang, Bing Shao, Zhuohui Sheng, Jiayang Shi, Qingyun Shi, Yang Shu, Aierpanjiang Simayi, Sirui Song, Yuxiao Song, Jiahao Sun, Zhe Sun, Wenzhe Tan, Guoxiang Wang, Hanchen Wang, Jie Wang, Pengbo Wang, Qing Wang, Rui Wang, Weihang Wang, Xiaotao Wang, Yuhui Wang, Zhekai Wang, Zihan Wang, Zile Wang, Jinke Wu, Liwei Wu, Xuansheng Wu, Yida Wu, Yihao Wu, Yinqi Wu, Yue Wu, Yuhan Wu, Yuwa Wu, Zhiheng Xi, Ying Xiao, Zhide Xie, Caijun Xu, Xingle Xu, Yichen Xu, Yongfeng Xu, Xiaolei Yang, Zhixiong Yang, Jiacheng Yao, Dingcheng Yi, Shihong Yi, Jinhui Yin, Peizhou Yu, Shan Yu, Hao Yuan, Junjie Yuan, Xiongyao Zha, Bo Zhang, Caixian Zhang, Kaicheng Zhang, Pengxiang Zhang, Qiuyinzhe Zhang, Wei Zhang, Xiaoqian Zhang, Xinsen Zhang, Jiyuan Zhao, Shuyu Zhao, Pujun Zheng, Zheyu Zheng, Xiaoxue Zhong, Peiheng Zhou, Xiaohao Zhou, Xinyu Zhou, Fangyi Zhu, Guanru Zhu, Yulun Zhu, Jiabao Zhuang, Pengfei Cao, Zhicheng Dou, Xianpei Han, Ben He, Guoxiu He, Xuanjing Huang, Tao Ji, Yu-Gang Jiang, Dahua Lin, Hongyu Lin, Kang Liu, Yaojie Lu, Le Sun, Ji-Rong Wen, Jun Zhao, Yutao Zhu, Qi Zhang, Bowen Zhou
- 链接：[arXiv](https://arxiv.org/abs/2611.21072) · [PDF](https://arxiv.org/pdf/2611.21072) · [HF](https://huggingface.co/papers/2611.21072)

We introduce Sage S1.5 Flash, a 320-billion-parameter general-purpose mixture-of-experts model designed to reason over scientific evidence and act in interactive environments. Sage Sci-Perception uses dedicated encoders for molecular graphs and biological sequences and represents spectra as ordered patches of measurements. Modality-specific projectors map these representations into the input space of a shared…

## 3. AscendGYM: A Cost-Aware Kernel Optimization Benchmark for Real-World Workloads on Ascend NPUs

- 分数：36.0  ·  HF 赞：83  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark, language model, large language
- 作者：AI Training Platform Team, Bingwei Zhang, Jing Li, Amir Abdullin, Sihang Chen, Xin Chen, Liangjun Feng, Yingmeng Gao, Tao Guo, Junjie Huang, Dongfang Li, Zhanglian Lin, Jiajun Liu, Zekun Liu, Zhengxuan Lu, Xiaodong Luo, Jian Meng, Ivan Nosov, Linyuan Qiu, Weijian Sun, Wanrui Yan, Binfan Zheng, Zhicheng Zhou, Baotian Hu, Min Zhang, Haizhou Li, Zhiquan Luo
- 链接：[arXiv](https://arxiv.org/abs/2611.17621) · [PDF](https://arxiv.org/pdf/2611.17621) · [HF](https://huggingface.co/papers/2611.17621)

Kernel optimization is essential for efficient large language model (LLM) training and inference on Ascend NPUs. Existing Ascend kernel benchmarks primarily focus on kernel generation, with less emphasis on the ability of agents to optimize existing implementations under input configurations drawn from real workloads. To address this requirement, we introduce AscendGYM, a benchmark whose initial suite comprises 48…

## 4. InclusionMed: Benchmarking AI for Inclusive Healthcare

- 分数：36.0  ·  HF 赞：81  ·  来源：huggingface
- 兴趣命中：reasoning, evaluation, benchmark, language model, large language, spec
- 作者：The InclusionMed Collaboration
- 链接：[arXiv](https://arxiv.org/abs/2611.21218) · [PDF](https://arxiv.org/pdf/2611.21218) · [HF](https://huggingface.co/papers/2611.21218)

Advancing medical AI for inclusive healthcare requires evaluation across diverse healthcare roles, tasks, and care settings, but benchmark coverage remains uneven. We introduce InclusionMed, an open medical AI evaluation initiative for inclusive healthcare. The InclusionMed Atlas organizes benchmarks across three healthcare roles and three AI capabilities. For the first release, we selected four public benchmarks…

## 5. K2-Horizon: A Frontier Fleet of Open Source Language Models

- 分数：36.0  ·  HF 赞：75  ·  来源：huggingface
- 兴趣命中：agent, reasoning, evaluation, benchmark, language model, coding
- 作者：K2 Team, Zhengzhong Liu, Haonan Li, Xuezhe Ma, Alexander Moreno, Subham Sekhar Sahoo, Rupesh Kumar Srivastava, Mikhail Yurochkin, Hadi Abdine, Yash Akhauri, Adharsh Babu, David Bellamy, Jalaj Bhandari, Dani Bouch, Wail Bouhedja, Weili Cao, Ahmad Chamma, Po-Chun Chang, Junlin Chen, Lingjie Chen, Zhoujun Cheng, Kyle Chickering, Ryandito Diandaru, Evan Dufraisse, Chaitanya Dwivedi, Bilal El Bouardi, Desai Fan, Richard Fan, Chengqian Gao, Rifo Ahmad Genadi, Jonathan Geuter, Charles Guille-Escuret, Willis Guo, Dhawal Gupta, Seungwook Han, Tingxu Han, Shibo Hao, Besher Hassan, Guowei He, Ming Shan Hee, Joel Hestness, Yu Huang, Yuan Huang, Haolong Jia, Linghao Jin, Junu Kim, Lingjing Kong, Nurkhan Laiyk, Andrej Leban, Liqun Ma, John Maggs, Amr Mohamed, Mukhesh Narra, Omkar Pangarkar, Aldo Pareja, Khiem Pham, Varad Pimpalkhute, Nikhil Ranjan, Elizaveta Rebrova, Hector Ren, Shaurya Rohatgi, Guokan Shang, Jianshu She, Chufan Shi, Aaryamonvikram Singh, Daria Soboleva, Kartik Sreenivasan, Suqi Sun, Yuekai Sun, Bowen Tan, Liping Tang, Shengkun Tang, Muzi Tao, Mallikarjuna Tupakula, Micah Villmow, Hongyi Wang, Huijuan Wang, Renxi Wang, Yongxin Wang, Yuqi Wang, Zhenting Wang, Shicheng Wen, Yingquan Wu, Anze Xie, Andrew Xing, Matthew Yang, Shuanghai Yu, Kerem Zaman, Zenan Zhai, Hongli Zhan, Xuezhou Zhang, Anshun Asher Zheng, Zhe Zhou, Richard Zhuang, Eric P. Xing
- 链接：[arXiv](https://arxiv.org/abs/2611.21003) · [PDF](https://arxiv.org/pdf/2611.21003) · [HF](https://huggingface.co/papers/2611.21003)

We present K2-Horizon, a fleet of six fully open language models, from a 0.9B dense model to a 375B-A23B MoE, built for general-purpose reasoning and agentic work across math and science, software engineering, deep research, office automation, and beyond. The models lead or are competitive with strong open models of their size on agentic and coding benchmarks. On the modeling side, to strengthen reasoning, we…

## 6. Weight-Space Programming Doesn't Need Transformers

- 分数：36.0  ·  HF 赞：40  ·  来源：huggingface
- 兴趣命中：memory, benchmark, language model, large language
- 作者：Hyunjong Ok, Jaeho Lee
- 链接：[arXiv](https://arxiv.org/abs/2611.22055) · [PDF](https://arxiv.org/pdf/2611.22055) · [HF](https://huggingface.co/papers/2611.22055)

Standard neural architectures such as the Transformer were chosen because they train well with gradient descent and run fast on GPUs. In weight-space programming, a large language model (LLM) writes target weights by hand without gradient-based training, so those reasons no longer apply. Should we keep the Transformer? Given minimal guidance, ten labeled examples, and a sandbox, mainly on multiple-choice questions,…

## 7. SWE-CoWork: Benchmarking Coding Agents as Digital Employees in Organizations

- 分数：34.0  ·  HF 赞：49  ·  来源：huggingface
- 兴趣命中：agent, benchmark, coding
- 作者：Xinping Lei, Minghao Liu, Ruijie Zhu, Xiaohui Hu, Xingqiao Li, Ao Zhang, Wenhao Chai, Han Li, Tao Wang, Jingyuan Zhang, Enduo Zhao, Yunfeng Shi, Yiming Liang, Zetao Yang, Xingjian Wang, Yifan Yao, Xinkai Ma, Yingru Li, Tianhan Yang, Huan Zhou, Weiran Shi, Shen Yan, Jiaheng Liu, Stephen Huang, Eli Cheung, Weihao Xuan
- 链接：[arXiv](https://arxiv.org/abs/2611.20218) · [PDF](https://arxiv.org/pdf/2611.20218) · [HF](https://huggingface.co/papers/2611.20218)

A coding agent working within a software organization must establish what to build, collaborate with colleagues, and verify what it delivers. We introduce SWE-CoWork, a benchmark comprising 101 development assignments across 101 real repositories, 11 programming languages, and 12 application domains. Each assignment places an agent in a simulated engineering organization with 26 colleagues who have distinct…

## 8. ScaleVLA: Scaling Vision-Language-Action Models to 552 Billion Parameters

- 分数：34.0  ·  HF 赞：43  ·  来源：huggingface
- 兴趣命中：agent, reasoning, language model
- 作者：Ruixi Yu, Dairu Liu, Xuchuan Chen, Zekun Qi, Zekai Li, Zhuo Cao, Luyang Niu, Yingsheng Zhang, Sikai Liang, Ke Fan, He Wang, Li Yi
- 链接：[arXiv](https://arxiv.org/abs/2611.21607) · [PDF](https://arxiv.org/pdf/2611.21607) · [HF](https://huggingface.co/papers/2611.21607)

Frontier Vision-Language Models (VLMs) such as GPT-6 Astra have demonstrated remarkable capabilities in robot control, suggesting that broad pretraining provides knowledge valuable for physical action. Yet most Vision-Language-Action (VLA) policies still rely on much smaller VLM backbones, leaving this potential largely untapped. We ask whether frontier-scale representations can provide a stronger foundation for…

## 9. SPILLWAY: Separating Target Admission from Sanitization to Defend Tool-Using Agents against Prompt Injection

- 分数：32.0  ·  HF 赞：64  ·  来源：huggingface
- 兴趣命中：agent, language model
- 作者：Woosang Lim, Yeseul Chang, Jaewoo Lee
- 链接：[arXiv](https://arxiv.org/abs/2611.07222) · [PDF](https://arxiv.org/pdf/2611.07222) · [HF](https://huggingface.co/papers/2611.07222)

Tool-using agents act on email, files, and payments, so an instruction hidden in a web page or a shared document can make an agent send data or money to an attacker. Many runtime defenses put a language model on the decision that lets an action through, so the decision depends on a model that may read the attacker's text and adds model calls to every step. Provenance defenses keep the model off the final check but…

## 10. AllocFlow: End-to-End Portfolio Trading Action Generation from Raw Market Data

- 分数：30.0  ·  HF 赞：70  ·  来源：huggingface
- 兴趣命中：reinforcement learning
- 作者：Annan Wang, Yuchen Xie, Yu Cen, Leon Liangyu Chen, Qianyu Julie Zhu, Xin Li, Tianyi Wei, Weisi Lin
- 链接：[arXiv](https://arxiv.org/abs/2611.19937) · [PDF](https://arxiv.org/pdf/2611.19937) · [HF](https://huggingface.co/papers/2611.19937)

Real-world portfolio management requires converting noisy market observations into coordinated, simultaneous allocations across multiple assets under shared capital constraints. Advances in forecasting models and alpha discovery help identify opportunities. However, traditional pipelines often decouple signal forecasting from portfolio construction, potentially misaligning learning with allocation and execution…

## 11. ForceHarness: Turning Force into Action and Physics for Frozen Frontier Models

- 分数：29.0  ·  HF 赞：38  ·  来源：huggingface
- 兴趣命中：benchmark
- 作者：Ke Sun, Kevin Yuchen Ma, Yike Zhang, Yanzhe Chen, Mike Zheng Shou
- 链接：[arXiv](https://arxiv.org/abs/2611.21099) · [PDF](https://arxiv.org/pdf/2611.21099) · [HF](https://huggingface.co/papers/2611.21099)

Frontier multimodal models can now control robots zero-shot from images, yet many manipulation tasks depend on contact forces that images cannot show. Bringing force to an API-only frozen model raises two challenges. First, contact evolves much faster than an API model can decide, so the system must close the loop on force beneath the model. Second, a frozen model cannot interpret raw force streams, so force must be…

## 12. Multi-Branch Transformer

- 分数：28.0  ·  HF 赞：28  ·  来源：huggingface
- 兴趣命中：long context, language model, coding
- 作者：Gaotang Li, Lingjie Chen, Chunyuan Deng, Zhiwei Xu, Hongzheng Chen, Christopher De Sa, Jingrui He, Yingheng Wang, Hanghang Tong
- 链接：[arXiv](https://arxiv.org/abs/2611.19800) · [PDF](https://arxiv.org/pdf/2611.19800) · [HF](https://huggingface.co/papers/2611.19800)

Transformer language models are commonly scaled by making their blocks wider or stacking them deeper. In this work, we explore a complementary path: branching, the parallel composition of full Transformer blocks. We introduce the Multi-Branch Transformer (MBT), which processes the input through shared initial layers, executes independently parameterized branches of sequential blocks in parallel, and fuses their…

## 13. PaperCritic: Training AI Reviewers to Assess the Soundness of Papers

- 分数：25.5  ·  HF 赞：31  ·  来源：huggingface
- 兴趣命中：reinforcement learning
- 作者：Hyun Ryu, Ji Yong Cho, Eunho Yang, Moontae Lee, June Yong Yang, Sean Welleck, Carolyn Rose
- 链接：[arXiv](https://arxiv.org/abs/2611.17834) · [PDF](https://arxiv.org/pdf/2611.17834) · [HF](https://huggingface.co/papers/2611.17834)

As AI conference submissions grow rapidly, AI reviewers are being considered as an alternative. However, simply imitating human reviewing is problematic because reviewing serves multiple purposes, including evaluating papers' soundness, interestingness, and clarity, the last two of which are subjective. In this work, we focus solely on evaluating soundness, the most important and objective criterion, and define the…

## 14. Accelerate Bench: Evaluating Agents for Application-Level Program Optimization

- 分数：24.5  ·  HF 赞：17  ·  来源：huggingface
- 兴趣命中：agent, benchmark, coding, spec
- 作者：Bowen Liu, Yuhan Li, Nuo Chen, Weile Luo, Miao Peng, Qintong Zhang, Qifan Zhang, Jia Li, Ziqi Gao, Lydell Huang
- 链接：[arXiv](https://arxiv.org/abs/2611.20882) · [PDF](https://arxiv.org/pdf/2611.20882) · [HF](https://huggingface.co/papers/2611.20882)

Application optimization requires coding agents to discover useful changes and coordinate them across a complete program while preserving the required computation. We introduce Accelerate Bench, a benchmark of 32 CPU optimization tasks adapted from scientific applications and supercomputing competitions. Each task provides a working program and specifies the workload, correctness requirements, timing boundaries, and…

## 15. VoxMel TTS Technical Report

- 分数：23.5  ·  HF 赞：23  ·  来源：huggingface
- 兴趣命中：evaluation, spec
- 作者：Wenhao Guan, Jiaxin Ye, Haitao Li, Yifan Duan, Junxi Liu, Wangjin Zhou, Lin Li, Qingyang Hong, Xie Chen
- 链接：[arXiv](https://arxiv.org/abs/2611.20254) · [PDF](https://arxiv.org/pdf/2611.20254) · [HF](https://huggingface.co/papers/2611.20254)

Continuous autoregressive TTS relies on an acoustic target that enables stable next-latent modeling while preserving fine-grained acoustic details. While existing approaches employ learned compressed representations (e.g., continuous VAE latents) to render prediction tractable, they rely on complex neural encoders that often cap generation fidelity. Conversely, training-free targets like mel-spectrograms eliminate…

## 16. TCP4D: A Unified Tool-Center-Point Tracking and Generation Model for Robot Manipulation

- 分数：23.0  ·  HF 赞：22  ·  来源：huggingface + arxiv
- 兴趣命中：-
- 作者：Haosong Peng, Xiangyang Liu, Zhengshen Zhang, Yunfeng Fan, Tianyu Qi, Xin Xia, Yufeng Zhan, Wenchao Xu
- 链接：[arXiv](https://arxiv.org/abs/2611.23143) · [PDF](https://arxiv.org/pdf/2611.23143) · [HF](https://huggingface.co/papers/2611.23143)

Robot manipulation videos provide a rich visual experience, yet recovering robot action and gripper-state annotations from RGB observations still remains challenging. Using the embodiment-agnostic tool-center-point (TCP) pose as the action space, we present TCP4D, a unified model in which a shared 4D scene representation both tracks observed TCP motion and generates future TCP trajectories. Given a monocular video…

## 17. Calpha: Toward Native Biomolecular Intelligence in a General-Purpose Language Model

- 分数：23.0  ·  HF 赞：14  ·  来源：huggingface
- 兴趣命中：reasoning, language model, large language, spec
- 作者：Yong Liu, Zhanpeng Shi, Peicong Lin, Zhenyi Zhong, Yizhou Dang, Wendi Wu, Haoling Li, Shuangjia Zheng
- 链接：[arXiv](https://arxiv.org/abs/2611.20986) · [PDF](https://arxiv.org/pdf/2611.20986) · [HF](https://huggingface.co/papers/2611.20986)

Biomolecular foundation models predict the structures of proteins and their complexes accurately, and large language models (LLMs) reason in natural language, but the two remain separate: the abilities of the former are not part of a general-purpose LLM, and the reasoning of the latter does not enter a structure prediction. Calpha aims at one general model that folds proteins and complexes, understands protein…

## 18. FastFrames: Video Generation at Interactive Latency

- 分数：22.5  ·  HF 赞：17  ·  来源：huggingface + arxiv
- 兴趣命中：coding
- 作者：Gene Chou, Guandao Yang, Fujun Luan, Lars Mescheder, Wei Dong, Stephan Richter, Vladlen Koltun
- 链接：[arXiv](https://arxiv.org/abs/2611.23226) · [PDF](https://arxiv.org/pdf/2611.23226) · [HF](https://huggingface.co/papers/2611.23226)

Autoregressive video diffusion models generate frames based on new observations and inputs, making them a promising medium for interactive visual experiences. However, existing models are orders of magnitude too slow for fluid interaction. This paper introduces FastFrames, a family of fast autoregressive video diffusion models that achieves interactive latency without compromising quality. We profile the inference…

## 19. Heave-Ho: Decentralized Long-Horizon Multi-Humanoid Collaboration

- 分数：22.0  ·  HF 赞：12  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark, planning
- 作者：Ting-Hsuan Chen, Siheng Zhao, Han Jiang, Qi Pan, Louison Lu, Jiaheng Luo, Henghui Bao, Yiyu Chen, Quan Nguyen, Yue Wang
- 链接：[arXiv](https://arxiv.org/abs/2611.22275) · [PDF](https://arxiv.org/pdf/2611.22275) · [HF](https://huggingface.co/papers/2611.22275)

Collaboration promises to extend humanoid capabilities beyond what individual robots can achieve. However, realizing this potential requires coordinated whole-body interactions, coherent long-horizon planning, and precise synchronization across robots. We introduce Heave-Ho, a decentralized framework for long-horizon collaborative multi-humanoid loco-manipulation. At the low level, we develop a multi-agent…

## 20. MedJev: A System One Vision-Language Decision Model for Fast and Effective Medical Image Understanding

- 分数：21.5  ·  HF 赞：11  ·  来源：huggingface
- 兴趣命中：reasoning, benchmark, language model, spec
- 作者：Fan Zhang, Hao Wu, Jinyang Wu, Hongyu Qu, Zheng Lian, Dongfu Yin, Qingsong Wen, Pheng-Ann Heng
- 链接：[arXiv](https://arxiv.org/abs/2611.20992) · [PDF](https://arxiv.org/pdf/2611.20992) · [HF](https://huggingface.co/papers/2611.20992)

Medical image understanding with vision-language models (VLMs) typically relies on autoregressively generating reasoning and answer tokens. These unnecessary tokens make the inference cost scale with the response length and force the answer to be parsed from free-form text, incurring avoidable latency and decision errors. To this end, we introduce MedJev, a system one vision-language decision model that maps medical…

## 21. LynnReal-Hand: Unlocking World Interaction with Hand Control

- 分数：21.0  ·  HF 赞：18  ·  来源：huggingface
- 兴趣命中：memory, evaluation
- 作者：Shaohao Rui, Chaoyang Zhang, Xiaofeng Mao, Weijie Ma
- 链接：[arXiv](https://arxiv.org/abs/2611.21479) · [PDF](https://arxiv.org/pdf/2611.21479) · [HF](https://huggingface.co/papers/2611.21479)

Interactive video world models enable exploration through text and camera controls, yet direct object interaction requires finer control. Hands provide a natural interface, but translating continuous hand movements into coherent visual responses remains challenging because of complex hand-object dynamics and demanding real-time computation. To address these challenges, we introduce LynnReal-Hand, a hand-controlled…

## 22. Self-Improvement Memory Enables Continual Recursive Self-Improvement

- 分数：21.0  ·  HF 赞：10  ·  来源：huggingface
- 兴趣命中：memory, evaluation, benchmark, coding
- 作者：Xin Yu, Fei Xia, Jiaqi Pan, Youbao Tang, Chengzhi Liu, Adams Yu, Sicong Jiang, Yanfei Chen, Lingzhou Xue, Ting Yu
- 链接：[arXiv](https://arxiv.org/abs/2611.18856) · [PDF](https://arxiv.org/pdf/2611.18856) · [HF](https://huggingface.co/papers/2611.18856)

Harness optimization is often studied with a fixed policy model and benchmark. When either changes, the optimizer must decide which parts of an evolved harness to reuse or revise, but the harness alone may not explain why earlier edits were made or how they performed. In this work, we study Continual Recursive Self-Improvement (CRSI), a setting for continuing existing harness-optimization methods across compatible…

## 23. Do LLM Agents Still Need to Be Told How to Self-Improve?

- 分数：21.0  ·  HF 赞：6  ·  来源：huggingface + arxiv
- 兴趣命中：agent, benchmark, spec
- 作者：Shobhita Sundaram, Cansu Sancaktar, Phillip Isola
- 链接：[arXiv](https://arxiv.org/abs/2611.23219) · [PDF](https://arxiv.org/pdf/2611.23219) · [HF](https://huggingface.co/papers/2611.23219)

LLM agents increasingly drive their own learning. Self-improvement methods delegate various components of model optimization to the models themselves. As models become more capable, this motivates a basic question: do these increasingly capable models still need us to specify how they should self-improve? In this paper we study an autonomous paradigm in which, given basic primitives, resources, and a general goal…

## 24. MovieRoll: A Systematic Framework for Rolling Out Long-Form Videos

- 分数：20.0  ·  HF 赞：12  ·  来源：huggingface
- 兴趣命中：memory, evaluation, coding
- 作者：Yunyang Ge, Weijie Kong, Ryan Xu, Yue Wu, Qi Tian, Jiangfeng Xiong, Bin Lin, Mingzhe Zheng, Shenghai Yuan, Zheyuan Liu, Jianwei Zhang, Li Yuan
- 链接：[arXiv](https://arxiv.org/abs/2611.21339) · [PDF](https://arxiv.org/pdf/2611.21339) · [HF](https://huggingface.co/papers/2611.21339)

Streaming video generation must sustain quality beyond the training horizon while handling self-generated history and growing cache costs. To address these challenges, we present MovieRoll, a base-to-distilled framework that connects streaming fine-tuning, long-rollout distillation, and long-horizon inference. We first establish a robust multi-step base through Window-wise Teacher Forcing (WinTF), which jointly…

## 25. Regularized Score Centering

- 分数：19.5  ·  HF 赞：7  ·  来源：huggingface
- 兴趣命中：agent, tool use, reasoning, reinforcement learning, evaluation, benchmark
- 作者：Hao Bai, Chenlu Ye, Xuanchang Zhang, Aviral Kumar, Tong Zhang
- 链接：[arXiv](https://arxiv.org/abs/2611.21791) · [PDF](https://arxiv.org/pdf/2611.21791) · [HF](https://huggingface.co/papers/2611.21791)

Asynchronous reinforcement learning increases training throughput, but data from stale policies and numerical mismatch between training and inference can destabilize learning. To stabilize off-policy learning, score centering (SC) removes the effect of reward baselines on the expected update. Our gradient diagnostics show less extreme gradients with SC than with importance sampling (IS), but SC can still fail when…

## 26. Breath-Dx: A Time Series Classification Benchmark for Disease Screening with eNose

- 分数：19.0  ·  HF 赞：10  ·  来源：huggingface
- 兴趣命中：evaluation, benchmark, spec
- 作者：Ivan Poddiakov, Ivan Kruzhilov, Galina Zubkova, Svetlana Erofeeva, Andrey Savchenko, Pavel Blinov
- 链接：[arXiv](https://arxiv.org/abs/2611.15348) · [PDF](https://arxiv.org/pdf/2611.15348) · [HF](https://huggingface.co/papers/2611.15348)

Electronic nose (eNose) technology offers a portable, non-invasive route for disease screening via exhaled breath analysis. However, progress in the field is hindered by the lack of systematic benchmarks that compare machine learning methods under realistic conditions, particularly sensor drift, a known but rarely quantified failure mode. Most existing studies rely on small, private datasets with inconsistent…

## 27. Continuation-Guided LLM Evolution of Program Policies and Goal Compilers in Craftax

- 分数：19.0  ·  HF 赞：6  ·  来源：huggingface
- 兴趣命中：agent, memory, coding, spec
- 作者：Víctor Gallego
- 链接：[arXiv](https://arxiv.org/abs/2611.19537) · [PDF](https://arxiv.org/pdf/2611.19537) · [HF](https://huggingface.co/papers/2611.19537)

Coding agents can synthesize and optimize code-based policies from simulator feedback, allowing the resulting program to act with zero inference model calls. But for long horizon tasks, two challenges arise: local improvements can hurt final success and switching to a new objective requires another expensive synthesis run. We propose a framework that first develops competence by refining the policy through a…

## 28. π^4: A Foundation Model for 4D Scene Geometry and Motion

- 分数：19.0  ·  HF 赞：6  ·  来源：huggingface + arxiv
- 兴趣命中：evaluation, benchmark
- 作者：Yifan Wang, Weiguang Zhao, Ni Yang, Haoyu Guo, Junting Dong, Weinan Zhang, Chunhua Shen
- 链接：[arXiv](https://arxiv.org/abs/2611.23144) · [PDF](https://arxiv.org/pdf/2611.23144) · [HF](https://huggingface.co/papers/2611.23144)

$π^4$ is a unified foundation model for 4D scene perception. From diverse, uncalibrated RGB observations in the wild---a single image, an unordered collection, or a video sequence---it recovers dense geometry, camera poses, and metric scale, together with 2D/3D point tracks and moving-object masks for multi-image inputs. It couples a geometry branch with a geometry-conditioned motion branch, which predicts…

## 29. ViRA: Toward Ultra-High-Resolution Visual Agents via Cross-Input Relative Policy Optimization

- 分数：18.5  ·  HF 赞：5  ·  来源：huggingface
- 兴趣命中：agent, reasoning, reinforcement learning, evaluation, benchmark
- 作者：Huawei Lin, Jinting Liu, Tongyan Wang, Xuyang Chen, Ruihua Shi, Zhichao Xu, Jiaxin Qin, Guoshenghui Zhao, Baijian Yang, Yingjie Victor Chen, Tan Yu, Weijie Zhao
- 链接：[arXiv](https://arxiv.org/abs/2611.21605) · [PDF](https://arxiv.org/pdf/2611.21605) · [HF](https://huggingface.co/papers/2611.21605)

Visual agents answer questions about ultra-high-resolution photos by zooming into the relevant regions. However, existing agents often answer from common sense instead of reading the evidence. Reinforcement learning (RL) on the final answer cannot correct this, because a guess earns the same reward as reading. We propose Cross-Input Relative Policy Optimization (CrossRPO), which trains agents on contrast sets. A…

## 30. Agentic On-Policy Distillation Implicitly Reshapes LLMs' ReAct Patterns

- 分数：17.0  ·  HF 赞：6  ·  来源：huggingface
- 兴趣命中：agent, reasoning, spec
- 作者：Deyang Kong, Zhaoyi Li, Sijian Ren, Yuan Wei, Ying Wei, Defu Lian, Shikun Zhang, Wei Ye
- 链接：[arXiv](https://arxiv.org/abs/2611.19244) · [PDF](https://arxiv.org/pdf/2611.19244) · [HF](https://huggingface.co/papers/2611.19244)

On-policy distillation (OPD) transfers specialized capabilities to language-model agents, but its cross-domain effects on interaction remain unclear. We investigate how OPD reshapes ReAct interaction patterns across mathematics, ALFWorld, and τ^2-bench, focusing on reasoning, actions, and observation acquisition. General-reasoning supervision reduces mathematical tool attempts from 70.4% to 14.4% while increasing…

## 31. Abstention Direction in Large Language Models: Mechanistic Interpretability of Abstention Across Query Ambiguity, Knowledge Limits, and Safety Alignment

- 分数：17.0  ·  HF 赞：6  ·  来源：huggingface
- 兴趣命中：language model, large language, spec
- 作者：Koki Itai, Jun Hirako, Hiroaki Yamagiwa
- 链接：[arXiv](https://arxiv.org/abs/2611.20441) · [PDF](https://arxiv.org/pdf/2611.20441) · [HF](https://huggingface.co/papers/2611.20441)

Abstention, the withholding of a response by a large language model (LLM) under uncertainty or safety risks, is essential for trustworthy models. The causes of abstention fall into three perspectives: ambiguity in the Query (Q), limits of Model Knowledge (MK), and misalignment with Human Values (HV). However, prior analyses of internal representations have focused on HV, using a refusal direction computed from…

## 32. Inside the Trading Loop: Markets, Models, and Moves with LLM Agents

- 分数：17.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：agent, language model, large language, spec
- 作者：Renee Jia, Di Mu, Yao Yu, Tianrui Liu
- 链接：[arXiv](https://arxiv.org/abs/2611.11657) · [PDF](https://arxiv.org/pdf/2611.11657) · [HF](https://huggingface.co/papers/2611.11657)

We built a hybrid multi-agent trading system that combines large language model (LLM) analysts with momentum-based portfolio construction and rule-based execution. Company-news and macroeconomic agents return structured reports to a coordinator that sets stock weights and cash reserves. We evaluate the portfolio engine using its broker-recorded paper account, which operated with deterministic fallbacks, and compare…

## 33. SALA: Semantically Aligned Latent Actions Enable Dual-Axis Scaling of Embodied Foundation Models

- 分数：16.5  ·  HF 赞：13  ·  来源：huggingface
- 兴趣命中：spec
- 作者：Jiachun Jin, Zetong Zhou, Haonan Wang, Zhijie Deng
- 链接：[arXiv](https://arxiv.org/abs/2611.17110) · [PDF](https://arxiv.org/pdf/2611.17110) · [HF](https://huggingface.co/papers/2611.17110)

Embodied foundation models hinge on diverse robot interaction data, which are costly to collect. Egocentric human videos offer a complementary source of experience, and latent action models (LAMs) provide a popular means of leveraging these videos for policy supervision. Compared with world-action models (WAMs), LAMs can offer greater training efficiency and potentially lower inference costs by avoiding explicit…

## 34. DominoBench: Evaluating Multi-Step Physical Reasoning from Still Images

- 分数：16.5  ·  HF 赞：5  ·  来源：huggingface
- 兴趣命中：reasoning, benchmark, language model
- 作者：Emilio Ferrara
- 链接：[arXiv](https://arxiv.org/abs/2611.20385) · [PDF](https://arxiv.org/pdf/2611.20385) · [HF](https://huggingface.co/papers/2611.20385)

Can a vision-language model look at a picture of a chain reaction and tell what will happen? Recent multimodal models describe scenes fluently and solve textbook physics problems, which suggests they should also predict how a scene of ramps, ledges, pendulums, seesaws and dominoes plays out once a ball is pushed. We tested this claim on 30 models from 10 families and reached a clear conclusion: unaided, no model…

## 35. More Agents, More Samples, or More Thinking? Untangling Coordination, Ensembling, and Test-Time Compute in Multi-Agent LLMs

- 分数：16.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：agent, evaluation, language model
- 作者：Seyed Mahmoud Sajjadi Mohammadabadi
- 链接：[arXiv](https://arxiv.org/abs/2611.17610) · [PDF](https://arxiv.org/pdf/2611.17610) · [HF](https://huggingface.co/papers/2611.17610)

Evaluations of multi-agent language models often compare communicating architectures against a single greedy pass. This practice confounds coordination with sample multiplicity and inference compute. We synthesize nine primary empirical evaluations comprising 516 unique multi-agent configurations organized along a resource vector R with six dimensions and a baseline ladder with four categories. Against baselines…

## 36. LoopFill: Pipelined Multi-Token Speculative Decoding for Looped Transformers

- 分数：16.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：benchmark, coding, spec
- 作者：Siqi Zhu, Suozhi Huang, Yi Zhao, Jiaxuan You
- 链接：[arXiv](https://arxiv.org/abs/2611.19649) · [PDF](https://arxiv.org/pdf/2611.19649) · [HF](https://huggingface.co/papers/2611.19649)

Looped Transformers improve parameter efficiency by repeatedly applying the same Transformer layers. During autoregressive decoding, however, generating each token requires several sequential passes through these layers, leading to high decoding latency. Pipelined self-speculative methods use shallow-loop predictions to process tokens at different loops in the same batch, but each token must reach the drafting depth…

## 37. Energy-Based Reasoners: Your Recurrent Reasoner Should Be an Energy-Based Model

- 分数：15.5  ·  HF 赞：7  ·  来源：huggingface
- 兴趣命中：reasoning, benchmark
- 作者：William Xingxu Chen, Alexi Gladstone, Zeyu Michael Li, Heng Ji, Yilun Du
- 链接：[arXiv](https://arxiv.org/abs/2611.08977) · [PDF](https://arxiv.org/pdf/2611.08977) · [HF](https://huggingface.co/papers/2611.08977)

Looping is a powerful inductive bias for reasoning. By repeatedly iterating a recurrent block, looped models can scale their effective depth and enable multi-step reasoning in latent space. However, existing looped models are not inherently guided by an explicit measure of progress, making it difficult to determine when to stop looping and how to improve upon the current state. To enable this, we introduce…

## 38. Correcting Persistent Failures in Point-Cloud Grasping Policies using Human Demonstrations in Virtual Reality

- 分数：15.5  ·  HF 赞：7  ·  来源：huggingface
- 兴趣命中：reinforcement learning, spec
- 作者：Achyuthan Unni Krishnan, Karthik Rengarajan, Bharath Narasimhan, Chris von Csefalvay
- 链接：[arXiv](https://arxiv.org/abs/2611.18919) · [PDF](https://arxiv.org/pdf/2611.18919) · [HF](https://huggingface.co/papers/2611.18919)

Robots in homes, warehouses and farms must pick up objects they have never seen, usually without a 3D model or a category label. A grasping policy that works directly on the point cloud from a depth sensor needs only the geometry the robot observes, so it applies to any new object. Offline grasp generators such as Contact-GraspNet work this way, but they rank grasps by learned plausibility rather than by whether the…

## 39. Flexible Multi-Stack Super-Resolution of Clinical Brain MRI Using Hetero-Orientation Variational Encoding: Expert Reader Evaluation in a Nigerian Cohort

- 分数：15.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：evaluation, benchmark, coding
- 作者：Kabir Hamzah Muhammad, Lorena Garcia-Foncillas Macias, Soumya Snigdha Kundu, Emily Guilhem, Jon Cleary, Amal Saleh Nour, Yodit Abraham Yaynishet, Chinasa Kalaiwo, Peter Chibuta, Ugumba Kwikima, Udunna Anazodo, Jonathan Shapey, Tom Vercauteren
- 链接：[arXiv](https://arxiv.org/abs/2611.21412) · [PDF](https://arxiv.org/pdf/2611.21412) · [HF](https://huggingface.co/papers/2611.21412)

High-resolution brain MRI is important for neuroradiological assessment, yet routine clinical protocols often rely on fast, anisotropic 2D acquisitions, particularly in resource-constrained settings. These acquisitions may differ in orientation, alignment and anatomical coverage, resulting in partially overlapping image stacks. Existing learning-based super-resolution methods typically rely on single,…

## 40. GPBam: A Retrieval-Aware German Public Law Exam Benchmark

- 分数：15.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：reasoning, benchmark, retrieval
- 作者：Abdullah Al Zubaer, Lorenz Wendlinger, Simon Alexander Nonn, Michael Granitzer, Jelena Mitrović
- 链接：[arXiv](https://arxiv.org/abs/2611.18981) · [PDF](https://arxiv.org/pdf/2611.18981) · [HF](https://huggingface.co/papers/2611.18981)

Legal reasoning in civil-law systems is not rule-lookup: the German state examination asks for a structured opinion (Gutachten) that names the governing norms, applies them to the facts, and argues to a conclusion. We introduce GPBam (German Public Law Bar-style Exam), 81 public-law examination cases with reference solutions, paired with a recitation task over 200 statutory provisions. Drawn from state examination…

## 41. Reflection Anchors for Propagation-Aware Visual Retention in Long-Chain Multimodal Reasoning

- 分数：15.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：reasoning, benchmark, language model
- 作者：Xuan Gong, Hanbo Huang, Hao Zheng, Yiran Zhang, Wenbin Dai, Weishu Zhao, Shiyu Liang
- 链接：[arXiv](https://arxiv.org/abs/2605.09614) · [PDF](https://arxiv.org/pdf/2605.09614) · [HF](https://huggingface.co/papers/2605.09614)

Long chain-of-thought (CoT) reasoning improves large vision--language models, but visual information often fades during generation, limiting long-horizon multimodal reasoning. Existing methods either re-inject vision at inference or train policies for stronger grounding, but where to intervene relies on perception heuristics rather than principled gain analysis, and how local visual influence propagates remains…

## 42. UMM-JEPA: Generative Pretraining via Masked Next-Scale Representation Prediction for Unified Multimodal Models

- 分数：14.5  ·  HF 赞：5  ·  来源：huggingface
- 兴趣命中：benchmark, spec
- 作者：Yucheng Zhou, Yunjia Xi, Di Yin, Jianbing Shen
- 链接：[arXiv](https://arxiv.org/abs/2611.18668) · [PDF](https://arxiv.org/pdf/2611.18668) · [HF](https://huggingface.co/papers/2611.18668)

Unified multimodal models can support both visual understanding and generation, yet generative training does not necessarily improve understanding. We argue that this limitation may arise from a mismatch between the representation targeted by generation and the perceptual representation used for understanding. Conventional generation objectives primarily optimize synthesis-oriented spaces such as discrete visual…

## 43. Termination Lag: Coding Agents Solve Early but Stop Late

- 分数：14.5  ·  HF 赞：5  ·  来源：huggingface
- 兴趣命中：agent, coding
- 作者：Musa Cim, Burak Topcu, Mahmut Taylan Kandemir
- 链接：[arXiv](https://arxiv.org/abs/2611.14960) · [PDF](https://arxiv.org/pdf/2611.14960) · [HF](https://huggingface.co/papers/2611.14960)

Coding agents can solve a task well before they stop working on it. We characterize termination lag--the number of steps between an agent's first correct patch and the end of its run--across five models, two agent frameworks, and three SWE-bench datasets by recording and testing every distinct repository patch generated during execution. Our analysis reveals that 38--82% of successful runs achieve a correct solution…

## 44. ResWAM: Learning What Changes, Not What Stays, for World-Action Models

- 分数：14.0  ·  HF 赞：8  ·  来源：huggingface
- 兴趣命中：benchmark
- 作者：Chongyu Fan, Gaowen Liu, Ramana Rao Kompella, Jason Corso, Sijia Liu
- 链接：[arXiv](https://arxiv.org/abs/2611.19559) · [PDF](https://arxiv.org/pdf/2611.19559) · [HF](https://huggingface.co/papers/2611.19559)

World-action models (WAMs) augment vision-language-action policies (VLAs) with future prediction so that the policy can anticipate how its actions will affect the physical world. Existing WAMs supervise complete future observations. However, observations typically change little over an action chunk, so the future loss is dominated by copying static background content rather than learning task-relevant robot and…

## 45. OutfitterBench: Evaluating LLM Agents on Long-Horizon Resource Allocation and Commitment Coordination

- 分数：14.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：agent, benchmark
- 作者：Jie Huang, Yuecheng Hong, Yao Chen, Shengding Jiao, Xudong Liu, Qiang Ye
- 链接：[arXiv](https://arxiv.org/abs/2611.17933) · [PDF](https://arxiv.org/pdf/2611.17933) · [HF](https://huggingface.co/papers/2611.17933)

In many long-horizon settings, an agent's own choices create future constraints: committing finite capacity establishes future obligations and forecloses later opportunities. Sustaining performance therefore requires both keeping evolving plans feasible and comparing the value of resource allocations with the alternatives they displace. Recent benchmarks increasingly evaluate LLM agents in continuing operations, but…

## 46. FMT: Lossless Image Compression in a Fixed Number of Parallel Steps

- 分数：14.0  ·  HF 赞：0  ·  来源：huggingface + arxiv
- 兴趣命中：coding
- 作者：Ammar Ali
- 链接：[arXiv](https://arxiv.org/abs/2611.23108) · [PDF](https://arxiv.org/pdf/2611.23108) · [HF](https://huggingface.co/papers/2611.23108)

Learned lossless codecs make smaller files than common classical codecs, yet the images we archive and train on still use classical codecs. A main reason is time: a learned codec takes seconds to decode a photo that a classical codec opens in milliseconds, and their faster variants give up most of their gain in size. We argue that much of this time is spent waiting, not computing: the network waits for the values it…

## 47. BitDecoding-FP4: Native FP4 KV Cache Decoding via Algorithm-System Co-Design

- 分数：13.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：memory, coding
- 作者：Dayou Du, Woon Yee Ng, Guangming Sheng, Nick Lau, Jianyi Cheng, Luo Mai
- 链接：[arXiv](https://arxiv.org/abs/2611.09825) · [PDF](https://arxiv.org/pdf/2611.09825) · [HF](https://huggingface.co/papers/2611.09825)

The key-value (KV) cache dominates memory capacity and bandwidth in long-context LLM serving. While 4-bit microscaling formats (NVFP4, MXFP4) shrink the cache and run attention on FP4 Tensor Cores, a fundamental gap remains between algorithmic quantization and system-aware acceleration: existing FP4 KV systems use vanilla quantization that causes severe accuracy drops, whereas accuracy-oriented 4-bit algorithms rely…

## 48. When Expert Disagreement Hurts: Prestige and Selectivity in LLM Decision Revision

- 分数：13.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：agent, language model
- 作者：Yupeng Tang, Mingfeng Lin
- 链接：[arXiv](https://arxiv.org/abs/2611.16694) · [PDF](https://arxiv.org/pdf/2611.16694) · [HF](https://huggingface.co/papers/2611.16694)

When language models revise a decision after another agent disagrees, neither reversal counts nor final accuracy shows whether they are fixing mistakes or abandoning correct answers. We introduce a controlled two-pass audit that holds the question, the evidence, and the model's initial answer fixed and varies only the revision context: neutral reflection, anonymous disagreement, or disagreement attributed to a…

## 49. Dataset Distillation via Drifting

- 分数：13.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：evaluation, spec
- 作者：George Cazenavette, Angelina Quan, Giannis Daras, Antonio Torralba, Vincent Sitzmann
- 链接：[arXiv](https://arxiv.org/abs/2611.16642) · [PDF](https://arxiv.org/pdf/2611.16642) · [HF](https://huggingface.co/papers/2611.16642)

The task of dataset distillation concerns the learning of a small set of synthetic samples that can serve as an effective replacement for a large real dataset when used for downstream tasks. While many solutions have been proposed since the problem's inception, most of them primarily seek to optimize the distilled data with respect to a classifier. In this work, we propose a new distillation method that learns a set…

## 50. A Reinforcement Learning Method to Navigate SMEFT Operator Space

- 分数：13.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：agent, reinforcement learning
- 作者：Jacky Kumar
- 链接：[arXiv](https://arxiv.org/abs/2611.21439) · [PDF](https://arxiv.org/pdf/2611.21439) · [HF](https://huggingface.co/papers/2611.21439)

In particle physics, discrepancies between experimental measurements and Standard Model (SM) predictions are commonly interpreted within new theoretical models. In this context, the Standard Model Effective Field Theory (SMEFT) provides a general framework encompassing a broad class of models. However, exploring the enormous space of possible SMEFT operators rapidly becomes a challenging combinatorial problem: many…

## 51. MPEG-Diffusion: Mixed-Resolution Video Generation

- 分数：13.0  ·  HF 赞：6  ·  来源：huggingface
- 兴趣命中：coding
- 作者：Dennis Menn, Tianpei Gu, Guande He, Aryan V S, Yanke Song, Nan Liu, Desai Xie, Xun Huang, Chenfeng Xu, Diana Marculescu
- 链接：[arXiv](https://arxiv.org/abs/2611.12069) · [PDF](https://arxiv.org/pdf/2611.12069) · [HF](https://huggingface.co/papers/2611.12069)

Video diffusion transformers (DiTs) generate realistic videos, but their heavy computational cost limits broader real-world applications. Mixed-resolution generation reduces this cost by generating the visually important region at high resolution (HR) and the rest at low resolution (LR), yet existing methods suffer a severe quality drop on videos and require knowing the HR region in advance. We show that these…

## 52. JEPA4R: Embodied JEPA World Models with 4D Point Planning

- 分数：12.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：planning
- 作者：Jiarui Dong, Zhiheng Liang, Yanjun Li, Zeyu Zhang, Heejeong Nam, Haoyu Chen, Hao Tang
- 链接：[arXiv](https://arxiv.org/abs/2611.19771) · [PDF](https://arxiv.org/pdf/2611.19771) · [HF](https://huggingface.co/papers/2611.19771)

Joint-embedding predictive architecture (JEPA) world models predict future embeddings instead of pixels and plan in latent space. Two challenges remain: 2D images leave the metric geometry that manipulation acts on implicit and entangled with appearance, and what these models imagine stays hidden, as they are mostly judged in simulation by short-horizon latent planning. We present JEPA4R, a JEPA world model that…

## 53. GlyphAtlas: Disentangling Stroke Detail from Layout for Scene Text Synthesis

- 分数：12.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：spec
- 作者：Luozheng Qin, Changhai Zhou, Yiyi Zhou
- 链接：[arXiv](https://arxiv.org/abs/2611.20192) · [PDF](https://arxiv.org/pdf/2611.20192) · [HF](https://huggingface.co/papers/2611.20192)

Scene text synthesis requires stroke-accurate characters rendered in a specified layout, as well as visual coherence with the surrounding scene. To achieve this, existing methods commonly pre-render the target text at its intended locations to form a glyph image that jointly specifies layout and glyph structure. However, this representation ties the resolution of each glyph to its target region, limiting…

## 54. Marimba: A System One Model for Speech

- 分数：11.5  ·  HF 赞：7  ·  来源：huggingface
- 兴趣命中：-
- 作者：Solano Amadori
- 链接：[arXiv](https://arxiv.org/abs/2611.18330) · [PDF](https://arxiv.org/pdf/2611.18330) · [HF](https://huggingface.co/papers/2611.18330)

Speech applications require decisions about term presence, turn completion, and language within an audio window. We present Marimba, an interface for typed speech decisions built on frozen Qwen3-ASR 0.6B features. Lexical questions use zero-shot scoring of ASR transcripts; non-lexical questions use a question-conditioned head and a separate layer-18 turn-end readout. Language identification uses the ASR model's own…

## 55. Correct Labels Are Not Enough: Reliable Metadata Can Silently Control Model Behavior

- 分数：11.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：evaluation
- 作者：Renee Jia, Jinzhou Wu
- 链接：[arXiv](https://arxiv.org/abs/2611.04395) · [PDF](https://arxiv.org/pdf/2611.04395) · [HF](https://huggingface.co/papers/2611.04395)

Fine-tuning data can include metadata that predicts the correct answer, such as a reward-model score or a quality label. We ask whether a model learns to rely on this metadata even when every training label is correct. We fine-tune 7-9B open-weight models from three families on multiple-choice questions in which (Reward: 5) always marks the correct option; when this annotation is moved to a wrong option at test…

## 56. Centered Ablation: Why Last-Layer Directional Ablation Under-Fires or Collapses, and a Closed-Form Fix

- 分数：11.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：language model
- 作者：Quy-Anh Dang, Chris Ngo
- 链接：[arXiv](https://arxiv.org/abs/2611.20148) · [PDF](https://arxiv.org/pdf/2611.20148) · [HF](https://huggingface.co/papers/2611.20148)

Directional ablation removes a hidden state's component along a "behaviour direction" while a language model runs. It is the standard way to switch a behaviour such as refusal off, but it is erratic: on some models it barely fires, on others the text collapses into repetition. We show why, and fix it. At the last residual stream, ablation is exactly a logit bias: a fixed vocabulary footprint scaled by a gate, the…

## 57. Invariant-Aware Harness Enforcement to Protect LLM Agents from Silent API Failures

- 分数：11.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：agent
- 作者：Sajib Acharjee Dip, Brian Ouyang, Lala Motlhabi
- 链接：[arXiv](https://arxiv.org/abs/2611.20595) · [PDF](https://arxiv.org/pdf/2611.20595) · [HF](https://huggingface.co/papers/2611.20595)

LLM agents answer questions by calling APIs and trusting the results. An API can fail silently. It ignores part of a request, such as a misnamed filter, yet returns HTTP 200 and a plausible but wrong result. Current fixes, such as checklists, reviewer models and LLM judges, ask the model to catch it. But models often see the problem and answer anyway. We present SilentGuard, which moves the decision from the model…

## 58. Latent Feedback Is a Compute and Data Amplifier

- 分数：11.0  ·  HF 赞：6  ·  来源：huggingface
- 兴趣命中：-
- 作者：Benhao Huang, Chaitanya Dwivedi, Xuezhe Ma, Alexander Moreno, Hector Liu
- 链接：[arXiv](https://arxiv.org/abs/2611.20404) · [PDF](https://arxiv.org/pdf/2611.20404) · [HF](https://huggingface.co/papers/2611.20404)

When high-quality data runs out, a common practice is to train on it for several epochs, but each repeat is worth less than the last. Latent feedback, which feeds each token's top-layer state into the next token's input, is another way to spend that compute, yet it has not been tested against a vanilla Transformer that spends the same compute on more epochs. We run this test across a ladder of model sizes, unique…

## 59. Glyph: An Interpretability Engine for AI-Driven Scientific Discovery in Clinical Data

- 分数：11.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：agent
- 作者：Robbie Holland, Ashwin Kumar, Mateus A. Esmeraldo, David Le, Andrea Fisher, Jiazhen Pan, Louisa Fay, Magdalini Paschali, Vasiliki Sideri-Lampretsa, Ates Fettahoglu, Stefania Moroianu, Philipp Wesp, Ivan Lopez, Tom Nuno Wolf, McKenzie S. White, Eduardo Pontes Reis, Fatima Rodriguez, Curtis P. Langlotz, Vasilis Syrgkanis, Imon Banerjee, Akshay S. Chaudhari, Sergios Gatidis
- 链接：[arXiv](https://arxiv.org/abs/2611.08922) · [PDF](https://arxiv.org/pdf/2611.08922) · [HF](https://huggingface.co/papers/2611.08922)

Automated scientific discovery has the potential to advance understanding of disease mechanisms and accelerate identification of early disease markers. Manual data annotation is infeasible at population scale, motivating methods that automatically extract pre-defined phenotypes in multimodal and unstructured clinical data. Such pre-defined feature sets determine and limit which associations these approaches can…

## 60. Ego Guidance: Enhancing Robot Policy Learning with Action-Free Human Egocentric Videos

- 分数：10.5  ·  HF 赞：5  ·  来源：huggingface
- 兴趣命中：-
- 作者：Lin Long, Tianren Ma, Zhong Chu, Di Wu, Maosong Cao, Qixiang Ye, Junbo Zhao, Shanghang Zhang
- 链接：[arXiv](https://arxiv.org/abs/2611.13685) · [PDF](https://arxiv.org/pdf/2611.13685) · [HF](https://huggingface.co/papers/2611.13685)

In this paper, we investigate how human egocentric videos can benefit robot policy learning without action supervision. Building on a pretrained VLM, we propose Shared Prediction on Action and Representation (SPAR), an MoT architecture in which future visual state prediction can provide independent and complementary learning signals alongside action prediction. We find that representations learned from egocentric…

## 61. Zuse: A Decision Model for European Languages

- 分数：9.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：-
- 作者：Umair Mehmood Imam
- 链接：[arXiv](https://arxiv.org/abs/2611.06238) · [PDF](https://arxiv.org/pdf/2611.06238) · [HF](https://huggingface.co/papers/2611.06238)

Decision models read a document and return a probability for each of a fixed set of options instead of generating text. Several appeared in 2026, but none has published results outside English. We describe Zuse, three decision models (4B, 9B and 27B) that train a low-rank adapter and a pointer head on frozen open-weight bases, targeting 27 European languages, and use them to study how this design behaves across…

## 62. From Perception to Simulation: Unveiling and Empowering Mental Spatial Dynamics in MLLMs

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, evaluation, benchmark, language model, large language, spec
- 作者：Jiachun Li, Zhuoran Jin, Kang Liu, Jun Zhao
- 链接：[arXiv](https://arxiv.org/abs/2611.22541) · [PDF](https://arxiv.org/pdf/2611.22541) · [HF](https://huggingface.co/papers/2611.22541)

Spatial reasoning is a fundamental component of world understanding for Multimodal Large Language Models (MLLMs). While existing research has advanced the perception of spatial relations in static scenes, the domain of dynamic spatial simulation remains relatively unexplored. To bridge this gap, we introduce MentalGrid, a benchmark focused on spatial reasoning tasks that require models to simulate evolving spatial…

## 63. MillBill: A Machining Agent with Geometric Feedback

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, language model, spec, planning
- 作者：Gennadii Savrasov, Artem Slavin, Soslan Kabisov, Andrey Kuznetsov, Anton Konushin, Dmitrii Zhemchuzhnikov
- 链接：[arXiv](https://arxiv.org/abs/2611.22565) · [PDF](https://arxiv.org/pdf/2611.22565) · [HF](https://huggingface.co/papers/2611.22565)

Turning a CAD model into a machining program requires both process knowledge and geometric precision. Language models can generate such workflows by writing geometry and toolpath code for each part, but this makes numerical execution part of the model's task. We introduce MillBill, an agent that separates machining decisions from their geometric execution and verification. Given a boundary-representation part,…

## 64. Do LLMs Understand Network Traces? A Comparative Study of Reasoning over Raw and Filtered Traffic Data

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, evaluation, language model, large language
- 作者：Irene Gosálvez-White, Roberto Magán-Carrión, Carlota de la Vega-Soriano, Pedro García-Teodoro
- 链接：[arXiv](https://arxiv.org/abs/2611.22575) · [PDF](https://arxiv.org/pdf/2611.22575) · [HF](https://huggingface.co/papers/2611.22575)

The effective delivery and monitoring of ICT services rely heavily on network traffic analysis. However, interpreting complex packet captures remains a challenging task that requires substantial technical expertise. Large language models (LLMs) offer promising opportunities to automate network traffic in- vestigation, yet their reliability in packet-level field extraction and flow-level sequence reconstruction…

## 65. Semantic-Guided Geometric Decoding for Token-Efficient Visual Grounding

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, language model, large language, coding, spec
- 作者：Zhaojie Chen, Junyan Yang, Le Yang, Qi Dang, Yucheng Huang, Qianyi Che, Zhaoqiang Chen, Xinqi Zhu, Qiang Zhao
- 链接：[arXiv](https://arxiv.org/abs/2611.22577) · [PDF](https://arxiv.org/pdf/2611.22577) · [HF](https://huggingface.co/papers/2611.22577)

Multimodal large language models (MLLMs) provide a unified interface for language-conditioned visual perception. In pixel-to-sequence grounding, autoregressive coordinate generation requires multiple sequential decoding steps per box, increasing inference cost with the number of instances. Pixel-to-embedding methods reduce this overhead but lack explicit spatial encoding when using a shared special token. We…

## 66. AfriNORM: An Evaluation Benchmark for Normative Reasoning of LLMs Across African Cultures

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, evaluation, benchmark, language model, large language
- 作者：Ahmad Samuel Gali, Tadesse Destaw Belay, Idris Abdulmumin, Seid Muhie Yimam, Shamsuddeen Hassan Muhammad
- 链接：[arXiv](https://arxiv.org/abs/2611.22580) · [PDF](https://arxiv.org/pdf/2611.22580) · [HF](https://huggingface.co/papers/2611.22580)

Large language models (LLMs) are increasingly deployed across various sectors. However, current evaluation benchmarks are insufficient to assess the applicability of these models in local African contexts, as most focus on linguistic fluency (grammar/translation) rather than cultural competence. The few existing benchmarks that measure general knowledge or social conventions do not capture the African deontic…

## 67. Adaptive LLM-Driven Honeypots vs. LLM-Driven Attackers: Does Narrative Coherence Improve Deception?

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, language model, large language, spec
- 作者：Pedro Beltrán-López, Raul Gonzalez Jimenez, Dario Maddaloni, Manuel Gil Pérez, Pantaleone Nespoli
- 链接：[arXiv](https://arxiv.org/abs/2611.22589) · [PDF](https://arxiv.org/pdf/2611.22589) · [HF](https://huggingface.co/papers/2611.22589)

Large Language Models (LLMs) enable honeypots to generate responses and deceptive artefacts on demand, yet existing approaches evaluate generated content one reply at a time and leave open whether artefacts that jointly describe a coherent event retain an attacker better than unrelated ones. This question becomes pressing as autonomous LLM-driven offensive agents emerge as realistic adversaries. This paper proposes…

## 68. PACT: Plan-Action Consistency Training by Preserving Correct Plans and Repairing Actions in GUI Agents

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reasoning, reinforcement learning, benchmark, planning
- 作者：Zhuohan Cai, Zhangxuan Gu, Runze Li, Beitong Zhou, Ming Wen, Hongbo Yu, Shuheng Shen, Changhua Meng
- 链接：[arXiv](https://arxiv.org/abs/2611.22591) · [PDF](https://arxiv.org/pdf/2611.22591) · [HF](https://huggingface.co/papers/2611.22591)

GUI agents can formulate a correct immediate plan in their reasoning yet emit an action that fails to execute it, creating an execution gap. This recurring mismatch undermines reliable task completion, as a single execution error can derail a multi-step workflow. In outcome-supervised reinforcement learning, broadcasting a negative response-level advantage across all generated tokens risks penalizing valid planning…

## 69. SpatialCast: Reading the 3D World via Cast Shadows

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, reasoning, evaluation, benchmark, language model, large language
- 作者：Enhan Li, Jinghao Zhou, Jiaze Zhang, Hongyang Du
- 链接：[arXiv](https://arxiv.org/abs/2611.22657) · [PDF](https://arxiv.org/pdf/2611.22657) · [HF](https://huggingface.co/papers/2611.22657)

As multimodal large language models (MLLMs) advance toward understanding and interacting with the physical world, spatial reasoning becomes essential for understanding scene structure and anticipating the effects of physical changes. Existing spatial benchmarks have made substantial progress in evaluating spatial relations, memory, and viewpoint reasoning, but less systematically assess how models connect physical…

## 70. FVScore: Specification-Driven Neuro-Symbolic Video Evaluation

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, evaluation, benchmark, spec
- 作者：Do Xuan Long, Long T. Le, Yiwen Song, Min-Yen Kan, Tomas Pfister, Yale Song
- 链接：[arXiv](https://arxiv.org/abs/2611.22673) · [PDF](https://arxiv.org/pdf/2611.22673) · [HF](https://huggingface.co/papers/2611.22673)

We introduce Faithfulness Video Score (FVSCORE), a neuro-symbolic framework for specification-driven video generation evaluation. Existing evaluators rely on holistic MLLM judgments or vision-language metrics, yet aligning their scores with human judgments and tracing them to specific temporal violations remain open challenges. FVSCORE addresses these limitations by compiling each video into explicit propositions…

## 71. Cross-cultural Adaptation of Recipes for Low-Resource Languages: A Benchmark and Multilingual Culinary Lexicon for Hausa, Yorùbá, and Igbo

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, language model, large language
- 作者：Nuhu Ibrahim, Maryam Abdulazeez, Fatsuma Jauro, Salisu Aliyu, Robert Stevens, Riza Batista-Navarro
- 链接：[arXiv](https://arxiv.org/abs/2611.22708) · [PDF](https://arxiv.org/pdf/2611.22708) · [HF](https://huggingface.co/papers/2611.22708)

Recent multilingual large language models (LLMs) have improved machine translation, yet culturally adaptive translation for low-resource languages (LRLs) remains underexplored. This is particularly challenging for recipes, where ingredients, cooking tools, measurements, and procedures may require adaptation to the target cultural context. In this work, we introduce ReciLoReL, a benchmark of 600 expert-translated and…

## 72. Teaching What to Look For: Privileged Perception Questions for Agentic On-Policy Distillation in Video Captioning

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reasoning, evaluation, benchmark, spec
- 作者：Yifan Xu, Ruopeng Gao, Zhixiao Wang, Jiafu Tang, Yichun Yang, Zihao Wang, Yuanxing Zhang, Limin Wang
- 链接：[arXiv](https://arxiv.org/abs/2611.22755) · [PDF](https://arxiv.org/pdf/2611.22755) · [HF](https://huggingface.co/papers/2611.22755)

Detailed video captioning requires comprehensive and faithful descriptions of objects, actions, and temporal events. Fixed-frame sampling, however, can miss brief motions, small objects, and other fine-grained evidence, motivating captioning agents that actively seek relevant moments and inspect local regions. Training such behavior is challenging because, unlike video question answering, generic captioning…

## 73. StitchRAG: Constructing Compact and Evidence-Preserving Contexts for RAG with Diffusion-Based Stitching

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, language model, large language, retrieval
- 作者：Minsang Kim, Junpyo Lim, Heeje Cho, Seungjun Baek
- 链接：[arXiv](https://arxiv.org/abs/2611.22766) · [PDF](https://arxiv.org/pdf/2611.22766) · [HF](https://huggingface.co/papers/2611.22766)

Retrieval-augmented generation (RAG) improves factuality by grounding large language models (LLMs) in external evidence. However, long retrieved contexts incur computational overhead and can even hurt performance due to noisy or irrelevant content. We propose \textsc{StitchRAG}, a framework for constructing compact context in RAG. \textsc{StitchRAG} builds a faithful, information-dense context while dynamically…

## 74. CrossEnv: Synthesizing Verifiable Cross-Environment Tasks for Long-Horizon Agent Training

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, tool use, benchmark, spec
- 作者：Zhengfeng Yu, Tian Lan, Zhijing Wu, Enbo Zhao, Xuannan Liu, Feihu Jiang, Qianghuai Jia, Longyue Wang, Zhao Xu, Weihua Luo, Xian-Ling Mao
- 链接：[arXiv](https://arxiv.org/abs/2611.22777) · [PDF](https://arxiv.org/pdf/2611.22777) · [HF](https://huggingface.co/papers/2611.22777)

Executable synthetic environments provide scalable training tasks and verifiable feedback for long-horizon agents. Existing environment synthesis methods primarily generate tasks within individual environments. However, these tasks do not adequately capture real-world interactions across services, where actions in one service depend on information obtained from another. Synthesizing such tasks is challenging because…

## 75. Compact and Decodable Electrocardiogram Text for Large Language Models

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：language model, large language, coding, spec
- 作者：Elif Dorukbaşı, İlker Türker
- 链接：[arXiv](https://arxiv.org/abs/2611.22827) · [PDF](https://arxiv.org/pdf/2611.22827) · [HF](https://huggingface.co/papers/2611.22827)

When a twelve-lead electrocardiogram is written as text for a large language model, the number of tokens has to be balanced against the information lost through compression. This paper presents a deterministic encoding that writes eight independent leads as amplitude letters and exact time gaps and recovers the remaining four limb leads algebraically. The key points are selected with a cardiac-cycle-dependent…

## 76. Synergizing Evidence Retrieval and Utilization for Self-Improving Multimodal Scientific Document Reasoning

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reasoning, evaluation, benchmark, spec, retrieval
- 作者：Frank Nie, Ethan B. Liu, Yuan Zhu, Jindong Han
- 链接：[arXiv](https://arxiv.org/abs/2611.22837) · [PDF](https://arxiv.org/pdf/2611.22837) · [HF](https://huggingface.co/papers/2611.22837)

Scientific document reasoning requires an agent to acquire and integrate evidence distributed across text, figures, and tables. Retrieval can identify relevant sources while missing complementary support, and answer-level feedback alone does not reveal whether an error stems from evidence acquisition or evidence use. We present an agentic Retriever--Perceiver--Reasoner framework for multimodal scientific document…

## 77. WATERFALL: Workflow for Adaptive Training with Evolutionary Reward Formulation and Automated Learning Loops

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, reinforcement learning, benchmark, language model
- 作者：Eleftherios Triantafyllidis, Filippos Christianos, Zhibin Li, Bernd Bickel
- 链接：[arXiv](https://arxiv.org/abs/2611.22854) · [PDF](https://arxiv.org/pdf/2611.22854) · [HF](https://huggingface.co/papers/2611.22854)

Reward design remains a central bottleneck in reinforcement learning (RL), particularly in sparse-reward, long-horizon and partially observable settings requiring dependency chaining, memory, and deceptive affordance disambiguation. While recent foundation-model approaches reduce manual reward engineering, most assume goal-conditioning, task descriptions, expert demonstrations, or ground-truth metrics. These…

## 78. Learning Agent-Centric Vision-Language-Action World Models for Autonomous Driving

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reasoning, reinforcement learning, planning
- 作者：Guoqing Wang, Pin Tang, Xiangxuan Ren, Chao Ma
- 链接：[arXiv](https://arxiv.org/abs/2611.22880) · [PDF](https://arxiv.org/pdf/2611.22880) · [HF](https://huggingface.co/papers/2611.22880)

Recent progress in integrating vision-language-action (VLA) models with world modeling has significantly advanced end-to-end autonomous driving by allowing systems to reason about imagined futures instead of merely reacting to current observations. However, most world VLA models generate future frames at the pixel level with plenty of dense visual tokens. Although such generated futures can be visually plausible,…

## 79. When Do Typed Decision Models Work in Transportation? Evidence from Travel Choice and Traffic Signal Control

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reinforcement learning, evaluation, language model, large language
- 作者：Hongyang Zhang, Boyuan Deng, Siyuan Feng, Kai Chen, Junbo Zhang
- 链接：[arXiv](https://arxiv.org/abs/2611.22926) · [PDF](https://arxiv.org/pdf/2611.22926) · [HF](https://huggingface.co/papers/2611.22926)

Typed decision models combine natural-language understanding with a structured interface that returns a selected action and an option-level probability distribution without generating lengthy textual responses. Their low inference cost and response latency make them attractive for transportation problems with predefined alternatives. This paper investigates their effectiveness, robustness, and efficiency in two…

## 80. The Shared Word: Evaluating Language Models on Dutch Word Puzzles

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, evaluation, benchmark, language model, spec
- 作者：Rik van Noord, Maurice Voors
- 链接：[arXiv](https://arxiv.org/abs/2611.22935) · [PDF](https://arxiv.org/pdf/2611.22935) · [HF](https://huggingface.co/papers/2611.22935)

Many LLM benchmarks for languages other than English are translated, multiple-choice, or difficult to score automatically. We introduce The Shared Word (TSW-NL), a Dutch benchmark built around four core principles: it is language-specific, open-vocabulary, human-curated, and deterministically scored. Each puzzle gives three clues that describe different senses or uses of the same Dutch word. The clues are…

## 81. The Kernel Reality Check: Benchmarking and Distilling Efficient Attention at Scale

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, evaluation, benchmark, language model
- 作者：Fırat Öncel, Cem Subakan, Mirco Ravanelli, Çağatay Yıldız
- 链接：[arXiv](https://arxiv.org/abs/2611.22947) · [PDF](https://arxiv.org/pdf/2611.22947) · [HF](https://huggingface.co/papers/2611.22947)

Kernelized attention methods, which aim to replace the $O(N^2)$ complexity of softmax attention with $O(N)$ alternatives, have been the focus of intense research in the last five years. Despite growing interest, systematic evaluations and fair comparisons across approaches and scales are still missing. We analyze kernelized attention in two halves and highlight prominent limitations on each. On efficiency,…

## 82. CodeReel: Accelerating Code-to-Video Agents with Exact Frame Reuse and Blocking-Aware Scheduling

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, benchmark, coding, spec
- 作者：Junyi Shen, Yao Lu
- 链接：[arXiv](https://arxiv.org/abs/2611.22967) · [PDF](https://arxiv.org/pdf/2611.22967) · [HF](https://huggingface.co/papers/2611.22967)

Coding agents make videos by writing and refining programs in a build--inspect--edit loop. A finished film costs a median of $2.85 in model calls and 11 minutes, over a third of that time in builds that block the agent. We find that much of this time is avoidable, for two reasons. First, 37.5% of the frames of a session's later films were drawn before, many shifted in time or inside an edited scene. Second, half of…

## 83. VITAL: A Framework for Validating Agentic AI in Pharmaceutical Drug Development and Clinical Trial Operations

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reasoning, evaluation, retrieval
- 作者：Sandeep Burugupalli, Pedro Matos-Filipe, Andrea Hita Ardiaca, Adam Taylor, Alex Grigorenko, Natalia Jakubiak, Xin Yu, Raghav Mani, Sherry Mangla, Alvi Lai, Rachel C. Mercado, Pratik Shah, Raja Shankar
- 链接：[arXiv](https://arxiv.org/abs/2611.22973) · [PDF](https://arxiv.org/pdf/2611.22973) · [HF](https://huggingface.co/papers/2611.22973)

Current assurance approaches do not establish whether evidence is sufficient to validate, monitor and govern agentic artificial intelligence (AI) within a pharmaceutical context of use. Plausible outputs may conceal failures in retrieval, reasoning, orchestration or human-control points, where reference standards are unavailable. We developed and operationalised VITAL (Validation by Intended use, Traceability,…

## 84. Structured AI ideation yields physical strategies for epithelial barrier repair

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, language model, large language, spec
- 作者：Geonho Nah, Johyun Park, Kyung-Ah Cho, Suyoung Hwang, Yoon Hee Lim, Eun-kyung Min, Seunghyun Moon, Donghyun Koh, Seungwon Kim, Jiho Park, Hojin Yoo, Myungsun Nam, Haneul Choi, Kyungsu Kim, In-Sun Hong, YunJae Jung, Minhyeong Lee
- 链接：[arXiv](https://arxiv.org/abs/2611.22988) · [PDF](https://arxiv.org/pdf/2611.22988) · [HF](https://huggingface.co/papers/2611.22988)

AI systems increasingly support literature analysis, candidate evaluation and hypothesis refinement, but enabling researchers to explore research directions beyond established disciplinary approaches remains challenging. We developed Abelio, an AI system designed to generate novel research directions by expanding investigators' avenues of inquiry. Abelio reformulates research objectives, uses these alternative…

## 85. PhysScope: Agentic Multimodal Physics Reasoning with Grounded Visual Memory

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, memory, reasoning, benchmark, language model
- 作者：Haoyang Liu, Kecheng Liang, Xinyu Li, Weixing Chen, Yang Liu
- 链接：[arXiv](https://arxiv.org/abs/2611.23010) · [PDF](https://arxiv.org/pdf/2611.23010) · [HF](https://huggingface.co/papers/2611.23010)

Vision-language models (VLMs) can correctly interpret physics diagrams yet apply constraints outside the states or conditions in which they hold, causing premise errors to propagate through subsequent calculations. We introduce PhysScope, an inference-time visual harness that supports self-correction of these scope mismatches without updating model weights. PhysScope enables the model to link physical scopes…

## 86. M3OPD-Reasoner: An Open Recipe for Post-Training Multimodal Reasoning with Multi-Teacher On-Policy Distillation

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, reinforcement learning, benchmark, language model
- 作者：Nguyen Quang Trung, Hoang Phan, Shuo Sun, Longyin Zhang, AiTi Aw
- 链接：[arXiv](https://arxiv.org/abs/2611.23034) · [PDF](https://arxiv.org/pdf/2611.23034) · [HF](https://huggingface.co/papers/2611.23034)

Multi-Teacher On-Policy Distillation (MOPD) enables a single student to absorb the skills of several domain teachers by learning from its own generated responses. We present Multimodal Model Multi-Teacher On-Policy Distillation Reasoner (M3OPD-Reasoner), a fully open recipe for post-training vision-language models (VLMs) over three reasoning domains: image STEM, image perception, and video. We curate two datasets,…

## 87. ForecastGym: A Live, Controlled, and Replayable Benchmark for Forecasting Agents

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, memory, reasoning, evaluation, benchmark, language model, large language, spec, retrieval
- 作者：Yicheng Tao, Yuante Li, Zipei Fan
- 链接：[arXiv](https://arxiv.org/abs/2611.23045) · [PDF](https://arxiv.org/pdf/2611.23045) · [HF](https://huggingface.co/papers/2611.23045)

Agents built on large language models (LLMs) increasingly forecast real-world events by searching the Web and reasoning over what they find. How well such an agent forecasts depends on both the retrieved evidence and the model, making control over that evidence essential for evaluation. Live evaluations can mix retrieval with reasoning when each system searches on its own, while retrospective search can leak later…

## 88. Natural Language Programming: Rethinking Language, Memory, and Cognition in the Era of Generative AI

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, reasoning, language model, large language, spec
- 作者：Giovanni Adorni, Daniele Grosso
- 链接：[arXiv](https://arxiv.org/abs/2611.23106) · [PDF](https://arxiv.org/pdf/2611.23106) · [HF](https://huggingface.co/papers/2611.23106)

Generative Artificial Intelligence is transforming the role of natural language in computational systems. In classical Natural Language Processing (NLP), language was treated as an object of computation: something to analyse, classify, translate, or generate. Large Language Models (LLMs) challenge this perspective, enabling natural language to function increasingly as an executable cognitive medium through which…

## 89. VIVID: Beyond Static Multi-Image Reasoning with Localized Visual Differences and Textual Entity Dynamics in Video MLLMs

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, reasoning, language model, large language, coding, planning
- 作者：Chengqian Ma, Yuanze Zeng, Hongyu Wang, Mingfeng Lin, YiCheng Xiao, Yu Chen, Pengyu Li, WenHao Wang, Yuexiao Ma, Xiawu Zheng, Fei Chao
- 链接：[arXiv](https://arxiv.org/abs/2611.23153) · [PDF](https://arxiv.org/pdf/2611.23153) · [HF](https://huggingface.co/papers/2611.23153)

Video question answering under tight frame budgets requires preserving localized motion and event order, yet current video multimodal large language models (MLLMs) reduce comprehension to static multi-image reasoning by discarding unselected frames and encoding keyframes independently: (1) Spatially, whole-frame pooling dilutes small moving targets into static backgrounds; (2) Temporally, dropping intermediate…

## 90. Learning Grounded Reasoning from Human Gaze

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, reinforcement learning, evaluation, language model
- 作者：Gabriel Sarch, Declan Campbell, Nicholas Budny, Kia Ghods, Katerina Fragkiadaki, Jonathan D. Cohen, Brenden M. Lake, Taylor W. Webb
- 链接：[arXiv](https://arxiv.org/abs/2611.23209) · [PDF](https://arxiv.org/pdf/2611.23209) · [HF](https://huggingface.co/papers/2611.23209)

Human visual reasoning is driven by systematic exploration and extraction of task-relevant visual evidence. Human gaze provides a window into this process, making gaze a useful source of guidance for visually-grounded reasoning in vision-language models (VLMs). However, human gaze also includes noise and redundancies that may transfer poorly to VLMs. In this work, we investigate how human gaze data can be…

## 91. StringQFT: A Multiuse Textbook Resource for AI-Assisted Theoretical Physics

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, tool use, benchmark, spec, retrieval
- 作者：Xingyang Yu
- 链接：[arXiv](https://arxiv.org/abs/2611.23225) · [PDF](https://arxiv.org/pdf/2611.23225) · [HF](https://huggingface.co/papers/2611.23225)

We present StringQFT as a textbook collection for string constructions of quantum field theory and as infrastructure for AI-assisted theoretical physics. The collection comprises 18 volumes, 190 chapters and 3,795 pages, covering brane probes, brane webs, geometric engineering, F-theory constructions, wrapped M5-branes and exact worldsheet constructions. Its open-book benchmark inventory contains 1,073 items,…

## 92. Spool: Low-Latency Streaming Inference for Hybrid Vision-Language Models

- 分数：9.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reasoning, benchmark, language model
- 作者：Rui Ning, Om Chabra, Hari Balakrishnan
- 链接：[arXiv](https://arxiv.org/abs/2611.23228) · [PDF](https://arxiv.org/pdf/2611.23228) · [HF](https://huggingface.co/papers/2611.23228)

Applications such as visual accessibility agents and robotics require answering questions about recent video content promptly, over a bounded window of past frames (e.g., the last two minutes). Hybrid vision-language models (VLMs), which interleave attention with linear recurrent layers such as Gated DeltaNet (GDN), are attractive for this setting, but maintaining a sliding window is expensive. The reason is that…

## 93. LMLineage: Content Lineage and Context Governance for LLM Agents

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, memory, reasoning
- 作者：Wei Hou, Jingxin Geng, Xin Chen, Zheqing Jiang
- 链接：[arXiv](https://arxiv.org/abs/2611.22511) · [PDF](https://arxiv.org/pdf/2611.22511) · [HF](https://huggingface.co/papers/2611.22511)

Interpretability for AI agents should not be confined to understanding the model's internal weights. It must also cover the agent's reasoning and decision-making process over multi-source context. We present LMLineage, an out-of-band system that attributes every output sentence of an agent session to its supporting input spans with calibrated confidences, without requiring white-box access to the model or any…

## 94. MM-ReportBench: A Comprehensive Benchmark for Multimodal Report Generation from Tables

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, language model
- 作者：Teng Lin, Nan Tang
- 链接：[arXiv](https://arxiv.org/abs/2611.22514) · [PDF](https://arxiv.org/pdf/2611.22514) · [HF](https://huggingface.co/papers/2611.22514)

The ability to generate multimodal reports integrating fluent narratives with faithful visualizations from tabular data, has become a cornerstone capability for modern vision-language models in practical domains such as finance, healthcare, and policy making. However, existing benchmarks are limited by single-modality focus, simplistic metrics, novelty evaluation, and visualization quality. We address these…

## 95. When Agent Skills Go Stale: Runtime Behavior and Selective Maintenance in Evolving Environments

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reasoning, spec
- 作者：Ömer Faruk Akgül, Shuli Jiang, Yuting Zhang, Yi Zhang, Xiaohan Fei, Wei Xia, Stefano Soatto
- 链接：[arXiv](https://arxiv.org/abs/2611.22525) · [PDF](https://arxiv.org/pdf/2611.22525) · [HF](https://huggingface.co/papers/2611.22525)

Agent skills use past experience and current observations to guide decisions and actions on related tasks. This experience is retained in skill state, whose reuse can amortize inference-time reasoning and environment interaction. When environment changes, parts of this state can become outdated while others remain useful. Across four task settings and two models, we compare skill reuse before and after environment…

## 96. CADMAGEDDON: High-Fidelity CAD Reconstruction with Local Inference

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reasoning, benchmark
- 作者：Oleg Pavlov, Nikita Gavrilov, Soslan Kabisov, Gennadii Savrasov, Andrey Kuznetsov, Anton Konushin, Dmitrii Zhemchuzhnikov
- 链接：[arXiv](https://arxiv.org/abs/2611.22563) · [PDF](https://arxiv.org/pdf/2611.22563) · [HF](https://huggingface.co/papers/2611.22563)

CAD practitioners often work with proprietary parts that they are unwilling to share with external services. For individuals and small companies, bringing this work in-house also requires computational resources they can afford. We introduce CADMAGEDDON, an open-source agent that reconstructs editable CAD from meshes and can run locally on single-GPU systems and current-generation laptops. The method decomposes this…

## 97. PlaceTally: A Test-Time Memory Model for Constructing Place Graphs

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, benchmark, language model
- 作者：Alibay Osmanli, Shaogang Gong
- 链接：[arXiv](https://arxiv.org/abs/2611.22608) · [PDF](https://arxiv.org/pdf/2611.22608) · [HF](https://huggingface.co/papers/2611.22608)

Counting distinct objects in a video is hard when the camera returns to places it has seen. A vision-language model that reads the whole video answers with a few small numbers, and one that reads it in parts counts an object again in every part that shows it. Object trackers need the category before the video is read, or a fixed vocabulary. We observe that a memory for counting does not need to know what it is…

## 98. EvoSkill-S1: Evolving Reusable Skills with Genetic-Inspired Operators

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, benchmark, spec
- 作者：Yujun Wang, Jiqiang Li, Yinuo Lu, Jinhe Bi,  Aniri, Wenxuan Ye, Boliang Liu, Sikuan Yan, Shuning Wang, Xuebing Zhou, S{ö}ren Pirk, Hinrich Sch{ü}tze, Yunpu Ma
- 链接：[arXiv](https://arxiv.org/abs/2611.22610) · [PDF](https://arxiv.org/pdf/2611.22610) · [HF](https://huggingface.co/papers/2611.22610)

Reusable skills allow language-model agents to accumulate and reuse problem-solving experience. However, most existing methods improve a skill bank only indirectly through rollout-driven accumulation and heuristic reflection, often resulting in shallow and weakly controlled updates. We present EvoSkill-S1, an RL-driven framework that instead treats reusable skills themselves as the direct objects of evolution. Given…

## 99. Must You See Fakes to Catch Fakes? Language Says What to Look For, Real Images What to Ignore

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, spec
- 作者：Tianchi Xu, Yuxuan Zhou, Yuheng Zhang, Yanan Guan, Tao Dai, Shu-Tao Xia
- 链接：[arXiv](https://arxiv.org/abs/2611.22650) · [PDF](https://arxiv.org/pdf/2611.22650) · [HF](https://huggingface.co/papers/2611.22650)

Must a detector see generated images in order to catch them? Detection of AI-generated images has long faced two problems. The cues a detector learns from the few generators in its training set carry traces specific to those generators and transfer poorly to new ones, which limits generalization. The real and generated training images also differ in format and content, so the detector takes these differences as…

## 100. AlignedHPO: Efficient Surrogate-Guided Loss Hyperparameter Optimization

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, evaluation, spec
- 作者：Ivan Karpukhin, Andrey Savchenko
- 链接：[arXiv](https://arxiv.org/abs/2611.22658) · [PDF](https://arxiv.org/pdf/2611.22658) · [HF](https://huggingface.co/papers/2611.22658)

Modern deep learning losses involve multiple hyperparameters, such as weights, scales, and margins, typically tuned manually or through expensive black-box optimization despite their differentiability. We propose AlignedHPO, an efficient framework for tuning differentiable loss hyperparameters using gradient alignment and surrogate validation objectives. Our method employs Jacobian-vector products to reduce…

## 101. VSpark: Speculative Decoding for Autoregressive Vision-Language-Action Models

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, coding, spec
- 作者：Suho Yoo, Youngjoon Jang, Hyebin Cho, Taeyeop Lee, Jaewook Jeong, Joon Son Chung
- 链接：[arXiv](https://arxiv.org/abs/2611.22666) · [PDF](https://arxiv.org/pdf/2611.22666) · [HF](https://huggingface.co/papers/2611.22666)

Our aim is to accelerate autoregressive vision-language-action models (VLAs), which generate robot actions one token at a time. Speculative decoding makes this possible: a lightweight draft model proposes several tokens at once, and the VLA verifies them in a single pass, accepting only those that match its own predictions, so decoding remains lossless. The speedup, however, is limited in robot control, where many…

## 102. Worldviews in Large Language Models

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, language model, large language
- 作者：Edmundo Lopez-Sola, Shamil Chandaria, Ruben Laukkonen
- 链接：[arXiv](https://arxiv.org/abs/2611.22670) · [PDF](https://arxiv.org/pdf/2611.22670) · [HF](https://huggingface.co/papers/2611.22670)

Large language models (LLMs) are often described in terms of personas and this framing has become central to alignment research. In this paper, we argue that there is a deeper level of description that lies in the agent's worldviews, i.e., its beliefs about what reality is and how it works. Treating LLMs as a population of subjects, we administer two worldview surveys from human psychology to eight models. We show…

## 103. Making the World React Realistically: A Closed-Loop Interactive World Model for Autonomous Driving

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, reinforcement learning, evaluation
- 作者：Jia Hu, Yang Chang, Panqu Wang, Zhijun Fu, Chang Liu, Changjian Yu, Jintao Lai
- 链接：[arXiv](https://arxiv.org/abs/2611.22691) · [PDF](https://arxiv.org/pdf/2611.22691) · [HF](https://huggingface.co/papers/2611.22691)

World models (WMs) generate driving scenarios beyond recorded logs, enabling the training and evaluation of autonomous driving systems in unseen interactions. However, existing WMs struggle to ensure both behavioral realism and visual fidelity, since they overlook the relationship between vehicle interactions and the ego visual observations. We propose a closed-loop interactive WM that couples behavior modeling and…

## 104. Remembered as Brief: Stored Preferences SilentlyRemove Decision-Critical Information

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, benchmark, spec
- 作者：Joshua Adrian Cahyono
- 链接：[arXiv](https://arxiv.org/abs/2611.22697) · [PDF](https://arxiv.org/pdf/2611.22697) · [HF](https://huggingface.co/papers/2611.22697)

People increasingly learn what they need for decisions about health, money, law and safety from AI assistants, and what an assistant leaves out the user never sees. An answer with a warning removed can be true in every sentence, so fact-checks pass it, and an assistant with memory applies a preference stored once to later questions the user never had in mind. We introduce \bench{}, an Inspect benchmark of 100…

## 105. TANGO: Real-World Unregistered RGB-Guided Hyperspectral Super-Resolution with Two-Camera Acquisitions

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, spec
- 作者：Matteo Kolyszko, Marco Buzzelli, Simone Bianco, Raimondo Schettini
- 链接：[arXiv](https://arxiv.org/abs/2611.22699) · [PDF](https://arxiv.org/pdf/2611.22699) · [HF](https://huggingface.co/papers/2611.22699)

Unregistered hyperspectral image super-resolution aims to recover a high-resolution HSI from a low-resolution hyperspectral observation and an unregistered high-resolution RGB reference. Although recent methods have begun to address the geometric misalignment between the two modalities, their evaluation is still constrained by the lack of a large-scale public benchmark based on real two-camera RGB--HSI acquisitions…

## 106. LoopZip: Visual Token Compression for Efficient Looped Vision-Language Models

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, benchmark, language model
- 作者：Weizhong Huang, Zhicheng Liu, Yan Zhang, Fei Chao, Xiawu Zheng, Liujuan Cao
- 链接：[arXiv](https://arxiv.org/abs/2611.22728) · [PDF](https://arxiv.org/pdf/2611.22728) · [HF](https://huggingface.co/papers/2611.22728)

Looped vision-language models (VLMs) deepen computation by reusing shared layers, approaching larger models' capabilities with fewer parameters and easing the storage and deployment burden of stacking independent layers. However, repeatedly processing long visual sequences still incurs substantial compute and GPU memory costs. Visual token compression reduces these costs by shortening sequences. Existing methods…

## 107. LoopPrune: Recurrent Pruning for Looped Diffusion Transformers

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, benchmark, spec
- 作者：Weizhong Huang, Huaijia Kou, Yan Zhang, Fei Chao, Xiawu Zheng, Liujuan Cao
- 链接：[arXiv](https://arxiv.org/abs/2611.22757) · [PDF](https://arxiv.org/pdf/2611.22757) · [HF](https://huggingface.co/papers/2611.22757)

Looped diffusion Transformers reuse shared blocks to deepen computation and match larger models with fewer parameters, reducing storage and deployment burdens. Yet repeated attention and MLP computations remain costly. Pruning reduces storage and computation by removing redundant parameters or units. Training-free methods struggle to resolve recurrent contributions, while training-based methods lack explicit…

## 108. Network-Exposed Configuration Attacks on LLM-Controlled Social Robots

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：memory, language model, large language
- 作者：Stanley Akingbola, Ugbede Ibrahim, Yan Lin Aung, Quang Dan Le, Hong Qing Yu
- 链接：[arXiv](https://arxiv.org/abs/2611.22761) · [PDF](https://arxiv.org/pdf/2611.22761) · [HF](https://huggingface.co/papers/2611.22761)

Large language models (LLMs) in embodied robots create security dependencies beyond inference. We investigate a network-exposed configuration attack on the Pollen Robotics Reachy Mini Lite, allowing an unauthenticated attacker to replace personality settings and the cloud LLM's system prompt through a management interface, without adversarial conversational input. Eleven prompt-injection attempts across five…

## 109. PANO: Parallel Latent Space Neural Operator for Solving PDEs

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：benchmark, coding, spec
- 作者：Zijiang Yang, Xiaomeng Wu, Chen Kuang, Dongmei Fu
- 链接：[arXiv](https://arxiv.org/abs/2611.22782) · [PDF](https://arxiv.org/pdf/2611.22782) · [HF](https://huggingface.co/papers/2611.22782)

Aggregating observations into a limited number of latent tokens and learning physical interactions in the latent space has emerged as an effective approach for Transformer-based neural operators to solve Partial Differential Equation (PDE) problems involving large-scale observations. However, existing methods typically compress observations using a single aggregation pattern, making physical information not retained…

## 110. NexSight: Verifiable Tasks for Fine-Grained Agentic Long-Video Understanding

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, benchmark, spec
- 作者：Tianci Xie, Li Chen, Pinxue Guo, Rui Zheng
- 链接：[arXiv](https://arxiv.org/abs/2611.22790) · [PDF](https://arxiv.org/pdf/2611.22790) · [HF](https://huggingface.co/papers/2611.22790)

Fine-grained questions about long videos ask how many times an action occurs, in what order events unfold, or exactly when a state changes. Answering them can require finding brief moments scattered across hours of footage. Agentic models that decide when and where to look promise to find these moments, yet this ability is hard both to measure and to learn. Sparse supporting evidence may establish that an action…

## 111. Pixel is All You Need

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：reasoning, language model, large language
- 作者：Jie Chu, Haoting Shi, Fucheng Zhang, Jiawei Liu, Junwei Liao, Ying Wen, Muning Wen
- 链接：[arXiv](https://arxiv.org/abs/2611.22820) · [PDF](https://arxiv.org/pdf/2611.22820) · [HF](https://huggingface.co/papers/2611.22820)

Text, images, audio, touch, and even robot actions can, in principle, all be rendered onto a single canvas, suggesting an ambitious goal of unifying all modalities within vision. Language provides the natural first test. To subsume it, a visual model must reason directly over text in pixels. Across a wide range of image, video, and unified multimodal generators, however, we find that their visual generation modules…

## 112. OICycle: Observe, Infer, and Intervene Cycle for Belief-State Learning in Longitudinal Clinical Decision Making

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, spec
- 作者：Jitindra Fartiyal, Pedro Freire, Sergei K. Turitsyn, Sergei G. Solovski
- 链接：[arXiv](https://arxiv.org/abs/2611.22826) · [PDF](https://arxiv.org/pdf/2611.22826) · [HF](https://huggingface.co/papers/2611.22826)

Clinical care is a closed loop: clinicians observe partial evidence, infer the patient's state, and intervene, and each intervention determines what is observed next. This makes clinical decision making a partially observable Markov decision process (POMDP), in which a belief over a latent patient state must be updated from irregular, multimodal, and incomplete records. Yet most deep clinical models predict from a…

## 113. TabDAG: Structured Evolutionary Search for Tabular Feature Engineering

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, coding, spec
- 作者：Anastasia Volkova, Andrey Kuznetsov, Ivan Oseledets, Valentin Khrulkov
- 链接：[arXiv](https://arxiv.org/abs/2611.22828) · [PDF](https://arxiv.org/pdf/2611.22828) · [HF](https://huggingface.co/papers/2611.22828)

Feature engineering can improve tabular prediction, but useful transformations are compositional, data-dependent, and subject to leakage constraints. We present TabDAG, a framework that combines evolutionary search with a graph representation of feature-engineering programs. Nodes implement row-wise or data-fitted transformations; edges encode dependencies among raw variables, intermediate values, and final…

## 114. When Passing Checks Do Not Establish Completion: Evidence Interpretation in Coding Agents

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, coding, spec
- 作者：Xueping Gao
- 链接：[arXiv](https://arxiv.org/abs/2611.22835) · [PDF](https://arxiv.org/pdf/2611.22835) · [HF](https://huggingface.co/papers/2611.22835)

Verification procedures in coding agents must preserve execution facts, interpret their scope and discharge checking obligations. We study these responsibilities through qualified repository checks, controlled evidence consumers and executable workflows. A prospective thirteen-task factorial study finds that correct reported facts need not yield the requested finite verdict. Conversely, all 122 delivered labels in a…

## 115. CaFe: Causally Faithful Conditional Traffic Scenario Generation

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, evaluation, benchmark
- 作者：Steven Yu Tung, Shubham Vaijanath Phoolari, Christoph Lauer, Abhinav Valada, Steven Peters
- 链接：[arXiv](https://arxiv.org/abs/2611.22855) · [PDF](https://arxiv.org/pdf/2611.22855) · [HF](https://huggingface.co/papers/2611.22855)

Language-conditioned traffic simulation enables scalable test scenarios steered by natural language. The goal is to control selected agents while surrounding traffic reacts to their observed behaviour. For example, a vehicle instructed to cut in late should cause the following vehicle to brake only when the manoeuvre becomes observable. Yet simulators can leak private instructions across agents, causing surrounding…

## 116. Propose & Verify: Fast Reflection Symmetry Detection via Harmonic Fields

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, spec
- 作者：Yishai Lavi, Shai Avidan
- 链接：[arXiv](https://arxiv.org/abs/2611.22856) · [PDF](https://arxiv.org/pdf/2611.22856) · [HF](https://huggingface.co/papers/2611.22856)

Detecting multiple reflection symmetries in 3D shapes requires aggregating geometric evidence over a large space of candidate planes, making traditional voting approaches computationally expensive. We introduce the Fourier Accelerated Symmetry Transform (FAST), a training-free framework that combines geometric pair voting with efficient spectral computation. Exploiting the fact that global reflection planes pass…

## 117. SlideJev: Order-Stable and Tissue-Grounded Jev Decisions for Whole-Slide Pathology

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：evaluation, benchmark, language model
- 作者：Lei Wu, Jiashuai Liu, Di Zhang, Chunze Yang, Jiusong Ge, Junbo Lu, Yongqi Liang, Wenjie Zhao, Ni Zhang, Chen Li, Zeyu Gao, Qidong Liu
- 链接：[arXiv](https://arxiv.org/abs/2611.22879) · [PDF](https://arxiv.org/pdf/2611.22879) · [HF](https://huggingface.co/papers/2611.22879)

Whole-slide visual question answering (VQA) offers a natural-language interface to pathology, allowing diagnostic and phenotypic questions to be answered directly from tissue slides. However, current vision-language models (VLMs) rely heavily on linguistic priors: their answers are sensitive to the order of the candidate answers, and can be reached through shortcuts that bypass the tissue evidence. To address these…

## 118. Beyond Attribute-Centric Fairness: Modelling and Mitigating Unified Bias Representation in Omni-modal Large Language Models

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：language model, large language, spec
- 作者：Runqi Lin, Suqin Yuan, Zihao Fu, Chris Russell
- 链接：[arXiv](https://arxiv.org/abs/2611.22889) · [PDF](https://arxiv.org/pdf/2611.22889) · [HF](https://huggingface.co/papers/2611.22889)

Omni-modal large language models (OLLMs) provide joint multimodal understanding and generation capabilities, making them well-suited to complex environments and promising backbones for next-generation AI. Despite these advances, the harmful stereotypes encoded in such models manifest in increasingly diverse forms, leading to broader and more severe societal consequences. Existing debiasing methods typically impose…

## 119. Born for the Task: Rethinking Quantum Chemistry with Foresighted Agentic Computing

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, coding, spec
- 作者：Haozhi Han, Junjie Yang, Ruge Zhang, Zihe Huang, Pengyi Xu, Bo Zhang, Yunquan Zhang, Ting Cao, Yunxin Liu, Yifeng Chen, Kun Li
- 链接：[arXiv](https://arxiv.org/abs/2611.22897) · [PDF](https://arxiv.org/pdf/2611.22897) · [HF](https://huggingface.co/papers/2611.22897)

Quantum chemistry relies on general-purpose software, whose generality leaves many large-scale calculations beyond practical resource budgets. Coding agents make task-specific programs cheap to write, but not efficient ones easy to find: whether a computational strategy is accurate and fast enough becomes clear only after it actually runs at the target scale. We introduce BORN, a foresighted agentic computing…

## 120. Done, But Still Working: Anytime Evaluation of When Coding Agents Should Stop

- 分数：7.0  ·  HF 赞：0  ·  来源：arxiv
- 兴趣命中：agent, evaluation, coding
- 作者：Zerui Yang, Quan Xue, Miaomiao Dong, Chaorui Zhang, Xuanyu Zheng, Xiyuan Wang, Haolin Ruan, Xueyan Niu, Guangcheng Song, Weixi Zhang, Wei Han, Bo Bai
- 链接：[arXiv](https://arxiv.org/abs/2611.22901) · [PDF](https://arxiv.org/pdf/2611.22901) · [HF](https://huggingface.co/papers/2611.22901)

Coding agents often continue working after their own tests pass. Does this additional work improve the patch, and how much could be saved by stopping earlier? We study these questions through anytime evaluation: replaying recorded runs, scoring intermediate patches with hidden tests, and measuring the cost incurred at each step. For policies that only stop a run or select an earlier patch, this allows paired…
