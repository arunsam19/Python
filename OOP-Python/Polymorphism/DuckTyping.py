class PyCharm:

    def execute(self):
        print("Compiling")
        print("Running \n")

class MyEditor:

    def execute(self):
        print("Checks grammer")
        print("Checks usage metrics")
        print("Compiling")
        print("Running")

class Laptop:

    def run(self, Editor):
        Editor.execute()



p = PyCharm()
m = MyEditor()

l = Laptop()

l.run(p)
l.run(m)


