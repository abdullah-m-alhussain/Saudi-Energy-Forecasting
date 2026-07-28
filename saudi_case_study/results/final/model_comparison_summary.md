# Model Comparison Summary

## Scope

Eight approaches are compared using the frozen 2021 validation and 2022 test outputs.
Prediction-level regional analyses cover ARIMA, Random Forest, XGBoost, and Hybrid because
baseline prediction rows were not saved in Phase 3.

## Numerical findings

- **Random Forest** and **Moving average baseline** share the leading mean numerical
  rank (2.50). Random Forest is listed first only because
  its test RMSE is lower under the declared tie-break.
- Random Forest test RMSE: 3.887 billion kWh.
- Moving-average baseline test RMSE: 4.179 billion kWh.
- ARIMA validation RMSE: 2.424 billion kWh; test RMSE:
  5.248 billion kWh.

## Interpretation

The leading numerical rank reflects several error criteria and validation-to-test stability,
not one metric. The moving-average baseline remains competitive and is much simpler. ARIMA is
strongest on validation but deteriorates on the single test year; supplied hybrid weights
collapse to ARIMA, so the hybrid does not diversify component errors.

## Statistical limitation

No formal significance test is performed. There are only 13 regional errors in one test year,
regions share national conditions, and only two holdout years exist. Standard independent-sample
or long-series forecast comparison tests would overstate evidence.
