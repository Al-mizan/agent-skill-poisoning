#!/usr/bin/env python3
"""
generate_diagrams.py
Generates publication-grade, low-text-density technical diagrams for the research poster.
- Diagram 1: threat_lifecycle (Figure 1: Five-Stage Threat Progression & Seam Interception)
- Diagram 2: defense_seam_architecture (Figure 2: Deterministic Authorization Seam Architecture)
Features:
- High visual impact: Custom vector icons, structural pipeline flow, badges, and chips
- Low text density: Replaces paragraphs with crisp architectural labels and key metrics
- Strict boundary control: Zero text clipping, ample padding, guaranteed container bounds
- Color palette: Deep Navy (#0a1e38), Accent Blue (#2563eb), Alert Red (#dc2626),
  Success Green (#16a34a), Invariant Teal (#0d9488), Amber (#ea580c)
"""

import os
import cairosvg

def generate_threat_lifecycle(out_svg_path, out_png_path):
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1920 1440" width="1920" height="1440">
  <defs>
    <!-- Arrow Markers -->
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

    <!-- Drop Shadows -->
    <filter id="cardShadow" x="-5%" y="-5%" width="110%" height="115%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#0f172a" flood-opacity="0.08"/>
    </filter>
    <filter id="glowTeal" x="-8%" y="-8%" width="116%" height="116%">
      <feDropShadow dx="0" dy="0" stdDeviation="8" flood-color="#0d9488" flood-opacity="0.25"/>
    </filter>

    <style>
      text { font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }
      .diagram-title { font-size: 44px; font-weight: 900; fill: #0a1e38; letter-spacing: -0.5px; }
      .diagram-subtitle { font-size: 23px; font-weight: 600; fill: #475569; }
      .phase-tag { font-size: 19px; font-weight: 800; letter-spacing: 0.5px; }
      .step-num { font-size: 16px; font-weight: 800; letter-spacing: 0.5px; }
      .card-head { font-size: 28px; font-weight: 800; fill: #0f172a; }
      .card-sub { font-size: 20px; font-weight: 600; fill: #475569; }
      .mono-chip { font-family: 'JetBrains Mono', monospace; font-size: 19px; font-weight: 700; }
      .status-pill { font-size: 17.5px; font-weight: 800; }
      .legend-text { font-size: 19px; font-weight: 700; fill: #334155; }
    </style>
  </defs>

  <!-- Clean Canvas Background -->
  <rect width="1920" height="1440" fill="#ffffff"/>

  <!-- ========================================================
       TOP HEADER TITLE BAR
       ======================================================== -->
  <g transform="translate(60, 48)">
    <rect x="0" y="0" width="8" height="52" rx="4" fill="#2563eb"/>
    <text x="24" y="38" class="diagram-title">Cross-Lingual Threat Progression &amp; Seam Interception</text>
    <text x="24" y="74" class="diagram-subtitle">Five-Stage Supply-Chain Exploit Lifecycle and Deterministic In-Process Mediation</text>
  </g>

  <!-- ========================================================
       PHASE I: SUPPLY-CHAIN DELIVERY (STAGES 1-4)
       ======================================================== -->
  <rect x="40" y="145" width="1840" height="490" rx="16" fill="#fffbf5" stroke="#fed7aa" stroke-width="2.5"/>
  <rect x="65" y="165" width="580" height="38" rx="8" fill="#ffedd5"/>
  <text x="82" y="191" class="phase-tag" fill="#c2410c">Phase I: Supply-Chain Ingestion &amp; Rug-Pull (Stages 1–4)</text>

  <!-- STAGE 1: Author Payload -->
  <g filter="url(#cardShadow)">
    <rect x="65" y="220" width="410" height="390" rx="14" fill="#ffffff" stroke="#ea580c" stroke-width="2.2"/>
    <rect x="65" y="220" width="410" height="8" rx="4" fill="#ea580c"/>
    
    <!-- Stage Header -->
    <rect x="85" y="246" width="100" height="30" rx="6" fill="#fff7ed"/>
    <text x="135" y="267" text-anchor="middle" class="step-num" fill="#c2410c">Stage 1</text>
    <text x="85" y="308" class="card-head">Author Payload</text>
    <text x="85" y="336" class="card-sub">Adversarial Skill Crafting</text>

    <!-- Visual Icon: Attacker & Code Manifest -->
    <g transform="translate(145, 360)">
      <rect x="0" y="0" width="130" height="135" rx="10" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>
      <path d="M 0 0 L 95 0 L 130 35 L 130 135 L 0 135 Z" fill="#f1f5f9"/>
      <path d="M 95 0 L 95 35 L 130 35 Z" fill="#cbd5e1"/>
      <rect x="20" y="45" width="90" height="8" rx="3" fill="#ea580c"/>
      <rect x="20" y="62" width="70" height="7" rx="3" fill="#94a3b8"/>
      <rect x="20" y="78" width="80" height="7" rx="3" fill="#94a3b8"/>
      <rect x="20" y="94" width="55" height="7" rx="3" fill="#dc2626"/>

      <circle cx="115" cy="115" r="22" fill="#fef2f2" stroke="#dc2626" stroke-width="2"/>
      <path d="M 115 104 L 115 116 M 115 122 L 115 125" stroke="#dc2626" stroke-width="3" stroke-linecap="round"/>
    </g>

    <!-- Language Register Chips -->
    <g transform="translate(85, 515)">
      <rect x="0" y="0" width="72" height="30" rx="6" fill="#eff6ff" stroke="#bfdbfe" stroke-width="1.2"/>
      <text x="36" y="21" text-anchor="middle" class="mono-chip" fill="#1e40af">EN</text>

      <rect x="82" y="0" width="72" height="30" rx="6" fill="#fffbeb" stroke="#fde68a" stroke-width="1.2"/>
      <text x="118" y="21" text-anchor="middle" class="mono-chip" fill="#b45309">BN</text>

      <rect x="164" y="0" width="105" height="30" rx="6" fill="#f0fdf4" stroke="#86efac" stroke-width="1.2"/>
      <text x="216" y="21" text-anchor="middle" class="mono-chip" fill="#15803d">BN-EN</text>
    </g>

    <!-- Bottom Status Pill -->
    <rect x="85" y="560" width="370" height="38" rx="8" fill="#fff7ed" stroke="#fed7aa" stroke-width="1.5"/>
    <text x="270" y="585" text-anchor="middle" class="status-pill" fill="#c2410c">Poisoned SKILL.md Manifest</text>
  </g>

  <!-- Arrow 1 -> 2 -->
  <path d="M 475 415 H 515" fill="none" stroke="#ea580c" stroke-width="4.5" marker-end="url(#arrowOrange)"/>

  <!-- STAGE 2: Registry Vetting Bypass -->
  <g filter="url(#cardShadow)">
    <rect x="525" y="220" width="410" height="390" rx="14" fill="#ffffff" stroke="#ea580c" stroke-width="2.2"/>
    <rect x="525" y="220" width="410" height="8" rx="4" fill="#ea580c"/>
    
    <!-- Stage Header -->
    <rect x="545" y="246" width="100" height="30" rx="6" fill="#fff7ed"/>
    <text x="595" y="267" text-anchor="middle" class="step-num" fill="#c2410c">Stage 2</text>
    <text x="545" y="308" class="card-head">Registry Scan</text>
    <text x="545" y="336" class="card-sub">Static Vetting Scanner</text>

    <!-- Visual Icon: Registry Cloud & Scanner Filter Funnel -->
    <g transform="translate(605, 360)">
      <rect x="0" y="0" width="140" height="70" rx="8" fill="#f1f5f9" stroke="#cbd5e1" stroke-width="2"/>
      <circle cx="20" cy="22" r="5" fill="#16a34a"/>
      <circle cx="36" cy="22" r="5" fill="#3b82f6"/>
      <rect x="55" y="18" width="70" height="8" rx="3" fill="#cbd5e1"/>
      <circle cx="20" cy="48" r="5" fill="#16a34a"/>
      <circle cx="36" cy="48" r="5" fill="#3b82f6"/>
      <rect x="55" y="44" width="70" height="8" rx="3" fill="#cbd5e1"/>

      <path d="M 170 10 L 220 10 L 205 45 L 205 65 L 185 65 L 185 45 Z" fill="#e2e8f0" stroke="#94a3b8" stroke-width="1.8"/>
      <text x="195" y="30" text-anchor="middle" font-size="12" font-weight="900" fill="#64748b">SCAN</text>

      <g transform="translate(0, 85)">
        <rect x="0" y="0" width="115" height="32" rx="6" fill="#fef2f2" stroke="#fca5a5" stroke-width="1.2"/>
        <text x="57" y="21" text-anchor="middle" font-size="15" font-weight="800" fill="#dc2626">EN: Filtered</text>

        <rect x="125" y="0" width="125" height="32" rx="6" fill="#f0fdf4" stroke="#86efac" stroke-width="1.2"/>
        <text x="187" y="21" text-anchor="middle" font-size="15" font-weight="800" fill="#16a34a">BN: BYPASSED</text>
      </g>
    </g>

    <!-- Bottom Status Pill -->
    <rect x="545" y="560" width="370" height="38" rx="8" fill="#fef2f2" stroke="#fca5a5" stroke-width="1.5"/>
    <text x="730" y="585" text-anchor="middle" class="status-pill" fill="#dc2626">100% Vetting Bypass Rate (VBR)</text>
  </g>

  <!-- Arrow 2 -> 3 -->
  <path d="M 935 415 H 975" fill="none" stroke="#ea580c" stroke-width="4.5" marker-end="url(#arrowOrange)"/>

  <!-- STAGE 3: Agent Ingestion -->
  <g filter="url(#cardShadow)">
    <rect x="985" y="220" width="410" height="390" rx="14" fill="#ffffff" stroke="#ea580c" stroke-width="2.2"/>
    <rect x="985" y="220" width="410" height="8" rx="4" fill="#ea580c"/>
    
    <!-- Stage Header -->
    <rect x="1005" y="246" width="100" height="30" rx="6" fill="#fff7ed"/>
    <text x="1055" y="267" text-anchor="middle" class="step-num" fill="#c2410c">Stage 3</text>
    <text x="1005" y="308" class="card-head">Agent Ingestion</text>
    <text x="1005" y="336" class="card-sub">Dynamic Manifest Loading</text>

    <!-- Visual Icon: Agent & Host Resources -->
    <g transform="translate(1085, 360)">
      <rect x="10" y="10" width="90" height="75" rx="16" fill="#eff6ff" stroke="#3b82f6" stroke-width="2.5"/>
      <circle cx="35" cy="42" r="9" fill="#2563eb"/>
      <circle cx="75" cy="42" r="9" fill="#2563eb"/>
      <rect x="35" y="62" width="40" height="6" rx="3" fill="#2563eb"/>
      <path d="M 55 10 L 55 0" stroke="#3b82f6" stroke-width="3" stroke-linecap="round"/>
      <circle cx="55" cy="0" r="4" fill="#3b82f6"/>

      <g transform="translate(125, 20)">
        <rect x="0" y="25" width="60" height="50" rx="6" fill="#fff7ed" stroke="#ea580c" stroke-width="2"/>
        <path d="M 12 25 L 12 12 C 12 2 48 2 48 12 L 48 25" fill="none" stroke="#ea580c" stroke-width="3.5"/>
        <circle cx="30" cy="50" r="5" fill="#ea580c"/>
      </g>
    </g>

    <!-- Ambient Privilege Badges -->
    <g transform="translate(1005, 480)">
      <rect x="0" y="0" width="175" height="32" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.2"/>
      <text x="87" y="21" text-anchor="middle" font-size="16" font-weight="700" fill="#334155">~/.ssh Credentials</text>

      <rect x="190" y="0" width="180" height="32" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.2"/>
      <text x="280" y="21" text-anchor="middle" font-size="16" font-weight="700" fill="#334155">Host Shell Writes</text>
    </g>

    <!-- Bottom Status Pill -->
    <rect x="1005" y="560" width="370" height="38" rx="8" fill="#fff7ed" stroke="#fed7aa" stroke-width="1.5"/>
    <text x="1190" y="585" text-anchor="middle" class="status-pill" fill="#c2410c">Ambient Privilege Inheritance</text>
  </g>

  <!-- Arrow 3 -> 4 -->
  <path d="M 1395 415 H 1435" fill="none" stroke="#ea580c" stroke-width="4.5" marker-end="url(#arrowOrange)"/>

  <!-- STAGE 4: Rug-Pull Update -->
  <g filter="url(#cardShadow)">
    <rect x="1445" y="220" width="415" height="390" rx="14" fill="#ffffff" stroke="#c2410c" stroke-width="2.5"/>
    <rect x="1445" y="220" width="415" height="8" rx="4" fill="#c2410c"/>
    
    <!-- Stage Header -->
    <rect x="1465" y="246" width="100" height="30" rx="6" fill="#ffedd5"/>
    <text x="1515" y="267" text-anchor="middle" class="step-num" fill="#c2410c">Stage 4</text>
    <text x="1465" y="308" class="card-head">Rug-Pull Update</text>
    <text x="1465" y="336" class="card-sub">Post-Install Payload Mutation</text>

    <!-- Visual Icon: Two-Phase Version Switcher -->
    <g transform="translate(1485, 365)">
      <rect x="0" y="0" width="150" height="85" rx="8" fill="#f0fdf4" stroke="#86efac" stroke-width="2"/>
      <text x="75" y="35" text-anchor="middle" font-size="20" font-weight="900" fill="#15803d">v1.0.0</text>
      <text x="75" y="62" text-anchor="middle" font-size="15" font-weight="800" fill="#16a34a">✓ Clean Scan</text>

      <path d="M 160 42 H 205" fill="none" stroke="#c2410c" stroke-width="4" marker-end="url(#arrowOrange)"/>

      <rect x="220" y="0" width="155" height="85" rx="8" fill="#fef2f2" stroke="#fca5a5" stroke-width="2"/>
      <text x="297" y="35" text-anchor="middle" font-size="20" font-weight="900" fill="#dc2626">v2.0.0</text>
      <text x="297" y="62" text-anchor="middle" font-size="15" font-weight="800" fill="#b91c1c">⚠ POISONED</text>
    </g>

    <!-- Activation Condition Callout -->
    <rect x="1465" y="480" width="375" height="45" rx="8" fill="#fef2f2" stroke="#fecaca" stroke-width="1.2"/>
    <text x="1652" y="508" text-anchor="middle" font-size="16.5" font-weight="800" fill="#b91c1c">Activates Covert Exploit In-Flight</text>

    <!-- Bottom Status Pill -->
    <rect x="1465" y="560" width="375" height="38" rx="8" fill="#fff7ed" stroke="#fed7aa" stroke-width="1.5"/>
    <text x="1652" y="585" text-anchor="middle" class="status-pill" fill="#c2410c">Two-Phase Rug-Pull Complete</text>
  </g>

  <!-- Corridor Connecting Stage 4 to Runtime Phase -->
  <path d="M 1652 610 V 665 H 270 V 710" fill="none" stroke="#ea580c" stroke-width="4" stroke-dasharray="8 6" marker-end="url(#arrowOrange)"/>
  <g transform="translate(860, 642)">
    <rect x="0" y="0" width="320" height="42" rx="8" fill="#ffffff" stroke="#fed7aa" stroke-width="2"/>
    <text x="160" y="27" text-anchor="middle" class="status-pill" fill="#c2410c">Poisoned Manifest Active</text>
  </g>

  <!-- ========================================================
       PHASE II: RUNTIME PLANNING & SEAM MEDIATION (STAGE 5)
       ======================================================== -->
  <rect x="40" y="705" width="1840" height="655" rx="16" fill="#f8fafc" stroke="#94a3b8" stroke-width="2.5"/>
  <rect x="65" y="725" width="690" height="38" rx="8" fill="#e2e8f0"/>
  <text x="82" y="750" class="phase-tag" fill="#0f2b5c">Phase II: Runtime Dispatch, Seam Mediation &amp; Execution (Stage 5)</text>

  <!-- 5A: Agent Reasoning Plane (Left) -->
  <g filter="url(#cardShadow)">
    <rect x="65" y="785" width="430" height="545" rx="14" fill="#ffffff" stroke="#3b82f6" stroke-width="2.5"/>
    <rect x="65" y="785" width="430" height="8" rx="4" fill="#2563eb"/>

    <!-- Badge Left-Aligned with Internal Padding -->
    <rect x="85" y="810" width="160" height="30" rx="6" fill="#eff6ff"/>
    <text x="100" y="831" font-size="16" font-weight="800" fill="#2563eb">Step 1 · Reason</text>
    <text x="85" y="872" class="card-head">Reasoning Plane</text>
    <text x="85" y="902" class="card-sub">Autonomous Tool Planner</text>

    <!-- Converging Input Visual -->
    <g transform="translate(85, 930)">
      <rect x="0" y="0" width="390" height="50" rx="8" fill="#eff6ff" stroke="#bfdbfe" stroke-width="1.5"/>
      <text x="18" y="32" font-size="17.5" font-weight="700" fill="#1e40af">✓ User Task (Clean Intent)</text>

      <circle cx="195" cy="72" r="14" fill="#e2e8f0"/>
      <text x="195" y="78" text-anchor="middle" font-size="20" font-weight="900" fill="#64748b">+</text>

      <rect x="0" y="94" width="390" height="50" rx="8" fill="#fef2f2" stroke="#fca5a5" stroke-width="1.5"/>
      <text x="18" y="126" font-size="17.5" font-weight="700" fill="#dc2626">⚠ Poisoned SKILL.md (EN/BN)</text>

      <rect x="0" y="170" width="390" height="95" rx="10" fill="#f1f5f9" stroke="#cbd5e1" stroke-width="1.8"/>
      <text x="18" y="202" font-size="18.5" font-weight="800" fill="#0f172a">LLM Planning Engine</text>
      <text x="18" y="230" font-size="14.5" font-weight="600" fill="#64748b">Gemini 2.5 Flash · Llama 70B · Open-Weights</text>
      <text x="18" y="252" font-size="14" font-weight="800" fill="#dc2626">Cannot police its own tool proposals</text>
    </g>

    <!-- Bottom Pill -->
    <rect x="85" y="1270" width="390" height="42" rx="8" fill="#eff6ff" stroke="#bfdbfe" stroke-width="1.5"/>
    <text x="280" y="1296" text-anchor="middle" class="status-pill" fill="#1d4ed8">Reasoning Plane Compromised</text>
  </g>

  <!-- Arrow Reasoning -> Dispatch Seam -->
  <path d="M 495 1055 H 565" fill="none" stroke="#0f2b5c" stroke-width="4.5" marker-end="url(#arrowNavy)"/>
  <rect x="496" y="1018" width="70" height="32" rx="6" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
  <text x="531" y="1039" text-anchor="middle" font-size="14.5" font-weight="800" fill="#0f2b5c">dispatch()</text>

  <!-- 5B: Deterministic Policy Enforcement Seam (Center) -->
  <g filter="url(#glowTeal)">
    <rect x="575" y="785" width="670" height="545" rx="14" fill="#ffffff" stroke="#0d9488" stroke-width="3"/>
    <rect x="575" y="785" width="670" height="8" rx="4" fill="#0f766e"/>

    <!-- Badge Left-Aligned with Internal Padding -->
    <rect x="595" y="810" width="220" height="30" rx="6" fill="#ccfbf1"/>
    <text x="610" y="831" font-size="16" font-weight="800" fill="#0f766e">Step 2 · Invariant Seam</text>
    <text x="595" y="872" class="card-head">Policy Enforcement Seam</text>
    <text x="595" y="902" class="card-sub">In-Process Deterministic Gateway</text>

    <!-- Three Modular Check Cards (Width 630, Safe Margins) -->
    <g transform="translate(595, 925)">
      <!-- Invariant 1: Capability Token -->
      <g transform="translate(0, 0)">
        <rect x="0" y="0" width="630" height="66" rx="8" fill="#f0fdfa" stroke="#99f6e4" stroke-width="1.5"/>
        <circle cx="35" cy="33" r="18" fill="#ccfbf1"/>
        <text x="35" y="40" text-anchor="middle" font-size="18" font-weight="900" fill="#0f766e">1</text>
        <text x="70" y="27" font-size="18" font-weight="800" fill="#0f766e">Capability Token Verification</text>
        <text x="70" y="51" font-size="15" font-weight="600" fill="#134e4a">Validates cryptographic token; rejects undeclared tools</text>
      </g>

      <!-- Invariant 2: Canonical Path & Alias Normalization -->
      <g transform="translate(0, 80)">
        <rect x="0" y="0" width="630" height="66" rx="8" fill="#f0fdfa" stroke="#99f6e4" stroke-width="1.5"/>
        <circle cx="35" cy="33" r="18" fill="#ccfbf1"/>
        <text x="35" y="40" text-anchor="middle" font-size="18" font-weight="900" fill="#0f766e">2</text>
        <text x="70" y="27" font-size="18" font-weight="800" fill="#0f766e">Canonical Path &amp; Parameter Normalization</text>
        <text x="70" y="51" font-size="15" font-weight="600" fill="#134e4a">realpath() halts .., symlinks; resolves alias (file_path -> path)</text>
      </g>

      <!-- Invariant 3: Workspace Sandboxing -->
      <g transform="translate(0, 160)">
        <rect x="0" y="0" width="630" height="66" rx="8" fill="#f0fdfa" stroke="#99f6e4" stroke-width="1.5"/>
        <circle cx="35" cy="33" r="18" fill="#ccfbf1"/>
        <text x="35" y="40" text-anchor="middle" font-size="18" font-weight="900" fill="#0f766e">3</text>
        <text x="70" y="27" font-size="18" font-weight="800" fill="#0f766e">Workspace Boundary Containment</text>
        <text x="70" y="51" font-size="15" font-weight="600" fill="#134e4a">Confines target inside root; blocks host ~/.ssh and /etc</text>
      </g>
    </g>

    <!-- Seam Performance Metric Bar -->
    <g transform="translate(595, 1195)">
      <rect x="0" y="0" width="630" height="58" rx="10" fill="#ccfbf1" stroke="#5eead4" stroke-width="2"/>
      
      <!-- Col 1: Latency -->
      <g transform="translate(105, 0)">
        <text y="28" text-anchor="middle" font-size="22" font-weight="900" fill="#0f766e">0.037 ms</text>
        <text y="48" text-anchor="middle" font-size="13" font-weight="800" fill="#115e59">OVERHEAD</text>
      </g>
      
      <line x1="210" y1="10" x2="210" y2="48" stroke="#5eead4" stroke-width="2"/>

      <!-- Col 2: Language Invariance -->
      <g transform="translate(315, 0)">
        <text y="28" text-anchor="middle" font-size="22" font-weight="900" fill="#0f766e">100% Invariant</text>
        <text y="48" text-anchor="middle" font-size="13" font-weight="800" fill="#115e59">EN · BN · BN-EN</text>
      </g>

      <line x1="420" y1="10" x2="420" y2="48" stroke="#5eead4" stroke-width="2"/>

      <!-- Col 3: False Denials -->
      <g transform="translate(525, 0)">
        <text y="28" text-anchor="middle" font-size="22" font-weight="900" fill="#0f766e">0.0% FDR</text>
        <text y="48" text-anchor="middle" font-size="13" font-weight="800" fill="#115e59">100% UTILITY</text>
      </g>
    </g>

    <!-- Bottom Pill -->
    <rect x="595" y="1270" width="630" height="42" rx="8" fill="#f0fdfa" stroke="#99f6e4" stroke-width="1.5"/>
    <text x="910" y="1296" text-anchor="middle" class="status-pill" fill="#0f766e">In-Process Pre-Execution Verification Seam</text>
  </g>

  <!-- Branch Arrows to Step 3 -->
  <!-- Top Branch: Pass -->
  <path d="M 1245 920 H 1315" fill="none" stroke="#16a34a" stroke-width="4.5" marker-end="url(#arrowGreen)"/>
  <rect x="1250" y="885" width="66" height="30" rx="5" fill="#ffffff" stroke="#86efac" stroke-width="1.5"/>
  <text x="1283" y="906" text-anchor="middle" font-size="14.5" font-weight="900" fill="#16a34a">VALID</text>

  <!-- Bottom Branch: Block -->
  <path d="M 1245 1195 H 1315" fill="none" stroke="#dc2626" stroke-width="4.5" marker-end="url(#arrowRed)"/>
  <rect x="1245" y="1160" width="76" height="30" rx="5" fill="#ffffff" stroke="#fca5a5" stroke-width="1.5"/>
  <text x="1283" y="1181" text-anchor="middle" font-size="14.5" font-weight="900" fill="#dc2626">BLOCKED</text>

  <!-- 5C: Outcome A - Authorized Sandboxed Tool (Top Right) -->
  <g filter="url(#cardShadow)">
    <rect x="1325" y="785" width="535" height="255" rx="14" fill="#ffffff" stroke="#16a34a" stroke-width="2.5"/>
    <rect x="1325" y="785" width="535" height="8" rx="4" fill="#16a34a"/>

    <!-- Badge Left-Aligned with Internal Padding -->
    <rect x="1345" y="810" width="220" height="30" rx="6" fill="#f0fdf4"/>
    <text x="1360" y="831" font-size="16" font-weight="800" fill="#16a34a">Outcome A · Authorized</text>
    <text x="1345" y="872" class="card-head">Sandboxed Tool Execution</text>
    
    <!-- Badges Strip -->
    <g transform="translate(1345, 895)">
      <rect x="0" y="0" width="220" height="32" rx="6" fill="#f0fdf4" stroke="#86efac" stroke-width="1.2"/>
      <text x="110" y="21" text-anchor="middle" font-size="14.5" font-weight="800" fill="#15803d">Container (--network none)</text>

      <rect x="235" y="0" width="245" height="32" rx="6" fill="#f0fdf4" stroke="#86efac" stroke-width="1.2"/>
      <text x="357" y="21" text-anchor="middle" font-size="14.5" font-weight="800" fill="#15803d">Clean Task Workspace Write</text>
    </g>

    <text x="1345" y="955" font-size="15" font-weight="600" fill="#15803d">✓ Normal tool invocation executes cleanly in sandbox</text>

    <!-- Bottom Pill -->
    <rect x="1345" y="985" width="495" height="38" rx="8" fill="#dcfce7" stroke="#86efac" stroke-width="1.5"/>
    <text x="1592" y="1010" text-anchor="middle" class="status-pill" fill="#15803d">100% Benign Utility (0% False Denials)</text>
  </g>

  <!-- 5D: Outcome B - Deterministic Denial (Bottom Right) -->
  <g filter="url(#cardShadow)">
    <rect x="1325" y="1075" width="535" height="255" rx="14" fill="#ffffff" stroke="#dc2626" stroke-width="2.5"/>
    <rect x="1325" y="1075" width="535" height="8" rx="4" fill="#dc2626"/>

    <!-- Badge Left-Aligned with Internal Padding -->
    <rect x="1345" y="1100" width="190" height="30" rx="6" fill="#fef2f2"/>
    <text x="1360" y="1121" font-size="16" font-weight="800" fill="#dc2626">Outcome B · Blocked</text>
    <text x="1345" y="1162" class="card-head">Deterministic Denial &amp; Alert</text>

    <!-- Badges Strip -->
    <g transform="translate(1345, 1185)">
      <rect x="0" y="0" width="220" height="32" rx="6" fill="#fef2f2" stroke="#fca5a5" stroke-width="1.2"/>
      <text x="110" y="21" text-anchor="middle" font-size="14.5" font-weight="800" fill="#b91c1c">Fail-Closed Boundary Halt</text>

      <rect x="235" y="0" width="245" height="32" rx="6" fill="#fef2f2" stroke="#fca5a5" stroke-width="1.2"/>
      <text x="357" y="21" text-anchor="middle" font-size="14.5" font-weight="800" fill="#b91c1c">Security Audit Log Generated</text>
    </g>

    <text x="1345" y="1245" font-size="15" font-weight="600" fill="#b91c1c">✗ Zero credential theft or host writes reach OS layer</text>

    <!-- Bottom Pill -->
    <rect x="1345" y="1275" width="495" height="38" rx="8" fill="#fee2e2" stroke="#fca5a5" stroke-width="1.5"/>
    <text x="1592" y="1300" text-anchor="middle" class="status-pill" fill="#b91c1c">ASR: 0.0% in Non-English (3.8% in English)</text>
  </g>

  <!-- ========================================================
       BOTTOM LEGEND (Calibrated Coordinates with Zero Truncation)
       ======================================================== -->
  <g transform="translate(60, 1395)">
    <circle cx="15" cy="15" r="9" fill="#ea580c"/>
    <text x="34" y="22" class="legend-text">Untrusted Supply-Chain Flow</text>

    <circle cx="410" cy="15" r="9" fill="#0f2b5c"/>
    <text x="429" y="22" class="legend-text">Candidate Tool Proposal</text>

    <circle cx="760" cy="15" r="9" fill="#0d9488"/>
    <text x="779" y="22" class="legend-text">In-Process Authorization Seam</text>

    <circle cx="1170" cy="15" r="9" fill="#16a34a"/>
    <text x="1189" y="22" class="legend-text">Authorized Execution (Pass)</text>

    <circle cx="1530" cy="15" r="9" fill="#dc2626"/>
    <text x="1549" y="22" class="legend-text">Deterministic Denial (Block)</text>
  </g>
</svg>"""

    with open(out_svg_path, "w", encoding="utf-8") as f:
        f.write(svg)
    cairosvg.svg2png(url=out_svg_path, write_to=out_png_path, output_width=1920, output_height=1440)
    print(f"[Threat Lifecycle] Generated: {out_png_path}")


def generate_defense_seam(out_svg_path, out_png_path):
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1920 1440" width="1920" height="1440">
  <defs>
    <!-- Arrow Markers -->
    <marker id="arrowNavy2" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#0f2b5c"/>
    </marker>
    <marker id="arrowGreen2" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#16a34a"/>
    </marker>
    <marker id="arrowRed2" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#dc2626"/>
    </marker>

    <!-- Drop Shadows -->
    <filter id="cardShadow2" x="-5%" y="-5%" width="110%" height="115%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#0f172a" flood-opacity="0.08"/>
    </filter>
    <filter id="glowFortress" x="-6%" y="-6%" width="112%" height="112%">
      <feDropShadow dx="0" dy="0" stdDeviation="8" flood-color="#0d9488" flood-opacity="0.22"/>
    </filter>

    <style>
      text { font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }
      .diagram-title { font-size: 44px; font-weight: 900; fill: #0a1e38; letter-spacing: -0.5px; }
      .diagram-subtitle { font-size: 23px; font-weight: 600; fill: #475569; }
      .zone-badge { font-size: 16px; font-weight: 800; letter-spacing: 0.5px; }
      .card-title { font-size: 28px; font-weight: 800; fill: #0f172a; }
      .card-sub { font-size: 20px; font-weight: 600; fill: #475569; }
      .code-font { font-family: 'JetBrains Mono', monospace; font-size: 17.5px; font-weight: 600; }
      .status-pill { font-size: 18px; font-weight: 800; }
      .check-title { font-size: 21px; font-weight: 800; }
      .check-desc { font-size: 15.5px; font-weight: 600; }
      .metric-num { font-size: 32px; font-weight: 900; }
      .metric-lbl { font-size: 14.5px; font-weight: 800; text-transform: uppercase; letter-spacing: 0.3px; }
      .legend-text { font-size: 19px; font-weight: 700; fill: #334155; }
    </style>
  </defs>

  <!-- Clean Canvas -->
  <rect width="1920" height="1440" fill="#ffffff"/>

  <!-- ========================================================
       TOP HEADER TITLE BAR
       ======================================================== -->
  <g transform="translate(60, 48)">
    <rect x="0" y="0" width="8" height="52" rx="4" fill="#0d9488"/>
    <text x="24" y="38" class="diagram-title">Deterministic Authorization Seam: Execution Boundary Architecture</text>
    <text x="24" y="74" class="diagram-subtitle">Pre-Execution Mediation of Capability Tokens, Canonical Invariants, and Container Sandboxing</text>
  </g>

  <!-- ========================================================
       ZONE 1: PROBABILISTIC REASONING PLANE (LEFT, UNTRUSTED)
       ======================================================== -->
  <g filter="url(#cardShadow2)">
    <rect x="40" y="145" width="440" height="1225" rx="16" fill="#f8fafc" stroke="#3b82f6" stroke-width="2.5"/>
    <rect x="40" y="145" width="440" height="8" rx="4" fill="#2563eb"/>

    <!-- Zone Badge Left-Aligned with Internal Padding -->
    <rect x="65" y="175" width="220" height="32" rx="6" fill="#eff6ff"/>
    <text x="80" y="197" class="zone-badge" fill="#2563eb">Zone 1 · Probabilistic</text>
    <text x="65" y="245" class="card-title">Agent Reasoning Plane</text>
    <text x="65" y="275" class="card-sub">Untrusted Decision Environment</text>

    <!-- Block 1A: Authentic User Intent -->
    <g transform="translate(65, 305)">
      <rect x="0" y="0" width="390" height="145" rx="10" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.8"/>
      <rect x="0" y="0" width="8" height="145" rx="4" fill="#16a34a"/>
      <g transform="translate(24, 28)">
        <text font-size="22" font-weight="800" fill="#0f2b5c">Authentic User Intent</text>
        <text y="30" font-size="17" font-weight="600" fill="#475569">Legitimate task instructions</text>
        <text y="54" font-size="17" font-weight="600" fill="#475569">(e.g., Git status, doc convert)</text>
        <rect x="0" y="68" width="190" height="28" rx="6" fill="#f0fdf4"/>
        <text x="95" y="87" text-anchor="middle" font-size="14" font-weight="800" fill="#166534">✓ Trusted Control Plane</text>
      </g>
    </g>

    <!-- Block 1B: Poisoned Skill Manifest -->
    <g transform="translate(65, 475)">
      <rect x="0" y="0" width="390" height="165" rx="10" fill="#fff7ed" stroke="#fed7aa" stroke-width="1.8"/>
      <rect x="0" y="0" width="8" height="165" rx="4" fill="#ea580c"/>
      <g transform="translate(24, 28)">
        <text font-size="22" font-weight="800" fill="#c2410c">Poisoned Skill Manifests</text>
        <text y="30" font-size="17" font-weight="600" fill="#9a3412">Ingested external SKILL.md</text>
        <text y="54" font-size="17" font-weight="600" fill="#9a3412">in English, Bangla, Banglish</text>
        <text y="78" font-size="17" font-weight="600" fill="#9a3412">targeting ~/.ssh credentials</text>
        <rect x="0" y="92" width="190" height="28" rx="6" fill="#fef2f2"/>
        <text x="95" y="111" text-anchor="middle" font-size="14" font-weight="800" fill="#dc2626">✗ Untrusted Data Plane</text>
      </g>
    </g>

    <!-- Block 1C: LLM Planning Engine -->
    <g transform="translate(65, 665)">
      <rect x="0" y="0" width="390" height="240" rx="10" fill="#ffffff" stroke="#bfdbfe" stroke-width="1.8"/>
      <rect x="0" y="0" width="8" height="240" rx="4" fill="#2563eb"/>
      <g transform="translate(24, 28)">
        <text font-size="22" font-weight="800" fill="#1e40af">LLM Planning Engine</text>
        <text y="32" font-size="16.5" font-weight="600" fill="#334155">• Multi-step reasoning loop</text>
        <text y="60" font-size="16.5" font-weight="600" fill="#334155">• Evaluated on open-weights &amp;</text>
        <text y="84" font-size="16.5" font-weight="600" fill="#334155">  Gemini 2.5 Flash / Llama 70B</text>
        <text y="114" font-size="16.5" font-weight="600" fill="#334155">• Susceptible to cross-lingual</text>
        <text y="138" font-size="16.5" font-weight="600" fill="#334155">  adversarial injection</text>
        <rect x="0" y="156" width="340" height="34" rx="6" fill="#fef2f2" stroke="#fca5a5" stroke-width="1.2"/>
        <text x="170" y="179" text-anchor="middle" font-size="15.5" font-weight="800" fill="#b91c1c">100% Vulnerable to Injections</text>
      </g>
    </g>

    <!-- Intercepted Tool Proposal Chip -->
    <g transform="translate(65, 935)">
      <rect x="0" y="0" width="390" height="310" rx="10" fill="#0f172a"/>
      <g transform="translate(20, 30)">
        <text class="code-font" fill="#38bdf8"># Intercepted Candidate</text>
        <text y="34" class="code-font" fill="#f8fafc">dispatch(request, ctx):</text>
        <text y="70" class="code-font" fill="#94a3b8">  tool = "file_write"</text>
        <text y="102" class="code-font" fill="#f8fafc">  target = "../../.ssh"</text>
        <text y="134" class="code-font" fill="#94a3b8">  token = "sess_4a91"</text>
        <text y="166" class="code-font" fill="#94a3b8">  mode = "sandboxed"</text>
        <rect x="0" y="195" width="350" height="58" rx="6" fill="#1e293b"/>
        <text x="14" y="222" font-size="14.5" font-weight="700" fill="#ea580c">Normalizes schema aliases:</text>
        <text x="14" y="242" class="code-font" font-size="14" fill="#fbbf24">file_path -> path; realpath()</text>
      </g>
    </g>

    <!-- Bottom Pill -->
    <rect x="65" y="1295" width="390" height="46" rx="8" fill="#eff6ff" stroke="#bfdbfe" stroke-width="1.5"/>
    <text x="260" y="1324" text-anchor="middle" class="status-pill" fill="#1d4ed8">Probabilistic Reasoning Plane</text>
  </g>

  <!-- Arrow Zone 1 -> Zone 2 -->
  <path d="M 480 750 H 545" fill="none" stroke="#0f2b5c" stroke-width="4.5" marker-end="url(#arrowNavy2)"/>
  <rect x="488" y="715" width="54" height="28" rx="5" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
  <text x="515" y="734" text-anchor="middle" font-size="13" font-weight="800" fill="#0f2b5c">CALL</text>

  <!-- ========================================================
       ZONE 2: IN-PROCESS DETERMINISTIC POLICY SEAM (CENTER, TRUSTED)
       ======================================================== -->
  <g filter="url(#glowFortress)">
    <rect x="555" y="145" width="760" height="1225" rx="16" fill="#ffffff" stroke="#0d9488" stroke-width="3.5"/>
    <rect x="555" y="145" width="760" height="8" rx="4" fill="#0f766e"/>

    <!-- Zone Badge Left-Aligned with Internal Padding -->
    <rect x="585" y="175" width="340" height="32" rx="6" fill="#ccfbf1"/>
    <text x="600" y="197" class="zone-badge" fill="#0f766e">Zone 2 · In-Process Trusted Anchor</text>
    <text x="585" y="245" class="card-title">Policy Enforcement Seam</text>
    <text x="585" y="275" class="card-sub">Mandatory Pre-Execution Authorization Gateway</text>

    <!-- Invariant Pipeline: 3 Visual Modules (Width 700, Safe Margins) -->
    <g transform="translate(585, 305)">

      <!-- Invariant 1: Capability Token -->
      <g transform="translate(0, 0)">
        <rect x="0" y="0" width="700" height="190" rx="12" fill="#f0fdfa" stroke="#99f6e4" stroke-width="2"/>
        <rect x="0" y="0" width="10" height="190" rx="4" fill="#0d9488"/>
        <g transform="translate(30, 36)">
          <circle cx="20" cy="12" r="18" fill="#ccfbf1"/>
          <text x="20" y="19" text-anchor="middle" font-size="20" font-weight="900" fill="#0f766e">1</text>
          <text x="55" y="22" class="check-title" fill="#0f766e">Capability Token Validation</text>
          <text x="55" y="58" class="check-desc" fill="#115e59">• Validates cryptographic token issued during task authorization</text>
          <text x="55" y="86" class="check-desc" fill="#115e59">• Verifies tool identity is permitted for active session</text>
          <text x="55" y="114" class="check-desc" fill="#115e59">• Rejects undeclared or escalated tool calls immediately</text>
        </g>
      </g>

      <!-- Invariant 2: Canonical Path & Schema Aliases -->
      <g transform="translate(0, 220)">
        <rect x="0" y="0" width="700" height="210" rx="12" fill="#f0fdfa" stroke="#99f6e4" stroke-width="2"/>
        <rect x="0" y="0" width="10" height="210" rx="4" fill="#0d9488"/>
        <g transform="translate(30, 36)">
          <circle cx="20" cy="12" r="18" fill="#ccfbf1"/>
          <text x="20" y="19" text-anchor="middle" font-size="20" font-weight="900" fill="#0f766e">2</text>
          <text x="55" y="22" class="check-title" fill="#0f766e">Canonical Path &amp; Parameter Normalization</text>
          <text x="55" y="58" class="check-desc" fill="#115e59">• Resolves realpath() across symlinks and path traversal (..)</text>
          <text x="55" y="86" class="check-desc" fill="#115e59">• Normalizes schema parameter aliases (file_path -> path)</text>
          <text x="55" y="114" class="check-desc" fill="#115e59">• Deterministic normalization eliminates 3.8% residual mismatch</text>
        </g>
      </g>

      <!-- Invariant 3: Workspace Sandboxing -->
      <g transform="translate(0, 460)">
        <rect x="0" y="0" width="700" height="190" rx="12" fill="#f0fdfa" stroke="#99f6e4" stroke-width="2"/>
        <rect x="0" y="0" width="10" height="190" rx="4" fill="#0d9488"/>
        <g transform="translate(30, 36)">
          <circle cx="20" cy="12" r="18" fill="#ccfbf1"/>
          <text x="20" y="19" text-anchor="middle" font-size="20" font-weight="900" fill="#0f766e">3</text>
          <text x="55" y="22" class="check-title" fill="#0f766e">Workspace Sandbox Containment</text>
          <text x="55" y="58" class="check-desc" fill="#115e59">• Confines all operations strictly within designated workspace root</text>
          <text x="55" y="86" class="check-desc" fill="#115e59">• Immutable boundaries block host credentials (~/.ssh, /etc)</text>
          <text x="55" y="114" class="check-desc" fill="#115e59">• Transparent pass-through for benign project workspace paths</text>
        </g>
      </g>

    </g>

    <!-- Deterministic Guarantees Metric Strip -->
    <g transform="translate(585, 1010)">
      <rect x="0" y="0" width="700" height="240" rx="14" fill="#ccfbf1" stroke="#5eead4" stroke-width="2.5"/>
      <text x="30" y="44" font-size="25" font-weight="900" fill="#0f766e">Empirical Seam Guarantees (N = 312)</text>
      
      <g transform="translate(30, 80)">
        <!-- Metric 1: Latency -->
        <rect x="0" y="0" width="195" height="120" rx="10" fill="#ffffff" stroke="#99f6e4" stroke-width="1.8"/>
        <text x="97" y="48" text-anchor="middle" class="metric-num" fill="#0f766e">0.037 ms</text>
        <text x="97" y="78" text-anchor="middle" class="metric-lbl" fill="#115e59">Overhead</text>
        <text x="97" y="100" text-anchor="middle" font-size="13.5" font-weight="600" fill="#134e4a">&lt;0.005% loop</text>

        <!-- Metric 2: Language Invariant (Calibrated Font Size to Fit Box) -->
        <rect x="220" y="0" width="200" height="120" rx="10" fill="#ffffff" stroke="#99f6e4" stroke-width="1.8"/>
        <text x="320" y="48" text-anchor="middle" class="metric-num" fill="#0f766e">100%</text>
        <text x="320" y="78" text-anchor="middle" class="metric-lbl" fill="#115e59">Language Invariant</text>
        <text x="320" y="100" text-anchor="middle" font-size="13.5" font-weight="600" fill="#134e4a">EN · BN · BN-EN</text>

        <!-- Metric 3: False Denials -->
        <rect x="445" y="0" width="195" height="120" rx="10" fill="#ffffff" stroke="#99f6e4" stroke-width="1.8"/>
        <text x="542" y="48" text-anchor="middle" class="metric-num" fill="#0f766e">0.0%</text>
        <text x="542" y="78" text-anchor="middle" class="metric-lbl" fill="#115e59">False Denials</text>
        <text x="542" y="100" text-anchor="middle" font-size="13.5" font-weight="600" fill="#134e4a">100% Utility (BUR)</text>
      </g>
    </g>

    <!-- Bottom Pill -->
    <rect x="585" y="1295" width="700" height="46" rx="8" fill="#f0fdfa" stroke="#99f6e4" stroke-width="1.5"/>
    <text x="935" y="1324" text-anchor="middle" class="status-pill" fill="#0f766e">In-Process Deterministic Enforcement Boundary</text>
  </g>

  <!-- Branch Arrows from Zone 2 to Zone 3 -->
  <!-- Upper: Pass -->
  <path d="M 1315 470 H 1375" fill="none" stroke="#16a34a" stroke-width="4.5" marker-end="url(#arrowGreen2)"/>
  <rect x="1322" y="435" width="56" height="28" rx="5" fill="#ffffff" stroke="#86efac" stroke-width="1.5"/>
  <text x="1350" y="454" text-anchor="middle" font-size="14" font-weight="900" fill="#16a34a">PASS</text>

  <!-- Lower: Deny -->
  <path d="M 1315 1040 H 1375" fill="none" stroke="#dc2626" stroke-width="4.5" marker-end="url(#arrowRed2)"/>
  <rect x="1322" y="1005" width="56" height="28" rx="5" fill="#ffffff" stroke="#fca5a5" stroke-width="1.5"/>
  <text x="1350" y="1024" text-anchor="middle" font-size="14" font-weight="900" fill="#dc2626">DENY</text>

  <!-- ========================================================
       ZONE 3: EXECUTION BOUNDARIES & OUTCOMES (RIGHT)
       ======================================================== -->
  <!-- 3A: Authorized Execution Container (Green) -->
  <g filter="url(#cardShadow2)">
    <rect x="1385" y="240" width="495" height="470" rx="16" fill="#ffffff" stroke="#16a34a" stroke-width="2.5"/>
    <rect x="1385" y="240" width="495" height="8" rx="4" fill="#16a34a"/>

    <!-- Zone Badge Left-Aligned with Internal Padding -->
    <rect x="1410" y="270" width="220" height="32" rx="6" fill="#f0fdf4"/>
    <text x="1425" y="292" class="zone-badge" fill="#16a34a">Outcome A · Authorized</text>
    <text x="1410" y="340" class="card-title">Sandboxed Execution</text>
    <text x="1410" y="370" class="card-sub">Compliant Tool Execution</text>

    <!-- Visual Box -->
    <g transform="translate(1410, 395)">
      <rect x="0" y="0" width="445" height="160" rx="10" fill="#f0fdf4" stroke="#86efac" stroke-width="1.8"/>
      <g transform="translate(20, 30)">
        <text font-size="18.5" font-weight="800" fill="#15803d">• Worker Container Sandbox</text>
        <text y="28" font-size="16" font-weight="600" fill="#166534">  Isolated network namespace (--network none)</text>
        
        <text y="68" font-size="18.5" font-weight="800" fill="#15803d">• Workspace Output Only</text>
        <text y="96" font-size="16" font-weight="600" fill="#166534">  Writes confined to task directory</text>
      </g>
    </g>

    <!-- Key Takeaway Pill -->
    <rect x="1410" y="585" width="445" height="50" rx="8" fill="#dcfce7" stroke="#86efac" stroke-width="1.5"/>
    <text x="1632" y="616" text-anchor="middle" class="status-pill" fill="#15803d">100% Benign Task Success (BUR)</text>

    <rect x="1410" y="650" width="445" height="40" rx="8" fill="#f0fdf4"/>
    <text x="1632" y="675" text-anchor="middle" font-size="16" font-weight="700" fill="#166534">0.0% False Positive Denials (FDR)</text>
  </g>

  <!-- 3B: Deterministic Denial & Alert (Red) -->
  <g filter="url(#cardShadow2)">
    <rect x="1385" y="810" width="495" height="470" rx="16" fill="#ffffff" stroke="#dc2626" stroke-width="2.5"/>
    <rect x="1385" y="810" width="495" height="8" rx="4" fill="#dc2626"/>

    <!-- Zone Badge Left-Aligned with Internal Padding (Width 280) -->
    <rect x="1410" y="840" width="280" height="32" rx="6" fill="#fef2f2"/>
    <text x="1425" y="862" class="zone-badge" fill="#dc2626">Outcome B · Security Intercept</text>
    <text x="1410" y="910" class="card-title">Deterministic Denial</text>
    <text x="1410" y="940" class="card-sub">Adversarial Action Aborted</text>

    <!-- Visual Box -->
    <g transform="translate(1410, 965)">
      <rect x="0" y="0" width="445" height="160" rx="10" fill="#fef2f2" stroke="#fca5a5" stroke-width="1.8"/>
      <g transform="translate(20, 30)">
        <text font-size="18.5" font-weight="800" fill="#b91c1c">• Immediate Fail-Closed Rejection</text>
        <text y="28" font-size="16" font-weight="600" fill="#991b1b">  Halted prior to operating system dispatch</text>

        <text y="68" font-size="18.5" font-weight="800" fill="#b91c1c">• Tamper-Proof Audit Event</text>
        <text y="96" font-size="16" font-weight="600" fill="#991b1b">  Logged to host security supervisor</text>
      </g>
    </g>

    <!-- Key Takeaway Pill -->
    <rect x="1410" y="1155" width="445" height="50" rx="8" fill="#fee2e2" stroke="#fca5a5" stroke-width="1.5"/>
    <text x="1632" y="1186" text-anchor="middle" class="status-pill" fill="#b91c1c">ASR: 0.0% (Bangla &amp; Banglish)</text>

    <rect x="1410" y="1220" width="445" height="40" rx="8" fill="#fef2f2"/>
    <text x="1632" y="1245" text-anchor="middle" font-size="16" font-weight="700" fill="#991b1b">Zero host credential access or writes</text>
  </g>

  <!-- ========================================================
       BOTTOM LEGEND (Calibrated Coordinates with Zero Truncation)
       ======================================================== -->
  <g transform="translate(45, 1395)">
    <circle cx="15" cy="15" r="9" fill="#2563eb"/>
    <text x="34" y="22" class="legend-text">Reasoning Plane</text>

    <circle cx="280" cy="15" r="9" fill="#0f2b5c"/>
    <text x="299" y="22" class="legend-text">Candidate Tool Proposal</text>

    <circle cx="640" cy="15" r="9" fill="#0d9488"/>
    <text x="659" y="22" class="legend-text">In-Process Authorization Seam</text>

    <circle cx="1060" cy="15" r="9" fill="#16a34a"/>
    <text x="1079" y="22" class="legend-text">Sandboxed Execution (Pass)</text>

    <circle cx="1460" cy="15" r="9" fill="#dc2626"/>
    <text x="1479" y="22" class="legend-text">Deterministic Denial (Block)</text>
  </g>
</svg>"""

    with open(out_svg_path, "w", encoding="utf-8") as f:
        f.write(svg)
    cairosvg.svg2png(url=out_svg_path, write_to=out_png_path, output_width=1920, output_height=1440)
    print(f"[Defense Seam Architecture] Generated: {out_png_path}")

if __name__ == "__main__":
    os.makedirs("poster", exist_ok=True)
    os.makedirs("poster_v2", exist_ok=True)

    # Generate for poster/
    generate_threat_lifecycle("poster/threat_lifecycle.svg", "poster/threat_lifecycle.png")
    generate_defense_seam("poster/defense_seam_architecture.svg", "poster/defense_seam_architecture.png")

    # Generate for poster_v2/
    generate_threat_lifecycle("poster_v2/threat_lifecycle.svg", "poster_v2/threat_lifecycle.png")
    generate_defense_seam("poster_v2/defense_seam_architecture.svg", "poster_v2/defense_seam_architecture.png")
    print("All diagrams generated successfully.")
