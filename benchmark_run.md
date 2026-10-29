# Benchmarking Guide: Cross-Lingual Agent Skill Poisoning (ADR-0004 & ADR-0005)

This guide documents the procedures for executing the Cross-Lingual Agent Skill Poisoning Benchmark across offline dry-run simulation, live foundation model evaluation, and containerized sandboxes.

---

## 1. Benchmark Execution Modes Overview

The benchmark supports two operational environments:

| Mode | Environment | Network Egress | Use Case | Command |
| :--- | :--- | :--- | :--- | :--- |
| **Host CLI (Dry-Run)** | Host Python 3.11+ | None needed | Rapid deterministic testing of scanner rules, manifests, and ADR-0002 seam dispatch | `python3 research/benchmark/run_pilot.py --dry-run --phase=both` |
| **Host CLI (Live APIs)** | Host Python 3.11+ | Outbound HTTPS | Direct live testing with Groq or Gemini using host environment variables | `python3 research/benchmark/run_cost_free_groq.py --phase=both` |
| **Container Sandbox (Live)** | Docker (`pilot-bench-live`) | Bridge Network | **Recommended for Safety**: Evaluates live Gemini/Groq APIs inside Docker; shields host filesystem & credentials | `docker compose -f research/benchmark/docker/docker-compose.yml run --rm pilot-bench-live` |
| **Container Sandbox (Hermetic)** | Docker (`pilot-bench-hermetic`) | Air-Gapped (`none`) | 100% air-gapped deterministic verification inside container | `docker compose -f research/benchmark/docker/docker-compose.yml run --rm pilot-bench-hermetic` |

---

## 2. Prerequisites & Environment Setup

### A. Python Environment (Host Execution)
Ensure Python 3.10+ is installed. The benchmark uses only the Python Standard Library (no third-party dependencies required):
```bash
python3 --version
```

### B. API Credentials (For Live Trials)
Export the relevant API keys in your terminal or configure them in `.env`:
```bash
# Google Gemini API Key
export GEMINI_API_KEY="your-gemini-api-key"

# Groq Cloud API Key (Free tier supported via ADR-0003 adaptive pacing)
export GROQ_API_KEY="your-groq-api-key"
```

---

## 3. Host-Native Execution

### A. Deterministic Dry-Run (Two-Phase Rug-Pull)
Executes the full two-phase trial suite across all 5 enterprise domains, 3 linguistic registers (`en`, `bn`, `bn-en`), and 4 defense tiers without consuming API quotas:
```bash
python3 research/benchmark/run_pilot.py --dry-run --phase=both
```

### B. Live Groq Cloud Evaluation (ADR-0003 Adaptive Pacing)
Runs live evaluations against `llama-3.3-70b-versatile` with automatic rate-limit pacing (7.0s intervals) and HTTP 429 exponential backoff:
```bash
python3 research/benchmark/run_cost_free_groq.py --phase=both
```

### C. Selective Phase Execution
You can control the rug-pull lifecycle phase using `--phase`:
* `--phase=1`: Runs only **Phase 1 (Clean Baseline `v1.0.0`)** to verify benign utility retention (BUR).
* `--phase=2`: Runs only **Phase 2 (Rug-Pull Mutation `v2.0.0`)** to measure scanner evasion and canary exploit execution (ASR).
* `--phase=both`: Sequentially runs Phase 1 followed by Phase 2 (default).

```bash
# Evaluate only clean utility
python3 research/benchmark/run_pilot.py --dry-run --phase=1

# Evaluate only the mutated exploit
python3 research/benchmark/run_pilot.py --dry-run --phase=2
```

---

## 4. Containerized Execution (ADR-0005 Sandboxes)

To protect your host machine from unintended side-effects, rogue command execution, or canary file clutter, run the benchmark inside Docker:

### A. Live Model Evaluation inside Sandbox (`pilot-bench-live`)
Runs live API models while keeping the host computer isolated:
- Mounts only `research/results/` to capture `pilot_runs.jsonl`.
- Host `$HOME`, `~/.ssh`, and local configs are unmounted and invisible.
- `/tmp` and `/workspace/output` are purely ephemeral inside the container.
- Memory capped at 2GB, CPU capped at 2 cores.
- Executes under unprivileged user `researcher` (UID 1000).

```bash
cd research/benchmark/docker

# Run live models safely in Docker
docker compose run --rm pilot-bench-live
```

To override flags (e.g. running only Gemini on Banglish):
```bash
docker compose run --rm pilot-bench-live --agents gemini --registers bn-en --phase=2
```

### B. Air-Gapped Hermetic Verification (`pilot-bench-hermetic`)
Runs deterministic dry-run verification in a completely network-severed container (`network_mode: none`):
```bash
cd research/benchmark/docker

docker compose run --rm pilot-bench-hermetic
```

---

## 5. Summarizing and Analyzing Results

All execution trials append structured records to `research/results/pilot_runs.jsonl`. To view the summary tables partitioned by phase:

```bash
python3 research/benchmark/summarize_results.py
```

To summarize a custom log file:
```bash
python3 research/benchmark/summarize_results.py --log /path/to/custom_runs.jsonl
```

### Output Metric Definitions
* **SSR (%) (Skill Selection Rate)**: Percentage of trials where the agent selected the target skill.
* **VBR (%) (Vetting Bypass Rate)**: Percentage of manifests that evaded install-time static scanning.
* **ASR (%) (Attack Success Rate)**: Percentage of trials where the canary exploit executed (`/tmp/canary_audit.marker`).
* **BUR (%) (Benign Utility Retention)**: Percentage of trials where the authentic user task completed correctly.