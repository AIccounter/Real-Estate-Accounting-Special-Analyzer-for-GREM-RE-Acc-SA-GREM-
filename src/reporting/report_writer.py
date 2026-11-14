from pathlib import Path


def write_report(variance_df, missing_vendors, filename="reports/report.txt") -> Path:
    """Write a plain-text analysis report and return its path."""
    report_path = Path(filename)
    report_path.parent.mkdir(parents=True, exist_ok=True)

    with report_path.open("w", encoding="utf-8") as report:
        report.write("REAL ESTATE ACCOUNTING ANALYZER\n\n")
        report.write("YEAR-OVER-YEAR VARIANCES\n")
        if variance_df.empty:
            report.write("No significant variances found.\n")
        else:
            report.write(variance_df.to_string(index=False))
            report.write("\n")

        report.write("\nMISSING RECURRING VENDORS\n")
        if not missing_vendors:
            report.write("No vendors from the previous period are missing.\n")
        else:
            for vendor in missing_vendors:
                report.write(f"- {vendor}\n")

    return report_path
