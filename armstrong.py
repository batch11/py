def is_armstrong(num):
    str_num = str(num)
    digi_num = len(str_num)
    sum = 0
    for digit in str_num:
        sum = sum + int(digit)**digi_num

    if sum == num:
        print(num, "is an Armstrong number")
    else:
        print(num, "is not an Armstrong number")

num = int(input("Enter the number: "))
is_armstrong(num)
