\# Experiments / 实验管理



This directory stores all formal research experiments.



本目录用于保存所有正式科研实验。



\---



\## 1. Core Principle / 核心原则



Every formal experiment must answer one clear research question.



每个正式实验都应该尽量回答一个明确问题。



Avoid:



避免：



> 一次修改很多变量，然后只看最终指标。



Prefer:



推荐：



> 一次尽量只改变一个关键变量，观察它对结果的影响。



This is the basis of controlled experiments.



这就是：



\*\*Controlled Experiment / 控制变量实验\*\*



\---



\## 2. Experiment ID / 实验编号



Every formal experiment must have a unique ID.



每个正式实验必须有唯一编号。



Example:



```text

EXP-001

EXP-002

EXP-003

```



Recommended folder naming:



推荐目录命名：



```text

experiments/

├── EXP-001\_baseline/

├── EXP-002\_remove\_doppler/

├── EXP-003\_low\_light/

└── ...

```



\---



\## 3. Recommended Experiment Folder / 推荐实验目录



Each experiment may contain:



每个实验可以包含：



```text

EXP-XXX\_description/

├── README.md

├── config.yaml

├── command.txt

├── metrics.json

├── environment.txt

├── notes.md

└── figures/

```



\---



\## 4. Required Information / 必须记录的信息



Each formal experiment should record:



每个正式实验至少记录：



\* Research Question / 实验问题

\* Hypothesis / 实验假设

\* Git Commit / 代码版本

\* Dataset / 数据集

\* Dataset Version / 数据版本

\* Data Split / 数据划分

\* Model / 模型

\* Configuration / 配置

\* Random Seed / 随机种子

\* Command / 执行命令

\* Metrics / 评价指标

\* Results / 实验结果

\* Conclusion / 实验结论



\---



\## 5. Git Commit / 为什么记录 Git Commit



The experiment result should be traceable to the exact code version.



实验结果必须能够追溯到准确的代码版本。



Example:



```text

Experiment:

EXP-023



Git Commit:

a83f29c



Result:

Motion Accuracy = 84.7%

```



This means that even after the code changes later, we can still identify which code version produced the result.



这样即使后续代码已经修改很多次，也能知道：



> 84.7% 到底是哪一版代码跑出来的。



\---



\## 6. Hypothesis First / 先写假设再跑实验



Before running an experiment, write the expected relationship.



实验开始前先写假设。



Recommended format:



推荐格式：



> If \_\_\_\_\_\_, then \_\_\_\_\_\_, because \_\_\_\_\_\_.



中文：



> 如果 \_\_\_\_\_\_，那么 \_\_\_\_\_\_，因为 \_\_\_\_\_\_。



Do not run the experiment first and then invent the hypothesis afterward.



不要先看到结果，再倒过来编实验假设。



\---



\## 7. Controlled Variables / 控制变量



For comparison experiments, keep unrelated settings unchanged whenever possible.



进行对比实验时，无关变量尽量保持一致。



Examples:



\* Dataset

\* Split

\* Model

\* Optimizer

\* Learning Rate

\* Epochs

\* Batch Size

\* Random Seed

\* Evaluation Protocol



Then change only the target variable.



然后只修改真正想研究的变量。



Example:



```text

Baseline:

Doppler = ON



Experiment:

Doppler = OFF

```



这样才能判断：



> 性能变化是否真的来自 Doppler。



\---



\## 8. Experimental Results / 实验结果



Results should not only record the final metric.



实验结果不能只记录一个最终数字。



Also record:



还应记录：



\* Baseline / 对照结果

\* Difference / 差异

\* Variance / 波动

\* Failure Cases / 失败案例

\* Visualization / 可视化

\* Possible Alternative Explanation / 其他可能解释



\---



\## 9. Repeated Experiments / 重复实验



When training is unstable or randomness affects results, repeat with multiple random seeds.



如果结果受随机性影响明显，应使用多个随机种子重复实验。



Example:



```text

Seed 0

Seed 1

Seed 2

```



Then report:



然后统计：



\* Mean / 均值

\* Standard Deviation / 标准差



\---



\## 10. Invalid Experiments / 无效实验



Failed or invalid experiments should not be deleted.



失败或无效实验不要直接删除。



Record why:



记录原因，例如：



\* Bug

\* Wrong configuration

\* Data leakage

\* Evaluation error

\* Hardware failure

\* Uncontrolled variable



These records prevent repeating the same mistake later.



这些记录可以避免以后再次踩同一个坑。



\---



\## 11. Experiment Template / 实验模板



Use:



使用：



```text

experiments/templates/experiment\_template.md

```



as the default template for formal experiments.



作为所有正式实验的默认母版。



\---



\## 12. Final Principle / 最终原则



A research result is meaningful only when we know:



一个科研结果只有在我们知道下面这些信息时才真正有意义：



```text

What question was tested?

研究了什么问题？



What changed?

改了什么？



What stayed unchanged?

什么没变？



Which code version was used?

用了哪版代码？



Which data were used?

用了什么数据？



What result was obtained?

结果是什么？



What conclusion is justified?

能够支持什么结论？

```



