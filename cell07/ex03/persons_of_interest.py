#!/usr/bin/env python3

# Define the famous_births method
def famous_births(persons_dict):
    # Sort the dictionary by the 'date_of_birth' key
    sorted_persons = sorted(persons_dict.items(), key=lambda x: x[1]['date_of_birth'])
    
    # Display the sorted persons with their birth years
    for key, value in sorted_persons:
        print(f"{value['name']} is a great scientist born in {value['date_of_birth']}.")

# Example usage
women_scientists = {
    "ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
    "cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
    "lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
    "grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}

# Call the method to display the famous births
famous_births(women_scientists)
