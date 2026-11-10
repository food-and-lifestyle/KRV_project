"""Create descriptive summaries from the validated coursework dataset."""
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "03_Data_Cleaning" / "Hosteller_Food_and_Lifestyle_Cleaned.csv"
OUT = ROOT / "04_Data_Analysis" / "outputs"

def main():
    if not INPUT.exists():
        raise FileNotFoundError("Run 03_Data_Cleaning/clean_data.py first.")
    OUT.mkdir(parents=True, exist_ok=True)
    df = pd.read_csv(INPUT)

    numeric = df.select_dtypes(include="number")
    numeric.describe().T.to_csv(OUT / "numeric_summary.csv")

    for category in ["Hostel Type", "Department", "Meal Habit Category",
                     "Dominant Lifestyle Issue"]:
        if category in df:
            df[category].value_counts(dropna=False).rename_axis(
                category
            ).reset_index(name="Count").to_csv(
                OUT / f"{category.lower().replace(' ', '_')}_counts.csv",
                index=False
            )

    grouped = df.groupby("Hostel Type", dropna=False).agg(
        records=("Record ID", "count"),
        avg_sleep_hours=("Sleep Hours Per Day", "mean"),
        avg_water_litres=("Daily Water Intake (Litres)", "mean"),
        avg_meal_regularity=("Meal Regularity Score", "mean"),
        avg_outside_food_days=("Outside Food Days Per Week", "mean"),
        avg_monthly_budget_inr=("Monthly Food Budget (INR)", "mean"),
    ).round(2)
    grouped.to_csv(OUT / "hostel_type_comparison.csv")

    findings = [
        "# Descriptive Findings",
        "",
        f"- Total records analysed: {len(df):,}.",
        f"- Average meal regularity score: {df['Meal Regularity Score'].mean():.2f}.",
        f"- Average sleep duration: {df['Sleep Hours Per Day'].mean():.2f} hours/day.",
        f"- Average daily water intake: {df['Daily Water Intake (Litres)'].mean():.2f} litres/day.",
        f"- Average outside-food frequency: {df['Outside Food Days Per Week'].mean():.2f} days/week.",
        f"- Average monthly food budget: INR {df['Monthly Food Budget (INR)'].mean():,.2f}.",
        "",
        f"- Most frequent recorded lifestyle issue: {df['Dominant Lifestyle Issue'].mode().iloc[0]}.",
        "",
        "> These are descriptive values from a synthetic coursework dataset. They are not",
        "> estimates of actual student behaviour and do not support causal or medical claims.",
    ]
    (OUT / "key_findings.md").write_text("\n".join(findings), encoding="utf-8")
    print(f"Analysis outputs saved to {OUT}")

if __name__ == "__main__":
    main()
