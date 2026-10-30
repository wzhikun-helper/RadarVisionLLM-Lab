\# RadarVisionLLM-Lab Research Roadmap / 科研路线图



This roadmap defines the long-term research path from beginner-level learning to a complete research paper.



本路线图用于规划从初学者入门，到能够独立完成一篇完整科研论文的长期过程。



\---



\## Milestone 0 — Research Engineering / 科研工程初始化



\### Goal / 目标



Build a reproducible and maintainable research workspace.



建立一个长期可维护、可复现、可追踪的科研工程环境。



\### Main Tasks / 主要任务



\* Git and version control / Git 与版本管理

\* Repository structure / 项目目录结构

\* README system / README 文档体系

\* Research protocol / 科研规范

\* Learning-note system / 学习笔记体系

\* Research logs / 科研日志体系

\* Experiment management / 实验管理体系

\* Paper-note system / 论文笔记体系

\* Innovation Bank / 创新点库



\### Exit Criteria / 阶段验收



I should be able to explain:



完成本阶段后，我应该能够解释：



\* What is a Git repository? / Git 仓库是什么？

\* What is a commit? / commit 是什么？

\* Why should experiments be traceable? / 为什么实验要可追溯？

\* What should and should not be uploaded to Git? / 哪些内容应该或不应该进入 Git？

\* How is the research repository organized? / 科研仓库如何组织？



\---



\## Milestone 1 — Radar and Camera Fundamentals / 雷达与相机基础



\### Goal / 目标



Understand the physical and geometric foundations of radar-camera fusion.



理解雷达-相机融合所需的物理基础和几何基础。



\### Radar Topics / 雷达知识



\* Electromagnetic wave basics / 电磁波基础

\* Range / 距离

\* Azimuth / 方位角

\* Elevation / 俯仰角

\* Doppler / 多普勒

\* Radial Velocity / 径向速度

\* RCS

\* Radar Point Cloud / 雷达点云

\* 3D Radar

\* 4D Radar

\* Multipath / 多径

\* Radar noise / 雷达噪声



\### Camera Topics / 相机知识



\* RGB image / RGB 图像

\* Pixel coordinates / 像素坐标

\* Depth / 深度

\* 2D Bounding Box

\* 3D Bounding Box

\* Camera Intrinsics / 相机内参

\* Camera Extrinsics / 相机外参



\### Fusion Geometry / 融合几何



\* Coordinate systems / 坐标系

\* Calibration / 标定

\* Projection / 投影

\* Coordinate transformation / 坐标变换

\* Synchronization / 时间同步



\### Exit Criteria / 阶段验收



I should be able to explain:



我应该能够独立解释：



\* How radar measures range and velocity

\* 雷达为什么能测距离和速度

\* Why Doppler is radial velocity

\* 为什么 Doppler 测的是径向速度

\* Why radar and camera need calibration

\* 为什么雷达和相机需要标定

\* How a radar point can be projected onto an image

\* 雷达点为什么能投影到相机图像上



\---



\## Milestone 2 — Dataset Engineering / 数据工程



\### Goal / 目标



Learn to read, visualize, transform, and validate radar-camera datasets.



学会读取、可视化、转换和验证雷视数据集。



\### Initial Dataset / 初始数据集



View-of-Delft (VoD)



\### Tasks / 任务



\* Understand dataset directory structure / 理解数据目录结构

\* Read camera frames / 读取相机图像

\* Read radar point clouds / 读取雷达点云

\* Understand annotations / 理解标注

\* Read calibration parameters / 读取标定参数

\* Coordinate transformation / 坐标变换

\* Radar-to-camera projection / 雷达点投影到图像

\* Data visualization / 数据可视化

\* Dataset split management / 数据划分管理



\### Deliverables / 产出



\* Dataset README

\* Data loader

\* Camera visualization

\* Radar visualization

\* Radar-camera projection figure

\* Learning notes

\* Reproducible scripts



\### Exit Criteria / 阶段验收



Given one frame of radar and camera data, I should be able to explain where every important field comes from and how the two modalities correspond.



给我一帧 Radar + Camera 数据，我能够解释主要字段、坐标系以及两种模态如何对应。



\---



\## Milestone 3 — Radar-Camera Fusion Baseline Reproduction / 雷视融合基线复现



\### Goal / 目标



Understand representative radar-camera fusion methods through reproduction.



通过复现代表性论文，真正理解雷视融合方法。



\### Candidate Papers / 候选论文



\* CenterFusion

\* CRN

\* MSSF

\* Other methods selected after literature review



\### Reproduction Workflow / 复现流程



README



→ Repository Structure



→ Dataset



→ Preprocessing



→ Model



→ Loss



→ Training



→ Evaluation



→ Paper Result



→ Reproduced Result



→ Difference Analysis



\### Exit Criteria / 阶段验收



I should be able to:



我应该能够：



\* Run the official baseline

\* 跑通官方 baseline

\* Understand the main data flow

\* 理解核心数据流

\* Explain key modules

\* 解释关键模块

\* Locate important code

\* 找到关键代码

\* Modify part of the model independently

\* 独立修改部分模型代码



\---



\## Milestone 4 — Vision-Language Model Fundamentals / 视觉语言模型基础



\### Goal / 目标



Understand how visual information is converted into representations that language models can use.



理解视觉信息如何被转换为大语言模型可以处理的表示。



\### Topics / 学习内容



\* Vision Encoder / 视觉编码器

\* Transformer

\* Attention

\* Cross-Attention

\* Token

\* Image Token

\* Text Token

\* Multimodal Alignment / 多模态对齐

\* Projector

\* Prompting

\* Instruction Tuning

\* LoRA

\* Grounding

\* Hallucination

\* Uncertainty



\### Practical Goal / 实践目标



Build a basic image-question-answering pipeline and understand its input, output, and limitations.



搭建一个基本的图像问答 pipeline，并理解输入、输出和局限。



\---



\## Milestone 5 — Literature Gap Discovery / 文献调研与问题发现



\### Goal / 目标



Identify a meaningful research problem supported by literature and experiments.



基于文献证据和实验事实发现有意义的科研问题。



\### Tools / 工具



\* Paper Matrix / 论文矩阵

\* Paper Notes / 论文笔记

\* Figure Library / 科研图库

\* Limitation Bank / 局限性库

\* Innovation Bank / 创新点库

\* Reproduction observations / 复现观察

\* Failure cases / 失败案例



\### Research Questions / 重点问题



For every candidate idea, ask:



每个候选 Idea 都要回答：



\* What exactly is the problem? / 问题到底是什么？

\* Is the problem important? / 问题重要吗？

\* Who has already studied it? / 谁已经研究过？

\* What remains unsolved? / 还有什么没解决？

\* Why do existing methods fail? / 现有方法为什么不够？

\* Can we verify the problem with a small experiment? / 能不能先用小实验验证？

\* Is the idea feasible for our resources? / 资源是否允许？



\### Exit Criteria / 阶段验收



A candidate idea should only enter method development after minimal validation.



只有经过最小实验验证的 Idea，才进入正式方法设计阶段。



\---



\## Milestone 6 — Proposed Method / 方法设计与实现



\### Goal / 目标



Develop a method that directly addresses the validated research problem.



围绕已经验证的问题设计真正对应的方法。



\### Principle / 原则



Do not add modules without a clear reason.



不因为“某个模块流行”就直接加入。



Every module should answer:



每个模块都要回答：



\* What problem does it solve? / 它解决什么问题？

\* Why is it necessary? / 为什么需要？

\* What evidence supports it? / 有什么证据支持？

\* What happens if it is removed? / 去掉后会怎样？



\---



\## Milestone 7 — Full Experimental Evaluation / 完整实验评估



\### Required Experiments / 必要实验



\* Strong baseline comparison / 强 baseline 对比

\* Ablation study / 消融实验

\* Robustness evaluation / 鲁棒性实验

\* Failure-case analysis / 失败案例分析

\* Qualitative visualization / 定性可视化

\* Quantitative evaluation / 定量评估

\* Efficiency analysis / 效率分析

\* Repeated experiments when needed / 必要时重复实验

\* Statistical analysis when appropriate / 适当的统计分析



\### Experiment Principle / 实验原则



Every claim in the paper should be supported by an experiment whenever possible.



论文中的重要结论尽可能都应有对应实验支撑。



\---



\## Milestone 8 — Paper Writing / 论文写作



\### Goal / 目标



Turn the completed research into a clear and reproducible academic paper.



把完成的研究组织成逻辑清晰、证据完整、可复现的学术论文。



\### Writing Structure / 写作结构



Background / 背景



→ Problem / 问题



→ Gap / 空白



→ Insight / 洞察



→ Method / 方法



→ Evaluation / 实验



→ Discussion / 讨论



→ Limitation / 局限



\### Writing Assets / 写作资产



Maintain continuously:



长期维护：



\* Academic Phrasebook

\* Motivation notes

\* Related-work matrix

\* Figure library

\* Experiment tables

\* Contribution statements

\* Limitation notes



\---



\## Milestone 9 — Submission and Iteration / 投稿与迭代



\### Goal / 目标



Submit the work to an appropriate venue and use review feedback to improve future research.



向合适的会议或期刊投稿，并把审稿意见转化为下一轮科研能力提升。



\### Short-term Target / 短期目标



A solid CCF-C-level research paper.



完成一篇扎实的 CCF-C 级别研究工作。



\### Long-term Target / 长期目标



Develop the ability to identify and solve deeper problems suitable for CCF-B-level research.



逐步具备发现和解决 CCF-B 深度科研问题的能力。



\---



\## Current Research Hypothesis v0.1 / 当前研究假设 v0.1



Can radar physical measurements such as range and Doppler help detect or correct unreliable VLM motion reasoning under visual degradation?



在夜间、模糊、遮挡等视觉退化环境下，能否利用雷达的距离、多普勒等物理测量信息，检测或纠正视觉语言模型不可靠的运动推理？



Status:



状态：



\*\*Candidate — not finalized\*\*



\*\*候选方向——尚未正式确定\*\*



The topic will only be finalized after literature review, baseline reproduction, and minimal experiments.



最终选题将在系统文献调研、baseline 复现和最小实验验证之后确定。




## 仓库操作入口

[文件管理规范](maintenance/FILE_MANAGEMENT_GUIDE.md)；[本轮审计](maintenance/REPOSITORY_AUDIT.md)。

## 2026-10-30 学习状态与后续编号

| 编号 | 论文 | 学习状态 | 证据范围 |
| --- | --- | --- | --- |
| P001 | VoD 3+1D Radar | 已有正式笔记及概念宝典；代码复现未证实 | 以笔记、勘误及复现记录为准 |
| P002 | CRN | 第一遍精读已完成；全文开放式理解验收此前通过 | 本次用户明确确认；原始问答、批改与补答仍未完整归档 |
| P002后续 | CRN代码精读、论文复现 | 代码精读未开始；复现未执行 | 不把作者指标当作本项目结果 |
| P003 | R4Det | 待开始 | 只登记规划，不创建正式笔记 |
| P004 | MSSF | 待开始 | 只登记规划，不创建正式笔记 |

第二轮基线报告推荐优先考察MSSF，是技术选型建议；本次用户指定的学习编号为P003=R4Det、P004=MSSF。两者用途不同，保留原审查结论，不冒称已统一为相同顺序。
