num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
operations = input("Choose the operation (+, -, *, /):")

match operations:
    case "+":
        print("The result is ",num1 + num2)
    case "-":
        print("The result is ",num1 - num2)
    case "*":
        print("The result is ",num1 * num2)
    case "/":
        if num2 != 0:
            print("The result is ",num1 / num2)
        else:
            print("Cannot divide by zero.")