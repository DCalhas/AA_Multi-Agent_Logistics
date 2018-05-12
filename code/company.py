import truck
from random import randint

class Company:

    def __init__(self, id, budget, local):
        self.id = id
        self.trucks = []
        self.profit = budget
        self.local = local

    def getId(self):
        return self.id

    def addTruck(self, truck):
        self.trucks.append(truck)

    def delTruck(self, truck):
        self.trucks.remove(truck)

    def getTrucks(self):
        return self.trucks

    def getProfit(self):
        return self.profit

    def setProfit(self, budget):
        self.profit = budget

    def getLocal(self):
        return self.local

    def setLocal(self, local):
        self.local = local

    def evaluateOffer(self, offer):
        start = offer[0]
        finish = offer[1]
        amount = offer[2]
        money = offer[3]

    def getUtility(self, distance):
        #put 0.2 after, if we organize the trucks with the products
        return distance * 1.2

    def buyTrucks(self, policy):

    #[1,2,3,4] 1: curto pessoas, 2: curto mercadorias, 3: longo pessoas, 4: longo mercadorias
        if policy == 1:
            x = truck.FiftyBus(randint(0, 100), self, 5)
        elif policy == 2:
            x = truck.FiftyTruck(randint(0, 100), self, 7)
        elif policy == 3:
            x = truck.SeventyBus(randint(0, 100), self, 10)
        elif policy == 4:
            x = truck.SeventyTruck(randint(0, 100), self, 14)

        self.profit -= x.getPrice()
        self.addTruck(x)