import fileio, setStuff, helpers,matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

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
                pointsX = [x[0] for x in points] 
                pointsY = [y[1] for y in points] 
                pointsZ = [z[2] for z in points]
                meansX = [x[0] for x in means]
                meansY = [y[1] for y in means]
                meansZ = [z[2] for z in means]
                newmeansX = [x[0] for x in newmeans]
                newmeansY = [y[1] for y in newmeans]
                newmeansZ = [z[2] for z in newmeans]
#                print pointsX
                fig = plt.figure()
                ax = fig.gca(projection = '3d')
                ax.scatter(pointsX,pointsY,pointsZ,c=(0.1,0.2,0.5),marker='+')
                ax.scatter(meansX,meansY,meansZ,c='r',marker='o')
                ax.scatter(newmeansX,newmeansY,newmeansZ,c='b',marker='o')
                ax.invert_yaxis()
                plt.show()#block = False)
#               plt.pause(2)
#               plt.close()
        count = count + 1
        error = helpers.error(means,newmeans)
        means = newmeans
    return means, quantizedSets

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

def main(length,numSets,accuracy,flag,testnum):
    
    if flag == 2:
        n = int(sys.argv[5])
        points = []
        means = [gen.group1(),gen.group2(),gen.group3(),gen.group4(),gen.group5()]
        for i in range(n):
            points.append(gen.generatePerson(5))
        print points
        print means
    elif flag == 1:
        n = int(sys.argv[5])
        low = int(sys.argv[6])
        high = int(sys.argv[7])
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
    import sys, random as rand, matplotlib.pyplot as plt, helpers,setStuff, fileio, randomGeneration as gen
    from mpl_toolkits.mplot3d import Axes3D
    args = sys.argv[1:]
    length = 3#int(args[3])
    numSets = int(args[0])
    accuracy = float(args[1])
    flag = int(args[2])
    testnum = args[3]
    main(length,numSets,accuracy,flag,testnum)
