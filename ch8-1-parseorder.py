def process_order(order):
    # Check if the order contains a colon
    if ':' not in order or order.index(':') == 0:
        print("Invalid order: Customer name missing.")
        return

    customer, products_str = order.split(':', 1)

    # Check if there are no products after the colon
    if not products_str:
        print("Invalid order: Products missing.")
        return

    products = products_str.split(',')

    # Print the customer name
    print(f"Customer:   {customer.strip()}")

    # Print each product with a consecutive number
    for i, product in enumerate(products, start=1):
        print(f"Product {i}:  {product.strip()}")


# Get the order from the user
order_input = input("Enter the order: ")
process_order(order_input)
