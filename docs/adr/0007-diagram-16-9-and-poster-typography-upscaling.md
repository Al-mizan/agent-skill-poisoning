# 16:9 Diagram Aspect Ratio Standardization & Poster Typography Upscaling (28–30px)

## Context

Following the horizontal row-wise tier architecture adopted in ADR 0006, the visual diagrams (Figure 1 Threat Lifecycle, Figure 2 Defense Seam Architecture, and Figure 3 ASR Evaluation Chart) were previously rendered with varying aspect ratios (4:3 for SVG diagrams and 1.75:1 for the ASR chart). In horizontal presentation panels, 4:3 diagrams consume excessive vertical height relative to their width, reducing the vertical budget available for primary textual content. Furthermore, conference poster presentation standards require high readability from a viewing distance of 3–5 feet, necessitating primary body text to be scaled to 28–30px with proportional increases across headings and auxiliary elements.

## Decision

We standardize the diagram generation pipeline and poster presentation typography as follows:

1. **Diagram 16:9 Aspect Ratio & Internal Typography**:
   - Re-architect all three technical diagrams (`threat_lifecycle`, `defense_seam_architecture`, and `asr_chart`) to strict **16:9** aspect ratio (`1920 × 1080` for SVG vector diagrams; `12.8 × 7.2` inches at 300 DPI for the matplotlib ASR chart).
   - Calibrate internal diagram typography so that base card text, labels, and descriptions render at **23–24px**, with diagram subheaders at **28–32px** and badges at **20–22px**.

2. **Poster Presentation Typography Upscaling (28–30px Base)**:
   - Scale primary body content (`.clean-list li`, `.callout-desc`, `.contrib-card`, `.rq-card`, `.trust-card`, `.figure-point-item`, `.figure-caption`, `.bottom-card p`) to **28–30px** (line-height: `1.34`).
   - Scale headers and structural text proportionally:
     - Masthead Title: 58px → **66px**
     - Key Takeaway Banner: 30px → **36px** (badge: 20px → **24px**)
     - Panel Headers / Titles: 31–35px → **40–42px**
     - Section Callout Titles: 21–23px → **28–30px**
     - Stat Card Numbers: 44px → **54px**; Labels: 18px → **22px**
     - Pivoted Table Cells: 20px → **25px** (95% Wilson CIs: 16px → **19px**)
     - Bottom Synthesis Cards: Headers **26px**, Paragraphs **26–28px**
     - Footer Bar: 22px → **26px**

3. **Canvas Height Calibration**:
   - Calibrate tier heights (`tier-1`: 720px, `tier-2`: 1060px, `tier-3`: 980px) and maintain concise, dense phrasing to ensure the entire layout fits within the 27" × 36" (2,700 × 3,600 px @ 100 DPI; 8,100 × 10,800 px @ 300 DPI) canvas with zero vertical canvas overflow or boundary clipping.

## Consequences

- 16:9 aspect ratio optimizes horizontal space in side-by-side panels, creating visual symmetry between the attack progression and defense seam in Tier 2.
- 28–30px body font ensures presentation readability across conference exhibition environments without requiring physical proximity.
- The 23–24px internal diagram typography eliminates visual squinting and maintains legibility when diagrams are embedded in the poster.
- Tight copy discipline guarantees full academic completeness (all 312 trials, Wilson CIs, 0.037 ms latency, JU institutional credits) while preserving generous margins.
