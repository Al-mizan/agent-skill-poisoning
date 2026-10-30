# 0008: Poster Copy Condensation and Diagram Typography Upscaling to 28px

## Context

Following the 16:9 diagram aspect ratio transformation and base poster typography upscaling (ADR 0007), visual inspection revealed that both the poster panels and the embedded technical diagrams suffered from heavy textual density. In academic poster presentations (viewed from 3–6 feet), dense multi-line paragraphs reduce attendee engagement and obscure key empirical insights. Furthermore, diagram annotations at 23–24px appeared visually crowded within dense multi-line cards. 

To maximize legibility, impact, and aesthetic elegance, the poster copy must be condensed into concise, punchy statements, and diagram typography must be upscaled to **28px** with correspondingly streamlined phrasing.

## Decision

We update the poster presentation layout and diagram generation pipeline as follows:

1. **Diagram Typography Upscaling to 28px & De-Cluttering**:
   - Upscale base card text, checklist items, and descriptions across Figure 1 (*Threat Lifecycle*), Figure 2 (*Defense Seam Architecture*), and Figure 3 (*ASR Chart*) to **28px** (titles: **32–34px**, badges/pills: **22–26px**).
   - Condense internal text lines to concise, punchy bullet points (15–24 characters per line max, 2–3 lines per container) to ensure generous internal whitespace and zero boundary collisions at 28px.
   - Maintain 100% SVG vector paths for status icons (`<path>` checkmarks and denial marks).

2. **Poster Body Copy Condensation**:
   - Condense all 7 panels into bite-sized, high-contrast, punchy statements while preserving 100% empirical rigor:
     - **Motivation:** 3 sharp bullets on unvetted ingestion, linguistic safety gap, and scanner evasion; 1-line semantic asymmetry callout.
     - **Contributions & RQs:** 3 one-line RQ cards and 3 numbered contribution cards with high-signal metric highlights.
     - **Threat Model:** 4-plane trust boundary architecture and concise rug-pull adversary description.
     - **Tier 2 Walkthroughs:** Streamlined single-line takeaways beneath Figure 1 and Figure 2.
     - **Key Results:** Preserves full 312-trial evaluation table (ASR, 95% Wilson CIs, BUR, VBR, FDR, latency) with compact metric and residual definitions.
     - **Security Impact:** 3 high-impact bullets and concise Strategic Directive / Deployment callouts.
     - **Conclusion & Future Work:** 3-column synthesis with concise findings, explicit scope bounds, and responsible disclosure notes.

3. **Spatial & Visual Breathing Room**:
   - With reduced text volume, the 28–30px poster body typography benefits from increased line-height (`1.45–1.50`) and generous card padding, completely eliminating visual crowding.
   - The dark navy institutional footer remains 100% visible on canvas (`y = 3550` to `3600px`).

## Consequences

- The poster transforms from a text-heavy document into an executive, high-impact conference visual presentation.
- Diagrams are instantly readable from 6 feet away, with 28px text and clear visual hierarchy.
- Zero loss of empirical facts: retains all 312 live trials, 26 tasks, 3 registers, 4 defense tiers, 95% Wilson CIs, 0.037 ms latency, 100% VBR, 0.0% FDR, 3.8% English residual audit, and official Jahangirnagar University CSE supervision credits.
