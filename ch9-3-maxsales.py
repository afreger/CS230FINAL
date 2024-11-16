def get_max_sales():
    sales_data = {}  # Dictionary to store names and sales

    while True:
        # Prompt for input on a new line each time
        print("Input name and sales:")
        user_input = input()  # Collect input

        if user_input == "":
            break  # Stop when no input is given

        # Split the input into name and sales
        try:
            name, sales = user_input.split()
            sales = float(sales)  # Convert sales to float
            sales_data[name] = sales
        except ValueError:
            print("Invalid input. Please enter in the format: Name Sales")
            continue

    if sales_data:
        # Initialize variables to keep track of the person with the highest sales
        max_sales_person = None
        max_sales = 0

        # Iterate through the dictionary using items() method
        for name, sales in sales_data.items():
            if sales > max_sales:
                max_sales_person = name
                max_sales = sales

        print(f"{max_sales_person} had the maximum sales of {max_sales}.")
    else:
        print("No sales data was entered.")


# Run the function
get_max_sales()

