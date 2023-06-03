# Mohammad Mishal S. Noroña | BSCPE 1-5 | Assignment #8
# Import Class_Calc.py
from Class_Calc import Calculator
# Create a Class Inheritance
class calc_inh(Calculator):
    # Percent Function
    def percent(self, num1, num2):
        avg = num1 * num2 / 100
        return avg
    # Exponent Function
    def exponent(self, num1, num2):
        exp = num1 ** num2
        return exp