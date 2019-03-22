import person as p, random, integrate as inte 

def giveRandom(people,iters,adsList):
    successes = 0
    for i in range(iters):
        for j in range(len(people)):
            successes = successes + people[j].clickAd(random.choice(adsList))
    return float(successes)/len(people)/iters            

def giveTargetted(people,iters):
    successes = 0
    for i in range(iters):
        for j in range(len(people)):
            print people[j].getProbsEmpirical()
            probs = inte.findProbs(people[j].getProbsEmpirical(),people[j].confidence())
            maxIndex = people[j].getMaxIndexActual()
            successes = successes + people[j].clickAd(maxIndex)
    return float(successes)/len(people)/iters

def oneIter(n,num,searches,adsGiven):
    adsList = range(n)
    people = []
    for i in range(num):
        people.append(p.Person(n))
        for j in range(searches):
            people[i].randomSearch()
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

if __name__ == "__main__":
    import sys
    args = sys.argv[1:]
    main(int(args[0]),int(args[1]),int(args[2]),int(args[3]),int(args[4]))
