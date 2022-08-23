import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
possible_choices = [rock, paper, scissors]

player_choice = int(input("What's your choice? Type 0 for Rock, 1 for paper or 2 for scissors? "))
print(possible_choices[player_choice])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(possible_choices[computer_choice])


if player_choice == 0 and computer_choice == 1: 
    print("You lose!")
elif player_choice == 0 and computer_choice == 2:
    ("You win!")
elif player_choice == 1 and computer_choice == 2:
    print("You lose!")
elif player_choice == 1 and computer_choice == 0:
    print("You win!")
elif player_choice == 2 and computer_choice == 0:
    print("You lose!")
elif player_choice == 2 and computer_choice == 1:
    print("You win!")
else:
    print("Draw!")


