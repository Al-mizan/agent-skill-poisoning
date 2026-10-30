# Row-Wise Narrative Tier Architecture for Research Presentation Poster

## Context

Research posters with portrait dimensions (27" × 36") frequently employ a 3-column vertical layout. While common, vertical column layouts on tall presentation formats introduce cognitive fatigue and physical dislocation: conference attendees must scan down Column 1 to the floor, return to the top for Column 2, and repeat for Column 3. Furthermore, related conceptual phases—such as the attack lifecycle and corresponding defense seam—become visually disjointed across column boundaries.

## Decision

We restructure the 27" × 36" research poster into four distinct horizontal narrative tiers (Rows 1–4):
1. **Tier 1 (Foundations & Research Scope):** Three side-by-side modular panels presenting *1. Motivation*, *2. Contributions & Research Questions* (ultra-concise cards), and *3. Threat Model*.
2. **Tier 2 (Architectural Core & Mechanisms):** Two symmetric side-by-side centerpiece figures presenting *Threat Model: Exploit Progression (Figure 1)* and *4. Methodology & Authorization Seam (Figure 2)*.
3. **Tier 3 (Empirical Validation & Impact):** Two side-by-side panels presenting *5. Key Results (Figure 3 & Pivoted Table)* alongside *6. Security Impact*.
4. **Tier 4 (Synthesis & Governance):** A full-width academic card banner covering *7. Conclusion & Future Work*.

## Consequences

- Readers navigate the poster intuitively from top to bottom, scanning left-to-right at each narrative milestone.
- The attack lifecycle and the deterministic defense architecture are positioned directly adjacent in Tier 2, establishing a direct visual contrast between exploit mechanics and policy seam mediation.
- Empirical results and strategic security directives share Tier 3, allowing quantitative evaluation to immediately substantiate security conclusions.
