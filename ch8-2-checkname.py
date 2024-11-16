import re

# Get product name from user
product_name = input("Enter product name: ")

# Validate the product name with additional checks
is_valid = (
    len(product_name) > 0 and                # Ensure the product name is not empty
    product_name[0].upper() == product_name[0] and  # Check if the first character is uppercase
    all(char.isalpha() or char.isdigit() for char in product_name) and  # Ensure all characters are letters or digits
    bool(re.match(r'^[A-Z][A-Za-z0-9]*$', product_name))  # Check if regex matches
)

# Print the result
print(is_valid)
