from cash_count import Cash_count
from coffe_maker import Coffeemaker

cash = Cash_count()
coffee = Coffeemaker()


is_on = True

while is_on:
    choice = input("choose a drink\n\nespresso\nlatte"
                   "\ncappuccino\n: "). lower()

    drink = coffee.resources[choice]
    if coffee.check_resources(drink['ingredients']):
        payment = cash.cash_count()
        if cash.is_transaction_succes(payment, drink["cost"]):
            coffee.make_coffe(choice, drink['ingredients'])



