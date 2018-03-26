class MathDojo(object):
    def __init__(self):
        self.number = 0
        self.result = []

    def add(self, *over):
        print self.number
        for i in over:
            if isinstance(i, list) or isinstance(i, float): 
                # self.result.append[i]
                print i
                self.number += sum(i)
            elif isinstance(i, int) or isinstance(i, tuple):
                print i
                self.number += i
            else: 
                print i
                return self
        return self

    def subtract(self, *over):
        for i in over:
            if isinstance(i, list) or isinstance(i, float):
                self.number += sum(i)
                print i
            elif isinstance(i, list) or isinstance(i, tuple):
                self.number += i
                print i
        return self 


md = MathDojo()
# md.add(4, 3).add(2, 14)
# print md.number

md.add([1], 3, 4).add([3, 5, 7, 8], [2, 4.3, 1.25]).subtract(2, [2, 3], [1.1, 2.3]).result
