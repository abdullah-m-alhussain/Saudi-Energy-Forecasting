# Exploratory Analysis Summary

Generated: 2026-07-23T16:00:58+03:00

## Scope

This analysis uses only the frozen Phase 1 validated annual and seasonal panels.

## Data-quality verification

- **annual_missing_required**: 0
- **seasonal_missing_required**: 0
- **annual_duplicate_keys**: 0
- **seasonal_duplicate_keys**: 0
- **nonpositive_annual_consumption**: 0
- **nonpositive_annual_cost**: 0
- **nonpositive_seasonal_consumption**: 0
- **nonpositive_seasonal_cost**: 0

## Key findings

- The validated annual panel contains 78 observations for 13 regions over 2017–2022.
- The seasonal panel contains 156 observations and exactly two published seasonal components for every region-year.
- No missing required analytical values, duplicate keys, non-positive consumption, or non-positive cost values remain.
- Riyadh has the highest mean annual household consumption (55.95 billion kWh), while Northern Borders has the lowest (1.95 billion kWh).
- The regional-sum annual consumption changed by -34.23% between 2017 and 2022.
- The median observed average cost is 0.2153 SAR/kWh, and the median winter share is 18.38%.
- The IQR procedure flags 21 variable-observations for review; these are retained because cross-region scale differences can be substantive.
- The panel is temporally balanced, but six annual observations per region are a short time series; later model evaluation must use chronological validation and report uncertainty cautiously.

## Interpretation limits

- Associations and correlations are descriptive and do not establish causality.
- IQR flags identify unusual scale, not necessarily erroneous observations.
- Regional sums should not be described as independently published national totals.
- The 2017–2018 source-provenance limitation documented in Phase 1 remains applicable.
