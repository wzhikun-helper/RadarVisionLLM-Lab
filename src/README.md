\# Source Code / 核心代码



This directory stores the core research code developed in RadarVisionLLM-Lab.



本目录用于保存 RadarVisionLLM-Lab 项目中我们自己开发和长期维护的核心研究代码。



\---



\## 1. Core Principle / 核心原则



`src/` should contain reusable and relatively stable research code.



`src/` 主要保存：



\* 可复用的核心实现

\* 相对稳定的模型代码

\* 数据处理核心模块

\* 评估模块

\* 公共工具函数



Temporary debugging code should not remain here for a long time.



临时调试代码不应长期堆在 `src/` 中。



\---



\## 2. Suggested Directory Structure / 推荐目录结构



Future structure may include:



```text

src/

├── datasets/

├── radar/

├── camera/

├── fusion/

├── models/

├── vlm/

├── evaluation/

└── utils/

```



\### `datasets/`



Dataset loaders and dataset interfaces.



数据集读取和统一接口。



\### `radar/`



Radar-related processing.



雷达相关处理，例如：



\* Point cloud processing / 点云处理

\* Doppler processing / Doppler 处理

\* Coordinate transformation / 坐标变换

\* Radar feature encoding / 雷达特征编码



\### `camera/`



Camera-related processing.



相机相关处理。



\### `fusion/`



Radar-camera fusion modules.



雷视融合模块。



\### `models/`



Complete models and model wrappers.



完整模型与模型封装。



\### `vlm/`



Vision-language-model related components.



视觉语言模型相关模块，例如：



\* Prompt construction

\* VLM interface

\* Multimodal input

\* Grounding

\* Reliability reasoning



\### `evaluation/`



Evaluation metrics and evaluation logic.



评估指标和测试逻辑。



\### `utils/`



Reusable utility functions.



公共工具函数。



\---



\## 3. Code Reading Principle / 代码理解原则



For every important module, we should be able to explain:



每个重要模块都应该能解释：



1\. What is the input? / 输入是什么？

2\. What is the output? / 输出是什么？

3\. What problem does it solve? / 解决什么问题？

4\. Why is it designed this way? / 为什么这样设计？

5\. Where is it used next? / 下一步进入哪里？



For tensors, also record:



对于 Tensor，还要尽量记录：



\* Shape / 维度

\* Meaning of each dimension / 每一维含义

\* Coordinate system / 坐标系

\* Unit / 单位

\* Data type / 数据类型



\---



\## 4. Research Code vs Experiment Code / 核心代码与实验代码



Core reusable implementation belongs in:



核心可复用实现放在：



```text

src/

```



Experiment-specific configuration and records belong in:



某次具体实验的配置和结果放在：



```text

experiments/

```



For example:



```text

src/fusion/doppler\_fusion.py

```



is the implementation.



而：



```text

experiments/EXP-023\_remove\_doppler/

```



records one specific experiment using or disabling that implementation.



\---



\## 5. Naming Principle / 命名原则



Prefer meaningful names.



推荐：



```text

radar\_encoder.py

camera\_encoder.py

cross\_modal\_fusion.py

motion\_reasoning.py

```



Avoid unclear names such as:



避免：



```text

test2.py

new\_model.py

final\_new.py

model\_latest\_v3.py

```



\---



\## 6. Configuration / 配置



Avoid burying important experiment parameters directly inside source code.



不要把大量实验参数硬编码在核心代码中。



Prefer:



优先使用：



\* Config files / 配置文件

\* Command-line arguments / 命令行参数

\* Experiment-specific configs / 实验专属配置



This makes controlled experiments easier.



这样更方便做控制变量实验。



\---



\## 7. Reusability / 可复用性



Whenever possible, code should be modular.



代码尽量模块化。



Example:



```text

Radar Encoder

&#x20;     ↓

Fusion Module

&#x20;     ↓

Prediction Head

```



Then individual modules can be:



这样各模块可以：



\* Replaced / 替换

\* Disabled / 关闭

\* Compared / 对比

\* Ablated / 做消融



This is important for research experiments.



这对科研实验尤其重要。



\---



\## 8. Final Principle / 最终原则



The goal is not only to make the code work.



目标不只是：



> “代码能跑。”



最终应该达到：



> I know where the data enter, how they change, why each module exists, and how to modify the system independently.



> 我知道数据从哪里进入、经过什么变化、每个模块为什么存在，并能够独立修改系统。



