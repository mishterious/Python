class Animal(object):
    def __init__(self, name, health):
        # super()
        self.name = name
        self.health = health

    def work(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self

    def displayHealth(self):
        print self.health 
        return self


class Dog(Animal):
    def runningDog(self):
        self.health = 150
        return self

    def pet(self):
        self.health += 5
        print self.health
        return self


class Dragon(Animal):
    def flyDragon(self):
        print self.health


allAnimals = Animal("Lion", 90)
allAnimals.work().work().work().run().run().displayHealth()


# newAnimal = Dog("Toby", 150)
# print " {} {}".format(newAnimal.name, newAnimal.health)

# newAnimal.work().work().work().pet().run().run().displayHealth()

newDragon = Dragon("Smaug", 150)
print newDragon.health

newAnimal = Animal("Turkey", 9)
print newAnimal.flyDragon()