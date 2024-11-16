# Initialize an empty list to store the numbers
numbers = []

# Loop to get user input until the user enters 0
value = float(input("Enter value (or 0 to end): "))
while value != 0:
    # Add the value to the list
    numbers.append(value)

    # Ask for the next value
    value = float(input("Enter value (or 0 to end): "))

# Check if the list has at least one value
if numbers:
    # Display the list
    print(numbers)

    # Calculate and display the range
    range_value = max(numbers) - min(numbers)
    print("Range =", range_value)

else:
    # Handle case where no values were entered
    print("No values entered.")
