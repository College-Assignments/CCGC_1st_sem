"""
Application Name: surajmandal.py
Author/Developer: Suraj Mandal
Date: 2023-02-06

This is a simple inventory management application using  file handling.

The main functions are as follows:
add_item() - Add an item to the inventory
display_items() - Display all the items in the inventory
search_items() - Search for an item by serial code
sales_invoice() - Generate a sales invoice
end_application() - Gracefully exit the application

The utility functions are as follows:
read_file() - Read the file and return a list of items
write_file() - Write the data to the file

The prompt functions are as follows:
menu_prompt() - Display the main menu and take user input

"""

import json

# This is just for internal configuration
# I like to do it this way
config = {
    "filename": "inventory.txt",
}

# -----------------|
#  Prompt functions|
# -----------------|
def menu_prompt():
    # Display the main menu and take user input
    print(
        """
        |---------------------------------------------------------------|
        |         Welcome to the Inventory Management System            |
        |---------------------------------------------------------------|
        | 1. Add inventory items                                        |
        | 2. Display all inventory items                                |
        | 3. Search an item                                             |
        | 4. Sales invoice    ------- To be implimented in the next lab |
        | 5. End application                                            |
        |---------------------------------------------------------------|
        """
    )
    try:
        return input("Enter your choice: ")
    except ValueError:
        print("Invalid input. Please enter a number.")
        menu_prompt()


def add_item_prompt():
    # Menu prompt to add an item to the inventory
    name = input("\tEnter inventory Item Name: ")
    serial_code = input("\tEnter inventory item code: ")
    quantity = int(input("\tEnter inventory item quantity: "))
    ppu = float(input("\tEnter inventory item price per unit: "))
    return name, serial_code, quantity, ppu


# ------------------|
# Utility functions |
# ------------------|
def read_file(filename=config["filename"]):
    # Read the file and return a list of items
    try:
        with open(filename, "r") as file:
            file = file.readlines()
            dct = json.loads(file[0])
            return dct
    except OSError as e:
        print(f"{e}")


def write_file(data, filename=config["filename"]):
    # Write the data to the file
    try:
        with open(filename, "w+") as file:
            clean = json.dumps(data)
            file.write(clean)
            return True
    except OSError as e:
        print(f"{e}")
        return False


# --------------------------------|
# Main functions of the program   |
# --------------------------------|
def add_item():
    # Add an item to the inventory
    data = read_file()
    name, serial_code, quantity, ppu = add_item_prompt()
    data[serial_code] = {
        "name": name,
        "quantity": quantity,
        "ppu": ppu,
    }
    write_file(data)


def display_items():
    # Display
    data = read_file()
    if data.__len__ == 0:
        print("Inventory does not have any item to display...")
        return

    print("\n")
    print("-" * 110)
    print("%110s" % ("Suraj Mandal"))
    print("%110s" % ("N01537188\n"))
    print("-" * 110)
    print("%20s%30s%30s%30s" % ("Name", "Serial Code", "Quantity", "Price per unit"))
    for item in data:
        print(
            "%20s%30s%30s%30s"
            % (
                data[item]["name"],
                item,
                data[item]["quantity"],
                "$" + str(data[item]["ppu"]),
            )
        )
    print("-" * 110)
    print("\n")


def search_items():
    # Search for an item by serial code
    data = read_file()
    if data.__len__() == 0:
        print("Inventory does not have any item to search...")
        return

    item_id = input("Enter serial code of the item: ")
    for item in data:
        if item == item_id:
            print("\n")
            print("-" * 110)
            print("%110s" % ("Suraj Mandal"))
            print("%110s" % ("N01537188"))
            print("\n")
            print("-" * 110)
            print(
                "%20s%30s%30s%30s"
                % ("Name", "Serial Code", "Quantity", "Price per unit")
            )
            print(
                "%20s%30s%30s%30s"
                % (
                    data[item]["name"],
                    item,
                    data[item]["quantity"],
                    "$" + str(data[item]["ppu"]),
                )
            )
            print("-" * 110)
            return True
    print("\tItem not found..")
    return False


def sales_invoice():
    # Sales invoice function, to be implimented in the next lab
    pass


def end_application():
    # Gracefully exit the application
    exit()


# ------------------------------------------------------|
# Main function, this is the entry point of the program |
# ------------------------------------------------------|
def main():
    while True:
        choice = menu_prompt()
        if choice.isdigit() is False:
            print("\tInvalid input, please enter a number")
            continue
        elif int(choice) == 1:
            add_item()
            continue
        elif int(choice) == 2:
            display_items()
            continue
        elif int(choice) == 3:
            search_items()
            continue
        elif int(choice) == 4:
            sales_invoice()
            continue
        elif int(choice) == 5:
            exit()
        else:
            print("\tEnter a valid choice...")
            continue


if __name__ == "__main__":
    # os.system("clear")
    main()
