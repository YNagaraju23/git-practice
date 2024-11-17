class class1:
    def method1(self):
        print("hello world")

class class2(class1):
    def method2(self):
        super().method1()
        print("this is method 2")

ob2=class2()
ob2.method2()
print(ob2)
