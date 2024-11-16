def calcCost(count, price, discount=0.1):
    if count < 5:
        return count * price
    else:
        return count * price * (1 - discount)

# Test case: 3 items priced at $25, with a 10% discount
count = 3
price = 25
discount = 0.1
cost = calcCost(count, price, discount)

# Display the result
print("Cost = $", cost)
