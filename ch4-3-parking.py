# Initial setup
base_fee = 5
hourly_rate = 2.5
minimum_fee = 10

# Print table header
print("Hours  Fee")

# Calculate and print fees for each increment of 0.5 hours from 1 to 6 hours
hours = 1.0
while hours <= 6.0:
    fee = base_fee + (hours * hourly_rate)
    fee = max(fee, minimum_fee)  # Ensure the fee is at least the minimum fee

    # Print the hours and fee using format strings
    print("{:.1f}   ${:.2f}".format(hours, fee))

    hours += 0.5



