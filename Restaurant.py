import Order

class Restaurant:
    def __init__(self,name):
        self.name = name
        self.menu = []    # List of MenuItem Objects
        self.orders = []  # List of Order Objects 

#add_dish(dish)
    def add_dish(self,dish):
        self.menu.append(dish)     # Adds a new  to the restaurants menu list 

#remove_dish(dish_name)
    def remove_dish(self,dish_name):
        for dish in self.menu:
            if dish.name == dish_name:
                self.menu.remove(dish)
                return True 
        return False

# display_menu()
    def display_menu(self):
        print("\n---------------TASTE THE FOOD-----------------" )
        print("\n BESIDE GANDHI BOMMA STREET , DHANAVAI PETA,")
        print("\n  RAJAMAHENDRAVARAM, ANDHRA PRADESH, 533103")
        print("\n---------------------Menu---------------------")
        for dish in self.menu:
            print(dish)   # prints all dishes in menu

# taking order
    def take_order(self):
        order = Order.Order()
        while True:
            self.display_menu()
            choice = input("Enter dish name to add :").lower()    # Taking order from customer 
            if choice.lower() == 'done':      # After succesfully completion to take order 
                break
            found = False
            for dish in self.menu:
                if dish.name.lower() == choice.lower() :
                    order.add_item(dish)
                    print(f"Added {dish.name} to order.")
                    found = True
                    break
            if not found:
                print("Dish not found !")
        if order.items:
            self.orders.append(order)
            print("\nOrder placed successifully!")
            order.display_order()

    def generate_bill(self,order_index):
        if 0 <= order_index < len(self.orders):
            print("\n---------------------Bill----------------------")
            self.orders[order_index].display_order()
        else:
            print("Invalid order index.")