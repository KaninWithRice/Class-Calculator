from Class_Calc import Calculator
from Class_User_Input import UserInput

calc = Calculator()
ui = UserInput()

num1 = ui.num_input()
num2 = ui.num_input()

operation = ui.operation_input()
if operation == "a":
    print(num1, "+", num2, "=", calc.addition(num1, num2))

elif operation == "s":
    print(num1, "-", num2, "=", calc.subtraction(num1, num2))

elif operation == "m":
    print(num1, "*", num2, "=", calc.multiplication(num1, num2))

elif operation == "d":
    print(num1, "/", num2, "=", calc.division(num1, num2))
