# Prompt for the number of items purchased
num_items = int(input("Enter number of items: "))

# Check if the input is negative
if num_items < 0:
    print("Error: The number of items cannot be negative.")
else:
    # Determine the cost per item based on the number of items purchased
    if num_items < 5:
        cost_per_item = 10
    elif num_items <= 10:  # Covers the range 5 to 10 inclusively
        cost_per_item = 9
    else:  # More than 10 items
        cost_per_item = 8

    # Calculate the total cost
    total_cost = num_items * cost_per_item

    # Display the total cost
    print(f"Total cost: $ {total_cost}")

