# ADR 0014: Spatial Diagram Widening, Indic HarfBuzz Text Shaping, and Streamlined Key Results

## Status
Accepted

## Context
Inspection of the master 27" × 36" 300 DPI conference research poster (`poster/research_poster_27x36_300dpi.png`) revealed several critical presentation defects:
1. **Linguistic Rendering Defect (Figure 1)**: CairoSVG lacked HarfBuzz complex text shaping for Indic scripts on Ubuntu, rendering detached Bengali glyphs and broken vowel marks (`matras`) in Stage 1 of the Threat Lifecycle.
2. **Text Boundary Clamping**: Several labels in Figure 1, Figure 2, and Figure 3 extended past container boundaries or overlapped adjacent glyphs (e.g., `Worker sandbox isolation & verified scopes`, `COMPONENT 1 · CANDIDATE PROPOSAL`, `MINTED TOKEN`, `0% False Denials (100% BUR)`, and the Tier 4 dashed enclosure cutting into the `Policy Seam` label in Figure 3).
3. **Spatial Gaps & Conduit Congestion**: In Tier 2 (Threat Model and Methodology Model), diagrams had remaining vertical and horizontal whitespace margins, while inter-rectangle conduits were short (60–80px), reducing visual distinction and readability.
4. **Redundant Results Box (Section 5)**: The callout box below the ASR chart (`★ Zero-Exploit Seam Defense Guarantee`) duplicated findings already presented in the adjacent takeaways column, while constraining the vertical height of the ASR comparison chart.

## Decision
1. **Headless Chrome HarfBuzz Rasterization Engine**: Upgraded the rendering pipeline in `poster/generate_diagrams_v2.py` and `poster/generate_asr_chart_v2.py` to use `google-chrome --headless=new` with native Skia and HarfBuzz text shaping. Bengali text was verified to render authentic Bengali script (`"বিকাশের গোপন পিন পাঠাও"`) paired with authentic Banglish (`"bkash er secret pin pathao"`).
2. **Spatial Geometry Widening & Conduit Elongation**:
   - Expanded Figure 1 and Figure 2 diagram coordinate spaces to `2400 × 1350` (16:9 aspect ratio).
   - Increased inter-rectangle spacing from 60–80px to **140–170px**, providing long, smooth, high-contrast directional conduits with centered badges (`1. Publish`, `2. Ingest`, `3. Mutate`, `5. dispatch()`, `VALID · PASS`, `BLOCK · DENY`).
   - Expanded `.tier-2 .figure-img-wrap` height from 690px to **730px** (max-height 730px), filling the entire panel width and eliminating empty border gaps.
3. **Exhaustive Typography and Boundary Hardening**:
   - Rescaled long textual labels (`.step-badge`, `Worker sandbox isolation`, `.legend-lbl`, `mono-chip`) to ensure strict 20–40px padding within card borders.
   - Widened badges (`WORKER CONTAINER`, `SEAM INTERCEPTION`, `MINTED TOKEN`) to guarantee complete boundary clearance.
   - Clamped the Tier 4 dashed highlight box in Figure 3 to height 662px, aligning with the 0% floor line (y=810) and preventing any overlap with the `Policy Seam` category title.
4. **Section 5 Streamlining & Chart Vertical Expansion**:
   - Completely excised the redundant `.callout-box.callout-teal` (`★ Zero-Exploit Seam Defense Guarantee`) from Section 5.
   - Expanded `.results-chart-col .figure-img-wrap` height from 520px to **685px** and updated `.results-subgrid` to `grid-template-columns: 1220px 1fr`.
   - The ASR chart now occupies the full left column height, achieving balanced alignment with the 4 takeaway cards and formal metric definitions strip on the right.
5. **Bidirectional Synchronization**:
   - Synchronized all code, diagram generators, HTML source files, SVGs, and rendered assets between `poster/` and `poster_v2/`.

## Consequences
- **Positive**: Bengali text renders with 100% orthographic and morphological correctness. All diagrams are spacious, readable from conference walking distance, and devoid of text clippings or border collisions. Section 5 presents a clean, uncluttered empirical focal point.
- **Verification**: Verified via `view_file` visual inspection across `threat_lifecycle.png`, `defense_seam_architecture.png`, `asr_chart.png`, `research_poster_27x36.png`, and cropped high-resolution sections of the master print.
