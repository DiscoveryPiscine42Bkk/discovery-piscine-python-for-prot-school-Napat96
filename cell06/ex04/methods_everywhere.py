#!/usr/bin/env python3
import sys

# Define the shrink method
def shrink(input_string):
    print(input_string[:8])  # Display the first 8 characters of the string

# Define the enlarge method
def enlarge(input_string):
    print(input_string.ljust(8, 'Z'))  # Pad the string with 'Z' to make it 8 characters

# Check if there are any parameters
if len(sys.argv) < 2:
    print("none")
else:
    # Process each argument
    for arg in sys.argv[1:]:
        if len(arg) > 8:
            shrink(arg)
        elif len(arg) < 8:
            enlarge(arg)
        else:
            print(arg)
