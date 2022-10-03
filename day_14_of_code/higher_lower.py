import random
from art import logo, vs
from game_data import data
from replit import clear

def format_data(account):
    """Format the account data into printable format."""
    account_name = account['name']
    account_descr = account['description']
    account_country = account['country']
    return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(answer, a_followers, b_followers):
    """Take the user guess and follower counts and returns if they got it right."""
    if a_followers > b_followers:
        return answer == "a"
    else:
        return answer == "b"

print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")
    answer = input("Who has more followers on Instagram? Type 'A' or 'B': ").lower()

    a_follower_count = account_a['follower_count']
    b_follower_count = account_b['follower_count']

    is_correct = check_answer(answer, a_follower_count, b_follower_count)
    
    clear()
    print(logo)
    
    if is_correct:
        score += 1
        print(f"You're right! Current score {score}.")
    else:
        game_should_continue = False
        print(f"That's wrong. Final score {score}.")
