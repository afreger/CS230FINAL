import math

# Prompt user for advertising spending
advertising_spending = float(input("Enter advertising spending ($): "))

# Calculate additional expected attendees using round for the square root calculation
additional_attendees = 2 * round(math.sqrt(advertising_spending))

# Calculate total expected attendees
expected_attendees = 20 + additional_attendees

# Calculate ticket sales
ticket_sales = expected_attendees * 10  # $10 per ticket

# Calculate total costs
fixed_costs = 200
total_costs = advertising_spending + fixed_costs

# Calculate expected profit
profit = ticket_sales - total_costs

# Display results
print(f"Expected attendees: {expected_attendees}")
print(f"Ticket sales: $ {ticket_sales:.2f}")
print(f"Total costs:  $ {total_costs:.2f}")
print(f"Profit:       $ {profit:.2f}")
