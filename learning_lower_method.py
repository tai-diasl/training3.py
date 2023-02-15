print("Welcome to the Love Calculator")

name1 = input("What is your name? ")
name2 = input("What is their name? ")

combined_names = (name1 + name2).lower()

true = 0
love = 0

true += combined_names.count("t")
true = combined_names.count("r")
true += combined_names.count("u")
true += combined_names.count("e")


love += combined_names.count("l")
love += combined_names.count("o")
love += combined_names.count("v")
love += combined_names.count("e")


true_string = str(true)
love_string = str(love)

score = true_string + love_string
love_score = int(score)

if love_score < 10 or love_score > 90:
    print(f"Your score id {love_score}, you go together like coke and mentos.")
elif love_score >= 40 or love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")