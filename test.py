
class A():
    def __init__(self, name='xiaomao', age=20):
        self.name = name
        self.age = age

    def say(self):
        print("My name is {},I'm {} years old.".format(self.name, self.age))




a = A('dagou',20)
b = A()
print(A.__dict__)
print('*'*20)
print(a.__dict__)
print('*'*20)
print(b.__dict__)