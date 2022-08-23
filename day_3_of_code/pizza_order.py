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

input_pizza_size = input("What size of pizza do you want? S / M / L ")
input_add_peperoni = input("Do you want add pepperoni? Y / N ")
input_extra_cheese = input("Do you want to add extra cheese? Y / N ")

bill = 0

if input_pizza_size == "S":
    bill += 15
elif input_pizza_size == "M":
    bill += 20
elif input_pizza_size == "L":
    bill += 25

if input_add_peperoni == "Y":
    if input_pizza_size == "S":
        bill += 2
    else:
        bill += 3

if input_extra_cheese == "Y":
    bill += 1

print(f"Your final bill is ${bill}")
