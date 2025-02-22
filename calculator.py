##-----Calculator App------ using python 
## create 4 differentfunctions to perform airthematic operation


def add(a, b):
        pass  # To be implemented by Developer 1

def subtract(a, b):
        pass  # To be implemented by Developer 2
                                        
def multiply(a,b):
        pass  # To be implemented by Developer 3

def divide(a,b):
        pass  # To be implemented by Developer 4


def calculator():
    print("\n------Calculator App------")
    

choice = input("Enter your choice: ")


if choice not in ('1', '2', '3', '4', '5'):
    print("Opps! Invalid choice! Please enter number between 1 - 5...!")
    

if choice == '5':
    print("Exiting the Calculator. Goodbye! See you next time!")
   

try:
    num1 = float(input("Enter your 1st number: "))
    num2 = float(input("Enter your 2nd number: "))


except ValueError:
    print("Invalid inputs! please enter numeric values.")
    

if ___name__ == "__main__":
    calculator()

