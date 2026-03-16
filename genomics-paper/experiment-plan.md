# Experiment & Simulation Plan

## A. Datasets & Splits
1. **Single-gene CRISPR Perturb-seq (Replogle)**
   - Split by held-out genes (20%) and held-out cell types (one lineage entirely unseen).
2. **Combinatorial Perturb-seq (Mixology)**
   - Evaluate extrapolation to unseen gene pairs and higher-order combinations synthesized in silico.
3. **Multiome Perturbation (10x pilot)**
   - Joint RNA+ATAC prediction; hold out perturbations + peaks.
4. **ECCITE-seq with proteins**
   - Assess protein prediction accuracy and multi-modal coherence.
5. **Drug-response CITE-seq**
   - Hold out compounds; test transfer from genetic to chemical perturbations.

## B. Baselines
- scGen, CPA, CellOT, MUSAE (multi-modal VAE), simple regression baselines.
- Evaluation: predictive R^2, KL divergence, Earth Mover’s Distance on expression distributions, AUROC for differential expression classification.

## C. Core Experiments
1. **Counterfactual Accuracy**
   - Predict expression profiles for held-out perturbations; compare to ground truth single-cell distributions.
2. **Combinatorial Generalization**
   - Predict double KO effects from single KO training data; evaluate synergy capture using Bliss/ZIP metrics.
3. **Cross-cell-type Transfer**
   - Train on hematopoietic cells, predict on epithelial cells; measure drop vs. baselines.
4. **Multi-omic Consistency**
   - Evaluate whether predicted ATAC opening precedes RNA upregulation for known TF targets.
5. **Chemical Generalization**
   - Map drug embeddings to gene programs; test predictions for unseen compounds using measured readouts.
6. **Uncertainty Calibration**
   - Reliability diagrams comparing predicted vs. actual error; show OOD detection for far-from-training perturbations.
7. **Biological Insight Case Studies**
   - Identify predicted mediators for a disease gene; validate against literature or withheld perturbations.

## D. Simulations
- **Synthetic regulatory networks**: use known GRNs (e.g., DREAM challenge) to simulate dynamics and confirm causal identifiability of the diffusion model.
- **Noise stress tests**: inject batch effects, guide dropout, incomplete modalities to test robustness.
- **In silico screening**: run exhaustive combinatorial perturbations (>10^6) to propose candidate rescue strategies; select a few for experimental validation discussion.

## E. Figures (Draft Concepts)
1. Schematic of model architecture with causal conditioning.
2. UMAP overlays comparing real vs. predicted cells for held-out perturbations.
3. Heatmaps of predicted vs. observed gene programs for combinatorial interventions.
4. Multi-modal coherence plot (chromatin peak changes vs. target gene expression).
5. Uncertainty calibration curves and OOD detection scatter.
6. Case study diagram showing predicted rescue pathway.

## F. Timelines (tentative)
- Week 1: Data wrangling + baseline reproduction.
- Week 2: Prototype diffusion model on RNA-only data.
- Week 3: Extend to multi-omic + combinatorial settings; run full benchmarks.
- Week 4: Final simulations, figures, manuscript polish.
