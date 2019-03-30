import integrate as inte, sys
sys.path.append("../")
from People import person as p

person = p.Person(3)
person.printProbs()

count = 0
for i in range(2,5):
    while count <= 10**i:
        person.randomSearch()
        count = count + 1
    print inte.findProbs(person.getProbsEmpirical(),person.confidence(),1)
