"""
Application Name: surajmandal.py
Author/Developer: Suraj Mandal
Date: 2023-01-18

Objective:
After displaying User name and N-number, application gets user input (for various data types).
Application then processes information and displays output to user.

Description:
Application asks user to enter the following information of two vehicle makes:
- Brand of vehicle
- Color of vehicle
- Quantity of vehicle
- Price of vehicle

After data is entered, application then displays the following output:

                                                                                          Dealership name: <your name>
                                                                                          Dealership code: <your nNumber>

Vehicle make                Vehicle color               Number of vehicles              Price per vehicle
<vehicle make 1 name >      <vehicle make 1 color>      <number of vehicles make 1>     <price per vehicle of make 1>
<vehicle make 2 name >      <vehicle make 2 color>      <number of vehicle make 2>      <price per vehicle of make 2>

                                                                              Total vehicles in dealership: <number>
                                                                                    Total inventory amount: <$amount>
                                                                             Total tax amount that is paid: <$amount>
                                                                          Total inventory amount and taxes: <$amount>

*****************************************************************************************************************************



"""

# Static variables as instructed
name = "Suraj Mandal"
nnumber = "n01537188"


# List of questions to ask user
q_vehicle_one_name = "Enter vehicle first brand of vehicle make: "
q_vehicle_one_color = "Enter color of first brand (make) of vehicles: "
q_vehicle_one_quantity = "Enter quantity of first brand (make) of vehicles: "
q_vehicle_one_price = (
    "Enter price per vehicle for the first brand (make) of vehicles:\t$"
)
q_vehicle_two_name = "Enter vehicle second brand of vehicle make: "
q_vehicle_two_color = "Enter color of second brand (make) of vehicles: "
q_vehicle_two_quantity = "Enter quantity of second brand (make) of vehicles: "
q_vehicle_two_price = (
    "Enter price per vehicle for the second brand (make) of vehicles: $"
)


"""
Take user input and store in variables
Variables are of type string, int, float
Type casting is required for int and float
"""
vehicle_one_name = input(q_vehicle_one_name)
vehicle_one_color = input(q_vehicle_one_color)
vehicle_one_quantity = int(input(q_vehicle_one_quantity))
vehicle_one_price = float(input(q_vehicle_one_price))
vehicle_two_name = input(q_vehicle_two_name)
vehicle_two_color = input(q_vehicle_two_color)
vehicle_two_quantity = int(input(q_vehicle_two_quantity))
vehicle_two_price = float(input(q_vehicle_two_price))


# Calculate total inventory amount and tax
total_inventory_amount = vehicle_one_price + vehicle_two_price
total_inventory_tax = total_inventory_amount * 0.13


# Print out the following information:
# - Name of the dealership
# - Name of the owner
# - Nnumber of the owner
# - Brand of vehicle(s)
# - Color of vehicle(s)
# - Quantity of vehicle(s)
# - Price of vehicle(s)
# - Total inventory amount
# - Total inventory tax
# - Total inventory amount and taxes
output = f"""
{'*'*120}
{"%70s"%("My car delarship")}
{'*'*120}

{"%120s"%(name)}
{"%120s"% (nnumber)}

{"%30s%30s%30s%30s"%("Veichle", "Vehicle color", "Number of vehicles", "Price per vehicle")}\n
{"%30s%30s%30s%30s"%(vehicle_one_name, vehicle_one_color, vehicle_one_quantity, "$%.2f"%(vehicle_one_price))}\n
{"%30s%30s%30s%30s"%(vehicle_two_name, vehicle_two_color, vehicle_two_quantity, "$%.2f"%(vehicle_two_price))}\n
{'*'*120}

{"%100s%20s"%("Total vehicles in delarship: ", vehicle_one_quantity + vehicle_two_quantity)}
{"%100s%20s"%("Total inventory amount: ", "$%.2f"%total_inventory_amount)}
{"%100s%20s"%("Total tax amount that is paid: ", "$%.2f"%total_inventory_tax)}
{"%100s%20s"%("Total inventory amount and taxes: ", "$%.2f"%(total_inventory_tax+total_inventory_amount))}

{'*'*120}
"""

print(output)
