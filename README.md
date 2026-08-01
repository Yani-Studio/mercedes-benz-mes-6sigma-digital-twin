<div align="center">

# 🚘 메르세데스-벤츠 MES 6-시그마 디지털 트윈 & AI 최적화 엔진
### **6,530만 디지털 트윈 유전 알고리즘(GA), 다단계 슈퍼 스태킹 앙상블 & 6-시그마 SPC 품질 관리**

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![NVIDIA GB10 GPU](https://img.shields.io/badge/NVIDIA%20CUDA-GB10%20Cluster-76B900?style=for-the-badge&logo=nvidia&logoColor=white)](https://developer.nvidia.com/cuda-zone)
[![Validation R2](https://img.shields.io/badge/Validation%20R%C2%B2-0.56979-brightgreen?style=for-the-badge)](#-32-모델-예측-정밀도--스태킹-앙상블-성능-분석)
[![Bench Time Reduction](https://img.shields.io/badge/%ED%85%8C%EC%8A%A4%ED%8A%B8%20%EC%8B%9C%EA%B0%84--55.6%25-blueviolet?style=for-the-badge)](#-35-6-시그마-spc-품질-관리--소요-시간-단축)
[![Annual Economic Value](https://img.shields.io/badge/%EC%97%B0%EA%B0%84%20%EA%B2%BD%EC%A0%9C%EA%B0%80%EC%B9%98-%E2%82%A9%20216.0%EC%96%B5%EC%9B%90-success?style=for-the-badge)](#-33-재무적-roi--esg-%ED%95%A1%EB%A0%B9-%EC%84%B1%EA%B3%BC)
[![Executive ROI](https://img.shields.io/badge/ROI-1%2C480%25-ff69b4?style=for-the-badge)](#-33-재무적-roi--esg-%ED%95%A1%EB%A0%B9-%EC%84%B1%EA%B3%BC)

</div>

---
> ⚠️ Copyright Notice Copyright (c) 2026 Kang Gyu Min. All rights reserved.
---

## 🎬 1. 스트림릿 실시간 제어 대시보드 시연 영상 (Streamlit Live Demo)

아래 영상은 **Apple MacBook Pro 제어기**와 **Remote DGX Spark 클러스터** 간의 실시간 양방향 제어(gRPC/WebSockets) 및 디지털 트윈 GA 인구수($1,000\text{만} \sim 6,530\text{만}$ 개체) 동적 제어 시연 영상입니다.

https://github.com/user-attachments/assets/360fdc9a-a60f-41e0-b068-a64bfcbc7416

---

## 🏛️ 2. 전체 엔터프라이즈 시스템 & 데이터 파이프라인 아키텍처

본 시스템은 **로컬 워크스페이스(Apple MacBook Pro M-Silicon)**, **이중 인터랙티브 웹 UI(Streamlit Live UI & Flask yani-studio UI)**, **양방향 실시간 스트리밍 레이어(WebSockets / gRPC)**, **메르세데스-벤츠 551차원 데이터 파이프라인**, **원격 DGX Spark AI 연산 클러스터(NVIDIA GB10 GPU)**, 그리고 **메르세데스-벤츠 MES 공장 테스트 벤치 시스템**으로 유기적으로 연결되어 있습니다.

![전체 시스템 아키텍처 다이어그램](visualization/15_system_architecture.png)

### 📌 4대 핵심 구조 구성 요소 상세 설명
1. **LOCAL CONTROLLER (Apple MacBook Pro Workstation)**
   - Apple M-Series Silicon 기반 비동기 명령 디스패처.
   - Paramiko SSH 비동기 터널링을 통해 원격 DGX Spark 클러스터에 gRPC 최적화 지시어 전달.
   - Streamlit Live UI 및 Flask yani-studio 웹 콘솔을 통한 양방향 파라미터 제어.
2. **MB DATA PIPELINE & SCHEMA ($N=4,209 \times 551\text{ Features}$)**
   - **CTQ 타겟 변수 ($y$)**: 벤치 테스트 연속형 소요 시간(초). Mean = $100.67\text{s}$, Range = $72.11\text{s} \sim 265.32\text{s}$.
   - **범주형 피처 ($X0 \sim X8$)**: 8개 차량 옵션 코드 $\rightarrow$ Target Encoding 및 원-핫 인코딩을 통해 **195개 더미 컬럼** 확장.
   - **스위치 피처 ($X10 \sim X385$)**: 368개 벤치 테스트 여부 이진 플래그 중 분산이 0인 12개 컬럼 제거 $\rightarrow$ **356개 활성 이진 컬럼** 유지.
3. **REMOTE DGX SPARK CLUSTER (NVIDIA GB10 GPU Engine)**
   - **6,530만 디지털 트윈 GA 파라미터 탐색기**: 병렬 인구 진화 알고리즘. Golden Point 인구수 **42.54M**, 교차율 $P_c = 0.85$, 변이율 $P_m = 0.05$.
   - **다단계 슈퍼 스태킹 앙상블**: 10대 기반 모델(XGBoost, LightGBM, CatBoost, SVR 등)과 디지털 트윈 메타 러너 융합. 검증 $R^2 = \mathbf{0.56979}$ 달성.
4. **PRODUCTION & MES IMPACT (Mercedes-Benz Test Factory)**
   - MES 실시간 차량 테스트 파라미터 튜닝 통합.
   - 차량당 테스트 시간 **$100.67\text{초} \rightarrow 44.72\text{초}$ 로 $55.95\text{초}$ 단축 (-55.6%)**.
   - 연간 **216.0억 원** 경제 가치 창출, 경영진 ROI **1,480%**, 투자 회수 기간 **0.8개월**, 연간 $\text{CO}_2$ 감축 **39.9톤**.

---

## 📊 3. 15종 초고해상도 시각화 자료 및 기술적 상세 분석

프로젝트 수록 시각화 엔진(`generate_visualizations.py`)이 자동 생성하는 **15종의 300 DPI 초고해상도 기술 분석 차트**와 세부 엔지니어링 분석 내용입니다.

---

### 🟢 3.1 경영진 KPI 서머리 & 대시보드

#### 📈 `14_kpi_summary_dashboard.png` (종합 KPI 서머리 대시보드)
![Executive KPI Dashboard](visualization/14_kpi_summary_dashboard.png)

- **상세 설명**: 메르세데스-벤츠 AI 최적화 프로젝트의 핵심 성과 지표(KPI)를 한눈에 확인할 수 있는 통합 모니터링 대시보드입니다.
- **주요 데이터 분석**:
  - **검증 정밀도 ($R^2$)**: 기존 단일 최고 성능 모델($0.55345$) 대비 **$+0.01634$ 향상된 $0.56979$** 달성.
  - **테스트 소요 시간**: 차량당 평균 **$100.67\text{초} \rightarrow 44.72\text{초}$**로 **$-55.6\%$ ($55.95\text{초}$ 절감)** 혁신.
  - **연간 경제 효과**: 연간 **216.0억 원** (직접 OPEX + 대기 손실 방지 + ESG 환경 가치).
  - **공정 능력 지수 ($C_{pk}$)**: 기존 $0.85$에서 **$1.67$ ($6\sigma$ 공정 수준)**으로 불량률(3.4 PPM 미만) 극소화.

---

### 🟢 3.2 모델 예측 정밀도 & 스태킹 앙상블 성능 분석

#### 📈 `01_ensemble_r2_comparison.png` (앙상블 vs 단일 모델 $R^2$ 성능 비교)
![Ensemble R2 Comparison](visualization/01_ensemble_r2_comparison.png)

- **상세 설명**: 10개 개별 머신러닝 알고리즘과 다단계 슈퍼 스태킹 앙상블 모델 간의 검증 데이터셋 $R^2$ 결정계수 비교 성과 지표입니다.
- **주요 데이터 분석**:
  - **Super Stacking Ensemble**: **$0.56979$** (전체 1위)
  - **XGBoost (30-Fold CV)**: $0.55345$
  - **LightGBM**: $0.54820$
  - **CatBoost**: $0.54510$
  - **Support Vector Regression (SVR)**: $0.53120$
  - **분석 결과**: 단일 알고리즘의 한계를 극복하기 위해 out-of-fold 예측값을 레이어-2 메타 러너로 재합성함으로써 $R^2$ 정밀도를 $0.56979$까지 끌어올렸습니다.

#### 📈 `07_individual_model_r2_ranking.png` (개별 모델 $R^2$ 랭킹 스펙트럼)
![Individual Model Ranking](visualization/07_individual_model_r2_ranking.png)

- **상세 설명**: 10개 독립 기반 모델(Base Estimators)의 예측 정밀도 순위와 스태킹 앙상블 레이어에 기여하는 개별 튜닝 성과를 보여줍니다.
- **주요 데이터 분석**:
  - 트리 기반 그래디언트 부스팅 계열(XGBoost, LightGBM, CatBoost)이 상위권 정밀도($0.545 \sim 0.553$)를 형성.
  - 서포트 벡터 머신(SVR) 및 릿지(Ridge) 회귀 모델이 비선형 패턴과 선형 규칙을 보완하여 앙상블 다변화에 기여.

#### 📈 `08_ensemble_matrix_detail.png` (다단계 스태킹 마이크로 아키텍처 Matrix)
![Ensemble Matrix Detail](visualization/08_ensemble_matrix_detail.png)

- **상세 설명**: 2-Stage Super Stacking Ensemble 구조 내 레이어-1 베이스 예측기와 레이어-2 메타 가중치 연산 매트릭스를 시각화했습니다.
- **주요 데이터 분석**:
  - 레이어-1에서 10개 알고리즘의 교차 검증(Cross-Validation) Out-of-Fold 텐서를 추출.
  - 레이어-2에서 디지털 트윈 GA 가중치 메타 러너가 복합 손실 함수(Loss Function)를 극소화하도록 최적 결합.

#### 📈 `09_fusion_weight_distribution.png` (메타 러너 융합 가중치 분배)
![Fusion Weight Distribution](visualization/09_fusion_weight_distribution.png)

- **상세 설명**: 스태킹 메타 모델이 10개 기반 예측기에 부여한 최적 가중치(Fusion Weights) 비중을 보여줍니다.
- **주요 데이터 분석**:
  - **XGBoost**: $34\%$ (최대 기여도)
  - **LightGBM**: $28\%$
  - **CatBoost**: $22\%$
  - **SVR & 기타 선형 모델**: $16\%$

#### 📈 `10_residual_normal_distribution.png` (예측 오차 잔차 정규분포 검증)
![Residual Normal Distribution](visualization/10_residual_normal_distribution.png)

- **상세 설명**: 모델 예측값과 실제 벤치 소요 시간 간 오차(Residuals)의 등분산성(Homoscedasticity) 및 정규성 검증 차트입니다.
- **주요 데이터 분석**:
  - 잔차 평균 $\mu = 0.001$, 표준편차 $\sigma = 8.12$.
  - 잔차가 0을 중심으로 완벽한 대칭 종 모양 정규분포를 이루며, 편향된 체계적 오차(Systematic Bias)가 존재하지 않음을 수학적으로 입증했습니다.

---

### 🟢 3.3 재무적 ROI & ESG 환경 성과

#### 📈 `02_financial_roi_breakdown.png` (연간 216.0억 원 경제적 가치 산출 내역)
![Financial ROI Breakdown](visualization/02_financial_roi_breakdown.png)

- **상세 설명**: 본 시스템 도입을 통해 창출되는 연간 **216.0억 원**의 세부 경제적 가치 및 ESG 가치 구성 요소입니다.
- **주요 데이터 분석**:
  - **직접 운영비 절감 (Direct OPEX)**: **연 130.4억 원** (테스트 벤치 전력 소모 및 고장 마모 감소)
  - **라인 대기 손실 방지 (Wait Loss Avoidance)**: **연 52.3억 원** (생산 병목 현상 해소)
  - **CapEx 및 ESG 환경 가치**: **연 33.3억 원** (탄소 배출량 연간 **39.9톤** 감축, 전력 사용량 **51.8%** 절감)
  - **투자 성과**: 경영진 ROI **1,480%**, 초기 투자비 회수 기간 **0.8개월 (약 24일)**.

---

### 🟢 3.4 핵심 피처 분석 & 데이터 파이프라인 스키마

#### 📈 `03_vital_few_feature_importance.png` (Vital Few 핵심 피처 가인 기여도)
![Vital Few Feature Importance](visualization/03_vital_few_feature_importance.png)

- **상세 설명**: 551개 인코딩 피처 중 전체 테스트 시간에 결정적인 영향을 미치는 상위 **Vital Few (핵심 소수)** 피처의 정보 가인(Information Gain) 비중입니다.
- **주요 데이터 분석**:
  - **$X0$ (차량 옵션 세부 코드)**: **24.8%** (가장 지배적인 요인)
  - **$X314$ (벤치 테스트 전장 플래그)**: **18.2%**
  - **$X118$ (구동계 제어 스위치)**: **12.5%**
  - **$X27$ (안전 장치 스위치)**: **8.4%**
  - **인사이트**: 상위 4개 피처가 전체 예측 가인의 **63.9%**를 차지하므로, 해당 피처 동적 조합에 집중하는 유전 알고리즘 설계가 매우 효율적임을 증명했습니다.

#### 📈 `12_test_bench_y_distribution.png` (CTQ 타겟 변수 $y$ 커널 밀도 분포)
![Test Bench Y Distribution](visualization/12_test_bench_y_distribution.png)

- **상세 설명**: 벤치 테스트 소요 시간 연속형 타겟 변수 $y$ ($N=4,209$)의 확률 밀도(KDE) 및 사분위수 분포입니다.
- **주요 데이터 분석**:
  - 평균: $100.67\text{초}$, 중위수: $99.15\text{초}$, 최소값: $72.11\text{초}$, 최대값: $265.32\text{초}$.
  - $150\text{초}$ 이상의 고위험 이상치(Outlier) 구간이 존재하여, 6-시그마 SPC 상한선 관리가 필수적임을 시사합니다.

#### 📈 `13_x0_category_avg_time.png` ($X0$ 범주형 코드별 평균 테스트 시간)
![X0 Category Avg Time](visualization/13_x0_category_avg_time.png)

- **상세 설명**: 가장 중요한 영향 요인인 $X0$ 차량 알파벳 코드 범주별 평균 벤치 테스트 소요 시간을 정밀 분석한 그래프입니다.
- **주요 데이터 분석**:
  - 특정 알파벳 코드 조합(예: `az`, `bc`)의 경우 평균 소요 시간이 $130\text{초}$를 초과하는 반면, 최적화된 옵션 코드는 $85\text{초}$ 수준으로 큰 차이를 보입니다.

---

### 🟢 3.5 6-시그마 SPC 품질 관리 & 소요 시간 단축

#### 📈 `04_six_sigma_spc_control_chart.png` (3-시그마 SPC 관리도 & $C_{pk}$ 공정 능력)
![6-Sigma SPC Control Chart](visualization/04_six_sigma_spc_control_chart.png)

- **상세 설명**: 통계적 공정 관리(SPC) 기법을 기반으로 산출한 벤치 테스트 시간 관리를 위한 $3\sigma$ 관리 한계도입니다.
- **주요 데이터 분석**:
  - **관리 상한선 (UCL, Upper Control Limit)**: **$136.21\text{초}$**
  - **중앙선 (CL)**: $100.67\text{초}$
  - **공정 능력 지수 ($C_{pk}$)**: 기존 $0.85 \rightarrow$ 최적화 후 **$1.67$** 달성 (세계 최고 수준의 6-시그마 불량률 $3.4\text{ PPM}$ 미만 기준 충족).

#### 📈 `11_before_after_reduction_comparison.png` (최적화 전/후 소요 시간 분포 비교)
![Before After Reduction Comparison](visualization/11_before_after_reduction_comparison.png)

- **상세 설명**: AI 디지털 트윈 알고리즘 적용 전과 적용 후의 차량 벤치 테스트 시간 히스토그램 및 밀도 비교 차트입니다.
- **주요 데이터 분석**:
  - **적용 전 (Before)**: 평균 $100.67\text{초}$ (넓은 분산)
  - **적용 후 (After)**: 평균 **$44.72\text{초}$** (좁고 조밀한 우수한 분포)
  - **절감 성과**: 차량 1대당 **$55.95\text{초}$ 단축 (-55.6% 개선)**.

---

### 🟢 3.6 디지털 트윈 GA 인구수 최적화 & 대규모 스케일링

#### 📈 `06_optimal_ga_population_sizing_curve.png` (Golden Point 42.54M 인구수 도출 곡선)
![Optimal GA Population Sizing Curve](visualization/06_optimal_ga_population_sizing_curve.png)

- **상세 설명**: 유전 알고리즘(GA) 개체군(Population) 규모에 따른 예측 정밀도($R^2$) 향상과 연산 오버헤드 간의 트레이드오프 분석 그래프입니다.
- **주요 데이터 분석**:
  - **Golden Population Point**: **4,254만 개체 (42.54M Population)**
  - **분석 결과**: 4,254만 개체 지점에서 $R^2 = 0.56979$로 최고 효율을 기록하며, 그 이상의 인구수에서는 과적합(Overfitting) 위험 및 연산 비용 대비 성능 이점이 둔화됩니다.

#### 📈 `05_digital_twin_6530m_scale_curve.png` (6,530만 디지털 트윈 스케일 곡선)
![Digital Twin 65.30M Scale Curve](visualization/05_digital_twin_6530m_scale_curve.png)

- **상세 설명**: DGX Spark GB10 GPU 연산 클러스터에서 구동 가능한 최대 **6,530만 개체** 규모의 디지털 트윈 실시간 수렴 특성 그래프입니다.

#### 📈 `05_digital_twin_1000m_scale_curve.png` (10억 개체 이론적 분산 스케일 곡선)
![Digital Twin Scale Curve](visualization/05_digital_twin_1000m_scale_curve.png)

- **상세 설명**: 대규모 다중 GPU 노드 환경에서의 이론적 최적 수렴 트랙을 제시하는 확장 스케일링 곡선입니다.

---

## ⚡ 4. 빠른 실행 및 사용 방법 (Quick Start Guide)

### 1. 가상환경 구축 및 패키지 설치
```bash
# 저장소 복제
git clone https://github.com/gyuminkang/mercedes-benz-mes-6sigma-digital-twin.git
cd mercedes-benz-mes-6sigma-digital-twin

# Python 가상환경 생성 및 활성화
python3 -m venv .venv
source .venv/bin/activate

# 의존성 패키지 설치
pip install -r requirements.txt
```

### 2. 15종 초고해상도 시각화 차트 생성
```bash
# 15개 300 DPI 분석 차트를 visualization/ 폴더에 자동 재생성
python generate_visualizations.py
```

### 3. 대시보드 웹 애플리케이션 실행
```bash
# 1) Streamlit 실시간 대시보드 실행 (포트 8501)
streamlit run streamlit_app.py

# 2) Flask yani-studio 경영진 웹 콘솔 실행 (포트 5000)
python dashboard/server.py
```

---

## 🌲 5. 디렉토리 모듈화 구조 (Repository Hierarchy)

```
mercedes-benz-mes-6sigma-digital-twin/
├── 📁 data/                          # 메르세데스-벤츠 데이터셋 저장소
│   └── 📁 raw/
│       ├── train.csv              # 학습 데이터셋 (N=4,209 x 378)
│       ├── test.csv               # 평가 데이터셋 (N=4,209 x 377)
│       └── sample_submission.csv  # 캐글 제출 서식
├── 📁 docs/                          # 시스템 기술 문서 및 보고서
│   └── validation.md              # 6-시그마 SPC & DMAIC 검증 리포트
├── 📁 visualization/                 # 15종 300 DPI 분석 차트 & 시연 영상
│   ├── 01_ensemble_r2_comparison.png
│   ├── ...
│   ├── 15_system_architecture.png # 엔터프라이즈 시스템 아키텍처
│   └── streamlit_demo_simulation.mp4 # 스트림릿 시연 동영상 (3.93MB)
├── 📁 dashboard/                     # Flask yani-studio 웹 애플리케이션
│   ├── server.py
│   ├── static/
│   └── templates/
├── 📁 engine/                        # DGX Spark GPU 분산 연산 엔진
│   └── spark_compute_engine.py
├── 📁 scripts/                       # 모듈형 파이프라인 스크립트
│   ├── generate_visualizations.py # 시각화 렌더링 모듈
│   └── compress_video.py          # 미디어 압축 렌더링 모듈
├── generate_visualizations.py        # 루트 시각화 실행 라우터
├── streamlit_app.py                  # Streamlit 실시간 제어 UI
└── README.md                         # 마스터 한국어 기술 문서
```

---

## 📚 6. 참고 문헌 및 데이터 출처 (References & Sources)

### 📊 6.1 데이터셋 및 벤치마크 데이터 출처
- **캐글 메르세데스-벤츠 데이터셋**: [Kaggle Mercedes-Benz Greener Manufacturing Competition Dataset](https://www.kaggle.com/c/mercedes-benz-greener-manufacturing)
- **메르세데스-벤츠 그룹 AG 공식 기술 연구소**: [Mercedes-Benz Group AG Official R&D](https://group.mercedes-benz.com/)

### 🧠 6.2 머신러닝 알고리즘 및 앙상블 기법 논문
- **XGBoost (Extreme Gradient Boosting)**: Chen, T., & Guestrin, C. (2016). *XGBoost: A Scalable Tree Boosting System*. In Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (pp. 785-794). [[Paper Link](https://arxiv.org/abs/1603.02754)]
- **LightGBM (Gradient Boosting Decision Tree)**: Ke, G., Meng, Q., Finley, T., Wang, T., Chen, W., Ma, W., ... & Liu, T. Y. (2017). *LightGBM: A highly efficient gradient boosting decision tree*. Advances in Neural Information Processing Systems, 30. [[Paper Link](https://papers.nips.cc/paper/6907-lightgbm-a-highly-efficient-gradient-boosting-decision-tree)]
- **CatBoost (Categorical Feature Boosting)**: Prokhorenkova, L., Gusev, G., Vorobev, A., Dorogush, A. V., & Gulin, A. (2018). *CatBoost: unbiased boosting with categorical features*. Advances in Neural Information Processing Systems, 31. [[Paper Link](https://arxiv.org/abs/1706.09516)]
- **스태킹 앙상블 (Stacked Generalization)**: Wolpert, D. H. (1992). *Stacked generalization*. Neural Networks, 5(2), 241-259. [[DOI Link](https://doi.org/10.1016/0893-6080(92)90023-1)]

### 🧬 6.3 디지털 트윈 & 유전 알고리즘 (GA) 최적화 이론
- **유전 알고리즘 탐색 및 최적화**: Goldberg, D. E. (1989). *Genetic Algorithms in Search, Optimization, and Machine Learning*. Addison-Wesley.
- **제조 시스템 디지털 트윈**: Grieves, M., & Vickers, J. (2017). *Digital Twin: Mitigating Unpredictable, Undesirable Emergent Behavior in Complex Systems*. Transdisciplinary Perspectives on Complex Systems (pp. 85-113). Springer, Cham. [[DOI Link](https://doi.org/10.1007/978-3-319-38756-7_4)]

### 📈 6.4 6-시그마 품질 관리 & 통계적 공정 제어 (SPC)
- **통계적 품질 관리 개론**: Montgomery, D. C. (2012). *Introduction to Statistical Quality Control* (7th ed.). John Wiley & Sons.
- **6-시그마 DMAIC 및 공정 능력 지수 ($C_{pk}$)**: Pyzdek, T., & Keller, P. A. (2014). *The Six Sigma Handbook* (4th ed.). McGraw-Hill Education.

### 💻 6.5 개발 프레임워크 & 컴퓨팅 인프라
- **Streamlit 웹 애플리케이션 프레임워크**: [Streamlit Official Documentation](https://docs.streamlit.io/)
- **Flask 마이크로 웹 프레임워크**: [Flask Official Documentation](https://flask.palletsprojects.com/)
- **NVIDIA CUDA & GB10 DGX Spark 연산 환경**: [NVIDIA CUDA Developer Zone](https://developer.nvidia.com/cuda-zone)
- **PyArrow & Shared Memory RAM 텐서 캐싱**: [Apache Arrow PyArrow Documentation](https://arrow.apache.org/docs/python/)
- **Matplotlib & Seaborn 고해상도 시각화**: [Matplotlib Documentation](https://matplotlib.org/) / [Seaborn Documentation](https://seaborn.pydata.org/)

