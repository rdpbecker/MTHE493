import fileio, setStuff, helpers,matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def sanitizeInput(header):
    print header
    line = sys.stdin.readline()
    print ""
    return line[:-1]

def doKMeans(points,means):
    n = len(points)
    numSets = len(means)
    # Initialize the counter and plotting variables
    count = 0
    meansY = [1 for i in range(numSets)]
    newmeansY = [1 for i in range(numSets)]
    pointsY = [1 for i in range(n)]
    
    error = 2*accuracy

    # Do the Lloyd-Max algorithm 10 times, printing and
    # plotting the results each time
    while error > accuracy:
        quantizedSets = setStuff.setsFromMeans(means,points,numSets)
        newmeans = setStuff.meansFromSets(quantizedSets,length,means)
#        print means 
        if length == 1 or length == 2 or length == 3:
            if length == 2:
                pointsX, pointsY = zip(*points)
                meansX, meansY = zip(*means)
                newmeansX, newmeansY = zip(*newmeans)
            if length < 3:
                plt.plot(pointsX,pointsY,'ro',meansX,meansY,'b+',newmeansX,newmeansY,'k+')
                plt.show(block=False)
                # The 2 here means the plot will stay for 2 seconds.
                # Change this if you would like the plot to stay 
                # longer
                plt.pause(2)
                plt.close()
            if length == 3:
#               pointsX = [x[0] for x in points] 
#               pointsY = [y[1] for y in points] 
#               pointsZ = [z[2] for z in points]
#               meansX = [x[0] for x in means]
#               meansY = [y[1] for y in means]
#               meansZ = [z[2] for z in means]
#               newmeansX = [x[0] for x in newmeans]
#               newmeansY = [y[1] for y in newmeans]
#               newmeansZ = [z[2] for z in newmeans]
#                print pointsX
#               fig = plt.figure()
#               ax = fig.gca(projection = '3d')
#               ax.scatter(pointsX,pointsY,pointsZ,c=(0.1,0.2,0.5),marker='+')
#               ax.scatter(meansX,meansY,meansZ,c='r',marker='o')
#               ax.scatter(newmeansX,newmeansY,newmeansZ,c='m',marker='o')
#               ax.invert_yaxis()
#               plt.show()#block = False)
#               plt.pause(2)
#               plt.close()
                plotSets(quantizedSets)
        count = count + 1
        error = helpers.error(means,newmeans)
        means = newmeans
    return means, quantizedSets

def doKMeans3(points,means,pausebuffer):
    n = len(points)
    numSets = len(means)
    # Initialize the counter and plotting variables
    count = 0
    
    error = 2*accuracy

    # Do the Lloyd-Max algorithm 10 times, printing and
    # plotting the results each time
    while error > accuracy:
        quantizedSets = setStuff.setsFromMeans3(means,points,numSets)
        newmeans = setStuff.meansFromSets3(quantizedSets,length,means)
        plotSets(quantizedSets,pausebuffer)
        count = count + 1
        error = helpers.error(means,newmeans)
        means = newmeans
    return means, quantizedSets

def plotSets(quantizedSets,pausebuffer):
    count = 1
    base = (0.31,0.43,0.27)
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
    ax.invert_yaxis()
    if pausebuffer <= 0:
        plt.show()
    else:
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
    gen.randomInit(mostRandom)
    points = {} 
    means = gen.meanInit(numSets)
    count = int(sanitizeInput("Input the number of iterations here:"))
    pausebuffer = float(sanitizeInput("Input the pause buffer here:"))
    for i in range(count):
        print "Iteration: ", i+1
        extendList(points,n)
        means, sets = doKMeans3(points,means,pausebuffer)    
    if not mostRandom:
        checkErrors(sets)

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
        n = int(sanitizeInput("Input the block size here:")) 
        mostRandom = int(sanitizeInput("Print 1 for purely random, 0 for predefined clusters"))
        increaseN(n,mostRandom,numSets)
        return
    elif flag == 1:
        n = int(sanitizeInput("Input the sample size here:") )
        low = float(sanitizeInput("Input the range minimum here:"))
        high = float(sanitizeInput("Input the range maximum here:"))
        points = []
        theRange = high - low
        spacing = float(theRange)/numSets
        means = []
        thePoint = ()
        midpoint = ()
        for j in range(length-1):
            thePoint = thePoint + (0,)
            midpoint = midpoint + (1/(numSets-1)**0.5,)
        thePoint = thePoint + (1,)
        midpoint = midpoint + (0,)
        increment = helpers.add(thePoint,helpers.mult(-1,midpoint))
        for i in range(numSets):
            means.append(helpers.add(thePoint,helpers.mult(float(i+0.5)/numSets,increment)))
        for i in range(n):
            thePoint = ()
            j = 0
            while j < length:
                thePoint = thePoint + (rand.uniform(low,high),)
                j = j + 1
            points.append(thePoint)
    else:
        testnum = sanitizeInput("Input the test number here:")
        filepath = "../Testing/test"+testnum+".csv"
        points = fileio.readFile(filepath)
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

#   print means
    doKMeans(points,means)

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
    import sys, random as rand, matplotlib.pyplot as plt, helpers,setStuff, fileio, randomGeneration as gen, helps
    from mpl_toolkits.mplot3d import Axes3D
    helps.helpStr()
    args = sys.argv[1:]
    length = 3#int(args[3])
    numSets = int(sanitizeInput("Input the desired number of clusters:"))
    accuracy = float(sanitizeInput("Input the desired percent accuracy:"))/100
    flag = int(sanitizeInput("Input the flag corresponding to the desired test:"))
    main(numSets,accuracy,flag,length)
