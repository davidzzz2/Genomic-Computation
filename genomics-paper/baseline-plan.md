# Baseline Reproduction Plan

| Baseline | Implementation | Key Hyperparameters | Expected Runtime | Purpose |
|----------|----------------|---------------------|------------------|---------|
| scGen (Lotfollahi et al.) | `scgen` package | 2-layer encoder/decoder, latent dim 100, KL weight 0.01 | 6h on A100 for Replogle subset | Canonical VAE perturbation predictor |
| CPA (Compositional Perturbation Autoencoder) | `cpa-tools` | 2-layer MLP for embeddings, latent 256, adversarial regularization | 8h | Strong baseline for combinatorial prediction |
| CellOT | Custom PyTorch (optimal transport) | Sinkhorn epsilon 0.05, 500 iterations | 4h | Provides non-parametric transport baseline |
| TotalVI baseline | `scvi-tools` | Latent 64 | 5h | Multi-omic generative baseline |
| Linear regression | sklearn | L2=1e-2 | 30m | sanity check |

**Evaluation checklist**
- Ensure all baselines trained on identical splits.
- Log metrics: Pearson R, R^2, DE gene AUROC, program-level cosine similarity, Earth Mover’s distance.
- Store outputs in `results/baselines/{model}/{dataset}.json`.
