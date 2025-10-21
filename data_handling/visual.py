import datetime as dt
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

stocks = ["AMZN", "FB" ,"GOOG","MSFT"]
start = dt.datetime.today() - dt.timedelta(365 * 10)
end = dt.datetime.today()

cl_price = pd.DataFrame()
ohlcv_data = {}

for ticker in stocks:
    cl_price[ticker] = yf.download(ticker, start, end, multi_level_index=False)['Close']

daily_returns = cl_price.pct_change()

# daily_returns.plot(subplots=True, layout=(2,2))
cumprod = (1 + daily_returns).cumprod() # cum product lets you visually how things will look compounded
# cumprod.plot()
# plt.show()

# matplotlib basics
fig , axis = plt.subplots() # figure is the canvas and axis is everything inside that canvas

axis.set(title="mean daily returns of the stock ", xlabel="stock", ylabel="mean daily return")
plt.bar(x = daily_returns.columns, height = daily_returns.mean())
plt.show()