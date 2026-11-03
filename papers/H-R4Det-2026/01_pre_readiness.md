# P003 R4Det：正式学习前准入检查

2026-10-31。**准备档案，不是第一遍精读、第二遍代码学习或模型复现记录。** 本轮只读取论文身份/摘要与官方准备相关文本，复用同一源码SHA的既有审查；不把静态检查写成工程成功。

## 1. 论文身份与版本选择（论文原文/作者机构事实）

- 题目：R4Det: 4D Radar-Camera Fusion for High-Performance 3D Object Detection。
- 作者：Zhongyu Xia、Yousen Tang、Yongtao Wang、Zhifeng Wang、Weijun Qin。
- [arXiv:2603.11566v2](https://arxiv.org/abs/2603.11566v2)，2026-05-11修订；v1为2026-03-12。arXiv DOI为10.48550/arXiv.2603.11566，是预印本标识，不等于会议DOI。
- [官方仓库](https://github.com/VDIGPKU/R4Det)引用CVPR2026；[作者机构报道](https://wict.pku.edu.cn/xwgg/xsj/f78135003f564c8dab72034ae807e1d0.htm)亦列为CVPR2026成果。本轮未取得独立可读取的最终会议PDF/正式会议DOI，记待核实，不把arXiv v2自动称最终出版版。CVPR站点部分页面受robots限制。
- 正式精读前由用户/教师确认采用最终版还是明确标注的v2；当前可用阅读候选是v2。版本变更需重查图表和配置，不混用数字。

## 2. 值得阅读的问题（作者摘要事实与本项目推断分开）

| 作者摘要/README所述贡献 | 相对P001/P002的阅读价值（静态判断，不是公平性能结论） | 与主线关系 |
| --- | --- | --- |
| PDF：联合绝对/相对深度 | 相比P001 Radar-only引入图像深度；相比CRN雷达引导，可研究不同几何约束形式 | 与几何可靠性相关；不代表论文有VLM |
| DGTF：无需自车pose的可变形门控时序融合 | P001点级累积与CRN历史BEV不是同一种时序策略；可比较对pose和动态目标的假设 | 有助于理解时间证据，对语言模块只是潜在基础 |
| IGDR：用2D实例引导语义原型精炼BEV | 针对少/零雷达回波小目标；可检查相机证据的来源和偏差 | 与对象对应诊断相关，不等于语言grounding |

作者报告VoD/TJ4DRadSet实验，不据跨论文数字证明全面优于P001/CRN。未来第一遍重点核对方法假设、数据、消融和失败范围；不在这里填写已掌握结论或代答。

## 3. 固定源码与工程资源（官方代码事实/静态审查）

已重新查询官方main，固定审查版本：`9418d11949f41e802b583d99e69c825387082094`，提交时间2026-05-30T04:17:42Z。与[既有工程审查](../../docs/research_gaps/baseline_selection_round2/02_code_audit.md)相同，故保留原风险；本轮未clone或执行源代码。

| 项 | 已确认来源 | 当前状态/阻塞 |
| --- | --- | --- |
| 安装声明 | [固定install.md](https://github.com/VDIGPKU/R4Det/blob/9418d11949f41e802b583d99e69c825387082094/docs/guidance/install.md) | Ubuntu、Python3.8、CUDA11.8、Torch2.0.1、torchvision0.15.2、mmcv-full1.7.1、mmdet2.28.2、mmseg0.30.0及NATTEN0.14.6；是作者测试环境，不是本机环境 |
| 依赖闭环 | [requirements](https://github.com/VDIGPKU/R4Det/blob/9418d11949f41e802b583d99e69c825387082094/requirements.txt)、environment.yaml路径存在 | 非完整可运行证明；自定义分支、额外导入、ABI/编译器兼容仍待后续审查 |
| CUDA算子 | [安装指南](https://github.com/VDIGPKU/R4Det/blob/9418d11949f41e802b583d99e69c825387082094/docs/guidance/install.md)及setup.py；自定义Detectron2/NATTEN，mmdet3d/ops/csrc与deformattn | 没有安装、导入或编译；仓库已有二进制不等于适合本机 |
| 数据支持 | [固定dataset.md](https://github.com/VDIGPKU/R4Det/blob/9418d11949f41e802b583d99e69c825387082094/docs/guidance/dataset.md)列VoD和TJ4DRadSet | 文档支持不等于配置/产物闭环；许可、split、info、标定、顺序历史帧、图像/点云均待本地验证 |
| 附加监督 | 同上，instance masks、annotation masks、depth supervision与info | 未下载或生成；预测深度/实例初始化与本地文件对应未知，不能凭目录树认为已具备 |
| TJ4D配置 | [最终配置](https://github.com/VDIGPKU/R4Det/blob/9418d11949f41e802b583d99e69c825387082094/configs/r4det/TJ4D-R4Det_det3d_2x4_12e.py)、[预训练配置](https://github.com/VDIGPKU/R4Det/blob/9418d11949f41e802b583d99e69c825387082094/configs/r4det/TJ4D-R4Det_pretrain_2x4_12e.py)均在树中 | 有绝对深度路径和初始化依赖。文件名12e不等于实际epochs；最终配置max_epochs18、samples_per_gpu4，未证明与论文v2训练协议一致 |
| VoD配置 | main README示例指向configs/sgdet3d/vod-R4Det_det3d_2x4_12e.py | 在本次完整Git树中未找到；configs/r4det只有TJ4D两配置。不得自行补写“官方VoD配置” |
| checkpoint | [官方README指向的HF库](https://huggingface.co/Hoeyy/R4Det/tree/main)列final_tj4d.pth、pretrained_tj4d.pth及TJ4D-ADDI | 仅检查文件名/元数据，未下载/反序列化/校验；VoD配套checkpoint未找到，非宣称不存在于任何私有渠道 |
| 评估入口 | [tools/test_vod.py](https://github.com/VDIGPKU/R4Det/blob/9418d11949f41e802b583d99e69c825387082094/tools/test_vod.py)、test_TJ4D.sh/test_VoD.sh | sh脚本有占位checkpoint、8进程；不能直接照抄。本轮只读，未执行评估；val/test样本协议对应仍待核 |
| 代码许可 | 固定README仅声明academic research；API未识别项目许可证 | 依赖许可证不能替代项目完整条款；HF标MIT不自动覆盖GitHub源代码或数据。用途/再发布范围待确认 |
| 数据入口 | [VoD官方](https://github.com/tudelft-iv/view-of-delft-dataset)、[TJ4DRadSet官方](https://github.com/TJRadarLab/TJ4DRadSet) | 不申请/代签许可，不下载数据；实际访问及使用条件尚未闭合 |

源码相关文本SHA与来源清单见[本轮状态](../../docs/maintenance/EVIDENCE_ROUND3_STATE.json)。这是学习前的有界资源核查，不标记第二遍代码精读完成。

## 4. 本机与实验室硬件分开登记

| 环境 | 用户提供信息 | 本轮可核实输出 | 准入判断 |
| --- | --- | --- | --- |
| 本机 | RTX3060 Laptop 6GB | 只读nvidia-smi：NVIDIA GeForce RTX 3060 Laptop GPU；6144 MiB；driver580.88 | 只证实型号/总显存/驱动，不证实空闲显存、训练峰值或CUDA算子兼容；不宣布能训练 |
| 实验室服务器 | 可申请RTX3090“20GB”资源 | 没有服务器nvidia-smi、调度配额、驱动/CUDA/系统或磁盘输出，实际型号/总量/可用量均未核 | 20GB按用户描述保留，不能按3090常见规格替换，也不能把本机输出套用；训练准入待定 |

未经实际检查不能把论文单3090测速等同于服务器20GB训练可行。未来需要真实分配节点输出、依赖/算子检查、batch与分辨率、前向/反向峰值和时间预算；本轮均不执行。

## 5. 分阶段准入结论

| 阶段 | 当前判断 | 进入条件 |
| --- | --- | --- |
| 第一遍论文精读 | 适合；可作为下一次教师授权的阅读候选，当前未开始 | 先确认正式版或明确使用v2；带着深度/pose/零回波三问题阅读，并记录原文与假设 |
| 第二遍代码与实验精读 | 有研究价值，但暂缓，不在本轮启动 | 第一遍解释经教师核查，明确数据集、固定SHA、模型分支与待核配置/监督问题 |
| 最小复现 | 目前不准入，非永久否定模型 | 首先解决VoD配置/权重或明确改TJ4D；核对许可/监督产物、初始化、评估协议与服务器资源；重新提出有界执行任务 |

关键阻塞：最终论文版本与DOI、VoD配置/权重、实际服务器配额、依赖/算子及监督链、数据/源码/权重条款、评价协议一致性。论文可以先读，工程不应因为登记完成而自动启动。

## 6. 学习准备清单（未执行）

- [ ] 用户/教师确认阅读版本。
- [ ] 第一遍按动机→模块输入输出→实验/消融→局限组织原文证据。
- [ ] 区分原始点、生成/预测监督、BEV特征与检测框，检查零回波假设。
- [ ] 第一遍完成后提供真实开放式回答和教师批改，不能由Codex补造历史记录。
- [ ] 决定是否值得第二遍；模型执行另行授权。

本文件不填写任何“学习完成”“教师通过”或“复现成功”记录。
