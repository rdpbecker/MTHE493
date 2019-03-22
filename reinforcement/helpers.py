##############################################################
##
##############################################################

def theMin(points):
    point = ()
    for i in range(len(points[0])):
        theMin = points[0][i]
        for j in range(len(points)):
            if points[j][i] < theMin:
                theMin = points[j][i]
        point = point + (theMin,)
    return point

##############################################################
##
##############################################################

def theMax(points):
    point = ()
    for i in range(len(points[0])):
        theMax = points[0][i]
        for j in range(len(points)):
            if points[j][i] > theMin:
                theMax = points[j][i]
        point = point + (theMax,)
    return point
##############################################################
##
##############################################################

def add(point1,point2):
    point = ()
    for i in range(len(point1)):
        point = point + (point1[i]+point2[i],)
    return point

##############################################################
##
##############################################################

def mult(num,point):
    new = ()
    for i in range(len(point)):
        new = new + (num*point[i],)
    return new

##############################################################
##
##############################################################

def mod(modulus,point):
    new = ()
    for i in range(len(point)):
        new = new + (point[i]%modulus,)
    return new

##############################################################
## Finds the Euclidean norm between two points
##
## Parameters: point1 - the first point
##             point2 - the second point
##
## Returns: the Euclidean distance between the two points
##############################################################

def distance(point1, point2):
    n = len(point1)
    theSum = 0
    for i in range(n):
        theSum = theSum + (point1[i]-point2[i])**2
    return theSum**0.5

##############################################################
## Finds the average of a list
##
## Parameters: aList - the list
##             low - the lowest value in the range
##             high - the highest value in the range
##
## Returns: the average of the list, the average value in the 
##          range if the list is empty
##############################################################

def mean(aList,length,mean):
#   print aList
    n = len(aList)
#   print n, length
    if not n:
        return mean 
    averagePoint = ()
    for i in range(length):
        theSum = 0
        average = 0
        for j in range(n):
            theSum = aList[j][i] + theSum
        averagePoint = averagePoint + (theSum/n,)
    return averagePoint

##############################################################
## Given a point, find the index of the value in means which 
## is closest to the point
## 
## Parameters: means - the set of current kMeans
##             point - the point to be checked
##             n - the number of kMeans
##
## Returns: the index of the value in means which is closest 
##          to point
##############################################################

def closest(means,point,n):
    minLen = distance(point,means[0])
    index = 0
    for i in range(n):
        if distance(point,means[i]) < minLen:
            minLen = distance(point,means[i])
            index = i
    return index

##############################################################
## Find the error between the last and current sets of means
##
## Parameters: means - the last set of means
##             newmeans - the current set of means
##
## Returns: the error between the sets of means
##############################################################

def error(means, newmeans):
    distSum = 0
#    print means
    for i in range(len(means)):
        distSum = distSum + distance(means[i],newmeans[i])
    return distSum

def partitionError(means,partition):
    error = 0
    for i in range(len(partition)):
        for point in partition[i]:
            error = error + distance(point,means[i])
    return error
