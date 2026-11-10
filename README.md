# Food and Lifestyle of Hostellers

A student Data Analytics and Visualization (DAV) project exploring food habits and lifestyle patterns among college hostellers.

## Dataset
The current coursework dataset contains **1,500 synthetic records** and 16 fields. It is explicitly labelled synthetic in the source CSV. It must not be presented as a real survey or as verified measurements from SR University students.

Topics include:
- Hostel type and department
- Meal regularity and weekly breakfast, lunch and dinner frequency
- Daily water intake and sleep duration
- Physical activity and outside-food frequency
- Monthly food budget and dominant lifestyle issue

## Repository workflow
1. Review the dataset and its data dictionary in `02_Data_Collection/`.
2. Run the validation/cleaning script in `03_Data_Cleaning/`.
3. Run the exploratory analysis in `04_Data_Analysis/`.
4. Generate static exploratory charts using `05_Data_Visualization/`.
5. Build and maintain the team's dashboard independently in `06_Dashboard/`.

> **Dashboard ownership:** The dashboard is intentionally not implemented in this repository. The student team will create it separately and add its files or link in `06_Dashboard/README.md`.

## Project structure
```
01_Project_Proposal/
02_Data_Collection/
03_Data_Cleaning/
04_Data_Analysis/
05_Data_Visualization/
06_Dashboard/
requirements.txt
```

## Setup
Python 3.10 or newer is recommended.

```bash
python -m venv .venv
# Windows PowerShell
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Run scripts from the repository root:

```bash
python 03_Data_Cleaning/clean_data.py
python 04_Data_Analysis/analyze_data.py
python 05_Data_Visualization/create_charts.py
```

## Data integrity and limitations
- The provided dataset's `Data Status` field identifies every row as synthetic coursework data.
- Synthetic values are suitable for demonstrating a reproducible analytics workflow, not for making claims about the actual health or behaviour of a student population.
- No causal or medical conclusions should be drawn from these records.
- If the team later collects genuine survey responses, retain the original file separately, document consent and anonymisation, and update this README and the data dictionary accordingly.

## Team contributions
Add team member names and roles here before submission.
