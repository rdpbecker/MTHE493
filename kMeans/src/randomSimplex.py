import random, matplotlib.pyplot as plt, helpers
from mpl_toolkits.mplot3d import Axes3D

def simplexPoint(n,radius):
    aList = []
    theSum = 0
    for i in range(n-1):
        num = random.uniform(0,radius-theSum)
        aList.append(num)
        theSum = theSum + num
    aList.append(radius-theSum)
    random.shuffle(aList)
    return aList

def plotPoints(points):
    fig = plt.figure()
    ax = fig.gca(projection = '3d')
    pointsX = [x[0] for x in points]
    pointsY = [y[1] for y in points]
    pointsZ = [z[2] for z in points]
    ax.scatter(pointsX,pointsY,pointsZ,c='r',marker='o')
    ax.invert_yaxis()
    plt.show()

def plotPointsWithNegs(points):
    fig = plt.figure()
    ax = fig.gca(projection = '3d')
    lists = [[],[],[],[],[],[],[],[]]
    for i in range(len(points)):
        if points[i][0] > 0:
            if points[i][1] > 0:
                if points[i][2] > 0:
                    lists[0].append(points[i])
                else:
                    lists[1].append(points[i])
            else:
                if points[i][2] > 0:
                    lists[2].append(points[i])
                else:
                    lists[3].append(points[i])
        else:
            if points[i][1] > 0:
                if points[i][2] > 0:
                    lists[4].append(points[i])
                else:
                    lists[5].append(points[i])
            else:
                if points[i][2] > 0:
                    lists[6].append(points[i])
                else:
                    lists[7].append(points[i])
    base = (0.13,0.73,0.35)
    colour = base
    for i in range(8):
        pointsX = [x[0] for x in lists[i]]
        pointsY = [y[1] for y in lists[i]]
        pointsZ = [z[2] for z in lists[i]]
        ax.scatter(pointsX,pointsY,pointsZ,c=colour,marker='o')
        colour = helpers.mod(1,helpers.add(colour,base))
    ax.invert_yaxis()
    plt.show()

def shuffleSum(point,positives,negatives):
    theSum = sum(point)
    count = 1
    print point
    print "The sum is: ", theSum
    while abs(theSum) > 0.001:
        print "Iteration: ", count
        posIndex = random.choice(positives)
        negIndex = random.choice(negatives)
        print "The sum is: ", theSum
        print "Positive Point: ", point[posIndex]
        print "Negative Point: ", point[negIndex]
        if theSum > 0:
            sign = 1
            m = min([point[negIndex]+1,point[posIndex]])
        else:
            sign = -1
            m = min([-1*point[negIndex],1-point[posIndex]])
        print "m is: ", m
        final = min([abs(theSum),m])
        print "The final radius is: ", final
        if abs(theSum)<0.1 and final == abs(theSum):
            point[negIndex] = point[negIndex] - theSum/2
            point[posIndex] = point[posIndex] - theSum/2
        else:
            randNum = random.uniform(0,final)
            point[negIndex] = point[negIndex] - sign*randNum
            point[posIndex] = point[posIndex] - sign*randNum
        print "Updated positive point is: ", point[posIndex]
        print "Updated negative point is: ", point[negIndex]
        theSum = sum(point)
        print ""
        count = count + 1
        if count > 100:
            return -1
    print "The final sum is: ", sum(point)
    print "The final 1-norm is: ", sum([abs(x) for x in point])
    print point

def generatePoints(num,n):
    points = []
    positives = []
    negatives = []
    for i in range(num):
        points.append(simplexPoint(n,random.random()**0.5))
    plotPoints(points)
    removed = 0
    for i in range(num):
        positives, negatives = chooseNegatives(points[i-removed])
        error = shuffleSum(points[i-removed],positives,negatives)
        if error:
            points.pop(i-removed)
            removed = removed + 1
    plotPoints(points)
    return points

def chooseNegatives(point):
    positives = []
    negatives = []
    for i in range(len(point)):
        if random.random() < 0.5:
            point[i] = -1*point[i]
            negatives.append(i)
        else:
            positives.append(i)
    if not len(positives) or not len(negatives):
        return chooseNegatives(point)
    else:
        return positives, negatives

def main(num,n):
    points = generatePoints(num,n)

main(1000,3)
