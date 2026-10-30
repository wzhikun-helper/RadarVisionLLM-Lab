## 学习总览

| 项目    | 当前内容                                                                                                                                          |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| 论文名称  | CRN: Camera Radar Net for Accurate, Robust, Efficient 3D Perception                                                                           |
| 作者／会议 | Youngseok Kim 等；ICCV 2023                                                                                                                     |
| 研究任务  | 基于 Camera + Radar 的 3D Detection，论文还涉及 Tracking、BEV Segmentation                                                                              |
| 主要数据集 | nuScenes                                                                                                                                      |
| 核心模块  | Radar-assisted View Transformation（RVT）；Multi-modal Feature Aggregation（MFA）                                                                  |
| 方法要点  | 相机语义 + 雷达测距线索；视锥到 BEV；MDCA 跨模态自适应采样与融合；可选 Top-K 稀疏聚合                                                                                          |
| 论文    | https://openaccess.thecvf.com/content/ICCV2023/html/Kim_CRN_Camera_Radar_Net_for_Accurate_Robust_Efficient_3D_Perception_ICCV_2023_paper.html |
| 官方仓库  | https://github.com/youngskkim/CRN                                                                                                             |

**核心问题：** Camera 能识别目标，却不一定能准确确定深度；常规车载 Radar 能提供距离与径向速度等观测，却点少、语义弱、存在误测。如何把两种模态变成更准确、鲁棒且计算可接受的 BEV 表征？

**研究主线：** Camera 语义和深度概率 + Radar 几何观测 → RVT 改善 Camera 特征进入 BEV 的过程 → MFA 以可变形注意力关联两种 BEV 特征 → 检测／跟踪／分割。**空间统一不代表位置一定准确；特征关联不代表误差全部消失。**

---

## Step 1｜Title + Abstract：先弄清论文做什么

### 1.1 标题逐项理解

| 词                | 当前理解                      | 验证边界                         |
| ---------------- | ------------------------- | ---------------------------- |
| Camera Radar Net | 同时利用 Camera 和 Radar 的感知网络 | 不是 Radar-only，也不是 LiDAR 参与推理 |
| Accurate         | 希望更准确定位并检测目标              | 需要通过 nuScenes 指标和对应基线验证      |
| Robust           | 希望对观测退化更稳健                | 不等于每种天气和干扰下都可靠               |
| Efficient        | 希望达到更高推理效率                | 要区分网络吞吐 FPS、单帧延迟、硬件和模型配置     |
| 3D Perception    | 三维空间感知                    | 当前方法重点涉及 3D 检测，并扩展到跟踪、BEV 分割 |

### 1.2 为什么仅有 Camera 不够？

普通 RGB Camera 能提取颜色、边缘、纹理、类别和上下文语义。然而从二维投影恢复三维位置存在**深度歧义（Depth Ambiguity）**。即使相机镜头已经理想校正，不同真实尺度与深度的物体仍可能呈现相似的投影大小。

**基础知识补充｜针孔投影（教学公式，并非 CRN 创新公式）**：

$$
h = \frac{fH}{Z}
$$

- $H$ 为真实物体高度，$Z$ 为相机光轴深度，$h$ 为图像投影高度，$f$ 为焦距。
- 小车 $H=1.5 \text{ m}, Z=10 \text{ m}$ 与大车 $H=3 \text{ m}, Z=20 \text{ m}$，都有 $H/Z=0.15$，仅从高度投影不能唯一恢复距离。
- **Lens Distortion（镜头畸变）≠ Depth Ambiguity（深度歧义）**。镜头畸变可校正相当一部分；投影丢失深度信息的问题不因此消失。

### 1.3 为什么加入 Radar？

| 模态             | 主要信息                                       | 典型局限                    |
| -------------- | ------------------------------------------ | ----------------------- |
| Camera         | 纹理、外观、类别、视觉语义                              | 深度歧义、低照度、遮挡、眩光          |
| Radar          | Range、Azimuth、Radial Velocity、部分雷达输出 RCS 等 | 点稀疏、杂波、测角误差、多径、部分目标无有效点 |
| Camera + Radar | 语义与物理测量互补                                  | 标定、时间同步、对应关系、错误测量传播     |

**Radar 不是稀疏的 LiDAR 替代品。** 它的价值不只来自点的几何位置，还来自测距和径向运动观测；RCS 描述散射响应而不是目标真实大小。常规 nuScenes 车载 Radar 也不能被当作 VoD 3+1D 成像 Radar。

### 1.4 两个核心贡献模块

- **RVT — Radar-assisted View Transformation**：利用 Radar 空间测量相关信息辅助图像特征的视角变换，缓解 Camera-to-BEV 时的深度／空间定位不确定性。Radar 点稀疏本身不是优势，而是覆盖限制。
- **MFA — Multi-modal Feature Aggregation**：Camera BEV 与 Radar BEV 即使处于同一网格系统仍可能错位；通过可变形跨模态注意力，学习从何处取特征以及怎样加权聚合。

**二者分工**：RVT 关注**图像特征怎样进入 BEV**；MFA 关注**已在 BEV 的两类特征怎样有效关联**。


---

## Step 2｜Introduction：为什么值得研究

### 2.1 BEV：为什么三维感知需要统一空间表示？

**BEV（Bird's-Eye View）** 是从俯视方向组织空间；**BEV Feature Map** 不是一张普通鸟瞰照片，而是按 BEV 网格排列的神经网络特征。教学示例 `[B, C, H, W] = [1, 64, 100, 100]` 表示一个样本、64 个通道、100×100 个网格，**不是 64 个物体类别，也不能直接推断 100 m × 100 m**。

![Pasted image 20261028091506.png](assets/P002_CRN/Pasted%20image%2020261028091506.png "原Obsidian宽度：673")
*一张包含 10,000 个空间位置的 BEV 特征图，每个位置都有一个 64 维特征向量。*

BEV 让车辆前后、左右、相互距离、目标朝向等信息便于统一表达和后续检测、跟踪。但**转换为 BEV 不会自动让深度变准，也不会凭空产生目标完整速度**。

### 2.2 Camera + Radar 为什么具有研究价值？

LiDAR 通常提供较丰富的三维几何，却有硬件成本和工程代价。Camera + Radar 希望兼顾语义、空间观测和较适合部署的硬件组合，但不能无条件认定其精度超过 LiDAR。

**LiDAR-free inference 的边界**：模型运行时不以 LiDAR 为输入，不代表训练监督、标签或数据准备期间从未用到 LiDAR。CRN 的图像深度分支训练包含 LiDAR 深度监督。

### 2.3 Camera-only：不适定问题与被动传感器

- **Ill-posed Problem（不适定问题）**：例如二维图像恢复三维深度时，结果可能不唯一或不稳定，并非完全无法估计。
- **Passive Sensor（被动式传感器）**：普通可见光相机依赖环境光和物体反射；夜晚、眩光、低对比度会影响图像观测。
- **两类问题不同**：光照影响成像质量；Depth Ambiguity 来自几何投影的信息不足。

### 2.4 Radar：优势之外为什么还会失败？

- **Sparsity（稀疏性）**：单个汽车可能只有少量散射点，缺乏完整边界，难以独自回归精确 3D Box。
- **Radar 测量级 False Negative（漏点）**：真实目标没有形成有效 Radar 点，可能因为低 RCS、门限或遮挡；但 Camera 分支仍可能检测成功，**不等于融合模型一定漏框**。
- **Radar 测量级 False Positive（错误点/误检）**：噪声、杂波或多径可能造成无真实目标对应的测量点；它可能污染特征，却不必然导致最终误检框。
- **Clutter 与 Multipath**：Clutter 偏非目标背景散射；Multipath 偏信号经多条反射路径返回；两者机制不同。雷达在恶劣可见性下有相对优势，也会受强雨、遮挡、噪声等影响。

### 2.5 Fusion 类型与准确性问题

| 融合思路                          | 信息组合阶段            | 可能优势或限制                   |
| ----------------------------- | ----------------- | ------------------------- |
| Early Fusion                  | 原始／低层数据           | 保留低层信息，但坐标与形状差异需处理        |
| Intermediate / Feature Fusion | 神经网络中间特征          | 有机会关联语义和空间证据，但需解决错位       |
| Late Fusion                   | 各模态先独立输出检测或决策，再合并 | 模块独立性好；不能充分利用没有形成预测框的中间证据 |

**Late Fusion 不是一定失败**：一个模态漏检，另一模态仍可能检测成功；具体行为由预测融合策略决定。CRN 的核心在于更早阶段的 BEV 表征与特征级聚合。

### 2.6 Introduction 开放式问答与学习状态

- **BEV 与 BEV Feature Map**：俯视空间表示和带通道的空间特征张量。
- **LiDAR-free**：推理时不输入 LiDAR 不等于训练监督无 LiDAR。
- **Ill-posed 与被动相机**：投影歧义以及光照退化与其区别。
- **RVT/MFA 动机**： BEV 坐标统一但特征仍可能错位；MFA 是学习式关联和聚合，而非保证所有对象坐标真值化。

---

## Step 3｜Methodology：从 Camera 与 Radar 到三维检测

### 3.1 网络整体流程与模块职责

![Pasted image 20261028142231.png](assets/P002_CRN/Pasted%20image%2020261028142231.png)

### 3.2 RVT — Radar-assisted View Transformation

**作者要解决什么？** Camera 具有语义但光学投影导致深度不确定；若图像特征被错误放入 BEV，会影响检测框位置。Radar 可提供测量距离，但它稀疏、测量可能有错。

![Pasted image 20261028193811.png](assets/P002_CRN/Pasted%20image%2020261028193811.png)

① **图像编码（Image Encoding）**  
==多视角相机图像首先经过 Backbone 和 FPN，提取两类信息==：  
- **==图像上下文特征（Image Context Feature）==**：图像中的语义和视觉特征。  
- **==深度分布（Depth Distribution）==**：每个图像位置对应不同深度区间的预测概率。  
例如，相机识别出一辆车，但无法确切判断其位于 10 米还是 20 米，Depth Distribution 正是用来表达这种深度不确定性。

② **雷达编码（Radar Encoding）**  
==雷达点云通过相机与雷达之间的标定关系投影到相机视角，并保留测量深度。==  
网络进一步构建出：  
- **雷达上下文特征（Radar Context Feature）**：雷达观测经过编码形成的特征。  
- **雷达占用（Radar Occupancy）**：由雷达特征预测的空间占用响应。  
要注意，Radar Occupancy 既不是目标的真实位置标签，也不是雷达为每个像素提供的精确深度。

③ **视锥特征构建（Frustum View Transformation）**  
这是 RVT 最关键的一步。  
图像上下文分别与两类空间信息结合：  
- **==视觉深度预测==**：Image Context Feature + Depth Distribution  
- **==雷达空间观测==**：Image Context Feature + Radar Occupancy  

==两路视锥特征 → 拼接 → 卷积，得到 **Frustum Feature（视锥特征）**。  ==
可以理解为：视觉深度预测提供一个空间分布，雷达占用响应补充物理测量线索，两者共同影响图像特征在视锥空间中的表示。

④ **BEV 变换（BEV Transformation）**  
最后，==将视锥空间中的特征按照几何关系映射到 BEV 网格。  ==
如果多个特征落入同一个 BEV 网格，由 Voxel Pooling 进行聚合，CRN 使用调整过的平均池化方式。  
输出的 Camera BEV Feature 可以用一个四维张量表示，例如 $[B,C,H,W]$，其中每个 BEV 网格对应一个 $C$ 维特征向量。实际通道数和网格尺寸需以 CRN 的配置为准。

**最重要的区别**：RVT 并不是直接将雷达点转换成 BEV 检测框，而是利用雷达观测辅助相机特征的空间变换。它输出的是供后续 MFA 使用的 BEV 特征，而不是最终检测结果。

**基础知识补充｜Depth Distribution 与 Radar Occupancy**

| 信息                        | 提供什么               | 为什么有用                    | 不足               |
| ------------------------- | ------------------ | ------------------------ | ---------------- |
| Camera Depth Distribution | 对多个候选深度区间的预测概率     | 图像位置覆盖相对密集；无 Radar 点也可预测 | 是预测值，可能不准        |
| Radar Occupancy           | 雷达观测经网络得到的视锥空间占用响应 | 提供额外的物理空间依据              | 雷达稀疏、误点／漏点、非真值标签 |

**教学例子**：相机认为一个位置在 10/20/30 m 的概率分别为 0.15/0.60/0.25，附近 Radar 检测到约 20 m 的有效反射。两者可互补；但不能据此认定这个像素真实深度必然为 20 m，更不能用单点替代整幅图像深度预测。

**关键局限**：Radar 点并不覆盖所有目标，Radar 反射也可能由多径或背景产生；==RVT 缓解而非彻底解决深度和空间定位误差。==

### 3.3 MFA — Multi-modal Feature Aggregation

**动机**：==已经获得 Camera BEV 和 Radar BEV，不代表两个模态对同一车辆的特征峰准确落在相同位置；直接逐位置相加或通道拼接本身不会主动寻找偏移后的相关位置。但拼接后若接卷积，也可能间接学习局部对应，因此不能绝对否定所有拼接方法。==

#### 3.3.1 MDCA — Multi-modal Deformable Cross Attention

**Query Feature**：==由 Camera/Radar BEV 信息构建的网络查询特征==；**不是 Radar Point**，也不等于真实车辆中心。

**Reference Point**：==与 Query 关联的参考空间位置==。**Sampling Offset**：==相对于该位置学习采样偏移==，回答“去哪里寻找信息”；**Attention Weight**：==学习不同采样结果的贡献==，回答“采到的信息使用多少”。

![Pasted image 20261028195714.png](assets/P002_CRN/Pasted%20image%2020261028195714.png)

① **输入：Camera BEV 与 Radar BEV**  
经过 RVT 和雷达特征编码，网络得到两张 BEV 特征图：  
- **Camera BEV**：视觉语义丰富，但空间位置可能存在误差。  
- **Radar BEV**：携带雷达空间测量相关信息，但特征可能稀疏或带有噪声。  
两者使用可比较的 BEV 空间表示，但同一目标的特征在两张图上未必完全对齐。

② **构建 Query**  
网络对 Camera BEV 和 Radar BEV 特征进行组合与投影，构建出 **Query Feature**。  
例如，某个 BEV 网格对应一个 64 维向量 $q_i = [q_1, q_2, \ldots, q_{64}]$（64 仅为教学示例，非 CRN 实际配置的固定通道数）。  
Query 是学习得到的特征向量，并非原始雷达测量点。

③ **Reference Point：参考位置**  
每个 Query 对应一个 BEV 空间中的参考位置 $p_i = (x_i, y_i)$，作为后续采样的起点。  
需要注意的是，Reference Point 并不保证恰好落在某辆车的真实中心。

④ **Sampling Offset 与 Attention Weight**  
这是 MDCA 的核心机制。  
假设 Query 位于网格 A，但对应车辆的 Radar 特征实际落在相邻网格 B，网络会学习两个东西：  

| 机制 | 作用 | 直观理解 |
|---|---|---|
| Sampling Offset | 决定从哪里采样 | 从 A 附近寻找可能相关的位置 B |
| Attention Weight | 决定不同采样结果的贡献 | 给更有用的特征分配较大权重 |

MDCA 可以分别从 Camera 和 Radar 特征图中采样，并学习相应的聚合权重。  
不过，权重由模型学习得到，并不保证每次都能正确识别噪声。

⑤ **在两种 BEV 特征图中采样**  
对于同一个 Query，网络可能从 Camera BEV 的若干位置提取视觉特征，同时从 Radar BEV 的若干位置提取雷达特征。  
这些采样点不必与 Query 位于同一网格。  
因此，相比简单的逐位置相加，MDCA 有机会利用空间上存在偏移但语义相关的信息。

⑥ **加权聚合**  
将采样得到的特征按学习到的注意力权重进行组合，可借助一个简化的概念公式理解：  
$$f_i^{\text{new}} = \sum_{k=1}^{K} w_{i,k} \, f_{i,k}$$  
其中：  
- $f_{i,k}$ 为第 $i$ 个 Query 采样得到的第 $k$ 个特征，  
- $w_{i,k}$ 为该采样特征对应的权重，  
- $f_i^{\text{new}}$ 为聚合后的更新特征。  

这是概念化公式，已省略 CRN 实际实现中的模态分支、注意力头以及投影等细节。

⑦ **更新融合 BEV 特征**  
MDCA 对参与计算的 Query 进行特征更新，形成融合后的 BEV 表示，再供下游三维检测等任务使用。  
这里需结合之前学过的 Sparse Aggregation：若开启 Top-K 筛选，并非全部 BEV Query 都会执行相同的 MDCA 聚合计算。

- **优势**：允许在相邻或其他相关位置自适应采样，缓解残余错位；只采样有限点，也减轻全局注意力的计算成本。
- **局限**：注意力权重是学得的，不保证会给每个噪声 Radar 点低权重；也不保证空间坐标全部被改正。

#### 3.3.2 Sparse Aggregation（稀疏聚合）

**动机**：在大范围 BEV 中，即使 MDCA 只对每个 Query 采少量点，所有 BEV 网格都作为 Query 仍然耗时。因此选择较高置信度的 **Top-K BEV Query** 执行昂贵聚合。

- 筛选依据与 Camera 深度分布、Radar Occupancy 的响应有关；**选择的是 BEV Query，不是原始 Radar 点数或图像像素数**。
- K 小：计算量较低，但可能错过有效位置；K 大：保留更多 Query，但计算量上涨。
- 未选中 Query 不代表对应 BEV 特征在整个网络中都被删除。

**作者附录 Table 13 部分数据**：

| Queries | Car AP | FPS |
|---|---|---|
| 1,024 | 49.8 | 14.1 |
| 4,096 | 54.0 | 14.0 |
| 8,192 | 54.6 | 13.8 |
| 65,536（全部） | 56.9 | 11.5 |

**注意**：这里是论文特定实验的 **Car AP**，不能当作 nuScenes 全类别 mAP；摘要中 20 FPS 的实时配置也不能与之混合。课堂曾引用 MFA 单模块延迟 21.01 → 4.96 ms，**不是整个系统端到端时延**。
### 3.4 Training Objectives and Task Heads

#### 3.4.1 Depth Supervision（深度监督）

训练时可将 LiDAR 点投影到相机视角，生成深度监督，指导图像深度分布网络学习。完成训练后，图像分支已学习相关参数；实际推理使用 Camera + Radar 输入，**不需要重复输入训练用 LiDAR 深度标签**。这是 Training-time supervision 与 Inference-time sensor input 的区别。
#### 3.4.2 Detection Head 与 Tracking

**BEV Feature Map 不等于 3D Bounding Box。** 检测头将融合特征转为目标中心、类别、位置、尺寸、朝向等预测，CRN 采用 CenterPoint 风格的检测思想。Tracking 再通过跨帧关联判断不同时间检测出的框属于哪个物体，不能仅凭单帧检测完成身份连续性。
#### 3.4.3 BEV Segmentation

除了检测与跟踪，CRN 还利用 BEV 特征预测车辆、可行驶区域等语义结果；这是 **BEV 上的语义分割**，与输出每个雷达点类别并非同一任务。

---

## Step 4｜Experiments：用实验证据判断方法是否有效

### 4.1 Experimental Setup（实验设置）

- **数据集与任务**：以 nuScenes 上的 3D 检测为主要讨论对象；不能把特定类别 Car AP 与全类别 mAP 混用。
- **评价指标**：mAP 评价检测准确性；mATE 衡量位置误差（越低越好）；NDS 为 nuScenes 综合检测指标（越高越好）。不同指标不能相互替代。
- **LiDAR-free 的边界**：推理时使用 Camera + Radar，不意味着训练阶段没有使用 LiDAR 深度监督或数据集标注。
- **公平比较**：记录 Backbone（如 R18/R50）、输入模态、训练配置、数据划分、测试协议、精度模式与推理硬件。不能把不同配置之间的全部差异归因于某个模块。

### 4.2 Main Results（主要结果）

![Pasted image 20261030141556.png](assets/P002_CRN/Pasted%20image%2020261030141556.png)

完整 CRN 模型在论文所报告的配置中具有较强的 3D 检测表现；但**完整模型优于另一模型**只说明相应设置下整体方案的表现，**不能直接证明全部提升来自 RVT 或 MFA**。判断模块贡献需要消融实验。不同 Backbone 和 FPS 配置必须分开解读。
### 4.3 Ablation Studies（消融实验）

#### 4.3.1 RVT 消融

![Pasted image 20261030141648.png](assets/P002_CRN/Pasted%20image%2020261030141648.png "原Obsidian宽度：404")

比较不同视角变换信息来源，考查 Radar 空间观测辅助 Camera 深度/BEV 变换是否有益。**RVT 缓解深度不确定性，不是直接把 Radar 距离设为每个像素的真值深度。**

#### 4.3.2 MFA 消融

![Pasted image 20261030141736.png](assets/P002_CRN/Pasted%20image%2020261030141736.png "原Obsidian宽度：417")

比较不同跨模态融合方式，考查可变形跨模态采样与聚合的效果。**MFA 有机会缓解 BEV 特征错位，不代表所有标定误差和定位误差均被消除。**

#### 4.3.3 Sparse Aggregation 消融

见 Step 3.3.2 已保留的作者附录 Table 13 数据：Top-K 1,024、4,096、8,192、65,536 对应不同 Car AP 和 FPS。随着 K 减小，计算可能更快，但会损失部分检测精度。**模块耗时下降不等于整条推理流水线同比例加速。**

### 4.4 Robustness & Efficiency（鲁棒性与效率）

#### 4.4.1 Camera View Drop（相机视角丢失）

以下为此前精读时记录的 **Car mAP**，不是全类别 mAP；用于理解不同退化条件下的比较，正式引用时仍应对照论文表格与实验协议。

| 丢失 Camera 视角数 | BEVDepth（Camera） | BEVFusion（Camera + Radar） | CRN（Camera + Radar） |
|---:|---:|---:|---:|
| 0 | 49.4 | 63.9 | 68.8 |
| 1 | 41.1 | 58.5 | 62.4 |
| 3 | 24.2 | 45.7 | 48.9 |
| 6 | 0 | 14.3 | 12.8 |

- Camera 丢失 3 个视角时，CRN 的剩余 Car mAP 48.9 高于 BEVFusion 的 45.7。
- **绝对下降值**：CRN = 68.8 − 48.9 = **19.9 个百分点**；BEVFusion = 63.9 − 45.7 = **18.2 个百分点**。因此剩余精度更高不等于下降幅度更小。
- Camera 全部 6 个视角丢失时，CRN（12.8）低于 BEVFusion（14.3）。**Camera 全失效不等于 Camera 和 Radar 同时失效。**

#### 4.4.2 Radar View Drop（雷达视角丢失）

| 丢失 Radar 视角数 | BEVFusion Car mAP | CRN Car mAP |
|---:|---:|---:|
| 0 | 63.9 | 68.8 |
| 1 | 59.9 | 64.3 |
| 3 | 50.9 | 57.0 |
| 6 | 34.4 | 43.8 |

这类人为输入丢弃实验**不等于**真实遮挡、暴雨、浓雾、杂波、多径或标定漂移实验；不能把某一种退化条件的结论推广到所有传感器故障。

#### 4.4.3 Efficiency（效率）

- FPS 与延迟需结合 GPU、Backbone、batch size、输入分辨率、精度模式、预处理/后处理及测试协议解释。
- 论文/仓库报告的速度不能直接证明实验室服务器能够达到相同 FPS。
- Top-K 的精度—速度权衡需要和完整模型的推理时间分开评价。


---

## Step 5｜Related Work + Conclusion：研究定位与结论

### 5.1 Related Work（相关研究定位）

- **Camera-based BEV 3D Detection**：图像语义丰富，但 Camera-to-BEV 视角变换存在深度不确定性。
- **Radar-Camera Fusion**：利用 Radar 测距/运动线索补充 Camera，但 Radar 稀疏、存在误测，且跨模态特征可能错位。
- **BEV Feature Aggregation / Deformable Attention**：在统一空间中学习相关位置的采样和特征聚合。

CRN 是 Radar-Camera 三维感知研究，**不是 Radar-Camera-VLM 模型**。后续 VLM 相关研究设想应单独标注为个人假设。

### 5.2 Conclusion（结论与证据边界）

| 模块 | 要解决的问题 | 已学实验支持的结论 | 不应过度宣称 |
|---|---|---|---|
| RVT | Camera 深度/空间变换不确定性 | Radar 辅助视角变换有助于检测表现 | 彻底消除深度误差 |
| MFA | 两种 BEV 特征残余错位与融合 | 相关消融支持该聚合机制的作用 | 自动纠正全部标定/定位错误 |
| Sparse Aggregation | 大量 BEV Query 的聚合开销 | 存在可量化的精度—速度权衡 | 模块加速即端到端同比加速 |

**研究边界**：View Drop ≠ 真实局部遮挡；局部遮挡 ≠ Radar-only；Camera 全视角丢失 ≠ 所有传感器全部失效。某一实验条件下更高 AP ≠ 所有恶劣天气中更鲁棒。
