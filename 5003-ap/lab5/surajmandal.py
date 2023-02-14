"""
Application Name: surajmandal.py
Author/Developer: Suraj Mandal
Date: 2023-02-14

This is a simple inventory management application using  file handling.

The structure of the app is

The prompt functions are as follows:
menu_prompt() - Display the main menu and take user input
add_item_prompt() - Menu prompt to add an item to the inventory
sales_invoice_prompt() - Menu prompt to add an item to the sales invoice

The main functions are as follows:
add_item() - Add an item to the inventory
display_items() - Display all the items in the inventory
search_items() - Search for an item by serial code
sales_invoice() - Generate a sales invoice
end_application() - Gracefully exit the application

The utility functions are as follows:
read_file() - Read the file and return a list of items
write_file() - Write the data to the file`
send_mail() - Send inventory report to the user

"""

from datetime import datetime
import json
import os

from dotenv import load_dotenv

# This is just for internal configuration
# I like to do it this way
config = {
    "inventory": "inventory.txt",
    "invoice": "invoice.txt",
    # Please paste your password in the .env file
    "mailfrom": "cruelplatypus67@gmail.com",
    "mailto": "me@surajmandal.in",
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
        | 4. Sales invoice                                              |
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


def sales_invoice_prompt():
    # Menu prompt to add an item to the sales invoice
    serial_code = input("\tEnter inventory item code: ")
    quantity = int(input("\tEnter inventory item quantity: "))
    return serial_code, quantity


# ------------------|
# Utility functions |
# ------------------|
def read_file(default=[], file_name=config["inventory"]):
    # Read the file and return a list of items
    try:
        with open(file_name, "r") as file:
            file = file.readlines()
            if len(file) == 0:
                return default
            else:
                dct = json.loads(file[0])
            return dct
    except Exception as e:
        print(f"{e}")
        return False


def write_file(data, file_name=config["inventory"]):
    # Write the data to the file
    try:
        with open(file_name, "w+") as file:
            clean = json.dumps(data)
            file.write(clean)
            return True
    except Exception as e:
        print(f"{e}")
        return False


def send_mail():
    # Send inventory report to the user
    data = read_file(file_name=config["invoice"])
    email_invoice_list = ""
    for item in data["list"]:
        email_invoice_list += "%22s%22s%22s%22s%22s\n" % (
            item["name"],
            item["name"],
            item["serial_code"],
            item["quantity"],
            item["ppu"],
        )
    email_text = f"""\n
    {"-" * 110}
    {("%110s" % ("Suraj Mandal"))}
    {"%110s" % ("N01537188")}\n
    {("-" * 110)}
    {("%22s%22s%22s%22s%22s" % ("Sale Time", "Name", "ID","Quantity", "Price Per Unit"))}
    {email_invoice_list}
    {("-" * 110)}
    \n
    """
    email = {
        "data": email_text,
        "password": os.environ["APP_PASSWORD"],
        "from": config["mailfrom"],
        "to": config["mailto"],
    }

    import ssl
    import smtplib

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(email["from"], email["password"])
        smtp.sendmail(email["from"], email["to"], email["data"])

    return True


def gen_invoice(selected_item, serial_code, quantity):
    # Not necessary but I like to keep it separate
    return {
        "time": datetime.now().isoformat(),
        "name": selected_item["name"],
        "serial_code": serial_code,
        "quantity": quantity,
        "ppu": selected_item["ppu"],
    }


# --------------------------------|
# Main functions of the program   |
# --------------------------------|
def add_item():
    # Add an item to the inventory
    data = read_file()
    name, serial_code, quantity, ppu = add_item_prompt()
    if serial_code in data:
        data[serial_code]["quantity"] += quantity
        if ppu >= data[serial_code]["ppu"]:
            data[serial_code]["ppu"] = ppu
    else:
        data[serial_code] = {
            "name": name,
            "quantity": quantity,
            "ppu": ppu,
        }
    print(f"\n\t{name} has been added to the record ")
    write_file(data)


def display_items():
    # Display
    data = read_file()
    if data.__len__() == 0:
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
    serial_code, quantity = sales_invoice_prompt()

    inventory = read_file()
    invoice = read_file(file_name=config["invoice"])

    selected_item = None
    write_invoice = invoice
    write_inventory = inventory

    for item in inventory:
        if item == serial_code:
            selected_item = inventory[item]
            gi = gen_invoice(selected_item, serial_code, quantity)
            # Check if the quantity is available
            if selected_item["quantity"] < quantity:
                print("Not enough quantity available..")
                return False
            elif selected_item["quantity"] == quantity:
                write_inventory.pop(item)
                write_invoice["list"].append(gi)
            else:
                write_inventory[item]["quantity"] -= quantity
                write_invoice["list"].append(gi)

    if selected_item is None:
        print("Item is not in inventory..")
        return False

    # Write to the file
    write_file(write_invoice, config["invoice"])
    write_file(write_inventory, config["inventory"])

    # Send mail to the customer
    send_mail()


def end_application():
    # Gracefully exit the application
    exit()


# ------------------------------------------------------|
# Main function, this is the entry point of the program |
# ------------------------------------------------------|
def main():
    load_dotenv()
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
