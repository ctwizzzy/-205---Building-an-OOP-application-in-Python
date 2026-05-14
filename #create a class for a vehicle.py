#create a class for a vehicle
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_info(self):
        return f"{self.year} {self.make} {self.model}"

#create a subclass for a car that inherits from the
class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year) 
        self.num_doors = num_doors

class ElectricCar(Car):
    def __init__(self, make, model, year, num_doors, battery_size):
        super().__init__(make, model, year, num_doors)
        self.battery_size = battery_size
    
    def get_info(self):
        base = super().get_info()
        return f"{base} ({self.num_doors} doors, {self.battery_size} kWh battery)"

ev = ElectricCar("BYD", "Seal", 2025, 4, 82)
print(ev.get_info())
