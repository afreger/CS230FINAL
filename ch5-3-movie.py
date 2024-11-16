import math


# Function to calculate profit and additional attendees
def movieModel(ticketPrice, fixedCost, adSpending):
    # Calculate additional attendees based on advertising spending
    additional_attendees = 2 * round(math.sqrt(adSpending))

    # Total attendees including the 20 forecasted without advertising
    total_attendees = 20 + additional_attendees

    # Calculate total revenue from ticket sales
    revenue = total_attendees * ticketPrice

    # Calculate profit by subtracting fixed costs and advertising spending from revenue
    profit = revenue - fixedCost - adSpending

    # Return the profit and additional attendees
    return profit, additional_attendees


# Main part of the program
def main():
    # Input advertising spending
    adSpending = float(input("Enter advertising ($): "))

    # Fixed values
    ticketPrice = 10
    fixedCost = 200

    # Call the movieModel function to get profit and additional attendees
    profit, additional_attendees = movieModel(ticketPrice, fixedCost, adSpending)

    # Display the results
    print(f"Additional attendees: {additional_attendees}")
    print(f"Profit: $ {profit:.1f}")


# Run the main program
main()
