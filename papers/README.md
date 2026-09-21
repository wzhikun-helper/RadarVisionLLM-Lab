\# Papers / 论文资料



This directory stores literature information related to the RadarVisionLLM-Lab research direction.



本目录用于管理与 RadarVisionLLM-Lab 研究主线相关的论文资料和文献信息。



\---



\## 1. Main Purpose / 主要用途



This directory is used to support:



本目录主要用于支持：



\* Literature Review / 系统文献调研

\* Paper Matrix / 论文矩阵

\* Topic Tracking / 研究方向跟踪

\* Related Work Comparison / Related Work 横向比较

\* Innovation Discovery / 创新点发现

\* Baseline Selection / Baseline 选择



\---



\## 2. Core File / 核心文件



\### `paper\_matrix.csv`



This file stores structured comparison information for relevant papers.



该文件用于对相关论文进行结构化横向比较。



Typical comparison dimensions include:



典型比较维度包括：



\* Task / 任务

\* Year / 年份

\* Venue / 会议或期刊

\* Radar Type / 雷达类型

\* Radar Representation / 雷达表示

\* Range

\* Doppler

\* RCS

\* Camera

\* Dataset

\* Fusion Level / 融合层级

\* BEV

\* Temporal Modeling / 时序建模

\* Cross-Attention

\* VLM

\* LLM

\* Physical Constraint / 物理约束

\* Uncertainty / 不确定性

\* Adverse Weather / 恶劣天气

\* Night / 夜间

\* Occlusion / 遮挡

\* Open Source / 是否开源

\* Main Contribution / 核心贡献

\* Main Limitation / 主要局限

\* Potential Gap / 潜在 Gap

\* Reproduction Value / 复现价值



\---



\## 3. Paper Storage Principle / 论文存储原则



The repository should primarily track metadata, notes, and public links.



Git 仓库主要管理：



\* Paper metadata / 论文元信息

\* Public links / 公开链接

\* Paper Matrix entries / 矩阵记录

\* Reading notes / 阅读笔记

\* Reproduction decisions / 复现决策



Large numbers of PDF files do not have to be committed directly into Git.



大量 PDF 原文不强制直接进入 Git。



Reasons include:



原因包括：



\* File size / 文件较大

\* Copyright / 版权问题

\* Difficult version comparison / 不适合版本差异比较

\* Repository maintenance / 增加仓库维护成本



\---



\## 4. Suggested Research Categories / 建议论文分类



Current categories may include:



当前建议重点关注：



\* Radar Fundamentals / 雷达基础

\* 4D Radar

\* Radar-Camera Fusion / 雷视融合

\* 3D Object Detection / 3D目标检测

\* BEV Perception / BEV感知

\* Multimodal Fusion / 多模态融合

\* VLM / 视觉语言模型

\* Radar-VLM

\* Sensor Grounding / 传感器约束

\* Robustness / 鲁棒性

\* Uncertainty / 不确定性

\* Adverse Weather / 恶劣天气

\* Motion Reasoning / 运动推理



\---



\## 5. Reading Relationship / 与论文笔记的关系



Detailed reading notes should be stored under:



详细阅读笔记放在：



```text

paper\_notes/

```



The relationship is:



二者关系：



```text

papers/

论文总体管理

&#x20;     ↓

paper\_matrix.csv

横向比较

&#x20;     ↓

paper\_notes/

单篇论文纵向精读

```



\---



\## 6. Principle / 原则



Do not read papers in isolation.



不要孤立地读论文。



Every relevant paper should gradually become part of a structured research map.



每篇重要论文最终都应进入系统化的研究版图中。



