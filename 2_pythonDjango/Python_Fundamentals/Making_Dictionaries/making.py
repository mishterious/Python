name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks",
                   "dolphins", "llamas"] 


def make_dict(list1, list2):
    new_dict = {}
    zipped = zip(list1, list2)
    print zipped
    for i in zipped:
        new_dict[i[0]] = i[1].title() 
    print new_dict
    # your code here
#   return new_dict


make_dict(name, favorite_animal)