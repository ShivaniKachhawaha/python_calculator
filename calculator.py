"""
Simple CLI Calculator
This script provides basic arithmetic operations including addition, subtraction,
multiplication, and division. The user can select an operation and input two numbers.
"""

def add(x, y):
    """Returns the sum of x and y."""
    return x + y

def subtract(x, y):
    """Returns the difference of x and y."""
    return x - y

def multiply(x, y):
    """Returns the product of x and y."""
    return x * y

def divide(x, y):
    """Returns the quotient of x and y, handling division by zero."""
    if y == 0:
        return "Error! Division by zero."
    return x / y

def calculator():
    """Runs the CLI calculator allowing users to select operations until they choose to exit."""
    while True:
        print("\nSimple CLI Calculator")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Enter choice (1-5): ")

        if choice == '5':
            print("Exiting calculator. Goodbye!")
            break

        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input! Please enter numbers only.")
                continue

            if choice == '1':
                print(f"Result: {add(num1, num2)}")
            elif choice == '2':
                print(f"Result: {subtract(num1, num2)}")
            elif choice == '3':
                print(f"Result: {multiply(num1, num2)}")
            elif choice == '4':
                print(f"Result: {divide(num1, num2)}")
        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    calculator()
