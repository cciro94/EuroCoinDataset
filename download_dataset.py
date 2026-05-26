"""
Download the EURO-Coin Dataset from Hugging Face Hub.

The full dataset (~4.9 GB, 12,878 images) is hosted at:
  https://huggingface.co/datasets/DAISLab-Unisa/EURO_Coin_Dataset

Usage
-----
    # Public access (no token required)
    python download_dataset.py

    # With a HuggingFace token (needed if the repo is private)
    python download_dataset.py --token hf_...

    # Download to a specific directory
    python download_dataset.py --dir /path/to/destination

Requirements
------------
    pip install huggingface_hub
"""

import argparse
import os
from huggingface_hub import snapshot_download, login


REPO_ID = "DAISLab-Unisa/EURO_Coin_Dataset"


def download(token: str | None = None, local_dir: str = ".") -> None:
    if token:
        login(token=token)

    print(f"Downloading {REPO_ID} into '{os.path.abspath(local_dir)}' ...")
    snapshot_download(
        repo_id=REPO_ID,
        repo_type="dataset",
        local_dir=local_dir,
        ignore_patterns=["samples/*", ".gitignore", "*.py"],
    )
    print("Done. Dataset downloaded successfully.")
    print(f"  - country_dataset/      → images organised by issuing country")
    print(f"  - denomination_dataset/ → images organised by denomination")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Download the EURO-Coin Dataset from Hugging Face Hub."
    )
    parser.add_argument(
        "--token",
        default=None,
        help="HuggingFace access token (required only for private repos).",
    )
    parser.add_argument(
        "--dir",
        default=".",
        help="Local directory where the dataset will be saved (default: current folder).",
    )
    args = parser.parse_args()
    download(token=args.token, local_dir=args.dir)
