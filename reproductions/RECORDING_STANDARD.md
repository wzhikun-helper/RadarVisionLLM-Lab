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
