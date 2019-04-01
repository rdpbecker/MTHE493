In this directory, we write some code to randomly generate some 
points which lie on a simplex and within a ball of given 1-norm
and center, then determine what proportion of these points lie 
in different regions of the simplex. This is broken down into 
the following files:

**helpers**: Add and mod vectors

**integrate**: Performs Monte Carlo integration on a ball around
a center point

**plotting**: A bunch of functions to plot lists of points arranged 
in different ways

**randomSimplex**: Randomly generate points on the simplex 

**userThroughTime**: Generate a random user and some searches
for that user. Plots the progression of the user's confidence
range for 100, 1000, and 10000 searches
