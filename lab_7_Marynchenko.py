print()
print("Завдання 1")
number_list = [1, -3, 9, -27, 81, -243, 729, -2187, 6561, -19683]
n_list = list(number_list)
n = float(input("Enter the number of fragments less than which you need to create a new list: "))
result = [i for i in number_list if i<n]
print(result)

print()
print("Завдання 2")
my_tuple = ("Lonlon is", " the capital of", " Great Britain")
my_tuple1 = (",".join(my_tuple))
print(my_tuple1)

print()
print("Завдання 3")
the_libryary = {
    "Alice's Adventures in Wonderland": ["Lewis Carroll", 1865, 104],
    "Charlie and the Chocolate Factory": ["Roald Dahl", 1964, 192],
    "The Divine comedy": ["Dante", 1321, 712],
    "A Study in Scarlet": ["Arthur Conan Doyle", 1887, 124],
    "Harry Potter and the Philosopher's Stone": ["J. K. Rowling", 1997, 223]
}
a = input("enter the book title: ")
item = the_libryary[a]
print(item)

print()
print("Завдання 4")
studs = {
    "Marynchenko": ("NIIELIIT", "third course", "KI-20-1"),
    "Shevchenko": ("NIIELIIT", "fitst course" "SOI-22-2"),
    "Mel'nyk": ("NIIELIIT", "second course", "AKIT-21-1")
}
a = input("enter the surenane of student: ")
item = studs[a]
print(item)

print()
print("Завдання 5")
from collections import defaultdict

phones = {
    "mother":['+380999999432', '+38068999432'],
    "fother":['+380999995432', '+38063995432'],
    "grandma":['+380999996543', '+38098996543'],
    "drandpa":['+380999976543', '+38098976543']
}
key = input("Enter name of contact: " )
value = str(input("Enter a phone number: "))

phones.setdefault(key, []).append(value)

for key, value in phones.items():
    print("Name: ", key, "phone: ", value)


