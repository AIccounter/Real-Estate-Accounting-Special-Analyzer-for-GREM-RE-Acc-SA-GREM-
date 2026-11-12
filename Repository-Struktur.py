Repository-Struktur

real-estate-accounting-analyzer/

│

├── README_DE.md

├── README_EN.md

├── LICENSE

├── .gitignore

├── requirements.txt

├── pyproject.toml

│

├── config/

│   └── rules.yaml

│

├── sample_data/

│   ├── current_year.csv

│   └── previous_year.csv

│

├── reports/

│   └── .gitkeep

│

├── src/

│   ├── main.py

│   │

│   ├── importer/

│   │   ├── __init__.py

│   │   └── excel_importer.py

│   │

│   ├── analyzer/

│   │   ├── __init__.py

│   │   ├── variance.py

│   │   ├── recurring_invoices.py

│   │   └── duplicate_detection.py

│   │

│   └── reporting/

│       ├── __init__.py

│       └── report_writer.py

│

└── tests/

    └── test_variance.py