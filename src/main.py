import argparse
from pathlib import Path

import yaml

from analyzer.recurring_invoices import check_missing_recurring_vendors
from analyzer.variance import analyse_variances
from importer.excel_importer import load_file
from reporting.report_writer import write_report


ROOT_DIR = Path(__file__).resolve().parents[1]


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Analyze real-estate accounting exports for variances and missing vendors."
    )
    parser.add_argument(
        "--current", type=Path, default=ROOT_DIR / "sample_data/current_year.csv",
        help="Current-period CSV or Excel file.",
    )
    parser.add_argument(
        "--previous", type=Path, default=ROOT_DIR / "sample_data/previous_year.csv",
        help="Previous-period CSV or Excel file.",
    )
    parser.add_argument(
        "--rules", type=Path, default=ROOT_DIR / "config/rules.yaml",
        help="YAML rules configuration.",
    )
    parser.add_argument(
        "--output", type=Path, default=ROOT_DIR / "reports/report.txt",
        help="Output path for the text report.",
    )
    return parser


def main() -> None:
    args = build_parser().parse_args()
    with args.rules.open("r", encoding="utf-8") as config_file:
        config = yaml.safe_load(config_file) or {}

    threshold = float(config.get("variance_threshold_percent", 20))
    current_df = load_file(args.current)
    previous_df = load_file(args.previous)
    variance_df = analyse_variances(current_df, previous_df, threshold)
    missing_vendors = check_missing_recurring_vendors(current_df, previous_df)
    report_path = write_report(variance_df, missing_vendors, args.output)
    print(f"Analysis completed. Report written to: {report_path}")


if __name__ == "__main__":
    main()
