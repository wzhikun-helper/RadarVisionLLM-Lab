# 整理变更报告｜2026-10-30

原HEAD：`20f21172642ba1f4f47cb6dacf0016a06af15d75`。图片移动14个，删除0个；正式笔记仅改图片标记，科学正文、表格、公式和重点标记保持一致。

新增：

- `docs/maintenance/DELETE_WHITELIST.md`
- `docs/maintenance/FILE_MANAGEMENT_GUIDE.md`
- `docs/maintenance/LEGACY_ASSET_REVIEW.md`
- `docs/maintenance/REPOSITORY_AUDIT.md`
- `docs/maintenance/REPOSITORY_INVENTORY.csv`
- `docs/maintenance/REPOSITORY_ORGANIZATION_STATE.json`
- `docs/maintenance/REPOSITORY_CHANGE_REPORT.md`

修改：

- `.gitignore`
- `README.md`
- `docs/roadmap.md`
- `papers/paper_matrix.csv`
- `paper_notes/P001_概念查询宝典.md`
- `paper_notes/P001_论文精读.md`
- `paper_notes/P002_CRN.md`
- `paper_notes/P002_概念查询宝典.md`
- `paper_notes/README.md`
- `scripts/README.md`
- `scripts/validate_lab.py`
- `docs/maintenance/CRN_FIRST_PASS_AUDIT.md`
- `docs/maintenance/CRN_FIRST_PASS_STATE.json`

图片移动逐项原/现路径、SHA与大小见[状态清单](REPOSITORY_ORGANIZATION_STATE.json)。初始统计见审计；最终统计与实际验证输出见状态清单。

P002学习状态已按用户确认更新，问答证据缺口仍保留。P003=R4Det、P004=MSSF均未开始，没有创建空白正式笔记。没有训练、复现、安装或模型修改。删除白名单为空。

Git仅定向暂存本轮路径；共享已修改文件采用本轮补丁增量，既有改动保留在工作区。当前旧P001资料有大量既有未提交/未跟踪内容，不因本轮而全量上传。提交与远程最终SHA以Git历史及交付回复为准。

仓库结构与学习索引已可支持P003 R4Det第一遍精读；不代表R4Det作为工程基线已通过准入，其VoD/资源缺口仍按原审查报告保留。

## 最终验证快照

整理前172个文件、73,896,699字节；整理后180个文件，总大小和各目录逐项计数见状态清单的after_bytes及after_directories。新增8个文件（含.gitattributes）、移动14张图、修改14个现有文件、实际删除0。三份只读入口退出码均为0。

.gitattributes仅对两份新纳入Git的P001原始Markdown允许行末空格及文件末尾空行，保留作者Markdown硬换行和段落结尾；其余空白检查继续启用，科学正文未据此改写。

Git范围限制：现有共享README、roadmap、matrix及scripts/README如含此前改动，暂存HEAD加本轮附加段/定点字段；用户原有差异保留在工作区。本轮显式纳入原已存在但未跟踪的P001正式笔记、配套索引和维护校验依赖，因为它们是本轮重组后的必要成果；没有将其它未改动的科研文件批量暂存。仓库本来已有大量未发布历史素材，本轮不声明远程已包含全部本地文件，GitHub上的全量本地资源验收仍需那些既有文件另行审阅提交。
