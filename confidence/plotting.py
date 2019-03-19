import matplotlib.pyplot as plt, helpers
from mpl_toolkits.mplot3d import Axes3D

def plotPoints(points):
    fig = plt.figure()
    ax = fig.gca(projection = '3d')
    pointsX = [x[0] for x in points]
    pointsY = [y[1] for y in points]
    pointsZ = [z[2] for z in points]
    ax.scatter(pointsX,pointsY,pointsZ,c='r',marker='o')
    ax.invert_yaxis()
    plt.show()

def plotPointsWithCenter(points,center):
    fig = plt.figure()
    ax = fig.gca(projection = '3d')
    pointsX = [x[0] for x in points]
    pointsY = [y[1] for y in points]
    pointsZ = [z[2] for z in points]
    ax.scatter(pointsX,pointsY,pointsZ,c='r',marker='o')
    ax.scatter([center[0]],[center[1]],[center[2]],c='g',marker='o')
    ax.invert_yaxis()
    plt.show()


def plotPointsWithNegs(points):
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
    plotLists(lists)

def plotLists(lists):
    fig = plt.figure()
    ax = fig.gca(projection = '3d')
    base = (0.13,0.73,0.35)
    colour = base
    print len(lists)
    for i in range(len(lists)):
        pointsX = [x[0] for x in lists[i]]
        pointsY = [y[1] for y in lists[i]]
        pointsZ = [z[2] for z in lists[i]]
        ax.scatter(pointsX,pointsY,pointsZ,c=colour,marker='o')
        colour = helpers.mod(1,helpers.add(colour,base))
    ax.invert_yaxis()
    plt.show()

