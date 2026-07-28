# ARIMA Summary Report

- Selected configuration: **ARIMA(0,1,0)_linear_drift**
- Selection data: 2021 validation only
- Test year: 2022, evaluated once after configuration selection
- Regional histories: four observations for validation and five for test
- Fit/fallback events: 0

## Scientific limitations

The series are far too short for reliable stationarity testing, parameter inference, or complex
ARIMA identification. AIC values are diagnostic only and were not used for cross-configuration
selection. Regional fits may be numerically fragile. All failures are retained in diagnostics,
and the documented last-observation fallback prevents silent row loss.
