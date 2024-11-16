# Function to find the employee with the largest sales
def find_top_salesperson(filename):
    try:
        # Open the file using the open function
        file = open(filename, 'r')

        top_employee = ""
        top_sales = 0.0

        for line in file:
            # Use strip() to remove the newline character and any extra spaces
            line = line.strip()

            # Split the line into name and sales
            data = line.split()
            name = data[0]
            sales = float(data[1])  # Convert sales to a float

            # Update top employee if current sales are higher
            if sales > top_sales:
                top_employee = name
                top_sales = sales

        # Display the employee with the largest sales
        print(f"{top_employee} had sales of {top_sales:.1f}")

        # Close the file after reading
        file.close()

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except ValueError:
        print("Error: File contains invalid data format.")


# Example usage
find_top_salesperson('sales.txt')
