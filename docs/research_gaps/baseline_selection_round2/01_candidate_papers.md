# 第二轮候选论文总表

审查日期：2026-10-30（Asia/Shanghai）。项目：RadarVisionLLM。范围：公开资料与固定源码静态审查；未安装、编译、导入候选项目、运行前向/评估/训练或加载权重。

## 结论与证据口径

优先补齐 **MSSF-PP / VoD 的 Level 2 准入证据**；SGDet3D / VoD 为条件备选。不是最终选择 P003，也不是宣告复现成功。**暂未找到已满足全部长期代码基线条件的模型。**

状态仅使用：已验证、部分验证、未验证、不满足。“已验证”须附范围：文件/声明/静态调用已验证不等于运行已验证。L1=真实样本前向；L2=固定权重、配置、完整划分和同协议评估；L3=按公开方案重新训练。所有候选的本项目 L1/L2/L3 运行结果均未验证。**单 GPU 20GB 可运行性尚未验证。**

## 检索与筛选

检索组合包括 4D radar camera fusion / BEV fusion / temporal fusion / instance-level fusion / reproducible benchmark / vision-language / language grounding。检索来源为 CVF、IEEE、arXiv、官方仓库及作者链接的资源站；第三方列表仅用于发现，不作为结论依据。重点覆盖2023–2026，保留LXL这样的代表性方法。

共初筛 **11篇检测论文：10篇 Radar-Camera 融合论文＋1篇雷达单模态对照 MAFF-Net**。不是把 MAFF-Net 算作融合方法。深入静态审查6篇融合候选（MSSF、SGDet3D、LXL、HP-C4D、HGSFusion、R4Det），并对用户指定 MAFF-Net 做专项代码审查；共7篇。RaGS、RCBEVDet、RPGFusion、CVFusion停留在初筛/资源复核，不宣称全部调用链已审完。

## 论文与资源

| ID / 论文 | 发表与论文来源 | 数据 / 核心问题 | 官方代码、权重与阻塞 | 初步结论 |
|---|---|---|---|---|
| C01 MSSF: A 4D Radar and Camera Fusion Framework With Multi-Stage Sampling for 3D Object Detection in Autonomous Driving | IEEE T-ITS 26(6), 8641–8656, 2025；[IEEE](https://ieeexplore.ieee.org/document/10947638/)、[全文v2](https://arxiv.org/html/2411.15016v2) | VoD/TJ4D；多阶段体素/柱与图像采样、语义引导重加权，针对特征模糊 | [官方仓库](https://github.com/EricLiuhhh/MSSF)；[HF资源](https://huggingface.co/EricLiuhhh/MSSF/tree/0c4106c2640c536bc3d36fd1059c585ca7896401)内有4组配置/权重；通过有界ZIP目录和小配置源码读取静态核实配对；权重未加载 | Level 2证据最值得继续；环境、数据、初始化、授权和显存未闭合 |
| C02 SGDet3D: Semantics and Geometry Fusion for 3D Object Detection Using 4D Radar and Camera | IEEE RA-L 10(1), 828–835, 2025；[IEEE原始入口](https://ieeexplore.ieee.org/document/10783046/)，2024早期在线；不能只把README BibTeX的2024当卷期年份 | VoD/TJ4D；几何深度完成、语义雷达分支、目标导向注意力 | [官方仓库](https://github.com/shawnnnkb/SGDet3D)；[发布资源](https://github.com/shawnnnkb/SGDet3D/releases/expanded_assets/weights-and-checkpoints)有final/pretrained ZIP；实际配置齐全，但验证也读取分割、LiDAR深度等 | 条件备选；发布版本再训练指标与原论文不同，须分开验收 |
| C03 LXL: LiDAR Excluded Lean 3D Object Detection With 4D Imaging Radar and Camera Fusion | IEEE T-IV 9(1), 79–92, 2024；2023早期在线；[论文](https://arxiv.org/abs/2307.00724)、DOI 10.1109/TIV.2023.3321240 | VoD/TJ4D；深度分布和雷达3D占用辅助采样 | [官方仓库](https://github.com/XiongWeiyi/LXL)为需合入MMDet3D的插件；[VoD权重入口](https://drive.google.com/file/d/1bNDLZ1or1QKcnwfbp_OIP6yOseK30aE3/view)未核验文件；README承认重构后结果变化 | 适合机制消融；不是即开即用完整发行包，TJ4D官方配置本轮未定位 |
| C04 HP-C4D: A Fast Camera and 4D Radar Fusion Framework With Height Prediction for 3D Object Detection | IEEE TMM 28, 5159–5174, 2026；[IEEE](https://ieeexplore.ieee.org/abstract/document/11397088)、DOI 10.1109/TMM.2026.3664971 | VoD/TJ4D；Height BEVPool、PVHG、IGF | [官方仓库](https://github.com/c-yyyy/HP-C4D)有配置、单卡测试及训练实现；README明确不分发训练checkpoint；还引用V2-99初始化权重 | 研究候选；Level 2先被已训练权重来源阻塞，速度不等于显存保证 |
| C05 HGSFusion: Radar-Camera Fusion with Hybrid Generation and Synchronization for 3D Object Detection | AAAI 2025；[出版记录](https://ojs.aaai.org/index.php/AAAI/article/view/32328)、[全文](https://arxiv.org/html/2412.11489v1) | VoD/TJ4D；RHGM点生成、DSM空间和模态同步 | [官方仓库](https://github.com/garfield-cpp/HGSFusion)；云盘权重/混合点文件清单未验证；当前仍导入3个缺失弃用模块 | 可做有限排障；原样工程准入不满足，作者称弃用不等于核心DSM未公开 |
| C06 R4Det: 4D Radar-Camera Fusion for High-Performance 3D Object Detection | CVPR 2026；[出版记录](https://openaccess.thecvf.com/content/CVPR2026/html/Xia_R4Det_4D_Radar-Camera_Fusion_for_High-Performance_3D_Object_Detection_CVPR_2026_paper.html)、[审阅全文v2](https://arxiv.org/html/2603.11566v2) | VoD/TJ4D；PDF深度、DGTF时序、IGDR实例精化 | [官方仓库](https://github.com/VDIGPKU/R4Det)、[TJ4D资源](https://huggingface.co/Hoeyy/R4Det/tree/main)；当前未见对应VoD实验配置/权重，训练叙述与默认配置不同 | 精读价值高；先VoD工程路线暂缓，TJ4D可补证 |
| C07 CVFusion: Cross-View Fusion of 4D Radar and Camera for 3D Object Detection | ICCV 2025；[CVF](https://openaccess.thecvf.com/content/ICCV2025/html/Zhong_CVFusion_Cross-View_Fusion_of_4D_Radar_and_Camera_for_3D_ICCV_2025_paper.html) | VoD/TJ4D；RGIter、PGF/GGF两阶段跨视角proposal精化 | [官方仓库](https://github.com/zhzhzhzhzhz/CVFusion)当前仅README、LICENSE、.gitignore | 方法参考；当前官方代码L1–L3不满足 |
| C08 RCBEVDet: Radar-camera Fusion in Bird's Eye View for 3D Object Detection | CVPR 2024；[论文](https://arxiv.org/abs/2403.16440) | nuScenes及VoD；RadarBEVNet、RCS-aware编码、CAMF | [官方仓库](https://github.com/VDIGPKU/RCBEVDet)以ZIP发布代码，不是“只有README所以无代码”；本轮未下载完整ZIP、未验证VoD包及云盘权重 | 高质量参考，不能把nuScenes发行资源自动视为4D VoD闭环；++不另算一篇凑数量 |
| C09 RaGS: Unleashing 3D Gaussian Splatting from 4D Radar and Monocular Cue(s) for 3D Object Detection | CVPR 2026；[CVF论文](https://openaccess.thecvf.com/content/CVPR2026/papers/Bai_RaGS_Unleashing_3D_Gaussian_Splatting_from_4D_Radar_and_Monocular_CVPR_2026_paper.pdf)、[arXiv](https://arxiv.org/abs/2507.19856)；标题单复数随版本差异 | VoD/TJ4D/OmniHD-Scenes；FLI、IMA、MGF及Gaussian表示 | [官方仓库](https://github.com/shawnnnkb/RaGS)有实现，安装文档混合torch2/cu118及torch1.13/cu116扩展指引，未形成权重配对清单 | 高研究价值但工程复杂；本轮不作为低成本首选 |
| C10 RPGFusion: 4D Radar Prior-Guided Multi-Modal Fusion for 3D Detection | CVPR 2026；[CVF](https://openaccess.thecvf.com/content/CVPR2026/html/Qiu_RPGFusion_4D_Radar_Prior-Guided_Multi-Modal_Fusion_for_3D_Detection_CVPR_2026_paper.html) | VoD/TJ4D；雷达置信度/深度先验、稀疏到稠密传播、对齐融合 | 论文真实；本轮未定位经作者/论文确认的官方仓库与权重，不猜测URL | 论文初筛保留，工程证据未验证；不是断言永无代码 |
| C11 MAFF-Net: Enhancing 3D Object Detection With 4D Radar Via Multi-Assist Feature Fusion | RA-L 2025；[IEEE入口](https://ieeexplore.ieee.org/document/10923711/) | VoD/TJ4D；SPA、速度聚类CQCA、CDA；**雷达单模态** | [官方仓库](https://github.com/TRV-Lab/MAFF-Net)、两套配置和发布权重；IMAGE_BACKBONE名下的CQCA_cfa实际读取points，不读照片 | 从融合主基线名单排除；保留为强Radar-only对照 |

## 固定版本与第一轮复核

| 仓库 | 本轮读取的HEAD SHA | 变化/范围 |
|---|---|---|
| EricLiuhhh/MSSF | 0c9482f8b0d9dc1c43b17a68fd5312bad97e7ea7 | 新增深入审查 |
| shawnnnkb/SGDet3D | 83f8c7d76f2b6d3e84ca948dee5f9e4ba472b64c | 新增深入审查 |
| XiongWeiyi/LXL | cde23c8af5dbeddfec33a34ec8c41a49b1a1a8f5 | 新增深入审查 |
| c-yyyy/HP-C4D | b796ac7ca638928f497b466f941871509f8588e3 | 新增深入审查 |
| TRV-Lab/MAFF-Net | 0bb253fbeebb0813d40b957e1e802e57690d6ed3 | master；主线专项核查 |
| VDIGPKU/R4Det | 9418d11949f41e802b583d99e69c825387082094 | 与第一轮相同；文件树未见所缺VoD配置，未观察到阻塞解除 |
| zhzhzhzhzhz/CVFusion | c05ba32d92a0781916b0be00bd973b2267b3cf98 | 与第一轮相同；完整树3个文件 |
| garfield-cpp/HGSFusion | fae255340620513dfc7cf9691d098b70bd5af406 | 与第一轮相同；弃用导入问题未在该提交消除 |
| VDIGPKU/RCBEVDet | 15c83ccdd5a8cfd3b7c0390eacd8664cf842d513 | 4个文件含代码ZIP；ZIP内部版本/配置未确认 |
| shawnnnkb/RaGS | ec5160c497305a7ced3488e3ea5f4ee0d725e06c | 通过git ls-remote只读确认HEAD；不拉取对象 |
| RPGFusion | 未验证 | 官方仓库尚未定位，不编造SHA |

GitHub API后续出现403限流；已取得的固定提交raw文件仍可查。SHA不变只表示版本无变，不表示运行已验证。具体源码证据见[02](02_code_audit.md)，评分见[03](03_reproducibility_ranking.md)。

## 新发现的重叠工作，单独跟踪、不凑检测候选数量

- [SGDet3D++，arXiv:2609.27671](https://arxiv.org/abs/2609.27671)：AGR/GCR/DVC、对象条件证据和Doppler历史验证，预印本称代码将发布；不能把原SGDet3D仓库算作++实现。对未来“实例/时序可信融合”存在直接重叠。
- [RCVLA，arXiv:2609.32681](https://arxiv.org/html/2609.32681v1)：Radar-Camera语言/动作路线，报告Cap4DR、OmniHD-QA。资源发布与标注质量本轮未审闭合，不拿论文声称规模当已可用数据。
- [Radar4D-VLM，arXiv:2608.04130](https://arxiv.org/abs/2608.04130)：雷达单模态、对象/场景/运动token与冻结语言模型；作者报告语言对齐未带来稳定直接头收益。它是语言收益对照设计参考，不是Camera-Radar检测基线。
- CRN是已学P002，主要nuScenes传统雷达路线，不重复充数；雷达-only SMURF、LiDAR-Radar V2X-R、同名但非本任务的MAFF论文不纳入融合推荐池。

## 数据、硬件与论文质量的共同限制

VoD/TJ4D授权、文件完整性、服务器均未核实。VoD当前使用[新申请站](https://viewofdelft-dataset.tudelft.nl/)，按[官方Access](https://github.com/tudelft-iv/view-of-delft-dataset#access)核查；TJ4D按[官方NDA申请说明](https://github.com/TJRadarLab/TJ4DRadSet#access_license)。公开代码许可与数据许可是两回事。

MSSF、LXL以及第一轮R4Det/HGSFusion/CVFusion的公开论文部分有具体消融证据；SGDet3D和MAFF-Net的IEEE页面本轮触发JS验证，HP-C4D可核实出版元数据和摘要，但全文消融未完整核查。相关研究质量评分保留扣分，不把会议/期刊身份当成全文审查通过。

不同数据集、版本、R11/R40、EAA/DC、3D/BEV和NDS不可混排数值。所有“下一步优先”均需教师复核，不启动正式精读或复现。
