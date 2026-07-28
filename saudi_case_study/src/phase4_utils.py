"""Shared, leakage-safe utilities for Phase 4 forecasting notebooks."""

from __future__ import annotations

from datetime import datetime
from pathlib import Path
import hashlib
import importlib
import importlib.util
import json
import platform

import numpy as np
import pandas as pd


TARGET = "annual_consumption_kwh"
KEYS = ["year", "region"]
PREDICTORS = [
    "time_index",
    "consumption_lag_1",
    "consumption_lag_2",
    "cost_lag_1",
    "cost_lag_2",
    "consumption_rolling_mean_2",
    "consumption_rolling_std_2",
    "cost_rolling_mean_2",
    "consumption_growth_lag_1_pct",
    "cost_growth_lag_1_pct",
    "winter_consumption_growth_lag_1_pct",
    "rest_consumption_growth_lag_1_pct",
    "region_historical_mean_consumption",
    "region_historical_mean_cost",
]
SPLIT_YEARS = {"train": [2019, 2020], "validation": [2021], "test": [2022]}
RANDOM_SEED = 42


def locate_project_root(start: Path) -> Path:
    start = start.resolve()
    for candidate in (start, *start.parents):
        if (candidate / "data" / "model_ready" / "train.csv").exists():
            return candidate
    raise FileNotFoundError("Run from the repository root or notebooks directory.")


def load_splits(project_root: Path):
    model_dir = project_root / "data" / "model_ready"
    frames = {}
    for split in ("train", "validation", "test"):
        combined = pd.read_csv(model_dir / f"{split}.csv").sort_values(KEYS).reset_index(drop=True)
        x_frame = pd.read_csv(model_dir / f"X_{split}.csv").sort_values(KEYS).reset_index(drop=True)
        y_frame = pd.read_csv(model_dir / f"y_{split}.csv").sort_values(KEYS).reset_index(drop=True)
        validate_split(split, combined, x_frame, y_frame)
        frames[split] = {"combined": combined, "X": x_frame, "y": y_frame}
    return frames


def validate_split(split, combined, x_frame, y_frame):
    expected_years = SPLIT_YEARS[split]
    if sorted(combined["year"].unique().tolist()) != expected_years:
        raise ValueError(f"{split} years differ from the frozen protocol.")
    if not x_frame[KEYS].equals(y_frame[KEYS]):
        raise ValueError(f"{split} X/y keys are not aligned.")
    if not combined[KEYS].equals(x_frame[KEYS]):
        raise ValueError(f"{split} combined/X keys are not aligned.")
    if combined.duplicated(KEYS).any() or x_frame.duplicated(KEYS).any():
        raise ValueError(f"{split} contains duplicate region-year keys.")
    missing_predictors = sorted(set(PREDICTORS) - set(x_frame.columns))
    if missing_predictors:
        raise ValueError(f"{split} is missing predictors: {missing_predictors}")
    if x_frame[PREDICTORS].isna().any().any() or y_frame[TARGET].isna().any():
        raise ValueError(f"{split} contains missing analytical values.")
    if not np.isfinite(x_frame[PREDICTORS].to_numpy(dtype=float)).all():
        raise ValueError(f"{split} contains infinite predictor values.")
    if not np.isfinite(y_frame[TARGET].to_numpy(dtype=float)).all():
        raise ValueError(f"{split} contains infinite target values.")
    if not combined["year"].is_monotonic_increasing:
        raise ValueError(f"{split} is not chronologically ordered.")


def load_evaluation_module(project_root: Path):
    path = project_root / "src" / "evaluation.py"
    spec = importlib.util.spec_from_file_location("saudi_evaluation", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def prediction_frame(keys, actual, predicted, model_name, split):
    frame = keys.reset_index(drop=True).copy()
    frame["actual"] = np.asarray(actual, dtype=float)
    frame["predicted"] = np.asarray(predicted, dtype=float)
    frame["residual"] = frame["actual"] - frame["predicted"]
    frame["absolute_error"] = frame["residual"].abs()
    frame["squared_error"] = frame["residual"] ** 2
    frame["model_name"] = model_name
    frame["dataset_split"] = split
    return frame


def evaluate_prediction_frame(evaluation, frame):
    return evaluation.evaluate_regression(
        frame["actual"],
        frame["predicted"],
        model_name=frame["model_name"].iloc[0],
        split=frame["dataset_split"].iloc[0],
    )


def package_versions(package_names):
    versions = {"python": platform.python_version(), "generated_at": datetime.now().astimezone().isoformat()}
    for name in package_names:
        try:
            module = importlib.import_module(name)
            versions[name] = getattr(module, "__version__", "available")
        except Exception as exc:
            versions[name] = f"UNAVAILABLE: {type(exc).__name__}: {exc}"
    return versions


def write_json(path: Path, payload):
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()
