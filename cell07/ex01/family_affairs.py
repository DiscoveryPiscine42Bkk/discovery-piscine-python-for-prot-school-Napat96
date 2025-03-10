#!/usr/bin/env python3

# Define the find_the_redheads method
def find_the_redheads(family_dict):
    # Use the filter function to get the first names of individuals with red hair
    redheads = list(filter(lambda name: family_dict[name] == 'red', family_dict))
    return redheads

# Example usage
dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"
}

# Print the result of calling find_the_redheads
print(find_the_redheads(dupont_family))
