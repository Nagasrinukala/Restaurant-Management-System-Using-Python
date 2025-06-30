# class MenuItems defines the class.
# This class stores of each dish(self,name and optional description).
class MenuItem:
    def __init__(self,name,price,description=" "):
            # __init__ is the constructor method that initializes the object.
        self.name = name 
        self.price = price 
        self.description = description 

    def __str__(self):
            # __str__ defines how the object should be represented as a string when printed.
        return f"{self.name}: ₹{self.price} - {self.description}"