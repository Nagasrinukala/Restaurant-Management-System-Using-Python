# __init__(self)
# Class Order defines the class.
'''' This class manages a single customer order , including :
     Adding / removing items 
     Calculatin the total bill'''
class Order:
    def __init__(self):            # __init__ is the constructor method that initializes the object.
        self.items = []         # [] empty list stores the MenuItem objects (items).


# ADD ITEM TO THE LIST 
    def add_item(self,item):
        self.items.append(item) # Adds the item to the list 


# REMOVE ITEM FROM THE LIST 
    def remove_item(self,item_name):
        for item in self.items:
            if item_name == item_name: # checks if item exists
                self.items.remove(item)
                return True      # Item removed 
        return False  # Item not found


# CALCULATE TOTAL(SELF)
    def calculate_total(self):
        return sum(item.price for item in self.items)     # Sums all prices


    def display_order(self):
        if not self.items:
            print("No items in the order.")
            return
        print("\n----------------- YOUR ORDER ------------------")
        for item in self.items:
            print(item)   # uses MenuItem __str__ method
        print(f"Total Bill Amount: ₹{self.calculate_total()}")
    