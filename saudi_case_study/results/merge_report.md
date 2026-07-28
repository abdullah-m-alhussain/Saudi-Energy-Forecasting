# Household Source Merge Report

Generated: 2026-07-23T14:38:38+03:00

## Authoritative inputs

- Original GASTAT household workbooks for 2019–2022.
- `houses-consumption-and-cost-of-electricity-in-the-administrative-regions- (2).csv` for 2017–2022.
- No historical merged panel, ML feature file, prediction, model, or metric was used.

## Merge key

`year + canonical administrative region + season + measure + unit`

## Overlap result

- Compared observations: 208
- Unresolved observations: 0
- Maximum absolute difference: 0.000000477
- Absolute tolerance: 0.001

## Source selection

- 2019–2022: original GASTAT workbook selected after the supplied CSV agreed within tolerance.
- 2017–2018: supplied household CSV selected because it is the only authoritative source provided.
- National total rows were used for reconciliation and excluded from regional panel rows.

## Important limitation

The publisher/provenance metadata for the supplied 2017–2018 CSV observations should be completed before publication. Their values are retained with explicit source labels rather than represented as GASTAT observations.
