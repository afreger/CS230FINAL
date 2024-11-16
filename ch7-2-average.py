# Function to read values from the file, calculate the average, and display the values
def calculate_average(filename):
    try:
        # Open the file using the open function
        file = open(filename, 'r')

        # Initialize an empty list to store the values
        values = []

        # Read each line, strip newline characters, and convert to float
        for line in file:
            line = line.strip()  # Remove the newline character
            value = float(line)  # Convert to float
            values.append(value)  # Add to the list

        # Close the file after reading
        file.close()

        # Display the list of values
        print(values)

        # Calculate and display the average (mean)
        if len(values) > 0:
            mean = sum(values) / len(values)
            print(f"Mean= {mean:.2f}")
        else:
            print("No values to calculate the average.")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except ValueError:
        print("Error: File contains invalid data format.")


# Example usage
calculate_average('values.txt')
