This directory includes a few scripts to show that our ideas
actually work. A description of each of the codes is as follows:

**adSuccess:** Generate a number of person objects (each with a
random internal distribution), and then distribute ads to those
people in two different ways:

  *Random method*: At each time step, give the person a random
(uniformly distributed) ad from our ad bank. 

  *Targetted method*: Generate some random (according to the 
person's internal distribution) searches for each person, then
give them the ad which has the greatest probability of being 
clicked.

For each of these methods, we give each person a bunch of ads 
and count the number of times an ad is clicked in each case.
At the end, we print out the percentage of ads clicked with
each method.

**learn:** Using a stochastic reinforcement learning method,
find the most successful ad (i.e. the one with the highest 
probability of being clicked) without attempting to 
approximate the person's distribution.
