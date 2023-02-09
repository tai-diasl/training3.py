# Odd or Even program

num = int(input("Which number would you like to check? "))

if num % 2 == 0:
    res = "EVEN"
else:
    res = "ODD"

print(f">> {num} is an {res} number.")