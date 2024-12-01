def max(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        print(n1, "is the maximum number")
    elif n2 > n1 and n2 > n3:
        print(n2, "is the maximum number")
    else:
        print(n3, "is the maximum number")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
max(num1, num2, num3)
