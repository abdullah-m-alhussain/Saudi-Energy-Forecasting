# Saudi Energy Forecasting Framework

A reproducible research framework for forecasting household electricity consumption using statistical, machine learning, and hybrid forecasting models, with a primary focus on Saudi Arabia and complementary benchmark datasets.

---

## Overview

This repository contains the complete implementation developed as part of an MSc research project on electricity consumption forecasting.

The project follows a reproducible research workflow beginning with data collection and validation, continuing through feature engineering and model development, and concluding with forecasting evaluation and comparison.

Two complementary research components are included:

- **Benchmark Experiments** – public datasets used to evaluate and compare forecasting methodologies under different conditions.
- **Saudi Case Study** – a regional household electricity consumption forecasting framework developed using official Saudi datasets covering the thirteen administrative regions.

---

## Quick Start

1. Clone this repository.
2. Create the project environment using:

```bash
conda env create -f environment.yml
conda activate saudi-energy-forecasting
```

3. Obtain the required datasets by following the instructions in:
   - `benchmarks/DATA_ACQUISITION.md`
   - `saudi_case_study/README.md`

4. Execute the benchmark or Saudi case study notebooks from their respective `notebooks/` directories.

---

## Data and Artifact Policy

Benchmark source datasets are obtained externally and are not committed. Benchmark
processed datasets, trained models, and full prediction outputs are also excluded;
the repository retains lightweight metrics, logs, environment records, summaries,
feature importance, and figures.

The Saudi case study currently retains its source and derived research artifacts.
See `benchmarks/DATA_ACQUISITION.md`, `docs/Data_Dictionary.md`, and
`saudi_case_study/README.md` for the component-specific policy and workflow.

---

## Research Objectives

The framework was developed to:

- Build a reproducible electricity forecasting workflow.
- Compare baseline, statistical, machine learning, and hybrid forecasting models.
- Investigate forecasting performance under limited-data conditions.
- Evaluate forecasting methods for Saudi regional household electricity consumption.
- Assess whether hybrid forecasting approaches provide improved predictive performance.

---

## Repository Structure

```text
Saudi_Energy_Forecasting/

├── benchmarks/
│   Public benchmark forecasting experiments
│
├── saudi_case_study/
│   ├── src/
│   │   Shared Saudi workflow utilities
│   └── Saudi household electricity forecasting framework
│
├── docs/
│   Project documentation
│
├── environment.yml
│   Project environment specification
│
├── CITATION.cff
│   Citation metadata
│
├── LICENSE
│   Repository license
│
└── README.md
```

---

## Forecasting Workflow

The Saudi forecasting framework follows the workflow below:

1. Data collection and validation
2. Data integration
3. Exploratory data analysis
4. Feature engineering
5. Baseline forecasting
6. Statistical forecasting (ARIMA)
7. Machine learning forecasting
8. Hybrid forecasting
9. Model evaluation
10. Final forecasting and visualization

---

## Forecasting Models

The project evaluates multiple forecasting approaches, including:

### Baseline Models

- Naïve Forecast
- Persistence Forecast
- Historical Mean
- Moving Average

### Statistical Model

- ARIMA

### Machine Learning Models

- Random Forest
- XGBoost

### Hybrid Model

- Hybrid forecasting framework combining statistical and machine learning predictions.

---

## Repository Components

### Benchmarks

The benchmark experiments provide reference implementations using publicly available datasets. These experiments establish common forecasting baselines and demonstrate the behavior of different algorithms outside the Saudi case study.

Each benchmark is implemented as a self-contained Jupyter notebook. Dataset acquisition instructions, execution details, and benchmark-specific documentation are provided in:

`benchmarks/README.md`

---

### Saudi Case Study

The Saudi case study presents the primary research contribution of this repository.

It includes:

- Official Saudi household electricity datasets
- Regional data integration
- Feature engineering
- Forecast model development
- Model comparison
- Hybrid forecasting
- Final evaluation

The complete workflow and execution instructions are provided in:

`saudi_case_study/README.md`

---

## Documentation

Additional documentation is available in the `docs/` directory.

This includes:

- Project overview
- Methodology
- Reproducibility guide
- Research contribution
- Data documentation

---

## Research Status

Current repository status:

- Dataset construction completed
- Feature engineering completed
- Baseline forecasting completed
- Statistical forecasting completed
- Machine learning forecasting completed
- Hybrid forecasting completed
- Model evaluation completed
- Documentation completed for the current release candidate

---

## Citation

Citation information for this project is provided in `CITATION.cff`.

---

## License

This project is distributed under the license provided in the `LICENSE` file.
