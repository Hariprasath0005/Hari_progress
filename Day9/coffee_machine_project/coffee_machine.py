from menu import menu
from menu import resources

def resourses_sufficient(order_ingredients):
    for i in order_ingredients:
        if order_ingredients[i]>=resources[i]:
            print(f"Sorry there is not enough {i}.")
            return False
    return True

def process_money():
    print("Please insert money.")
    total = int(input("how many 10's?: ")) *10
    total += int(input("how many 20's?: ")) *20
    total += int(input("how many 50's?: ")) *50
    total += int(input("how many 100's?: "))*100
    print(f"Total paid: {total}")
    return total
amount = 0
def transaction(user_money,drink_cost):
    if user_money>=drink_cost:
        change = round(user_money - drink_cost,2)
        print(f"Here is your change {change}, Please collect!")
        global amount
        amount+=drink_cost
        return True
    else:
        print( "Sorry that's not enough money. Money refunded.")
        return False

def cal_resourses(drink_name,order_ingredients):
    for i in order_ingredients:
        resources[i]-=order_ingredients[i]
    print(f"Here is your {drink_name}, Enjoy!")


switch = True
while switch:
    user_input= input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_input=="off":
        switch=False
    elif user_input=="report":
        print(f"water:  {resources['water']}ml.")
        print(f"Milk:   {resources['milk']}ml.")
        print(f"Coffee: {resources['coffee']}ml.")
        print(f"Amount: {amount}rs.")
    else:
        drink = menu[user_input]
        print(f"{user_input} price : {drink["cost"]}Rs")
        if resourses_sufficient(drink["ingredients"]):
            pay = process_money()
            if transaction(pay,drink["cost"]):
                cal_resourses(user_input,drink["ingredients"])