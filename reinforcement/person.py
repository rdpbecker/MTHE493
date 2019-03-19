import random

def generateRandList(num):
    theSum = 0
    aList = []
    for i in range(num-1):
        randNum = random.uniform(0,1-theSum)
        aList.append(randNum)
        theSum = theSum + randNum
    aList.append(1-theSum)
    random.shuffle(aList)
    return aList

class Person:
    probs = []
    n = 0

    def __init__(self,num):
        self.probs = generateRandList(num)
        self.n = num

    def printProbs(self):
        for i in range(self.n):
            print "Probability ", i , ": ", self.probs[i]

    def clickAd(self,ad):
        num = random.random()
        if num < self.probs[ad]:
            return 1
        else:
            return 0
