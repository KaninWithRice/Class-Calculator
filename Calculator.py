# Mohammad Mishal S. Noroña | BSCPE 1-5 | Assignment #7
# Import Colorama
import colorama
from colorama import Fore, Back, Style
colorama.init()
# Add Time Delay
import time
# Import Classes
from Class_Calc import Calculator
from Class_User_Input import UserInput
from Calculator_Inh import calc_inh
def start():    
    calc = Calculator()
    ui = UserInput()
    inh = calc_inh()
    # Introduction
    print("")
    print(Fore.CYAN + "WELCOME TO SIMPLE CALCULATOR".center(40," ") )
    print(Fore.YELLOW + "By: Mishal Noroña".center(40," ") + Fore.WHITE )
    print(Fore.YELLOW + "\n Note: Calculating Percent \n Number1: (Value) \n Number2: (Percent) \n".center(40," ") + Fore.WHITE )
    # Ask for user's Number Input 
    num1 = ui.num_input()
    num2 = ui.num_input()
    # Ask for Operation Input
    operation = ui.operation_input()
    if operation == "a":
        print(Fore.LIGHTBLUE_EX + "\nCalculating Please wait......\n" + Fore.YELLOW)
        time.sleep(1.0)
        print(num1, "+", num2, Fore.LIGHTGREEN_EX + "\nAnswer =", calc.addition(num1, num2))
        # If user enters "a" Print output of addition
    elif operation == "s":
        print(Fore.LIGHTBLUE_EX + "\nCalculating Please wait......\n" + Fore.YELLOW)
        time.sleep(1.0)
        print(num1, "-", num2, Fore.LIGHTGREEN_EX + "\nAnswer =", calc.subtraction(num1, num2))
        # If user enters "s" Print output of subtraction
    elif operation == "m":
        print(Fore.LIGHTBLUE_EX + "\nCalculating Please wait......\n" + Fore.YELLOW)
        time.sleep(1.0)
        print(num1, "*", num2, Fore.LIGHTGREEN_EX + "\nAnswer =", calc.multiplication(num1, num2))
        # If user enters "m" Print output of multiplication
    elif operation == "d":
        print(Fore.LIGHTBLUE_EX + "\nCalculating Please wait......\n" + Fore.YELLOW)
        time.sleep(1.0)
        print(num1, "/", num2, Fore.LIGHTGREEN_EX + "\nAnswer =", calc.division(num1, num2))
        # If user enters "d" Print output of division
    elif operation == "p":
        print(Fore.LIGHTBLUE_EX + "\nCalculating Please wait......\n" + Fore.YELLOW)
        time.sleep(1.0)
        print(num2, "%" + " of", num1, Fore.LIGHTGREEN_EX + "\nAnswer =", inh.percent(num1, num2))
        # If user enters "p" Print output of percent
    elif operation == "e":
        print(Fore.LIGHTBLUE_EX + "\nCalculating Please wait......\n" + Fore.YELLOW)
        time.sleep(1.0)
        print(num1, "^", num2, Fore.LIGHTGREEN_EX + "\nAnswer =", inh.exponent(num1, num2))
        # If user enters "e" Print output of exponent
        #     
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

