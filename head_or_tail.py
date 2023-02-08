# Create a program that plays Head or Tail
# I could have chosen the numbers 0 and 1, but I wanted to take the opportunity to use the modulus operator.

import random

num = random.randint(0, 10)
#print(num)

if num % 2 == 0:
    print("Head")
else:
    print("Tail")
