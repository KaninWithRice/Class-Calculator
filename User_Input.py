class UserInput:
    def num1_input(self):
        num1 = float(input("Enter the first number:"))
        return num1
    def num2_input(self):
        num2 = float(input("Enter the second number:"))
        return num2
    def operation_input(self):
        print("\nList Of Operation \n")
        print("[a] Add")
        print("[s] Subtract")
        print("[m] Multiply")
        print("[d] Divide")
        
        operation = input("Enter an Operation [a/s/m/d]: ")
        return operation