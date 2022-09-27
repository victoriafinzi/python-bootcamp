"""
Regras do BlackJack:
É um jogo de cartas onde o intuíto é chegar na contagem de 21pontos ou perto disso.
Jamais poderá ultrapassar o valor de 21pontos, se não perde. 
A contagem das cartas é feita da seguinte forma:
Cartas de 2 a 10 representam o seu valor real;
Carta Ás representa 11 ou 1 você escolhe;
Cartas Rei, Rainha ou Valete valem 10 respectivamente. 
Se você ou o computador tiverem duas cartas, mas a somatória é < 17,
é necessário que mais uma carta seja gerada. 
Se os valores de vocẽs dois no final do round forem iguais, empata;
Se o seu valor for maior do que o do computador, você ganha;
Se o seu valor for menor do que o do computador, você perde. 
"""
from art import logo
from replit import clear
import random

def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack!"
    elif user_score == 0:
        return "Win with a Blackjack!"
    elif user_score > 21:
        return "You went over. You lose!"
    elif computer_score > 21:
        return "Oponnent went over. You win!"
    elif user_score > computer_score:
        return "You win!"
    else:
        return "You lose!"

def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    is_game_over = False

    for card in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            another_card = input("Do you want to choose another card? Type 'y' or 'pass': ")
            if another_card == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Your final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    clear()
    play_game()
