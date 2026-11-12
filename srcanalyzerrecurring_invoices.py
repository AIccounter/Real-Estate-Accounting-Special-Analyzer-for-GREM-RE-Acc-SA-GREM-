src/analyzer/recurring_invoices.py

def check_missing_recurring_vendors(

        current_df,

        previous_df):

 

    previous_vendors = set(previous_df["vendor"])

    current_vendors = set(current_df["vendor"])

 

    missing = previous_vendors - current_vendors

 

    return list(missing)