def power (a,b):
    return a ** b

def modulus (a,b):
    return a % b

def add (a,b):
    return a + b 

def subtract (a,b):
    return a -b 

def multiply (a,b):
    return a*b

def divide (a,b):
    return a / b

print ("=====SmartCalc Calculator==========")
print("1. Addition")
print("2. Subtraction")
print ("3. Multiplication")
print ("4. Division")
print ("5. Power")
print ("6. Modulus")


choice = int(input("Select an operation from the list: "))

if choice >= 1 and choice <=6:

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))


    if choice ==1:
        result = add(num1,num2)
        print ("The result is:",result)


    elif choice ==2:
        result = subtract(num1,num2)
        print ("The result is",result)

    elif choice == 3:
        result =multiply (num1,num2)
        print("The result is:",result)

    elif choice == 4:
        if num2 == 0:
            print ("Cnnot divide by zero")


        elif num1 == 0:
            print("Cnnot divide by zero")

        else:
            result = divide(num1, num2)
            print("The result is:", result)

    elif choice == 5:
        result = power (num1,num2)
        print ("The result is:",result)

    elif choice == 6:
        if num2 == 0:
            print ("Cannot calculate modulus by zero")
        else:
            result = modulus (num1, num2)
            print ("The result is:",result)
else: 
    print ("Option not listed")