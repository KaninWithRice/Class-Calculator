# Mohammad Mishal S. Noroña | BSCPE 1-5 | Assignment #7
# Create a Class Calculator
class Calculator:
# Addition
    def addition(self, num1, num2):
        add = num1 + num2
        return add
# Subtraction
    def subtraction(self, num1, num2):
        sub = num1 - num2
        return sub
# Multiplication
    def multiplication(self, num1, num2):
        mul = num1 * num2
        return mul
# Division
    def division(self, num1, num2):
        try:
            div = num1 / num2
        except ZeroDivisionError:
            print("\nDivision by Zero Error")
        return div
