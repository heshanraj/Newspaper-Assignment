

class Person :
    def __init__(self, name  ):
        self.name = name
        self.address = None
        self.age = None
        self.id = id
        self.familyname = None
    def speak (self):
        print (f"Hi My name is {self.name}")


class Teacher (Person):

    def __init__(self,name, salary):
        super().__init__(name)
        self.salary = salary
    def speak (self):
        super().speak ()
        print (f"Hi My name is {self.name} and I earn {self.salary}")



class Student (Person):
    def __init__(self, name, studyprog):
        #super().__init__ (self)
        Person.__init__(self, name )
        self.studyprog = studyprog
        self.fees = None


class EUStudent (Student):
    def __init__(self, name, studyprog):
        super().__init__(name, studyprog)
        self.fees = 400

class NonEUStudent (Student):
    def __init__(self, name, studyprog):
        super().__init__(name, studyprog)
        self.fees = 10000


s1 = EUStudent ("SamuelE", "INF")
print (s1.name )
print (s1.age )
s1.speak()

print (repr (s1))


s2 = NonEUStudent ("SamuelNE", "INF")
s1.speak ()


t1 = Teacher ("Deepak D", 100)
print (t1.salary)
t1.speak()


p1 = Person ("Sam")
p1.speak()

