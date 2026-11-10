# Data Cleaning and Validation

The supplied CSV is already named as a cleaned dataset. The script here performs reproducible validation and standardisation checks; it does not claim to reconstruct undocumented raw-data cleaning steps.

## Input
`02_Data_Collection/hosteller_food_lifestyle.csv`

## Output
- `03_Data_Cleaning/Hosteller_Food_and_Lifestyle_Cleaned.csv`
- `03_Data_Cleaning/data_quality_report.txt`

## Run
```bash
python 03_Data_Cleaning/clean_data.py
```

The script checks required columns, empty cells, duplicate record IDs, date parsing and sensible ranges for weekly frequencies. Any issue is reported rather than silently hidden.
