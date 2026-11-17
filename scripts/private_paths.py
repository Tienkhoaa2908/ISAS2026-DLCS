"""Resolve local private-data paths outside the repository worktree."""

from __future__ import annotations

import os
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent


def outside_repo(path: Path, name: str) -> Path:
    resolved = Path(path).expanduser().resolve()
    try:
        resolved.relative_to(REPO_ROOT)
    except ValueError:
        try:
            REPO_ROOT.relative_to(resolved)
        except ValueError:
            return resolved
    raise ValueError(f'{name} must resolve outside and not contain the repository worktree.')


def private_root() -> Path:
    override = os.environ.get('ISAS2026_PRIVATE_DIR')
    if override:
        root = Path(override)
    elif Path('/content').exists():
        root = Path('/content/ISAS2026-private')
    else:
        root = REPO_ROOT.parent / f'{REPO_ROOT.name}-private'
    return outside_repo(root, 'ISAS2026_PRIVATE_DIR')
