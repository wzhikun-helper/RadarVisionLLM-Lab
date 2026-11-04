# P001 / P002 科研档案导航

按相同十二类职责维护；文件存在不代表所有阶段完成。正式笔记只保留原文件，以下均为相对链接。当前P003为CenterFusion、P004为RCBEVDet、P005为RaCFormer；R4Det以H-R4Det-2026保留。

## P003–P005｜当前学习入口

| 编号 | 精读 | 概念宝典 | 状态 |
| --- | --- | --- | --- |
| P003 CenterFusion | [精读](P003_CenterFusion.md) | [宝典](P003_概念查询宝典.md) | Lesson 01 PASS（首轮Q1未过、补学通过）；Lesson 02未开始 |
| P004 RCBEVDet | [草稿](P004_RCBEVDet.md) | [宝典](P004_概念查询宝典.md) | 尚未开始 |
| P005 RaCFormer | [唯一正文，保留旧路径](P003_RaCFormer.md) | [宝典](P005_概念查询宝典.md) | 原Abstract状态保留，待答未验收 |

每节真实验收后执行[同步规范](../docs/research_log/P003_P005_SECTION_SYNC.md)。不存在独立概念宝库目录，继续使用paper_notes下的编号宝典。

[H-R4Det-2026历史入口](../papers/H-R4Det-2026/README.md)：暂停第一遍精读，第一课未验收；原始准备资料保留，旧P003称谓仅属历史。

## P001

| 档案类型 | 当前入口 |
| --- | --- |
| 正式精读笔记 | [P001_论文精读.md](../paper_notes/P001_论文精读.md) |
| 概念查询宝典 | [P001_概念查询宝典.md](../paper_notes/P001_概念查询宝典.md) |
| 正式笔记图片 | [P001](../paper_notes/assets/P001/) |
| 论文图表索引 | [FIGURE_INDEX.md](../figures/library/P001/FIGURE_INDEX.md) |
| Research Gap | [P001_Limitations_Research_Gap.md](../docs/research_gaps/P001_Limitations_Research_Gap.md) |
| 创新分析 | [P001_INNOVATION_NOTES.md](../docs/innovation_bank/P001_INNOVATION_NOTES.md) |
| 创新想法CSV | [P001_ideas.csv](../docs/innovation_bank/P001_ideas.csv) |
| 阅读研究日志 | [P001_READING_REPORT.md](../docs/research_log/P001_READING_REPORT.md) |
| 开放式问答与教师验收 | [P001_REVIEW.md](../docs/research_log/P001_REVIEW.md) |
| 复现计划及可行性 | [README.md](../reproductions/P001_PointPillars_VoD/README.md) |
| 实验跟踪表 | [experiment_tracker.csv](../reproductions/P001_PointPillars_VoD/experiment_tracker.csv) |
| 论文信息、状态与导航 | [paper_matrix.csv](../papers/paper_matrix.csv) |

## P002

| 档案类型 | 当前入口 |
| --- | --- |
| 正式精读笔记 | [P002_CRN.md](../paper_notes/P002_CRN.md) |
| 概念查询宝典 | [P002_概念查询宝典.md](../paper_notes/P002_概念查询宝典.md) |
| 正式笔记图片 | [P002_CRN](../paper_notes/assets/P002_CRN/) |
| 论文图表索引 | [FIGURE_INDEX.md](../figures/library/P002/FIGURE_INDEX.md) |
| Research Gap | [P002_CRN_Limitations_Research_Gap.md](../docs/research_gaps/P002_CRN_Limitations_Research_Gap.md) |
| 创新分析 | [P002_CRN_INNOVATION_NOTES.md](../docs/innovation_bank/P002_CRN_INNOVATION_NOTES.md) |
| 创新想法CSV | [P002_ideas.csv](../docs/innovation_bank/P002_ideas.csv) |
| 阅读研究日志 | [P002_CRN_READING_REPORT.md](../docs/research_log/P002_CRN_READING_REPORT.md) |
| 开放式问答与教师验收 | [P002_CRN_REVIEW.md](../docs/research_log/P002_CRN_REVIEW.md) |
| 复现计划及可行性 | [README.md](../reproductions/P002_CRN/README.md) |
| 实验跟踪表 | [experiment_tracker.csv](../reproductions/P002_CRN/experiment_tracker.csv) |
| 论文信息、状态与导航 | [paper_matrix.csv](../papers/paper_matrix.csv) |

## 学习与证据状态

P001精读完成，教师全文验收原文待补；P002第一遍完成、教师此前确认通过，原始问答仍缺完整归档。两者模型复现均未证实，P002未进行代码精读/运行。见[12类对齐审计](../docs/maintenance/P001_P002_PARITY_MATRIX.md)。

[统一档案模板](templates/paper_archive_checklist.md) · [复现记录规范](../reproductions/RECORDING_STANDARD.md) · [文件管理规范](../docs/maintenance/FILE_MANAGEMENT_GUIDE.md)。

<details>
<summary>此前首页/索引（历史快照，不代表当前进度）</summary>

````markdown
# 论文笔记索引

- [P001论文精读](P001_论文精读.md)
- [P001概念查询宝典](P001_概念查询宝典.md)
- [P002 CRN精读](P002_CRN.md)
- [P002概念查询宝典](P002_概念查询宝典.md)
- [笔记模板](templates/paper_note_template.md)
- [P001图表索引](../figures/library/P001/FIGURE_INDEX.md)
- [P001勘误（已整合）](../docs/research_gaps/P001_CONTENT_SUPPLEMENT.md)
- [CRN归档证据](../docs/maintenance/CRN_FIRST_PASS_AUDIT.md)

图片分别存放`assets/P001/`与`assets/P002_CRN/`，使用标准Markdown相对路径与URL编码，兼容GitHub及Obsidian。原宽度参数保留在图片标题元数据中；GitHub不承诺按该宽度渲染。仅转换图片引用，正文与公式未改写。

## 2026-10-30 学习状态与后续编号

| 编号 | 论文 | 学习状态 | 证据范围 |
| --- | --- | --- | --- |
| P001 | VoD 3+1D Radar | 已有正式笔记及概念宝典；代码复现未证实 | 以笔记、勘误及复现记录为准 |
| P002 | CRN | 第一遍精读已完成；全文开放式理解验收此前通过 | 本次用户明确确认；原始问答、批改与补答仍未完整归档 |
| P002后续 | CRN代码精读、论文复现 | 代码精读未开始；复现未执行 | 不把作者指标当作本项目结果 |

后续论文的预定安排已撤下，待用户决定后再登记。既有基线比较是历史技术调查，不代表当前选定的学习对象。

## P002研究配套与后续归档标准

- [局限与候选Gap](../docs/research_gaps/P002_CRN_Limitations_Research_Gap.md)
- [候选想法证据链](../docs/innovation_bank/P002_CRN_INNOVATION_NOTES.md)
- [静态复现可行性](../reproductions/P002_CRN/README.md)：非优先工程目标，未运行
- [第一遍阅读日志](../docs/research_log/P002_CRN_READING_REPORT.md)
- [7张配图索引](../figures/library/P002/FIGURE_INDEX.md)
- [P001/P002对照审计](../docs/maintenance/P001_P002_CONSISTENCY_AUDIT.md)
- [单篇归档检查表](templates/paper_archive_checklist.md)：P003/P004未来沿用，当前不创建其正式笔记

````

</details>
