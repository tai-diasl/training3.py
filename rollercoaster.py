print("Welcome to the rollercoaster!")

ticket = 0

height = int(input("Please, enter your height, in cm: "))

if height >= 120:
    age = int(input("Now, enter your age: "))
    if age < 12:
        age_group = "Child"
        ticket = 5
    elif age < 18:
        age_group = "Youth"
        ticket = 7
    elif 45 <= age <= 55:
        age_group = "Special category"
        ticket = 0
        print("\n** Everything is going to be ok. Have free ride on us. **")
    else:
        age_group = "Adult"
        ticket = 12

    print(f"\n{age_group} tickets are €{ticket}.")

    photo = input("Would you like to have a photo for an extra €3? [yes/no]? ")

    photo_lower = photo.lower()
    if photo_lower == "yes":
        ticket += 3
    print(f"\nThe total bill is €{ticket}.")
else:
    print("Sorry, you have to grow taller.")