##############################################################
## Adds two points
##############################################################

def add(point1,point2):
    point = ()
    for i in range(len(point1)):
        point = point + (point1[i]+point2[i],)
    return point

##############################################################
## Takes the modulus of a point, componentwise
##############################################################

def mod(modulus,point):
    new = ()
    for i in range(len(point)):
        new = new + (point[i]%modulus,)
    return new
