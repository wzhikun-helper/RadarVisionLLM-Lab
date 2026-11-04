# P003 CenterFusion Lesson 01归档记录

日期：2026-11-04；起点提交`a622d73971627e8d8713c8eab3001753b3193562`；目标研究分支`research/p003-p005-reading-reproduction-20261103`。远程起点相同，独立工作区干净；原main的24个修改与4个未跟踪文件归属已知，本轮保持不动、不暂存。

## 模板与正式路径

沿用[精读](../../paper_notes/P001_论文精读.md)、[概念宝典](../../paper_notes/P001_概念查询宝典.md)、[问答验收](../research_log/P001_REVIEW.md)的真实结构。P001/P002原文件不改写。没有创建第二套概念宝库，P003继续使用[已有宝典](../../paper_notes/P003_概念查询宝典.md)。

## 用户证据与状态

[独立验收原文](../research_log/P003_CenterFusion_REVIEW.md)逐字保留首轮三答及连续补学原答，教师判定/四条纠正单列。首轮Q1未通过→补学01-R1通过→最终Lesson 01=PASS；Q2/Q3首轮通过。实际授课/验收时间与完整聊天导出未提供，不编造日期或教师身份。Introduction与复现执行均NOT_STARTED；不是整篇论文通过。

## 论文证据

正式PDF：[WACV 2021原文](https://openaccess.thecvf.com/content/WACV2021/papers/Nabati_CenterFusion_Center-Based_Radar_and_Camera_Fusion_for_3D_Object_Detection_WACV_2021_paper.pdf)。10页，印刷1527–1536；SHA-256：`a0b8711eabb881c05ead46278985e93c79a9b0efb923774ad5c416e565c53574`。web工具403，但通过只读HTTP下载取得PDF，在仓库外提取正文并渲染相关页核对；不把抓取失败写成证据缺失，也不将PDF加入仓库。

- PDF1 / Abstract：主任务、方法与作者结果声明。
- PDF2 / Fig.1及融合分类：关联后的特征融合再预测，不是最终框的简单合并。
- PDF3–5 / §3–4、Fig.2–4：中心/速度/视锥说明，RCS不自动等于已用通道。
- PDF6–7 / §5–6与Table 1：配置与test/val的不同backbone、原始NDS/mAP/mAVE，区分相对与绝对提升。
- 摘要无额外时序信息的表述需结合§3.1的3雷达sweeps理解；不解释为完全没有历史输入。源码细节未检查，未运行任何模型。

## 概念和科研记录

C01/C02扩充已有草稿；C03–C08对既有概念补CenterFusion应用与来源，保持P001/P002基本定义唯一；新增C09测量错误/关联错误辨析。所有教学公式与自拟例子标明用途，不当作论文创新或原图。P003-I01–I03为Candidate / Unverified，10列想法表不填主观评分，无查新或实验成功声明。

## 保留、验证及未完成

P001/P002、P004/P005、旧RaCFormer路径及正文、R4Det历史原文均保留；历史初始化审计不重写。最新检查见[验证结果](P003_LESSON01_CHECKS_20261104.json)。只读检查覆盖Markdown链接、CSV/JSON、编号、状态、原话保存与受保护文件哈希；不认证模型或教师能力。未安装环境、未下载数据/权重、未操作服务器、未训练/评估/消融。

后续：Lesson 02尚未开始；代码、数据、权重、依赖、服务器配置、复现与候选查新均未完成。Git提交与远程核验结果在最终交付中报告，不预填SHA。

## 本轮文件清单

- `docs/research_log/P003_CenterFusion_REVIEW.md`
- `paper_notes/P003_CenterFusion.md`
- `paper_notes/P003_概念查询宝典.md`
- `docs/research_log/P003_CenterFusion_READING_LOG.md`
- `docs/research_log/P003_P005_SECTION_SYNC.md`
- `docs/innovation_bank/P003_P005_RESEARCH_QUESTIONS.md`
- `docs/innovation_bank/P003_ideas.csv`
- `docs/maintenance/RESEARCH_STATUS.json`
- `papers/paper_matrix.csv`
- `README.md`
- `paper_notes/README.md`
- `papers/README.md`
- `papers/P003_CenterFusion/README.md`
- `reproductions/P003_CenterFusion/README.md`
- `docs/maintenance/P003_LESSON01_ARCHIVE_20261104.md`
- `docs/maintenance/P003_LESSON01_CHECKS_20261104.json`
