# 仓库增删改查规范

## 分类与存放

A正式科研成果长期保留；B来源、勘误、日志与验证证据保留；C独有历史讲稿/提示词/素材保留；D重复或可再生成制作产物仅列候选、审批后处理；E秘密/数据/权重/环境/缓存不进入Git。目录不是删除依据。

## 新增

论文放paper_notes，更新该目录README和papers/paper_matrix.csv；主矩阵36列与P001导入表23列不得混用。图片放assets/论文编号；未选定的论文不提前创建空白正式笔记。
实验代码放src或对应reproductions子目录；配置放experiments；日志和指标放按唯一实验ID建立的目录，登记Git SHA、数据版本/划分、种子、环境、命令、输出与成功判据。数据、权重不提交。

## 修改

修改前保存Git状态与文件SHA。保留笔记标题、表格、公式、重点标记和教师批改；记录理由、核对图片和索引；只更新明确合法变化对应的预期哈希，不能将全部磁盘状态无条件当新基线。图片用标准Markdown相对路径；含空格和中文的路径使用URL编码。图片宽度如需保留，存标题元数据，显示宽度由阅读器决定。Obsidian原库不动。

## 删除

检查不是唯一资料、不是正式成果、没有有效引用、不影响历史验收，列大小、哈希、保留副本及恢复方式；得到逐项授权后才删除并更新清单。SHA相同只能证明字节重复，不能证明所有依赖可删除。历史目录、ZIP和未跟踪文件不等于垃圾。

## 查询：PowerShell示例

```powershell
Set-Location D:\RadarVisionLLM-Lab
Get-ChildItem paper_notes -Filter '*P002*'
Get-ChildItem paper_notes/assets/P002_CRN
rg -n 'assets/|!\[|!\[\[' paper_notes
rg -n '来源|Table|Fig|假设' docs/innovation_bank docs/research_gaps
rg -n 'experiment_id|run_id|配置|指标|日志' experiments reproductions results
git log --follow -- paper_notes/P002_CRN.md
git diff -- paper_notes/P002_CRN.md
Get-ChildItem paper_notes,work,presentations -File -Recurse | Get-FileHash -Algorithm SHA256 | Group-Object Hash | Where-Object Count -gt 1
python -B scripts/validate_lab.py
```

## Git

先查status和暂存区；有他人暂存内容即停止。本次变更路径明确列出后逐项add，禁用add .和add -A。共享文件存在本轮前修改时，按补丁暂存本轮增量，其他改动留在工作区；新依赖文件明确纳入提交范围。执行git diff --cached --check。禁止reset --hard、clean -fd、强推；远程冲突/认证失败停止，不自动合并。核验远程SHA后才报告同步成功。

## 学习状态

P002第一遍及全文理解验收通过来自本轮用户确认；原始问答证据独立登记。代码精读未开始、复现未执行。后续论文预定安排已撤下，待用户决定。基线推荐顺序与阅读编号分开记录，未改变已有基线审查结论。
