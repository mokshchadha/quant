import numpy as np

class OptionPricing:

    def __init__(self, S0, E, T, rf, sigma, iterations):
        self.S0 = S0
        self.E = E
        self.T = T
        self.rf = rf
        self.sigma = sigma
        self.iterations = iterations

    def call_option_simulation(self):
        #we have 2 columsn : first with 0s and second will store the payoff 
        # we need the first column of 0s : because the payoff function is max(0, S-E) for call option
        option_data = np.zeros([self.iterations, 2])

        # dimension: 1 dimensional array with as many items as the iterations
        rand = np.random.normal(0, 1, [1, self.iterations])
        stock_price = self.S0 * np.exp(self.T * (self.rf - 0.5 * self.sigma ** 2) + self.sigma * np.sqrt(self.T) * rand)

        # we need S-E because we have to calculate the max(S-E, 0)
        option_data[:, 1] = stock_price - self.E

        # average for the monte carlo method
        # max() return the max(0, S-E) according to the formulae
        average = np.sum(np.amax(option_data, axis=1)) / float(self.iterations)
        return np.exp(-1.0 * self.rf * self.T) * average
    
    def put_option_simulation(self):
        #we have 2 columsn : first with 0s and second will store the payoff 
        # we need the first column of 0s : because the payoff function is max(0, S-E) for call option
        option_data = np.zeros([self.iterations, 2])

        # dimension: 1 dimensional array with as many items as the iterations
        rand = np.random.normal(0, 1, [1, self.iterations])
        stock_price = self.S0 * np.exp(self.T * (self.rf - 0.5 * self.sigma ** 2) + self.sigma * np.sqrt(self.T) * rand)

        # we need S-E because we have to calculate the max(S-E, 0)
        option_data[:, 1] = self.E - stock_price

        # average for the monte carlo method
        # max() return the max(0, S-E) according to the formulae
        average = np.sum(np.amax(option_data, axis=1)) / float(self.iterations)
        return np.exp(-1.0 * self.rf * self.T) * average





if __name__ == "__main__":
    model = OptionPricing(100, 100, 1, 0.05, 0.2, 10000)
    cp = model.call_option_simulation()
    pp = model.put_option_simulation()
    print("Call price ", cp)
    print("Put price ", pp)
