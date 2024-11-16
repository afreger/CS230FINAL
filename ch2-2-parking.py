# Prompt the user for the number of hours parked
hours_parked = float(input("Enter hours parked: "))

# Define constants
BASE_FEE = 5.0
HOURLY_RATE = 2.5
MAXIMUM_FEE = 20.0

# Calculate the total fee
total_fee = BASE_FEE + (hours_parked * HOURLY_RATE)

# Ensure the fee does not exceed the maximum fee using the min function
total_fee = min(total_fee, 20)

# Display the parking fee
print(f"Parking fee: $ {total_fee:.2f}")

