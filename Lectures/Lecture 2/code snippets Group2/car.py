
class Car:
    def __init__(self, numberplate):
        self.model = None
        self.Year = None
        self.numberplate = numberplate
        self.owner = None
    def __str__(self):
        return self.numberplate + " and the owner is " + str (self.owner)

class Customer:
    def __init__(self, name):
        self.cars = []
        self.ID = None
        self.name = name
        self.address = None
        self.agent = None
        self.insuranceCompany = None
    def addcar (self, car):
        self.cars.append(car)

    def setagent (self, agent) :
        self.agent = agent

    def __str__(self):
        return self.name

class Agent:
    def __init__(self, name ):
        self.ID = None
        self.name = name
        self.address = None
        self. customers = []
        self.insuranceCompany = None

class CarInsuranceCompany:
    def __init__(self, name ):
        self.agents = []
        self.customers = []
        self. name = name


    def addagent (self, agent):
        self.agents.append(agent )

    def addcustomer (self, customer):
        self.customers.append(customer)


car1 = Car ("W 12313 F")
p1= Customer ("Samuel Jackson")
p1.addcar(car1)
car1.owner = p1

a1 = Agent ("Agent 1")


p1.setagent (a1)


company = CarInsuranceCompany ("We ensure your safety")
company.addagent (a1)
company.addcustomer (p1)

print (car1.__dict__)
print (p1)
print (a1)

