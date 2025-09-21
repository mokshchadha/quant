class ZeroCouponBonds:
    def __init__(self, principal, maturity, market_interest_rate):
        self.principal = principal
        self.maturity_years = maturity
        #market related interest rate
        self.market_interest_rate = market_interest_rate/100

    def present_value_bond(self, amount_to_return, n):
        return amount_to_return / (1 + self.market_interest_rate) ** n


    

def main():
    zb = ZeroCouponBonds(1000, 2, 4)
    print(zb.present_value_bond(1000, 2))

main()