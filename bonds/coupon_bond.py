from math import exp as exponential

class CouponBond:
    def __init__(self, principal_amount, bond_annual_rate ,maturity_years, market_rate_of_interest):
        self.principal_amount = principal_amount
        self.market_rate_of_interest = market_rate_of_interest /100
        self.maturity_years = maturity_years
        self.bond_annual_rate = bond_annual_rate / 100

    def present_value_discrete(self, x, n):
        return x / (1 + self.market_rate_of_interest) ** n

    def present_value_continuous(self, x , n):
        return x * exponential( -self.market_rate_of_interest * n)
    
    def calculate_price_discrete(self):
        coupon_amount = 0
        for t in range(1, self.maturity_years + 1 ):
            coupon_yearly_topup = self.principal_amount * self.bond_annual_rate
            coupon_amount = coupon_amount + self.present_value_discrete(coupon_yearly_topup, t)
        
        maturity_year_amount = self.principal_amount / (1 + self.market_rate_of_interest) ** self.maturity_years
        return coupon_amount + maturity_year_amount
    
    def calculate_price_continuous(self):
        coupon_amount =0
        for t in range(1, self.maturity_years +1):
            coupon_yearly_topup = self.principal_amount * self.bond_annual_rate
            coupon_amount = coupon_amount + self.present_value_continuous(coupon_yearly_topup, t)

        # without yield of maturity this is not possible???

    


bond = CouponBond(1000, 10, 3 , 4)
print(bond.calculate_price_discrete())
