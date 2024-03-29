import random

# Функція для виведення дошки
def print_board(board):
    print("+-------+-------+-------+")
    for row in board:
        print("|       |       |       |")
        print("|   {}   |   {}   |   {}   |".format(row[0], row[1], row[2]))
        print("|       |       |       |")
        print("+-------+-------+-------+")

# Функція для перевірки, чи гра закінчена
def game_over(board):
    # Перевірка рядків
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != "_":
            return True

    # Перевірка стовпців
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != "_":
            return True

    # Перевірка діагоналей
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "_":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "_":
        return True

    # Перевірка нічиєї
    if all("_" not in row for row in board):
        return True

    return False

# Створення пустої дошки
board = [["_"] * 3 for _ in range(3)]

# Перший хід комп'ютера
board[1][1] = "X"

# Основний цикл гри
while not game_over(board):
    # Виведення дошки
    print_board(board)

    # Хід користувача
    while True:
        user_choice = int(input("Ваш хід (введіть номер квадрата 1-9): "))
        row = (user_choice - 1) // 3
        col = (user_choice - 1) % 3
        if board[row][col] == "_":
            board[row][col] = "O"
            break
        else:
            print("Цей квадрат уже зайнятий! Спробуйте ще раз.")

    # Перевірка, чи гра закінчена після ходу користувача
    if game_over(board):
        break

    # Хід комп'ютера
    while True:
        computer_choice = random.randint(1, 9)
        row = (computer_choice - 1) // 3
        col = (computer_choice - 1) % 3
        if board[row][col] == "_":
            board[row][col] = "X"
            break

# Виведення остаточної дошки
print_board(board)

# Визначення результату гри
if "_" not in board[0] and "_" not in board[1] and "_" not in board[2]:
    print("Гра завершилась нічиєю!")
elif any(row[0] == row[1] == row[2] == "X" for row in board) or any(board[0][col] == board[1][col] == board[2][col] == "X" for col in range(3)):
    print("Ви програли!")
else:
    print("Ви виграли!")
