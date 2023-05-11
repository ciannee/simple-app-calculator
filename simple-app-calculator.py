# Name: Pineda, Patricia Anne E.
# Section: BSCPE 1-5
# Assigment 5: Simple App Calculator

import time
# while loop: 
simple_calculator = ""
while simple_calculator != "NO":

    # ask user's name
    name = input("\n\033[01mPlease enter your name: ")
    time.sleep(3)

    print("Hi,", name, "I have prepared a simple calculator for you!")
   
    # ask user for input: math operations
    operation = input("\n\033[01m\nPlease choose among the four math operations:\n\nAddition\nSubtraction\nMultiplication\nDivision\n\nEnter your answer: ")
    time.sleep(2)

    # ask user for input: float
    print ("\n\nGreat! Please enter two numbers of your choice!")
    num1 = input ("Enter your first number: ")
    num2 = input ("\nEnter your second number: ")

    # addition
    if operation.upper() == "ADDITION":
        try:
            print("\nWe'll be performing addition on", num1, "and", num2)
        except:
            print("oh no, may mali!")
        finally:
            addition = (float(num1) + float(num2))
            print("\n\033[36mSTARTING..........")
            time.sleep(3)
            print("\n  █▒▒▒▒▒▒▒▒▒")
            time.sleep(1)
            print("\n  ███▒▒▒▒▒▒▒")
            time.sleep(1)
            print("\n  █████▒▒▒▒▒")
            time.sleep(1)
            print("\n  ███████▒▒▒")
            time.sleep(1)
            print("\n  ██████████")
            time.sleep(3)
            print ("\nResult = ", addition)
    # subtraction
    if operation.upper() == "SUBTRACTION":
        print("\nWe'll be performing subtraction on", num1, "and", num2)
        subtraction = (float(num1) - float(num2))
        print("\n\033[36mSTARTING..........")
        time.sleep(3)
        print("\n  █▒▒▒▒▒▒▒▒▒")
        time.sleep(1)
        print("\n  ███▒▒▒▒▒▒▒")
        time.sleep(1)
        print("\n  █████▒▒▒▒▒")
        time.sleep(1)
        print("\n  ███████▒▒▒")
        time.sleep(1)
        print("\n  ██████████")
        time.sleep(3)
        print ("\nResult = ", subtraction)
    # multiplication
    if operation.upper() == "MULTIPLICATION":
        try:
            print("\nWe'll be performing multiplication on", num1, "and", num2)
        except:
            print("hala may mali!")
        finally:
            multiplication = (float(num1) * float(num2))
            print("\n\033[36mSTARTING..........")
            time.sleep(3)
            print("\n  █▒▒▒▒▒▒▒▒▒")
            time.sleep(1)
            print("\n  ███▒▒▒▒▒▒▒")
            time.sleep(1)
            print("\n  █████▒▒▒▒▒")
            time.sleep(1)
            print("\n  ███████▒▒▒")
            time.sleep(1)
            print("\n  ██████████")
            time.sleep(3)
            print ("\nResult = ", multiplication)
    # division
    if operation.upper() == "DIVISION":
        print("\nWe'll be performing division on", num1, "and", num2)
        print("\n\033[36mSTARTING..........")
        time.sleep(3)
        print("\n  █▒▒▒▒▒▒▒▒▒")
        time.sleep(1)
        print("\n  ███▒▒▒▒▒▒▒")
        time.sleep(1)
        print("\n  █████▒▒▒▒▒")
        time.sleep(1)
        print("\n  ███████▒▒▒")
        time.sleep(1)
        print("\n  ██████████")
        time.sleep(3)
        try:
            division = (float(num1) / float(num2))
        except ZeroDivisionError:
            division = 0
        print("\nResult = ", division)

    # looping: ask user to try again
    simple_calculator = input("\nDo you want to try again? ")
    
    # if yes
    if simple_calculator.upper() == "YES":
        print("STARTING.....")

    # if no
    else: 
        simple_calculator.upper() == "NO"
        print("THANK YOU!")
        break