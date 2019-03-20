import person as p, random

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
            maxIndex = people[j].getMaxIndex()
            successes = successes + people[j].clickAd(maxIndex)
    return float(successes)/len(people)/iters

def main(n,num,iters):
    adsList = range(n)
    people = []
    for i in range(num):
        people.append(p.Person(n))
    print "With random ads: ", giveRandom(people,iters,adsList)
    print "With targetted ads: ", giveTargetted(people,iters)

main(3,100,5)
