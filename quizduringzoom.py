def pick_balls():
    red_count = yellow_count = green_count = total_value = 0
    ball_limit = 4

    print("Enter 'R' for Red, 'Y' for Yellow, 'G' for Green.")

    for i in range(ball_limit):
        ball = input(f"Pick ball {i + 1}: ").strip().upper()

        if ball not in ['R', 'Y', 'G']:
            print("Invalid input. Please enter 'R', 'Y', or 'G'.")
            continue

        if ball == 'R':
            red_count += 1
            points = 0
        elif ball == 'Y':
            yellow_count += 1
            points = 1
        elif ball == 'G':
            green_count += 1
            points = 3

        total_value += points

        if total_value >= 5:
            break

    print("\nResults:")
    print(f"Total balls selected: {red_count + yellow_count + green_count}")
    print(f"Total value of balls: {total_value}")
    print(f"Red balls: {red_count}")
    print(f"Yellow balls: {yellow_count}")
    print(f"Green balls: {green_count}")

    if total_value < 5:
        print("Value is less than 5")


pick_balls()
