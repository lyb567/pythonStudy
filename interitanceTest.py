class Dog():
    def __init__(self):
        print('Creating a dog...')


class HabaDog(Dog):

    pass
#当子类没有构造函数时，将调用父类构造函数
h = HabaDog()


class Person():
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def introduce(self):
        print("My name is {0}, I'm {1} years old!".format(self.__name, self.__age))


class Student(Person):
    pass


s = Student('大狗', 20)   #此时应该调用父类Person的构造，故应传相应参数
s.introduce()