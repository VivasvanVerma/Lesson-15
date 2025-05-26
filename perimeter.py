print("Shapes: ")
print("a. Square")
print("b. Rectangle")
print("c. Circle")
print("d. Triangle")

choice = input("Select Shape(a/b/c/d): ")

def a():
    side = int(input("Enter side length: "))
    per = 4*side
    print("Perimeter: ", per)

def b():
    length = int(input("Enter length: "))
    breadth = int(input("Enter breadth: "))
    per = 2*(length + breadth)
    print("Perimeter: ", per)

def c():
    radius = int(input("Enter radius length: "))
    per = 2*3.14*radius
    print("Circumference: ", per)

def d():
    s1 = int(input("Enter side 1 length: "))
    s2 = int(input("Enter side 2 length: "))
    s3 = int(input("Enter side 3 length: "))
    per = s1+s2+s3
    print("Perimeter: ", per)

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