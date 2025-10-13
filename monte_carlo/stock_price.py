import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

NUM_OF_SIMULATIONS = 100

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
    plt.plot(simulation_data)
    plt.show()
    return simulation_data

if __name__ == "__main__":
    print(stock_monte_carlo(50, 0.0002, 0.01))