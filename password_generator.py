
from random import *
#Data

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#Input

print("Password Generator!")
nr_letters = int(input("How many letters?\n"))
nr_symbols = int(input(f"How many symbols?\n"))
nr_numbers = int(input(f"How many numbers \n"))


#Brain
password= []

for char in range(nr_letters):
    password.append(choice(letters))
for char in range(nr_numbers):
    password.append(choice(numbers))
for char in range(nr_symbols):
    password.append(choice(symbols))

shuffle(password)
i = ""
for char in password:
  i += char
  
 #Output
print(f" password : {i}")

