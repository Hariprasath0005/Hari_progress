import random
from data import account_data
from os import system
from art import logo
def format_data(account):
    name = account["name"]
    desc = account["description"]
    country = account["country"]
    return (f"{name}, a {desc}, from {country}")

def check_ans(guess,a_follower,b_follower):
    if a_follower > b_follower:
         return guess == "a"
    else:
        return guess == "b"
    
def game():
    print(logo)
    continue_game = True   
    score = 0
    account_b = random.choice(account_data)
    while continue_game:
        
        account_a = account_b
        account_b = random.choice(account_data)
        while account_a == account_b:
            account_b = random.choice(account_data)


        print(f"Compare A: {format_data(account_a)}")
        print("-----------VS------------")
        print(f"Compare B: {format_data(account_b)}")
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        a_follower = account_a["follower_count"]
        b_follower = account_b["follower_count"]

        is_correct = check_ans(guess,a_follower,b_follower)
        system("cls")
        print(logo)
        if is_correct:
            score+=1
            print(f"You are correct, score: {score}")
        else:
            continue_game=False
            print(f"You are wrong, Final score: {score}")

while input("Do you want to play a game? Type 'yes' or 'no': ").lower() =="yes":
    system("cls")
    game()
