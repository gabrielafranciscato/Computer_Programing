# Part 1: Writing a Simple Program

print ("Welcome to Computer Programming with Python!")


print ("The sum is:", 10+5)
print ("The difference is:", 10-3)
print ("The product is:", 10*3)
print ("The quotient is:", 10/3)


#Part 2: Arithmetic Operations with Fixed Values

a=10
b=12

print ("The sum is:", a+b)
print ("The difference is:", a-b)
print ("The product is:", a*b)
print ("The quotient is", a/b)


# Part 3: Arithmetic Operations with User Input

a = float(input("Enter first number"))
b = float(input(" enter second number"))

print ("The sum is:",a+b)
print ("The difference is:", a-b)
print ("The product is:", a*b)
print ("The quotient is", a/b)



# Part 4: Multiple Operations in One Run


a = float(input("Enter first number: "))
b = float(input(" enter second number: "))

print(
    "The sum is:", a + b,

a = float(input("Enter first number: "))
b = float(input(" enter second number: "))
    "\nThe difference is:", a - b,
    "\nThe product is:", a * b,
    "\nThe quotient is:", a / b
)


#Part 5: Menu-Driven Calculator

print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter your choice (1-4): ")

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if choice == "1":
    print("The sum is:", a + b)

elif choice == "2":
    print("The difference is:", a - b)

elif choice == "3":
    print("The product is:", a * b)

elif choice == "4":
    print("The quotient is:", a / b)

else:
    print("Invalid operation.")


# Part 6: Challenge/Trivia – Continuous Calculator

while True:

    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter your choice (1-4): ")

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if choice == "1":
        print("The sum is:", a + b)

    elif choice == "2":
        print("The difference is:", a - b)

    elif choice == "3":
        print("The product is:", a * b)

    elif choice == "4":
        print("The quotient is:", a / b)

    else:
        print("Invalid operation.")

    continue_calculation = input("Do you want to continue? (yes/no): ")

    if continue_calculation == "no":
        print("Calculator closed.")
        break

