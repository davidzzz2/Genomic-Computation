"""Convert Mixology (Norman et al.) combinatorial Perturb-seq dataset to AnnData.
Assumes raw counts + metadata downloaded manually from GEO (GSE121981).
"""

from __future__ import annotations

import argparse
from pathlib import Path

import anndata as ad
import pandas as pd


def main(raw_dir: Path, out_path: Path) -> None:
    raw_counts = ad.read_10x_mtx(raw_dir)
    combos = pd.read_csv(raw_dir / "mixology_combinations.csv")
    cell_meta = pd.read_csv(raw_dir / "cell_metadata.csv", index_col=0)

    adata = raw_counts.copy()
    adata.obs = adata.obs.join(cell_meta, how="left")
    adata.obs["perturbation_a"] = adata.obs["guide_a"].map(dict(zip(combos["guide_a"], combos["gene_a"])))
    adata.obs["perturbation_b"] = adata.obs["guide_b"].map(dict(zip(combos["guide_b"], combos["gene_b"])))
    adata.obs["combo_label"] = adata.obs.apply(
        lambda row: "+".join(sorted(filter(None, [row["perturbation_a"], row["perturbation_b"]]))), axis=1
    )

    adata.write_h5ad(out_path, compression="gzip")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("raw_dir", type=Path)
    parser.add_argument("out", type=Path)
    args = parser.parse_args()
    main(args.raw_dir, args.out)
