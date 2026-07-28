# Model Preparation Report

Generated: 2026-07-23T17:33:32+03:00

## Input

- Frozen Phase 2 feature dataset only.
- Input dimensions: 52 rows × 31 columns.
- No missing values, duplicate keys, or infinite numeric values.

## Outputs

- 11 model-ready CSV datasets with identical region-year alignment.
- 14 leakage-safe historical/time predictors.
- One reusable evaluation module.
- Validation and test predictions for four baseline labels.

## Scientific limitations

- Only four model-ready target years are available.
- Training contains 26 region-year observations and two target years.
- Regional observations within a year share national conditions and are not independent time replicates.
- Test metrics describe one held-out year and must not be over-generalized.
- Naive and persistence are identical for this annual one-step protocol.
- No current-year consumption, cost, ratio, or metadata variable is admitted as a predictor.
