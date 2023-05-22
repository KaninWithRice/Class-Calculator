class UserInput:
    def num1_input(self):
        num = float(input("Enter the first number:"))
        return num
    def operation_input(self):
        print("\nList Of Operation \n")
        print("[a] Add")
        print("[s] Subtract")
        print("[m] Multiply")
        print("[d] Divide")

        self.operation = input("Enter an Operation [a/s/m/d]: ")
        return self.operation