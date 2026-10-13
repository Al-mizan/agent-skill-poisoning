# AI Agent Security & Jailbreaking Research

Domain model and canonical vocabulary for research on AI agent vulnerabilities, indirect prompt injection (IPI), RAG knowledge poisoning, and agentic execution hijacks.

## Core Concepts & Trust Boundaries

**Control Plane**:
The privileged channel comprising developer system prompts, safety guidelines, and authenticated user instructions.
_Avoid_: User space, prompt channel

**Reasoning Plane**:
The intermediate state space where the agent plans, decomposes tasks, maintains scratchpads, and executes reasoning steps (e.g. ReAct loops).
_Avoid_: Cognitive plane, internal state

**Data Plane**:
The untrusted channel carrying retrieved documents, API responses, tool observation outputs, and external content.
_Avoid_: External data, payload plane

**Control-Data Conflation**:
The architectural flaw where an LLM interprets text from the untrusted Data Plane as privileged directives from the Control Plane.
_Avoid_: Prompt mixing, input confusion

**Confused Deputy**:
A vulnerability where an agent with high system permissions is tricked by untrusted data into executing unauthorized actions on behalf of an attacker.
_Avoid_: Agent proxy exploit

## Attack Taxonomy & Outcomes

**Indirect Prompt Injection (IPI)**:
An attack where adversarial instructions embedded in passive third-party content (web pages, files, emails, RAG chunks) hijack agent execution flow.
_Avoid_: Data injection, second-order prompt injection

**Direct Prompt Injection (DPI)**:
An attack where the direct user deliberately crafts adversarial prompts to override system instructions or developer constraints.
_Avoid_: Prompt hacking, prompt override

**Jailbreak**:
An attack that bypasses safety alignment training or guardrail policies to cause the model to generate prohibited content or violate safety boundaries.
_Avoid_: Tool exploit, prompt injection (when not bypassing safety policies)

**Tool Hijack**:
An exploit where injected instructions coerce an agent into invoking external tools with attacker-chosen arguments or malicious side-effects.
_Avoid_: Function spoofing, tool misuse (when unintentional)

**Data Exfiltration**:
The unauthorized extraction and transmission of private context, memory, or user data to an attacker-controlled receiver.
_Avoid_: Data leakage, information bleeding

## Agentic State & Memory Vulnerabilities

**Scratchpad Pollution**:
The transient poisoning of an agent's working memory or chain-of-thought during a single execution turn, corrupting intermediate reasoning steps.
_Avoid_: Thought injection, reasoning poisoning

**Episodic Memory Poisoning**:
The contamination of multi-turn conversational history or session logs, causing malicious instructions to persist across subsequent turns in an active session.
_Avoid_: Conversation hijacking, chat history corruption

**Semantic Memory Poisoning**:
The persistent injection of malicious payloads into long-term retrieval databases, user profiles, or knowledge stores that survive across distinct user sessions.
_Avoid_: Long-term memory backdoor, vector memory corruption

## Threat Actors & Interaction Modes

**Passive Adversary**:
An attacker who implants static payloads in external data sources (websites, files, emails) and relies on the agent fetching them during benign workflows without real-time feedback.
_Avoid_: Static attacker, offline adversary

**Active Adversary**:
An attacker who interacts with the agent dynamically across multiple turns, observing tool execution feedback and adapting injected payloads in real time.
_Avoid_: Interactive attacker, dynamic adversary

**Collusive Adversary**:
A threat scenario where an untrusted data provider coordinates with a malicious internal user to bypass authorization or sandbox controls.
_Avoid_: Hybrid attacker, dual-threat agent

## RAG Attack Lifecycle

**Knowledge Poisoning**:
The corruption of the RAG knowledge base, source repositories, or data loaders to place adversarial content into the corpus prior to indexing.
_Avoid_: Corpus poisoning, document contamination

**Retrieval Manipulation**:
Attacks manipulating embedding distances, keyword frequencies, or rankers to force poisoned passages into top-k retrieved results.
_Avoid_: Search hijacking, embedding collision

**Context Exploitation**:
The activation and execution of adversarial instructions contained within retrieved passages once assembled into the model generation prompt.
_Avoid_: Chunk activation, retrieval execution

## Defensive Architecture & Runtime Enforcement

**Prompt-Level Isolation**:
Heuristic formatting mechanisms (delimiters, XML tags, border strings, spotlighting) used within prompts to visually separate untrusted data from instructions.
_Avoid_: Soft defense, prompt guarding

**Guardrail Classifier**:
An auxiliary model or heuristic filter (input scanner, LLM judge, perplexity checker) that inspects inputs or outputs for adversarial content before propagation.
_Avoid_: Outer guard, input shield

**Architectural Segregation**:
A system design pattern (such as Dual-LLM or Split-Context) that physically separates privileged planning LLMs from unprivileged data-processing LLMs.
_Avoid_: Two-tier LLM, sandbox model

**Runtime Policy Enforcement**:
Deterministic execution controls (Mandatory Access Control, capability tokens, schema validation, human approval gates) that govern tool calls independently of LLM reasoning.
_Avoid_: Tool sandbox, runtime firewall

**Policy Enforcement Module**:
A deep module placed at the tool execution seam that validates behavioral specifications, capability tokens, and parameter invariants before invoking external tool adapters.
_Avoid_: Tool gateway, permission service

**Behavioral Invariant**:
A declarative constraint governing tool execution preconditions, parameter bounds, and data-flow destinations (e.g. prohibiting outbound network calls when untrusted data is loaded).
_Avoid_: Tool rule, safety check

**Taint Propagation**:
The tracking of untrusted Data Plane labels across tool outputs, intermediate reasoning scratchpads, and subsequent tool execution parameters.
_Avoid_: Data tracking, flow tracing

**Capability Token**:
An ephemeral, scoped authorization token granting temporary permission to execute specific tool actions with validated parameter boundaries.
_Avoid_: API key, auth credential

## Evaluation Metrics

**Attack Success Rate (ASR)**:
The percentage of attack attempts that successfully achieve the adversary's objective (e.g., executing a target tool, leaking secrets, or violating policy).
_Avoid_: Compromise rate, hack rate, Unauthorized Tool Action Rate (UTAR)

**Skill Selection Rate (SSR)**:
The percentage of evaluation trials in which an agent's planning module selects a target or poisoned skill from the registry prior to tool execution.
_Avoid_: Selection hijacking rate, routing rate

**Benign Utility Retention (BUR)**:
The percentage of benign tasks successfully completed without false-positive refusal or execution degradation when defenses are enabled.
_Avoid_: Clean accuracy, task preservation, Task Success Rate (TSR)

**Defense Robustness Rate (DRR)**:
The quantitative reduction in Attack Success Rate achieved by a defense against adaptive or secondary attack mutations.
_Avoid_: Defense effectiveness, mitigation score

**Contextual Injection**:
An indirect prompt injection embedded naturally within plausible domain content to evade lexical and perplexity-based filters.
_Avoid_: Stealth injection, natural injection

**Obvious Injection**:
A raw, uncamouflaged adversarial prompt injection used primarily as an upper-bound baseline in vulnerability evaluations.
_Avoid_: Naive injection, direct payload

## Agent Skill & Tool Supply Chain

**Agent Skill**:
A modular distribution package containing natural language instructions, tool configurations, and executable scripts that extends an agent's reasoning capabilities.
_Avoid_: Plugin, tool package, agent extension

**Skill Manifest**:
A structured specification file (such as `SKILL.md`) defining an agent skill's identity, trigger descriptions, dependencies, and execution permissions.
_Avoid_: Skill config, agent definition file

**Tool Schema Poisoning**:
An attack altering tool descriptions, parameter schemas, or function signatures in a registry to induce unauthorized execution or parameter manipulation.
_Avoid_: Function definition poisoning, schema tampering

**Two-Channel Injection**:
An attack splitting adversarial instructions across separate communication channels—such as the user prompt and tool metadata—that assemble into an active exploit only upon execution.
_Avoid_: Dual-payload attack, multi-vector injection

**Cross-Artifact Injection**:
A supply-chain attack where instructions in a `SKILL.md` manifest coerce the agent into invoking or modifying bundled auxiliary scripts, configurations, or reference files that complete the exploit chain.
_Avoid_: Mixed skill attack, script-split injection

**Front-Loaded Inducement**:
The deliberate placement of coercive instructions at the beginning of a tool or skill description to preemptively bias agent selection heuristics.
_Avoid_: Priority injection, early prompt stuffing

## Attack Archetypes & Execution Camouflage

**Document-Driven Implicit Payload Execution (DDIPE)**:
An attack pattern where processing an untrusted document triggers an agent to load and execute a malicious skill or tool without explicit user authorization.
_Avoid_: Passive skill hijack, document trigger exploit

**Data Thief**:
A stealthy malicious skill or tool payload designed to covertly harvest and exfiltrate environment variables, credentials, or private workspace data.
_Avoid_: Exfiltration script, credential stealer

**Agent Hijacker**:
A persistent malicious skill that overrides system instructions, subverts core reasoning loops, and coerces the agent into serving as an adversarial proxy.
_Avoid_: Persistent rootkit, agent botnet node

**Platform Trust Weaponization**:
The exploitation of implicit platform trust—such as verified author badges, marketplace popularity metrics, or default local permissions—to bypass execution guardrails.
_Avoid_: Marketplace spoofing, reputation poisoning

## Supply Chain Threat Lifecycle

**Discovery Manipulation**:
The manipulation of semantic search embeddings, skill tags, or registry descriptions to force malicious skills into top-k discovery results.
_Avoid_: Search ranking hijack, registry poisoning

**Selection Manipulation**:
The deceptive crafting of skill descriptions or functional overlap to deceive an agent's planning module into selecting a malicious skill over a benign equivalent.
_Avoid_: Skill collision, routing confusion

**Governance Evasion**:
Techniques—such as polymorphic payloads, dynamic imports, or steganographic instructions—used to bypass static analysis and marketplace security vetting.
_Avoid_: Store bypass, vetting evasion

**Rug-Pull Update**:
An install- or update-stage supply-chain attack where a previously benign skill or tool server introduces malicious instructions or payloads in a subsequent version update.
_Avoid_: Delayed poisoning, post-install mutation

## Cross-Lingual Alignment & Safety Disparities

**English Calibration Gap**:
The systematic performance disparity where safety alignment and guardrails perform significantly better on English prompts than on non-English or low-resource languages.
_Avoid_: Language defense disparity, multilingual safety lag

**Translation Quality Fallacy**:
The flawed assumption that machine-translated or ungrammatical adversarial prompts fail to execute, despite LLMs retaining sufficient semantic comprehension to process the attack while guardrails fail.
_Avoid_: Translation defense myth, syntax protection fallacy

**Linguistic Proficiency Paradox**:
The vulnerability dynamic where a model's multilingual task capability far outpaces the sensitivity and coverage of its safety guardrails in low-resource languages.
_Avoid_: Capability-safety gap, cross-lingual asymmetry

