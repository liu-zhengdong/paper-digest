# 每日 AI 论文

生成时间：2026-10-23 04:50 UTC  ·  共 82 篇（已按 arXiv ID 去重）

来源：Hugging Face Daily Papers + arXiv（cs.AI / cs.LG / cs.CL / cs.CV）。
排序：HF 上榜、点赞、多源命中、兴趣词。兴趣词可在 `config.json` 改。

## 1. SpatialScout: Can VLM Agents Actively Explore and Map 3D Scenes?

- 分数：36.0  ·  HF 赞：131  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark, language model
- 作者：Zhaoxi Zhang, Hao Liang, Linxuan Wu, Yiming Wu, Yifu Yuan, Kun Liang, Chenming Tang, Meiyi Qiang, Wentao Zhang, Weikang Li
- 链接：[arXiv](https://arxiv.org/abs/2610.26659) · [PDF](https://arxiv.org/pdf/2610.26659) · [HF](https://huggingface.co/papers/2610.26659)

Spatial intelligence requires agents to actively acquire visual evidence and integrate observations into a coherent representation of the three-dimensional world. Yet spatial question answering offers limited evidence of whether models can construct accurate metric maps through autonomous exploration. We introduce SpatialScout, a benchmark for evaluating vision-language model (VLM) agents on active object-level 3D…

## 2. Cache Engineering for Agents

- 分数：36.0  ·  HF 赞：119  ·  来源：huggingface
- 兴趣命中：agent, benchmark, language model, large language, coding, spec
- 作者：Tianyu Fu, Ruoxi Wang, Zihan Min, Zhongqi Ren, Zhihao Li, Tengxuan Liu, Shengxu Mu, Hanling Zhang, Yu Wang
- 链接：[arXiv](https://arxiv.org/abs/2610.28577) · [PDF](https://arxiv.org/pdf/2610.28577) · [HF](https://huggingface.co/papers/2610.28577)

Large Language Model (LLM) agents can handle increasingly complex tasks, navigating long trajectories of observations and actions. As these trajectories grow, key-value (KV) cache I/O and storage become the dominant cost. Trajectories can also exceed the LLM's maximum context length, requiring control over active cache growth. Prior work uses context engineering to reduce cache size by trimming or summarizing…

## 3. Agent World Model in the Wild: Computer-Use Agent Environment Synthesis

- 分数：36.0  ·  HF 赞：64  ·  来源：huggingface
- 兴趣命中：agent, tool use, benchmark, spec
- 作者：Zhaoyang Wang, Qianhui Wu, Haorui Wang, Simon Yu, Baolin Peng, Canwen Xu, Hao Cheng, Wenlin Yao, Boyi Liu, Yite Wang, Jianfeng Gao, Huaxiu Yao
- 链接：[arXiv](https://arxiv.org/abs/2610.26828) · [PDF](https://arxiv.org/pdf/2610.26828) · [HF](https://huggingface.co/papers/2610.26828)

Agent learning is shifting from learning from human data toward learning through interaction with the world. However, scaling such learning directly in real-world computer systems is challenging and can introduce substantial security risks. We therefore propose Agent World Model in the Wild (WildAWM), a scalable pipeline for synthesizing controllable environments and tasks for training general computer-use agents…

## 4. Deep Search in Real-World Web Environments

- 分数：36.0  ·  HF 赞：53  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark, retrieval
- 作者：Xiaomin Yu, Hongliang Chen, Zhe Huang, Shilin Yan, Shao-Rong Su, Xuqiao Ma, Feiyang Wang, Jiayu Chen, Jiwei Fang, Yu Yan, Yini Huang, Chen Chen, Ruoxi Cheng, Yuzhi He, Yuhui Zhang, Xiaoxing Hu, Chen Liu, Jianbo Lin, Yijiang Li, Xiaobin Hu, Menglong Li, Zhuoran Lu, Weishi Wang, Zhongqi Yue, Chengwei Qin
- 链接：[arXiv](https://arxiv.org/abs/2610.30181) · [PDF](https://arxiv.org/pdf/2610.30181) · [HF](https://huggingface.co/papers/2610.30181)

Despite substantial progress in Deep Search agents, their ability to conduct end-to-end research in real-world open Web environments remains insufficiently evaluated. Unlike static retrieval settings, information on the real-world Web is distributed across diverse sources, modalities, and heterogeneous formats, often involving complex interaction mechanisms that require agents to autonomously search for, access, and…

## 5. StreamEval: Evaluating Interactive Streaming Video Generation Models

- 分数：34.0  ·  HF 赞：379  ·  来源：huggingface
- 兴趣命中：evaluation, benchmark, spec
- 作者：StreamEval Team
- 链接：[arXiv](https://arxiv.org/abs/2610.28402) · [PDF](https://arxiv.org/pdf/2610.28402) · [HF](https://huggingface.co/papers/2610.28402)

As streaming video generation advances, enabling real-time interaction with generated video is becoming increasingly important. We introduce StreamEval, a unified benchmark for interactive streaming video generation spanning five tasks: avatar dialogue, avatar performance, world generation, instruction editing, and reference editing. StreamEval comprises 300 scripted test cases lasting 15-300s, each specifying…

## 6. Scaling in Games: Continued Pre-Training For Embodied Agents In Diverse Virtual Worlds

- 分数：34.0  ·  HF 赞：53  ·  来源：huggingface
- 兴趣命中：agent, benchmark, spec
- 作者：Kuan Zhang, Yukun Chen, Zhihao Yang, Yue Su, Xiangnan Wu, Zirong Chen, Run Luo, Jinkun Hou, Tao Tan, Yinhe Zheng, Yiming Li
- 链接：[arXiv](https://arxiv.org/abs/2610.28698) · [PDF](https://arxiv.org/pdf/2610.28698) · [HF](https://huggingface.co/papers/2610.28698)

Scaling data, diversity and model capacity has improved embodied learning in physical environments, where diverse experiences remain grounded in shared physical laws. Whether these gains extend to virtual worlds with different visual styles, dynamics, controls, and objectives remains unclear. We investigate this question through a controlled study of continued pre-training (CPT) across three axes: data volume,…

## 7. PrismaCoder: Pushing the Boundaries of Open Multimodal Code Intelligence through Decomposed Rubric Synthesis

- 分数：34.0  ·  HF 赞：50  ·  来源：huggingface
- 兴趣命中：reinforcement learning, coding, spec
- 作者：Qiushi Sun, Jingyang Gong, Yang Liu, Qiaosheng Chen, Zhangyue Yin, Zixian Huang, Hanxu Hu, Jing Xiong, Fangzhi Xu, Haochen Tan, Haoli Bai, Lifeng Shang, Xiaoguang Li, Ben Kao, Qipeng Guo, Lingpeng Kong, Jiahui Gao
- 链接：[arXiv](https://arxiv.org/abs/2610.20538) · [PDF](https://arxiv.org/pdf/2610.20538) · [HF](https://huggingface.co/papers/2610.20538)

Multimodal code intelligence connects the symbolic world of programs with the visual world their execution creates. Interest in this capability is burgeoning, as models are increasingly asked to produce charts, webpages, animations, and semi-structured documents. Recently, proprietary models have pushed far ahead, producing interactive artifacts even from a text description or a screenshot alone. Yet their data and…

## 8. Making MLLM Latents Matter: Factor-Aware Predictive Learning for Cinematic Video Generation

- 分数：34.0  ·  HF 赞：41  ·  来源：huggingface
- 兴趣命中：language model, large language, spec
- 作者：Songlin Yang, Zhe Wang, Xiaotong Zhao, Xi Wang, Ran Zhang, Shuai Li, Taiyi Wu, Songlian Li, Eric Liu, Alan Zhao, Anyi Rao
- 链接：[arXiv](https://arxiv.org/abs/2610.30926) · [PDF](https://arxiv.org/pdf/2610.30926) · [HF](https://huggingface.co/papers/2610.30926)

Cinematic video generation requires both temporal inference from limited inputs (i.e., sparse rather than frame-by-frame guidance) and factor-aware control of character, scene, action, and camera. Multimodal large language models (MLLMs) offer useful priors for both capabilities, but their representations are not automatically actionable for video generation: a Video Diffusion Transformer (DiT) may bypass them…

## 9. Spectral-Spatial Interpretation

- 分数：32.0  ·  HF 赞：123  ·  来源：huggingface
- 兴趣命中：evaluation, spec
- 作者：Haotian Ma, Ruqi Yang, Philip Townsend
- 链接：[arXiv](https://arxiv.org/abs/2610.21114) · [PDF](https://arxiv.org/pdf/2610.21114) · [HF](https://huggingface.co/papers/2610.21114)

Post-hoc image explanations usually show where a model looks using spatial heatmaps or indicate which channels matter using global channel scores. These separate views are limiting for multispectral data because channel relevance is often spatially localized and physically meaningful. We introduce Spectral-Spatial Interpretation (SSI), a full-grid attribution method over position-channel players (g,c). For each…

## 10. Right Screen, Wrong Transition: World Models as Verifiers for GUI Agents

- 分数：32.0  ·  HF 赞：102  ·  来源：huggingface
- 兴趣命中：agent, spec
- 作者：Jiaming Zhang, Xuan Wang, Fuyao Zhang, Yang Cao, Lingjuan Lyu, Wei Yang Bryan Lim
- 链接：[arXiv](https://arxiv.org/abs/2610.11942) · [PDF](https://arxiv.org/pdf/2610.11942) · [HF](https://huggingface.co/papers/2610.11942)

A login screen that appears after a tap on Sign in is expected; the same screen after a tap on View order is an attack. For GUI agents, safety is therefore a property of the transition rather than of the screen, and a monitor that inspects only screens can be defeated by reusing a legitimate one. Judging a transition requires an expectation of what should have followed the action. Existing GUI world models provide…

## 11. Socratic Skill Learning: Interleaving Teaching and Practice for Transferable Agent Skills

- 分数：29.5  ·  HF 赞：31  ·  来源：huggingface
- 兴趣命中：agent, evaluation, spec
- 作者：Letian Zhu, Han Li, Yifan Yao, Xinping Lei, Xinyu Che, Jiahao Wang, Dianyi Wang, Yucheng Fu, Jiakai Wang, Zhiqi Bai, Wenbo Su, Jiaheng Liu
- 链接：[arXiv](https://arxiv.org/abs/2610.17860) · [PDF](https://arxiv.org/pdf/2610.17860) · [HF](https://huggingface.co/papers/2610.17860)

Agent Skills improve LLM agents by making task knowledge reusable across sessions. Learning transferable Skills requires evidence about a procedure and its conditions of use, which a successful task attempt can leave untested. We introduce Socratic Skill Learning (SSL), which interleaves expert teaching with Student practice. An Educator guides investigation while the Student remains the sole environment operator…

## 12. Retrieval Augmented Generation Compositionality

- 分数：29.5  ·  HF 赞：27  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark, language model, large language, retrieval
- 作者：Ido Levy, Segev Shlomov, Leshem Choshen
- 链接：[arXiv](https://arxiv.org/abs/2610.29722) · [PDF](https://arxiv.org/pdf/2610.29722) · [HF](https://huggingface.co/papers/2610.29722)

Retrieval Augmented Generation (RAG) grounds large language models in external knowledge. Modern pipelines combine embedding, chunking, retrieval, reranking, query augmentation, context compression, and agentic verification, yet these techniques are typically evaluated one at a time. It remains unclear whether their isolated gains survive composition, whether retrieval quality and answer faithfulness favor the same…

## 13. Deep Fusion Memory: A Chunk-Level Parametric Memory for Large Language Models

- 分数：28.5  ·  HF 赞：25  ·  来源：huggingface
- 兴趣命中：memory, language model, large language, spec, retrieval
- 作者：Rubin Wei, Siyuan Sun, Hao Sun, Yuliang Liu, Xiang Shi, Jiarui Wang, Junming Zhang, Zhouhan Lin
- 链接：[arXiv](https://arxiv.org/abs/2610.25100) · [PDF](https://arxiv.org/pdf/2610.25100) · [HF](https://huggingface.co/papers/2610.25100)

Large language models need effective ways to acquire and use external knowledge beyond what they retain from pretraining. Continued pretraining risks catastrophic forgetting, while retrieval at inference time can add substantial overhead. External parametric memory avoids online retrieval, but constructing its training data requires extensive offline search, and output-level interpolation provides only shallow…

## 14. Looking Ahead: Modeling Future Evolution in Autoregressive Video Generation

- 分数：28.0  ·  HF 赞：141  ·  来源：huggingface
- 兴趣命中：-
- 作者：Ruopeng Gao, Yukun Huang, Jiarui Hu, Shuai Wang, Wenbo Hu, Ying Shan, Limin Wang
- 链接：[arXiv](https://arxiv.org/abs/2610.29989) · [PDF](https://arxiv.org/pdf/2610.29989) · [HF](https://huggingface.co/papers/2610.29989)

Autoregressive video diffusion models generate videos chunk by chunk, yet producing plausible continuations does not guarantee that they capture how scenes evolve. Under teacher forcing, strong temporal redundancy may allow local visual continuity to serve as a shortcut for current-chunk denoising, reducing the pressure to model visual evolution. We introduce Future Chunk Prediction (FCP), an auxiliary objective…

## 15. DONIC: Generalist Dexterous Bimanual Tracking Control from Human Demonstrations

- 分数：28.0  ·  HF 赞：133  ·  来源：huggingface
- 兴趣命中：-
- 作者：Mingze Sun, Ziang Cao, Yuan Fei, Qiankuan Tao, Zihan Wang, Tianqi Liu, Junhao Chen, Haiwen Diao, Fangzhou Hong, Zhaoxi Chen, Ziwei Liu
- 链接：[arXiv](https://arxiv.org/abs/2610.29997) · [PDF](https://arxiv.org/pdf/2610.29997) · [HF](https://huggingface.co/papers/2610.29997)

Despite recent progress in dexterous reference tracking, existing models focus primarily on single-hand manipulation and a limited range of interactions, leaving the bimanual dexterous behaviors common in real life unaddressed. The scarcity of contact-rich bimanual manipulation data and the increased complexity of coordinating contacts make developing a generalist bimanual tracker particularly challenging.…

## 16. TraceForge: Distilling with Your Own Thinking

- 分数：27.0  ·  HF 赞：22  ·  来源：huggingface
- 兴趣命中：reasoning, benchmark, coding, spec
- 作者：Yan Wang
- 链接：[arXiv](https://arxiv.org/abs/2610.29680) · [PDF](https://arxiv.org/pdf/2610.29680) · [HF](https://huggingface.co/papers/2610.29680)

Using an LLM to generate training data for another is among the most general ways to train one, and it remains common practice. Some frontier teams have closed that route for their own models: what comes back is an answer, or a short summary, without the detailed reasoning trace behind it. That is a little ironic: they were themselves built on distilling human knowledge, and distilling an open-source model is still…

## 17. AgenticRoboRL: Bringing Coding-Agent Post-Training to Agentic Robotics

- 分数：26.5  ·  HF 赞：21  ·  来源：huggingface
- 兴趣命中：agent, memory, reinforcement learning, coding, spec
- 作者：Xinxin Liu, Bingxin Xu, Wenrui Bao, Ming Li, Wentao Bao, Chen Chen, Yuzhang Shang
- 链接：[arXiv](https://arxiv.org/abs/2610.28589) · [PDF](https://arxiv.org/pdf/2610.28589) · [HF](https://huggingface.co/papers/2610.28589)

Agentic robotics systems combine planners with robot harnesses to perform complex manipulation tasks. Recent work improves these systems through better harnesses and external memory, but relies on powerful closed-source models as planners and does not improve the planners' own capabilities. In contrast, coding agents have improved substantially by post-training the model itself. We therefore investigate whether…

## 18. CulturalRiddles: A Multicultural Benchmark of Riddles

- 分数：26.0  ·  HF 赞：20  ·  来源：huggingface
- 兴趣命中：reasoning, evaluation, benchmark, spec
- 作者：My Chiffon Nguyen, Tianyi Hu, Vinod Anbalagan, Henry Gagnier, Pouya Sadeghi, Farah Abdou, Tidor-Vlad Pricope, Diego MMS Oliveira, Jocelyn K D&#39;Arcy, Madeline Smith, Oluwaseun A Ajayi, Yusser Al Ghussin, Zena Al-Khalili, Micol Altomare, Shayan Amir, Ahanaf Aziz, Bryan Chen, Ruchira Dhar, Abdellah El Mekki, Rawan Mohammed Elframawy, Akhil Eppa, Silvia Fernandez, Alex Gimei, Arya Hariharan, Christian Hoang, RamMohanRao Kadiyala, Diana Kozachek, Peerat Limkonchotiwat, Ankita Maity, Di Mo, Ayush Munot, Aylin Naebzadeh, Anastasiia Nikitina, Dina Pisarevskaya, Divas Poudel, Jebish Purbey, Md Rabius Sany Apu, Ahmad Mufli Ramadhan, Ralitza Nikolova Rizova, Diogo M. Serrano-Miranda, Vivek Gopalkrishna Silimkhan, Luis Fernando Solis Navarro, Kaiser Sun, Arya Suneesh, Manaswitha Sunkara, Tejaswi Sunkara, Jonathan E Swindell, Hanna Yukhymenko, Jingyi Zheng, Esther Adenuga, Ilia Afanasev, Wafa Aissa, Lisa Alazraki, Lauren C Altomare, Priscilla Amondi Amuok, Emile Anand, Gabriel Assis, José Matías Avalos, Silvia Lorena Avila, Zakaria Baannou, Niyati Bafna, Yash Bagla, Sarah Bahrami, Bontu F Balcha, Vanya Bannihatti Kumar, Irene Baucells, Abdumutalib Begmuratov, Naman Bhatia, Souvik Bhattacharyya, Isabel Blanco Ferreiro, Felipe Bochini, Sayuru Bopitiya, Angana Borah, Tulika Bose, Olena Bugaiova, Juliana Carvalho, Nancy F Chen, Stephy Chen, Rochelle Choenni, Jayanth Krishna Chundru, Leandro A Cossio, Nebojša Damnjanović, Ona de Gibert, Marco De Santis, Pedro Delgado, Kaustubh Dholé, Adnan El Assadi, Wesam El-Sayed, Nadine M Elframawy, Oumayma Essarhi, Naome A Etori, Reuben Chagas Fernandes, Saanidhi Pravin Gade, Javier García Gilabert, Álvaro González-Escapa, Bin Hu, Kaiyu Huang, Abderrahmane Issam, Danka Jokić, Ulugbek Khalilov, Dominik Krzemiński, Roy Ka-Wei Lee, Haichang Li, Chen Cecilia Liu, Zhengyuan Liu, Cedric Lothritz, Houman Mehrafarin, Antonio Miranda-Escalada, Fengran Mo, Mehrnaz Mofakhami, Wafaa Mohammed, Felipe Moreno-Vera, Prahitha Movva, Jannatul Nayem, Van Ngo, Joy Olusanya, Marc Pàmies, Avinash Kuney Pandey, Yurii Paniv, Fred Philippy, Vladislav Poritski, Dikshya Poudel, Joanna Radoła, Sara Rajaee, Swati Rajwal, Prerana Rane, Muhammad Ravi Shulthan Habibi, Lucas Resck, Shubhashis Roy Dipta, Ananya Sahu, Eduardo Sánchez, Borja Sánchez Clemente, Aleix Sant, Nobin Sarwar, Istiak Shihab, Santhoshini Pranathi Singaraju, Jane Smith, David Stap, Emily Z Su, Ananth K Suresh, Sajag Swami, Ruiyang Tan, Nazia Tasnim, Khalid Tounoussi, Patteera Triamamornwooth, Muhammad Saad Umar, Shankar Venkitachalam, Oksana Volchek, Lingbo Wang, Debela Desalegn Yadeta, Rushikesh Zawar, Jinghan Zhang, Mike Zhang, Weihua Zheng, Marzieh Fadaee, Akhil Arora, Károly Boczka, Julia Kreutzer
- 链接：[arXiv](https://arxiv.org/abs/2610.29968) · [PDF](https://arxiv.org/pdf/2610.29968) · [HF](https://huggingface.co/papers/2610.29968)

As LLMs expand their language coverage, evaluating how well they understand and represent diverse cultures becomes increasingly important. However, many benchmarks remain English-centric, with limited cultural coverage and a focus on factual knowledge over its application in real-world cultural contexts. We propose CulturalRiddles, a benchmark of original, culturally grounded riddles created entirely by humans…

## 19. Memory-Centric Continual Learning for AI Agents

- 分数：26.0  ·  HF 赞：20  ·  来源：huggingface
- 兴趣命中：agent, memory, evaluation, retrieval
- 作者：Dongfang Li, Zhuoen Chen, Bonian Jia, Zixuan Liu, Zhengxuan Lu, Can Deng, Yukun Shi, Yuhang Meng, Xin Zhang, Jiahe Huang, Fuhao Li, Junmai Wang, Shunyao Wen, Jingjun Sun, Jiaxu Tian, Jiangling Zhang, Zihan Wang, Liangyou Li, Yitong Yao, Shuangyong Song, Beilun Wang, Pengxu Wei, Hanlin Xu, Chang Liu, Yongxiang Li, Baotian Hu, Xiangyang Ji, Min Zhang
- 链接：[arXiv](https://arxiv.org/abs/2610.29357) · [PDF](https://arxiv.org/pdf/2610.29357) · [HF](https://huggingface.co/papers/2610.29357)

Autonomous agents powered by foundation models can reason, plan, and use tools, but their fixed weights and context limits hinder sustained learning from experience over long-term deployment. While external memory systems attempt to bridge this gap, they mostly act as passive retrieval caches, evaluated primarily by whether they can recall stored facts or past interactions. Whether memory can drive genuine continual…

## 20. Multimodal Embodied Agents: A Unified Capability-centric Perspective from Computer-Use to Robot-Use

- 分数：25.5  ·  HF 赞：19  ·  来源：huggingface
- 兴趣命中：agent, memory, reasoning, evaluation, benchmark, spec
- 作者：Yanzhe Chen, Ziyi Yang, Jifeng Zhu, Qiming Huang, Ruihe An, Peiyao Xu, Hesen Yang, Runda Liu, Chang Gong, Zhijun Cao, Zechen Bai, Wenzheng Zeng, Yiqi Lin, Guoqiang Liang, Kevin Yuchen Ma, Kevin Qinghong Lin, Mike Zheng Shou
- 链接：[arXiv](https://arxiv.org/abs/2610.30108) · [PDF](https://arxiv.org/pdf/2610.30108) · [HF](https://huggingface.co/papers/2610.30108)

Multimodal agents (MMAs) sustain interaction through reasoning, memory, tools, and feedback, most visibly as computer-use agents, while robotic systems (RSs) couple sensing and actuation under physical dynamics. We define multimodal embodied agents (MMEAs) as goal-directed systems that couple multimodal task reasoning with physical action and revise decisions from the resulting feedback. This raises a central…

## 21. Building AI Research Teams for Autonomous Discovery of Linear Attention Architectures

- 分数：24.0  ·  HF 赞：16  ·  来源：huggingface
- 兴趣命中：agent, reasoning, language model, retrieval
- 作者：Yujian Liu, Li An, Zelin He, Jacob Helwig, Jiabao Ji, Rohit Jain, Siyu Zhu, Shiyu Chang
- 链接：[arXiv](https://arxiv.org/abs/2610.28887) · [PDF](https://arxiv.org/pdf/2610.28887) · [HF](https://huggingface.co/papers/2610.28887)

Autonomous agents can increasingly propose ideas, modify code, and run experiments, creating an opportunity to accelerate scientific discovery using teams of collaborative AI researchers. To escape local minima in the discovery, we propose to encourage orthogonal exploration by constructing the team using agents with varying expertise. However, realizing this design requires more than diverse backgrounds. When…

## 22. Harness Scaling for Generalizable Agentic Reinforcement Learning

- 分数：24.0  ·  HF 赞：16  ·  来源：huggingface
- 兴趣命中：agent, reinforcement learning, benchmark, spec
- 作者：Fei Bai, Huatong Song, Chuan Hao, Ran Tao, Jian Yang, Bryan Dai, Wayne Xin Zhao, Ji-Rong Wen
- 链接：[arXiv](https://arxiv.org/abs/2610.29458) · [PDF](https://arxiv.org/pdf/2610.29458) · [HF](https://huggingface.co/papers/2610.29458)

Agent harnesses have become a central component of modern agentic systems, shaping how models use tools, manage context, and coordinate long-horizon interaction. Realizing the benefits of these harnesses depends on how effectively the underlying model can make use of them, motivating reinforcement learning directly through the harness. However, existing approaches typically train through a single fixed harness,…

## 23. PACE: Periodic and Channel-Aligned Encoding of Four-Bit Recurrent States

- 分数：23.5  ·  HF 赞：19  ·  来源：huggingface
- 兴趣命中：memory, language model, coding
- 作者：Patrick Haller, Filipe Laitenberger, Alan Akbik
- 链接：[arXiv](https://arxiv.org/abs/2610.29545) · [PDF](https://arxiv.org/pdf/2610.29545) · [HF](https://huggingface.co/papers/2610.29545)

Linear-attention language models keep their context in a recurrent state of fixed size, where an inference system stores one copy of this state for every sequence it decodes at the same time. Storing the state at lower precision therefore lets more sequences share an accelerator. Existing state quantizers round the state after every generated token and report that four bits lose accuracy unless the bit width is…

## 24. ALPS: Visual State Encoders for World Models

- 分数：23.5  ·  HF 赞：19  ·  来源：huggingface
- 兴趣命中：evaluation, spec, planning
- 作者：Yanqing Liu, Letian Zhang, Chengzhi Liu, Zijun Wang, Jieru Mei, Hongliang Fei, Yuyin Zhou, Cihang Xie
- 链接：[arXiv](https://arxiv.org/abs/2610.30120) · [PDF](https://arxiv.org/pdf/2610.30120) · [HF](https://huggingface.co/papers/2610.30120)

World models turn visual representations into predictions and actions. We argue that their visual foundation should combine physical-state information, native language alignment, and pixel reconstruction, so that a single representation can support prediction, instruction, and inspection. However, existing encoders typically specialize in only one or two of these capabilities; we therefore introduce ALPS, a…

## 25. Agentic World Action Models

- 分数：22.5  ·  HF 赞：13  ·  来源：huggingface
- 兴趣命中：agent, reasoning, evaluation, planning
- 作者：Zhuoyang Liu, Dantong Niu, Botong Zhang, Boning Shao, Jing Wang, Ruijie Zheng, Yuvan Sharma, Runyu Lu, Jiaming Liu, Renrui Zhang, Roei Herzig, Yutong Bai, Ken Goldberg, Danfei Xu, Yuke Zhu, Guanzhi Wang, Linxi &#34;Jim&#34; Fan, Trevor Darrell
- 链接：[arXiv](https://arxiv.org/abs/2610.30136) · [PDF](https://arxiv.org/pdf/2610.30136) · [HF](https://huggingface.co/papers/2610.30136)

Recent world action models provide visual foresight and future prediction for robot manipulation, but lack explicit mechanisms for compositional skill reuse. Agentic robotics combines code-based planning and reasoning with reusable skills, but often lacks predictive grounding in physical dynamics. We introduce AW-0, an agentic world action model framework that integrates code-based planning with joint video and…

## 26. DeLoop: Repeated Actions as Self-Supervision for Long-Horizon Agents

- 分数：21.0  ·  HF 赞：18  ·  来源：huggingface
- 兴趣命中：agent, context window
- 作者：Tianle Chen, Pushkar Singh, Ketan Todi, Biswajit Paria, Qijia He, Wenqi Wang, Yuwen Tan, Jike Zhong, Sugato Basu, Deepti Ghadiyaram, Arjun Akula
- 链接：[arXiv](https://arxiv.org/abs/2610.19376) · [PDF](https://arxiv.org/pdf/2610.19376) · [HF](https://huggingface.co/papers/2610.19376)

Language-model agents that run long tasks often redo work they have already done: they re-issue a tool call they made earlier and get back exactly the same observation, a step that adds no new information. We identify this failure as a loop. Loops appear natively in Qwen, Llama, and Gemini agents and become far more common once the agent's history is compressed to fit its context window. To reduce these loops, we…

## 27. Automating ML for Science: Can Frontier Agents Climb Scientific Hills in the Wild?

- 分数：20.5  ·  HF 赞：13  ·  来源：huggingface
- 兴趣命中：agent, benchmark, coding
- 作者：Ming Zhong, Stacy Li, Nicholas Carlini, Matthew Jagielski
- 链接：[arXiv](https://arxiv.org/abs/2610.28763) · [PDF](https://arxiv.org/pdf/2610.28763) · [HF](https://huggingface.co/papers/2610.28763)

Frontier coding agents are increasingly framed as end-to-end automated researchers, and ML for science offers a demanding test of that promise: improving a scientific model often requires domain insight beyond routine ML engineering. We introduce Agent4Sci, a long-horizon testbed for measuring how far today's agents can improve the published best models on scientific ML benchmarks, spanning 20 benchmarks across 11…

## 28. Qwen-Audio-3.1-ASR Technical Report

- 分数：20.0  ·  HF 赞：12  ·  来源：huggingface
- 兴趣命中：reasoning, evaluation, language model
- 作者：Chuanmeng Bian, Daren Chen, Peixin Chen, Zhigao Chen, Chong Deng, Zhiyun Fan, Zhifu Gao, Bo Gong, Qing Gu, Jiajun He, Yawei Hu, Yunjie Ji, Wei Ju, Jingbei Li, Xiangang Li, Xu Li, Zengxi Li, Zheng Li, Chengdong Liang, Baiji Liu, Yaming Liu, Ying Liu, Bin Ma, Yiping Peng, Yuezhang Peng, Zhendong Peng, Yu Pu, Yang Shi, Xin Shu, Jian Tang, Biao Tian, Peiyao Wang, Tianzi Wang, Wen Wang, Wupeng Wang, Cheng Wen, Yuzhong Wu, Zijian Xia, Yunchong Xiao, Nan Yang, Jianwei Yu, Jixing Yu, Binbin Zhang, Lei Zhang, Sitong Zhao, Guangdong Zhou, Yuan Zhou, Jianheng Zhuo
- 链接：[arXiv](https://arxiv.org/abs/2610.28711) · [PDF](https://arxiv.org/pdf/2610.28711) · [HF](https://huggingface.co/papers/2610.28711)

We present Qwen-Audio-3.1-ASR, a family of audio-language models that builds upon its predecesor Qwen-Audio-3.0-ASR with improved speech recognition and expanded capabilities in speaker-diarized transcription and general audio understanding. The family retains support for 30 languages and 16 Chinese dialects, together with instruction-controlled capabilities including historical-context conditioning, hierarchical…

## 29. SpatialBrain: Spatial Intelligence Growing from Experience

- 分数：20.0  ·  HF 赞：12  ·  来源：huggingface
- 兴趣命中：memory, reasoning, benchmark
- 作者：Yifan Zhou, Ziyang Gong, Xiaojun Ye, Yifei Liu, Donggang Li, Xiaolong Zhou, Zhihang Zhong, Xue Yang
- 链接：[arXiv](https://arxiv.org/abs/2610.29317) · [PDF](https://arxiv.org/pdf/2610.29317) · [HF](https://huggingface.co/papers/2610.29317)

Spatial reasoning requires more than access to geometric tools: a reasoner must decide when direct observation is sufficient and when to reconstruct, measure, or change reference frames. We present SpatialBrain, a framework that retains experience about these decisions while keeping its vision-language backbone fixed. The key distinction is between evidence about a scene and experience about how to reason with that…

## 30. Code2Video-Compass: A Comprehensive Benchmark for General-Purpose Code-Based Video Generation across T2V, I2V, and V2V

- 分数：20.0  ·  HF 赞：8  ·  来源：huggingface
- 兴趣命中：evaluation, benchmark, language model, large language, spec
- 作者：Zhenghan Chen, Zekai Shao, Xin Lin, Leting Cheng, Siming Chen
- 链接：[arXiv](https://arxiv.org/abs/2610.28416) · [PDF](https://arxiv.org/pdf/2610.28416) · [HF](https://huggingface.co/papers/2610.28416)

Code-based video generation offers fine-grained control, targeted editing, and component reuse compared with direct video generation. This approach requires multimodal large language models (MLLMs) to translate visual and temporal requirements into executable programs that produce complete videos. However, existing code-based benchmarks primarily target specialized tasks, leaving complete video creation across…

## 31. Meta Expert: Cross-Layer Expert Sharing for Storage- and Retrieval-Efficient MoE

- 分数：19.5  ·  HF 赞：19  ·  来源：huggingface
- 兴趣命中：retrieval
- 作者：Ermo Hua, Xiangyu Hong, Baiting Wu, Che Jiang, Haozheng Hou, Yicheng Gu, Hanjing Wang, Qirui Zeng, Ming Zhang, Ning Ding, Qipeng Guo, Youbang Sun, Biqing Qi, Bowen Zhou
- 链接：[arXiv](https://arxiv.org/abs/2610.27598) · [PDF](https://arxiv.org/pdf/2610.27598) · [HF](https://huggingface.co/papers/2610.27598)

As model parameters scale up, sparsely activated Mixture-of-Experts (MoE) approaches have become essential for model scaling. However, mainstream models currently adopt hierarchical architectures, where experts in different layers, although topologically independent, exhibit substantial similarity and redundancy in their stored content. Compared to the hierarchically arranged Local Expert in existing mainstream…

## 32. Evolving with Open Worlds: Towards Recursive Self-Improvement for Future Forecasting

- 分数：19.5  ·  HF 赞：11  ·  来源：huggingface
- 兴趣命中：agent, reasoning, evaluation
- 作者：Zhipeng Chen, Yunsen Liang, Yanxi Chen, Hongkang Zhao, Lingyun Feng, Ruiyang Ren, Guoxin Chen, Jia Deng, Feng Chang, Chuan Hao, Ran Tao, Jian Yang, Ji-Rong Wen, Bryan Dai, Wayne Xin Zhao
- 链接：[arXiv](https://arxiv.org/abs/2610.29784) · [PDF](https://arxiv.org/pdf/2610.29784) · [HF](https://huggingface.co/papers/2610.29784)

Most contemporary artificial intelligence (AI) systems are released with frozen parameters and improve through external updates, whereas an ideal system would keep improving from its own experience, a capacity we call recursive self-improvement (RSI). Yet studying RSI requires an environment that is continuously changing, objectively verifiable, and naturally grounded, posing a fundamental challenge for agent…

## 33. RubatoCodec: Budgeted Adaptive Speech Tokenization with Streaming Decoding

- 分数：19.5  ·  HF 赞：11  ·  来源：huggingface
- 兴趣命中：benchmark, coding, spec
- 作者：Chihiro Arata, Shohei Taniguchi, Gouki Minegishi, Kan Hatakeyama-Sato
- 链接：[arXiv](https://arxiv.org/abs/2610.29434) · [PDF](https://arxiv.org/pdf/2610.29434) · [HF](https://huggingface.co/papers/2610.29434)

Neural speech codecs provide discrete tokens for speech generation. Lower frame rates shorten token sequences, but each token must then carry more linguistic and acoustic information. Variable-frame-rate codecs address this trade-off by adapting token allocation to speech content, but threshold-based allocation lets content determine the token count, so the sequence length a speech generator must produce varies…

## 34. ToM2Vec: Continuous Theory-of-Mind Tokens for Multi-Agent Coordination

- 分数：19.5  ·  HF 赞：7  ·  来源：huggingface
- 兴趣命中：agent, reasoning, language model, large language, spec
- 作者：Nithin Sivakumaran, Ali Payani, Hyunji Lee, Mohit Bansal, Elias Stengel-Eskin
- 链接：[arXiv](https://arxiv.org/abs/2610.29934) · [PDF](https://arxiv.org/pdf/2610.29934) · [HF](https://huggingface.co/papers/2610.29934)

Forming an accurate theory-of-mind (ToM) is key to successful multi-agent collaboration and requires reasoning under uncertainty to capture multiple possible partner states. This is hard to do in the text representation space native to large language model (LLM) agents, which more easily describe a single partner state. To address this challenge, we introduce ToM2Vec, which learns to form abstract theories-of-mind…

## 35. Is Complex Agentic Memory Always Needed? Naive RAG Is Stronger Than We Thought

- 分数：19.5  ·  HF 赞：7  ·  来源：huggingface
- 兴趣命中：agent, memory, benchmark, retrieval
- 作者：Zhengye Bao, Shengtao Zhang, Haokai Zhang, Shiqi Lou, Muning Wen, Minnan Luo
- 链接：[arXiv](https://arxiv.org/abs/2610.30755) · [PDF](https://arxiv.org/pdf/2610.30755) · [HF](https://huggingface.co/papers/2610.30755)

LLM memory is widely used in long-term conversation understanding. Agentic memory systems often use mutation, structural organization, learned retrieval strategies, or other complex operations. Is this complexity always necessary? We study Raw-RAG, a naive RAG baseline using dense retrieval and reranking over raw history to supply evidence to a reader LLM. Across LoCoMo, LongMemEval, MEME, and MemoryAgentBench,…

## 36. From VLM Planners to Robotic Agents: Self-Evolving Harnesses for History-Dependent Manipulation

- 分数：19.0  ·  HF 赞：10  ·  来源：huggingface
- 兴趣命中：agent, memory, planning
- 作者：Tingwen Du, Haoyu Guo, Hanxue Zhang, Xuanxu Wang, Junting Dong, Chao Gao, Mingfei Han, Tao Lu, Mulin Yu, Chunhua Shen, Xiaojun Chang, Zhihui Li
- 链接：[arXiv](https://arxiv.org/abs/2610.29560) · [PDF](https://arxiv.org/pdf/2610.29560) · [HF](https://huggingface.co/papers/2610.29560)

Vision-language-action (VLA) models achieve strong performance across embodied manipulation tasks by unifying visual understanding, language conditioning, and action generation. However, long-horizon tasks can involve non-Markovian dependencies: successful decisions may require retaining task progress and past interaction outcomes, while partial observability and execution errors compound over time. Existing work…

## 37. DiffResearch: Accelerating Deep Research with Diffusion Language Models

- 分数：19.0  ·  HF 赞：6  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark, language model, coding, planning, retrieval
- 作者：Alan-Barsag Gazzaev, Alexey Gavrilov, Mikhail Mozikov, Sergey Muravyov
- 链接：[arXiv](https://arxiv.org/abs/2610.28909) · [PDF](https://arxiv.org/pdf/2610.28909) · [HF](https://huggingface.co/papers/2610.28909)

Deep research systems iteratively plan, gather evidence, synthesize, and revise, making end-to-end latency a key bottleneck for interactive use. Almost all production systems are built on autoregressive (AR) language models and inherit left-to-right decoding in planning and long-form writing. We present DiffResearch, an open multi-agent deep research framework that places a diffusion language model (dLLM) at the…

## 38. Beyond Watching and Searching: Benchmarking Agents for Video-centered Deep Research Reports

- 分数：19.0  ·  HF 赞：6  ·  来源：huggingface
- 兴趣命中：agent, evaluation, benchmark, spec
- 作者：Jiahao Meng, Qize Yang, Yuxuan Wang, Yunfei Chu, Wensi Dai, Jin Xu, Yunhai Tong
- 链接：[arXiv](https://arxiv.org/abs/2610.31158) · [PDF](https://arxiv.org/pdf/2610.31158) · [HF](https://huggingface.co/papers/2610.31158)

Deep research agents synthesize open-web evidence into long reports, but current benchmarks do not evaluate research centered on a source video. We introduce Video-Centered Deep Research Report Generation. Given a video and user request, an agent identifies research questions, retrieves external multimodal evidence, and produces an interactive report linked to relevant video moments. This task has direct practical…

## 39. Real In, Real Out: What If We Only Use Real Data for Scene Text Editing?

- 分数：18.5  ·  HF 赞：17  ·  来源：huggingface
- 兴趣命中：benchmark
- 作者：Xingsong Ye, Yongkun Du, Jiaxin Zhang, Chong Sun, Zhineng Chen
- 链接：[arXiv](https://arxiv.org/abs/2610.27592) · [PDF](https://arxiv.org/pdf/2610.27592) · [HF](https://huggingface.co/papers/2610.27592)

Aiming to modify textual content while preserving the original style, Scene Text Editing (STE) has significant practical value in many applications. STE typically requires paired images before and after editing for training. However, recent approaches rely heavily on synthetic paired data and complex disentanglement strategies. They struggle to faithfully capture the diversity and complexity of natural scenes, often…

## 40. Language Models Learn to Improve Language Models

- 分数：18.5  ·  HF 赞：5  ·  来源：huggingface
- 兴趣命中：reinforcement learning, evaluation, language model, large language
- 作者：Minhua Lin, Zijun Wang, Zewen Liu, Zhaotian Weng, Bing He, Zhan Shi, Benoit Dumoulin, Xiang Zhang, Suhang Wang, Hanqing Lu
- 链接：[arXiv](https://arxiv.org/abs/2610.23344) · [PDF](https://arxiv.org/pdf/2610.23344) · [HF](https://huggingface.co/papers/2610.23344)

Large language models (LLMs) are increasingly used to automate AI research, including language-model (LM) development, offering a potential path toward recursive self-improvement. However, turning experimental feedback into a learned ability to propose effective improvements across models faces two challenges. First, training such an ability with real feedback is expensive: reinforcement learning (RL) requires…

## 41. AgentVQA: A Unified Benchmark for Agentic Visual Understanding

- 分数：18.5  ·  HF 赞：5  ·  来源：huggingface
- 兴趣命中：agent, reasoning, evaluation, benchmark, language model, planning
- 作者：Advait Gupta, Sachin Konan, Tom Yin, Gabriel Sarch, Zhuang Liu
- 链接：[arXiv](https://arxiv.org/abs/2610.31494) · [PDF](https://arxiv.org/pdf/2610.31494) · [HF](https://huggingface.co/papers/2610.31494)

Vision-language models (VLMs) can perform a broad range of tasks across diverse settings, yet their performance in agentic contexts remains poorly understood. Although online evaluations in simulators and real-world environments are essential for measuring interactive agent performance, they are costly and challenging to scale. Complementary offline VQA benchmarks can enable faster and more reliable comparisons…

## 42. CompactSplat: Spatially Adaptive Gaussian Distribution for Feedforward Scene Reconstruction

- 分数：18.0  ·  HF 赞：12  ·  来源：huggingface
- 兴趣命中：memory, spec
- 作者：Bing He, Jingnan Gao, Yunuo Chen, Zhengxue Cheng, Rong Xie, Li Song, Wenjun Zhang
- 链接：[arXiv](https://arxiv.org/abs/2610.13177) · [PDF](https://arxiv.org/pdf/2610.13177) · [HF](https://huggingface.co/papers/2610.13177)

Reconstructing 3D scenes from sparse views without per-scene optimization remains highly challenging, especially for recovering accurate geometry and fine textures. While recent feedforward approaches leverage generalizable 3D Gaussian Splatting (3DGS) for scene generation, they typically assign one or multiple Gaussians to each pixel. Such uniform allocation not only produces highly redundant representations by…

## 43. Entertain, then Cancel: How Thinking Makes Reasoning Models Read Some and Or Literally

- 分数：18.0  ·  HF 赞：12  ·  来源：huggingface
- 兴趣命中：reasoning, evaluation
- 作者：Zhizhuo Kou, Jian Yang, Pengfei Hao, Junyu Luo, Jingshu Peng, Sirui Han, Yike Guo
- 链接：[arXiv](https://arxiv.org/abs/2610.21204) · [PDF](https://arxiv.org/pdf/2610.21204) · [HF](https://huggingface.co/papers/2610.21204)

When a speaker says ``some students passed'', listeners infer that not all of them did. Reasoning models now let users decide how long a model thinks before it answers, but we do not know what extra thinking does to such everyday inferences. We study this directly: we keep a model's weights fixed, change only how much it thinks, and record which reading it chooses. A second tool cuts the model's own reasoning at…

## 44. RealMe: Immersive Volumetric Video from Minimal Captures

- 分数：18.0  ·  HF 赞：12  ·  来源：huggingface
- 兴趣命中：benchmark, spec
- 作者：Chenxu Zhou, Zhiyuan Yu, Yudong Jin, Yinji Shentu, Yu Zhang, Jiaming Sun, Xiaowei Zhou
- 链接：[arXiv](https://arxiv.org/abs/2610.30023) · [PDF](https://arxiv.org/pdf/2610.30023) · [HF](https://huggingface.co/papers/2610.30023)

This paper addresses the problem of creating immersive volumetric videos from sparse and low-resolution capture resources. Conventional dense multi-view reconstruction methods can produce high-quality volumetric videos, but their reliance on costly capture setups makes them impractical in real-world scenarios. Recent approaches use generative models to relax capture requirements, but still suffer from limited…

## 45. VerifierBench: Benchmarking the Generation of Executable Verifiers for LLM Agents

- 分数：18.0  ·  HF 赞：8  ·  来源：huggingface
- 兴趣命中：agent, tool use, benchmark
- 作者：Jianing Yin, Ziyi Chen, Hao Wang, Yiyou Sun, Zijian Jin, Dawn Song, Daoan Zhang
- 链接：[arXiv](https://arxiv.org/abs/2610.28679) · [PDF](https://arxiv.org/pdf/2610.28679) · [HF](https://huggingface.co/papers/2610.28679)

Agents need reliable ways to validate their outputs, both when completing tasks and when filtering synthetic training data. We study verifier generation: from the instruction and environment available for solving a task, an agent writes an executable verifier that must accept every valid solution and reject invalid ones. We introduce VerifierBench, a benchmark of 222 tasks from six agent benchmarks spanning…

## 46. Quant-Arena: Benchmarking LLM Agents for Quantitative Trading Research

- 分数：18.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：agent, benchmark, language model, large language
- 作者：Houde Qian, Zheng Jiang, Wenyi Li, Chenxi Xu, Xinjie Lin, Yuzhao Peng, Ruoyu Han, Youjie Zheng, Kaisen Yang, Qinhuai Na, You Fu, Calvin Xiao
- 链接：[arXiv](https://arxiv.org/abs/2610.30113) · [PDF](https://arxiv.org/pdf/2610.30113) · [HF](https://huggingface.co/papers/2610.30113)

Quantitative research is an iterative loop: a researcher proposes a market hypothesis, implements it as an executable signal, tests it on historical data, and decides what to keep. Existing benchmarks score formulas, code, or individual trading decisions, leaving open whether large language models (LLMs) can complete this loop and produce strategies that work beyond the research period. We introduce Quant-Arena, a…

## 47. Think Harder Where It Matters: Item-Level Adaptive Recursion for Sequential Recommendation

- 分数：17.5  ·  HF 赞：11  ·  来源：huggingface
- 兴趣命中：reasoning, benchmark
- 作者：Zhanshuo Cao, Jiakai Tang, Yuqi Zhou, Sunhao Dai, Jun Xu
- 链接：[arXiv](https://arxiv.org/abs/2610.30128) · [PDF](https://arxiv.org/pdf/2610.30128) · [HF](https://huggingface.co/papers/2610.30128)

Existing sequential recommenders usually allocate a fixed computational budget to every item in a user's interaction history, regardless of the item's contribution to the final prediction. We challenge this de facto design with two diagnostic findings. (1) Non-uniform computational need: items within the same sequence vary drastically in how much computation they require. Most converge after shallow processing while…

## 48. Hidden Messages Between Diffusion Language Model Agents: Causal Evidence for Latent Communication

- 分数：17.5  ·  HF 赞：7  ·  来源：huggingface
- 兴趣命中：agent, language model, coding
- 作者：Alan-Barsag Gazzaev, Alexey Gavrilov, Sergey Muravyov, Ilya Makarov
- 链接：[arXiv](https://arxiv.org/abs/2610.28905) · [PDF](https://arxiv.org/pdf/2610.28905) · [HF](https://huggingface.co/papers/2610.28905)

Diffusion language models form answers through a sequence of revisable continuous states, but multi-agent systems usually discard those states and make agents communicate only after decoding text. We ask whether one independent diffusion trajectory can pass a compact hidden message into another and, crucially, whether the receiver uses what that message means. In Hidden Messages, a sender compresses its denoising…

## 49. Verus-Insight: Towards Explainable Artifact Detection in AI-Generated Videos

- 分数：17.5  ·  HF 赞：7  ·  来源：huggingface
- 兴趣命中：benchmark, spec, planning
- 作者：Zhuoran Zhang, Yang Shi, Qixun Wang, Tengfei Liu, Yuqi Tang, Xuanyu Zhu, Yizhuo Jia, Jingyun Hua, Shixuan Liu, Xianghua Ying, Haotian Wang, Yuanxing Zhang, Pengfei Wan, Wenjing Yang
- 链接：[arXiv](https://arxiv.org/abs/2610.30866) · [PDF](https://arxiv.org/pdf/2610.30866) · [HF](https://huggingface.co/papers/2610.30866)

Recent advances in video generation have made synthetic videos increasingly realistic, placing greater demands on reliable AI-generated video detection. Existing artifact-based detectors typically identify generation artifacts as evidence for source prediction, yet they may either fail to recognize subtle artifacts or reach the correct source decision without faithfully identifying the evidence underlying it. In…

## 50. Which Agent's Skill Should Change? Group-Relative Credit Assignment for Evolving Multi-Agent Teams

- 分数：17.0  ·  HF 赞：10  ·  来源：huggingface
- 兴趣命中：agent, retrieval
- 作者：Yanan Ma, Yang Wang, David Le, Chenhan Yuan, Yizheng Sun, Guangwei Zhang, Chenghao Xiao, Chenghua Lin, Imon Banerjee
- 链接：[arXiv](https://arxiv.org/abs/2610.27227) · [PDF](https://arxiv.org/pdf/2610.27227) · [HF](https://huggingface.co/papers/2610.27227)

Cooperative language-model agents can improve without weight updates by revising reusable skills, but only if a shared team reward is traced to the responsible agent and skill. Existing methods credit the skills present in each trajectory, yet presence is not responsibility: a harmful skill active in successful runs still earns positive credit. We present GRSE, Group-Relative Skill Evolution, which assigns…

## 51. From RL Papers to Framework Code: Inclusion and Review in Seven Open-Source Training Frameworks

- 分数：17.0  ·  HF 赞：10  ·  来源：huggingface
- 兴趣命中：reinforcement learning, language model
- 作者：Taiheng Pan
- 链接：[arXiv](https://arxiv.org/abs/2610.28027) · [PDF](https://arxiv.org/pdf/2610.28027) · [HF](https://huggingface.co/papers/2610.28027)

Practitioners use reinforcement learning methods for language models through training frameworks, so a method that a framework includes is one configuration change away for its users. We measure how often this happens. We trace seven open-source frameworks for RL post-training through their commit histories and link them to 6,939 screened arXiv papers from January 2025 to June 2026. Of 1,598 papers that propose a…

## 52. Stratified Sparse Attention: Reducing the Sparse-to-Dense Gap at Extreme Sparsity

- 分数：17.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：long context, language model, large language, spec, retrieval
- 作者：Sahil Joshi, Prithvi Dixit, Aryan Katiyar, Agniva Chowdhury, Joseph E. Gonzalez, Anshumali Shrivastava, Aditya Desai, Kumar Krishna Agrawal
- 链接：[arXiv](https://arxiv.org/abs/2610.28441) · [PDF](https://arxiv.org/pdf/2610.28441) · [HF](https://huggingface.co/papers/2610.28441)

Large Language Model inference over long contexts is increasingly bottlenecked by the cost of attending to a growing Key-Value (KV) cache. Sparse attention reduces this cost by accessing only a fraction of the cache, but existing methods face a trade-off between deterministic retrieval, which captures high-scoring tokens but discards residual attention mass, and sampling, which improves coverage at the cost of…

## 53. SCOPE: Compiling Natural-Language Policies into Neurosymbolic Predicate Programs

- 分数：17.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：agent, reasoning, benchmark, spec
- 作者：Arnon Mazza, Elad Levi
- 链接：[arXiv](https://arxiv.org/abs/2610.31062) · [PDF](https://arxiv.org/pdf/2610.31062) · [HF](https://huggingface.co/papers/2610.31062)

Policy enforcement for LLM agents has shifted from single-turn content moderation to compound, application-specific policies evaluated over multi-turn transcripts and tool-call trajectories. Fine-tuned guardrail models are efficient but degrade on compound policies, and while LLM-as-a-judge approaches achieve higher accuracy, they incur high inference cost and tend to produce unstable predictions. Neurosymbolic…

## 54. ACE-Brain-0.6: Scaling Spatial Grounding for Physical Foundation Models

- 分数：16.5  ·  HF 赞：9  ·  来源：huggingface
- 兴趣命中：reasoning, benchmark
- 作者：Yinhe Wang, Tao Tao, Zexin He, Shuang Luo, Wei Mao, Yao Mu, Feng Pan, Hanming Deng, Lewei Lu, Zhi Hou, Xingang Pan, Dahua Lin, Dacheng Tao, Xiaogang Wang
- 链接：[arXiv](https://arxiv.org/abs/2610.27040) · [PDF](https://arxiv.org/pdf/2610.27040) · [HF](https://huggingface.co/papers/2610.27040)

General-purpose multimodal models, including GPT-6 Astra and Claude Opus 5.5, demonstrate broad capabilities in embodied manipulation. Our analysis indicates that this generality is accompanied by strong spatial perception, as Astra can determine where to interact with task-relevant entities amid visual distractors. Because spatial perception connects high-level reasoning to the physical scene, we investigate…

## 55. WorldStream: Streaming Interactive 3D Worlds with Hierarchical Planning and Persistent State

- 分数：16.5  ·  HF 赞：9  ·  来源：huggingface
- 兴趣命中：spec, planning
- 作者：Xiaoxiao Ma, Weiyang Jin, Yanwen Ma, Haoran Li, Zhixiang Wei, Songchun Zhang, Yaowei Li, Junhao Zhuang, Zeyue Xue, Yuming Li, Zheming Fu, Haoyang Huang, Nan Duan, Feng Zhao
- 链接：[arXiv](https://arxiv.org/abs/2610.28827) · [PDF](https://arxiv.org/pdf/2610.28827) · [HF](https://huggingface.co/papers/2610.28827)

We present WorldStream, an open-ended 3D world model with three simultaneous capabilities: it extends playable terrain beyond any pre-specified map, acts on open-ended language in the running world, and restores visited places with their edits. A hierarchical planner over a typed decision model emits structured decision state: Macro fixes settlement, ecology, transport, and hydrological structure across a group of…

## 56. Toward Part-Aware Choral Transcription with singing voice assignment

- 分数：16.0  ·  HF 赞：8  ·  来源：huggingface
- 兴趣命中：evaluation, spec
- 作者：Hanyu Meng, Zhanhong He, Zixun Guo, Yaolong Ju
- 链接：[arXiv](https://arxiv.org/abs/2610.09861) · [PDF](https://arxiv.org/pdf/2610.09861) · [HF](https://huggingface.co/papers/2610.09861)

Single-instrument automatic music transcription (AMT) has advanced substantially, yet choral applications require soprano, alto, tenor, and bass (SATB) to be transcribed as separate parts. Recent note-level choral AMT instead produces a single merged note track, limiting rehearsal, education, and score reconstruction. To address this limitation, we introduce Part-aware Choral Transcription (PawCT), to our knowledge…

## 57. Design Anything, Design at Scale

- 分数：16.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：agent, evaluation, spec
- 作者：Xuchao Ren, Siyuan Feng, Jing Huang, Yanhua Yao, Jing Wang, Lingyu Alina Wang, Anan Chen, Hangjie Yuan, Tao Feng, Qiong Wu, Sai Ma
- 链接：[arXiv](https://arxiv.org/abs/2610.24771) · [PDF](https://arxiv.org/pdf/2610.24771) · [HF](https://huggingface.co/papers/2610.24771)

As multimodal resources are transformed into media outputs, agentic AI is expected to stay aligned with design intent over long horizons. Designers follow briefs specifying goals, constraints, and deliverables, with later work building on earlier decisions. Recent work reuses design experience across tasks, yet alignment among artifacts within one project remains challenging. Agents therefore need to preserve and…

## 58. MMedAgent-Plus: Scaling Multimodal Medical Agents across Modalities, Tasks and Workflows

- 分数：16.0  ·  HF 赞：0  ·  来源：huggingface
- 兴趣命中：agent, tool-use, evaluation, benchmark, spec
- 作者：Ruoxin Wang, Yuanting Pan, Binxu Li, Ruiyang Ji, Yaqian Chen, Jiayuan Ding, Qifan Wang, Lifu Huang, Mingjie Li, Yu Zhang, Ehsan Adeli, Kilian Pohl, Zhe Xu, Zihao Lin, Haoyu Dong, Yixin Wang
- 链接：[arXiv](https://arxiv.org/abs/2610.27233) · [PDF](https://arxiv.org/pdf/2610.27233) · [HF](https://huggingface.co/papers/2610.27233)

Medical workflows often require multiple interdependent analyses, but existing specialist and generalist AI models are not designed to coordinate them. We introduce MMedAgent-Plus, a multimodal medical tool-use agent that combines a vision-language planner with 18 leading specialist models spanning 12 tasks and 8 modalities. Through a unified tool interface, the planner selects specialists, executes them in…

## 59. Sparsity Should Be ALLOTted by Output: Training-Free Allocation of Block-Sparse Attention for Video Diffusion Transformers

- 分数：15.5  ·  HF 赞：15  ·  来源：huggingface
- 兴趣命中：-
- 作者：Tianze Xia, Xiaoling Zhou, Ruya Lan, Yiqiao Liao, Chengru Song, Shiming Xiang
- 链接：[arXiv](https://arxiv.org/abs/2610.29441) · [PDF](https://arxiv.org/pdf/2610.29441) · [HF](https://huggingface.co/papers/2610.29441)

Full 3D attention is costly in video Diffusion Transformers. Block-sparse attention reduces this cost by computing only selected attention blocks. However, existing methods either overlook the potential to optimize sparsity allocation or rely on heuristic rules or local metrics to guide it. In this work, we observe that sparsifying attention in different layers and at different denoising steps affects final-video…

## 60. Rethinking Sequence Compression with Test-time Regression

- 分数：15.5  ·  HF 赞：7  ·  来源：huggingface
- 兴趣命中：language model, large language
- 作者：Sihan Yang, Jie Huang, Hanxuan Li, Yifan Guo, Weigao Sun, Yiran Zhong, Weiyang Liu
- 链接：[arXiv](https://arxiv.org/abs/2610.31574) · [PDF](https://arxiv.org/pdf/2610.31574) · [HF](https://huggingface.co/papers/2610.31574)

Sequence compression is a fundamental operation and a critical information bottleneck in efficient language and multimodal models, and yet prevailing approaches based on pooling or learned projections remain underperforming. We revisit sequence compression through the lens of test-time regression: input tokens define a regression problem whose fitted coefficients form the compressed representation. Importantly, the…

## 61. Reading, Writing, Sharing, and Interacting with the World through Video

- 分数：15.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：evaluation, benchmark, spec
- 作者：Shengqiong Wu, Meng Luo, Bobo Li, Ziwei Liu, Shuicheng Yan, Ming-Hsuan Yang, Philip Torr, Hao Fei
- 链接：[arXiv](https://arxiv.org/abs/2610.31668) · [PDF](https://arxiv.org/pdf/2610.31668) · [HF](https://huggingface.co/papers/2610.31668)

Video foundation models have advanced rapidly in understanding and generating visual sequences, while video world models seek to capture the underlying dynamics of the world they depict. Despite their different objectives, both concern the relationship between video observations and an evolving world. This survey adopts world modeling as a unifying lens for examining these developments. Viewing an observed video as…

## 62. LaLa-World: Scaling Latent World Models with Natural Language Actions

- 分数：15.0  ·  HF 赞：6  ·  来源：huggingface
- 兴趣命中：language model, planning
- 作者：Junha Song, Geonmo Gu, Jeongeun Park, Heejeong Nam, Lucas Maes, Byeongho Heo, Dongyoon Han, Sangdoo Yun
- 链接：[arXiv](https://arxiv.org/abs/2610.27851) · [PDF](https://arxiv.org/pdf/2610.27851) · [HF](https://huggingface.co/papers/2610.27851)

This paper shows that JEPA-style latent world models (LWMs) can learn across diverse domains and data sources by adopting the language-conditioned interface of video generation models. We establish this approach as an effective and efficient basis for planning with imagination and downstream policy fine-tuning. To this end, we introduce LaLa-World, a Language-conditioned Latent World model that learns from…

## 63. RoboCasa-Shift: Stage-Aware Robustness Evaluation of Vision-Language-Action Policies in Long-Horizon Household Manipulation

- 分数：15.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：evaluation, benchmark, spec
- 作者：Haocheng Wang, Youquan Liu, Weiyu Guo, Aokai Zhang, Donghang Wu, Hongyu Liu, Sha Zhang, Weidong Yang, Ben Fei
- 链接：[arXiv](https://arxiv.org/abs/2610.27861) · [PDF](https://arxiv.org/pdf/2610.27861) · [HF](https://huggingface.co/papers/2610.27861)

Vision-language-action (VLA) robustness is commonly summarized by aggregate task success, which obscures how individual executions change under distribution shifts and where failures emerge in long-horizon tasks. We introduce RoboCasa-Shift, a diagnostic robustness benchmark built on RoboCasa365 that combines controlled single-factor shifts, matched clean-perturbed rollouts in which each pair shares the same…

## 64. StyleStream 2.0: Fast and Controllable Streaming Voice Style Conversion

- 分数：14.5  ·  HF 赞：9  ·  来源：huggingface
- 兴趣命中：spec
- 作者：Yisi Liu, Nicholas Lee, Gopala K. Anumanchipalli
- 链接：[arXiv](https://arxiv.org/abs/2610.28940) · [PDF](https://arxiv.org/pdf/2610.28940) · [HF](https://huggingface.co/papers/2610.28940)

Voice style conversion (VSC) aims to transform a source utterance to match the timbre, accent, and emotion of a target voice while preserving linguistic content. StyleStream 1.0 introduced the first streamable zero-shot VSC system with state-of-the-art conversion quality, but remained limited in two ways: approximately 1s end-to-end latency on consumer hardware, and the lack of a text-based interface for designing…

## 65. VX-One: Typed, Calibrated Decision Heads for Real-Time Perimeter Triage - An empirical study of unknown-attack honesty, cascade gray zones, and calibration under drift

- 分数：14.5  ·  HF 赞：9  ·  来源：huggingface
- 兴趣命中：benchmark
- 作者：Juan S. Santillana
- 链接：[arXiv](https://arxiv.org/abs/2610.30090) · [PDF](https://arxiv.org/pdf/2610.30090) · [HF](https://huggingface.co/papers/2610.30090)

Perimeter triage faces a latency/semantics trade-off: signature engines are fast and format-safe but blind to unseen attacks, while generative models are semantic but slow and produce unparseable output. In late 2026 a class of commercial System One decision models (TypeSafe Jev; Microsoft-Decision-1) began selling typed decision primitives - binary gates, closed-set choices, ordinal scores - as product APIs, with…

## 66. AnyGameRenderer: Entity-Consistent Generative Rendering Across Games and an Entity-Level Benchmark

- 分数：14.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：agent, benchmark, coding
- 作者：Ruicong Liu, Liangyang Ouyang, Fengbo Lan, Zhixiang Wang, Kaipeng Zhang
- 链接：[arXiv](https://arxiv.org/abs/2610.31466) · [PDF](https://arxiv.org/pdf/2610.31466) · [HF](https://huggingface.co/papers/2610.31466)

AI coding agents can now build small playable games in minutes, but the results usually look like programmer art: gray blockouts, colored geometric primitives, and flat semantic blobs. We present AnyGameRenderer, a video-to-video generative renderer that turns such footage into high-quality visuals with characters, motion detail, and effects. Throughout, it keeps the layout, camera, and every entity's position and…

## 67. Skeleton-Grounded Latent Action Model for Robot World Models

- 分数：14.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：evaluation, coding, spec
- 作者：Qi Lv, Jiayi Lin, Yuxin Jiang, Jianzong Wang, Xiang Deng, Mike Shou Zheng
- 链接：[arXiv](https://arxiv.org/abs/2610.31474) · [PDF](https://arxiv.org/pdf/2610.31474) · [HF](https://huggingface.co/papers/2610.31474)

Robot world models simulate how environments evolve in response to robot actions. Latent action models enable learning dynamics from videos by encoding visual transitions as proxy actions. However, reconstruction-driven latent actions mix robot motion with object responses and other scene changes, complicating their correspondence with robot controls. We propose SkeLAM, a skeleton-guided latent action model for…

## 68. Answering in the User's Variety: Calibrated Accommodation Pairs for Post-Training

- 分数：14.0  ·  HF 赞：8  ·  来源：huggingface
- 兴趣命中：reinforcement learning
- 作者：Zhizhuo Kou, Heming Li, Jian Yang, Junyu Luo, Jingshu Peng, Sirui Han, Yike Guo
- 链接：[arXiv](https://arxiv.org/abs/2610.28474) · [PDF](https://arxiv.org/pdf/2610.28474) · [HF](https://huggingface.co/papers/2610.28474)

People adapt how they talk to the person in front of them. However, chat models tend to respond in Standard English regardless of the dialect used by the user. A uniform answer can hide whether training treats these users alike, and output audits cannot tell as well. We trace how each post-training stage, from supervised fine-tuning (SFT) to preference optimization (DPO) and reinforcement learning, changes a model's…

## 69. Looped Uniform Diffusion Language Models

- 分数：14.0  ·  HF 赞：4  ·  来源：huggingface
- 兴趣命中：reasoning, language model
- 作者：Saiteja Utpala, Chieh-Hsin Lai, Yuki Mitsufuji, Praneeth Vepakomma
- 链接：[arXiv](https://arxiv.org/abs/2610.30066) · [PDF](https://arxiv.org/pdf/2610.30066) · [HF](https://huggingface.co/papers/2610.30066)

Uniform diffusion language models (UDLMs) generate text by iteratively denoising sequences of ordinary vocabulary tokens, any of which may be corrupted and subsequently revised. During training, UDLMs must denoise from a context that may itself be unreliable, whereas masked diffusion language models (MDLMs) always condition on a clean context. This challenging training objective makes UDLMs more FLOP-intensive to…

## 70. Same Simulation, Different Evidence: Where Retrieved Tool Output Costs LLM Agents Accuracy

- 分数：14.0  ·  HF 赞：0  ·  来源：huggingface
- 兴趣命中：agent, context window, retrieval
- 作者：Ke Zhang, Sahchit Chundur, Jerry Peprah Owusu, Mohammad Javad Abdolhosseini Qomi, Maziar Raissi
- 链接：[arXiv](https://arxiv.org/abs/2610.26836) · [PDF](https://arxiv.org/pdf/2610.26836) · [HF](https://huggingface.co/papers/2610.26836)

LLM agents that compute the right answer can still answer wrongly. Agent harnesses increasingly keep long tool outputs out of the context window, saving them to files that the agent searches or reads on demand. We ask where this costs accuracy with a real scientific tool: PHREEQC, a widely used geochemistry simulator from the USGS, whose reports reach 846.8k characters and whose determinism lets every printed value…

## 71. Exploring The Empirical Privacy Landscape of Synthetic Data

- 分数：13.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：evaluation, language model
- 作者：Zihao Zhao, Avi Schwarzschild, Casey Meehan, Katherine Lee, Zhili Feng, Dylan Sam
- 链接：[arXiv](https://arxiv.org/abs/2610.22659) · [PDF](https://arxiv.org/pdf/2610.22659) · [HF](https://huggingface.co/papers/2610.22659)

Methods for training language models on sensitive data differ in how they balance capability gains against the risk of leaking private information. In this paper, we present a controlled comparison of data-level and training-level interventions for navigating the capability-privacy tradeoff on synthetic medical records with canaries to probe for leakage. Direct finetuning performs best on capability metrics but…

## 72. Toward Recursive Self-Improvement in Physical AI

- 分数：13.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：agent, evaluation
- 作者：Meng Luo, Zechen Bai, Shanqing Xu, Yanlin Li, Kaixin Li, Mengchen Qian, Weifeng Lu, Ran Zhang, Yingtian Zou, Ziyang Luo, Wei Chen, Hongzhan Lin
- 链接：[arXiv](https://arxiv.org/abs/2610.29677) · [PDF](https://arxiv.org/pdf/2610.29677) · [HF](https://huggingface.co/papers/2610.29677)

Recursive self-improvement (RSI) describes a system that improves not only its behavior but also the process by which it improves. Recent digital agents test this idea by rewriting their own code and checking each version with executable tests. Bringing these mechanisms into the physical world requires learning from partial observations through costly trials, while accounting for changing operating conditions and…

## 73. Inherited, Not Invented: Tracing the Provenance of Wait in Reasoning Models

- 分数：13.0  ·  HF 赞：2  ·  来源：huggingface
- 兴趣命中：reasoning, reinforcement learning
- 作者：Zhizhuo Kou, Sizai Hou, Long Chen, Jian Yang, Junyu Luo, Jingshu Peng, Wenkai Zhang, Sirui Han, Yike Guo
- 链接：[arXiv](https://arxiv.org/abs/2610.30882) · [PDF](https://arxiv.org/pdf/2610.30882) · [HF](https://huggingface.co/papers/2610.30882)

Reinforcement learning (RL) is credited with teaching reasoning models to write {wait} before reconsidering a step, yet large RL accuracy gains do not require the word. This view can confuse what RL discovers with what a model inherits from its training data. We trace the word through open models' training histories, reading it with label-free indices of frequency, position, form and usage and an injected-error…

## 74. Cola2: Co-Adaptive Hierarchical Language Modeling with Continuous Semantic Compression and Balanced Discrete Generation

- 分数：12.5  ·  HF 赞：5  ·  来源：huggingface
- 兴趣命中：language model
- 作者：Hongcan Guo, Yian Zhao, Feng Wang, Shen Nie, Guoqiang Wei, Yan Zeng, Hengshuang Zhao
- 链接：[arXiv](https://arxiv.org/abs/2610.31305) · [PDF](https://arxiv.org/pdf/2610.31305) · [HF](https://huggingface.co/papers/2610.31305)

Hierarchical language generation separates continuous semantic modeling from discrete text realization, but its effectiveness depends on what the latent space compresses and how the discrete generator uses it. We propose Cola2, a framework that jointly studies continuous semantic compression, the balance between reconstruction and generation, and continuous-discrete co-adaptation. Cola2 dynamically segments text…

## 75. FrontierCS 2: A Benchmark for Computer Science R&D

- 分数：12.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：agent, benchmark
- 作者：Qiuyang Mang, Wenhao Chai, Runyuan He, Dongruixuan Li, Zihan Zheng, Yujun He, Xuanyi Zhou, Hao Wang, Siddhant Ray, Bo Peng, Ruyi Ji, Shuo Yang, Haocheng Xi, Boru Chen, Xinyang David Han, Melissa Pan, Mayank Mishra, Boxi Yu, Sijia Liu, Kerem Akillioglu, Yi Pan, Zirui Wang, Mert Cemri, Diogo Antunes, Yichuan Wang, Aiwei Ivy Zhang, Zhenyang Chen, Qizheng Zhang, Kaiyuan Liu, Wenyuan Huang, Sherry Ruan, Shu Liu, Dacheng Li, Zerui Cheng, Zeyu Shen, Shang Zhou, Hanfei Chen, Yuzhong Zhang, Bohan Lyu, Qu Ao, Han Zheng, Chonghe Jiang, Jingzhuo Hu, Xiaokun Chen, Kunjun Li, Zhiqing Zhong, Haoye Tian, Tong Zhao, Yunzhong He, Hanchen Li, Ofir Press, Jiantao Jiao, Kunle Olukotun, Karthik R. Narasimhan, Jingbo Shang, Koushik Sen, Matei Zaharia, Alex Dimakis, Ion Stoica, Joseph E. Gonzalez, Alvin Cheung
- 链接：[arXiv](https://arxiv.org/abs/2610.29932) · [PDF](https://arxiv.org/pdf/2610.29932) · [HF](https://huggingface.co/papers/2610.29932)

Can LLM agents make contributions to frontier computer science R&D? We introduce FrontierCS 2, a benchmark of 48 open-ended tasks. We take a paper and the code its authors released and delete the paper's contribution. The deleted code becomes the human reference that sets the bar. Earlier open-ended benchmarks give each agent a problem statement and grade one program after the run. FrontierCS 2 places the agent…

## 76. Foundation4D: Towards a unified perception and reconstruction model for autonomous vehicles

- 分数：12.0  ·  HF 赞：0  ·  来源：huggingface
- 兴趣命中：benchmark, spec
- 作者：NVIDIA, Sérgio Agostinho, Maximilian Apodaca, Emmanuel Attia, Guillem Braso, George Dong, Ilya Fedorov, Michele Fenzi, Gang Huang, Jiahui Huang, Shengyu Huang, Bingxin Ke, Laura Leal-Taixé, Kuan-Ting Lee, Mingxuan Liu, Tian Liu, Tim Meinhardt, Aljoša Ošep, Naveen Kumar Rai, Kefei Ren, Cristiano Saltori, Keqiang Wu, Ning Xu, Fei Xue, Jin-Bey Yu, Lei Zhang, Qunjie Zhou
- 链接：[arXiv](https://arxiv.org/abs/2610.30340) · [PDF](https://arxiv.org/pdf/2610.30340) · [HF](https://huggingface.co/papers/2610.30340)

We introduce Foundation4D, a unified feed-forward model for geometry estimation, 3D detection, semantic occupancy, and Gaussian reconstruction from multi-camera driving video. A shared backbone uses factorized spatiotemporal attention to efficiently combine observations across cameras and time. Our video inference pipeline uses pose graph optimization to refine camera trajectories and assembles object tracks across…

## 77. MolLean: A Process-Verifiable Language for Chemical Reasoning

- 分数：11.5  ·  HF 赞：3  ·  来源：huggingface
- 兴趣命中：reasoning
- 作者：Jiatong Li, Yatao Bian
- 链接：[arXiv](https://arxiv.org/abs/2610.20459) · [PDF](https://arxiv.org/pdf/2610.20459) · [HF](https://huggingface.co/papers/2610.20459)

Chemical chain-of-thought can contain hallucinated structural and property claims. We thereby introduce MolLean, a process-verifiable language that grounds chemical reasoning in an explicit molecular state. A layered Lean-based kernel checks state transitions and assertions over molecular readouts, from primitive graph edits to compound transformations. Meanwhile, a typed witness protocol separates native structural…

## 78. Policy-Mask: Budget-Aware Adaptation of Diffusion Features to Discriminative Tasks

- 分数：10.5  ·  HF 赞：5  ·  来源：huggingface
- 兴趣命中：-
- 作者：Ivan Listopadov, Maksim Nakhodnov, Aibek Alanov
- 链接：[arXiv](https://arxiv.org/abs/2610.28889) · [PDF](https://arxiv.org/pdf/2610.28889) · [HF](https://huggingface.co/papers/2610.28889)

Selecting intermediate features from a frozen diffusion model for discriminative tasks is non-trivial because the useful signal is distributed across the denoising trajectory, network depth, and channels. In practice, this requires choosing a timestep, a block, and a channel subset. Existing methods either fix these choices by hand or optimize only a few extraction hyperparameters, most often the timestep, then…

## 79. SEAM: Spectral Embedding Alignment and Merging for Low-Resource TTS

- 分数：10.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：spec
- 作者：Walaa Othman, Baher Mohammad, Stamatios Lefkimmiatis, Ammar Ali
- 链接：[arXiv](https://arxiv.org/abs/2610.26252) · [PDF](https://arxiv.org/pdf/2610.26252) · [HF](https://huggingface.co/papers/2610.26252)

Expanding the vocabulary of conditional text-to-speech (TTS) models typically requires extensive fine-tuning with paired audio, creating a major bottleneck for low-resource and cross-lingual adaptation. To address this, we introduce SEAM, a zero-audio initialization method that constructs embeddings for unseen tokens from known subtokens. Unlike standard pooling strategies that ignore sequential structure, SEAM…

## 80. Bridged Self-Distillation for On-Policy Learning

- 分数：10.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：reasoning
- 作者：Runsheng Chen, Yihong Liu, Raoyuan Zhao, Michael A. Hedderich, Hinrich Schütze, Matthias Grabmair
- 链接：[arXiv](https://arxiv.org/abs/2610.26397) · [PDF](https://arxiv.org/pdf/2610.26397) · [HF](https://huggingface.co/papers/2610.26397)

On-policy distillation can transfer the reasoning capabilities of a strong teacher to a smaller student. However, distillation from a stronger teacher model faces two mismatches: its solutions may be difficult for a smaller student to imitate, and its token-level probabilities may be incompatible with, or even unavailable to, the student. Existing methods handle these settings through different forms of supervision.…

## 81. Self-Distilling Future Video Representations for World Action Models

- 分数：10.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：spec
- 作者：Huiwon Jang, Suhyeok Jang, Hyeonmo Kang, Seungku Kim, Jinwoo Shin, Sihyun Yu
- 链接：[arXiv](https://arxiv.org/abs/2610.30320) · [PDF](https://arxiv.org/pdf/2610.30320) · [HF](https://huggingface.co/papers/2610.30320)

World Action Models (WAMs) have emerged as a promising approach to learning generalist robot policies using rich spatiotemporal priors from pre-trained video diffusion models. A recent line of WAMs improves inference efficiency by conditioning a separate action decoder on intermediate future video representations extracted from a single denoising step, avoiding costly iterative denoising required for video…

## 82. F2G-Pose: Geometry-Aware Foundation Feature Lifting for Direct RGB-D Category-Level Object Pose Estimation

- 分数：10.5  ·  HF 赞：1  ·  来源：huggingface
- 兴趣命中：spec
- 作者：Jinyu Zhang, Haitao Lin, Jiashu Hou, Xiangyang Xue, Yanwei Fu
- 链接：[arXiv](https://arxiv.org/abs/2610.31623) · [PDF](https://arxiv.org/pdf/2610.31623) · [HF](https://huggingface.co/papers/2610.31623)

This paper studies category-level RGB-D object pose estimation, which recovers an object's 3D rotation and translation without instance-specific CAD models or reference views. This task is highly ambiguous due to intra-class variations, symmetries, and partial observations. Current solutions struggle to balance reliability and efficiency: methods based on intermediate structures are prone to error propagation, while…
