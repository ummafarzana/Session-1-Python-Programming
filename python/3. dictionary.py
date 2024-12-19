# Advanced Python: Dictionaries

"""
Author: Kalim Amzad Chy
Email: kalim.amzad.chy@gmail.com

This Python script is designed to provide a comprehensive understanding of Python dictionaries.
We will explore:
1. Dictionary basics - Creation, accessing, and updating.
2. All dictionary methods and their uses.
3. Integrating dictionaries with lists and tuples for complex data structures.

Each section includes detailed explanations, examples, and challenging assignments.
"""

# Section 1: Dictionary Basics
# ----------------------------
# Dictionaries in Python are unordered collections that store data in key-value pairs.

# Example 1: Creating and Using Dictionaries
simple_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
print(simple_dict["city"])
# print(simple_dict['address'])  # Accessing value by key
print(simple_dict.get('age', 0))  # Accessing value by key
print(simple_dict.get('address', 'Texas'))  # Accessing value by key


# Updating dictionary
simple_dict['age'] = 31  # Updates the age
simple_dict['country'] = 'USA'  # Adds a new key-value pair
# print("Updated Dictionary: ", simple_dict)

# Dictionary Methods
# keys(), values(), items()
print(simple_dict.keys())  # Prints all keys
print(simple_dict.values())  # Prints all values
print(simple_dict.items())  # Prints all key-value pairs as tuples

# get()
print(simple_dict.get('name'))  # Returns 'John'

# pop()
removed_value = simple_dict.pop('country')  # Removes 'country' key and returns its value
print("Removed Value:", removed_value)
print("Dictionary after pop(): ", simple_dict)

# popitem()
last_item = simple_dict.popitem()  # Removes and returns the last inserted key-value pair
print("Last Item:", last_item)
print("Dictionary after popitem(): ", simple_dict)

# update()
simple_dict.update({'age': 32, 'email': 'john@example.com'})  # Updates the dictionary
print("Dictionary after update(): ", simple_dict)

# clear()
# simple_dict.clear()  # Empties the dictionary
# print("Dictionary after clear(): ", simple_dict)

# copy()
dict_copy = simple_dict.copy()  # Creates a shallow copy of the dictionary
print("Dictionary Copy: ", dict_copy)

# Assignment 1: Create a dictionary representing a student with keys like 'name', 'roll_number', 'grades' (a list of subjects and marks).

student = {
    "name": "Ahona",
    "roll_number": 2024,
    "grades": {
        "Math": 95,
        "Physics": 88,
        "Chemistry": 91,
        "English": 87
    }
}

# Access and display information from the dictionary
print("Student Information:")
print(f"Name: {student['name']}")
print(f"Roll Number: {student['roll_number']}")
print("Grades:")
for subject, marks in student["grades"].items():
    print(f"  {subject}: {marks}")

# Adding a new subject and grade
student["grades"]["History"] = 89

# Updating a grade
student["grades"]["Math"] = 97

# Deleting a subject
removed_subject = student["grades"].pop("Physics", None)

# Display updated dictionary
print("\nUpdated Student Information:")
print(f"Name: {student['name']}")
print(f"Roll Number: {student['roll_number']}")
print("Grades:")
for subject, marks in student["grades"].items():
    print(f"  {subject}: {marks}")

if removed_subject:
    print("\nRemoved Subject - Physics: ", removed_subject)

# Section 2: Integrating Dictionaries with Lists and Tuples
# ---------------------------------------------------------
# Dictionaries can be used with lists and tuples to create complex data structures.

# Example 2: List of Dictionaries
students = [
    {'name': 'Alice', 'grade': 85},
    {'name': 'Bob', 'grade': 90},
    {'name': 'Charlie', 'grade': 78}
]

# Sorting list of dictionaries by grade
students_sorted_by_grade = sorted(students, key=lambda x: x['grade'], reverse=True)
print("Students sorted by grade: ", students_sorted_by_grade)

# Example 3: Dictionary of Tuples
# Using tuples as keys
coordinates_info = {(35.6895, 139.6917): "Tokyo", (40.7128, -74.0060): "New York"}

# Assignment 2: Create a dictionary where keys are student names and values are lists of grades. Calculate the average grade for each student.
# Write your code below:
student_grades = {
    "Ahona": [85, 90, 78],
    "Mehedi": [92, 88, 84],
    "Chomok": [76, 85, 80]
}

# Calculate the average grade for each student
average_grades = {name: sum(grades) / len(grades) for name, grades in student_grades.items()}

# Display the average grades
print("Average Grades:")
for student, avg_grade in average_grades.items():
    print(f"{student}: {avg_grade:.2f}")

# Add a new student with grades
student_grades["David"] = [89, 92, 95]

# Update average grades after adding the new student
average_grades = {name: sum(grades) / len(grades) for name, grades in student_grades.items()}

# Display updated dictionary
print("\nUpdated Average Grades:")
for student, avg_grade in average_grades.items():
    print(f"{student}: {avg_grade:.2f}")

# Congratulations on completing the advanced section on Python dictionaries!
# Review the assignments, try to solve them, and check your understanding of this powerful data structure.
