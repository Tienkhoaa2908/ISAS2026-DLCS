# Change and verification report

## Worktree

- Repository: Tienkhoaa2908/ISAS2026-DLCS
- Branch: codex/isas2026-dlcs-rebuild-20261118
- Base commit checked on 2026-11-18: 46d8132ce20322e4fdc0972852933b813b35786c
- Remote writes: none

## Changes

- Rebuilt the README as an English overview followed by a matching Vietnamese translation, grouped contribution areas, larger top-down Mermaid diagrams, authorized reproduction path, license boundary, and documentation index.
- Updated the public status wording with the author’s confirmation that Paper 139 passed the ISAS presentation round; the evidence ledger labels this presentation result as author-reported while retaining the organizer and IOP evidence separately.
- Added authoritative method, results, data-governance, reproduction, evidence, contribution, benchmark, agent-log, and open-question documents.
- Rewrote the Vietnamese overview as a short navigation page.
- Added the author-designated paper byte for byte under paper/ and removed the stale paper copy only from this worktree.
- Generalized archive member paths in the preparation/reader code and notebooks through a local JSON manifest. Private archive member names are not embedded in the public files.
- Left config/beacon_coords.json and config/room_centers.json unchanged at the user’s explicit direction.

## Checks completed

- The author-designated source paper and `paper/ISAS2026_Paper139_Full_Paper.pdf` have the same SHA-256: `D220C3836266D706A34D98E088AEE0415C0165E3B34B70AFAF80E63FD59D5735`. The old repository PDF had a different hash, page count, text, and metadata; it is absent from this worktree.
- The preserved prompt optimizer input SHA-256 is `EFC93A41AB3A8EF22F2A70D86E2899B369528E4DED7A25F56B671E50C4C8B4A9`; the packet SHA-256 is `162EEFFA17B4AB9040A004A06B5BEA380E481A909371B974EF9357B70572AFDD`. The JSON packet parses successfully.
- Eight changed Python files parse with Python 3.13. Both notebook files parse as JSON; all 10 code cells compile, and every saved output and execution count is empty.
- The private-path helper accepts the default sibling private directory and rejects the repository, a child path, its parent, and the drive root after path resolution. CLI outputs default outside the clone; CLI paths that contain or fall inside it are rejected. Colab path detection matches the notebooks.
- README structure checks passed: title plus exactly two introductory paragraphs, two Mermaid source blocks, and 10 benchmark repositories. All local Markdown links resolve.
- The Vietnamese README was independently compared with the English version; an initially extra Vietnamese-only result detail was removed. The final review found the sections, diagrams, and claims aligned. Both language versions use top-down diagrams with 18px labels and expanded spacing.
- A scoped scan found no private archive member names or credential-like strings. `runtime/` is no longer a CLI default. `runtime/` and `data_manifest.json` are ignored as safeguards. The two coordinate configuration files match the baseline.
- `git diff --check` passed. Git emitted only line-ending normalization notices for text files.
- Three CLI `--help` commands ran; `test_inference.py --help` and `lodo_validation.py --help` could not run because the available Python 3.13 environment lacks NumPy. Their source parsed successfully. No model/data workflow was used as a substitute.
- Mermaid source structure was checked, but no local Mermaid renderer was available, so rendered appearance was not verified.
- Independent final review found the notebook output and CLI path issues described in `docs/agent-work-log.md`; both were fixed. A fresh review after the fixes found no remaining actionable findings. The latest README review also found no remaining issues.
- One ignored bytecode file, `scripts/__pycache__/private_paths.cpython-313.pyc`, remains from static compilation. Automatic review blocked its removal; it is excluded from Git status and the diff.
- No training, validation, evaluation, notebook execution, hidden-test inference, or remote GitHub mutation was performed.
