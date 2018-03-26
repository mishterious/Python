def say_hi():
    return "Hi"
    greeting = say_hi() #the returned value from say_hi function gets assigned to the 'greeting' variable
    print greeting 


def add(a, b):
    x = a + b
    print x
    return x


sum1 = add(4,6)
sum2 = add(1,4)
sum3 = sum1 + sum2

print sum3

def multiply(arr,num):
    for x in arr:
        x *= num
    return arr
    a = [2,4,10,16]
    b = multiply(a,5)
    print b
# output:

def multiply(arr,num):
    print arr, num # output should be [2,4,10,16] 5
    for x in arr:
        print x
        x *= num
        print arr
    return arr

a = [2,4,10,16]
b = multiply(a,5)
print b

dog[0] = "X"
dog = dog + ("domestic",)
#result is...
#("Canis Familiaris", "Dog", "carnivore", 12, "domestic")
dog = dog[:3] + ("man's best friend",) + dog[4:]