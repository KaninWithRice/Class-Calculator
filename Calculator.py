# Mohammad Mishal S. Noroña | BSCPE 1-5 | Assignment #7
def start():
    # Import Classes
    from Class_Calc import Calculator
    from Class_User_Input import UserInput
    
    calc = Calculator()
    ui = UserInput()
    # Ask for user's Number Input 
    num1 = ui.num_input()
    num2 = ui.num_input()
    # Ask for Operation Input
    operation = ui.operation_input()
    # Add Time Delay
    import time
    if operation == "a":
        print("\nCalculating Please wait......\n")
        time.sleep(1.0)
        print(num1, "+", num2, "\nAnswer =", calc.addition(num1, num2))
        # If user enters "a" Print output of addition
    elif operation == "s":
        print("\nCalculating Please wait......\n")
        time.sleep(1.0)
        print(num1, "-", num2, "\nAnswer =", calc.subtraction(num1, num2))
        # If user enters "s" Print output of subtraction
    elif operation == "m":
        print("\nCalculating Please wait......\n")
        time.sleep(1.0)
        print(num1, "*", num2, "\nAnswer =", calc.multiplication(num1, num2))
        # If user enters "m" Print output of multiplication
    elif operation == "d":
        print("\nCalculating Please wait......\n")
        time.sleep(1.0)
        print(num1, "/", num2, "\nAnswer =", calc.division(num1, num2))
        # If user enters "d" Print output of division

    # Ask for another Input
    more_input = ui.try_again()
    if more_input == "y":  
        start()
    elif more_input == "n":
        print("Thank you for using Simple Calculator")
    else:
        print("\nInvalid Input")
        exit()
start()

