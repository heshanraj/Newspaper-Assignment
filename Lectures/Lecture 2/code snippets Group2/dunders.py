class Person :
    def __init__(self, name,id   ):
        self.name = name
        self.id = id
        self.__password = "hyppy"

    def __eq__(self, o1):
        return self.id == o1.id and self.name == o1.name

    def __repr__(self):
        return self.name


class University:
    def __init__(self):
        self.students = []
    def __len__(self):
        return len (self.students)

    def addStudent (self, st):
        if isinstance(st, Person):
            self.students.append(st)


class Length :
    def __init__(self, dimension, unit):
        self.dimension = dimension
        self.unit = unit

    def __add__(self, l1 ):
        if self.unit =="m":
            self.unit ="cm"
            self.dimension = self.dimension*100
        if l1.unit == "m":
            l1.unit = "cm"
            l1.dimension = l1.dimension * 100
        result = (self.dimension+l1.dimension, "cm")

        return Length (result[0], result[1])

    def __str__(self):
        return str (self.dimension)  + " " + self.unit



x1 = Length (100, "m")
x2 = Length(200 , "cm")

print (x1+x2) # 2.2 m




p1 = Person ("Sam", 312)
p2 = Person ("Sam3", 312 )
print (p1._Person__password)
print (p1.__dict__)

p1.name = "George"



imc = University()
imc.students.append(p1)
imc.students.append(p2)
imc.addStudent(Length(12, "cm"))
imc.students.append (Length(12, "cm"))


print (imc.__dict__)





print (id(p1))
print (id(p2))

print (p1==p2) # p1.__eq__(p2)

print (len (imc))

