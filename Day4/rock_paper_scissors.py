rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
list1 = [rock,paper,scissors]

#users
user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.: "))
user_choose =list1[user]
print(f"You choose: {user_choose}")

#computer
ran = random.randint(0,2)
comp = list1[ran]
print(f"Computer choose: {comp}")

if user>=3 or user<0:
    print("Invalid Input, Enter a valid input")
elif user ==0 and ran==2:
    print("You win")
elif user ==2 and ran==1:
    print("You win")
elif user==1 and ran==0:
    print("You win")
elif ran==user:
    print("Draw game")
else:
    print("You lose")




