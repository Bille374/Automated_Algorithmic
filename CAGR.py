# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 19:59:45 2022

@author: 
"""

import yfinance as yf

tickers = ["AMZN","GOOG","MSFT"]
ohlcv_data = {}
for ticker in tickers:
    temp = yf.download(ticker,period='7mo',interval='1d')
    temp.dropna(how="any",inplace=True)
    ohlcv_data[ticker] = temp
    
def CAGR(DF):
    df = DF.copy()
    df =df.copy()
    
    df["return"] = df["Adj Close"].pct_change()
    df["cum_return"] = (1+df["return"]).cumprod()
    n=len(df)/252
    CAGR = (df["cum_return"][-1])**(1/n) - 1
    return CAGR

for ticker in ohlcv_data:
    print("CAGR for {} = {}".format(ticker,CAGR(ohlcv_data[ticker])))