import random 
import hangman_stages
from word_list import words_list
from hangman_stages import stages
from hangman_stages import logo
print(logo)
chosen_word = random.choice(words_list)
#print(chosen_word)

display=[]
word_len = len(chosen_word)
for i in range(1,word_len+1):
    display+="_"
lives = 6
game_end = False
while not game_end:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"You already choosen the letter: ")
        
    for i in range(word_len):
        letter = chosen_word[i]
        if letter ==guess:
            display[i] = letter
    print(display)
    word = ""
    for i in display:
        word+=i
    print(word)
    print(f"{' '.join(display)}")
    if guess not in chosen_word:
        print(f"You guessed {guess}, not in the letter you lost a life.")
        lives-=1
        if lives ==0:
            game_end = True
            print("You lose")
    
    print(stages[lives])
    if "_" not in display:
        game_end = True
        print("You Win")
    

