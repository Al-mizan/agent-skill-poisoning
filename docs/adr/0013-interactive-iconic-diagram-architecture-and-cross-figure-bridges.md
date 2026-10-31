# 0013. Interactive Iconic Diagram Architecture and Cross-Figure Semantic Bridges

Date: 2026-10-30

## Status

Accepted

## Context

The research poster presentation for *Cross-Lingual Agent Skill Poisoning: Active Runtime Exploitation and Deterministic Authorization in Tool-Using LLM Agents* features three core figures:
- **Figure 1**: Threat Model · Exploit Progression & Seam Interception
- **Figure 2**: Methodology & Authorization Scheme · Deterministic Authorization Seam Architecture
- **Figure 3**: Key Results · Attack Success Rate (ASR) Comparison Chart across defense tiers and linguistic registers

Prior iterations established 16:9 canvas scaling and base typography. However, visual evaluation revealed four design challenges:
1. **Redundancy & Blurred Boundary**: Both Figure 1 and Figure 2 illustrated the Reasoning Plane and Policy Seam with overlapping components, reducing conceptual distinctness.
2. **Text-Heavy Cards**: Critical defense mechanisms (Capability Tokens, Canonical Path Normalization, Sandbox Confinement) relied on textual bullet points rather than immediate visual schematics.
3. **Disjointed Cross-Figure Narrative**: While Figures 1, 2, and 3 represent sequential stages of the scientific narrative (Macro Threat Lifecycle $\to$ Micro Seam Kernel $\to$ Empirical Proof), they lacked explicit visual flow conduits and cross-figure reference anchors.
4. **Static Presentation Constraints**: The poster diagrams were static PNG images, missing opportunities for interactive exploration in the web viewer (`research_poster.html`).

## Decision

1. **Clear Macro vs. Micro Architectural Separation**:
   - **Figure 1 (Macro Threat Pipeline)**: Focuses exclusively on the five-stage end-to-end exploit lifecycle (Authoring $\to$ Marketplace Evasion $\to$ Agent Ingestion $\to$ Rug-Pull Update $\to$ Runtime Reasoning & Seam Interception). Includes a dedicated cross-figure bridge badge (`[🔍 Micro-Kernel Architecture ➔ See Figure 2]`).
   - **Figure 2 (Micro Seam Deep-Dive)**: Focuses strictly on the inner workings of the Deterministic Policy Enforcement Seam: Pre-Dispatch Candidate Proposal, the Three Mandatory Invariants, and Container Sandbox Execution vs. Deterministic Denial.

2. **Self-Describing Visual Micro-Schematics (Zero Bullets)**:
   - Replace textual bullet lists with publication-grade SVG schematics:
     - *Capability Token Gate*: Visual session key glyph, cryptographic token badge (`sess_4a91`), and explicit scope whitelist chip (`scope: tool_read`).
     - *Canonical Path Normalization*: Directory tree schematic showing traversal attempts (`../../.ssh/id_rsa`) clamped and terminated at the `/workspace/sandbox/` boundary with a red barrier mark.
     - *Sandbox Confinement & Egress Gateway*: Isolated container enclosure schematic with an egress firewall illustrating external WAN/LAN blocked ($\times$) while foundation model API outbound traffic is permitted ($\checkmark$).

3. **Explicit Cross-Figure Semantic Conduits**:
   - Establish unbroken visual narrative bridges connecting Tier 2 and Tier 3:
     - *Figure 1 $\to$ Figure 2*: Teal bridge conduit linking Stage 5 (*Candidate Dispatch*) directly to Figure 2's pre-dispatch hook.
     - *Figure 2 $\to$ Figure 3*: Red denial conduit carrying an empirical verification badge (`[📊 Empirically Proven: 0.0% ASR ➔ See Figure 3 Chart]`).
   - Enforce unified color coding: Orange (*Untrusted Attack / Data Plane*), Navy (*Candidate Proposal / Control Plane*), Teal (*Deterministic Seam Invariants*), Green (*Authorized Worker Sandbox*), and Red (*Deterministic Denial*).

4. **Dual-Mode Interactive & 300 DPI Architecture**:
   - **Web Viewer (`research_poster.html` / `research_poster_print.html`)**: Render diagrams as rich vector SVGs featuring CSS animated pulse conduits, hover state transitions, and an interactive trace toggle (`All Stages / Attack Flow / Benign Flow`) for live presentation.
   - **Master Print Asset (`research_poster_27x36_300dpi.png` / PDF)**: Compile vector assets with fine-tuned drop shadows, subtle gradients, and high-contrast chips to produce crisp 300 DPI conference prints.

## Consequences

- The conceptual journey from threat delivery to enforcement mechanics to empirical validation becomes intuitive and self-evident without requiring dense text reading.
- Visual schematics eliminate cognitive load for conference viewers standing 4–6 feet away.
- Both physical print deliverables and live browser demonstrations are fully supported.
