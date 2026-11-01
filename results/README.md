# Results / 实验结果管理

This directory stores processed experimental results, summary tables, statistics, and analysis outputs.

本目录用于保存经过整理的实验结果、汇总表、统计结果和分析输出。

---

## 1. Core Principle / 核心原则

Every important result must be traceable.

每一个重要结果都必须可追溯。

Recommended traceability chain:

推荐追溯链：

```text

Result

结果

&#x20; ↓

Experiment ID

实验编号

&#x20; ↓

Configuration

配置

&#x20; ↓

Dataset / Split

数据与划分

&#x20; ↓

Git Commit

代码版本

```

---

## 2. Suggested Directory Structure / 推荐目录结构

Future structure:

```text

results/

├── raw/

├── processed/

├── tables/

├── statistics/

└── summaries/

```

### `raw/`

Raw outputs copied or referenced from formal experiments.

正式实验产生的原始输出。

### `processed/`

Processed metrics and analysis results.

经过整理和处理后的结果。

### `tables/`

Tables used for comparison or papers.

用于对比分析和论文的表格。

### `statistics/`

Statistical analysis.

统计分析结果，例如：

* Mean / 均值

* Standard Deviation / 标准差

* Confidence Interval / 置信区间

### `summaries/`

Human-readable summaries of important experiments.

重要实验的文字总结。

---

## 3. Naming Principle / 命名原则

Avoid unclear filenames such as:

避免：

```text

final.csv

new\_result.csv

latest\_result\_v2\_final.csv

```

Prefer:

推荐：

```text

EXP-012\_metrics.json

EXP-012\_summary.csv

EXP-012\_ablation.csv

EXP-012\_analysis.md

```

The filename should indicate where the result came from.

文件名应该能看出结果来源。

---

## 4. Relationship with Experiments / 与实验目录的关系

`experiments/` stores the complete experimental process.

`experiments/` 保存完整实验过程。

`results/` stores selected and organized results.

`results/` 保存整理后的关键结果。

Relationship:

```text

experiments/EXP-023/

&#x20;       ↓

raw experiment output

&#x20;       ↓

analysis

&#x20;       ↓

results/EXP-023\_\*

```

---

## 5. Paper Results / 论文结果

Before a number enters the final paper, it should be possible to answer:

一个数字进入论文前，必须能回答：

* Which experiment produced it? / 哪个实验产生？

* Which code version was used? / 哪版代码？

* Which dataset split? / 哪个数据划分？

* Which metric definition? / 指标怎么计算？

* Was it repeated? / 是否重复实验？

* Is it mean or best result? / 是均值还是最好结果？

---

## 6. Statistical Integrity / 统计规范

Do not selectively report only the best random run without explanation.

不要只挑最好的随机结果而不说明。

If multiple runs are required, record:

如果需要多次实验，应记录：

```text

Seed 0:

Seed 1:

Seed 2:



Mean:

Std:

```

---

## 7. Figures and Tables / 图表关系

Results should feed directly into reproducible analysis scripts.

推荐流程：

```text

Experiment

实验

&#x20;  ↓

Result File

结果文件

&#x20;  ↓

Analysis Script

分析脚本

&#x20;  ↓

Table / Figure

表格或图片

&#x20;  ↓

Paper

论文

```

---

## 8. Final Principle / 最终原则

Do not keep unexplained numbers.

不要留下来源不明的数字。

Every important result should have:

每个重要结果都应该有：

> Source + Configuration + Code Version + Interpretation

即：

> 来源 + 配置 + 代码版本 + 结论解释

## 维护入口（2026-11-01）

本目录只登记真实run产物及分析，作者论文目标不写成本项目指标。工程证据阶段与字段见[统一规范](../reproductions/RECORDING_STANDARD.md)，未运行保持Not Run。
