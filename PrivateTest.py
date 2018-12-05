class Person(object):

    def __init__(self, name, age):
        self.name = name
        self.__age = age


p = Person('dagou', 2)
print(p.name)
