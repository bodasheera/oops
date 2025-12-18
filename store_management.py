class Item:

    def calculate_total_price(self, x, y):
        # every python method is passed a arguement by default as object/ istance of the class -> self
        # if you create a method without self it will throw error
        return x * y


# create a instance
item1 = Item()

# assign attribute to instances
item1.name = "Phone"
item1.price = 100
item1.quantity = 5

print(type(item1))  # __main__.Item
print(type(item1.name))  # str
print(type(item1.price))  # int
print(type(item1.quantity))  # int
print(item1.calculate_total_price(item1.price, item1.quantity))

random_str = "aaa"
print(random_str.upper())  # upper is method of the class 'str'


# create a instance
item2 = Item()

# assign attribute to instances
item2.name = "Laptop"
item2.price = 1000
item2.quantity = 3
print(item2.calculate_total_price(item2.price, item2.quantity))

# as of now we are hardcoding the attributes after creating object of the class

# __init__ it is called a constructor -> we can make sure we are initializing the attributes as soon as we
# create the instance of the class

# __method__ these are called magic methods


class Items:
    def __init__(self, name: str, price: float, quantity=0) -> None:

        # Run validations to the recieved arguements
        assert price >= 0, f"price {price} is not greater than 0"
        assert quantity >= 0, f"quantity {quantity} is not greater than 0"


        # assign to self object
        print(f"An instance created {name}")
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        # every python method is passed a arguement 
        # by default as object/ istance of the class -> self
        # if you create a method without self it will throw error
        return self.price * self.quantity


item3 = Items("Phone", 100)
item4 = Items("Laptop", 1000, 4)

print(item3.name)
print(item3.price)
print(item3.quantity)

print(item4.name)
print(item4.price)
print(item4.quantity)

# __init__ -> you should always take care of the attributes that you want to assign to an object inside _init__

# we can also make mandatory and non mandatory params
# give default value to non mandatory params in __init__ -> quanity = 0

# we can assign attributes to instances individually
# for eg -> for laptop we nned attr to tell if numpad or not
# we dont need that attr for phone

item4.has_numpad = False  # only for laptop

print(item3.calculate_total_price())
print(item4.calculate_total_price())


# item5 = Items("Phone", "100", 2)
# print(item5.calculate_total_price())  # 100100

# we need to validate data types -> use typings in parameters 
# name -> str, price -> float , qty -> int 

# item6 = Items(1, "100", 2)


# how to make sure price and quantity are positive 
# use assert -> it will not show any message if condition is true
# it will throw error if condition is false
# assert condition

item7 = Items("Bag",-1,2)

# you can also add your own error message for assert 
# assert codition , message 