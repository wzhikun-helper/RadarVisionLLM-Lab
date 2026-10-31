# P001 PointPillars + VoD 复现计划

**状态：Planned（未安装、未下载数据、未训练、未验证）**。

## Phase 0｜资源与环境核查

1. 核对 VoD 官方网站、使用许可、数据集版本、train/val/test 划分；论文原始 split 为 59/15/26（按 clip）。
2. 查找 P001 官方作者代码、论文补充材料及 OpenPCDet 对应版本；**当前未验证存在可直接运行的官方 P001 配置**。
3. 检查本机 Windows 11 GPU 型号、显存、驱动、CUDA、可用磁盘空间；先决定 WSL2 Ubuntu 还是原生 Ubuntu，不假定已配置。
4. 明确需要的数据转换（KITTI-like 标注、坐标系、Radar 特征）、官方评估实现与驾驶走廊区域过滤。
5. 检查 `.gitignore`，数据集、模型权重、日志大文件只在本地或外部存储。

**预期产物**：`environment_report.md`、`data_license_check.md`、`baseline_sources.md`（待生成）。

## Phase 1｜最小可运行基线

- 创建隔离 Python 环境，记录 PyTorch/CUDA/OpenPCDet 的版本与 Git commit。
- 仅下载/加载许可允许的少量样本，检查 `(x,y,z,v_rel,RCS)` 的坐标和单位。
- 可视化一帧 Radar 点云与 3D GT 框，验证标定、数据范围、类别标签。
- 运行一个 batch 的 PointPillars 前向传播，确认输出张量与 3D 框坐标。
- 跑通 AP3D/AOS 评价脚本；检查 Car IoU 0.5、Ped/Cyclist 0.25。

**成功标准**：命令可重复运行、无 NaN、输出预测框、生成合法指标；不要求立即达到论文数值。

## Phase 2｜论文实验复现

| Experiment | Paper target mAP | Status |
|---|---:|---|
| Radar 1 scan full | 38.0 | Planned |
| Radar no Doppler | 29.1 | Planned |
| Radar no Elevation | 31.9 | Planned |
| Radar no RCS | 36.6 | Planned |
| Radar 3 scans | 46.3 | Planned |
| Radar 5 scans | 47.0 | Planned |
| LiDAR 1 scan | 62.1 | Planned |
| Driving Corridor Radar 5 scans | 71.4 | Planned |

- 每个实验保存 YAML 配置、随机种子、数据版本、训练/推理命令、完整日志、评估 JSON、环境信息。
- 与原文不同的硬件、数据拆分、输入特征、评估脚本必须在对照表明确注明，不能混为“精确复现”。

## Phase 3｜分析与扩展

- 绘制按类别、距离、3D IoU 的 AP/Recall；绘制远距离失败案例。
- 统计每个 GT 内的 Radar 点数、RCS 与距离分布，注意遮挡/类别混杂因素。
- 比较不同帧数收益与延迟、动态目标残影。
- 生成 `results/` 报告；尚无数据时不得虚构曲线。

## 每阶段执行记录模板

| 日期 | 阶段 | 操作/命令 | 目的 | 预期输出 | 实际输出 | 异常与排查 | 产物路径 |
|---|---|---|---|---|---|---|---|
| 待执行 | Phase 0 | 待填写 | 环境核查 | 环境清单 | 未运行 | - | - |

## 常见故障排查顺序

1. 数据路径/许可与文件完整性；2. 坐标系/标定和时间对齐；3. 点特征维度与 RCS/Doppler 单位；4. CUDA/PyTorch/OpenPCDet 版本；5. 标签与 IoU 评价协议；6. 多帧累积的自车坐标变换。

## 安全与资源

未经用户许可不下载大型 VoD 数据、不运行 GPU 长训练、不改写现有项目配置、不提交二进制数据或模型权重。

## 2026-10-31 统一档案字段与当前状态

按[统一记录规范](../RECORDING_STANDARD.md)维护与P002一致的字段与状态。当前工程状态为Planned，复现未证实；原表中的论文目标与计划不代表本项目已有结果。官方源码固定SHA、资源许可、可运行配置与权重、本机环境/算子/硬件均未完成准入核查。下一步仍是Phase 0，需另行授权；没有新增run、训练结果或评估指标。既有8列表头及Planned行原样保留。
