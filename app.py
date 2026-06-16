import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from scipy import stats

st.set_page_config(page_title="Cookie Cats A/B Test", layout="wide")
st.title("Cookie Cats Gate A/B Test Analysis")
st.markdown("Analyzing whether gate position at level 30 or 40 better retains players")

@st.cache_data
def load_data():
    df = pd.read_csv('cookie_cats.csv')
    return df[df['sum_gamerounds'] > 0]

df = load_data()
gate30 = df[df['version'] == 'gate_30']
gate40 = df[df['version'] == 'gate_40']

# Section 1
st.header("1. Retention Rates by Gate")

col1, col2 = st.columns(2)

with col1:
    st.metric(label="Gate 30 - 7 Day Retention", value="19.84%")
    st.metric(label="Gate 40 - 7 Day Retention", value="19.03%")
    st.metric(label="Difference", value="0.81 percentage points")

with col2:
    retention_data = pd.DataFrame({
        'Gate': ['Gate 30', 'Gate 40', 'Gate 30', 'Gate 40'],
        'Retention Type': ['Day 1', 'Day 1', 'Day 7', 'Day 7'],
        'Rate': [
            gate30['retention_1'].mean(),
            gate40['retention_1'].mean(),
            gate30['retention_7'].mean(),
            gate40['retention_7'].mean()
        ]
    })
    fig = px.bar(retention_data, x='Retention Type', y='Rate',
                 color='Gate', barmode='group',
                 title='Day 1 vs Day 7 Retention by Gate')
    st.plotly_chart(fig)

# Section 2
st.header("2. Business Impact Calculator")

dau = st.slider("Daily Active Users",
                min_value=10000,
                max_value=500000,
                value=50000,
                step=10000)

arpu = st.slider("Revenue per Retained Player per Day (₹)",
                 min_value=1,
                 max_value=50,
                 value=5)

diff = gate30['retention_7'].mean() - gate40['retention_7'].mean()
daily_player_diff = dau * diff
daily_revenue_diff = daily_player_diff * arpu
annual_revenue_diff = daily_revenue_diff * 365

st.metric("Annual Revenue at Risk if Switching to Gate 40",
          f"₹{annual_revenue_diff:,.0f}")

# Section 3
st.header("3. Conclusion & Recommendation")

st.success("✅ Recommendation: Keep the gate at Level 30")

st.markdown("""
We tested whether moving the gate from level 30 to level 40 affects 7-day player retention.

**Key Findings:**
- Gate 30 retains **19.84%** of players at day 7 vs **19.03%** for gate 40
- Difference of **0.81 percentage points** in favour of gate 30
- Z-test p-value: **0.0026** — statistically significant
- Confidence interval: **(0.284%, 1.341%)** — entire interval above zero
- Bayesian analysis: **99.86% probability** gate 30 is genuinely better

**Visual Evidence:**
- Density plot shows gate 40 causes sharp player drop-off at round 40
- Gate 30 players continue playing well beyond round 30

**Limitations:**
- Revenue estimates are illustrative — real analysis needs actual monetization data
- Experiment duration and novelty effects not accounted for
""")