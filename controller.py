from model import *
from view import *
def calculator():
    print("Welcome to the simple calculator!")
    operation = input("Enter operation (add, subtract, multiply, divide): ")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    result = calculate(operation, a, b)
    display_result(result)


# Запуск калькулятора
if __name__ == "__main__":
    calculator()
