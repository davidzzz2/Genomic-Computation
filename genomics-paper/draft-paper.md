# Draft Paper – Causal Diffusion Models for Single-cell Perturbation Responses

> **Note:** Living document; quantitative results/figures will be inserted as experiments complete.

## Title (working)
**Causal Diffusion Models Enable Multi-omic In Silico Single-cell Perturbation Responses**

## Abstract (placeholder ~150 words)
Large-scale single-cell perturbation atlases have illuminated how gene and chemical interventions reshape cellular programs, yet we still lack models that can predict these responses across modalities, cell types, and unseen perturbation combinations. Here we introduce a causal diffusion framework that conditions on baseline multi-omic states, explicit intervention descriptors, and regulatory priors to simulate counterfactual molecular profiles. Trained on harmonized Perturb-seq, Multiome, and CITE-seq datasets spanning thousands of perturbations, the model outperforms state-of-the-art perturbation predictors on held-out genes, cell types, and combinatorial knockdowns while maintaining regulatory consistency between chromatin, RNA, and protein layers. We further demonstrate accurate prediction of drug synergies and rescue strategies in silico, with calibrated uncertainty that flags out-of-distribution interventions. Our approach establishes a general recipe for generative, causally grounded digital perturbation screens, accelerating hypothesis generation for therapeutics and cell engineering.

## Introduction
Technologies such as Perturb-seq, ECCITE-seq, and 10x Multiome now profile millions of single cells under thousands of genetic or chemical interventions, revealing how perturbations propagate through regulatory networks. Despite this deluge, perturbation design remains largely empirical because current statistical models capture correlations in individual datasets but fail to generalize across cell types, combinatorial interventions, or molecular modalities. Existing approaches—autoencoders (scGen), optimal-transport models (CellOT), or compositional perturbation autoencoders (CPA)—offer valuable baselines yet lack (i) explicit causal structure that reflects intervention semantics, (ii) joint modeling of RNA, chromatin, and protein, and (iii) principled uncertainty estimates when extrapolating to new perturbations.

We posit that a generative model should respect the logic of interventions: applying a do-operator on a regulator should induce downstream effects according to the regulatory graph, not arbitrary covariances learned from data. Diffusion and score-based models provide a flexible foundation for learning high-dimensional distributions, but to date they have not been adapted to the causal and multi-omic requirements of perturbation biology. Our goal is to bridge this gap by combining diffusion generative modeling with structured conditioning, enabling in silico experiments that can reduce laboratory burden and surface non-obvious therapeutic hypotheses.

## Results
### 1. A causal diffusion architecture for perturbation responses
Describe model architecture, conditioning strategy, multi-omic decoders, and causal masks. Include Figure 1 schematic.

### 2. Accurate counterfactual predictions for held-out perturbations
Summarize performance vs. scGen/CPA/CellOT on Replogle splits (gene-level and cell-type generalization). Placeholder for quantitative table.

### 3. Combinatorial and cross-modality generalization
Report Mixology double-perturbation results and Multiome/ECCITE RNA+ATAC+protein coherence metrics. Highlight regulatory consistency analysis.

### 4. Application to drug synergy and rescue design
Outline virtual screening experiments on drug-response CITE-seq data; include case study figure once ready.

### 5. Uncertainty-guided exploration of novel interventions
Discuss calibration plots, OOD detection, and how uncertainty guides experiment selection.

## Discussion
- Summarize contributions and implications for perturbation biology and therapeutic discovery.
- Discuss limitations: dataset coverage, reliance on existing regulatory priors, need for prospective validation.
- Future directions: integration with spatial omics, adaptive experimental design, prospective CRISPR screens.

## Methods (to be expanded)
1. **Datasets and preprocessing** – details of each dataset, QC steps, harmonization strategy, and split definitions.
2. **Model architecture** – mathematical description of diffusion process, conditioning, causal masks, and decoders.
3. **Training procedure** – loss functions, optimization schedule, hardware.
4. **Baselines** – implementation details for scGen, CPA, CellOT, TOTALVI.
5. **Evaluation metrics** – definitions of R^2, DE gene AUROC, EMD, synergy metrics, uncertainty calibration.
6. **Case-study analyses** – e.g., gene program enrichment, mediator identification.

## Data and Code Availability
- Code: repository URL (public/private status TBD).
- Datasets: GEO/SRA accessions and licensing notes.

## Acknowledgements / Author Contributions
(To be drafted later.)
