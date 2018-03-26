# Strings
# https://docs.python.org/2.6/library/string.html#string.find
# find
str = "bob, is a funky clown in Montana"
print str.find("Montana")
# capitalize
# upper
# lower

str_c = str.capitalize()
str = str.upper()
str_l = str.lower()
str_t = str.title()
print str
print str_t
print str_c
print str_l

# count
sentence = 'Mary had a little lamb'
print sentence.count("a")
print str_l.count("bob")
print str.count(" ")

# index   returns 13
print sentence.index("t")

# split
split_result = sentence.split()
for temp in split_result:
    print temp

# join
sentence_join = " "
print sentence_join.join(split_result)

# replace
sentence_rp = sentence.replace("little", "tasty", 1)
print sentence_rp

# format
print("Sammy has {} balloons.".format("red"))

# Lists
# https://www.tutorialspoint.com/python/python_lists.htm
# len
# max
# min
x = [2, 54, -2, 7, 12, 98]
print min(x)
print max(x)
print len(x)

# index
print x.index(12)

# append
x.append(112)
print x

# pop
print x.pop()

# remove
x.remove(54)
print x

# insert
x.insert(3, "here")
print x

# sort
x.sort()
print x

# reverse
x.reverse()
print x

# (optional) extend
y = [2, 66, 88, 1, 4, 245, "bob"]
x.extend(y)
print x

# (optional) list
gator = []
gator = list(y)
print gator 

