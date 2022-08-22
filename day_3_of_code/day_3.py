"""
BMI calculator 2.0
Under 18.5 are underweight
Over 18.5 but below 25 they have a normal weight
Over 25 but below 30 they are overweight
Over 30 but below 35 they are obese
Above 35 they are clinically obese
"""

# input_person_weight = float(input("What is your weight in kg?"))
# input_person_height = float(input("What is your height in meters?"))
# bmi = round(input_person_weight/input_person_height**2)


# if bmi < 18.5:
#     print("You're underweight, you should look for a doctor.")
# elif bmi < 25:
#     print("Your weight is normal.")
# elif bmi < 30:
#     print("You're overweight")
# elif bmi < 35:
#     print("You're obese, you should look for a doctor")
# else: 
#     print("You're clinical obese, you should look for a doctor")

"""
This is how you work out whether if a particular year is a leap year.

on every year that is evenly divisible by 4 
**except** every year that is evenly divisible by 100 
**unless** the year is also evenly divisible by 400
"""

# input_year = int(input("Enter a year to know if it is leap or not: "))

# if input_year % 4 == 0:
#     if input_year % 100 == 0:
#         if input_year % 400 == 0:
#             print("Leap year!")
#         else:
#             print("Not leap!")
#     else:
#         print("Leap year! ")
# else: 
#     print("not leap")

"""
Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.

Based on a user's order, work out their final bill.

Small Pizza: $15
Medium Pizza: $20
Large Pizza: $25
Pepperoni for Small Pizza: +$2
Pepperoni for Medium or Large Pizza: +$3
Extra cheese for any size pizza: + $1
"""

# input_pizza_size = input("What size of pizza do you want? S / M / L ")
# input_add_peperoni = input("Do you want add pepperoni? Y / N ")
# input_extra_cheese = input("Do you want to add extra cheese? Y / N ")

# bill = 0

# if input_pizza_size == "S":
#     bill += 15
# elif input_pizza_size == "M":
#     bill += 20
# elif input_pizza_size == "L":
#     bill += 25

# if input_add_peperoni == "Y":
#     if input_pizza_size == "S":
#         bill += 2
#     else:
#         bill += 3

# if input_extra_cheese == "Y":
#     bill += 1

# print(f"Your final bill is ${bill}")

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