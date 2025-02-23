##-----Calculator App------ using python 
## create 4 differentfunctions to perform airthematic operation


def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
                                        
def multiply(a,b):
    return a * b

def divide(a,b):
    pass  # to be implemented by Developer 4

def calculator():
    print("\n------Calculator App------\n")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    
        
    while True:
        choice = input("Enter your choice (1-5): ")

        if choice == '5':
            print("Exiting the Calculator. GoodBye! See you Again")
            break  # exit the loop      
       
        if choice not in ('1', '2', '3', '4'):
            print("Opps! Invalid choice! Please enter number between 1 - 5...!")
            continue  # Ask for the input again

        try:
            num1 = float(input("Enter your 1st number: "))
            num2 = float(input("Enter your 2nd number: "))
        except ValueError:
            print("Invalid inputs! please enter numeric values.")
            continue  # ask for input again

        if choice == '1':
            print("Result : ", add(num1, num2))
        elif choice == '2':
            print("Result : ", subtract(num1, num2))
        elif choice == '3':
            print("Result : ", multiply(num1, num2))
            

if __name__ == "__main__":
    calculator()                                                                                                                                                                                                                           
