
# def rangeNumber(start, stop):
#     for i in range(start, stop):
#         if i % 2 == 0: 
#             print "Number is {} This is an even number." .format(i)
#         else: 
#             print "Number is {} This is an odd number." .format(i)


# rangeNumber(0, 2001)


a = [2, 4, 3, 1]


def multiples(list, val):
    for x in range(len(list)):
        list[x] = list[x] * 3
    return list
    print multiples(list)
    print "Nonehere either"


def layered_multiples(arr):
    new_Array = []
    for y in arr:
        last_Array = []
        for z in range(y):
            last_Array.append(1)
        new_Array.append(last_Array)
    print new_Array

x = layered_multiples(multiples([2,4,2],4))
print x
