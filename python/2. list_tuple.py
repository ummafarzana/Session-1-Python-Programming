# Advanced Python: Lists and Tuples

"""
Author: Kalim Amzad Chy
Email: kalim.amzad.chy@gmail.com

This Python script is designed to provide an in-depth understanding of Python lists and tuples.
We will explore:
1. Lists - Creation, accessing elements, operations, and methods.
2. Tuples - Characteristics, usage, and differences from lists.
3. Advanced applications including 1D and 2D lists, and lists with mixed data types.

Each section includes detailed explanations, examples, and challenging assignments.
"""

# Section 1: Python Lists
# -----------------------
# Lists in Python are ordered, mutable (changeable), and allow duplicate elements.

# Example 1: Creating Lists
simple_list = [8, 2, 9, 4, 5]
mixed_list = [1, "Hello", 3.14, True]
temp_list = []  # Empty list
empty_list = list()

# 2D List (List of Lists)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Accessing Elements
# You can access elements by their index, which starts at 0.
first_element = simple_list[2]  # Outputs 9
second_row_first_col = matrix[1][2]  # Outputs 4
list_range = simple_list[1:4] # Outputs [2, 9, 4]
# list_stepping = simple_list[1:7:2]
list_stepping = simple_list[::2]
print(first_element)
print(second_row_first_col)
print("List Stepping: ", list_stepping)
print("List Range: ", list_range)

# List Operations
# Adding elements
print("Before Apprend Operation: ", simple_list)
simple_list.append(6)  # Adds 6 to the end
print("After Append operation: ", simple_list)
simple_list.insert(2, 6)  # Inserts 0 at the beginning
print("After Insert operation: ", simple_list)

# Removing elements
simple_list.remove(6)  # Removes the first occurrence of 6
print("After Remove operation: ", simple_list)
popped_element = simple_list.pop()  # Removes and returns the last element
print("Popped element:", popped_element)
print("After Pop operation: ", simple_list)

# List Methods
# Join lists
combined_list = simple_list + mixed_list
print("Combined List: ", combined_list)

# Sort lists
simple_list.sort()  # Sorts the list in place
print("Sorted List: ", simple_list)

# Copy a list
duplicate_list = simple_list

duplicate_list.append(7)
print("simple_list id", id(simple_list), "duplicate_list id: ", id(duplicate_list))
print("Duplicate List: ", duplicate_list)
print("Simple List: ", simple_list)

list_copy = simple_list.copy()
list_copy.append(8)
print("simple_list id", id(simple_list), "list_copy id: ", id(list_copy))
print("List Copy: ", list_copy)
print("Simple List: ", simple_list)

# Get the number of elements
list_length = len(simple_list)

# Assignment 1: Create a 2D list representing a 3x3 matrix and perform operations like accessing, modifying, and iterating through it.
# Write your code below:
# Create a 2D list representing a 3x3 matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Access elements in the matrix
print("Access element at row 1, column 2:", matrix[0][1])  # Access 2 (row 0, column 1)

# Modify an element in the matrix
matrix[1][1] = 10  # Change the center element (5) to 10
print("Modified matrix:")
for row in matrix:
    print(row)

# Iterate through the matrix and print each element
print("Iterating through the matrix:")
for i in range(len(matrix)):  # Loop through rows
    for j in range(len(matrix[i])):  # Loop through columns
        print(f"Element at ({i},{j}):", matrix[i][j])

# Section 2: Python Tuples
# ------------------------
# Tuples are ordered collections like lists but are immutable (cannot be changed after creation).

# Example 2: Creating and Using Tuples
simple_tuple = (1, 2, 3, 4, 5)
mixed_tuple = (1, "Hello", 3.14, True)
temp_tuple = ()  # Empty tuple
empty_tuple = tuple()


# simple_tuple[2] = 76768  # This will raise TypeError as tuples are immutable
print(simple_tuple)

# Accessing elements
first_tuple_element = simple_tuple[0]

# Tuples are immutable
# Trying to change an element like below will raise a TypeError
# simple_tuple[0] = 0

# Tuples can be used as keys in dictionaries because of their immutability
tuple_dict = {simple_tuple: "My Tuple"}

# Assignment 2: Create a tuple with mixed data types and demonstrate its potential use cases in data structures like dictionaries.
# Write your code below:
# Create a tuple with mixed data types
mixed_data_tuple = ("MD", 25, 5.6, False)  # Name, age, height, is_student

# Use the tuple as a key in a dictionary
profile_data = {
    mixed_data_tuple: {
        "job": "Software Developer",
        "city": "New York",
        "hobbies": ["Reading", "Traveling", "Swimming"]
    }
}

# Access and manipulate the dictionary
print("Profile Data using Tuple Key:")
print(profile_data[mixed_data_tuple])

# Add another entry to the dictionary using a new tuple key
another_tuple = ("Hossain", 32, 6.0, True)
profile_data[another_tuple] = {
    "job": "Data Scientist",
    "city": "San Francisco",
    "hobbies": ["Gaming", "Cooking"]
}

# Iterate through the dictionary and print each tuple and its associated data
print("\nIterating through the profile data:")
for key, value in profile_data.items():
    print(f"Key (tuple): {key}")
    print(f"Value (profile): {value}")

# Demonstrate that tuples are immutable
try:
    mixed_data_tuple[1] = 30  # Attempt to modify the tuple
except TypeError as e:
    print("\nError:", e)

# Section 3: Advanced Applications
# --------------------------------
# Dealing with more complex list and tuple structures for real-world applications.

# Example 3: Advanced List Operations
# Filtering with list comprehensions
# even_numbers = [x for x in simple_list if x % 2 == 0]

# for x in simple_list:
#     if x%2==0:
#         print("Even: ", x)

even_numbers = [x for x in simple_list if x % 2 ==0]

print(even_numbers)


# Nested list comprehensions for 2D list transformations
incremented_matrix = [[cell + 1 for cell in row] for row in matrix]

# Assignment 3: Create a list of tuples, where each tuple contains a student's name and their grade. Sort this list by grades.
# Write your code below:
# Create a list of tuples with student names and their grades
students = [
    ("Rakhi", 85),
    ("Rubayat", 72),
    ("Monika", 90),
    ("Ratul", 65),
    ("Imran", 78)
]

# Sort the list by grades (second item in each tuple)
students_sorted_by_grades = sorted(students, key=lambda student: student[1])

# Print the sorted list
print("Students sorted by grades:")
for student in students_sorted_by_grades:
    print(student)

# Congratulations on completing the advanced section on Python lists and tuples!
# Review the assignments, try to solve them, and check your understanding of these versatile data structures.
