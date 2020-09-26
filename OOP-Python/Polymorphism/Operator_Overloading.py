a = 4
b = 6

c = 'Test'
d = 'program'

#print (a  + b)
#print(c + d)

#print(int.__add__(a,b))




class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        self.t = self.m1 + self.m2
        other.t = other.m1 + other.m2
        if  self.t > other.t:
            print("{} {} ".format(self.t, other.t))


s1 = Student(46,53)
s2 = Student(73,2)
#print(s1 + s2)
print(s1.__add__(s2))


