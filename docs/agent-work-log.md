# Agent work log

Date: 2026-11-18. Worktree: codex/isas2026-dlcs-rebuild-20261118, based on verified live main commit 46d8132ce20322e4fdc0972852933b813b35786c.

This log records the task-specific reviews and edits used to rebuild the repository. Review agents did not train models, evaluate predictions, access private archives, or write to GitHub.

| Role | Scope and boundary | Outcome |
|---|---|---|
| Research Synthesist | Read-only search and inspection of public GitHub repositories, READMEs, repository trees, docs, and linked papers. | Identified exactly 10 paper-linked research repositories and concrete documentation/reproducibility lessons. Full list is in docs/repository-benchmark.md. |
| Technical evidence auditor | Read-only comparison of the handoff, paper, code, saved aggregate outputs, and validation protocol. | Confirmed the locked main/specialist/gate/smoothing setup; identified the context-bin lookahead and the untraced visit exposure and gate-selection history. No experiment or edit. |
| Independent Code Reviewer | Fresh read-only check of the specialist context join. | Confirmed that a complete 50-second bin can include observations after the corresponding 10-second midpoint. |
| Smoothing and gate red-team auditor | Read-only independent review of smoothing and correction behavior. | Checked the centered-window settings, exception rules, tie behavior, gate conditions, and inactive pair overrides against the source and paper. No method or result change proposed. |
| Privacy Engineer | Read-only review of the original tracked tree and notebooks; did not open private archive contents. | Found no raw challenge artifacts or credentials in the tracked snapshot, but found identifier-like private input filenames in scripts/docs/notebooks and facility geometry in config. User directed that both geometry files remain. |
| Minimal Change Engineer | Owned only path abstraction in scripts, src readers, and the two notebooks. | Added a local JSON manifest with seven logical roles, generic runtime aliases, environment/upload notebook input, and the verified repository URL. Confirmed empty notebook outputs. Static Python/JSON/notebook checks passed; no model, training, validation, or notebook run. |
| Minimal Change Engineer, CLI private paths | Owned the CLI wrappers and `scripts/private_paths.py`; did not run data/model workflows. | Moved dataset, fingerprint, validation, cache, and inference defaults to an external private root. CLI wrappers reject resolved paths inside or containing the clone. Local sibling and Colab defaults match the notebooks. Static AST/path checks passed. |
| Primary agent | Owned paper identity, README, focused documentation, status/evidence reconciliation, and final verification. | Copied the author-designated PDF byte for byte, removed only the stale PDF from the new worktree, and drafted the evidence, method, results, data, reproduction, benchmark, contribution, and status docs. At the user’s follow-up, grouped the README contributions, enlarged and reoriented diagrams vertically, added the Vietnamese translation, and recorded the author-confirmed presentation pass in the evidence ledger. |
| Fresh final diff reviewer | Independent read-only review of notebook and CLI data/output paths, README contract, docs, and final private-path guard. Did not inspect private submission rows or run model/data workflows. | Found that notebook uploads/runtime outputs first remained in the clone; after that fix, found CLI `runtime/` defaults and an ancestor-path deletion hazard, plus one wording mismatch. Notebook and CLI paths were moved outside the clone, the helper now rejects both ancestors and descendants, and the wording was aligned. A fresh review after all fixes found no actionable findings. |
| Language Translator and fresh README reviewer | Read-only comparison of the English and Vietnamese README, contribution grouping, status evidence, and Mermaid layout. | Found Vietnamese-only result tables in the first translation pass; they were removed to match the English README. Final review confirmed the two language sections align, both diagrams are top-down with larger labels and spacing, the opening remains two paragraphs, and the presentation status is correctly labeled author-reported in the ledger. No remaining README finding. |

## User decisions

- Keep config/beacon_coords.json and config/room_centers.json unchanged. The second file is read by src/models/hier_adj.py.
- Generalize private archive member names in code and notebooks, while keeping the archive-specific mapping in a local manifest.

## Handling and verification notes

- No GitHub push, pull request, release, tag, settings change, or other remote mutation was made.
- The supplied handoff and original repo snapshot remain outside the rebuilt worktree and unchanged.
- No ML experiment, training, evaluation, or hidden-test prediction was run.
- One ignored `scripts/__pycache__/private_paths.cpython-313.pyc` was produced by static compilation. Automatic review blocked its removal; it is excluded from the Git diff/status.
- One broad local text search unintentionally emitted matching row-level submission lines into the internal tool transcript. The output was stopped; no row-level predictions were copied into the repository or another artifact, used for analysis, or sent to GitHub. Subsequent searches were narrowed to aggregate evidence and code.
