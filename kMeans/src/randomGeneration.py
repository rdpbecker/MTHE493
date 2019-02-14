import random as rand, sys, allio
mostRandom = 1
ps = []

def randomInit(randomness,clusters):
    global mostRandom
    mostRandom = randomness
    if not randomness:
        choosePs(clusters)

def meanInit(num):
    if mostRandom:
        means = []
        for i in range(num):
            means.append(randomFunc())
    else:
        means = [group1(),group2(),group3(),group4(),group5()]
    return means

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

def checkRandomness():
    print mostRandom

def randomInteger(num):
    return int(rand.uniform(0,num)) + 1

def randomSelector():
    num = rand.uniform(0,1)
    for i in range(len(ps)-1):
        if num >= ps[i] and num < ps[i+1]:
            return i+1
    return len(ps)-1

def rearrange(arr):
    newarr = [arr.pop(randomInteger(3)-1)]
    newarr.append(arr.pop(randomInteger(2)-1))
    newarr.append(arr.pop(0))
    return newarr

def randomFunc():
    coord1 = rand.uniform(0,1)
    coord2 = rand.uniform(0,1-coord1)
    coord3 = 1-coord1-coord2
    arr = [coord1,coord2,coord3]
    rand.shuffle(arr)
    return tuple(arr)

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

def generatePerson(num):
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
