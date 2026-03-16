# Concept Brief: Causal Diffusion Models for Single-cell Perturbation Responses

## Vision
Develop a generative statistical framework that predicts genome-wide molecular responses (RNA, chromatin, surface proteins) to arbitrary genetic or chemical perturbations across diverse cell states. The model combines causal intervention labels, single-cell multi-omic measurements, and contextual signals (cell lineage, microenvironment) to simulate counterfactual perturbation outcomes with calibrated uncertainty.

## Core Questions
1. **Predictive Scope**: Given a baseline cell state and specified perturbation(s), can we generate the full distribution of resulting molecular readouts without performing the experiment?
2. **Causality**: How do we ensure the model captures intervention-specific effects rather than spurious correlations, especially when extrapolating to unseen perturbations or cell types?
3. **Multi-omic Coherence**: How do we jointly model RNA, chromatin, and protein changes so predictions respect known regulatory constraints (e.g., TF binding leads chromatin opening, which drives transcription)?

## Statistical Ingredients
- **Diffusion-based Generative Model**: Conditional diffusion/score model that denoises synthetic multi-omic vectors while conditioning on perturbation descriptors, baseline cell embeddings, and biological priors.
- **Causal Graph Constraints**: Incorporate known regulatory edges (TF→target, enhancer→promoter) via neural ODE regularization or masked attention, ensuring interventions propagate through biologically plausible pathways.
- **Multi-view Latent Space**: Shared latent representation linking RNA, ATAC, and protein modalities via product-of-experts or shared Gaussian process priors, enabling cross-modality coherence.
- **Uncertainty + Counterfactuals**: Bayesian diffusion (stochastic guidance) to quantify uncertainty for out-of-distribution perturbations and deliver counterfactual samples.

## Expected Contributions
1. **Method**: First causal diffusion architecture tailored to single-cell perturbation data with multi-omic conditioning.
2. **Dataset Integration**: Harmonized mega-dataset fusing Perturb-seq, Multiome, and CITE-seq assays covering thousands of perturbations and cell types.
3. **Benchmark**: New evaluation suite for counterfactual perturbation prediction, including combinatorial and extrapolation tests.
4. **Applications**: Demonstrations on (a) prioritizing rescue combos for disease variants, (b) predicting drug synergies, (c) designing minimal perturbation sets to steer cell fate.

## Success Criteria (Nature bar)
- Large-scale validation showing predictive power beyond strong baselines (e.g., scGen, CPA, cross-attention VAEs) on held-out perturbations/cell types.
- Biological insight: discovery of non-obvious regulatory mediators validated via held-out experiments or literature.
- Generality: ability to plug in new perturbation descriptors (DNA sequence, chemical fingerprints) and still produce coherent responses.
