#!/usr/bin/env python3
from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path
from private_paths import outside_repo, private_root


def main() -> None:
    ap = argparse.ArgumentParser(description='Run the locked repeated session-grouped DLCS confirmation.')
    ap.add_argument('--data-root', type=Path, required=True)
    ap.add_argument('--outdir', type=Path, help='Validation outputs outside the repository worktree.')
    ap.add_argument('--trees', type=int, default=1200)
    args = ap.parse_args()

    repo = Path(__file__).resolve().parent.parent
    try:
        data_root = outside_repo(args.data_root, '--data-root')
        outdir = outside_repo(args.outdir or private_root() / 'session_grouped', '--outdir')
    except ValueError as error:
        ap.error(str(error))
    outdir.mkdir(parents=True, exist_ok=True)

    total_zip = outdir.parent / 'dataset_runtime.zip'
    with zipfile.ZipFile(total_zip, 'w', zipfile.ZIP_DEFLATED) as z:
        for p in data_root.rglob('*'):
            if p.is_file():
                z.write(p, Path('Dataset') / p.relative_to(data_root))

    script = repo / 'src' / 'dlcs' / 'session_grouped_validation.py'
    cmd = [
        sys.executable, str(script), '--total-zip', str(total_zip),
        '--outdir', str(outdir), '--stage', 'confirm', '--trees', str(args.trees),
        '--confirm-config', 'strong_plus_local'
    ]
    subprocess.run(cmd, check=True)
    subprocess.run([
        sys.executable, str(repo / 'src' / 'dlcs' / 'verify_results.py'),
        '--results-dir', str(outdir)
    ], check=True)


if __name__ == '__main__':
    main()
