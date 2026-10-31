# P001 Table IV数值勘误：35.9 / 36.0

日期：2026-10-31。先形成此勘误，再执行用户本轮授权的定点修订。证据层级：论文原文事实与本项目静态核查，不是模型结果。

## 两个版本分别核对

| 版本 | 来源与指纹 | 页/表/行/列 | 数值 |
| --- | --- | --- | --- |
| 最终发表版，RA-L 7(2)，2022，4961–4968，DOI 10.1109/LRA.2022.3147324 | 本地原论文SHA-256 `d19bf8e168da7af27924ddaa55c42a4a395e681a15bbc40346f8502b292dfdfa`；[机构正式版本登记](https://research.tudelft.nl/en/publications/multi-class-road-user-detection-with-31d-radar-in-the-view-of-del/) | PDF p6 / 印刷4966，Table IV，PP-radar行，Entire annotated area / Car | 35.9 |
| 作者接受预印版，页眉Accepted January 2022 | [作者公开PDF](https://intelligent-vehicles.org/wp-content/uploads/2022/02/palffy2022ral_view_of_delft.pdf)；下载副本SHA-256 `3ad8c1b0f34802d5b0770b9551ccb9b39825e18ac979ac8175534a2e4eb8c908` | PDF p6，Table IV，同一行与列 | 35.9 |

两版表题均表示“全部测试方法在完整标注区域及Driving Corridor内的结果”。两版§V位于PDF p5：VoD，按clip分train/val/test为59%/15%/26%，同一clip不跨集合，表格为测试结果；类别Car/Pedestrian/Cyclist。单扫描PP-radar用完整Radar特征，表列x/y/z/RCS/补偿径向速度；它不同于no-Doppler、3 scans、5 scans及LiDAR行。Car AP按3D IoU0.5；另外两类阈值0.25。35.9是整区域Car AP，不是三类mAP38.0，也不是走廊Car AP74.1。

## 差异归因及修订

结论归类 **A：原笔记相对于上述原文的转录数值错误**。两个实际核对版本均为35.9，未发现支持B“版本差异”的证据；两版同样保留一位小数，不支持C“按该表精度四舍五入成36.0”。原始写作过程未保存，不能进一步推测由手打、OCR还是其他环节造成。未声称排查了所有历史私有稿件。

修订范围仅限[正式精读](../../paper_notes/P001_论文精读.md)§6.2“额外结果”中的Car 36.0→Car 35.9。其余文字、章节、公式、表格和引用不变。第二轮补充保留原勘误发现并追加本次已修订指针，不回写历史审计为当时已修复。相关[图表索引](../../figures/library/P001/FIGURE_INDEX.md)及[复现计划](../../reproductions/P001_PointPillars_VoD/README.md)未发现另一处需要改动的单帧Car数值；其中mAP38.0不是错误，不替换。

旧/新SHA与精确补丁见[本轮执行状态](EVIDENCE_ROUND3_STATE.json)及Git差异。图片不变，数据/模型未运行。维护清单只更新当前内容的哈希，源副本和历史审计的旧指纹保留。
