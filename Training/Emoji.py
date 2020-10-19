class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname


    def printname(self):
        print(self.firstname, self.lastname)


class Student(Person):
    print()

ali = Person("alireza", "omidvar" )
ali.printname()
student = Student("ahmad", "rezaee")
student.printname()