#Function for checking prime number

def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("Prime Number")
    else:
        print("Non Prime Number")

# Interaction console

number = int(input("Number:"))

prime_checker(number)
