# 0009: Removal of Dense Results Table, Figure De-Textualization, and Noticeable Line Spacing

## Context

Following user feedback on the previous iteration of the conference research poster, attendees and viewers reported that:
1. The 7-column Defense Configuration Table in Section 5 (*Key Results*) was excessively text-dense and difficult to parse quickly from a standing viewing distance of 3–5 feet.
2. The technical figures (Figure 1: *Threat Lifecycle*, Figure 2: *Defense Seam Architecture*, Figure 3: *ASR Chart*), while standardized to 16:9 and 28px font, still contained multiple lines of explanatory prose that distracted from the core graphical workflow.
3. The vertical line spacing across poster cards and lists felt tight, making individual bullet points harder to distinguish rapidly.

## Decision

We make the following architectural and typographic decisions:

1. **Elimination of the 7-Column Defense Configuration Table**:
   - Remove the dense HTML table from Section 5 (*Key Results*).
   - In its place, structure Section 5 into a clean two-column layout:
     - **Left Column**: Prominent 16:9 Figure 3 ASR chart (which already visualizes ASR percentages, error bars, and baseline comparisons across all tiers and registers) with its zero-exploit takeaway badge.
     - **Right Column**: Four spacious, high-contrast quantitative takeaway cards with noticeable line spacing covering:
       - 100% Exploit Neutralization (0.0% ASR in non-English).
       - Sub-0.05ms Overhead (0.037 ms latency, 0.0% FDR, 100% benign utility).
       - 100% Marketplace Scanner Bypass (VBR).
       - Task-02 Residual Root Cause and Schema Alias Normalization.

2. **Figure De-Textualization & Minimal Graphical Workflow**:
   - Strip all non-essential explanatory prose from Figure 1 and Figure 2, leaving only high-signal labels (max 2 short lines per card) at **28px** font size.
   - Use bold SVG vector icons (`<path>` checkmarks and denial crosses) to convey security states visually rather than through lengthy sentences.
   - Streamline Figure 3 title, subtitle, and callout labels for instant visual comprehension.

3. **Noticeable Line Spacing Across All Panels**:
   - Increase `line-height` across all body elements (`.clean-list li`, `.figure-point-item`, `.callout-desc`, `.bottom-card p`) from `1.34–1.40` to **`1.55–1.65`**.
   - Increase vertical spacing between items to **`12–16px`** so each line stands out distinctly.
   - Preserve total canvas budget (`3,600px` height) with zero canvas overflow and 100% visibility of the institutional footer.

## Consequences

- The poster shifts from a document-heavy format to a punchy, executive conference presentation asset.
- Viewers can absorb key findings in under 30 seconds from 5 feet away.
- All empirical metrics (N = 312, 26 tasks, 3 registers, 4 defense tiers, 95% Wilson CIs, 0.037 ms latency, 100% VBR, 0.0% FDR, 3.8% residual) remain fully represented and cited without visual crowding.
