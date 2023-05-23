# Mohammad Mishal S. Noroña | BSCPE 1-5 | Assignment #7
# Creata a Class for USer's Input
class UserInput:
    # Number Input Function
    def num_input(self):
        while True:
            try:
                num = float(input("Enter a number:"))
                return num
            except ValueError:
                print("\nInvalid Input")
                print("Enter a Numerical Value\n")
                continue
    # Operation Input Function
    def operation_input(self):
        print("\nList Of Operation \n")
        print("[a] Add")
        print("[s] Subtract")
        print("[m] Multiply")
        print("[d] Divide")

        operation = input("\nEnter an Operation [a/s/m/d]: ")
        return operation
    # Ask user for another input
    def try_again(self):
        more_input = input("\nDo you want to Enter another? (y/n): ")
        return more_input