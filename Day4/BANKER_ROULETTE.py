import random
names = input("Enter the names: ").split(",")
names_list = len(names)
ran = random.randint(0,names_list-1)
list = names[ran]
print(list)
