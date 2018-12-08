class Person(object):

    def __init__(self, name, age):
        self.name = name
        self.__age = age


p = Person('dagou', 2)
print(p.name)


class Dog(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print("My name is {0},I'm {1} years old.".format(self.name, self.age))


d = Dog('dagou', 5)
print(d.name)
d.say_hello()
