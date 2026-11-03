# RadarVisionLLM-Lab

## 1. 项目简介与研究目标

围绕Radar–Camera三维感知建立可追溯的论文学习、研究假设、复现和实验资料体系，以可复现代码与充分实验支持论文写作。VLM关联目前仍是候选研究方向，没有以学习记录冒充新方法或实验成果。

## 2. 当前科研进度

P001与P002已有正式精读、概念宝典和研究配套；本轮补齐对称的学习日志和验收状态入口。尚无本项目成功模型复现或训练/评估结果。文件/导航完整性与科研证据完整性分别记录。

## 3. 当前论文进度

| 编号 | 论文 | 学习状态 | 工程状态 |
| --- | --- | --- | --- |
| P001 | VoD + PointPillars，RA-L 2022 | 精读完成；教师验收原文待补 | Planned；复现未证实 |
| P002 | CRN，ICCV 2023 | 第一遍完成；教师此前确认通过，原问答缺口保留 | 代码精读未开始；复现未执行，暂不优先 |
| P003 | [RaCFormer，CVPR 2025](papers/P003_RaCFormer/README.md) | Abstract已讲授；等待用户开放题回答，未通过验收 | RaCFormer-R50 / nuScenes；RTX 4090 D 24GB为目标资源，尚未验证运行 |

R4Det现以[H-R4Det-2026](papers/H-R4Det-2026/README.md)保留：暂停第一遍精读，第一课未验收。当前状态见[研究状态登记](docs/maintenance/RESEARCH_STATUS.json)。

## 4. P001/P002完整科研档案

- [P001十二类档案入口](paper_notes/README.md#p001)
- [P002十二类档案入口](paper_notes/README.md#p002)
- [逐项对齐矩阵与剩余缺口](docs/maintenance/P001_P002_PARITY_MATRIX.md)
- [论文信息主矩阵](papers/paper_matrix.csv)与[CRN详细登记](papers/P002_CRN_RECORD.md)

## 5. 工程基线与复现状态

[第二轮基线调查](docs/research_gaps/baseline_selection_round2/05_decision_and_plan.md)仅保留历史比较证据；当前P003学习论文为RaCFormer；尚不指定长期主基线。该技术建议仅为历史候选意见，不构成模型执行准入。P001有计划、P002暂缓，均不能写成已经跑通。

[P001工程档案](reproductions/P001_PointPillars_VoD/README.md) · [P002工程档案](reproductions/P002_CRN/README.md) · [统一字段与状态](reproductions/RECORDING_STANDARD.md)。

## 6. 研究路线与近期任务

先补齐可取得的真实验收原始记录、复核候选问题与已有工作的重合，再按学习安排进入后续论文；模型执行另行经过资源、许可、环境及明确授权准入。不自动启动后续论文，不安装、下载数据/权重或运行模型。

[研究路线](docs/roadmap.md)中的初始化里程碑属于历史阶段，当前不是项目初始化状态；后续计划以本页及最新基线审查为当前入口，不改写原阶段记录。

## 7. 目录职责

| 目录 | 内容 |
| --- | --- |
| paper_notes/ | 唯一正式笔记、概念宝典、分组图片与档案模板 |
| papers/ | 论文矩阵、元信息及字段证据 |
| docs/research_gaps/、innovation_bank/ | 证据分层的研究问题与候选想法 |
| docs/research_log/ | 学习报告、原问答与验收状态 |
| figures/library/ | 图表索引，复用原有配图 |
| reproductions/、experiments/ | 工程可行性、配置和真实运行记录规范 |
| src/、results/ | 后续研究代码与结果位置，当前不宣称已有模型成果 |
| docs/maintenance/ | 哈希、审计、历史与缺口记录 |

## 8. 科研规范

论文明确证据、基于证据的推断、待验证假设分开；作者指标与本项目实测分开。无原问答不补造答案，无运行不填结果；不同论文不要求相同图片和实验数量，但十二类都必须有文件或明确入口。

[统一档案检查模板](paper_notes/templates/paper_archive_checklist.md) · [科研规范](docs/research_protocol.md)。统一档案结构检查：`python -B scripts/validate_lab.py`；检查不再依赖P001专用历史清单和ZIP。

## 9. 历史与维护入口

P001原历史归档报告（旧路径 `docs/research_log/P001_ARCHIVE_REPORT.md` 已按用户要求移除）与[CRN此前审计](docs/maintenance/CRN_FIRST_PASS_AUDIT.md)保留当时语境，不替代当前学习状态。历史课件、work、archive已于2026-11-02按用户要求删除；旧报告中的“待合并”等表述不应被当作当前状态。

[文件管理规范](docs/maintenance/FILE_MANAGEMENT_GUIDE.md) · [本轮维护状态](docs/maintenance/P001_P002_PARITY_STATE.json)。

<details>
<summary>此前首页/索引（历史快照，不代表当前进度）</summary>

````markdown
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

## 仓库操作入口

[文件管理规范](docs/maintenance/FILE_MANAGEMENT_GUIDE.md)；[本轮审计](docs/maintenance/REPOSITORY_AUDIT.md)。

## 2026-10-30 学习状态与后续编号

| 编号 | 论文 | 学习状态 | 证据范围 |
| --- | --- | --- | --- |
| P001 | VoD 3+1D Radar | 已有正式笔记及概念宝典；代码复现未证实 | 以笔记、勘误及复现记录为准 |
| P002 | CRN | 第一遍精读已完成；全文开放式理解验收此前通过 | 本次用户明确确认；原始问答、批改与补答仍未完整归档 |
| P002后续 | CRN代码精读、论文复现 | 代码精读未开始；复现未执行 | 不把作者指标当作本项目结果 |

后续论文的预定安排已撤下，待用户决定后再登记。既有基线比较是历史技术调查，不代表当前选定的学习对象。

````

</details>
