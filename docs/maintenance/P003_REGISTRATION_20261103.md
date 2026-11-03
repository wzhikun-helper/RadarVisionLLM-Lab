# P003编号安全调整记录｜2026-11-03

## 决策、时间与证据

日期：2026-11-03（Asia/Shanghai）。用户明确选择RaCFormer（CVPR 2025）为正式P003，暂停R4Det。此前2026-11-02撤销待选论文的提交为`c055359154b9662e930b2e6c5f0d2bc266cff21c`；本轮不撤销该提交、不改Git历史，而是新增明确的历史入口。

- [正式P003档案](../../papers/P003_RaCFormer/README.md)；[唯一正式笔记](../../paper_notes/P003_RaCFormer.md)；[历史R4Det入口](../../papers/H-R4Det-2026/README.md)。
- 论文身份来自[arXiv v2摘要和元信息](https://arxiv.org/abs/2412.12725v2)及[固定官方README](https://github.com/cxmomo/RaCFormer/blob/4d4c534f84acef9ec390523134367aad40619057/README.md)。没有阅读全文后声称完成精读，没有执行作者代码。
- P003状态来源为本次用户指令：Abstract已讲授，等待用户开放题回答；原题、答案及批改未提供，未标记通过。目标为nuScenes / RaCFormer-R50 / RTX 4090 D 24GB；这是用户指定资源，不是实测硬件或运行结果。
- R4Det当前状态同样来自用户：暂停第一遍精读，第一课未验收；不修改原始准备报告中的历史状态。检索当前文件、全部本地分支及Git历史，未发现冲突的既有H-R4Det-2026编号。

## 原始资料保留策略

当前main没有R4Det目录，但治理分支`codex/repository-maintenance-20261101`和历史提交仍有两份准备资料。原始准备资料从`c0ee5b5ee6b25fb7a09a51177d26e05c399abda4`逐字节恢复到历史入口，不删除、不覆盖、不重命名任何现有文件。其他R4Det历史比较、JSON审查证据及分支保持原样。历史报告中的P003=R4Det与P004=MSSF不作为当前注册状态；历史证据不改写为新的科研事实。

| 原路径 | 恢复路径 | 字节数 | SHA-256 |
| --- | --- | --- | --- |
| `papers/P003_R4Det/README.md` | [papers/H-R4Det-2026/ORIGINAL_README.md](../../papers/H-R4Det-2026/ORIGINAL_README.md) | 1451 | `24cae872082a8cc88fe5b55c9b39d4b703bbba9e071a762f2ebe962f385f4640` |
| `papers/P003_R4Det/01_pre_readiness.md` | [papers/H-R4Det-2026/01_pre_readiness.md](../../papers/H-R4Det-2026/01_pre_readiness.md) | 8301 | `42838bbdb5790e1c0ec87b5e5f49d7e7b66cf1e33e833f675e7ccf022683e71c` |

原入口与准入正文保持原始字节。恢复后目录深度相同，保留原相对链接。旧论文原始资料存在于本地Git历史，不能根据远程当前目录缺失推断其不存在。

## 当前与历史状态分离

当前main此前无RESEARCH_STATUS.json，故新增[当前研究状态](RESEARCH_STATUS.json)，不将治理分支中未合并的旧状态直接拷贝到main。该治理分支仍有P003=R4Det及P004=MSSF的历史设定，**未来合并必须另行协调状态冲突**；本次不合并、不修改该分支。当前P004未选定，不重新登记MSSF。P001/P002状态以现有验收入口为依据，正文不改写。

## 本轮文件变更清单

- `paper_notes/README.md`
- `README.md`
- `papers/README.md`
- `papers/paper_matrix.csv`
- `papers/H-R4Det-2026/README.md`
- `papers/P003_RaCFormer/README.md`
- `paper_notes/P003_RaCFormer.md`
- `papers/H-R4Det-2026/ORIGINAL_README.md`
- `papers/H-R4Det-2026/01_pre_readiness.md`
- `docs/maintenance/RESEARCH_STATUS.json`
- `docs/maintenance/P003_REGISTRATION_20261103.md`

## 工作区保护与提交方式

执行前main与远程main均为`c055359154b9662e930b2e6c5f0d2bc266cff21c`。已有24个修改文件及4个未跟踪文件，暂存区为空。README.md与paper_notes/README.md有既有修改；仅构造基于HEAD的本轮独立登记补丁，不把两文件的原有修改加入提交。其他22个修改文件及4个未跟踪文件不暂存、不改写。papers/README.md与papers/paper_matrix.csv开始时干净。

本轮主矩阵仅追加P003一行，原36列及P001/P002原始行字节不变；未核实属性留空。不新增训练结果、复现结论或教师反馈。未安装环境、下载数据/权重、编译模型、训练或评估。

## 验证与尚未完成事项

- `python -B scripts/validate_lab.py`：退出码`0`。
- `python -B scripts/check_public_docs.py --include-untracked`：退出码`0`。
- `git diff --check`：退出码`0`。
- 既有文件只有上述4个索引/矩阵被本轮增量修改；其余原始文件哈希不变，P001/P002正式正文与现有图片均不变。
- 两份R4Det恢复原文SHA与源提交完全一致；主矩阵36列、P001/P002原行不变、ID唯一。
- 链接检查覆盖本轮文件与当前仓库Markdown相对路径，不将历史编号文字当作当前注册。

原开放题、用户回答、教师批改和教学原文仍待提供。未核对整篇论文方法公式与实验，未完成代码级审查或模型准入。HTTP资源仅核对论文摘要、固定代码页面与README，不声称全部历史外链、PDF、模型资源均可用。

Git提交和推送结果在最终交付中给出；本文件不预填尚未产生的提交SHA或同步成功结论。
