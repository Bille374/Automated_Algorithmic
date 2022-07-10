# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 10:47:55 2022

@author: 
"""

import datetime as dt
import yfinance as yf
import pandas as pd

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

cl_price.plot(subplots=True, layout=(3,3), 
              title="Stock Prices daily_return",grid=True)

daily_return.plot(subplots=True, layout=(3,3))

(1 + daily_return).cumprod().plot(subplots=True,layout=(3,3), 
              title="Stock Prices portfolio_return",grid=True)
(1 + daily_return).cumsum()