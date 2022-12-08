#Rows

row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️"]

#Arrangement

map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")

#Input

print("The positions are\n[11,21,31]\n[12,22,32]\n[13,23,33]")

position = input("Where do you want to put the marker 'X' as per the above arrangemnt ? ")


#Position Marking

h = int(position[0]) 
v = int (position[1]) 

selected_row = map[v - 1]
selected_row[h-1] = 'X'

print(f"{row1}\n{row2}\n{row3}")
