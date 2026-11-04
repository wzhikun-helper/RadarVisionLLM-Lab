# P003 CenterFusion Lesson 02归档记录

归档日期2026-11-04（Asia/Shanghai）；研究分支`research/p003-p005-reading-reproduction-20261103`，起点`9c497f49c3a0a2c7b68e93daf49f0a0b606ddbbb`。原main仍有24个修改与4个未跟踪文件，已记录状态/哈希，不混入本轮；研究工作区起初干净。首次远程查询TLS握手失败，使用HTTP/1.1且保持证书校验后重试成功，远程与本地Lesson 01提交一致，无意外提交。

## 本轮归档与依据

- [精读Step 2](../../paper_notes/P003_CenterFusion.md#lesson02)：背景/动机、单目深度、教学针孔公式、雷达距离、数据关联、20/40 m教师案例、研究思路及假设边界。
- [真实问答与补学](../research_log/P003_CenterFusion_REVIEW.md#lesson02-review)：Q1 PASS，Q2未通过，02-R1 PASS；原答逐字保留，教师三条纠正单列，未将补答改成标准答案。
- [概念宝典](../../paper_notes/P003_概念查询宝典.md#p003-c10)：C10/C11复用原定义补应用，C12关联辨析，C13测量/预测；既有C02/C09补Lesson 02限定，不复制新宝库。
- 证据复用已核WACV PDF（仓库外），SHA-256 `a0b8711eabb881c05ead46278985e93c79a9b0efb923774ad5c416e565c53574`；§1位于PDF1–2、Fig.1位于PDF2，关联解释辅助参照§4.2。全文来源与版本见[Lesson 01报告](P003_LESSON01_ARCHIVE_20261104.md)。本轮没有新增论文实验数值或图片。
- 教师案例只给A20 m、B40 m及补答中的B8 m/s；未给A速度、像素或模型输出，不补造。错关联引入B观测不代表A预测固定等于观测。
- [P001精读](../../paper_notes/P001_论文精读.md)与[概念宝典](../../paper_notes/P001_概念查询宝典.md)结构继续沿用；P001/P002正文不改。已有三个候选仅作研究启发引用，未新增未经查新的候选或实验。

## 当前状态与计划映射

Lesson 01保留原PASS及01-R1过程，Lesson 02 PASS，实验复现NOT_STARTED。按用户本次明确要求，P003下一课为Lesson 03 Related Work NOT_STARTED；将仅含待填字段的Related Work/Methodology/Experiments占位按新计划排为Step3/4/5，不将其当作已授课记录。早期学习日志/维护报告中的旧待验收状态与顺序保留历史，不篡改原验收。P004/P005及旧RaCFormer、R4Det资料与状态不变。

## 检查和剩余缺口

实际检查结果见[Lesson 02验证JSON](P003_LESSON02_CHECKS_20261104.json)。本轮只提交下列范围，提交SHA/推送核验在最终交付报告提供，不预填成功状态。

补学三道题的完整原题、授课/验收日期与时长、完整对话导出尚未提供。Lesson 03、源码学习、服务器配置验证、数据/权重/环境、训练/评估/消融、候选查新与验证均未完成，未运行任何模型。针孔关系为理想教学模型，20/40 m为教学案例，不冒充论文图表/实验或本项目实测。

## 修改文件清单

- `docs/research_log/P003_CenterFusion_REVIEW.md`
- `paper_notes/P003_CenterFusion.md`
- `paper_notes/P003_概念查询宝典.md`
- `docs/research_log/P003_CenterFusion_READING_LOG.md`
- `docs/maintenance/RESEARCH_STATUS.json`
- `papers/paper_matrix.csv`
- `README.md`
- `paper_notes/README.md`
- `papers/README.md`
- `papers/P003_CenterFusion/README.md`
- `reproductions/P003_CenterFusion/README.md`
- `docs/research_log/P003_P005_SECTION_SYNC.md`
- `docs/maintenance/P003_LESSON02_ARCHIVE_20261104.md`
- `docs/maintenance/P003_LESSON02_CHECKS_20261104.json`
