import allio, setStuff, helpers,matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def doKMeans3(points,means,pausebuffer):
    n = len(points)
    numSets = len(means)
    # Initialize the counter and plotting variables
    count = 0
 #  
    error = 2*accuracy

    # Do the Lloyd-Max algorithm 10 times, printing and
    # plotting the results each time
    while error > accuracy:
        quantizedSets = setStuff.setsFromMeans3(means,points,numSets)
        newmeans = setStuff.meansFromSets3(quantizedSets,length,means)
        plotSets(quantizedSets,newmeans,pausebuffer)
        count = count + 1
        error = design.error(means,newmeans)
        print "Current error: ", design.partitionError(newmeans,quantizedSets)/n
        means = newmeans
    return means, quantizedSets

def plotSets12(quantizedSets,means,length,pausebuffer):
    base = (0.31,0.53,0.87)
    colour = (0.0,0.0,0.0)
    for cluster in quantizedSets:
        colour = helpers.add(colour,base)
        colour = helpers.mod(1,colour)
        pointsX = [x[0] for x in cluster.keys()]
        if length == 2:
            pointsY = [y[0] for y in cluster.keys()]
        elif length == 1:
            pointsY = [1 for y in cluster.keys()]
        plt.plot(pointsX,pointsY,c=colour,marker='+')
    if length == 2:
        pointsX = [x[0] for x in means]
        pointsY = [y[1] for y in means]
    elif length == 1:
        pointsX = means
        pointsY = [1 for y in means]
    plt.plot(pointsX,pointsY,c='r',marker='o')
    if pausebuffer <= 0:
        plt.show()
    else:
        plt.show(block=False)
        plt.pause(pausebuffer)
        plt.close()

def plotSets(quantizedSets,means,pausebuffer):
    count = 1
    base = (0.31,0.53,0.87)
    colour = (0.0,0.0,0.0)
    fig = plt.figure()
    ax = fig.gca(projection = '3d')
    for cluster in quantizedSets:
        colour = helpers.add(colour,base)
        colour = helpers.mod(1,colour)
        pointsX = [x[0] for x in cluster.keys()]
        pointsY = [y[1] for y in cluster.keys()]
        pointsZ = [z[2] for z in cluster.keys()]
        ax.scatter(pointsX,pointsY,pointsZ,c=colour,marker='+')
        count = count + 1
    colour = helpers.add(colour,base)
    colour = helpers.mod(1,colour)
    pointsX = [x[0] for x in means]
    pointsY = [y[1] for y in means]
    pointsZ = [z[2] for z in means]
    ax.scatter(pointsX,pointsY,pointsZ,c='r',marker='o')
    ax.invert_yaxis()
    if pausebuffer <= 0:
        plt.show()
    elif pausebuffer > 0:
        plt.show(block=False)
        plt.pause(pausebuffer)
        plt.close()

def checkErrors(quantizedSets):
    n = len(quantizedSets)
    for i in range(n):
        cluster = quantizedSets[i]
        flag = 1
        for point in cluster.keys():
            if cluster[point] != i+1:
                print point, "Expected: ", cluster[point], ", got: ", i+1
                flag = 0
        if flag:
            print "Everything ok for cluster #", i+1

def extendList(points,n):
    for i in range(n):
        vect, group = gen.generatePerson(5)
        points[vect] = group

def increaseN(n,mostRandom,numSets):
    gen.randomInit(mostRandom,numSets)
    points = {} 
    means = gen.meanInit(numSets)
    count = int(allio.sanitizeInput("Input the number of iterations here:"))
    pausebuffer = float(allio.sanitizeInput("Input the pause buffer here:"))
    for i in range(count):
        print "Iteration: ", i+1
        extendList(points,n)
        means, sets = doKMeans3(points,means,pausebuffer)    
    if not mostRandom:
        checkErrors(sets)
    print "\nThe average error is: ", design.partitionError(means,sets)/n/count
    write = allio.sanitizeInput("Export the data used? [y/n]")
    if write == "y":
        allio.exportData(points.keys())

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

def main(numSets,accuracy,flag,length=3):
    if flag == 2:
        n = int(allio.sanitizeInput("Input the block size here:")) 
        mostRandom = int(allio.sanitizeInput("Print 1 for purely random, 0 for predefined clusters"))
        increaseN(n,mostRandom,numSets)
        return
    else:
        testnum = allio.sanitizeInput("Input the test number here:")
        filepath = "../Testing/test"+testnum+".csv"
        points = allio.readFile(filepath)
#       low = helpers.theMin(points)
#       high = helpers.theMax(points)
#       spacing = ()
#       for i in range(length):
#           spacing = spacing + ((high[i]-low[i])/numSets,)
        means = []
        n = len(points)
        thePoint = ()
        midpoint = ()
        for j in range(length-1):
            thePoint = thePoint + (0,)
            midpoint = midpoint + (1/float(length-1),)
        thePoint = thePoint + (1,)
        midpoint = midpoint + (0,)
        increment = helpers.add(midpoint,helpers.mult(-1,thePoint))
#       print thePoint, midpoint, increment
        thePoint = helpers.add(thePoint,helpers.mult(0.25,increment))
        increment = helpers.mult(0.5,increment)
#       print thePoint, increment
        for i in range(numSets):
            means.append(helpers.add(thePoint,helpers.mult(float(i+0.5)/numSets,increment)))
        means = gen.meanInit(numSets)

#   print means
    pausebuffer = float(allio.sanitizeInput("Input the pause buffer here:"))
    means, sets = doKMeans3(points,means,pausebuffer)

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
    import sys, random as rand, matplotlib.pyplot as plt, helpers,setStuff, design, allio, randomGeneration as gen, helps
    from mpl_toolkits.mplot3d import Axes3D
    helps.helpStr()
    args = sys.argv[1:]
    length = int(allio.sanitizeInput("Input the dimension of the points you'd like to generate:"))
    numSets = int(allio.sanitizeInput("Input the desired number of clusters:"))
    accuracy = float(allio.sanitizeInput("Input the desired percent accuracy:"))/100
    flag = int(allio.sanitizeInput("Input the flag corresponding to the desired test:"))
    main(numSets,accuracy,flag,length)
