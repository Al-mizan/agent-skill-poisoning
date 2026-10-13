"""Summarize pilot JSONL records into a clean Markdown table."""
from __future__ import annotations

from collections import defaultdict
import json
from pathlib import Path
from config import PILOT_RUNS_LOG


def main() -> None:
    if not PILOT_RUNS_LOG.exists():
        print(f"No results found at {PILOT_RUNS_LOG}")
        return

    records = [
        json.loads(line)
        for line in PILOT_RUNS_LOG.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    if not records:
        print("Log file is empty.")
        return

    # Group by (defense_tier, language_register)
    grouped: dict[tuple[str, str], list[dict]] = defaultdict(list)
    for r in records:
        key = (r["defense_tier"], r["language_register"])
        grouped[key].append(r)

    print(f"\n### Pilot Benchmark Results Summary ({len(records)} total trials)\n")
    print("| Defense Tier | Register | Trials | SSR (%) | ASR (%) | BUR (%) |")
    print("| :--- | :--- | :--- | :--- | :--- | :--- |")

    for (defense, reg), items in sorted(grouped.items()):
        n = len(items)
        ssr = sum(i["metrics"]["skill_selected_ssr"] for i in items) / n * 100
        asr = sum(i["metrics"]["canary_triggered_asr"] for i in items) / n * 100
        bur = sum(i["metrics"]["benign_task_completed_bur"] for i in items) / n * 100
        print(f"| {defense} | {reg} | {n} | {ssr:.1f}% | {asr:.1f}% | {bur:.1f}% |")
    print()


if __name__ == "__main__":
    main()
