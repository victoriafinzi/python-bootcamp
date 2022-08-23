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