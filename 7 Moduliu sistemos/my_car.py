
from car import Car
from electric_car import ElectricCar  #Import the Car class in the Car module


my_new_car = Car("audi","Q5", 2014)
print(my_new_car.get_description())

my_new_car.orometer_reading = 25
my_new_car.read_odometer()

my_car = ElectricCar("tesa","model's",2019)
print(my_car.get_description())
my_car.battery.describe_battery()
my_car.battery.get_range()

my_beetle = Car("Volkswagen",'beetle',2019)
print(my_beetle.get_description())

my_tesla = ElectricCar('tesla','roadster',2019)
print(my_tesla.get_description())



# from module_name import klase
# REKOMENDUOINA
# from module_name.class_name  # Tokiu būdu naudojamos klasės nėra nurodytos failo pradžioje, tačiau jūs aiškiai žinote, kur programoje yra importuojami moduliai, ir galite išvengti konflikto tarp importuojamų klasių ir pavadinimų