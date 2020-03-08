class Car:

    wheels = 4      #class variables

    def __inti__(self):
        self.mil = 10            # instance variables
        self.model = "Polo"

    def modelpare(self, other):
        if self.mil == other.mil:
            return True
        else:
            return False


c1 = Car()
c2 = Car()

c1.mil = 15
c2.mil = 20
c1.model = "Polo"
c2.model = "Rapid"

print c1.mil, c1.model, c1.wheels
print (c2.mil, c2.model, c2.wheels)
c1.wheels= 6
print c1.mil, c1.model, c1.wheels
print (c2.mil, c2.model, c2.wheels)

Car.wheels= 8
print c1.mil, c1.model, c1.wheels
print (c2.mil, c2.model, c2.wheels)
