import cmath

a = float(input("Enter coefficient value a: "))
b = float(input("Enter coefficient value b: "))
c = float(input("Enter coefficient value c: "))

d = b**2 - 4*a*c

if d > 0:
    root1 = (-b + d**0.5) / (2*a)
    root2 = (-b - d**0.5) / (2*a)
    print("The equation has two real and distinct roots:")
    print("Root1:", root1)
    print("Root2:", root2)
elif d == 0:
    root = (-b / (2*a))
    print("The equation has one real root:")
    print("Root:", root)
else:
    root1 = (-b + cmath.sqrt(d)) / (2*a)
    root2 = (-b - cmath.sqrt(d)) / (2*a)
    print("The equation has two complex roots:")
    print("Root1:", root1)
    print("Root2:", root2)
