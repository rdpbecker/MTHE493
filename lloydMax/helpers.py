import sys

def distance(point1, point2):
    n = len(point1)
    theSum = 0
    for i in range(n):
        theSum = theSum + (point1[i]-point2[i])**2
    return theSum**0.5

def closest(means,point,n):
    minLen = sys.maxint
    index = -1
    for i in range(n):
        dist = abs(point-means[i])
        if dist < minLen:
            minLen = dist
            index = i
    return index

def mean(aList,mean):
    n = len(aList)
    if not n:
        return mean
    averagePoint = ()
    length = len(aList[0])
    for i in range(length):
        theSum = 0
        for j in range(n):
            theSum = aList[j][i] + theSum
        averagePoint = averagePoint + (theSum/n,)
    return averagePoint

def oneMean(aList,mean):
    n = len(aList)
    if not n:
        return mean
    theSum = 0
    for i in range(n):
        theSum = theSum + aList[i]
    return theSum/n
