src/analyzer/duplicate_detection.py

def detect_duplicates(df):

 

    duplicates = df[

        df.duplicated(

            subset=["vendor", "amount"],

            keep=False

        )

    ]

 

    return duplicates