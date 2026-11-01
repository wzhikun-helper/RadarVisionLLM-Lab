# 统一复现档案与实验记录规范

适用于P001/P002及后续论文。档案有入口不等于已经运行模型。

## 档案字段

每篇对应复现README至少登记论文/代码来源及核查范围、固定源码SHA状态、数据/版本/划分/许可、配置、权重、环境及算子、硬件、当前阶段、工程优先级/原因、下一步准入条件、实际运行证据路径。未核查即写未核查，不凭作者README认定可运行。

## 统一状态

| 状态 | 依据 |
| --- | --- |
| Not Started | 尚无工程执行，允许保留可行性说明 |
| Planned | 有计划，尚未开始执行 |
| Deferred | 已说明暂缓原因，尚不优先进入工程 |
| Environment Setup | 有实际环境命令与依赖/算子日志 |
| Running | 有真实run_id、命令及运行日志 |
| Partial Reproduction | 有实际指标及未复现/协议差异说明 |
| Verified | 在明确数据/配置/评价容差下完成核验 |
| Reproducible | 新环境或独立重复运行成功，有证据 |

第一遍阅读、教师理解验收、代码精读与上述工程状态独立。P001为Planned且未证实复现；P002为Deferred / Not Started，代码精读未开始，未执行任何模型运行、训练或评估。

## CSV与详细运行记录

P001/P002实验表统一8列：`experiment_id,config,seed,data_split,environment,metric,status,notes`。字段相同不要求记录数相同：P001保留原有Planned占位行；P002保持0条运行记录。Planned行没有metric不等于实验失败，也不是成功证据。

每个真实run通过config/environment/notes关联Git commit、数据版本与划分、随机种子、硬件和依赖、完整命令、日志、指标文件、成功判据与异常。作者论文目标指标另列于README，不能填作本项目实测metric。没有运行就不建立虚构运行行。

使用[现有记录模板](templates/reproduction_template.md)，状态推进须由真实证据驱动。本轮只规范档案，不安装、不下载数据/权重、不运行模型。

## 2026-11-01：证据阶段与完整执行字段

工作流状态（Not Started、Planned、Running、Blocked等）与证据阶段分开记录；Blocked保留最后实际达到的阶段和阻塞原因，不能把中断改成成功。

| 证据阶段 | 必需依据 |
| --- | --- |
| Paper-reported | 原论文版本、页/表/设置；不是本项目指标 |
| Static Check | 固定源码与配置的只读检查、文件路径/哈希；没有运行保证 |
| Environment Check | 真实系统/依赖/算子检查命令、退出码和日志 |
| Forward Pass | 固定样本/配置/权重的真实前向命令、输出与日志 |
| Evaluation | 固定数据/划分/评估协议的真实指标原始输出 |
| Reproduced | 预先约定成功判据、协议差异及重复运行证据，不能仅凭前向或单次数字 |
| Blocked（状态） | 阻塞原因、已有证据阶段、缺项和下一步，不伪填模型指标 |

复用现有实验/复现模板，8列tracker不改结构；详细字段通过config/environment/notes关联单一run：

| 字段组 | 必须记录 |
| --- | --- |
| 身份与来源 | paper/baseline、官方URL、源代码commit SHA、代码/数据/权重许可证及核查状态 |
| 环境硬件 | OS/Python/依赖锁定、驱动/CUDA/自定义算子、CPU/GPU/实际显存与分配配额；本机和服务器分开 |
| 数据 | 数据集/版本、train/val/test清单与校验、预处理实现/参数/输出SHA |
| 配置权重 | 配置原路径及哈希、初始化/最终权重来源、版本/校验、加载差异 |
| 执行 | 唯一experiment_id/run_id、完整命令、cwd、种子、开始结束时间、退出码、真实stdout/stderr路径 |
| 评价结果 | 评估实现commit/协议、原始日志与指标JSON、结果/图表路径、每个指标的来源层级 |
| 结论与失败 | 论文目标与本项目实测分栏、预定容差/成功标准、失败/阻塞、重跑证据与下一步 |

模板存在不算run；不得将作者、外部研究者和本项目指标混写。详见[长期工作流](../docs/RESEARCH_WORKFLOW.md)。本轮仅整理规范，无模型安装/运行。
