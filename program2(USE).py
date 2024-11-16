# Program 2: EV Purchase
# Name: Andrew
# Date: 9/26/2024
# Description: This program processes customer orders for Tesla EVs, including model, wheel drive, color selection,
#              and optional leasing with tax calculation and Federal Tax Credit eligibility.
# Certification: I have completed this work individually.

# CONSTANTS
SALES_TAX = 0.0625
TOW_HITCH_COST = 8000
DOWN_PAYMENT = 3000
MONTHLY_INTEREST_RATE = 0.015
FEDERAL_TAX_CREDIT = 7500
INCOME_ELIGIBILITY = 150000

# PRICES
SEDAN_FRONT_WHITE = 24000
SEDAN_FRONT_BLUE = 24500
SEDAN_FRONT_RED = 25000
SEDAN_REAR_WHITE = 26000
SEDAN_REAR_BLUE = 26500
SEDAN_REAR_RED = 27000
SEDAN_ALL_WHITE = 28000
SEDAN_ALL_BLUE = 28500
SEDAN_ALL_RED = 29000

SUV_FRONT_WHITE = 26000
SUV_FRONT_BLUE = 26500
SUV_FRONT_RED = 27000
SUV_REAR_WHITE = 28000
SUV_REAR_BLUE = 28500
SUV_REAR_RED = 29000
SUV_ALL_WHITE = 30000
SUV_ALL_BLUE = 30500
SUV_ALL_RED = 31000

# GET INPUTS FROM THE USER
print("==========Build Your EV==========")
model = input("Please select the EV model (Sedan, SUV): ").strip().lower()
while model not in ["sedan", "suv"]:
    print("Invalid model")
    model = input("Please select the EV model (Sedan, SUV): ").strip().lower()

# Tow hitch add-on for SUV
tow_hitch = "n"
if model == "suv":
    tow_hitch = input("Do you want to add the tow hitch? ([Y], [N]): ").strip().lower()
    while tow_hitch not in ["y", "n"]:
        print("Invalid input. Please enter 'Y' or 'N'.")
        tow_hitch = input("Do you want to add the tow hitch? ([Y], [N]): ").strip().lower()

# Input: Drive Type
drive_type = input("Please select the wheel drive type (Front, Rear, All): ").strip().lower()
while drive_type not in ["front", "rear", "all"]:
    print("Invalid input. Please enter 'Front', 'Rear', or 'All'.")
    drive_type = input("Please select the wheel drive type (Front, Rear, All): ").strip().lower()

# Input: Color
color = input("Please select the color (White, Blue, Red): ").strip().lower()
while color not in ["white", "blue", "red"]:
    print("Invalid color. Please enter 'White', 'Blue', or 'Red'.")
    color = input("Please select the color (White, Blue, Red): ").strip().lower()

# Determine the base price using nested if statements
if model == "sedan":
    if drive_type == "front":
        if color == "white":
            base_price = SEDAN_FRONT_WHITE
        elif color == "blue":
            base_price = SEDAN_FRONT_BLUE
        elif color == "red":
            base_price = SEDAN_FRONT_RED
    elif drive_type == "rear":
        if color == "white":
            base_price = SEDAN_REAR_WHITE
        elif color == "blue":
            base_price = SEDAN_REAR_BLUE
        elif color == "red":
            base_price = SEDAN_REAR_RED
    elif drive_type == "all":
        if color == "white":
            base_price = SEDAN_ALL_WHITE
        elif color == "blue":
            base_price = SEDAN_ALL_BLUE
        elif color == "red":
            base_price = SEDAN_ALL_RED
elif model == "suv":
    if drive_type == "front":
        if color == "white":
            base_price = SUV_FRONT_WHITE
        elif color == "blue":
            base_price = SUV_FRONT_BLUE
        elif color == "red":
            base_price = SUV_FRONT_RED
    elif drive_type == "rear":
        if color == "white":
            base_price = SUV_REAR_WHITE
        elif color == "blue":
            base_price = SUV_REAR_BLUE
        elif color == "red":
            base_price = SUV_REAR_RED
    elif drive_type == "all":
        if color == "white":
            base_price = SUV_ALL_WHITE
        elif color == "blue":
            base_price = SUV_ALL_BLUE
        elif color == "red":
            base_price = SUV_ALL_RED

# Tow hitch option
if model == "suv" and tow_hitch == "y":
    base_price += TOW_HITCH_COST

# Leasing or Purchase Option
leasing_option = input("Do you want the leasing option? ([Y], [N]): ").strip().lower()
while leasing_option not in ["y", "n"]:
    print("Invalid input. Please enter 'Y' or 'N'.")
    leasing_option = input("Do you want the leasing option? ([Y], [N]): ").strip().lower()

# Leasing
if leasing_option == "y":
    months = int(input("Please enter the leasing months between 1 and 9: "))
    while not (1 <= months <= 9):
        print("Invalid number. Please enter a number between 1 and 9.")
        months = int(input("Please enter the leasing months between 1 and 9: "))

    monthly_payment = base_price * MONTHLY_INTEREST_RATE
    monthly_tax = monthly_payment * SALES_TAX
    total_monthly_payment = monthly_payment + monthly_tax
    balance = base_price - DOWN_PAYMENT

    # Calculate initial balance as if the payments had been made for 8 months already
    initial_balance = total_monthly_payment * 9

    print("\n==========Order Summary==========")
    print(f"{'Model:':20s} {model.upper()}")
    print(f"{'Wheel Drive:':20s} {drive_type.upper()}-Wheel Drive")
    print(f"{'Color:':20s} {color.upper()}")

    if model == "suv" and tow_hitch == "y":
        print(f"\n*Added the Tow Hitch")

    print(f"\n{'Payment:':20s} Leasing")
    print(f"{'Months:':20s} {months}")
    print(f"{'Monthly Payment:':20s} $   {monthly_payment:,.2f}")
    print(f"{'Monthly Tax:':20s} $    {monthly_tax:,.2f}")
    print(f"-------------------------------")
    print(f"{'Total:':20s} $ {(total_monthly_payment * months):,.2f}")

    # Monthly Breakdown
    print("\nMonth  MonthlyPmt  MonthlyTax  TotalPmt  Balance")
    total_paid = 0  # Initialize total paid so far
    balance = initial_balance  # Start balance as if 8 months of payments were made

    for month in range(1, months + 1):
        # Calculate cumulative total paid so far
        total_paid += total_monthly_payment

        # Calculate the balance as the initial balance minus the total paid so far
        balance -= total_monthly_payment  # This mirrors the total payment in reverse

        # Ensure balance doesn't go negative on the last payment
        if balance < 0:
            balance = 0

        print(f"{month:<6} ${monthly_payment:,.2f}    ${monthly_tax:,.2f}     ${total_paid:,.2f}   ${balance:,.2f}")

# If purchasing with cash
else:
    apply_credit = input("Do you want to apply the Federal Tax Credit? ([Y], [N]): ").strip().lower()
    while apply_credit not in ["y", "n"]:
        print("Invalid input. Please enter 'Y' or 'N'.")
        apply_credit = input("Do you want to apply the Federal Tax Credit? ([Y], [N]): ").strip().lower()

    if apply_credit == "y":
        income = input(f"Is your annual income less than or equal to ${INCOME_ELIGIBILITY:,}? ([Y], [N]): ").strip().lower()
        while income not in ["y", "n"]:
            print("Invalid input. Please enter 'Y' or 'N'.")
            income = input(f"Is your annual income less than or equal to ${INCOME_ELIGIBILITY:,}? ([Y], [N]): ").strip().lower()
        if income == "y":
            base_price -= FEDERAL_TAX_CREDIT

    total_price_with_tax = base_price * (1 + SALES_TAX)

    print("\n==========Order Summary==========")
    print(f"{'Model:':20s} {model.upper()}")
    print(f"{'Wheel Drive:':20s} {drive_type.upper()}-Wheel Drive")
    print(f"{'Color:':20s} {color.upper()}")

    print(f"\n{'Payment:':20s} Cash")
    if apply_credit == "y":
        print(f"\n*Applied the ${FEDERAL_TAX_CREDIT:,.2f} Federal Tax Credit")
    print(f"{'Subtotal:':20s} $ {base_price:,.2f}")
    print(f"{'Tax:':20s} $ {base_price * SALES_TAX:,.2f}")
    print(f"-------------------------------")
    print(f"{'Total:':20s} $ {total_price_with_tax:,.2f}")

# Thank you message
print("\nThank you for your purchase!")
