while True:
    print("Menu:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Division")
    print("5. Floor Division")
    print("6. Modulus")

    choose = int(input("Enter the choices 1-6: "))
    num_a = float(input("Enter first number: "))
    num_b = float(input("Enter second number: "))

    if choose == 1:
        answer = num_a + num_b
        print("Result is:", answer)
    elif choose == 2:
        answer = num_a - num_b
        print("Result is:", answer)
    elif choose == 3:
        answer = num_a * num_b
        print("Result is:", answer)
    elif choose == 4:
        if num_b != 0:
            answer = num_a / num_b
            print("Result is:", answer)
        else:
            print("Error! Division by zero.")
    elif choose == 5:
        if num_b != 0:
            answer = num_a // num_b
            print("Result is:", answer)
        else:
            print("Error! Division by zero.")
    elif choose == 6:
        answer = num_a % num_b
        print("Result is:", answer)
    else:
        print("Invalid choice! Please enter a number between 1 and 6.")
        break
