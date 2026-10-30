#!/usr/bin/env python3
"""
generate_diagrams_v2.py
Generates robust, iconic, publication-grade technical diagrams
in strict 16:9 aspect ratio (1920x1080).
- Iconic vector emblems embedded in every component (Adversary, Cloud, Agent, Trojan, Brain, Shield, Vault, Firewall)
- Continuous lifecycle flow conduits with directional chevrons, numbered step badges, and cross-phase routing
- Large 28px base body font (titles 30-40px, badges/pills 22-26px)
- 100% SVG vector paths for checkmarks, denial marks, icons, and arrows (zero CairoSVG font glyph issues)
- Calibrated coordinates: generous margins, zero box collisions, zero text clipping
- Exports to both poster/ and poster_v2/
"""

import os
import cairosvg

def generate_threat_lifecycle():
    # Strict 16:9 aspect ratio: 1920 x 1080
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1920 1080" width="1920" height="1080">
  <defs>
    <marker id="arrowOrange" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#ea580c"/>
    </marker>
    <marker id="arrowRed" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#dc2626"/>
    </marker>
    <marker id="arrowGreen" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#16a34a"/>
    </marker>
    <marker id="arrowNavy" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#0f2b5c"/>
    </marker>
    <filter id="shadow" x="-4%" y="-4%" width="108%" height="112%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#0f172a" flood-opacity="0.08"/>
    </filter>
    <style>
      text { font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }
      .main-title { font-size: 40px; font-weight: 900; fill: #0a1e38; letter-spacing: -0.4px; }
      .main-sub { font-size: 24px; font-weight: 500; fill: #475569; }
      .phase-label { font-size: 22px; font-weight: 800; letter-spacing: 0.8px; text-transform: uppercase; }
      .stage-badge { font-size: 21px; font-weight: 800; letter-spacing: 0.8px; text-transform: uppercase; }
      .card-title { font-size: 30px; font-weight: 800; fill: #0f172a; }
      .card-body { font-size: 28px; font-weight: 500; fill: #334155; line-height: 1.48; }
      .pill-text { font-size: 23px; font-weight: 800; }
      .seam-title { font-size: 28px; font-weight: 800; fill: #0f766e; }
      .seam-body { font-size: 27px; font-weight: 600; fill: #115e59; line-height: 1.45; }
      .legend-lbl { font-size: 25px; font-weight: 700; fill: #334155; }
      .conduit-badge { font-size: 14.5px; font-weight: 800; }
    </style>
  </defs>

  <!-- Clean Canvas -->
  <rect width="1920" height="1080" fill="#ffffff"/>

  <!-- Top Title Bar -->
  <text x="960" y="46" text-anchor="middle" class="main-title">Cross-Lingual Threat Progression &amp; Seam Interception</text>
  <text x="960" y="82" text-anchor="middle" class="main-sub">End-to-End Exploit Lifecycle: Supply-Chain Evasion  —  Runtime Reasoning  —  Deterministic Seam Interception</text>

  <!-- Container I: Supply-Chain Delivery (Stages 1-4) -->
  <rect x="35" y="105" width="1850" height="415" rx="14" fill="#fffaf5" stroke="#fed7aa" stroke-width="2.2" stroke-dasharray="8 6"/>
  <rect x="55" y="117" width="530" height="36" rx="7" fill="#ffedd5"/>
  <text x="75" y="142" class="phase-label" fill="#c2410c">Phase I · Supply-Chain Distribution &amp; Evasion</text>

  <!-- STAGE 1: Author Payload (x=55, width=390, ends at 445) -->
  <g filter="url(#shadow)">
    <rect x="55" y="160" width="390" height="338" rx="10" fill="#ffffff" stroke="#ea580c" stroke-width="2.2"/>
    <rect x="55" y="160" width="390" height="8" rx="4" fill="#ea580c"/>
    <!-- Iconic Badge: Adversary Terminal -->
    <g transform="translate(75, 178)">
      <rect width="46" height="46" rx="9" fill="#fff7ed" stroke="#fed7aa" stroke-width="1.5"/>
      <rect x="7" y="10" width="32" height="22" rx="4" fill="#ea580c"/>
      <path d="M12 16l4 4-4 4M20 25h8" fill="none" stroke="#ffffff" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>
    </g>
    <text x="132" y="208" class="stage-badge" fill="#ea580c">Stage 1 · Author</text>
    <text x="75" y="260" class="card-title">1. Author Payload</text>
    <text x="75" y="320" class="card-body">• Poisoned SKILL.md</text>
    <text x="75" y="375" class="card-body">• Non-English prompts</text>
    <rect x="75" y="432" width="350" height="48" rx="8" fill="#fff7ed" stroke="#fed7aa" stroke-width="1.5"/>
    <text x="250" y="464" text-anchor="middle" class="pill-text" fill="#c2410c">Cross-Lingual Injection</text>
  </g>

  <!-- Conduit 1 -> 2 (80px gap: 445 to 525) -->
  <path d="M 445 335 H 525" fill="none" stroke="#ea580c" stroke-width="4" marker-end="url(#arrowOrange)"/>
  <rect x="449" y="285" width="72" height="26" rx="6" fill="#ffffff" stroke="#ea580c" stroke-width="1.4"/>
  <text x="485" y="303" text-anchor="middle" class="conduit-badge" fill="#c2410c">1. Publish</text>

  <!-- STAGE 2: Registry Scan (x=525, width=390, ends at 915) -->
  <g filter="url(#shadow)">
    <rect x="525" y="160" width="390" height="338" rx="10" fill="#ffffff" stroke="#ea580c" stroke-width="2.2"/>
    <rect x="525" y="160" width="390" height="8" rx="4" fill="#ea580c"/>
    <!-- Iconic Badge: Cloud Registry & Scanner -->
    <g transform="translate(545, 178)">
      <rect width="46" height="46" rx="9" fill="#fff7ed" stroke="#fed7aa" stroke-width="1.5"/>
      <path d="M13 30a6 6 0 0 1 0-12 8 8 0 0 1 15-3 7 7 0 0 1 6 9 5 5 0 0 1-3 6z" fill="#ea580c" opacity="0.85"/>
      <path d="M20 26l3 3 7-7" fill="none" stroke="#ffffff" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>
    </g>
    <text x="602" y="208" class="stage-badge" fill="#ea580c">Stage 2 · Marketplace</text>
    <text x="545" y="260" class="card-title">2. Registry Scan</text>
    <text x="545" y="320" class="card-body">• Public hub publishing</text>
    <text x="545" y="375" class="card-body">• English regex evasion</text>
    <rect x="545" y="432" width="350" height="48" rx="8" fill="#fff7ed" stroke="#fed7aa" stroke-width="1.5"/>
    <text x="720" y="464" text-anchor="middle" class="pill-text" fill="#c2410c">100% Vetting Bypass</text>
  </g>

  <!-- Conduit 2 -> 3 (80px gap: 915 to 995) -->
  <path d="M 915 335 H 995" fill="none" stroke="#ea580c" stroke-width="4" marker-end="url(#arrowOrange)"/>
  <rect x="922" y="285" width="66" height="26" rx="6" fill="#ffffff" stroke="#ea580c" stroke-width="1.4"/>
  <text x="955" y="303" text-anchor="middle" class="conduit-badge" fill="#c2410c">2. Ingest</text>

  <!-- STAGE 3: Agent Install (x=995, width=390, ends at 1385) -->
  <g filter="url(#shadow)">
    <rect x="995" y="160" width="390" height="338" rx="10" fill="#ffffff" stroke="#ea580c" stroke-width="2.2"/>
    <rect x="995" y="160" width="390" height="8" rx="4" fill="#ea580c"/>
    <!-- Iconic Badge: AI Agent Ingestion -->
    <g transform="translate(1015, 178)">
      <rect width="46" height="46" rx="9" fill="#fff7ed" stroke="#fed7aa" stroke-width="1.5"/>
      <rect x="10" y="13" width="26" height="20" rx="4" fill="#ea580c"/>
      <circle cx="17" cy="21" r="2.2" fill="#ffffff"/>
      <circle cx="29" cy="21" r="2.2" fill="#ffffff"/>
      <line x1="23" y1="8" x2="23" y2="13" stroke="#ea580c" stroke-width="2.2" stroke-linecap="round"/>
      <circle cx="23" cy="7" r="2" fill="#ea580c"/>
    </g>
    <text x="1072" y="208" class="stage-badge" fill="#ea580c">Stage 3 · Agent Host</text>
    <text x="1015" y="260" class="card-title">3. Agent Install</text>
    <text x="1015" y="320" class="card-body">• Ingested into agent</text>
    <text x="1015" y="375" class="card-body">• Ambient privilege abuse</text>
    <rect x="1015" y="432" width="350" height="48" rx="8" fill="#fff7ed" stroke="#fed7aa" stroke-width="1.5"/>
    <text x="1190" y="464" text-anchor="middle" class="pill-text" fill="#c2410c">Ambient Host Access</text>
  </g>

  <!-- Conduit 3 -> 4 (80px gap: 1385 to 1465) -->
  <path d="M 1385 335 H 1465" fill="none" stroke="#ea580c" stroke-width="4" marker-end="url(#arrowOrange)"/>
  <rect x="1391" y="285" width="68" height="26" rx="6" fill="#ffffff" stroke="#ea580c" stroke-width="1.4"/>
  <text x="1425" y="303" text-anchor="middle" class="conduit-badge" fill="#c2410c">3. Mutate</text>

  <!-- STAGE 4: Rug-Pull Update (x=1465, width=400, ends at 1865) -->
  <g filter="url(#shadow)">
    <rect x="1465" y="160" width="400" height="338" rx="10" fill="#ffffff" stroke="#c2410c" stroke-width="2.4"/>
    <rect x="1465" y="160" width="400" height="8" rx="4" fill="#c2410c"/>
    <!-- Iconic Badge: Trojan Switch / Mutation -->
    <g transform="translate(1485, 178)">
      <rect width="46" height="46" rx="9" fill="#fff7ed" stroke="#fed7aa" stroke-width="1.5"/>
      <path d="M26 8L15 25h9l-2 15 13-19H24z" fill="#c2410c"/>
    </g>
    <text x="1542" y="208" class="stage-badge" fill="#c2410c">Stage 4 · Rug-Pull</text>
    <text x="1485" y="260" class="card-title">4. Rug-Pull Update</text>
    <text x="1485" y="320" class="card-body">• Clean v1 passes scan</text>
    <text x="1485" y="375" class="card-body">• Mutated v2 deploys</text>
    <rect x="1485" y="432" width="360" height="48" rx="8" fill="#fff7ed" stroke="#fed7aa" stroke-width="1.5"/>
    <text x="1665" y="464" text-anchor="middle" class="pill-text" fill="#c2410c">Post-Install Exploit</text>
  </g>

  <!-- ══════════════════════════════════════════════════════════════════════
       CONTINUOUS LIFECYCLE FLOW CONDUIT: PHASE I -> PHASE II
       ══════════════════════════════════════════════════════════════════════ -->
  <path d="M 1665 498 V 535 H 265 V 604" fill="none" stroke="#ea580c" stroke-width="3.5" stroke-dasharray="8 5" marker-end="url(#arrowNavy)"/>
  <rect x="680" y="520" width="560" height="30" rx="7" fill="#ffffff" stroke="#ea580c" stroke-width="1.6"/>
  <text x="960" y="541" text-anchor="middle" font-size="16" font-weight="900" fill="#c2410c">4. Covert Activation: Mutated Manifest Ingested into Runtime Context</text>

  <!-- Container II: Runtime Planning, Dispatch & Seam Interception -->
  <rect x="35" y="555" width="1850" height="460" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2.2"/>
  <rect x="55" y="567" width="670" height="36" rx="7" fill="#e2e8f0"/>
  <text x="75" y="592" class="phase-label" fill="#0f2b5c">Phase II · Runtime Execution &amp; Deterministic Boundary Interception</text>

  <!-- Step 1: Reasoning Plane (x=55, width=420, ends at 475) -->
  <g filter="url(#shadow)">
    <rect x="55" y="612" width="420" height="385" rx="10" fill="#ffffff" stroke="#3b82f6" stroke-width="2.4"/>
    <rect x="55" y="612" width="420" height="8" rx="4" fill="#2563eb"/>
    <!-- Iconic Badge: Neural Planner -->
    <g transform="translate(75, 630)">
      <rect width="46" height="46" rx="9" fill="#eff6ff" stroke="#bfdbfe" stroke-width="1.5"/>
      <rect x="11" y="11" width="24" height="24" rx="4" fill="#2563eb"/>
      <circle cx="17" cy="17" r="2" fill="#ffffff"/>
      <circle cx="29" cy="17" r="2" fill="#ffffff"/>
      <circle cx="23" cy="27" r="2.5" fill="#ffffff"/>
      <path d="M17 17l6 10 6-10" fill="none" stroke="#ffffff" stroke-width="1.5"/>
    </g>
    <text x="132" y="660" class="stage-badge" fill="#2563eb">Step 1 · Planner Engine</text>
    <text x="75" y="710" class="card-title">Reasoning Plane</text>
    <text x="75" y="770" class="card-body">• Poisoned skill prompt</text>
    <text x="75" y="825" class="card-body">• Unauthorized tool call</text>
    <rect x="75" y="925" width="380" height="50" rx="8" fill="#eff6ff" stroke="#bfdbfe" stroke-width="1.5"/>
    <text x="265" y="958" text-anchor="middle" class="pill-text" fill="#1d4ed8">Compromised Proposal</text>
  </g>

  <!-- Conduit Step 1 -> Seam (105px gap: 475 to 580) -->
  <path d="M 475 805 H 580" fill="none" stroke="#0f2b5c" stroke-width="4" marker-end="url(#arrowNavy)"/>
  <rect x="484" y="765" width="86" height="28" rx="6" fill="#ffffff" stroke="#0f2b5c" stroke-width="1.6"/>
  <text x="527" y="785" text-anchor="middle" font-size="14" font-weight="900" fill="#0f2b5c">5. dispatch()</text>

  <!-- Step 2: Policy Enforcement Seam (Security Fortress) -->
  <g filter="url(#shadow)">
    <rect x="580" y="612" width="645" height="385" rx="10" fill="#ffffff" stroke="#0d9488" stroke-width="2.8"/>
    <rect x="580" y="612" width="645" height="8" rx="4" fill="#0f766e"/>
    <!-- Iconic Badge: Fortress Security Shield -->
    <g transform="translate(600, 630)">
      <rect width="46" height="46" rx="9" fill="#f0fdfa" stroke="#99f6e4" stroke-width="1.5"/>
      <path d="M23 9L35 14v10c0 8-5 15-12 18-7-3-12-10-12-18V14z" fill="#0d9488"/>
      <path d="M23 18a3 3 0 0 0-3 3v2h6v-2a3 3 0 0 0-3-3z" fill="#ffffff"/>
      <rect x="18" y="23" width="10" height="8" rx="1.5" fill="#ffffff"/>
    </g>
    <text x="657" y="660" class="stage-badge" fill="#0d9488">Deterministic Seam</text>
    <text x="600" y="710" class="card-title">Policy Enforcement Seam</text>
    <text x="600" y="744" font-size="24" font-weight="700" fill="#0f766e">Pre-Execution Invariant Verification Gate:</text>

    <!-- Invariant Checklist Box -->
    <rect x="600" y="756" width="605" height="155" rx="8" fill="#f0fdfa" stroke="#99f6e4" stroke-width="1.6"/>

    <g transform="translate(620, 792)">
      <circle cx="12" cy="-6" r="11" fill="#0d9488"/>
      <path d="M 7 -6 L 11 -2 L 17 -10" fill="none" stroke="#ffffff" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>
      <text x="34" y="2" class="seam-body">Capability Token Validation</text>
    </g>

    <g transform="translate(620, 838)">
      <circle cx="12" cy="-6" r="11" fill="#0d9488"/>
      <path d="M 7 -6 L 11 -2 L 17 -10" fill="none" stroke="#ffffff" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>
      <text x="34" y="2" class="seam-body">Canonical Path Normalization</text>
    </g>

    <g transform="translate(620, 884)">
      <circle cx="12" cy="-6" r="11" fill="#0d9488"/>
      <path d="M 7 -6 L 11 -2 L 17 -10" fill="none" stroke="#ffffff" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>
      <text x="34" y="2" class="seam-body">Workspace Sandbox Boundary</text>
    </g>

    <rect x="600" y="925" width="605" height="50" rx="8" fill="#ccfbf1" stroke="#5eead4" stroke-width="1.5"/>
    <text x="902" y="958" text-anchor="middle" class="pill-text" fill="#0f766e">0.037 ms Overhead · Zero False Denials</text>
  </g>

  <!-- Branch Conduits to Outcomes (95px gap: 1225 to 1320) -->
  <path d="M 1225 705 H 1320" fill="none" stroke="#16a34a" stroke-width="4" marker-end="url(#arrowGreen)"/>
  <rect x="1232" y="670" width="86" height="28" rx="6" fill="#ffffff" stroke="#16a34a" stroke-width="1.6"/>
  <text x="1275" y="690" text-anchor="middle" font-size="13" font-weight="900" fill="#16a34a">VALID · PASS</text>

  <path d="M 1225 905 H 1320" fill="none" stroke="#dc2626" stroke-width="4" marker-end="url(#arrowRed)"/>
  <rect x="1230" y="870" width="88" height="28" rx="6" fill="#ffffff" stroke="#dc2626" stroke-width="1.6"/>
  <text x="1274" y="890" text-anchor="middle" font-size="13" font-weight="900" fill="#dc2626">BLOCK · DENY</text>

  <!-- Outcome A: Sandboxed Execution -->
  <g filter="url(#shadow)">
    <rect x="1320" y="612" width="545" height="185" rx="10" fill="#ffffff" stroke="#16a34a" stroke-width="2.4"/>
    <rect x="1320" y="612" width="545" height="8" rx="4" fill="#15803d"/>
    <!-- Iconic Badge: Green Vault -->
    <g transform="translate(1340, 628)">
      <rect width="44" height="44" rx="9" fill="#f0fdf4" stroke="#86efac" stroke-width="1.5"/>
      <rect x="9" y="9" width="26" height="26" rx="4" fill="#16a34a"/>
      <path d="M15 22l4 4 10-10" fill="none" stroke="#ffffff" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>
    </g>
    <text x="1395" y="654" class="stage-badge" fill="#16a34a">Outcome A · Authorized</text>
    <text x="1340" y="700" class="card-title">Sandboxed Execution</text>
    <g transform="translate(1340, 735)">
      <circle cx="10" cy="-6" r="9" fill="#16a34a"/>
      <path d="M 6 -6 L 9 -3 L 14 -9" fill="none" stroke="#ffffff" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>
      <text x="26" y="2" class="card-body">Worker sandbox isolation</text>
    </g>
    <rect x="1340" y="746" width="505" height="40" rx="7" fill="#dcfce7" stroke="#86efac" stroke-width="1.5"/>
    <text x="1592" y="773" text-anchor="middle" class="pill-text" fill="#15803d">100% Benign Utility (0% FDR)</text>
  </g>

  <!-- Outcome B: Deterministic Denial -->
  <g filter="url(#shadow)">
    <rect x="1320" y="812" width="545" height="185" rx="10" fill="#ffffff" stroke="#dc2626" stroke-width="2.4"/>
    <rect x="1320" y="812" width="545" height="8" rx="4" fill="#b91c1c"/>
    <!-- Iconic Badge: Red Firewall Barrier -->
    <g transform="translate(1340, 828)">
      <rect width="44" height="44" rx="9" fill="#fef2f2" stroke="#fca5a5" stroke-width="1.5"/>
      <circle cx="22" cy="22" r="14" fill="#dc2626"/>
      <path d="M15 15l14 14M29 15L15 29" fill="none" stroke="#ffffff" stroke-width="2.8" stroke-linecap="round"/>
    </g>
    <text x="1395" y="854" class="stage-badge" fill="#dc2626">Outcome B · Attack Blocked</text>
    <text x="1340" y="900" class="card-title">Deterministic Denial</text>
    <g transform="translate(1340, 935)">
      <circle cx="10" cy="-6" r="9" fill="#dc2626"/>
      <path d="M 6 -10 L 14 -2 M 14 -10 L 6 -2" fill="none" stroke="#ffffff" stroke-width="2.2" stroke-linecap="round"/>
      <text x="26" y="2" class="card-body">Hostile call intercepted</text>
    </g>
    <rect x="1340" y="946" width="505" height="40" rx="7" fill="#fee2e2" stroke="#fca5a5" stroke-width="1.5"/>
    <text x="1592" y="973" text-anchor="middle" class="pill-text" fill="#b91c1c">ASR: 0.0% (Bangla &amp; Banglish)</text>
  </g>

  <!-- Bottom Legend Bar -->
  <g transform="translate(60, 1052)">
    <circle cx="15" cy="10" r="10" fill="#ea580c"/>
    <text x="36" y="19" class="legend-lbl">Untrusted Attack Flow</text>

    <circle cx="390" cy="10" r="10" fill="#0f2b5c"/>
    <text x="411" y="19" class="legend-lbl">Candidate Proposal</text>

    <circle cx="720" cy="10" r="10" fill="#0d9488"/>
    <text x="741" y="19" class="legend-lbl">Authorization Seam</text>

    <circle cx="1100" cy="10" r="10" fill="#16a34a"/>
    <text x="1121" y="19" class="legend-lbl">Authorized Pass</text>

    <circle cx="1490" cy="10" r="10" fill="#dc2626"/>
    <text x="1511" y="19" class="legend-lbl">Deterministic Block</text>
  </g>
</svg>"""

    for base_dir in ["poster", "poster_v2"]:
        os.makedirs(base_dir, exist_ok=True)
        out_svg = os.path.join(base_dir, "threat_lifecycle.svg")
        out_png = os.path.join(base_dir, "threat_lifecycle.png")
        out_300 = os.path.join(base_dir, "threat_lifecycle_300dpi.png")
        with open(out_svg, "w", encoding="utf-8") as f:
            f.write(svg)
        cairosvg.svg2png(url=out_svg, write_to=out_png, output_width=1920, output_height=1080)
        cairosvg.svg2png(url=out_svg, write_to=out_300, output_width=3840, output_height=2160)
        print(f"Generated 16:9 Threat Lifecycle: {out_png} & {out_300}")


def generate_defense_seam():
    # Strict 16:9 aspect ratio: 1920 x 1080
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1920 1080" width="1920" height="1080">
  <defs>
    <marker id="arrowNavy" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#0f2b5c"/>
    </marker>
    <marker id="arrowGreen" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#16a34a"/>
    </marker>
    <marker id="arrowRed" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#dc2626"/>
    </marker>
    <filter id="shadow" x="-4%" y="-4%" width="108%" height="112%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#0f172a" flood-opacity="0.08"/>
    </filter>
    <style>
      text { font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }
      .main-title { font-size: 38px; font-weight: 900; fill: #0a1e38; letter-spacing: -0.4px; }
      .main-sub { font-size: 23px; font-weight: 500; fill: #475569; }
      .step-badge { font-size: 21px; font-weight: 800; letter-spacing: 0.8px; text-transform: uppercase; }
      .card-title { font-size: 30px; font-weight: 800; fill: #0f172a; }
      .card-body { font-size: 27px; font-weight: 500; fill: #334155; line-height: 1.48; }
      .pill-text { font-size: 23px; font-weight: 800; }
      .seam-header { font-size: 27px; font-weight: 800; fill: #0f766e; }
      .check-item { font-size: 26px; font-weight: 600; fill: #115e59; line-height: 1.45; }
      .legend-lbl { font-size: 25px; font-weight: 700; fill: #334155; }
      .conduit-label { font-size: 14px; font-weight: 900; }
    </style>
  </defs>

  <!-- Clean Canvas -->
  <rect width="1920" height="1080" fill="#ffffff"/>

  <!-- Top Title Bar -->
  <text x="960" y="46" text-anchor="middle" class="main-title">Deterministic Authorization Seam: Execution Boundary Architecture</text>
  <text x="960" y="80" text-anchor="middle" class="main-sub">In-process pre-execution gateway mediating proposed tool dispatches: capability tokens, invariants, and containment</text>

  <!-- COMPONENT 1: Reasoning Plane (Left, width=410) -->
  <g filter="url(#shadow)">
    <rect x="40" y="105" width="410" height="925" rx="14" fill="#f8fafc" stroke="#3b82f6" stroke-width="2.2"/>
    <rect x="40" y="105" width="410" height="8" rx="4" fill="#2563eb"/>

    <!-- Iconic Badge: Neural Planner -->
    <g transform="translate(65, 126)">
      <rect width="44" height="44" rx="9" fill="#eff6ff" stroke="#bfdbfe" stroke-width="1.5"/>
      <rect x="10" y="10" width="24" height="24" rx="4" fill="#2563eb"/>
      <circle cx="16" cy="16" r="2" fill="#ffffff"/>
      <circle cx="28" cy="16" r="2" fill="#ffffff"/>
      <circle cx="22" cy="26" r="2.5" fill="#ffffff"/>
      <path d="M16 16l6 10 6-10" fill="none" stroke="#ffffff" stroke-width="1.5"/>
    </g>
    <text x="120" y="152" class="step-badge" fill="#2563eb">Component 1 · Probabilistic</text>
    <text x="65" y="196" class="card-title">Reasoning Plane</text>

    <!-- Card 1A: User Intent -->
    <rect x="65" y="218" width="360" height="185" rx="9" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
    <!-- User Icon -->
    <g transform="translate(85, 235)">
      <circle cx="14" cy="10" r="7" fill="#0f2b5c"/>
      <path d="M4 28c0-6 5-10 10-10s10 4 10 10" fill="#0f2b5c"/>
    </g>
    <text x="118" y="254" font-size="26" font-weight="800" fill="#0f2b5c">Authentic Intent</text>
    <text x="85" y="305" class="card-body">User task prompt</text>
    <g transform="translate(85, 360)">
      <circle cx="12" cy="-6" r="10" fill="#16a34a"/>
      <path d="M 7 -6 L 11 -2 L 17 -10" fill="none" stroke="#ffffff" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>
      <text x="32" y="2" font-size="24" font-weight="800" fill="#16a34a">Trusted Control Plane</text>
    </g>

    <!-- Card 1B: Poisoned Skills -->
    <rect x="65" y="420" width="360" height="215" rx="9" fill="#fff7ed" stroke="#fed7aa" stroke-width="1.6"/>
    <!-- Virus/Bug Icon -->
    <g transform="translate(85, 436)">
      <circle cx="12" cy="12" r="8" fill="#c2410c"/>
      <line x1="4" y1="12" x2="20" y2="12" stroke="#ffffff" stroke-width="2"/>
      <line x1="12" y1="4" x2="12" y2="20" stroke="#ffffff" stroke-width="2"/>
    </g>
    <text x="118" y="458" font-size="26" font-weight="800" fill="#c2410c">Poisoned Manifest</text>
    <text x="85" y="510" class="card-body">Untrusted skill input</text>
    <text x="85" y="555" class="card-body">Cross-lingual injection</text>
    <g transform="translate(85, 602)">
      <circle cx="12" cy="-6" r="10" fill="#dc2626"/>
      <path d="M 7 -11 L 17 -1 M 17 -11 L 7 -1" fill="none" stroke="#ffffff" stroke-width="2.4" stroke-linecap="round"/>
      <text x="32" y="2" font-size="24" font-weight="800" fill="#dc2626">Untrusted Data Plane</text>
    </g>

    <!-- Card 1C: LLM Planner Loop -->
    <rect x="65" y="655" width="360" height="275" rx="9" fill="#ffffff" stroke="#bfdbfe" stroke-width="1.6"/>
    <text x="85" y="694" font-size="26" font-weight="800" fill="#1d4ed8">LLM Planner Loop</text>
    <text x="85" y="745" font-size="26" font-weight="600" fill="#334155">• Multi-step reasoning</text>
    <text x="85" y="790" font-size="26" font-weight="600" fill="#334155">• Cannot self-police</text>
    <rect x="85" y="825" width="320" height="60" rx="7" fill="#fef2f2" stroke="#fca5a5" stroke-width="1.2"/>
    <text x="245" y="862" text-anchor="middle" font-size="21" font-weight="800" fill="#dc2626">100% Injection Vulnerable</text>

    <!-- Bottom pill -->
    <rect x="65" y="950" width="360" height="48" rx="8" fill="#eff6ff" stroke="#bfdbfe" stroke-width="1.5"/>
    <text x="245" y="982" text-anchor="middle" class="pill-text" fill="#1d4ed8">Probabilistic Plane</text>
  </g>

  <!-- Conduit Component 1 -> Component 2 (Thick Bus with Data Marker) -->
  <path d="M 450 565 H 498" fill="none" stroke="#0f2b5c" stroke-width="4" marker-end="url(#arrowNavy)"/>

  <!-- COMPONENT 2: Proposed Tool Call (Dispatch Hook, width=324) -->
  <g filter="url(#shadow)">
    <rect x="498" y="210" width="324" height="715" rx="12" fill="#ffffff" stroke="#0f2b5c" stroke-width="2.4"/>
    <rect x="498" y="210" width="324" height="8" rx="4" fill="#0f2b5c"/>

    <!-- Terminal Window Top Bar with macOS dots -->
    <rect x="498" y="218" width="324" height="34" fill="#f1f5f9"/>
    <circle cx="518" cy="235" r="5" fill="#ef4444"/>
    <circle cx="533" cy="235" r="5" fill="#f59e0b"/>
    <circle cx="548" cy="235" r="5" fill="#10b981"/>
    <text x="660" y="240" text-anchor="middle" font-size="13" font-weight="700" fill="#475569">dispatch_hook.py</text>

    <text x="518" y="285" class="step-badge" fill="#0f2b5c">Step 2 · Candidate Call</text>
    <text x="518" y="324" class="card-title">Proposed Call</text>
    <text x="518" y="362" font-size="24" font-weight="600" fill="#475569">Candidate dispatch:</text>

    <!-- Code Block Window -->
    <rect x="514" y="385" width="292" height="460" rx="8" fill="#0f172a"/>
    <text x="530" y="426" font-family="'JetBrains Mono', monospace" font-size="21" font-weight="bold" fill="#38bdf8">dispatch(req, ctx):</text>
    <text x="530" y="474" font-family="'JetBrains Mono', monospace" font-size="19.5" fill="#f8fafc">tool  = "file_write"</text>
    <text x="530" y="522" font-family="'JetBrains Mono', monospace" font-size="19.5" fill="#f8fafc">path  = "../../.ssh"</text>
    <text x="530" y="570" font-family="'JetBrains Mono', monospace" font-size="19.5" fill="#f8fafc">token = "sess_4a91"</text>
    <text x="530" y="640" font-family="'JetBrains Mono', monospace" font-size="18.5" fill="#ea580c"># Seam Mediation:</text>
    <text x="530" y="685" font-family="'JetBrains Mono', monospace" font-size="18.5" fill="#ea580c">• alias: file_path</text>
    <text x="530" y="730" font-family="'JetBrains Mono', monospace" font-size="18.5" fill="#ea580c">• realpath traversal</text>
    <text x="530" y="775" font-family="'JetBrains Mono', monospace" font-size="18.5" fill="#ea580c">• workspace check</text>

    <rect x="514" y="860" width="292" height="48" rx="7" fill="#f1f5f9" stroke="#cbd5e1" stroke-width="1.5"/>
    <text x="660" y="892" text-anchor="middle" class="pill-text" fill="#0f2b5c">Pre-Dispatch Hook</text>
  </g>

  <!-- Conduit Component 2 -> Component 3 (Thick Bus with Mediation Marker) -->
  <path d="M 822 565 H 855" fill="none" stroke="#0f2b5c" stroke-width="4" marker-end="url(#arrowNavy)"/>

  <!-- COMPONENT 3: Deterministic Policy Enforcement Seam (width=570, ends at 1425) -->
  <g filter="url(#shadow)">
    <rect x="855" y="105" width="570" height="925" rx="14" fill="#ffffff" stroke="#0d9488" stroke-width="2.8"/>
    <rect x="855" y="105" width="570" height="8" rx="4" fill="#0f766e"/>

    <!-- Iconic Badge: Fortress Security Shield -->
    <g transform="translate(880, 126)">
      <rect width="44" height="44" rx="9" fill="#f0fdfa" stroke="#99f6e4" stroke-width="1.5"/>
      <path d="M22 8L34 13v10c0 8-5 15-12 18-7-3-12-10-12-18V13z" fill="#0d9488"/>
      <path d="M22 17a3 3 0 0 0-3 3v2h6v-2a3 3 0 0 0-3-3z" fill="#ffffff"/>
      <rect x="17" y="22" width="10" height="8" rx="1.5" fill="#ffffff"/>
    </g>
    <text x="935" y="152" class="step-badge" fill="#0d9488">Component 2 · Trusted Anchor</text>
    <text x="880" y="196" class="card-title">Policy Enforcement Seam</text>
    <text x="880" y="234" font-size="25" font-weight="700" fill="#0f766e">Mandatory Invariant Verification:</text>

    <!-- Invariant 1: Capability Tokens -->
    <rect x="880" y="250" width="520" height="155" rx="8" fill="#f0fdfa" stroke="#99f6e4" stroke-width="1.6"/>
    <!-- Token Key Icon -->
    <g transform="translate(900, 268)">
      <circle cx="10" cy="10" r="7" fill="none" stroke="#0f766e" stroke-width="2.5"/>
      <path d="M15 15l10 10m-4-2l2-2m3 3l2-2" fill="none" stroke="#0f766e" stroke-width="2.2" stroke-linecap="round"/>
    </g>
    <text x="935" y="288" class="seam-header">1. Capability Tokens</text>
    <g transform="translate(900, 345)">
      <circle cx="12" cy="-6" r="10" fill="#0f766e"/>
      <path d="M 7 -6 L 11 -2 L 17 -10" fill="none" stroke="#ffffff" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>
      <text x="32" y="2" class="check-item">Session token verification</text>
    </g>

    <!-- Invariant 2: Path Normalization -->
    <rect x="880" y="420" width="520" height="155" rx="8" fill="#f0fdfa" stroke="#99f6e4" stroke-width="1.6"/>
    <!-- Path Folder Icon -->
    <g transform="translate(900, 438)">
      <path d="M4 6h6l2 2h8a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2z" fill="#0f766e"/>
    </g>
    <text x="935" y="458" class="seam-header">2. Path Normalization</text>
    <g transform="translate(900, 515)">
      <circle cx="12" cy="-6" r="10" fill="#0f766e"/>
      <path d="M 7 -6 L 11 -2 L 17 -10" fill="none" stroke="#ffffff" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>
      <text x="32" y="2" class="check-item">Canonical realpath(..) check</text>
    </g>

    <!-- Invariant 3: Sandbox Confinement -->
    <rect x="880" y="590" width="520" height="155" rx="8" fill="#f0fdfa" stroke="#99f6e4" stroke-width="1.6"/>
    <!-- Sandbox Enclosure Icon -->
    <g transform="translate(900, 608)">
      <rect x="2" y="2" width="22" height="22" rx="4" fill="none" stroke="#0f766e" stroke-width="2.4" stroke-dasharray="4 2"/>
      <circle cx="13" cy="13" r="4" fill="#0f766e"/>
    </g>
    <text x="935" y="628" class="seam-header">3. Sandbox Confinement</text>
    <g transform="translate(900, 685)">
      <circle cx="12" cy="-6" r="10" fill="#0f766e"/>
      <path d="M 7 -6 L 11 -2 L 17 -10" fill="none" stroke="#ffffff" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>
      <text x="32" y="2" class="check-item">Isolated workspace boundary</text>
    </g>

    <!-- Performance Metric Box -->
    <rect x="880" y="762" width="520" height="175" rx="8" fill="#ccfbf1" stroke="#5eead4" stroke-width="1.6"/>
    <text x="900" y="800" font-size="27" font-weight="900" fill="#0f766e">Empirical Guarantees (N = 312)</text>

    <g transform="translate(900, 836)">
      <circle cx="12" cy="-6" r="10" fill="#0f766e"/>
      <path d="M 7 -6 L 11 -2 L 17 -10" fill="none" stroke="#ffffff" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>
      <text x="32" y="2" font-size="26" font-weight="700" fill="#115e59">0.037 ms Overhead (&lt;0.005%)</text>
    </g>

    <g transform="translate(900, 874)">
      <circle cx="12" cy="-6" r="10" fill="#0f766e"/>
      <path d="M 7 -6 L 11 -2 L 17 -10" fill="none" stroke="#ffffff" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>
      <text x="32" y="2" font-size="26" font-weight="700" fill="#115e59">100% Invariant (0.0% ASR in BN)</text>
    </g>

    <g transform="translate(900, 912)">
      <circle cx="12" cy="-6" r="10" fill="#0f766e"/>
      <path d="M 7 -6 L 11 -2 L 17 -10" fill="none" stroke="#ffffff" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>
      <text x="32" y="2" font-size="26" font-weight="700" fill="#115e59">0.0% False Denials (100% Utility)</text>
    </g>

    <rect x="880" y="950" width="520" height="48" rx="8" fill="#f0fdfa" stroke="#99f6e4" stroke-width="1.5"/>
    <text x="1140" y="982" text-anchor="middle" class="pill-text" fill="#0f766e">Deterministic Enforcement</text>
  </g>

  <!-- Branch Conduits to Component 4 (80px gap: 1425 to 1505) -->
  <path d="M 1425 355 H 1505" fill="none" stroke="#16a34a" stroke-width="4" marker-end="url(#arrowGreen)"/>
  <rect x="1438" y="320" width="56" height="26" rx="5" fill="#ffffff" stroke="#16a34a" stroke-width="1.6"/>
  <text x="1466" y="338" text-anchor="middle" font-size="13" font-weight="900" fill="#16a34a">PASS</text>

  <path d="M 1425 785 H 1505" fill="none" stroke="#dc2626" stroke-width="4" marker-end="url(#arrowRed)"/>
  <rect x="1438" y="750" width="56" height="26" rx="5" fill="#ffffff" stroke="#dc2626" stroke-width="1.6"/>
  <text x="1466" y="768" text-anchor="middle" font-size="13" font-weight="900" fill="#dc2626">DENY</text>

  <!-- COMPONENT 4: Execution Outcomes (x=1505 to 1890, width=385) -->
  <!-- 4A: Authorized Execution Container -->
  <g filter="url(#shadow)">
    <rect x="1505" y="150" width="385" height="400" rx="12" fill="#ffffff" stroke="#16a34a" stroke-width="2.2"/>
    <rect x="1505" y="150" width="385" height="8" rx="4" fill="#15803d"/>
    <!-- Iconic Badge: Green Vault -->
    <g transform="translate(1528, 168)">
      <rect width="42" height="42" rx="8" fill="#f0fdf4" stroke="#86efac" stroke-width="1.5"/>
      <rect x="8" y="8" width="26" height="26" rx="4" fill="#16a34a"/>
      <path d="M14 21l4 4 10-10" fill="none" stroke="#ffffff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
    </g>
    <text x="1580" y="194" class="step-badge" fill="#16a34a">Outcome A · Authorized</text>
    <text x="1528" y="240" class="card-title">Sandboxed Execution</text>
    <text x="1528" y="278" font-size="25" font-weight="600" fill="#15803d">Compliant calls execute:</text>

    <rect x="1520" y="298" width="355" height="170" rx="8" fill="#f0fdf4" stroke="#86efac" stroke-width="1.5"/>
    <g transform="translate(1535, 360)">
      <circle cx="10" cy="-6" r="9" fill="#16a34a"/>
      <path d="M 6 -6 L 9 -3 L 14 -9" fill="none" stroke="#ffffff" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>
      <text x="26" y="2" font-size="24" font-weight="700" fill="#15803d">Worker sandbox isolation</text>
    </g>
    <g transform="translate(1535, 420)">
      <circle cx="10" cy="-6" r="9" fill="#16a34a"/>
      <path d="M 6 -6 L 9 -3 L 14 -9" fill="none" stroke="#ffffff" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>
      <text x="26" y="2" font-size="24" font-weight="700" fill="#15803d">Confined task root</text>
    </g>

    <rect x="1520" y="485" width="355" height="46" rx="7" fill="#dcfce7" stroke="#86efac" stroke-width="1.5"/>
    <text x="1697" y="516" text-anchor="middle" class="pill-text" fill="#15803d">100% Benign Success</text>
  </g>

  <!-- 4B: Deterministic Denial -->
  <g filter="url(#shadow)">
    <rect x="1505" y="580" width="385" height="410" rx="12" fill="#ffffff" stroke="#dc2626" stroke-width="2.2"/>
    <rect x="1505" y="580" width="385" height="8" rx="4" fill="#b91c1c"/>
    <!-- Iconic Badge: Red Firewall Barrier -->
    <g transform="translate(1528, 598)">
      <rect width="42" height="42" rx="8" fill="#fef2f2" stroke="#fca5a5" stroke-width="1.5"/>
      <circle cx="21" cy="21" r="13" fill="#dc2626"/>
      <path d="M14 14l14 14M28 14L14 28" fill="none" stroke="#ffffff" stroke-width="2.6" stroke-linecap="round"/>
    </g>
    <text x="1580" y="624" class="step-badge" fill="#dc2626">Outcome B · Intercept</text>
    <text x="1528" y="670" class="card-title">Deterministic Denial</text>
    <text x="1528" y="708" font-size="25" font-weight="600" fill="#b91c1c">Hostile calls intercepted:</text>

    <rect x="1520" y="728" width="355" height="170" rx="8" fill="#fef2f2" stroke="#fca5a5" stroke-width="1.5"/>
    <g transform="translate(1535, 790)">
      <circle cx="10" cy="-6" r="9" fill="#dc2626"/>
      <path d="M 6 -10 L 14 -2 M 14 -10 L 6 -2" fill="none" stroke="#ffffff" stroke-width="2.2" stroke-linecap="round"/>
      <text x="26" y="2" font-size="24" font-weight="700" fill="#b91c1c">Fail-closed call block</text>
    </g>
    <g transform="translate(1535, 850)">
      <circle cx="10" cy="-6" r="9" fill="#dc2626"/>
      <path d="M 6 -10 L 14 -2 M 14 -10 L 6 -2" fill="none" stroke="#ffffff" stroke-width="2.2" stroke-linecap="round"/>
      <text x="26" y="2" font-size="24" font-weight="700" fill="#b91c1c">Zero host secret access</text>
    </g>

    <rect x="1520" y="915" width="355" height="46" rx="7" fill="#fee2e2" stroke="#fca5a5" stroke-width="1.5"/>
    <text x="1697" y="946" text-anchor="middle" class="pill-text" fill="#b91c1c">ASR: 0.0% (BN &amp; BN-EN)</text>
  </g>

  <!-- Bottom Legend Bar -->
  <g transform="translate(45, 1052)">
    <circle cx="15" cy="10" r="10" fill="#2563eb"/>
    <text x="34" y="19" class="legend-lbl">Reasoning Plane</text>

    <circle cx="310" cy="10" r="10" fill="#0f2b5c"/>
    <text x="329" y="19" class="legend-lbl">Candidate Proposal</text>

    <circle cx="700" cy="10" r="10" fill="#0d9488"/>
    <text x="719" y="19" class="legend-lbl">Authorization Seam</text>

    <circle cx="1180" cy="10" r="10" fill="#16a34a"/>
    <text x="1199" y="19" class="legend-lbl">Authorized Pass</text>

    <circle cx="1560" cy="10" r="10" fill="#dc2626"/>
    <text x="1579" y="19" class="legend-lbl">Deterministic Block</text>
  </g>
</svg>"""

    for base_dir in ["poster", "poster_v2"]:
        os.makedirs(base_dir, exist_ok=True)
        out_svg = os.path.join(base_dir, "defense_seam_architecture.svg")
        out_png = os.path.join(base_dir, "defense_seam_architecture.png")
        out_300 = os.path.join(base_dir, "defense_seam_architecture_300dpi.png")
        with open(out_svg, "w", encoding="utf-8") as f:
            f.write(svg)
        cairosvg.svg2png(url=out_svg, write_to=out_png, output_width=1920, output_height=1080)
        cairosvg.svg2png(url=out_svg, write_to=out_300, output_width=3840, output_height=2160)
        print(f"Generated 16:9 Defense Seam: {out_png} & {out_300}")

if __name__ == "__main__":
    generate_threat_lifecycle()
    generate_defense_seam()
