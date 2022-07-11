# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 20:32:24 2022

@author: 
    
"""
import yfinance as yf
import numpy as np

tickers = ["AMZN","GOOG","MSFT"]
ohlcv_data = {}
for ticker in tickers:
    temp = yf.download(ticker,period='7mo',interval='1d')
    temp.dropna(how="any",inplace=True)
    ohlcv_data[ticker] = temp
def volatitity(DF):
    df = DF.copy()
    
    df["return"] = df["Adj Close"].pct_change()
    vol = df["return"].std() *np.sqrt(252)
    return vol
for ticker in ohlcv_data:
    print("Volatility for {} = {}".format(ticker,(ohlcv_data[ticker])))