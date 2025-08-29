# def functions
def addition(num1,num2):
    return num1+num2
def subtraction(num1,num2):
    return num1-num2
def multiplication(num1,num2):
    return num1*num2
def division(num1,num2):
    if num2==0:
        print("Invalid: Division by zero")
        return None
    return num1/num2

while True:
    print("\nChoose operation: ")
    print("1. Addition, 2. Subtraction, 3. Multiplication, 4. Division, 5. Exit")
    choice = input("Enter choice (1/2/3/4/5): ")

    if choice=='5':
        print("Exiting..")
        break

    if choice in ['1','2','3','4']:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))

    if choice == '1':
        print("Result:", addition(a,b))
    elif choice == '2':
        print("Result:", subtraction(a,b))
    elif choice == '3':
        print("Result:", multiplication(a,b))
    elif choice == '4':
        result= division(a,b)
        if result is not None:
            print("Result:",result)
    else:
        print("Invalid choice. Try again.")