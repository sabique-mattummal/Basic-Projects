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
class Coffeemaker:
    def __init__(self):
        self.resources = MENU
    def check_resources(self, order_ingredients):
        for item in order_ingredients:
            if order_ingredients[item] > resources[item]:
                print(f"Not enough {item} available")
                return False
            else:
                return True

    def make_coffe(self,drink_name, order_ingredients):
        for item in order_ingredients:
            resources[item] -= order_ingredients[item]
        print(f"Here is {drink_name}")

