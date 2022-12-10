class Cash_count:
    def __init__(self):
        self.profit = 0

    def is_transaction_succes(self,money_recieved, money_required):
        if money_recieved >= money_required:
            balance = round(money_recieved - money_required, 2)
            print(f"Balance ${balance} returned")
            global profit
            self.profit += money_recieved
            return True
        else:
            print(f"Not enough money ${money_required}")
            return False

    def cash_count(self):
        print("Please Insert Coins:\n")
        total = int(input("Quarters (1/4): \n")) * .25
        total += int(input("Dimes (1/10) : \n")) * .1
        return total