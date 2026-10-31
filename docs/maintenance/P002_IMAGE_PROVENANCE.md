# P002七张图片来源审查

2026-10-31。A=论文原始图表文件；B=论文截图/裁剪；C=确认根据论文重绘的教学图；D=其他已确认资料；E=来源暂无法确认。类别表示来源证据强度，不只是图片看起来像什么。静态视觉核对基于第二轮逐图检查，本轮重新计算原字节SHA并核查引用；不重新生成或修改图片。

正式依据：用户CRN ICCV2023 PDF（12页，SHA-256 `e833ebf328d1eaecb0536699c9f29a13e36616e4ae0cfd6aa874d762a1f10296`）；[正式来源登记](../../papers/P002_CRN_RECORD.md)。后三张表格版式、行列及数值对应原文，截图创建时间与软件不作推断。

| 文件与SHA-256 | 分类/图片类型 | 是否来自论文原图及版本 | PDF页/印刷页 | 图表号 | 正文位置 | 裁剪/重绘/自制判断 |
| --- | --- | --- | --- | --- | --- | --- |
| [Pasted image 20261028091506.png](../../paper_notes/assets/P002_CRN/Pasted%20image%2020261028091506.png)<br>`f1b62d85e2772678dac8bc1af1c1df6aa0b8c6340eb94c8ba8ecbfbb66b58d1f` | E：BEV教学示意；外观为自制/组合图，历史制作证据不足 | 不属于CRN原Figure；对应概念2.1 | 无 | 无 | 精读§2.1 L72 | 不是原论文裁图；是否自制及素材来源待核 |
| [Pasted image 20261028142231.png](../../paper_notes/assets/P002_CRN/Pasted%20image%2020261028142231.png)<br>`7ac2431f5ea214dda30683af3b2828f837f6833375e111ec4cc8a66bb4b9ed07` | E：CRN流程教学示意；疑为重绘但不能确认制作来源 | 相关S2 §3/Fig.2，不等同原图 | 无 | 无 | 精读§3.1 L119 | 重新绘制外观；制作者/底图/工具日志未知 |
| [Pasted image 20261028193811.png](../../paper_notes/assets/P002_CRN/Pasted%20image%2020261028193811.png)<br>`deaa34a9b8dbb10c8cd2e07cc3520ba2c750061f4dea67fae3fcd3c8f7da2d76` | E：RVT教学示意；疑为按论文重绘 | 相关S2 §3.2/Fig.3，不是原图 | 无 | 无 | 精读§3.2 L125 | 重绘外观；不能用相关图号冒充直接来源 |
| [Pasted image 20261028195714.png](../../paper_notes/assets/P002_CRN/Pasted%20image%2020261028195714.png)<br>`cf80fe106e531e7a5187209ce7f93cc0ccecd21b8df27499d5a9ff6be375c085` | E：MDCA教学示意；疑为按机制绘制 | 相关S2 Eq.7，不是原Figure | 无 | 无 | 精读§3.3.1 L177 | 重绘外观；制作者/原始素材待用户确认 |
| [Pasted image 20261030141556.png](../../paper_notes/assets/P002_CRN/Pasted%20image%2020261030141556.png)<br>`74cbc895f9c4d1ff254f3de91b9256f1ff720b019d5231a1411af168bd234a0c` | B：论文表截图/裁图，含学习标色 | ICCV2023正式PDF | 6 / 17620 | Table 1 | 精读§4.2 L271 | 裁剪及黄色标记可见；未重绘数值 |
| [Pasted image 20261030141648.png](../../paper_notes/assets/P002_CRN/Pasted%20image%2020261030141648.png)<br>`47d59ec293429e85fa01ad0eb071ae094497406c53423e1a83c20e972f832e4c` | B：论文表截图/裁图，包含caption | ICCV2023正式PDF | 7 / 17621 | Table 5 | 精读§4.3.1 L278 | 已裁剪；未发现重绘证据 |
| [Pasted image 20261030141736.png](../../paper_notes/assets/P002_CRN/Pasted%20image%2020261030141736.png)<br>`dd9102c0aab2ec3f80f75ee7aec0549f24e8508a433268e434c9c59b510c4d0b` | B：论文表截图/裁图，包含caption | ICCV2023正式PDF | 7 / 17621 | Table 6 | 精读§4.3.2 L284 | 已裁剪；未发现重绘证据 |

前四图不标C，是因为缺少用户确认、源工程/生成提示词、制作记录及底层素材来源；“教学示意”外观可以识别，但不能据此证明具体重绘链。取得这些证据后才从E改为C或D。全部保留，未发现A类原始矢量/原图源文件。E不是假图判定，不因此删除。

[精读](../../paper_notes/P002_CRN.md)的7个图片引用均指向上述现存资产；[概念宝典](../../paper_notes/P002_概念查询宝典.md)没有独立图片嵌入，不添加重复图片。历史行号随编辑可能变化，章节为稳定定位。图片字节、SHA及本轮验证见[执行状态](EVIDENCE_ROUND3_STATE.json)。
