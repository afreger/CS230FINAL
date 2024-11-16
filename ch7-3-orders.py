# Function to process inventory and determine order quantities
def process_inventory(input_filename, output_filename):
    try:
        # Open the inventory file for reading
        input_file = open(input_filename, 'r')

        # Open the orders file for writing
        output_file = open(output_filename, 'w')

        # Process each line in the inventory file
        for line in input_file:
            # Use strip() to remove newline characters and store the result in a variable
            stripped_line = line.strip()

            # Use split() and store the result in a variable
            data = stripped_line.split(',')
            product = data[0]
            inventory_level_str = data[1]  # Store the inventory level as a string first
            inventory_level = int(inventory_level_str)  # Convert the string to an integer

            # Check if an order is needed (inventory below 10)
            if inventory_level < 10:
                # Calculate the order amount to bring inventory to 20
                order_amount = 20 - inventory_level
                # Write the product name and order size to the output file
                output_line = f"{product},{order_amount}\n"
                output_file.write(output_line)

        # Close both files after processing
        input_file.close()
        output_file.close()

        print(f"Orders have been written to {output_filename}")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    except ValueError:
        print("Error: File contains invalid data format.")


# Example usage
process_inventory('inventory.csv', 'orders.csv')
