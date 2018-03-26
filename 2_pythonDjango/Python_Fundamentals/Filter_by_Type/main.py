
def filterType(parameter):
    if type(parameter) is int:
        if parameter >= 100:
            print "That's a big number!"
        elif parameter < 100:
            print "That's a small number"
    if type(parameter) is str:
        if len(parameter) >= 50:
            print "Long sentence."
        elif len(parameter) < 50:
            print "Short sentence."
    if type(parameter) is list:
        if len(parameter) >= 5:
            print "Big list!" 
        elif len(parameter) < 5:
            print "Short List"


filterType(19983983)
filterType(10)
filterType("We're here to code here in Coding Dojo!!!!")
filterType("Let's make it happen!")
filterType([1, 36, 6, 3, 3, 576, 546, 4, 3, 65, 7])
filterType(["Hello", "This", "Works"])