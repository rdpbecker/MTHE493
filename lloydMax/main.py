def sumMins(partition,means,N):
    theSum = 0
    for i in range(N):
        for point in partition[i]:
            theSum = theSum + abs(point-means[i])
    return theSum

def main():
    n = 30
    N = 3
    maxIterations = 10
    error = 0.1
    x = [0.43,0.5,0.6,0.7,3.5,3.6,3.7,0.2,0.1,0.3,0.4,0.45,0.35,0.43,3.45,3.55,3.65,3.61,3.56,3.49,5.5,5.6,5.7,5.8,5.65,5.75,5.55,5.58,5.63,5.64] 
    y = [0.5,3.5,5.5]
    distance = sys.maxint
    partition = []

    xY = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    yY = [1,1,1]
    
    for i in range(maxIterations):
        partition = setStuff.setsFromMeans(x,y,N)
        distortion = sumMins(partition,y,N)/n
        print partition, (distance-distortion)/distortion
        if (distance-distortion)/distortion <= error:
            break
        plt.plot(x,xY,'k.',y,yY,'bo')
        setStuff.meansFromSets(partition,y,N)
        plt.plot(y,yY,'ro')
        plt.show()
        distance = distortion

if __name__ == "__main__":
    import sys, setStuff, helpers, matplotlib.pyplot as plt
    main()
