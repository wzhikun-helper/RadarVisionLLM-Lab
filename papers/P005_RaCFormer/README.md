# P005｜RaCFormer：正式学习与复现档案

2026-11-04登记。CVPR 2025；角色：Query跨视角融合；主要创新基线候选（用户计划，未证明新颖性）。选择角色是用户计划，不等于已验证创新或已完成工程基线。

## 当前状态

沿用原RaCFormer Abstract已讲授状态；开放题待答、未验收。第一遍均无本轮新通过记录；第二遍代码精读未开始；实验未执行。硬件计划RTX 3090 24GB、2–3TB，服务器完整配置未知。

| 编号职责 | 唯一入口 / 当前状态 |
| --- | --- |
| `01_paper_review.md` | [精读](../../paper_notes/P003_RaCFormer.md)；保留旧P003物理路径，新增编号说明，原正文保留 |
| `02_concept_handbook.md` | [概念宝典](../../paper_notes/P005_概念查询宝典.md)；待核实 |
| `03_research_gaps.md` / `04_innovation_notes.md` | [候选问题状态](../../docs/innovation_bank/P003_P005_RESEARCH_QUESTIONS.md)；无已验证候选，不自动建CSV |
| `05_reading_log.md` / `06_questions_and_feedback.md` | [日志、原始问答与验收](../../docs/research_log/P005_RaCFormer_READING_LOG.md) |
| `07_reproducibility_audit.md` | [四阶段学习/复现计划](../../reproductions/P005_RaCFormer/README.md)；工程审查未完成 |
| `08_figure_index.md` / `assets/` | 未引入新图；图号、页码、来源和解释随真实学习登记到精读，不造空白图片成果 |
| 实验跟踪 | [8列跟踪表](../../reproductions/P005_RaCFormer/experiment_tracker.csv)，0次运行 |
| 登记与状态 | [36列主矩阵](../paper_matrix.csv)；[研究状态](../../docs/maintenance/RESEARCH_STATUS.json) |

## 学习顺序与每节同步

Abstract → Introduction → Methodology → Experiments → Related Work → Conclusion；按[同步规范](../../docs/research_log/P003_P005_SECTION_SYNC.md)同时维护精读、概念、研究问题和日志。没有真实原题/回答/批改/教师通过证据，不推进为通过。

原RaCFormer Step 1对应Abstract；Step 2对应Introduction；Step 3对应Methodology；Step 4对应Experiments；原稿没有独立Related Work槽位，后续按真实授课追加；原Step 5是整篇验收，不冒充Conclusion。旧稿不重排或改写。

[论文](https://arxiv.org/abs/2412.12725v2) · [官方代码](https://github.com/cxmomo/RaCFormer) · [模板映射与编号记录](../../docs/maintenance/P003_P005_TEMPLATE_MAPPING_20261104.md)
