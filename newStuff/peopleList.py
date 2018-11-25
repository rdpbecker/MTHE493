import people, random, math

def norm(point):
    aSum = 0
    for i in point:
        aSum = aSum + i**2
    return aSum**0.5

def addPoint(point1,point2):
    point = []
    for i in range(len(point1)):
        point.append(point1[i]+point2[i])
    return point

def multPoint(point,mult):
    newpoint
    for i in range(len(point)):
        newpoint.append(mult*point[i])
    return newpoint

def dist(point1,point2):
    return norm(addPoint(point1,multPoint(point2,-1)))

def distList(people,ad):
    distList = []
    aSum = 0
    for person in people:
        distance = dist(person,ad)
        distList.append(distance)
        aSum = aSum + distance
    for i in range(len(distList)):
        distList[i] = distList[i]/aSum
    return distList

def click(prob):
    if random.uniform(0,1) < prob:
        return 1
    return 0

def peopleFromBinary(people,clicks):
    aList = []
    for i in range(len(clicks)):
        if clicks[i]:
            aList.append(people[i])
    return aList

def centroid(aList):
    m = len(aList[0])
    for i in range(m):
        sumPoint.append(0)
    n = len(aList)
    for i in range(n):
        sumPoint = addPoint(sumPoint,aList[i])
    return multPoint(sumPoint,1/n)

def main():
    for i in range(10):
        rand = int(math.floor(random.uniform(0,3)))+1
        string = "Type" + str(rand)
        function = getattr(people,string)
        newClass = function()
        newClass.__str__()
    
    people = [[2,6],[2,5],[2,2],[3,2],[3,4]]
    probs = [1,1,0,0,0]
    ad = [1,1]
    
    for i in range(10):
        clicks = []
        normedDistList = distList(people,ad)
        for prob in probs
            clicks.append(click(prob))
        clickedList = peopleFromBinary(people,clicks)
        aSum = 0
        for i in range(len(people)):
            aSum = aSum + clicks[i]*normedDistList[i]
        assumption = centroid(clickedList)


if __name__ == "__main__":
    import sys
    args = sys.argv[1:]
    list1 = []
    list2 = []
    n = len(args)/2
    for i in range(n):
        list1.append(int(args[i]))
    for i in range(n):
        list2.append(int(args[n+i]))
    print dist(list1,list2) 
    #main()
