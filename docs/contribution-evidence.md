# Contribution evidence

This record distinguishes source-backed repository work from broader author-reported contributions. Git history is evidence that code was added under the author name shown in the commit; it does not by itself prove team leadership or every offline data-preparation task.

## Author-reported statement

The author states: “I led the SQ3K team and built the end-to-end system.” The local repository history and implementation files support substantial code contributions to the system listed below. They do not independently establish the team-leadership claim.

## Source-backed repository contributions

| Area | Evidence in Git history | What the source supports |
|---|---|---|
| Data preparation and fingerprint integrity | 8e7b408, a74b1ea, ca9f57c | Adds the private-data preparation entry point, fingerprint reconstruction check, and locked fingerprint builder. This supports authorship of the public code, not every offline data-restructuring operation. |
| Main model and resampling | d525876, 84876a1, fdf46ba, 0b1dbf9, 5121d3c | Adds the hierarchical classifier, model entry points, fold-safe resampling wrapper, and Random Forest training code. |
| Shared model/evaluation utilities | e3141d0, d862d43 | Adds common model utilities and the locked DLCS evaluation core. |
| Context and smoothing | 11c58d0 | Adds the long-context feature and temporal utility implementation. |
| Session-grouped validation | a71dc88, dce422c, f4f6381 | Adds the repeated validation runner, DLCS validation workflow, and locked result verification. |
| Fixed-class LODO | 6488c29 | Adds the fixed-22-class LODO validation runner. |
| Hidden-test inference | 88465b7 | Adds the locked main-model inference script. The method uses centered smoothing and does not call the DLCS specialist or gate. |
| Reproduction notebooks | a7c8fff, 12681c6, 9267d14 | Adds the training and inference notebooks and a later completion update. Their current saved outputs are empty. |

The short subjects above are copied from the public commit history. The displayed author name is Tienkhoaa2908. The source bundle does not establish independent account-level authorship for activities outside repository commits.

## README contribution wording

The README groups the first-person contribution claims into these areas:

- **Data preparation and features:** fingerprint reconstruction/integrity, BLE event and label alignment, 10-second windows and 50-second context features, and a local-manifest archive preparation workflow.
- **Models and correction:** the 22-class hierarchical Random Forest, fold-local resampling, 14-room long-context specialist, frozen directional gate, and centered smoother.
- **Evaluation and inference:** repeated session-grouped and fixed-class LODO workflows, visit-audit limitations, and the locked main-model-plus-smoothing inference path.
- **Reproducibility:** training and evaluation notebooks, scripts, and fingerprint integrity checks.

Code/history verifies implementation of most listed components. Commit 8e7b408 supports the original archive-preparation script; the local manifest abstraction is new in this rebuild and is not attributed to that historical commit. The statement that the author personally ran and audited every validation step is author-reported, while the saved aggregate results verify the reported results. In particular, the 80/332 visit split and 44.3–44.8% same-visit exposure values lack the supporting run output in the reviewed bundle. The frozen gate’s implementation is verified, but its empirical selection history and the derivation of its clusters/margins remain untraced.

## Scope of attribution

- The code history supports the author’s repository contributions. It does not prove that the author worked alone or that the author was responsible for every coauthor’s scientific, writing, or data-collection contribution.
- The statement “I led the SQ3K team” remains author-reported.
- The exact offline process used to restructure every source archive is not fully established by commit history; the public helper code and current data contract are what can be verified.
- No claim is made here about challenge ranking, a hidden-test score, IOP acceptance, publication, DOI, or publication date.

See docs/evidence-ledger.md for the claim-by-claim source path and evidence status.
