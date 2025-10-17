from alpha_vantage.timeseries import TimeSeries
import pandas as pd
import time

import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("ALPHA_VANTAGE_KEY")

ts = TimeSeries(api_key, 'pandas')
data = ts.get_daily(symbol="EURUSD", outputsize='full')[0]
data.columns = ['open', 'close', 'high', 'low', 'volume']

all_tickers = ["AAPL", "MSFT", "CSCO", "AMZN", "FB", "GOOG"]
close_prices = pd.DataFrame()

for ticker in all_tickers:
    data = ts.get_intraday(symbol=ticker, interval="1min", outputsize="full")[0]
    data.columns = ['open', 'close', 'high', 'low', 'volume']
    close_prices[ticker] = data['close']



print(close_prices)


