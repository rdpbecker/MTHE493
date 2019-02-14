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
    for i in range(len(means)):
        distSum = distSum + distance(means[i],newmeans[i])
    return distSum

##############################################################
## Find the sum of the errors between each point and its 
## representative
##
## Parameters: means - the set of means
##             partition - the set of clusters
##
## Returns: the sum of the errors of all the points
##############################################################

def partitionError(means,partition):
    error = 0
    for i in range(len(partition)):
        for point in partition[i]:
            error = error + distance(point,means[i])
    return error

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
