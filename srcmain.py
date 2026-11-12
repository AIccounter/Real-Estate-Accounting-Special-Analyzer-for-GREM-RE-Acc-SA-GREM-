src/main.py

import yaml

 

from importer.excel_importer import load_file

from analyzer.variance import analyse_variances

from analyzer.recurring_invoices import (

    check_missing_recurring_vendors

)

from reporting.report_writer import write_report

 

def main():

 

    current_df = load_file(

        "sample_data/current_year.csv"

    )

 

    previous_df = load_file(

        "sample_data/previous_year.csv"

    )

 

    with open(

        "config/rules.yaml",

        "r",

        encoding="utf-8"

    ) as f:

        config = yaml.safe_load(f)

 

    threshold = config[

        "variance_threshold_percent"

    ]

 

    variance_df = analyse_variances(

        current_df,

        previous_df,

        threshold

    )

 

    missing_vendors = (

        check_missing_recurring_vendors(

            current_df,

            previous_df

        )

    )

 

    write_report(

        variance_df,

        missing_vendors

    )

 

    print(

        "Analysis completed."

    )

 

if __name__ == "__main__":

    main()