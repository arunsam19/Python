class Student():

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def sum(self, a=None, b=None, c=None ):

        if(a != None and b != None and c != None):
            return a+b+c
        elif( a != None and b!= None):
            return a+b
        elif(a != None):
            return a
        else:
            return 0

s1 = Student(4, 6)

print(s1.sum(3,65, 2))

