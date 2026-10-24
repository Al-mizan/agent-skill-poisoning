# Agent Skill Distribution & Ethical Supply-Chain Attack Modeling

**Date:** October 2026  
**Status:** Primary Research Note  
**Context:** Cross-Lingual Agent Skill Poisoning Benchmark  

---

## 1. Executive Summary

1. **Remote Skill Distribution via GitHub and `npx` is an Established Reality**:
   - Agent skills (`SKILL.md` packages) are consumed by modern coding agents (Claude Code, Gemini CLI, Cursor, Codex) through **filesystem-based progressive disclosure**.
   - Remote distribution directly from GitHub repositories via `npx` is actively standardized by the `skills.sh` ecosystem (`npx skills add <owner/repo>`). This downloads skill folders from GitHub, places them in the target agent directory (`.claude/skills/`, `.cursor/skills/`, `.gemini/skills/`, `.agents/skills/`), and generates a `skills-lock.json` lockfile.
   - For Model Context Protocol (MCP) servers, distribution via `npx -y <package>` is the official, first-party execution model for `stdio`-based tool servers across Claude Desktop, Claude Code, and Cursor.

2. **Ethical Security Research Does Not Require Public Registries**:
   - Leading academic benchmarks in agent security—**Skill-Inject** (Schmotz et al., 2026), **AgentDojo** (Debenedetti et al., 2024), and **MCPTox** (Wang et al., 2026)—**never deploy malicious payloads to public marketplaces or live registries**.
   - Research adheres to the **Menlo Report (2012)** ethical guidelines: hermetic local sandboxing (Docker with `--network none`), harmless canary indicators (e.g., `/tmp/canary_audit.marker`), and programmatic simulation of supply-chain stages on the local filesystem.

---

## 2. Part 1: Skill Distribution Mechanisms (GitHub, `npx`, and Filesystem Discovery)

### 2.1 Filesystem Discovery Across Major Agent Architectures

| Agent System | Local Discovery Paths | Loading Mechanism |
| :--- | :--- | :--- |
| **Anthropic Claude Code** | `.claude/skills/<name>/SKILL.md`<br>`~/.claude/skills/<name>/SKILL.md` | **3-Phase Progressive Disclosure:** Scans YAML frontmatter (`name`, `description`) at startup. The markdown body and helper scripts are loaded into context only when user task intent matches or when invoked explicitly via `/command`. |
| **Google Gemini CLI** | `.gemini/skills/<name>/SKILL.md`<br>`.agents/skills/<name>/SKILL.md`<br>`~/.gemini/skills/` | Controlled via `settings.json` under `"skills": {"enabled": true}`. Hierarchical lookup: Built-in $\rightarrow$ Extension $\rightarrow$ User Global $\rightarrow$ Project Workspace. |
| **Cursor** | `.cursor/skills/<name>/SKILL.md`<br>`~/.cursor/skills/`<br>Also scans `.claude/skills/` | Dual system: static rules (`.cursorrules`, `.cursor/rules/*.mdc`) are concatenated into system prompts; agent skills (`SKILL.md`) are loaded dynamically on semantic match or `@skill` invocation. |

### 2.2 Distributing Skills via GitHub + `npx` (`skills.sh`)

It is entirely possible to host skill manifests on GitHub and distribute them via `npx`. In fact, this is already the de facto packaging standard:

* **The CLI Tool (`npx skills`)**:
  Initiated by Vercel Labs (`vercel-labs/skills`) and indexed at `skills.sh`:
  ```bash
  # Install a skill directly from a public GitHub repository
  npx skills add <owner/repo> --skill <skill-name>

  # Install globally for the user's CLI agents
  npx skills add <owner/repo> -g
  ```
* **How It Operates**:
  1. The CLI queries the GitHub repository using the Git/raw content API.
  2. It copies the target folder containing `SKILL.md`, `scripts/`, and `references/` into the local agent directory (e.g., `.agents/skills/<skill-name>/`).
  3. It computes the SHA-256 hash of the installed manifest and records provenance in `skills-lock.json`.
* **Verification in this Repository**:
  The workspace root of this project already contains a `skills-lock.json` file maintaining SHA-256 integrity hashes for skills pulled from GitHub repositories (e.g., `mattpocock/skills`).

### 2.3 Model Context Protocol (MCP) Execution via `npx`

For agent systems using Anthropic's Model Context Protocol (MCP), server tools are officially deployed using `npx`:

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/workspace/data"]
    },
    "memory": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-memory"]
    }
  }
}
```
The `-y` (or `--yes`) flag instructs `npx` to automatically fetch and execute the npm package in an ephemeral cache without interactive user prompts.

---

## 3. Part 2: How to Research Supply-Chain Attacks Without Public Registries

### 3.1 Precedents in Leading Peer-Reviewed Security Benchmarks

| Benchmark / Paper | Target Surface | Registry Interaction | How Supply Chain is Simulated |
| :--- | :--- | :--- | :--- |
| **Skill-Inject** (Schmotz et al., arXiv:2602.20156) | `SKILL.md` files | **Zero public registry traffic.** | Local Python scripts construct isolated Docker containers and programmatically inject adversarial payloads into `.claude/skills/` or `.gemini/skills/` on the local filesystem. |
| **AgentDojo** (Debenedetti et al., NeurIPS 2024) | Tool outputs & environment data | **Zero public registry traffic.** | Evaluates 70+ mock tools across simulated environments (Slack, Workspace, Banking) by mutating in-memory data states. |
| **MCPTox** (Wang et al., AAAI 2026) | MCP Server Tool Metadata | **Zero public registry traffic.** | Executes 45 authentic, open-source MCP servers locally in a test harness; dynamically mutates tool descriptions and JSON schemas in memory. |
| **MalSkillBench** (Guo et al., arXiv:2606.07131) | Skills (`SKILL.md` + code) | **Hybrid / Read-only.** | Scraped 703 real-world malicious skills from ClawHub (observational only), but synthesized 3,214 closed-loop skills tested purely inside local sandboxes with `strace` and `inotifywait`. |

### 3.2 Ethical Guidelines: The Menlo Report (2012)

Publishing live poisoned packages or functional exploits to public package managers (npm, PyPI, ClawHub) violates academic research ethics:
* **Principle of Beneficence:** Research must minimize risk to innocent third parties. Public packages can be accidentally discovered and installed by real users.
* **Respect for Law and Public Interest:** Namespace pollution and deploying unrequested code violates registry terms of service and can lead to IP bans and legal liability.

---

## 4. Practical Implementation: The Local / Offline 5-Stage Attack Lifecycle

You do not need to host anything on public marketplaces to conduct rigorous, publishable research. You model all 5 stages locally within an air-gapped testbed:

```
[1. Local Authoring] ──► [2. Simulated Registry] ──► [3. Local Install] ──► [4. Version Mutation] ──► [5. Runtime Execution]
   (Create variants        (Feed files through          (Copy folder into        (Swap v1 -> v2 to        (Agent reasons & calls
    in testbed data)        static scanners)             sandbox directory)       test caching/update)     tools; Seam intercepts)
```

1. **Stage 1: Authoring (Local Benchmark Data)**
   - Maintain your skill variants locally in JSON/YAML (as in `research/benchmark/data/xling_tasks_expanded.json`).
   - Define paired tasks with benign descriptions and embedded contextual injection in `en`, `bn`, and `bn-en`.
   - Use safe telemetry markers (`/tmp/canary_audit.marker`) rather than destructive payloads.

2. **Stage 2: Simulated Registry & Ingestion**
   - Model the registry vetting gate by passing the raw skill markdown through static scanners (YARA rules, Cisco Skill Scanner heuristics, or string matchers).
   - Record whether the scanner blocks the file (`blocked_at_install = True/False`).
   - If blocked, record install failure (SSR=0%, ASR=0%, BUR=0%). If passed, proceed to Stage 3.

3. **Stage 3: Local Installation**
   - Simulate installation by copying the generated `SKILL.md` directly into the agent's target skill directory inside an isolated Docker container (`--network none`).
   - The agent CLI indexes the file exactly as if it had been downloaded via `npx skills add` or git clone.

4. **Stage 4: Version Mutation (Rug-Pull Simulation)**
   - To model a rug-pull update, your benchmark script runs the agent first with a benign `SKILL.md` ($v1$), records clean completion, and then programmatically overwrites the file with the poisoned variant ($v2$) before invoking the agent again.
   - This measures whether agents retain cached trust or re-evaluate updated manifests.

5. **Stage 5: Runtime Execution & Seam Interception**
   - The agent receives an authentic user request, selects the skill, and generates tool call proposals.
   - The Policy Enforcement Module (ADR-0002) inspects each proposed call at the dispatch seam.
   - Evaluate quantitative metrics: SSR, ASR, BUR, and defense latency.

---

## 5. Primary Citations

1. **Vercel Labs**: `skills.sh` Package Manager CLI Specification ([skills.sh](https://skills.sh)).
2. **Anthropic**: Model Context Protocol (MCP) Specification ([modelcontextprotocol.io](https://modelcontextprotocol.io)).
3. **Schmotz et al. (2026)**: *SKILL-INJECT: Measuring Agent Vulnerability to Skill File Attacks*, arXiv:2602.20156.
4. **Debenedetti et al. (2024)**: *AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents*, NeurIPS 2024, arXiv:2406.13352.
5. **Wang et al. (2026)**: *MCPTox: A Benchmark for Tool Poisoning Attack on Real-World MCP Servers*, AAAI 2026, arXiv:2508.14925.
6. **Guo et al. (2026)**: *MalSkillBench: A Runtime-Verified Benchmark of Malicious Agent Skills*, arXiv:2606.07131.
7. **DHS / IEEE (2012)**: *The Menlo Report: Ethical Principles and Guidelines for Cybersecurity Research*.
