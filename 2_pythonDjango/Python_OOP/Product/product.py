class product(object):
    reason = ""

    def __init__(self, name, price, weight, brand, status):
        self.name = name
        self.price = price
        self.weight = weight
        self.brand = brand
        self.status = status

    def sell(self):
        self.status = "sold"
        print self.status
        return self
    
    def addTax(self):
        self.price = self.price + self.price/10
        self.tax = self.price/10
        print self.tax
        return self

    def returnNow(self, reason):
        if reason == "broken":
            self.price = 0
            self.reason = "defective"
            print self.reason
            return self
        elif reason == "open":
            self.reason = "used"
            print self.price
            self.price *= 0.8
            print self.price
            return self
        elif reason == "new":
            self.status = "For Sale!"
            return self

    def displayInfo(self):
        print myProduct.name
        print myProduct.price
        print myProduct.weight
        print myProduct.brand
        print myProduct.status
        print myProduct.tax
        return self


myProduct = product("MacBook Pro", 2100, "5 lbs", "Apple", "for sale")
myProduct.sell().addTax().returnNow("open").displayInfo()