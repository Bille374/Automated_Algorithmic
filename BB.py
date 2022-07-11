# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 15:15:17 2022

@author: 
"""

import yfinance as yf

tickers = ["AMZN", "GOOG","AAPL"]
ohlcv_data = {}

for ticker in tickers:
    temp = yf.download(ticker,period='1mo',interval='5m')
    temp.dropna(how="any",inplace=True)
    ohlcv_data[ticker] = temp
    
  #Calculation  
#Middle Band – 20 Day Simple Moving Average
#Upper Band – 20 Day Simple Moving Average + (Standard Deviation x 2)
#Lower Band – 20 Day Simple Moving Average - (Standard Deviation x 2)
def boll_Band(DF, n=14):
    df = DF.copy()
    df["MB"] = df["Adj Close"].rolling(n).mean()
    df["UB"] = df["MB"] + 2*df["Adj Close"].rolling(n).std(ddof=0)
    df["LB"] = df["MB"] - 2*df["Adj Close"].rolling(n).std(ddof=0)
    df["BB_Width"] = df["UB"] -df["LB"]
    return df[["MB","UB","LB","BB_Width"]]
for ticker in ohlcv_data:
    ohlcv_data[ticker][["MB","UB","LB","BB_Width"]] = boll_Band(ohlcv_data[ticker])
    