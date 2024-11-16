"""
# Program 2: EV Purchase
# Name: Andrew
# Date: 9/26/2024
# Description: This program processes customer orders for Tesla EVs, including model, wheel drive, color selection,
               and optional leasing with tax calculation and Federal Tax Credit eligibility.
# Certification: I have completed this work individually.
"""

# CONSTANTS
SALES_TAX = 0.0625
TOW_HITCH_COST = 8000
DOWN_PAYMENT = 3000
MONTHLY_INTEREST_RATE = 0.015
FEDERAL_TAX_CREDIT = 7500
INCOME_ELIGIBILITY = 150000

# INPUTS FROM THE USER
print("==========Build Your EV==========")
model = input("Please select the EV model (Sedan, SUV): ").strip().lower()
while model != "sedan" and model != "suv":
    print("Invalid model")
    model = input("Please select the EV model (Sedan, SUV): ").strip().lower()

# Tow hitch add-on for SUV
tow_hitch = "n"
if model == "suv":
    tow_hitch = input("Do you want to add the tow hitch? ([Y], [N]): ").strip().lower()
    while tow_hitch != "y" and tow_hitch != "n":
        print("Invalid input. Please enter 'Y' or 'N'.")
        tow_hitch = input("Do you want to add the tow hitch? ([Y], [N]): ").strip().lower()

# Drive Type Input
drive_type = input("Please select the wheel drive type (Front, Rear, All): ").strip().lower()
while drive_type != "front" and drive_type != "rear" and drive_type != "all":
    print("Invalid input. Please enter 'Front', 'Rear', or 'All'.")
    drive_type = input("Please select the wheel drive type (Front, Rear, All): ").strip().lower()

# Color Input
color = input("Please select the color (White, Blue, Red): ").strip().lower()
while color != "white" and color != "blue" and color != "red":
    print("Invalid color. Please enter 'White', 'Blue', or 'Red'.")
    color = input("Please select the color (White, Blue, Red): ").strip().lower()

# Determine the base price using nested if statements
base_price = 0

if model == "sedan":
    if drive_type == "front":
        if color == "white":
            base_price = 24000
        elif color == "blue":
            base_price = 24500
        elif color == "red":
            base_price = 25000
    elif drive_type == "rear":
        if color == "white":
            base_price = 26000
        elif color == "blue":
            base_price = 26500
        elif color == "red":
            base_price = 27000
    elif drive_type == "all":
        if color == "white":
            base_price = 28000
        elif color == "blue":
            base_price = 28500
        elif color == "red":
            base_price = 29000
else:  # model == "suv"
    if drive_type == "front":
        if color == "white":
            base_price = 26000
        elif color == "blue":
            base_price = 26500
        elif color == "red":
            base_price = 27000
    elif drive_type == "rear":
        if color == "white":
            base_price = 28000
        elif color == "blue":
            base_price = 28500
        elif color == "red":
            base_price = 29000
    elif drive_type == "all":
        if color == "white":
            base_price = 30000
        elif color == "blue":
            base_price = 30500
        elif color == "red":
            base_price = 31000

# Tow hitch option
if model == "suv" and tow_hitch == "y":
    base_price += TOW_HITCH_COST

# Purchase Or Leasing
leasing_option = input("Do you want the leasing option? ([Y], [N]): ").strip().lower()
while leasing_option != "y" and leasing_option != "n":
    print("Invalid input. Please enter 'Y' or 'N'.")
    leasing_option = input("Do you want the leasing option? ([Y], [N]): ").strip().lower()

# Leasing
if leasing_option == "y":
    months = int(input("Please enter the leasing months between 1 and 9: "))
    while months < 1 or months > 9:
        print("Invalid number. Please enter a number between 1 and 9.")
        months = int(input("Please enter the leasing months between 1 and 9: "))

    monthly_payment = base_price * MONTHLY_INTEREST_RATE
    monthly_tax = monthly_payment * SALES_TAX
    total_monthly_payment = monthly_payment + monthly_tax
    balance = base_price - DOWN_PAYMENT

    # Calculate initial balance for Eight Months
    initial_balance = total_monthly_payment * 9

    print("\n==========Order Summary==========")
    # Model display with all caps for both models
    print(f"{'Model:':20s}{model.upper()}")
    print(f"{'Wheel Drive:':20s}{drive_type.capitalize()}")
    print(f"{'Color:':20s}{color.capitalize()}")

    if model == "suv" and tow_hitch == "y":
        print(f"{'*Added the Tow Hitch:':20s}{''}")
    print(f"{'Payment:':20s}{'Leasing'}")
    print(f"{'Months:':20s}{months}")
    print(f"{'Monthly Payment:':20s}$ {monthly_payment:,.2f}")
    print(f"{'Monthly Tax:':20s}$ {monthly_tax:,.2f}")
    print(f"{'-'*31}")
    print(f"{'Total:':20s}$ {(total_monthly_payment * months):,.2f}")

    # Breakdown by Month
    print(f"\n{'Month':6s} {'MonthlyPmt':20s} {'MonthlyTax':20s} {'TotalPmt':20s} {'Balance':20s}")
    total_paid = 0  # Initialize cumulative at this point
    balance = initial_balance  # Balance for eight months of pay

    for month in range(1, months + 1):
        # Cumulative
        total_paid += total_monthly_payment

        # Basic Calculation
        balance -= total_monthly_payment  # Reverse Total Payment

        # No Negative Balance
        if balance < 0:
            balance = 0

        print(f"{month:<6} ${monthly_payment:20,.2f} ${monthly_tax:20,.2f} ${total_paid:20,.2f} ${balance:20,.2f}")

# Cash Purchase
else:
    apply_credit = input("Do you want to apply the Federal Tax Credit? ([Y], [N]): ").strip().lower()
    while apply_credit != "y" and apply_credit != "n":
        print("Invalid input. Please enter 'Y' or 'N'.")
        apply_credit = input("Do you want to apply the Federal Tax Credit? ([Y], [N]): ").strip().lower()

    if apply_credit == "y":
        income = input(f"Is your annual income less than or equal to ${INCOME_ELIGIBILITY:,}? ([Y], [N]): ").strip().lower()
        while income != "y" and income != "n":
            print("Invalid input. Please enter 'Y' or 'N'.")
            income = input(f"Is your annual income less than or equal to ${INCOME_ELIGIBILITY:,}? ([Y], [N]): ").strip().lower()
        if income == "y":
            base_price -= FEDERAL_TAX_CREDIT

    total_price_with_tax = base_price * (1 + SALES_TAX)

    print("\n==========Order Summary==========")
    # Model display with all caps for both models
    print(f"{'Model:':20s}{model.upper()}")
    print(f"{'Wheel Drive:':20s}{drive_type.capitalize()}")
    print(f"{'Color:':20s}{color.capitalize()}")

    print(f"{'Payment:':20s}{'Cash'}")
    if apply_credit == "y":
        print(f"{'*Applied the Federal Tax Credit:':20s}${FEDERAL_TAX_CREDIT:,.2f}")
    print(f"{'Subtotal:':20s}$ {base_price:,.2f}")
    print(f"{'Tax:':20s}$ {base_price * SALES_TAX:,.2f}")
    print(f"{'-'*31}")
    print(f"{'Total:':20s}$ {total_price_with_tax:,.2f}")

print("\nThank you for purchasing an EV!")
