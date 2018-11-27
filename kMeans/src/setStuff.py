import helpers 

##############################################################
## Given a set of means and a set of points, finds the set of 
## closest points to each of the means
## 
## Parameters: means - the set of kMeans
##             points - the set of points
##             n - the number of kMeans
##
## Returns: the set of closest points to each of the means, 
##          which is index aligned
##############################################################

def setsFromMeans(means,points,n):    
    sets = []
    for i in range(n):
        sets.append([])
    for point in points:
        sets[helpers.closest(means,point,n)].append(point)
    return sets

##############################################################
## Given a set of sets, finds the mean of each set
##
## Parameters: sets - the set of sets
##             low - the lowest possible value in the range
##             high - the highest possible value in the range
##
## Returns: a list of the averages of the sets
##############################################################

def meansFromSets(sets,length,means):
    newmeans = []
    print sets, means
    for i in range(len(sets)):
        newmeans.append(helpers.mean(sets[i],length,means[i]))
    return newmeans
