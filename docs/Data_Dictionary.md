# Data Dictionary

## Overview

This document describes the datasets used throughout the Saudi Energy Forecasting Framework and explains how they are organized within the repository.

The project contains two complementary research components:

- **Benchmark Experiments** using publicly available datasets.
- **Saudi Case Study** using official Saudi household electricity consumption data.

The purpose of this document is to provide a high-level reference for the datasets, their organization, and the types of variables used during forecasting.

---

# Repository Data Organization

The repository separates datasets according to the research component.

```text
benchmarks/
    PJM/
    Spain/
    UCI_Household/

saudi_case_study/
```

The Saudi case study uses the complete staged data organization:

```text
data/
├── raw/
├── processed/
├── features/
└── model_ready/
```

Each benchmark uses `data/raw/` and `data/processed/` inside its own directory and
creates modeling features within its self-contained notebook. Benchmark raw and
processed datasets are intentionally omitted from version control; `.gitkeep` files
preserve the required directories.

The repository structure is designed to support a reproducible forecasting workflow from the original raw data through model-ready datasets.

---

# Benchmark Datasets

The benchmark experiments use publicly available datasets to evaluate forecasting methods under different conditions.

## PJM Benchmark

Dataset:

- PJM Hourly Energy Consumption

Primary content:

- Hourly electricity demand
- Timestamp information

Purpose:

- Regional electricity load forecasting benchmark

---

## Spain Benchmark

Dataset:

- Spain Energy Demand and Weather Dataset

Primary content:

- Electricity demand
- Weather observations
- Temporal information

Purpose:

- Multi-variable electricity demand forecasting benchmark

---

## UCI Household Benchmark

Dataset:

- Individual Household Electric Power Consumption

Primary content:

- Household electricity consumption
- Voltage
- Current
- Sub-metering measurements
- Timestamp information

Purpose:

- Residential electricity consumption forecasting benchmark

---

# Saudi Case Study

The Saudi case study forms the primary research contribution of this repository.

The datasets support regional household electricity consumption forecasting across the thirteen administrative regions of Saudi Arabia.

The forecasting workflow includes:

- raw datasets
- validated datasets
- processed datasets
- feature-engineered datasets
- model-ready datasets

---

# Dataset Categories

The forecasting framework organizes data into four primary categories.

## Raw Data

Original datasets obtained from their respective sources.

These files remain unchanged and provide the foundation for the reproducible workflow.

---

## Processed Data

Processed datasets contain cleaned, validated, and integrated observations suitable for analysis.

Typical processing steps include:

- data cleaning
- validation
- standardization
- integration

---

## Feature Datasets

Feature datasets contain variables generated during feature engineering.

Examples include:

- lag features
- rolling statistics
- growth indicators
- temporal features

---

## Model-Ready Data

Model-ready datasets contain the final predictor variables and forecasting targets used for model training and evaluation.

These datasets are generated automatically during the forecasting workflow.

---

# Variable Categories

Although variable names differ between datasets, they generally fall into the following categories:

- regional identifiers
- timestamps
- electricity consumption measurements
- weather variables (where applicable)
- engineered forecasting features
- forecasting target variables

Refer to the corresponding benchmark or Saudi case study documentation for dataset-specific variable descriptions.

---

# Notes

The benchmark policy and Saudi case-study policy are intentionally different:

- **Benchmarks:** raw datasets are externally acquired. Raw data, processed data,
  trained models, and full prediction outputs are not distributed. Lightweight
  metrics, logs, environment records, summaries, feature importance, and figures are
  retained.
- **Saudi case study:** the source, interim, processed, feature-engineered,
  model-ready, model, prediction, result, and figure artifacts currently present in
  the repository are retained as the research record. Their source attribution,
  licensing, and redistribution permissions must be confirmed before public release.

The notebooks regenerate their corresponding derived artifacts when the required
inputs are available.

Refer to:

- `benchmarks/DATA_ACQUISITION.md`
- `saudi_case_study/README.md`

for dataset acquisition and execution instructions.
