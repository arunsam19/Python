class Student:
    school = "ITO"                  # class variable
    def __init__(self,m1,m2,m3):
        self.m1 = m1                # instance variable
        self.m2 = m2
        self.m3 = m3

    def avg(self):                  #instance method
        return (self.m1 + self.m2 + self.m3)/3

    @classmethod
    def getSchool(cls):             #class method
        return cls.school

    @staticmethod
    def info():                     #static method
        print("This is Student class... in abc module")

s1 = Student(34,64,52)
s2 = Student(73,32,64)



print(s1.avg())
print(Student.getSchool())
s1.school = "ITO HSS"
print(Student.getSchool())
print(Student.info())

