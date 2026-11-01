# Experiment Record / 实验记录

## Experiment ID / 实验编号

**EXP-XXX**

---

## 1. Basic Information / 基本信息

* **Date / 日期：**

* **Researcher / 实验者：**

* **Status / 状态：**

* **Git Commit：**

* **Branch：**

* **Dataset：**

* **Dataset Version：**

* **Train Split：**

* **Validation Split：**

* **Test Split：**

Status:

* Planned

* Running

* Completed

* Failed

* Invalid

---

# 2. Research Question / 实验问题

本次实验到底想回答什么问题？

>

只能尽量回答一个明确问题。

---

# 3. Hypothesis / 实验假设

Before running the experiment:

实验前先写：

> If \_\_\_\_\_\_, then \_\_\_\_\_\_, because \_\_\_\_\_\_.

中文：

> 如果 \_\_\_\_\_\_，那么 \_\_\_\_\_\_，因为 \_\_\_\_\_\_。

不要跑完实验再倒推假设。

---

# 4. Baseline / 对照实验

Baseline Experiment ID:

```text

EXP-XXX

```

Baseline Result:

>

---

# 5. Changed Variable / 本次修改变量

只描述本次真正修改的主要变量：

>

Examples:

```text

Doppler: ON → OFF



Fusion:

Concatenation → Cross-Attention



Visual Degradation:

Normal → Low Light

```

---

# 6. Controlled Variables / 保持不变的变量

* Dataset：

* Data Split：

* Model：

* Optimizer：

* Learning Rate：

* Epoch：

* Batch Size：

* Random Seed：

* Evaluation：

* Other：

---

# 7. Configuration / 实验配置

Config File:

```text

configs/...

```

Important Parameters:

| Parameter | Value |
| --------- | ----- |
|           |       |

---

# 8. Hardware and Environment / 硬件与环境

* GPU：

* CUDA：

* PyTorch：

* Python：

* Other：

Environment record:

```text

environment.txt

```

---

# 9. Command / 执行命令

```bash

...

```

参数解释：

\*

\*

\*

---

# 10. Expected Result / 预期结果

实验前预测：

>

为什么？

>

---

# 11. Actual Result / 实际结果

| Metric | Baseline | This Experiment | Difference |
| ------ | -------: | --------------: | ---------: |
|        |          |                 |            |

---

# 12. Raw Output / 原始输出

Log:

```text

...

```

Result File:

```text

...

```

Checkpoint:

```text

...

```

---

# 13. Visualization / 可视化

Generated figures:

```text

figures/...

```

图表达什么？

>

---

# 14. Interpretation / 结果解释

实验结果是否支持假设？

* \[ ] Supports

* \[ ] Partially Supports

* \[ ] Does Not Support

* \[ ] Inconclusive

解释：

>

---

# 15. Alternative Explanations / 其他可能原因

结果变化是否可能来自：

* Random seed

* Dataset split

* Training instability

* Hyperparameter change

* Preprocessing difference

* Evaluation difference

* Data leakage

* Bug

分析：

>

---

# 16. Repetition / 重复实验

是否需要多次运行？

* \[ ] Yes

* \[ ] No

Seeds:

```text

0

1

2

```

Results:

| Seed | Result |
| ---: | -----: |
|      |        |

Mean:

Standard Deviation:

---

# 17. Conclusion / 实验结论

一句话结论：

>

注意：

实验结论不能超过实验真正能够证明的范围。

---

# 18. Paper Usage / 论文用途

这个实验未来可能用于：

* \[ ] Motivation

* \[ ] Main Comparison

* \[ ] Ablation

* \[ ] Robustness

* \[ ] Parameter Study

* \[ ] Failure Analysis

* \[ ] Qualitative Result

* \[ ] Efficiency Analysis

* \[ ] Not Used

---

# 19. Next Experiment / 下一步实验

Next Experiment ID:

```text

EXP-XXX

```

Reason:

>

---

# 20. Research Log Link / 科研日志关联

Related Research Log:

```text

docs/research\_log/...

```

---

# 21. Final Status / 最终状态

* \[ ] Valid Experiment / 有效实验

* \[ ] Invalid Experiment / 无效实验

* \[ ] Needs Re-run / 需要重跑

* \[ ] Archived / 已归档

Reason:

>
