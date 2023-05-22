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
# Math Operation
    def operation(self, operation):
        while operation != 0:
            if self.operation == "a":
                print(self.num1, "+", self.num2, "=", self.addition())

            elif self.operation == "s":
                print(self.num1, "-", self.num2, "=", self.subtraction())

            elif self.operation == "m":
                print(self.num1, "*", self.num2, "=", self.multiplication())

            elif self.operation == "d":
                print(self.num1, "/", self.num2, "=", self.division())
            else:
                return operation
            