# brain-tumor-ai

An end-to-end brain tumor AI system, built step by step: from data exploration and
classical ML to deep-learning classification, 3D tumor segmentation on BraTS,
secure deployment, and a GenAI assistant (RAG + agents) on top.

## Status

**Phase 1: Python via data.** Environment set up; dataset exploration in progress.

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/CodeByMughal/brain-tumor-ai.git
cd brain-tumor-ai
```

### 2. Create and activate a virtual environment

Requires Python 3.12.

```bash
python -m venv .venv
```

Activate it:

- Windows (PowerShell): `.venv\Scripts\activate`
- Linux / macOS: `source .venv/bin/activate`

You should see `(.venv)` at the start of your terminal prompt.

> **Windows note:** if activation fails with "running scripts is disabled", run
> `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` once.
> If importing pandas fails with "An Application Control policy has blocked this file",
> Windows Smart App Control is blocking compiled libraries.

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Download the dataset

The dataset is **not** included in this repository (size and licensing).

1. Download it from [Kaggle](https://www.kaggle.com/datasets/masoudnickparvar/brain-tumor-mri-dataset).
2. Unzip it into `data/raw/` so the structure looks like this:

```
data/raw/
├── Training/
│   ├── glioma/
│   ├── meningioma/
│   ├── notumor/
│   └── pituitary/
└── Testing/
    ├── glioma/
    ├── meningioma/
    ├── notumor/
    └── pituitary/
```

Watch out for an extra nested folder (e.g. `data/raw/archive/Training/`) after unzipping.

### 5. Verify the setup

```bash
python scripts/check_env.py
```

Expected: library versions, then 4 classes under each split
(1400 images per class in `Training`, 400 per class in `Testing`).

## Dataset

- **Name:** Brain Tumor MRI Dataset (Kaggle) by Masoud Nickparvar 
- **Credit:** Dataset by Masoud Nickparvar, available on
  [Kaggle](https://www.kaggle.com/datasets/masoudnickparvar/brain-tumor-mri-dataset),
  licensed under CC BY 4.0.
- **License:** Attribution 4.0 International (CC BY 4.0)
- **Classes:** glioma, meningioma, notumor, pituitary
- **Format:** 2D MRI slices, JPG

## Known data issues

- Meningioma files are prefixed `aug` (e.g. `Tr-aug-me_1.jpg`), suggesting the class
  was padded with **augmented** images to reach a balanced count.
- Augmented images in the **test** set can inflate evaluation metrics, and augmented
  copies of the same original scan appearing in both splits would cause **data leakage**.
- This dataset is used for Python and data exploration only. Before any model
  evaluation, augmented files will be filtered out or replaced with the original release.

## Project structure

```
brain-tumor-ai/
├── data/raw/          # dataset (git-ignored)
├── notebooks/         # exploration
├── scripts/           # runnable scripts
├── src/               # reusable code
├── reports/figures/   # generated plots
└── PROGRESS.md        # learning log
```

## License

Code: MIT (see `LICENSE`). Dataset: see its own license above.