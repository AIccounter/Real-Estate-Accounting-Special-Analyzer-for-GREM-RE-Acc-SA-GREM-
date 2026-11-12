src/reporting/report_writer.py

from pathlib import Path

 

def write_report(

    variance_df,

    missing_vendors,

    filename="reports/report.txt"

):

 

    Path("reports").mkdir(

        parents=True,

        exist_ok=True

    )

 

    with open(filename, "w", encoding="utf-8") as report:

 

        report.write(

            "REAL ESTATE ACCOUNTING ANALYZER\n\n"

        )

 

        report.write(

            "YEAR-OVER-YEAR VARIANCES\n"

        )

 

        report.write(

            variance_df.to_string(index=False)

        )

 

        report.write("\n\n")

 

        report.write(

            "MISSING RECURRING VENDORS\n"

        )

 

        for vendor in missing_vendors:

            report.write(

                f"- {vendor}\n"

            )