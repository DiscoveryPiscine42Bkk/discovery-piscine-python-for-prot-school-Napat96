#!/usr/bin/env python3
import sys

# Check if at least one parameter is given
if len(sys.argv) > 1:
    print(sys.argv[1] + "$")  # Print the first parameter followed by "$"
else:
    print("none$")  # Print "none$" if no parameters are passed
