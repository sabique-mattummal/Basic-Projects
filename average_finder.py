#Input
student_heights = input("Input a list of student heights, (seperated by a space or tab only) :  ").split()

#Conversion of each value in list to an integer value in order to make mathematical oprations
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

#Brain
total_height = 0
for height in student_heights:
    total_height += height
number = 0
for student in student_heights:
    number += 1 
average = round(total_height / number,1)

#Output
print(f"The average of {len(student_heights)} students is {average}")





