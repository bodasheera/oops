class Microvawe:
    
    def __init__(self, brand : str, power_rating : str) -> None :
        self.brand = brand
        self.power_rating = power_rating
        self.turned_on: bool = False

    def turn_on(self) -> None:
        if self.turned_on:
            print(f"Microvawe {self.brand} is already turned on")
        else:
            self.turned_on = True
            print(f"Microvawe {self.brand} is now turned on")

    def turn_off(self) -> None:
        if self.turned_on:
            self.turned_on = False
            print(f"Microvawe {self.brand} is now turned off")
        else:
            print(f"Microvawe {self.brand} is already turned off")

    def run(self, seconds: int ) -> None:
        if self.turned_on:
            print(f"Running  {self.brand} for {seconds} seconds")
        else:
            print("A mystical force whispers: Turn on your microvawe first")


    # dunder method 
    def __add__(self, other):
        return (f"{self.brand} and {other.brand}")
    
    # dunder method 
    def __mul__(self, other):
        return (f"{self.brand} * {other.brand}")
    
    def __str__(self) -> str:
        return f"{self.brand} and {self.power_rating}"
    
    def __repr__(self):
        return f"Microvawe(brand = '{self.brand}', power_rating = '{self.power_rating}')"
        

smeg: Microvawe = Microvawe( brand='Smeg',power_rating='B')

# print(smeg.brand)
# print(smeg.power_rating)

bosch: Microvawe = Microvawe('Bosch', 'C')

# print(bosch.brand)
# print(bosch.power_rating)

# smeg.turn_on()
# smeg.turn_on()
# smeg.run(30)
# smeg.turn_off()
# smeg.run(10)

print(smeg + bosch)
print(smeg * bosch)
print(smeg)

print(repr(smeg))