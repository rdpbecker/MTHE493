def main(accuracy, testnum,eaccuracy,length=3,flag=0):
    error = sys.maxint
    error2 = sys.maxint
    newerror = sys.maxint / 10
    numSets = 0
    while ((error-newerror)/newerror > eaccuracy) or ((error2-error)/error > eaccuracy):
        numSets = numSets + 1
        means, partition = kMeans.main(length,numSets,accuracy,flag,testnum)
        error2 = error
        error = newerror
        newerror = helpers.partitionError(means,partition)
        print "Error is: ", error, "New error is: ", newerror
    return numSets

if __name__ == "__main__":
    import sys, kMeans, helpers
    args = sys.argv[1:]
    accuracy = float(args[0])
    testnum = args[1]
    eaccuracy = float(args[2])
    print main(accuracy,testnum,eaccuracy)
