class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age



    def talk(self):
        print(f"Hi ,I am {self.name} and I'm {self.age} years old ")


safiyeh = Person("safiyeh nikkhah", 35)
alireza = Person("Alireza omidvar", 34)
safiyeh.age = 25
safiyeh.talk()
alireza.talk()


