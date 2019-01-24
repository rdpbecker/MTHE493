helpString = """This is a description of all the command line 
arguments that are needed to run this program and their 
descriptions. 

Arguments:

#1: numSets - The number of means desired (i.e. the number of 
              clusters you want to see in the result)

#2: accuracy - The percent accuracy desired between iterations 
               of the k-means algorithm before termination

#3: flag - There are three ways this program can be run
           0) With manual input data. This data should be
              stored in the ../Testing directory, and should 
              be called test%.csv, where % is replaced by some
              integer. This integer (%) is the command line
              argument
           1) Randomly generate data according to a single 
              distribution, then cluster them according to
              this randomly generated data
           2) Randomly generate data in predefined clusters.
              The distribution of each of these clusters is
              governed by a RNG in randomGeneration.py. The
              distribution of the clusters is decided in 
              group%(), and the selection of which cluster
              is done by generatePerson.py. The points are 
              added to the set in blocks of `n' points, and 
              are added for `count' iterations

#4: testnum - The test number (required for manually selected
              test data

#5: n - The number points generated with flags 1 and 2. Only 
        required if flag=1,2

#6: low - The low end of the uniform distribution generated in
          case 1. Only required if flag=1

#7: high - The high bound on the uniform distribution generated
           in case 1. Only required if flag=1
"""

def helpStr():
    print helpString
