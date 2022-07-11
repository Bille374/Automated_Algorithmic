# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 21:40:36 2022

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
    

def max_dd(DF):
    df = DF.copy()    
    df = ohlcv_data["AMZN"].copy()
    df["return"] = df["Adj Close"].pct_change()
    df["cum_roll_max"] =df["cum_return"].cummax()
    df["drawdown"] = df["cum_roll_max"] - df["cum_return"]
    (df["drawdown"]/df["cum_roll_max"]).max()

for ticker in ohlcv_data:
    print("max drawdown of {} = {}".format(ticker,max_dd(ohlcv_data[ticker])))

