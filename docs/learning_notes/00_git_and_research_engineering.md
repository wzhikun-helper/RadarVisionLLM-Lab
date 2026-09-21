\# 00 Git and Research Engineering / Git 与科研工程化



\## 1. What Did I Learn? / 我学了什么？



In this stage, I created the initial engineering structure of the RadarVisionLLM-Lab research project and learned the basic Git workflow.



本阶段完成了 RadarVisionLLM-Lab 科研项目的工程初始化，并学习了 Git 最基础的版本管理流程。



Completed:



已完成：



\* Installed and verified Git / 安装并验证 Git

\* Created the research project / 创建科研项目

\* Initialized a Git repository / 初始化 Git 仓库

\* Created the first repository structure / 建立第一版科研目录

\* Created README documents / 建立 README 文档

\* Created `.gitignore` / 建立 `.gitignore`

\* Created research protocol / 建立科研规范

\* Created research roadmap / 建立科研路线图

\* Completed the first Git commit / 完成第一次 Git 提交



\---



\# 2. What Is Git? / Git 是什么？



Git is a distributed version-control system.



Git 是一个分布式版本控制系统。



For research, Git can record:



在科研中，Git 可以记录：



\* Code changes / 代码修改

\* Experiment scripts / 实验脚本

\* Configuration changes / 配置变化

\* Documentation / 科研文档

\* Figure-generation scripts / 图片生成脚本

\* Research progress / 科研进度



The most important purpose is traceability.



最重要的价值是：



\*\*Traceability / 可追溯性\*\*



For example:



例如未来我们得到：



```text

EXP-023

Motion Accuracy = 84.7%

```



We should be able to determine:



我们应该能够查到：



```text

Git Commit

Dataset Split

Config

Random Seed

Model

Evaluation Script

```



也就是回答：



> 这个实验到底是用哪一版代码跑出来的？



\---



\# 3. What Is a Repository? / Repository 是什么？



A Git repository is a project directory managed by Git.



Git Repository 可以理解为：



\*\*被 Git 进行版本管理的项目文件夹。\*\*



Our repository is:



```text

D:\\RadarVisionLLM-Lab

```



After running:



```bash

git init

```



Git created:



```text

.git/

```



This hidden directory stores Git metadata and version history.



`.git` 是 Git 的内部版本数据库。



Do not manually delete or modify `.git`.



不要手动删除或修改 `.git`。



\---



\# 4. `git init`



Command:



```bash

git init

```



Purpose:



用途：



Convert the current directory into a Git repository.



把当前普通文件夹初始化为 Git 仓库。



Our output was:



```text

Initialized empty Git repository in D:/RadarVisionLLM-Lab/.git/

```



Meaning:



说明 Git 已经开始管理 RadarVisionLLM-Lab。



\---



\# 5. `git status`



Command:



```bash

git status

```



Purpose:



用途：



Check the current state of the repository.



查看当前 Git 仓库状态。



Before the first commit, we saw:



```text

On branch main

No commits yet

```



Meaning:



含义：



\* `main` is the current branch / 当前处于 main 分支

\* There was no saved Git version yet / 当时还没有任何 commit



We also saw:



```text

Untracked files

```



Meaning:



Git discovered these files but had not started tracking them.



表示 Git 已经发现这些文件，但尚未正式纳入版本管理。



\---



\# 6. Working Directory, Staging Area, Repository



Git can be understood using three layers:



Git 最核心的模型可以理解成三层：



```text

Working Directory

工作区

&#x20;     ↓

&#x20;  git add

&#x20;     ↓

Staging Area

暂存区

&#x20;     ↓

&#x20; git commit

&#x20;     ↓

Repository History

版本历史

```



\## Working Directory / 工作区



The files currently being edited.



当前正在修改的文件。



For example:



```text

README.md

research\_protocol.md

roadmap.md

```



\---



\## Staging Area / 暂存区



Files selected for the next commit.



准备进入下一次 commit 的文件。



Command:



```bash

git add .

```



The `.` means:



`.` 表示：



Current directory and all eligible files below it.



当前目录及其所有允许 Git 跟踪的内容。



Important:



重要：



`git add` does NOT create a permanent version.



`git add` 并不等于“提交”。



它只是把文件放进：



\*\*Staging Area / 暂存区\*\*



\---



\# 7. What Is a Commit? / Commit 是什么？



A commit is a version snapshot.



Commit 可以理解成：



\*\*科研项目在某个重要时间点的一张正式版本快照。\*\*



Command:



```bash

git commit -m "init bilingual research repository"

```



Our first commit was:



```text

e87f073

```



Commit message:



```text

init bilingual research repository

```



This is the first commit of RadarVisionLLM-Lab.



这是 RadarVisionLLM-Lab 项目的第一次正式版本提交。



\---



\# 8. Why Is the Commit ID Important? / Commit ID 为什么重要？



Each commit has a unique identifier.



每次 commit 都有一个唯一标识。



Example:



```text

e87f073

```



Future experiments should record their code version.



未来正式实验可以记录：



```text

Experiment ID:

EXP-023



Git Commit:

e87f073

```



Then the experiment can be traced back to the exact source-code version.



这样以后就能准确恢复实验时所使用的代码版本。



\---



\# 9. What Is `.gitignore`? / `.gitignore` 是什么？



`.gitignore` tells Git which files should not be tracked.



`.gitignore` 用来告诉 Git：



> 哪些文件不要进入版本管理。



Examples that should usually NOT enter Git:



通常不应直接进入 Git 的内容：



```text

Large datasets

大型数据集



Model weights

模型权重



Checkpoints

训练 checkpoint



Temporary files

临时文件



Passwords

密码



API keys

API 密钥



Private credentials

私人凭证

```



Examples that SHOULD usually enter Git:



通常应该进入 Git：



```text

Source code

代码



Configuration

配置文件



README

说明文档



Experiment scripts

实验脚本



Data split descriptions

数据划分说明



Paper notes

论文笔记



Small processed results

小型处理结果

```



\---



\# 10. Why Does Git Ignore Empty Folders? / 为什么 Git 不记录空文件夹？



Git tracks files, not directories themselves.



Git 本质上跟踪的是文件，而不是空文件夹。



Therefore:



因此：



```text

papers/

```



如果完全为空，Git 通常不会记录它。



This is one reason important directories contain:



这也是为什么重要目录通常要建立：



```text

README.md

```



README has two purposes:



README 同时承担两个作用：



1\. Explain what the directory is for / 说明目录用途

2\. Allow the directory structure to be tracked / 让目录结构能够进入版本管理



\---



\# 11. Why Do Research Projects Need README Files? / 为什么科研项目需要 README？



A README is not decoration.



README 不是装饰文件。



It answers:



它应该回答：



```text

What is this project?

这个项目是什么？



What problem are we studying?

研究什么问题？



How is the repository organized?

目录怎么组织？



How should the code be run?

代码怎么运行？



Where are experiments stored?

实验放在哪里？



How can results be reproduced?

怎么复现实验结果？

```



The root README is the navigation page of the whole research project.



根目录 README 是整个科研项目的总导航入口。



\---



\# 12. Current Repository Structure / 当前仓库结构



The project currently contains:



目前核心结构包括：



```text

RadarVisionLLM-Lab/

│

├── README.md

├── .gitignore

│

├── docs/

│   ├── README.md

│   ├── research\_protocol.md

│   ├── roadmap.md

│   ├── learning\_notes/

│   ├── research\_log/

│   ├── weekly\_reports/

│   └── innovation\_bank/

│

├── papers/

├── paper\_notes/

├── reproductions/

├── data/

├── src/

├── experiments/

├── results/

├── figures/

├── scripts/

├── writing/

└── manuscript/

```



\---



\# 13. Research Engineering Principle / 科研工程化原则



Our project follows:



我们的核心原则是：



```text

Result

结果

&#x20;↓

Experiment

实验

&#x20;↓

Configuration

配置

&#x20;↓

Code

代码

&#x20;↓

Git Commit

版本

```



Every important result should be traceable.



每一个正式科研结果最终都应该可以追溯。



Do not rely on memory such as:



不能依赖这种科研方式：



> “我记得当时好像改了一个参数，所以效果变好了。”



Instead, record:



应该变成：



```text

EXP-015



Changed:

Doppler feature ON



Baseline:

EXP-012



Git Commit:

xxxxxxx



Result:

+3.2%



Conclusion:

...

```



\---



\# 14. Commands Learned / 已学习命令



Check Git version:



检查 Git 版本：



```bash

git --version

```



Initialize repository:



初始化仓库：



```bash

git init

```



Check status:



查看仓库状态：



```bash

git status

```



Add files to staging area:



加入暂存区：



```bash

git add .

```



Create commit:



创建提交：



```bash

git commit -m "message"

```



View commit history:



查看提交历史：



```bash

git log --oneline

```



Create directory in Windows CMD:



Windows CMD 创建文件夹：



```cmd

mkdir folder\_name

```



View directory tree:



查看目录树：



```cmd

tree /F

```



\---



\# 15. Current Project Status / 当前项目状态



Completed:



已完成：



```text

Git installation

Git 安装



Repository initialization

仓库初始化



Research repository structure

科研仓库结构



README

项目 README



.gitignore

忽略规则



Research Protocol

科研规范



Research Roadmap

科研路线图



First Commit

第一次 Git Commit

```



First commit:



第一次提交：



```text

e87f073

init bilingual research repository

```



\---



\# 16. What Should I Be Able to Answer? / 学完后我应该能回答什么？



After this stage, I should be able to explain:



现在我应该能够解释：



1\. What is Git?

&#x20;  Git 是什么？



2\. What is a Git repository?

&#x20;  Repository 是什么？



3\. What does `git init` do?

&#x20;  `git init` 做了什么？



4\. What is the difference between `git add` and `git commit`?

&#x20;  `git add` 和 `git commit` 有什么区别？



5\. What is the staging area?

&#x20;  暂存区是什么？



6\. What is a commit?

&#x20;  commit 是什么？



7\. Why does an experiment need a Git commit ID?

&#x20;  为什么实验要记录 Git commit？



8\. What is `.gitignore`?

&#x20;  `.gitignore` 是干什么的？



9\. Why should raw datasets and large model weights not be committed?

&#x20;  为什么大型数据集和模型权重不能直接进入 Git？



10\. Why does a research project need systematic README files?

&#x20;   为什么科研项目需要系统的 README？



\---



\# 17. Next Step / 下一步



Next milestone:



下一阶段：



\*\*Research Repository Structure v1.0 / 科研目录体系 v1.0\*\*



Next tasks:



接下来建立：



```text

Paper Notes System

论文笔记体系



Paper Matrix

论文矩阵



Figure Library

科研图库



Reproduction Template

复现模板



Experiment Template

实验模板



Innovation Bank Template

创新点模板

```



After the research-management system is complete, start:



科研管理系统建立完成后正式进入：



\*\*Milestone 1 — Radar Fundamentals / 雷达基础\*\*



