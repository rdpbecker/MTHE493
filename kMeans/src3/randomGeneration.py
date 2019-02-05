import random as rand, sys
mostRandom = 1

def randomInit(randomness):
    global mostRandom 
    mostRandom = randomness

def meanInit(num):
    if mostRandom:
        means = []
        for i in range(num):
            means.append(randomFunc())
    else:
        means = [group1(),group2(),group3(),group4(),group5()]
    return means

def checkRandomness():
    print(mostRandom)

def randomInteger(num):
    return int(rand.uniform(0,num)) + 1

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
    newarr = rearrange(arr)
    return (newarr[0],newarr[1],newarr[2])

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
    group = randomInteger(num)
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
