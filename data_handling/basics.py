import datetime as dt
import yfinance as yf
import pandas as pd

stocks = ["AMZN", "MSFT", "FB", "GOOG"]

start = dt.datetime.today() - dt.timedelta(365)
end = dt.datetime.today()

cl_price = pd.DataFrame()
ohlcv_data = {}

for ticker in stocks:
    cl_price[ticker] = yf.download(ticker, start, end, multi_level_index=False)['Close']

print(cl_price)

#filled_na = cl_price.fillna({"FB":0, "GOOG":-1}) # better to do .fillna(0) -- this will make all na values 0 or u can also pass a method
#filled_na_method = cl_price.fillna(method='bfill', axis=1) # back fill with the last available value defaul axis=0 value fills columns else u can refer row also
dropped_na = cl_price.dropna(axis=0, how='any') # deletes the row if na exists in any field - here axis is 0 and how=any (drop if any field is nan | all (drops only if all fields are nan)

print(dropped_na)

### basics of statistics
mean = cl_price.mean()
std = cl_price.std()
print(mean, std)
print(cl_price.describe())

### any quantitivate analysis relies on the return of the assests and not the price of the asset
daily_return = cl_price.pct_change()
print(daily_return) # simply calculating the percentage change
print(daily_return.mean())
print(daily_return.std()) #volatily of daily returns

# rolling 
daily_return.rolling(window=10).mean() # by rolling you can create a overlapping window , it is not chunking becaue chunks dont overlap
daily_return.rolling(window=10).std() # u can use ops like mean, sum, std for analysis