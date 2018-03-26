print "Hello World"

name = [32,4,6]
print "My name is", name


name = "[32,4,5,6]"
print "My name is " + name

first_name = "Zen"
last_name = "Coder"
print "My name is {} {}".format(first_name, last_name)

hw = "hello %s" % 'world'
print hw
# the output would be:
# hello world

x = "Hello World"
print x.upper()
# output:
"HELLO WORLD"


fruits = ['apple', 'banana', 'orange', 'strawberry']
vegetables = ['lettuce','cumcumber', 'carrots']

fruits_and_vegetables = fruits + vegetables
print fruits_and_vegetables
salad = 3 * vegetables
print salad 


x = [99,4,2,5,-3]
print x[:]
#the output would be [99,4,2,5,-3]
print x[1:]
#the output would be [4,2,5,-3];
print x[:4]
#the output would be [99,4,2,5]
print x[2:4]
#the output would be [2,5];