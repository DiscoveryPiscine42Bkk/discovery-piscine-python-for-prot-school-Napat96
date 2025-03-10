#!/usr/bin/env python3

# Define the greetings method
def greetings(name="noble stranger"):
    # Check if the name is a string
    if isinstance(name, str):
        print(f"Hello, {name}.")
    else:
        print("Error! It was not a name.")

# Test the method with different arguments
greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)
