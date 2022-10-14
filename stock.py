import yfinance as yf
import streamlit as st

st.write("""
# STOCK PRICING APPLICATION

""")

name = st.text_input('Enter your Stocks TickerSymbol: ', '')
tickerSymbol = name

#getting data on this ticker
tickerData = yf.Ticker(tickerSymbol)

#getting the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')

st.write("""
Showing are the stock **closing price** and ***volume*** 

         
## Closing Price

""")
st.line_chart(tickerDf.Close)
st.write("""
         
## Volume Price

""")

st.line_chart(tickerDf.Volume)
