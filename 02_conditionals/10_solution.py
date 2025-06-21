# Pet Food Recommendation
pet_species = "Dog"
pet_age = 29

if pet_species == 'Dog':
    if (pet_age < 2):
        print("Puppy Food")
    else:
        print("Adult Dog Food")
elif pet_species == 'Cat':
    if (pet_age < 5):
        print("Kitten Food")
    else:
        print("Senior Cat Food")
