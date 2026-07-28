# Feature Selection Report

Generated: 2026-07-23T17:33:32+03:00

## Forecast origin

Predict annual regional household consumption for year t using information available by the end of t−1.

## Complete variable decisions

| variable | category | role | decision_reason |
| --- | --- | --- | --- |
| year | Time | Key (not numeric predictor) | Region-year observation key retained for alignment and grouping. |
| region | Identifier | Key (not numeric predictor) | Region-year observation key retained for alignment and grouping. |
| annual_consumption_kwh | Consumption | Target | One-year-ahead regional household consumption target. |
| annual_cost_sar | Cost | Excluded | Current-year outcome unavailable at the end of t−1. |
| winter_consumption_kwh | Consumption | Excluded | Current-year target component; deterministically leaks target information. |
| rest_of_year_consumption_kwh | Consumption | Excluded | Current-year target component; deterministically leaks target information. |
| winter_cost_sar | Cost | Excluded | Current-year outcome unavailable at forecast origin. |
| rest_of_year_cost_sar | Cost | Excluded | Current-year outcome unavailable at forecast origin. |
| average_cost_sar_per_kwh | Ratio / intensity | Excluded | Uses current-year target in its denominator and current-year cost. |
| winter_consumption_share_pct | Ratio / intensity | Excluded | Calculated from current-year target components. |
| selected_source | Metadata / lineage | Excluded | Source-lineage metadata, not a forecasting signal. |
| source_file | Metadata / lineage | Excluded | Source-lineage metadata, not a forecasting signal. |
| time_index | Time | Predictor | Known by forecast origin and scientifically relevant historical predictor. |
| region_id | Identifier | Excluded | Arbitrary nominal code; numeric use would impose false ordinality. |
| rest_to_winter_consumption_ratio | Ratio / intensity | Excluded | Calculated from current-year consumption components. |
| winter_to_rest_consumption_ratio | Ratio / intensity | Excluded | Calculated from current-year consumption components. |
| winter_cost_share_pct | Ratio / intensity | Excluded | Calculated from current-year costs. |
| consumption_lag_1 | Lag | Predictor | Known by forecast origin and scientifically relevant historical predictor. |
| cost_lag_1 | Lag | Predictor | Known by forecast origin and scientifically relevant historical predictor. |
| consumption_lag_2 | Lag | Predictor | Known by forecast origin and scientifically relevant historical predictor. |
| cost_lag_2 | Lag | Predictor | Known by forecast origin and scientifically relevant historical predictor. |
| consumption_rolling_mean_2 | Rolling statistic | Predictor | Known by forecast origin and scientifically relevant historical predictor. |
| consumption_rolling_std_2 | Rolling statistic | Predictor | Known by forecast origin and scientifically relevant historical predictor. |
| cost_rolling_mean_2 | Rolling statistic | Predictor | Known by forecast origin and scientifically relevant historical predictor. |
| consumption_growth_lag_1_pct | Growth | Predictor | Known by forecast origin and scientifically relevant historical predictor. |
| cost_growth_lag_1_pct | Growth | Predictor | Known by forecast origin and scientifically relevant historical predictor. |
| winter_consumption_growth_lag_1_pct | Growth | Predictor | Known by forecast origin and scientifically relevant historical predictor. |
| rest_consumption_growth_lag_1_pct | Growth | Predictor | Known by forecast origin and scientifically relevant historical predictor. |
| region_historical_mean_consumption | Regional historical | Predictor | Known by forecast origin and scientifically relevant historical predictor. |
| region_historical_mean_cost | Regional historical | Predictor | Known by forecast origin and scientifically relevant historical predictor. |
| source_lineage | Metadata / lineage | Excluded | Source-lineage metadata, not a forecasting signal. |

## Predictor contract

The exported X files contain `year` and `region` alignment keys followed by these approved predictors:

- `time_index`
- `consumption_lag_1`
- `consumption_lag_2`
- `cost_lag_1`
- `cost_lag_2`
- `consumption_rolling_mean_2`
- `consumption_rolling_std_2`
- `cost_rolling_mean_2`
- `consumption_growth_lag_1_pct`
- `cost_growth_lag_1_pct`
- `winter_consumption_growth_lag_1_pct`
- `rest_consumption_growth_lag_1_pct`
- `region_historical_mean_consumption`
- `region_historical_mean_cost`
