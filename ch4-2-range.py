# Initialize max and min values to None initially
max_value = None
min_value = None

# Start a loop for user input
value = float(input("Enter a value (0 to end): "))

# Only proceed if the first input is not 0
if value != 0:
    max_value = value
    min_value = value

    while value != 0:
        # Prompt user to enter a value
        value = float(input("Enter a value (0 to end): "))

        # If it's not 0, update max and min
        if value != 0:
            if value > max_value:
                max_value = value
            if value < min_value:
                min_value = value

    # Calculate and display the range
    range_value = max_value - min_value
    print(f"Range = {range_value}")
else:
    print("No numbers were entered.")
