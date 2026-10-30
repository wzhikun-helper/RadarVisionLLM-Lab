# 最终建议与7天最小行动计划

日期：2026-10-30。只结束本轮审查与报告同步；不启动P003正式精读、安装、编译或模型运行。

## 决策

1. **最先精读建议：MSSF。** 论文正式发表于T-ITS，公开全文可核查融合阶段、语义头等消融；与CRN知识衔接，且不以最新SOTA为唯一标准。LXL作为采样/占用机制对照。教师核准前不启动正式精读。
2. **最先补齐官方评估准入：MSSF-PP / VoD。** 官方包内配套配置与epoch_40目录关系已静态核实；明确选PP版本，不混用Voxel版或仓库近似配置。仍缺权重实际匹配、数据、服务器、二进制环境和显存证据，不能写“已具备运行条件”。
3. **长期主代码基线：暂未找到合格基线。** MSSF是条件优先，必须先通过资源/许可、L1、L2和小型可训练性验收。分数86不是成功概率。
4. **第一候选失败后的第二候选：SGDet3D / VoD。** 只针对可取得完整预处理/发布资源且补齐论文质量证据的条件；若其辅助产物和旧环境成本过高，再看LXL的VoD路线，不同时搭三套环境。
5. HP-C4D先解决最终checkpoint与V2-99初始化来源；MAFF-Net只做雷达对照；R4Det的VoD缺口、CVFusion无核心代码和HGSFusion弃用导入均未因本轮而解除。
6. 新发现的RaGS/RPGFusion保留观察，SGDet3D++/RCVLA/Radar4D-VLM用于创新重叠检查，不为了“接大模型”立即转向更昂贵的系统。

证据：[候选总表](01_candidate_papers.md)、[代码审查](02_code_audit.md)、[评分依据](03_reproducibility_ranking.md)、[创新假设](04_innovation_opportunities.md)。

## 本轮真正取得与未取得的证据

已取得：9个仓库API固定提交与筛选文件树、RaGS只读HEAD引用、新候选说明/配置/测试parser/关键模型源码、MSSF压缩包目录与一份配置、公开论文部分消融、旧候选相同SHA复核。SGDet3D发布页可列final/pretrained资产，但有界ZIP请求返回501，未读取整包。

没有取得：实验室服务器访问与硬件记录；数据授权证明或逐样本完整性；权重张量匹配；候选环境导入/算子运行日志；本项目前向/指标/训练记录；任何模型20GB峰值显存。IEEE部分页面JS验证、GitHub API后续403限流、云盘访问限制均按未验证保留。

论文/README指标为作者报告；issue是外部复现者或作者说明；本轮HTTP、Git只读查询和文件核查是实际检查结果。三者不混同。**单 GPU 20GB 可运行性尚未验证。**

## 7天计划：每天最多3小时，一次一个工程目标

| 天 | 单一目标与前置条件 | 最小验收 / 停止条件 |
|---|---|---|
| D1 | 教师与用户共同复核报告；只读 | 确定是否优先MSSF-PP/VoD以及接受发布版本的指标目标；未定则不部署 |
| D2 | 资源清单闭合；需要数据保管人/授权情况 | 验证VoD授权、val样本ID、7维点云、图像/标定/标签、kitti_infos_val.pkl与velodyne_reduced；记录存在/齐全/可加载三个不同状态。无数据则停止安装 |
| D3 | 服务器只读盘点；需要明确访问入口 | 系统、GPU/可用显存、驱动、nvcc、GCC、磁盘/配额、共享内存、权限有实际输出；没有入口则只列未确认，不借本地Windows替代 |
| D4 | 固定单一路线的环境/资源方案；需D2/D3通过 | 锁定代码和HF版本、配置、初始化/检测权重、许可边界；形成唯一安装与构建方案，标明可逆变更、输出目录、预计空间；教师未批准不安装 |
| D5 | 经另行明确授权后才进行最小环境/算子检查 | 只验证关键导入、MMCV/spconv及所需算子；不用训练来检验安装。遇无法经济解决的依赖链则记录并转备选，不顺带升级全框架 |
| D6 | 经Level1授权后单真实样本前向 | 验证ID/标定/特征顺序、checkpoint未加载键、有限且有效的框/类别/置信度、峰值显存与耗时；不计算论文指标，不以batch1保证20GB |
| D7 | 审阅Level1日志并决定Level2申请 | 检查完整val预算、token/ID集合、评估器和指标协议；另行授权后才运行完整评估。未通过则保留Conditional Go，不启动训练 |

这不是本轮自动执行清单。D5/D6依赖后续授权和真实资源，不能因时间到了就自动通过。总预算上限21小时；训练、大模型和多候选环境不放入这7天默认任务。

## 安全的服务器只读信息采集（本轮未执行）

```bash
uname -srmo
cat /etc/os-release
getconf GNU_LIBC_VERSION
nvidia-smi
nvidia-smi --query-gpu=name,driver_version,memory.total,memory.used,memory.free,compute_mode --format=csv
command -v python python3 nvcc gcc g++ cmake ninja
python3 -B -I --version
nvcc --version
gcc --version
g++ --version
free -h
df -hT
df -i
df -h /dev/shm
ulimit -n
```

获准目录再检查ls -ld、findmnt -T和test -r/-w/-x；不使用touch证明权限，不打印全部环境变量、密码、token或私钥。目录权限位不等于有配额/管理员授权。先确认驱动、Torch CUDA构建、Toolkit和GPU架构；不能由nvidia-smi里的“CUDA Version”推断本机编译环境。

## Level 1正式启动前准入

- 数据授权及研究使用环境允许；至少一个真实样本和全部引用元数据/图像/点云完整，特征顺序正确。
- 固定代码SHA、资源版本及配套配置；检测权重和初始化资源来源已确认；后续下载时记录大小/SHA256，不反向编造本轮校验值。
- 对MSSF确认历史环境实际可构建；不是只让pip结束或版本断言通过。
- 明确输出目录与可逆修改范围，保留现有用户工作区；模型加载的pickle风险按来源审查，不在本轮反序列化。
- 已有真实GPU、磁盘、配额、权限证据；预先定义OOM/依赖失败后的停止规则，不自动降分辨率后声称官方配置复现。

## Level 2正式启动前准入

- Level1有实际日志，checkpoint关键键/形状匹配；不能只看strict=False无报错。
- 使用完整固定官方val划分；数据ID与预测ID逐项一致，不以小子集指标替代；数据类别顺序、坐标系/框尺寸、FoV筛选一致。
- 记录EAA/DC、IoU阈值、R11/R40/插值方式、3D/BEV及过滤规则；与对应论文/发布版本表格逐项对齐，不能默认不同仓库evaluator相同。
- 实测batch1峰值显存、加载/评估速度和存储预算；单卡前向成功不自动批准全量训练。
- 输出完整日志、结果文件、配置和版本标识；偏差如实报告，不挑子集、换划分或混用作者重训数字。

## Level 3与长期基线的额外门槛

训练代码及损失可追溯；初始化权重齐全；全局batch/学习率/epoch/SyncBN与论文差异可解释；至少一个固定预算消融可以重复；代码修改和再发布授权范围清楚。单GPU微调与单GPU完整训练分别评估。VLM需要另建数据和对照协议，不把闭集检测AP当语言理解证据。

## 本轮写入和Git同步范围

用户本轮附件明确允许创建五份报告，并在远程/授权及公开内容检查通过后提交推送。本轮唯一计划写入目录为：

docs/research_gaps/baseline_selection_round2/

文件为01_candidate_papers.md、02_code_audit.md、03_reproducibility_ranking.md、04_innovation_opportunities.md、05_decision_and_plan.md。创建前目录不存在，父目录非链接；不覆盖现有文件。

开始时分支main，HEAD为8c9abc543a89ec5169e0c4dff75c703f29772d55；已有大量用户修改/未跟踪文件及一项既有删除，暂存区为空。只允许本轮五份文档进入提交，不能使用git add .、清理、reset、恢复删除、强推或把既有改动带入。

远程origin为https://github.com/wzhikun-helper/RadarVisionLLM-Lab.git。现有.gitignore覆盖常见数据/权重/缓存/.env/*.key/credentials.*等，但不是穷尽的保密保证；不改忽略规则，以本轮文件白名单和内容审查控制同步。报告只含公开来源与用户已授权项目计划，不含原始数据、权重、访问凭据或服务器秘密。

最终提交SHA、推送是否成功及远程核验结果在对话交付中给出，不在提交前预填成功状态。遇认证/非快进等失败则仅保留本地报告与实际提交，不强推、不拉取合并、不声称已同步。

## 停止点

完成五份报告和本轮允许的同步后停止，等待用户与ChatGPT教师审查。当前结论为 **Conditional Go（仅继续补证），不是部署Go；暂未找到合格长期主基线。**
