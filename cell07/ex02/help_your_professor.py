#!/usr/bin/env python3

# Define the average method
def average(class_dict):
    # Calculate the average score by dividing the sum of the scores by the number of students
    return sum(class_dict.values()) / len(class_dict)

# Example usage
class_3B = {
    "marine": 18,
    "jean": 15,
    "coline": 8,
    "luc": 9
}

class_3C = {
    "quentin": 17,
    "julie": 15,
    "marc": 8,
    "stephanie": 13
}

# Print the averages for the two classes
print(f"Average for class 3B: {average(class_3B)}.")
print(f"Average for class 3C: {average(class_3C)}.")
