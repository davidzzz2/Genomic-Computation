"""Utility for fetching the Replogle et al. Perturb-seq atlas and converting it to AnnData.

Steps performed:
1. Download processed count matrices + metadata from the Broad single-cell portal.
2. Load matrices into AnnData, attach guide/cell annotations.
3. Save compressed `.h5ad` plus split metadata JSON.

NOTE: Requires manual portal token for authenticated downloads; set `BROAD_PORTAL_TOKEN` env var.
"""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path

import anndata as ad
import pandas as pd
import requests
from tqdm import tqdm

BROAD_BASE = "https://singlecell.broadinstitute.org/single_cell/api/v1"  # placeholder
DATASET_ID = "SCP1288"  # example ID for Replogle atlas


def download_file(url: str, dest: Path, token: str) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    headers = {"Authorization": f"Bearer {token}"}
    with requests.get(url, headers=headers, stream=True, timeout=60) as r:
        r.raise_for_status()
        total = int(r.headers.get("Content-Length", 0))
        with open(dest, "wb") as fh, tqdm(total=total, unit="B", unit_scale=True, desc=dest.name) as bar:
            for chunk in r.iter_content(chunk_size=1 << 20):
                if chunk:
                    fh.write(chunk)
                    bar.update(len(chunk))


def build_anndata(counts_path: Path, obs_path: Path, var_path: Path, out_path: Path) -> None:
    counts = ad.read_mtx(counts_path)
    obs = pd.read_csv(obs_path, index_col=0)
    var = pd.read_csv(var_path, index_col=0)
    adata = ad.AnnData(X=counts.X, obs=obs, var=var)
    adata.layers["counts"] = adata.X.copy()
    adata.write_h5ad(out_path, compression="gzip")


def main(out_dir: Path) -> None:
    token = os.environ.get("BROAD_PORTAL_TOKEN")
    if not token:
        raise RuntimeError("Set BROAD_PORTAL_TOKEN for authenticated downloads")

    dataset_dir = out_dir / "replogle"
    dataset_dir.mkdir(parents=True, exist_ok=True)

    files = {
        "matrix": f"{BROAD_BASE}/datasets/{DATASET_ID}/download?type=mtx",
        "obs": f"{BROAD_BASE}/datasets/{DATASET_ID}/download?type=cell_metadata",
        "var": f"{BROAD_BASE}/datasets/{DATASET_ID}/download?type=gene_metadata",
    }

    for key, url in files.items():
        dest = dataset_dir / f"{key}.tsv.gz"
        download_file(url, dest, token)

    build_anndata(
        counts_path=dataset_dir / "matrix.tsv.gz",
        obs_path=dataset_dir / "obs.tsv.gz",
        var_path=dataset_dir / "var.tsv.gz",
        out_path=dataset_dir / "replogle.h5ad",
    )

    split = {
        "held_out_genes": [],
        "held_out_celltypes": [],
        "timestamp": pd.Timestamp.utcnow().isoformat(),
    }
    with open(dataset_dir / "splits.json", "w", encoding="utf-8") as fh:
        json.dump(split, fh, indent=2)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, default=Path("data"))
    args = parser.parse_args()
    main(args.out)
