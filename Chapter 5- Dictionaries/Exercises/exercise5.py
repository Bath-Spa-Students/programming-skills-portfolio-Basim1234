#Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the owner’s name. Store these dictionaries in a list called pets. Next, loop through your list and asyou do, print everything you know about each pet

# Make an empty list to store the pets in.
pets = []

# Make individual pets, and store each one in the list.
pet = {
    'animal type': 'cat',
    'name': 'tommy',
    'owner': 'elsa',
    'weight': 7,
    'eats': 'oats',
}
pets.append(pet)

pet = {
    'animal type': 'horse',
    'name': 'lama',
    'owner': 'doreaemon',
    'weight': 56,
    'eats': 'grass',
}
pets.append(pet)

pet = {
    'animal type': 'dog',
    'name': 'paul',
    'owner': 'kioo',
    'weight': 25,
    'eats': 'meat',
}
pets.append(pet)

# Display information about each pet.
for pet in pets:
    print("\nHere's what I know about " + pet['name'].title() + ":")
    for key, value in pet.items():
        print("\t" + key + ": " + str(value))