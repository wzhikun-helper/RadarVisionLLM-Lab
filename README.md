# RadarVisionLLM-Lab

**Radar-Camera Fusion and Vision-Language Model Research Project**
**雷达-视觉融合与视觉语言大模型长期科研项目**

## 1. Research Goal / 研究目标

This repository records the complete research process from beginner-level learning to independent research in radar-camera fusion and multimodal large models.

本仓库用于完整记录从初学者入门，到能够独立开展雷视融合与多模态大模型研究的全过程。

### Short-term Goal / 短期目标

Complete a solid research project with the quality required for an appropriate **CCF-C-level publication**.

完成一项完整、规范、具有明确创新和充分实验支撑的研究工作，并以合适的 **CCF-C 级别论文**作为阶段性目标。

### Long-term Goal / 长期目标

Develop independent research ability and gradually explore research problems with the depth required for **CCF-B-level work**.

逐步形成独立科研能力，包括论文调研、问题发现、代码复现、方法设计、实验分析和论文写作，并逐渐探索具有 **CCF-B 深度**的问题。

---

## 2. Main Research Direction / 主要研究方向

**Radar-Camera Fusion + Vision-Language Models**

**雷达-相机融合 + 视觉语言模型**

Current preliminary research question:

当前初步研究问题：

> Can physical measurements from radar, such as range and Doppler velocity, improve the reliability of VLM motion reasoning under visual degradation?

> 在夜间、模糊、遮挡等视觉退化环境中，能否利用雷达提供的距离和多普勒速度等物理测量信息，提高视觉语言模型运动推理的可靠性？

This is only a preliminary hypothesis and may change after literature review, reproduction, and experiments.

该问题目前只是 **Research Hypothesis v0.1**，后续将根据论文调研、开源项目复现和实验结果持续调整，不预先锁死研究题目。

---

## 3. Research Principles / 科研原则

1. **Problem-driven research rather than module-driven research.**
   以问题驱动科研，而不是为了加入某个网络模块而寻找问题。

2. **Reproduce strong baselines before proposing new methods.**
   在提出新方法之前，优先复现有代表性的强基线。

3. **Every important experiment must be reproducible.**
   每个重要实验必须能够复现。

4. **Every result should be traceable to code, configuration, data split, and Git commit.**
   每个实验结果都应能够追溯到代码版本、配置、数据划分和 Git commit。

5. **Research ideas must be supported by literature evidence.**
   创新点必须由系统性的文献证据支撑，不能只凭感觉。

6. **Failed experiments and rejected ideas should also be recorded.**
   失败实验和被淘汰的 Idea 同样需要记录，因为它们也是科研过程的一部分。

7. **Figures, tables, notes, code, and manuscripts should be systematically organized.**
   图表、笔记、代码、实验结果和论文稿件都应进行工程化管理。

8. **Understand before modifying.**
   修改开源代码之前，应先理解数据输入、核心模块、输出以及设计原因。

---

## 4. Repository Structure / 仓库结构

* `docs/` — Research roadmap, learning notes, logs, weekly reports
  科研路线图、学习笔记、科研日志和周报

* `papers/` — Paper collection and Paper Matrix
  论文资料与论文横向比较矩阵

* `paper_notes/` — Detailed paper reading notes
  每篇论文的完整精读与阅读笔记

* `reproductions/` — Reproduction of open-source research projects
  开源论文和项目复现

* `data/` — Dataset documentation, metadata, and splits
  数据集说明、元数据和数据划分

* `src/` — Core research code
  自己编写的核心研究代码

* `experiments/` — Experiment configurations and records
  正式实验配置与实验记录

* `results/` — Experimental results and statistics
  实验结果与统计分析

* `figures/` — Visualizations and paper figures
  数据可视化与论文图片

* `scripts/` — Preprocessing, training, evaluation, and analysis scripts
  数据预处理、训练、测试和分析脚本

* `writing/` — Academic writing notes and Academic Phrasebook
  学术写作训练与 Academic Phrasebook

* `manuscript/` — Paper drafts and submission materials
  论文草稿、图表、参考文献和投稿材料

---

## 5. Research Workflow / 科研流程

```text
Literature Review / 文献调研
        ↓
Paper Matrix / 论文矩阵
        ↓
Core Paper Reading / 核心论文精读
        ↓
Open-source Reproduction / 开源项目复现
        ↓
Failure Case Analysis / 失败案例分析
        ↓
Innovation Bank / 创新点库
        ↓
Minimal Idea Validation / 最小实验验证
        ↓
Method Development / 方法设计与实现
        ↓
Controlled Experiments / 控制变量实验
        ↓
Ablation & Robustness / 消融与鲁棒性实验
        ↓
Figure & Result Analysis / 图表与结果分析
        ↓
Paper Writing / 论文写作
        ↓
Submission / 投稿
```

---

## 6. Current Stage / 当前阶段

**Milestone 0 — Research Engineering Initialization**
**里程碑 0 —— 科研工程初始化**

* [x] Git installed / Git 已安装
* [x] Git repository initialized / Git 仓库已初始化
* [x] Initial repository folders created / 第一版项目目录已创建
* [ ] Bilingual README completed / 中英文 README 完成
* [ ] `.gitignore` completed / `.gitignore` 完成
* [ ] Research protocol completed / 科研规范完成
* [ ] First Git commit / 第一次 Git 提交
* [ ] First learning note / 第一份正式学习笔记

---

## 7. Long-term Research Assets / 长期科研资产

This project will continuously maintain:

本项目将长期维护：

* Paper Matrix / 论文矩阵
* Paper Notes / 论文笔记
* Figure Library / 科研图库
* Limitation Bank / 局限性库
* Innovation Bank / 创新点库
* Academic Phrasebook / 学术表达库
* Reproduction Records / 论文复现记录
* Experiment Records / 实验记录
* Weekly Reports / 科研周报
* Paper Figures / 论文图片
* Manuscripts / 论文稿件

---

## 8. Project Status / 项目状态

Project started in September 2026.

项目于 **2026 年 9 月**正式启动。

The repository will evolve together with the research direction.

仓库结构和研究问题都允许随着科研进展持续迭代。
