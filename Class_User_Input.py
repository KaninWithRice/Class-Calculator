# Mohammad Mishal S. Noroña | BSCPE 1-5 | Assignment #7
# Creata a Class for USer's Input
class UserInput:
    # Number Input Function
    def num_input(self):
        num = float(input("Enter a number:"))
        return num
    # Operation Input Function
    def operation_input(self):
        print("\nList Of Operation \n")
        print("[a] Add")
        print("[s] Subtract")
        print("[m] Multiply")
        print("[d] Divide")

        operation = input("Enter an Operation [a/s/m/d]: ")
        return operation
    # Ask user for another input
    def try_again(self):
        more_input = input("Do you want to Enter another? (y/n): ")
        return more_input