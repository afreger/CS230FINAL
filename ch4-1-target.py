# Program to track progress toward a sales target over 5 days
target = float(input("Enter total sales target: "))
cumulative_sales = 0.0

# Loop for 5 days
for day in range(1, 6):
    sales = float(input("Enter day " + str(day) + " sales: "))
    cumulative_sales += sales
    percentage = (cumulative_sales / target) * 100
    print("Cumulative sales: " + str(cumulative_sales) + " ( " + str(round(percentage, 1)) + " % )")
