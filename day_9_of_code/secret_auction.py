from replit import clear
from art import logo
print(logo)
print("Welcome to the secret auction program.")

should_continue = True
while should_continue:
    auction = []
    names = input("What is your name?: ")
    bids = int(input("What is your bid?: $"))
    
    def add_persons(names, bids):
        add_person = {}
        add_person["name"] = names
        add_person["bid"] = bids
        auction.append(add_person)

    
    add_persons(names, bids)
    
    add_more_bids = input("Are there any other bidders? Type 'yes' or 'no'.")
    clear()
    print(auction)
    if add_more_bids == "no":
        should_continue = False
        max_value = max(auction)
        print(max_value)
