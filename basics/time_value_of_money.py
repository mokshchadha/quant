from math import exp as exponential

def future_discrete_value(amount, rate, no_of_years):
    rate_by_hundred = rate / 100
    return amount * (1+rate_by_hundred) ** no_of_years

def future_continuous_value(amount, rate, no_of_years):
    rate_by_hundred = rate / 100
    return amount * (exponential(rate_by_hundred * no_of_years))

def main():
    principle = 100
    rate = 5
    years = 3
    x = future_continuous_value(principle, rate, years)
    print(x)

main()