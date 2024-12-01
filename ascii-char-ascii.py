def char_ascii():
    if len(char) == 1:
        print("The ASCII code for character", char, "is:", ord(char))
    else:
        print("Enter a character of length 1 only")

def ascii_char():
    if 0 <= ascii_code <= 127:
        print("The character of the ASCII Code", ascii_code, "is:", chr(ascii_code))
    else:
        print("Enter a valid ASCII code value between (0-127)")

while True:
    print("Menu:")
    print("1. Character to ASCII Code")
    print("2. ASCII Code to Character")
    choose = int(input("Enter the choice: "))
    if choose > 2:
        print("Wrong Input!")
        break
    if choose == 1:
        char = input("Enter the character: ")
        char_ascii()
    elif choose == 2:
        ascii_code = int(input("Enter the ASCII code: "))
        ascii_char()
