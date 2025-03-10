#!/usr/bin/env python3
import sys

# Check if exactly one parameter is given
if len(sys.argv) == 2:
    print(sys.argv[1].upper() + "$")  # Convert to uppercase and add "$"
else:
    print("none$")
