def is_palindrome(string):
    string = string.lower()
    start = 0
    end = len(string) - 1

    while start < end:
        if string[start] != string[end]:
            return False  # Not a palindrome
        start += 1
        end -= 1

    return True

user_string = input("Enter a string to check if it's a palindrome: ")
if is_palindrome(user_string):
    print(f'"{user_string}" is a palindrome!')
else:
    print(f'"{user_string}" is not a palindrome.')
