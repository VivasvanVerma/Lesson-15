print("Operation Choices:")
print("a. Addition")
print("b. Subtraction")
print("c. Multiplication")
print("d. Division")

choice = input("Enter Choice (a/b/c/d): ")

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

def add():
    addition = num1 + num2
    print(num1, "+ ", num2, " = ", addition)

def sub():
    minus = num1 - num2
    print(num1, "- ", num2, " = ", minus)

def mult():
    into = num1 * num2
    print(num1, "x ", num2, " = ", into)

def div():
    divide = num1 + num2
    print(num1, "/ ", num2, " = ", divide)

if choice == "a":
    add()
elif choice == "b":
    sub()
elif choice == "c":
    mult()
elif choice == "d":
    div()
else:
    print("Invalid choice.")
