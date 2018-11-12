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

def mean(aList,low,high):
    n = len(aList)
    if not n:
        return (low+high)/2
    theSum = 0
    for i in range(n):
        theSum = aList[i] + theSum
    return theSum/n

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
    minLen = abs(point-means[0])
    index = 0
    for i in range(1,n):
        if abs(point-means[i]) < minLen:
            minLen = abs(point-means[i])
            index = i
    return index

##############################################################
## Given a set of means and a set of points, finds the set of 
## closest points to each of the means
## 
## Parameters: means - the set of kMeans
##             points - the set of points
##             n - the number of kMeans
##
## Returns: the set of closest points to each of the means, 
##          which is index aligned
##############################################################

def setsFromMeans(means,points,n):    
    sets = []
    for i in range(n):
        sets.append([])
    for point in points:
        sets[closest(means,point,n)].append(point)
    return sets

##############################################################
## Given a set of sets, finds the mean of each set
##
## Parameters: sets - the set of sets
##             low - the lowest possible value in the range
##             high - the highest possible value in the range
##
## Returns: a list of the averages of the sets
##############################################################

def meansFromSets(sets,low,high):
    means = []
    for aSet in sets:
        means.append(mean(aSet,low,high))
    return means

##############################################################
## Does the Lloyd-Max algorithm on a 1-D set (that is 
## constructed here)
##
## Parameters: low - the lowest possible value in the range
##             high - the highest possible value in the range
##             n - the number of points in the set
##             numSets - the number of desired kMeans
##
## Returns: nothing. The results are printed using matplotlib
##############################################################

def main(low,high,n,numSets):
    # Generate a uniformly spaced list for the starting kMeans
    theRange = high - low
    spacing = theRange/(numSets-1)
    points = []
    means = range(low,high+spacing,numSets)

    # Randomly generate the set of points
    for i in range(n):
        points.append(rand.uniform(low,high))

    # Initialize the counter and plotting variables
    count = 0
    setsY = [1 for i in range(numSets)]
    pointsY = [1 for i in range(n)]
    
    # Do the Lloyd-Max algorithm 10 times, printing and
    # plotting the results each time
    while count < 10:
        quantizedSets = setsFromMeans(means,points,numSets)
        newmeans = meansFromSets(quantizedSets,low,high)
        print means 
        plt.plot(points,pointsY,'ro',means,setsY,'b+',newmeans,setsY,'k+')
        plt.show(block=False)
        # The 2 here means the plot will stay for 2 seconds.
        # Change this if you would like the plot to stay 
        # longer
        plt.pause(2)
        plt.close()
        count = count + 1
        means = newmeans

##############################################################
## Command line things. When you run the thing from the 
## command line, it goes here. This is where we import 
## stuff (make sure you have matplotlib installed properly.
## Takes 4 command line arguments
## 
## Arguments: low (int) - the lower bound for the randomly 
##                        generated set
##            high (int) - the upper bound for the randomly 
##                         generated set
##            n (int) - the number of points in the randomly
##                      generated set
##            numSets (int) - the number of kMeans
##############################################################
if __name__ == "__main__":
    import sys, random as rand, matplotlib.pyplot as plt, time
    args = sys.argv[1:]
    low = int(args[0])
    high = int(args[1])
    n = int(args[2])
    numSets = int(args[3])
    main(low,high,n,numSets)
