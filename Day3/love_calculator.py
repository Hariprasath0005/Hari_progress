print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
name = name1 + name2
lower_name = name.lower()
t = lower_name.count("t")
r = lower_name.count("r")
u = lower_name.count("u")
e = lower_name.count("e")
true = t+r+u+e

l = lower_name.count("l")
o = lower_name.count("o")
v = lower_name.count("v")
e = lower_name.count("e")
love = l+o+v+e
total = int(f"{true}{love}")
if total <10 or total >90:
  print(f"Your score is {total}, you go together like coke and mentos.")
elif total >=40 and total<=50:
  print(f"Your score is {total}, you are alright together.")
else:
  print(f"Your score is {total}.")