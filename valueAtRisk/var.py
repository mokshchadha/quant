import numpy as np
import yfinance as yf
from scipy.stats import norm
import pandas as pd
import datetime

def download_data(stock, start_date, end_date):
    ticker = yf.download(stock, start=start_date, end=end_date)
    return ticker[['Close']].rename(columns={'Close': stock})

def calculate_var(position, c , mu, sigma): # this is var for tomorrow
    alpha_val = norm.ppf(1-c)
    var = position * (mu - sigma *alpha_val)
    return var

def calculate_future_var(position, c, mu , sigma, n): # this for var for n days in future
    alpha_val = norm.ppf(1-c)
    var = position * (mu - sigma * np.sqrt(n) *alpha_val)
    return var


if __name__ == '__main__':
    start = datetime.datetime(2014, 1, 1)
    end = datetime.datetime(2018, 1, 1)
    ril = 'RELIANCE.NS'
    stockdata = download_data(ril, start, end)
    log_daily_returns = np.log(stockdata[ril] / stockdata[ril].shift(1))
    log_daily_returns = log_daily_returns[1:] # because first will be NaN
    stockdata['returns'] = log_daily_returns
    S = 1e6  # this is the start value of the investment 
    c = 0.95 #confidence level this time it is 95%

    # we assume the daily returns are normally distributed
    mu = np.mean(stockdata['returns'])
    sigma = np.std(stockdata['returns'])

    print("python value at risk", calculate_var(S, c, mu, sigma))
    print("value at risk after 10 days", calculate_future_var(S, c, mu, sigma, 10))
