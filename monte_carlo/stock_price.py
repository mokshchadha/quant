import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

NUM_OF_SIMULATIONS = 1000

def stock_monte_carlo(S0, mu, sigma, N=1000):
    result = []
    for _ in range(NUM_OF_SIMULATIONS):
        prices = [S0] #starting with s0
        for _ in range(N):
            # since we are going to simulate it day by day we can take t = 1
            stock_price = prices[-1] * np.exp((mu - 0.5 * sigma ** 2) + sigma * np.random.normal()) 
            prices.append(stock_price)
        result.append(prices)
    simulation_data = pd.DataFrame(result)
    simulation_data = simulation_data.T # the given columns will contain the time seriesfor a given simulation hence the transpose
    simulation_data["mean"] = simulation_data.mean(axis=1) # according to monte carlo the mean of simulations is the future price of the stock
    plt.plot(simulation_data["mean"])
    plt.show()
    print("Prediction of future stock price : ", simulation_data["mean"].tail(1))
    return simulation_data

if __name__ == "__main__":
    stock_monte_carlo(50, 0.0002, 0.01)