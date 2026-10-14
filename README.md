# nonprofit_impact_analytics
Data analytics pipeline, cohort analysis, and Tableau dashboard measuring workforce &amp; housing outcomes for non-profit programs.


# Nonprofit Impact & Cohort Analytics

## Overview
This project presents an end-to-end data analytics pipeline and interactive BI dashboard evaluating participant outcomes, housing stability, and resource hub utilization across different non-profit program delivery modalities (Virtual vs. In-Person Launchpad).

## Interactive Dashboard
🔗 **[View Live Tableau Public Dashboard](https://public.tableau.com/your-actual-dashboard-link)**

## Key Features
- **Synthetic Data Generation:** Engineered a realistic, anonymized dataset of 500 participant profiles using Python (`faker`, `pandas`, `numpy`).
- **Cohort Analysis:** Evaluated completion, employment, and housing stability rates between virtual and in-person cohorts.
- **Data Visualization:** Built interactive Tableau Public charts with dynamic filter actions for stakeholder reporting.

## Project Structure
- `generate_data.py`: Script generating synthetic demographic and program data.
- `impact_analysis.py`: Aggregations and summary statistics.
- `synthetic_impact_data.csv`: Output dataset.

## How to Run
```bash
pip install pandas numpy faker
python generate_data.py
python impact_analysis.py

---

### Step 3: Push Everything to GitHub

#### Method A: Using PyCharm UI (Easiest)
1. In PyCharm's top menu bar, click **Git** $\rightarrow$ **Commit...** (or press `Cmd + K` on Mac / `Ctrl + K` on Windows).
2. In the left panel, check the boxes next to all your files (`generate_data.py`, `impact_analysis.py`, `synthetic_impact_data.csv`, `README.md`).
3. In the **Commit Message** box, type: `"Add full project scripts, synthetic data, and documentation"`.
4. Click the **Commit and Push...** button at the bottom.
5. In the pop-up window, click **Push**.

#### Method B: Using PyCharm Terminal
If you prefer terminal commands, open the **Terminal** tab at the bottom of PyCharm and run:

```bash
git add .
git commit -m "Add full project scripts, synthetic data, and documentation"
git push origin main