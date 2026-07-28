# Baseline Forecast Summary

Generated: 2026-07-23T17:33:32+03:00

## Baselines evaluated

- Naive: previous annual regional observation.
- Persistence: no-change forecast; mathematically identical to naive here.
- Historical mean: expanding regional mean through t−1.
- Moving average: mean of regional observations at t−1 and t−2.
- Seasonal naive: not scientifically appropriate for the annual target and not implemented.

## Results

| split | model | n_observations | MAE | RMSE | MAPE | R2 |
| --- | --- | --- | --- | --- | --- | --- |
| test | Moving Average (2-year) | 13 | 2,323,903,878.164 | 4,178,515,931.410 | 14.928 | 0.9226 |
| test | Naive | 13 | 3,050,746,607.318 | 4,773,581,114.159 | 23.656 | 0.8990 |
| test | Persistence | 13 | 3,050,746,607.318 | 4,773,581,114.159 | 23.656 | 0.8990 |
| test | Historical Mean | 13 | 3,500,664,048.243 | 5,664,021,617.856 | 26.669 | 0.8578 |
| validation | Naive | 13 | 1,682,348,599.077 | 2,547,485,217.383 | 27.109 | 0.9809 |
| validation | Persistence | 13 | 1,682,348,599.077 | 2,547,485,217.383 | 27.109 | 0.9809 |
| validation | Moving Average (2-year) | 13 | 3,003,103,114.385 | 4,415,550,204.813 | 38.665 | 0.9425 |
| validation | Historical Mean | 13 | 3,852,466,023.793 | 5,782,286,158.550 | 65.996 | 0.9014 |

## Reference baselines

- Lowest validation RMSE: **Naive** (2.547 billion kWh).
- Lowest test RMSE: **Moving Average (2-year)** (4.179 billion kWh).
- Later models should improve upon these references while preserving the fixed split.
