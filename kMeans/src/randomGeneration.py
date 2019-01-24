import random as rand, sys

def randomInteger(num):
    return int(rand.uniform(0,num)) + 1

def group1():
    return (rand.gauss(-80,5),rand.gauss(70,4),rand.gauss(0,5))

def group2():
    return (rand.gauss(-10,5),rand.gauss(-70,4),rand.gauss(60,5))

def group3():
    return (rand.gauss(20,5),rand.gauss(10,4),rand.gauss(40,5))

def group4():
    return (rand.gauss(50,5),rand.gauss(70,4),rand.gauss(-70,5))

def group5():
    return (rand.gauss(-40,5),rand.gauss(-40,4),rand.gauss(-30,5))

def generatePerson(num):
    group = randomInteger(num)
    if group == 1:
        return group1()
    elif group == 2:
        return group2()
    elif group == 3:
        return group3()
    elif group == 4:
        return group4()
    elif group == 5:
        return group5()

print generatePerson(5)
