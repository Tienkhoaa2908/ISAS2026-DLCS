# Method and locked configuration

This page describes the configuration present in the public source. It is a record of the submitted method, not a tuning proposal. The source audit is cross-checked against the author-designated submitted paper, especially Sections 3–4 and Tables 2–3.

## Main fingerprint path

- 25 BLE beacons.
- Windows are 10 seconds long with a 2-second stride. The location label is assigned from the labeled interval containing the window midpoint.
- Current-window features are mean RSSI, presence, population standard deviation, maximum RSSI, and packet count for each beacon: 25 × 5 = 125 values.
- History features summarize the previous eight retained windows for each beacon: mean packet count and mean RSSI standard deviation: 25 × 2 = 50 values.
- The model receives 175 numeric features. Missing mean and maximum RSSI use -125; other missing features use zero.
- The retained training fingerprint reference contains 15,382 rows and 22 classes. Its SHA-256 is d95ce428732af277c74bf8bd3fb16301c9aaeddbbb1c46a6b394905bfe5b3877.

Relevant source: src/build_fingerprints.py, src/model_core.py, and scripts/verify_fingerprints.py.

## Main classifier and fold-local balancing

The main classifier has two levels: patient rooms versus common areas, then a class prediction within the routed group. Both forests use 400 trees, max_features=sqrt, and class_weight=balanced_subsample.

Inside each training fold, random oversampling raises classes with fewer than 6 examples to 6; Borderline-SMOTE-1 then raises classes below support 200 to 200. Validation rows are not used to fit either resampling stage. The setup uses seed 42 for the random oversampling/model setup and random_state 0 for Borderline-SMOTE-1; these are distinct settings.

Relevant source: src/models/train_resample.py, src/models/resample_wrap.py, and src/models/hier_adj.py.

## Long-context specialist

The specialist uses non-overlapping 50-second BLE bins without labels. It has 119 named numeric features: four per-beacon statistics for 25 beacons (100 total) and 19 global/time features. An availability flag is also supplied, giving 120 model columns. It trains only on the 14 classes:

501, 502, 503, 506, 508, 510, 511, 512, 513, 515, 518, 520, 522, 523.

It is a 1,200-tree Random Forest with square-root feature subsampling and balanced-subsample class weights. The configuration uses random_state 42. For evaluation, training rows whose exact 50-second context key is also present in the validation fold are purged.

The context is label-free, but it is not causal at the 10-second midpoint. The complete 50-second bin is joined to a 10-second window by its midpoint bin key. As a result, a specialist feature can include observations after the 10-second window midpoint, by up to about 45 seconds. The paper separately labels the centered smoother as offline; this context lookahead is an additional offline/batch limitation.

Relevant source: src/dlcs/common.py, src/dlcs/evaluation_core.py, and src/dlcs/session_grouped_validation.py.

## Frozen directional gate

The selected configuration is strong_plus_local. The main probabilities are normalized over the specialist’s 14-class scope and blended with specialist probabilities:

    q(c) = 0.25 × normalized_main(c) + 0.75 × specialist(c)

The directional gate starts from the main prediction and permits a change only when all applicable checks pass:

1. A 50-second context is available.
2. The main top-one and top-two classes are both in the 14-class specialist scope.
3. The main top-one minus top-two probability margin is no greater than 0.30.
4. The proposed class differs from the main prediction.
5. The main prediction is not a protected source.
6. The proposed target is active.
7. Both main top classes belong to the cluster configured for the proposed target.
8. The blended candidate score exceeds the source score by at least the required margin.

Protected sources are 501, 502, 516, 522, and 523. Active targets are 508, 510, 513, 515, 518, and 520.

| Candidate target | Required main top-two cluster |
|---|---|
| 508 | {508, 511, 520} |
| 510 | {510, 511, 512} |
| 513 | {501, 513, 515} |
| 515 | {501, 513, 515} |
| 518 | {515, 517, 518, 520, 522} |
| 520 | {518, 520, 522, 523} |

The default candidate advantage is 0.03. The source also declares pair overrides: 502→503 at 0.10; 522→520 and 523→520 at 0.12; 501→513 and 501→515 at 0.10. These overrides are inactive in strong_plus_local: target 503 is inactive, and all listed sources are protected. Every accepted correction therefore uses 0.03.

The code proves the frozen constants and decision path. The historical empirical ranking on development repetitions 3–5 and the evidence used to derive clusters and margins are untraced because the corresponding saved summaries/selection file are absent. The configuration is not changed here.

Relevant source: src/dlcs/evaluation_core.py. The LODO result is tied to the paper’s explicit frozen-gate evaluation, not to archival V34/V35 branches.

## Temporal smoothing

The same smoother is applied to raw main and DLCS predictions, separately within ordered sequences:

- The default centered vote radius is 15, a 31-position window, clipped at each sequence edge.
- Hallway uses radius 2, a 5-position window.
- For classes 501, 513, and 515, preserve the original class when its run length is at least 3 or its vote share is below 0.70.
- If the original current class is tied for the maximum vote, keep it. Otherwise, use the first class in the fixed class order among tied maxima.

The centered window uses predictions on both sides of the current position. The procedure is offline/noncausal and must not be described as streaming smoothing.

Relevant source: src/dlcs/common.py.

## Validation protocols

The repeated diagnostic uses five folds grouped by contiguous sessions, with repetitions 10–13. It is not grouped by physical visits. Exact shared 50-second context keys are purged from specialist training for each validation fold.

The day-separated audit is four-fold fixed-22-class leave-one-day-out (LODO): hold out one of four dates and train on the other three. It is not forward-chaining, since an earlier held-out date can train on later dates. The gate was frozen before LODO, so this is not fully nested day-level model selection.

The visit split and same-visit exposure figures shown in the paper are retained in the results report but marked untraced: no saved audit output establishing those exact values was present in the reviewed handoff. See docs/results.md and docs/evidence-ledger.md.
