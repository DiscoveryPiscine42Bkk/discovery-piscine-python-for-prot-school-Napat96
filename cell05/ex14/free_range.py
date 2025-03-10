#!/usr/bin/env python3
import sys

# Check if exactly two parameters are passed
if len(sys.argv) == 3:
    # Convert the parameters to integers
    start = int(sys.argv[1])
    end = int(sys.argv[2])

    # Create an array using range with the two numbers
    result = list(range(start, end))

    # Display the array
    print(result)
else:
    print("none")  # If there are not exactly two parameters, print "none"
