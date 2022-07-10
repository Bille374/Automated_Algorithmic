# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 10:18:06 2022

@author: 
"""

import datetime as dt
import yfinance as yf
import pandas as pd

stocks = ["AMZN","3988.HK","FB","GOOG","MSFT"]

start = dt.datetime.today()-dt.timedelta(4650)
end = dt.datetime.today()
cl_price = pd.DataFrame()
ohlcv_data = {}
# looping over tickers 
for ticker in stocks:
    cl_price[ticker] = yf.download(ticker,start,end)["Adj Close"]
    
    
cl_price.dropna(axis=0, how='any',inplace=True)

cl_price.mean()
cl_price.std()
cl_price.median()
cl_price.describe()
cl_price.head(10)
cl_price.tail(6)



daily_return = cl_price.pct_change()
daily_return.mean(axis=1,skipna=True)
daily_return.std()

df = daily_return.rolling(window=10, min_periods=10).mean()
daily_return.rolling(window=10).std()
df = daily_return.rolling(window=10).max()
daily_return.rolling(window=10).sum()


df2 = daily_return.ewm(com=10, min_periods=10).mean()







