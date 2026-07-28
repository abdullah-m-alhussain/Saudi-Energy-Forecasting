# PJM Benchmark

## Overview

This benchmark evaluates the forecasting framework using historical electricity demand data from the PJM Interconnection. It serves as one of the three public benchmark datasets used to assess the robustness and generalizability of the proposed machine learning forecasting framework.

The benchmark is implemented as a **single Jupyter notebook** that performs the complete workflow, including:

- Raw data loading
- Data preprocessing
- Feature engineering
- Model training
- Model evaluation
- Result generation

---

# Dataset

### Required file

```
PJME_hourly.csv
```

### Destination

```
data/raw/
```

Instructions for obtaining the dataset are provided in:

```
../DATA_ACQUISITION.md
```

---

# Directory Structure

```
PJM/
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
│   └── PJM_Benchmark.ipynb
├── models/
├── results/
├── figures/
└── README.md
```

---

# Execution

After placing the required dataset in `data/raw/`, open the following notebook from the `notebooks/` directory:

```
PJM_Benchmark.ipynb
```

The notebook performs the complete benchmark workflow, including preprocessing, feature engineering, model training, evaluation, and figure generation.

---

# Outputs

Executing the notebook regenerates:

- Processed datasets
- Trained machine learning models
- Prediction outputs
- Evaluation metrics
- Benchmark figures
- Execution logs

To keep the repository lightweight, large generated artifacts (processed datasets, trained models, and full prediction outputs) are intentionally excluded from version control. Summary metrics, logs, environment information, and figures are retained for documentation and reproducibility.

---

# Notes

- Keep the raw dataset filename unchanged.
- Place the raw dataset inside `data/raw/`.
- Execute the notebook from the `notebooks/` directory.
- The benchmark is fully reproducible using the provided notebook, the project environment, and the required external dataset.