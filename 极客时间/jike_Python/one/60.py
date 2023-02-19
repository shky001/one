class WaterMixin(object):

    def __init__(self):
        self.temperature = None
        self.volume = 0

    def addWater(self, nums, temp):
        self.volume = nums
        if temp == "cold":
            self.temperature = "cold"           
        elif temp == "hot":
            self.temperature = "hot"
        
        return f"add {self.temperature} water {self.volume} ML "

class CoffeeMixin(object):

    def __init__(self):
        self.numbers = 0


    def addCoffee(self, nums):
        self.numbers = nums
        
        return f"add coffee {self.numbers} part"

class MilkMixin(object):
    def __init__(self):
        self.temperature = None
        self.volume = 0

    def addMilk(self, nums, temp):
        self.volume = nums
        if temp == "cold":
            self.temperature = "cold"       
        elif temp == "hot":
            self.temperature = "hot"
        
        return f"add {self.temperature} milk {self.volume} ML "

class Coffee(WaterMixin, CoffeeMixin, MilkMixin):
    def  __init__(self, water=-1, water_temp="cold", milk=-1, milk_temp="cold", coffee=1):
        self.water = water
        self.water_temp = water_temp
        self.milk = milk
        self.milk_temp = milk_temp
        self.coffee = coffee
        self.prescription = []

        if int(self.water) > 0:
            self.prescription.append(super().addWater(self.water, self.water_temp))
        
        if int(self.milk) > 0:
            self.prescription.append(super().addMilk(self.milk, self.milk_temp))
        
        if int(self.coffee) > 0:
            self.prescription.append(super().addCoffee(self.coffee))

    def showPrescription(self):
        for i in self.prescription:
            print(i)

americano_ice = Coffee(milk=150,milk_temp="hot",coffee=1)

americano_ice.showPrescription()