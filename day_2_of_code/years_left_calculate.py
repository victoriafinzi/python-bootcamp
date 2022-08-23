"""
Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.
It will take your current age as the input and output a message with our time left in this format:
You have x days, y weeks, and z months left.
Where x, y and z are replaced with the actual calculated numbers.
"""

input_person_currently_age = input("What is your currently age?")
if int(input_person_currently_age) > 0 and int(input_person_currently_age) < 90:
    total_lived_years = 90
    years_left = 90 - int(input_person_currently_age)
    total_days_left = 365 * years_left
    total_weeks_left = 52 * years_left
    total_months_left = 12 * years_left
    print(f"You have {total_days_left} days, {total_weeks_left} weeks, {total_months_left} months left")
    total_days_lived = 365 * int(input_person_currently_age)
    total_weeks_lived = 52 * int(input_person_currently_age)
    total_months_lived = 12 * int(input_person_currently_age)
    print(f"You have alread lived {total_days_lived} days, {total_weeks_lived} weeks, {total_months_lived} months.")
else:
    print("Your age is out of our calculation")

