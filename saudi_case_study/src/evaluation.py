# Reusable regression evaluation for Saudi household forecasts.

from __future__ import annotations

import numpy as np
import pandas as pd


METRIC_COLUMNS = ["MAE", "RMSE", "MAPE", "R2"]


def evaluate_regression(y_true, y_pred, model_name=None, split=None):
    'Return MAE, RMSE, MAPE (%), and R² with strict finite-value checks.'
    actual = np.asarray(y_true, dtype=float)
    predicted = np.asarray(y_pred, dtype=float)
    if actual.shape != predicted.shape:
        raise ValueError("Actual and predicted arrays must have identical shapes.")
    if actual.size == 0:
        raise ValueError("Evaluation arrays cannot be empty.")
    if not np.isfinite(actual).all() or not np.isfinite(predicted).all():
        raise ValueError("Evaluation arrays must contain only finite values.")
    if np.any(actual == 0):
        raise ValueError("MAPE is undefined when an actual target equals zero.")

    residual = actual - predicted
    mae = float(np.mean(np.abs(residual)))
    rmse = float(np.sqrt(np.mean(residual ** 2)))
    mape = float(np.mean(np.abs(residual / actual)) * 100)
    denominator = float(np.sum((actual - np.mean(actual)) ** 2))
    r2 = float(1 - np.sum(residual ** 2) / denominator) if denominator > 0 else np.nan

    result = {"MAE": mae, "RMSE": rmse, "MAPE": mape, "R2": r2}
    if model_name is not None:
        result["model"] = model_name
    if split is not None:
        result["split"] = split
    return result


def evaluate_prediction_frame(frame, actual_column, prediction_columns, split=None):
    'Evaluate multiple named prediction columns using one consistent implementation.'
    records = []
    for column in prediction_columns:
        records.append(
            evaluate_regression(
                frame[actual_column],
                frame[column],
                model_name=column,
                split=split,
            )
        )
    return pd.DataFrame(records)
