def fibonacci_series(num):
    a = 0
    b = 1
    if num == 1:
        print(a, end=" ")
    else:
        print(a, end=" ")
        print(b, end=" ")

        for i in range(2, num):
            c = a + b
            a = b
            b = c
            print(c, end=" ")

# Input from user
num = int(input("Enter the number of terms for Fibonacci series: "))
if num <= 0:
    print("Please enter a positive number")
else:
    fibonacci_series(num)
