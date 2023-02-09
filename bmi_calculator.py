"""
Body mass index (BMI) is a measure of body fat based on height and weight
that applies to adult men and women.
"""

print("| :: | BMI Calculator | :: |\n")

height = float(input("Please, enter your height in m: "))
weight = float(input("Now, enter your weight in kg: "))

bmi = round(weight / (height ** 2), 1)

if bmi < 18.5:
    status = "you are underweight"
elif bmi < 25:
    status = "you have a normal weight"
elif bmi < 30:
    status = "you are slightly overweight"
elif bmi < 35:
    status = "you are obese"
else:
    status = "you are clinically obese"

print(f"\nYour BMI is {bmi}, {status}.")
