# Model Architecture Sketch

## Inputs
- **Baseline state**: Multi-omic vector (RNA counts, chromatin accessibility peaks, protein abundances). When modalities missing, encode via modality-specific encoders producing a shared latent `z_state`.
- **Perturbation descriptor**: 
  - Genetic: one-hot gene target, functional annotations, TF binding profiles, CRISPR modality (KO, KD, activation), multiplicity.
  - Chemical: learned embedding from molecular fingerprints/SMILES encoder.
  - Environmental cues: cytokine stimuli, cell-cell neighborhood summaries, time since perturbation.
- **Context priors**: Regulatory graph (TF→target edges, enhancer-promoter links) encoded as adjacency matrices for structured attention masks.

## Architecture
1. **Encoders**
   - Modality-specific encoders (RNA transformer, ATAC CNN, protein MLP) → latent embeddings.
   - Perturbation encoder (Transformer over gene sets / graph neural net) outputs perturbation latent `z_pert`.
   - Context encoder (graph neural net over regulatory network) conditions attention masks.

2. **Causal Diffusion Core**
   - Score-based diffusion model operating on concatenated multi-omic latent `z_state`.
   - Conditioning implemented via cross-attention to `z_pert` + context embeddings at each denoising step.
   - **Structural masks** enforce directionality: perturbation channels only influence downstream targets consistent with regulatory graph; uses masked cross-attention and learnable edge weights.
   - **Do-operator conditioning**: explicit intervention channel indicating which genes are “forced” (modeled as setting parent nodes) to enforce causal semantics.

3. **Guidance + Calibration**
   - Classifier-free guidance to adjust strength of perturbation effect vs. baseline.
   - Energy-based regularizer to penalize predictions violating conservation laws (e.g., over-opening chromatin without TF binding evidence).
   - Posterior predictive uncertainty estimated via stochastic sampling; temperature scaled by OOD score (Mahalanobis distance in latent space).

4. **Decoders**
   - Modality-specific decoders map latent samples back to counts/accessibility/protein space with appropriate likelihoods (NB for RNA, ZINB for ATAC, Gaussian/log-normal for proteins).

## Training Strategy
- **Multi-task objective** combining reconstruction loss, denoising score matching, causal consistency (contrastive losses against shuffled perturbations), and regulatory edge alignment (encourage gradients along known TF-target links).
- **Curriculum**: start with single perturbations on RNA-only datasets, then progressively add modalities and combinatorial interventions.
- **Cross-dataset harmonization** via domain-adversarial loss ensuring latent space is dataset-agnostic.

## Inference / Simulation
- Sample counterfactual trajectories for unseen perturbations or cell types by feeding baseline embeddings + new perturbation descriptors.
- Perform sensitivity analysis by perturbing regulatory graph edges to infer mediators.

## Baselines
- scGen / scANVI
- Compositional Perturbation Autoencoder (CPA)
- CellOT / OT-based transport models
- CITE-seq-specific multimodal VAEs
- Foundation-model fine-tuned predictors (e.g., Enformer-based variant effect models)
