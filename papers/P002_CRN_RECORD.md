# P002 CRN｜文献登记与字段依据

更新时间：2026-10-31。对应[36列主矩阵](paper_matrix.csv)中的唯一P002行；不是另一套精读笔记。

## 论文身份与来源

- 题目：CRN: Camera Radar Net for Accurate, Robust, Efficient 3D Perception。
- 作者：Youngseok Kim、Juyeb Shin、Sanmin Kim、In-Jae Lee、Jun Won Choi、Dongsuk Kum。
- 发表：ICCV 2023，17615–17626页。
- [CVF正式页面](https://openaccess.thecvf.com/content/ICCV2023/html/Kim_CRN_Camera_Radar_Net_for_Accurate_Robust_Efficient_3D_Perception_ICCV_2023_paper.html)、[官方代码](https://github.com/youngskkim/CRN)。DOI未独立核实，不补造。
- 本轮主依据为用户提供的正式论文PDF，共12页，文件内容未修改、未复制上传。以下PDF页码从1开始，区别于文中印刷页码17615–17626。

源PDF SHA-256：`e833ebf328d1eaecb0536699c9f29a13e36616e4ae0cfd6aa874d762a1f10296`。

## 字段证据与解释边界

| 字段组 | 依据 | 登记口径 |
| --- | --- | --- |
| 身份、任务、相机与数据集 | PDF p1摘要、p3 Fig.2、p5 §3.4/§4.1 | 包含检测及跟踪/BEV分割扩展；主要数据集nuScenes |
| Radar类型、表示、高程 | PDF p3 §3.1、p4 §3.2/Eq.4–5 | 不提供可靠高程；pillar风格、高度折叠；不将其当VoD成像Radar |
| Range | PDF p7 §4.4、Table 7 | BEV范围与评价距离分别登记，不将传感器最大量程混入模型范围 |
| Doppler、RCS、时序 | PDF p5 §4.1 | 使用归一化RCS与Doppler；六次历史radar sweep及三张历史BEV，不能混称同一种帧数 |
| RVT、MFA、BEV、Cross-Attention | PDF p3 Fig.2、p4 §3.2、p5 §3.3 | RVT视角变换与MFA聚合职责分开；MDCA为跨模态采样关联 |
| VLM、LLM、Radar_Token | 对已发表方法§3的组成核查 | 本项目字段分类：原方法无VLM/LLM模块；注意力query不等于面向语言模型的Radar Token，不冒称作者专门给出否定声明 |
| Physical_Constraint、Uncertainty | PDF p4 Eq.2–5及§3方法描述 | 有标定投影与几何引导、深度分布/占用响应；不能因此登记为已校准不确定性或独立物理一致性损失 |
| 雨天/夜间 | PDF p8 Table 9、§4.4，Fig.5 | 有定量子集实验，不只view drop；但不能推广到所有天气 |
| 遮挡与故障 | PDF p5 Fig.4、p8 Fig.5；p7 Table 8 | 定性遮挡、人工视角丢弃、真实遮挡控制实验分别理解 |
| 开源与工程可行性 | 官方仓库文档此前已静态读取；[本地可行性记录](../reproductions/P002_CRN/README.md) | 确认作者仓库入口，不代表源码全量审计、许可/权重可用或本机可运行 |
| Main_Limitation、Potential_Gap | Table 7/8/9及[研究问题](../docs/research_gaps/P002_CRN_Limitations_Research_Gap.md) | 输入挑战、实验范围和稀疏聚合权衡分别记录；候选问题未完成查新，不算独立创新 |
| Reproduction_Value/Difficulty、学习状态、主线关系 | 用户明确研究安排及[阅读日志](../docs/research_log/P002_CRN_READING_REPORT.md) | 工程优先级是维护决策；难度未实测。第一遍完成、教师此前验收通过；代码精读未开始、复现未执行，原始问答缺口仍保留 |

## 作者报告的代表性实验（本项目未运行）

| 来源及设置 | 作者报告值 | 比较边界 |
| --- | --- | --- |
| PDF p6 Table 1，nuScenes val，R50、256×704 | NDS 56.0，mAP 49.0，FPS 20.4 | 不和README Model Zoo的发布配置或其他表格混用 |
| PDF p7 Table 6，消融配置 | 完整MFA+RVT：NDS 53.9、mAP 45.2 | §4.3为两帧消融设置，不能与主表模型直接归因比较 |
| PDF p7 Table 7，R50、256×704、长距离Car评价 | CRN：AP 56.9、FPS 11.5；CRN-S：AP 54.0、FPS 14.0 | Car类别和指定距离范围，展示速度/精度权衡 |
| PDF p7 Table 8，Car类、单帧故障分析 | Camera丢3视角：CRN 48.9、BEVFusion 45.7；Camera全丢：12.8、14.3 | 是特定单模态输入丢弃，不是真实遮挡或双模态同时失效 |
| PDF p8 Table 9，R101、512×1408 | CRN Sunny/Rainy/Day/Night mAP：54.8/57.0/55.1/30.4 | 作者在指定天气/光照子集报告；不是全场景鲁棒保证 |

速度解释依据PDF p5 §4.1及p8 Fig.6：RTX3090、batch size 1、FP16等条件必须保留，模块时间与端到端速度不能互换。上述数值均不是本项目结果，没有产生run_id、训练日志或评估输出。

## 主矩阵36字段当前值

| 字段 | P002登记值 |
| --- | --- |
| `Paper_ID` | P002 |
| `Title` | CRN: Camera Radar Net for Accurate, Robust, Efficient 3D Perception |
| `Year` | 2023 |
| `Venue` | ICCV |
| `Task` | 3D object detection; extensions to tracking and BEV semantic segmentation |
| `Radar_Type` | Conventional automotive radar in nuScenes; not VoD 3+1D imaging radar |
| `Radar_Representation` | Radar point clouds; pillar-style frustum encoding and radar BEV features |
| `Range` | Main BEV range +/-51.2 m; long-range +/-102.4 m; Table 7 Car evaluation [0,100) m; not sensor maximum range |
| `Doppler` | Yes; Doppler speed used as radar feature (Sec. 4.1) |
| `RCS` | Yes; normalized RCS used as radar feature (Sec. 4.1) |
| `Elevation` | No reliable radar elevation; height collapsed in RVT pillar-style representation (Secs. 3.1-3.2) |
| `Camera` | Yes; multi-view camera images |
| `Dataset` | nuScenes; reported val/test protocols vary by table and model configuration |
| `Fusion_Level` | Feature-level fusion: radar-assisted image view transformation (RVT), followed by multi-modal BEV feature aggregation (MFA) |
| `BEV` | Yes; unified camera-radar BEV features for downstream tasks |
| `Temporal_Modeling` | Current plus 3 previous BEV maps at 1-second intervals; six previous radar sweeps accumulated (Sec. 4.1) |
| `Cross_Attention` | Yes; multi-modal deformable cross attention (MDCA) in MFA |
| `VLM` | No VLM component in the published CRN method |
| `LLM` | No LLM component in the published CRN method |
| `Radar_Token` | No VLM-facing radar token interface; BEV attention queries are not language tokens |
| `Physical_Constraint` | Calibration/projection geometry and radar spatial guidance in RVT; no separately claimed physics-consistency loss |
| `Uncertainty` | Image depth distribution and radar occupancy response; not established as calibrated predictive uncertainty |
| `Adverse_Weather` | Yes; sunny/rainy subset analysis in Table 9 and qualitative Fig. 5; not a guarantee for all adverse weather |
| `Night` | Yes; day/night subset mAP in Table 9, under the reported configuration |
| `Occlusion` | Qualitative occlusion examples in Figs. 4-5; view-drop Table 8 is not a controlled real-occlusion experiment |
| `Open_Source` | Yes; official repository documentation inspected; code execution and full release coverage not verified |
| `Official_Code` | https://github.com/youngskkim/CRN |
| `Main_Contribution` | RVT for radar-assisted image-to-BEV transformation; MFA with MDCA; optional top-K sparse aggregation |
| `Main_Limitation` | Sparse/ambiguous radar inputs and imperfect spatial alignment remain design challenges; sparse aggregation has accuracy/speed tradeoffs; robustness conclusions are bounded by tested settings |
| `Potential_Gap` | Candidate / Unverified: geometry reliability, modality conflict, sparse-region regression, alignment diagnostics and geometry-grounded VLM interfaces; novelty not established |
| `Reproduction_Value` | Method-learning and reference value; not currently prioritized for engineering reproduction (maintainer decision) |
| `Reproduction_Difficulty` | Not assessed by execution; legacy dependencies, GPU operators, data/license and checkpoint compatibility require audit |
| `Reading_Level` | First-pass intensive reading completed; code-level second pass not started |
| `Reading_Status` | Completed; teacher acceptance previously passed per user confirmation; original Q&A archive incomplete |
| `Relation_to_Our_Work` | Camera-radar BEV fusion reference connecting P001 radar basics to future fusion-paper selection; VLM extensions are project hypotheses |
| `Notes` | paper_notes/P002_CRN.md; field evidence: papers/P002_CRN_RECORD.md; feasibility: reproductions/P002_CRN/README.md; no model execution, training or evaluation performed |

## 与P001历史导入表的关系

P001的23列历史导入表已按2026-11-02用户要求删除。两篇论文统一在36列主矩阵登记；P002逐字段依据仍保留在本说明，不新增独立导入CSV。
