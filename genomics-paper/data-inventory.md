# Data Inventory (Initial Pass)

| Dataset | Modalities | Perturbation Types | Scale | Source / Access | Notes |
|---------|------------|--------------------|-------|------------------|-------|
| **Replogle et al. 2022 Perturb-seq Atlas** | scRNA-seq (+ CRISPR guide labels) | CRISPRi/a gene knockdowns/ups in K562, HEK293T, others | 2.5M cells, ~6,000 perturbations | GEO: GSE181546; Broad portal | Rich single-cell RNA + guide metadata; no ATAC/protein but good for baseline training + validation |
| **Mixology (Norman et al.) Perturb-seq** | scRNA-seq | Combinatorial CRISPRi pairs targeting TFs | ~1M cells | GEO: GSE121981 | Essential for combinatorial perturbation generalization tests |
| **Perturb-seq v3 (Frangieh et al. 2023)** | scRNA + multiplexed cytokine stimulation | CRISPR KO + stimulation conditions | 0.7M cells | GEO: GSE205117 | Adds environmental cues; good for context conditioning |
| **10x Genomics Multiome Perturbation Pilot** | Paired scRNA + scATAC | CRISPR knockouts (K562) | 200k cells | 10x support site | Limited perturbation diversity but gives matched RNA/ATAC |
| **ECCITE-seq (Mimitou et al.)** | RNA + surface proteins + TCR + CRISPR guides | CRISPR KO + protein readouts | 300k cells | GEO: GSE133344 | Provides protein modality for multi-omic coherence |
| **OptoSeq / Light-activated Perturb-seq** | RNA | Temporal perturbations | 100k cells | Preprint data share | Useful for dynamic validation |
| **Drug-response CITE-seq (Haney et al. 2024)** | RNA + surface proteins | Small-molecule treatments | 500k cells, 250 compounds | Proprietary? (check SRA) | Needed for chemical perturbation generalization |
| **Human Cell Atlas Multiome (no perturb.)** | RNA + ATAC | None | 10M+ cells | HCA portal | Not perturbed, but supplies diverse baseline states for conditioning/simulation |

**Action items**
- Download & preprocess key open datasets (Replogle, Mixology, ECCITE). 
- Verify licensing/usage for drug-response datasets; identify public subsets if proprietary.
- Plan synthetic augmentation to align modalities when not jointly measured (e.g., align scRNA-only perturbations with matched ATAC via shared latent space).
