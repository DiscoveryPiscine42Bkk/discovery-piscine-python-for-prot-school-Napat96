#!/usr/bin/env python3
import sys

# Define the downcase_it method
def downcase_it(input_string):
    return input_string.lower()

# Check if there are no parameters
if len(sys.argv) == 1:
    print("none")
else:
    # Apply the downcase_it method to each parameter and print the result
    for param in sys.argv[1:]:
        print(downcase_it(param))
