# Python Conditional Logic: Mastering Control Flow

"""
Author: Kalim Amzad Chy
Email: kalim.amzad.chy@gmail.com

This Python script is designed to provide an in-depth understanding of Python's conditional statements.
We will explore:
1. Basic if, if-else, and if-elif-else statements.
2. Logical and boolean operations in conditions.
3. Real-world applications with engaging examples.
4. Nested conditional statements for complex decision making.

Each section includes detailed explanations, examples, and assignments.
"""

# Section 1: Basic Conditional Statements
# ---------------------------------------
# The `if` statement is the simplest form of control flow, allowing for conditional execution of code blocks.

# Example 1: Simple if statement
age = 20
if age >= 18:
    print("You are eligible to vote.")
    print("Please register to vote as soon as possible.")

# The `if-else` statement provides an alternative execution when the `if` condition is not met.
# Example 2: if-else statement
temperature = 30
if temperature > 25:
    print("It's a hot day.")
else:
    print("It's not a hot day.")

# The `if-elif-else` structure allows for multiple conditions to be checked sequentially.
# Example 3: if-elif-else statement
score = 75
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: D or F")

# Assignment 1: Write a Python script that determines if a number is positive, negative, or zero using if-elif-else.
# Write your code below:
# Input from the user
number = float(input("Enter a number: "))

# Using if-elif-else to determine the type of number
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

# Section 2: Logical and Boolean Operations
# -----------------------------------------
# Logical operators (and, or, not) are used to combine conditional statements.

# Example 4: Using logical operators
height = 175
weight = 70
if height > 170 and weight > 65:
    print("You are fit for the sports team.")
else:
    print("You do not meet the physical requirements for the sports team.")

# Example 5: Combining conditions with or
day = "Sunday"
if day == "Saturday" or day == "Sunday":
    print("It's the weekend!")
else:
    print("It's a weekday.")

# Assignment 2: Create a script that checks if a person is eligible for a senior citizen discount based on age and residency.
# Write your code below:
# Input: Age and residency status
age = int(input("Enter your age: "))
residency = input("Are you a resident? (yes/no): ").strip().lower()

# Check eligibility using logical operators
if age >= 60 and residency == "yes":
    print("You are eligible for the senior citizen discount.")
else:
    print("You are not eligible for the senior citizen discount.")


# Section 3: Real-World Applications
# -----------------------------------
# Applying conditional logic to solve real-world problems.

# Example 6: Nested if-elif-else in a real-world context
# Ticket pricing system with age and membership checks
age = 65
member = True

if age < 18:
    price = 10
elif age >= 18:
    if member:
        price = 15
    else:
        price = 20

    if age >= 65:
        price -= 5  # Discount for seniors

print(f"Ticket price: ${price}")

# Assignment 3: Write a script that simulates a basic login system. Check username and password correctness.
# Write your code below:
# Correct username and password (you can change them)
correct_username = "user123"
correct_password = "password123"

# Input from the user
username = input("Enter your username: ")
password = input("Enter your password: ")

# Check if both username and password are correct
if username == correct_username and password == correct_password:
    print("Login successful!")
else:
    print("Invalid username or password. Please try again.")


# Example 7: Loan Approval System
# This example uses multiple conditions to determine if an applicant qualifies for a personal loan.
income = 45000
credit_score = 700
employment_status = "employed"
existing_loans = False

if (income > 40000 and credit_score >= 650) and (employment_status == "employed" and not existing_loans):
    print("Loan approved.")
else:
    print("Loan denied.")

# Example 8: Environment Control System
# A system that adjusts temperature and humidity based on multiple sensor readings.
temperature = 22
humidity = 85
weather_outside = "rainy"

if temperature < 20 or (humidity > 80 and weather_outside == "rainy"):
    print("Turning on heating and dehumidifier.")
elif temperature > 30 or (humidity < 30 and weather_outside == "sunny"):
    print("Turning on air conditioning and humidifier.")
else:
    print("No change needed.")

# Example 9: Custom Shipping Logic
# Determine shipping costs based on weight, distance, and customer loyalty.
weight = 5  # in kilograms
distance = 300  # in kilometers
is_loyal_customer = True

if weight > 10:
    shipping_cost = 25
elif weight > 5:
    shipping_cost = 15
else:
    shipping_cost = 5

if distance > 200:
    shipping_cost += 10

if is_loyal_customer:
    shipping_cost *= 0.9  # 10% discount for loyal customers

print(f"Total shipping cost: ${shipping_cost:.2f}")

# Assignment 4: Implement a system that categorizes a day based on temperature and weather conditions.
# Use nested if-elif-else and logical operators to determine if it's a beach day, skiing day, or a stay-home day.
# Get user input for temperature and weather condition
temperature = float(input("Enter the temperature (in Celsius): "))  # Get temperature as a float
weather_condition = input("Enter the weather condition (sunny, cloudy, rainy, snowy): ").lower()  # Get weather condition and convert to lowercase

# Categorizing the day based on temperature and weather
if temperature > 25:
    if weather_condition == "sunny":
        print("It's a beach day!")
    elif weather_condition == "cloudy":
        print("It's a good day for a walk.")
    elif weather_condition == "rainy":
        print("It's too wet for the beach, stay indoors.")
    else:
        print("It's hot but snowy, stay home.")
elif 15 <= temperature <= 25:
    if weather_condition == "sunny":
        print("Great for outdoor activities, maybe a hike.")
    elif weather_condition == "cloudy":
        print("Good for a walk or exploring the outdoors.")
    elif weather_condition == "rainy":
        print("Might want to stay indoors or go for an indoor activity.")
    elif weather_condition == "snowy":
        print("Skiing day! Perfect for the slopes.")
else:
    if weather_condition == "sunny":
        print("It's cold but sunny, great for a stay-home day.")
    elif weather_condition == "cloudy":
        print("Stay home, it's too cold and cloudy outside.")
    elif weather_condition == "rainy":
        print("Stay home, it's too cold and rainy.")
    elif weather_condition == "snowy":
        print("A snowy day, perfect for skiing.")

# Congratulations on completing the advanced section on Python conditional statements!
# Review the assignments, try to solve them, and check your understanding of control flow in Python.
