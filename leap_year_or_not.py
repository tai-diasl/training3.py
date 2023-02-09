# Checks whether a year was, is or will be a leap year

print("| :: | Leap Year or Not? | :: |\n")

year = int(input("Which year would you like to check? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            res = "a leap year"
        else:
            res = "not a leap year"
    else:
        res = "a leap year"
else:
    res = "not a leap year"

current_year = int(input("Enter the current year: "))

if year < current_year:
    to_be = "was"
elif year > current_year:
    to_be = "will be"
else:
    to_be = "is"

print(f"\nThe year of {year} {to_be} {res}.")
