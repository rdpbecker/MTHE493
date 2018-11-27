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

def main(length,numSets,accuracy,flag):
    
    if flag:
        n = int(sys.argv[4])
        low = int(sys.argv[5])
        high = int(sys.argv[6])
        points = []
        theRange = high - low
        spacing = float(theRange)/numSets
        means = []
        i = low+spacing/2
        while i < high:
            j = 0
            thePoint = ()
            while j < length:
                thePoint = thePoint + (i,)
                j = j + 1
            means.append(thePoint)
            i = i + spacing
        for i in range(n):
            thePoint = ()
            j = 0
            while j < length:
                thePoint = thePoint + (rand.uniform(low,high),)
                j = j + 1
            points.append(thePoint)
    else:
        filepath = "../Testing/test"+sys.argv[4]+".csv"
        points = fileio.readFile(filepath)
        low = helpers.theMin(points)
        high = helpers.theMax(points)
        spacing = (high[0]-low[0]/numSets,high[1]-low[1]/numSets)
        means = []
        n = len(points)
        for i in range(numSets):
            means.append(helpers.add(low,helpers.mult(i,spacing)))

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
        newmeans = setStuff.meansFromSets(quantizedSets,low,high,length)
        print means 
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
                print pointsX
                fig = plt.figure()
                ax = fig.gca(projection = '3d')
                ax.scatter(pointsX,pointsY,pointsZ,c=(0.1,0.2,0.5),marker='+')
                ax.scatter(meansX,meansY,meansZ,'b+')
                ax.scatter(newmeansX,newmeansY,newmeansZ,'k+')
                plt.show()
        count = count + 1
        error = helpers.error(means,newmeans)
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
    import sys, random as rand, matplotlib.pyplot as plt, helpers,setStuff, fileio
    from mpl_toolkits.mplot3d import Axes3D
    args = sys.argv[1:]
    length = 3#int(args[3])
    numSets = int(args[0])
    accuracy = float(args[1])
    flag = int(args[2])
    main(length,numSets,accuracy,flag)
