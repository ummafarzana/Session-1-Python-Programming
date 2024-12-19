# Advanced Python: Strings

"""
Author: Kalim Amzad Chy
Email: kalim.amzad.chy@gmail.com

This Python script is designed to provide a comprehensive understanding of Python strings.
We will explore:
1. String basics - Creation, accessing, and updating.
2. All string methods and their uses.
3. Practical applications of strings in data manipulation.

Each section includes detailed explanations, examples, and challenging assignments.
"""

# Section 1: String Basics
# ------------------------
# Strings in Python are sequences of characters.

# Example 1: Creating and Using Strings
simple_string = "Hello, Python learners!"
# print(simple_string[0])  # Accessing the first character

# Strings are immutable
# Trying to change a character directly will raise a TypeError
# simple_string[0] = "h"  # Uncommenting this line will cause an error

# String Methods
# Finding substrings
# print(simple_string.find('python'))  # Returns the start index of 'Python'

# Replacing substrings
modified_string = simple_string.replace('learners', 'developers')
print("Modified String:", modified_string)

# Splitting strings
# print(simple_string)

marks = "80: 83: 70: 48: 47"
marks_list = marks.split(': ')  # Splits the string into a list of marks
print("Array of marks:", marks_list)

words = simple_string.split(', ')  # Splits the string into a list of words
print("Array of words:", words)

# Joining strings
joined_string = '-'.join(marks_list)  # Joins the list back into a single string
print("Joined string:", joined_string)

# Case conversion
# print(simple_string.upper())  # Converts to uppercase
# print(simple_string.lower())  # Converts to lowercase

# Stripping whitespace
user_input = "   some user input   "
# print(user_input)
# print(user_input.strip())  # Removes leading and trailing whitespace
# print(user_input.rstrip())  # Removes trailing whitespace
# print(user_input.lstrip())  # Removes leading whitespace

# Assignment 1: Create a string that contains a simple bio data like name, age, and country. Extract each piece of information and print them separately.
# Write your code below:
# Creating a string with bio data
bio_data = "Name: Farzana, Age: 23, Country: Bangladesh"

# Extracting each piece of information
name = bio_data[bio_data.find("Name:") + len("Name: "):bio_data.find(", Age:")]
age = bio_data[bio_data.find("Age:") + len("Age: "):bio_data.find(", Country:")]
country = bio_data[bio_data.find("Country:") + len("Country: "):]

# Printing each piece of information
print("Name:", name.strip())
print("Age:", age.strip())
print("Country:", country.strip())

# Section 2: Advanced String Operations
# -------------------------------------
# Strings can be used in more complex operations like formatting.

# Example 2: String Formatting
name = "Alice"
age = 30
greeting = f"Hello, my name is {name} and I am {age} years old."
print(greeting)

# Old-style formatting
old_greeting = "Hello, my name is %s and I am %d years old." % (name, age)
print(old_greeting)


# Assignment 2: Create a formatted string that includes data from a list or dictionary. For example, use a dictionary to store a person's information and format a string to include it.
# Write your code below:
# Creating a dictionary with a person's information
person_info = {
    "name": "John",
    "age": 28,
    "country": "USA",
    "profession": "Software Engineer"
}

# Formatting a string to include data from the dictionary
formatted_string = (
    f"My name is {person_info['name']}. "
    f"I am {person_info['age']} years old. "
    f"I live in {person_info['country']} and work as a {person_info['profession']}."
)

# Printing the formatted string
print(formatted_string)

# Section 3: Advanced Slicing and Multiline Strings
# -------------------------------------
# Python strings are immutable, which means that every string operation creates a new string.

# Example 1: Advanced Slicing
complex_string = "Hello, Python enthusiasts!"
reverse_string = complex_string[::-1]  # Reverses the string using slicing
# print(reverse_string)

# Multiline strings
multiline_string = """This is a string that spans
multiple lines within triple quotes."""
# print(multiline_string)

# Raw strings
path = r"C:\new_folder\test.txt"  # Raw string ignores escape characters
print(path)

# String Methods
# Counting substrings
# print("The count of 'n' is:", complex_string.count('n'))

# Formatting strings with str.format() and f-strings
pi = 3.14159
formatted_string = "The value of pi is {:.2f}".format(pi)  # Formatting to two decimal places
# print(formatted_string)

# Assignment 3: Write a function that takes a string and returns a dictionary with the counts of each character in the string.
# Write your code below:
def count_characters(input_string):
    # Create an empty dictionary to store the character counts
    char_count = {}
    
    # Loop through each character in the string
    for char in input_string:
        # If the character is already in the dictionary, increment its count
        if char in char_count:
            char_count[char] += 1
        else:
            # Otherwise, add it to the dictionary with count 1
            char_count[char] = 1
    
    return char_count

# Example usage of the function
test_string = "hello, python enthusiasts!"
char_count_result = count_characters(test_string)

# Printing the result
print(char_count_result)

# Section 4: Regular Expressions
# ------------------------------
# Regular expressions are used for pattern matching in strings.


import re

# Basic Regex: Matching Literal Strings
pattern = 'earth'
text = 'Hello, world!'
match = re.search(pattern, text)
if match:
    print("Match found:", match.group())
else:
    print("No match found.")


# Character Classes
pattern = r'\d+'  # Matches one or more digits
text = 'There are 123 apples, 45 oranges, and 78 bananas.'
matches = re.findall(pattern, text)
print("Numbers found:", matches)

# Alternation and Grouping
pattern = r'apple|banana'  # Matches 'apple' or 'banana'
text = 'I like apples, oranges.'
matches = re.findall(pattern, text)
print("Fruits found:", matches)


# Positive Lookahead
pattern = r'\d{3}(?=px)'  # Matches a number only if it's followed by 'px'
text = 'The 487 image is 106px by 209px.'
matches = re.findall(pattern, text)
print("Numbers followed by 'px':", matches)

# Non-capturing Group
pattern = r'(?:\d{3}-)?\d{3}-\d{4}'  # Matches phone numbers with optional area code
text = 'Call 415-555-1234 or 555-4321 or 008-718-6897'
matches = re.findall(pattern, text)
print("Phone numbers found:", matches)


# Example: Email Validation
# A more detailed regex for validating an email address.
email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
email = "example@domain.com"
email = "example@domain"
if re.match(email_regex, email):
    print("Valid email!")
else:
    print("Invalid email!")


# Example: Extracting Phone Numbers
# Regex to match US phone number formats
phone_regex = r"\b\d{3}[-.]?\d{3}[-.]?\d{4}\b"
text = "Call me at 415-555-1011 tomorrow, or 564-9712 or at 415.555.9999 for office line."
phones = re.findall(phone_regex, text)
print("Phone numbers found:", phones)

# Example: Replacing Text
# Replacing all occurrences of digits with a placeholder
replaced_text = re.sub(r'\d', 'X', 'My number: 12345, office: 98765')
print("Censored text:", replaced_text)

# Assignment: Write a regex to find all the hashtags in a string.
text_with_hashtags = "This is a #great day to learn #regex in #Python!"
# Regular expression to match hashtags
hashtag_pattern = r'#\w+'  # Matches '#' followed by one or more word characters (letters, digits, underscores)

# Example text with hashtags
text_with_hashtags = "This is a #great day to learn #regex in #Python!"

# Using re.findall to find all hashtags
hashtags = re.findall(hashtag_pattern, text_with_hashtags)

# Printing the result
print("Hashtags found:", hashtags)

# Assignments: Write a regex to find the Bangladesh phone number with all variations.
# 01454565767
# +880196345634
# 0088785674657
# 01845-567567

import re

# Regular expression to match Bangladesh phone numbers with all variations
bangladesh_phone_regex = r"\b(\+880|\d{3}-?)?\d{3}-?\d{6}\b"

# Example text with Bangladesh phone numbers in different formats
text_with_phones = "Here are some Bangladesh phone numbers: 01454565767, +880196345634, 0088785674657, 01845-567567"

# Using re.findall to find all Bangladesh phone numbers
bangladesh_phones = re.findall(bangladesh_phone_regex, text_with_phones)

# Printing the result
print("Bangladesh phone numbers found:", bangladesh_phones)

# Congratulations on completing the advanced section on Python strings!
# Review the assignments, try to solve them, and check your understanding of string manipulation techniques.
