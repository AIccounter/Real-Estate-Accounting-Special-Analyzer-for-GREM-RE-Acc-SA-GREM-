src/analyzer/variance.py

import pandas as pd

 

def analyse_variances(current_df, previous_df, threshold=20):

 

    merged = current_df.merge(

        previous_df,

        on=["property", "account"],

        suffixes=("_current", "_previous")

    )

 

    findings = []

 

    for _, row in merged.iterrows():

 

        prev = row["amount_previous"]

        curr = row["amount_current"]

 

        if prev == 0:

            continue

 

        variance = ((curr - prev) / prev) * 100

 

        if abs(variance) >= threshold:

            findings.append({

                "property": row["property"],

                "account": row["account"],

                "previous": prev,

                "current": curr,

                "variance_percent": round(variance, 2)

            })

 

    return pd.DataFrame(findings)

