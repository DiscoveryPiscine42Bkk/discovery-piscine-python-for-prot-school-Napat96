#!/usr/bin/env python3
import sys

# Check if exactly one parameter is given
if len(sys.argv) == 2:
    # Prompt the user to enter a word
    user_input = input("Enter a word: ")
    
    # Compare the entered word with the passed parameter
    if user_input == sys.argv[1]:
        print("Good job!")
    else:
        print("Nope, sorry...")
else:
    print("none")  # If the number of parameters is not 1, print "none"
