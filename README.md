<div align="center">

# 🚘 Mercedes-Benz Greener Manufacturing
### **65.30M Digital Twin GA Optimization, Multi-Stage Super Stacking & 6-Sigma SPC Control**

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![NVIDIA GB10 GPU](https://img.shields.io/badge/NVIDIA%20CUDA-GB10%20Cluster-76B900?style=for-the-badge&logo=nvidia&logoColor=white)](https://developer.nvidia.com/cuda-zone)
[![Validation R2](https://img.shields.io/badge/Validation%20R%C2%B2-0.56979-brightgreen?style=for-the-badge)](#-model-performance--benchmark)
[![Bench Time Reduction](https://img.shields.io/badge/Bench%20Time--55.6%25-blueviolet?style=for-the-badge)](#-manufacturing--mes-impact)
[![Annual Economic Value](https://img.shields.io/badge/Annual%20Value-%E2%82%A9%2021.60B-success?style=for-the-badge)](#-financial--esg-roi-breakdown)
[![Executive ROI](https://img.shields.io/badge/ROI-1480%25-ff69b4?style=for-the-badge)](#-financial--esg-roi-breakdown)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)

</div>

---

## 🏛️ End-to-End System & Data Architecture

The system coordinates a **Local Controller (Apple MacBook Pro M-Silicon Workstation)**, dual interactive web interfaces (**Streamlit Live UI & Flask yani-studio UI**), a **Bi-Directional Streaming Layer (WebSockets / gRPC)**, the **Mercedes-Benz 551D Dataset Pipeline**, a **Remote DGX Spark AI Compute Cluster (NVIDIA GB10 GPUs)**, and **Mercedes-Benz MES Test Bench Integration**.

![End-to-End System Architecture](visualization/15_system_architecture.png)

---

## 🚀 Key Performance & Financial Highlights

| Metric | Baseline | DGX Spark AI Engine | Delta / Improvement |
| :--- | :---: | :---: | :---: |
| **Validation $R^2$ Score** | `0.55345` (Best Single Model) | **`0.56979`** (Super Stacking) | **$+0.01634$ Gain** |
| **Mean Bench Duration** | `100.67 seconds` | **`44.72 seconds`** | **▼ 55.6% (-55.95s / car)** |
| **6-Sigma Quality ($C_{pk}$)** | $0.85$ ($3\sigma$) | **`1.67` ($6\sigma$)** | **$< 3.4$ PPM Defect Rate** |
| **Annual Economic Value** | Baseline Cost | **`₩ 21.60 Billion / Year`** | Direct OPEX + Wait Loss + ESG |
| **Executive ROI** | N/A | **`1,480%`** | **Payback: 0.8 Months** |
| **Carbon Offset ($\text{CO}_2$)** | Baseline Emissions | **`39.9 Tons CO₂ / Year`** | **51.8% kWh Power Saved** |

---

## 💻 Tech Stack & Remote Cluster Orchestration

- **Local Workstation**: Apple MacBook Pro (M-Series Silicon, Paramiko SSH Async Tunneling)
- **Dual Interactive UIs**:
  - **Streamlit Live Dashboard** (`streamlit_app.py`): Real-time GA population slider ($10\text{M} \sim 65.30\text{M}$), live fitness curve, interactive telemetry stream.
  - **yani-studio Flask Web UI** (`dashboard/server.py`): Executive control console, SSE live execution logs, REST API endpoints.
- **Bi-Directional Communication Engine**: WebSockets, gRPC async directives, Server-Sent Events (SSE) telemetry synchronization.
- **Remote Compute Cluster**: DGX Spark (NVIDIA GB10 GPU Acceleration Engine).
- **ML & Statistical Modeling Pipeline**: XGBoost, LightGBM, CatBoost, SVR, Random Forest, Ridge, ElasticNet, Multi-Stage Super Stacking Ensemble.

---

## 📊 15-Chart Visual Analytics Suite

The repository automatically generates **15 high-resolution (300 DPI) publication-ready charts** in the `visualization/` directory:

| Chart # | Title | Key Insight Visualized |
| :---: | :--- | :--- |
| **01** | `01_ensemble_r2_comparison.png` | Validation $R^2$ ranking comparing Super Stacking (`0.56979`) vs 10 base models. |
| **02** | `02_financial_roi_breakdown.png` | ₩21.60B/Yr economic value breakdown (OPEX, Wait Loss, CapEx/ESG). |
| **03** | `03_vital_few_feature_importance.png` | Vital Few feature gain drivers ($X0: 24.8\%, X314: 18.2\%, X118: 12.5\%, X27: 8.4\%$). |
| **04** | `04_six_sigma_spc_control_chart.png` | $3\sigma$ SPC control chart with UCL limit ($136.21\text{s}$) & $C_{pk}=1.67$. |
| **05** | `05_digital_twin_6530m_scale_curve.png` | Digital Twin GA population scale curve up to **65.30 Million** individuals. |
| **06** | `06_optimal_ga_population_sizing_curve.png` | **42.54 Million GA Population** Golden Optimal Point derivation. |
| **07** | `07_individual_model_r2_ranking.png` | Individual model performance spectrum and baseline comparison. |
| **08** | `08_ensemble_matrix_detail.png` | Multi-stage stacking matrix weights and layer-1 meta-learner fusion. |
| **09** | `09_fusion_weight_distribution.png` | Optimal fusion weight distribution across base estimators. |
| **10** | `10_residual_normal_distribution.png` | Model prediction residual normal distribution & homoscedasticity check. |
| **11** | `11_before_after_reduction_comparison.png` | Test bench duration histogram (Before: $100.67\text{s}$ vs After: $44.72\text{s}$). |
| **12** | `12_test_bench_y_distribution.png` | Mercedes-Benz CTQ target variable $y$ kernel density & quantiles. |
| **13** | `13_x0_category_avg_time.png` | Top categorical feature $X0$ option code duration impact. |
| **14** | `14_kpi_summary_dashboard.png` | Complete Executive KPI Summary Dashboard. |
| **15** | `15_system_architecture.png` | **End-to-End System & MB Data Pipeline Architecture Diagram**. |

---

## ⚡ Quick Start Guide

### 1. Environment Setup
```bash
# Clone the repository
git clone https://github.com/gyuminkang/mercedes-benz-greener-manufacturing.git
cd mercedes-benz-greener-manufacturing

# Initialize Python virtual environment
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2. Generate 15 Visualizations
```bash
# Render all 15 high-resolution (300 DPI) charts in English
python generate_visualizations.py
```

### 3. Launch Interactive UIs
```bash
# Streamlit Live Performance Dashboard
streamlit run streamlit_app.py

# Flask Executive Web Console (yani-studio)
python dashboard/server.py
```

---

## 📦 Mercedes-Benz Dataset Schema ($N=4,209 \times 551\text{ Features}$)

- **CTQ Target Variable ($y$)**: Continuous test bench duration in seconds ($N=4,209$ training samples, $N=4,209$ testing samples).
- **Categorical Features ($X0 \sim X8$)**: 8 vehicle option configuration codes, encoded into **195 dummy columns**.
- **Binary Feature Switches ($X10 \sim X385$)**: 368 test bench feature flags. 12 zero-variance columns dropped $\rightarrow$ **356 active binary features**.
- **Total Encoded Feature Matrix**: $551$ dimensions.

---

## 🌲 Repository Structure

```
mercedes-benz-greener-manufacturing/
├── data/                          # Mercedes-Benz Dataset Subdirectory
│   └── raw/
│       ├── train.csv              # Training Dataset (N=4,209 x 378)
│       ├── test.csv               # Testing Dataset (N=4,209 x 377)
│       └── sample_submission.csv
├── docs/                          # Project Documentation & Reports
│   └── validation.md              # 6-Sigma SPC & DMAIC Verification Report
├── visualization/                 # 15 High-Resolution PNG Visualizations (300 DPI)
│   ├── 01_ensemble_r2_comparison.png
│   ├── ...
│   └── 15_system_architecture.png
├── dashboard/                     # Flask yani-studio Web UI Application
│   ├── server.py
│   ├── static/
│   └── templates/
├── engine/                        # Distributed DGX Spark Computing Engine
│   └── spark_compute_engine.py
├── scripts/                       # Modular Python Scripts
│   └── generate_visualizations.py # 15-Chart Automated Rendering Engine
├── generate_visualizations.py    # Main Visualization Launcher
├── streamlit_app.py               # Streamlit Live Control & Telemetry Dashboard
└── README.md
```

---

## 📄 License & Citation

This project is licensed under the **MIT License**.

```
Mercedes-Benz Greener Manufacturing Digital Twin System
Copyright (c) 2026 Gyumin Kang & AI Engineering Team
```
