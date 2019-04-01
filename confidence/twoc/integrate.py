import randomSimplex as rand, plotting, copy

##############################################################
## Initialize a dictionary with n+1 keys, where key i 
## corresponds to the number of points whose maximum element
## is i, and key -1 corresponds to points which lie outside
## the simplex
## 
## Parameters: n - the number of components in the probability
##                 vectors
##
## Returns: a dictionary with all 0 values
##############################################################

def initCounts(n):
    counts = {}
    for i in range(-1,n):
        counts[i] = 0
    return counts

##############################################################
## Creates an list of empty lists
## 
## Parameters: n - the number of lists to create
##
## Returns: a list of (unaliased) empty lists
##############################################################

def createEmptyLists(n):
    lists = []
    aList = []
    for i in range(n):
        lists.append(copy.deepcopy(aList))
    return lists

##############################################################
## Finds the index of the maximum value of a list
##
## Parameters: point - the list to be checked
##
## Returns: the index of the maximum value of point. Returns
##          -1 if there is a value outside [0,1]
##############################################################

def findMaxIndex(point):
    maxIndex = -1
    maxVal = 0
    for i in range(len(point)):
        if point[i] > maxVal:
            maxIndex = i
            maxVal = point[i]
        elif point[i] < 0:
            return -1
    if maxVal > 1:
        return -1
    return maxIndex

##############################################################
## Generates points to draw a 3-simplex with lines between the
## areas with different maximal components. The list of points
## is returned
##############################################################

def simplex():
    aList = []
    for i in range(100):
        aList.append((i/float(100),1-i/float(100),0))
        aList.append((i/float(100),0,1-i/float(100)))
        aList.append((0,i/float(100),1-i/float(100)))
        aList.append((i/float(600)+1/float(3),i/float(600)+1/float(3),-1*i/float(300)+1/float(3)))
        aList.append((-1*i/float(300)+1/float(3),i/float(600)+1/float(3),i/float(600)+1/float(3)))
        aList.append((i/float(600)+1/float(3),-1*i/float(300)+1/float(3),i/float(600)+1/float(3)))
    return aList

##############################################################
## Finds the proportions of the ball which are in each area
##
## Parameters: center - the center point of the ball to be
##                      generated
##             radius - the radius of the ball to generate
##             flag - 1 to plot the stuff, 0 to not
##
## Returns: a list with the proportions of the ball which are 
##          in each area
##############################################################

def findProbs(center,radius,flag=0):
    ball = rand.generateBall(1000,len(center),center,radius)
    n = len(center)
    counts = initCounts(n)
    lists = createEmptyLists(n+1)
#   print n,lists
    for i in range(len(ball)):
        index = findMaxIndex(ball[i])
#       print "Point: ", ball[i]
#       print "Index: ", index
#       print ""
        counts[index] = counts[index] + 1
        lists[index+1].append(ball[i])
    total = 0
#   print [len(x) for x in lists]
    for i in range(n):
        total = total + counts[i]
    total = float(total)
    probs = []
    for i in range(n):
        probs.append(counts[i]/total)
    if flag:
        lists.insert(0,simplex())
        plotting.plotListsWithCenter(lists,center)
    return probs

#print findProbs((0.1,0.2,0.7),0.6)
