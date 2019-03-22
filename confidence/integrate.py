import randomSimplex as rand, plotting, copy

def initCounts(n):
    counts = {}
    for i in range(-1,n):
        counts[i] = 0
    return counts

def createEmptyLists(n):
    lists = []
    aList = []
    for i in range(n):
        lists.append(copy.deepcopy(aList))
    return lists

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

def findProbs(center,radius):
    ball = rand.generateBall(1000,len(center),center,radius)
    n = len(center)
    counts = initCounts(n)
    lists = createEmptyLists(n+1)
#   print lists
    for i in range(len(ball)):
        index = findMaxIndex(ball[i])
#       print "Point: ", ball[i]
#       print "Index: ", index
#       print ""
        counts[index] = counts[index] + 1
        lists[index+1].append(ball[i])
    total = 0
    for i in range(n):
        total = total + counts[i]
    total = float(total)
    probs = []
    for i in range(n):
        probs.append(counts[i]/total)
    plotting.plotListsWithCenter(lists,center)
    return probs

#print findProbs((0.1,0.2,0.7),0.6)
