src/importer/excel_importer.py

import pandas as pd

 

def load_file(path: str):

    if path.endswith(".xlsx"):

        return pd.read_excel(path)

 

    return pd.read_csv(path)