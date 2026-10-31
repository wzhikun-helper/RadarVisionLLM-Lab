# P002 CRN｜复现可行性记录（暂不进入工程复现）

**未执行任何模型运行、训练或评估。** 代码第二遍精读未开始；本轮只是文档来源的静态核查。

## 已知来源与核查范围

官方代码入口：[youngskkim/CRN](https://github.com/youngskkim/CRN)。2026-10-30读取[官方README](https://raw.githubusercontent.com/youngskkim/CRN/main/README.md)，作者与正式笔记入口一致；没有克隆或固定官方代码commit，不声称完整源码审计或当前可运行。

| 项目 | 已知情况 | 未核实/本地状态 |
| --- | --- | --- |
| 数据 | README要求nuScenes及预处理；深度监督涉及LiDAR关键帧，雷达预处理涉及sweeps | 数据许可、版本、划分、下载与文件完整性未核实；未获取数据 |
| 环境 | README列出旧PyTorch/CUDA、MMCV/MMDetection系列依赖与GPU构建步骤 | 未安装、未验证操作系统/二进制算子兼容，不照搬为已成功环境 |
| 配置 | README Model Zoo列有CRN R18/R50配置链接 | 未读取逐项配置差异，未核对本地路径 |
| 权重 | README提供检测checkpoint链接 | 未下载，未检查资源可达性或权重键匹配 |
| 许可 | 需分别核对代码、数据和权重条款 | 本轮未独立核实许可，不写可任意再发布 |
| 硬件 | 作者速度依赖特定测试条件 | 本实验室GPU、显存和端到端耗时均未验证 |

## 为什么暂不优先复现

CRN当前承担融合基础学习与研究问题提取角色。按用户明确范围，不为每篇精读论文都部署旧环境；后续工程路线优先服从[已有基线审查](../../docs/research_gaps/baseline_selection_round2/05_decision_and_plan.md)。这是一项研究管理决策，不是认定CRN无法复现。

## 重新评估的触发条件

只有确需CRN对照且获得另行授权后，先固定源码SHA、核对许可和数据、确认单一配置/权重及硬件条件，再提出有界环境检查方案。不得把本文件当作安装或训练授权。

[experiment_tracker.csv](experiment_tracker.csv)仅建立与P001兼容的8列表头，**0条运行记录**。后续若进入工程阶段，每个真实run需关联配置、源码commit、数据版本/划分、种子、环境、命令、日志、指标及成功判据；不把作者Model Zoo结果填进本项目metric列。

来源阅读不等于代码精读、环境运行、模型前向或指标复现。

## 2026-10-31 统一档案字段与当前状态

与P001统一遵循[记录规范](../RECORDING_STANDARD.md)，同样登记来源、源码版本、数据/许可、配置/权重、环境/硬件、阶段、优先级和运行证据。当前为Deferred / Not Started：代码精读未开始、复现未执行、无本项目训练结果、无本项目评估指标，暂不列为优先工程基线。8列表头与P001一致，运行记录数保持0。未来需重新核对源码SHA、许可、数据和权重后才提出工程方案，不因建立档案而获安装或训练授权。

## 2026-10-31 内容审计：作者发布物与论文结果分开

重新静态读取[官方README](https://raw.githubusercontent.com/youngskkim/CRN/main/README.md)：提供检测配置和checkpoint链接，Model Zoo声明四keyframes且未使用CBGS；分割代码/权重在该README清单仍未勾选。不能由检测发布推定跟踪/分割工程资产齐全，也不能将Model Zoo数值自动替代正式论文Table 1。外部main未固定SHA，配置/权重未下载验证，具体任务源码覆盖仍待核查。

论文消融默认两帧、鲁棒性单帧、主实验及长距设置分别核对；Top-K还涉及训练监督/激活差异。[补充证据](../../docs/research_gaps/P002_CRN_CONTENT_SUPPLEMENT.md)列出这些边界及nuScenes官方评价入口。未来需固定eval配置、距离过滤、模态、checkpoint、数据/代码版本和命令，再分别验收流程可运行与指标复现；预期数值容差尚未约定。

维持Deferred / Not Started：代码精读未开始，模型复现未执行；0条实际运行记录，无本项目训练结果和评估指标。
