import numpy as np
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import scipy.optimize as optimization

# For NSE stocks, add ".NS" suffix to symbol
# For BSE stocks, add ".BO" suffix to symbol

# stocks we are going to handle
stocks = ['RELIANCE.NS', 'TCS.BO', 'INFY.NS', 'ICICIBANK.NS', 'SBIN.NS', 'PNB.NS'] #the data will be INR


# historical data - define start and end dates (using past dates with actual trading data)
start_date = '2021-01-01'
end_date = '2025-01-01'
NUM_TRADING_DAYS = 4* 252 # trading days are the days on which u can trade
NUM_PORTFOLIOS = 10_000

def download_data():
    stock_dataframes = []
    stock_names = []
    
    for stock in stocks:
        data = yf.download(stock, start=start_date, end=end_date, auto_adjust=True)
        stock_dataframes.append(data['Close']) 
        stock_names.append(stock) 
                
    df = pd.concat(stock_dataframes, axis=1, keys=stock_names)
    df = df.dropna(how='all')
    
    return df

def show_data(data):
    data.plot(figsize=(10,6))
    plt.show()

def calculate_return(data):
    # data 1 2 3 4 5
    #.       1 2 3 5 
    # hence we arrive at s(t+1) / s(t) -- gross return of a price
    log_return = np.log(data/ data.shift(1)) #log return --> normalisatoin
    return log_return[1:] # because 1 row has nothing to be subratcted from 

def show_statistics(returns):
    print(returns.mean() * NUM_TRADING_DAYS)
    print(returns.cov() * NUM_TRADING_DAYS)

def show_mean_variance(returns, weights):
    weights = np.array(weights)
    # we are after the annual returns and not daily
    portfolio_return = np.sum(returns.mean() * weights) * NUM_TRADING_DAYS # -- imp formulae
    transpose_weights = weights.T
    portfolio_volatily_square =  np.dot(transpose_weights, np.dot(returns.cov() * NUM_TRADING_DAYS, weights)) # wt . E w -- imp formula
    portfolio_volatily = np.sqrt(portfolio_volatily_square)

    print("expected returns : ", portfolio_return)
    print("expected volatitly :", portfolio_volatily)

def generate_portfolios(returns):
    portfolio_means = []
    portfolio_risks = []
    portfolio_weights = []
    
    rng = np.random.default_rng(42)

    for _ in range(NUM_PORTFOLIOS):
        w = rng.random(len(stocks))
        w = w / np.sum(w)
        portfolio_weights.append(w)
        portfolio_means.append(np.sum(returns.mean() * w) * NUM_TRADING_DAYS)
        portfolio_risks.append(np.sqrt(np.dot(w.T, np.dot(returns.cov() * NUM_TRADING_DAYS, w))))

    return np.array(portfolio_weights), np.array(portfolio_means), np.array(portfolio_risks)

def show_portfolios(returns, volatilities):
    fig, ax = plt.subplots(figsize=(10, 5), layout='constrained')
    scatter = ax.scatter(volatilities, returns, c=returns/volatilities, marker='o', cmap='viridis') #c is the color ration and marker is how a point is represneted
    ax.grid(True)
    ax.set_xlabel('Volatalities')
    ax.set_ylabel('Returns')
    fig.colorbar(scatter, ax=ax, label='Sharpe Ratio')
    plt.show()  # This was missing!

def statistics(weights, returns):
    portfolio_return = np.sum(returns.mean() * weights) * NUM_TRADING_DAYS
    portfolio_risk = np.sqrt(np.dot(weights.T, np.dot(returns.cov()* NUM_TRADING_DAYS, weights))) # squre root of dot product of weight tranpose with (dot product of covarians and weights)
    sharpe_ratio = portfolio_return/portfolio_risk
    return np.array([portfolio_return, portfolio_risk, sharpe_ratio])

#optimisation - scipy optimize can find the minimum of a function
# the maximum of a f(x) is the minum of -f(x)
def min_function_sharpe(weights, returns):
    return -1 * statistics(weights, returns)[2]

def constraints1(weights):
    #what is the constraint in markowitz -- the sum of weights should be 1
    # sum of w = 1 ie. sum of w -1 = fx =0 is the function to be minimized
    return np.sum(weights) - 1

def optimize_portfolio(weights, returns):
    constraints = {'type':'eq', 'fun': constraints1}
    bound = (0.0, 1.0) # the weight can be from 0 to 1 and there are 
    bounds = tuple(bound for _ in range(len(stocks)))
    intialWeights = weights[0]
    return optimization.minimize(fun=min_function_sharpe, x0=intialWeights, args=returns, method='SLSQP', bounds=bounds, constraints=[constraints])


def print_optimal_porfolio(optimum, returns):
    print("Optimal portfolio", optimum['x'].round(3))
    print("Expected return , volatily and sharpe ratio", statistics(optimum['x'].round(3), returns))

def main():
    stock_data = download_data()
    # show_data(stock_data)
    returns = calculate_return(stock_data)
    show_statistics(returns)
    weights, means, risks = generate_portfolios(returns)
    # show_portfolios(means, risks)
    optimum = optimize_portfolio(weights, returns)
    print_optimal_porfolio(optimum, returns)


if __name__ == "__main__":
    main()