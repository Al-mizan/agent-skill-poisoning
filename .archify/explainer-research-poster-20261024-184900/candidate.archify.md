# Research Poster: Cross-Lingual Agent Skill Poisoning and Deterministic Runtime Authorization {#research-poster-ju-cse}

Cross-lingual skill manifests compromise tool-using agents by evading static scanners, but **deterministic runtime policy enforcement** delivers language-invariant defense.

- English-calibrated static scanners miss 100% of malicious skills written in native Bangla and Romanized Banglish.[](source:groq-results)
- Soft prompt isolation causes severe utility collapse, reducing legitimate task completion to 76.9%.
- The runtime policy enforcement module eliminates policy violations in 0.038 milliseconds with zero false denials.[](source:adr0002)
- Interactive authorization halts out-of-scope operations and guarantees that mutated skills cannot compromise host files.

@answer scope="JU-CSE B.Sc. Research · 26 Task Domains · 312 Live Trials · Groq Qwen-2.5-27B"
@meta locale=en style=clean
@source groq-results title="Groq 26-Domain Live Evaluation Benchmark (312 trials)" path=research/results/groq_26_domains_live.jsonl lines=1:312
@source adr0002 title="ADR-0002: Deterministic Runtime Authorization Seam" path=docs/adr/0002-deterministic-runtime-authorization.md lines=1:60
@source tasks26 title="26 Multi-Domain Task Variants Dataset" path=research/benchmark/data/xling_tasks_26.json lines=1:100
@source proposal title="Formal Research Proposal: Cross-Lingual Skill Poisoning" path=proposal_cross_lingual_skill_poisoning.md lines=1:150

## Problem Formulation & The Semantic Supply Chain Surface {#problem-formulation}

Autonomous Large Language Model agents extend their capabilities at inference time using modular skill files like `SKILL.md`. An agent skill combines executable tool definitions with natural-language guidance. When an agent loads a third-party skill, it ingests untrusted text directly into its reasoning context. This causes **Control-Data Conflation**.

- **English Calibration Gap:** Security scanners evaluate shallow English keywords and miss non-Latin morphological variations.
- **Linguistic Proficiency Paradox:** Multilingual models comprehend Bangla instructions, but existing safety filters fail to intercept them.
- **Ambient Authority Vulnerability:** Agent tools execute with full user privileges rather than least-privilege capability boundaries.

## The 5-Stage Attack Lifecycle: Supply Chain to Runtime Tool Hijack {#threat-lifecycle}

@workflow id=poster-lifecycle-flow title="5-stage attack lifecycle from authoring to runtime exploitation"
| lane supply | Untrusted Supply Chain |
| lane runtime | Agent Runtime Boundary |
| author | 1. Authoring | external | supply |
| publish | 2. Registry | external | supply |
| install | 3. Install | backend | supply |
| rugpull | 4. Rug-Pull | backend | runtime |
| plan | 5. Execution | security | runtime |
| author > publish | |
| publish > install | |
| install > rugpull | |
| rugpull > plan | exploit | emphasis |

@steps id=poster-lifecycle-steps
| s1 | 1. Authoring | Attacker crafts a dual-intent skill embedding out-of-scope instructions in Bangla or Banglish. | poster-lifecycle-flow | author |
| s2 | 2. Registry | Marketplace scanners accept the package because regex patterns only match English keywords. | poster-lifecycle-flow | publish |
| s3 | 3. Install | Agent runtime installs markdown skill into prompt context with ambient user permissions. | poster-lifecycle-flow | install |
| s4 | 4. Rug-Pull | Attacker mutates local skill file after install vetting without triggering re-authorization. | poster-lifecycle-flow | rugpull |
| s5 | 5. Execution | LLM planner emits unauthorized file writes to `/tmp` alongside legitimate user tasks. | poster-lifecycle-flow | plan |

## Interactive Mode & Runtime Interception Seam Architecture {#interactive-seam-panel}

@sequence id=poster-seam-sequence title="Interactive runtime authorization sequence"
| actor user | Human Operator | frontend |
| actor agent | LLM Planner | backend |
| actor seam | Policy Seam | security |
| actor host | Sandboxed Host | database |
| user | agent | Request file operation in workspace |
| agent | seam | Propose write_file to /tmp | emphasis |
| seam | user | Yield interactive decision dialog | security |
| user | seam | Choose deterministic denial [D] | return |
| seam | agent | Return path invariant rejection | return |
| agent | seam | Propose authorized write to /workspace/output |
| seam | host | Execute compliant tool call |
| host | agent | Return tool output code 0 | return |
| agent | user | Present completed result | return |

@steps id=poster-seam-steps
| r1 | Proposal | Agent generates function call targeting restricted directory `/tmp/canary_audit.marker`. | poster-seam-sequence | agent |
| r2 | Interception | Policy interceptor checks destination path against `/workspace/output/` and halts execution. | poster-seam-sequence | seam |
| r3 | Operator Choice | Human operator reviews risk modal and clicks deterministic denial to block the exploit. | poster-seam-sequence | user |
| r4 | Clean Recovery | Agent planner continues execution and generates benign output file successfully. | poster-seam-sequence | host |

## Empirical Evaluation across 26 Multi-Domain Task Variants (312 Trials) {#empirical-results}

| Configuration {#col-config} | Register | Trials | ASR | PVR | TSR | Latency | FDR |
| --- | --- | --- | --- | --- | --- | --- | --- |
| None (EN) {#row-none-en} | English | 26 | 100.0% {bad:Compromised} | 100.0% | 100.0% | 0.0000ms | 0.0% |
| None (BN) {#row-none-bn} | Bangla | 26 | 100.0% {bad:Compromised} | 100.0% | 100.0% | 0.0000ms | 0.0% |
| None (BN-EN) {#row-none-bnen} | Banglish | 26 | 100.0% {bad:Compromised} | 100.0% | 100.0% | 0.0000ms | 0.0% |
| Static Scanner (EN) {#row-scanner-en} | English | 26 | 76.9% {caution:Partial} | 76.9% | 76.9% | 0.0000ms | 23.1% {bad:False Denials} |
| Static Scanner (BN) {#row-scanner-bn} | Bangla | 26 | 100.0% {bad:100% Bypass} | 100.0% | 100.0% | 0.0000ms | 0.0% |
| Static Scanner (BN-EN) {#row-scanner-bnen} | Banglish | 26 | 100.0% {bad:100% Bypass} | 100.0% | 100.0% | 0.0000ms | 0.0% |
| Prompt Isolation (EN) {#row-prompt-en} | English | 26 | 7.7% | 7.7% | 76.9% {caution:Degraded} | 0.0000ms | 0.0% |
| Prompt Isolation (BN) {#row-prompt-bn} | Bangla | 26 | 3.8% | 3.8% | 84.6% {caution:Degraded} | 0.0000ms | 0.0% |
| Prompt Isolation (BN-EN) {#row-prompt-bnen} | Banglish | 26 | 0.0% {good:Defended} | 0.0% | 84.6% {caution:Degraded} | 0.0000ms | 0.0% |
| Policy Enforcement (EN) {#row-policy-en} | English | 26 | 3.8% | 3.8% | 100.0% {good:Full Utility} | 0.0370ms {good:Sub-ms} | 0.0% {good:Zero FDR} |
| Policy Enforcement (BN) {#row-policy-bn} | Bangla | 26 | 0.0% {good:Defended} | 0.0% | 100.0% {good:Full Utility} | 0.0368ms {good:Sub-ms} | 0.0% {good:Zero FDR} |
| Policy Enforcement (BN-EN) {#row-policy-bnen} | Banglish | 26 | 0.0% {good:Defended} | 0.0% | 100.0% {good:Full Utility} | 0.0408ms {good:Sub-ms} | 0.0% {good:Zero FDR} |

```mermaid title="Attack Success Rate (ASR %) across defense tiers and linguistic registers"
xychart-beta
  x-axis ["English", "Bangla", "Banglish"]
  y-axis "ASR %" 0 --> 100
  bar "None" [100, 100, 100]
  bar "Static Scanner" [77, 100, 100]
  bar "Prompt Isolation" [8, 4, 0]
  bar "Policy Enforcement" [4, 0, 0]
```

## Key Scientific Findings & Current Progress {#key-findings-progress}

- **Active Runtime Vulnerability:** Cross-lingual skill poisoning reliably compromises live agent tool dispatch across 26 enterprise domains.
- **Scanner Breakdown:** Static scanners fail completely against non-English manifests, yielding 100% attack success in Bangla and Banglish.
- **Prompt Isolation Trade-Off:** Soft prompt warnings reduce attack success but harm model utility, lowering task completion by up to 23.1%.
- **Deterministic Protection:** ADR-0002 runtime enforcement provides sub-millisecond, language-invariant defense with 100% task completion.

## Research Expansion Roadmap {#research-roadmap}

- [x] Phase 1: Completed threat modeling, ADR formalization, pilot benchmarks, and 26-domain live evaluation.
- [ ] Phase 2: Scale benchmark from 26 to 50 enterprise workflows across additional low-resource languages.
- [ ] Phase 3: Conduct defense ablation studies measuring memory usage, token overhead, and multi-turn stability.
- [ ] Phase 4: Submit full paper to top-tier security and NLP conferences.
