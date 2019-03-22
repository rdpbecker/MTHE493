import person as p, random, integrate as inte 
from timeit import default_timer as timer

def giveRandom(people,iters,adsList):
    successes = 0
    for i in range(iters):
        for j in range(len(people)):
            successes = successes + people[j].clickAd(random.choice(adsList))
    return float(successes)/len(people)/iters            

def giveTargetted(people,iters):
    successes = 0
    intTime = 0
    adTime = 0
    start = timer()
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

def oneIter(n,num,searches,adsGiven):
    adsList = range(n)
    people = []
    for i in range(num):
        people.append(p.Person(n))
        for j in range(searches):
            people[i].randomSearch()
#       print "Generated person ", i
#       people[i].printPerson()
    randPct = giveRandom(people,adsGiven,adsList)
    targetPct = giveTargetted(people,adsGiven)
    print "With random ads: ", randPct
    print "With targetted ads: ", targetPct 
    return randPct, targetPct

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

def testUpdating():
    person = p.Person(3)
    person2 = p.Person(3)
    for i in range(5):
        person.randomSearch()
        person2.randomSearch()
    person.printPerson()
    person2.printPerson()

if __name__ == "__main__":
    import sys
    args = sys.argv[1:]
    main(int(args[0]),int(args[1]),int(args[2]),int(args[3]),int(args[4]))
#   testUpdating()
