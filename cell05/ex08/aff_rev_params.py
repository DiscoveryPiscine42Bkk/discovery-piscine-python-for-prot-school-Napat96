#!/usr/bin/env python3
import sys

# Check if there are at least two parameters
if len(sys.argv) > 1:
    # Print each parameter in reverse order
    for param in reversed(sys.argv[1:]):
        print(param)
else:
    print("none")  # If fewer than two parameters, print "none"
