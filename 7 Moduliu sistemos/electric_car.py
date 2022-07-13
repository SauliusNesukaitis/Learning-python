from car import Car
import battery

class ElectricCar(Car):
    #Special features of simulated electric vehicles

    def __init__(self,make,model,year):
        super().__init__(make,model,year)#super is a special function that helps Python associate parent and child classes
        self.battery = battery.Battery() #A new battery class is defined here