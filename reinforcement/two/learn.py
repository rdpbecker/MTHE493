import random, sys
sys.path.append("../../People")
from two import person as p

##############################################################
## Print a dictionary
##
## Parameters: aDict - the dictionary to print
##             header - the header to printed at the start of 
##                      the dictionary
##             elemHeader - a header to print before each 
##                          element
##
## Returns: None
##############################################################

def printDict(aDict,header,elemHeader):
    print header
    for i in range(len(aDict.keys())):
        print elemHeader, " ", i, ": ", aDict[i]
    print ""

##############################################################
## Chooses a random integer between 0 and n-1
##############################################################

def randInt(n):
    randNum = random.uniform(0,n)
    for i in range(n):
        if randNum >= i and randNum <= (i+1):
            return i

##############################################################
## Finds the index of the maximum element in an array
##
## Parameters: percents - the array to find the maximum of
##             n - the length of percents
##
## Returns: the index of the maximum element in percents
##############################################################

def maxIndex(percents,n):
    maxIndex = 0
    for i in range(1,n):
        if percents[i] > percents[maxIndex]:
            maxIndex = i
    return maxIndex 

##############################################################
## Learns the best ad to present a person using a stochastic
## policy
##
## Parameters: person - the person whose best ad we should 
##                      learn
##             decay - the decay rate of the policy
##
## Returns: None
##############################################################

def learn(person,decay):
    clicks = {}
    ads = {}
    percents = {}
    for i in range(person.n):
        clicks[i] = 2
        ads[i] = 4.0
        percents[i] = 0.5
    for i in range(1000):
        randNum = random.random()
        print "Iteration ", i+1
        print "Random number: ", randNum
        print "Decay percent: ", decay**(i+1)
        if randNum < decay**(i+1):
            ad = randInt(person.n)
        else:
            ad = maxIndex(percents,person.n)
        print "Ad picked: ", ad
        ads[ad] = ads[ad] + 1
        if person.clickAd(ad):
            clicks[ad] = clicks[ad] + 1
        percents[ad] = clicks[ad]/ads[ad]
    printDict(ads,"Number of times each ad is selected", "Ad selected")
    printDict(percents,"Percents","Percent for ad")

##############################################################
## Generates a person and learns the best ad to give them
##############################################################

def main():
    person = p.Person(3)
    learn(person,0.98)
    person.printProbs()

##############################################################
## Runs the script
##############################################################

if __name__ == "__main__":
    main()
