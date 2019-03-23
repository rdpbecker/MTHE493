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

def createUniformList(n,num):
    aList = []
    for i in range(n):
        aList.append(num)
    return aList

def pickWeighted(aList):
    theSum = 0
    randNum = random.random()
    for i in range(len(aList)):
        if randNum >= theSum and randNum <= theSum + aList[i]:
            return i
        theSum = theSum + aList[i]

class Person:
    probsActual = ()
    probsEmpirical = []
    countEmpirical = []
    totalSearches = 0
    n = 0
    maxIndexActual = -1
    maxIndexEmpirical = 0

    def __init__(self,num):
        self.probsActual = tuple(generateRandList(num))
        self.probsEmpirical = createUniformList(num,1/float(num))
        self.countEmpirical = createUniformList(num,0)
        self.n = num
        self.maxIndexActual = findMaxIndex(self.probsActual,num)
        

    def printProbs(self):
        for i in range(self.n):
            print "Probability ", i , ": ", self.probsActual[i]

    def clickAd(self,ad):
        num = random.random()
        if num < self.probsActual[ad]:
            return 1
        else:
            return 0

    def randomSearch(self):
        searched = pickWeighted(self.probsActual)
        self.updateProbs(searched)

    def updateProbs(self,searched):
        self.countEmpirical[searched] = self.countEmpirical[searched] + 1
        self.totalSearches = self.totalSearches + 1
        for i in range(self.n):
            self.probsEmpirical[i] = self.countEmpirical[i]/float(self.totalSearches)
        if self.countEmpirical[searched] > self.countEmpirical[self.maxIndexEmpirical]:
            self.maxIndexEmpirical = searched
    
    def confidence(self):
        return 1/float(self.totalSearches)**0.1
    
    def getMaxIndexActual(self):
        return self.maxIndexActual

    def getMaxIndexEmpirical(self):
        return self.maxIndexEmpirical

    def getProbsActual(self):
        return self.probsActual

    def getProbsEmpirical(self):
        return self.probsEmpirical

    def getLength(self):
        return self.n

    def getSearches(self):
        return self.totalSearches

    def getCounts(self):
        return self.countEmpirical
        
    def printPerson(self):
        print self.probsActual
        print self.probsEmpirical
        print self.countEmpirical
        print self.totalSearches
        print ""
