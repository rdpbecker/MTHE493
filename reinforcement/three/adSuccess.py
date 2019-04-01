import random, sys#, person as p, integrate as inte 
sys.path.append("../../People")
sys.path.append("../../confidence")
from timeit import default_timer as timer
from two import person as p
from twoc import integrate as inte

##############################################################
## Gives a group of people a number of ads from a list, 
## chosen randomly
## 
## Parameters: people - the group of people, as a list
##             iters - the number of ads to give each person
##             adsList - the list of ads to give
##
## Returns: the percent of ads which were clicked
##############################################################

def giveRandom(people,iters,adsList):
    successes = 0
    for i in range(iters):
        for j in range(len(people)):
            successes = successes + people[j].clickAd(random.choice(adsList))
    return float(successes)/len(people)/iters            

##############################################################
## Gives a group of people a number of ads from a list, 
## targetted towards the people 
## 
## Parameters: people - the group of people, as a list
##             iters - the number of ads to give each person
##
## Returns: the percent of ads which were clicked
##############################################################

def giveTargetted(people,iters):
    successes = 0
    intTime = 0
    adTime = 0
    for i in range(len(people)):
#       start = timer()
        probs = inte.findProbs(people[i].getProbsEmpirical(),people[i].confidence(),0)
#       mid = timer()
        for j in range(iters):
#           intTime = intTime + mid - start
            maxIndex = people[i].getMaxIndexActual()
            successes = successes + people[i].clickAd(maxIndex)
#       end = timer()
#       adTime = adTime + end - mid
        if i and not i%100:
            print "Done person ", i, " targetted"
#       print "Integration time: ", intTime
#       print "Ad distribution time: ", adTime
#       print "% integration time: ", intTime/(intTime+adTime)
#       print ""
    return float(successes)/len(people)/iters

##############################################################
## Randomly generate a given number of people to be presented
## a certain number of ads, then generate search histories for
## each of them and determine what proportion of ads are 
## clicked by each person if they are given
##
## 1. Randomly selected ads
## 2. Targetted ads
##
## Parameters: n - the number of ads in the pool
##             num - the number of people to generate
##             searches - the number of searches to generate
##                        for each person
##             adsGiven - the number of ads to present each 
##                        person
##
## Returns: the percent of ads clicked by random selection and
##          by targetted selection
##############################################################

def oneIter(n,num,searches,adsGiven):
    adsList = range(n)
    people = []
    for i in range(num):
        people.append(p.Person(n))
        for j in range(searches):
            people[i].randomSearch()
        print "Generated person ", i
        people[i].printPerson()
    randPct = giveRandom(people,adsGiven,adsList)
    targetPct = giveTargetted(people,adsGiven)
    print "With random ads: ", randPct
    print "With targetted ads: ", targetPct 
    return randPct, targetPct

##############################################################
## Generate some groups of people and present ads to them to
## determine the approximate improvement of giving targetted
## ads over random ads
##
## Parameters: dim, people, searches, adsGiven - see oneIter()
##             peopleSets - the number of groups of people to 
##                          generate
##
## Returns: None
##############################################################

def main(dim,people,searches,adsGiven,peopleSets):
    randSum = 0
    targetSum = 0
    for i in range(peopleSets):
        print "Iteration: ", i
        rand, target = oneIter(dim,people,searches,adsGiven)
        randSum = rand + randSum
        targetSum = target + targetSum
        print ""
    print "With random ads: ", randSum/peopleSets
    print "With targetted ads: ", targetSum/peopleSets

##############################################################
## Actually run the script
##############################################################

if __name__ == "__main__":
    import sys
    args = sys.argv[1:]
    main(int(args[0]),int(args[1]),int(args[2]),int(args[3]),int(args[4]))
#   testUpdating()
