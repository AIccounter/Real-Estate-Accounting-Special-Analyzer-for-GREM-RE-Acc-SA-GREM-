import pandas as pd


KEY_COLUMNS = ["property", "account"]


def analyse_variances(
    current_df: pd.DataFrame,
    previous_df: pd.DataFrame,
    threshold: float = 20,
) -> pd.DataFrame:
    """Return account-level changes whose absolute variance meets the threshold.

    Amounts are summed by property and account first, so repeated journal lines
    do not create a many-to-many merge or inflate the findings.
    """
    for label, frame in (("current", current_df), ("previous", previous_df)):
        missing = set(KEY_COLUMNS + ["amount"]) - set(frame.columns)
        if missing:
            raise ValueError(
                f"{label} data is missing required columns: {', '.join(sorted(missing))}"
            )

    current = current_df.groupby(KEY_COLUMNS, dropna=False, as_index=False)["amount"].sum()
    previous = previous_df.groupby(KEY_COLUMNS, dropna=False, as_index=False)["amount"].sum()
    merged = current.merge(
        previous,
        on=KEY_COLUMNS,
        how="outer",
        suffixes=("_current", "_previous"),
        indicator=True,
    )

    findings = []
    for _, row in merged.iterrows():
        current_amount = row["amount_current"]
        previous_amount = row["amount_previous"]
        if row["_merge"] == "left_only":
            previous_amount = 0
            variance = None
            finding = "new account"
        elif row["_merge"] == "right_only":
            current_amount = 0
            variance = -100.0 if previous_amount != 0 else None
            finding = "missing account"
        elif previous_amount == 0:
            if current_amount == 0:
                continue
            variance = None
            finding = "new amount (previously zero)"
        else:
            variance = ((current_amount - previous_amount) / abs(previous_amount)) * 100
            if abs(variance) < threshold:
                continue
            finding = "increase" if variance > 0 else "decrease"

        findings.append(
            {
                "property": row["property"],
                "account": row["account"],
                "previous": previous_amount,
                "current": current_amount,
                "variance_percent": round(variance, 2) if variance is not None else None,
                "finding": finding,
            }
        )

    return pd.DataFrame(
        findings,
        columns=["property", "account", "previous", "current", "variance_percent", "finding"],
    )
