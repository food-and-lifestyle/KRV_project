"""Validate the supplied hosteller dataset and write a standardised copy.

Run from the repository root:
    python 03_Data_Cleaning/clean_data.py
"""
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "02_Data_Collection" / "hosteller_food_lifestyle.csv"
OUTPUT = ROOT / "03_Data_Cleaning" / "Hosteller_Food_and_Lifestyle_Cleaned.csv"
REPORT = ROOT / "03_Data_Cleaning" / "data_quality_report.txt"

REQUIRED = [
    "Hostel Type", "Department", "Meal Regularity Score",
    "Meal Habit Category", "Breakfast Days Per Week",
    "Lunch Days Per Week", "Dinner Days Per Week",
    "Daily Water Intake (Litres)", "Sleep Hours Per Day",
    "Physical Activity (Hours Per Week)", "Outside Food Days Per Week",
    "Monthly Food Budget (INR)", "Dominant Lifestyle Issue",
    "Observation Date", "Record ID", "Data Status",
]
WEEKLY_FIELDS = [
    "Breakfast Days Per Week", "Lunch Days Per Week",
    "Dinner Days Per Week", "Outside Food Days Per Week",
]

def main():
    if not INPUT.exists():
        raise FileNotFoundError(
            f"Dataset not found: {INPUT}\n"
            "Add the supplied CSV to 02_Data_Collection/ and name it "
            "hosteller_food_lifestyle.csv."
        )

    df = pd.read_csv(INPUT)
    missing_columns = [c for c in REQUIRED if c not in df.columns]
    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")

    issues = []
    missing_cells = int(df.isna().sum().sum())
    if missing_cells:
        issues.append(f"Missing cells: {missing_cells}")

    if df["Record ID"].duplicated().any():
        duplicate_count = int(df["Record ID"].duplicated().sum())
        issues.append(f"Duplicate Record IDs: {duplicate_count}")

    df["Observation Date"] = pd.to_datetime(
        df["Observation Date"], errors="coerce"
    )
    invalid_dates = int(df["Observation Date"].isna().sum())
    if invalid_dates:
        issues.append(f"Invalid observation dates: {invalid_dates}")

    for column in WEEKLY_FIELDS:
        invalid = ~df[column].between(0, 7)
        if invalid.any():
            issues.append(f"{column}: {int(invalid.sum())} values outside 0-7")

    if (df["Daily Water Intake (Litres)"] < 0).any():
        issues.append("Negative water-intake values found")
    if (df["Sleep Hours Per Day"] < 0).any():
        issues.append("Negative sleep-duration values found")
    if (df["Monthly Food Budget (INR)"] < 0).any():
        issues.append("Negative monthly budget values found")

    # Keep all source records; report problems for review instead of silently
    # dropping records or inventing replacement values.
    df.to_csv(OUTPUT, index=False, date_format="%Y-%m-%d")

    status_values = df["Data Status"].dropna().astype(str).unique().tolist()
    report = [
        "HOSTELLER DATA QUALITY REPORT",
        "=" * 32,
        f"Rows: {len(df)}",
        f"Columns: {len(df.columns)}",
        f"Missing cells: {missing_cells}",
        f"Duplicate Record IDs: {int(df['Record ID'].duplicated().sum())}",
        f"Invalid dates: {invalid_dates}",
        f"Data status values: {status_values}",
        "",
        "Issues requiring review:",
        *(issues if issues else ["No validation issues detected."]),
        "",
        "Provenance note: preserve the source Data Status field. Synthetic",
        "coursework data must not be described as real student survey data.",
    ]
    REPORT.write_text("\n".join(report), encoding="utf-8")
    print(f"Validated dataset saved to: {OUTPUT}")
    print(f"Quality report saved to: {REPORT}")

if __name__ == "__main__":
    main()
