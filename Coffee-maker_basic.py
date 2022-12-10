#data sheet

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def check_resources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Not enough {item} available")
            return False
        else:
            return True

def cash_count():
    print("Please Insert Coins:\n")
    total = int(input("Quarters (1/4): \n")) * .25
    total += int(input("Dimes (1/10) : \n")) * .1
    return total

def is_transaction_succes(money_recieved, money_required):
    if money_recieved >= money_required:
        balance = round(money_recieved - money_required, 2)
        print(f"Balance ${balance} returned")
        global profit
        profit += money_recieved
        return True
    else:
        print(f"Not enough money ${money_required}")
        return False

def make_coffe(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is {drink_name}")

is_on = True

while is_on:
    choice = input("choose a drink\n\nespresso\nlatte"
                   "\ncappuccino\n: "). lower()

    drink = MENU[choice]
    if check_resources(drink['ingredients']):
        payment = cash_count()
        if is_transaction_succes(payment, drink["cost"]):
            make_coffe(choice, drink['ingredients'])



