# Real Estate Accounting Special Analyzer for GREM

An open-source Python MVP for reviewing structured real-estate accounting exports. It compares two periods, flags material account variances, and reports vendors present in the previous period but absent in the current one. Results are screening indicators, not accounting, audit, legal, or compliance conclusions.

## Quick start

Requires Python 3.10 or newer.

```bash
python -m venv .venv
# macOS/Linux
source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python src/main.py
```

The sample run writes `reports/report.txt`. You can provide your own CSV or Excel files:

```bash
python src/main.py --current path/to/current.csv --previous path/to/previous.xlsx --output reports/review.txt
```

Optional arguments are `--current`, `--previous`, `--rules`, and `--output`. Input files must have the columns `property`, `account`, `vendor`, and `amount`. Supported formats are CSV, XLSX, and XLSM. The variance threshold is configured in `config/rules.yaml`.

## Checks and tests

```bash
python -m pytest
```

## Project layout

```text
config/rules.yaml
sample_data/current_year.csv
sample_data/previous_year.csv
src/main.py
src/analyzer/variance.py
src/analyzer/recurring_invoices.py
src/importer/excel_importer.py
src/reporting/report_writer.py
tests/test_analysis.py
```

## Current limitations

- Vendor absence between two periods is only a signal; the tool does not verify invoice frequency or contractual recurrence.
- Variance analysis groups values by property and account. It does not yet analyze invoice dates, budgets, cost centers, currencies, or accounting-specific chart mappings.
- Keep real accounting exports confidential and ensure you have permission to process them. The sample files are synthetic.
- Direct ERP/GARAIO REM integration, PDF/OCR processing, dashboards, and machine-learning detection are not implemented.
