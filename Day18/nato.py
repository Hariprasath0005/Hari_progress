import pandas
nato = pandas.read_csv("./Day18/nato.csv")


dict2 = {value.letter:value.code for (index, value) in nato.iterrows()}

user = input("Enter: ").upper()

list1 = [dict2[i] for i in user]
print(list1)


