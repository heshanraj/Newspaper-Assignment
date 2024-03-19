
class Book():
    """A book class."""
    def __init__(self, name, pages):
        self.name = name
        self.pages = pages

    def sell(self):
        print("Sold")

    def __eq__(self, other):
        if isinstance(other, Book):
            return self.name == other.name
        elif isinstance(other, str):
            return self.name == other
        else:
            return False

    def __str__(self):
        return f"The Book {self.name} with {self.pages}"

    def __len__(self):
        return self.pages

a1 = Book("Harry Potter", 304)
a2 = Book("Harry Potter", 310)

def sameBook(book1, book2):
    return book1.name == book2.name

print("Comparison with ==", a1 == a2)
print("Same Book function", sameBook(a1, a2))


print("Comparison with 'Harry Potter' string", a1 == "Harry Potter")
print("Comparison with 365", a1 == 365)


print(str(a1))


print("Documentation", a1.__doc__)


print(a1.__class__("Hunger Games", 1000))

print("Object Dict", a1.__dict__)

print("Class dict", a1.__class__.__dict__)

print("Init from dict", a1.__class__.__dict__["__init__"])


# fam = Family()
#
# person = Human()
#
# fam + person
# fam - person
# fam - dog
#
#
# (stefan in family)