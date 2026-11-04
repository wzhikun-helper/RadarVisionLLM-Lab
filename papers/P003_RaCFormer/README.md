> 历史编号入口（2026-11-04）：RaCFormer当前正式编号为[P005](../P005_RaCFormer/README.md)。本目录与下方原文保留旧编号语境，当前P003为[CenterFusion](../P003_CenterFusion/README.md)。不以旧硬件/编号作为当前计划。

# P003｜RaCFormer：统一论文档案

正式登记：2026-11-03（Asia/Shanghai）。RaCFormer，CVPR 2025。取代当前学习序号中的R4Det；[R4Det历史档案](../H-R4Det-2026/README.md)保留。

## 当前学习状态

Abstract已讲授（本次用户提供状态）；**等待用户开放题回答，未批改、未验收通过**。未提供本课教学/题答原文，不补造。其余第一遍章节尚未登记完成；代码精读未开始；模型运行、训练、评估与复现均未执行。

## 统一编号职责

| 编号槽位 | 正式入口或状态 |
| --- | --- |
| `01_paper_review.md` | [唯一正式精读笔记](../../paper_notes/P003_RaCFormer.md)，学习总览与Step进度 |
| `02_concept_handbook.md` | [术语解释入口](../../paper_notes/P003_RaCFormer.md#术语解释)，当前待学习，未单独复制笔记 |
| `03_research_gaps.md` | 尚未开展，不提前生成研究结论 |
| `04_innovation_notes.md` | 尚未开展，不宣称创新 |
| `05_reading_log.md` | [学习总览](../../paper_notes/P003_RaCFormer.md#学习总览)，只登记本次用户提供状态 |
| `06_questions_and_feedback.md` | [开放问答、教师批改与验收](../../paper_notes/P003_RaCFormer.md#开放问答教师批改与验收)，原文待提供 |
| `07_reproducibility_audit.md` | 下列资源登记仅为范围约束，未完成代码审查或工程准入 |
| `08_figure_index.md` | [图表记录](../../paper_notes/P003_RaCFormer.md#图表记录)，尚未引入图片 |
| `ideas.csv` | 未创建，当前无正式创新候选 |
| `assets/` | 尚无新增图片，不复制P001/P002图片 |

## 固定学习与工程范围

- [论文 arXiv:2412.12725v2](https://arxiv.org/abs/2412.12725v2)：2025-03-24修订；[CVPR正式论文入口](https://openaccess.thecvf.com/content/CVPR2025/html/Chu_RaCFormer_Towards_High-Quality_3D_Object_Detection_via_Query-based_Radar-Camera_Fusion_CVPR_2025_paper.html)。图表和页码须按实际阅读版本登记，不混用。
- [官方代码固定commit](https://github.com/cxmomo/RaCFormer/tree/4d4c534f84acef9ec390523134367aad40619057)：`4d4c534f84acef9ec390523134367aad40619057`。
- 主数据集：nuScenes；目标模型：RaCFormer-R50（用户指定）。官方固定README列出`configs/racformer_r50_nuimg_704x256_f8.py`；本轮仅读README，未检查完整代码、数据、权重或环境闭环。
- 实验GPU目标：RTX 4090 D 24GB（用户指定，尚未验证运行）；无服务器实测输出，不沿用R4Det旧硬件，不据型号判断可训练。
- 本项目实际实验结果：无。官方README训练示例为8 GPU，不据此认定单卡训练可行。暂不授予环境安装、数据/权重下载、训练或评估准入。

[论文矩阵](../paper_matrix.csv) · [当前研究状态](../../docs/maintenance/RESEARCH_STATUS.json) · [编号调整记录](../../docs/maintenance/P003_REGISTRATION_20261103.md)
