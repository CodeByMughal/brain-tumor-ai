"""Smoke Test: check library versions and that the dataset is in place"""

import sys
from pathlib import Path

import matplotlib
import pandas as pd
import numpy as np
import PIL

# ---- library Versions ----
print(f"Python:     {sys.version.split()[0]}")
print(f"Pandas:     {pd.__version__}")
print(f"NumPy:      {np.__version__}")
print(f"Matplotlib: {matplotlib.__version__}")
print(f"Pillow:     {PIL.__version__}")

# ---- Dataset check ----
DATA_DIR = Path("data/raw")

if not DATA_DIR.exists():
    sys.exit(f"Dataset not found at {DATA_DIR.resolve()} (see README)")


for split_dir in DATA_DIR.iterdir():
    if not split_dir.is_dir():
        continue
    print(f"{split_dir.name}")
    for class_dir in split_dir.iterdir():
        if not class_dir.is_dir():
            continue
        count = len(list(class_dir.iterdir()))
        print(f"  {class_dir.name:<12} {count}")

