# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 18:05:26 2022

@author: eszczepalink
"""

import yfinance as yf
from stocktrends import Renko

tickers = ["AMZN", "GOOG","AAPL"]
ohlcv_data = {}
hour_data = {}
renko_data = {}


for ticker in tickers:
    temp = yf.download(ticker,period='1mo',interval='5m')
    temp.dropna(how="any",inplace=True)
    ohlcv_data[ticker] = temp
    temp = yf.download(ticker,period='1y',interval='1h')
    temp.dropna(how="any",inplace=True)
def ATR(DF, n=14):
    "function to calculate True Range and Average True Range"
    df = DF.copy()
    df["H-L"] = df["High"] - df["Low"]
    df["H-PC"] = abs(df["High"] - df["Adj Close"].shift(1))
    df["L-PC"] = abs(df["Low"] - df["Adj Close"].shift(1))
    df["TR"] = df[["H-L","H-PC","L-PC"]].max(axis=1, skipna=False)
    df["ATR"] = df["TR"].ewm(com=n, min_periods=n).mean()
    return df["ATR"]


def renko_DF(DF, hourly_df):
    df = DF.copy()
    df.drop("Close",axis=1,inplace=True)
    df.reset_index(inplace=True)
    df.columns = ["date","open","high","low","close","volume"]
    df2 = Renko(df)
    df2.brick_size = 3*round(ATR(hourly_df,120).iloc[-1])
    renko_df = df2.get_ohlc_data()
    return renko_df
for ticker in ohlcv_data:
    renko_data[ticker] = renko_DF(ohlcv_data[ticker],hour_data[ticker])

    