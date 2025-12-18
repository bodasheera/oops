# Inheritance 

# creating new classes based on existing classes 

# A car is a vehicle 
# A bike is a vehicle 

class Vehicle:

    def __init__(self, brand , model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        print("Vehicle started")

    def stop(self):
        print("Vehicle stopped")

        

class Bike(Vehicle):

    def __init__(self, brand , model , year, no_of_wheels):
        super().__init__(brand,model,year)
        self.no_of_wheels = no_of_wheels

    def __str__(self):
        return (f"{self.brand} {self.model} {self.year} {self.no_of_wheels}")

    def start_bike(self):
        print("Bike started")

    def stop_bike(self):
        print("Bike stopped")

class Car(Vehicle):

    def __init__(self, brand , model , year, no_of_doors , no_of_wheels):
        super().__init__(brand,model,year)
        self.no_of_doors = no_of_doors
        self.no_of_wheels = no_of_wheels

    def __str__(self):
        return (f"{self.brand} {self.model} {self.year} {self.no_of_doors} {self.no_of_wheels}")

    def start_car(self):
        print("Car started")

    def stop_car(self):
        print("Car stopped")
    
car = Car("Ford", "Focus", 2008 , 5 , 4)
bike = Bike("Honda", "Scoopy", 2018 , 2)

print(car)
print(bike)

car.start_car()
bike.start_bike()

print(car.__dict__)