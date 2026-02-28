import streamlit as st
import pandas as pd
import plotly.express as px
df = pd.read_csv('sp500.csv')
df['date'] = pd.to_datetime(df['date'])
st.title('S&P 500 Dashboard')
fig = px.line(df[df['symbol']=='AAPL'], x='date', y='close', title='AAPL Trend')
st.plotly_chart(fig)
st.metric("Avg Close", f"${df['close'].mean():.2f}")
