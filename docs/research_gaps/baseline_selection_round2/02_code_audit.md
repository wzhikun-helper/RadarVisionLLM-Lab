# 第二轮重点候选代码审查

日期：2026-10-30。全部为静态审查；下面的命令是未来运行候选，**本轮均未执行**，它们会创建输出，不能称为只读测试。本轮仅保存这五份审查文档，不落地第三方源码。

## 证据覆盖与状态矩阵

版本见[01固定版本表](01_candidate_papers.md)。已验证仅针对对应静态对象；资源二进制、ABI、权重张量匹配及实际指标没有验证。深入6篇融合候选＋MAFF-Net主线专项核查，共7篇。

| 静态核查项 | MSSF | SGDet3D | LXL | HP-C4D | HGSFusion | R4Det | MAFF-Net |
|---|---|---|---|---|---|---|---|
| 论文/作者与仓库关联 | 已验证 | 部分验证 | 部分验证 | 部分验证 | 已验证 | 已验证 | 部分验证 |
| 固定提交与模型文件 | 已验证 | 已验证 | 已验证 | 已验证 | 已验证 | 已验证 | 已验证 |
| 数据加载类 | 已验证 | 已验证 | 部分验证 | 部分验证 | 已验证 | 已验证 | 部分验证 |
| 预处理脚本/声明 | 已验证 | 已验证 | 已验证 | 已验证 | 已验证 | 已验证 | 已验证 |
| 预处理产物完整可取 | 部分验证 | 未验证 | 未验证 | 未验证 | 未验证 | 部分验证 | 未验证 |
| VoD实际实验配置 | 已验证 | 已验证 | 已验证 | 已验证 | 已验证 | 不满足 | 已验证 |
| 训练入口 | 已验证 | 已验证 | 已验证 | 已验证 | 已验证 | 已验证 | 已验证 |
| 单GPU测试代码分支 | 已验证 | 已验证 | 已验证 | 已验证 | 已验证 | 已验证 | 已验证 |
| 发布权重可定位 | 已验证 | 部分验证 | 部分验证 | 未验证 | 部分验证 | 部分验证 | 部分验证 |
| 权重参数完整匹配 | 未验证 | 未验证 | 未验证 | 未验证 | 未验证 | 未验证 | 未验证 |
| 固定环境可实际构建 | 未验证 | 未验证 | 未验证 | 未验证 | 未验证 | 未验证 | 未验证 |
| 应用导入/算子全链可执行 | 未验证 | 未验证 | 未验证 | 未验证 | 不满足 | 未验证 | 未验证 |
| 主线Radar+Camera | 已验证 | 已验证 | 已验证 | 已验证 | 已验证 | 已验证 | 不满足 |
| 本项目前向/评估/训练结果 | 未验证 | 未验证 | 未验证 | 未验证 | 未验证 | 未验证 | 未验证 |

关联“部分验证”的原因：可核实官方自述、论文身份和仓库引用，但本轮受出版页面访问限制等影响，没有全部取得论文侧的反向代码链接。不能把它写成双向关联全部独立验证。

## MSSF

### 固定源码与数据流

仓库提交：0c9482f8b0d9dc1c43b17a68fd5312bad97e7ea7。

- M1：[VoxelNetFuse](https://github.com/EricLiuhhh/MSSF/blob/0c9482f8b0d9dc1c43b17a68fd5312bad97e7ea7/mmdet3d/models/detectors/voxelnet_fuse.py#L18)，类VoxelNetFuse；extract_feat(:137)取得图像、点云和points_misc；predict(:168)、loss(:234)分别供测试和训练。并不存在必须名为mssf.py的要求。
- M2：[SECONDFuse](https://github.com/EricLiuhhh/MSSF/blob/0c9482f8b0d9dc1c43b17a68fd5312bad97e7ea7/mmdet3d/models/backbones/second_fuse.py#L28)，init_query、query_voxel_fuse、apply_seg_scores、forward、aux_loss提供阶段采样/重加权接口；[VoxelFusion](https://github.com/EricLiuhhh/MSSF/blob/0c9482f8b0d9dc1c43b17a68fd5312bad97e7ea7/mmdet3d/models/layers/fusion_layers/voxel_fusion.py#L252)负责图像采样。
- M3：[VodDataset](https://github.com/EricLiuhhh/MSSF/blob/0c9482f8b0d9dc1c43b17a68fd5312bad97e7ea7/mmdet3d/datasets/vod_dataset.py)与[转换入口](https://github.com/EricLiuhhh/MSSF/blob/0c9482f8b0d9dc1c43b17a68fd5312bad97e7ea7/tools/create_data.py)。默认VoD需要7维雷达点、图像、标定、标签及info；配置读取training/velodyne_reduced，不是只检查velodyne即可。
- M4：[tools/test.py](https://github.com/EricLiuhhh/MSSF/blob/0c9482f8b0d9dc1c43b17a68fd5312bad97e7ea7/tools/test.py#L15)：config是位置参数，--checkpoint、--metric等是真实参数。导入的自定义Runner是包[mmdet3d/custom_runner/fast_runner.py](https://github.com/EricLiuhhh/MSSF/blob/0c9482f8b0d9dc1c43b17a68fd5312bad97e7ea7/mmdet3d/custom_runner/fast_runner.py#L60)，不是缺失的custom_runner.py。
- M5：[VODMetric](https://github.com/EricLiuhhh/MSSF/blob/0c9482f8b0d9dc1c43b17a68fd5312bad97e7ea7/mmdet3d/evaluation/metrics/vod_metric.py#L21)及eval_vod实现。真实注册名是VODMetric；不能原样传README示意的“[VoDMetric,TJ4DMetric]”字符串。优先保持配套配置内的evaluator，不另换协议。

补查的数据转换命令差异：[tools/create_data.py:335](https://github.com/EricLiuhhh/MSSF/blob/0c9482f8b0d9dc1c43b17a68fd5312bad97e7ea7/tools/create_data.py#L335)将dataset定义为**位置参数**，README的--dataset不能原样照抄；args.extra_tag决定info前缀。与当前kitti_infos_val.pkl配套的未来候选是 `python tools/create_data.py vod --root-path data/vod --out-dir data/vod --extra-tag kitti`。脚本会生成文件，本轮未执行；先核查已有info，避免重复生成。

协议静态证据：[eval_vod.py:614–626](https://github.com/EricLiuhhh/MSSF/blob/0c9482f8b0d9dc1c43b17a68fd5312bad97e7ea7/mmdet3d/evaluation/functional/kitti_utils/eval_vod.py#L614)分别计算11点与40点AP；[VODMetric:297–306](https://github.com/EricLiuhhh/MSSF/blob/0c9482f8b0d9dc1c43b17a68fd5312bad97e7ea7/mmdet3d/evaluation/metrics/vod_metric.py#L297)对entire_area和roi调用custom_method 0/3，最终map取Car/Pedestrian/Cyclist的非R40的3D AP均值。eval_vod另输出R40与strict分支，不能挑不同分支去匹配论文。对应宽松3D IoU阈值为0.5/0.25/0.25，仍需后续把最终日志键和论文/发布表对应验收。

流程：七维雷达→PillarFeatureNet/Scatter→多阶段融合骨干；图像→ResNet50/FPN→采样特征；融合BEV→检测头→VODMetric。配置中的use_lidar=True是框架点云接口命名，不能据此把这套七维输入称为LiDAR传感器输入。

### 权重—配置配对的实际证据

官方README链接HF；固定资源版本为 **0c4106c2640c536bc3d36fd1059c585ca7896401**。[固定资源树](https://huggingface.co/EricLiuhhh/MSSF/tree/0c4106c2640c536bc3d36fd1059c585ca7896401)

本轮没有下载1.23GB压缩包：读取末尾65,536字节ZIP目录；另请求8,192字节，只解压其中3,607字节的配置源码，得到791行文本。未反序列化权重。服务器必须返回206且范围匹配，否则中止正文读取。

| ZIP内目录 | 配置文件 | 对应权重；解压后大小 |
|---|---|---|
| mssf_pp_vod | pointpillars_hv_secfpn_8xb6-160e_vod-3d-3class_mm_bb_bevfeat_lr0001.py | epoch_40.pth；182,937,759 B |
| mssf_pp_tj4d | pointpillars_hv_secfpn_8xb6-160e_tj4d-3d-4class_mm_bb_bevfeat_lr00005.py | epoch_40.pth；184,375,455 B |
| mssf_vx_vod | vx_mm_r50_ablation_n2m4.py | epoch_40.pth；508,315,013 B |
| mssf_vx_tj4d | vx_mm_r50_mulscore_lr0001_tj4d.py | epoch_40.pth；511,178,197 B |

上表是目录配对，仍不证明参数键/形状兼容或性能。仅完整检查了PP/VoD配置源码；没有假称另外三份配置也已逐行核查。

该配置：test_dataloader(:417) batch_size=1；data_root=data/vod/，kitti_infos_val.pkl，points来自training/velodyne_reduced；VODMetric(:491)；train_cfg(:555)实际40 epochs，不能按文件名中的160e推定训练轮数。load_from(:61)仍是作者旧输出目录，未来应由--checkpoint明确覆盖。声明img_scale=(1333,800)，但不能仅凭这一字段认定已执行某种resize；本轮不据此估算显存。

### 环境、评估与训练

[environment.yaml](https://github.com/EricLiuhhh/MSSF/blob/0c9482f8b0d9dc1c43b17a68fd5312bad97e7ea7/environment.yaml)声明Python3.9.17、PyTorch1.10.1/cu113、MMCV2.0.1、MMDet3.1.0、MMEngine0.8.4、spconv-cu113 2.3.6及pytorch-scatter。README写environment.yml，而实际文件是environment.yaml。不要直接照抄作者机器prefix。

[mmdet3d/__init__.py:9–36](https://github.com/EricLiuhhh/MSSF/blob/0c9482f8b0d9dc1c43b17a68fd5312bad97e7ea7/mmdet3d/__init__.py#L9)限制MMCV>=2.0.0rc4,<2.1.0；MMEngine>=0.8,<1；MMDet>=3.0,<3.2。将MMDet升级3.3会触发不兼容。FastRunner使用MMEngine内部接口，不能仅让顶层版本断言通过就宣告环境可用。

图像初始化配置引用HTC COCO/nuImages权重；paper说明冻结图像分支，源码VoxelNetFuse.init_weights(:49–63)确有冻结逻辑。初始化资源路径和Runner加载顺序仍需在后续部署验证，不能认为最终checkpoint自动消除了所有骨干预训练依赖。无须因此下载整个nuImages训练集。

未来候选命令，路径均待实际部署建立：

```bash
python tools/test.py exps/mssf_pp_vod/pointpillars_hv_secfpn_8xb6-160e_vod-3d-3class_mm_bb_bevfeat_lr0001.py --checkpoint exps/mssf_pp_vod/epoch_40.pth --work-dir work_dirs/r2_mssf_pp_vod
python tools/train.py CONFIG --work-dir WORK_DIR
```

论文和README的PP/VoD参考为EAA63.31、DC79.78；属于作者结果，不能以此填入本项目results。论文报告单3090训练，未给本项目20GB显存保证。TJ4D还需作者提供的绝对径向速度，8维原始点扩为9维；VoD首测可避免此额外产物。

L1：缺服务器/环境/一个合法真实样本/初始化与检测权重。L2：再缺完整val与协议/类别映射/所有权重键匹配/完整预测集合证据。L3：还需训练样本、训练资源和多次运行可追溯记录。最低成本先完成样本清单和静态导入闭合，不能先训练。

长期阻塞：顶层LICENSE请求404，GitHub许可字段为空；上游文件的Apache标头不等于项目全部新增代码的授权已确认。需澄清可修改及再发布范围。本轮不作法律结论。

## SGDet3D

版本：83f8c7d76f2b6d3e84ca948dee5f9e4ba472b64c。

- S1：[模型SGDet3D](https://github.com/shawnnnkb/SGDet3D/blob/83f8c7d76f2b6d3e84ca948dee5f9e4ba472b64c/projects/SGDet3D/mmdet3d_plugin/models/detectors/SGDet3D.py)；图像ResNet/FPN与雷达PillarNet，经GeometryDepth_Net、MRF3Net、Cross_Modal_Fusion、FRPN及BackwardProjection交互；特征提取和前后投影模块可作为消融接口。
- S2：[VoD最终配置](https://github.com/shawnnnkb/SGDet3D/blob/83f8c7d76f2b6d3e84ca948dee5f9e4ba472b64c/projects/SGDet3D/configs/vod-SGDet3D_det3d_2x4_12e.py#L355)，同目录另有VoD/TJ4D预训练及最终配置；VoD loader在projects/SGDet3D/mmdet3d_plugin/datasets/vod_dataset.py。
- S3：[数据说明](https://github.com/shawnnnkb/SGDet3D/blob/83f8c7d76f2b6d3e84ca948dee5f9e4ba472b64c/docs/Guidance/dataset.md)。实际配置根为data/VoD/radar_5frames；指南目录有radar_5_scans字样，须核对真实路径。train/test pipeline都包含loadSegmentation、CreateDepthFromLiDAR/CreateDepthFromRaDAR、gen2DMask。纯验证也不能直接删掉LiDAR/分割资源。是否所有标注只用于辅助/可视化，仍需详细追踪，不据此武断认定泄漏。
- S4：[测试入口](https://github.com/shawnnnkb/SGDet3D/blob/83f8c7d76f2b6d3e84ca948dee5f9e4ba472b64c/tools_det3d/test.py)有single_gpu_test；[test_VoD.sh](https://github.com/shawnnnkb/SGDet3D/blob/83f8c7d76f2b6d3e84ca948dee5f9e4ba472b64c/test_VoD.sh)默认4卡，先format-only，再FINAL_EVAL.py，并非一个单卡脚本。
- S5：[发布资产目录](https://github.com/shawnnnkb/SGDet3D/releases/expanded_assets/weights-and-checkpoints)实际列出final_ckpt.zip约1.23GB、pretrained_ckpt.zip约915MB。尝试只读ZIP目录遇HTTP501 Unsupported client range，停止，不回退整包下载；内部文件名、参数及校验值未验证。
- S6：[安装声明](https://github.com/shawnnnkb/SGDet3D/blob/83f8c7d76f2b6d3e84ca948dee5f9e4ba472b64c/docs/Guidance/Install.md)：Python3.7、Torch1.9.1/cu111、MMCV-full1.4、MMDet2.14、MMSeg0.14.1、Detectron2、NATTEN；setup.sh另构建DFA3D和Voxelization。mmengine等未完整固定。旧Python及二进制依赖风险较高。

未来候选：python tools_det3d/test.py --config projects/SGDet3D/configs/vod-SGDet3D_det3d_2x4_12e.py --checkpoint ACTUAL_FINAL_VOD --launcher none --format-only --eval-options submission_prefix=ACTUAL_OUTPUT；再按FINAL_EVAL.py核对完整val评估。训练入口tools_det3d/train.py，另有dist_train.sh。

[训练/评估说明](https://github.com/shawnnnkb/SGDet3D/blob/83f8c7d76f2b6d3e84ca948dee5f9e4ba472b64c/docs/Guidance/train_and_eval.md)报告四4090、两阶段训练；不是单20GB证据。README声明发布代码重训后指标更好：验收应针对其发布版本目标（VoD EAA59.75/DC77.42），不要混称原论文数字逐项复现。

L1缺环境、合法样本及所有辅助输入；L2还缺ZIP内部资源匹配、完整验证及独立官方评估一致性；L3缺两阶段初始化完整性/训练预算。先查资源目录而不是先编译。顶层LICENSE本轮404，二次开发发布授权未确认。IEEE全文消融访问不完整，需教师补充论文证据。

## LXL

版本：cde23c8af5dbeddfec33a34ec8c41a49b1a1a8f5。

- L1：[LXLDetector](https://github.com/XiongWeiyi/LXL/blob/cde23c8af5dbeddfec33a34ec8c41a49b1a1a8f5/plugin/lxl/models/detectors/lxl_detector.py#L13)，extract_feat(:139)、fuse_feats(:200)、forward_train/simple_test可定位。
- L2：[SamplingBasedViewTrans](https://github.com/XiongWeiyi/LXL/blob/cde23c8af5dbeddfec33a34ec8c41a49b1a1a8f5/plugin/lxl/models/view_trans/sampling_based_view_trans.py#L11)：图像多尺度特征/深度与雷达占用→采样图像体素→图像BEV；与雷达BEV通过ConcatFusion融合。构造中有device=cuda，CPU-only冒烟不是等价路线。
- L3：[实际配置目录是大写LXL](https://github.com/XiongWeiyi/LXL/blob/cde23c8af5dbeddfec33a34ec8c41a49b1a1a8f5/plugin/lxl/configs/LXL/LXL_vod.py)，README命令用小写lxl，Linux需修正大小写。数据配置使用7维radar、VoD_infos_val.pkl、绝对data_root占位；pretrained_img指向YOLOX-s作者机器路径。
- L4：[tools/test_v2.py](https://github.com/XiongWeiyi/LXL/blob/cde23c8af5dbeddfec33a34ec8c41a49b1a1a8f5/tools/test_v2.py)与train_v2.py存在；create_data_vod.py提供转换入口。仓库仅31个文件，README要求将文件合入MMDet3D，而不是完整独立框架。
- 环境声明：Python3.8、Torch1.12/cu113、MMCV1.6、MMDet2.25、MMSeg0.26、MMDet3D1.0.0rc3、vod-tudelft1.0.3；上游ops版本及插件合入边界需核对。
- [作者checkpoint入口](https://drive.google.com/file/d/1bNDLZ1or1QKcnwfbp_OIP6yOseK30aE3/view)文件未核实。README说明重构后重训模型与论文表现略有不同，未给可直接采用的精确新目标。

未来候选：python tools/test_v2.py plugin/lxl/configs/LXL/LXL_vod.py ACTUAL_CHECKPOINT --eval bbox。训练同配置使用tools/train_v2.py。论文有采样/深度/占用以及CRN式辅助对照，适合可解释消融；没有独立语言token实现。

L1须补上游安装、插件和单样本；L2须确认权重、配套版本、完整val和重训目标；L3须初始化权重、train划分及固定随机设置。公开TJ4D训练/评估配置本轮未定位，不能按论文两个数据集自动宣称两套资源齐全。许可和显存仍待核实。

## HP-C4D

版本：b796ac7ca638928f497b466f941871509f8588e3。

- H1：[HPC4D](https://github.com/c-yyyy/HP-C4D/blob/b796ac7ca638928f497b466f941871509f8588e3/projects/HP_C4D/hpc4d_model/HP_C4D.py#L17)，extract_feat、loss、predict(:191)；真实流为相机/雷达→图像BEV/雷达BEV→IGF→检测。
- H2：[HPC4DViewTransformer](https://github.com/c-yyyy/HP-C4D/blob/b796ac7ca638928f497b466f941871509f8588e3/projects/HP_C4D/hpc4d_model/view_trans/view_transformer_hpc4d.py#L244)，使用height_bevpool得到bev_feat、bev_height，再将高度信息送入bbox head；不能仅从“height prediction”名称推断是额外深度大模型。PVHG.forward与IGF.forward真实存在。
- H3：[融合配置](https://github.com/c-yyyy/HP-C4D/blob/b796ac7ca638928f497b466f941871509f8588e3/projects/HP_C4D/configs/hpc4d_radar%2Bcam.py)：图像320×960；启用Height BEVPool/PVHG/IGF；训练LoadGtDepthFromFile，测试管线不加载该训练监督。另有TJ4D的pp+cam_tj4d.py。
- H4：[tools/test.py:18–19、127、143–150](https://github.com/c-yyyy/HP-C4D/blob/b796ac7ca638928f497b466f941871509f8588e3/tools/test.py#L18)真实接收--config/--checkpoint，经Runner.test；单卡候选命令与README一致，不是仅一个空壳bash。
- H5：[项目算子setup](https://github.com/c-yyyy/HP-C4D/blob/b796ac7ca638928f497b466f941871509f8588e3/projects/HP_C4D/setup.py)包含Voxel、BEVPool、Height BEVPool等CUDA/C++。环境：Python3.8、Torch2/cu118、MMEngine0.10.5、MMCV2.0.0rc4、MMDet3.3；依赖安装成功/ABI未验证。
- [README数据与资源说明](https://github.com/c-yyyy/HP-C4D/blob/b796ac7ca638928f497b466f941871509f8588e3/README.md#L69)明确不分发训练checkpoint。配置还引用depth_pretrained_v99-reduced_backbone.pth；本轮未核实该初始化资源的官方获取路径。

未来候选：python tools/test.py --config projects/HP_C4D/configs/hpc4d_radar+cam.py --checkpoint ACTUAL_CHECKPOINT --work-dir ACTUAL_OUTPUT。训练tools/train.py或dist_train.sh，示例2卡。

论文摘要报告单3090为21.4FPS，是作者速度结果，不是显存实测、不是本项目记录。L1仍缺模型/骨干权重；L2存在直接checkpoint来源缺口；L3训练代码可定位，但监督产物、初始化和预算未闭合。先取得权重清单，不能把“从头训练拿个模型”当作低成本补齐官方评估。

## HGSFusion：同一固定版本的复核

版本：fae255340620513dfc7cf9691d098b70bd5af406，与第一轮相同。

- G1：[fusion_vfe.py:8–13](https://github.com/garfield-cpp/HGSFusion/blob/fae255340620513dfc7cf9691d098b70bd5af406/pcdet/models/backbones_3d/vfe/fusion_vfe.py#L8)无条件导入不存在的feature_sampler、radar_occupancy_2d、foreground_sampler；vfe/__init__.py也无条件导入FusionVFE。[作者说明它们弃用](https://github.com/garfield-cpp/HGSFusion/issues/5#issuecomment-2789073682)。注册字典仍引用类名，不能只删import，也不能自行编个同名模块冒充论文实现。
- G2：[配置](https://github.com/garfield-cpp/HGSFusion/blob/fae255340620513dfc7cf9691d098b70bd5af406/tools/cfgs/hgsfusion/hgsfusion_vod.yaml)→CaDDN/FusionVFE→ImageVFE/PillarNet→RadarOccupancy2DV2→FusionAfterBEVSEDirect→AnchorHeadSingle。DSM已有占用增强与SE融合实现，不能由弃用模块缺失推断核心DSM必然未公开。
- G3：[VoD loader](https://github.com/garfield-cpp/HGSFusion/blob/fae255340620513dfc7cf9691d098b70bd5af406/pcdet/datasets/kitti/vod_dataset.py#L108)：data/vod_radar_5frames、ImageSets/val.txt、kitti_infos_val.pkl、7维点云、image_2/*.jpg、calib及混合点*.pkl.npy。dataset配置另有vod_lidar路径，需按实际调用区分必需程度。
- G4：[混合点生成](https://github.com/garfield-cpp/HGSFusion/blob/fae255340620513dfc7cf9691d098b70bd5af406/hybrid_pts/README.md)需要Mask2Former/Detectron2/Swin-L；已有缓存可不重跑。点目录名1:4是比例，不等于只有5点；[作者确认](https://github.com/garfield-cpp/HGSFusion/issues/3#issuecomment-2726431230)。
- G5：[测试parser](https://github.com/garfield-cpp/HGSFusion/blob/fae255340620513dfc7cf9691d098b70bd5af406/tools/test.py#L22)为--ckpt，README误写--ckpy。默认launcher=none。未来候选python tools/test.py --cfg_file tools/cfgs/hgsfusion/hgsfusion_vod.yaml --ckpt ACTUAL_CHECKPOINT --batch_size 1。
- 权重和混合点链接在[README](https://github.com/garfield-cpp/HGSFusion/blob/fae255340620513dfc7cf9691d098b70bd5af406/README.md#L46)；云盘内部文件清单未验证。DeepLabV3骨干另需权重，README .pt与配置.pth/相对路径不一致。
- Python3.9.18、Torch1.13/cu116、MMCV2.1/MMDet3.3；spconv未精确固定，PillarNet实际使用稀疏卷积，另需Pillar/NMS/PointNet/BEV等扩展。通用旧OpenPCDet安装文档不是已验证安装锁。
- [作者训练配置说明](https://github.com/garfield-cpp/HGSFusion/issues/3#issuecomment-2789071080)为四3090、每卡batch1；当前train.py有单进程入口及可选SyncBN，但单卡修改改变全局batch和训练统计。load_params_from_file使用strict=False，必须审未更新键。

当前原样L1入口不满足；L2还缺缓存、权重完整性和评估实测；L3还需复核SyncBN与重复训练差异。只有小范围官方弃用适配经另行授权后才值得试导入，本轮不修。

## R4Det：同一固定版本的复核

版本：9418d11949f41e802b583d99e69c825387082094，与第一轮相同。

- R1：[模型R4Det/IGDRModule](https://github.com/VDIGPKU/R4Det/blob/9418d11949f41e802b583d99e69c825387082094/mmdet3d/models/detectors/R4Det.py#L42)与[TemporalDeformableFusion](https://github.com/VDIGPKU/R4Det/blob/9418d11949f41e802b583d99e69c825387082094/mmdet3d/models/fusion_layers/temporal_r4det_fusion.py#L104)真实存在；支持BEV/实例/时序研究。
- R2：公开configs/r4det只有TJ4D预训练/最终配置。README VoD示例的configs/sgdet3d/vod-R4Det_det3d_2x4_12e.py不在该树。test_VoD.sh占位路径、8卡启动，不能直接应用。
- R3：[TJ4D最终配置](https://github.com/VDIGPKU/R4Det/blob/9418d11949f41e802b583d99e69c825387082094/configs/r4det/TJ4D-R4Det_det3d_2x4_12e.py#L501)：480×640、samples_per_gpu=4；深度绝对路径；max_epochs18、freeze_images=True。预训练亦18 epochs，另引用图像和radar-only初始化。arXiv v2描述15+15及第二阶段全解冻；本轮没证明二者指标一致。
- R4：[tools/test_vod.py](https://github.com/VDIGPKU/R4Det/blob/9418d11949f41e802b583d99e69c825387082094/tools/test_vod.py)支持--launcher none和single_gpu_test。TJ4D候选：python tools/test_vod.py --config configs/r4det/TJ4D-R4Det_det3d_2x4_12e.py --checkpoint ACTUAL_FINAL_TJ4D --eval mAP --launcher none。cfg使用val.pkl与论文test名称的样本对应尚待核实。
- R5：[HF](https://huggingface.co/Hoeyy/R4Det/tree/main)列final_tj4d、pretrained_tj4d及TJ4D-ADDI（约38.2GB）；未验证VoD对应产物。分割、annotation mask、深度、info和顺序历史帧需要逐项匹配。Metric3D伪深度监督见论文；生成工具与检查点的闭环未核实。
- 环境声明Ubuntu/Python3.8/Torch2.0.1/cu118、MMCV-full1.7.1、MMDet2.28.2、定制Detectron2/NATTEN及多套算子。实际主模型还import Pyro4，顶层requirements未列；vod devkit是另一个已知依赖。
- 作者论文报告单3090推理测速，不代表20GB峰值。论文训练全局batch32，两阶段多模块优化，单卡重训成本风险高。

VoD L2当前不满足配置/权重闭环；TJ4D L1/L2部分验证；L3训练协议未闭合。先补VoD资源或选择TJ4D，不能按文件名“12e”推断18/15 epoch配置。

## MAFF-Net：指定候选的主线专项核查

版本：0bb253fbeebb0813d40b957e1e802e57690d6ed3。真实RA-L论文，不因不符合融合主线而贬低论文质量。

- A1：[MAFF_Net](https://github.com/TRV-Lab/MAFF-Net/blob/0bb253fbeebb0813d40b957e1e802e57690d6ed3/pcdet/models/detectors/MAFF_Net.py)与VoD/TJ4D配置、train.py/test.py存在。
- A2：[CQCA_cfa.forward:90–108](https://github.com/TRV-Lab/MAFF-Net/blob/0bb253fbeebb0813d40b957e1e802e57690d6ed3/pcdet/models/backbones_image/CQCA_cfa.py#L90)输入batch_dict['points']，输出spatial_features_img与cluster_points；这里“img”只是变量名，不能当作照片输入证据。
- A3：[VoD数据配置](https://github.com/TRV-Lab/MAFF-Net/blob/0bb253fbeebb0813d40b957e1e802e57690d6ed3/tools/cfgs/dataset_configs/vod_dataset_radar.yaml#L16)只有GET_ITEM_LIST=['points']，7维雷达；绝对DATA_PATH需未来适配。info生成模块入口在docs/guidance/dataset.md。SPA/CQCA/CDA提供强雷达对照而不是现成Radar-Camera融合模型。
- 两个checkpoint链接分别对应两份配置；Release页存在，但完整资产下载/参数匹配未验证。未来官方命令：python tools/test.py --cfg_file tools/cfgs/MAFF-Net/MAFF-Net_vod.yaml --batch_size 1 --ckpt checkpoints/vod2025010810360.pth。
- 声明Ubuntu20.04、Python3.8、Torch1.10.1/cu113、spconv-cu113，spconv/其他依赖未完整锁定；训练说明单4090、batch4、60epochs，不是20GB通过记录。
- 雷达-only L1/L2/L3均仍缺实际环境/数据/运行证据；作为融合主基线不满足，作为强雷达分支对照可保留。为其新增相机、融合和语言分支会扩大任务，不能把这称为“最小复现准备”。

## 共同风险与安全边界

1. 没有访问实验室服务器；实际系统、显卡、可用显存、驱动、nvcc、编译器、磁盘/配额、读写权限均未验证。不能用本地Windows替代。
2. 单卡推理、完整验证、微调、全量训练需要分别验收。所有候选均为：**单 GPU 20GB 可运行性尚未验证。**
3. 新驱动向后兼容不代表扩展可编译；分别记录驱动、Torch CUDA构建、Toolkit、GPU架构、编译器及实际算子执行。不能因为nvidia-smi显示较新CUDA就整体升级历史框架。
4. 数据规模未逐文件盘点，不给总存储量承诺；MSSF包/HF附加文件、SG发布包、R4 TJ4D附加包大小仅是已读远端元数据，不含原始数据与环境空间。
5. 归档中的pickle/checkpoint未反序列化；平台安全扫描标签不当作文件安全或加载成功证明。
6. 探测某个猜测文件404不构成缺代码证据：例如MSSF custom_runner是包，实际fast_runner.py已定位；真正缺口需完整树或实际无条件导入佐证。
7. R4Det/CVFusion/HGSFusion重查SHA未变，保留第一轮同版本源码证据；没有把旧问题永久化，也没有新增虚构运行结果。
