"""Summarize pilot JSONL records into clean Markdown tables by Phase (ADR-0004)."""
from __future__ import annotations

import sys
from collections import defaultdict
import json
from pathlib import Path

BENCHMARK_DIR = Path(__file__).resolve().parent
if str(BENCHMARK_DIR) not in sys.path:
    sys.path.insert(0, str(BENCHMARK_DIR))

import argparse
from config import PILOT_RUNS_LOG


def main() -> None:
    parser = argparse.ArgumentParser(description="Summarize pilot JSONL records.")
    parser.add_argument(
        "--log",
        type=Path,
        default=PILOT_RUNS_LOG,
        help="Path to JSONL log file.",
    )
    args = parser.parse_args()

    if not args.log.exists():
        print(f"No results found at {args.log}")
        return

    records = [
        json.loads(line)
        for line in args.log.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    if not records:
        print("Log file is empty.")
        return

    # Group by phase -> (defense_tier, language_register)
    phases = sorted(list({r.get("phase", "legacy_single_phase") for r in records}))

    print(f"\n# Benchmark Results Summary ({len(records)} total trials)\n")

    for phase in phases:
        phase_records = [r for r in records if r.get("phase", "legacy_single_phase") == phase]
        phase_title = (
            "Phase 1: Clean Baseline (v1.0.0)"
            if phase == "phase_1_clean"
            else "Phase 2: Rug-Pull Mutation (v2.0.0)"
            if phase == "phase_2_mutated"
            else "Legacy / Single-Phase Trials"
        )
        print(f"## {phase_title} ({len(phase_records)} trials)\n")
        print("| Defense Tier | Register | Trials | SSR (%) | VBR (%) | ASR (%) | BUR (%) |")
        print("| :--- | :--- | :--- | :--- | :--- | :--- | :--- |")

        grouped: dict[tuple[str, str], list[dict]] = defaultdict(list)
        for r in phase_records:
            key = (r["defense_tier"], r["language_register"])
            grouped[key].append(r)

        for (defense, reg), items in sorted(grouped.items()):
            n = len(items)
            ssr = sum(i["metrics"]["skill_selected_ssr"] for i in items) / n * 100
            asr = sum(i["metrics"]["canary_triggered_asr"] for i in items) / n * 100
            bur = sum(i["metrics"]["benign_task_completed_bur"] for i in items) / n * 100
            vbr = sum(i["metrics"].get("vetting_bypassed_vbr", 1 if i.get("vetting_bypassed", True) else 0) for i in items) / n * 100
            print(f"| {defense} | {reg} | {n} | {ssr:.1f}% | {vbr:.1f}% | {asr:.1f}% | {bur:.1f}% |")
        print()


if __name__ == "__main__":
    main()
