class Person(object):
    name = 'dagou'
    __age = 2

    def pr_name(self):
        print('My name is {0}'.format(self.name))

class Student(Person):
    def st_name(self):
        Student.pr_name(self)
        super().pr_name()
        print(Student.name)
    pass


s = Student()
s.st_name()

