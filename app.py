import streamlit as st
import pandas as pd
import plotly.express as px
import yfinance as yf

st.title('🧮 S&P 500 Market Trends Dashboard')

@st.cache_data
def load_data():
    df = yf.download('AAPL MSFT TSLA', start='2020-01-01')
    return df.reset_index()

df = load_data()

st.subheader('📈 Live Stock Trends')
fig = px.line(df, x='Date', y='Close', color='Ticker', title='Top Stocks Price Trends')
st.plotly_chart(fig, use_container_width=True)

col1, col2, col3 = st.columns(3)
col1.metric("Avg Close", f"${df['Close'].mean():.2f}")
col2.metric("Total Volume", f"{df['Volume'].sum():,}")
col3.metric("Volatility", f"{df['Close'].std():.2f}")

st.subheader('🎯 Business Insights')
st.info("✅ Upward trend since 2020\n✅ AAPL leads growth\n✅ High volume = strong interest")
