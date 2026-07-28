# Phase 1 Data Quality Report

Generated: 2026-07-23T14:38:10+03:00

## Scope

All files under `data/raw/` were inventoried. Historical files under `technical_work_reference/` were audited as non-authoritative artifacts and were not used as primary evidence.

## GASTAT and household CSV overlap

- Overlapping observations compared: 208
- Observations requiring a scientific source decision: 0
- Maximum absolute numeric difference: 0.000000477
- Tolerance: 0.001 in the reported unit.

The supplied CSV agrees with the original GASTAT 2019–2022 regional seasonal tables within numeric tolerance. Notebook 02 therefore selects GASTAT for overlapping years because it is the original publication, while retaining the CSV value and comparison evidence.

## Household panel coverage

- Raw household CSV years: 2017–2022
- Canonical administrative regions: 13
- Region-year combinations: 78
- Season counts other than two: 0
- Measure counts other than two: 0

## Important quality findings

- GASTAT workbooks use presentation layouts with multirow headers, titles, totals, footers, merged cells, and in 2020–2021 large formatted empty regions.
- Region spelling varies across years and sources; all mappings are explicit and no fuzzy matching is used.
- The national electricity-user CSV contains blank/metadata rows and a scale discontinuity in 2023–2024 that must be resolved before analytical use.
- The 2023 four-operating-region consumption file has an unclear unit definition and remains independent.
- Administrative-region household data must not be merged with four-region electricity-system data without an authoritative crosswalk.

## Formatting and metadata

Metadata rows and source/footer text are documented rather than silently treated as observations. Original raw files remain unchanged.
