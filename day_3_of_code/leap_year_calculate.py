"""
This is how you work out whether if a particular year is a leap year.

on every year that is evenly divisible by 4 
**except** every year that is evenly divisible by 100 
**unless** the year is also evenly divisible by 400
"""

input_year = int(input("Enter a year to know if it is leap or not: "))

if input_year % 4 == 0:
    if input_year % 100 == 0:
        if input_year % 400 == 0:
            print("Leap year!")
        else:
            print("Not leap!")
    else:
        print("Leap year! ")
else: 
    print("not leap")