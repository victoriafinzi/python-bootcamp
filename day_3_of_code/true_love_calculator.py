"""
True Love calculator
Take both people's names and check for the number of times the letters in the word TRUE occurs. 
Then check for the number of times the letters in the word LOVE occurs. 
Then combine these numbers to make a 2 digit number.
"""

name_one = input("What's your first and lastname? ")
name_two = input("What's your lover first and lastname?")

combined_names = name_one + name_two
lower_case_names = combined_names.lower()

t = lower_case_names.count("t")
r = lower_case_names.count("r")
u = lower_case_names.count("u")
e = lower_case_names.count("e")

true = t + r + u + e

l = lower_case_names.count("l")
o = lower_case_names.count("o")
v = lower_case_names.count("v")
e = lower_case_names.count("e")

love = l + o + v + e

love_score = str(true) + str(love)

if int(love_score) <= 10 or int(love_score) >= 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif int(love_score) >=40 and int(love_score) <= 50:
    print(f"Your score is {int(love_score)}, you are alright together ")
else:
    print(f"Your score is {int(love_score)}.")