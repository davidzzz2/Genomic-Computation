# Genomic Computation – Causal Diffusion for Single-cell Perturbations

This repository hosts the working notes, scripts, and manuscript scaffolding for the Nature-level project on **causal diffusion models for multi-omic single-cell perturbation responses**.

## Structure

- `genomics-paper/`
  - `field-survey.md`, `topic-candidates.md`: landscape scan + topic selection rationale.
  - `concept-brief.md`: problem definition and success criteria.
  - `data-inventory.md`, `data-pipeline.md`: datasets, acquisition plans, and preprocessing pipeline.
  - `model-design.md`: architectural sketch for the causal diffusion model.
  - `experiment-plan.md`, `baseline-plan.md`: benchmarking + evaluation roadmap.
  - `paper-outline.md`: Nature-style manuscript outline.
  - `scripts/`: data download/conversion utilities (Replogle atlas, Mixology dataset).
  - `status-YYYY-MM-DD.md`: rolling progress logs.

## Next Milestones

1. Populate `scripts/download_replogle.py` with final file IDs and run the initial dataset pull.
2. Convert ECCITE-seq (RNA+protein) into the shared format and extend scripts accordingly.
3. Reproduce baseline models (scGen, CPA, CellOT) on the standardized splits.
4. Prototype the causal diffusion architecture and start logging quantitative comparisons.
5. Draft the full Nature-style manuscript once the first round of results is in.

## Environment Notes

- Target stack: Python 3.11 + PyTorch, Scanpy/anndata, scvi-tools, pytorch-lightning.
- Data lives outside the repo (see `.gitignore` exclusions) to keep the repo lightweight.

Pull requests / branches:
- Working branch: `monessy/causal-diffusion` (initial push from the workspace).
