"""
BMI calculator 2.0
Under 18.5 are underweight
Over 18.5 but below 25 they have a normal weight
Over 25 but below 30 they are overweight
Over 30 but below 35 they are obese
Above 35 they are clinically obese
"""

input_person_weight = float(input("What is your weight in kg?"))
input_person_height = float(input("What is your height in meters?"))
bmi = round(input_person_weight/input_person_height**2)


if bmi < 18.5:
    print("You're underweight, you should look for a doctor.")
elif bmi < 25:
    print("Your weight is normal.")
elif bmi < 30:
    print("You're overweight")
elif bmi < 35:
    print("You're obese, you should look for a doctor")
else: 
    print("You're clinical obese, you should look for a doctor")