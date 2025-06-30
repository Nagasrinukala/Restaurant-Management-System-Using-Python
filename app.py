import MenuItem
import Order
import Restaurant

item_1 = MenuItem.MenuItem("Biryani",250,"FRY PIECE") 
print(item_1)

# Create MenuItems
item1 = MenuItem.MenuItem("Chicken Biryani",250,"FRY PIECE")
item2 = MenuItem.MenuItem("Mutton Biryani",550,"EXTRA PIECES") 
item3 = MenuItem.MenuItem("Noodles",175,"CHICKEN")
item4 = MenuItem.MenuItem("Fried rice",130,"VEG")
print(item1)
print(item2)
print(item3)
print(item4)

# Create an Order and add items 
order = Order.Order()
order.add_item(item1)
order.add_item(item2)
# Display the Order 
order.display_order()

# Remove an item and display again
order.remove_item(item1)
# Display the Order 
order.display_order()

if __name__ == "__main__":
    my_restaurant = Restaurant.Restaurant("Mehfill")

    my_restaurant.add_dish(MenuItem.MenuItem("Chicken Biryani",250,"FRY PIECE"))
    my_restaurant.add_dish(MenuItem.MenuItem("Mutton Biryani",550,"EXTRA PIECES"))
    my_restaurant.add_dish(MenuItem.MenuItem("Mutton Mandi",670,"KAAZU MANDI"))
    my_restaurant.add_dish(MenuItem.MenuItem("Chicken Dum Biryani",250,"DOUBLE MASALA"))
    my_restaurant.add_dish(MenuItem.MenuItem("Chicken pulav",185,"EXTRA PIECES"))
    my_restaurant.add_dish(MenuItem.MenuItem("Bahubali Biryani",1250,"UNLIMITED"))
    my_restaurant.add_dish(MenuItem.MenuItem("Noodles",175,"CHICKEN"))
    my_restaurant.add_dish(MenuItem.MenuItem("Veg Noodles",150,"EXTRA MASSALA"))
    my_restaurant.add_dish(MenuItem.MenuItem("Fried rice",130,"VEG"))
    my_restaurant.add_dish(MenuItem.MenuItem("Veg Fried Rice",145,"VEG"))
    

    print("\n Taking a new Order")
    my_restaurant.take_order()

    print("\n Generating bill")
    my_restaurant.generate_bill(0)