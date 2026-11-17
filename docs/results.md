# Results and evaluation limits

This report preserves the locked values from the submitted manuscript and the aggregate result files. No model was trained and no evaluation was run during this repository rebuild.

## Repeated session-grouped diagnostic

Five-fold validation grouped by contiguous sessions was repeated for seeds 10–13. The saved aggregate is in results/session_grouped/summary.csv; per-repetition values and fold audits are in the adjacent CSV files.

| System | Macro-F1, mean ± SD | Accuracy, mean ± SD | Balanced accuracy, mean ± SD |
|---|---:|---:|---:|
| Balanced linear | 0.4489 ± 0.0335 | 0.6809 ± 0.0096 | — |
| Balanced Extra Trees | 0.4629 ± 0.0142 | 0.7216 ± 0.0060 | — |
| Balanced flat Random Forest | 0.4773 ± 0.0168 | 0.7349 ± 0.0048 | — |
| Hierarchical RF with Borderline-SMOTE | 0.5367 ± 0.0116 | 0.7366 ± 0.0038 | 0.5110 ± 0.0148 |
| DLCS | 0.5487 ± 0.0158 | 0.7389 ± 0.0034 | 0.5225 ± 0.0160 |

The main and DLCS Macro-F1 means are 0.5366869167 and 0.5486823605. Their paired mean difference is 0.0119954438; DLCS is higher in all four confirmation repetitions.

This is an optimistic within-period diagnostic, not the primary evidence of day-to-day generalization. The submitted paper reports that 80 of 332 visits (24.1%) cross session groups and that 44.3–44.8% of validation windows have another window from the same visit in training. The corresponding visit-level audit table or run log was not present in the reviewed source bundle. Those figures are preserved as paper-reported but untraced from saved output. The saved confirmation fold audit does establish that there are zero shared exact 50-second context bins after the specialist purge; it does not establish the visit exposure figures.

The non-DLCS baseline rows are preserved exactly as approved Table 6 values and were not independently revalidated in this rebuild. The same is true of their reported accuracy and balanced accuracy values.

## Fixed-22-class leave-one-day-out

Four LODO folds each hold out one full date and train on the other three. Metrics aggregate all held-out predictions across the four days and use a fixed set of 22 classes.

| System | Macro-F1 | Accuracy | Balanced accuracy |
|---|---:|---:|---:|
| Main, raw | 0.3647 | 0.6649 | 0.3746 |
| DLCS, raw | 0.3680 | 0.6655 | 0.3754 |
| Main, common centered smoothing | 0.4026 | 0.6990 | 0.4051 |
| DLCS, common centered smoothing | 0.3993 | 0.6984 | 0.4018 |

Exact aggregate values in results/lodo/aggregate.csv are:

| System | Macro-F1 |
|---|---:|
| Main, raw | 0.3647477962 |
| DLCS, raw | 0.3679587836 |
| Main, centered | 0.4025838387 |
| DLCS, centered | 0.3993311822 |

The raw DLCS ordering is slightly higher than main; common centered smoothing reverses the ordering. The smoothed DLCS result does not improve on the smoothed main model. LODO is a four-day, one-facility audit, not forward-chaining: an earlier held-out day can have later days in training. The gate and window configuration were frozen before LODO; model selection was not nested by held-out day.

Smoothed Macro-F1 by held-out date is:

| Held-out date | Main | DLCS | DLCS minus main |
|---|---:|---:|---:|
| 10 April 2023 | 0.2337 | 0.2337 | 0.0000 |
| 11 April 2023 | 0.3644 | 0.3644 | 0.0000 |
| 12 April 2023 | 0.3791 | 0.3610 | -0.0181 |
| 13 April 2023 | 0.3558 | 0.3707 | +0.0149 |

These are per-day metrics; the aggregate values above are computed across all held-out predictions and are not the mean of these four rows.

Four classes have zero F1 in the smoothed LODO result: 503, 505, 508, and 510. Class 505 has 17 training fingerprints and is outside the 14-room specialist scope. These results do not support a broad claim that the gate solves minority-room failure.

## LODO gate activity

The saved LODO audit records the following cumulative gate flow over 15,382 raw predictions:

| Gate stage | Candidates remaining | Rejected at stage |
|---|---:|---:|
| Context available, both main top classes in scope, main margin ≤ 0.30 | 888 | — |
| Candidate differs from main prediction | 453 | 435 unchanged |
| Source is not protected | 279 | 174 protected |
| Candidate target is active | 90 | 189 inactive target |
| Main top two fit the target cluster | 47 | 43 cluster mismatch |
| Candidate advantage meets the margin | 46 | 1 insufficient margin |
| Accepted corrections | 46 | — |

The 46 accepted corrections are:

| Correction | Count |
|---|---:|
| 515 → 513 | 36 |
| 518 → 520 | 6 |
| 511 → 510 | 2 |
| 520 → 518 | 2 |

The corrections are concentrated: 36 of 46 change 515 to 513. The results do not show broad coverage across every configured cluster or establish generalization to new days.

## Hidden-test artifact

The locked inference record reports 62,222 organizer rows and 4,690 windows. Its CSV SHA-256 is 4b1a80a214b53b531a40467a515e2afbe4350b7b0533144ec1415c3eb9a43d80. This is an integrity reference only. The CSV, labels, and per-row predictions are not included; no hidden-test metric is reported.

## Evidence locations

- results/session_grouped/summary.csv and results/session_grouped/by_repetition.csv: aggregate and per-repetition confirmation values.
- results/lodo/aggregate.csv, results/lodo/by_day.csv, and results/lodo/per_class_main_centered.csv: fixed-class LODO metrics and class coverage.
- The author-designated paper, Tables 4–7, pages 6–7: submitted values and gate audit.
- The external local handoff’s EVIDENCE_AND_PROVENANCE.md: limitations on which reported audit claims have retained run output.

See docs/evidence-ledger.md for each claim’s status and source location.
