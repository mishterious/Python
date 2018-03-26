

words = "It's thanksgiving day. It's my birthday,too!"

print words.find('day')

words = words.replace("day", "month", 18)
print words

x = [2,54,-2,7,12,98]
print min(x)
print max(x)

y = ["hello",2,54,-2,7,12,98,"world"]


new_list = "My name is {} {}".format(y[0], y[7])
print new_list

x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
B = x[:len(x)/2]
C = x[len(x)/2:]
print x
print B
print C

B.insert(0, C)
print B
# empty_list = []

# split_result = x.split()
# for temp in split_result:
#     print temp




