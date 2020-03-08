
class A:

    def __init__(self):
        print("in A init")

    def feature1(self):
        print("Feature 1")

    def feature3(self):
        print("Feature 2")


class B():

    def __init__(self):
        print("in B init")

    def feature3(self):
        print("Feature 3")

    def feature4(self):
        print("Feature 4")

class C(B):

    def __init__(self):
        super(C, self).__init__()
        print("in C init")


    def feature5(self):
        print("Feature 5")

    def feature6(self):
        print("Feature 6")


a1 = C()
a1.feature5()
