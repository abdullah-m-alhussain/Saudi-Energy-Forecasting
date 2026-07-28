# Feature Engineering Report

Generated: 2026-07-23T16:01:19+03:00

## Scope and frozen inputs

- Input: `data/processed/saudi_household_admin_region_annual_panel.csv`
- Input: `data/processed/saudi_household_admin_region_seasonal_panel.csv`
- The Phase 1 files were read without modification.

## Forecasting unit

One row represents one administrative region in one year.

## Leakage controls

- All lag, rolling, growth, and historical regional features use values through t−1.
- Rolling windows are shifted before calculation.
- No random split, target-derived future value, or arbitrary polynomial interaction is used.

## History requirement

- Full input rows: 78
- Excluded warm-up rows: 26 (2017–2018)
- Final model-ready rows: 52
- Final coverage: 2019–2022, 13 regions
- Warm-up rows were excluded rather than imputed because two-year history does not exist.

## Quality control

- **rows**: 52
- **columns**: 31
- **duplicate_keys**: 0
- **missing_cells**: 0
- **infinite_cells**: 0
- **constant_columns**: 1
- **nonpositive_consumption_target**: 0
- **nonpositive_cost**: 0
- **negative_time_index**: 0
- **winter_share_outside_0_100**: 0
- **winter_cost_share_outside_0_100**: 0

## Constant columns

- selected_source

## Modeling cautions

- The final table is small; later evaluation must be chronological and uncertainty-aware.
- Current-year consumption and cost components must not be used to predict the same-year annual consumption target. Later model notebooks must define predictors according to the forecast origin.
- `region_id` is an identifier, not an ordinal measure. Later models should use appropriate categorical encoding or region-aware modeling.
- Lineage text fields are retained for auditability and should be excluded from numeric models.
