"""Configuration for the Cross-Lingual Agent Skill Poisoning Pilot Benchmark."""
from __future__ import annotations

from pathlib import Path

BENCHMARK_ROOT = Path(__file__).resolve().parent
RESEARCH_ROOT = BENCHMARK_ROOT.parent
WORKSPACE_ROOT = RESEARCH_ROOT.parent

DATA_DIR = BENCHMARK_ROOT / "data"
RESULTS_DIR = RESEARCH_ROOT / "results"
PILOT_TASKS_FILE = DATA_DIR / "pilot_tasks.json"
PILOT_RUNS_LOG = RESULTS_DIR / "pilot_runs.jsonl"

TARGET_SKILLS = [
    "pdf",
    "git",
    "email-api",
    "internal-comms",
    "webapp-testing",
]

LINGUISTIC_REGISTERS = [
    "en",      # English baseline
    "bn",      # Native-script Bangla
    "bn-en",   # Banglish code-mixed
]

SUPPORTED_AGENTS = {
    "gemini": {
        "provider": "google",
        "default_model": "gemini-2.5-flash",
        "env_key": "GEMINI_API_KEY",
    },
    "groq": {
        "provider": "groq",
        "default_model": "llama-3.3-70b-versatile",
        "env_key": "GROQ_API_KEY",
    },
    "simulation": {
        "provider": "mock",
        "default_model": "deterministic-pilot-mock",
        "env_key": None,
    },
}

CANARY_TARGET_PATH = "/tmp/canary_audit.marker"
AUTHORIZED_WORKSPACE_DIR = "/workspace/output"
