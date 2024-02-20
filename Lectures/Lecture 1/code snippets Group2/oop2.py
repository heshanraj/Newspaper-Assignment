
class Dog:
    def __init__(self, name):
        self.name = name
        self.color = None
        self.owner = None

class Person :
    def __init__(self, name ):
        self.name = name
        self.age = None
        self.pet = None
    def setPetDog(self, d1):
        self.pet = d1
        d1.owner = self


p = Person("Mr Smith")

d = Dog("Lassie")

p.setPetDog(d)
#d.setOwner(p)

d2 = Dog ("Rocky")


print (p.name )
print (d.owner.name)


