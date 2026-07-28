# Evaluation Protocol

Generated: 2026-07-23T17:33:32+03:00

## Forecast definition

- Target: `annual_consumption_kwh`
- Unit: administrative region × target year
- Horizon: one year ahead
- Forecast origin: end of t−1

## Fixed chronological partitions

- Training: 2019–2020
- Validation: 2021
- Final test: 2022

Random splitting is prohibited because it leaks later temporal regimes into earlier forecasts and mixes region-year observations from the same national context.

## Model-development rule

Use 2021 for model selection and hyperparameter decisions. Do not inspect 2022 during selection. After fixing the specification, a future notebook may refit on data through 2021 and evaluate once on 2022.

## Metrics

- MAE in kWh
- RMSE in kWh
- MAPE in percent
- R² across the 13 regional observations in each holdout year

All future notebooks must import `src/evaluation.py` rather than redefining metrics.
