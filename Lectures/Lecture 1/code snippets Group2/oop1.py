
class Dog:


    def bark (self):
        print (self.name, "is barking and is ", self.age , "years old ")
    def __init__(self, nameX, colorX):
        #print (self)
        #print ("Hello", name )
        self.name = nameX
        self.color = colorX
        self.age = 10
        self.bark()


lassie = Dog ("Lassie", "black" )
print (lassie.color)
lassie.bark()

lassie.name = "Junky"
lassie.bark ()

rocky = Dog ("Rocky", "white")

carly = Dog ("Carli", "red")
print (carly.color)




class Person:
    pass

deepak = Person ()
sam = Person ()