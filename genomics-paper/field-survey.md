# Statistical Genomics Landscape (Mar 2026)

## 1. Foundation Models for Regulatory Genomics
- **What**: Transformer/MaskGNN/State Space Models trained on genome-scale sequences, chromatin accessibility, and epigenomic tracks (e.g., Enformer, Basenji2, EvoFM). Recent trend toward multi-task learning across species and modalities.
- **Stats angle**: Self-supervised density modeling + Bayesian fine-tuning on task-specific signals (variant effect prediction, promoter activity). Emphasis on uncertainty calibration for clinical use.
- **Gaps**: Limited capacity to predict perturbation responses (CRISPR screens, drug treatments) and to generalize to unseen cell states or combinatorial perturbations.

## 2. Single-cell Multi-omic Integration + Causal Inference
- **What**: Joint profiling (scRNA+ATAC, CITE-seq, Perturb-seq) with >10M cells. Statistical focus on latent variable models, nonlinear manifold alignment, and causal graph learning linking perturbations to regulatory programs.
- **Stats angle**: Variational autoencoders, normalizing flows, graph neural networks for cell trajectories; counterfactual estimation under interventions.
- **Gaps**: Scalable causal estimators that fuse perturbation labels, lineage, temporal snapshots, and extracellular cues to predict responses in unmeasured contexts.

## 3. Spatial Transcriptomics + Multi-scale Modeling
- **What**: Nanostring CosMx, 10x Xenium, Vizgen MERSCOPE delivering subcellular resolution for millions of spots with partial gene panels.
- **Stats angle**: Bayesian spatial point processes, Gaussian Markov Random Fields, diffusion-based imputation to recover whole-transcriptome & infer cell-cell signaling.
- **Gaps**: Joint modeling of spatial context with perturbation outcomes; integrating spatial proteomics and metabolomics; uncertainty-quantified predictions for therapeutic targeting.

## 4. Population-scale Variant-to-Phenotype Prediction with Functional Priors
- **What**: UK Biobank (500K+ genomes), All of Us, national biobanks. Combining GWAS summary stats with functional annotations (chromatin states, transcription factor occupancy) to refine causal variants.
- **Stats angle**: Fine-mapping with hierarchical priors, sparse Bayesian regression, deep kernel methods, causal mediation.
- **Gaps**: Transferable models that leverage foundation-model-derived functional priors to predict phenotype consequences for rare variants in underrepresented ancestries.

## 5. Programmable Editing + High-throughput Screens
- **What**: Base/prime editing, saturation mutagenesis, CRISPRi/a screens with transcript readouts (Perturb-seq 2.0).
- **Stats angle**: Design of experiments, causal effect estimation with off-target corrections, multi-task shrinkage across guide RNAs.
- **Gaps**: Unified statistical frameworks that jointly learn sequence-function landscapes and guide design policies, especially for combinatorial edits and multiplexed interventions.

## 6. Clinical Multi-modal Data Fusion
- **What**: Tumor genomics + radiomics + pathology images + longitudinal lab data integrated for prognosis/therapy selection.
- **Stats angle**: Multi-view statistical learning, survival models with high-dimensional structured covariates, uncertainty-aware decision policies.
- **Gaps**: End-to-end models linking genomic events to cellular phenotypes to patient outcomes with clear interpretability for clinical adoption.

---
**Observation**: The most “Nature-ready” gap is the absence of a unified statistical framework that can *causally* predict gene expression/program responses to arbitrary perturbations across cell states—something that would fuse foundation models, single-cell multi-omics, and perturbation data. This points toward a generative causal model for regulatory responses, potentially framed as a diffusion/energy-based model constrained by biological networks.
