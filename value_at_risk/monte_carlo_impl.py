import numpy as np
import yfinance as yf
import pandas as pd
import datetime

def download_data(stock, start, end):
    ticker = yf.download(stock, start, end)
    return ticker['Close'] 

class ValueAtRiskMonteCarlo:
    def __init__(self, S, mu, sigma, c, n , iterations):
        self.S = S
        self.mu = mu
        self.sigma = sigma
        self.c = c
        self.n = n
        self.iterations = iterations # simply the number of stocks we will simulate
    
    def simulate(self):
        rand = np.random.normal(0, 1, [1, self.iterations])
        # equation for the S(t)
        #the random walk of the intial investment
        stock_price = self.S * np.exp(self.n * (self.mu - 0.05 * self.sigma ** 2) + self.sigma * np.sqrt(self.n) * rand)

        # to determine the stock percentile we have to sort them 
        stock_price = np.sort(stock_price)

        # it depends on confidence level 95%->5 percentile and 99% -> 1 percentile
        percentile = np.percentile(stock_price, (1 - self.c)* 100)
        return self.S - percentile 





if __name__ == '__main__':
    
    S = 1e6
    n = 1
    c = 0.95
    iterations = 100_000

    tcs = 'TCS.BO'
    start = datetime.datetime(2020, 1, 1)
    end = datetime.datetime(2025, 1, 1)
    data = download_data(tcs, start, end)

    tcs_returns = data[tcs].pct_change().dropna()  # drop NaN values

    # Extract scalar values using .iloc[0] or .values[0] or just use the Series methods
    mu = tcs_returns.mean()  # This returns a scalar
    sigma = tcs_returns.std()  # This returns a scalar

    print(f"Mean return (μ) ", mu)
    print(f"Standard deviation",sigma)

    model = ValueAtRiskMonteCarlo(S, mu, sigma, c, n, iterations)
    monte = model.simulate()
    print(f"Value at Risk with Monte Carlo:", monte)