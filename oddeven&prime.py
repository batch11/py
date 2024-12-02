def odd_even(num):
    if num % 2 == 0:
        print(num, "is even number")
    else:
        print(num, "is odd number")

def prime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                print("The number is not prime")
                break
        else:
            print("The number is prime")
    elif num == 1:
        print("The number is not prime")

while True:
    print("Menu:")
    print("1. Check odd or even")
    print("2. Check prime")
    choose = int(input("Enter the choice: "))
    
    if choose > 2:
        print("Wrong Input!")
        break
    
    num = int(input("Enter the number: "))
    
    if choose == 1:
        odd_even(num)
    elif choose == 2:
        prime(num)
