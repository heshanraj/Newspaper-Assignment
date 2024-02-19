"""
-- Task 1:

Write a class "Car" with a constructor for the parameters
- make (e.g. Audi)
- age (e.g. 20 for 20 years)

and a method "describe()" that prints this information

-- Task 2
Write a method that celebrates my car's birthday.
i.e. increase its age by 1.
"""


class Car:

    def __init__(self, make, age):
        self.make = make
        self.age = age

    def describe(self):
        print(self.make, self.age)
        # return self.make, self.age

    def birthday(self):
        self.age += 1
        print("happy birthday")

    def get_make(self):
        return self.make


car1 = Car("VW", 10)
car1.describe()
# print(car1.describe())

car1.birthday()   # <-- implement this!
car1.describe()


class Dog:
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner

    def set_owner(self, owner):
        self.owner = owner

class Person:
    def __init__(self, name, age, job, pet):
        self.name = name
        self.age = age
        self.job = job

    def describe(self):
        print(self.name, self.age, self.job)

    def set_pet(self, pet):
        self.pet = pet

stefan = Person("Stefan", 21, "Nerd")
pluto = Dog("pluto", stefan)
goofy = Person("Goofy", 7, "Comedian")

print(pluto.name)
# print(pluto.owner)
# print(pluto.owner.name)
pluto.owner.describe()

pluto.set_owner(goofy)
pluto.owner.describe()


goofy.set_pet(pluto)

print(pluto.owner.pet.name)
print(goofy.pet.owner.name)