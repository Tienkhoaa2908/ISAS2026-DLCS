# Authorized reproduction

The commands below describe the public workflow for a reader who already has authorized access to the required data. They were not run as part of this rebuild. No training, validation, or hidden-test inference was performed for this documentation work. Replace each output placeholder with a directory outside the repository worktree.

The scripts use `ISAS2026_PRIVATE_DIR` when set. Otherwise, local execution defaults to a sibling `<repo-name>-private` directory; Colab defaults to `/content/ISAS2026-private`. The CLI rejects input and output paths that resolve inside the repository clone, including paths reached through symlinks. This applies to `--archive`, `--manifest`, `--data-root`, `--out`, `--outdir`, and `--workdir` where those options are used.

## 1. Prepare an isolated environment

Use a supported Python installation and install the pinned dependencies:

    python -m pip install -r requirements.txt

The workflow uses Python, pandas, NumPy, scikit-learn, imbalanced-learn, and Jupyter/Colab. Keep the dataset, manifest, generated files, and logs outside the repository.

## 2. Map authorized archive members locally

Create a JSON file outside the repository with string values mapping the seven keys listed in docs/data.md to the appropriate member paths in the private archive. The seven logical keys are:

- training_fingerprints
- room_labeled_ble_events
- processed_ble_events
- fingerprint_location_intervals
- source_location_labels
- inference_ble_events
- cached_oof_probabilities

Do not commit this manifest. Its member paths may identify private files or people. The code writes generic runtime aliases and does not need those private names in source or notebook cells.

## 3. Prepare and verify the fingerprint reference

    python scripts/prepare_data.py --archive <private-archive> --manifest <local-manifest> --out <private-runtime>/Dataset
    python scripts/verify_fingerprints.py --data-root <private-runtime>/Dataset --out <private-runtime>/rebuilt_fingerprints.csv

The expected retained fingerprint reference is 15,382 rows, 175 numeric features, 22 classes, and SHA-256 d95ce428732af277c74bf8bd3fb16301c9aaeddbbb1c46a6b394905bfe5b3877.

## 4. Optional labeled-data evaluation

These commands train and evaluate models. Run them only when a separate reproduction is authorized and intended. Write all outputs to private directories outside the repository worktree. LODO writes a row-level prediction artifact as well as aggregates; keep that artifact private and do not distribute it.

Repeated session-grouped diagnostic:

    python scripts/session_grouped_validation.py --data-root <private-runtime>/Dataset --outdir <private-run>/session_grouped --trees 1200

Fixed-22-class leave-one-day-out evaluation:

    python scripts/lodo_validation.py --data-root <private-runtime>/Dataset --outdir <private-run>/lodo --specialist-trees 1200 --force

The command outputs are not expected to prove the untraced visit exposure figures unless the corresponding audit is separately rebuilt and its run output retained. Preserve split definitions, version information, aggregate outputs, and checksums for any new authorized reproduction.

## Hidden-test records

The repository has a hidden-input inference path in scripts/test_inference.py and notebooks/test_prediction.ipynb. It uses the hierarchical 10-second main model and centered smoothing, not the long-context specialist or directional gate. This path was not run during this rebuild. The CLI defaults to `<private-root>/test_inference/submission.csv`; pass `--workdir <private-root>/test_inference` and `--out <private-root>/test_inference/submission.csv` to choose an explicit external location. The public tree does not include the hidden-input CSV, labels, or per-row predictions. The recorded row/window counts and submitted CSV SHA-256 are integrity references only.

## Notebooks

The notebooks provide a walkthrough of the training and evaluation path. Their saved cell outputs are empty. Both notebooks place uploads, the manifest, the prepared dataset, evaluation outputs, caches, and inference output in a private directory outside the repository clone. The default is `/content/ISAS2026-private` in Colab and a sibling `<repo-name>-private` directory on a local machine; set `ISAS2026_PRIVATE_DIR` to choose another location. `DATA_ARCHIVE` and `DATA_MANIFEST` paths that resolve inside the clone are rejected. When the upload prompt is used, the notebook temporarily changes to the private directory so uploaded files are not saved in the clone. The filename `data_manifest.json` is also ignored by Git as a safeguard.
