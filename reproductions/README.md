\# Reproductions / 论文复现



This directory stores reproduction projects for open-source research papers.



本目录用于保存开源论文和科研项目的复现过程。



\---



\## 1. Goal / 目标



The goal of reproduction is not only to make the code run.



复现的目标不只是：



> “代码跑通了。”



真正目标是理解：



\* Input / 输入是什么

\* Dataset / 数据怎么读

\* Preprocessing / 预处理怎么做

\* Model / 模型结构是什么

\* Fusion / 融合发生在哪里

\* Loss / 损失函数是什么

\* Training / 训练流程是什么

\* Evaluation / 测试流程是什么

\* Output / 输出代表什么



最终达到：



> \*\*能够自己修改核心代码，而不是只会执行命令。\*\*



\---



\## 2. Directory Structure / 目录结构



Each reproduced paper should have an independent folder.



每篇正式复现论文建立独立目录。



Example:



```text

reproductions/

├── centerfusion/

├── crn/

├── mssf/

└── ...

```



Recommended structure:



```text

reproductions/

└── mssf/

&#x20;   ├── README.md

&#x20;   ├── configs/

&#x20;   ├── scripts/

&#x20;   ├── logs/

&#x20;   ├── results/

&#x20;   └── notes/

```



\---



\## 3. Required Records / 必须记录



Each reproduction project should record:



每个复现项目至少记录：



\* Paper Information / 论文信息

\* Official Repository / 官方代码

\* Official Commit / 官方代码版本

\* Environment / 环境

\* Dataset / 数据集

\* Input Format / 输入格式

\* Preprocessing / 预处理

\* Core Model / 核心模型

\* Loss / 损失函数

\* Training Command / 训练命令

\* Evaluation Command / 测试命令

\* Paper Result / 论文结果

\* Reproduced Result / 我们的复现结果

\* Difference Analysis / 差异分析

\* Errors / 报错

\* Solutions / 解决方法

\* Failure Cases / 失败案例

\* Limitations / 局限

\* Possible Ideas / 潜在 Idea



\---



\## 4. Code Reading Principle / 代码阅读原则



When reading important code, answer three questions:



阅读重要代码时，固定回答三个问题：



1\. \*\*What does this code do? / 这段代码干什么？\*\*

2\. \*\*Why is it written this way? / 为什么这样写？\*\*

3\. \*\*What does it output? / 输出是什么？\*\*



For tensors and features, also record:



对于 Tensor 和 Feature，还要记录：



\* Shape / 维度

\* Meaning of each dimension / 每一维代表什么

\* Data type / 数据类型

\* Coordinate system / 坐标系

\* Next module / 下一步进入哪里



\---



\## 5. Reproduction Result / 复现结果



A reproduced baseline should be compared against the paper result.



正式复现后应比较：



| Metric | Paper | Ours | Difference |

| ------ | ----: | ---: | ---------: |

|        |       |      |            |



If the gap is large, do not immediately use the result as a baseline.



如果复现结果与论文差距很大，不能马上用来声称：



> “我们的方法超过了 baseline。”



需要先检查：



\* Dataset Version / 数据集版本

\* Data Split / 数据划分

\* Config / 配置

\* Preprocessing / 预处理

\* Random Seed / 随机种子

\* Evaluation Protocol / 评估方式

\* Environment / 软件环境



\---



\## 6. Modification Requirement / 修改能力要求



After reproducing an important project, perform at least one small modification.



重要项目复现后，至少进行一次小修改，例如：



\* Change a parameter / 修改参数

\* Disable one module / 关闭一个模块

\* Change one feature / 修改输入特征

\* Add visualization / 增加可视化

\* Add debugging output / 增加调试输出



The purpose is to verify:



目的是确认：



> 我已经开始理解代码，而不是只会运行。



\---



\## 7. Reproduction Template / 复现模板



Use:



使用：



```te

```



