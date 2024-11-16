"""
Andrew's Commuting Cost Calculator
Section: 5
Date: 9/9/2024

Description:
This program calculates the monthly and annual cost of commuting based on the user's input of daily round trip miles,
number of commuting days, and monthly parking cost. It also outputs the time spent commuting and average speed.

Constants:
- COST_PER_MILE: Cost per mile in dollars (based on AAA's 2022 estimate)
- AVERAGE_SPEED_MPH: Average speed in miles per hour
- MILES_TO_KILOMETERS: Conversion factor from miles to kilometers
- MONTHS_IN_YEAR: Number of months in a year
- MINUTES_IN_HOUR: Number of minutes in an hour
- SECONDS_IN_MINUTE: Number of seconds in a minute (if needed for future use)

Inputs:
- daily_round_trip_miles: User's daily round trip distance in miles
- commuting_days_per_month: Number of days per month the user commutes
- monthly_parking_cost: User's monthly parking cost in dollars

Outputs:
- Monthly and annual commuting costs
- Time spent commuting in hours and minutes
- Average speed in kilometers per minute
"""

# Constants
COST_PER_MILE = 0.72
AVERAGE_SPEED_MPH = 45
MILES_TO_KILOMETERS = 1.609344
MONTHS_IN_YEAR = 12
MINUTES_IN_HOUR = 60
SECONDS_IN_MINUTE = 60

# Input Section
print("========== Input Commuting Values ==========")
daily_round_trip_miles = float(input("What is your daily round trip to school/work? "))
commuting_days_per_month = int(input("How many days per month do you commute? "))
monthly_parking_cost = float(input("How much do you pay for parking per month? "))

# Calculations
monthly_miles = daily_round_trip_miles * commuting_days_per_month
monthly_cost = (monthly_miles * COST_PER_MILE) + monthly_parking_cost
annual_cost = monthly_cost * MONTHS_IN_YEAR

# Time spent commuting
total_time_spent_hours = monthly_miles / AVERAGE_SPEED_MPH
time_spent_hours = int(total_time_spent_hours)
time_spent_minutes = (total_time_spent_hours - time_spent_hours) * MINUTES_IN_HOUR

# Average speed
speed_kph = AVERAGE_SPEED_MPH * MILES_TO_KILOMETERS
speed_kpm = speed_kph / MINUTES_IN_HOUR

# Output Section
print("\n========== Commuting Statistics ==========")
print("At an average speed of", AVERAGE_SPEED_MPH, "miles per hour,")
print("you spend", time_spent_hours, "hours and", round(time_spent_minutes, 2), "minutes a month commuting")
print("The average speed of", AVERAGE_SPEED_MPH, "miles per hour is", round(speed_kpm, 2), "kilometers per minute")
print("Your estimated monthly cost of commuting is $", round(monthly_cost, 1), sep="")
print("Your estimated yearly cost of commuting is $", round(annual_cost, 1), sep="")
