import random

n = 11  # Size of the bridge
valid_input = False

# Input validation
while not valid_input:
    start = input(f"Enter the starting position (M for middle or a number between 1 and {n}): ").strip()

    if start.lower() == 'm':  # Middle option, accepting 'M' or 'm'
        position = (n + 1) // 2
        valid_input = True
    elif start.isdigit() and 1 <= int(start) <= n:  # Check for valid number input
        position = int(start)
        valid_input = True
    else:
        print("Invalid value. Please try again.")

step = 0
bridge = "[" + "." * (position - 1) + "#" + "." * (n - position) + "]"
print(f"Step: {step:>2}  {bridge}  Position: {position:>2}")

# Random walk loop
while position != 1 and position != n:
    step += 1
    move = random.choice([-1, 1])  # Randomly move left (-1) or right (+1)
    position += move
    bridge = "[" + "." * (position - 1) + "#" + "." * (n - position) + "]"
    print(f"Step: {step:>2}  {bridge}  Position: {position:>2}")

# Output the final step and where Avery exits
if position == 1:
    step = step + 1
    bridge = "[" + "." * (position - 1) + "#" + "." * (n - position) + "<"
    print(f"Step: {step:>2}  {bridge}  Exit Left")
elif position == n:
    step = step + 1
    bridge = "[" + "." * (position - 1) + "#" + "." * (n - position) + ">"
    print(f"Step: {step:>2}  {bridge}  Exit Right")

# Output the number of steps taken
print(f"Number of steps to get off the bridge: {step}")
