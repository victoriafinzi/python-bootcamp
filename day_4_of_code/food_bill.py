
"""
You are going to write a program which will select a random name from a list of names. 
The person selected will have to pay for everybody's food bill.
Important: You are not allowed to use the choice() function.
Line 8 splits the string names_string into individual names and puts them inside a List called names. 
For this to work, you must enter all the names as name followed by comma then space. e.g. name, name, name
"""
# input_names = input("Give everybody's names, seperated by a comma: ")

# names = input_names.split(",")
# names_size = len(names)
# random_choice = random.randint(0, names_size - 1)
# person_who_will_pay = names[random_choice]
# print(f"Who will pay the bill is: {person_who_will_pay} !!")

###############################
#Smater way to do it: 

import random


input_names = input("Give everybody's names, seperated by a comma: ")
names = input_names.split(",")
unlucky_person = random.choice(names)
print(f"Who will pay the bill is: {unlucky_person} !!")
