from pathlib import Path

import pandas as pd


REQUIRED_COLUMNS = {"property", "account", "vendor", "amount"}


def load_file(path: str | Path) -> pd.DataFrame:
    """Load a supported accounting export (CSV or Excel) into a DataFrame."""
    file_path = Path(path)
    if not file_path.is_file():
        raise FileNotFoundError(f"Input file not found: {file_path}")

    suffix = file_path.suffix.lower()
    if suffix == ".csv":
        data = pd.read_csv(file_path)
    elif suffix in {".xlsx", ".xlsm"}:
        data = pd.read_excel(file_path)
    else:
        raise ValueError(
            f"Unsupported file type '{suffix}'. Supported formats are .csv, .xlsx, and .xlsm."
        )

    data.columns = data.columns.astype(str).str.strip().str.lower()
    missing = REQUIRED_COLUMNS - set(data.columns)
    if missing:
        raise ValueError(
            f"{file_path} is missing required columns: {', '.join(sorted(missing))}"
        )

    data["amount"] = pd.to_numeric(data["amount"], errors="raise")
    return data
