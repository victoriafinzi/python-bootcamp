# another_card = input("Do you want to choose another card? Type 'y' or 'pass': ")
# if another_card == 'y':
#     user_card_3 = random.choice(list_of_cards)
#     user_total = user_points + user_card_3
#     computer_card_3 = random.choice(list_of_cards)
#     computer_total = computer_points + computer_card_3
#     if user_total > 21 and computer_total < 21:
#         print(f"Score: \n your points: {user_total} - cards: [{user_card_1}, {user_card_2}, {user_card_3}] \n computer points: {computer_total} \n YOU LOSE!")
#     elif computer_total > 21 and user_total < 21:
#         print(f"Score: \n your points: {user_total} - cards: [{user_card_1}, {user_card_2}, {user_card_3}] \n computer points: {computer_total} \n YOU WIN!")
#     elif user_total and computer_total > 21:
#         print(f"Score: \n your points: {user_total} - cards: [{user_card_1}, {user_card_2}, {user_card_3}] \n computer points: {computer_total} \n YOU BOTH LOSE!")
#     elif user_total == computer_total:
#         print(f"Score: \n your points: {user_total} - cards: [{user_card_1}, {user_card_2}, {user_card_3}] \n computer points: {computer_total} \n DRAW!")
#     elif user_total == 21:
#         print(f"Score: \n your points: {user_total} - cards: [{user_card_1}, {user_card_2}, {user_card_3}] \n computer points: {computer_total} \n YOU WIN!")
#     elif computer_total == 21 and user_total < 21:
#         print(f"Score: \n your points: {user_total} - cards: [{user_card_1}, {user_card_2}, {user_card_3}] \n computer points: {computer_total} \n YOU LOSE!")
#     elif user_total < 21 and user_total > computer_points:
#         print(f"Score: \n your points: {user_total} - cards: [{user_card_1}, {user_card_2}, {user_card_3}] \n computer points: {computer_total} \n YOU WIN!")
# elif another_card == 'pass':
#     if computer_points > 18:
#         if computer_points == user_points:
#             print(f"Score: \n your points: {user_points} - cards: [{user_card_1}, {user_card_2}] \n computer points: {computer_points} \n DRAW!")
#         elif computer_points < user_points:
#             print(f"Score: \n your points: {user_points} - cards: [{user_card_1}, {user_card_2}] \n computer points: {computer_points} \n YOU WIN!")
#         elif computer_points > user_points:
#             print(f"Score: \n your points: {user_points} - cards: [{user_card_1}, {user_card_2}] \n computer points: {computer_points} \n YOU LOSE!")
#     elif computer_points <= 17:
#         computer_card_3 = random.choice(list_of_cards)
#         computer_total = computer_points + computer_card_3
#         if computer_total > 21 and user_points < 21:
#             print(f"Score: \n your points: {user_points} - cards: [{user_card_1}, {user_card_2}] \n computer points: {computer_total} \n YOU WIN!")
#         elif user_points == computer_total:
#             print(f"Score: \n your points: {user_points} - cards: [{user_card_1}, {user_card_2}] \n computer points: {computer_total} \n DRAW!")
#         elif user_points == 21:
#             print(f"Score: \n your points: {user_points} - cards: [{user_card_1}, {user_card_2}] \n computer points: {computer_total} \n YOU WIN!")
#         elif computer_total == 21 and user_points < 21:
#             print(f"Score: \n your points: {user_points} - cards: [{user_card_1}, {user_card_2}] \n computer points: {computer_total} \n YOU LOSE!")
#         elif user_points < 21 and user_points > computer_points:
#             print(f"Score: \n your points: {user_points} - cards: [{user_card_1}, {user_card_2}] \n computer points: {computer_total} \n YOU WIN!")
