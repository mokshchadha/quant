from scipy import stats
from numpy import log,exp,sqrt

def call_option_price(S, E, T, rf, sigma):
    #first we have to calculate the d1 and d2 parameters
    d1 = (log(S/E) + (rf+sigma*sigma/2.0) * T) / (sigma * sqrt(T))
    d2 = d1 - sigma * sqrt(T)
    print("the d1 and d2 params are ", d1, d2)
    # for returning the call option
    return S * stats.norm.cdf(d1) - E * exp(-rf * T) * stats.norm.cdf(d2) # this is the price if u want to do call option

def put_option_price(S, E, T, rf, sigma):
    # first we have to calculate d1 and d2 parameters
    d1 = (log(S/E) + (rf + sigma * sigma/2.0) * T) / (sigma * sqrt(T))
    d2 = d1 - sigma * sqrt(T)
    print("the d1 and d2 params are ", d1, d2)
    return -S * stats.norm.cdf(-d1) + E * exp(-rf * T) * stats.norm.cdf(d2)


if __name__ == "__main__":
    S0=100 # underlying stock price at t =0
    E=100 # strike price 
    T = 1 # expiry in a year = 365 days
    rf = 0.05 # risk free rate
    sigma = 0.2 # volatility of the underlyting stock 

    cp = call_option_price(S0, E, T, rf, sigma)
    pp = put_option_price(S0, E, T, rf, sigma)

    print("Call price", cp)
    print("Put Price",pp)
