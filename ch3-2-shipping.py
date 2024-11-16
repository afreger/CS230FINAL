# Get the number of packages and shipping method from the user
num_packages = int(input("Enter # of packages to ship: "))
shipping_method = input("Enter r for regular, e for express: ").lower()

# Define the shipping costs
regular_cost = 10
express_cost = 15

# Calculate the total cost based on the shipping method
if shipping_method == 'r':
    total_cost = num_packages * regular_cost
elif shipping_method == 'e':
    total_cost = num_packages * express_cost
else:
    print("Invalid shipping method.")
    total_cost = None

# Display the total cost if it's valid
if total_cost is not None:
    print(f"Total cost: $ {total_cost}")
