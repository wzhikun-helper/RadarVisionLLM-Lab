\# Paper Note / 论文精读笔记



\## 0. Basic Information / 基本信息



\* \*\*Title / 题目：\*\*

\* \*\*Authors / 作者：\*\*

\* \*\*Venue / 会议或期刊：\*\*

\* \*\*Year / 年份：\*\*

\* \*\*DOI / arXiv：\*\*

\* \*\*Paper Link / 论文链接：\*\*

\* \*\*Official Code / 官方代码：\*\*

\* \*\*Dataset / 数据集：\*\*

\* \*\*Reading Level / 阅读等级：\*\* A / B / C

\* \*\*Reading Status / 阅读状态：\*\* Not Started / Reading / Finished

\* \*\*Date / 阅读日期：\*\*



\---



\# 1. Why Are We Reading This Paper? / 为什么读这篇论文？



这篇论文与我们的主线有什么关系？



\* Radar / 雷达：

\* Camera / 相机：

\* Radar-Camera Fusion / 雷视融合：

\* VLM / 大模型：

\* Robustness / 鲁棒性：

\* Physical Grounding / 物理约束：

\* Baseline Value / Baseline价值：



\### One-Sentence Reason / 一句话说明



>



\---



\# 2. One-Sentence Summary / 一句话总结论文



用自己的话完成：



> 作者针对 \_\_\_\_\_\_ 问题，观察到 \_\_\_\_\_\_，因此提出 \_\_\_\_\_\_，并在 \_\_\_\_\_\_ 数据集上证明 \_\_\_\_\_\_。



\---



\# 3. Background / 背景



论文研究的领域是什么？



当前任务是什么？



为什么这个任务重要？



涉及哪些核心概念？



\---



\# 4. Problem / 研究问题



作者真正想解决的问题是什么？



不要写成：



> “提高准确率。”



应该写成具体问题，例如：



> 现有 Radar-Camera 方法在雷达点云稀疏时，难以充分建立 Radar 与 Camera 特征之间的语义对应关系。



\---



\# 5. Existing Methods / 现有方法



论文之前主要有哪些方法？



\### Method A



\* 核心思想：

\* 优点：

\* 缺点：



\### Method B



\* 核心思想：

\* 优点：

\* 缺点：



\---



\# 6. Research Gap / 研究空白



作者认为现有工作哪里不够？



\### Explicit Gap / 作者明确指出的 Gap



>



\### Implicit Gap / 我们自己观察到的 Gap



>



注意区分：



\* 作者明确声明的 limitation

\* 我们自己推断出的 limitation



\---



\# 7. Key Observation / 核心观察



作者观察到了什么现象？



例如：



> Radar Doppler information remains reliable under poor illumination.



这个 observation 是否有实验支持？



\* \[ ] Yes

\* \[ ] No

\* \[ ] Partially



对应 Figure / Table：



\---



\# 8. Insight / 核心洞察



作者从 Observation 得出了什么设计思想？



用：



```text

Observation

&#x20;   ↓

Insight

&#x20;   ↓

Method

```



整理。



\### Observation



>



\### Insight



>



\### Method



>



\---



\# 9. Method Overview / 方法总览



先不用看公式。



回答：



\### Input / 输入



\* Camera：

\* Radar：

\* Other：



\### Output / 输出



\### Overall Pipeline / 总流程



```text

Input

&#x20; ↓

Encoder

&#x20; ↓

Fusion

&#x20; ↓

Prediction

```



根据论文自行修改。



\---



\# 10. Module Analysis / 模块分析



\## Module 1



\### Name / 名称



\### Input



\### Output



\### Purpose / 解决什么问题？



\### How / 怎么实现？



\### Why / 为什么这样设计？



\### Important Code / 对应代码



\---



\## Module 2



\### Name



\### Input



\### Output



\### Purpose



\### How



\### Why



\### Important Code



\---



\# 11. Important Equations / 重要公式



\## Equation 1



原公式：



\[

...

]



\### Symbols / 符号解释



\*

\*

\*



\### Plain-Language Explanation / 大白话解释



>



\### Why Is It Needed? / 为什么需要？



>



\---



\# 12. Data Flow / 数据流



重点记录 Tensor / Feature shape。



例如：



```text

Radar Points

\[N, 5]



↓ Radar Encoder



Radar Features

\[B, C, H, W]



↓ Fusion



BEV Features

\[B, C', H', W']

```



实际论文：



```text

...

```



\---



\# 13. Dataset / 数据集



\* Dataset：

\* Training Split：

\* Validation Split：

\* Test Split：

\* Number of Frames：

\* Sensors：

\* Radar Type：

\* Camera：

\* Annotation：

\* Weather：

\* Day/Night：

\* Important Characteristics：



\---



\# 14. Experimental Setup / 实验设置



\* GPU：

\* Framework：

\* Optimizer：

\* Learning Rate：

\* Batch Size：

\* Epochs：

\* Input Resolution：

\* Radar Sweeps：

\* Random Seed：

\* Main Metrics：



\---



\# 15. Baselines / 对比方法



| Method | Year | Main Idea | Why Compare? |

| ------ | ---: | --------- | ------------ |

|        |      |           |              |



\---



\# 16. Main Results / 主要结果



| Method   | Metric 1 | Metric 2 | Metric 3 |

| -------- | -------: | -------: | -------: |

| Baseline |          |          |          |

| Paper    |          |          |          |



\### What Does the Result Actually Prove? / 这个结果真正证明了什么？



>



\### What Does It NOT Prove? / 它没有证明什么？



>



\---



\# 17. Ablation Study / 消融实验



记录每个模块：



| Component | Result | Change | Interpretation |

| --------- | -----: | -----: | -------------- |

|           |        |        |                |



问题：



> 如果去掉核心模块，性能真的下降了吗？



> 是否存在模块很多但贡献很小的情况？



\---



\# 18. Robustness / 鲁棒性



论文是否测试：



\* \[ ] Night / 夜间

\* \[ ] Rain / 雨

\* \[ ] Fog / 雾

\* \[ ] Snow / 雪

\* \[ ] Occlusion / 遮挡

\* \[ ] Sensor Noise / 传感器噪声

\* \[ ] Missing Modality / 模态缺失

\* \[ ] Domain Shift / 跨域

\* \[ ] Different Scenes / 不同场景



结果：



>



\---



\# 19. Failure Cases / 失败案例



论文在哪里失败？



是否展示 failure case？



\### Case 1



场景：



原因：



\### Case 2



场景：



原因：



\---



\# 20. Limitations / 局限性



\## Author-Stated Limitations / 作者明确承认



1\.

2\.

3\.



\## Our Observed Limitations / 我们观察到



1\.

2\.

3\.



注意：



这里是未来 Research Gap 的重要来源。



\---



\# 21. Figure Library / 图库记录



\## Figure X



\### Type



\* Motivation

\* System Overview

\* Architecture

\* Heatmap

\* CDF

\* Ablation

\* Robustness

\* Failure Case

\* Other



\### What Does It Show? / 表达什么？



>



\### Why Is It Good? / 为什么画得好？



>



\### Role in Paper Story / 在论文故事里的作用



>



\### How Could We Draw Something Similar? / 我们以后怎么重新画？



需要的数据：



需要的脚本：



横轴：



纵轴：



想证明的结论：



\---



\# 22. Academic Phrasebook / 好词好句



不要整句复制使用，只学习表达结构。



\### Phrase 1



Original:



>



Function / 功能：



例如：



\* 引出问题

\* 描述挑战

\* 指出现有不足

\* 提出 insight

\* 描述实验结果



Pattern / 可学习结构：



>



Our Possible Usage / 我们以后可以怎么表达：



>



\---



\# 23. Reproduction Value / 复现价值



\### Is the Code Open Source? / 是否开源？



\* \[ ] Yes

\* \[ ] No



\### Is the Dataset Available? / 数据是否可获得？



\* \[ ] Yes

\* \[ ] No



\### Reproduction Difficulty / 复现难度



\* Low / 低

\* Medium / 中

\* High / 高



\### Why Reproduce? / 为什么值得复现？



>



\### Decision / 决策



\* \[ ] Full Reproduction / 完整复现

\* \[ ] Partial Reproduction / 部分复现

\* \[ ] Read Only / 只阅读



\---



\# 24. Possible Research Ideas / 潜在创新点



\## IDEA Candidate 1



\### Problem



\### Evidence



\### Closest Work



\### Difference



\### Minimal Experiment



\### Risk



\---



\# 25. Relation to Our Main Research / 与我们主线的关系



这篇论文对我们的：



\### Background



>



\### Baseline



>



\### Method



>



\### Evaluation



>



\### Innovation



>



有什么价值？



\---



\# 26. Questions I Still Cannot Answer / 尚未理解的问题



1\.

2\.

3\.



这些问题后续读代码或相关论文解决。



\---



\# 27. Final Takeaways / 最终收获



\### Three Most Important Things / 最重要的三点



1\.

2\.

3\.



\### One Thing Worth Reusing / 最值得借鉴的一点



>



\### One Limitation Worth Investigating / 最值得继续研究的局限



>



\### Paper Status



\* \[ ] Finished

\* \[ ] Matrix Updated

\* \[ ] Figures Archived

\* \[ ] Phrasebook Updated

\* \[ ] Innovation Bank Updated

\* \[ ] Reproduction Decision Made



