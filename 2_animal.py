class Dog:


    def __init__(self, name, age):
        self.name = name
        self.age= age

    def bark(self):
        print("bark")

    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age

d = Dog('tim', 34)
print(d.get_name())
print(d.get_age())


