
class People(object):

    def __init__(self, name='', age=0, gender='male', account='', password=''):
        self.__name = name
        self.__age = age
        self.__gender = gender
        self.__account = account
        self.__password = password

    def set_name(self, name):
        '''

        :param name:
        :return:
        '''
        self.__name = name
        return None

    def set_age(self, age):
        self.__age = age
        return None

    def set_gender(self, gender):
        self.__gender = gender
        return None

    def set_account(self, account):
        self.__account = account
        return None

    def set_password(self, password):
        self.__password = password
        return None

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_gender(self):
        return self.__gender

    def get_account(self):
        return self.__gender

    def get_password(self):
        return self.__password

    def speak(self):
        print("My name is {0},I am {1} years old, I am {2}.".format(self.get_name(), self.get_age(), self.get_gender()))


class Student(People):

    def __init__(self):
        People.__init__(self, name='studier')
        pass


p = People()
s = Student()
print(s.get_name())

s.speak()
p.speak()
