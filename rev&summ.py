while True:
    print("Menu:")
    print("1. Reverse the entered number")
    print("2. Calculate the sum of digits of the entered number")

    choose = int(input("Enter your choice: "))
    
    if choose > 2:
        print("Wrong Input!")
        break

    num = input("Enter the number to perform operations: ")
    sum_dignum = 0

    if choose == 1:
        rev_num = num[::-1]
        print("Reverse of", num, "is:", rev_num)

    elif choose == 2:
        for digit in num:
            sum_dignum = sum_dignum + int(digit)
        print("The sum of the digits of", num, "is:", sum_dignum)
