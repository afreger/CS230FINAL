# List of sales for each day
sales = [50, 75, 150, 125, 100]

# List of corresponding days
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

# Initialize variables to store the maximum sales and corresponding day
max_sales = 0
max_sales_day = ""

# Use a for loop to go through each day's sales
for i in range(len(sales)):
    # If the current sales is greater than the maximum so far, update max_sales and max_sales_day
    if sales[i] > max_sales:
        max_sales = sales[i]
        max_sales_day = days[i]

# Display the result
print("Max sales = $", max_sales)
print("Max sales day =", max_sales_day)
