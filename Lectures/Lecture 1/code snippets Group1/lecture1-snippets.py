obj = object()
print(obj)
# obj.color = "red"  # <--- Causes errors

# class definition
class Dog:

    # constructor  ("initializer")
    def __init__(self, name, color, height="medium"):
        # This code is called every time I create an object of class Dog
        self.name = name
        self.color = color  #"brown"
        self.height = height  #"tall"

    # method
    def bark(self):
        print("woof")

    def describe(self):
        """A method to print out the dog's name, color and height"""
        print(self.name, self.color, self.height)



dog1 = Dog("Lassie", color="black", height="mini")
# print(dog1)
#dog1.bark()
# print(dog1.name, dog1.color, dog1.height)
dog1.describe()

dog2 = Dog("Max", color="white", height="huge")
# print(dog2.name, dog2.color, dog2.height)
dog2.describe()

dog3 = Dog("Pluto", color="brown")
# print(dog3.name, dog3.color, dog3.height)
dog3.describe()


def describeDog(dog_dict):
    print(dog_dict["name"], dog_dict["color"], dog_dict["height"])