# Prompt the user for the price of an item
price_per_item = float(input("Enter price per item: "))

# Prompt the user for the number of items purchased
number_of_items = int(input("Enter number of items: "))

# Calculate the pre-tax cost and round it to two decimal places
pre_tax_cost = price_per_item * number_of_items

# Calculate the total sales tax (7.5% of the pre-tax cost) and round to two decimal places
tax_rate = 0.075
total_sales_tax = round(pre_tax_cost * tax_rate, 2)

# Calculate the after-tax cost and round to two decimal places
after_tax_cost = round(pre_tax_cost + total_sales_tax, 2)

# Display the results with appropriate formatting
print("Pre-tax cost = {:.2f}".format(round(pre_tax_cost, 2)))
print("Tax paid = {:.2f}".format(total_sales_tax))
print("After-tax cost = {:.2f}".format(after_tax_cost))
