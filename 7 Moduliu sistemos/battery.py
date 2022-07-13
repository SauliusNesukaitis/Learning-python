#===2 dalis kelios klases
class Battery():
    #An attempt to simulate electric vehicle charging
    def __init__(self,battery_size = 70):
        #Initialize electrical frequency properties
        self.battert_size = battery_size

    def describe_battery(self):
        print("This car has a "+ str(self.battert_size) + " -kwh battery")

    def get_range(self):
        #Print a message describing the battery range
        if self.battert_size == 80:
            range = 260
        elif self.battert_size == 85:
            range = 270

    message = "This kind of car can go approximately " + str(range)
    message +=" miles on a full charge"
    print(message)
