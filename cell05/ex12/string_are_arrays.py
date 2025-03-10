#!/usr/bin/env python3
import sys

# Check if exactly one parameter is passed
if len(sys.argv) == 2:
    # Get the string passed as a parameter
    input_string = sys.argv[1]
    
    # Count occurrences of 'z' and print "z" for each occurrence
    if 'z' in input_string:
        for char in input_string:
            if char == 'z':
                print("z")
    else:
        print("none")  # If there are no 'z' characters, print "none"
else:
    print("none")  # If the number of parameters is not 1, print "none"
