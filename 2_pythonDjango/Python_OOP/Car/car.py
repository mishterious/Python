class car(object):
    def __init__(self, name, price, speed, fuel, mileage):
        self.name = name
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage

    def taxChance(self):
        if self.price > 10000:
            self.tax = 0.15
            print self.tax
        else:
            self.tax = 0.12
            print self.tax
        return self

    def fuelUse(self):
        if self.fuel == "Full":
            self.fuel = "Less than full"
            print self.fuel
            return self
        elif self.fuel == "Half Full":
            self.fuel = "Almost Empty"
            print self.fuel
            return self


myCar = car('BMW', 55000, "90mpg", "Almost over", "70mpg")
print myCar.fuel
myCar.taxChance().fuelUse()

myCar = car('Ferrari', 270000, "90mpg", "Half Full", "12mpg")
myCar.taxChance().fuelUse()

myCar = car('Volvo', 2700, "90mpg", "Full", "25mpg")
myCar.taxChance().fuelUse()