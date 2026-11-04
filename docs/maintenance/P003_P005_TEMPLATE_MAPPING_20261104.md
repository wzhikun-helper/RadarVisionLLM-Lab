# P003–P005｜P001模板映射与初始化证据

日期：2026-11-04（Asia/Shanghai）。当前修改只位于独立worktree的`research/p003-p005-reading-reproduction-20261103`分支；起点`fee22e100e4e7771ab4366182883c052fa862877`。原main工作区已有24个修改文件与4个未跟踪文件，原暂存区为空，未复制这些未提交内容到独立分支。

## 实际目录与模板映射

| 核查对象 | 真实路径 / 组织 | 本轮沿用方式 |
| --- | --- | --- |
| P001精读 | [唯一精读](../../paper_notes/P001_论文精读.md)：学习总览，Step 1–8，公式、表格、标准Markdown图片和证据边界 | 新笔记使用学习总览与Step；按用户当前阅读顺序组织，不复制学术结论 |
| P001概念宝库 | [概念查询宝典](../../paper_notes/P001_概念查询宝典.md)：分部分、编号概念，基本定义唯一 | 继续paper_notes/编号_概念查询宝典.md；不新建不兼容宝库目录 |
| 学习笔记目录 | docs/learning_notes/当前只有[Git与科研工程笔记](../learning_notes/00_git_and_research_engineering.md) | 这是通用学习目录，不冒认论文概念宝库；不重构或移动 |
| 概念索引 | P001宝典以分组标题和编号检索；P002有[独立宝典](../../paper_notes/P002_概念查询宝典.md)，没有另一个概念目录 | 新宝典建立原定义索引，已有概念链接并补应用，新概念独立条目 |
| 验收日志 | [P001学习报告](../research_log/P001_READING_REPORT.md)、[P001验收](../research_log/P001_REVIEW.md) | 保留真实状态与历史证据缺口；新篇用逐节原题、真回答、批改、补答、验收字段 |
| 研究与复现 | docs/innovation_bank、reproductions、[已有规范](../../reproductions/RECORDING_STANDARD.md) | 有研究价值才建候选，8列实验表零运行；不抄结论或伪造运行 |
| GitHub方式 | 本地Git文档为正式来源，标准相对链接，原项目已有普通commit/push记录 | 本次在用户指定独立分支只提交明确文件；普通推送并核对远程SHA，不发布到main |

本轮程序读取上述P001/P002笔记全文并核对标题/条目；模板映射不等于重新审查全部学术内容，也不替代P001教师验收。P001/P002文件字节均不改写。

## 当前编号和保留策略

| 当前编号 | 正式精读 / 正式档案 | 旧编号与保留 |
| --- | --- | --- |
| P003 CenterFusion | [精读](../../paper_notes/P003_CenterFusion.md)；[入口](../../papers/P003_CenterFusion/README.md) | 新草稿；Abstract已讲授，三题待验收 |
| P004 RCBEVDet | [精读](../../paper_notes/P004_RCBEVDet.md)；[入口](../../papers/P004_RCBEVDet/README.md) | 新计划，学习未开始；不沿用旧候选MSSF编号 |
| P005 RaCFormer | [唯一精读保留旧路径](../../paper_notes/P003_RaCFormer.md)；[当前入口](../../papers/P005_RaCFormer/README.md) | 旧P003原稿正文逐字节保留，仅增加当前编号/硬件说明，不物理移动、不复制第二份正式精读 |
| H-R4Det-2026 | [历史入口](../../papers/H-R4Det-2026/README.md) | 暂停第一遍精读，第一课未验收；两份原始报告不变 |

RaCFormer旧路径和历史报告里的P003=RaCFormer、R4Det早期资料里的P003=R4Det、旧P004=MSSF均按当时语境保留。当前矩阵与RESEARCH_STATUS为当前登记，不能批量替换历史原文。治理分支未合并，不拷贝其旧编号状态。

## 已建立的草稿与事实边界

CenterFusion三道原题和用户回答均未提供，日志只保存Q1–Q3待补槽位；不编题、不代答、不批改、不标通过。两条概念为待核实应用草稿，包含八类字段，不将它们计作已掌握概念。RCBEVDet与RaCFormer宝典本次0个新概念。科研候选0项，无创新评分；实验运行0次。

硬件改记用户最新计划RTX 3090 24GB、2–3TB；不是服务器实测。旧4090 D、3060与3090旧配额描述保留在明确历史语境，不作为当前环境证据。授课时间和学习时长未知，维护日期不冒充授课日期。

外部证据：[CenterFusion元信息/摘要](https://arxiv.org/abs/2011.04841v1)、[官方代码](https://github.com/mrnabati/CenterFusion)、[RCBEVDet元信息](https://arxiv.org/abs/2403.16440v1)、[官方发布入口](https://github.com/VDIGPKU/RCBEVDet)、[RaCFormer固定版本](https://github.com/cxmomo/RaCFormer/tree/4d4c534f84acef9ec390523134367aad40619057)。仅读元信息、摘要/README与发布列表；未核全文公式/图表、未下载ZIP或权重、未执行代码。CVF CenterFusion页面本轮403，RCBEVDet尝试的CVF页面未能读取，未作为正文证据。

## 验证与交付

验证结果见[本轮检查记录](P003_P005_INITIALIZATION_CHECKS_20261104.json)，其中明确区分执行范围与未执行项目。Git提交/推送结果在交付时提供，不预填尚未产生的SHA。

## 本轮文件清单

- `docs/research_log/P003_P005_SECTION_SYNC.md`
- `paper_notes/P003_CenterFusion.md`
- `paper_notes/P003_概念查询宝典.md`
- `docs/research_log/P003_CenterFusion_READING_LOG.md`
- `reproductions/P003_CenterFusion/README.md`
- `reproductions/P003_CenterFusion/experiment_tracker.csv`
- `papers/P003_CenterFusion/README.md`
- `paper_notes/P004_RCBEVDet.md`
- `paper_notes/P004_概念查询宝典.md`
- `docs/research_log/P004_RCBEVDet_READING_LOG.md`
- `reproductions/P004_RCBEVDet/README.md`
- `reproductions/P004_RCBEVDet/experiment_tracker.csv`
- `papers/P004_RCBEVDet/README.md`
- `paper_notes/P003_RaCFormer.md`
- `paper_notes/P005_概念查询宝典.md`
- `docs/research_log/P005_RaCFormer_READING_LOG.md`
- `reproductions/P005_RaCFormer/README.md`
- `reproductions/P005_RaCFormer/experiment_tracker.csv`
- `papers/P005_RaCFormer/README.md`
- `docs/innovation_bank/P003_P005_RESEARCH_QUESTIONS.md`
- `papers/P003_RaCFormer/README.md`
- `papers/H-R4Det-2026/README.md`
- `papers/paper_matrix.csv`
- `docs/maintenance/RESEARCH_STATUS.json`
- `README.md`
- `paper_notes/README.md`
- `papers/README.md`
- `docs/maintenance/P003_P005_TEMPLATE_MAPPING_20261104.md`
- `docs/maintenance/P003_P005_INITIALIZATION_CHECKS_20261104.json`

<!-- FILE_LIST_COMPLETE -->
