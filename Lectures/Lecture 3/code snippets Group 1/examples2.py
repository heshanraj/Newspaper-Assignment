

class NormalBook():
    def __init__(self, name):
        self.name = name

# b = NormalBook("Harry Potter")
# print(b.name)
# b.name = "Hunger Games"
# print(b.name)


class Book():

    def __init__(self, name):
        self.__name = name  # actually the attr name is _Book__name
        # self.__discount = discount

    def set_name(self, name):
        if "badword" in name:
            raise Exception("Bad word exception")

        self.__name = name

    def get_name(self):
        return self.__name

    # def computePrice(self, price):
    #     return price * self.__discount
    #
    #
    # def __calc_discount(self, totalPrice):
    #     return totalPrice * 123414312

b2 = Book("Harry Potter")


# b2.set_name("This is a badword")
b2.__name = "This is a badword"
b2.set_name("Hunger Games")

print(b2.get_name())

print("Printing secret stuff", b2.__name)

print("Accessing internal", b2._Book__name)


class Dog():
    counter = 0
    def __init__(self, name):
        self.name = name
        # self.counter = 13
        Dog.counter += 1

print("Dogcounter", Dog.counter)

fluffy = Dog("Fluffy")
max = Dog("Max")

print("Dogcounter", Dog.counter)
print("Fluffy counter", fluffy.counter)

