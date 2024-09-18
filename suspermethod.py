class Parent():
    def printmsg(self):
        print('hi how are you')

class Child(Parent):
    def printmsg(self):
        super().printmsg()
        print('hi how are you... i am fine')

ch1=Child()
ch1.printmsg()

x=10
y=x
print(y)
