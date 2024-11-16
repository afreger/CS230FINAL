# Prompt the user to enter a temperature in Fahrenheit
temperature_fahrenheit = float(input("Enter temperature in Fahrenheit: "))

# Convert to Celsius and round to 1 decimal place
temperature_celsius = round((temperature_fahrenheit - 32) * 5 / 9, 1)

# Display the temperature in Celsius
print(f"Temperature in Celsius: {temperature_celsius}")

# Determine and display the state of water
if temperature_celsius <= 0:
    print("Ice")
elif temperature_celsius < 100:
    print("Liquid")
else:
    print("Gas")