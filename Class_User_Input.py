class UserInput:
    def num_input(self):
        num = float(input("Enter a number:"))
        return num
    def operation_input(self):
        print("\nList Of Operation \n")
        print("[a] Add")
        print("[s] Subtract")
        print("[m] Multiply")
        print("[d] Divide")

        operation = input("Enter an Operation [a/s/m/d]: ")
        return operation
    
    def try_again(self):
        more_input = input("Do you want to Enter another? (y/n): ")
        return more_input