import os

from art import auc_logo

def new_participant():
    name = input("What is you name?: ")
    bid = int(input("What is you bid?: $"))
    participants[name] = bid
    

def checking_bids(bids):
    winner = ''
    biggest_bid = 0
    for key in bids:
        if bids[key] > biggest_bid:
            winner = key
            biggest_bid = bids[key]
    print(f"The winner is {winner} with a bid of ${biggest_bid}")

participants = {}

print(auc_logo)
while True:
    new_participant()
    other = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    os.system("cls")
    if other == 'no':
        checking_bids(participants)
        break
    elif other !='yes':
        print("Only 'yes' or 'no', monor!!!")
        break
    