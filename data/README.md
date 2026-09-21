\# Data / 数据管理



This directory stores dataset documentation, metadata, split information, and data-processing instructions.



本目录用于管理数据集说明、元数据、数据划分和数据处理方法。



\---



\## 1. Core Principle / 核心原则



Large raw datasets should usually NOT be committed directly into Git.



大型原始数据集通常不直接提交到 Git。



Instead, Git should record:



Git 主要记录：



\* Dataset Name / 数据集名称

\* Dataset Version / 数据集版本

\* Official Source / 官方来源

\* Download Date / 下载日期

\* Directory Structure / 目录结构

\* Train/Validation/Test Split / 数据划分

\* Calibration Information / 标定信息

\* Annotation Format / 标注格式

\* Preprocessing Steps / 预处理流程

\* Dataset License / 数据集许可证



\---



\## 2. Why Not Store Large Raw Data in Git? / 为什么大型原始数据不直接进 Git？



Reasons include:



原因包括：



\* Large file size / 文件体积大

\* Repository becomes difficult to clone / 仓库难以克隆

\* Binary files are inefficient for version comparison / 二进制文件不适合版本差异管理

\* Dataset versions may change / 数据版本可能变化

\* Copyright and licensing / 版权和许可证问题



The goal is:



我们的目标是：



> Manage the information and processing pipeline of the data, not necessarily the raw data itself.



> 管理“数据是什么、来自哪里、如何处理”，而不是把所有数据本体塞进 Git。



\---



\## 3. Suggested Directory Structure / 推荐目录结构



Future structure may include:



未来可以逐步建立：



```text

data/

├── README.md

├── raw/

├── processed/

├── splits/

├── calibration/

├── metadata/

└── samples/

```



\### `raw/`



Original downloaded data.



原始下载数据。



Usually ignored by `.gitignore`.



通常不进入 Git。



\### `processed/`



Processed data generated from raw data.



预处理后数据。



较大的处理结果通常也不直接进入 Git。



\### `splits/`



Train/validation/test split files.



训练集、验证集、测试集划分文件。



这些通常应该进入 Git，因为它们决定实验可复现性。



\### `calibration/`



Calibration-related metadata or converted calibration files.



标定相关信息。



\### `metadata/`



Dataset metadata.



数据集元数据。



\### `samples/`



Very small example files used for debugging or visualization.



用于调试和演示的小样例。



只有文件足够小、版权允许时才考虑进入 Git。



\---



\## 4. Dataset Record Template / 数据集记录模板



For every important dataset, create a record.



每个正式使用的数据集都应该建立记录。



Example:



```text

Dataset Name:

View-of-Delft (VoD)



Version:



Official Website:



Official Repository:



Download Date:



Sensors:

\- Camera

\- Radar

\- LiDAR



Radar Type:



Number of Frames:



Annotations:



Train Split:



Validation Split:



Test Split:



Calibration:



Coordinate Systems:



Preprocessing:



License:



Notes:

```



\---



\## 5. Data Split Reproducibility / 数据划分可复现性



Data split is part of the experiment.



数据划分本身就是实验配置的一部分。



For example:



```text

Train:

70%



Validation:

10%



Test:

20%

```



is not enough.



仅记录比例通常不够。



We should preferably save the exact sample IDs or official split files.



更推荐保存：



> 哪些具体样本属于 Train / Validation / Test。



Otherwise, different random splits may produce different results.



否则即使比例相同，不同划分也可能产生不同实验结果。



\---



\## 6. Dataset Version / 数据版本



Always record the dataset version when possible.



正式实验尽量记录数据集版本。



Example:



```text

Dataset:

VoD



Version:

vX.X



Downloaded:

YYYY-MM-DD

```



This prevents confusion if the official dataset is later updated.



这样以后官方数据更新时，不会混淆：



> 当时实验到底使用的是哪一版数据？



\---



\## 7. Preprocessing / 数据预处理



Every important preprocessing step should be reproducible.



所有重要预处理步骤都应该能够复现。



Preferred workflow:



```text

Raw Data

&#x20;  ↓

Preprocessing Script

&#x20;  ↓

Processed Data

&#x20;  ↓

Model Input

```



Avoid undocumented manual processing.



避免：



> 手工改了一批数据，但没有记录怎么改。



\---



\## 8. Calibration / 标定信息



Radar-camera fusion depends heavily on calibration.



雷视融合高度依赖标定。



For relevant datasets, record:



需要重点记录：



\* Radar Coordinate System / 雷达坐标系

\* Camera Coordinate System / 相机坐标系

\* Intrinsic Parameters / 相机内参

\* Extrinsic Parameters / 外参

\* Transformation Matrices / 坐标变换矩阵

\* Timestamp / 时间戳

\* Synchronization Method / 同步方式



这些信息以后会直接决定：



> Radar 点能否正确投影到 Camera 图像上。



\---



\## 9. Current Planned Dataset / 当前计划数据集



Initial candidate:



初始候选数据集：



\*\*View-of-Delft (VoD)\*\*



Current purpose:



当前计划用途：



\* Learn radar-camera data structure / 学习雷视数据结构

\* Learn coordinate transformation / 学习坐标变换

\* Radar-camera projection / Radar→Camera 投影

\* Reproduce radar-camera fusion baselines / 复现雷视融合 baseline

\* Support future VLM experiments / 支撑后续 VLM 实验



This choice may change after further literature review.



后续可根据文献调研和实验需要调整。



