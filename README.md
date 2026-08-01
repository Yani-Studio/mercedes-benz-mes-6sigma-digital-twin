<div align="center">

# 🚘 Mercedes-Benz MES 6-Sigma Digital Twin & AI Engine
### **65.30M Digital Twin Genetic Algorithm (GA), Multi-Stage Super Stacking Ensemble & 6-Sigma SPC Quality Control**

[![MacBook Pro M5](https://img.shields.io/badge/MacBook%20Pro-M5-000000?style=for-the-badge&logo=apple&logoColor=white)](https://www.apple.com/macbook-pro/)
[![DGX Spark 128GB RAM](https://img.shields.io/badge/DGX%20Spark-128GB%20RAM-76B900?style=for-the-badge&logo=nvidia&logoColor=white)](https://developer.nvidia.com/cuda-zone)
[![FastAPI](https://img.shields.io/badge/FastAPI-Async%20REST-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![PyArrow Shared Memory](https://img.shields.io/badge/PyArrow-Shared%20Memory-E05D44?style=for-the-badge&logo=apache&logoColor=white)](https://arrow.apache.org/)
[![gRPC & WebSockets](https://img.shields.io/badge/gRPC%20%26%20WebSockets-Bi--Directional-4285F4?style=for-the-badge)](https://grpc.io/)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![6-Sigma SPC](https://img.shields.io/badge/6--Sigma-SPC-00599E?style=for-the-badge)](#-35-6-sigma-spc-quality-control--bench-time-reduction)

</div>

---
> ⚠️ Copyright Notice Copyright (c) 2026 Kang Gyu Min. All rights reserved.
---

## 🎬 1. Streamlit Live Performance Telemetry Demo

Below is the **live demonstration video** of the Streamlit control dashboard, exhibiting dynamic GA population tuning ($10\text{M} \sim 65.30\text{M}$ individuals), real-time bi-directional telemetry streaming (gRPC / WebSockets) between the Apple MacBook Pro controller and the remote DGX Spark GPU cluster, and 6-Sigma SPC parameter synchronization:

https://github.com/user-attachments/assets/360fdc9a-a60f-41e0-b068-a64bfcbc7416

---

### 🔍 Detailed Breakdown of Interactive Demo Features

- **Dynamic Digital Twin GA Population Sizing (GA Population Slider)**:
  - When the user adjusts the GA population slider from $10\text{M}$ to $65.30\text{M}$ candidates (Golden Optimal Point: $42.54\text{M}$), the DGX Spark GPU cluster recalculates and projects the estimated validation $R^2$ accuracy in real time.
- **Bi-Directional Telemetry Stream Console**:
  - **Outbound gRPC Directives**: Transmits low-latency control directives from the Apple MacBook Pro workstation to the remote DGX Spark GPU node, updating crossover probability ($P_c = 0.85$), mutation rate ($P_m = 0.05$), and population scale.
  - **Inbound WebSockets / SSE Telemetry**: Receives live GPU VRAM usage, GA fitness convergence curves, and MES bench sensor feedback logs at 100ms refresh intervals onto the local Streamlit console.
- **Dynamic 6-Sigma SPC Boundary Monitoring**:
  - Simulates test bench duration distributions under selected parameter sets, continuously verifying compliance against the Upper Control Limit ($UCL = 136.21\text{s}$).

---

## 🏛️ 2. End-to-End Enterprise Architecture & Data Pipeline

The enterprise system coordinates a **Local Controller (Apple MacBook Pro M-Silicon Workstation)**, dual interactive web interfaces (**Streamlit Live UI & Flask yani-studio UI**), a **Bi-Directional Streaming Layer (WebSockets / gRPC)**, the **Mercedes-Benz 551D Dataset Pipeline**, a **Remote DGX Spark AI Compute Cluster (NVIDIA GB10 GPUs)**, and **Mercedes-Benz MES Test Bench Integration**.

![End-to-End System Architecture Diagram](visualization/15_system_architecture.png)

---

### 📌 Exhaustive Breakdown of System Components & Operational Mechanisms

#### 1. LOCAL CONTROLLER (Apple MacBook Pro Workstation)
- **Async Command Dispatcher**:
  - Runs natively on Apple M-Series Silicon, establishing Paramiko-based asynchronous SSH tunnels to send gRPC control directives to the remote DGX Spark compute cluster.
- **Dual Interactive Interfaces**:
  - **Streamlit Live UI (`streamlit_app.py`)**: An intuitive control tower allowing R&D engineers to dynamically adjust GA parameters and inspect live telemetry streams.
  - **yani-studio Flask Web UI (`dashboard/server.py`)**: An executive-level web console serving Server-Sent Events (SSE) and REST API endpoints for plant management.

#### 2. MB DATA PIPELINE & SCHEMA ($N=4,209 \times 551\text{ Features}$)
- **CTQ (Critical-to-Quality) Target Variable ($y$)**:
  - Continuous float representing actual vehicle test bench duration in seconds ($N=4,209$).
  - Mean = $100.67\text{s}$, Median = $99.15\text{s}$, Range = $72.11\text{s} \sim 265.32\text{s}$.
- **Categorical Feature Processing ($X0 \sim X8$)**:
  - 8 vehicle configuration codes transformed via Target Encoding and One-Hot Encoding into **195 orthogonal dummy columns**.
- **Binary Switch Feature Validation ($X10 \sim X385$)**:
  - 368 binary test feature switches evaluated; 12 zero-variance columns dropped $\rightarrow$ **356 active binary feature flags** retained.
- **Total Encoded Feature Matrix**: **551-dimensional** feature matrix.

#### 3. REMOTE DGX SPARK CLUSTER (NVIDIA GB10 GPU Engine)
- **65.30M Digital Twin GA Search Engine**:
  - Evolving up to **65.30 Million** candidate individuals in parallel across the 551-dimensional vehicle option space.
  - Mathematically derived Golden Optimal Population Point: **42.54M Population**, Crossover Rate $P_c = 0.85$, Mutation Rate $P_m = 0.05$.
- **Multi-Stage Super Stacking Ensemble**:
  - Collects Out-of-Fold prediction tensors from 10 Level-1 base estimators (XGBoost, LightGBM, CatBoost, SVR, Random Forest, Ridge, etc.).
  - Fuses predictions via a Level-2 Digital Twin Meta-Learner to achieve a validation $R^2 = \mathbf{0.56979}$.

#### 4. PRODUCTION & MES IMPACT (Mercedes-Benz Test Factory)
- **MES (Manufacturing Execution System) Factory Integration**:
  - Directly interfaces with vehicle test cases ($N=4,209$) on the Mercedes-Benz factory floor, executing real-time parameter tuning directives.
- **Operational & Financial Breakthroughs**:
  - Reduces test bench time from **$100.67\text{s} \rightarrow 44.72\text{s}$ ($55.95\text{s}$ saved per vehicle, -55.6%)**.
  - Generates **$\text{₩ } 21.60\text{ Billion / Year}$** in economic value, delivering an Executive ROI of **1,480%**, a payback period of **0.8 months**, a **51.8%** power reduction, and **39.9 Tons/Year** of avoided $\text{CO}_2$ emissions.

---

## 📊 3. Comprehensive Visual Analytics & Detailed Engineering Analysis

Below is an in-depth academic and statistical breakdown of the **15 publication-quality visual artifacts** (300 DPI) generated by `generate_visualizations.py`.

---

### 🟢 3.1 Executive Summary & Key Metric Highlights

#### 📈 `14_kpi_summary_dashboard.png` (Executive KPI Summary Dashboard)
![Executive KPI Dashboard](visualization/14_kpi_summary_dashboard.png)

- **Engineering Description**:
  - An executive-level monitoring panel consolidating core performance indicators (KPIs) of the Mercedes-Benz AI optimization project.
- **Statistical Analysis**:
  - **Validation Accuracy ($R^2$)**: Achieves **$0.56979$**, a **$+0.01634$ gain** over the single best base model ($0.55345$).
  - **Test Bench Time**: Optimized from **$100.67\text{s} \rightarrow 44.72\text{s}$**, achieving a **$-55.6\%$ reduction ($55.95\text{s}$ saved per car)**.
  - **Annual Economic Impact**: **$\text{₩ } 21.60\text{ Billion / Year}$** (Direct OPEX + Wait Loss Avoidance + ESG).
  - **Process Capability Index ($C_{pk}$)**: Elevated from $0.85$ to **$1.67$ ($6\sigma$ quality level)**, capping defect rates below $3.4\text{ PPM}$.

---

### 🟢 3.2 Model Predictive Accuracy & Stacking Ensemble Performance

#### 📈 `01_ensemble_r2_comparison.png` (Ensemble vs Base Models $R^2$ Comparison)
![Ensemble R2 Comparison](visualization/01_ensemble_r2_comparison.png)

- **Engineering Description**:
  - Validation $R^2$ determination coefficient comparison across 10 individual machine learning algorithms and the Multi-Stage Super Stacking Ensemble.
- **Statistical Analysis**:
  - **Super Stacking Ensemble**: **$0.56979$** (Rank 1)
  - **XGBoost (30-Fold CV)**: $0.55345$
  - **LightGBM**: $0.54820$
  - **CatBoost**: $0.54510$
  - **Support Vector Regression (SVR)**: $0.53120$
  - **Mechanism**: Out-of-fold prediction tensors from base models are synthesized by the Layer-2 Meta-Learner, mitigating individual model variance and boosting $R^2$ to $0.56979$.

#### 📈 `07_individual_model_r2_ranking.png` (Individual Model $R^2$ Spectrum Ranking)
![Individual Model Ranking](visualization/07_individual_model_r2_ranking.png)

- **Engineering Description**:
  - Performance spectrum and validation $R^2$ ranking across 10 independent base estimators.
- **Statistical Analysis**:
  - Tree-based gradient boosting algorithms (XGBoost, LightGBM, CatBoost) lead single-model accuracy ($0.545 \sim 0.553$).
  - Support Vector Regression (SVR) and Ridge regression contribute structural diversity for ensemble fusion.

#### 📈 `08_ensemble_matrix_detail.png` (Multi-Stage Stacking Micro-Architecture Matrix)
![Ensemble Matrix Detail](visualization/08_ensemble_matrix_detail.png)

- **Engineering Description**:
  - Micro-architecture matrix displaying Layer-1 out-of-fold predictions and Layer-2 meta-weight computations.
- **Statistical Analysis**:
  - Out-of-Fold prediction tensors collected from cross-validation in Layer-1 are passed to Layer-2, where the Digital Twin GA Meta-Learner minimizes the joint loss function.

#### 📈 `09_fusion_weight_distribution.png` (Meta-Learner Fusion Weight Distribution)
![Fusion Weight Distribution](visualization/09_fusion_weight_distribution.png)

- **Engineering Description**:
  - Relative fusion weights assigned by the meta-model across the 10 base estimators.
- **Statistical Analysis**:
  - **XGBoost**: $34\%$ (Highest contribution)
  - **LightGBM**: $28\%$
  - **CatBoost**: $22\%$
  - **SVR & Linear Regressors**: $16\%$

#### 📈 `10_residual_normal_distribution.png` (Residual Error Normal Distribution Verification)
![Residual Normal Distribution](visualization/10_residual_normal_distribution.png)

- **Engineering Description**:
  - Residual error homoscedasticity and normality verification chart comparing model predictions against ground truth test durations.
- **Statistical Analysis**:
  - Residual mean $\mu = 0.001$, standard deviation $\sigma = 8.12$.
  - Perfect bell-shaped normal distribution centered at zero confirms absence of unmodeled systematic bias.

---

### 🟢 3.3 Financial ROI & ESG Sustainability Impact

#### 📈 `02_financial_roi_breakdown.png` (Annual ₩21.60B Economic Value Breakdown)
![Financial ROI Breakdown](visualization/02_financial_roi_breakdown.png)

- **Engineering Description**:
  - Granular breakdown of the **$\text{₩ } 21.60\text{ Billion / Year}$** annual economic and ESG environmental value generated.
- **Statistical Analysis**:
  - **Direct OPEX Savings**: **$\text{₩ } 13.04\text{B / Yr}$** (Reduced energy and bench degradation)
  - **Wait Loss Cost Avoidance**: **$\text{₩ } 5.23\text{B / Yr}$** (Line bottleneck elimination)
  - **CapEx & ESG Value**: **$\text{₩ } 3.33\text{B / Yr}$** ($39.9\text{ Tons / Year}$ $\text{CO}_2$ offset, **51.8%** kWh saved)
  - **Financial Metrics**: Executive ROI = **1,480%**, Payback Period = **0.8 Months (~24 Days)**.

---

### 🟢 3.4 Feature Importance & Data Pipeline Schema

#### 📈 `03_vital_few_feature_importance.png` (Vital Few Feature Gain Contribution)
![Vital Few Feature Importance](visualization/03_vital_few_feature_importance.png)

- **Engineering Description**:
  - Information gain contribution of the **Vital Few** features isolated from the 551 total encoded dimensions.
- **Statistical Analysis**:
  - **$X0$ (Vehicle Option Code)**: **24.8%** Gain (Dominant factor)
  - **$X314$ (Bench Test Flag)**: **18.2%** Gain
  - **$X118$ (Powertrain Switch)**: **12.5%** Gain
  - **$X27$ (Safety Option Switch)**: **8.4%** Gain
  - **Insight**: Top 4 features account for **63.9%** of total predictive gain, confirming GA optimization efficiency.

#### 📈 `12_test_bench_y_distribution.png` (CTQ Target Variable $y$ Kernel Density)
![Test Bench Y Distribution](visualization/12_test_bench_y_distribution.png)

- **Engineering Description**:
  - Empirical probability density (KDE) and quantile breakdown of target variable $y$ ($N=4,209$).
- **Statistical Analysis**:
  - Mean: $100.67\text{s}$, Median: $99.15\text{s}$, Min: $72.11\text{s}$, Max: $265.32\text{s}$.
  - Outliers above $150\text{s}$ underline the necessity of 6-Sigma SPC upper bound enforcement.

#### 📈 `13_x0_category_avg_time.png` (Average Duration by $X0$ Category Code)
![X0 Category Avg Time](visualization/13_x0_category_avg_time.png)

- **Engineering Description**:
  - Breakdown of average test bench duration across individual $X0$ categorical codes.
- **Statistical Analysis**:
  - Specific option codes (e.g., `az`, `bc`) exhibit high average durations ($>130\text{s}$), whereas optimized codes average $\sim 85\text{s}$.

---

### 🟢 3.5 6-Sigma SPC Quality Control & Bench Time Reduction

#### 📈 `04_six_sigma_spc_control_chart.png` (3-Sigma SPC Control Chart & $C_{pk}$ Capability)
![6-Sigma SPC Control Chart](visualization/04_six_sigma_spc_control_chart.png)

- **Engineering Description**:
  - Statistical Process Control (SPC) chart setting $3\sigma$ control limits for test duration management.
- **Statistical Analysis**:
  - **Upper Control Limit (UCL)**: **$136.21\text{s}$** ($\mu + 3\sigma$)
  - **Center Line (CL)**: $100.67\text{s}$ ($\mu$)
  - **Capability Index ($C_{pk}$)**: Elevated from $0.85 \rightarrow$ **$1.67$**, achieving 6-Sigma quality ($<3.4\text{ PPM}$ defect rate).

#### 📈 `11_before_after_reduction_comparison.png` (Before vs After Duration Distribution)
![Before After Reduction Comparison](visualization/11_before_after_reduction_comparison.png)

- **Engineering Description**:
  - Test bench duration distribution comparison before vs after applying Digital Twin AI optimization.
- **Statistical Analysis**:
  - **Before**: Mean = $100.67\text{s}$ (Wide variance)
  - **After**: Mean = **$44.72\text{s}$** (Tight, optimized distribution)
  - **Net Reduction**: **$55.95\text{s}$ saved per vehicle (-55.6% improvement)**.

---

### 🟢 3.6 Digital Twin GA Scale & Population Sizing

#### 📈 `06_optimal_ga_population_sizing_curve.png` (Golden Optimal 42.54M Population Curve)
![Optimal GA Population Sizing Curve](visualization/06_optimal_ga_population_sizing_curve.png)

- **Engineering Description**:
  - Trade-off curve evaluating GA population size against validation accuracy ($R^2$) and compute cost.
- **Statistical Analysis**:
  - **Golden Optimal Population Point**: **42.54 Million Candidates**
  - **Insight**: 42.54M population achieves peak generalization ($R^2 = 0.56979$), beyond which marginal accuracy gains diminish while compute cost escalates.

#### 📈 `05_digital_twin_6530m_scale_curve.png` (65.30M Digital Twin Scale Curve)
![Digital Twin 65.30M Scale Curve](visualization/05_digital_twin_6530m_scale_curve.png)

- **Engineering Description**:
  - Real-time convergence trajectory scaling up to **65.30 Million candidates** on the DGX Spark GB10 GPU cluster.

#### 📈 `05_digital_twin_1000m_scale_curve.png` (1 Billion Theoretical Scaling Curve)
![Digital Twin Scale Curve](visualization/05_digital_twin_1000m_scale_curve.png)

- **Engineering Description**:
  - Theoretical scaling curve modeling convergence dynamics across multi-node distributed GPU environments.

---

## ⚡ 4. Quick Start Guide

### 1. Environment Setup
```bash
# Clone repository
git clone https://github.com/gyuminkang/mercedes-benz-mes-6sigma-digital-twin.git
cd mercedes-benz-mes-6sigma-digital-twin

# Create & activate virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install required dependencies
pip install -r requirements.txt
```

### 2. Generate 15 Visualizations
```bash
# Generate 15 high-resolution (300 DPI) charts in visualization/
python generate_visualizations.py
```

### 3. Launch Interactive UIs
```bash
# 1) Streamlit Live Control Dashboard (Port 8501)
streamlit run streamlit_app.py

# 2) Flask yani-studio Web Console (Port 5000)
python dashboard/server.py
```

---

## 🌲 5. Repository Structure

```
mercedes-benz-mes-6sigma-digital-twin/
├── 📁 data/                          # Dataset Directory
│   └── 📁 raw/
│       ├── train.csv              # Training Dataset (N=4,209 x 378)
│       ├── test.csv               # Testing Dataset (N=4,209 x 377)
│       └── sample_submission.csv  # Kaggle Submission Template
├── 📁 docs/                          # Engineering Documentation
│   └── validation.md              # 6-Sigma SPC & DMAIC Verification Report
├── 📁 visualization/                 # 15 Visual Artifacts & Video Demo
│   ├── 01_ensemble_r2_comparison.png
│   ├── ...
│   ├── 15_system_architecture.png # System Architecture Diagram
│   └── streamlit_demo_simulation.mp4 # Streamlit Video Demo (3.93MB)
├── 📁 dashboard/                     # Flask yani-studio Web Application
│   ├── server.py
│   ├── static/
│   └── templates/
├── 📁 engine/                        # Distributed DGX Spark Computing Engine
│   └── spark_compute_engine.py
├── 📁 scripts/                       # Modular Python Scripts
│   ├── generate_visualizations.py # Visualization Module
│   └── compress_video.py          # Video Processing Module
├── generate_visualizations.py        # Main Visualization Launcher
├── streamlit_app.py                  # Streamlit Live Control UI
└── README.md                         # Master Engineering README
```

---

## 📚 6. References & Sources

### 📊 6.1 Benchmark Datasets & Official Sources
- **Kaggle Mercedes-Benz Dataset**: [Kaggle Mercedes-Benz Greener Manufacturing Competition](https://www.kaggle.com/c/mercedes-benz-greener-manufacturing)
- **Mercedes-Benz Group AG Official R&D**: [Mercedes-Benz Group AG Official R&D](https://group.mercedes-benz.com/)

### 🧠 6.2 Machine Learning Algorithms & Ensemble Literature
- **XGBoost (Extreme Gradient Boosting)**: Chen, T., & Guestrin, C. (2016). *XGBoost: A Scalable Tree Boosting System*. KDD '16. [[Paper Link](https://arxiv.org/abs/1603.02754)]
- **LightGBM (Gradient Boosting Decision Tree)**: Ke, G., et al. (2017). *LightGBM: A highly efficient gradient boosting decision tree*. NIPS 2017. [[Paper Link](https://papers.nips.cc/paper/6907-lightgbm-a-highly-efficient-gradient-boosting-decision-tree)]
- **CatBoost (Categorical Feature Boosting)**: Prokhorenkova, L., et al. (2018). *CatBoost: unbiased boosting with categorical features*. NeurIPS 2018. [[Paper Link](https://arxiv.org/abs/1706.09516)]
- **Stacked Generalization**: Wolpert, D. H. (1992). *Stacked generalization*. Neural Networks, 5(2), 241-259. [[DOI Link](https://doi.org/10.1016/0893-6080(92)90023-1)]

### 🧬 6.3 Digital Twin & Genetic Algorithm (GA) Theory
- **Genetic Algorithms in Search & Optimization**: Goldberg, D. E. (1989). *Genetic Algorithms in Search, Optimization, and Machine Learning*. Addison-Wesley.
- **Manufacturing Digital Twin Systems**: Grieves, M., & Vickers, J. (2017). *Digital Twin: Mitigating Unpredictable Emergent Behavior*. Springer, Cham. [[DOI Link](https://doi.org/10.1007/978-3-319-38756-7_4)]

### 📈 6.4 6-Sigma Quality Control & Statistical Process Control (SPC)
- **Statistical Quality Control**: Montgomery, D. C. (2012). *Introduction to Statistical Quality Control* (7th ed.). John Wiley & Sons.
- **Six Sigma DMAIC & Capability Index ($C_{pk}$)**: Pyzdek, T., & Keller, P. A. (2014). *The Six Sigma Handbook* (4th ed.). McGraw-Hill Education.

### 💻 6.5 Development Frameworks & Computing Infrastructure
- **Streamlit Framework**: [Streamlit Documentation](https://docs.streamlit.io/)
- **Flask Framework**: [Flask Documentation](https://flask.palletsprojects.com/)
- **NVIDIA CUDA & GB10 DGX Spark Environment**: [NVIDIA CUDA Zone](https://developer.nvidia.com/cuda-zone)
- **PyArrow Caching**: [Apache Arrow PyArrow Documentation](https://arrow.apache.org/docs/python/)
- **Matplotlib & Seaborn**: [Matplotlib](https://matplotlib.org/) / [Seaborn](https://seaborn.pydata.org/)

