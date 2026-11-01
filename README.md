# RadarVisionLLM-Lab

面向 **4D Radar + Camera Fusion + VLM** 的个人科研工作仓库，连接论文学习、可追溯研究问题、基线审查与可复现实验。当前以文献学习和工程准备为主，尚无本项目模型训练、评估或成功复现结果。

## 研究目标与问题

从2026年10月13日起，争取在六个月内形成至少一项可复现、有证据支撑的研究成果，优先CCF-C、争取CCF-B；既有2027年4月13日目标作为计划约束，不是成果保证。当前候选问题围绕稀疏雷达的几何证据质量、雷视对象对应与融合失效诊断；VLM是否必要仍需对照证据。

[论文档案](papers/README.md) · [文献矩阵](papers/paper_matrix.csv) · [科研工作流](docs/RESEARCH_WORKFLOW.md) · [目录职责](docs/maintenance/REPOSITORY_GUIDE.md)

## 当前论文进度

以下摘要来自[唯一当前状态源](docs/maintenance/RESEARCH_STATUS.json)，由检查脚本核对；历史审计不覆盖为当前进度。

<!-- BEGIN RESEARCH STATUS -->
| 编号 / 论文 | 阅读状态 | 验收证据 | 工程状态 |
| --- | --- | --- | --- |
| [P001 · VoD + PointPillars](papers/P001_PointPillars_VoD/README.md) | 精读完成 | Evidence Missing：教师原始结论/题答待补 | 代码学习证据未完整核实；模型复现Not Run |
| [P002 · CRN](papers/P002_CRN/README.md) | 第一遍完成；用户确认此前理解验收通过 | Evidence Missing：原题答/批改原文待补 | 代码精读Not Started；复现Not Run / Deferred |
| [P003 · R4Det](papers/P003_R4Det/README.md) | Pre-readiness；第一遍Not Started | Not Started | 第二遍Not Started；最小复现未准入 |
| [P004 · MSSF](papers/README.md) | 两遍均Not Started | Not Started | 阅读编号与工程候选排序独立 |
<!-- END RESEARCH STATUS -->

P001/P002分别保留唯一正式精读、概念宝典及原图。已建立十项独立入口及十二类档案对齐，不以文件存在认定证据齐全；原题答、部分教学图来源仍待补。P001数值勘误和P002创新查新见各自独立入口。

## 基线候选与复现

MSSF-PP/VoD是[第二轮审查](docs/research_gaps/baseline_selection_round2/05_decision_and_plan.md)的重点核查候选，SGDet3D等为其他候选；均不能称已部署或复现。论文编号表示阅读安排，不是基线优先级。

[复现记录规范](reproductions/RECORDING_STANDARD.md)区分Paper-reported、Static Check、Environment Check、Forward Pass、Evaluation、Reproduced和Blocked。作者指标与本项目输出分开登记。

## 目录导航

| 目录 | 用途 |
| --- | --- |
| [paper_notes/](paper_notes/) | 唯一正式笔记、概念、原图与论文模板 |
| [papers/](papers/) | 文献矩阵、逐篇档案入口与P003准备清单 |
| [docs/](docs/) | Research Gap、创新、日志、规范与维护证据 |
| [figures/](figures/) | 图表来源、用途与原图引用索引 |
| [reproductions/](reproductions/) | 工程可行性、准入与真实运行证据索引 |
| [data/](data/) | 来源/许可/版本登记；真实数据不提交 |
| [experiments/](experiments/) | 配置与唯一实验记录模板 |
| [results/](results/) | 真实输出及分析入口，当前无模型结果 |
| [src/](src/) · [scripts/](scripts/) | 研究实现与维护检查分开 |
| [writing/](writing/) · [manuscript/](manuscript/) | 表达积累与论文写作材料 |
| [历史与本地资料职责](docs/maintenance/REPOSITORY_GUIDE.md) | presentations/work/archive继续保留原资料，不因目录名称删除 |

## 工作流与近期任务

遵循用户既有两遍阅读法：教师讲解与验收、用户亲自理解回答、Codex按授权整理/执行。未取得教师验收不自动通过，不因论文读完就安装或训练。原《第四次学习规划》尚未在仓库定位，等待原文建立引用；不以本次规范替代它。

近期先补原问答/批改与教学图来源，教师审查候选处置及P003版本；工程侧先补数据许可、权重/配置、服务器与评估协议证据。P003正式精读、第二遍和模型执行均等待明确授权。

## 证据与可复现性

正式笔记/原图/失败记录长期保留。论文事实、代码事实、静态核查、外部复现、本项目实测与假设分别标识；没有run、日志和协议就不填成功指标。复用[现有实验模板](experiments/templates/experiment_template.md)，不复制空模板覆盖正式档案。

公开克隆的文档/配置/安全检查：

```powershell
python -B scripts/validate_lab.py --scope tracked
```

完整本地资产与历史SHA检查（需原维护资料及pypdf）：

```powershell
python -B scripts/validate_lab.py
```

两种范围分别报告；脚本通过不代表模型可运行、科学结论成立或教师验收通过。工具说明见[治理方案](docs/maintenance/REPOSITORY_PLAN_2026-11-01.md)。

## 文档与历史

[仓库审计](docs/maintenance/REPOSITORY_AUDIT_2026-11-01.md) · [变更报告](docs/maintenance/REPOSITORY_CHANGE_REPORT_2026-11-01.md) · [旧首页原文](docs/maintenance/history/README_BEFORE_2026-11-01.md) · [既有文件管理规范](docs/maintenance/FILE_MANAGEMENT_GUIDE.md)。

旧首页及历史初始化里程碑保留当时语境，首页不再嵌套多份完整README。原工作区未提交资料未自动纳入本次发布。
