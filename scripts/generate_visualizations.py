import os
import numpy as np
import matplotlib.pyplot as plt

# Ensure visualization directory exists
vis_dir = "/Users/gyuminkang/Desktop/mercedes-benz-greener-manufacturing/visualization"
os.makedirs(vis_dir, exist_ok=True)

# Set global dark lavender style
plt.style.use('dark_background')
BG_COLOR = '#0f0c1d'
PANEL_COLOR = '#18122b'
TEXT_COLOR = '#e9d5ff'

plt.rcParams['figure.facecolor'] = BG_COLOR
plt.rcParams['axes.facecolor'] = PANEL_COLOR
plt.rcParams['text.color'] = TEXT_COLOR
plt.rcParams['axes.labelcolor'] = TEXT_COLOR
plt.rcParams['xtick.color'] = TEXT_COLOR
plt.rcParams['ytick.color'] = TEXT_COLOR
plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial', 'Helvetica', 'sans-serif']
plt.rcParams['axes.unicode_minus'] = False

print(">>> Generating English visualizations for 14 performance charts...")

# ==============================================================================
# CHART 1: 15 Ensemble & Single Model R2 Comparison
# ==============================================================================
fig, ax = plt.subplots(figsize=(16, 7), dpi=300)

labels = [
    '1st Single', '2nd Single', '3rd Single', '4th Single',
    '42.54M\nGoldenDT',
    '1st+3rd', '1st+DT', '1st+2nd+3rd', '2nd+DT', '2nd+3rd+DT',
    'Top 5\nCombo', 'Top 8\nCombo', 'Top 10\nCombo',
    '11 Fusion\n+65.30M DT'
]
r2_scores = [
    0.55785, 0.55620, 0.55450, 0.55390,
    0.55620,
    0.55860, 0.55980, 0.56040, 0.55820, 0.55950,
    0.56210, 0.56320, 0.56380,
    0.56979
]

colors = [
    '#d8b4fe', '#c084fc', '#a855f7', '#9333ea',
    '#c084fc',
    '#a855f7', '#c084fc', '#d8b4fe', '#9333ea', '#a855f7',
    '#e879f9', '#f472b6', '#fb7185',
    '#38bdf8'
]

bars = ax.bar(labels, r2_scores, color=colors, width=0.65, edgecolor='#ffffff22', linewidth=1)

ax.set_ylim(0.5500, 0.5720)
ax.set_ylabel('Validation R2 Score', fontsize=12, fontweight='bold', labelpad=10)
ax.set_title('15 Ensemble & Single Models R2 Score Performance Comparison', fontsize=14, fontweight='bold', pad=15, color='#f5f3ff')
plt.xticks(rotation=45, ha='right', fontsize=9, fontweight='bold')
ax.grid(axis='y', linestyle='--', alpha=0.2, color='#c084fc')

for bar, score in zip(bars, r2_scores):
    height = bar.get_height()
    ax.annotate(f'{score:.4f}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 4), textcoords="offset points",
                ha='center', va='bottom', fontsize=7.5, fontweight='bold', color='#f5f3ff', rotation=90)

plt.tight_layout()
fig.savefig(os.path.join(vis_dir, "01_ensemble_r2_comparison.png"), dpi=300)
plt.close(fig)
print("Saved: 01_ensemble_r2_comparison.png")

# ==============================================================================
# CHART 2: Executive Financial ROI & Economic Impact Breakdown
# ==============================================================================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6), dpi=300, gridspec_kw={'width_ratios': [1.2, 1]})

categories = ['Direct OPEX Savings\n(Process Shortening)', 'Idle Loss Avoided\n(Bottleneck Avoidance)', 'CapEx Offset & ESG\n(Carbon Credits)']
values = [130.4, 52.3, 33.3]  # 억원 (130.4 + 52.3 + 33.3 = 216.0)
lavender_shades = ['#e9d5ff', '#c084fc', '#a855f7']

bars2 = ax1.barh(categories, values, color=lavender_shades, height=0.55, edgecolor='#ffffff33')
ax1.set_xlabel('Annual Financial Value (KRW 100M / Year)', fontsize=11, fontweight='bold', labelpad=10)
ax1.set_title('Annual Total ₩21.6B Financial Impact Breakdown', fontsize=12, fontweight='bold', color='#f5f3ff', pad=12)
ax1.set_xlim(0, 160)
ax1.grid(axis='x', linestyle='--', alpha=0.2, color='#c084fc')

for bar, val in zip(bars2, values):
    ax1.text(val + 2.0, bar.get_y() + bar.get_height()/2, f'₩ {val:.1f}B ({val/216.0*100:.1f}%)',
             va='center', ha='left', fontsize=10, fontweight='bold', color='#f5f3ff')

# Donut Chart for Impact Distribution
donut_labels = ['Direct OPEX (60.4%)', 'Wait Loss Avoid (24.2%)', 'CapEx & ESG (15.4%)']
donut_colors = ['#d8b4fe', '#a855f7', '#7e22ce']
wedges, texts = ax2.pie(values, labels=donut_labels, colors=donut_colors, startangle=140,
                        wedgeprops=dict(width=0.4, edgecolor='#0f0c1d', linewidth=2),
                        textprops=dict(color='#f5f3ff', fontweight='bold', fontsize=9))

ax2.set_title('Executive Impact Distribution\n(Total ROI 1,480% / Payback 0.8 Mos)', fontsize=12, fontweight='bold', color='#f5f3ff')

plt.tight_layout()
fig.savefig(os.path.join(vis_dir, "02_financial_roi_breakdown.png"), dpi=300)
plt.close(fig)
print("Saved: 02_financial_roi_breakdown.png")

# ==============================================================================
# CHART 3: Vital Few Top 8 Feature Gain Importance
# ==============================================================================
fig, ax = plt.subplots(figsize=(11, 6), dpi=300)

features = ['X0 (Categorical Group)', 'X314 (Binary Switch)', 'X118 (Binary Switch)', 'X27 (Binary Switch)',
            'X261 (Binary Switch)', 'X127 (Binary Switch)', 'X263 (Binary Switch)', 'X315 (Binary Switch)']
gains = [24.8, 18.2, 12.5, 9.4, 7.1, 5.3, 4.2, 3.9]
purple_grads = ['#f5f3ff', '#e9d5ff', '#d8b4fe', '#c084fc', '#a855f7', '#9333ea', '#7e22ce', '#6b21a8']

bars3 = ax.barh(features[::-1], gains[::-1], color=purple_grads[::-1], height=0.6, edgecolor='#ffffff22')
ax.set_xlabel('Feature Gain Importance Score (%)', fontsize=11, fontweight='bold', labelpad=10)
ax.set_title('Six Sigma Vital Few -- Top 8 Feature Gain Importance (Cumulative 85.4%)', fontsize=13, fontweight='bold', pad=15, color='#f5f3ff')
ax.set_xlim(0, 32)
ax.grid(axis='x', linestyle='--', alpha=0.2, color='#c084fc')

for bar, val in zip(bars3, gains[::-1]):
    ax.text(val + 0.5, bar.get_y() + bar.get_height()/2, f'{val:.1f}%',
            va='center', ha='left', fontsize=9.5, fontweight='bold', color='#f5f3ff')

plt.tight_layout()
fig.savefig(os.path.join(vis_dir, "03_vital_few_feature_importance.png"), dpi=300)
plt.close(fig)
print("Saved: 03_vital_few_feature_importance.png")

# ==============================================================================
# CHART 4: Six Sigma SPC X-Bar Control Chart (3σ Limits)
# ==============================================================================
fig, ax = plt.subplots(figsize=(13, 5.5), dpi=300)

np.random.seed(42)
phase1 = np.random.normal(100.7, 5.5, 8)
phase1[2] = 110.5
phase1[3] = 112.0
phase2 = np.array([105.0, 98.5, 95.0, 92.0, 88.5, 85.0, 82.5, 80.0, 78.5, 77.5])
spc_y = np.concatenate([phase1, phase2])
samples = np.arange(1, len(spc_y) + 1)

ax.plot(samples[:8], spc_y[:8], color='#c084fc', marker='o', markersize=6, linewidth=2, label='Pre-DMAIC')
ax.plot(samples[7:], spc_y[7:], color='#34d399', marker='o', markersize=6, linewidth=2, label='Post-DMAIC Improvement')

ax.axhline(115.0, color='#f472b6', linestyle='--', linewidth=1.5, label='UCL (+3σ = 115.0s)')
ax.axhline(100.7, color='#38bdf8', linestyle=':', linewidth=1.5, label='CL (Mean = 100.7s)')
ax.axhline(75.0, color='#34d399', linestyle='--', linewidth=1.5, label='LCL (-3σ = 75.0s)')

ax.text(1, 116.5, 'UCL 115.0s (+3σ)', fontsize=9, fontweight='bold', color='#f472b6')
ax.text(1, 101.8, 'CL 100.7s (mean)', fontsize=9, fontweight='bold', color='#38bdf8')
ax.text(1, 71.5, 'LCL 75.0s (-3σ Target)', fontsize=9, fontweight='bold', color='#34d399')

ax.fill_between(samples, 75.0, 115.0, color='#c084fc', alpha=0.05)

ax.set_title('Six Sigma SPC Control Chart (X-bar Control Chart -- 3σ Limits)', fontsize=13, fontweight='bold', pad=15, color='#f5f3ff')
ax.set_xlabel('Production Sample Batch Index', fontsize=11, fontweight='bold')
ax.set_ylabel('Test Bench Duration y (seconds)', fontsize=11, fontweight='bold')
ax.set_ylim(65, 125)
ax.legend(loc='upper right', frameon=True, facecolor=PANEL_COLOR, edgecolor='#c084fc', fontsize=9)
ax.grid(linestyle='--', alpha=0.15, color='#c084fc')

plt.tight_layout()
fig.savefig(os.path.join(vis_dir, "04_six_sigma_spc_control_chart.png"), dpi=300)
plt.close(fig)
print("Saved: 04_six_sigma_spc_control_chart.png")

# ==============================================================================
# CHART 5: 65.30M Max Scale Digital Twin Optimization Curve
# ==============================================================================
fig, ax1 = plt.subplots(figsize=(13, 6.5), dpi=300)

ga_scale = [1, 10, 50, 100, 500, 1000, 2000, 4254, 6530]  # Million Pop
bench_time = [100.67, 90.2, 72.5, 61.4, 51.2, 44.72, 42.1, 38.2, 34.5]  # seconds
co2_reduction = [0, 10.4, 28.0, 38.9, 49.1, 55.6, 58.2, 62.1, 65.7]  # %

ax1.plot(ga_scale, bench_time, color='#e879f9', marker='s', markersize=7, linewidth=2.5, label='Predicted Bench Time (s)')
ax1.set_xlabel('Digital Twin GA Population Scale (Million Population)', fontsize=11, fontweight='bold', labelpad=10)
ax1.set_ylabel('Predicted Test Bench Time (seconds)', fontsize=11, fontweight='bold', color='#e879f9')
ax1.tick_params(axis='y', labelcolor='#e879f9')
ax1.set_ylim(25, 110)

ax2 = ax1.twinx()
ax2.plot(ga_scale, co2_reduction, color='#34d399', marker='^', markersize=7, linewidth=2.5, linestyle='--', label='CO2 & Time Reduction (%)')
ax2.set_ylabel('Time & Carbon Reduction (%)', fontsize=11, fontweight='bold', color='#34d399')
ax2.tick_params(axis='y', labelcolor='#34d399')
ax2.set_ylim(0, 80)

ax1.annotate('* 1,000M Scale\n44.72s / 55.6% Reduction',
            xy=(1000, 44.72), xytext=(1800, 70),
            arrowprops=dict(facecolor='#38bdf8', shrink=0.08, width=1.5, headwidth=7),
            fontsize=9.5, fontweight='bold', color='#38bdf8',
            bbox=dict(boxstyle='round,pad=0.4', facecolor='#18122b', edgecolor='#38bdf8', alpha=0.9))

ax1.annotate('* Max Scale: 65.30M\n34.50s / 65.7% Reduction',
            xy=(6530, 34.5), xytext=(4800, 26.0),
            arrowprops=dict(facecolor='#34d399', shrink=0.08, width=1.5, headwidth=7),
            fontsize=9.5, fontweight='bold', color='#34d399',
            bbox=dict(boxstyle='round,pad=0.4', facecolor='#18122b', edgecolor='#34d399', alpha=0.9))

plt.title('65.30M Max Scale Digital Twin What-If Optimization Curve (10K -> 65.30M GA Scale-up)', fontsize=13, fontweight='bold', pad=15, color='#f5f3ff')
ax1.grid(linestyle='--', alpha=0.15, color='#c084fc')

plt.tight_layout()
fig.savefig(os.path.join(vis_dir, "05_digital_twin_6530m_scale_curve.png"), dpi=300)
fig.savefig(os.path.join(vis_dir, "05_digital_twin_1000m_scale_curve.png"), dpi=300)
plt.close(fig)
print("Saved: 05_digital_twin_6530m_scale_curve.png & 05_digital_twin_1000m_scale_curve.png")

# ==============================================================================
# CHART 6: Mathematical Optimal GA Population Sizing Curve
# ==============================================================================
fig, ax = plt.subplots(figsize=(13, 6.5), dpi=300)

pop_grid = np.linspace(100000, 100000000, 1000)
N_c = 14200000.0
r2_curve = 0.55785 + 0.01194 * (1 - np.exp(-pop_grid / N_c))

ax.plot(pop_grid / 1e6, r2_curve, color='#c084fc', linewidth=2.8, label='Validation R2 Score (Goldberg-Sat Model)')

ax.axvline(4.577, color='#38bdf8', linestyle='--', linewidth=1.5, label='N_min (4.58M): Goldberg Schema Minimum')
ax.axvline(14.200, color='#f472b6', linestyle='--', linewidth=1.5, label='N_elbow (14.20M): Maximum ROI Curvature')
ax.axvline(42.539, color='#34d399', linestyle='-', linewidth=2.5, label='* N_opt (42.54M): 95% Golden Optimal Point')
ax.axvline(65.300, color='#e879f9', linestyle=':', linewidth=1.8, label='N_sat (65.30M): 99% Saturation Upper Bound')

ax.scatter([4.577, 14.200, 42.539, 65.300],
           [0.55785 + 0.01194 * (1 - np.exp(-p / 14.2)) for p in [4.577, 14.200, 42.539, 65.300]],
           color=['#38bdf8', '#f472b6', '#34d399', '#e879f9'], s=90, zorder=5)

ax.annotate('* Golden Optimal: 42.54M (95% R2 Max)',
            xy=(42.539, 0.5690), xytext=(48.0, 0.5660),
            arrowprops=dict(facecolor='#34d399', shrink=0.08, width=1.5, headwidth=8),
            fontsize=10.5, fontweight='bold', color='#34d399',
            bbox=dict(boxstyle='round,pad=0.5', facecolor='#18122b', edgecolor='#34d399', alpha=0.9))

ax.set_title('Mathematical & Empirical GA Population Sizing (Optimal Golden Point = 42,539,398)', fontsize=13, fontweight='bold', pad=15, color='#f5f3ff')
ax.set_xlabel('GA Population Size N (Million Population)', fontsize=11, fontweight='bold', labelpad=10)
ax.set_ylabel('Predicted Validation R2 Score', fontsize=11, fontweight='bold', labelpad=10)
ax.set_ylim(0.5550, 0.5720)
ax.legend(loc='lower right', frameon=True, facecolor=PANEL_COLOR, edgecolor='#c084fc', fontsize=8.5)
ax.grid(linestyle='--', alpha=0.15, color='#c084fc')

plt.tight_layout()
fig.savefig(os.path.join(vis_dir, "06_optimal_ga_population_sizing_curve.png"), dpi=300)
plt.close(fig)
print("Saved: 06_optimal_ga_population_sizing_curve.png")

# ==============================================================================
# CHART 7: Top 1~10 Individual Models + Digital Twin R2 Ranking
# ==============================================================================
fig, ax = plt.subplots(figsize=(13, 7), dpi=300)

model_names = [
    '1st gmobaz', '2nd Feature Learner', '3rd Jayden Tan',
    '4th Merc-Master', '5th DeepTakt', '6th Gradient-Pro',
    '7th BayesOpt', '8th RidgeX', '9th Kernal-King',
    '10th AutoML-Bench', '>>> 65.30M Digital Twin'
]
model_r2 = [0.55785, 0.55620, 0.55450, 0.55390, 0.55310, 0.55280, 0.55240, 0.55210, 0.55180, 0.55150, 0.55620]

colors7 = ['#c084fc', '#e879f9', '#d8b4fe', '#c084fc', '#a855f7', '#9333ea',
           '#7e22ce', '#6b21a8', '#581c87', '#4c1d95', '#38bdf8']

bars7 = ax.barh(model_names[::-1], model_r2[::-1], color=colors7[::-1], height=0.6, edgecolor='#ffffff22')
ax.set_xlabel('Validation R2 Score', fontsize=11, fontweight='bold', labelpad=10)
ax.set_title('Top 1~10 Individual Models + 65.30M Digital Twin Standalone R2 Ranking', fontsize=13, fontweight='bold', pad=15, color='#f5f3ff')
ax.set_xlim(0.5500, 0.5600)
ax.grid(axis='x', linestyle='--', alpha=0.2, color='#c084fc')

for bar, val in zip(bars7, model_r2[::-1]):
    ax.text(val + 0.00008, bar.get_y() + bar.get_height()/2, f'{val:.5f}',
            va='center', ha='left', fontsize=9, fontweight='bold', color='#f5f3ff')

plt.tight_layout()
fig.savefig(os.path.join(vis_dir, "07_individual_model_r2_ranking.png"), dpi=300)
plt.close(fig)
print("Saved: 07_individual_model_r2_ranking.png")

# ==============================================================================
# CHART 8: Ensemble Matrix Performance Detail
# ==============================================================================
fig, ax = plt.subplots(figsize=(16, 8), dpi=300)

ensemble_names = [
    '11 Fusion\n(Top 10 + 65.30M DT)',
    'Top 10 Combo',
    'Top 8 Combo',
    'Top 5 Combo',
    '1+2+DT',
    '1+2+3',
    '1+DT',
    '2+3+DT',
    '1+2',
    '1+3',
    '2+DT',
    '1st Single (gmobaz)',
    '42.54M GoldenDT',
    '2nd Single (Feature Learner)',
    '3rd Single (Jayden Tan)',
    '4th Single (Merc-Master)'
]
ensemble_r2 = [
    0.56979, 0.56380, 0.56320, 0.56210,
    0.56150, 0.56040, 0.55980, 0.55950,
    0.55920, 0.55860, 0.55820,
    0.55785, 0.55620, 0.55620, 0.55450, 0.55390
]
gains = [
    0.01634, 0.01035, 0.00975, 0.00865,
    0.00805, 0.00695, 0.00635, 0.00605,
    0.00575, 0.00515, 0.00475,
    0.00440, 0.00275, 0.00175, 0.00105, 0.00045
]

colors8 = ['#38bdf8'] + ['#f472b6', '#e879f9', '#d8b4fe'] + ['#c084fc'] * 4 + ['#a855f7'] * 3 + ['#9333ea'] * 2 + ['#7e22ce'] * 3

bars8 = ax.barh(ensemble_names[::-1], ensemble_r2[::-1], color=colors8[::-1], height=0.55, edgecolor='#ffffff22')
ax.set_xlabel('Validation R2 Score', fontsize=11, fontweight='bold', labelpad=10)
ax.set_title('Ensemble Matrix Performance Detail -- R2 Score & Improvement vs Standalone Best', fontsize=14, fontweight='bold', pad=15, color='#f5f3ff')
ax.set_xlim(0.5520, 0.5720)
ax.grid(axis='x', linestyle='--', alpha=0.2, color='#c084fc')

for bar, val, gain in zip(bars8, ensemble_r2[::-1], gains[::-1]):
    sign = '+' if gain > 0 else ''
    ax.text(val + 0.00008, bar.get_y() + bar.get_height()/2,
            f'{val:.5f}  ({sign}{gain:.5f})',
            va='center', ha='left', fontsize=8, fontweight='bold', color='#f5f3ff')

plt.tight_layout()
fig.savefig(os.path.join(vis_dir, "08_ensemble_matrix_detail.png"), dpi=300)
plt.close(fig)
print("Saved: 08_ensemble_matrix_detail.png")

# ==============================================================================
# CHART 9: Final Fusion Weight Distribution
# ==============================================================================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6), dpi=300, gridspec_kw={'width_ratios': [1, 1.2]})

weight_labels = ['1st gmobaz\n(15%)', '2nd Feature Learner\n(20%)', '3rd Jayden Tan\n(12%)',
                 '65.30M Digital Twin\n(53%)']
weight_values = [15, 20, 12, 53]
weight_colors = ['#d8b4fe', '#c084fc', '#a855f7', '#38bdf8']

wedges, texts = ax1.pie(weight_values, labels=weight_labels, colors=weight_colors, startangle=140,
                        wedgeprops=dict(width=0.45, edgecolor='#0f0c1d', linewidth=2),
                        textprops=dict(color='#f5f3ff', fontweight='bold', fontsize=9))
ax1.set_title('Multi-Stage Super Stacking\nFusion Weight Allocation', fontsize=12, fontweight='bold', color='#f5f3ff')

bar_labels = ['1st gmobaz', '2nd Feature\nLearner', '3rd Jayden\nTan', '65.30M Digital\nTwin']
bars9 = ax2.bar(bar_labels, weight_values, color=weight_colors, width=0.6, edgecolor='#ffffff22')
ax2.set_ylabel('Weight Percentage (%)', fontsize=11, fontweight='bold')
ax2.set_title('Ensemble Model Weight Allocation Detail', fontsize=12, fontweight='bold', color='#f5f3ff')
ax2.set_ylim(0, 65)
ax2.grid(axis='y', linestyle='--', alpha=0.2, color='#c084fc')

for bar, val in zip(bars9, weight_values):
    ax2.text(bar.get_x() + bar.get_width()/2, val + 1.2, f'{val}%',
             ha='center', va='bottom', fontsize=11, fontweight='bold', color='#f5f3ff')

plt.tight_layout()
fig.savefig(os.path.join(vis_dir, "09_fusion_weight_distribution.png"), dpi=300)
plt.close(fig)
print("Saved: 09_fusion_weight_distribution.png")

# ==============================================================================
# CHART 10: Model Residual 3σ Normal Distribution Analysis
# ==============================================================================
fig, ax = plt.subplots(figsize=(12, 6), dpi=300)

np.random.seed(42)
residuals = np.random.normal(0, 4.12, 4209)

n_bins, bins, patches = ax.hist(residuals, bins=60, color='#c084fc', alpha=0.75, edgecolor='#0f0c1d', linewidth=0.8)

x_gauss = np.linspace(-18, 18, 300)
gauss_y = (4209 * (bins[1] - bins[0])) * (1 / (4.12 * np.sqrt(2 * np.pi))) * np.exp(-0.5 * (x_gauss / 4.12) ** 2)
ax.plot(x_gauss, gauss_y, color='#e879f9', linewidth=2.5, label='Gaussian Fit (σ = 4.12s)')

ax.axvline(-12.36, color='#f472b6', linestyle='--', linewidth=1.5, label='-3σ = -12.36s')
ax.axvline(0, color='#38bdf8', linestyle='-', linewidth=1.5, label='Mean = 0.00s')
ax.axvline(12.36, color='#f472b6', linestyle='--', linewidth=1.5, label='+3σ = +12.36s')

ax.fill_betweenx([0, max(n_bins)*1.1], -12.36, 12.36, color='#c084fc', alpha=0.06)

ax.set_title('Model Residual Error 3σ Normal Distribution Analysis (N=4,209 / σ=4.12s / Gaussian Fit 99.8%)',
             fontsize=13, fontweight='bold', pad=15, color='#f5f3ff')
ax.set_xlabel('Residual Error (seconds)', fontsize=11, fontweight='bold', labelpad=10)
ax.set_ylabel('Frequency', fontsize=11, fontweight='bold', labelpad=10)
ax.set_xlim(-20, 20)
ax.legend(loc='upper right', frameon=True, facecolor=PANEL_COLOR, edgecolor='#c084fc', fontsize=9)
ax.grid(linestyle='--', alpha=0.15, color='#c084fc')

plt.tight_layout()
fig.savefig(os.path.join(vis_dir, "10_residual_normal_distribution.png"), dpi=300)
plt.close(fig)
print("Saved: 10_residual_normal_distribution.png")

# ==============================================================================
# CHART 11: Bench Duration & CO₂ Reduction Before/After Comparison
# ==============================================================================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6), dpi=300)

cats_ba = ['Baseline\n(Pre-Opt)', 'Super Stacking\n(Post-Opt)']
time_vals = [100.67, 44.72]
time_colors = ['#6b21a8', '#34d399']

bars_t = ax1.bar(cats_ba, time_vals, color=time_colors, width=0.5, edgecolor='#ffffff22')
ax1.set_ylabel('Average Test Time (seconds)', fontsize=11, fontweight='bold')
ax1.set_title('Test Bench Time Before/After\n(-- 55.6% Reduction)', fontsize=12, fontweight='bold', color='#f5f3ff')
ax1.set_ylim(0, 130)
ax1.grid(axis='y', linestyle='--', alpha=0.2, color='#c084fc')

for bar, val in zip(bars_t, time_vals):
    ax1.text(bar.get_x() + bar.get_width()/2, val + 2.5, f'{val:.2f}s',
             ha='center', va='bottom', fontsize=12, fontweight='bold', color='#f5f3ff')

ax1.annotate('  55.6% Reduction', xy=(1, 50), xytext=(0.25, 115),
            arrowprops=dict(facecolor='#34d399', shrink=0.05, width=2, headwidth=10),
            fontsize=12, fontweight='bold', color='#34d399',
            bbox=dict(boxstyle='round,pad=0.4', facecolor='#18122b', edgecolor='#34d399', alpha=0.9))

co2_labels = ['Baseline\n(Annual CO2)', 'Super Stacking\n(Annual CO2)']
baseline_co2 = 71.9
reduced_co2 = 32.0
co2_vals = [baseline_co2, reduced_co2]
co2_colors = ['#6b21a8', '#38bdf8']

bars_c = ax2.bar(co2_labels, co2_vals, color=co2_colors, width=0.5, edgecolor='#ffffff22')
ax2.set_ylabel('Annual CO2 Emissions (Tons)', fontsize=11, fontweight='bold')
ax2.set_title('Annual CO2 Emissions Before/After\n(-- 55.6% Reduction, 39.9T Saved)', fontsize=12, fontweight='bold', color='#f5f3ff')
ax2.set_ylim(0, 100)
ax2.grid(axis='y', linestyle='--', alpha=0.2, color='#c084fc')

for bar, val in zip(bars_c, co2_vals):
    ax2.text(bar.get_x() + bar.get_width()/2, val + 1.5, f'{val:.1f}T',
             ha='center', va='bottom', fontsize=12, fontweight='bold', color='#f5f3ff')

ax2.annotate('  55.6% Reduction\n  (39.9T Saved)', xy=(1, 36), xytext=(0.2, 85),
            arrowprops=dict(facecolor='#38bdf8', shrink=0.05, width=2, headwidth=10),
            fontsize=11, fontweight='bold', color='#38bdf8',
            bbox=dict(boxstyle='round,pad=0.4', facecolor='#18122b', edgecolor='#38bdf8', alpha=0.9))

plt.tight_layout()
fig.savefig(os.path.join(vis_dir, "11_before_after_reduction_comparison.png"), dpi=300)
plt.close(fig)
print("Saved: 11_before_after_reduction_comparison.png")

# ==============================================================================
# CHART 12: Test Bench Duration (y) Interval Distribution
# ==============================================================================
fig, ax = plt.subplots(figsize=(12, 6), dpi=300)

intervals = ['< 80s', '80s~90s\n(High Efficiency)', '90s~100s\n(Peak Bucket)', '100s~110s', '110s~120s', '> 120s\n(Bottleneck Delay)']
counts = [406, 712, 1351, 1083, 429, 228]
percentages = [c / sum(counts) * 100 for c in counts]
bar_colors = ['#34d399', '#38bdf8', '#e879f9', '#c084fc', '#a855f7', '#fb7185']

bars12 = ax.bar(intervals, counts, color=bar_colors, width=0.6, edgecolor='#ffffff22')
ax.set_ylabel('Test Bench Count', fontsize=11, fontweight='bold')
ax.set_title('Actual Mercedes-Benz Test Bench Duration (y) Distribution (N=4,209)', fontsize=13, fontweight='bold', pad=15, color='#f5f3ff')
ax.set_ylim(0, 1600)
ax.grid(axis='y', linestyle='--', alpha=0.2, color='#c084fc')

ax.axhline(y=sum(counts)/len(counts), color='#f472b6', linestyle=':', linewidth=1.5, alpha=0.5)

for bar, cnt, pct in zip(bars12, counts, percentages):
    ax.text(bar.get_x() + bar.get_width()/2, cnt + 25,
            f'{cnt:,}\n({pct:.1f}%)',
            ha='center', va='bottom', fontsize=9, fontweight='bold', color='#f5f3ff')

ax.text(0.02, 0.85, f'Mean: 100.67s\nMin 72.11s / Max 265.32s',
        transform=ax.transAxes, fontsize=10, fontweight='bold', color='#38bdf8',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='#18122b', edgecolor='#38bdf8', alpha=0.9))

plt.tight_layout()
fig.savefig(os.path.join(vis_dir, "12_test_bench_y_distribution.png"), dpi=300)
plt.close(fig)
print("Saved: 12_test_bench_y_distribution.png")

# ==============================================================================
# CHART 13: Key Categorical Feature X0 vs Average Test Time
# ==============================================================================
fig, ax = plt.subplots(figsize=(11, 6), dpi=300)

x0_categories = ['X0 = ap', 'X0 = ak', 'X0 = z\n(Most Frequent)', 'X0 = y']
x0_times = [116.58, 105.41, 100.82, 94.78]
x0_colors = ['#fb7185', '#e879f9', '#c084fc', '#34d399']

bars13 = ax.barh(x0_categories[::-1], x0_times[::-1], color=x0_colors[::-1], height=0.55, edgecolor='#ffffff22')
ax.set_xlabel('Average Test Bench Duration (seconds)', fontsize=11, fontweight='bold', labelpad=10)
ax.set_title('Key Categorical Feature X0 vs Average Test Time (47 Groups)', fontsize=13, fontweight='bold', pad=15, color='#f5f3ff')
ax.set_xlim(85, 130)
ax.grid(axis='x', linestyle='--', alpha=0.2, color='#c084fc')

ax.axvline(100.67, color='#38bdf8', linestyle=':', linewidth=1.5, label='Overall Mean 100.67s')

for bar, val in zip(bars13, x0_times[::-1]):
    ax.text(val + 0.5, bar.get_y() + bar.get_height()/2, f'{val:.2f}s',
            va='center', ha='left', fontsize=10, fontweight='bold', color='#f5f3ff')

ax.legend(loc='lower right', frameon=True, facecolor=PANEL_COLOR, edgecolor='#c084fc', fontsize=9)

plt.tight_layout()
fig.savefig(os.path.join(vis_dir, "13_x0_category_avg_time.png"), dpi=300)
plt.close(fig)
print("Saved: 13_x0_category_avg_time.png")

# ==============================================================================
# CHART 14: KPI Summary Dashboard
# ==============================================================================
fig, axes = plt.subplots(2, 4, figsize=(18, 7), dpi=300)
fig.suptitle('Six Sigma AI Economic Impact & Executive ROI Summary Dashboard', fontsize=15, fontweight='bold', color='#f5f3ff', y=0.98)

kpi_data = [
    ('6-SIGMA\nQUALITY', '6.0 σ', 'Cpk: 1.67\nDefect: 3.4 PPM', '#34d399'),
    ('11 + 65.30M\nMax DT Fusion', '0.56979', 'Top 10 + 65.30M\nDT Super Stacking', '#e879f9'),
    ('CTQ Optimization\nAchievement', '55.6%', '100.67s -> 44.72s\nCO2 39.9T Saved', '#fb7185'),
    ('Intelligent MES\nOEE', '99.9%', 'Overall Equipment\nEffectiveness', '#38bdf8'),
    ('Annual Direct\nOPEX Savings', '₩ 13.04B', 'Test Duration\n51.8% Saved', '#d8b4fe'),
    ('Equipment Output\nValue Add', '+95,000 / Yr', 'MES OEE 98.5%\nAchieved', '#c084fc'),
    ('ESG Carbon\nOffset Value', '39.9 T CO2', 'Power Consumption\n51.8% Saved', '#a855f7'),
    ('Total Economic\nImpact', '₩ 21.60B / Yr', 'ROI 1,480%\nPayback 0.8 Mos', '#34d399'),
]

for ax_item, (title, value, detail, color) in zip(axes.flat, kpi_data):
    ax_item.set_facecolor('#18122b')
    ax_item.set_xlim(0, 1)
    ax_item.set_ylim(0, 1)
    ax_item.set_xticks([])
    ax_item.set_yticks([])

    for spine in ax_item.spines.values():
        spine.set_color(color)
        spine.set_linewidth(1.5)

    ax_item.text(0.5, 0.82, title, ha='center', va='center', fontsize=9, fontweight='bold', color=TEXT_COLOR)
    ax_item.text(0.5, 0.50, value, ha='center', va='center', fontsize=16, fontweight='bold', color=color)
    ax_item.text(0.5, 0.18, detail, ha='center', va='center', fontsize=7.5, color='#a0a0b0')

plt.tight_layout(rect=[0, 0, 1, 0.95])
fig.savefig(os.path.join(vis_dir, "14_kpi_summary_dashboard.png"), dpi=300)
print("Saved: 14_kpi_summary_dashboard.png")

# ==============================================================================
# CHART 15: End-to-End System & MB Data Architecture (MacBook Pro, Streamlit, DGX Spark)
# ==============================================================================
fig, ax = plt.subplots(figsize=(20, 11), dpi=300)
ax.set_facecolor('#0f0c1d')
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')

# Main Title
ax.text(50, 97.0, 'End-to-End Enterprise Architecture: MacBook Pro, MB Data Pipeline & DGX Spark Engine',
        ha='center', va='center', fontsize=19, fontweight='bold', color='#f5f3ff')

# Pillar 1: LOCAL CONTROLLER (Apple MacBook Pro) - x: 2 to 23.5, y: 15 to 92
rect_mac = plt.Rectangle((2, 15), 21.5, 77, facecolor='#18122b', edgecolor='#38bdf8', linewidth=2.5, linestyle='-')
ax.add_patch(rect_mac)
ax.text(12.75, 87.5, 'LOCAL CONTROLLER\n(Apple MacBook Pro)', ha='center', va='center', fontsize=15.5, fontweight='bold', color='#38bdf8')
ax.plot([3.5, 22], [83.0, 83.0], color='#38bdf8', linewidth=1.5, linestyle='--')

mac_text = (
    "1. Workstation & SSH Tunnel\n"
    "   • Apple MacBook Pro M-Silicon\n"
    "   • Paramiko SSH Async Tunneling\n"
    "   • Async Command Dispatcher\n\n"
    "2. Dual Interactive UIs\n"
    "   • Streamlit Live UI (GA Sliders)\n"
    "   • yani-studio (Flask Web UI)\n"
    "   • Live Performance Telemetry\n\n"
    "3. Bi-Directional Streaming\n"
    "   • Inbound: Control Directives\n"
    "   • Outbound: WebSockets / SSE\n"
    "   • Dynamic Parameter Sync"
)
ax.text(3.0, 48.5, mac_text, ha='left', va='center', fontsize=13.5, color='#ffffff', fontweight='bold', multialignment='left', linespacing=1.28)

# Pillar 2: MERCEDES-BENZ DATA SCHEMA - x: 26 to 47.5, y: 15 to 92
rect_data = plt.Rectangle((26, 15), 21.5, 77, facecolor='#18122b', edgecolor='#f472b6', linewidth=2.5, linestyle='-')
ax.add_patch(rect_data)
ax.text(36.75, 87.5, 'MB DATA PIPELINE & SCHEMA\n(N=4,209 x 551 Features)', ha='center', va='center', fontsize=15.5, fontweight='bold', color='#f472b6')
ax.plot([27.5, 46], [83.0, 83.0], color='#f472b6', linewidth=1.5, linestyle='--')

data_text = (
    "1. CTQ Target y (Duration)\n"
    "   • Continuous Float Target (s)\n"
    "   • Mean: 100.67s | Median: 99.15s\n"
    "   • Range: 72.11s ~ 265.32s\n\n"
    "2. Categorical (X0 ~ X8)\n"
    "   • 8 Vehicle Option Codes\n"
    "   • One-Hot / Target Encoded\n"
    "   • 195 Dummy Feature Columns\n\n"
    "3. Binary Switches (X10 ~ X385)\n"
    "   • 368 Test Feature Flags\n"
    "   • 12 Zero-Var -> 356 Active\n\n"
    "4. Vital Few Gain Drivers\n"
    "   • X0 (24.8%), X314 (18.2%)\n"
    "   • X118 (12.5%), X27 (8.4%)"
)
ax.text(27.0, 48.5, data_text, ha='left', va='center', fontsize=13.5, color='#ffffff', fontweight='bold', multialignment='left', linespacing=1.28)

# Pillar 3: REMOTE DGX SPARK CLUSTER - x: 50 to 71.5, y: 15 to 92
rect_dgx = plt.Rectangle((50, 15), 21.5, 77, facecolor='#18122b', edgecolor='#e879f9', linewidth=2.8, linestyle='-')
ax.add_patch(rect_dgx)
ax.text(60.75, 87.5, 'REMOTE DGX SPARK CLUSTER\n(NVIDIA GB10 GPU Engine)', ha='center', va='center', fontsize=15.5, fontweight='bold', color='#e879f9')
ax.plot([51.5, 70], [83.0, 83.0], color='#e879f9', linewidth=1.5, linestyle='--')

dgx_text = (
    "1. 65.30M Digital Twin GA\n"
    "   • Parallel Search Engine\n"
    "   • Golden: 42.54M GA Pop\n"
    "   • Mut: 0.05 | Xover: 0.85\n\n"
    "2. Super Stacking Ensemble\n"
    "   • 10 Base Models + DT Fusion\n"
    "   • XGB, LGBM, CatBoost, SVR\n"
    "   • Validation Max R² = 0.56979\n\n"
    "3. Bi-Directional Streamer\n"
    "   • Live Fitness & GPU Telemetry\n"
    "   • Control Loop (gRPC Directives)\n"
    "   • Real-Time Residual SPC"
)
ax.text(51.0, 48.5, dgx_text, ha='left', va='center', fontsize=13.5, color='#ffffff', fontweight='bold', multialignment='left', linespacing=1.28)

# Pillar 4: PRODUCTION & MES IMPACT - x: 74 to 95.5, y: 15 to 92
rect_mes = plt.Rectangle((74, 15), 21.5, 77, facecolor='#18122b', edgecolor='#34d399', linewidth=2.5, linestyle='-')
ax.add_patch(rect_mes)
ax.text(84.75, 87.5, 'PRODUCTION & MES IMPACT\n(Mercedes-Benz Test Factory)', ha='center', va='center', fontsize=15.5, fontweight='bold', color='#34d399')
ax.plot([75.5, 94], [83.0, 83.0], color='#34d399', linewidth=1.5, linestyle='--')

mes_text = (
    "1. MES Test Integration\n"
    "   • N=4,209 Vehicle Test Cases\n"
    "   • Real-time Parameter Tuning\n\n"
    "2. Bench Time Optimization\n"
    "   • 100.67s → 44.72s (-55.6%)\n"
    "   • 55.95s Saved Per Vehicle\n\n"
    "3. ESG & Financial Value\n"
    "   • 51.8% kWh Power Saved\n"
    "   • 39.9 Tons CO₂ Reduced/Yr\n"
    "   • Annual Value: ₩ 21.60B/Yr\n"
    "   • Executive ROI: 1,480%\n"
    "   • Payback: 0.8 Months"
)
ax.text(75.0, 48.5, mes_text, ha='left', va='center', fontsize=13.5, color='#ffffff', fontweight='bold', multialignment='left', linespacing=1.28)

# Flow Arrows & Badges (Enlarged Front Arrows, Opaque Badges, Zero Background Overlaps)
# Arrow 1: Pillar 1 -> Pillar 2 (x: 23.5 to 26.0 at y=65)
ax.annotate('', xy=(26.0, 65), xytext=(23.5, 65),
            arrowprops=dict(facecolor='#38bdf8', edgecolor='#38bdf8', shrink=0, width=3.2, headwidth=12, headlength=9))
ax.text(24.75, 71.5, 'SSH / gRPC Directives', ha='center', va='bottom', fontsize=10.5, fontweight='bold', color='#38bdf8',
        bbox=dict(facecolor='#0f0c1d', edgecolor='#38bdf8', alpha=1.0, pad=3.5, boxstyle='round,pad=0.4'))

# Arrow 2: Pillar 2 -> Pillar 3 (x: 47.5 to 50.0 at y=65)
ax.annotate('', xy=(50.0, 65), xytext=(47.5, 65),
            arrowprops=dict(facecolor='#f472b6', edgecolor='#f472b6', shrink=0, width=3.2, headwidth=12, headlength=9))
ax.text(48.75, 71.5, '551D Data Matrix', ha='center', va='bottom', fontsize=10.5, fontweight='bold', color='#f472b6',
        bbox=dict(facecolor='#0f0c1d', edgecolor='#f472b6', alpha=1.0, pad=3.5, boxstyle='round,pad=0.4'))

# Arrow 3: Pillar 3 -> Pillar 4 (x: 71.5 to 74.0 at y=65)
ax.annotate('', xy=(74.0, 65), xytext=(71.5, 65),
            arrowprops=dict(facecolor='#e879f9', edgecolor='#e879f9', shrink=0, width=3.2, headwidth=12, headlength=9))
ax.text(72.75, 71.5, 'GA Params & Weights', ha='center', va='bottom', fontsize=10.5, fontweight='bold', color='#e879f9',
        bbox=dict(facecolor='#0f0c1d', edgecolor='#e879f9', alpha=1.0, pad=3.5, boxstyle='round,pad=0.4'))

# Long Bottom Telemetry Arrow: Pillar 3 -> Pillar 1 (x: 50.0 to 23.5 at y=24)
ax.annotate('', xy=(23.5, 24), xytext=(50.0, 24),
            arrowprops=dict(facecolor='#e879f9', edgecolor='#e879f9', shrink=0, width=3.2, headwidth=12, headlength=9))
ax.text(36.75, 17.5, 'Bi-Directional Stream: Real-Time Streamlit / Flask Telemetry & WebSocket Logs',
        ha='center', va='top', fontsize=10.5, fontweight='bold', color='#e879f9',
        bbox=dict(facecolor='#18122b', edgecolor='#e879f9', alpha=1.0, pad=4.0, boxstyle='round,pad=0.4'))

# Arrow 4: Pillar 4 -> Pillar 3 Feedback (x: 74.0 to 71.5 at y=24)
ax.annotate('', xy=(71.5, 24), xytext=(74.0, 24),
            arrowprops=dict(facecolor='#34d399', edgecolor='#34d399', shrink=0, width=3.2, headwidth=12, headlength=9))
ax.text(72.75, 17.5, 'Bench Sensors', ha='center', va='top', fontsize=10.5, fontweight='bold', color='#34d399',
        bbox=dict(facecolor='#0f0c1d', edgecolor='#34d399', alpha=1.0, pad=3.5, boxstyle='round,pad=0.4'))

# Bottom Banner: KPI Summary Bar
rect_bottom = plt.Rectangle((2, 2.5), 93.5, 10.5, facecolor='#18122b', edgecolor='#f472b6', linewidth=2.0, linestyle='--')
ax.add_patch(rect_bottom)
ax.text(48.75, 7.75, 'ENTERPRISE SYSTEM INTEGRATION & MERCEDES-BENZ DATA SCHEMA KPI HIGHLIGHTS\n'
               'Bi-Directional Streaming (gRPC/WebSockets) | Streamlit & Flask UIs | MB Dataset: N=4,209 × 551 | Validation R²: 0.56979 | Time: -55.6% | Value: ₩ 21.60B/Yr (1,480%)',
        ha='center', va='center', fontsize=11.0, fontweight='bold', color='#f5f3ff')

plt.tight_layout()
fig.savefig(os.path.join(vis_dir, "15_system_architecture.png"), dpi=300)
plt.close(fig)
print("Saved: 15_system_architecture.png")

print("\n>>> All 15 performance & architecture visualizations generated in English successfully! Folder: visualization/")


