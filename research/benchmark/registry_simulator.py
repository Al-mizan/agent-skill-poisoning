"""Hermetic Local Skill Registry and Rug-Pull Simulator (ADR-0004).

Simulates the complete 5-stage agent skill supply-chain threat lifecycle
on the local filesystem without requiring external network connectivity or
public package registries:

  Stage 1: Authoring (Clean v1.0.0 vs Poisoned v2.0.0 across en / bn / bn-en)
  Stage 2: Registry Publishing (Rich marketplace metadata, bilingual discovery tags)
  Stage 3: Install-Time Vetting (StaticSkillScanner inspection & SHA-256 lockfile)
  Stage 4: Rug-Pull Update (In-place package mutation v1.0.0 -> v2.0.0)
  Stage 5: Execution Seam (Taint evaluation & PolicyEnforcementModule dispatch)
"""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
from typing import Any

from config import DATA_DIR, PILOT_TASKS_FILE
from defenses.policy_enforcement import StaticSkillScanner


@dataclass(frozen=True)
class MarketplaceMetadata:
    """Rich marketplace metadata simulating public skill repositories (Stage 2)."""

    package_name: str
    author: str
    verified_author: bool
    stars: int
    downloads: int
    published_at: str
    bilingual_tags: list[str]


@dataclass(frozen=True)
class SkillManifest:
    """Represents a specific language register variant of an Agent Skill manifest."""

    name: str
    description: str
    instructions: str
    version: str
    register: str
    is_mutated: bool

    def compute_sha256(self) -> str:
        payload = f"{self.name}:{self.version}:{self.register}:{self.description}:{self.instructions}"
        return hashlib.sha256(payload.encode("utf-8")).hexdigest()

    def to_markdown(self) -> str:
        return (
            f"---\n"
            f"name: {self.name}\n"
            f"version: {self.version}\n"
            f"register: {self.register}\n"
            f"description: \"{self.description}\"\n"
            f"---\n\n"
            f"# {self.name} ({self.version})\n\n"
            f"{self.description}\n\n"
            f"## Operating Instructions\n"
            f"{self.instructions}\n"
        )


@dataclass
class InstallationRecord:
    """Audit record returned upon installing or updating a skill package."""

    task_id: str
    package_name: str
    version: str
    register: str
    sha256_hash: str
    staged_path: Path
    scanner_verdict: dict[str, Any]
    vetting_bypassed: bool
    installed_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())


class MockSkillRegistry:
    """Hermetic local catalog maintaining skill packages and version histories."""

    def __init__(self, tasks_file: Path | None = None) -> None:
        self.tasks_file = tasks_file or PILOT_TASKS_FILE
        self._raw_tasks = json.loads(self.tasks_file.read_text(encoding="utf-8"))
        self._tasks_by_id = {t["task_id"]: t for t in self._raw_tasks}
        self._tasks_by_domain = {t["domain"]: t for t in self._raw_tasks}

    def list_catalog(self) -> list[dict[str, Any]]:
        """Return the public marketplace catalog index."""
        catalog = []
        for task in self._raw_tasks:
            meta = task.get("marketplace_metadata", {})
            catalog.append(
                {
                    "task_id": task["task_id"],
                    "domain": task["domain"],
                    "package_name": meta.get("package_name", task["domain"]),
                    "author": meta.get("author", "unknown"),
                    "verified_author": meta.get("verified_author", False),
                    "stars": meta.get("stars", 0),
                    "downloads": meta.get("downloads", 0),
                    "tags": meta.get("bilingual_tags", []),
                    "available_versions": list(task.get("versions", {}).keys()),
                }
            )
        return catalog

    def get_manifest(
        self,
        task_id: str,
        version: str = "v1.0.0",
        register: str = "en",
    ) -> SkillManifest:
        """Resolve a specific version and language register of a skill."""
        task = self._tasks_by_id.get(task_id)
        if not task:
            raise KeyError(f"Task ID '{task_id}' not found in registry.")

        versions = task.get("versions", {})
        if version not in versions:
            raise KeyError(f"Version '{version}' not found for task '{task_id}'.")

        v_data = versions[version]
        variant = v_data["skill_variants"][register]
        return SkillManifest(
            name=variant["name"],
            description=variant["description"],
            instructions=variant["instructions"],
            version=version,
            register=register,
            is_mutated=v_data.get("is_mutated", False),
        )


class SkillInstaller:
    """Simulates agent package installation, local staging, and static vetting."""

    def __init__(self, registry: MockSkillRegistry, staging_root: Path | None = None) -> None:
        self.registry = registry
        self.staging_root = staging_root or (DATA_DIR / ".staged_skills")
        self.staging_root.mkdir(parents=True, exist_ok=True)
        self.installed_packages: dict[str, InstallationRecord] = {}

    def install(
        self,
        task_id: str,
        version: str = "v1.0.0",
        register: str = "en",
    ) -> InstallationRecord:
        """Stage a skill manifest to local sandbox and invoke install-time static scanning."""
        manifest = self.registry.get_manifest(task_id, version=version, register=register)
        target_dir = self.staging_root / task_id / manifest.name
        target_dir.mkdir(parents=True, exist_ok=True)

        skill_md_path = target_dir / "SKILL.md"
        skill_md_path.write_text(manifest.to_markdown(), encoding="utf-8")

        # Install-time vetting check (StaticSkillScanner)
        scanner_verdict = StaticSkillScanner.inspect_skill(manifest.instructions, register)
        vetting_bypassed = not scanner_verdict["blocked_at_install"]

        record = InstallationRecord(
            task_id=task_id,
            package_name=manifest.name,
            version=version,
            register=register,
            sha256_hash=manifest.compute_sha256(),
            staged_path=skill_md_path,
            scanner_verdict=scanner_verdict,
            vetting_bypassed=vetting_bypassed,
        )
        self.installed_packages[task_id] = record
        return record

    def simulate_rug_pull(
        self,
        task_id: str,
        target_version: str = "v2.0.0",
    ) -> InstallationRecord:
        """Simulate in-place package update from benign (v1) to mutated (v2) instructions."""
        existing = self.installed_packages.get(task_id)
        if not existing:
            raise RuntimeError(f"Cannot rug-pull uninstalled task '{task_id}'.")

        # Pull mutated version in the same linguistic register
        return self.install(task_id, version=target_version, register=existing.register)

    def clean_staging(self) -> None:
        """Purge temporary staged files after test runs."""
        import shutil

        if self.staging_root.exists():
            shutil.rmtree(self.staging_root)
            self.staging_root.mkdir(parents=True, exist_ok=True)
