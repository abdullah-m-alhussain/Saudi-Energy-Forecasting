# Benchmark Data Acquisition Guide

## Overview

To keep this repository lightweight and compliant with GitHub's file size limits, benchmark datasets are **not included** in the repository.

Each benchmark notebook automatically generates the required processed datasets from the original raw data. Therefore, only the original raw datasets are required before running the benchmark workflows.

Create the following directory structure if it does not already exist:

```text
benchmarks/
├── PJM/
│   └── data/
│       └── raw/
├── Spain/
│   └── data/
│       └── raw/
└── UCI_Household/
    └── data/
        └── raw/
```

---

# 1. PJM Benchmark

### Required file

```text
PJME_hourly.csv
```

### Destination

```text
benchmarks/PJM/data/raw/
```

### Data source

PJM Interconnection publishes historical electricity load data through its public data services.

Download the dataset containing **PJME_hourly.csv** and place the file in the directory above.

### Source and integrity record

| Field | Value |
|---|---|
| Dataset owner | PJM Interconnection |
| Dataset title | TODO: record the exact published dataset title |
| Dataset URL | TODO: add the canonical landing-page or download URL |
| Version / access date | TODO: record the version or date accessed |
| Required filename | `PJME_hourly.csv` |
| Archive and extraction | TODO: state whether an archive is supplied and how to extract it |
| SHA-256 checksum | TODO: calculate from the authoritative downloaded file |
| License / terms | TODO: record the applicable reuse terms |

---

# 2. Spain Benchmark

### Required files

```text
energy_dataset.csv
weather_features.csv
```

### Destination

```text
benchmarks/Spain/data/raw/
```

### Data source

The benchmark uses the public Spain electricity demand and weather dataset available on Kaggle.

Download the dataset, extract the archive, and copy the two required CSV files into the directory above.

### Source and integrity record

| Field | Value |
|---|---|
| Dataset owner | TODO: record the dataset owner/publisher |
| Dataset title | TODO: record the exact Kaggle dataset title |
| Dataset URL | TODO: add the canonical Kaggle dataset URL |
| Version / access date | TODO: record the version or date accessed |
| Required filenames | `energy_dataset.csv`; `weather_features.csv` |
| Archive and extraction | Download the source archive, extract it, and copy both CSV files to the destination above. TODO: record the archive filename. |
| SHA-256 checksums | TODO: calculate one checksum for each authoritative CSV |
| License / terms | TODO: record the Kaggle dataset license and any access requirements |

---

# 3. UCI Household Benchmark

### Required file

```text
household_power_consumption.txt
```

### Destination

```text
benchmarks/UCI_Household/data/raw/
```

### Data source

The benchmark uses the **Individual Household Electric Power Consumption** dataset from the UCI Machine Learning Repository.

Download the dataset, extract the archive, and copy the text file into the directory above.

### Source and integrity record

| Field | Value |
|---|---|
| Dataset owner | UCI Machine Learning Repository / TODO: record the original data creator |
| Dataset title | Individual Household Electric Power Consumption |
| Dataset URL | TODO: add the canonical UCI dataset URL |
| Version / access date | TODO: record the version or date accessed |
| Required filename | `household_power_consumption.txt` |
| Archive and extraction | Download and extract the source archive, then copy the required text file to the destination above. TODO: record the archive filename. |
| SHA-256 checksum | TODO: calculate from the authoritative extracted file |
| License / terms | TODO: record the applicable UCI dataset license and citation |

---

# Processed Data

Processed datasets are **not distributed** with this repository.

They are generated automatically when the corresponding benchmark notebook is executed.

If the processed-data directories are empty, simply run the appropriate benchmark notebook after placing the required raw dataset(s) in the correct `data/raw/` directory.

---

# Notes

- Keep the original filenames exactly as listed above.
- Place each dataset in its corresponding `data/raw/` directory.
- Do not rename any files.
- Do not place datasets in the project root.
- The benchmark notebooks assume this directory structure.

After the required raw datasets have been placed correctly, each benchmark notebook can be executed to generate the processed datasets and reproduce the benchmark results.

The TODO fields above must be completed from the authoritative source records before a
formal public release. They are intentionally not populated with unverified values.
