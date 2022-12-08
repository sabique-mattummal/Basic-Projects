# Input
numbers = input("Input a list of student scores(seperated by a space only) : ").split()

# Conversion of number into an integer
for n in range(0, len(numbers)):
    numbers[n] = int(numbers[n])
print(numbers)

# Brain
higher_number = 0
for value in numbers:
    if value > higher_number:
        higher_number = value

# Output

print(f"The highest number in the list is : {higher_number}")
