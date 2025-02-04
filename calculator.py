print("calculator".center(60))

x = int(input("ENTER THE FIRST NUMBER: "))

y = int(input("ENTER THE SECOND NUMBER: "))

z = input("ENTER YOUR CHOICE (-, +, /, *, %): ")

if z == '+':
    print("The addition of two numbers is:", x + y)
elif z == '-':
    print("The subtraction of two numbers is:", x - y)
elif z == '*':
    print("The multiplication of two numbers is:", x * y)
elif z == '/':
    if y != 0:
        print("The division of two numbers is:", x / y)
    else:
        print("Error: Division by zero is not allowed.")
elif z == '%':
    if y != 0:
        print("The modulus of two numbers is:", x % y)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operator.")

print("Your Calculation is Successfully Done:)")
