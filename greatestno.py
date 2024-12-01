num = int(input("How many numbers do you want to enter? "))
greatest_num = None

for i in range(num):
    num = float(input(f"Enter number {i+1}: "))
    if greatest_num is None or num > greatest_num:
        greatest_num = num

print("The greatest number is:", greatest_num)
