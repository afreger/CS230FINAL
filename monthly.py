# Program: TeslEV Customer Order Processing
# Author: Andrew
# Date: 9/17/24
# Description: This program processes customer orders for Tesla EVs, including model, wheel drive, color selection,
#              and optional leasing with tax calculation and Federal Tax Credit eligibility.
# Certification: I have completed this work individually.

# CONSTANTS
TAX_RATE = 0.0625
FEDERAL_TAX_CREDIT = 7500
DOWN_PAYMENT = 3000
MONTHLY_PERCENTAGE = 0.015  # Leasing percentage (interest rate)
TOW_HITCH_COST = 8000

# MODEL PRICES (WITHOUT DICTIONARY)
# Prices for SEDAN
SEDAN_FRONT_WHITE = 24000
SEDAN_FRONT_BLUE = 24500
SEDAN_FRONT_RED = 25000
SEDAN_REAR_WHITE = 26000
SEDAN_REAR_BLUE = 26500
SEDAN_REAR_RED = 27000
SEDAN_ALL_WHITE = 28000
SEDAN_ALL_BLUE = 28500
SEDAN_ALL_RED = 29000

# Prices for SUV
SUV_FRONT_WHITE = 26000
SUV_FRONT_BLUE = 26500
SUV_FRONT_RED = 27000
SUV_REAR_WHITE = 28000
SUV_REAR_BLUE = 28500
SUV_REAR_RED = 29000
SUV_ALL_WHITE = 30000
SUV_ALL_BLUE = 30500
SUV_ALL_RED = 31000

# Get inputs from the user
print("=========Build Your EV=========")
model = input("Please select the EV model (Sedan, SUV): ").lower()
wheel_drive = input("Please select the wheel drive type (Front, Rear, All): ").lower()

# Correcting the check for "All" and "Y"
if wheel_drive == "all" or wheel_drive == "y":
    wheel_drive = "all"

color = input("Please select the color (White, Blue, Red): ").lower()

# Determine the price based on the selections (manually handling cases)
if model == "sedan":
    if wheel_drive == "front":
        if color == "white":
            price = SEDAN_FRONT_WHITE
        elif color == "blue":
            price = SEDAN_FRONT_BLUE
        else:
            price = SEDAN_FRONT_RED
    elif wheel_drive == "rear":
        if color == "white":
            price = SEDAN_REAR_WHITE
        elif color == "blue":
            price = SEDAN_REAR_BLUE
        else:
            price = SEDAN_REAR_RED
    else:
        if color == "white":
            price = SEDAN_ALL_WHITE
        elif color == "blue":
            price = SEDAN_ALL_BLUE
        else:
            price = SEDAN_ALL_RED
elif model == "suv":
    if wheel_drive == "front":
        if color == "white":
            price = SUV_FRONT_WHITE
        elif color == "blue":
            price = SUV_FRONT_BLUE
        else:
            price = SUV_FRONT_RED
    elif wheel_drive == "rear":
        if color == "white":
            price = SUV_REAR_WHITE
        elif color == "blue":
            price = SUV_REAR_BLUE
        else:
            price = SUV_REAR_RED
    else:
        if color == "white":
            price = SUV_ALL_WHITE
        elif color == "blue":
            price = SUV_ALL_BLUE
        else:
            price = SUV_ALL_RED

    # Tow hitch option only for SUVs
    tow_hitch = input("Do you want to add the tow hitch? ([Y], [N]): ").lower()
    if tow_hitch == 'y':
        price += TOW_HITCH_COST

# Leasing option
leasing_option = input("Do you want the leasing option? ([Y], [N]): ").lower()

if leasing_option == 'y':
    months = int(input("Please enter the leasing months between 1 and 9: "))

    # Updated leasing payment formula
    down_payment = DOWN_PAYMENT
    lease_price = price - down_payment  # Subtract down payment from the total price

    # **Key Fix**: Monthly payment should be based on remaining price + interest
    monthly_payment = (lease_price / months) + (lease_price * MONTHLY_PERCENTAGE)

    total_payment = down_payment + (monthly_payment * months)
    total_tax = total_payment * TAX_RATE
    final_total = total_payment + total_tax
else:
    federal_credit = input("Do you want to apply the Federal Tax Credit? ([Y], [N]): ").lower()
    if federal_credit == 'y':
        income = input("Is your annual income less than $150,000? ([Y], [N]): ").lower()
        if income == 'y':
            price -= FEDERAL_TAX_CREDIT
    total_tax = price * TAX_RATE
    final_total = price + total_tax

# Print the order summary with format strings, 20-character spacing, and thousands separators
print("\n=========Order Summary========")
print(f"{'Model:':20s}{model.upper()}")
print(f"{'Wheel Drive:':20s}{wheel_drive.capitalize()}")
print(f"{'Color:':20s}{color.capitalize()}")

if leasing_option == 'y':
    print(f"{'Payment:':20s}Leasing")
    print(f"{'Months:':20s}{months}")
    print(f"{'Monthly Payment:':20s}$ {monthly_payment:,.2f}")  # Use thousands separator with comma
    print(f"{'Monthly Tax:':20s}$ {(total_tax / months):,.2f}")  # Tax divided across months
    print("-------------------------------")
    print(f"{'Total:':20s}$ {final_total:,.2f}")
else:
    print(f"{'Payment:':20s}Cash")
    if federal_credit == 'y' and income == 'y':
        print(f"{'* Applied the Federal Tax Credit:':20s}$7,500")
    print(f"{'Subtotal:':20s}$ {price:,.2f}")
    print(f"{'Tax:':20s}$ {total_tax:,.2f}")
    print("-------------------------------")
    print(f"{'Total:':20s}$ {final_total:,.2f}")
