import pandas as pd


def check_missing_recurring_vendors(
    current_df: pd.DataFrame,
    previous_df: pd.DataFrame,
) -> list[str]:
    """List vendors present in the previous period but absent from the current one."""
    for label, frame in (("current", current_df), ("previous", previous_df)):
        if "vendor" not in frame.columns:
            raise ValueError(f"{label} data is missing required column: vendor")

    previous_vendors = {
        str(vendor).strip()
        for vendor in previous_df["vendor"].dropna()
        if str(vendor).strip()
    }
    current_vendors = {
        str(vendor).strip()
        for vendor in current_df["vendor"].dropna()
        if str(vendor).strip()
    }
    return sorted(previous_vendors - current_vendors, key=str.casefold)
