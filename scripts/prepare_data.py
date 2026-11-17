#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import zipfile
from pathlib import Path

from private_paths import REPO_ROOT, outside_repo, private_root

ROLE_OUTPUTS = {
    'training_fingerprints': 'train_fingerprints.csv',
    'room_labeled_ble_events': 'room_labeled_ble_events.csv',
    'processed_ble_events': 'processed_ble_events.csv',
    'fingerprint_location_intervals': 'fingerprint_location_intervals.csv',
    'source_location_labels': 'source_location_labels.csv',
    'inference_ble_events': 'inference_ble_events.csv',
    'cached_oof_probabilities': 'cache/oof_probabilities.npz',
}

EXPECTED_FINGERPRINT_SHA256 = 'd95ce428732af277c74bf8bd3fb16301c9aaeddbbb1c46a6b394905bfe5b3877'


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest()


def copy_sources(repo: Path, runtime: Path) -> None:
    src = repo / 'src'
    for p in src.rglob('*.py'):
        rel = p.relative_to(src)
        dst = runtime / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(p, dst)
    for p in (repo / 'config').glob('*.json'):
        dst = runtime / 'config' / p.name
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(p, dst)


def main() -> None:
    ap = argparse.ArgumentParser(description='Prepare the input archive for the reproducibility scripts.')
    ap.add_argument('--archive', type=Path, required=True, help='Input archive distributed separately from GitHub.')
    ap.add_argument(
        '--manifest', type=Path, required=True,
        help='Local JSON mapping each logical input role to its archive member path.',
    )
    ap.add_argument('--out', type=Path, help='Prepared dataset directory outside the repository worktree.')
    args = ap.parse_args()

    repo = REPO_ROOT
    try:
        archive = outside_repo(args.archive, '--archive')
        manifest_path = outside_repo(args.manifest, '--manifest')
        out = outside_repo(args.out or private_root() / 'Dataset', '--out')
    except ValueError as error:
        ap.error(str(error))
    manifest = json.loads(manifest_path.read_text(encoding='utf-8'))

    if not isinstance(manifest, dict) or set(manifest) != set(ROLE_OUTPUTS):
        missing = sorted(set(ROLE_OUTPUTS) - set(manifest)) if isinstance(manifest, dict) else sorted(ROLE_OUTPUTS)
        extra = sorted(set(manifest) - set(ROLE_OUTPUTS)) if isinstance(manifest, dict) else []
        raise ValueError(f'Manifest roles must match the required logical inputs; missing={missing}, extra={extra}')
    if any(not isinstance(member, str) or not member.strip() for member in manifest.values()):
        raise ValueError('Every manifest role must map to a non-empty archive member path.')

    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True)

    with zipfile.ZipFile(archive) as z:
        names = set(z.namelist())
        missing = [role for role, member in manifest.items() if member not in names]
        if missing:
            raise FileNotFoundError('Archive is missing members for logical roles: ' + ', '.join(missing))
        for role, member in manifest.items():
            dst = out / ROLE_OUTPUTS[role]
            dst.parent.mkdir(parents=True, exist_ok=True)
            with z.open(member) as source, dst.open('wb') as target:
                shutil.copyfileobj(source, target)

    copy_sources(repo, out)

    digest = sha256(out / 'train_fingerprints.csv')
    print('runtime_data_root =', out)
    print('train_fingerprint_sha256 =', digest)
    print('matches_reference =', digest == EXPECTED_FINGERPRINT_SHA256)


if __name__ == '__main__':
    main()
