import csv

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

print readFile("../Testing/test0.csv")
