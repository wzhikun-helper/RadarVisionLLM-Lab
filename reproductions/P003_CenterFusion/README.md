# P003｜CenterFusion 复现计划（执行状态NOT_STARTED）

[论文](https://arxiv.org/abs/2011.04841v1) · [官方仓库](https://github.com/mrnabati/CenterFusion) · [正式档案](../../papers/P003_CenterFusion/README.md)。固定commit尚未选择；不将滚动分支当作冻结版本。

## 第一、二遍与工程顺序

第一遍按Abstract→Introduction→Methodology→Experiments→Related Work→Conclusion，每节真实验收并同步精读/概念/候选问题/日志。第二遍追踪数据预处理、初始化、forward、张量维度、Loss与梯度流、训练验证及指标。当前均无已完成源码精读证据；第一遍各节状态见正式档案。

## 第三阶段计划（尚未获准执行）

nuScenes mini调试 → 官方权重评估 → 训练与验证闭环；mini用于调试，不用mini指标冒充完整nuScenes基准。

## 资源登记与准入缺口

| 项 | 当前状态 |
| --- | --- |
| GPU / 存储计划 | RTX 3090 24GB，2–3TB（用户提供目标）；不是服务器实测输出 |
| 服务器完整配置 | CPU/RAM/驱动/CUDA/系统/可用显存/配额/磁盘路径均未确认 |
| 数据 | 主数据集nuScenes；合法访问、版本、划分、实际路径、预处理和校验均未核实；未下载 |
| 代码与配置 | 固定SHA、模型配置与全部调用链待第二遍核查（P005仅保留已核SHA） |
| 权重 | 来源/许可证/模型版本/校验值/配置兼容待确认；未下载 |
| 环境与算子 | 依赖版本、ABI与自定义算子待审查；未安装或编译 |
| 实际运行 / 日志 / 指标 | 无；不填预测显存、FPS或本项目mAP/NDS |
| 成功判据 | 执行前固定split、协议、官方目标/容差与日志输出；目前未定义可运行配置 |

## 第四阶段科研总结与证据区分

后续记录真实结果、失败案例、消融、局限、创新候选及相关论文证据。论文指标、官方权重本机评估、自己训练结果分别标注；当前三类均不填作本项目已取得结果。

[实验跟踪表](experiment_tracker.csv)沿用P001/P002的8列，无运行记录。每次run须关联commit、配置、seed、数据版本/划分、硬件依赖、命令、日志/结果和成功判据，按[已有记录规范](../RECORDING_STANDARD.md)维护。实验执行需另行明确授权，本次仅登记计划。

## Lesson 01归档后的执行状态

Title & Abstract验收PASS；Lesson 02 Introduction=NOT_STARTED；代码精读未开始，实验复现=NOT_STARTED。Planned仅指计划已登记，不表示环境已建立或模型已运行。[验收原文](../../docs/research_log/P003_CenterFusion_REVIEW.md)。
