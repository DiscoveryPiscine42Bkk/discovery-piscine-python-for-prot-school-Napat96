#!/usr/bin/env python3

# Define the array_of_names method
def array_of_names(names_dict):
    # Build the list of full names, capitalizing the first letter of first and last names
    full_names = [f"{first.capitalize()} {last.capitalize()}" for first, last in names_dict.items()]
    return full_names

# Example usage
persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}

# Print the result of calling array_of_names
print(array_of_names(persons))
