# Reproduction Record / 论文复现记录

## 0. Project Information / 项目信息

* **Paper / 论文：**

* **Venue / 会议期刊：**

* **Year / 年份：**

* **Official Code / 官方代码：**

* **Repository Commit / 官方代码版本：**

* **Dataset / 数据集：**

* **Start Date / 开始日期：**

* **Status / 状态：**

Status:

* Not Started

* Environment Setup

* Data Preparation

* Running

* Debugging

* Reproduced

* Failed

* Completed

---

# 1. Why Reproduce This Paper? / 为什么复现？

它在我们的研究中扮演什么角色？

* \[ ] Learn basic concepts / 学基础

* \[ ] Learn code structure / 学代码结构

* \[ ] Candidate baseline / 候选 baseline

* \[ ] Direct baseline / 正式 baseline

* \[ ] Closest related work / 最接近工作

* \[ ] Build dataset pipeline / 搭数据 pipeline

说明：

>

---

# 2. Expected Output / 复现目标

论文报告结果：

| Metric | Paper Result |
| ------ | -----------: |
|        |              |

我们的目标：

> 尽量在相同配置下复现接近论文报告的结果。

Acceptable difference / 可接受差距：

>

---

# 3. Environment / 环境

## Hardware / 硬件

* OS：

* CPU：

* GPU：

* GPU Memory：

* RAM：

## Software / 软件

* Python：

* CUDA：

* cuDNN：

* PyTorch：

* MMDetection3D：

* Other：

## Environment File

```text

environment.yml

requirements.txt

```

---

# 4. Repository Structure / 官方代码结构

记录核心目录：

```text

project/

├── configs/

├── datasets/

├── models/

├── tools/

└── ...

```

逐个说明：

### `configs/`

作用：

### `datasets/`

作用：

### `models/`

作用：

---

# 5. Dataset / 数据集

* Dataset：

* Version：

* Download Source：

* Directory：

* Train Split：

* Validation Split：

* Test Split：

实际目录：

```text

data/

...

```

---

# 6. Input Data / 输入数据

## Camera

Input:

Shape:

Meaning:

## Radar

Input:

Shape:

Fields:

例如：

```text

x

y

z

Doppler

RCS

```

## Labels

Format:

---

# 7. Preprocessing / 数据预处理

完整记录：

```text

Raw Data

&#x20;  ↓

Step 1

&#x20;  ↓

Step 2

&#x20;  ↓

Model Input

```

### Step 1

代码位置：

输入：

输出：

为什么需要：

---

# 8. Model Data Flow / 模型数据流

```text

Camera

↓

Camera Encoder

↓

Image Feature



Radar

↓

Radar Encoder

↓

Radar Feature



↓

Fusion

↓

Prediction

```

根据实际论文修改。

---

# 9. Core Code Reading / 核心代码阅读

## Entry Point / 程序入口

File:

Function:

Purpose:

## Dataset Loader

File:

Class:

Input:

Output:

## Model

File:

Class:

## Loss

File:

Function:

## Evaluation

File:

Function:

---

# 10. Commands / 命令记录

## Installation

```bash

...

```

## Training

```bash

...

```

逐个参数解释：

* `--xxx`：

* `--xxx`：

## Evaluation

```bash

...

```

## Visualization

```bash

...

```

---

# 11. First Run / 第一次运行

Date:

Git Commit:

Command:

```bash

...

```

Output:

```text

...

```

结果是什么意思：

>

---

# 12. Errors and Debugging / 报错与排查

## Error 001

### Error Message

```text

...

```

### Cause / 原因

>

### Solution / 解决方法

>

### What I Learned / 学到了什么

>

---

# 13. Reproduced Results / 复现结果

| Metric | Paper | Ours | Difference |
| ------ | ----: | ---: | ---------: |
|        |       |      |            |

---

# 14. Difference Analysis / 差异分析

如果没有复现到论文结果，检查：

* Dataset version

* Data split

* Preprocessing

* Config

* Random seed

* Number of epochs

* Batch size

* Learning rate

* CUDA/PyTorch version

* Evaluation protocol

分析：

>

---

# 15. Code Understanding / 代码理解

我是否能够解释：

* \[ ] 输入数据在哪里进入程序

* \[ ] Dataset loader 在哪里

* \[ ] Camera encoder 在哪里

* \[ ] Radar encoder 在哪里

* \[ ] Fusion module 在哪里

* \[ ] Loss 在哪里

* \[ ] Evaluation 在哪里

* \[ ] Output 是什么

---

# 16. Modification Test / 修改能力测试

为了证明不是只会运行代码，完成至少一个小修改。

例如：

* 修改一个参数

* 关闭一个模块

* 修改输入特征

* 增加一个打印/可视化

* 替换一小段模块

Modification:

>

Expected:

>

Actual:

>

Interpretation:

>

---

# 17. Failure Cases / 失败案例

记录模型容易失败的情况：

1\.

2\.

3\.

这些可能成为未来科研问题。

---

# 18. Limitations / 局限

作者没有解决的问题：

1\.

2\.

代码或系统存在的问题：

1\.

2\.

---

# 19. Possible Research Ideas / 潜在 Idea

### IDEA

Problem:

Observation:

Possible Solution:

Minimal Experiment:

Closest Work:

---

# 20. Final Reproduction Conclusion / 最终复现结论

### Reproduction Status

* \[ ] Fully Reproduced

* \[ ] Mostly Reproduced

* \[ ] Partially Reproduced

* \[ ] Failed

### Main Result

>

### What I Learned

>

### Can We Use It as a Baseline?

* \[ ] Yes

* \[ ] No

* \[ ] Maybe

Reason:

>

### Next Step

>
