# 0011. Removal of Redundant Sub-Figure Text in Threat Model and Methodology Panels

Date: 2026-10-30

## Status

Accepted

## Context

The research poster presentation for *Cross-Lingual Agent Skill Poisoning: Active Runtime Exploitation and Deterministic Authorization in Tool-Using LLM Agents* features two centerpiece architectural diagrams in Row Tier 2:
- **Figure 1**: Threat Progression & Seam Interception (`threat_lifecycle.png`)
- **Figure 2**: Deterministic Authorization Seam Architecture (`defense_seam_architecture.png`)

Following ADR 0010, both figures were upgraded to robust, iconic vector graphics featuring comprehensive internal titles, subtitles, step conduits, and invariant labels. However, beneath each diagram in Tier 2, there remained:
1. A figure caption box (e.g. `Figure 1: Five-stage threat progression...`).
2. A 3-item bulleted walkthrough card duplicating the supply-chain, rug-pull, and seam enforcement concepts already visualized inside the figures.

This sub-figure text caused two primary issues:
- **Text Density**: Unnecessary textual clutter in a row designed to serve as the visual centerpiece of the poster.
- **Diagram Scaling Constraint**: The ~360px vertical space consumed by captions and bullet points forced the 16:9 diagrams to be artificially restricted to `height: 505px` (`width: ~888px`), leaving empty lateral margins inside 1,307px wide panels.

## Decision

1. **Remove All Text Below Figures in Tier 2**:
   - Completely eliminate `.figure-caption` and `.figure-points` below Figure 1 (Threat Model) and Figure 2 (Methodology).
   - The body of each Tier 2 panel now contains exclusively the 16:9 diagram wrapper.

2. **Header Figure Identification Badges**:
   - Add clean academic badges (`[ Figure 1 ]` and `[ Figure 2 ]`) to the right side of `.figure-header` using flexbox space-between alignment.
   - This preserves figure references without encroaching on canvas space.

3. **Diagram Scaling to Full 16:9 Dimensions**:
   - Expand `.tier-2 .figure-img-wrap` to `height: 720px`.
   - The 16:9 diagrams now scale to `1277 × 718 px`, filling the full card width with zero letterboxing—a **44% enlargement in active visual area**.

4. **Vertical Tier Height Recalibration**:
   - Rebalance poster rows to maintain exact `3600px` canvas containment:
     - `tier-1`: `800px` (provides generous vertical spacing for Motivation, Contributions, and Threat Model).
     - `tier-2`: `815px` (houses 720px figures with 0px gap and zero overflow).
     - `tier-3`: `1015px` (houses 385px ASR chart and spacious takeaway cards).
   - Verified via Chrome DevTools Protocol that **100% of panels report `overflow: false`** and `poster.scrollHeight == poster.clientHeight == 3600px`.

## Consequences

- Row Tier 2 becomes an uncluttered, high-impact visual centerpiece where diagrams are immediately legible from 6+ feet away.
- Redundant explanatory text is eliminated while preserving complete academic rigor.
- Master print assets (27" × 36" vector PDF and 300 DPI PNG) render with zero clipping and perfect bottom footer alignment.
