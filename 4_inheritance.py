# class Dog:

#     def __init__(self, name , age):
#         self.name = name
#         self.age =  age
    
#     def speak(self):
#         print("Bark")


# class Dog:

#     def __init__(self, name , age):
#         self.name = name
#         self.age =  age
    
#     def speak(self):
#         print("Meow")


class Pet:
    def __init__(self, name , age):
        self.name = name
        self.age =  age

    def show(self):
        print(f"I am {self.name} and {self.age} years old")

    def speak(self):
        print("I dont know what I say")


class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color


    def speak(self):
        print("Meow")

    def show(self):
        print(f"I am {self.name} and {self.age} years old and color {self.color}")

class Dog(Pet):
    def speak(self):
        print("Bark")


p = Pet("Tim", 19)
p.show()
p.speak()

c = Cat("Bill", 34, "pink")
c.show()
c.speak()

d = Dog("Jill", 25)
d.show()
d.speak()

