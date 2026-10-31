# 第一轮：P001/P002统一论文档案核查

日期：2026-10-31。基线HEAD：`2b879ee6b35597e30f0a7778f48903047cdec211`。本轮仅建立独立逻辑档案，不迁移正文，不改造根README，不清理历史资产，不运行模型。

## 十项整改前后对照

| 类型 | P001实际路径 | P002实际路径 | 整改前 | 整改后 / 动作 | 证据来源与缺口 |
| --- | --- | --- | --- | --- | --- |
| README | [独立入口](../../papers/P001_PointPillars_VoD/README.md) | [独立入口](../../papers/P002_CRN/README.md) | 无论文独立目录入口 | 新建对称编号导航 | 正式来源映射见下；内容仍唯一 |
| 正式精读 | [paper_notes/P001_论文精读.md](../../paper_notes/P001_论文精读.md) | [paper_notes/P002_CRN.md](../../paper_notes/P002_CRN.md) | 已有，分散目录 | 纳入相同编号入口，不改写源文件 | 正文、公式、表格原样保留；依据正式笔记及既有来源登记 |
| 概念宝典 | [paper_notes/P001_概念查询宝典.md](../../paper_notes/P001_概念查询宝典.md) | [paper_notes/P002_概念查询宝典.md](../../paper_notes/P002_概念查询宝典.md) | 已有，分散目录 | 纳入相同编号入口，不改写源文件 | 已有正式材料，不重写；依据正式笔记及既有来源登记 |
| Research Gap | [docs/research_gaps/P001_Limitations_Research_Gap.md](../research_gaps/P001_Limitations_Research_Gap.md) | [docs/research_gaps/P002_CRN_Limitations_Research_Gap.md](../research_gaps/P002_CRN_Limitations_Research_Gap.md) | 已有，分散目录 | 纳入相同编号入口，不改写源文件 | 已有；证据、推断、假设分开，实验未执行；依据正式笔记及既有来源登记 |
| 创新记录 | [docs/innovation_bank/P001_INNOVATION_NOTES.md](../innovation_bank/P001_INNOVATION_NOTES.md) | [docs/innovation_bank/P002_CRN_INNOVATION_NOTES.md](../innovation_bank/P002_CRN_INNOVATION_NOTES.md) | 已有，分散目录 | 纳入相同编号入口，不改写源文件 | 已有候选分析，非已验证创新；依据正式笔记及既有来源登记 |
| 阅读日志 | [docs/research_log/P001_READING_REPORT.md](../research_log/P001_READING_REPORT.md) | [docs/research_log/P002_CRN_READING_REPORT.md](../research_log/P002_CRN_READING_REPORT.md) | 已有，分散目录 | 纳入相同编号入口，不改写源文件 | 已有当前日志；历史报告保留；依据正式笔记及既有来源登记 |
| 开放问答与批改 | [docs/research_log/P001_REVIEW.md](../research_log/P001_REVIEW.md) | [docs/research_log/P002_CRN_REVIEW.md](../research_log/P002_CRN_REVIEW.md) | 已有，分散目录 | 纳入相同编号入口，不改写源文件 | 有状态入口；原始问答证据尚未归档；依据正式笔记及既有来源登记 |
| 复现审查 | [reproductions/P001_PointPillars_VoD/README.md](../../reproductions/P001_PointPillars_VoD/README.md) | [reproductions/P002_CRN/README.md](../../reproductions/P002_CRN/README.md) | 已有，分散目录 | 纳入相同编号入口，不改写源文件 | 有计划/可行性；无成功复现证据；依据正式笔记及既有来源登记 |
| 图表索引 | [figures/library/P001/FIGURE_INDEX.md](../../figures/library/P001/FIGURE_INDEX.md) | [figures/library/P002/FIGURE_INDEX.md](../../figures/library/P002/FIGURE_INDEX.md) | 已有，分散目录 | 纳入相同编号入口，不改写源文件 | 已有；未确认的论文图号保留待核实；依据正式笔记及既有来源登记 |
| 创新CSV | [docs/innovation_bank/P001_ideas.csv](../innovation_bank/P001_ideas.csv) | [docs/innovation_bank/P002_ideas.csv](../innovation_bank/P002_ideas.csv) | 已有，分散目录 | 纳入相同编号入口，不改写源文件 | 同10列；P002未评分，不造结果；依据正式笔记及既有来源登记 |

## 迁移依赖审查与取舍

完整本地文件树/哈希、全部匹配P001/P002/CRN文本的完整读取清单，以及Markdown、CSV、JSON、脚本等静态引用命中记录见[本轮状态](P001_P002_DOSSIER_ROUND1_STATE.json)。Git已跟踪路径与历史哈希亦属于路径依赖。本轮静态扫描不能穷尽外部工具或动态访问，未证明物理迁移安全，采用用户允许的索引方式。编号文件名为逻辑槽位，并不宣称这些物理文件已迁移落地。后续确需移动时再修复引用和哈希清单，不覆盖历史证据。

## 设计参考

- [OpenPCDet官方仓库](https://github.com/open-mmlab/OpenPCDet)：借鉴文档、数据、工具和模型实现分工以及模型结果与使用说明分离；不照搬工具箱为个人档案增加空目录。
- [MMDetection3D配置文档](https://mmdetection3d.readthedocs.io/en/latest/user_guides/config.html)：借鉴模块配置、继承与实验设置可追踪理念。现有复现规范已要求记录源码、配置、数据、环境与日志；本轮只链接该规范，不创建虚假配置或运行。

## 内容证据与未解决事项

P002复用正式精读、概念宝典、正式PDF逐字段登记、既有Gap和创新表。正式PDF登记SHA为e833ebf328d1eaecb0536699c9f29a13e36616e4ae0cfd6aa874d762a1f10296；本轮未重新执行独立论文事实审稿。正式论文与预印本附录的来源边界保留。RVT/MFA/MDCA已有设计与候选创新分开，最小方案只是设计，未执行。

P001原内容不重写；历史归档报告不替换。两篇原始问答证据尚未归档，P001教师结论待补；P002用户确认此前通过与原文缺失同时登记。七张P002图片已有笔记位置与用途，论文原图编号尚待逐图确认。两篇无本项目成功复现证据；P002代码精读未开始。P003/P004均未开始。

## 验证与变更范围

执行结果、退出码、哈希比对、Markdown/Obsidian目标检查及CSV只读结构检查见本轮状态JSON。仅新增两个独立README、本报告和状态JSON，更新papers/README导航及原维护状态中新增P002入口登记；不关闭任何验证规则。原工作区每个文件保持字节不变，唯一预期例外为papers/README和维护状态文件的本轮增量。

**交付状态：结构入口已对齐，历史证据仍有缺口；等待教师核查，不自行宣告全部通过。**
