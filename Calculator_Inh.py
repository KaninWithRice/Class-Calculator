# Mohammad Mishal S. Noroña | BSCPE 1-5 | Assignment #8
from Class_Calc import Calculator

class calc_inh(Calculator):
    def percent(self, num1, num2):
        avg = num1 * num2 / 100
        return avg
    
    def exponent(self, num1, num2):
        exp = num1 ** num2
        return exp