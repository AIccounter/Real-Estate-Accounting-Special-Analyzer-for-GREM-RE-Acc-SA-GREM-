import pandas as pd

from analyzer.recurring_invoices import check_missing_recurring_vendors
from analyzer.variance import analyse_variances


def test_variance_threshold_and_new_account():
    previous = pd.DataFrame(
        [
            {"property": "A", "account": "Heating", "amount": 100},
            {"property": "A", "account": "Insurance", "amount": 100},
        ]
    )
    current = pd.DataFrame(
        [
            {"property": "A", "account": "Heating", "amount": 125},
            {"property": "A", "account": "Insurance", "amount": 110},
            {"property": "A", "account": "Repairs", "amount": 40},
        ]
    )

    result = analyse_variances(current, previous, threshold=20)

    assert set(result["account"]) == {"Heating", "Repairs"}
    heating = result.set_index("account").loc["Heating"]
    assert heating["variance_percent"] == 25.0
    assert heating["finding"] == "increase"
    repairs = result.set_index("account").loc["Repairs"]
    assert repairs["finding"] == "new account"


def test_duplicate_rows_are_aggregated_before_comparison():
    previous = pd.DataFrame(
        [{"property": "A", "account": "Heating", "amount": 100}]
    )
    current = pd.DataFrame(
        [
            {"property": "A", "account": "Heating", "amount": 60},
            {"property": "A", "account": "Heating", "amount": 60},
        ]
    )

    result = analyse_variances(current, previous, threshold=20)

    assert result.iloc[0]["current"] == 120
    assert result.iloc[0]["variance_percent"] == 20.0


def test_missing_vendors_are_sorted_and_ignore_empty_values():
    previous = pd.DataFrame({"vendor": ["Vendor B", "Vendor A", None, " "]})
    current = pd.DataFrame({"vendor": ["Vendor B"]})

    assert check_missing_recurring_vendors(current, previous) == ["Vendor A"]
