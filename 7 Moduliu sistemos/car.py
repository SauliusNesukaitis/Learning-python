#====1 dalis - 1 klase

class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.orometer_reading = 0

    def get_description(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name

    def read_odometer(self):
        print("This car has "+ str(self.orometer_reading) + " miles on it")

    def update_orometer(self,miles):
        if miles >= self.orometer_reading:
            self.orometer_reading = miles
        else:
            print("You can'troll back an odometer")

    def increase(self,miles):
        self.orometer_reading +=miles

