def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    if y!= 0:
        return x/y
    else:
        return "Cannot divide any number by zero"

def modulus(x,y):
    if y!=0:
        return x%y
    else:
        return "Cannot calculate modulus. The divisor (y) cannot be zero."


while True:
    print("\nLet's Calculate!")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulus")
    print("6. Exit")

    choice = input("Enter your choice (1/2/3/4/5/6): ")

    if choice in ('1', '2', '3', '4','5','6'):
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
            continue

        if choice == '1':
            result = add(num1, num2)
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            print(f"{num1} / {num2} = {divide(num1, num2)}")
        elif choice=='5':
            print(f"{num1} % {num2} = {modulus(num1, num2)}") 
        elif choice == '6':
            print("Exiting the calculator!")
            break
    else:
        print("Invalid choice. Please enter a valid choice.")
