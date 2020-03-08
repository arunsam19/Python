class Student:

    def __init__(self, name, rno, model, cpu, RAM):
        self.name = name
        self.rno = rno
        self.lap = self.laptop(model, cpu, RAM)

    def show(self):
        print self.name, self.rno
        self.lap.show()

    class laptop:

        def __init__(self, model, cpu, RAM):
            self.model = model
            self.cpu = cpu
            self.RAM = RAM

        def show(self):
            print self.model, self.cpu, self.RAM


s1 = Student('Arun', 442, 'Lenovo', 'i5', 16)
s1.show()
s1.lap.show()

