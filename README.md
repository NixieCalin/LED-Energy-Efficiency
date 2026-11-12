
# LED vs Incandescent Energy Efficiency Analysis

## Project Overview
This project presents a software-based comparison of LED and incandescent bulbs using existing datasets. It analyzes lighting efficiency, power consumption, annual energy usage, electricity costs, and estimated carbon emissions.

## Objectives
- Compare the average brightness of LED and incandescent bulbs.
- Analyze power consumption and luminous efficacy.
- Estimate annual electricity consumption and cost.
- Compare estimated annual CO₂ emissions.
- Present the results through an interactive Streamlit dashboard.

## Technologies Used
- Python
- Pandas and NumPy
- Matplotlib and Seaborn
- Jupyter Notebook
- Streamlit

## Project Structure
```text
LED-Energy-Efficiency/
├── app.py
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
│   └── data_analysis.ipynb
├── outputs/
└── README.md
```

## Methodology
1. Collected existing LED and incandescent bulb datasets.
2. Inspected and validated the datasets.
3. Cleaned the selected dataset and recalculated derived metrics.
4. Compared average values for both bulb types.
5. Generated visualizations and summary results.
6. Developed an interactive Streamlit dashboard.

## Key Results

| Metric | Incandescent | LED |
|---|---:|---:|
| Average brightness | 986.60 lm | 995.79 lm |
| Average power | 70.56 W | 11.12 W |
| Luminous efficacy | 14.02 lm/W | 89.63 lm/W |
| Annual energy | 139.91 kWh | 19.70 kWh |
| Annual electricity cost | ₹1,119.31 | ₹157.58 |
| Annual CO₂ emissions | 97.94 kg | 13.79 kg |

**Key observation:** Based on dataset averages, LED bulbs consume approximately 85.92% less annual energy than incandescent bulbs while providing similar average brightness.

*Note: Cost and emissions are estimates based on the assumptions provided in the dataset. This project uses existing data and does not involve physical bulb experiments.*

## How to Run the Project

1. Clone the repository:
   `git clone https://github.com/NixieCalin/LED-Energy-Efficiency.git`

2. Navigate to the project folder:
   `cd LED-Energy-Efficiency`

3. Install the required packages:
   `py -m pip install pandas numpy matplotlib seaborn jupyter streamlit`

4. Run the dashboard:
   `py -m streamlit run app.py`

5. Open the local URL displayed in the terminal.

## Future Scope
- Include additional bulb technologies.
- Add interactive filters for more detailed comparisons.
- Improve visualizations and extend the analysis using larger datasets.

## Author
**Nixie Calin Y**

GitHub: https://github.com/NixieCalin

