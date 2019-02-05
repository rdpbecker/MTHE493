import csv,random as rand

def readFile(filepath):
    points = []
    with open(filepath, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            current = ()
            for thing in row:
                current = current + (float(thing),)
            points.append(current)
    return points

def writeFile(filepath,length,n):
    points = []
    for i in range(n):
        theSum = 0
        point = []
        for j in range(length-1):
            num = rand.uniform(0,1-theSum)
            theSum = theSum + num
            point.append(num)
        point.append(1-theSum)
        points.append([str(x) for x in point])
    
    with open(filepath,'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        for point in points:
            csvwriter.writerow(point)
    return points

if __name__ == "__main__":
    import sys
    args = sys.argv[1:]
    writeFile("../Testing/test"+args[0]+".csv",int(args[1]),int(args[2]))
