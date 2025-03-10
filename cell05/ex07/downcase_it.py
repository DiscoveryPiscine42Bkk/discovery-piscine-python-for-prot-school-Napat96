#!/usr/bin/env python3
import sys

# Check if exactly one parameter is given
if len(sys.argv) == 2:
    print(sys.argv[1].lower())  # Convert the input to lowercase and print
else:
    print("none")  # Print "none" if the number of parameters is not 1
