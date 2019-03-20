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

def findMaxIndex(aList,n):
    ind = 0
    for i in range(1,n):
        if aList[i] > aList[ind]:
            ind = i
    return ind

class Person:
    probs = []
    n = 0
    maxIndex = -1

    def __init__(self,num):
        self.probs = generateRandList(num)
        self.n = num
        self.maxIndex = findMaxIndex(self.probs,num)

    def printProbs(self):
        for i in range(self.n):
            print "Probability ", i , ": ", self.probs[i]

    def clickAd(self,ad):
        num = random.random()
        if num < self.probs[ad]:
            return 1
        else:
            return 0

    def getMaxIndex(self):
        return self.maxIndex
