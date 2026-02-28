import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

st.title('🧮 S&P 500 Market Trends Dashboard')

# Sample market data (no external downloads)
np.random.seed(42)
dates = pd.date_range('2020-01-01', periods=1000)
df = pd.DataFrame({
    'Date': dates,
    'AAPL': 100 + np.cumsum(np.random.randn(1000)*0.5),
    'MSFT': 150 + np.cumsum(np.random.randn(1000)*0.3),
    'TSLA': 200 + np.cumsum(np.random.randn(1000)*1.2)
}).melt(id_vars='Date', var_name='Ticker', value_name='Close')

fig = px.line(df, x='Date', y='Close', color='Ticker', title='Stock Trends')
st.plotly_chart(fig, use_container_width=True)

st.metric("Avg AAPL", f"${df[df.Ticker=="AAPL"].Close.mean():.2f}")
