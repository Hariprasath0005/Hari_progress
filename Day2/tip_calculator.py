print("Welcome to tip calculator and split amount")
bill = float(input("What is your total bill? "))
tip = float(input("What percentage tip would you like to give? 10, 12, 15? "))
person = float(input("How many people to split the bill? "))
#tip_percent = (bill*tip)/100
bill_amt = bill + (bill*tip)/100
split = round(bill_amt/person,2)
print(f"Each person should pay: {split}")
