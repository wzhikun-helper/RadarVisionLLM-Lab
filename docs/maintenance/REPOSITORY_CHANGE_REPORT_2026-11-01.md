# 仓库治理交付：2026-11-01

基线：`c0ee5b5ee6b25fb7a09a51177d26e05c399abda4`。独立分支：`codex/repository-maintenance-20261101`。从main创建干净工作副本，原`D:/RadarVisionLLM-Lab`的前序修改、未跟踪和忽略资产保留；不直接推main。完整初始盘点见[审计](REPOSITORY_AUDIT_2026-11-01.md)和[资产清单](REPOSITORY_INVENTORY_2026-11-01.json)。

## A. 审计结论

原本地完整验证通过，HEAD全部已解析Markdown目标未发现缺失，但公开文件范围与本地资料范围不同。主要问题：脏工作区误提交风险（高）；19份已提交Markdown的转义标题/列表/格式问题、首页完整旧README内嵌、状态分散（中）；原问答、第四次规划原文、教学图制作链及实际工程准入证据缺口（中）。没有发现精确SHA重复组或>=10MiB文件，也没有本轮高置信敏感模式命中，不能据此保证不存在所有秘密。

## B. 前后结构与必要变化

原主要目录不变；无科研资料移动或删除。新增少量治理文件：RESEARCH_STATUS.json提供唯一当前状态；REPOSITORY_GUIDE.md解释目录/权威来源；RESEARCH_WORKFLOW.md定义角色、两遍法及证据交付。旧Git首页正文完整保存在history/README_BEFORE_2026-11-01.md，首页改为单一当前入口，不覆盖原工作区未提交首页。

19份既有Markdown仅修开头被转义的标题/列表/分隔线、显示用粗体转义及多余空行/表格行间空行，代码围栏内容和学术字词保留；其中docs/README.md、docs/roadmap.md及scripts/reproductions/experiments/results索引另补当前规范入口，明确初始化里程碑是历史规划。不是将原本地未提交版本复制进分支。

## C. 完整文件变更清单

| 路径 | 动作/职责 |
| --- | --- |
| `.gitignore` | 修改（只在整理分支）：补凭证文件名/本地账户目录保护 |
| `README.md` | 修改（只在整理分支）：当前首页去重；原Git版本保留快照 |
| `data/README.md` | 修改（只在整理分支）：Markdown显示格式；必要处追加导航 |
| `docs/README.md` | 修改（只在整理分支）：Markdown显示格式；必要处追加导航 |
| `docs/RESEARCH_WORKFLOW.md` | 新增（只在整理分支） |
| `docs/innovation_bank/idea_template.md` | 修改（只在整理分支）：Markdown显示格式；必要处追加导航 |
| `docs/learning_notes/00_git_and_research_engineering.md` | 修改（只在整理分支）：Markdown显示格式；必要处追加导航 |
| `docs/maintenance/P001_CURRENT_STATE.json` | 修改（只在整理分支）：仅更新合法当前文档哈希，不重写历史来源 |
| `docs/maintenance/REPOSITORY_AUDIT_2026-11-01.md` | 新增（只在整理分支） |
| `docs/maintenance/REPOSITORY_CHANGE_REPORT_2026-11-01.md` | 新增（只在整理分支） |
| `docs/maintenance/REPOSITORY_GUIDE.md` | 新增（只在整理分支） |
| `docs/maintenance/REPOSITORY_INVENTORY_2026-11-01.json` | 新增（只在整理分支） |
| `docs/maintenance/REPOSITORY_PLAN_2026-11-01.md` | 新增（只在整理分支） |
| `docs/maintenance/REPOSITORY_VALIDATION_2026-11-01.json` | 新增（只在整理分支） |
| `docs/maintenance/RESEARCH_STATUS.json` | 新增（只在整理分支） |
| `docs/maintenance/history/README_BEFORE_2026-11-01.md` | 新增（只在整理分支） |
| `docs/research_protocol.md` | 修改（只在整理分支）：Markdown显示格式；必要处追加导航 |
| `docs/roadmap.md` | 修改（只在整理分支）：Markdown显示格式；必要处追加导航 |
| `docs/weekly_reports/weekly_report_template.md` | 修改（只在整理分支）：Markdown显示格式；必要处追加导航 |
| `experiments/README.md` | 修改（只在整理分支）：Markdown显示格式；必要处追加导航 |
| `experiments/templates/experiment_template.md` | 修改（只在整理分支）：Markdown显示格式；必要处追加导航 |
| `figures/README.md` | 修改（只在整理分支）：Markdown显示格式；必要处追加导航 |
| `manuscript/README.md` | 修改（只在整理分支）：Markdown显示格式；必要处追加导航 |
| `paper_notes/templates/paper_note_template.md` | 修改（只在整理分支）：Markdown显示格式；必要处追加导航 |
| `reproductions/README.md` | 修改（只在整理分支）：Markdown显示格式；必要处追加导航 |
| `reproductions/RECORDING_STANDARD.md` | 修改（只在整理分支）：复用原规范补证据阶段与完整run字段 |
| `reproductions/templates/reproduction_template.md` | 修改（只在整理分支）：Markdown显示格式；必要处追加导航 |
| `results/README.md` | 修改（只在整理分支）：Markdown显示格式；必要处追加导航 |
| `scripts/README.md` | 修改（只在整理分支）：Markdown显示格式；必要处追加导航 |
| `scripts/validate_lab.py` | 修改（只在整理分支）：保留full规则、增加明确tracked范围与状态/格式/安全检查 |
| `src/README.md` | 修改（只在整理分支）：Markdown显示格式；必要处追加导航 |
| `writing/README.md` | 修改（只在整理分支）：Markdown显示格式；必要处追加导航 |
| `writing/academic_phrasebook.md` | 修改（只在整理分支）：Markdown显示格式；必要处追加导航 |

移动：0。删除：0。科研语义变更：0。需审批的资产合并/删除/大迁移没有执行项。旧P001英文名文件的本地删除继续保持原未提交状态，不由本轮代为提交或恢复。

## D. 科研状态

以[唯一状态源](RESEARCH_STATUS.json)及原证据为准：P001精读完成但教师原始题答缺，复现Not Run；P002第一遍与此前用户确认通过状态保留，原题答/批改缺，代码精读Not Started，复现Deferred/Not Run。P003 R4Det仅Pre-readiness，P004 MSSF两遍Not Started。MSSF-PP/VoD为重点核查候选而非已部署主基线，SGDet3D等为其他候选；没有任何本项目模型成功复现记录。

## E. 验证结果与明确范围

实际输出见[验证记录](REPOSITORY_VALIDATION_2026-11-01.json)。分别运行原工作区默认完整检查、增强脚本对原工作区的full检查、整理分支tracked文档治理范围及git diff --check。tracked不是默认full的替代，不把不含本地历史素材的干净工作副本当作完整资产副本；没有调整历史检查为虚假通过。原默认full检查逻辑保留，缺少私有资产时仍应报错。

对链接漂移和状态漂移执行负例回归，确认会失败；所有测试产生的临时文件只在干净工作副本创建并移除，不接触原资料。JSON/CSV/Python语法、忽略探针和高置信敏感模式按实际范围检查。整理分支无YAML文件；原目录两份未跟踪YAML没有可用PyYAML完整解析，明确未执行，未安装依赖。不将所有HTTP链接、全部锚点、所有密钥模式或科研结论列为已认证。

## F. Git交付与合并建议

只显式暂存本清单文件到整理分支，审查没有数据/权重/私钥/本地环境内容。普通推送分支，不覆盖main。实际commit和远程SHA在最终交付中核验，不将提交自身哈希写回形成循环。PR建议标题：`chore(repo): clarify research workflow and repository governance`。

合并前检查：

- [ ] 审查本轮全部差异，确认格式变化未改变科学内容，状态源没有超出证据。
- [ ] 对照原D盘未提交文件：本轮不包含这些增量，合并时需逐个保护/协调；不要直接用分支版本覆盖本地文件。
- [ ] 确认新状态源与用户最新安排一致，并补《第四次学习规划》原文入口。
- [ ] 区分公开tracked通过与完整本地资产full通过；合并后刷新合法当前哈希，保留历史来源指纹。
- [ ] 未审批资产删除/合并/大迁移，不因本PR合并而自动开始P003、安装或训练。

## G. 遗留问题

原工作区未提交修改与未跟踪科研资产仍需单独审阅；原始问答、教师批改、部分图片制作链及第四次规划原文缺失；服务器配额/数据许可/权重/配置/评价链尚未闭合。历史不同阶段/编号按原日期保留，不依据它们覆盖当前编号。没有以新规范重建原规划或捏造历史学习/运行证据。

## H. 下一步（不超过五项）

1. 审阅整理分支及与原工作区重叠的文件，确认保全后再决定是否合并。
2. 提供第四次规划原文、真实原问答和教师批改，建立可追溯链接。
3. 补教学图来源与授权链，核查P002候选处置。
4. 教师确认P003阅读版本和第一遍准入；本轮不启动。
5. 工程侧先补MSSF-PP/VoD资源/许可/评估证据，取得有界授权后才执行模型检查。
