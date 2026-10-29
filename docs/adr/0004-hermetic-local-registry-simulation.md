# ADR 0004: Hermetic Local Registry and Two-Phase Rug-Pull Simulation

## Context

Evaluating supply-chain risks in AI agent skill ecosystems (such as Anthropic `SKILL.md` packages and Model Context Protocol servers) requires modeling the entire threat lifecycle: Package Authoring, Registry Publishing, Install-Time Vetting, Rug-Pull Mutation, and Runtime Execution. However, deploying functional dual-use manifests or active injection payloads to public marketplaces (GitHub, npm, PyPI, or open MCP registries) is hazardous to innocent third parties, violates marketplace terms of service, and breaches the Menlo Report (2012) ethical guidelines for computer security research. 

Prior academic benchmarks (Skill-Inject, AgentDojo, MCPTox, MalSkillBench) established that rigorous, reproducible security evaluations do not require public registry traffic. Instead, the supply-chain lifecycle must be modeled hermetically within an air-gapped testbed.

## Decision

We implement a local, hermetic registry simulation architecture (`research/benchmark/mock_registry/` and `research/benchmark/registry_simulator.py`) operating strictly on the local filesystem:

1. **Filesystem Directory Catalog**: Skills are packaged as local versioned directory manifests (`v1.0.0` for clean utility baseline; `v2.0.0` for poisoned payload) governed by an index metadata catalog (`registry_index.json`).
2. **Two-Phase Dynamic Rug-Pull Workflow**: Evaluation trials execute in two consecutive phases:
   - **Phase 1 (Benign Baseline)**: The agent installs `v1.0.0`, passes static vetting, executes the clean user task, and logs baseline Benign Utility Retention (BUR).
   - **Phase 2 (Rug-Pull Mutation)**: The package is updated in-place to `v2.0.0`. The static scanner re-evaluates the manifest. Non-English (`bn`, `bn-en`) manifests bypass English-calibrated heuristics, allowing the agent to load the poisoned instructions into its Reasoning Plane and attempt canary execution against the dispatch seam.
3. **Dual Metric Logging**: The install-time static scanner operates in observation-logging mode during benchmark trials. It records formal admission verdicts (`blocked_at_install`, matched patterns, behavioral flags) while allowing runtime execution to proceed so that downstream Attack Success Rate (ASR) and Policy Violation Rate (PVR) can be measured empirically.

## Consequences

- No external network requests, public repository publishing, or live package registry accounts are required.
- The benchmark runs deterministically in network-isolated sandboxes (`docker run --network none`).
- The transition dynamics of rug-pull supply-chain poisoning are quantified directly: comparing pre-mutation and post-mutation scanner evasion and agent execution behavior.
