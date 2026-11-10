"""Generate static exploratory charts; this is not the interactive dashboard."""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "03_Data_Cleaning" / "Hosteller_Food_and_Lifestyle_Cleaned.csv"
OUT = ROOT / "05_Data_Visualization" / "outputs"

def save_bar(series, title, xlabel, ylabel, filename, rotate=0):
    ax = series.plot(kind="bar", figsize=(9, 5))
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    plt.xticks(rotation=rotate, ha="right" if rotate else "center")
    plt.tight_layout()
    plt.savefig(OUT / filename, dpi=160)
    plt.close()

def main():
    if not INPUT.exists():
        raise FileNotFoundError("Run 03_Data_Cleaning/clean_data.py first.")
    OUT.mkdir(parents=True, exist_ok=True)
    df = pd.read_csv(INPUT)

    save_bar(df["Dominant Lifestyle Issue"].value_counts(),
             "Dominant Lifestyle Issues (Synthetic Dataset)",
             "Issue category", "Number of records",
             "lifestyle_issues.png", 25)

    save_bar(df.groupby("Hostel Type")["Sleep Hours Per Day"].mean(),
             "Average Sleep by Hostel Type",
             "Hostel type", "Average sleep (hours/day)",
             "average_sleep_by_hostel.png", 20)

    save_bar(df[["Breakfast Days Per Week", "Lunch Days Per Week",
                 "Dinner Days Per Week"]].mean(),
             "Average Meal Frequency",
             "Meal", "Average days per week",
             "average_meal_frequency.png")

    plt.figure(figsize=(7, 5))
    plt.scatter(df["Sleep Hours Per Day"],
                df["Physical Activity (Hours Per Week)"], alpha=0.45)
    plt.title("Sleep Duration vs Physical Activity")
    plt.xlabel("Sleep (hours/day)")
    plt.ylabel("Physical activity (hours/week)")
    plt.tight_layout()
    plt.savefig(OUT / "sleep_vs_activity.png", dpi=160)
    plt.close()
    print(f"Charts saved to {OUT}")

if __name__ == "__main__":
    main()
