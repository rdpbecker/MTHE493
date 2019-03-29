import random as rand, sys, allio
mostRandom = 1
ps = []

##############################################################
## Initialize the module
##
## Parameters: randomness - a flag described in the helpstring
##             clusters - the number of clusters which will be 
##                        used
##
## Returns: None
##############################################################

def randomInit(randomness,clusters):
    global mostRandom
    mostRandom = randomness
    if not randomness:
        choosePs(clusters)

##############################################################
## Randomly initialize means for the clustering algorithm
##
## Parameters: num - the number of required clusters
##
## Returns: the means in a list
##############################################################

def meanInit(num):
    if mostRandom:
        means = []
        for i in range(num):
            means.append(randomFunc())
    else:
        means = [group1(),group2(),group3(),group4(),group5()]
    return means

##############################################################
## Choose the probability distribution for the pre-clustered
## data
##
## Parameters: num - the number of clusters
##
## Returns: None
##############################################################

def choosePs(num):
    theSum = 0
    global ps
    ps = []
    for i in range(num):
        p = rand.uniform(0,1-theSum)
        theSum = theSum + p
        ps.append(theSum)
    ps.append(1)
    print ps

##############################################################
## Chooses a random integer from 1 to num
##
## Parameters: num - the upper bound on the range to choose 
##                   from
## 
## Returns: a random integer between 1 and num
##############################################################

def randomInteger(num):
    return int(rand.uniform(0,num)) + 1

##############################################################
## Randomly chooses a number according to the global 
## distribution
##
## Returns: a randomly selected tag
##############################################################

def randomSelector():
    num = rand.uniform(0,1)
    for i in range(len(ps)-1):
        if num >= ps[i] and num < ps[i+1]:
            return i+1
    return len(ps)-1

##############################################################
## Randomly generates a vector on the 3-d simplex
##
## Returns: the 3-d vector as a tuple
##############################################################

def randomFunc():
    aList = [0]
    newList = []
    for i in range(2):
        num = random.uniform(0,1)
        aList.append(num)
    aList.append(1)
    aList.sort()
    for i in range(n):
        newList.append(aList[i+1]-aList[i])
    return tuple(newList)

##############################################################
## Randomly generate people in specific groups
##
## Returns: a randomly generated 3-component vector
##############################################################

def group1():
    return (rand.gauss(-10,5),rand.gauss(30,4),rand.gauss(0,5))

def group2():
    return (rand.gauss(-10,5),rand.gauss(-30,4),rand.gauss(25,5))

def group3():
    return (rand.gauss(20,5),rand.gauss(10,4),rand.gauss(20,5))

def group4():
    return (rand.gauss(10,5),rand.gauss(40,4),rand.gauss(-25,5))

def group5():
    return (rand.gauss(-30,5),rand.gauss(-10,4),rand.gauss(-5,5))

##############################################################
## Randomly chooses a group from which to generate a point and
## then generates a point in that group
##
## Returns: a randomly generated 3-d vector, along with a tag
##          for the group it was generated from
##############################################################

def generatePerson():
    if mostRandom:
        return randomFunc(), 1
    group = randomSelector()
    if group == 1:
        return group1(), group
    elif group == 2:
        return group2(), group
    elif group == 3:
        return group3(), group
    elif group == 4:
        return group4(), group
    elif group == 5:
        return group5(), group
