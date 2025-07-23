num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Choose the operation (+,-,*,/): ")

match operation:
    case "+":
        result = num1 + num2
    case "-":
        result = num1 - num2
    case "*":
        result = num1 * num2
    case "/":
        result = "Error: Division by zero" if num2 == 0 else num1 / num2
    case _:
        result = "Invalid operation"

print(f"The result is {result}")
