"""
Exercise one: Write a program that adds the digts in a 2 digit number. 
If the input was 35, then the output should be 3 + 5 = 8
"""

input_number = input("Write a number greater than 10:")
input_sum = int(input_number[0]) + int(input_number[1])
print(input_sum)

##############################################################################################################
"""
Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
The BMI is a measure of some's weight taking into account their height.
If a tall person and a short person both weigh the same amount, the short person is usually more overweight.
The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):
BMI = weight(kg)/height²(m²)
"""

input_person_weight = input("What is your weight in kg?")
input_person_height = input("What is your height in meters?")
bmi_calculation = int(input_person_weight)/float(input_person_height)**2
print(bmi_calculation)

##############################################################################################################
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

##############################################################################################################
"""
If the bill was $150.00, split between 5 people, with 12% tip.
Each person should pay (150.00 / 5) * 1.12 = 33.6
Format the result to 2 decimal places = 33.60
Thus everyone's share of the total bill is $30.00 plus a $3.60 tip.
"""
print("Welcome to the tip calculator!")
total_bill = input("What is the total bill?")
percentage_tip = input("What is the percentage tip?")
split_total_bill = input("How many people to split the bill?")
percentage_tip_calculate = (float(percentage_tip)/100) * float(total_bill)
total_payment = (float(total_bill)/int(split_total_bill)) + percentage_tip_calculate
final_amount = "{:.2f}".format(total_payment)
print(f"O total da conta para cada um será: R${final_amount}")
