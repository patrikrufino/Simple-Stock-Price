# IMPORTS
import yfinance as yf
import streamlit as st
import pandas as pd

tickerSymbol = 'MSFT'

st.write("""
# SIMPLE STOCK PRICE APP

Shown are the stock closing **price**, **max price** and **volume** of **MICROSOFT**

""")


tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period="max")

st.write("""
### Closing Price
""")
st.line_chart(tickerDf.Close)

st.write("""
### Volume Price
""")
st.line_chart(tickerDf.Volume)

st.write("""
### Max Price
""")
st.line_chart(tickerDf.High)
