import allio
scheme = -1 

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

def partitionError(means,partition):
    global scheme
    error = 0
    for i in range(len(partition)):
        for point in partition[i]:
            error = error + distance(point,means[i])
    return error

##############################################################
##
##
##
##############################################################

def partitionError1(means,partition):
    error = 0
    for i in range(len(partition)):
        for point in partition[i]:
            error = error + innerProduct(point,means[i])
    return error

##############################################################
## Find the sum of the errors between each point and its 
## representative using some l_p norm defined by the distance
## function
##
## Parameters: means - the set of means
##             partition - the set of clusters
##
## Returns: the sum of the errors of all the points
##############################################################

def partitionError2(means,partition):
    error = 0
    for i in range(len(partition)):
        for point in partition[i]:
            error = error + distance(point,means[i])
    return error

##############################################################
##
##
##
##############################################################

def distance(point1,point2):
    global scheme
    if not scheme+1:
        scheme = int(allio.sanitizeInput("Pick the distortion measure - l_{\infty} (0) or l_p (p)"))
    if not scheme:
        return distanceInfty(point1,point2)
    if scheme >= 1:
        return distancep(point1,point2,scheme)
            

##############################################################
## Finds the l_p norm between two points
##
## Parameters: point1 - the first point
##             point2 - the second point
##
## Returns: the Euclidean distance between the two points
##############################################################

def distancep(point1, point2,p=2):
    n = len(point1)
    theSum = 0
    for i in range(n):
        theSum = theSum + abs((point1[i]-point2[i])**p)
    return theSum**(1/float(p))

##############################################################
##
##
##
##############################################################

def distanceInfty(point1,point2):
    n = len(point1)
    maxVal = -1
    for i in range(n):
        if abs(point1[i]-point2[i]) > maxVal:
            maxVal = abs(point1[i]-point2[i])
    return maxVal

##############################################################
##
##
##
##############################################################

def innerProduct(point1,point2):
    n = len(point1)
    theSum = 0
    for i in range(n):
        theSum = theSum + point1[i]*point2[i]
    return theSum

##############################################################
##
##
##
##############################################################

def norm(vector):
    theSum = 0
    for i in range(len(vector)):
        theSum = vector[i]**2
    return theSum**0.5

##############################################################
##
##
##
##############################################################

def closest(means,point,n):
    minLen = distance(point,means[0])
    index = 0
    for i in range(n):
        num = distance(point,means[i])
        if num < minLen:
            minLen = num
            index = i
    return index

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

def closest1(means,point,n):
    maxLen = innerProduct(point,means[0])
    maxList = [0]
#   print "\nNew point\n" ,point
#   print means[0], ": ", maxLen
    for i in range(1,n):
        prod = innerProduct(point,means[i])
#       print means[i], ": ", prod
        if prod > maxLen:
            maxLen = prod
            maxList = [i]
#           print "New max: ", maxList
        elif prod == maxLen:
            maxList.append(i)
#           print "Same max: ", maxList
    minLen = norm(means[maxList[0]])
    index = maxList[0]
    for i in range(1,len(maxList)):
        if norm(means[maxList[i]]) < minLen:
            minLen = norm(means[maxList[i]])
            index = maxList[i]
    return index

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

def closest2(means,point,n):
    minLen = distance(point,means[0])
    index = 0
    for i in range(n):
        num = distance(point,means[i])
        if num < minLen:
            minLen = num
            index = i
    return index
