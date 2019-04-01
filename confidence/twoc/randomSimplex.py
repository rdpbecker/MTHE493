import random, matplotlib.pyplot as plt, plotting, sys, helpers
from mpl_toolkits.mplot3d import Axes3D

##############################################################
## Defines a pdf according to a random number and the radius
## of the ball to be generated
##############################################################

def pdf(num,radius):
    return num**0.5*radius 

##############################################################
## Generates a single on the n-simplex with \sum_i=1^n =radius
##
## Parameters: n - the dimension of the point generated
##             radius - the radius of the point on the simplex
##
## Returns: a random (uniform) simplex point
##############################################################

def simplexPoint(n,radius):
    aList = [0]
    newList = []
    for i in range(n-1):
        num = random.uniform(0,radius)
        aList.append(num)
    aList.append(radius)
    aList.sort()
    for i in range(n):
        newList.append(aList[i+1]-aList[i])
    return newList

##############################################################
## Once we have a simplex point, shift it so that 
## \sum_i=1^n =0 with an unchanged 1-norm
##
## Parameters: point - the point to be shifted
##             positives - a list of the positive components 
##                         of point
##             negatives - a list of the negative components
##                         of point
##
## Returns: -1 if there is an error, None otherwise
##############################################################

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

##############################################################
## Generates num points in n-dimensions in a ball of radius
## radius
##
## Parameters: num - the number of points to generate
##             n - the dimension of points to generate
##             radius - the radius of the ball to generate
##
## Returns: a list of points in a given radius
##############################################################

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
        if error: ## Point not generated
            points.pop(i-removed)
            removed = removed + 1
#   plotting.plotPoints(points)
    return points

##############################################################
## Randomly choose some of the components of the simplex point
## to be negative
## 
## Parameters: point - the point in question
##
## Returns: lists of the indexes of the positive and negative 
## components
##############################################################

def chooseNegatives(point):
    positives = []
    negatives = []
    for i in range(len(point)):
        if random.random() < 0.5:
            point[i] = -1*point[i]
            negatives.append(i)
        else:
            positives.append(i)
    if not len(positives) or not len(negatives): ## Shuffle won't work, so try again
        return chooseNegatives(point)
    else:
        return positives, negatives

##############################################################
## Generates a given number of points with a given number of
## components and given radius about a specified center
##
## Parameters: num - the number of points to generate
##             n - the dimesion of points to generate
##             center - the center of the ball
##             radius - the radius of the ball
##         
## Returns: a list of points in the specified ball
##############################################################

def generateBall(num,n,center,radius):
    points = generatePoints(num,n,radius)
    ball = []
    for i in range(len(points)):
        ball.append(helpers.add(center,points[i]))
#   plotting.plotPointsWithCenter(ball,center)
    return ball

##############################################################
## Run as script for testing
##############################################################

if __name__ == "__main__":
    generateBall(1000,3,(0.1,0.2,0.7),0.4)
