# 文献登记

- [paper_matrix.csv](paper_matrix.csv)：36列主矩阵，登记论文属性、方法、学习状态与项目关系。
- [正式笔记入口](../paper_notes/README.md)：逐篇精读与概念宝典。

## 登记规则

1. 每篇论文使用唯一ID；当前P001为VoD，P002为CRN；P003为CenterFusion、P004为RCBEVDet、P005为RaCFormer；历史R4Det使用H-R4Det-2026。
2. 以正式论文和作者来源为准；尚未核查的字段留空，不推测指标、开源状态或复现难度。
3. P001/P002统一使用主矩阵；导入信息须先按字段映射核对。
4. 阅读状态、代码精读和模型复现分别记录。作者报告的结果不填作本项目结果。
5. 论文PDF、数据和权重不在此目录批量存放；外部资源遵循其原始访问与使用条件。

修改主表后，核对36列结构、ID唯一性与笔记入口；不要将研究设想写成论文已有贡献。

## P002 CRN详细登记

主矩阵已有唯一P002行，已按用户提供的正式论文核对全部36列。[CRN登记说明](P002_CRN_RECORD.md)列出逐字段依据、论文页/节/图表、作者报告指标及未核实边界。P001独立导入表已移除；两篇统一使用主矩阵登记。

## 统一论文独立档案

- [P001：VoD / PointPillars](P001_PointPillars_VoD/README.md)
- [P002：CRN](P002_CRN/README.md)

两者采用相同编号槽位链接唯一正式来源，当前不物理迁移。整改证据与缺口见[第一轮对照报告](../docs/maintenance/P001_P002_DOSSIER_ROUND1.md)。

## 旧编号登记（2026-11-03历史）

- [原P003：RaCFormer历史入口](P003_RaCFormer/README.md)：现为P005；原Abstract状态保留。
- [H-R4Det-2026：R4Det](H-R4Det-2026/README.md)：暂停第一遍精读，第一课未验收。原始资料从Git历史恢复保留，旧编号不再用于当前登记。
- [编号调整与证据记录](../docs/maintenance/P003_REGISTRATION_20261103.md)。

## 当前正式编号（2026-11-04）

- [P003：CenterFusion](P003_CenterFusion/README.md)：Lesson 01 Title & Abstract PASS；Lesson 02 Introduction NOT_STARTED。
- [P004：RCBEVDet](P004_RCBEVDet/README.md)：尚未开始；只初始化计划与待核实入口。
- [P005：RaCFormer](P005_RaCFormer/README.md)：沿用原RaCFormer Abstract已讲授状态；开放题待答、未验收。

[模板与编号映射](../docs/maintenance/P003_P005_TEMPLATE_MAPPING_20261104.md)。
