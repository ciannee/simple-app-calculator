# Name: Pineda, Patricia Anne E.
# Section: BSCPE 1-5
# Assigment 5: Simple App Calculator

# while loop: 
simple_calculator = ""
while simple_calculator != "NO":

    # ask user for input: math operations
    operation = input("\n\033[01mHi! Pleases choose among the four math operations:\n\nAddition\nSubtraction\nMultiplication\nDivision\n\nEnter your answer: ")
   
    # ask user for input: float
    print ("\n\nGreat! Please enter two numbers of your choice!")
    num1 = input ("Enter your first number: ")
    num2 = input ("\nEnter your second number: ")

    # addition
    if operation.upper() == "ADDITION":
        print("\nWe'll be performing addition on", num1, "and", num2)
        addition = (float(num1) + float(num2))
        print (addition)
    # subtraction
    if operation.upper() == "SUBTRACTION":
        print("\nWe'll be performing subtraction on", num1, "and", num2)
        subtraction = (float(num1) - float(num2))
        print (subtraction)
    # multiplication
    if operation.upper() == "MULTIPLICATION":
        print("\nWe'll be performing multiplication on", num1, "and", num2)
        multiplication = (float(num1) * float(num2))
        print (multiplication)
    # division
    if operation.upper() == "DIVISION":
        print("\nWe'll be performing division on", num1, "and", num2)
        division = (float(num1) / float(num2))
        print (division)

    # looping: ask user to try again
    simple_calculator = input("Do you want to try again? ")
    
    # if yes
    if simple_calculator.upper() == "YES":
        print("STARTING.....")

    # if no
    else: 
        simple_calculator.upper() == "NO"
        print("THANK YOU!")
        break