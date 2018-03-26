
lola = ['magical unicorns', 19, 'hello', 98382, 'world']
newList = []
sum = 0

for i in lola:
    if isinstance(i, int) or isinstance(i, float):
        sum += i
    else: 
        newList.append(i)

print sum, newList

if sum > 0 and len(newList) == 0:
    print "Integer only"
elif sum == 0 and len(newList) > 0: 
    print "String only"
else: 
    print "Mixed"