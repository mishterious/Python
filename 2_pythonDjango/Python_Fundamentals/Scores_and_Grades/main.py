import random

def newScores():
    for i in range(10): 
        random_num = random.randint(60, 100)
        if random_num >= 60 and random_num <= 69:
            print "Score: {}; Your grade is D".format(random_num)
        elif random_num >= 70 and random_num <= 79:
            print "Score: {}; Your grade is C".format(random_num)
        elif random_num >= 80 and random_num <= 89:
            print "Score: {}; Your grade is B".format(random_num)
        elif random_num >= 90 and random_num <= 100:
            print "Score: {}; Your grade is A".format(random_num)
        else:
            print "Score: {}; Your grade is ".format(random_num)

newScores()