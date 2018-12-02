
class A():
    name = "dagou"
    age = 1

    def __init__(self, name='xiaomao', age=20):
        self.name = name
        self.age = age

    def say(self):
        print('my name is {0},I am {1} years old.'.format(self.name, self.age))

    def sayClass(name=name, age=age):
        print("My name is {0},I'm {1} years old.".format(name, age))


