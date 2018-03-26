
class Bike(object):
    def __init__(self, price, max_speed, miles):
        self.price = price
        self.max_speed = max_speed
        self.miles = miles

    def displayInfo(self):
        print myBike.price
        print myBike.max_speed
        print myBike.miles
        return self

    def ride(self):
        self.miles += 10
        print self.miles
        return self

    def reverse(self):
        self.miles -= 5
        print self.miles
        return self


myBike = Bike("$80000", 220, 899)

myBike.displayInfo().ride().ride().reverse()