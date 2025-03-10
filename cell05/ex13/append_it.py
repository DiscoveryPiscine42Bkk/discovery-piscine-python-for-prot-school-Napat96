#!/usr/bin/env python3
import sys

# Check if there are no parameters
if len(sys.argv) == 1:
    print("none")
else:
    # Iterate over each parameter passed
    for param in sys.argv[1:]:
        # Check if the parameter does not already end with "ism"
        if not param.endswith("ism"):
            print(param + "ism")
