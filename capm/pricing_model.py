import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

class CAPM:
    def __init__(self, stocks, start_date, end_date):
        self.stocks = stocks
        self.start_date = start_date
        self.end_date = end_date
        self.data = None

    def download_data(self):
        # Download all stocks at once - more efficient and avoids alignment issues
        data = yf.download(self.stocks, self.start_date, self.end_date, auto_adjust=True)
        return data['Close']
    
    def initialise(self):
        stock_data = self.download_data()
        # we use monthly data instead of daily data
        # daily returs are superior for short term analysis 
        # capm is a long term so it is better to analyse monthly returns -- the main benefit is that with montly data returs are at least appx normally distributed
        stock_data = stock_data.resample('ME').last()
        ibm_stock = self.stocks[0]
        market = self.stocks[1]
        self.data = pd.DataFrame({'s_adjclose': stock_data[ibm_stock], 'm_adjclose':stock_data[market]})
        
        #logarithmic monthly returns
        self.data[['s_returns', 'm_returns']] = np.log(self.data[['s_adjclose', 'm_adjclose']]/ self.data[['s_adjclose', 'm_adjclose']].shift(1)) #short hand syntax
        self.data = self.data[1:]
        return self.data
    
    def calculate_beta(self):
        # covariance matrix : the daigonal items are the variances 
        # off diagonals are covariances
        # the matrix is symmertrice : = cov[0, 1] == cov[1,0] --- 
        covarince_matrix = np.cov(self.data['s_returns'], self.data['m_returns'])
        beta = covarince_matrix[0,1] / covarince_matrix[1,1]
        print("beta is ", beta)
        return beta

if __name__ == '__main__':
    # ibm and the s&P 500
    capm = CAPM(['IBM', '^GSPC'], '2010-01-01', '2017-01-01')
    capm.initialise()
    capm.calculate_beta()





