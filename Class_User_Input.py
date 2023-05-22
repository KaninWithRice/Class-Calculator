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
        while True:
            more_input = input("Do you want to Enter another? (y/n): ")
            if more_input == "y":  
                continue
            elif more_input == "n":
                print("Thank you for using Simple Calculator")
                break
            else:
                print("\nInvalid Input")
                break