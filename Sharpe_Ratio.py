# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 20:59:44 2022

@author: 
"""

import yfinance as yf
import numpy as np
import pandas as pd

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


def volatitity(DF):
    df = DF.copy()
    
    df["return"] = df["Adj Close"].pct_change()
    vol = df["return"].std() *np.sqrt(252)
    return vol

def sharp(DF, rf):
    df = ohlcv_data["AMZN"].copy()
    return (CAGR(df) - rf)/volatitity(df)


def sortino(DF, fr):
    df = DF.copy()
    df["return"] = df["Adj Close"].pct_change()
    df["return"] = df["Adj Close"].pct_change()
    neg_return = np.where(df["return"]>0,0,df["return"])
    neg_vol = pd.Series(neg_return[neg_return!=0]).std()
    return (CAGR(df) - rf)/neg_vol

for ticker in ohlcv_data:
    print("Shape for {} = {}".format(ticker,sharp(ohlcv_data[ticker],0.03)))
    print("Sortino for {} = {}".format(ticker,sharp(ohlcv_data[ticker],0.03)))









