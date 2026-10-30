# 0010. Robust, Iconic Diagram Flow Architecture

Date: 2026-10-30

## Status

Accepted

## Context

The research poster presentation for *Cross-Lingual Agent Skill Poisoning: Active Runtime Exploitation and Deterministic Authorization in Tool-Using LLM Agents* features three core figures:
- **Figure 1**: Threat Progression & Seam Interception (attack lifecycle and runtime mediation)
- **Figure 2**: Deterministic Authorization Seam Architecture (execution boundary pipeline)
- **Figure 3**: Attack Success Rate (ASR) Comparison Chart across defense tiers and linguistic registers

While the previous iteration de-textualized the diagrams and upscaled base typography to 28px, the diagrams required visual robustness and iconic presentation:
1. Clearer visual metaphors (iconic emblems for actors, processes, and barriers) rather than standard geometric boxes.
2. Unbroken, directional flow conduits connecting stages and phases (specifically linking supply-chain distribution in Phase I directly to runtime reasoning in Phase II).
3. Robust architectural card designs (multi-layer containers, subtle elevation, header classification bars, and high-contrast status tags).
4. For Figure 3 (the ASR chart), authoritative visual badges, baseline reference thresholds, and a highlighted defense zone.

## Decision

1. **Pure Vector Iconic SVG Emblems**:
   Embed hand-crafted, publication-quality SVG vector glyphs into every stage and component:
   - *Phase I*: Adversary/Exploit authoring glyph, Marketplace Registry cloud scanner glyph, AI Agent terminal/ingestion glyph, Trojan/Rug-pull trigger switch glyph.
   - *Phase II & Seam*: LLM Neural Planner glyph, Pre-dispatch terminal with macOS window controls, Fortress Security Seam shield with token verification keyhole, Sandboxed Execution container with isolation boundaries, Deterministic Denial hard firewall with stop emblem.
   - *Pillars & Invariants*: Vector token key, canonical path resolution folder/traversal mark, and sandbox boundary icons.

2. **Continuous Lifecycle Flow Conduits**:
   - Upgrade arrow lines to robust pipeline conduits with directional flow chevrons and numbered progression tags (`① Ingestion`, `② Bypass`, `③ Rug-Pull Switch`, `④ Candidate Dispatch`, `⑤ Seam Verification`, `⑥ Forked Execution`).
   - Introduce a downward routing conduit linking Stage 4 (*Rug-Pull Update*) to Step 1 (*Reasoning Plane: Ingested Manifest*), establishing an unbroken end-to-end lifecycle narrative.

3. **Chart Visual Robustness (Figure 3)**:
   - Add status badges under defense tiers (`⚠ Baseline`, `🔍 Regex Bypass`, `🛡 Boundary Isolation`, `🔒 Deterministic Seam`).
   - Add shaded focus region around Tier 4 (*Policy Seam*) emphasizing the zero-exploit protection zone.
   - Style callout pills above bars with colored fills, bold borders, and publication-grade typography.

4. **Retention of Core Constraints**:
   - Maintain exact 16:9 aspect ratio (`1920 × 1080 px`).
   - Retain base body typography of 28px (titles 32–40px, badges 22–26px).
   - Maintain exact empirical data (N = 312, 26 tasks, 3 registers, 4 defense tiers, 95% Wilson CIs, 0.037 ms latency).

## Consequences

- Visual clarity and audience engagement are significantly improved for physical conference viewing (4–6 feet distance).
- Flow becomes instantly intuitive without needing to read extensive explanatory text.
- Vector SVG icons guarantee 100% sharpness with zero font glyph rendering anomalies across both 100 DPI preview and 300 DPI print-ready master assets.
