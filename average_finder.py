#Input
numbers = input("Input a list of numbers, (seperated by a space or tab only) :  ").split()

#Conversion of each value in list to an integer value in order to make mathematical oprations
for n in range(0, len(numbers)):
  numbers[n] = int(numbers[n])

#Brain
total_height = 0
for height in numbers:
    total_height += height
number = 0
for student in numbers:
    number += 1
average = round(total_height / number,1)

#Output
print(f"The average of {len(numbers)} numbers is {average}")



