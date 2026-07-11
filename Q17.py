#----<<<<< Restaurant Order & Billing System that can:------>>>>

""" 1.Store a menu of food items, each with name, category, and price
    2.Let the user add items to a "cart" (with quantity)
    3.Show the current cart with subtotal
    4.Remove an item from the cart
    5.Apply a discount code (if valid)
    6.Calculate tax (5%) and generate a final bill
    7.Save completed orders into an order history
    8.Show past order history
    9.Menu-driven loop until user exits"""


menu = []            # list of all food items available (dictionaries)
cart = []            # list of items currently added to the order
order_history = []   # list of completed/past orders
next_item_id = 1     # used to auto-assign IDs to menu items

#function to add a new item.

def add_menu_item(name, category, price):
    global next_item_id

    item = {
        "id": next_item_id,
        "name": name,
        "category": category,
        "price": price

    }
    menu.append(item)
    print(f"Added to menu: {name} ({category}) - Rs.{price}")
    next_item_id +=1

# Function to display the full menu, grouped by category..

def show_menu():
    print("\n -- MENU --")

    if len(menu) == 0:
        print("Menu is empty")
        return
    
    #Get a list of unique categories from the menu.
    categories = []
    for item in menu:
        if item["category"] not in categories:
            categories.append(item["category"])

    # Print items grouped under each category
    for category in categories:
        print(f"\n-- {category} --")
        for item in menu:
            if item["category"] == category:
                print(f"  ID {item['id']}: {item['name']} - Rs.{item['price']}")

# Helper function to find a menu item by its ID..

def find_menu_item(item_id):
    for item in menu:
        if item["id"] == item_id:
            return item
    return None

def add_to_cart(item_id, quantity):
    menu_item = find_menu_item(item_id)

    if menu_item is None:
        print("Menu item not found.")
        return

    if quantity <= 0:
        print("Quantity must be greater than zero.")
        return

    # Check if this item is already in the cart, if so just increase quantity
    for cart_item in cart:
        if cart_item["id"] == item_id:
            cart_item["quantity"] += quantity
            print(f"Updated {menu_item['name']} quantity to {cart_item['quantity']} in cart.")
            return   # important: stop here so it doesn't also add a duplicate below

    # Otherwise, add it as a new entry in the cart
    cart_entry = {
        "id": menu_item["id"],
        "name": menu_item["name"],
        "price": menu_item["price"],
        "quantity": quantity
    }
    cart.append(cart_entry)
    print(f"Added {quantity} x {menu_item['name']} to cart.")

# Function to remove an item from the cart completely..

def remove_from_cart(item_id):
    for cart_item in cart:
        if cart_item["id"] == item_id:
            cart.remove(cart_item)
            print(f"Removed {cart_item['name']} from cart.")
            return

    print("Item not found in cart.")

# Function to calculate the subtotal of all items in the cart..

def calculate_subtotal():
    subtotal = 0
    for cart_item in cart:
        subtotal += cart_item["price"] * cart_item["quantity"]
    return subtotal

# Function to display the current cart with subtotal...

def show_cart():
    print("\n===== YOUR CART =====")

    if len(cart) == 0:
        print("Cart is empty.")
        return

    for cart_item in cart:
        item_total = cart_item["price"] * cart_item["quantity"]
        print(f"ID {cart_item['id']}: {cart_item['name']} x {cart_item['quantity']} = Rs.{item_total}")

    subtotal = calculate_subtotal()
    print(f"\nSubtotal: Rs.{subtotal}")


# Function to check and apply a discount code
# Returns the discount percentage (0 if code is invalid)..

def get_discount_percentage(discount_code):
    valid_codes = {
        "SAVE10": 10,
        "SAVE20": 20,
        "WELCOME5": 5
    }

    discount_code = discount_code.strip().upper()

    if discount_code in valid_codes:
        return valid_codes[discount_code]
    else:
        return 0
    
# Function to generate the final bill
# Applies discount, then adds tax, and prints a clean bill..

def generate_bill(discount_code=""):
    if len(cart) == 0:
        print("Cart is empty. Add items before generating a bill.")
        return

    subtotal = calculate_subtotal()

    # Apply discount if a valid code was given
    discount_percent = get_discount_percentage(discount_code)
    discount_amount = subtotal * (discount_percent / 100)
    amount_after_discount = subtotal - discount_amount

    # Apply tax (5%) on the discounted amount
    tax_rate = 0.05
    tax_amount = amount_after_discount * tax_rate
    final_total = amount_after_discount + tax_amount

    # Print a clean, formatted bill
    print("\n== FINAL BILL ==")
    for cart_item in cart:
        item_total = cart_item["price"] * cart_item["quantity"]
        print(f"{cart_item['name']} x {cart_item['quantity']} = Rs.{item_total}")

    print("---------------------------------")
    print(f"Subtotal: Rs.{subtotal:.2f}")

    if discount_percent > 0:
        print(f"Discount ({discount_percent}%): -Rs.{discount_amount:.2f}")

    print(f"Tax (5%): Rs.{tax_amount:.2f}")
    print(f"TOTAL: Rs.{final_total:.2f}")
    print("------")

    # Save this completed order into order history
    completed_order = {
        "items": cart.copy(),
        "subtotal": subtotal,
        "discount_percent": discount_percent,
        "tax_amount": tax_amount,
        "total": final_total
    }
    order_history.append(completed_order)

    # Clear the cart since the order is now complete
    cart.clear()
    print("Order placed successfully! Cart has been cleared.")

# Function to show all past completed orders..

def show_order_history():
    print("\n===== ORDER HISTORY =====")

    if len(order_history) == 0:
        print("No past orders yet.")
        return

    order_number = 1
    for order in order_history:
        print(f"\n--- Order #{order_number} ---")
        for item in order["items"]:
            print(f"  {item['name']} x {item['quantity']}")
        print(f"  Discount Applied: {order['discount_percent']}%")
        print(f"  Total Paid: Rs.{order['total']:.2f}")
        order_number += 1

# Function to display the menu of options to the user..

def show_options_menu():
    print("\n===== RESTAURANT SYSTEM MENU =====")
    print("1. Show Menu")
    print("2. Add Item to Cart")
    print("3. Remove Item from Cart")
    print("4. Show Cart")
    print("5. Generate Bill (Checkout)")
    print("6. Show Order History")
    print("7. Exit")

# MAIN PROGRAM...

if __name__ == "__main__":

    # sample item..
    add_menu_item("Paneer Tikka", "Starters", 180)
    add_menu_item("Veg Spring Rolls", "Starters", 150)
    add_menu_item("Butter Chicken", "Main Course", 320)
    add_menu_item("Dal Makhani", "Main Course", 220)
    add_menu_item("Garlic Naan", "Breads", 60)
    add_menu_item("Gulab Jamun", "Desserts", 90)
    add_menu_item("Cold Coffee", "Beverages", 120)

    while True:
        show_options_menu()
        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            show_menu()

        elif choice == "2":
            item_id = int(input("Enter item ID to add: "))
            quantity = int(input("Enter quantity: "))
            add_to_cart(item_id, quantity)

        elif choice == "3":
            item_id = int(input("Enter item ID to remove: "))
            remove_from_cart(item_id)

        elif choice == "4":
            show_cart()

        elif choice == "5":
            discount_code = input("Enter discount code (or press Enter to skip): ")
            generate_bill(discount_code)

        elif choice == "6":
            show_order_history()

        elif choice == "7":
            print("Thank you for visiting! Goodbye.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 7.")
