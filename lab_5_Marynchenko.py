from typing import List, Any

print("Завдання 1")
hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.

# Step 1: write a line of code that prompts the user
# to replace the middle number with an integer number entered by the user.
print(hat_list)
user_number = (int(input("Enter an integer to replace the middle number: ")))
hat_list[int(len(hat_list)//2)] = user_number
print(hat_list)
# Step 2: write a line of code that removes the last element from the list.
del hat_list[-1]
print(hat_list)
# Step 3: write a line of code that prints the length of the existing list.
print(len(hat_list))
print()
print("Завдання 2")
my_list = [1, 4, 6, 2, 7, 3]

swapped = True

while swapped:
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

            print(my_list)

print()
print("Завдання 3")
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
newlist = []

for i in my_list:
    if i not in newlist:
        newlist.append(i)

print(my_list)
# print("The list with unique elements only:")
print(newlist)
print()
print("Завдання 4")

chessboard = [['_'] * 8 for _ in range(8)]

chessboard[0][0] = 'I'
chessboard[0][7] = 'I'
chessboard[7][0] = 'I'
chessboard[7][7] = 'I'

for row in chessboard:
    print(' '.join(row))
