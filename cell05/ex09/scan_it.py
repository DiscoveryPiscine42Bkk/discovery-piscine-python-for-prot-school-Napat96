#!/usr/bin/env python3
import sys

# Check if exactly two parameters are given
if len(sys.argv) == 3:
    keyword = sys.argv[1]  # First parameter: the keyword
    text = sys.argv[2]     # Second parameter: the string to search in

    # Count the occurrences of the keyword in the text
    count = text.count(keyword)

    # If the keyword is found, display the count, otherwise display "none"
    if count > 0:
        print(count)
    else:
        print("none")
else:
    print("none")  # If there are not exactly two parameters, print "none"
