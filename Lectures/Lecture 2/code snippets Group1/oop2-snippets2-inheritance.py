
class Animal:

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def noise(self):
        print(self.name, "grrrrrr")


class Cat(Animal):

    def __init__(self, name, weight, furcolor):
        super().__init__(name, weight)
        self.furcolor = furcolor

    def noise(self):
        print(self.name, "Meow!")
        super().noise()

    # def __eq__(self, other):
        # if isinstance(other, self.__class__):


class Kitten(Cat):

    def noise(self):
        super().noise()
        Cat.noise(self)  # equal to the one above

        Animal.noise(self)  # this is different!

class Dog(Animal):

    def noise(self):
        print(self.name, "woof!")

a1 = Animal("Random animal", 20)
a1.noise()

cat1 = Cat("Fluffy", 5, "green")
cat1.noise()

print(cat1.furcolor, cat1.weight, cat1.name)

dog1 = Dog("Lassie", 15)
dog1.noise()

print(dog1.weight)

kitten = Kitten("BabyFluffy", 0.3, "white")



animals = [
    a1,
    cat1,
    dog1,
    kitten
]

for a in animals:
    if isinstance(a, Cat):
        print("Playing with ", a.name)
    else:
        print("not playing with ", a.name)



print("abc" + "cde")

class String:
    def __init__(self):
        self.value = []

    def __add__(self, other):
        self.value.extend(other.value)


class Integer:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        if isinstance(other, Integer):
            return Integer(self.value + other.value)


    def __str__(self):
        return str(self.value)


i1 = Integer(5)
i2 = Integer(7)

print(i1 + i2)