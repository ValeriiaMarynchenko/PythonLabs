print("Завдання 1")
n = int(input("Enter an integer: "))
print(n >= 100)
print()
print("Завдання 2")
a = float(input("Enter value for A: "))
b = float(input("Enter value for B: "))
if a > b:
    print(a, " more then ", b)
else:
    print(b, " more then ", a)
print()
print("Завдання 3")
a = str(input('I\'d like you to type "Spathiphyllum":'))
if a == "Spathiphyllum":
    print("Yes - Spathiphyllum is the best plant ever!")
elif a == "spathiphyllum":
    print("No, I want a big Spathiphyllum!")
else:
    print("Spathiphyllum! Not ", a, "!")
print()
print("Завдання 4")
income = float(input("Enter the annual income: "))

if income <= 85528:
    tax = income * 0.18 - 556.02
else:
    tax = 14839.02 + (income - 85528) * 0.32

if tax > 0:
    tax = round(tax, 0)
else:
    tax = 0
print("The tax is:", tax, "thalers")
print()
print("Завдання 5")
year = int(input("Enter a year: "))
year1 = year % 4
year2 = year % 100
year3 = year % 400
if year > 1582:
    if year1 == 0:
        if year2 == 0 & year3 != 0:
            print("Common year")
        else:
            print("Leap year")
    else:
        print("Common year")
else:
    print("Not within the Gregorian calendar period.")
print()
print("Завдання 6")
secret_number = 777

print("""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")
while secret_number != int(input("I think it is")):
    print("Ха-ха! Ви застрягли у моїй петлі!")
print("Молодець, магле! Тепер ти вільний")
print()
print("Завдання 7")
import time

counter = 1
for counter in range(10):
    counter += 1
    time.sleep(1)
    print(counter, "Mississippi")
print("Ready or not, here I come!")
print()
print("Завдання 8")
secret_word = "chupacabra"
while 1 == 1:
    if secret_word != str(input("Enter a word: ")):
        print("You've successfully left the loop.!")
    else:
        break
    break
print()
print("Завдання 9")
user_word = str(input("Enter a word: "))
user_word = user_word.upper()
counter = 0
aeiou = ("A E I O U")
for counter in range(len(user_word)):
    if user_word[counter] not in aeiou:
        print(user_word[counter])
        counter += 1
    else:
        counter += 1
print()
print("Завдання 10")
word_without_vowels = ""

user_word = str(input("Enter a word: "))
user_word = user_word.upper()
counter = 0
aeiou = ("A E I O U")
for counter in range(len(user_word)):
    if user_word[counter] not in aeiou:
        print(user_word[counter], end="")
        counter += 1
    else:
        counter += 1
print()
print("Завдання 11")
number_of_blocks = int(input("Enter a number of blocks: "))
a = 0   # hight
b = 0   # using bloks
while number_of_blocks >= b:
    a += 1
    b = b+a
print(a - 1)
print()
print("Завдання 12")
c0 = int(input("Enter a positive integer: "))
counter = 0
while c0 != 1:
    if c0 % 2 == 0:
        c0 = c0/2
        print(c0)
        counter += 1
    else:
        c0 = 3*c0+1
        print(c0)
        counter += 1
print("steps", counter)
