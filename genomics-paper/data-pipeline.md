# Data Processing Pipeline (Draft)

## Tooling
- **Languages**: Python 3.11 (Scanpy, scvi-tools, PyTorch), R (Seurat for sanity checks).
- **Storage layout**: `/data/perturbseq/{dataset}/{raw,processed}` with `.h5ad` outputs.
- **Key packages**:
  - `scanpy`, `anndata`, `mudata` for multi-omic containers
  - `scvi-tools` for variational harmonization
  - `scprep`, `scrublet` for QC
  - `pytorch-lightning` for training diffusion model
  - `rdkit` for chemical descriptors

## Steps
1. **Acquisition**
   - Use `prefetch`/`fasterq-dump` for SRA entries or download processed `.h5ad` when available (Replogle provides H5AD through Broad portal).
   - Mirror metadata (guide-to-gene maps, perturbation types) into `metadata/`.

2. **QC & Filtering**
   - Standard cell QC: min 500 UMIs, <20% mitochondrial.
   - Guide assignment filtering (≥1 guide, on-target probability >0.8).
   - For ATAC: min fragments 1k, TSS enrichment >4.

3. **Normalization & Embedding**
   - RNA: SCTransform or CPM+log1p; select 5k HVGs.
   - ATAC: TF-IDF + LSI.
   - Protein: CLR normalization.
   - Encode each modality via modality-specific autoencoders to produce latent `z_rna`, `z_atac`, `z_prot`.

4. **Alignment / Harmonization**
   - Use `scvi-tools TOTALVI` (RNA+protein) and `PeakVI` (RNA+ATAC) to align modalities.
   - Map purely RNA perturbations into multi-omic latent space via learned translators (regression heads) to enable training with incomplete modalities.

5. **Split Strategy**
   - Create standardized splits stored as JSON (train perturbations, held-out genes, held-out cell types) for reproducibility.
   - Save `AnnData` objects with `obs` columns: `perturbation_id`, `cell_type`, `batch`, `modality_mask`.

6. **Baselines Data Interface**
   - Export `torch.utils.data.Dataset` wrappers for scGen, CPA, etc., ensuring identical splits.

7. **Versioning**
   - Track preprocessing steps via `DVC` or git-lfs, logging parameters in `metadata/preprocessing-log.yaml`.

## Immediate Tasks
- [ ] Download Replogle atlas processed `.h5ad` (~6 GB) and verify guide metadata.
- [ ] Script Mixology combinatorial dataset conversion to `.h5ad`.
- [ ] Acquire ECCITE-seq multi-omic counts; run TOTALVI to get RNA+protein latent embeddings.
