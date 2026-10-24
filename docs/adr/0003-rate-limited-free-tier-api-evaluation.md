# ADR 0003: Rate-Limited Cost-Free API Evaluation Architecture

## Context

Academic reproduction of LLM agent benchmarks often incurs significant cloud API costs or fails due to unmanaged request flooding against provider free tiers. For example, Groq Cloud provides free-tier access to `llama-3.3-70b-versatile`, but enforces strict limits:
- 30 Requests Per Minute (RPM)
- 6,000 Tokens Per Minute (TPM)
- 1,000 Requests Per Day (RPD)

Because each agent evaluation trial exchanges 500–800 tokens (system prompt, skill manifest, user prompt, and tool arguments), unthrottled concurrent execution hits the 6,000 TPM bottleneck within 8–9 requests, triggering HTTP 429 (`rate_limit_exceeded`) failures.

## Decision

We introduce a dedicated, cost-free benchmark execution engine (`research/benchmark/run_cost_free_groq.py`) with four architectural controls:
1. **Adaptive Token-Aware Pacing**: Inter-request sleep delays calibrated to model limits:
   - `llama-3.3-70b-versatile`: $7.0 \text{ s}$ delay ($\sim 8.5 \text{ RPM}$, $\approx 4,800 \text{ TPM} \le 6,000 \text{ TPM}$).
   - `llama-3.1-8b-instant`: $2.5 \text{ s}$ delay ($\sim 24 \text{ RPM}$, $\approx 14,000 \text{ TPM} \le 30,000 \text{ TPM}$).
2. **Exponential Backoff and Jitter**: Automated parsing of HTTP 429 `Retry-After` headers with fallback backoff ($10 \text{ s} \rightarrow 15 \text{ s} \rightarrow 22.5 \text{ s}$) up to 5 retries.
3. **Resumable Append-Only Checkpointing**: Every completed trial is flushed immediately to JSONL, allowing interrupted runs to resume without re-running or re-spending token quotas.
4. **Zero-Configuration Dry-Run Fallback**: If no API key is set, the harness defaults to deterministic dry-run simulation so test suites, CI/CD, and invariant verification execute without external network dependencies.

## Consequences

- Researchers can evaluate live frontier models on Groq's free tier with zero monetary cost.
- Execution is strictly single-threaded and sequentially paced, trading wall-clock execution time for budget elimination (e.g., 24 trials complete in $\sim 3$ minutes; 60 trials in $\sim 7.5$ minutes).
- Test runs remain reproducible and resilient against network spikes or temporary cloud provider throttling.
