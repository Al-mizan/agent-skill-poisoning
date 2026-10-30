#!/usr/bin/env python3
"""
generate_asr_chart_v2.py
Generates the centerpiece ASR chart in strict 16:9 aspect ratio (1920x1080)
with publication-quality 28px typography, iconic status badges,
and highlighted zero-exploit protection zone.
"""

import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

def generate_asr_chart():
    # Academic publication styling
    plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
    plt.rcParams['axes.edgecolor'] = '#94a3b8'
    plt.rcParams['axes.linewidth'] = 2.0

    # Strict 16:9 ratio: 19.2 x 10.8 inches at 100 DPI -> 1920 x 1080 px
    fig, ax = plt.subplots(figsize=(19.2, 10.8), dpi=100)
    fig.patch.set_facecolor('#ffffff')
    ax.set_facecolor('#ffffff')

    # Categories
    defenses = [
        'Undefended\n(Baseline)',
        'Static Scanner\n(Marketplace)',
        'Prompt Isolation\n(Boundary Defense)',
        'Policy Seam\n(Deterministic Ours)'
    ]
    n_groups = len(defenses)

    # Data: ASR percentages
    asr_en = [100.0, 76.9, 7.7, 3.8]
    asr_bn = [100.0, 100.0, 3.8, 0.0]
    asr_bnen = [100.0, 100.0, 0.0, 0.0]

    # Asymmetric Wilson 95% CI error bounds: (val - lower, upper - val)
    err_en = np.array([
        [12.9, 0.0],
        [19.0, 12.1],
        [5.6, 16.4],
        [3.1, 15.1]
    ]).T

    err_bn = np.array([
        [12.9, 0.0],
        [12.9, 0.0],
        [3.1, 15.1],
        [0.0, 12.9]
    ]).T

    err_bnen = np.array([
        [12.9, 0.0],
        [12.9, 0.0],
        [0.0, 12.9],
        [0.0, 12.9]
    ]).T

    bar_width = 0.24
    indices = np.arange(n_groups)

    # High-contrast color palette matching poster
    c_en = '#2563eb'    # Royal Blue
    c_bn = '#d97706'    # Amber / Orange
    c_bnen = '#059669'  # Emerald Green

    # Highlight Zone behind Tier 4 (Policy Seam)
    seam_highlight = patches.Rectangle(
        (indices[3] - bar_width * 1.8, 0),
        bar_width * 3.6,
        124,
        linewidth=2.0,
        edgecolor='#10b981',
        facecolor='#f0fdf4',
        linestyle='--',
        alpha=0.6,
        zorder=0
    )
    ax.add_patch(seam_highlight)

    # Seam highlight banner text placed at y=113 (below legend)
    ax.text(indices[3], 114.0, '★ Zero-Exploit Seam Defense (0.0% Non-English ASR)',
            ha='center', va='center', fontsize=17, fontweight='bold', color='#0f766e',
            bbox=dict(boxstyle='round,pad=0.4', facecolor='#ccfbf1', edgecolor='#14b8a6', linewidth=1.5), zorder=2)

    # Baseline risk reference line at 100%
    ax.axhline(y=100, color='#ef4444', linestyle=':', linewidth=2.6, alpha=0.9, zorder=1)
    ax.text(indices[3] + bar_width * 1.7, 102.5, 'Baseline Risk (100%)',
            fontsize=18, fontweight='bold', color='#dc2626', ha='right', va='bottom')

    # Plot grouped bars
    bars1 = ax.bar(indices - bar_width, asr_en, bar_width, yerr=err_en, capsize=7,
                   color=c_en, edgecolor='#1e40af', linewidth=2.0, label='English (en) [n=26]',
                   error_kw={'elinewidth': 2.4, 'ecolor': '#1e3a8a'}, zorder=3)
    bars2 = ax.bar(indices, asr_bn, bar_width, yerr=err_bn, capsize=7,
                   color=c_bn, edgecolor='#b45309', linewidth=2.0, label='Bangla native (bn) [n=26]',
                   error_kw={'elinewidth': 2.4, 'ecolor': '#78350f'}, zorder=3)
    bars3 = ax.bar(indices + bar_width, asr_bnen, bar_width, yerr=err_bnen, capsize=7,
                   color=c_bnen, edgecolor='#047857', linewidth=2.0, label='Banglish mixed (bn-en) [n=26]',
                   error_kw={'elinewidth': 2.4, 'ecolor': '#064e3b'}, zorder=3)

    # Numeric callout badges above the bars
    # 1. Undefended
    ax.text(indices[0], 104.5, '100% (All Registers)',
            ha='center', va='bottom', fontsize=19, fontweight='bold', color='#991b1b',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#fee2e2', edgecolor='#fca5a5', linewidth=1.4), zorder=4)

    # 2. Static Scanner
    ax.text(indices[1] - bar_width, 76.9 + 12.1 + 3.0, '76.9%',
            ha='center', va='bottom', fontsize=19, fontweight='bold', color='#991b1b',
            bbox=dict(boxstyle='round,pad=0.25', facecolor='#fee2e2', edgecolor='#fca5a5', linewidth=1.2), zorder=4)
    ax.text(indices[1] + (bar_width / 2.0), 104.5, '100% (100% VBR)',
            ha='center', va='bottom', fontsize=19, fontweight='bold', color='#b45309',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#fef3c7', edgecolor='#fcd34d', linewidth=1.4), zorder=4)

    # 3. Prompt Isolation
    ax.text(indices[2] - bar_width, 7.7 + 16.4 + 3.0, '7.7%',
            ha='center', va='bottom', fontsize=18.5, fontweight='bold', color='#1e293b',
            bbox=dict(boxstyle='round,pad=0.25', facecolor='#f1f5f9', edgecolor='#cbd5e1', linewidth=1.2), zorder=4)
    ax.text(indices[2], 3.8 + 15.1 + 3.0, '3.8%',
            ha='center', va='bottom', fontsize=18.5, fontweight='bold', color='#1e293b',
            bbox=dict(boxstyle='round,pad=0.25', facecolor='#f1f5f9', edgecolor='#cbd5e1', linewidth=1.2), zorder=4)
    ax.text(indices[2] + bar_width, 0.0 + 12.9 + 3.0, '0.0%',
            ha='center', va='bottom', fontsize=18.5, fontweight='bold', color='#15803d',
            bbox=dict(boxstyle='round,pad=0.25', facecolor='#dcfce7', edgecolor='#86efac', linewidth=1.2), zorder=4)

    # 4. Policy Seam
    ax.text(indices[3] - bar_width, 3.8 + 15.1 + 3.0, '3.8%*',
            ha='center', va='bottom', fontsize=19, fontweight='bold', color='#0f766e',
            bbox=dict(boxstyle='round,pad=0.25', facecolor='#ccfbf1', edgecolor='#5eead4', linewidth=1.2), zorder=4)
    ax.text(indices[3] + (bar_width / 2.0), 0.0 + 12.9 + 3.0, '0.0% (Zero Exploits)',
            ha='center', va='bottom', fontsize=19, fontweight='bold', color='#15803d',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#dcfce7', edgecolor='#86efac', linewidth=1.5), zorder=4)

    # Iconic status badges below category labels
    status_badges = [
        '[ Baseline Vulnerable ]',
        '[ 100% Registry Bypass ]',
        '[ Boundary Isolation ]',
        '[ Deterministic Seam Gateway ]'
    ]
    status_colors = ['#dc2626', '#d97706', '#2563eb', '#0f766e']
    status_bgs = ['#fee2e2', '#fef3c7', '#eff6ff', '#ccfbf1']

    for i in range(n_groups):
        ax.text(indices[i], -12.5, status_badges[i],
                ha='center', va='top', fontsize=16.5, fontweight='bold', color=status_colors[i],
                bbox=dict(boxstyle='round,pad=0.3', facecolor=status_bgs[i], edgecolor=status_colors[i], linewidth=1.4))

    # Gridlines & Axis Limits (expanded to 136 for clean top legend clearance)
    ax.set_ylim(0, 136)
    ax.set_yticks([0, 20, 40, 60, 80, 100])
    ax.set_yticklabels(['0%', '20%', '40%', '60%', '80%', '100%'], fontsize=20, fontweight='bold', color='#334155')
    ax.set_ylabel('Attack Success Rate (ASR %)', fontsize=22, fontweight='bold', color='#0f172a', labelpad=18)

    ax.set_xticks(indices)
    ax.set_xticklabels(defenses, fontsize=20, fontweight='bold', color='#0f172a')

    ax.grid(axis='y', linestyle='--', alpha=0.45, color='#94a3b8', zorder=0)
    ax.set_axisbelow(True)

    # Spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#94a3b8')
    ax.spines['bottom'].set_color('#0f172a')
    ax.spines['bottom'].set_linewidth(2.4)

    # Clean Top Legend shifted left to avoid seam highlight banner
    legend = ax.legend(frameon=True, facecolor='#f8fafc', edgecolor='#cbd5e1',
                       fontsize=19.5, loc='upper left', bbox_to_anchor=(0.04, 0.98), ncol=3)
    legend.get_frame().set_linewidth(1.8)
    for text in legend.get_texts():
        text.set_color('#1e293b')
        text.set_fontweight('bold')

    # Title & Subtitle
    ax.set_title('Attack Success Rate (ASR) Across Defense Tiers & Linguistic Registers\n'
                 'N = 312 Live Trials · 26 tasks × 3 registers × 4 defense tiers · 95% Wilson Score CIs',
                 fontsize=23, fontweight='bold', color='#0a1e38', pad=24, linespacing=1.35)

    plt.subplots_adjust(bottom=0.14)
    plt.tight_layout()
    for base_dir in ['poster', 'poster_v2']:
        os.makedirs(base_dir, exist_ok=True)
        out_path = os.path.join(base_dir, 'asr_chart.png')
        plt.savefig(out_path, dpi=100, bbox_inches='tight')
        print(f"ASR chart (16:9) generated at: {out_path}")
    plt.close()

if __name__ == '__main__':
    generate_asr_chart()
