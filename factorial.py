def factorial(num):
    if num == 0 or num == 1:
        return 1
    elif num > 1:
        return num * factorial(num - 1)
    else:
        print("Wrong Input!")

num = int(input("Enter the number: "))
print("The factorial of the number", num, "is:", factorial(num))
