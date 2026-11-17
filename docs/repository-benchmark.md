# Repository benchmark: 10 paper-linked research projects

Checked 2026-11-18 using read-only GitHub repository search and inspection of each repository’s README, relevant tree/docs, and linked paper or project page where available. Entries were selected for a direct paper-to-code connection. Stars were not used as a quality proxy.

The review considered paper/code traceability, explanation quality, reproduction steps, results and caveats, data/license clarity, organization, maintenance signals, and relevance to this repository. License notes below refer to the inspected repository’s stated code/model/data terms; they are not legal determinations.

| # | Repository and paper | Evidence reviewed | Concrete lesson | Pattern not to copy |
|---:|---|---|---|---|
| 1 | [geekfeiw/ARIL](https://github.com/geekfeiw/ARIL), [arXiv:1904.04964](https://arxiv.org/abs/1904.04964) | README, model documentation, paper link, and external data/weight instructions. | Link the paper, identify labels and hardware, and explain which model artifact belongs to which result. | Do not depend on opaque external weights/data with weak checksums or unclear split details; the project-level license was not clear in the reviewed tree. |
| 2 | [facebookresearch/mae](https://github.com/facebookresearch/mae), [arXiv:2111.06377](https://arxiv.org/abs/2111.06377) | README, PRETRAIN.md, FINETUNE.md, model code, license, checkpoint and hardware instructions. | Separate pretraining and fine-tuning, include commands and compute context, checksum checkpoints, and report run variation. | Do not assume the code license covers ImageNet or other external data; the repository was archived at review time. |
| 3 | [google-research/vision_transformer](https://github.com/google-research/vision_transformer), [arXiv:2010.11929](https://arxiv.org/abs/2010.11929) | README, configs, tests, model documentation, license, paper links. | Configurations, tests, and model documentation make the paper implementation easier to trace. | Do not leave multiple linked papers ambiguous about which result or code path is being reproduced; external ImageNet terms remain separate. |
| 4 | [facebookresearch/dino](https://github.com/facebookresearch/dino), [arXiv:2104.14294](https://arxiv.org/abs/2104.14294) | README, training/evaluation code, checkpoint arguments, logs, hardware notes, license. | Show training and evaluation commands and connect checkpoint settings to reported results. | Do not omit known framework issues or treat external dataset rights as part of the code license. |
| 5 | [openai/improved-diffusion](https://github.com/openai/improved-diffusion), [arXiv:2102.09672](https://arxiv.org/abs/2102.09672) | README, dataset instructions, training/sampling code, paper link, license. | Explain data layout and artifact paths beside the commands that consume them. | Do not leave data rights and limitations implicit merely because the code is MIT-licensed. |
| 6 | [openai/guided-diffusion](https://github.com/openai/guided-diffusion), [arXiv:2105.05233](https://arxiv.org/abs/2105.05233) | README, model card, evaluation and data docs, code, license. | Explain intended use, evaluation limits, and tradeoffs near the implementation. | Do not imply that a model result applies beyond the benchmark and data conditions documented for it. |
| 7 | [microsoft/LoRA](https://github.com/microsoft/LoRA), [arXiv:2106.09685](https://arxiv.org/abs/2106.09685) | README, examples, development/test instructions, license, benchmark reporting. | Separate development from test, report medians and repeated-run variation, and state hardware. | Do not let an MIT code license imply that example datasets have the same terms. |
| 8 | [facebookresearch/VideoPose3D](https://github.com/facebookresearch/VideoPose3D), [arXiv:1811.11742](https://arxiv.org/abs/1811.11742) | README, DATASETS, DOCUMENTATION, scripts, paper link, license. | Define evaluation protocols and distinguish causal from symmetric temporal methods. | Do not present a symmetric, future-using model as causal; dataset terms remain with the provider. |
| 9 | [google-research/simclr](https://github.com/google-research/simclr), [arXiv:2002.05709](https://arxiv.org/abs/2002.05709) | README, TensorFlow 2 implementation, training instructions, Colabs, checkpoint and compute notes, license. | Put the compute scale, checkpoints, and known issues in the same reproduction path. | Do not present a high-compute recipe as a lightweight reproduction or hide compute requirements. |
| 10 | [facebookresearch/dinov2](https://github.com/facebookresearch/dinov2), [arXiv:2304.07193](https://arxiv.org/abs/2304.07193) | README, model card, configs, model/data license notes, paper link. | Separate intended use and limitations from the model-specific terms and configuration details. | Do not treat an umbrella repository license as automatically governing every model or artifact. |

## Findings applied to this repository

- Pair the paper and code paths with exact method and result references.
- Separate the two evaluation protocols and disclose the session-group leakage caveat and non-forward LODO protocol.
- Record the environment and integrity hashes without copying private datasets or hidden predictions.
- State the data boundary and separate software, paper, organizer, and dataset rights.
- Keep one authoritative method and results page, then link to it from the README and evidence ledger.
- Mark missing run artifacts and gate-selection provenance as untraced instead of filling gaps by inference.

This is a point-in-time documentation comparison. It is not a ranking of research quality, and no repository’s star count was considered.
