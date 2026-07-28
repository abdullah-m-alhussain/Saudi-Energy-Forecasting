# Phase 1 Household Panel Validation Summary

Generated: 2026-07-23T14:38:38+03:00

- Annual panel rows: 78
- Seasonal panel rows: 156
- Years: 2017–2022
- Administrative regions: 13
- Missing required annual numeric values: 0
- Duplicate annual keys: 0
- Duplicate seasonal keys: 0

## Check results

- **PASS** — 2017 administrative-region coverage: observed `13.0`, expected `13`
- **PASS** — 2018 administrative-region coverage: observed `13.0`, expected `13`
- **PASS** — 2019 administrative-region coverage: observed `13.0`, expected `13`
- **PASS** — 2020 administrative-region coverage: observed `13.0`, expected `13`
- **PASS** — 2021 administrative-region coverage: observed `13.0`, expected `13`
- **PASS** — 2022 administrative-region coverage: observed `13.0`, expected `13`
- **PASS** — 2017 Rest of the year regional sum versus reported total: observed `1.0`, expected `absolute difference <= 5.0 kWh/SAR (published-total rounding tolerance)`
- **PASS** — 2017 Winter regional sum versus reported total: observed `0.00041961669921875`, expected `absolute difference <= 5.0 kWh/SAR (published-total rounding tolerance)`
- **PASS** — 2018 Rest of the year regional sum versus reported total: observed `2.0`, expected `absolute difference <= 5.0 kWh/SAR (published-total rounding tolerance)`
- **PASS** — 2018 Winter regional sum versus reported total: observed `1.0`, expected `absolute difference <= 5.0 kWh/SAR (published-total rounding tolerance)`
- **PASS** — 2019 Rest of the year regional sum versus reported total: observed `2.0`, expected `absolute difference <= 5.0 kWh/SAR (published-total rounding tolerance)`
- **PASS** — 2019 Winter regional sum versus reported total: observed `1.0`, expected `absolute difference <= 5.0 kWh/SAR (published-total rounding tolerance)`
- **PASS** — 2020 Rest of the year regional sum versus reported total: observed `1.0`, expected `absolute difference <= 5.0 kWh/SAR (published-total rounding tolerance)`
- **PASS** — 2020 Winter regional sum versus reported total: observed `1.0`, expected `absolute difference <= 5.0 kWh/SAR (published-total rounding tolerance)`
- **PASS** — 2021 Rest of the year regional sum versus reported total: observed `3.0`, expected `absolute difference <= 5.0 kWh/SAR (published-total rounding tolerance)`
- **PASS** — 2021 Winter regional sum versus reported total: observed `2.0`, expected `absolute difference <= 5.0 kWh/SAR (published-total rounding tolerance)`
- **PASS** — 2022 Rest of the year regional sum versus reported total: observed `0.00018310546875`, expected `absolute difference <= 5.0 kWh/SAR (published-total rounding tolerance)`
- **PASS** — 2022 Winter regional sum versus reported total: observed `5.340576171875e-05`, expected `absolute difference <= 5.0 kWh/SAR (published-total rounding tolerance)`

All annual values were calculated only when both seasonal components were present. No missing component was replaced with zero.

Reported national totals differ from summed regional components by at most three kWh/SAR units in the supplied sources. These immaterial arithmetic differences are classified as published-total rounding; regional observations were not modified.
