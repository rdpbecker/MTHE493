import random

q = [[0.9,0.1,0.1],[0.1,0.1,0.9],[0.1,0.9,0.1]]

class adType:
    def __init__(self,p1,p2,p3):
        self.p = [p1,p2,p3]

class Type1:
    def __init__(self):
        self.p = []
        for i in range(3):
            self.p.append(random.uniform(q[0][i]-0.05,q[0][i]+0.05))

    def __str__(self):
        print self.p

class Type2:
    def __init__(self):
        self.p = []
	for i in range(3):
            self.p.append(random.uniform(q[1][i]-0.05,q[1][i]+0.05))

    def __str__(self):
        print self.p

class Type3:
    def __init__(self):
        self.p = []
	for i in range(3):
            self.p.append(random.uniform(q[2][i]-0.05,q[2][i]+0.05))

    def __str__(self):
        print self.p

if __name__ == "__main__":
    new = Type1()
    new.__str__()
