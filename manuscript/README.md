\# Manuscript / 论文稿件



This directory stores paper-writing and submission materials for RadarVisionLLM-Lab.



本目录用于保存 RadarVisionLLM-Lab 项目的论文写作、修改和投稿材料。



\---



\## 1. Core Principle / 核心原则



Paper writing should grow together with the research process.



论文写作不应等所有实验结束后才开始。



During research, we should continuously accumulate:



科研过程中持续积累：



\* Background / 背景

\* Problem / 问题

\* Research Gap / 研究空白

\* Insight / 核心洞察

\* Contribution / 贡献

\* Related Work / 相关工作

\* Experimental Evidence / 实验证据

\* Failure Cases / 失败案例

\* Limitations / 局限性



\---



\## 2. Suggested Directory Structure / 推荐目录结构



Future structure may include:



```text

manuscript/

├── README.md

├── outline.md

├── draft/

├── figures/

├── tables/

├── references.bib

├── supplementary/

└── rebuttal/

```



\### `outline.md`



Paper structure and research story.



论文整体结构和科研故事线。



\### `draft/`



Draft versions.



论文草稿。



\### `figures/`



Final figures used in the paper.



正式论文图片。



\### `tables/`



Paper tables.



论文表格。



\### `references.bib`



Reference database.



参考文献数据库。



\### `supplementary/`



Supplementary materials.



补充材料。



\### `rebuttal/`



Reviewer-response materials.



审稿意见回复与 rebuttal 材料。



\---



\## 3. Paper Story / 论文故事线



A strong paper should usually follow a clear logic:



一篇清晰的论文通常需要形成：



```text

Background

背景

&#x20;  ↓

Problem

问题

&#x20;  ↓

Gap

现有不足

&#x20;  ↓

Observation

关键观察

&#x20;  ↓

Insight

核心洞察

&#x20;  ↓

Method

方法

&#x20;  ↓

Evaluation

实验验证

&#x20;  ↓

Discussion

讨论

&#x20;  ↓

Limitation

局限

```



\---



\## 4. Evidence-Driven Writing / 证据驱动写作



Every important claim should be supported by evidence whenever possible.



论文中的重要论断应尽量有证据支撑。



Examples:



```text

Claim:

Doppler improves motion reasoning.



Evidence:

Ablation experiment

```



```text

Claim:

The method is more robust under low light.



Evidence:

Low-light robustness experiment

```



Do not write claims that experiments cannot support.



不要写超出实验能够证明范围的结论。



\---



\## 5. Figures and Tables / 图表



Final paper figures should preferably come from reproducible scripts.



正式论文图尽量通过可复现脚本生成。



Recommended chain:



```text

Experiment

&#x20;  ↓

Result

&#x20;  ↓

Analysis Script

&#x20;  ↓

Figure / Table

&#x20;  ↓

Paper

```



\---



\## 6. Version Control / 论文版本管理



Important manuscript milestones should be committed with Git.



重要论文版本也要进入 Git 历史。



Example commit messages:



```text

add initial paper outline

draft introduction section

add ablation table

revise related work

update paper after advisor feedback

```



Avoid filenames such as:



```text

paper\_final.docx

paper\_final2.docx

paper\_final\_really\_final.docx

```



Use Git history instead of filename chaos.



不要靠文件名堆版本，尽量依赖 Git 管理版本。



\---



\## 7. Writing and Research Integration / 写作与科研结合



Research outputs should gradually map into paper sections.



科研产出要逐渐映射到论文内容。



Example:



```text

Failure Case

&#x20;  ↓

Motivation



Paper Matrix

&#x20;  ↓

Related Work



Minimal Experiment

&#x20;  ↓

Problem Validation



Ablation

&#x20;  ↓

Method Justification



Robustness Experiment

&#x20;  ↓

Evaluation



Observed Limitation

&#x20;  ↓

Discussion

```



\---



\## 8. Final Goal / 最终目标



The goal is not only to finish a manuscript.



目标不只是“写完一篇论文”。



The final paper should be:



最终论文应尽量做到：



\* Clear / 逻辑清楚

\* Evidence-based / 证据充分

\* Reproducible / 可复现

\* Well-organized / 组织规范

\* Honest about limitations / 对局限保持诚实

\* Traceable to experiments and code / 能追溯到实验和代码



