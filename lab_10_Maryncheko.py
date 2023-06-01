print("Завдання 1")
def is_hidden(word, combination):
    word = word.lower()
    combination = combination.lower()

    current_index = -1

    for char in word:
        current_index = combination.find(char, current_index + 1)

        if current_index == -1:
            return False

    return True


word = input("Enter a word ")
combination = input("Enter a combination of symbols: ")

if is_hidden(word, combination):
    print("Yes")
else:
    print("No")



print()
print("Завдання 2")

date = input("Введіть дату народження у форматі YYYYMMDD:")

while True:
    try:
        sum = 0
        for symbol in date:
            sum += int(symbol)

        date = str(sum)

        if len(date) == 1:
            break

    except ValueError:
        print("Введені дані некоректні. Будь ласка, спробуйте ще раз.")

print(sum)



print()
print("Завдання 3")
def get_integer_input(prompt, min_v, max_v):
    while True:
        try:
            value = int(input(prompt))
            if value < min_v or value > max_v:
                print(f"Error: the value is not within permitted range ({min_v}..{max_v})")
            else:
                return value
        except ValueError:
            print("Error: wrong input")

input1 = "Enter an integer: "
min_v = 1
max_v = 10

int_v = get_integer_input(input1, min_v, max_v)
print(f"Entered number: {int_v}")
