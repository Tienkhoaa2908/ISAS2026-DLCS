# Data governance and input contract

## Distribution boundary

The public repository does not contain challenge archives, raw BLE traces, location labels, hidden-test labels, submissions, caches, or per-row validation predictions. Do not add them to commits, notebook outputs, logs, screenshots, or issue comments. Keep local archives, manifests, runtime directories, evaluation output, and caches outside the repository.

Use only data you are authorized to access. The public code describes a reproduction path; it does not grant access to or redistribution rights for the challenge data.

## Local archive manifest

The preparation script accepts a local JSON manifest that maps seven logical roles to member paths in the private archive. The manifest belongs outside the repository and must not be committed. The runtime aliases are generic:

| Manifest key | Runtime alias | Purpose |
|---|---|---|
| training_fingerprints | train_fingerprints.csv | Reference training fingerprint table |
| room_labeled_ble_events | room_labeled_ble_events.csv | Room-labeled BLE observations |
| processed_ble_events | processed_ble_events.csv | Processed training observations |
| fingerprint_location_intervals | fingerprint_location_intervals.csv | Intervals used to align fingerprint labels |
| source_location_labels | source_location_labels.csv | Source location-label table |
| inference_ble_events | inference_ble_events.csv | Inference input observations |
| cached_oof_probabilities | cache/oof_probabilities.npz | Cached out-of-fold probabilities used by the original workflow |

The corresponding JSON structure is an object with those keys and string values naming members in the archive. Use the archive’s local member names as values; do not paste them into public documentation or code. Keep the manifest path and archive path in local command history only.

Prepare the runtime layout with:

    python scripts/prepare_data.py --archive <private-archive> --manifest <local-manifest> --out <private-runtime>/Dataset

The script prints the reconstructed training fingerprint digest and whether it matches the reference. Do not include the local manifest or private member names in logs intended for publication.

## Fingerprint reference

The recorded training fingerprint table has:

- 15,382 rows
- 22 location classes
- 175 numeric model features
- SHA-256: d95ce428732af277c74bf8bd3fb16301c9aaeddbbb1c46a6b394905bfe5b3877

The public builder uses timestamped BLE observations and source location intervals to make 10-second windows with a 2-second stride and midpoint labels. It retains transition and boundary windows as described in the submitted paper. The integrity digest verifies file identity; it does not validate the original location labels.

## Geometry configuration

config/beacon_coords.json and config/room_centers.json are retained unchanged at the user’s explicit direction. They contain floor-layout coordinate information. The latter is consumed by src/models/hier_adj.py. Their presence does not imply that the challenge dataset or room-level labels may be redistributed.

## Rights

The repository’s MIT license applies to repository software. It does not grant rights to the author-designated paper, organizer materials, private challenge data, raw observations, labels, submissions, or any source archive. Paper rights remain with their respective rights holders; challenge-data use remains governed by the organizer’s terms and the user’s access authorization.

See docs/reproducibility.md for commands and docs/evidence-ledger.md for the source of the integrity claims.
