from replit import clear
from art import logo
print(logo)
print("Welcome to the secret auction program.")

should_continue = True
bids = {}

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with the bid of ${highest_bid}")

while should_continue:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    
    add_more_bids = input("Are there any other bidders? Type 'yes' or 'no'.\n")

    if add_more_bids == "no":
        should_continue = False
        find_highest_bidder(bids)
    elif add_more_bids == "yes":
        clear()
