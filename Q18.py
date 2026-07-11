#----------<<<<<<< HOTEL ROOM BOOKING SYSTEM... ---------------->>>>>>>>

""" Features:
 1. Store rooms with type, price, and status
 2. Book a room for a guest
 3. Check out a room and generate bill
 4. Search available rooms by type
 5. Show currently booked rooms
 6. Calculate total revenue
 7. Cancel a booking.. """

rooms = []           # list of all rooms...
total_revenue = 0    # tracks total money earned from checkout...s



# Function to add a new room to the hotel..

def add_room(room_number, room_type, price_per_night):
    room = {
        "room_number": room_number,
        "type": room_type,
        "price_per_night": price_per_night,
        "status": "available",   
        "guest_name": None,
        "check_in_day": None,
        "nights": None
    }
    rooms.append(room)
    print(f"Room {room_number} ({room_type}) added at Rs.{price_per_night}/night")


# Helper function to find a room by its room number...

def find_room(room_number):
    for room in rooms:
        if room["room_number"] == room_number:
            return room
    return None


# Function to display all rooms with their status..

def show_all_rooms():
    print("\n---- ALL ROOMS ----")

    if len(rooms) == 0:
        print("No rooms added yet.")
        return

    for room in rooms:
        if room["status"] == "available":
            print(f"Room {room['room_number']} ({room['type']}) - Rs.{room['price_per_night']}/night - AVAILABLE")
        else:
            print(f"Room {room['room_number']} ({room['type']}) - Rs.{room['price_per_night']}/night - "
                  f"BOOKED by {room['guest_name']}")


# Function to search available rooms by type..

def search_available_rooms(room_type):
    print(f"\n---- AVAILABLE {room_type.upper()} ROOMS ----")
    found_any = False

    for room in rooms:
        if room["type"].lower() == room_type.lower() and room["status"] == "available":
            print(f"Room {room['room_number']} - Rs.{room['price_per_night']}/night")
            found_any = True

    if not found_any:
        print(f"No available rooms of type '{room_type}' right now.")

# Function to book a room for a guest..

def book_room(room_number, guest_name, check_in_day, nights):
    room = find_room(room_number)

    if room is None:
        print("Room not found.")
        return

    if room["status"] == "booked":
        print(f"Room {room_number} is already booked.")
        return

    if nights <= 0:
        print("Number of nights must be greater than zero.")
        return

    # Mark the room as booked and store guest details
    room["status"] = "booked"
    room["guest_name"] = guest_name
    room["check_in_day"] = check_in_day
    room["nights"] = nights

    total_cost = room["price_per_night"] * nights
    print(f"Room {room_number} booked for {guest_name} starting day {check_in_day} "
          f"for {nights} night(s). Estimated bill: Rs.{total_cost}")

# Function to check out a guest and generate the final bill..

def check_out(room_number):
    global total_revenue

    room = find_room(room_number)

    if room is None:
        print("Room not found.")
        return

    if room["status"] == "available":
        print(f"Room {room_number} is not currently booked.")
        return

    # Calculate the bill based on nights stayed
    bill_amount = room["price_per_night"] * room["nights"]
    total_revenue += bill_amount

    print(f"\n----- CHECKOUT BILL -----")
    print(f"Guest: {room['guest_name']}")
    print(f"Room: {room['room_number']} ({room['type']})")
    print(f"Nights stayed: {room['nights']}")
    print(f"Total Bill: Rs.{bill_amount}")
    print("-----")

    # Reset the room back to available for the next guest
    room["status"] = "available"
    room["guest_name"] = None
    room["check_in_day"] = None
    room["nights"] = None

    print(f"Room {room_number} is now available again.")

# Function to cancel a booking (before checkout)...

def cancel_booking(room_number):
    room = find_room(room_number)

    if room is None:
        print("Room not found.")
        return

    if room["status"] == "available":
        print(f"Room {room_number} has no active booking to cancel.")
        return

    print(f"Booking for {room['guest_name']} in Room {room_number} has been cancelled.")

    # Reset room back to available, no charge since guest never checked out
    room["status"] = "available"
    room["guest_name"] = None
    room["check_in_day"] = None
    room["nights"] = None

# Function to show only currently booked rooms...

def show_booked_rooms():
    print("\n--- CURRENTLY BOOKED ROOMS -----")
    found_any = False

    for room in rooms:
        if room["status"] == "booked":
            print(f"Room {room['room_number']} ({room['type']}) - Guest: {room['guest_name']} - "
                  f"Check-in Day: {room['check_in_day']} - Nights: {room['nights']}")
            found_any = True

    if not found_any:
        print("No rooms are currently booked.")

# Function to show total revenue earned so far..

def show_total_revenue():
    print(f"\nTotal Revenue Earned So Far: Rs.{total_revenue}")


# Function to display the menu of options..

def show_options_menu():
    print("\n---- HOTEL BOOKING SYSTEM MENU ----")
    print("1. Show All Rooms")
    print("2. Search Available Rooms by Type")
    print("3. Book a Room")
    print("4. Check Out a Room")
    print("5. Cancel a Booking")
    print("6. Show Currently Booked Rooms")
    print("7. Show Total Revenue")
    print("8. Exit")

# MAIN PROGRAM..

if __name__ == "__main__":

    # Pre-populate some sample rooms
    add_room(101, "Single", 1500)
    add_room(102, "Single", 1500)
    add_room(201, "Double", 2500)
    add_room(202, "Double", 2500)
    add_room(301, "Suite", 5000)

    while True:
        show_options_menu()
        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            show_all_rooms()

        elif choice == "2":
            room_type = input("Enter room type (Single/Double/Suite): ")
            search_available_rooms(room_type)

        elif choice == "3":
            room_number = int(input("Enter room number to book: "))
            guest_name = input("Enter guest name: ")
            check_in_day = int(input("Enter check-in day (e.g., 1, 2, 3...): "))
            nights = int(input("Enter number of nights: "))
            book_room(room_number, guest_name, check_in_day, nights)

        elif choice == "4":
            room_number = int(input("Enter room number to check out: "))
            check_out(room_number)

        elif choice == "5":
            room_number = int(input("Enter room number to cancel booking: "))
            cancel_booking(room_number)

        elif choice == "6":
            show_booked_rooms()

        elif choice == "7":
            show_total_revenue()

        elif choice == "8":
            print("Thank you for using the Hotel Booking System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 8.")