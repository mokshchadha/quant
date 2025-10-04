import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

RISK_FREE_RATE = 0.05
MONTHS_IN_A_YEAR = 12


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
    
    def regression(self):
        # using linear regression to fit a line to the data
        # [stock_returns, maket_return] - slope is the beta
        beta, alpha = np.polyfit(self.data['m_returns'], self.data['s_returns'], deg=1) # deg = 1 is linear functin deg = 2 is quadratic function
        print("beta from regression", beta)
        expected_returns = RISK_FREE_RATE + beta * (self.data['m_returns'].mean() * MONTHS_IN_A_YEAR - RISK_FREE_RATE)
        print("Expected return ", expected_returns)
        self.plot_regression(alpha, beta)

    def plot_regression(self, alpha, beta):
        fig, axis = plt.subplots(1, figsize=(20,10))
        axis.scatter(self.data['m_returns'], self.data["s_returns"], label="data points")
        axis.plot(self.data["m_returns"], beta * self.data["m_returns"] + alpha, color="red", label="CAPM Line")
        plt.title("Capital asset pricing model, finding alpha and beta")
        plt.xlabel("Market return $R_m$", fontsize=18)
        plt.ylabel("Stock return $R_a$")
        plt.text(0.08, 0.05, r'$R_a = \beta * R_m + \alpha$' , fontsize=18)
        plt.legend()
        plt.grid(True)
        plt.show()




if __name__ == '__main__':
    # ibm and the s&P 500
    capm = CAPM(['IBM', '^GSPC'], '2010-01-01', '2017-01-01')
    capm.initialise()
    capm.calculate_beta()
    capm.regression()





