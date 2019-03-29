import random

##############################################################
## Generates a random list of a given length
##
## Parameters: num - the length of the generated list
##
## Returns: a uniformly distributed list of length num and 
##          1-norm 1
##############################################################

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

##############################################################
## Finds the index of the maximum value of a list
## 
## Parameters: aList - the list to find the maximum of
##             n - the length of the list
##
## Returns: the index of the maximum value of aList
##############################################################

def findMaxIndex(aList,n):
    ind = 0
    for i in range(1,n):
        if aList[i] > aList[ind]:
            ind = i
    return ind

##############################################################
## Generate a list of given length whose elements are all 
## equal
## 
## Parameters: n - the length of the list
##             num - the value with which every element should
##                   be equal
##
## Returns: a list of length n whose elements are all equal
##############################################################

def createUniformList(n,num):
    aList = []
    for i in range(n):
        aList.append(num)
    return aList

##############################################################
## Given a discrete distribution on the numbers 0 through n
## for some n, generate a random number
##
## Parameters: aList - the discrete distribution
##
## Returns: the randomly generated number
##############################################################

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

    ##########################################################
    ## Instantiates a Person object with a randomly generated
    ## internal distribution and no searches, all with a given
    ## number of ads
    ##
    ## Parameters: num - the dimension of the vectors to be
    ##                   instantiated
    ##
    ## Returns: None
    ##########################################################
    
    def __init__(self,num):
        self.probsActual = tuple(generateRandList(num))
        self.probsEmpirical = createUniformList(num,1/float(num))
        self.countEmpirical = createUniformList(num,0)
        self.n = num
        self.maxIndexActual = findMaxIndex(self.probsActual,num)

    ##########################################################
    ## Given that the person is presented a particular ad, 
    ## determines if the person clicks the ad. This is decided 
    ## according to the person's internal distribution
    ##
    ## Parameters: ad - an integer denoting the ad presented
    ##                  to the user
    ##
    ## Returns: 1 if the person clicks the ad, 0 if not
    ##########################################################
    
    def clickAd(self,ad):
        num = random.random()
        if num < self.probsActual[ad]:
            return 1
        else:
            return 0

    ##########################################################
    ## Generate a random search (according to the person's 
    ## internal distribution) and update all the necessary 
    ## attributes accordingly
    ##########################################################

    def randomSearch(self):
        searched = pickWeighted(self.probsActual)
        self.updateProbs(searched)

    ##########################################################
    ## Update the necessary attributes given an ad that is 
    ## searched. These attributes are:
    ##   probsEmpirical
    ##   countEmpirical
    ##   totalSearches
    ##   maxIndexEmpirical
    ##
    ## Parameters: searched - the ad that was searched
    ##
    ## Returns: None
    ##########################################################

    def updateProbs(self,searched):
        self.countEmpirical[searched] = self.countEmpirical[searched] + 1
        self.totalSearches = self.totalSearches + 1
        for i in range(self.n):
            self.probsEmpirical[i] = self.countEmpirical[i]/float(self.totalSearches)
        if self.countEmpirical[searched] > self.countEmpirical[self.maxIndexEmpirical]:
            self.maxIndexEmpirical = searched
    
    ##########################################################
    ## Find the radius of the confidence interval of this 
    ## person
    ##########################################################

    def confidence(self):
        return 1/float(self.totalSearches)**0.1
    
    ##########################################################
    ## Get all the attributes. Probably not necessary because
    ## attributes aren't private, but there for completeness
    ##########################################################
    
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
        
    ##########################################################
    ## Print the probabilities (nicely formatted)
    ##########################################################

    def printProbs(self):
        for i in range(self.n):
            print "Probability ", i , ": ", self.probsActual[i]

    ##########################################################
    ## Print all the attributes of the person
    ##########################################################
    
    def printPerson(self):
        print self.probsActual
        print self.probsEmpirical
        print self.countEmpirical
        print self.totalSearches
        print ""
