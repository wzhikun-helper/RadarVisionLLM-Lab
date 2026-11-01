# 仓库只读审计：2026-11-01

审计根目录：`D:/RadarVisionLLM-Lab`。原HEAD：`c0ee5b5ee6b25fb7a09a51177d26e05c399abda4`；main与远程main只读核验一致。完整目录、Git分类、文件大小及非敏感资产SHA见[盘点](REPOSITORY_INVENTORY_2026-11-01.json)。不记录凭证值；敏感路径若发现不计算内容哈希。

## 1. Git与已有修改

暂存区为空；本地有前序未提交修改和未跟踪资产，其来源仅能确认“本轮前已存在”，具体作者/时间不能从Git推断。完整路径按盘点Git状态保存。对这些文件不覆盖、不暂存、不代为提交；保留原工作区在main。采用从原HEAD创建的独立分支/工作副本实施低风险治理，最终只推整理分支，不覆盖main。

## 2. 完整目录盘点

本地文件218个；Git索引110路径（含1个本地已删除路径）；未跟踪107；忽略2。以下是相对根目录完整文件路径，`.git`内部不扫描：

```text
.gitattributes
.github/workflows/docs.yml
.gitignore
archive/ARCHIVE_MANIFEST.md
archive/cleanup_2026-10-17/manifest.csv
archive/cleanup_2026-10-17/presentations/P001_Paper_Review/P001_Paper_Review_Visual_Exact.verification.json
archive/cleanup_2026-10-17/presentations/P001_Radar_Detection_Prerequisite/backups/20261017_before_image_rebuild/P001_Speaker_Notes.md
archive/cleanup_2026-10-17/presentations/P001_Radar_Detection_Prerequisite/backups/20261017_before_image_rebuild/README.md
archive/cleanup_2026-10-17/README.md
archive/cleanup_2026-10-17/work/p001_ppt_build/cases.png
archive/cleanup_2026-10-17/work/p001_ppt_build/curves.png
archive/cleanup_2026-10-17/work/p001_ppt_build/scene.png
archive/cleanup_2026-10-17/work/p001_ppt_build/sensor.png
archive/cleanup_2026-10-17/work/p001_prereq_build/paper.txt
archive/retired_ppt_work/README.md
CONTRIBUTING.md
data/README.md
docs/innovation_bank/idea_template.md
docs/innovation_bank/P001_ideas.csv
docs/innovation_bank/P001_INNOVATION_NOTES.md
docs/innovation_bank/P002_CRN_INNOVATION_NOTES.md
docs/innovation_bank/P002_ideas.csv
docs/innovation_bank/P002_NOVELTY_REVIEW_20261031.md
docs/learning_notes/00_git_and_research_engineering.md
docs/learning_notes/01 RadarVisionLLM-Lab：FMCW、回波与多普勒基础.md
docs/maintenance/CRN_FIRST_PASS_AUDIT.md
docs/maintenance/CRN_FIRST_PASS_STATE.json
docs/maintenance/DELETE_WHITELIST.md
docs/maintenance/EVIDENCE_ROUND3_STATE.json
docs/maintenance/FILE_MANAGEMENT_GUIDE.md
docs/maintenance/LEGACY_ASSET_REVIEW.md
docs/maintenance/P001_CURRENT_STATE.json
docs/maintenance/P001_EVIDENCE_ERRATA.md
docs/maintenance/P001_history.zip
docs/maintenance/P001_P002_CONSISTENCY_AUDIT.md
docs/maintenance/P001_P002_CONTENT_AUDIT.md
docs/maintenance/P001_P002_CONTENT_AUDIT_STATE.json
docs/maintenance/P001_P002_DOSSIER_ROUND1.md
docs/maintenance/P001_P002_DOSSIER_ROUND1_STATE.json
docs/maintenance/P001_P002_PARITY_MATRIX.md
docs/maintenance/P001_P002_PARITY_STATE.json
docs/maintenance/P001_TABLE_IV_ERRATUM.md
docs/maintenance/P002_ALIGNMENT_STATE.json
docs/maintenance/P002_IMAGE_PROVENANCE.md
docs/maintenance/P002_MATRIX_REGISTRATION.json
docs/maintenance/README.md
docs/maintenance/REPOSITORY_AUDIT.md
docs/maintenance/REPOSITORY_CHANGE_REPORT.md
docs/maintenance/REPOSITORY_INVENTORY.csv
docs/maintenance/REPOSITORY_ORGANIZATION_STATE.json
docs/README.md
docs/research_gaps/baseline_selection_round2/01_candidate_papers.md
docs/research_gaps/baseline_selection_round2/02_code_audit.md
docs/research_gaps/baseline_selection_round2/03_reproducibility_ranking.md
docs/research_gaps/baseline_selection_round2/04_innovation_opportunities.md
docs/research_gaps/baseline_selection_round2/05_decision_and_plan.md
docs/research_gaps/P001_CONTENT_SUPPLEMENT.md
docs/research_gaps/P001_Limitations_Research_Gap.md
docs/research_gaps/P002_CRN_CONTENT_SUPPLEMENT.md
docs/research_gaps/P002_CRN_Limitations_Research_Gap.md
docs/research_log/P001_ARCHIVE_REPORT.md
docs/research_log/P001_READING_REPORT.md
docs/research_log/P001_REVIEW.md
docs/research_log/P002_CRN_READING_REPORT.md
docs/research_log/P002_CRN_REVIEW.md
docs/research_log/research_log_template.md
docs/research_protocol.md
docs/roadmap.md
docs/weekly_reports/weekly_report_template.md
experiments/README.md
experiments/templates/config_template.yaml
experiments/templates/experiment_template.md
figures/library/P001/FIGURE_INDEX.md
figures/library/P001/paper_page_01_reference.png
figures/library/P001/paper_page_04_reference.png
figures/library/P001/paper_page_06_reference.png
figures/library/P001/paper_page_07_reference.png
figures/library/P002/FIGURE_INDEX.md
figures/README.md
manuscript/README.md
NOTICE.md
paper_notes/assets/P001/ChatGPT Image 2026年9月23日 15_22_18.png
paper_notes/assets/P001/ChatGPT 图像 2026年9月29日 11_04_16.png
paper_notes/assets/P001/ChatGPT 图像 2026年9月29日 15_17_15.png
paper_notes/assets/P001/Pasted image 20261009152348.png
paper_notes/assets/P001/Pasted image 20261014185700.png
paper_notes/assets/P001/Pasted image 20261014185737.png
paper_notes/assets/P001/Pasted image 20261019144201.png
paper_notes/assets/P002_CRN/Pasted image 20261028091506.png
paper_notes/assets/P002_CRN/Pasted image 20261028142231.png
paper_notes/assets/P002_CRN/Pasted image 20261028193811.png
paper_notes/assets/P002_CRN/Pasted image 20261028195714.png
paper_notes/assets/P002_CRN/Pasted image 20261030141556.png
paper_notes/assets/P002_CRN/Pasted image 20261030141648.png
paper_notes/assets/P002_CRN/Pasted image 20261030141736.png
paper_notes/P001_概念查询宝典.md
paper_notes/P001_论文精读.md
paper_notes/P002_CRN.md
paper_notes/P002_概念查询宝典.md
paper_notes/README.md
paper_notes/templates/paper_archive_checklist.md
paper_notes/templates/paper_note_template.md
papers/P001_PointPillars_VoD/README.md
papers/P002_CRN/README.md
papers/P002_CRN_RECORD.md
papers/P003_R4Det/01_pre_readiness.md
papers/P003_R4Det/README.md
papers/paper_matrix.csv
papers/paper_matrix_P001_import.csv
papers/README.md
presentations/HISTORY.md
presentations/P001_Paper_Review/assets/fig4_original.png
presentations/P001_Paper_Review/assets/fig5_original.png
presentations/P001_Paper_Review/assets/paper_page_06_220dpi.png
presentations/P001_Paper_Review/P001_Paper_Review_Speaker_Notes.md
presentations/P001_Paper_Review/README.md
presentations/P001_Paper_Review/slide_content.json
presentations/P001_Paper_Review/sources.md
presentations/P001_Paper_Review/verify_visual_exact.py
presentations/P001_paper_review_images/01_Cover.png
presentations/P001_paper_review_images/01_Cover_prompt.md
presentations/P001_paper_review_images/02_Visual.png
presentations/P001_paper_review_images/03_Visual.png
presentations/P001_paper_review_images/04_Visual.png
presentations/P001_paper_review_images/05_Visual.png
presentations/P001_paper_review_images/06_Visual.png
presentations/P001_paper_review_images/07_Visual.png
presentations/P001_paper_review_images/08_Visual.png
presentations/P001_paper_review_images/09_Visual.png
presentations/P001_paper_review_images/10_Visual.png
presentations/P001_paper_review_images/11_Visual.png
presentations/P001_paper_review_images/12_Visual.png
presentations/P001_paper_review_images/13_Visual.png
presentations/P001_paper_review_images/14_Visual.png
presentations/P001_paper_review_images/generation_prompts.json
presentations/P001_paper_review_images/image_manifest.json
presentations/P001_paper_review_images/README.md
presentations/P001_Radar_Detection_Prerequisite/assets/notes_image_rebuild.json
presentations/P001_Radar_Detection_Prerequisite/assets/slide-01.png
presentations/P001_Radar_Detection_Prerequisite/assets/slide-02.png
presentations/P001_Radar_Detection_Prerequisite/assets/slide-03.png
presentations/P001_Radar_Detection_Prerequisite/assets/slide-04.png
presentations/P001_Radar_Detection_Prerequisite/assets/slide-05.png
presentations/P001_Radar_Detection_Prerequisite/assets/slide-06.png
presentations/P001_Radar_Detection_Prerequisite/assets/slide-07.png
presentations/P001_Radar_Detection_Prerequisite/assets/slide-08.png
presentations/P001_Radar_Detection_Prerequisite/assets/slide-09.png
presentations/P001_Radar_Detection_Prerequisite/assets/text-fit.json
presentations/P001_Radar_Detection_Prerequisite/assets/validation.json
presentations/P001_Radar_Detection_Prerequisite/P001_Speaker_Notes.md
presentations/P001_Radar_Detection_Prerequisite/README.md
presentations/P001_Radar_Detection_Prerequisite/sources.md
presentations/P001_slide_images/01_Cover.png
presentations/P001_slide_images/02_FMCW.png
presentations/P001_slide_images/03_Radar_Dimensions.png
presentations/P001_slide_images/04_Radar_Point_Cloud.png
presentations/P001_slide_images/05_Radar_Pipeline.png
presentations/P001_slide_images/06_PointPillars.png
presentations/P001_slide_images/07_Temporal_Accumulation.png
presentations/P001_slide_images/08_Detection_Metrics.png
presentations/P001_slide_images/09_Knowledge_Summary.png
presentations/P001_slide_images/generation_prompts.json
presentations/P001_slide_images/image_manifest.json
presentations/P001_slide_images/README.md
presentations/README.md
README.md
reproductions/P001_PointPillars_VoD/.gitignore
reproductions/P001_PointPillars_VoD/experiment_tracker.csv
reproductions/P001_PointPillars_VoD/README.md
reproductions/P002_CRN/experiment_tracker.csv
reproductions/P002_CRN/README.md
reproductions/README.md
reproductions/RECORDING_STANDARD.md
reproductions/templates/reproduction_template.md
results/README.md
scripts/__pycache__/maintenance_paths.cpython-312.pyc
scripts/__pycache__/validate_lab.cpython-312.pyc
scripts/check_public_docs.py
scripts/maintenance_paths.py
scripts/README.md
scripts/validate_lab.py
src/README.md
work/p001_exact_current_build.txt
work/p001_prereq_supplied_images/convert.mjs
work/p001_prereq_supplied_images/manifest.json
work/p001_prereq_supplied_images/renders/01.png
work/p001_prereq_supplied_images/renders/02.png
work/p001_prereq_supplied_images/renders/03.png
work/p001_prereq_supplied_images/renders/04.png
work/p001_prereq_supplied_images/renders/05.png
work/p001_prereq_supplied_images/renders/06.png
work/p001_prereq_supplied_images/renders/07.png
work/p001_prereq_supplied_images/renders/08.png
work/p001_prereq_supplied_images/renders/09.png
work/p001_prereq_supplied_images/validation.json
work/p001_prereq_supplied_images/verification.json
work/p001_visual_exact_20261017T100548/finalize-options.json
work/p001_visual_exact_20261017T100548/manifest.json
work/p001_visual_exact_20261017T100548/renders/01.png
work/p001_visual_exact_20261017T100548/renders/02.png
work/p001_visual_exact_20261017T100548/renders/03.png
work/p001_visual_exact_20261017T100548/renders/04.png
work/p001_visual_exact_20261017T100548/renders/05.png
work/p001_visual_exact_20261017T100548/renders/06.png
work/p001_visual_exact_20261017T100548/renders/07.png
work/p001_visual_exact_20261017T100548/renders/08.png
work/p001_visual_exact_20261017T100548/renders/09.png
work/p001_visual_exact_20261017T100548/renders/10.png
work/p001_visual_exact_20261017T100548/renders/11.png
work/p001_visual_exact_20261017T100548/renders/12.png
work/p001_visual_exact_20261017T100548/renders/13.png
work/p001_visual_exact_20261017T100548/renders/14.png
work/p001_visual_exact_20261017T100548/validation.json
work/p001_visual_exact_20261017T100548/verification.json
work/README.md
work/verify_p001_exact_current.py
writing/academic_phrasebook.md
writing/README.md
```

## 3. 主要科研资产

- 正式精读/概念各2份位于paper_notes，14张原图按P001/P002分组，哈希基线完整。
- P001/P002十项独立入口与十二类档案矩阵、三轮审计保留；三轮P00135.9定点勘误是当前有效值。
- P002创新五项外部查新、7图来源分类已完成记录；原问答和教学图来源缺口保留。
- P003只有两份R4Det准备档案，P004 MSSF未开始；现有代码审查和基线排序不是学习编号。
- MSSF-PP/VoD仅条件重点核查候选；P001 Planned、P002 Deferred，均无本项目成功模型复现。
- 历史P001 ZIP、课件视觉稿/来源/提示词和制作记录是科研来源资产，未跟踪不等于无用。

## 4. 重复与职责冲突

全量非Git文件精确SHA重复组0；没有据文件名判断内容重复。重名路径见盘点，README/模板同名通常职责不同。未发现>=10MiB大文件（实际大文件表以盘点为准）。
首页内嵌另一份完整历史README，读者易混淆当前/历史状态；同一进度在多个说明中重复维护。Git仍跟踪旧P001_MultiClass_Road_User_Detection.md，而本地已有未提交删除；不擅自提交该删除，旧文件按历史来源识别，不取代当前正式笔记。

## 5. 文档与引用

现有完整本地validate_lab.py返回0，Markdown本地目标可解析；但这不等于GitHub目标齐全。HEAD全部Markdown的Git树核查发现下列未发布目标：

| 来源 | 目标 | 问题 |
| --- | --- | --- |

HEAD公开目标成功解析340项；受转义标题影响文件19份，详见盘点。修复活动入口可定位链接；历史证据中的旧链接保留并明确报告，不能为零报错抹去历史。

## 6. 科研状态一致性

P001精读完成、教师原始验收Evidence Missing、复现Not Run；P002第一遍及此前用户确认的理解验收完成，原题答/批改Evidence Missing，代码精读Not Started、复现Not Run；P003 R4Det Pre-readiness，P004 MSSF Not Started。现有第四次学习规划原文未在仓库中定位，不能凭记忆重写；保留既有两遍法和任务授权边界，待用户提供原文再建立引用。历史记录中不同编号和当时待合并等表述不覆盖。

## 7. 风险分级

| 级别 | 问题 | 处理 |
| --- | --- | --- |
| 高 | 直接在脏工作区重写/批量暂存会覆盖或混入前序科研修改 | 干净独立工作副本、显式路径提交；原目录字节保护 |
| 中 | 本地与HEAD公开链接不同，旧P001文件删除未提交，首页历史快照重复 | 活动导航修复、历史首页单独保全；不提交旧笔记删除 |
| 中 | 状态多处复制，环境/前向/评价/复现证据层级易混 | 唯一状态源和生成式首页表；补统一证据阶段 |
| 中 | 第四次学习规划原文、原问答、部分图来源、服务器资源证据缺失 | 标记缺口，不编造或自动进入学习/模型阶段 |
| 低 | 缓存/未跟踪制作资料、Markdown转义与检查工具职责重叠 | 不删文件；复用validate_lab，新公开范围明确说明，不提交旧重复工具 |

## 8. 建议及本轮范围

见[方案/路径对照](REPOSITORY_PLAN_2026-11-01.md)。允许继续首页/导航/规范/工具范围改进；任何科研资产合并、删除或整体搬迁本轮不做，后续须逐项审批。

## 9. 不应修改

四份正式笔记、14图、原始问答/历史批改、CSV原始记录、旧ZIP、来源/提示词/实验记录、模型代码/配置、原工作区全部前序修改。根README只在独立分支编辑；原工作区README完全保留。

## 10. 实际检查及限制

现有本地验证脚本exit0；JSON基本格式未报错；没有发现本轮高置信密钥模式或敏感文件名命中，但这不是完整密钥审计，不输出任何可疑值。2个忽略缓存仍保留。PyYAML未预装，未为此安装；YAML完整语法检查需复用可用解析器或明确登记未执行，不能称已通过。没有运行训练/推理/评估。完整结果见盘点；远程只读SHA已核验，未依赖公开页面代替本地检查。
