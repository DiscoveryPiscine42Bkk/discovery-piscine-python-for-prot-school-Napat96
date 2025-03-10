#!/usr/bin/env python3

# Define the original array
original_array = [2, 8, 9, 48, 8, 22, -12, 2]

# Create a new array by adding 2 to each element, but only if it's greater than 5
new_array = [x + 2 for x in original_array if x > 5]

# Remove duplicates while maintaining order
unique_new_array = list(dict.fromkeys(new_array))

# Display both arrays
print("Original array:", original_array)
print("New array:", unique_new_array)
