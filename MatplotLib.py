# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 11:21:41 2022

@author: 
"""
import datetime as dt
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

stocks = ["AMZN","FB","GOOG","MSFT","IMOEX.ME","DAX"]

start = dt.datetime.today()-dt.timedelta(4650)
end = dt.datetime.today()
cl_price = pd.DataFrame()
ohlcv_data = {}
# looping over tickers 
for ticker in stocks:
    cl_price[ticker] = yf.download(ticker,start,end)["Adj Close"]
    
    
cl_price.dropna(axis=0, how='any',inplace=True)
daily_return = cl_price.pct_change()

fig, ax = plt.subplots()
ax.set(title="Mean return on tech stocks", xlabel="Tech Stocks", ylabel = "Mean Returns")
plt.bar(x=daily_return.columns, height=daily_return.mean())
fig, ax = plt.subplots()
ax.set(title="Std return on tech stocks", xlabel="Tech Stocks", ylabel = "Std Returns")
plt.bar(x=daily_return.columns, height=daily_return.std())