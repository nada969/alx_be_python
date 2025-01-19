def safe_divide(numerator, denominator):
    try:
        result = numerator / denominator
        return (f"The result of the division is {result}")

    except ValueError as e:
        return ("Error: Please enter numeric values only.")
    
    except ZeroDivisionError as e:
        return ("Error: Cannot divide by zero.")
    
print(safe_divide(1,2))