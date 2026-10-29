# ADR 0005: Egress-Gated Container Sandbox Architecture for Safe Live Benchmarking

## Context

Benchmarking agent skill supply-chain vulnerabilities requires evaluating live LLM backbones (Google Gemini 2.5 Flash, Groq Llama 3.3 70B) under active tool execution. However, executing unvetted or mutated agent skill payloads introduces two conflicting operational risks:

1. **Host Compromise Risk (Host-Native Execution)**: Running benchmark scripts directly on the host machine risks exposing ambient host credentials (e.g. `~/.ssh/id_rsa`, AWS environment variables, local bash history) and polluting host temporary directories (`/tmp/canary_audit.marker`).
2. **Connectivity Barrier (Hermetic Air-Gapping)**: Complete network isolation (`network_mode: none`, as initially specified in ADR-0004 for offline dry-runs) severs outbound DNS and HTTPS sockets, preventing the agent from communicating with remote foundation model inference endpoints (`generativelanguage.googleapis.com` and `api.groq.com`).

Prior state-of-the-art benchmarks (`skill-inject`, `MalSkillBench`) resolve this tension by deploying containerized sandboxes that couple **strict local filesystem containment** with **controlled outbound bridge networking**.

## Decision

We introduce an **Egress-Gated Container Sandbox** configuration in `research/benchmark/docker/` providing two distinct operational profiles in `docker-compose.yml`:

1. **`pilot-bench-live` (Egress-Gated Live Evaluation)**:
   - **Network**: Uses standard Docker bridge networking (`bridge`), granting outbound HTTPS access strictly for LLM API calls.
   - **Credential Isolation**: Passes only explicit model credentials (`GEMINI_API_KEY`, `GROQ_API_KEY`) via environment variables; all host environment variables, SSH keys, and system configs are completely hidden.
   - **Filesystem Isolation**: Mounts only `research/results` (read-write for `pilot_runs.jsonl`). Scratch directories (`/tmp`, `/workspace/output`, and staged skills) remain ephemeral within the container and are discarded on termination (`--rm`).
   - **Privilege De-escalation**: Executes under unprivileged UID 1000 (`researcher`) with resource caps (2 CPUs, 2GB RAM).

2. **`pilot-bench-hermetic` (Hermetic Offline Verification)**:
   - **Network**: Strictly air-gapped (`network_mode: none`).
   - **Scope**: Dedicated to deterministic `--dry-run` trials, scanner rule regression tests, and invariant dispatch verification.

## Consequences

- The host computer is completely protected: canary writes, rogue bash commands, or filesystem traversals cannot escape the container boundary or affect host system integrity.
- Live model benchmarks execute safely with full API access without requiring complex host proxy configurations.
- Results from containerized runs are written directly to the host's `research/results/pilot_runs.jsonl` with matching UID 1000 permissions.
