
class Fruit:
    pass

class Apple (Fruit):
    def __init__(self, stem_length):
        self.stem_length = stem_length

class Orange (Fruit):
    def __init__(self, pulp):
        self.pulp = pulp
        self.color = "orange"


def special (list1):
    if "apple" in  list1:
        return Apple (2)

    else:
        return Orange ("tasty")


x = special(["Apple", "Orange"])

attrList = ["pulp", "color"]


if isinstance(x, Apple):
    print (x.stem_length)

if isinstance(x, Orange):
    print((x.pulp))

if hasattr(x, "pulp"):
    for attr in attrList:
        setattr(x, attr, 23)






