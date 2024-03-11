import random
from os import system
logo=""""
   ___                _                            _                                   
  / __|_  _ ___ _____(_)_ _  __ _   _ _ _  _ _ __ | |__  ___ _ _   __ _ __ _ _ __  ___ 
 | (_ | || / -_|_-<_-< | ' \/ _` | | ' \ || | '  \| '_ \/ -_) '_| / _` / _` | '  \/ -_)
  \___|\_,_\___/__/__/_|_||_\__, | |_||_\_,_|_|_|_|_.__/\___|_|   \__, \__,_|_|_|_\___|
                            |___/                                 |___/                
"""
easy_level = 10
hard_level = 5
turns = 0
def guessing(user_input,computer,turns):
    if computer == user_input:
        print(f"Correct, the answer is {computer}")
        
    elif user_input>computer:
        print("Too high. Try Again!")
        return turns-1
    elif user_input<computer:
        print("Too Low. Try Again!")
        return turns-1

def difficulty():
    level = input("Difficulty level: 'e' for Easy or 'h' for hard:").lower()
    if level =="e":
        return easy_level
    elif level =="h":
        return hard_level
    
def game():
    print(logo)
    print("Welcome to number guessing game. ")
    
    turns = difficulty()
    print("Guess a number between 0 to 100")
    
    computer = random.randint(0,100)
    user_input=0
    while user_input!=computer:
        print(f"Number of turns left {turns}")
        user_input = int(input("Guess a number: "))
        turns = guessing(user_input,computer,turns)
        if turns==0:
            print("No more chance, You lose")
            return
    


while input("Do you want to play a game? Type 'yes' or 'no': ").lower() =="yes":
    system("cls")
    game()



