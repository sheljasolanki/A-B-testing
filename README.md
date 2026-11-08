# Gate 30 vs Gate 40: Mobile Game A/B Test

**Live site:** https://sheljasolanki.github.io/A-B-testing/ · **Full analysis:** [Testing.ipynb](Testing.ipynb)

## Business Problem
In the mobile puzzle game *Cookie Cats*, gates force players to wait (or pay) before they can continue. New players were randomly given the first gate at **level 30** (control) or **level 40** (treatment). This project tests which placement keeps more players coming back **7 days after install**.

## Dataset
- 90,189 players from a randomized A/B test
- Columns: `version` (gate_30 / gate_40), `sum_gamerounds` (rounds played in the first 14 days), `retention_1`, `retention_7`
- Source: [Mobile Games A/B Testing (Kaggle)](https://www.kaggle.com/datasets/yufengsui/mobile-games-ab-testing)

## Methodology
1. **Data quality checks:** duplicates, missing values, and a 49,854-round logging outlier
2. **Sample ratio mismatch (SRM) check:** chi-square test of the 50/50 split
3. **Modified intention-to-treat (mITT):** removed 3,994 players with 0 rounds, after checking that both groups lose a similar share (p = 0.17)
4. **Survivor-bias check:** showed why filtering to "players who reached their gate" is invalid (it filters on a post-treatment variable)
5. **Two-proportion z-test** and **95% confidence intervals** for day-1 and day-7 retention
6. **Power analysis:** power for the observed effect and the minimum detectable effect
7. **Bayesian Beta-Binomial model:** probability that gate 30 is truly better
8. **Gameplay analysis:** share of players who played at least *k* rounds in each version
9. **Business impact:** retention gap × daily installs × value per retained player, as a range from the CI

## Key Findings
| Metric | Gate 30 | Gate 40 | Difference | Result |
|---|---|---|---|---|
| 7-day retention | 19.84% | 19.03% | +0.81 pp (+4.3% relative) | **significant**, p = 0.0026 |
| 1-day retention | 46.75% | 46.22% | +0.54 pp | not significant, p = 0.11 |

- 95% CI for the 7-day difference: **+0.28 pp to +1.34 pp**, entirely above zero
- Test power for the observed 7-day effect: ~85% (MDE ≈ 0.76 pp)
- Bayesian probability that gate 30 has the higher 7-day retention: **≈ 99.9%**
- Rounds played are nearly identical between versions (about 32% of players in both pass round 40). The gate changes whether players *return*, not visibly how much they play.
- Illustrative impact (50,000 installs/day, ₹5 per retained player): switching to gate 40 would cost about **₹2.6 – 12.2 lakh per year**

## Recommendation
**Keep the gate at level 30.** The effect is small, but frequentist and Bayesian analyses agree, and the experiment had enough power to detect it.

## Limitations
- **Sample ratio mismatch:** the split is 49.6% / 50.4% (p = 0.0086). The cause should be investigated before acting.
- Revenue figures are illustrative. Real install volume and player LTV are needed.
- Only day-1 and day-7 retention are available. Long-term retention, purchases and novelty effects are not measured.
- `sum_gamerounds` counts rounds (including replays), not levels reached

## Project Structure
```
├── index.html        # Interactive one-page results site (no dependencies)
├── Testing.ipynb     # Full analysis notebook
├── cookie_cats.csv   # Raw dataset
├── requirements.txt  # Python dependencies for the notebook
└── README.md
```

## How to Run
```bash
# Notebook
pip install -r requirements.txt
jupyter notebook Testing.ipynb

# Website: just open index.html in a browser (or see the live link above)
```

## Tools Used
Python, pandas, NumPy, SciPy, statsmodels, Matplotlib, seaborn, plus HTML/CSS/JavaScript for the interactive site.
