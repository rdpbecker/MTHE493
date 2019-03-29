This directory contains a couple classes which can be used to 
describe people. The important one is person.py, which contains
the class description for *Person*. This class has the following 
attributes and methods. The methods are described in more depth 
in the file:

##Attributes

**probsActual** *(tuple)*
A tuple describing the person's actual dispositions. Randomly
generated when the class is instantiated.

**probsEmpirical** *(list)*
A list describing what the person looks like empirically based
on their search history.

**countEmpirical** *(list)*
A list counting the searches relating to each ad. The *i*th 
element is the count of the *i*th ad.

**totalSearches** *(int)*
The total number of searches.

**n** *(int)*
The number of ads, which is the length of tuples and lists. 
Included only for convenience.

**maxIndexActual** *(int)*
The index of the element of probsActual with the maximum value.

**maxIndexEmpirical** *(int)*
The index of the element of probsEmpirical with the maximum
value. If two elements are equal, the index which reached the
maximum first.

##Methods

**__init__**

**clickAd**

**randomSearch**

**updateProbs**

**confidence**

**get_**

**printProbs**

**printPerson**
