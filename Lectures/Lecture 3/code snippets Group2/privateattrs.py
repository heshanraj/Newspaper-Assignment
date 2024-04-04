

class Newspaper ():
    count = 0
    publisher = "IMC"
    def __init__(self, name):
        self.name = name
        Newspaper.count +=1


    def read (self):
        print (self.name)

    @classmethod
    def getNewspaperCount (clz) :
        print (clz)
        return Newspaper.count

n1 = Newspaper ("Times")
n1.read()

n2 = Newspaper ("Times 2")
n2.read ()

print (Newspaper.getNewspaperCount())



Newspaper ("Times")
Newspaper ("Times")
Newspaper ("Times")
Newspaper ("Times")
Newspaper ("Times")
Newspaper ("Times")
Newspaper ("Times")
Newspaper ("Times")


print (Newspaper.count)


