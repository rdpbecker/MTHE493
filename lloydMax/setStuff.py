import helpers

def setsFromMeans(points,means,n):
    sets = []
    for i in range(n):
        sets.append([])
    for point in points:
        sets[helpers.closest(means,point,n)].append(point)
    return sets

def meansFromSets(sets,means,N):
    for i in range(N):
        means[i] = helpers.oneMean(sets[i],means[i])
