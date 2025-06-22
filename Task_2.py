# Task 2: Create a Personalized Greeting
# Problem Statement: Write a Python program that:
# 1.  Takes a user's first name and last name as input.
# 2.  Concatenates the first name and last name into a full name.
# 3.  Prints a personalized greeting message using the full name.

a=str(input("Enter your first name:"))
b=str(input("Enter your last name:"))
full_name = f"{a} {b}"
print(f"\nHello, {full_name}! Welcome to the Python program.")