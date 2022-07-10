# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 08:35:25 2022

@author: 
"""

import datetime as dt
import yfinance as yf
import pandas as pd

stocks = ["AMZN","3988.HK","FB","GOOG","MSFT"]
#stocks = ["FTSE", "DAX","IMOEX.ME"]
start = dt.datetime.today()-dt.timedelta(4650)
end = dt.datetime.today()
cl_price = pd.DataFrame()
ohlcv_data = {}

for ticker in stocks:
    cl_price[ticker] = yf.download(ticker,start,end)["Adj Close"]
# filling Nan value
#scalar
cl_price.fillna(method='bfill',axis=0,inplace=True)
# dict{}
#cl_price.fillna({"FB":0,"GOOG":1})

# dropping NaN values
cl_price.dropna(axis=0,how='all')