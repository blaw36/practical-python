class Stock:
    def __init__(self, name, shares, price):
        self.name=name
        self.shares=shares
        self.price=price
    
    def cost(self):
        return round(self.shares*self.price,2)
    
    def sell(self, units):
        self.shares -= units
