# Mohammad Mishal S. Noroña | BSCPE 1-5 | Assignment #7
# Create a Class Calculator
class Calculator:
# Addition Function
    def addition(self, num1, num2):
        add = num1 + num2
        return add
# Subtraction Function
    def subtraction(self, num1, num2):
        sub = num1 - num2
        return sub
# Multiplication Function
    def multiplication(self, num1, num2):
        mul = num1 * num2
        return mul
# Division Function
    def division(self, num1, num2):
        while True:
            try:
                div = num1 / num2
                return div
            except ZeroDivisionError:
                print("\nDivision by Zero Error")
                print("You can't divide numbers to zero\n")
                break
                
