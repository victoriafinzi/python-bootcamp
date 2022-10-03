import random
from art import logo, vs
from game_data import data

end_of_game = False

points = 0

while not end_of_game:
    choice_one = random.choice(data)
    choice_two = random.choice(data)
    #print(logo)
    print(f"Compare A: {choice_one['name']}, a {choice_one['description']}, from {choice_one['country']}" )
    print(vs)
    print(f"Compare B: {choice_two['name']} a  {choice_two['description']}, from {choice_two['country']}")
    answer = input("Who has more followers on Instagram? Type 'A' or 'B': ")
    if answer == 'A':
        if choice_two['follower_count'] < choice_one['follower_count']:
            print('you got it!')
            points += 1
        else:
            print("you're wrong!")
            print(f"You made: {points} points")
            end_of_game = True
    elif answer == 'B':
        if choice_two['follower_count'] > choice_one['follower_count']:
            print('you got it!')
            points += 1
        else:
            print("you're wrong!")
            print(f"You made: {points} points")
            end_of_game = True