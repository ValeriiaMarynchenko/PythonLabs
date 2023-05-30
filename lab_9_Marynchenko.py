def caesar(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                base = ord('A')
            else:
                base = ord('a')

            encoded = (ord(char) - base + shift) % 26 + base
            encoded_char = chr(encoded)
            result += encoded_char
        else:
            result += char

    return result


text = input("Enter the string to be encrypted: ")
shift = None

while True:
    shift_input = input("Enter an offset value (an integer from the range 1-25): ")
    try:
        shift = int(shift_input)
        if 1 <= shift <= 25:
            break
        else:
            print("Error.The offset value must be in the range 1-25.")
    except ValueError:
        print("Error. Incorrect input. Enter an integer.")

if shift is not None:
    encrypted_text = caesar(text, shift)
    print("Encoded text:", encrypted_text)
