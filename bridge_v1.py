import random

n = 11  # Size of the bridge
valid_input = False

# Input validation
while not valid_input:
    start = input(f"Enter the starting position (M for middle or a number between 1 and {n}): ")

    if start == 'M' or start == 'm':  # Middle option
        position = (n + 1) // 2
        valid_input = True
    elif start.isdigit() and 1 <= int(start) <= n:  # Check for valid number input
        position = int(start)
        valid_input = True
    else:
        print("Invalid value. Please try again.")

step = 0
print(f"Step: {step}, Position: {position}")

# Random walk loop
while position != 1 and position != n:
    step += 1
    move = random.choice([-1, 1])  # Randomly move left (-1) or right (+1)
    position += move
    print(f"Step: {step}, Position: {position}")

# Output the number of steps
if position == 1:
    print(f"Avery exited to the left after {step} steps.")
elif position == n:
    print(f"Avery exited to the right after {step} steps.")