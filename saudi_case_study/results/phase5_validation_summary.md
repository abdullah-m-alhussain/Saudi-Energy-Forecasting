# Phase 5 Validation Summary

Generated: 2026-07-23T21:40:49+03:00

## Notebooks created

- `10_Model_Evaluation_and_Comparison.ipynb`
- `11_Final_Forecasts_and_Visualizations.ipynb`

## Frozen inputs used

- `results/baseline_results.csv`
- `results/arima/metrics.csv` and `predictions.csv`
- `results/random_forest/metrics.csv` and `predictions.csv`
- `results/xgboost/metrics.csv` and `predictions.csv`
- `results/hybrid/metrics.csv` and `predictions.csv`
- Notebook 10 approved comparison tables

## Outputs

- Five final evaluation/result files under `results/final/`
- Eight final comparison figures under `figures/final/`
- Four thesis table/note files under `results/thesis_tables/`
- Six thesis figures under `figures/thesis/`

## Reproducibility and integrity

- No model was retrained or rerun.
- No parameter, dataset, feature, split, or previous result was modified.
- Prediction keys and actual values were aligned before comparison.
- Baseline prediction-level analyses were not invented because Phase 3 saved metrics only.
- Formal significance tests were not performed because the sample is too small and spatially dependent.
- The official Phase 1–4 repository was hashed before Phase 5 and remains unchanged.

## Interpretation

The selected presentation model is `Random Forest`, based on a multi-criterion numerical
ranking. The conclusion remains conditional on one 2022 test year and does not imply causation.
