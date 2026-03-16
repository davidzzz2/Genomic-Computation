# Draft Paper – Causal Diffusion Models for Single-cell Perturbation Responses

> **Note:** Living document; quantitative results/figures will be inserted as experiments complete.

## Title (working)
**Causal Diffusion Models Enable Multi-omic In Silico Single-cell Perturbation Responses**

## Abstract (placeholder ~150 words)
Large-scale single-cell perturbation atlases have illuminated how gene and chemical interventions reshape cellular programs, yet we still lack models that can predict these responses across modalities, cell types, and unseen perturbation combinations. Here we introduce a causal diffusion framework that conditions on baseline multi-omic states, explicit intervention descriptors, and regulatory priors to simulate counterfactual molecular profiles. Trained on harmonized Perturb-seq, Multiome, and CITE-seq datasets spanning thousands of perturbations, the model outperforms state-of-the-art perturbation predictors on held-out genes, cell types, and combinatorial knockdowns while maintaining regulatory consistency between chromatin, RNA, and protein layers. We further demonstrate accurate prediction of drug synergies and rescue strategies in silico, with calibrated uncertainty that flags out-of-distribution interventions. Our approach establishes a general recipe for generative, causally grounded digital perturbation screens, accelerating hypothesis generation for therapeutics and cell engineering.

## Introduction
Technologies such as Perturb-seq, ECCITE-seq, and 10x Multiome now profile millions of single cells under thousands of genetic or chemical interventions, revealing how perturbations propagate through regulatory networks. The public Replogle atlas alone contains >2.5 million CRISPRi/a profiles, while Mixology and ECCITE extend coverage to combinatorial and protein-resolved measurements. Despite this deluge, perturbation design remains largely empirical because current statistical models capture correlations in individual datasets but fail to generalize across cell types, combinatorial interventions, or molecular modalities. Existing approaches—autoencoders (scGen), optimal-transport models (CellOT), or compositional perturbation autoencoders (CPA)—offer valuable baselines yet lack (i) explicit causal structure that reflects intervention semantics, (ii) joint modeling of RNA, chromatin, and protein, and (iii) principled uncertainty estimates when extrapolating to new perturbations.

Recent diffusion and score-based models have achieved striking success in imaging and protein design by learning expressive data distributions with stochastic denoising. We posit that the same machinery, when combined with structured conditioning, can deliver perturbation-aware generative models that respect the logic of interventions: applying a do-operator on a regulator should induce downstream effects via the regulatory graph, not arbitrary covariances learned from batch-specific data. However, simply conditioning a diffusion model on perturbation labels is insufficient; we must encode biological priors about directionality, enforce multi-omic coherence, and produce uncertainty estimates that flag extrapolations to unseen interventions.

Here we bridge these gaps with a causal diffusion framework that integrates regulatory graphs, multi-omic encoders, and intervention descriptors within the denoising process. Our approach:
1. Harmonizes large Perturb-seq, Multiome, and CITE-seq collections into a shared latent space so RNA, chromatin, and protein responses can be predicted jointly.
2. Uses masked attention guided by curated TF–target and enhancer–promoter maps to constrain diffusion dynamics to biologically plausible directions.
3. Provides calibrated uncertainty and out-of-distribution detection signals that guide experimental prioritization.

This manuscript details the model, benchmark suite, and applications to drug synergy and rescue design, laying the groundwork for in silico perturbation screens at scale.

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

## Methods (in progress)

### Datasets and preprocessing
We assemble six publicly available resources: the Replogle Perturb-seq atlas (CRISPRi/a in K562, HEK293T, and immune cell lines), Mixology combinatorial CRISPRi data, Frangieh cytokine-perturbation Perturb-seq, the 10x Multiome perturbation pilot (paired RNA+ATAC), ECCITE-seq (RNA+protein), and a drug-response CITE-seq collection. Raw matrices are downloaded via GEO/SRA or provider portals using scripted pipelines (see `scripts/`). Each dataset undergoes consistent QC (minimum 500 UMIs and <20% mitochondrial RNA per cell; guide assignment probability ≥0.8; ATAC fragments ≥1,000). Counts are normalized using SCTransform (RNA), TF-IDF/LSI (ATAC), and CLR (proteins). We embed each modality with lightweight autoencoders and align them into a shared latent space via scvi-tools (TOTALVI/PeakVI). Standardized splits hold out perturbations, cell types, or combinatorial pairs depending on the benchmark; split metadata is stored alongside the processed `.h5ad` objects.

### Model architecture
The causal diffusion model operates on concatenated latent representations of RNA, ATAC, and protein modalities. During each denoising step, the model receives (i) a baseline cell embedding, (ii) perturbation descriptors (gene targets, CRISPR modality, chemical fingerprints), and (iii) regulatory graph encodings. Conditioning is implemented with masked cross-attention so that interventions influence only their downstream targets according to curated TF–target networks and enhancer–promoter links. We additionally inject do-operator indicators that clamp the latent state of directly targeted genes, ensuring interventions act as hard constraints. Decoders map denoised latents back to modality-specific likelihoods (negative binomial for RNA, zero-inflated NB for ATAC, log-normal for proteins).

### Training procedure
We train the diffusion backbone with a multi-term objective that combines standard score-matching loss, reconstruction losses for each modality, a causal consistency loss (penalizing predictions that violate intervention directionality), and a domain-adversarial term to harmonize datasets. Optimization uses AdamW with cosine learning-rate decay, gradient clipping, and mixed precision on 8×A100 GPUs. Classifier-free guidance scales the perturbation conditioning strength at inference time, and we sample multiple trajectories to obtain predictive distributions.

### Baselines and evaluation
Baselines include scGen, CPA, CellOT, TOTALVI, and linear regression. All models share the same training/validation splits and input features. Evaluation metrics cover gene-wise Pearson r/R², differential-expression AUROC, Earth Mover’s Distance between full single-cell distributions, synergy metrics (Bliss independence, ZIP) for combinatorial predictions, and calibration curves for uncertainty. For biological interpretation, we perform gene-set enrichment on predicted programs, trace mediator edges via integrated gradients, and validate top-ranked rescue strategies against held-out perturbations or literature.

## Data and Code Availability
- Code: repository URL (public/private status TBD).
- Datasets: GEO/SRA accessions and licensing notes.

## Acknowledgements / Author Contributions
(To be drafted later.)
