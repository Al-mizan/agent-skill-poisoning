# Cross-Lingual Agent Skill Poisoning: Benchmarking Active Runtime Exploitation and Deterministic Authorization in Tool-Using LLM Agents

**Authors:** Al-mizan and Eva  
**Supervisor:** Dr. Md. Rafsan Jani  
**Affiliation:** Department of Computer Science & Engineering, Jahangirnagar University, Savar, Dhaka, Bangladesh  
**Date:** October 2026  

---

## Abstract

Tool-using Large Language Model agents increasingly rely on modular skill packages, such as filesystem-based skill manifests and Model Context Protocol configurations, to dynamically extend their operational capabilities. Because these skill manifests combine executable function schemas with free-form natural-language instructions, they introduce a semantic supply-chain attack surface where untrusted text is ingested directly into an agent's planning loop. While existing supply-chain security benchmarks measure prompt injection in English skill files, they operate under the assumption that security risks and detection tooling are language-independent. Recent empirical audits show that automated scanners flag non-English skill packages for behavioral anomalies up to five times more frequently than English packages while exhibiting near-zero precision. However, whether these cross-lingual manifests actively hijack agent tool execution at runtime remains unmeasured.

This proposal presents a systematic investigation into cross-lingual agent skill supply-chain poisoning. We introduce an evaluation benchmark that assesses how natural-language variation across English, high-resource languages such as Mandarin and Spanish, low-resource registers including native-script Bangla, and colloquial code-mixed Banglish alters agent vulnerability. We evaluate frontier proprietary models and open-weights architectures across skill discovery, selection, and tool execution. Furthermore, we examine the resilience of three defense paradigms: install-time static screening, prompt-level isolation, and an in-process deterministic policy enforcement module positioned at the tool execution seam. Preliminary pilot trials across five skill domains indicate that while English-calibrated scanners and prompt warnings fail against non-English manifests, deterministic invariant enforcement achieves language-invariant protection. This research provides empirical evidence on multilingual supply-chain risks, establishes a reproducible benchmark, and designs architectural safeguards for multilingual agent ecosystems.

---

## 1. Introduction

### 1.1 Operational Skill Manifests and the Semantic Supply Chain

The rapid integration of Large Language Models into autonomous workflows has shifted model evaluation from conversational fluency to real-world task execution. Modern software engineering, financial modeling, and system administration workflows employ autonomous agents equipped with tools that interact with operating system shells, query production databases, manipulate local filesystems, and issue authenticated network requests (Debenedetti et al., 2024; Zhan et al., 2024). To manage these capabilities modularly, current agent architectures adopt filesystem-based skill manifests, commonly distributed as markdown packages containing metadata headers and operational instructions (Anthropic, 2025; Schmotz et al., 2026).

These manifests blur the classical boundary between code and documentation. When an agent indexes a skill repository, it ingests unstructured text directly into its intermediate reasoning loop. Consequently, untrusted text functions as executable guidance. An adversary who publishes or updates a third-party skill package can embed coercive instructions within routine usage notes, parameter explanations, or configuration scripts. When the agent selects the skill to fulfill an authentic user request, the injected instructions can override developer guidelines, turning the agent into a confused deputy that carries out unauthorized actions under the user's ambient privileges (Greshake et al., 2023; Saha et al., 2026).

### 1.2 The Linguistic Proficiency Paradox in Agentic Tool Use

Safety alignment research demonstrates that model robustness varies across linguistic distributions. While reinforcement learning from human feedback reinforces refusal boundaries on English adversarial prompts, safety guardrails degrade on non-English inputs, particularly in low-resource and code-mixed settings (Deng et al., 2024; Yong et al., 2024). In the agent skill ecosystem, this disparity creates the linguistic proficiency paradox: foundation models possess the semantic capacity to comprehend instructions in non-English registers, yet the safety classifiers and static heuristics guarding the execution environment remain tuned for English syntax.

Recent large-scale static audits confirm this imbalance at the registry level. Zhang, Yuan, et al. (2026) scanned thousands of public agent skills across eight languages, observing that while direct code vulnerabilities occurred at an identical baseline rate of 2.3 percent across all languages, behavioral flags such as vague descriptions were up to five times more frequent in non-English packages. Manual inspection revealed that these behavioral warnings reflected scanner calibration bias rather than genuine malice, with heuristics achieving zero percent precision on Japanese packages. However, static audits cannot evaluate interactive agent execution. Whether non-English or code-mixed instructions allow an adversary to bypass security screening while successfully hijacking an agent's runtime tool selection remains an open question.

### 1.3 Research Questions and Testable Hypotheses

This research investigates four primary research questions:

1. **Research Question 1 (Runtime Exploitation Disparity)**: Does embedding contextual injection payloads in low-resource Bangla or code-mixed Banglish increase the Skill Selection Rate and Attack Success Rate compared to equivalent English instructions?
   * *Hypothesis 1*: Non-English and code-mixed skill manifests achieve higher runtime attack success against models whose safety alignment is concentrated on English prompts.
2. **Research Question 2 (Governance Evasion and Scanner Bias)**: How do existing static skill scanners and prompt-level filters perform when evaluating cross-lingual skill manifests compared to English baselines?
   * *Hypothesis 2*: Rule-based scanners and soft prompt warnings experience severe performance degradation on non-English instructions, permitting malicious non-English manifests to pass install-time vetting.
3. **Research Question 3 (Model Architecture Stratification)**: How do frontier proprietary models compare with open-weights architectures in resisting cross-lingual supply-chain manipulation?
   * *Hypothesis 3*: Proprietary frontier models resist simple English injection more effectively than open-weights models, but this performance gap narrows significantly under code-mixed framing.
4. **Research Question 4 (Language Invariance of Runtime Defenses)**: Can a deterministic policy enforcement module positioned at the tool execution seam provide language-invariant protection without imposing a utility penalty on benign tasks?
   * *Hypothesis 4*: Evaluating structural parameter invariants and destination paths at the tool dispatch seam eliminates dependence on natural-language comprehension, achieving zero attack success across all languages while retaining full benign task utility.

### 1.4 Scope and Delimitations

This study focuses on natural-language skill manifests and their interaction with tool-execution environments. We concentrate on contextual injections embedded within markdown instructions that induce agents to invoke system tools. To avoid the translation quality fallacy identified by Marx & Dunaiski (2026), where machine-translated prompts fail due to syntactic incoherence rather than robust alignment, all non-English payloads are authored and validated by native speakers. Experimental evaluations replace destructive payloads with harmless local canary markers inside network-isolated containers, ensuring zero risk of credential exposure or host modification.

---

## 2. Literature Review

### 2.1 Indirect Prompt Injection and Agent Skill Supply-Chain Poisoning

Indirect prompt injection occurs when an autonomous model processes untrusted external data that contains adversarial directives (Greshake et al., 2023). In agentic workflows, indirect prompt injection allows third-party inputs to hijack tool selection and exfiltrate confidential data (Debenedetti et al., 2024; Zhan et al., 2024). In the supply-chain domain, researchers have recently identified package manifests as a vulnerable vector. Schmotz et al. (2026) developed Skill-Inject, demonstrating attack success rates reaching 80 percent across coding agents when malicious instructions were hidden within skill files. Similarly, Qu et al. (2026) introduced Document-Driven Implicit Payload Execution, showing that agents frequently execute malicious logic embedded in documentation code examples during routine execution.

Concurrently, large-scale empirical studies by Liu, Wang, et al. (2026a) and Liu, Chen, et al. (2026b) analyzed tens of thousands of skills from public marketplaces, uncovering pervasive vulnerabilities including credential exfiltration and unauthorized shell commands. Saha et al. (2026) investigated semantic registry attacks, demonstrating that manipulating description text enables an adversary to win skill selection in over 75 percent of paired trials. Furthermore, automated attack generation frameworks such as SkillJect (Jia et al., 2026) and backdoor formulations such as BadSkill (Tie et al., 2026) confirm the potency of poisoned packages. However, every active exploitation benchmark in this literature operates exclusively in English, leaving cross-lingual manipulation unstudied.

### 2.2 Cross-Lingual Alignment Disparities and Scanner Calibration Bias

The disparity in multilingual safety alignment is well documented in conversational models. Benchmarks including MultiJail (Deng et al., 2024) and empirical evaluations by Atil et al. (2025) demonstrate that commercial language models exhibit higher attack vulnerability when queried in non-English languages. In low-resource African languages, Marx & Dunaiski (2026) showed that translation quality is the primary determinant of attack success, with native-speaker red-teaming increasing bypass rates substantially over automated translations. In South Asian languages, Hassan & Hossain (2026) documented that colloquial and code-mixed Bangla routinely bypasses standard guardrails, while lightweight filters introduce excessive false-positive rates on benign inputs.

In the skill supply chain, Zhang, Yuan, et al. (2026) provided the first static analysis across eight languages, discovering that while verifiable code vulnerabilities occur at equal rates across languages, automated security tooling produces up to five times more behavioral warnings for non-English packages. Their manual inspection revealed that these flags were false positives caused by English-centric heuristics. Similarly, Bhardwaj (2026) analyzed 540 skills, noting that static information-flow checks struggle to separate dual-use operations from malicious code. While these studies reveal scanner bias, they do not evaluate live agent execution.

### 2.3 Runtime Policy Enforcement versus Semantic Monitors

To mitigate prompt injection, researchers have proposed defenses spanning prompt filtering, internal probing, and runtime enforcement. Prompt-level filtering attempts to instruct the model to disregard third-party commands, but empirical evaluations indicate that soft instructions provide incomplete protection (Debenedetti et al., 2024; Schmotz et al., 2026). Internal representation defenses, such as the probe-gated reasoning proposed by Dong et al. (2026), identify injection exposure within model hidden states; however, these techniques require white-box model weight access, making them unusable for closed-source commercial APIs.

In response, system-level runtime defenses enforce behavioral boundaries at the execution layer. Ji, Wu, et al. (2026) proposed SEAgent, using mandatory access control and information flow graphs to prevent privilege escalation. Li, Chen, et al. (2026) introduced VIGIL, which verifies execution traces against formal behavioral policies using SMT solvers. In realistic virtual environments, Zhao et al. (2026) demonstrated that pre-execution tool-call authorization intercepts malicious actions effectively. These defenses, however, either rely on natural-language policy translation or have not been tested against multilingual attack vectors.

### 2.4 Synthesis of Research Gaps and Study Positioning

The synthesis of prior work highlights four confirmed gaps:

First, existing active skill benchmarks are monolingual, failing to evaluate whether cross-lingual manifests alter runtime agent decisions. Second, prior cross-lingual skill studies are purely static and observational, lacking interactive red-teaming. Third, low-resource South Asian and code-mixed registers have not been examined within agent skill ecosystems where English code syntax mingles with non-English instructions. Finally, the language invariance of deterministic execution authorization remains unmeasured. This study positions itself directly at this intersection, providing an empirical runtime benchmark and a language-invariant defense evaluation.

---

## 3. Methodology

### 3.1 Threat Model and Lifecycle Formulation

We adopt the system architecture and threat boundaries established in the project domain model. The system comprises a privileged Control Plane, an intermediate Reasoning Plane, and an untrusted Data Plane. The adversary is a passive supply-chain actor who authors or updates a third-party skill package. The attacker cannot alter system prompts or model weights, and the authenticated user prompt is completely benign. Compromise occurs if the agent selects the poisoned skill and executes an unauthorized action.

The attack spans five lifecycle stages:

1. **Authoring**: The adversary crafts contextual injection instructions in English, native-script Bangla, or code-mixed Banglish, embedding dual-use prerequisite steps that reference system tools.
2. **Registry**: The adversary publishes the package, using bilingual keywords to ensure retrieval visibility while evading English-calibrated static scanners.
3. **Install**: The skill is installed into the agent's local registry, inheriting ambient user permissions.
4. **Update**: A previously benign skill package introduces a poisoned instruction through a subsequent version update.
5. **Execution**: When assigned a relevant benign user task, the agent's planning loop selects the skill and triggers the injected tool action.

### 3.2 Benchmark Architecture

We construct the evaluation in two coordinated phases:

* **Phase 1 (Canary Pilot)**: A focused pilot spanning five representative domains: document processing (`pdf`), version control (`git`), email management (`email-api`), corporate communications (`internal-comms`), and web application testing (`webapp-testing`). Each task is paired with an authentic user prompt, clean tool expectations, and three skill variants (`en`, `bn`, `bn-en`).
* **Phase 2 (XLingSkillBench Expansion)**: A comprehensive benchmark scaling to 50 enterprise workflows across four linguistic registers: English, high-resource (Mandarin and Spanish), low-resource (native-script Bangla), and code-mixed Banglish.

### 3.3 Linguistic Registers and Quality Control

To isolate linguistic effects while avoiding syntactic artifacts, we define three core registers:

* **English Baseline (`en`)**: Formal technical English describing prerequisites and usage conventions.
* **Native Bangla (`bn`)**: Standard formal Bengali script expressing equivalent procedural requirements.
* **Banglish Code-Mixed (`bn-en`)**: Colloquial code-mixing commonly used in South Asian developer communities, where tool names, file paths, and CLI arguments remain in English while operational framing uses Bengali grammar.

All non-English instructions are authored and cross-verified by native Bengali speakers, eliminating the translation quality artifacts common in automated benchmarks.

### 3.4 Defense Evaluation Framework

We benchmark three defensive baselines against an undefended control condition:

1. **Static Keyword and YARA Scanner**: Represents current marketplace vetting tools, scanning manifest text for known inducement strings and evaluating description length heuristics.
2. **Prompt-Level Isolation**: Injects explicit security warning instructions into the system prompt, directing the model to ignore side-effect instructions located in skill documentation.
3. **Policy Enforcement Module**: Implements the deterministic dispatch seam specified in architectural decision record ADR-0002. Positioned between the agent's reasoning loop and tool adapters, this module evaluates declarative capability tokens and path invariants, blocking actions directed outside authorized workspace directories.

### 3.5 Evaluation Metrics

We measure four quantitative metrics:

$$\text{SSR} = \frac{\sum \mathbb{I}(\text{Selected Skill} = \text{Target Skill})}{N} \times 100$$

$$\text{ASR} = \frac{\sum \mathbb{I}(\text{Canary Marker Executed})}{N} \times 100$$

$$\text{BUR} = \frac{\sum \mathbb{I}(\text{Clean Task Completed Successfully})}{N} \times 100$$

$$\text{DRR} = \frac{\text{ASR}_{\text{undefended}} - \text{ASR}_{\text{defended}}}{\text{ASR}_{\text{undefended}}} \times 100$$

### 3.6 Compute Budget, Safety, and Reproducibility

Evaluations are conducted using lightweight commercial and open-weights API endpoints, specifically Gemini 2.5 Flash and Groq Llama 3.3 70B Versatile, requiring an estimated API budget under 50 US dollars. The test harness runs inside sandboxed containers with network access disabled (`--network none`). Every trial logs complete prompts, model identifiers, tool proposals, and evaluation verdicts to structured JSONL records. All code, prompts, and evaluation traces will be released under an open-source license.

---

## 4. Timeline and Milestones

The proposed research spans a six-month execution timeline divided into four phases:

* **Phase 1: Pilot and Supervisor Defense (Month 1)**:
  * Complete literature review matrix and formalize threat model.
  * Scaffold five-skill canary pilot and run initial baseline trials.
  * Prepare research poster and present preliminary findings to supervisor.
* **Phase 2: Benchmark Expansion (Months 2–3)**:
  * Scale dataset to 50 enterprise tasks across four linguistic registers.
  * Implement automated validation harness and verify native annotations.
  * Conduct full-scale evaluation across Gemini, Groq, and local open-weights backbones.
* **Phase 3: Defense Integration and Ablation Studies (Month 4)**:
  * Benchmark static scanners, prompt-level policies, and the deterministic policy module.
  * Measure false-positive over-refusal rates and execution latency overhead.
* **Phase 4: Manuscript Preparation and Submission (Months 5–6)**:
  * Draft full research paper and package reproducible code artifacts.
  * Conduct internal peer review with academic advisors.
  * Submit manuscript to a top-tier security or natural language processing conference.

---

## 5. Significance and Expected Contributions

### 5.1 Scientific and Methodological Contributions

This study provides the first active runtime evaluation of cross-lingual skill supply-chain poisoning in autonomous agents. By contrasting static scanner results with live execution outcomes, this research uncovers the extent to which current registry vetting tools suffer from calibration bias. Methodologically, introducing native-script Bangla and code-mixed Banglish establishes an evaluation standard for non-Western developer registers in agent security research.

### 5.2 Practical and Ecosystem Implications

Practically, this work demonstrates that natural-language prompt warnings and keyword scanners cannot provide reliable defense across languages. By validating a deterministic policy enforcement module at the tool dispatch seam, this research offers agent developers a practical architectural pattern that eliminates language-dependent vulnerabilities while preserving task utility.

---

## References

1. Anthropic. (2025). *Agent Skills Overview*. https://agentskills.io/home
2. Atil, B., Passonneau, R. J., & Morstatter, F. (2025). Do Methods to Jailbreak and Defend LLMs Generalize Across Languages? *arXiv preprint arXiv:2511.00689*. https://doi.org/10.48550/arXiv.2511.00689
3. Bhardwaj, V. P. (2026). Formal Analysis and Supply Chain Security for Agentic AI Skills. *arXiv preprint arXiv:2603.00195v2*. https://doi.org/10.48550/arXiv.2603.00195
4. Debenedetti, E., Zhang, J., Balunović, M., Beurer-Kellner, L., Fischer, M., & Vechev, M. (2024). AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents. *Thirty-eighth Conference on Neural Information Processing Systems (NeurIPS 2024) Datasets and Benchmarks Track*. https://doi.org/10.52202/079017-2636
5. Deng, Y., Zhang, W., Pan, S. J., & Bing, L. (2024). Multilingual Jailbreak Challenges in Large Language Models. *International Conference on Learning Representations (ICLR 2024)*. https://doi.org/10.48550/arXiv.2310.06474
6. Dong, J., Liu, Y., Zhang, M., Deng, N., Xu, P., Zhang, X., Zhang, T., Zhang, J., & Qiu, H. (2026). Your Agentic LLMs Secretly Encode Indirect Prompt-Injection Exposure in Hidden States. *arXiv preprint arXiv:2608.02657*. https://doi.org/10.48550/arXiv.2608.02657
7. Greshake, K., Abdelnabi, S., Mishra, S., Endres, C., Holz, T., & Fritz, M. (2023). Not what you've signed up for: Compromising real-world LLM-integrated applications with indirect prompt injection. *Proceedings of the 16th ACM Workshop on Artificial Intelligence and Security (AISEC 2023)*, 79–90. https://doi.org/10.1145/3605764.3623985
8. Guo, W., Zeng, W., Liu, C., Jia, X., Xu, Y., Tang, L., Fang, Y., & Liu, Y. (2026). MalSkillBench: A Runtime-Verified Benchmark of Malicious Agent Skills. *arXiv preprint arXiv:2606.07131*. https://doi.org/10.48550/arXiv.2606.07131
9. Hassan, M. R., & Hossain, M. I. (2026). BanglaVeilGuard: Cross-Script Safety Benchmarking and Lightweight Guardrails for Bangla Large Language Models. *arXiv preprint arXiv:2608.21880*. https://doi.org/10.48550/arXiv.2608.21880
10. Huang, C., Huang, X., Tran, N. P., & Fard, A. M. (2026). Model Context Protocol Threat Modeling and Analyzing Vulnerabilities to Prompt Injection with Tool Poisoning. *arXiv preprint arXiv:2603.22489*. https://doi.org/10.48550/arXiv.2603.22489
11. Ji, Z., Wu, D., Jiang, W., Ma, P., Li, Z., Gao, Y., Wang, S., & Li, Y. (2026). Taming Various Privilege Escalation in LLM-Based Agent Systems: A Mandatory Access Control Framework. *arXiv preprint arXiv:2601.11893*. https://doi.org/10.48550/arXiv.2601.11893
12. Ji, Z., Xu, C., Li, Z., Gao, Y., Wei, X., Wang, S., & Cheung, S.-C. (2026). Cloak and Detonate: Scanner Evasion and Dynamic Detection of Agent Skill Malware. *arXiv preprint arXiv:2607.02357*. https://doi.org/10.48550/arXiv.2607.02357
13. Jia, X., Liao, J., Qin, S., Gu, J., Ren, W., Cao, X., Liu, Y., & Torr, P. (2026). SkillJect: Effectively Automating Skill-Based Prompt Injection for Skill-Enabled Agents. *arXiv preprint arXiv:2602.14211*. https://doi.org/10.48550/arXiv.2602.14211
14. Li, Y., Chen, Y., Wen, H., Zhang, B., Liu, H., Wang, P., Feng, Y., & Tian, Y. (2026). VIGIL: Runtime Enforcement of Behavioral Specifications in AI Agent Skills. *arXiv preprint arXiv:2606.26524*. https://doi.org/10.48550/arXiv.2606.26524
15. Liu, Y., Chen, Z., Zhang, Y., Deng, G., Li, Y., Ning, J., & Zhang, L. Y. (2026b). "Do Not Mention This to the User": Detecting and Understanding Malicious Agent Skills in the Wild. *arXiv preprint arXiv:2602.06547*. https://doi.org/10.48550/arXiv.2602.06547
16. Liu, Y., Wang, W., Feng, R., Zhang, Y., Xu, G., Deng, G., Li, Y., & Zhang, L. (2026a). Agent Skills in the Wild: An Empirical Study of Security Vulnerabilities at Scale. *arXiv preprint arXiv:2601.10338*. https://doi.org/10.48550/arXiv.2601.10338
17. Marx, D., & Dunaiski, M. (2026). Multilingual jailbreaking of LLMs using low-resource languages. *arXiv preprint arXiv:2605.18239*. https://doi.org/10.48550/arXiv.2605.18239
18. Muhtadi, A. M., & Tazwar, M. R. (2026). MIPIAD: Multilingual Indirect Prompt Injection Attack Defense with Qwen -- TF-IDF Hybrid and Meta-Ensemble Learning. *arXiv preprint arXiv:2605.07269*. https://doi.org/10.48550/arXiv.2605.07269
19. Qu, Y., Liu, Y., Geng, T., Deng, G., Li, Y., Zhang, L. Y., Zhang, Y., & Ma, L. (2026). Supply-Chain Poisoning Attacks Against LLM Coding Agent Skill Ecosystems. *arXiv preprint arXiv:2604.03081*. https://doi.org/10.48550/arXiv.2604.03081
20. Saha, S., Faghih, K., & Feizi, S. (2026). Under the Hood of SKILL.md: Semantic Supply-chain Attacks on AI Agent Skill Registry. *arXiv preprint arXiv:2605.11418*. https://doi.org/10.48550/arXiv.2605.11418
21. Schmotz, D., Beurer-Kellner, L., Abdelnabi, S., & Andriushchenko, M. (2026). Skill-Inject: Measuring Agent Vulnerability to Skill File Attacks. *arXiv preprint arXiv:2602.20156*. https://doi.org/10.48550/arXiv.2602.20156
22. Tie, G., Shi, J., Zhou, P., & Sun, L. (2026). BadSkill: Backdoor Attacks on Agent Skills via Model-in-Skill Poisoning. *arXiv preprint arXiv:2604.09378*. https://doi.org/10.48550/arXiv.2604.09378
23. Wang, Z., Gao, Y., Wang, Y., Liu, S., Sun, H., Cheng, H., Shi, G., Du, H., & Li, X. (2026). MCPTox: A Benchmark for Tool Poisoning Attack on Real-World MCP Servers. *Fortieth AAAI Conference on Artificial Intelligence (AAAI 2026)*. https://doi.org/10.1609/aaai.v40i42.40895
24. Yong, Z.-X., Menghini, C., & Bach, S. H. (2024). Low-Resource Languages Jailbreak GPT-4. *2024 Annual Conference of the North American Chapter of the Association for Computational Linguistics (NAACL 2024)*. https://doi.org/10.48550/arXiv.2310.02447
25. Zhan, Q., Liang, Z., Ying, Z., & Kang, D. (2024). InjecAgent: Benchmarking Indirect Prompt Injections in Tool-Integrated Large Language Model Agents. *Findings of the Association for Computational Linguistics: ACL 2024*, 9951–9967. https://doi.org/10.18653/v1/2024.findings-acl.624
26. Zhang, H., Huang, J., Mei, K., Yao, Y., & Wei, X. (2025). Agent Security Bench: Formalizing and Benchmarking Attacks and Defenses in LLM-based Agents. *International Conference on Learning Representations (ICLR 2025)*. https://doi.org/10.48550/arXiv.2410.02644
27. Zhang, H., Yuan, A., Nian, Y., & Zhao, Y. (2026). Do Agent Skills Speak Safety in Every Language? A Cross-Lingual Security Analysis of the Skills Ecosystem. *AgentSkills Workshop, ACM Conference on Conversational and Agentic AI Systems (CAIS 2026)*.
28. Zhao, L., Bhaskar, A., & Dobriban, E. (2026). LivePI: More Realistic Benchmarking of Agents Against Indirect Prompt Injection. *arXiv preprint arXiv:2605.17986*. https://doi.org/10.48550/arXiv.2605.17986
