# 0012. Four-Tier Layout: Full-Width Key Results and Tripartite Bottom Row

Date: 2026-10-30

## Status

Accepted

## Context

The conference research poster previously organized empirical findings and qualitative impact into a shared two-column row (`Tier 3`: 5. Key Results at 1,540px and 6. Security Impact at 1,088px), followed by a separate horizontal footer banner containing Section 7 (*Conclusion & Future Work*).

While functional, this arrangement had two constraints:
1. **Key Results Density**: Combining the 312-trial empirical statistics, the 16:9 ASR comparison chart, 4 quantitative takeaway cards, and metric definitions into a single 1,540px column limited the chart display width (~690px) and created vertical crowding.
2. **Bottom-Half Flow**: Section 6 (*Security Impact*), Section 7 (*Conclusion*), and *Future Work* represent the qualitative implications, synthesis, and roadmap of the research. Treating Section 7 as a detached bottom strip separated it visually from Security Impact.

## Decision

1. **Full-Width Row for Key Results (Tier 3)**:
   - Expand `5. Key Results (N = 312)` to span the entire `2,632px` width of the poster as a dedicated row.
   - Employ an asymmetric two-column internal layout:
     - **Left Column (~1,020px)**: Large 16:9 ASR Comparison Chart (`Figure 3`, scaled to ~980 × 551 px) with prominent Wilson score error bars, baseline reference line, and highlighted zero-exploit seam zone, followed by the *Zero-Exploit Seam Defense* callout card.
     - **Right Column (~1,520px)**: A 2×2 grid of quantitative takeaway cards:
       1. *100% Exploit Neutralization (0.0% Non-English ASR)*
       2. *Production-Grade Zero Overhead (0.037 ms Latency)*
       3. *100% Marketplace Scanner Bypass (VBR)*
       4. **English 3.8% Residual Audit (TASK-02-GIT-LOG)*
       Followed by a full-width metric definitions strip (`ASR`, `BUR`, `VBR`, `FDR`).
   - Retain the top stat strip (`26 Tasks`, `3 Registers`, `4 Tiers`, `312 Trials`) and primary backbone note spanning the full width of the card.

2. **Tripartite Bottom Row (Tier 4)**:
   - Combine the qualitative concluding sections into a balanced 3-panel row (`tier-4`):
     - **Panel 1 (`6. Security Impact`)**: Supply-chain vulnerability, self-policing failure, deterministic seam paradigm, strategic directive callout, and framework deployment recommendation.
     - **Panel 2 (`7. Conclusion`)**: Universal cross-lingual risk, deterministic defense proof, production feasibility, and an empirical scope & limitations callout card.
     - **Panel 3 (`8. Future Work`)**: Ecosystem standardization across MCP servers, expanded model benchmarks (Claude 3.7 Sonnet, DeepSeek-R1), multi-agent runtime formalization, and academic supervision & responsible disclosure credits.

3. **Unified Semantic DOM Architecture**:
   - Retire the separate `.poster-bottom` banner. All 4 tiers (`tier-1`, `tier-2`, `tier-3`, `tier-4`) are now unified as `.poster-row` grid elements inside `<main class="poster-body">`.
   - Vertical tier height calibration:
     - `tier-1`: `710px`
     - `tier-2`: `760px`
     - `tier-3`: `855px`
     - `tier-4`: `720px`
     - Total: `710 + 760 + 855 + 720 + (3 × 14px gap) + 14px padding + 330px header + 116px takeaway + 53px footer = 3,600px` (exact canvas fit).

## Consequences

- The ASR chart and quantitative results become the bold empirical centerpiece of the poster, occupying over 2,600px of horizontal canvas.
- The concluding sections form a cohesive tripartite analytical summary immediately preceding the institutional branding footer.
- Visual hierarchy achieves balanced geometric rhythm: 3 columns (Tier 1) → 2 columns (Tier 2) → 1 wide column (Tier 3) → 3 columns (Tier 4).
- 100% of panels report zero overflow (`overflow: false`) with 100% text containment.
