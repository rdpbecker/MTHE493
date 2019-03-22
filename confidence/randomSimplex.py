import random, matplotlib.pyplot as plt, helpers, plotting
from mpl_toolkits.mplot3d import Axes3D

def pdf(num,radius):
    return num**0.5*radius 

def simplexPoint(n,radius):
    aList = []
    theSum = 0
    for i in range(n-1):
        num = random.uniform(0,radius-theSum)
        aList.append(num)
        theSum = theSum + num
    aList.append(radius-theSum)
    random.shuffle(aList)
    return aList

def shuffleSum(point,positives,negatives):
    theSum = sum(point)
    count = 1
#   print point
#   print "The sum is: ", theSum
    while abs(theSum) > 0.001:
#       print "Iteration: ", count
        posIndex = random.choice(positives)
        negIndex = random.choice(negatives)
#       print "The sum is: ", theSum
#       print "Positive Point: ", point[posIndex]
#       print "Negative Point: ", point[negIndex]
        if theSum > 0:
            sign = 1
            m = min([point[negIndex]+1,point[posIndex]])
        else:
            sign = -1
            m = min([-1*point[negIndex],1-point[posIndex]])
#       print "m is: ", m
        final = min([abs(theSum),m])
#       print "The final radius is: ", final
        if abs(theSum)<0.1 and final == abs(theSum):
            point[negIndex] = point[negIndex] - theSum/2
            point[posIndex] = point[posIndex] - theSum/2
        else:
            randNum = random.uniform(0,final)
            point[negIndex] = point[negIndex] - sign*randNum
            point[posIndex] = point[posIndex] - sign*randNum
#       print "Updated positive point is: ", point[posIndex]
#       print "Updated negative point is: ", point[negIndex]
        theSum = sum(point)
#       print ""
        count = count + 1
        if count > 50:
            return -1
#   print "The final sum is: ", sum(point)
#   print "The final 1-norm is: ", sum([abs(x) for x in point])
#   print point

def generatePoints(num,n,radius):
    points = []
    positives = []
    negatives = []
    for i in range(num):
        points.append(simplexPoint(n,pdf(random.random(),radius)))
#   plotting.plotPoints(points)
    removed = 0
    for i in range(num):
        positives, negatives = chooseNegatives(points[i-removed])
        error = shuffleSum(points[i-removed],positives,negatives)
        if error:
            points.pop(i-removed)
            removed = removed + 1
#   plotting.plotPoints(points)
    return points

def chooseNegatives(point):
    positives = []
    negatives = []
    for i in range(len(point)):
        if random.random() < 0.5:
            point[i] = -1*point[i]
            negatives.append(i)
        else:
            positives.append(i)
    if not len(positives) or not len(negatives):
        return chooseNegatives(point)
    else:
        return positives, negatives

def generateBall(num,n,center,radius):
    points = generatePoints(num,n,radius)
    ball = []
    for i in range(len(points)):
        ball.append(helpers.add(center,points[i]))
#   plotting.plotPointsWithCenter(ball,center)
    return ball

if __name__ == "__main__":
    generateBall(1000,3,(0.1,0.2,0.7),0.4)
