# Cookie Cats A/B Test Analysis

## Business Problem
Cookie Cats is a mobile puzzle game that uses gates to force players 
to wait before continuing. This project analyzes whether placing the 
gate at level 30 vs level 40 better retains players after 7 days.

## Dataset
- 90,189 players from a randomized A/B test
- Features: version (gate_30/gate_40), sum_gamerounds, 
  retention_1, retention_7
- Source: Kaggle — Cookie Cats Dataset

## Methodology
- **mITT Filtering** — removed 5,000 players who never played 
  a single round as the gate could not influence their behavior
- **Z-test for proportions** — tested statistical significance 
  of retention difference
- **Confidence Intervals** — estimated range of true difference
- **Bayesian Analysis** — calculated probability gate_30 is 
  genuinely better using Beta distribution
- **Business Impact** — translated retention difference into 
  annual revenue impact

## Key Findings
| Metric | Gate 30 | Gate 40 |
|--------|---------|---------|
| 7-day retention | 19.84% | 19.03% |
| 1-day retention | 46.8% | 45.9% |

- Z-test p-value: 0.0026 (statistically significant)
- 95% CI: (0.284%, 1.341%) — entirely above zero
- Bayesian probability gate_30 is better: 99.86%
- Annual revenue at risk if switching to gate_40: ₹2.6L — ₹12.2L

## Recommendation
Keep the gate at level 30. Both frequentist and Bayesian analysis 
confirm gate_30 retains more players, and this difference is 
unlikely to be due to random chance.

## Project Structure
├── cookie_cats.csv          # Raw dataset

├── explore.ipynb            # Full analysis notebook

├── app.py                   # Streamlit interactive app

└── README.md

## How to Run
```bash
# Install dependencies
pip install pandas numpy scipy statsmodels matplotlib seaborn streamlit plotly

# Run the Streamlit app
streamlit run app.py
```

## Tools Used
Python, Pandas, NumPy, SciPy, Statsmodels, Matplotlib, 
Seaborn, Plotly, Streamlit
