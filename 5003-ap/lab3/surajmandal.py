"""
Application Name: surajmandal.py
Author/Developer: Suraj Mandal
Date: 2023-01-24

This program is a simple inventory management system that allows the user to add items to the inventory, display the inventory items, search for an item by serial code and end the application.

There are 4 main functions in this program:
- add_item() - This function allows the user to add items to the inventory. It takes the items dictionary as an argument and returns the updated dictionary.
- display_items() - This function displays the items in the inventory. It takes the items dictionary as an argument and returns nothing.
- search_items() - This function allows the user to search for an item by serial code. It takes the items
dictionary as an argument and returns True if the item is found and False if the item is not found.
- main() - This is the main function of the program. It calls the menu_prompt() function to display the main menu and calls the appropriate function based on the user's choice.

There are 2 helper functions in this program:
main_prompt() - This function displays the main menu and returns the user's choice.
add_item_prompt() - This function displays the prompts to add an item to the inventory and returns the user's input.
"""

import os
from pprint import pp


# Main prompt at the start of the applciation
def menu_menu_prompt():
    selection = input(
        """
        |--------------------------------------------------|
        | Welcome to the Inventory Management System       |
        |--------------------------------------------------|
        | 1. Add Item in Inventory                         |
        | 2. Display inventory items                       |
        | 3. Search inventory item by Serial code          |
        | 4. End application                               |
        |--------------------------------------------------|\n\n
        """
    )
    return selection


def add_item_prompt():
    name = input("\tEnter name of the item: ")
    serial_code = input("\tEnter serial code of the item: ")
    quantity = int(input("\tEnter quantity of the item: "))
    ppu = float(input("\tEnter price per unit of the item: "))
    return name, serial_code, quantity, ppu


# Main functions
def add_item(items):
    name, serial_code, quantity, ppu = add_item_prompt()
    if serial_code in items:
        items[serial_code]["quantity"] += quantity
        if ppu >= items[serial_code]["ppu"]:
            items[serial_code]["ppu"] = ppu
    else:
        items[serial_code] = {
            "name": name,
            "quantity": quantity,
            "ppu": ppu,
        }
    print(f"\n\t{name} has been added to the record ")
    return items


def display_items(items):
    if not items:
        print("\tThere are no items in inventory...")
        return
    print("\n")
    print("-" * 110)
    print("%110s" % ("Suraj Mandal"))
    print("%110s" % ("N01537188\n"))
    print("-" * 110)
    print("%20s%30s%30s%30s" % ("Name", "Serial Code", "Quantity", "Price per unit"))
    for item in items:
        print(
            "%20s%30s%30s%30s"
            % (
                items[item]["name"],
                item,
                items[item]["quantity"],
                "$" + str(items[item]["ppu"]),
            )
        )
    print("-" * 110)
    print("\n")


def search_items(items):
    if len(items) == 0:
        print("\tNo items in inventory...")
        return
    item_id = input("\tEnter Item ID: ")
    for item in items:
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
                    items[item]["name"],
                    item,
                    items[item]["quantity"],
                    "$" + str(items[item]["ppu"]),
                )
            )
            return True
    print("\tItem not found..")
    return False


def main():
    items = {}
    while True:
        choice = menu_menu_prompt()
        if choice.isdigit() is False:
            print("\tInvalid input, please enter a number")
            continue
        elif int(choice) == 1:
            items = add_item(items)
            continue
        elif int(choice) == 2:
            display_items(items)
            continue
        elif int(choice) == 3:
            search_items(items)
            continue
        elif int(choice) == 4:
            break
        else:
            print("\tEnter a valid choice...")
            continue


if __name__ == "__main__":
    # os.system("clear")
    main()
