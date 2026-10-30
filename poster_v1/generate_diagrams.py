import os
import subprocess
import cairosvg

def generate_threat_lifecycle():
    threat_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1920 1200" width="1920" height="1200">
  <defs>
    <marker id="arrowOrange" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#ea580c"/>
    </marker>
    <marker id="arrowBlue" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#2563eb"/>
    </marker>
    <marker id="arrowPurple" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#7c3aed"/>
    </marker>
    <marker id="arrowGreen" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#16a34a"/>
    </marker>
    <marker id="arrowRed" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#dc2626"/>
    </marker>
    <filter id="cardShadow" x="-10%" y="-10%" width="120%" height="130%">
      <feDropShadow dx="0" dy="4" stdDeviation="8" flood-color="#0f172a" flood-opacity="0.08"/>
    </filter>
    <style>
      text { font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }
      .main-title { font-size: 42px; font-weight: 800; fill: #0a1e38; letter-spacing: -0.5px; }
      .main-sub { font-size: 21px; font-weight: 500; fill: #475569; }
      .container-header { font-size: 20px; font-weight: 800; letter-spacing: 1px; }
      .container-sub { font-size: 16px; font-weight: 500; fill: #64748b; }
      .badge-type { font-size: 15px; font-weight: 800; letter-spacing: 0.8px; }
      .card-title { font-size: 27px; font-weight: 800; fill: #0f172a; letter-spacing: -0.3px; }
      .card-desc { font-size: 18px; font-weight: 500; fill: #334155; }
      .tech-pill { font-size: 16px; font-weight: 700; }
      .flow-label { font-size: 15.5px; font-weight: 800; }
      .legend-text { font-size: 17px; font-weight: 600; fill: #475569; }
      .footer-text { font-size: 15px; font-weight: 500; fill: #94a3b8; }
    </style>
  </defs>

  <rect width="1920" height="1200" fill="#ffffff"/>

  <!-- Title & Subtitle -->
  <text x="960" y="52" text-anchor="middle" class="main-title">Cross-Lingual Agent Skill Poisoning: Threat Lifecycle &amp; Mitigation</text>
  <text x="960" y="85" text-anchor="middle" class="main-sub">Five-stage attack progression through untrusted supply chains to runtime policy interception</text>

  <!-- Container 1: Untrusted Supply Chain -->
  <rect x="40" y="110" width="1840" height="445" rx="16" fill="#fffaf5" stroke="#fed7aa" stroke-width="2.2" stroke-dasharray="8 6"/>
  <text x="65" y="145" class="container-header" fill="#ea580c">UNTRUSTED SUPPLY CHAIN (STAGES 1–4)</text>
  <text x="65" y="172" class="container-sub">Adversary crafts cross-lingual injection, evades static marketplace scanners, and mutates skill post-vetting</text>

  <!-- Container 2: Agent Runtime & Defense -->
  <rect x="40" y="590" width="1840" height="475" rx="16" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2.2" stroke-dasharray="8 6"/>
  <text x="65" y="625" class="container-header" fill="#0d9488">AGENT RUNTIME &amp; EXECUTION BOUNDARY (STAGE 5)</text>
  <text x="65" y="652" class="container-sub">Autonomous planning loop ingests context; deterministic policy seam halts malicious invocation at execution boundary</text>

  <!-- STAGE 1: Authoring -->
  <g filter="url(#cardShadow)">
    <rect x="60" y="195" width="420" height="335" rx="12" fill="#ffffff" stroke="#f97316" stroke-width="2"/>
    <rect x="60" y="195" width="420" height="6" rx="3" fill="#ea580c"/>
    <text x="85" y="235" class="badge-type" fill="#ea580c">ATTACK STAGE 1</text>
    <text x="85" y="275" class="card-title">1. Authoring</text>
    <text x="85" y="322" class="card-desc">Crafted in EN, Bangla (BN), or</text>
    <text x="85" y="356" class="card-desc">code-mixed Banglish (BN-EN)</text>
    <text x="85" y="390" class="card-desc">registers within SKILL.md.</text>
    <rect x="85" y="465" width="370" height="44" rx="8" fill="#fff7ed" stroke="#fed7aa" stroke-width="1.2"/>
    <text x="270" y="493" text-anchor="middle" class="tech-pill" fill="#c2410c">Register Poisoning</text>
  </g>

  <!-- Arrow 1 -> 2 -->
  <path d="M 480 362 H 514" fill="none" stroke="#ea580c" stroke-width="3" marker-end="url(#arrowOrange)"/>

  <!-- STAGE 2: Registry -->
  <g filter="url(#cardShadow)">
    <rect x="526" y="195" width="420" height="335" rx="12" fill="#ffffff" stroke="#f97316" stroke-width="2"/>
    <rect x="526" y="195" width="420" height="6" rx="3" fill="#ea580c"/>
    <text x="551" y="235" class="badge-type" fill="#ea580c">ATTACK STAGE 2</text>
    <text x="551" y="275" class="card-title">2. Registry</text>
    <text x="551" y="322" class="card-desc">Published to skill registry; evades</text>
    <text x="551" y="356" class="card-desc">English-calibrated keyword scanners</text>
    <text x="551" y="390" class="card-desc">via cross-lingual embedding blindspots.</text>
    <rect x="551" y="465" width="370" height="44" rx="8" fill="#fff7ed" stroke="#fed7aa" stroke-width="1.2"/>
    <text x="736" y="493" text-anchor="middle" class="tech-pill" fill="#c2410c">Scanner Evasion (100% VBR)</text>
  </g>

  <!-- Arrow 2 -> 3 -->
  <path d="M 946 362 H 980" fill="none" stroke="#ea580c" stroke-width="3" marker-end="url(#arrowOrange)"/>

  <!-- STAGE 3: Install -->
  <g filter="url(#cardShadow)">
    <rect x="992" y="195" width="420" height="335" rx="12" fill="#ffffff" stroke="#f97316" stroke-width="2"/>
    <rect x="992" y="195" width="420" height="6" rx="3" fill="#ea580c"/>
    <text x="1017" y="235" class="badge-type" fill="#ea580c">ATTACK STAGE 3</text>
    <text x="1017" y="275" class="card-title">3. Install</text>
    <text x="1017" y="322" class="card-desc">Installed into agent environment;</text>
    <text x="1017" y="356" class="card-desc">inherits ambient user permissions</text>
    <text x="1017" y="390" class="card-desc">and workspace execution credentials.</text>
    <rect x="1017" y="465" width="370" height="44" rx="8" fill="#fff7ed" stroke="#fed7aa" stroke-width="1.2"/>
    <text x="1202" y="493" text-anchor="middle" class="tech-pill" fill="#c2410c">Privilege Inheritance</text>
  </g>

  <!-- Arrow 3 -> 4 -->
  <path d="M 1412 362 H 1446" fill="none" stroke="#ea580c" stroke-width="3" marker-end="url(#arrowOrange)"/>

  <!-- STAGE 4: Update -->
  <g filter="url(#cardShadow)">
    <rect x="1458" y="195" width="400" height="335" rx="12" fill="#ffffff" stroke="#ea580c" stroke-width="2.2"/>
    <rect x="1458" y="195" width="400" height="6" rx="3" fill="#c2410c"/>
    <text x="1483" y="235" class="badge-type" fill="#c2410c">ATTACK STAGE 4</text>
    <text x="1483" y="275" class="card-title">4. Update</text>
    <text x="1483" y="322" class="card-desc">Rug-pull update mutates previously</text>
    <text x="1483" y="356" class="card-desc">vetted skill, activating high-impact</text>
    <text x="1483" y="390" class="card-desc">exfiltration logic dynamically.</text>
    <rect x="1483" y="465" width="350" height="44" rx="8" fill="#fff7ed" stroke="#fed7aa" stroke-width="1.2"/>
    <text x="1658" y="493" text-anchor="middle" class="tech-pill" fill="#c2410c">Two-Phase Rug-Pull</text>
  </g>

  <!-- Corridor Arrow: Stage 4 -> Stage 5 -->
  <path d="M 1658 530 V 568 H 685 V 675" fill="none" stroke="#ea580c" stroke-width="3" stroke-dasharray="8 6" marker-end="url(#arrowOrange)"/>
  <rect x="1070" y="552" width="260" height="32" rx="6" fill="#ffffff" stroke="#fed7aa" stroke-width="1.5"/>
  <text x="1200" y="574" text-anchor="middle" class="flow-label" fill="#ea580c">Poisoned Skill Injected</text>

  <!-- AUTHENTIC INPUT: Benign User Task -->
  <g filter="url(#cardShadow)">
    <rect x="60" y="685" width="380" height="350" rx="12" fill="#ffffff" stroke="#3b82f6" stroke-width="2"/>
    <rect x="60" y="685" width="380" height="6" rx="3" fill="#2563eb"/>
    <text x="85" y="235-10" class="badge-type" fill="#2563eb" style="display:none;"></text>
    <text x="85" y="725" class="badge-type" fill="#2563eb">AUTHENTIC INPUT</text>
    <text x="85" y="765" class="card-title">Benign User Task</text>
    <text x="85" y="812" class="card-desc">Legitimate user workflow</text>
    <text x="85" y="846" class="card-desc">prompt without attack payload</text>
    <text x="85" y="880" class="card-desc">(e.g., PDF parse, Git sync).</text>
    <rect x="85" y="965" width="330" height="44" rx="8" fill="#eff6ff" stroke="#bfdbfe" stroke-width="1.2"/>
    <text x="250" y="993" text-anchor="middle" class="tech-pill" fill="#1d4ed8">Clean User Prompt</text>
  </g>

  <!-- Arrow Benign -> Stage 5 -->
  <path d="M 440 860 H 480" fill="none" stroke="#2563eb" stroke-width="3" marker-end="url(#arrowBlue)"/>
  <rect x="445" y="847" width="44" height="26" rx="4" fill="#ffffff" stroke="#bfdbfe" stroke-width="1.5"/>
  <text x="467" y="865" text-anchor="middle" font-size="13" font-weight="800" fill="#2563eb">Task</text>

  <!-- RUNTIME STAGE 5: Planning & Tool Selection -->
  <g filter="url(#cardShadow)">
    <rect x="495" y="685" width="410" height="350" rx="12" fill="#ffffff" stroke="#f97316" stroke-width="2"/>
    <rect x="495" y="685" width="410" height="6" rx="3" fill="#ea580c"/>
    <text x="520" y="725" class="badge-type" fill="#ea580c">RUNTIME STAGE 5</text>
    <text x="520" y="765" class="card-title">5. Planning &amp; Dispatch</text>
    <text x="520" y="812" class="card-desc">Model reasoning plane ingests</text>
    <text x="520" y="846" class="card-desc">poisoned manifest &amp; proposes</text>
    <text x="520" y="880" class="card-desc">unauthorized tool call (read SSH).</text>
    <rect x="520" y="965" width="360" height="44" rx="8" fill="#fff7ed" stroke="#fed7aa" stroke-width="1.2"/>
    <text x="700" y="993" text-anchor="middle" class="tech-pill" fill="#c2410c">LLM Planning Loop</text>
  </g>

  <!-- Arrow Stage 5 -> Policy Module -->
  <path d="M 905 860 H 945" fill="none" stroke="#7c3aed" stroke-width="3" marker-end="url(#arrowPurple)"/>
  <rect x="911" y="847" width="42" height="26" rx="4" fill="#ffffff" stroke="#ddd6fe" stroke-width="1.5"/>
  <text x="932" y="865" text-anchor="middle" font-size="13" font-weight="800" fill="#7c3aed">Call</text>

  <!-- DEFENSE SEAM: Boundary Interceptor -->
  <g filter="url(#cardShadow)">
    <rect x="960" y="685" width="440" height="350" rx="12" fill="#ffffff" stroke="#0d9488" stroke-width="2.2"/>
    <rect x="960" y="685" width="440" height="6" rx="3" fill="#0f766e"/>
    <text x="985" y="725" class="badge-type" fill="#0d9488">DEFENSE INTERCEPTOR</text>
    <text x="985" y="765" class="card-title">Policy Enforcement Seam</text>
    <text x="985" y="812" class="card-desc">In-process security gate intercepts</text>
    <text x="985" y="846" class="card-desc">all candidate tool dispatches,</text>
    <text x="985" y="880" class="card-desc">evaluating capability tokens &amp; paths.</text>
    <rect x="985" y="965" width="390" height="44" rx="8" fill="#f0fdfa" stroke="#99f6e4" stroke-width="1.2"/>
    <text x="1180" y="993" text-anchor="middle" class="tech-pill" fill="#0f766e">Deterministic Seam Hook (0.037ms)</text>
  </g>

  <!-- Arrow Policy -> Authorized (Pass) -->
  <path d="M 1400 770 H 1455" fill="none" stroke="#16a34a" stroke-width="3" marker-end="url(#arrowGreen)"/>
  <rect x="1405" y="757" width="44" height="26" rx="4" fill="#ffffff" stroke="#86efac" stroke-width="1.5"/>
  <text x="1427" y="775" text-anchor="middle" font-size="13" font-weight="800" fill="#16a34a">Pass</text>

  <!-- Arrow Policy -> Deny (Block) -->
  <path d="M 1400 950 H 1455" fill="none" stroke="#dc2626" stroke-width="3" marker-end="url(#arrowRed)"/>
  <rect x="1403" y="937" width="46" height="26" rx="4" fill="#ffffff" stroke="#fca5a5" stroke-width="1.5"/>
  <text x="1426" y="955" text-anchor="middle" font-size="13" font-weight="800" fill="#dc2626">Block</text>

  <!-- COMPLIANT PATH: Authorized Execution -->
  <g filter="url(#cardShadow)">
    <rect x="1460" y="685" width="398" height="175" rx="12" fill="#ffffff" stroke="#16a34a" stroke-width="2"/>
    <rect x="1460" y="685" width="398" height="5" rx="2.5" fill="#15803d"/>
    <text x="1485" y="722" class="badge-type" fill="#16a34a">COMPLIANT PATH (GREEN)</text>
    <text x="1485" y="756" class="card-title" font-size="24">Authorized Execution</text>
    <text x="1485" y="792" class="card-desc" font-size="17">Verified task runs in sandbox;</text>
    <text x="1485" y="820" class="card-desc" font-size="17">zero alerts (100% utility retained).</text>
    <text x="1835" y="848" text-anchor="end" font-size="13.5" font-weight="800" fill="#15803d">Workspace Sandboxed</text>
  </g>

  <!-- VIOLATION BLOCKED: Deterministic Deny -->
  <g filter="url(#cardShadow)">
    <rect x="1460" y="875" width="398" height="175" rx="12" fill="#ffffff" stroke="#dc2626" stroke-width="2"/>
    <rect x="1460" y="875" width="398" height="5" rx="2.5" fill="#b91c1c"/>
    <text x="1485" y="912" class="badge-type" fill="#dc2626">VIOLATION BLOCKED (RED)</text>
    <text x="1485" y="946" class="card-title" font-size="24">Deterministic Deny</text>
    <text x="1485" y="982" class="card-desc" font-size="17">Unauthorized call halted at boundary;</text>
    <text x="1485" y="1010" class="card-desc" font-size="17">zero writes or secrets leak to host.</text>
    <text x="1835" y="1038" text-anchor="end" font-size="13.5" font-weight="800" fill="#b91c1c">0.0% ASR Enforcement</text>
  </g>

  <!-- Legend -->
  <g transform="translate(60, 1095)">
    <circle cx="10" cy="10" r="7" fill="#ea580c"/>
    <text x="26" y="16" class="legend-text">Attack Lifecycle Flow</text>

    <circle cx="280" cy="10" r="7" fill="#2563eb"/>
    <text x="296" y="16" class="legend-text">Benign Task Flow</text>

    <circle cx="530" cy="10" r="7" fill="#7c3aed"/>
    <text x="546" y="16" class="legend-text">Tool Proposal Dispatch</text>

    <circle cx="820" cy="10" r="7" fill="#16a34a"/>
    <text x="836" y="16" class="legend-text">Authorized Execution (Pass)</text>

    <circle cx="1140" cy="10" r="7" fill="#dc2626"/>
    <text x="1156" y="16" class="legend-text">Deterministic Deny (Block)</text>
  </g>

  <!-- Footer -->
  <text x="60" y="1165" class="footer-text">Research Poster · Cross-Lingual Agent Skill Poisoning · Threat Lifecycle &amp; Mitigation Architecture</text>
</svg>"""

    with open("poster/threat_lifecycle.svg", "w", encoding="utf-8") as f:
        f.write(threat_svg)
    cairosvg.svg2png(url="poster/threat_lifecycle.svg", write_to="poster/threat_lifecycle.png", output_width=1920, output_height=1200)
    print("threat_lifecycle.png generated successfully!")


def generate_defense_seam():
    defense_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1920 1200" width="1920" height="1200">
  <defs>
    <marker id="arrowPurple" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#7c3aed"/>
    </marker>
    <marker id="arrowOrange" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#ea580c"/>
    </marker>
    <marker id="arrowGreen" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#16a34a"/>
    </marker>
    <marker id="arrowRed" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#dc2626"/>
    </marker>
    <filter id="cardShadow" x="-10%" y="-10%" width="120%" height="130%">
      <feDropShadow dx="0" dy="4" stdDeviation="8" flood-color="#0f172a" flood-opacity="0.08"/>
    </filter>
    <style>
      text { font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }
      .main-title { font-size: 42px; font-weight: 800; fill: #0a1e38; letter-spacing: -0.5px; }
      .main-sub { font-size: 21px; font-weight: 500; fill: #475569; }
      .container-header { font-size: 19px; font-weight: 800; letter-spacing: 0.8px; }
      .container-sub { font-size: 15.5px; font-weight: 500; fill: #64748b; }
      .badge-type { font-size: 15px; font-weight: 800; letter-spacing: 0.8px; }
      .card-title { font-size: 27px; font-weight: 800; fill: #0f172a; letter-spacing: -0.3px; }
      .card-desc { font-size: 18px; font-weight: 500; fill: #334155; }
      .tech-pill { font-size: 16px; font-weight: 700; }
      .flow-label { font-size: 15px; font-weight: 800; }
      .legend-text { font-size: 17px; font-weight: 600; fill: #475569; }
      .footer-text { font-size: 15px; font-weight: 500; fill: #94a3b8; }
      .inv-item-title { font-size: 18px; font-weight: 800; fill: #0f172a; }
      .inv-item-desc { font-size: 15px; font-weight: 500; fill: #475569; }
    </style>
  </defs>

  <rect width="1920" height="1200" fill="#ffffff"/>

  <!-- Title & Subtitle -->
  <text x="960" y="52" text-anchor="middle" class="main-title">Deterministic Authorization Seam: Execution Boundary Architecture</text>
  <text x="960" y="85" text-anchor="middle" class="main-sub">Direct mediation of candidate tool proposals between Reasoning Plane and external Tool Adapters</text>

  <!-- Container 1: Reasoning Plane (Untrusted Influence) -->
  <rect x="40" y="110" width="460" height="955" rx="16" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2.2" stroke-dasharray="8 6"/>
  <text x="65" y="145" class="container-header" fill="#2563eb">REASONING PLANE (UNTRUSTED)</text>
  <text x="65" y="172" class="container-sub">Model generates tool proposals via ReAct planning</text>

  <!-- Container 2: Deterministic Authorization Seam (Enforcement Gate) -->
  <rect x="530" y="110" width="860" height="955" rx="16" fill="#f0fdfa" stroke="#0d9488" stroke-width="2.4" stroke-dasharray="8 6"/>
  <text x="555" y="145" class="container-header" fill="#0d9488">DETERMINISTIC AUTHORIZATION SEAM</text>
  <text x="555" y="172" class="container-sub">In-process execution boundary intercepts dispatch(request, context)</text>

  <!-- Container 3: Execution Boundary & Tool Adapters (MAC Boundary) -->
  <rect x="1420" y="110" width="460" height="955" rx="16" fill="#f8fafc" stroke="#94a3b8" stroke-width="2.2" stroke-dasharray="8 6"/>
  <text x="1445" y="145" class="container-header" fill="#334155">EXECUTION BOUNDARY &amp; ADAPTERS</text>
  <text x="1445" y="172" class="container-sub">Strict Mandatory Access Control (MAC) boundary</text>

  <!-- NODE 1: Proposed Tool Call (Left Top) -->
  <g filter="url(#cardShadow)">
    <rect x="65" y="200" width="410" height="385" rx="12" fill="#ffffff" stroke="#3b82f6" stroke-width="2"/>
    <rect x="65" y="200" width="410" height="6" rx="3" fill="#2563eb"/>
    <text x="90" y="242" class="badge-type" fill="#2563eb">PROPOSED TOOL INVOCATION</text>
    <text x="90" y="282" class="card-title">Reasoning Plane: Call</text>
    <text x="90" y="328" class="card-desc">Model proposes tool_name and</text>
    <text x="90" y="362" class="card-desc">parameters from untrusted skill</text>
    <text x="90" y="396" class="card-desc">manifests during autonomous planning.</text>
    <rect x="90" y="505" width="360" height="46" rx="8" fill="#eff6ff" stroke="#bfdbfe" stroke-width="1.2"/>
    <text x="270" y="534" text-anchor="middle" class="tech-pill" fill="#1d4ed8">dispatch(request, context)</text>
  </g>

  <!-- NODE 2: Session Context & Tokens (Left Bottom) -->
  <g filter="url(#cardShadow)">
    <rect x="65" y="635" width="410" height="385" rx="12" fill="#ffffff" stroke="#64748b" stroke-width="2"/>
    <rect x="65" y="635" width="410" height="6" rx="3" fill="#475569"/>
    <text x="90" y="677" class="badge-type" fill="#475569">PROVENANCE &amp; STATE</text>
    <text x="90" y="717" class="card-title">Session Context &amp; Tokens</text>
    <text x="90" y="763" class="card-desc">Carries verified capability tokens,</text>
    <text x="90" y="797" class="card-desc">session credentials, and untrusted</text>
    <text x="90" y="831" class="card-desc">Data Plane taint history across turns.</text>
    <rect x="90" y="940" width="360" height="46" rx="8" fill="#f1f5f9" stroke="#cbd5e1" stroke-width="1.2"/>
    <text x="270" y="969" text-anchor="middle" class="tech-pill" fill="#334155">Ephemeral Auth Tokens</text>
  </g>

  <!-- CONNECTOR: Proposed Call -> Policy Gate -->
  <path d="M 475 392 H 560" fill="none" stroke="#7c3aed" stroke-width="3" marker-end="url(#arrowPurple)"/>
  <rect x="483" y="379" width="70" height="26" rx="4" fill="#ffffff" stroke="#ddd6fe" stroke-width="1.5"/>
  <text x="518" y="397" text-anchor="middle" class="flow-label" fill="#7c3aed">Proposal</text>

  <!-- CONNECTOR: Context Tokens -> Checks -->
  <path d="M 475 827 H 560" fill="none" stroke="#ea580c" stroke-width="3" marker-end="url(#arrowOrange)"/>
  <rect x="486" y="814" width="64" height="26" rx="4" fill="#ffffff" stroke="#fed7aa" stroke-width="1.5"/>
  <text x="518" y="832" text-anchor="middle" class="flow-label" fill="#ea580c">Tokens</text>

  <!-- NODE 3: Policy Enforcement Module (Seam Top) -->
  <g filter="url(#cardShadow)">
    <rect x="560" y="200" width="800" height="385" rx="12" fill="#ffffff" stroke="#059669" stroke-width="2.2"/>
    <rect x="560" y="200" width="800" height="6" rx="3" fill="#047857"/>
    <text x="590" y="242" class="badge-type" fill="#059669">EXECUTION INTERCEPTOR GATE</text>
    <text x="590" y="282" class="card-title" font-size="28">Policy Enforcement Module</text>
    <text x="590" y="328" class="card-desc" font-size="18.5">In-process security gate mediates adapter calls independently of model reasoning.</text>
    <text x="590" y="362" class="card-desc" font-size="18.5">Zero bypass surface for prompt injections across EN, BN, and BN-EN registers.</text>
    <text x="590" y="396" class="card-desc" font-size="18.5">Guarantees deterministic fail-closed safety with 0.037ms latency overhead.</text>
    <rect x="590" y="505" width="740" height="46" rx="8" fill="#ecfdf5" stroke="#a7f3d0" stroke-width="1.2"/>
    <text x="960" y="534" text-anchor="middle" class="tech-pill" fill="#065f46">Deterministic Invariant Enforcement (0.037ms · 0.0% False Denials)</text>
  </g>

  <!-- CONNECTOR: Policy Module -> Invariant Checks (Vertical) -->
  <path d="M 960 585 V 630" fill="none" stroke="#7c3aed" stroke-width="3" marker-end="url(#arrowPurple)"/>

  <!-- NODE 4: Four Invariant Validation Controls (Seam Bottom) -->
  <g filter="url(#cardShadow)">
    <rect x="560" y="635" width="800" height="385" rx="12" fill="#ffffff" stroke="#059669" stroke-width="2.2"/>
    <rect x="560" y="635" width="800" height="6" rx="3" fill="#047857"/>
    <text x="590" y="677" class="badge-type" fill="#059669">INVARIANT VALIDATION ENGINE</text>
    <text x="590" y="717" class="card-title" font-size="28">Four Pre-Execution Invariant Controls</text>

    <!-- 4 Sub-blocks -->
    <!-- Block 1: Capability Tokens -->
    <rect x="590" y="745" width="355" height="85" rx="8" fill="#f0fdf4" stroke="#bbf7d0" stroke-width="1"/>
    <text x="605" y="776" class="inv-item-title">1. Capability Tokens</text>
    <text x="605" y="806" class="inv-item-desc">Cryptographic intent token validation.</text>

    <!-- Block 2: Path Invariants -->
    <rect x="975" y="745" width="355" height="85" rx="8" fill="#f0fdf4" stroke="#bbf7d0" stroke-width="1"/>
    <text x="990" y="776" class="inv-item-title">2. Path Invariants</text>
    <text x="990" y="806" class="inv-item-desc">realpath() workspace sandboxing.</text>

    <!-- Block 3: Workspace Sandbox -->
    <rect x="590" y="845" width="355" height="85" rx="8" fill="#f0fdf4" stroke="#bbf7d0" stroke-width="1"/>
    <text x="605" y="876" class="inv-item-title">3. Workspace Sandbox</text>
    <text x="605" y="906" class="inv-item-desc">Unprivileged container isolation.</text>

    <!-- Block 4: Language Invariance -->
    <rect x="975" y="845" width="355" height="85" rx="8" fill="#f0fdf4" stroke="#bbf7d0" stroke-width="1"/>
    <text x="990" y="876" class="inv-item-title">4. Language Invariance</text>
    <text x="990" y="906" class="inv-item-desc">Raw dispatch check (100% register agnostic).</text>

    <!-- Code strip -->
    <rect x="590" y="945" width="740" height="46" rx="8" fill="#064e3b" stroke="#047857" stroke-width="1.2"/>
    <text x="960" y="974" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="17" font-weight="700" fill="#a7f3d0">dispatch(req, ctx) -&gt; verify(token) -&gt; assert(path) -&gt; execute()</text>
  </g>

  <!-- CONNECTOR: Policy Gate -> Authorized Execution (Pass) -->
  <path d="M 1360 392 H 1445" fill="none" stroke="#16a34a" stroke-width="3" marker-end="url(#arrowGreen)"/>
  <rect x="1369" y="379" width="66" height="26" rx="4" fill="#ffffff" stroke="#86efac" stroke-width="1.5"/>
  <text x="1402" y="397" text-anchor="middle" class="flow-label" fill="#16a34a">Passed</text>

  <!-- CONNECTOR: Invariant Checks -> Deterministic Deny (Block) -->
  <path d="M 1360 827 H 1445" fill="none" stroke="#dc2626" stroke-width="3" marker-end="url(#arrowRed)"/>
  <rect x="1366" y="814" width="72" height="26" rx="4" fill="#ffffff" stroke="#fca5a5" stroke-width="1.5"/>
  <text x="1402" y="832" text-anchor="middle" class="flow-label" fill="#dc2626">Violation</text>

  <!-- NODE 5: Tool Adapter Execution (Right Top) -->
  <g filter="url(#cardShadow)">
    <rect x="1445" y="200" width="410" height="385" rx="12" fill="#ffffff" stroke="#16a34a" stroke-width="2"/>
    <rect x="1445" y="200" width="410" height="6" rx="3" fill="#15803d"/>
    <text x="1470" y="242" class="badge-type" fill="#16a34a">COMPLIANT EXECUTION (PASS)</text>
    <text x="1470" y="282" class="card-title">Tool Adapter Execution</text>
    <text x="1470" y="328" class="card-desc">Permitted tool executes inside</text>
    <text x="1470" y="362" class="card-desc">container sandbox; zero canary</text>
    <text x="1470" y="396" class="card-desc">telemetry triggered (100% utility).</text>
    <rect x="1470" y="505" width="360" height="46" rx="8" fill="#f0fdf4" stroke="#86efac" stroke-width="1.2"/>
    <text x="1650" y="534" text-anchor="middle" class="tech-pill" fill="#15803d">Bash / Git / API Adapters</text>
  </g>

  <!-- NODE 6: Deterministic Deny (Right Bottom) -->
  <g filter="url(#cardShadow)">
    <rect x="1445" y="635" width="410" height="385" rx="12" fill="#ffffff" stroke="#dc2626" stroke-width="2"/>
    <rect x="1445" y="635" width="410" height="6" rx="3" fill="#b91c1c"/>
    <text x="1470" y="677" class="badge-type" fill="#dc2626">VIOLATION BLOCKED (DENY)</text>
    <text x="1470" y="717" class="card-title">Deterministic Deny</text>
    <text x="1470" y="763" class="card-desc">Unauthorized path traversal or</text>
    <text x="1470" y="797" class="card-desc">secret exfiltration halted before</text>
    <text x="1470" y="831" class="card-desc">adapter call; zero writes reach host.</text>
    <rect x="1470" y="940" width="360" height="46" rx="8" fill="#fef2f2" stroke="#fca5a5" stroke-width="1.2"/>
    <text x="1650" y="969" text-anchor="middle" class="tech-pill" fill="#b91c1c">MAC Invariant Rejection</text>
  </g>

  <!-- Legend -->
  <g transform="translate(65, 1095)">
    <circle cx="10" cy="10" r="7" fill="#7c3aed"/>
    <text x="26" y="16" class="legend-text">Tool Call Proposal</text>

    <circle cx="260" cy="10" r="7" fill="#ea580c"/>
    <text x="276" y="16" class="legend-text">Context &amp; Token Evaluation</text>

    <circle cx="580" cy="10" r="7" fill="#16a34a"/>
    <text x="596" y="16" class="legend-text">Authorized Execution (Pass)</text>

    <circle cx="890" cy="10" r="7" fill="#dc2626"/>
    <text x="906" y="16" class="legend-text">Deterministic Policy Deny (Block)</text>
  </g>

  <!-- Footer -->
  <text x="65" y="1165" class="footer-text">Research Poster · Deterministic Authorization Seam Architecture &amp; Execution Boundary</text>
</svg>"""

    with open("poster/defense_seam_architecture.svg", "w", encoding="utf-8") as f:
        f.write(defense_svg)
    cairosvg.svg2png(url="poster/defense_seam_architecture.svg", write_to="poster/defense_seam_architecture.png", output_width=1920, output_height=1200)
    print("defense_seam_architecture.png generated successfully!")

if __name__ == "__main__":
    generate_threat_lifecycle()
    generate_defense_seam()
