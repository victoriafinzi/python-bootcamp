
from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def set_difficulty():
    difficulty = input("Choose a difficulty, type 'easy' or 'hard': ")
    if difficulty == 'easy':        
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

turns = 0
def check_answer(guessing, computer_number, turns):
    """Checks answer against guess. Returns the number of turns remaining"""
    if guessing > computer_number:
        print("Too high! \n Guess again!")
        return turns - 1
    elif guessing < computer_number:
        print("Too low! \n Guess again!")
        return turns - 1
    else:
        print("You guessed it!")

def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    computer_number = randint(1, 100)

    turns = set_difficulty()

    guessing = 0
    while guessing != computer_number:
        print(f"You have {turns} attempts remaning to guess the number")
        guessing = int(input("Make a guess: "))
        turns = check_answer(guessing, computer_number, turns)
        if turns == 0:
            print("You've run out of guesses. You lose!")
            return
game()
