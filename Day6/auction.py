from os import system
from auction_logo import logo
print(logo)
dict = {}

price = {}
def highest_bid(dict):
    amt = 0
    winner = ""
    for i in dict:
        price=dict[i]
        if price>amt:
            amt= price
            winner = i
    print(f"Highest Bidder is {winner} with ₹{amt} bid")


ask = True
while  ask:
    name = input("what is your name? ")
    bid = int(input("What's your bid? ₹"))
    dict[name] = bid
    asking = input("Are there any other bidders? Yes or No: ").lower()
    if asking=="no":
        ask = False
        highest_bid(dict)
    elif asking=="yes":
        system("cls")
    else:
        system("cls")
        print("invalid entry")
        asking = input("Are there any other bidders? Yes or No: ").lower()
        if asking=="no":
            ask = False



