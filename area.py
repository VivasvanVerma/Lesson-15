print("Shapes: ")
print("a. Square")
print("b. Rectangle")
print("c. Circle")
print("d. Rhombus")

choice = input("Select Shape(a/b/c/d): ")

def a():
    side = int(input("Enter side length: "))
    area = side**2
    print("Area = ", area)

def b():
    length = int(input("Enter length: "))
    width = int(input("Enter width: "))
    area = length*width
    print("Area = ", area)

def c():
    radius = int(input("Enter radius: "))
    area = 3.14 * (radius**2)
    print("Area = ", area)

def d():
    d1 = int(input("Enter Diagonal 1: "))
    d2= int(input("Enter Diagonal 2: "))
    area = 0.5 * d1 * d2
    print("Area = ", area)

if choice == "a":
    a()
elif choice == "b":
    b()
elif choice == "c":
    c()
elif choice == "d":
    d()
else:
    print("Invalid Choice")
